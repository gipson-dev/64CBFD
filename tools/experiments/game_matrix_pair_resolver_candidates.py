"""Recover the four matrix-pair routes and recursive output/readback order."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15031070, 0x5E520, 85
FUNCTION = 'func_15031070'
SYMBOLS = dict(D_800BE9C0=0x800BE9C0, func_1503195C=0x1503195C)
PROTOTYPE = 's32 func_15031070(u8 *node, u8 *actor, Mtx **primary, Mtx **secondary);'
BASELINE = '''s32 func_15031070(u8 *node, u8 *actor, u8 **primary, u8 **secondary) {
    u8 *attachment;
    u8 *parent;

    attachment = *(u8 **)(node + 0x48);
    if (attachment != 0) {
        if (attachment[0x3F6] == 0) {
            return 0;
        }
        *primary = ((u8 **)(attachment + 0x3E8))[D_800BE9C0];
        *secondary = ((u8 **)(*(u8 **)(node + 0x48) + 0x3E0))[D_800BE9C0];
    } else if (*(u8 **)(node + 0x34) != 0) {
        *primary = *(u8 **)(node + 0x34) + D_800BE9C0 * 64;
        *secondary = *(u8 **)(actor + 0x1D4) + node[2] * 64;
    } else if (*(u16 *)(node + 0x1E) != 0) {
        parent = (u8 *)func_1503195C(actor, *(u16 *)(node + 0x1E), 0);
        if (parent == 0) {
            return 0;
        }
        if (func_15031070(parent, actor, primary, secondary) == 0) {
            return 0;
        }
        *primary += *(u16 *)(node + 0x20) * 64;
        return 1;
    } else {
        *primary = *(u8 **)(actor + 0x1D4);
        *primary += node[2] * 64;
        *secondary = *primary;
    }
    return 1;
}'''


def candidates():
    for registers, key, base, repeated in itertools.product(range(4), (False, True), (False, True), (False, True)):
        body = BASELINE
        if registers & 1:
            body = body.replace('u8 *node,', 'register u8 *node,', 1)
        if registers & 2:
            body = body.replace('u8 **primary,', 'register u8 **primary,', 1)
        if key:
            body = body.replace('    u8 *parent;', '    u8 *parent;\n    u32 key;')
            body = body.replace('} else if (*(u16 *)(node + 0x1E) != 0)',
                '} else if ((key = *(u16 *)(node + 0x1E)) != 0)')
            body = body.replace('actor, *(u16 *)(node + 0x1E), 0)', 'actor, key, 0)')
        if base:
            body = body.replace('    u8 *parent;', '    u8 *parent;\n    u8 *bank;')
            body = body.replace('} else if (*(u8 **)(node + 0x34) != 0)',
                '} else if ((bank = *(u8 **)(node + 0x34)) != 0)')
            body = body.replace('*primary = *(u8 **)(node + 0x34) +', '*primary = bank +')
        if not repeated:
            body = body.replace('((u8 **)(*(u8 **)(node + 0x48) + 0x3E0))',
                '((u8 **)(attachment + 0x3E0))')
        yield 'register%d-key%d-bank%d-reread%d' % (registers, key, base, repeated), body


def lifetime_candidates():
    for matrices, carrier, returns in itertools.product((False, True), ('repeat', 'route', 'parent'), range(2)):
        body = BASELINE
        if matrices:
            body = body.replace('u8 **primary, u8 **secondary', 'Mtx **primary, Mtx **secondary')
            body = body.replace('((u8 **)(attachment + 0x3E8))', '((Mtx **)(attachment + 0x3E8))')
            body = body.replace('((u8 **)(*(u8 **)(node + 0x48) + 0x3E0))',
                '((Mtx **)(*(u8 **)(node + 0x48) + 0x3E0))')
            body = body.replace('*(u8 **)(node + 0x34) + D_800BE9C0 * 64',
                '*(Mtx **)(node + 0x34) + D_800BE9C0')
            body = body.replace('*(u8 **)(actor + 0x1D4) + node[2] * 64',
                '*(Mtx **)(actor + 0x1D4) + node[2]')
            body = body.replace('*primary = *(u8 **)(actor + 0x1D4)', '*primary = *(Mtx **)(actor + 0x1D4)')
            body = body.replace('*primary += *(u16 *)(node + 0x20) * 64;', '*primary += *(u16 *)(node + 0x20);')
            body = body.replace('*primary += node[2] * 64;', '*primary += node[2];')
        if carrier == 'route':
            body = body.replace('    u8 *attachment;', '    u32 routeValue;')
            body = body.replace('attachment = *(u8 **)(node + 0x48);', 'routeValue = *(u32 *)(node + 0x48);')
            body = body.replace('if (attachment != 0)', 'if (routeValue != 0)')
            body = body.replace('attachment[0x3F6]', '((u8 *)routeValue)[0x3F6]')
            body = body.replace('attachment + 0x3E8', '(u8 *)routeValue + 0x3E8')
            body = body.replace('} else if (*(u16 *)(node + 0x1E) != 0)',
                '} else if ((routeValue = *(u16 *)(node + 0x1E)) != 0)')
            body = body.replace('actor, *(u16 *)(node + 0x1E), 0)', 'actor, routeValue, 0)')
        elif carrier == 'parent':
            body = body.replace('} else if (*(u16 *)(node + 0x1E) != 0)',
                '} else if ((parent = (u8 *)(u32)*(u16 *)(node + 0x1E)) != 0)')
            body = body.replace('actor, *(u16 *)(node + 0x1E), 0)', 'actor, (u32)parent, 0)')
        if returns:
            body = body.replace('        return 1;\n    } else {', '    } else {', 1)
        yield 'lifetime-matrices%d-carrier%s-return%d' % (matrices, carrier, returns), body


def branch_candidates():
    prefix, rest = BASELINE.split('    } else if (*(u16 *)(node + 0x1E) != 0) {\n', 1)
    keyed, rest = rest.split('    } else {\n', 1)
    fallback, ending = rest.split('    }\n    return 1;', 1)
    for order, local, typed in itertools.product(range(2), ('repeat', 's32', 'u32', 'u16'), (False, True)):
        before = prefix
        selection, call = '*(u16 *)(node + 0x1E)', keyed
        if local != 'repeat':
            before = before.replace('    u8 *parent;', '    u8 *parent;\n    %s key;' % local)
            selection = '(key = *(u16 *)(node + 0x1E))'
            call = keyed.replace('actor, *(u16 *)(node + 0x1E), 0)', 'actor, key, 0)')
        body = before + '    } else {\n        switch (%s) {\n' % selection
        default_case, zero_case = '        default:\n' + call, '        case 0:\n' + fallback + '        break;\n'
        body += (default_case + zero_case if not order else zero_case + default_case)
        body += '        }\n    }\n    return 1;' + ending
        if typed:
            body = body.replace('    u8 *parent;', '    u8 *parent;\n    s32 func_1503195C(u8 *, s32, s32);')
        yield 'switch-order%d-key%s-prototype%d' % (order, local, typed), body


def flow_candidates():
    prefix, rest = BASELINE.split('    } else if (*(u16 *)(node + 0x1E) != 0) {\n', 1)
    keyed, rest = rest.split('    } else {\n', 1)
    fallback, ending = rest.split('    }\n    return 1;', 1)
    for selector in ('switch', 'if', 'boolean'):
        body = prefix + '    } else {\n'
        if selector == 'switch':
            body += '        switch (*(u16 *)(node + 0x1E)) {\n        case 0: goto fallback;\n        default: break;\n        }\n'
        elif selector == 'boolean':
            body += '        switch (*(u16 *)(node + 0x1E) != 0) {\n        case 0: goto fallback;\n        default: break;\n        }\n'
        else:
            body += '        if (*(u16 *)(node + 0x1E) == 0) { goto fallback; }\n'
        body += keyed + 'fallback:\n' + fallback + '    }\n    return 1;' + ending
        yield 'flow-' + selector, body
    for binding in ('parent', 'local'):
        body = BASELINE
        name = 'parent' if binding == 'parent' else 'lookupActor'
        if binding == 'local':
            body = body.replace('    u8 *parent;', '    u8 *parent;\n    u8 *lookupActor;')
        body = body.replace('} else if (*(u16 *)(node + 0x1E) != 0)',
            '} else if ((%s = actor, *(u16 *)(node + 0x1E)) != 0)' % name)
        body = body.replace('func_1503195C(actor,', 'func_1503195C(%s,' % name)
        yield 'flow-actor-' + binding, body


SELECTED = dict(lifetime_candidates())['lifetime-matrices1-carrierrepeat-return0']


def compile_candidate(root, out, name, body=BASELINE, profile='o2g3', lookup_declaration='s32 func_1503195C();'):
    out.mkdir(exist_ok=True)
    source, obj, elf = (out / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\nextern u8 D_800BE9C0;\n' + lookup_declaration + '\n' + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, text=True, capture_output=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = out / 'matrix-pair.ld'
    script.write_text('SECTIONS { .text 0x15031070 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, relocs = parse_object(obj)
    meta, pools = functions[FUNCTION], sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size']//4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>85I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        relocations=relocs, diagnostics=diagnostics, pool_bytes=len(pools.get('.rodata', (0, b''))[1])), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--lifetimes', action='store_true')
    group.add_argument('--profiles', action='store_true')
    group.add_argument('--branches', action='store_true')
    group.add_argument('--flow', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-matrix-pair-resolver'
    records = []
    forms = [(name, body, 'o2g3') for name, body in flow_candidates()] if args.flow else (
        [(name, body, 'o2g3') for name, body in branch_candidates()] if args.branches else (
        [(name, body, 'o2g3') for name, body in lifetime_candidates()] if args.lifetimes else (
        [('profile-' + profile, BASELINE, profile) for profile in PROFILES] if args.profiles else
        [(name, body, 'o2g3') for name, body in candidates()])))
    for name, body, profile in forms:
        record, _ = compile_candidate(root, out, name, body, profile)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (out / ('flow.json' if args.flow else 'branches.json' if args.branches else 'lifetimes.json' if args.lifetimes else 'profiles.json' if args.profiles else 'measurements.json')).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
