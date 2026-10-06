"""Screen the retail XOR-swap and saved-pointer shape of the integer pair clamp."""

import argparse
import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


ENTRY, ROM, WORDS = 0x15143D18, 0x1711C8, 36
TYPES = 'typedef int s32; typedef unsigned int u32;\n'
SELECTED = '''void func_15143D18(s32 *arg0, s32 *arg1, s32 arg2, s32 arg3) {
    s32 *ptr1;
    s32 *ptr0;
    s32 value1;
    s32 value0;

    ptr1 = arg1;
    ptr0 = arg0;
    if (arg3 < arg2) {
        s32 tmp;
        s32 newArg3;

        tmp = arg2 ^ arg3;
        newArg3 = arg3 ^ tmp;
        arg3 = newArg3;
        arg2 = tmp ^ newArg3;
    }

    value1 = *ptr1;
    value0 = *ptr0;
    if (value1 < value0) {
        s32 tmp;

        tmp = value0 ^ value1;
        *ptr0 = tmp;
        value1 = *ptr1 ^ tmp;
        *ptr1 = value1;
        value0 = *ptr0 ^ value1;
        *ptr0 = value0;
    }

    if (value0 < arg2) {
        *ptr0 = arg2;
    }
    if (arg3 < *ptr1) {
        *ptr1 = arg3;
    }
}'''
BASELINE = '''void func_15143D18(s32 *arg0, s32 *arg1, s32 arg2, s32 arg3) {
    s32 tmp;

    if (arg3 < arg2) {
        tmp = arg2;
        arg2 = arg3;
        arg3 = tmp;
    }

    if (*arg1 < *arg0) {
        tmp = *arg0;
        *arg0 = *arg1;
        *arg1 = tmp;
    }

    if (*arg0 < arg2) {
        *arg0 = arg2;
    }

    if (arg3 < *arg1) {
        *arg1 = arg3;
    }
}'''
PROFILES = {'o2g3': ['-O2', '-g3'], 'o2': ['-O2'], 'o1g3': ['-O1', '-g3'], 'o1': ['-O1']}


def candidates():
    forms = [('existing-temp-swap', BASELINE), ('xor-cached-values', SELECTED)]
    forms.append(('reverse-pointer-capture', SELECTED.replace('    ptr1 = arg1;\n    ptr0 = arg0;',
                                                             '    ptr0 = arg0;\n    ptr1 = arg1;')))
    forms.append(('reverse-value-read', SELECTED.replace('    value1 = *ptr1;\n    value0 = *ptr0;',
                                                        '    value0 = *ptr0;\n    value1 = *ptr1;')))
    forms.append(('simple-xor-bounds', SELECTED.replace('''        s32 tmp;
        s32 newArg3;

        tmp = arg2 ^ arg3;
        newArg3 = arg3 ^ tmp;
        arg3 = newArg3;
        arg2 = tmp ^ newArg3;''', '''        arg2 ^= arg3;
        arg3 ^= arg2;
        arg2 ^= arg3;''')))
    forms.append(('explicit-xor-stores', SELECTED.replace('''        s32 tmp;

        tmp = value0 ^ value1;
        *ptr0 = tmp;
        value1 = *ptr1 ^ tmp;
        *ptr1 = value1;
        value0 = *ptr0 ^ value1;
        *ptr0 = value0;''', '''        *ptr0 ^= *ptr1;
        *ptr1 ^= *ptr0;
        *ptr0 ^= *ptr1;
        value0 = *ptr0;''')))
    for name, pointers, values in (('register-pointers', True, False), ('register-values', False, True),
                                  ('register-all', True, True)):
        body = SELECTED
        if pointers:
            body = body.replace('    s32 *ptr', '    register s32 *ptr')
        if values:
            body = body.replace('    s32 value', '    register s32 value')
        forms.append((name, body))
    for name, parameters in (('volatile-first-pointer', ('arg0',)), ('volatile-second-pointer', ('arg1',)),
                             ('volatile-both-pointers', ('arg0', 'arg1'))):
        body = SELECTED
        for parameter in parameters:
            body = body.replace('s32 *' + parameter, 's32 *volatile ' + parameter, 1)
        forms.append((name, body))
    forms.append(('reload-lower', SELECTED.replace('    if (value0 < arg2)', '    if (*ptr0 < arg2)')))
    for name, base in (('full-register-hints', SELECTED),
                       ('full-register-simple-bounds', dict(forms)['simple-xor-bounds']),
                       ('full-register-explicit-stores', dict(forms)['explicit-xor-stores'])):
        body = base.replace('s32 *arg0, s32 *arg1, s32 arg2, s32 arg3',
                            'register s32 *arg0, register s32 *arg1, register s32 arg2, register s32 arg3')
        body = body.replace('    s32 ', '    register s32 ')
        forms.append((name, body))
    for name, order in (('value-first-declarations', (2, 3, 0, 1)),
                        ('lower-first-declarations', (1, 0, 3, 2)),
                        ('interleaved-declarations', (0, 2, 1, 3))):
        declarations = ['    s32 *ptr1;', '    s32 *ptr0;', '    s32 value1;', '    s32 value0;']
        forms.append((name, SELECTED.replace('\n'.join(declarations), '\n'.join(declarations[i] for i in order))))
    forms.append(('volatile-first-pointee', SELECTED.replace('s32 *ptr0;', 'volatile s32 *ptr0;')))
    forms.append(('volatile-second-pointee', SELECTED.replace('s32 *ptr1;', 'volatile s32 *ptr1;')))
    forms.append(('volatile-both-pointees', SELECTED.replace('s32 *ptr', 'volatile s32 *ptr')))
    forms.append(('shared-xor-temporary', SELECTED.replace('    s32 value0;', '    s32 value0;\n    s32 tmp;')
                  .replace('        s32 tmp;\n', '')))
    return forms


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text(TYPES + body + '\n')
    command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
               '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
               '-mips2', '-o32', *PROFILES[profile], '-o', str(obj.relative_to(root)), str(source.relative_to(root))]
    compiled = subprocess.run(command, cwd=root, capture_output=True, text=True)
    diagnostics = compiled.stdout + compiled.stderr
    if compiled.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'pair.ld'
    script.write_text('SECTIONS { .text 0x15143D18 : SUBALIGN(4) { *(.text) } }\n')
    linked = subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
                             '-e', 'func_15143D18', '-o', str(elf), str(obj)], capture_output=True, text=True)
    if linked.returncode:
        raise ValueError(linked.stdout + linked.stderr)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_15143D18']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    if any(words[end:]):
        raise ValueError('nonzero tail after return')
    words = words[:end]
    retail = list(struct.unpack_from('>36I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    slot = words + [0] * max(0, WORDS - end)
    differences = [(i * 4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-(word & 65535)) & 65535 for word in words
              if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=max(frames, default=0),
                differences=len(differences) + max(0, end - WORDS), different_words=differences,
                exact=words == retail, diagnostics=diagnostics), words


def register_lifetimes():
    forms = []
    parameters = ('s32 *arg0', 's32 *arg1', 's32 arg2', 's32 arg3')
    for mask in range(16):
        for locals_mask in range(4):
            body = SELECTED
            for index, parameter in enumerate(parameters):
                if mask & 1 << index:
                    body = body.replace(parameter, 'register ' + parameter, 1)
            if locals_mask & 1:
                body = body.replace('    s32 *ptr', '    register s32 *ptr')
            if locals_mask & 2:
                body = body.replace('    s32 value', '    register s32 value')
            forms.append(('register-parameters-%02x-locals-%x' % (mask, locals_mask), body))
    return forms


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--register-lifetimes', action='store_true',
                        help='screen separate parameter/local hints under O2/g3 and O1/g3')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    suffix = '-register-lifetimes' if args.register_lifetimes else ''
    output = root / ('conker/build/game-integer-pair-clamp' + suffix)
    output.mkdir(exist_ok=True)
    records = []
    forms = register_lifetimes() if args.register_lifetimes else candidates()
    profiles = ('o2g3', 'o1g3') if args.register_lifetimes else PROFILES
    for name, body in forms:
        for profile in profiles:
            record, _ = compile_candidate(root, output, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
