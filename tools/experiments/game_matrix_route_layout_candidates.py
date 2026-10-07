"""Fit real private variables and return topology without instruction patches."""

import argparse
import itertools
import json
import sys
from pathlib import Path

from tools.experiments import game_matrix_route_candidates as route


def debug_locals(obj):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'ultralib/tools'))
    from libelf import ElfFile
    from mdebug import EcoffSt
    elf = ElfFile(Path(obj).read_bytes())
    for fdr in elf.find_section_by_name('.mdebug').fdrs:
        for pdr in fdr.pdrs:
            if pdr.name == route.FUNCTION:
                return dict(frame=pdr.frameoffset, locals={s.name: dict(storage=str(s.sc),
                    value=s.value - 0x100000000 if s.value & 0x80000000 else s.value)
                    for s in pdr.symrs if s.st == EcoffSt.LOCAL})
    raise ValueError('Missing matrix-route debug procedure')


def return_shape(body, kind):
    if kind == 1:
        body = body.replace('        }\n        return 1;\n    }\n    return 0;\n}',
            '        }\n    } else {\n        return 0;\n    }\n    return 1;\n}')
    elif kind == 2:
        body = body.replace('        }\n        return 1;\n    }\n    return 0;\n}',
            '        }\n    }\n    if (matrix == 0) {\n        return 0;\n    }\n    return 1;\n}')
    elif kind == 3:
        body = body.replace('        }\n        return 1;\n    }\n    return 0;\n}',
            '        }\n    }\n    return matrix != 0;\n}')
    return body


def lookup_shape(body, kind):
    marker = '        if (*(u8 **)((u8 *)lookup + 0x48) != 0)'
    if marker not in body:
        marker = '        if (*(u8 **)((u8 *)input + 0x48) != 0)'
    assert marker in body
    if kind == 1:
        body = body.replace(marker, '        matrix = lookupMatrix;\n' + marker, 1)
        body = body.replace('        } else {\n            matrix = lookupMatrix;\n        }', '        }')
    elif kind == 2:
        body = body.replace(marker, '        matrix = lookupMatrix;\n' + marker, 1)
        body = body.replace('            matrix = lookupMatrix + *(u16 *)(descriptor + 0x20);',
            '            matrix += *(u16 *)(descriptor + 0x20);')
        body = body.replace('        } else {\n            matrix = lookupMatrix;\n        }', '        }')
    return body


def topology_candidates():
    for returns, lookup in itertools.product(range(4), range(3)):
        yield 'topology-return%d-lookup%d' % (returns, lookup), lookup_shape(return_shape(route.SELECTED, returns), lookup)


def storage_candidates():
    base = lookup_shape(return_shape(route.SELECTED, 1), 1)
    for order, placement, attachment, bank in itertools.product(range(2), range(2), (False, True), (False, True)):
        body = base
        for declaration in ('    f32 converted[4][4];\n', '    Mtx *lookupMatrix;\n', '    Mtx *other;\n'):
            body = body.replace(declaration, '')
        declarations = '    Mtx *lookupMatrix;\n    Mtx *other;\n' if not order else '    Mtx *other;\n    Mtx *lookupMatrix;\n'
        if placement == 0:
            declarations += '    f32 converted[4][4];\n'
        body = body.replace('    Mtx *matrix;', declarations + '    Mtx *matrix;', 1)
        if placement == 1:
            body = body.replace('    s32 i;', '    s32 i;\n    f32 converted[4][4];', 1)
        if attachment:
            body = body.replace('    u8 *attachment;\n', '')
            body = body.replace('attachment = *(u8 **)(descriptor + 0x48);', 'matrix = *(Mtx **)(descriptor + 0x48);')
            body = body.replace('if (attachment != 0)', 'if (matrix != 0)')
            body = body.replace('attachment[0x3F6]', '((u8 *)matrix)[0x3F6]')
            body = body.replace('attachment + 0x3E8', '(u8 *)matrix + 0x3E8')
        if bank:
            body = body.replace('    u8 *bank;\n', '')
            body = body.replace('(bank = (u8 *)actor->unk1D4)', 'actor->unk1D4')
            body = body.replace('bank + descriptor[2] * 64', '(u8 *)actor->unk1D4 + descriptor[2] * 64')
        yield 'storage-order%d-placement%d-attachment%d-bank%d' % (order, placement, attachment, bank), body


def parameter_candidates():
    base = return_shape(route.SELECTED, 1)
    base = base.replace('    Mtx *matrix;\n', '').replace('    u8 *bank;\n', '').replace('    s32 i;\n', '')
    base = base.replace('(bank = (u8 *)actor->unk1D4)', 'actor->unk1D4')
    base = base.replace('bank + descriptor[2] * 64', '(u8 *)actor->unk1D4 + descriptor[2] * 64')
    for expression in ('((Mtx **)(attachment + 0x3E8))[D_800BE9C0] + index',
            'lookupMatrix + *(u16 *)(descriptor + 0x20)', 'lookupMatrix',
            '*(Mtx **)(descriptor + 0x34) + D_800BE9C0'):
        base = base.replace('matrix = ' + expression + ';', 'descriptor = (u8 *)(' + expression + ');')
    base = base.replace('if (matrix != 0)', 'if (descriptor != 0)')
    base = base.replace('guMtxL2F(converted, matrix)', 'guMtxL2F(converted, (Mtx *)descriptor)')
    base = base.replace('i = 0;', 'index = 0;').replace('i++;', 'index++;').replace('i != count', 'index != count')
    variables = dict(lookup='    struct126 *lookup;\n', attachment='    u8 *attachment;\n',
        input='    struct17 **input;\n', outputs='    struct17 **outputs;\n')
    for key, order, tail in itertools.product((False, True), range(2), variables):
        body = base
        for declaration in (*variables.values(), '    Mtx *lookupMatrix;\n', '    Mtx *other;\n', '    f32 converted[4][4];\n'):
            body = body.replace(declaration, '')
        declarations = ''.join(value for name, value in variables.items() if name != tail)
        declarations += ('    Mtx *lookupMatrix;\n    Mtx *other;\n' if not order else
            '    Mtx *other;\n    Mtx *lookupMatrix;\n')
        declarations += '    f32 converted[4][4];\n' + variables[tail]
        body = body.replace('s32 count) {\n', 's32 count) {\n' + declarations, 1)
        if key:
            body = body.replace('} else if (*(u16 *)(descriptor + 0x1E) != 0)',
                '} else if ((index = *(u16 *)(descriptor + 0x1E)) != 0)')
            body = body.replace('actor, *(u16 *)(descriptor + 0x1E), 0)', 'actor, index, 0)')
        yield 'parameter-key%d-order%d-tail%s' % (key, order, tail), body


def indexed_candidates():
    base = return_shape(route.SELECTED, 1)
    base = base.replace('    struct17 **input;\n', '').replace('    struct17 **outputs;\n', '')
    base = base.replace('        input = inputArgument;\n        outputs = outputArgument;\n', '')
    base = base.replace('(*input)->', 'inputArgument[i]->').replace('(*outputs)->', 'outputArgument[i]->')
    base = base.replace('            input++;\n            outputs++;\n', '')
    for reuse, placement, order in itertools.product(range(3), range(2), range(2)):
        body = base
        if reuse == 0:
            body = body.replace('    u8 *bank;\n', '')
            body = body.replace('(bank = (u8 *)actor->unk1D4)', '(matrix = (Mtx *)actor->unk1D4)')
            body = body.replace('bank + descriptor[2] * 64', '(u8 *)matrix + descriptor[2] * 64')
        elif reuse == 1:
            body = body.replace('    u8 *attachment;\n', '')
            body = body.replace('attachment = *(u8 **)(descriptor + 0x48);', 'matrix = *(Mtx **)(descriptor + 0x48);')
            body = body.replace('if (attachment != 0)', 'if (matrix != 0)')
            body = body.replace('attachment[0x3F6]', '((u8 *)matrix)[0x3F6]')
            body = body.replace('attachment + 0x3E8', '(u8 *)matrix + 0x3E8')
        else:
            body = body.replace('    s32 i;\n', '')
            body = body.replace('i = 0;', 'index = 0;').replace('i++;', 'index++;')
            body = body.replace('i != count', 'index != count').replace('Argument[i]', 'Argument[index]')
        declarations = [line for line in body.splitlines(keepends=True) if line.startswith('    ')
            and line.rstrip().endswith(';') and not line.startswith('        ')][:7]
        assert len(declarations) == 7 and '    f32 converted[4][4];\n' in declarations
        for declaration in declarations:
            body = body.replace(declaration, '', 1)
        variables = [line for line in declarations if line not in
            ('    f32 converted[4][4];\n', '    Mtx *lookupMatrix;\n', '    Mtx *other;\n')]
        outputs = ['    Mtx *lookupMatrix;\n', '    Mtx *other;\n']
        if order:
            outputs.reverse()
        ordered = variables[:3] + outputs + ['    f32 converted[4][4];\n'] + variables[3:]
        if placement:
            ordered = variables[:1] + outputs + variables[1:3] + ['    f32 converted[4][4];\n'] + variables[3:]
        body = body.replace('s32 count) {\n', 's32 count) {\n' + ''.join(ordered), 1)
        yield 'indexed-reuse%d-placement%d-order%d' % (reuse, placement, order), body


def pointer_phase_candidates():
    base = return_shape(route.SELECTED, 1)
    base = base.replace('    struct126 *lookup;\n', '')
    base = base.replace('lookup = func_1503195C(', 'input = (struct17 **)func_1503195C(')
    base = base.replace('if (lookup == 0)', 'if (input == 0)')
    base = base.replace('func_15031070(lookup, actor,', 'func_15031070((struct126 *)input, actor,')
    base = base.replace('(u8 *)lookup + 0x48', '(u8 *)input + 0x48')
    for reuse, first, lookup in itertools.product(range(2), range(2), range(3)):
        body = base
        if reuse == 0:
            body = body.replace('    u8 *attachment;\n', '')
            body = body.replace('attachment = *(u8 **)(descriptor + 0x48);', 'matrix = *(Mtx **)(descriptor + 0x48);')
            body = body.replace('if (attachment != 0)', 'if (matrix != 0)')
            body = body.replace('attachment[0x3F6]', '((u8 *)matrix)[0x3F6]')
            body = body.replace('attachment + 0x3E8', '(u8 *)matrix + 0x3E8')
        else:
            body = body.replace('    u8 *bank;\n', '')
            body = body.replace('(bank = (u8 *)actor->unk1D4)', '(matrix = (Mtx *)actor->unk1D4)')
            body = body.replace('bank + descriptor[2] * 64', '(u8 *)matrix + descriptor[2] * 64')
        body = lookup_shape(body, lookup)
        declarations = [line for line in body.splitlines(keepends=True) if line.startswith('    ')
            and line.rstrip().endswith(';') and not line.startswith('        ')][:8]
        assert len(declarations) == 8
        for declaration in declarations:
            body = body.replace(declaration, '', 1)
        variables = [line for line in declarations if line not in
            ('    f32 converted[4][4];\n', '    Mtx *lookupMatrix;\n', '    Mtx *other;\n')]
        if first:
            variables = variables[1:] + variables[:1]
        ordered = variables[:3] + ['    Mtx *lookupMatrix;\n', '    Mtx *other;\n',
            '    f32 converted[4][4];\n'] + variables[3:]
        body = body.replace('s32 count) {\n', 's32 count) {\n' + ''.join(ordered), 1)
        yield 'pointer-reuse%d-first%d-lookup%d' % (reuse, first, lookup), body


def output_phase_candidates():
    base = return_shape(route.SELECTED, 1)
    base = base.replace('    struct126 *lookup;\n', '').replace('    u8 *bank;\n', '')
    base = base.replace('(bank = (u8 *)actor->unk1D4)', '(outputs = (struct17 **)actor->unk1D4)')
    base = base.replace('bank + descriptor[2] * 64', '(u8 *)outputs + descriptor[2] * 64')
    base = base.replace('lookup = func_1503195C(', 'input = (struct17 **)func_1503195C(')
    base = base.replace('if (lookup == 0)', 'if (input == 0)')
    base = base.replace('func_15031070(lookup, actor,', 'func_15031070((struct126 *)input, actor,')
    base = base.replace('(u8 *)lookup + 0x48', '(u8 *)input + 0x48')
    declarations = ('    Mtx *matrix;\n', '    u8 *attachment;\n', '    struct17 **input;\n',
        '    Mtx *lookupMatrix;\n', '    Mtx *other;\n', '    f32 converted[4][4];\n',
        '    struct17 **outputs;\n', '    s32 i;\n')
    for declaration in declarations:
        base = base.replace(declaration, '')
    base = base.replace('s32 count) {\n', 's32 count) {\n' + ''.join(declarations), 1)
    for lookup, kind in itertools.product(range(3), ('fixed', 'bytes', 'address')):
        body = lookup_shape(base, lookup)
        if kind != 'fixed':
            raw = 'u8 *' if kind == 'bytes' else 'u32 '
            body = body.replace('Mtx *lookupMatrix;', raw + 'lookupMatrix;').replace('Mtx *other;', raw + 'other;')
            body = body.replace('&lookupMatrix, &other)', '(Mtx **)&lookupMatrix, (Mtx **)&other)')
            expression = 'lookupMatrix + *(u16 *)(descriptor + 0x20)'
            body = body.replace('matrix = ' + expression + ';',
                'matrix = (Mtx *)(lookupMatrix + (*(u16 *)(descriptor + 0x20) << 6));')
            body = body.replace('matrix = lookupMatrix;', 'matrix = (Mtx *)lookupMatrix;')
            body = body.replace('matrix += *(u16 *)(descriptor + 0x20);',
                'matrix = (Mtx *)((u8 *)matrix + (*(u16 *)(descriptor + 0x20) << 6));')
        yield 'output-lookup%d-kind%s' % (lookup, kind), body


SELECTED = dict(pointer_phase_candidates())['pointer-reuse1-first0-lookup0'].replace(
    '''        do {
            func_150A7960(converted, (*input)->unk0, (*input)->unk4, (*input)->unk8,
                &(*outputs)->unk0, &(*outputs)->unk4, &(*outputs)->unk8);
            input++;
            outputs++;
            i++;
        } while (i != count);
        return 1;''',
    '''            do {
                func_150A7960(converted, (*input)->unk0, (*input)->unk4, (*input)->unk8,
                    &(*outputs)->unk0, &(*outputs)->unk4, &(*outputs)->unk8);
                input++;
                outputs++;
                i++;
            } while (i != count);
            return 1;''')


def private_offsets(words):
    resolver = 0x0C000000 | route.SYMBOLS['func_15031070'] >> 2 & 0x3FFFFFF
    at = next(i for i, word in enumerate(words) if word == resolver)
    primary, secondary = words[at - 1], words[at + 1]
    assert primary & 0xFFFF0000 == 0x27A60000 and secondary & 0xFFFF0000 == 0x27A70000
    matrix = [word & 65535 for word in words if word & 0xFFFF0000 == 0x27B40000]
    assert len(matrix) == 1
    return dict(primary_offset=primary & 65535, secondary_offset=secondary & 65535, matrix_offset=matrix[0])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--storage', action='store_true')
    parser.add_argument('--parameters', action='store_true')
    parser.add_argument('--indexed', action='store_true')
    parser.add_argument('--pointers', action='store_true')
    parser.add_argument('--outputs', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-matrix-route-layout'
    records = []
    for name, body in output_phase_candidates() if args.outputs else pointer_phase_candidates() if args.pointers else indexed_candidates() if args.indexed else parameter_candidates() if args.parameters else storage_candidates() if args.storage else topology_candidates():
        record, words = route.compile_candidate(root, out, name, body)
        record.update(private_offsets(words))
        record['debug'] = debug_locals(out / (name + '.o'))
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'],
            [hex(record[key]) for key in ('matrix_offset', 'primary_offset', 'secondary_offset')], flush=True)
    (out / ('outputs.json' if args.outputs else 'pointers.json' if args.pointers else 'indexed.json' if args.indexed else 'parameters.json' if args.parameters else 'storage.json' if args.storage else 'topology.json')).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
