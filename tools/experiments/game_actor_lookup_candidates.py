"""Recover the actor lookup's original nested exits under the owner profile."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS, FUNCTION = 0x15142444, 0x16F8F4, 44, 'func_15142444'
SYMBOLS = {'func_15083E90': 0x15083E90}
PROTOTYPE = 'void *func_15142444(u8 arg0, u8 *arg1);'
LEGACY_DECLARATIONS = 'extern u8 *func_15083E90(s32);\n'
DECLARATIONS = 'extern u8 *func_15083E90(u8);\n'
BASELINE = '''void *func_15142444(u8 arg0, u8 *arg1) {
    u8 *found;

    if (arg0 == 0xFF) {
        if (*(s32 *)(arg1 + 0x1D4) != 0) {
            return arg1;
        }
        return NULL;
    }

    if ((arg1 != NULL) && (*(s32 *)arg1 != 0) && (arg0 == arg1[0x3B])) {
        if (*(s32 *)(arg1 + 0x1D4) != 0) {
            return arg1;
        }
        return NULL;
    }

    found = (u8 *)func_15083E90(arg0);
    if (found == NULL) {
        return NULL;
    }
    if (*(s32 *)(found + 0x1D4) == 0) {
        return NULL;
    }
    return found;
}'''


def body_for(outer=False, nested=0, reuse=False):
    body = BASELINE
    if nested:
        begin = body.index('    if (found == NULL)')
        if nested == 1:
            tail = '''    if (found != NULL && *(s32 *)(found + 0x1D4) != 0) {
        return found;
    }
    return NULL;
}'''
        elif nested == 2:
            tail = '''    if (found != NULL) {
        if (*(s32 *)(found + 0x1D4) != 0) {
            return found;
        } else {
            return NULL;
        }
    } else {
        return NULL;
    }
    return NULL;
}'''
        else:
            tail = '''    if (found != NULL) {
        if (*(s32 *)(found + 0x1D4) != 0) {
            return found;
        }
    }
    return NULL;
}'''
        body = body[:begin] + tail
    if outer:
        body = body.replace('    }\n\n    if ((arg1', '    } else if ((arg1')
        body = body.replace('    }\n\n    found =', '    } else {\n    found =')
        body = body.removesuffix('\n}') + '\n    }\n}'
    if reuse:
        body = body.replace('    u8 *found;\n', '').replace('found', 'arg1')
    return body


def candidates():
    for outer, nested, reuse in itertools.product((False, True), range(4), (False, True)):
        yield 'outer%d-nested%d-reuse%d' % (outer, nested, reuse), body_for(outer, nested, reuse)
    for kind, expression in itertools.product(('u8', 's32', 'u32'), (False, True)):
        body = body_for(nested=3)
        body = body.replace('    u8 *found;', '    u8 *found;\n    %s slot;' % kind)
        body = body.replace('    if (arg0 ==', '    slot = arg0;\n    if (slot ==')
        body = body.replace('(arg0 == arg1', '(slot == arg1').replace('func_15083E90(arg0)', 'func_15083E90(slot)')
        if expression:
            body = body.replace('    slot = arg0;\n    if (slot ==', '    if ((slot = arg0) ==')
        yield 'slot-%s-expression%d' % (kind, expression), body
    for scope in (False, True):
        body = body_for(outer=True, nested=3)
        if scope:
            body = body.replace('    u8 *found;\n', '').replace('    } else {\n    found =',
                '    } else {\n    u8 *found;\n    found =')
        yield 'found-scope%d' % scope, body
    yield 'return-u8ptr', body_for(nested=3).replace('void *func_15142444', 'u8 *func_15142444')
    for kind, test in itertools.product(('u8', 's32', 'u32'), (False, True)):
        body = body_for(nested=3).replace('    u8 *found;', '    u8 *found;\n    %s slot;' % kind)
        body = body.replace('    if (arg0 ==', '    slot = arg0;\n    if (arg0 ==')
        body = body.replace('(arg0 == arg1', '(slot == arg1')
        if test:
            body = body.replace('if (arg0 == 0xFF)', 'if (slot == 0xFF)')
        yield 'compare-slot-%s-test%d' % (kind, test), body


SELECTED = body_for(nested=3)


def compile_candidate(root, out, name, body=SELECTED, profile='o2g3', declarations=DECLARATIONS):
    source, obj, elf = (out / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n' + declarations + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn',
        '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root,
        capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = out / 'lookup.ld'
    script.write_text('SECTIONS { .text 0x15142444 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, relocations = parse_object(obj)
    target = functions[FUNCTION]
    pools = sections(elf)
    words = list(struct.unpack_from('>%dI' % (target['size'] // 4), pools['.text'][1], target['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>44I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    return dict(name=name, profile=profile, body_words=end, frame=(-words[0]) & 65535,
        diagnostics=diagnostics, relocations=relocations,
        pool_bytes=len(pools.get('.rodata', (0, b''))[1]),
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0))), words


def main():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-actor-lookup'
    out.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for abi, declaration in (('legacy-word', LEGACY_DECLARATIONS), ('retail-byte', DECLARATIONS)):
            record, _ = compile_candidate(root, out, name + '-' + abi, body, declarations=declaration)
            record['lookup_abi'] = abi
            records.append(record)
            print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
