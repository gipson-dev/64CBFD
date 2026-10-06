"""Recover the recursive X/Z threshold visitor without changing retail's masks."""

import argparse
import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


ENTRY = 0x1508B2A8
QUERY = '''typedef struct NeighborVisitQueryB3020 {
    f32 x;
    f32 z;
    f32 threshold;
    f32 distances[8];
    s16 count;
    u8 ids[8];
    u8 visited[32];
} NeighborVisitQueryB3020;'''
BASELINE = '''void func_1508B2A8(u8 id, u8 *query) {
    u8 *node;
    s32 i;
    u8 neighbor;
    f32 x;
    f32 z;
    f32 distance;

    query[(id >> 3) + 0x36] |= 1 << (id & 3);
    node = D_800D2350 + id * 16;
    x = (f32)*(s16 *)(node + 0) - *(f32 *)(query + 0);
    z = (f32)*(s16 *)(node + 4) - *(f32 *)(query + 4);
    distance = x * x + z * z;
    if (*(f32 *)(query + 8) < distance) {
        if (*(s16 *)(query + 0x2C) < 8) {
            query[*(s16 *)(query + 0x2C) + 0x2E] = id;
            *(f32 *)(query + *(s16 *)(query + 0x2C) * 4 + 0xC) = distance;
            (*(s16 *)(query + 0x2C))++;
        }
    } else {
        for (i = 0; i < 5; i++) {
            neighbor = node[9];
            if (neighbor != 0xFF) {
                if (!(query[(neighbor >> 3) + 0x36] & (1 << (neighbor & 3)))) {
                    func_1508B2A8(neighbor, query);
                }
            }
            node++;
        }
    }
}'''


def replace(body, before, after, count=1):
    if body.count(before) != count:
        raise ValueError('neighbor-visitor anchor no longer binds: ' + before)
    return body.replace(before, after)


def candidates():
    forms = [('raw-byte-walk', BASELINE)]
    forms.append(('word-neighbor', replace(BASELINE, '    u8 neighbor;', '    s32 neighbor;')))
    forms.append(('word-id', replace(BASELINE, 'u8 id,', 's32 id,')))
    forms.append(('early-return', replace(replace(BASELINE, '    } else {\n', '        return;\n    }\n    {\n'),
                    '    }\n}', '    }\n}')))
    forms.append(('combined-neighbor-gate', replace(BASELINE,
        '''            if (neighbor != 0xFF) {
                if (!(query[(neighbor >> 3) + 0x36] & (1 << (neighbor & 3)))) {
                    func_1508B2A8(neighbor, query);
                }
            }''',
        '''            if (neighbor != 0xFF && !(query[(neighbor >> 3) + 0x36] & (1 << (neighbor & 3)))) {
                func_1508B2A8(neighbor, query);
            }''')))
    parameter = replace(replace(BASELINE, '    u8 neighbor;\n', ''), '            neighbor = node[9];',
                         '            id = node[9];').replace('neighbor', 'id')
    forms.append(('parameter-reuse', parameter))
    z_reuse = replace(replace(replace(parameter, '    f32 distance;\n', ''),
                             '    distance = x * x + z * z;', '    z = x * x + z * z;'),
                             'distance', 'z', 2)
    forms.append(('parameter-z-reuse', z_reuse))
    for name, body in (('walker', BASELINE), ('parameter-walker', parameter), ('parameter-z-walker', z_reuse)):
        body = replace(body, '    u8 *node;', '    u8 *node;\n    u8 *walk;')
        body = replace(body, 'for (i = 0; i < 5; i++)', 'for (i = 0, walk = node; i < 5; i++)')
        body = replace(replace(body, 'node[9]', 'walk[9]'), '            node++;', '            walk++;')
        forms.append((name, body))
        forms.append((name + '-index-first', replace(body, '    u8 *node;\n    u8 *walk;\n    s32 i;',
                                                   '    s32 i;\n    u8 *node;\n    u8 *walk;')))
    walk = dict(forms)['parameter-z-walker']
    forms.append(('walker-divided-edge', replace(walk, 'id = walk[9];', 'id = walk[9] / 1;')))
    forms.append(('walker-late-byte-index', replace(walk, 'query[(id >> 3) + 0x36] & (1 << (id & 3))',
                 'query[((u8)(id / 1) >> 3) + 0x36] & (1 << ((u8)(id / 1) & 3))')))
    forms.append(('walker-word-cast-edge', replace(walk, 'id = walk[9];', 'id = (s32)walk[9];')))
    forms.append(('walker-negated-edge', replace(walk, 'id = walk[9];', 'id = -(-walk[9]);')))
    forms.append(('walker-byte-edge-separate-mask', replace(walk, 'id = walk[9];', 'id = walk[9] & 0xFF;')))
    late = dict(forms)['walker-late-byte-index']
    flags = late.replace('query[(id >> 3) + 0x36]', '*(query + (id >> 3) + 0x36)')
    flags = flags.replace('query[((u8)(id / 1) >> 3) + 0x36]', '*(query + ((u8)(id / 1) >> 3) + 0x36)')
    forms.append(('late-explicit-flag-dereferences', flags))
    typed = replace(late, 'u8 *query)', 'NeighborVisitQueryB3020 *query)')
    typed = typed.replace('query[(id >> 3) + 0x36]', 'query->visited[id >> 3]')
    typed = typed.replace('query[((u8)(id / 1) >> 3) + 0x36]', 'query->visited[(u8)(id / 1) >> 3]')
    typed = typed.replace('*(f32 *)(query + 0)', 'query->x').replace('*(f32 *)(query + 4)', 'query->z')
    typed = typed.replace('*(f32 *)(query + 8)', 'query->threshold')
    typed = typed.replace('*(s16 *)(query + 0x2C)', 'query->count')
    typed = typed.replace('query[query->count + 0x2E]', '((u8 *)query)[query->count + 0x2E]')
    typed = typed.replace('(query + query->count * 4 + 0xC)', '((u8 *)query + query->count * 4 + 0xC)')
    forms.append(('typed-query-late-index', typed))
    opaque = replace(typed, 'NeighborVisitQueryB3020 *query)', 'void *context)')
    opaque = replace(opaque, '    u8 *node;', '    NeighborVisitQueryB3020 *query;\n    u8 *node;')
    opaque = replace(opaque, '    query->visited[id >> 3]', '    query = context;\n    query->visited[id >> 3]')
    forms.append(('opaque-query-local', opaque))
    forms.append(('opaque-query-local-last', replace(replace(opaque, '    NeighborVisitQueryB3020 *query;\n', ''),
                                                    '    f32 z;', '    f32 z;\n    NeighborVisitQueryB3020 *query;')))
    local = replace(late, '    f32 z;', '    f32 z;\n    s32 maskIndex;')
    local = replace(local, '            id = walk[9];', '            id = walk[9];\n            maskIndex = (u8)(id / 1);')
    local = local.replace('(u8)(id / 1)', 'maskIndex').replace('maskIndex = maskIndex;', 'maskIndex = (u8)(id / 1);')
    forms.append(('late-word-index-local', local))
    forms.append(('late-byte-index-local', replace(local, '    s32 maskIndex;', '    u8 maskIndex;')))
    return forms


SELECTED = dict(candidates())['typed-query-late-index']


def compile_candidate(root, output, name, body, no_unroll=True):
    conker = root / 'conker'
    source, obj, elf = [output / (name + suffix) for suffix in ('.c', '.o', '.elf')]
    preamble = '#include <ultra64.h>\nextern u8 *D_800D2350;\n\n'
    if 'NeighborVisitQueryB3020' in body:
        preamble += QUERY + '\n\n'
    source.write_text(preamble + body + '\n')
    command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
               '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
               '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', '-woff', '649,838']
    for include in ('.', 'include', 'include/2.0L', 'include/2.0L/PR', 'include/libc'):
        command += ['-I', include]
    command += ['-mips2', '-o32', '-O2', '-g3']
    if no_unroll:
        command += ['-Wo,-loopunroll,0']
    command += ['-o', str(obj.relative_to(conker)), str(source.relative_to(conker))]
    result = subprocess.run(command, cwd=conker, capture_output=True, text=True, check=True)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1508B2A8 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1508B2A8',
                    '--defsym=D_800D2350=0x800D2350', '-o', str(elf), str(obj)], capture_output=True, check=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_1508B2A8']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    words = words[:size]
    retail = list(struct.unpack_from('>84I', (conker / 'conker.us.bin').read_bytes(), 0xB8758))
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(words, retail)) if a != b]
    saves = [w >> 16 & 31 for w in words if w >> 26 == 43 and w >> 21 & 31 == 29
             and 16 <= w >> 16 & 31 <= 23]
    return dict(name=name, body_words=size, frame=(-words[0]) & 65535, saved=saves,
                real_differences=len(differences) + abs(size - 84), differences=differences,
                diagnostics=result.stdout + result.stderr), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--names', nargs='*')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-record-neighbor-visit'
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
