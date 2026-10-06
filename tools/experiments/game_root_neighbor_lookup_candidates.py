"""Recover the cached-seed, filtered nearest-node lookup without slot overflow."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions
from tools.experiments.game_record_neighbor_visit_candidates import replace


ENTRY = 0x15085DF8
SYMBOLS = {'D_80087290': 0x80087290, 'D_8008729C': 0x8008729C,
           'D_800D2350': 0x800D2350, 'D_800D2354': 0x800D2354,
           'D_8009D9CC': 0x8009D9CC, 'func_15086D94': 0x15086D94}
DECLARATIONS = '''extern s16 D_80087290;
extern u8 D_8008729C;
extern u8 *D_800D2350;
extern s32 D_800D2354;
extern f32 D_8009D9CC;
f32 func_15086D94(f32, f32, f32, f32, f32);
'''
BASELINE = '''s32 func_15085DF8(f32 x, f32 y, f32 z, s8 mode, s8 band) {
    u8 *node;
    s32 i;
    s32 best;
    s32 check;
    f32 dx;
    f32 dy;
    f32 dz;
    f32 distance;
    f32 minimum;

    check = 0;
    minimum = D_8009D9CC;
    if (mode == 0) {
        check = 1;
    }
    if (D_8008729C != 0xFF) {
        node = D_800D2350 + D_8008729C * 16;
        dx = (f32)*(s16 *)(node + 0) - x;
        dy = (f32)*(s16 *)(node + 2) - y;
        dz = (f32)*(s16 *)(node + 4) - z;
        if (!check || (check && func_15086D94(x, y, z, dx, dz) < 0.0f)) {
            minimum = dx * dx + dy * dy + dz * dz + 10.0f;
        }
        D_8008729C = 0xFF;
    }
    best = 0xFF;
    for (i = 0; i < D_80087290; i++) {
        node = D_800D2350 + i * 16;
        if (node[6] == band || band == -1) {
            if (node[14] == mode || mode == -1) {
                dx = (f32)*(s16 *)(node + 0) - x;
                dy = (f32)*(s16 *)(node + 2) - y;
                dz = (f32)*(s16 *)(node + 4) - z;
                distance = dx * dx + dy * dy + dz * dz;
                if (distance < minimum &&
                    (!check || (check && func_15086D94(x, y, z, dx, dz) < 0.0f))) {
                    minimum = distance;
                    best = i;
                }
            }
        }
    }
    D_800D2354 = (s32)sqrtf(minimum);
    return best;
}'''
PLACEHOLDER = '''s32 func_15085DF8(f32 x, f32 y, f32 z, s32 mode, s32 band) {
    return 0;
}'''


def inline_nodes(body):
    body = replace(body, '    u8 *node;\n', '')
    first, last = body.split('    best = 0xFF;\n', 1)
    first = replace(first, '        node = D_800D2350 + D_8008729C * 16;\n', '')
    first = first.replace('node +', '(D_800D2350 + D_8008729C * 16) +')
    last = replace(last, '        node = D_800D2350 + (i << 4);\n', '')
    last = last.replace('node +', '(D_800D2350 + (i << 4)) +').replace(
        'node[', '(D_800D2350 + (i << 4))[')
    return first + '    best = 0xFF;\n' + last


def candidates():
    forms = [('signed-byte-arguments', BASELINE), ('placeholder', PLACEHOLDER)]
    words = replace(BASELINE, 's8 mode, s8 band', 's32 mode, s32 band')
    words = replace(words, '    check = 0;', '    mode = (s8)mode;\n    band = (s8)band;\n    check = 0;')
    forms.append(('word-arguments-narrowed', words))
    for name, body in (('byte', BASELINE), ('word', words)):
        forms.append((name + '-boolean-check', replace(body,
            '    check = 0;\n    minimum = D_8009D9CC;\n    if (mode == 0) {\n        check = 1;\n    }',
            '    minimum = D_8009D9CC;\n    check = mode == 0;')))
        forms.append((name + '-simple-short-circuit', body.replace(
            '(check && func_15086D94(x, y, z, dx, dz) < 0.0f)',
            'func_15086D94(x, y, z, dx, dz) < 0.0f')))
        forms.append((name + '-nested-check', replace(body,
            '                if (distance < minimum &&\n'
            '                    (!check || (check && func_15086D94(x, y, z, dx, dz) < 0.0f))) {\n'
            '                    minimum = distance;\n                    best = i;\n                }',
            '                if (distance < minimum) {\n'
            '                    if (!check || (check && func_15086D94(x, y, z, dx, dz) < 0.0f)) {\n'
            '                        minimum = distance;\n                        best = i;\n                    }\n'
            '                }')))
        forms.append((name + '-z-reuse', body.replace('    f32 distance;\n', '')
                      .replace('distance', 'dz')))
        forms.append((name + '-unsigned-best', body.replace('    s32 best;', '    u32 best;')))
        forms.append((name + '-unsigned-index-negative-control', body.replace('    s32 i;', '    u32 i;')))
        forms.append((name + '-index-divide', body.replace(
            'node = D_800D2350 + i * 16;', 'node = D_800D2350 + (i / 1) * 16;')))
        forms.append((name + '-increment-divide', body.replace(
            'i < D_80087290; i++', 'i < D_80087290; i = i / 1 + 1')))
        forms.append((name + '-integer-node-address', body.replace(
            'node = D_800D2350 + i * 16;', 'node = (u8 *)((s32)D_800D2350 + i * 16);')))
    divided = dict(forms)['byte-index-divide']
    for kind in ('s8', 'u8', 's16', 'u16'):
        forms.append(('index-divide-' + kind + '-check', divided.replace('    s32 check;', '    ' + kind + ' check;')))
    for name, increment in (('late-divide', 'i = (i + 1) / 1'),
                            ('multiply-one', 'i = (i + 1) * 1'),
                            ('bitwise-full', 'i = (i + 1) & -1'),
                            ('xor-zero', 'i = (i + 1) ^ 0')):
        forms.append(('index-' + name, BASELINE.replace('i < D_80087290; i++',
                                                       'i < D_80087290; ' + increment)))
    for name, expression in (('word-shift', '(i << 4)'),
                             ('unsigned-shift', '((u32)i << 4)'),
                             ('byte-offset-divide', '((i * 16) / 1)'),
                             ('unsigned-multiply', '(i * 16U)')):
        forms.append((name, BASELINE.replace('D_800D2350 + i * 16', 'D_800D2350 + ' + expression)))
    shifted = dict(forms)['word-shift']
    forms.append(('inline-node-addresses', inline_nodes(shifted)))
    forms.append(('inline-node-addresses-boolean-check', inline_nodes(shifted).replace(
        '    check = 0;\n    minimum = D_8009D9CC;\n    if (mode == 0) {\n        check = 1;\n    }',
        '    minimum = D_8009D9CC;\n    check = mode == 0;')))
    return forms


SELECTED = dict(candidates())['inline-node-addresses']


def compile_candidate(root, output, name, body, unroll=False):
    conker = root / 'conker'
    source, obj, elf = [output / (name + suffix) for suffix in ('.c', '.o', '.elf')]
    source.write_text('#include <ultra64.h>\n' + DECLARATIONS + '\n' + body + '\n')
    command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
               '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
               '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', '-woff', '649,838']
    for include in ('.', 'include', 'include/2.0L', 'include/2.0L/PR', 'include/libc'):
        command += ['-I', include]
    command += ['-mips2', '-o32', '-O2', '-g3']
    if not unroll:
        command += ['-Wo,-loopunroll,0']
    command += ['-o', str(obj.relative_to(conker)), str(source.relative_to(conker))]
    result = subprocess.run(command, cwd=conker, capture_output=True, text=True, check=True)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x15085DF8 : SUBALIGN(4) { *(.text) } }\n')
    link = ['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_15085DF8']
    link += ['--defsym=' + symbol + '=' + hex(address) for symbol, address in SYMBOLS.items()]
    subprocess.run(link + ['-o', str(elf), str(obj)], capture_output=True, check=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_15085DF8']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    words = words[:size]
    retail = list(struct.unpack_from('>168I', (conker / 'conker.us.bin').read_bytes(), 0xB32A8))
    slot = words + [0] * max(0, 168 - size)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}')
                   for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    return dict(name=name, body_words=size, frame=(-words[0]) & 65535 if words[0] >> 16 == 0x27BD else 0,
                real_differences=len(differences) + max(0, size - 168), differences=differences,
                diagnostics=result.stdout + result.stderr, unroll=unroll), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-root-neighbor-lookup'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for unroll in (False, True):
            record, _ = compile_candidate(root, output, name + ('-unroll' if unroll else ''), body, unroll)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']),
                  record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
