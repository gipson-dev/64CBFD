"""Measure index canonicalization before IDO's pointer strength reduction."""

import argparse
import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


ENTRY = 0x15040CC8
BASELINE = '''void func_15040CC8(u8 *arg0) {
    s32 i;
    u8 *record;

    /* Retail retains this short empty delay before dispatching the records. */
    for (i = 0; i < 16; i++) {
    }

    for (i = -20; i < 10; i++) {
        record = arg0 + i * 8;
        D_800844B0[record[0]]((s32)record);
    }
    if (D_800848B0 != 0) {
        func_1500390C(D_800848B0);
    }
}'''


def replace(body, before, after):
    if body.count(before) != 1:
        raise ValueError('record-dispatch anchor no longer binds: ' + before)
    return body.replace(before, after, 1)


def candidates():
    expressions = (
        ('baseline', 'arg0 + i * 8'),
        ('aligned-offset', 'arg0 + (i * 8 & -8)'),
        ('unsigned-aligned-offset', 'arg0 + (s32)((u32)i * 8 & 0xFFFFFFF8U)'),
        ('split-offset', 'arg0 + i * 4 + i * 4'),
        ('split-offset-2-6', 'arg0 + i * 2 + i * 6'),
        ('split-offset-1-7', 'arg0 + i + i * 7'),
        ('integer-split-subtract', '(u8 *)((u32)arg0 + (u32)i * 16 - (u32)i * 8)'),
        ('unsigned-shift', 'arg0 + (s32)((u32)i << 3)'),
        ('signed-half-index', 'arg0 + (s16)i * 8'),
        ('signed-byte-index', 'arg0 + (s8)i * 8'),
        ('signed-half-offset', 'arg0 + (s16)(i * 8)'),
        ('offset-with-high-mask', 'arg0 + (s32)((u32)(i * 8) & 0xFFFFFFFFU)'),
        ('integer-aligned-offset', '(u8 *)((u32)arg0 + ((u32)i * 8 & 0xFFFFFFF8U))'),
        ('integer-split-offset', '(u8 *)((u32)arg0 + (u32)i * 4 + (u32)i * 4)'),
        ('complement-index', 'arg0 - (~i + 1) * 8'),
        ('complement-offset', 'arg0 - ~(i * 8) - 1'),
        ('integer-xor-offset', '(u8 *)((u32)arg0 + (((u32)i * 8) ^ 0x80000000U) - 0x80000000U)'),
    )
    forms = [(name, replace(BASELINE, 'arg0 + i * 8', expression)) for name, expression in expressions]
    for name, update in (('word-modular-increment', 'i = (s32)((u32)i + 1)'),
                         ('halfword-increment', 'i = (s16)(i + 1)'),
                         ('byte-increment', 'i = (s8)(i + 1)')):
        forms.append((name, replace(BASELINE, 'i = -20; i < 10; i++', 'i = -20; i < 10; ' + update)))
    for name, header in (
            ('preincrement-header', 'i = -21; ++i < 10;'),
            ('postincrement-header', 'i = -21; i++ < 9;'),
            ('halfword-condition', 'i = -20; (s16)i < 10; i++'),
            ('byte-condition', 'i = -20; (s8)i < 10; i++'),
            ('unsigned-biased-condition', 'i = -20; (u32)(i + 20) < 30; i++'),
            ('two-sided-condition', 'i = -20; i < 10 && i >= -20; i++'),
            ('division-index', 'i = -20; i < 10; i++')):
        body = replace(BASELINE, 'i = -20; i < 10; i++', header)
        if name == 'division-index':
            body = replace(body, 'arg0 + i * 8', 'arg0 + (i * 8 / 8) * 8')
        forms.append((name, body))
    for kind in ('s16', 's8'):
        forms.append((kind + '-local', replace(BASELINE, '    s32 i;', '    ' + kind + ' i;')))
    for name, update in (
            ('negated-complement-increment', 'i = -~i'),
            ('complement-subtract-increment', 'i = (s32)~((u32)~i - 1U)'),
            ('complement-negated-increment', 'i = ~(-i - 2)'),
            ('narrow-before-increment', 'i = (s16)i + 1'),
            ('split-increment', 'i = i + 2 - 1'),
            ('division-increment', 'i = (i + 1) / 1'),
            ('double-negated-increment', 'i = -(-i - 1)')):
        forms.append((name, replace(BASELINE, 'i = -20; i < 10; i++', 'i = -20; i < 10; ' + update)))
    for name, body in (
            ('address-increment-before-call', replace(replace(BASELINE, 'i = -20; i < 10; i++',
                   'i = -20; i < 10;'), 'record = arg0 + i * 8;', 'record = arg0 + i++ * 8;')),
            ('address-preincrement-before-call', replace(replace(BASELINE, 'i = -20; i < 10; i++',
                   'i = -21; i < 9;'), 'record = arg0 + i * 8;', 'record = arg0 + ++i * 8;')),
            ('postincrement-separate-argument', replace(replace(BASELINE, 'i = -20; i < 10; i++',
                   'i = -20; i < 10;'), 'D_800844B0[record[0]]((s32)record);',
                   'D_800844B0[record[0]]((s32)(arg0 + i++ * 8));'))):
        forms.append((name, body))
    division = dict(forms)['division-increment']
    inline = replace(replace(division, '    u8 *record;\n', ''),
                     '        record = arg0 + i * 8;\n        D_800844B0[record[0]]((s32)record);',
                     '        D_800844B0[(arg0 + i * 8)[0]]((s32)(arg0 + i * 8));')
    forms.append(('division-inline-address', inline))
    forms.append(('division-unused-record-local', replace(inline, '    s32 i;', '    s32 i;\n    u8 *record;')))
    # The assignment/read across separate arguments is deliberately not a semantic candidate.
    forms.append(('division-unsequenced-negative-control', replace(division,
                 '        record = arg0 + i * 8;\n        D_800844B0[record[0]]((s32)record);',
                 '        D_800844B0[(record = arg0 + i * 8)[0]]((s32)record);')))
    forms.append(('division-explicit-dereference', replace(inline, '(arg0 + i * 8)[0]', '*(arg0 + i * 8)')))
    forms.append(('division-integer-record', replace(replace(division, '    u8 *record;', '    s32 record;'),
                 'record = arg0 + i * 8;', 'record = (s32)(arg0 + i * 8);')
                 .replace('record[0]', '*(u8 *)record')))
    forms.append(('integer-record-only', replace(replace(BASELINE, '    u8 *record;', '    s32 record;'),
                 'record = arg0 + i * 8;', 'record = (s32)(arg0 + i * 8);')
                 .replace('record[0]', '*(u8 *)record')))
    return forms


SELECTED = dict(candidates())['division-integer-record']


def compile_candidate(root, output, name, body):
    conker = root / 'conker'
    source, obj, elf = [output / (name + suffix) for suffix in ('.c', '.o', '.elf')]
    source.write_text('#include <ultra64.h>\nextern void (*D_800844B0[])(s32);\n'
                      'extern s32 D_800848B0;\ns32 func_1500390C(s32);\n\n' + body + '\n')
    command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
               '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
               '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', '-woff', '649,838']
    for include in ('.', 'include', 'include/2.0L', 'include/2.0L/PR', 'include/libc'):
        command += ['-I', include]
    command += ['-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)), str(source.relative_to(conker))]
    result = subprocess.run(command, cwd=conker, capture_output=True, text=True, check=True)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x15040CC8 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_15040CC8',
                    '--defsym=D_800844B0=0x800844B0', '--defsym=D_800848B0=0x800848B0',
                    '--defsym=func_1500390C=0x1500390C', '-o', str(elf), str(obj)], capture_output=True, check=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_15040CC8']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    words = words[:size]
    retail = list(struct.unpack_from('>38I', (conker / 'conker.us.bin').read_bytes(), 0x6E178))
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(words, retail)) if a != b]
    saves = [word >> 16 & 31 for word in words if word >> 26 == 43 and word >> 21 & 31 == 29
             and 16 <= word >> 16 & 31 <= 23]
    return dict(name=name, body_words=size, frame=(-words[0]) & 65535, saved=saves,
                real_differences=len(differences) + abs(size - 38), differences=differences,
                diagnostics=result.stdout + result.stderr), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--names', nargs='*')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-record-dispatch-induction'
    output.mkdir(exist_ok=True)
    forms = candidates()
    if args.names:
        wanted = set(args.names)
        if not wanted <= dict(forms).keys():
            parser.error('unknown candidate')
        forms = [(n, b) for n, b in forms if n in wanted]
    records = []
    for name, body in forms:
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], record['frame'], record['saved'], record['real_differences'], flush=True)
    (output / ('selected-screen.json' if args.names else 'screen.json')).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
