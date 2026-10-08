"""Recover the actor-group/key lookup and its matching-node ordinal."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x1503195C, 0x5EE0C, 28
FUNCTION = 'func_1503195C'
HEAD = 0x800C3EE0
BASELINE = '''s32 func_1503195C(u8 *actor, s32 key, u32 ordinal) {
    u32 group = actor[0x3B];
    u8 *current;
    u8 *next;

    if (group == 0) {
        return 0;
    }
    current = D_800C3EE0;
    if (current != 0) {
        do {
            next = *(u8 **)(current + 0x54);
            if (group == current[0]) {
                if (key == current[6]) {
                    if (ordinal-- == 0) {
                        return (s32)current;
                    }
                }
            }
            current = next;
        } while (current != 0);
    }
    return 0;
}'''


def candidates():
    for group, ordinal, decrement, conditions in itertools.product(
            ('u32', 's32', 'u8'), ('u32', 's32'), ('post', 'separate'), ('nested', 'combined')):
        body = BASELINE.replace('u32 group =', group+' group =').replace('u32 ordinal)', ordinal+' ordinal)')
        if decrement == 'separate':
            body = body.replace('if (ordinal-- == 0)', 'if (ordinal == 0)').replace(
                '                        return (s32)current;\n                    }',
                '                        return (s32)current;\n                    }\n                    ordinal--;')
        if conditions == 'combined':
            body = body.replace('if (group == current[0]) {\n                if (key == current[6]) {',
                'if (group == current[0] && key == current[6]) {').replace(
                '                }\n            }\n            current = next;',
                '            }\n            current = next;')
        yield '%s-%s-%s-%s' % (group, ordinal, decrement, conditions), body
    for loop, condition, post in itertools.product(('current', 'next', 'while'), ('continue', 'goto'), (False, True)):
        body = BASELINE.split('            if (group == current[0]) {', 1)[0]
        update = 'current = next;\n                continue;' if condition == 'continue' else 'goto advance;'
        body += '''            if (group != current[0]) {
                %s
            }
            if (key != current[6]) {
                %s
            }
            if (%s) {
                return (s32)current;
            }
            %s
            %scurrent = next;
        } while (%s != 0);
    }
    return 0;
}''' % (update, update, 'ordinal-- == 0' if post else 'ordinal == 0',
            '' if post else 'ordinal--;', 'advance:\n            ' if condition == 'goto' else '',
            'next' if loop == 'next' else 'current')
        if loop == 'while':
            body = body.replace('    if (current != 0) {\n        do {', '    while (current != 0) {')
            body = body.replace('        } while (current != 0);\n    }', '    }')
        yield 'flow-%s-%s-post%d' % (loop, condition, post), body
    for advance, inverse, formal in itertools.product(('common', 'matching', 'each'), (False, True), (False, True)):
        body = BASELINE.replace('if (ordinal-- == 0)', 'if (ordinal == 0)').replace(
            '                        return (s32)current;\n                    }',
            '                        return (s32)current;\n                    }\n                    ordinal--;')
        if inverse:
            body = body.replace('''                    if (ordinal == 0) {
                        return (s32)current;
                    }
                    ordinal--;''', '''                    if (ordinal != 0) {
                        ordinal--;
                    } else {
                        return (s32)current;
                    }''')
        if advance == 'matching':
            body = body.replace('                }\n            }\n            current = next;',
                '                    current = next;\n                }\n            }\n            current = next;')
        elif advance == 'each':
            body = body.replace('                }\n            }\n            current = next;',
                '                    current = next;\n                } else {\n                    current = next;\n                }\n'
                '            } else {\n                current = next;\n            }')
        if formal:
            body = body.replace('    u8 *next;\n', '').replace('next =', 'actor =').replace('current = next', 'current = actor')
        yield 'advance-%s-inverse%d-formal%d' % (advance, inverse, formal), body
    for inverse, separate_advance in itertools.product((False, True), (False, True)):
        body = BASELINE.split('            if (group == current[0]) {', 1)[0]
        decision = '''                if (ordinal != 0) {
                    ordinal--;
                } else {
                    return (s32)current;
                }''' if inverse else '''                if (ordinal == 0) {
                    return (s32)current;
                }
                ordinal--;'''
        body += '            if (group == current[0] && key == current[6]) {\n'+decision
        if separate_advance:
            body += '\n                current = next;\n            } else {\n                current = next;\n            }\n'
        else:
            body += '\n            }\n            current = next;\n'
        body += '        } while (current != 0);\n    }\n    return 0;\n}'
        yield 'combined-inverse%d-advance%d' % (inverse, separate_advance), body


SELECTED = dict(candidates())['combined-inverse1-advance1']


def compile_candidate(root, out, name, body=SELECTED, profile='o2g3'):
    out.mkdir(exist_ok=True)
    source, obj, elf = (out / (name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\nextern u8 *D_800C3EE0;\n'+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))],
        cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = out / 'parent-lookup.ld'
    script.write_text('SECTIONS { .text 0x1503195C : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        '--defsym=D_800C3EE0=0x800C3EE0', '-o', str(elf), str(obj)], check=True, capture_output=True)
    _, functions, relocs = parse_object(obj)
    meta, pools = functions[FUNCTION], sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size']//4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>28I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word)&65535 for word in words if word&0xFFFF0000 == 0x27BD0000 and word&0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        diagnostics=diagnostics, relocations=relocs, pool_bytes=len(pools.get('.rodata', (0, b''))[1])), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profiles', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-matrix-parent-lookup'
    records = []
    forms = [(name, body, 'o2g3') for name, body in candidates()]
    if args.profiles:
        bodies = dict(candidates())
        forms = [(name+'-'+profile, bodies[name], profile)
            for name, profile in itertools.product(('u32-u32-separate-nested', 'flow-current-continue-post0'), PROFILES)]
    for name, body, profile in forms:
        record, _ = compile_candidate(root, out, name, body, profile)
        records.append(record)
        print(name, record['body_words'], record['frame'], record['differences'], flush=True)
    (out / ('profiles.json' if args.profiles else 'measurements.json')).write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
