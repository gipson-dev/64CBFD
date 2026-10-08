"""Screen the resolver's key/parent/result phases without inserting instructions."""

import argparse
import itertools
import json
from pathlib import Path

from tools.experiments import game_matrix_pair_resolver_candidates as pair


def result_candidates():
    for scalar, reuse, common, register in itertools.product(('s32', 'u32'), ('parent', 'child', 'both'),
            (False, True), (False, True)):
        body = pair.SELECTED.replace('    u8 *parent;', '    u8 *parent;\n    %s%s value;' %
            ('register ' if register else '', scalar))
        body = body.replace('} else if (*(u16 *)(node + 0x1E) != 0)',
            '} else if ((value = *(u16 *)(node + 0x1E)) != 0)')
        body = body.replace('actor, *(u16 *)(node + 0x1E), 0)', 'actor, value, 0)')
        if reuse in ('parent', 'both'):
            body = body.replace('    u8 *parent;\n', '')
            body = body.replace('parent = (u8 *)func_1503195C', 'value = func_1503195C')
            body = body.replace('if (parent == 0)', 'if (value == 0)')
            body = body.replace('func_15031070(parent,', 'func_15031070((u8 *)value,')
        if reuse in ('child', 'both'):
            body = body.replace('if (func_15031070(', 'if ((value = func_15031070(')
            body = body.replace('primary, secondary) == 0)', 'primary, secondary)) == 0)')
        if common:
            body = body.replace('        return 1;\n    } else {', '    } else {', 1)
        yield 'result-%s-%s-common%d-register%d' % (scalar, reuse, common, register), body


def pointer_candidates():
    for carrier, key, common in itertools.product(('attachment', 'parent', 'node'),
            (False, True), (False, True)):
        body = pair.SELECTED
        if carrier == 'attachment':
            body = body.replace('    u8 *parent;\n', '').replace('parent = ', 'attachment = ')
            body = body.replace('if (parent == 0)', 'if (attachment == 0)')
            body = body.replace('func_15031070(parent,', 'func_15031070(attachment,')
        elif carrier == 'node':
            body = body.replace('    u8 *parent;', '    u8 *current = node;')
            body = body.replace('parent = ', 'node = ').replace('if (parent == 0)', 'if (node == 0)')
            body = body.replace('func_15031070(parent,', 'func_15031070(node,')
            body = body.replace('*(u16 *)(node + 0x20)', '*(u16 *)(current + 0x20)')
            body = body.replace('node[2]', 'current[2]')
        if key:
            name = carrier
            body = body.replace('} else if (*(u16 *)(node + 0x1E) != 0)',
                '} else if ((%s = (u8 *)(u32)*(u16 *)(node + 0x1E)) != 0)' % name)
            body = body.replace('actor, *(u16 *)(node + 0x1E), 0)', 'actor, (u32)%s, 0)' % name)
        if common:
            body = body.replace('        return 1;\n    } else {', '    } else {', 1)
        yield 'pointer-%s-key%d-common%d' % (carrier, key, common), body


NODE_VIEW = '''typedef struct {
    u8 pad0[2];
    u8 slot;
    u8 pad3[0x1B];
    u16 key;
    u16 offset;
    u8 pad22[0x12];
    Mtx *bank;
    u8 pad38[0x10];
    u8 *attachment;
} MatrixPairNode;
'''


def node_candidates():
    for kind, key, common in itertools.product(('local', 'formal'), (False, True), (False, True)):
        body = pair.SELECTED
        if kind == 'formal':
            body = body.replace('u8 *node,', 'MatrixPairNode *node,', 1)
            body = body.replace('u8 *parent;', 'MatrixPairNode *parent;')
            body = body.replace('(u8 *)func_1503195C', '(MatrixPairNode *)func_1503195C')
            name = 'node'
        else:
            body = body.replace('    u8 *parent;', '    u8 *parent;\n    MatrixPairNode *current = (MatrixPairNode *)node;')
            name = 'current'
        for expression, field in (('*(u8 **)(node + 0x48)', 'attachment'),
                ('*(u8 **)(node + 0x34)', 'bank'), ('*(Mtx **)(node + 0x34)', 'bank'),
                ('*(u16 *)(node + 0x1E)', 'key'), ('*(u16 *)(node + 0x20)', 'offset'), ('node[2]', 'slot')):
            body = body.replace(expression, name+'->'+field)
        if key:
            body = body.replace('    u8 *attachment;', '    u8 *attachment;\n    u32 key;')
            body = body.replace('} else if (%s->key != 0)' % name, '} else if ((key = %s->key) != 0)' % name)
            body = body.replace('actor, %s->key, 0)' % name, 'actor, key, 0)')
        if common:
            body = body.replace('        return 1;\n    } else {', '    } else {', 1)
        yield 'node-%s-key%d-common%d' % (kind, key, common), NODE_VIEW+body


def declarations():
    for key in ('s32', 'u32', 'u16'):
        yield 'declaration-key-'+key, pair.SELECTED, 's32 func_1503195C(u8 *, %s, s32);' % key
    yield 'declaration-pointer', pair.SELECTED, 'u8 *func_1503195C(u8 *, s32, s32);'


def flow_candidates():
    prefix, rest = pair.SELECTED.split('    } else if (*(u16 *)(node + 0x1E) != 0) {\n', 1)
    keyed, rest = rest.split('    } else {\n', 1)
    fallback, ending = rest.split('    }\n    return 1;', 1)
    for common, returns, key in itertools.product((False, True), ('early', 'goto', 'comma', 'logical'), (False, True)):
        before, selection, branch = prefix, '*(u16 *)(node + 0x1E)', keyed
        if key:
            before = before.replace('    u8 *parent;', '    u8 *parent;\n    u32 key;')
            selection = '(key = *(u16 *)(node + 0x1E))'
            branch = branch.replace('actor, *(u16 *)(node + 0x1E), 0)', 'actor, key, 0)')
        if common:
            before = before.replace('    } else if (*(u8 **)(node + 0x34) != 0) {',
                '        return 1;\n    }\n    if (*(u8 **)(node + 0x34) != 0) {')
            before += '        return 1;\n    }\n'
        else:
            before += '    } else {\n'
        if returns == 'early':
            tail = '        if (%s != 0) {\n' % selection + branch + '        }\n' + fallback
        elif returns == 'goto':
            tail = '        if (%s == 0) { goto fallback; }\n' % selection + branch + 'fallback:\n' + fallback
        else:
            lookup_key = 'key' if key else '*(u16 *)(node + 0x1E)'
            lookup = 'parent = (u8 *)func_1503195C(actor, %s, 0)' % lookup_key
            recursive = 'func_15031070(parent, actor, primary, secondary)'
            adjust = '(*primary += *(u16 *)(node + 0x20), 1)'
            zero = '(*primary = *(Mtx **)(actor + 0x1D4), *primary += node[2], *secondary = *primary, 1)'
            positive = '((%s) != 0 && %s != 0 && %s)' % (lookup, recursive, adjust) if returns == 'logical' else (
                '(%s, parent != 0 ? (%s != 0 ? %s : 0) : 0)' % (lookup, recursive, adjust))
            tail = '        return %s != 0 ? %s : %s;\n' % (selection, positive, zero)
        body = before + tail + ('    return 1;' + ending if common else '    }\n    return 1;' + ending)
        yield 'flow-common%d-%s-key%d' % (common, returns, key), body
    for key, order in itertools.product((False, True), range(2)):
        before, selection, branch = prefix, '*(u16 *)(node + 0x1E)', keyed
        if key:
            before = before.replace('    u8 *parent;', '    u8 *parent;\n    u32 key;')
            selection = '(key = *(u16 *)(node + 0x1E))'
            branch = branch.replace('actor, *(u16 *)(node + 0x1E), 0)', 'actor, key, 0)')
        branch = branch.replace('        return 1;\n', '        break;\n')
        zero = '        case 0:\n' + fallback + '        break;\n'
        positive = '        default:\n' + branch
        body = before + '    } else {\n        switch (%s) {\n' % selection
        body += zero+positive if order else positive+zero
        body += '        }\n    }\n    return 1;' + ending
        yield 'switch-common-key%d-order%d' % (key, order), body


def actor_candidates():
    for location, scalar in itertools.product(('entry', 'key'), ('u8 *', 'void *', 'const u8 *', 'u32')):
        body = pair.SELECTED
        value = '(u32)actor' if scalar == 'u32' else 'actor'
        declaration = '    %s lookupActor%s;' % (scalar, ' = '+value if location == 'entry' else '')
        body = body.replace('    u8 *parent;', '    u8 *parent;\n'+declaration)
        if location == 'key':
            body = body.replace('} else if (*(u16 *)(node + 0x1E) != 0)',
                '} else if ((lookupActor = %s, *(u16 *)(node + 0x1E)) != 0)' % value)
        body = body.replace('func_1503195C(actor,', 'func_1503195C(lookupActor,')
        yield 'actor-%s-%s' % (location, scalar.replace(' ', '').replace('*', 'pointer')), body
    for typed in (False, True):
        body = NODE_SELECTED if typed else pair.SELECTED
        assignment, following = body.split('        parent = ', 1)
        call, ending = following.split(';\n        if (parent == 0)', 1)
        yield 'parent-condition-typed%d' % typed, assignment+'        if ((parent = '+call+') == 0)'+ending
        body = body.replace('    u8 *parent;\n', '')
        position = '    } else if ((key = current->key) != 0) {\n' if typed else (
            '    } else if (*(u16 *)(node + 0x1E) != 0) {\n')
        body = body.replace(position, position+'        u8 *parent;\n')
        yield 'parent-inner-scope-typed%d' % typed, body


def bank_candidates():
    expression = '*(Mtx **)(actor + 0x1D4) + node[2]'
    forms = dict(integer_first='node[2] + *(Mtx **)(actor + 0x1D4)',
        indexed='&(*(Mtx **)(actor + 0x1D4))[node[2]]',
        bytes='(Mtx *)((u8 *)*(Mtx **)(actor + 0x1D4) + (node[2] << 6))',
        bytes_integer_first='(Mtx *)((node[2] << 6) + (u8 *)*(Mtx **)(actor + 0x1D4))',
        address='(Mtx *)((u32)*(Mtx **)(actor + 0x1D4) + (node[2] << 6))',
        address_integer_first='(Mtx *)((node[2] << 6) + (u32)*(Mtx **)(actor + 0x1D4))')
    for name, replacement in forms.items():
        yield 'bank-'+name, pair.SELECTED.replace(expression, replacement)


def candidates():
    for group in (result_candidates, pointer_candidates, node_candidates, flow_candidates, actor_candidates, bank_candidates):
        for name, body in group():
            yield name, body, 's32 func_1503195C();'
    yield from declarations()


NODE_SELECTED = dict(node_candidates())['node-local-key1-common0']
SELECTED = dict(bank_candidates())['bank-integer_first']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-matrix-pair-key'
    records = []
    for name, body, declaration in candidates():
        record, _ = pair.compile_candidate(root, out, name, body, lookup_declaration=declaration)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (out / 'measurements.json').write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
