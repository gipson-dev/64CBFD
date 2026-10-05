"""25-actor SDK display-list traversal with mode gates and live callback reads."""

import itertools
import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


DECLARATIONS = '''typedef struct ActorDisplay58F80 {
    s32 active;
    u8 id;
    u8 state;
    u8 pad6[0x17E];
    u32 flags;
    u8 pad188[0x1A4];
} ActorDisplay58F80;

extern ActorDisplay58F80 D_800CC2D0[26];
extern Gfx D_80084160[], D_80084190[];
extern s32 D_8003C8E0;
s32 func_1506196C(ActorDisplay58F80 *actor, s32 view);
Gfx *func_1502C408();
Gfx *func_1502C974();
Gfx *func_150368C4(Gfx *commands, s32 slot, s32 view);
Gfx *func_15030E08(Gfx *commands, s32 view, s32 mode);
'''

BASELINE = '''Gfx *func_1502BAD0(Gfx *commands, s32 mode, s16 view) {
    ActorDisplay58F80 *actor;
    s32 slot;
    u8 state;

    gSPDisplayList(commands++, D_80084160);
    actor = D_800CC2D0;
    for (slot = 0; slot != 25; slot++, actor++) {
        D_8003C8E0 = (slot & 0xFFFFFF) | 0x1000000;
        if (actor->active == 0) {
            continue;
        }
        state = actor->state;
        if (state == 3 || state == 5) {
            continue;
        }
        if (state == 2) {
            if (mode != 2) {
                continue;
            }
        } else if (actor->id == 255) {
            continue;
        }
        if (mode == 6) {
            if (state != 7) {
                continue;
            }
        } else if (mode == 0) {
            if (((actor->flags >> 9) & 1) == 0) {
                continue;
            }
        } else if (mode == 1) {
            if (state == 7 || state == 1) {
                continue;
            }
            if (state == 0 && func_1506196C(actor, view) < 255) {
                continue;
            }
        } else if (mode == 2) {
            if (state != 2) {
                if (state == 7 || (state != 0 && state != 1)) {
                    continue;
                }
                if (state == 0 && func_1506196C(actor, view) == 255) {
                    continue;
                }
            }
        }
        if (actor->state == 2) {
            commands = func_1502C408(commands, slot);
        } else {
            commands = func_1502C974(commands, slot, view, mode, 0);
            if (slot == 0) {
                commands = func_150368C4(commands, slot, view);
            }
        }
    }
    D_8003C8E0 = 0x1FFFFFF;
    if (mode == 1) {
        commands = func_15030E08(commands, view, 0);
    } else if (mode == 2) {
        commands = func_15030E08(commands, view, 1);
    } else if (mode == 6) {
        commands = func_15030E08(commands, view, 2);
    }
    gSPDisplayList(commands++, D_80084190);
    D_8003C8E0 = 0;
    return commands;
}'''

PLACEHOLDER = '''s32 func_1502BAD0() {
    return 0;
}'''


def candidates():
    forms = [('baseline', BASELINE), ('placeholder', PLACEHOLDER)]
    declarations = '    ActorDisplay58F80 *actor;\n    s32 slot;\n    u8 state;'
    for index, order in enumerate(itertools.permutations(declarations.splitlines())):
        forms.append(('layout-' + str(index), BASELINE.replace(declarations, '\n'.join(order))))
    for name, before, after in (
            ('word-state', '    u8 state;', '    u32 state;'),
            ('signed-state', '    u8 state;', '    s32 state;'),
            ('register-actor', '    ActorDisplay58F80 *actor;', '    register ActorDisplay58F80 *actor;'),
            ('register-slot', '    s32 slot;', '    register s32 slot;'),
            ('count-less', 'slot != 25', 'slot < 25'),
            ('pointer-first-update', 'slot++, actor++', 'actor++, slot++'),
            ('bit-mask', '((actor->flags >> 9) & 1)', '(actor->flags & 0x200)'),
            ('unsigned-alpha', 'func_1506196C(actor, view) < 255', '(u32)func_1506196C(actor, view) < 255')):
        forms.append((name, BASELINE.replace(before, after)))
    selected = dict(forms)['signed-state']
    forms.append(('selected-active-state', selected.replace('        if (actor->active == 0) {',
                 '        state = actor->active;\n        if (state == 0) {')))
    reversed_state = re.sub(r'(?<!->)\bstate (==|!=) (1|2|7)\b',
                            lambda m: m[2] + ' ' + m[1] + ' state', selected)
    forms.append(('selected-constant-first', reversed_state))
    forms.append(('selected-active-constant-first', reversed_state.replace('        if (actor->active == 0) {',
                 '        state = actor->active;\n        if (state == 0) {')))
    for index, order in enumerate(itertools.permutations(('    ActorDisplay58F80 *actor;', '    s32 slot;', '    s32 state;'))):
        forms.append(('selected-layout-' + str(index), selected.replace(declarations.replace('u8 state', 's32 state'), '\n'.join(order))))
    active = dict(forms)['selected-active-state']
    forms.append(('selected-one-first', active.replace('state == 7 || state == 1', 'state == 1 || state == 7')))
    forms.append(('selected-constant-locals', active.replace('    s32 state;',
        '    s32 state;\n    s32 one = 1;\n    s32 seven = 7;').replace('state == 7', 'state == seven')
        .replace('state != 7', 'state != seven').replace('state == 1', 'state == one')
        .replace('state != 1', 'state != one').replace('mode == 1', 'mode == one')))
    forms.append(('selected-mode-one-first', active.replace(
        'if (mode == 6) {\n            if (state != 7) {\n                continue;\n            }\n        } else if (mode == 0) {',
        'if (mode == 0) {').replace('        if (actor->state == 2) {',
        '        if (mode == 6 && state != 7) { continue; }\n        if (actor->state == 2) {')))
    return forms


def compile_candidate(root, output, name, source):
    conker = root / 'conker'
    path = output / (name + '.c')
    obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
    path.write_text('#include <ultra64.h>\n' + DECLARATIONS + '\n' + source + '\n')
    command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
        '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', '-woff', '649,838']
    for include in ('.', 'include', 'include/2.0L', 'include/2.0L/PR', 'include/libc'):
        command += ['-I', include]
    command += ['-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)), str(path.relative_to(conker))]
    result = subprocess.run(command, cwd=conker, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1502BAD0 : SUBALIGN(4) { *(.text) } }\n')
    symbols = dict(D_800CC2D0=0x800CC2D0, D_80084160=0x80084160, D_80084190=0x80084190,
                   D_8003C8E0=0x8003C8E0, func_1506196C=0x1506196C, func_1502C408=0x1502C408,
                   func_1502C974=0x1502C974, func_150368C4=0x150368C4, func_15030E08=0x15030E08)
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1502BAD0',
        *['--defsym=' + symbol + '=' + hex(value) for symbol, value in symbols.items()],
        '-o', str(elf), str(obj)], check=True, capture_output=True)
    functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
    words = functions['func_1502BAD0']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 173 - size)
    retail = struct.unpack_from('>173I', (conker / 'conker.us.bin').read_bytes(), 0x58F80)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    record = dict(name=name, body_words=size,
                  frame=(-words[0]) & 0xFFFF if words[0] >> 16 == 0x27BD else 0,
                  real_differences=len(differences) + max(0, size - 173),
                  differences=differences, diagnostics=result.stdout + result.stderr)
    return record, slot


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-display-scan'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
