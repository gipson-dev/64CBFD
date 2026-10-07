"""Recover the four matrix routes, helper failures and point-list home reloads."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x1514654C, 0x1739FC, 120
FUNCTION = 'func_1514654C'
SYMBOLS = dict(func_1503195C=0x1503195C, func_15031070=0x15031070,
    func_15145EA4=0x15145EA4, guMtxL2F=0x151EFEB8, func_150A7960=0x150A7960,
    D_800BE9C0=0x800BE9C0)
DECLARATIONS = '''s32 func_15031070(struct126 *, struct127 *, Mtx **, Mtx **);
void func_15145EA4(struct17 **, struct17 **, u8 *, s32);
void func_150A7960(f32 [4][4], f32, f32, f32, f32 *, f32 *, f32 *);
'''
PROTOTYPE = '''s32 func_1514654C(struct127 *actor, u8 *descriptor, s32 index,
    struct17 **inputArgument, struct17 **outputArgument, s32 count);'''
BASELINE = '''s32 func_1514654C(struct127 *actor, u8 *descriptor, s32 index,
    struct17 **inputArgument, struct17 **outputArgument, s32 count) {
    f32 converted[4][4];
    Mtx *matrix;
    Mtx *other;
    struct126 *lookup;
    u8 *attachment;
    u8 *bank;
    struct17 **input;
    struct17 **outputs;
    s32 i;

    if (actor == 0 || descriptor == 0 || (bank = (u8 *)actor->unk1D4) == 0) {
        return 0;
    }
    attachment = *(u8 **)(descriptor + 0x48);
    if (attachment != 0) {
        if (attachment[0x3F6] == 0) {
            return 0;
        }
        matrix = ((Mtx **)(attachment + 0x3E8))[D_800BE9C0] + index;
    } else if (*(u16 *)(descriptor + 0x1E) != 0) {
        lookup = func_1503195C(actor, *(u16 *)(descriptor + 0x1E), 0);
        if (lookup == 0) {
            return 0;
        }
        if (func_15031070(lookup, actor, &matrix, &other) == 0) {
            return 0;
        }
        if (*(u8 **)((u8 *)lookup + 0x48) != 0) {
            matrix += *(u16 *)(descriptor + 0x20);
        }
    } else if (*(Mtx **)(descriptor + 0x34) != 0) {
        matrix = *(Mtx **)(descriptor + 0x34) + D_800BE9C0;
    } else {
        func_15145EA4(inputArgument, outputArgument, bank + descriptor[2] * 64, count);
        return 1;
    }
    if (matrix != 0) {
        guMtxL2F(converted, matrix);
        input = inputArgument;
        outputs = outputArgument;
        for (i = 0; i < count; i++) {
            func_150A7960(converted, (*input)->unk0, (*input)->unk4, (*input)->unk8,
                &(*outputs)->unk0, &(*outputs)->unk4, &(*outputs)->unk8);
            input++;
            outputs++;
        }
        return 1;
    }
    return 0;
}'''


def candidates():
    for null_gate, loop, early, views in itertools.product((False, True), range(3), (False, True), (False, True)):
        body = BASELINE
        if null_gate:
            body = body.replace('    if (matrix != 0) {', '    if (matrix == 0) { return 0; }\n    {')
            body = body.replace('    }\n    return 0;\n}', '    }\n}')
        if loop == 1:
            body = body.replace('        for (i = 0; i < count; i++) {',
                '        i = 0;\n        if (count > 0) {\n        do {')
            body = body.replace('            outputs++;\n        }',
                '            outputs++;\n            i++;\n        } while (i != count);\n        }')
        elif loop == 2:
            body = body.replace('        for (i = 0; i < count; i++) {',
                '        i = 0;\n        while (i < count) {')
            body = body.replace('            outputs++;\n        }', '            outputs++;\n            i++;\n        }')
        if early:
            body = body.replace('    struct17 **outputs;\n', '    struct17 **outputs;\n    struct17 *point;\n    struct17 *destination;\n')
            body = body.replace('            func_150A7960(', '            point = *input;\n            destination = *outputs;\n            func_150A7960(', 1)
            body = body.replace('(*input)->', 'point->').replace('(*outputs)->', 'destination->')
        if views:
            body = body.replace('((Mtx **)(attachment + 0x3E8))[D_800BE9C0] + index',
                '(Mtx *)(((u8 **)(attachment + 0x3E8))[D_800BE9C0] + ((u32)index << 6))')
            body = body.replace('matrix += *(u16 *)(descriptor + 0x20);',
                'matrix = (Mtx *)((u8 *)matrix + (*(u16 *)(descriptor + 0x20) << 6));')
        yield 'gate%d-loop%d-points%d-views%d' % (null_gate, loop, early, views), body


def lifetime_candidates():
    forms = dict(candidates())
    for split, key, scopes, early in itertools.product((False, True), (False, True), range(3), (False, True)):
        body = forms['gate0-loop1-points%d-views0' % early]
        if split:
            body = body.replace('    Mtx *other;', '    Mtx *other;\n    Mtx *lookupMatrix;')
            body = body.replace('actor, &matrix, &other)', 'actor, &lookupMatrix, &other)')
            body = body.replace('        if (*(u8 **)((u8 *)lookup',
                '        matrix = lookupMatrix;\n        if (*(u8 **)((u8 *)lookup', 1)
        if key:
            body = body.replace('    s32 i;', '    s32 i;\n    s32 lookupKey;')
            body = body.replace('} else if (*(u16 *)(descriptor + 0x1E) != 0)',
                '} else if ((lookupKey = *(u16 *)(descriptor + 0x1E)) != 0)')
            body = body.replace('func_1503195C(actor, *(u16 *)(descriptor + 0x1E), 0)',
                'func_1503195C(actor, lookupKey, 0)')
        if scopes == 1:
            body = body.replace('    f32 converted[4][4];\n', '')
            body = body.replace('    if (matrix != 0) {', '    if (matrix != 0) {\n        f32 converted[4][4];')
        elif scopes == 2:
            body = body.replace('    f32 converted[4][4];\n', '')
            body = body.replace('    s32 i;', '    f32 converted[4][4];\n    s32 i;')
        yield 'lifetime-split%d-key%d-scopes%d-points%d' % (split, key, scopes, early), body


def branch_candidates():
    base = dict(lifetime_candidates())['lifetime-split1-key0-scopes0-points0']
    for key_type, assignment, returns, reuse in itertools.product(('s32', 'u32', 'u16'), (False, True), range(3), (False, True)):
        body = base.replace('    s32 i;', '    s32 i;\n    ' + key_type + ' lookupKey;')
        body = body.replace('} else if (*(u16 *)(descriptor + 0x1E) != 0)',
            '} else if ((lookupKey = *(u16 *)(descriptor + 0x1E)) != 0)')
        body = body.replace('func_1503195C(actor, *(u16 *)(descriptor + 0x1E), 0)',
            'func_1503195C(actor, lookupKey, 0)')
        if assignment:
            body = body.replace('        matrix = lookupMatrix;\n', '')
            body = body.replace('            matrix += *(u16 *)(descriptor + 0x20);\n        }',
                '            matrix = lookupMatrix + *(u16 *)(descriptor + 0x20);\n'
                '        } else {\n            matrix = lookupMatrix;\n        }')
        if returns == 1:
            body = body.replace('        } while (i != count);\n        }',
                '        } while (i != count);\n        return 1;\n        }')
        elif returns == 2:
            body = body.replace('        } while (i != count);\n        }',
                '        } while (i != count);\n        return 1;\n        } else { return 1; }')
        if reuse:
            body = body.replace('    struct17 **input;\n    struct17 **outputs;\n', '')
            body = body.replace('        input = inputArgument;\n        outputs = outputArgument;\n', '')
            body = body.replace('(*input)->', '(*inputArgument)->').replace('(*outputs)->', '(*outputArgument)->')
            body = body.replace('            input++;', '            inputArgument++;')
            body = body.replace('            outputs++;', '            outputArgument++;')
        yield 'branch-key%s-assignment%d-returns%d-reuse%d' % (key_type, assignment, returns, reuse), body


def register_candidates():
    base = dict(branch_candidates())['branch-keyu32-assignment1-returns1-reuse0']
    for mask, order in itertools.product(range(16), range(2)):
        body = base
        for i, declaration in enumerate(('s32 i;', 'struct17 **input;', 'struct17 **outputs;', 'u32 lookupKey;')):
            if mask >> i & 1:
                body = body.replace('    ' + declaration, '    register ' + declaration, 1)
        if order:
            body = body.replace('    f32 converted[4][4];\n', '')
            body = body.replace('    Mtx *matrix;', '    Mtx *matrix;\n    f32 converted[4][4];')
        yield 'register-mask%d-order%d' % (mask, order), body


def phase_candidates():
    base = dict(branch_candidates())['branch-keys32-assignment1-returns1-reuse0']
    for bank, key, matrix, counter, order in itertools.product((False, True), (False, True),
            (False, True), (False, True), range(3)):
        body = base
        if bank:
            body = body.replace('    u8 *bank;\n', '')
            body = body.replace('(bank = (u8 *)actor->unk1D4)', 'actor->unk1D4')
            body = body.replace('bank + descriptor[2] * 64', '(u8 *)actor->unk1D4 + descriptor[2] * 64')
        if key:
            body = body.replace('    s32 lookupKey;\n', '').replace('lookupKey', 'index')
        if matrix:
            body = body.replace('    Mtx *matrix;\n', '')
            for expression in ('((Mtx **)(attachment + 0x3E8))[D_800BE9C0] + index',
                    'lookupMatrix + *(u16 *)(descriptor + 0x20)', 'lookupMatrix',
                    '*(Mtx **)(descriptor + 0x34) + D_800BE9C0'):
                body = body.replace('matrix = ' + expression + ';',
                    'descriptor = (u8 *)(' + expression + ');')
            body = body.replace('if (matrix != 0)', 'if (descriptor != 0)')
            body = body.replace('guMtxL2F(converted, matrix)', 'guMtxL2F(converted, (Mtx *)descriptor)')
        if counter:
            body = body.replace('    s32 i;\n', '')
            body = body.replace('i = 0;', 'index = 0;').replace('i++;', 'index++;').replace('i != count', 'index != count')
        if order:
            body = body.replace('    f32 converted[4][4];\n', '')
            marker = '    Mtx *other;' if order == 1 else '    struct126 *lookup;'
            body = body.replace(marker, '    f32 converted[4][4];\n' + marker)
        yield 'phase-bank%d-key%d-matrix%d-counter%d-order%d' % (bank, key, matrix, counter, order), body


def layout_candidates():
    base = dict(branch_candidates())['branch-keys32-assignment1-returns1-reuse0']
    for key, counter, binding, zero_else in itertools.product((False, True), (False, True), range(3), (False, True)):
        body = base
        if not key:
            body = body.replace('    s32 lookupKey;\n', '')
            body = body.replace('((lookupKey = *(u16 *)(descriptor + 0x1E)) != 0)',
                '(*(u16 *)(descriptor + 0x1E) != 0)')
            body = body.replace('actor, lookupKey, 0)', 'actor, *(u16 *)(descriptor + 0x1E), 0)')
        if counter:
            body = body.replace('        i = 0;\n', '')
            body = body.replace('        input = inputArgument;', '        i = 0;\n        input = inputArgument;')
        if binding:
            body = body.replace('    f32 converted[4][4];', '    f32 converted[4][4];\n    f32 (*working)[4];')
            body = body.replace('    if (actor == 0', '    working = converted;\n    if (actor == 0', 1) if binding == 1 else (
                body.replace('    attachment = ', '    working = converted;\n    attachment = ', 1))
            body = body.replace('guMtxL2F(converted, matrix)', 'guMtxL2F(working, matrix)')
            body = body.replace('func_150A7960(converted,', 'func_150A7960(working,')
        if zero_else:
            body = body.replace('    }\n    return 0;\n}', '    } else {\n        return 0;\n    }\n}')
        yield 'layout-key%d-counter%d-binding%d-zero%d' % (key, counter, binding, zero_else), body


def route_candidates():
    base = dict(layout_candidates())['layout-key0-counter1-binding0-zero0']
    for kind, cache, storage in itertools.product(('s32', 'u32'), (False, True), range(4)):
        body = base.replace('    u8 *attachment;', '    ' + kind + ' route;')
        body = body.replace('    attachment = *(u8 **)(descriptor + 0x48);\n    if (attachment != 0)',
            '    route = *(' + kind + ' *)(descriptor + 0x48);\n    if (route != 0)')
        body = body.replace('attachment[0x3F6]', '((u8 *)route)[0x3F6]')
        body = body.replace('attachment + 0x3E8', '(u8 *)route + 0x3E8')
        body = body.replace('} else if (*(u16 *)(descriptor + 0x1E) != 0)',
            '} else if ((route = *(u16 *)(descriptor + 0x1E)) != 0)')
        body = body.replace('actor, *(u16 *)(descriptor + 0x1E), 0)', 'actor, route, 0)')
        if cache:
            body = body.replace('} else if (*(Mtx **)(descriptor + 0x34) != 0)',
                '} else if ((route = *(' + kind + ' *)(descriptor + 0x34)) != 0)')
            body = body.replace('matrix = *(Mtx **)(descriptor + 0x34) +', 'matrix = (Mtx *)route +')
        if storage:
            body = body.replace('    f32 converted[4][4];\n', '')
            body = body.replace('    Mtx *other;\n    Mtx *lookupMatrix;\n', '')
            fields = ('    f32 converted[4][4];', '    Mtx *other;', '    Mtx *lookupMatrix;')
            order = ((0, 1, 2), (1, 2, 0), (0, 2, 1))[storage - 1]
            declaration = '    struct {\n' + '\n'.join(fields[i] for i in order) + '\n    } workspace;\n'
            body = body.replace('    Mtx *matrix;\n', '    Mtx *matrix;\n' + declaration, 1)
            for field in ('converted', 'other', 'lookupMatrix'):
                body = body.replace(field, 'workspace.' + field)
            body = body.replace('f32 workspace.converted', 'f32 converted')
            body = body.replace('Mtx *workspace.other', 'Mtx *other').replace('Mtx *workspace.lookupMatrix', 'Mtx *lookupMatrix')
        yield 'route-type%s-cache%d-storage%d' % (kind, cache, storage), body


SELECTED = dict(layout_candidates())['layout-key0-counter1-binding0-zero0']


def compile_candidate(root, out, name, body=BASELINE, profile='o2g3'):
    out.mkdir(exist_ok=True)
    source, obj, elf = (out / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n#include "variables.h"\n' + DECLARATIONS + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, text=True, capture_output=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = out / 'matrix-route.ld'
    script.write_text('SECTIONS { .text 0x1514654C : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, rel = parse_object(obj)
    meta, pools = functions[FUNCTION], sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % WORDS, (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        pool_bytes=len(pools.get('.rodata', (0, b''))[1]), diagnostics=diagnostics, relocations=rel,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0))), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profiles', action='store_true')
    parser.add_argument('--lifetime', action='store_true')
    parser.add_argument('--branches', action='store_true')
    parser.add_argument('--registers', action='store_true')
    parser.add_argument('--phase', action='store_true')
    parser.add_argument('--layout', action='store_true')
    parser.add_argument('--route', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-matrix-route'
    forms = [('profile-' + p, BASELINE, p) for p in PROFILES] if args.profiles else [(n, b, 'o2g3') for n, b in
        (route_candidates() if args.route else layout_candidates() if args.layout else phase_candidates() if args.phase else register_candidates() if args.registers else branch_candidates() if args.branches else lifetime_candidates() if args.lifetime else candidates())]
    records = []
    for name, body, profile in forms:
        record, _ = compile_candidate(root, out, name, body, profile)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (out / ('profiles.json' if args.profiles else 'route.json' if args.route else 'layout.json' if args.layout else 'phase.json' if args.phase else 'registers.json' if args.registers else 'branches.json' if args.branches else 'lifetime.json' if args.lifetime else 'primary.json')).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
