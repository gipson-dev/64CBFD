"""Recover the queued-zone player selection pass and measure its retail slot."""

import argparse
import json
import re
import struct
import subprocess
from textwrap import indent
from pathlib import Path

from tools.match_progress import load_elf_functions
from tools.experiments.game_record_neighbor_visit_candidates import QUERY, replace


ENTRY = 0x1508B3F8
SYMBOLS = {'D_800D23B0': 0x800D23B0, 'D_8008FD8C': 0x8008FD8C,
           'D_8008FD90': 0x8008FD90, 'D_800CC2D0': 0x800CC2D0,
           'D_800D2350': 0x800D2350, 'D_8009DA5C': 0x8009DA5C,
           'func_15085DA8': 0x15085DA8, 'func_15085DF8': 0x15085DF8,
           'bzero': 0x100226F0, 'func_1508B2A8': 0x1508B2A8}
DECLARATIONS = '''extern s32 D_800D23B0;
extern s8 D_8008FD8C;
extern s8 D_8008FD90;
extern u8 D_800CC2D0[];
extern u8 *D_800D2350;
extern f32 D_8009DA5C;
s32 func_15085DA8(f32);
s32 func_15085DF8(f32, f32, f32, s8, s8);
void func_1508B2A8(u8, NeighborVisitQueryB3020 *);
'''
BASELINE = '''void func_1508B3F8(void) {
    NeighborVisitQueryB3020 query;
    s32 *selections;
    u8 *zone;
    u8 *actor;
    u8 *nodes;
    u8 *node;
    s32 i;
    s32 player;
    s32 ready;
    s32 root;
    s32 best;
    s32 j;
    f32 x;
    f32 y;
    f32 z;
    f32 dx;
    f32 dz;
    f32 distance;
    f32 minimum;

    selections = (s32 *)(D_800D23B0 + 0x55C);
    zone = (u8 *)D_800D23B0 + 0x1748;
    for (i = 0; i < D_8008FD8C; i++) {
        if (selections[i] != -1) {
            selections[i] = -2;
        }
    }
    for (i = 0; i < *(s8 *)((u8 *)D_800D23B0 + 0x1745); i++, zone += 12) {
        query.threshold = *(f32 *)(zone + 0);
        x = (f32)*(s16 *)(zone + 4);
        y = (f32)*(s16 *)(zone + 6);
        z = (f32)*(s16 *)(zone + 8);
        ready = 0;
        for (player = D_8008FD90, actor = D_800CC2D0 + player * 0x32C;
             player < D_8008FD8C; player++, actor += 0x32C) {
            distance = *(f32 *)(actor + 0x18) - y;
            if (distance < 200.0f && -100.0f < distance) {
                dx = *(f32 *)(actor + 0x14) - x;
                dz = *(f32 *)(actor + 0x1C) - z;
                if (dx * dx + dz * dz < query.threshold + 100.0f) {
                    best = 0xFF;
                    minimum = D_8009DA5C;
                    if (!ready) {
                        query.count = 0;
                        ready = 1;
                        root = func_15085DF8(x, y, z, 0, func_15085DA8(y));
                        if (root != -1) {
                            query.x = x;
                            query.z = z;
                            query.count = 0;
                            bzero(query.visited, 32);
                            func_1508B2A8((u8)root, &query);
                        }
                    }
                    nodes = D_800D2350;
                    for (j = 0; j < query.count; j++) {
                        node = nodes + query.ids[j] * 16;
                        dx = (f32)*(s16 *)(node + 0) - *(f32 *)(actor + 0x14);
                        dz = (f32)*(s16 *)(node + 4) - *(f32 *)(actor + 0x1C);
                        distance = dx * dx + dz * dz;
                        if (distance < query.distances[j] && distance < minimum) {
                            best = query.ids[j];
                            minimum = distance;
                        }
                    }
                    if (best != 0xFF) {
                        node = D_800D2350 + best * 16;
                        if (selections[player] != -2) {
                            *(s32 *)((u8 *)D_800D23B0 + player * 4 + 0x5C) = 1;
                        }
                        selections[player] = node[7];
                    }
                }
            }
        }
    }
    for (i = 0; i < D_8008FD8C; i++) {
        if (selections[i] < 0) {
            selections[i] = -1;
        }
    }
    *(s8 *)((u8 *)D_800D23B0 + 0x1745) = 0;
}'''


def candidates():
    forms = [('indexed', BASELINE)]
    forms.append(('split-height-call', replace(BASELINE,
        'root = func_15085DF8(x, y, z, 0, func_15085DA8(y));',
        'root = func_15085DA8(y);\n                        root = func_15085DF8(x, y, z, 0, root);')))
    forms.append(('distance-z-reuse', re.sub(r'\bdistance\b', 'dz',
                  replace(BASELINE, '    f32 distance;\n', ''))))
    forms.append(('byte-best', replace(BASELINE, '    s32 best;', '    u8 best;')))
    forms.append(('word-query', BASELINE.replace('query.ids[j]', '((u8 *)&query)[j + 0x2E]')
                  .replace('query.distances[j]', '*(f32 *)((u8 *)&query + j * 4 + 0xC)')))
    forms.append(('explicit-actor-coordinates', replace(replace(BASELINE, '    f32 minimum;',
        '    f32 minimum;\n    f32 actorX;\n    f32 actorZ;'),
        '                    nodes = D_800D2350;',
        '                    nodes = D_800D2350;\n                    actorX = *(f32 *)(actor + 0x14);\n                    actorZ = *(f32 *)(actor + 0x1C);')
        .replace('- *(f32 *)(actor + 0x14)', '- actorX').replace('- *(f32 *)(actor + 0x1C)', '- actorZ')))
    loop = BASELINE.split('                    for (j = 0; j < query.count; j++) {\n', 1)[1].split('\n                    }', 1)[0]
    original = '                    for (j = 0; j < query.count; j++) {\n' + loop + '\n                    }'
    manual = ('                    j = 0;\n'
              '                    if (query.count > 0) {\n'
              '                        for (; j < (query.count & 3); j++) {\n' + loop + '\n                        }\n'
              '                        for (; j < query.count; j += 4) {\n' +
              '\n'.join(loop.replace('query.ids[j]', 'query.ids[j + %d]' % n)
                        .replace('query.distances[j]', 'query.distances[j + %d]' % n) for n in range(4)) +
              '\n                        }\n                    }')
    forms.append(('explicit-four-candidates', replace(BASELINE, original, manual)))
    gated = replace(BASELINE, '                    nodes = D_800D2350;',
                    '                    if (query.count > 0) {\n                    nodes = D_800D2350;')
    gated = replace(gated, '                    if (best != 0xFF)',
                    '                    }\n                    if (best != 0xFF)')
    forms.append(('positive-count-gate', gated))
    forms.append(('positive-count-narrow-best', gated.replace('best = query.ids[j];',
                 'best = (u8)(query.ids[j] / 1);')))
    forms.append(('positive-count-z-reuse', re.sub(r'\bdistance\b', 'dz',
                  replace(gated, '    f32 distance;\n', ''))))
    manual_body = dict(forms)['explicit-four-candidates']
    forms.append(('manual-four-narrow-best', re.sub(r'best = (query\.ids\[[^]]+\]);',
                  r'best = (u8)(\1 / 1);', manual_body)))
    manual_gated = replace(manual_body, '                    nodes = D_800D2350;\n', '')
    manual_gated = replace(manual_gated, '                    if (query.count > 0) {',
                           '                    if (query.count > 0) {\n                        nodes = D_800D2350;')
    forms.append(('manual-four-gated-base', manual_gated))
    forms.append(('manual-four-gated-z-reuse', re.sub(r'\bdistance\b', 'dz',
                  replace(manual_gated, '    f32 distance;\n', ''))))
    for name, body in (('manual-four', manual_gated), ('indexed', BASELINE)):
        forms.append((name + '-query-last', replace(replace(body,
            '    NeighborVisitQueryB3020 query;\n', ''), '    f32 minimum;',
            '    f32 minimum;\n    NeighborVisitQueryB3020 query;')))
    pointer = replace(manual_body, '    f32 minimum;',
                      '    f32 minimum;\n    u8 *ids;\n    f32 *distances;\n    f32 *end;')
    repeated = '\n'.join(loop.replace('query.ids[j]', 'query.ids[j + %d]' % n)
                         .replace('query.distances[j]', 'query.distances[j + %d]' % n) for n in range(4))
    pointer_repeated = '\n'.join(loop.replace('query.ids[j]', 'ids[%d]' % n)
                                .replace('query.distances[j]', 'distances[%d]' % n) for n in range(4))
    pointer = replace(pointer, '                        for (; j < query.count; j += 4) {\n' + repeated,
        '                        ids = query.ids + j;\n'
        '                        distances = query.distances + j;\n'
        '                        end = query.distances + query.count;\n'
        '                        for (; distances != end; distances += 4, ids += 4) {\n' + pointer_repeated)
    forms.append(('manual-four-pointer-end', pointer))
    forms.append(('manual-four-pointer-end-z-reuse', re.sub(r'\bdistance\b', 'dz',
                  replace(pointer, '    f32 distance;\n', ''))))
    forms.append(('manual-four-pointer-end-count-exit', replace(pointer,
        '                        ids = query.ids + j;',
        '                        if (j == query.count) {\n                            goto selection;\n                        }\n'
        '                        ids = query.ids + j;').replace(
        '                    if (best != 0xFF)', '                  selection:\n                    if (best != 0xFF)')))
    retail_loop = ('                    /* Keep the remainder-first, four-candidate retail scan. */\n'
                  '                    j = 0;\n'
                  '                    if (query.count > 0) {\n'
                  '                        nodes = D_800D2350;\n'
                  '                        remainder = query.count & 3;\n'
                  '                        if (remainder) {\n'
                  '                            do {\n' + indent(loop, '        ') + '\n'
                  '                                j++;\n'
                  '                            } while (j != remainder);\n'
                  '                            if (j == query.count) {\n'
                  '                                goto selection;\n'
                  '                            }\n'
                  '                        }\n'
                  '                        ids = query.ids + j;\n'
                  '                        distances = query.distances + j;\n'
                  '                        end = query.distances + query.count;\n'
                  '                        do {\n' + indent(pointer_repeated, '    ') + '\n'
                  '                            distances += 4;\n'
                  '                            ids += 4;\n'
                  '                        } while (distances != end);\n'
                  '                    }')
    retail = replace(BASELINE, '    f32 minimum;',
                     '    f32 minimum;\n    u8 *ids;\n    f32 *distances;\n    f32 *end;\n    s32 remainder;')
    retail = replace(retail, '                    nodes = D_800D2350;\n' + original, retail_loop)
    retail = replace(retail, '                    if (best != 0xFF)',
                     '                  selection:\n                    if (best != 0xFF)')
    forms.append(('retail-remainder-and-pointer-end', retail))
    forms.append(('retail-remainder-z-reuse', re.sub(r'\bdistance\b', 'dz',
                  replace(retail, '    f32 distance;\n', ''))))
    hoisted = replace(retail, '    f32 minimum;', '    f32 minimum;\n    f32 actorX;\n    f32 actorZ;')
    hoisted = replace(hoisted, '                        nodes = D_800D2350;',
        '                        nodes = D_800D2350;\n'
        '                        actorX = *(f32 *)(actor + 0x14);\n'
        '                        actorZ = *(f32 *)(actor + 0x1C);')
    hoisted = hoisted.replace('- *(f32 *)(actor + 0x14)', '- actorX').replace('- *(f32 *)(actor + 0x1C)', '- actorZ')
    forms.append(('retail-remainder-cached-coordinates', hoisted))
    reused = dict(forms)['retail-remainder-z-reuse']
    biased = reused.replace('ids = query.ids + j;', 'ids = (u8 *)&query + j;')
    biased = biased.replace('distances = query.distances + j;', 'distances = (f32 *)((u8 *)&query + j * 4);')
    biased = biased.replace('end = query.distances + query.count;', 'end = (f32 *)((u8 *)&query + query.count * 4);')
    biased = re.sub(r'ids\[([0-3])\]', lambda m: 'ids[%d]' % (int(m[1]) + 0x2E), biased)
    biased = re.sub(r'distances\[([0-3])\]', lambda m: 'distances[%d]' % (int(m[1]) + 3), biased)
    forms.append(('retail-biased-cursors', biased))
    chars = biased.replace('f32 *distances;', 'u8 *distances;').replace('f32 *end;', 'u8 *end;')
    chars = chars.replace('(f32 *)((u8 *)&query + j * 4)', '(u8 *)&query + j * 4')
    chars = chars.replace('(f32 *)((u8 *)&query + query.count * 4)', '(u8 *)&query + query.count * 4')
    chars = re.sub(r'distances\[([3-6])\]', lambda m: '*(f32 *)(distances + %d)' % (int(m[1]) * 4), chars)
    chars = chars.replace('distances += 4;', 'distances += 16;')
    forms.append(('retail-byte-cursors', chars))
    for name, body in (('retail', reused), ('biased', biased), ('byte', chars)):
        forms.append((name + '-integer-minimum-address', body.replace('minimum = D_8009DA5C;',
                      'minimum = *(f32 *)((s32)&D_8009DA5C / 1);')))
        forms.append((name + '-integer-node-base', body.replace('nodes = D_800D2350;',
                      'nodes = (u8 *)((s32)D_800D2350 / 1);')))
    return forms


CHECKPOINT = dict(candidates())['retail-byte-cursors']


def retain_query_pointer(body, flags=False):
    body = replace(body, '    NeighborVisitQueryB3020 query;',
                   '    NeighborVisitQueryB3020 query;\n'
                   '    NeighborVisitQueryB3020 *context;'
                   + ('\n    u8 *flags;' if flags else ''))
    body = body.replace('query.', 'context->').replace('&query', 'context')
    body = replace(body, '    selections =',
                   '    context = &query;\n'
                   + ('    flags = context->visited;\n' if flags else '')
                   + '    selections =')
    if flags:
        body = body.replace('bzero(context->visited, 32);', 'bzero(flags, 32);')
    return body


SELECTED = retain_query_pointer(CHECKPOINT)


def compile_candidate(root, output, name, body, unroll=False):
    conker = root / 'conker'
    source, obj, elf = [output / (name + suffix) for suffix in ('.c', '.o', '.elf')]
    source.write_text('#include <ultra64.h>\n' + QUERY + '\n' + DECLARATIONS + '\n' + body + '\n')
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
    script.write_text('SECTIONS { .text 0x1508B3F8 : SUBALIGN(4) { *(.text) } }\n')
    link = ['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1508B3F8']
    link += ['--defsym=' + symbol + '=' + hex(address) for symbol, address in SYMBOLS.items()]
    subprocess.run(link + ['-o', str(elf), str(obj)], capture_output=True, check=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_1508B3F8']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    words = words[:size]
    retail = list(struct.unpack_from('>369I', (conker / 'conker.us.bin').read_bytes(), 0xB88A8))
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(words, retail)) if a != b]
    return dict(name=name, body_words=size, frame=(-words[0]) & 65535,
                real_differences=len(differences) + abs(size - 369), differences=differences,
                diagnostics=result.stdout + result.stderr, unroll=unroll), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--names', nargs='*')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-zone-neighbor-selection'
    output.mkdir(exist_ok=True)
    forms = candidates()
    if args.names:
        wanted = set(args.names)
        if not wanted <= dict(forms).keys():
            parser.error('unknown candidate')
        forms = [(n, b) for n, b in forms if n in wanted]
    records = []
    for name, body in forms:
        for unroll in (False, True):
            record, _ = compile_candidate(root, output, name + ('-unroll' if unroll else ''), body, unroll)
            records.append(record)
            print(record['name'], record['body_words'], record['frame'], record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
