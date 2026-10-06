"""Recover horizontal graph-edge crossings and retail's last-fraction result."""

import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions
from tools.experiments.game_record_neighbor_visit_candidates import replace


ENTRY = 0x15086D94
SYMBOLS = {'D_80087290': 0x80087290, 'D_800D2350': 0x800D2350,
           'func_15085DA8': 0x15085DA8}
DECLARATIONS = '''extern s16 D_80087290;
extern u8 *D_800D2350;
s32 func_15085DA8(f32);
'''
BASELINE = '''f32 func_15086D94(f32 x, f32 y, f32 z, f32 dx, f32 dz) {
    s32 band;
    s32 count;
    s32 i;
    s32 j;
    s32 id;
    u8 *nodes;
    u8 *first;
    u8 *second;
    f32 minimum;
    f32 fraction;
    f32 ax;
    f32 az;
    f32 nx;
    f32 nz;
    f32 constant;
    f32 start;
    f32 end;
    f32 a;
    f32 b;
    f32 swap;

    band = func_15085DA8(y);
    count = D_80087290;
    minimum = 100.0f;
    if (count > 0) {
        nodes = D_800D2350;
        for (i = 0; i < count; i++) {
            first = nodes + i * 16;
            if (first[14] == 1 && first[6] == band) {
                for (j = 0; j < 5; j++) {
                    id = first[j + 9];
                    if (id != 255 && i < id) {
                        second = nodes + id * 16;
                        if (second[14] == 1) {
                            nx = (f32)(*(s16 *)(second + 4) - *(s16 *)(first + 4));
                            nz = -(f32)(*(s16 *)(second + 0) - *(s16 *)(first + 0));
                            ax = (f32)*(s16 *)(first + 0);
                            az = (f32)*(s16 *)(first + 4);
                            constant = -(ax * nx + nz * az);
                            start = x * nx + z * nz + constant;
                            end = (x + dx) * nx + (z + dz) * nz + constant;
                            a = start;
                            b = end;
                            if ((end < 0.0f && 0.0f <= start) ||
                                (start < 0.0f && 0.0f <= end)) {
                                if (end < 0.0f) {
                                    b = -end;
                                }
                                if (start < 0.0f) {
                                    a = -start;
                                }
                                swap = nx;
                                nx = -nz;
                                nz = swap;
                                fraction = a / (a + b);
                                constant = -(ax * nx + swap * az);
                                start = (x + fraction * dx) * nx +
                                        (z + fraction * dz) * nz + constant;
                                end = (f32)*(s16 *)(second + 0) * nx +
                                      nz * (f32)*(s16 *)(second + 4) + constant;
                                if ((0.0f < end && 0.0f < start && start <= end) ||
                                    (end < 0.0f && start < 0.0f && end <= start)) {
                                    if (fraction < minimum) {
                                        minimum = fraction;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    if (minimum <= 1.0f) {
        /* Retail returns the last crossing fraction, even if that edge was rejected. */
        return sqrtf(dx * dx + dz * dz) * fraction;
    }
    return -1.0f;
}'''


def candidates():
    forms = [('pointer-baseline', BASELINE)]
    forms.append(('explicit-index-shifts', BASELINE.replace('i * 16', '(i << 4)')
                  .replace('id * 16', '(id << 4)')))
    forms.append(('reused-side-values', BASELINE.replace('    f32 a;\n    f32 b;\n', '')
                  .replace('                            a = start;\n                            b = end;\n', '')
                  .replace('b = -end;', 'end = -end;').replace('a = -start;', 'start = -start;')
                  .replace('fraction = a / (a + b);', 'fraction = start / (start + end);')))
    forms.append(('minimum-result-negative-control', BASELINE.replace(
        'sqrtf(dx * dx + dz * dz) * fraction', 'sqrtf(dx * dx + dz * dz) * minimum')))
    for name, body in list(forms[:3]):
        forms.append((name + '-early-count-return', replace(body,
            '    minimum = 100.0f;\n    if (count > 0) {',
            '    if (count <= 0) {\n        return -1.0f;\n    }\n'
            '    minimum = 100.0f;\n    {')))
        forms.append((name + '-byte-band', body.replace('    s32 band;', '    u8 band;')))
        forms.append((name + '-reversed-constant-operands', body.replace(
            'nx + nz * az', 'nx + az * nz').replace('nx + swap * az', 'nx + az * swap')))
    return forms


def lifetime_candidates():
    body = BASELINE.replace('i * 16', '(i << 4)').replace('id * 16', '(id << 4)')
    body = replace(body, '    if (count > 0) {\n        nodes = D_800D2350;\n'
                   '        for (i = 0; i < count; i++) {',
                   '    i = 0;\n    if (count > 0) {\n        nodes = D_800D2350;\n        do {')
    body = replace(body, '        }\n    }\n    if (minimum',
                   '            i++;\n        } while (i < count);\n    }\n    if (minimum')
    forms = [('indexed-do-while', body)]
    forms.append(('indexed-do-while-side-copies', body.replace('                            start = (x + fraction',
                  '                            a = (x + fraction').replace(
                  '                            end = (f32)', '                            b = (f32)').replace(
                  '(0.0f < end && 0.0f < start && start <= end)',
                  '(0.0f < b && 0.0f < a && a <= b)').replace(
                  '(end < 0.0f && start < 0.0f && end <= start)',
                  '(b < 0.0f && a < 0.0f && b <= a)')))
    for name, candidate in list(forms):
        for suffix, before, after in (
                ('fraction-first', '    f32 minimum;\n    f32 fraction;', '    f32 fraction;\n    f32 minimum;'),
                ('z-first', 'x * nx + z * nz', 'z * nz + x * nx'),
                ('copy-tangent', 'constant = -(ax * nx + swap * az);', 'constant = -(ax * nx + nz * az);'),
                ('sentinel-first', 'id != 255', '255 != id')):
            forms.append((name + '-' + suffix, replace(candidate, before, after)))
    return forms


def cursor_candidates():
    body = BASELINE.replace('    u8 *second;', '    u8 *second;\n    u8 *cursor;')
    body = replace(body, 'for (j = 0; j < 5; j++)', 'for (j = 0, cursor = first; j < 5; j++, cursor++)')
    body = replace(body, 'id = first[j + 9];', 'id = cursor[9];')
    body = body.replace('i * 16', '(i << 4)').replace('id * 16', '(id << 4)')
    forms = [('edge-cursor', body)]
    for inline in (False, True):
        candidate = body
        if inline:
            candidate = replace(candidate, '    u8 *first;\n', '')
            candidate = replace(candidate, '            first = nodes + (i << 4);\n', '')
            candidate = candidate.replace('first[', '(nodes + (i << 4))[')
            candidate = candidate.replace('cursor = first;', 'cursor = nodes + (i << 4);')
            candidate = candidate.replace('(first +', '((nodes + (i << 4)) +')
            forms.append(('edge-cursor-inline-owner', candidate))
        for suffix, before, after in (
                ('side-copies', '                            start = (x + fraction', '                            a = (x + fraction'),
                ('fraction-first', '    f32 minimum;\n    f32 fraction;', '    f32 fraction;\n    f32 minimum;'),
                ('assignments-swapped', '                            a = start;\n                            b = end;',
                 '                            b = end;\n                            a = start;'),
                ('sentinel-first', 'id != 255', '255 != id')):
            variant = replace(candidate, before, after)
            if suffix == 'side-copies':
                variant = variant.replace('                            end = (f32)', '                            b = (f32)')
                variant = variant.replace('(0.0f < end && 0.0f < start && start <= end)',
                                          '(0.0f < b && 0.0f < a && a <= b)')
                variant = variant.replace('(end < 0.0f && start < 0.0f && end <= start)',
                                          '(b < 0.0f && a < 0.0f && b <= a)')
            forms.append(('edge-cursor' + ('-inline-owner' if inline else '') + '-' + suffix, variant))
    return forms


def parameter_candidates():
    forms = []
    for name, body in [('pointer-baseline', BASELINE)] + cursor_candidates()[:2]:
        body = replace(body, '    f32 nx;\n    f32 nz;', '    f32 query_x;')
        body = replace(body, '    band = func_15085DA8(y);', '    query_x = x;\n    band = func_15085DA8(y);')
        prefix, calculations = body.split('                            nx = ', 1)
        calculations = '                            nx = ' + calculations
        calculations = re.sub(r'\bx\b', 'query_x', calculations)
        calculations = re.sub(r'\bnx\b', 'x', calculations)
        calculations = re.sub(r'\bnz\b', 'y', calculations)
        body = prefix + calculations
        forms.append((name + '-parameter-normal', body))
        forms.append((name + '-parameter-normal-copy-tangent', body.replace('swap * az', 'y * az')))
    return forms


SELECTED = dict(candidates())['reused-side-values']


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
    script.write_text('SECTIONS { .text 0x15086D94 : SUBALIGN(4) { *(.text) } }\n')
    link = ['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_15086D94']
    link += ['--defsym=' + symbol + '=' + hex(address) for symbol, address in SYMBOLS.items()]
    subprocess.run(link + ['-o', str(elf), str(obj)], capture_output=True, check=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_15086D94']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    words = words[:size]
    retail = list(struct.unpack_from('>207I', (conker / 'conker.us.bin').read_bytes(), 0xB4244))
    slot = words + [0] * max(0, 207 - size)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}')
                   for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    return dict(name=name, body_words=size, frame=(-words[0]) & 65535,
                real_differences=len(differences) + max(0, size - 207), differences=differences,
                diagnostics=result.stdout + result.stderr, unroll=unroll), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-graph-edge-crossing'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates() + lifetime_candidates() + cursor_candidates() + parameter_candidates():
        for unroll in (False, True):
            record, _ = compile_candidate(root, output, name + ('-unroll' if unroll else ''), body, unroll)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']),
                  record['real_differences'], record['diagnostics'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
