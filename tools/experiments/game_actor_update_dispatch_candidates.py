"""Actor update dispatcher, preserving ordered opaque calls and live field reads."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


DECLARATIONS = '''typedef struct ActorUpdate58F80 {
    s32 active;
    u8 id;
    u8 state;
    u8 pad6[0x5F];
    u8 predecessor;
    u8 pad66[0x3E];
    u8 signal;
    u8 padA5[0x53];
    u32 flags;
    u8 padFC[0x38];
    u8 eventA;
    u8 eventB;
    u8 pad136[0x93];
    u8 prepare;
    u8 pad1CA[0xA];
    s32 work;
    u8 pad1D8[0x24];
    u8 status;
    u8 pad1FD[0x63];
    u32 optional;
    u8 pad264[0x10];
    u8 maskId;
    u8 pad275[0xB7];
} ActorUpdate58F80;

extern u8 D_800C666F[];
s32 func_1502DF38();
s32 func_1502C608();
s32 func_1502FBE8();
s32 func_1502E4C4();
s32 func_1503A08C();
s32 func_150345E4();
s32 func_1503A830();
s32 func_1503DF48();
s32 func_1502EEF4();
s32 func_1502F264();
s32 func_1502EAFC();
s32 func_150A4B04();
s32 func_1517AD00();
'''

BASELINE = '''void func_1502BD84(ActorUpdate58F80 *actor, s32 slot) {
    s32 state;

    state = actor->state;
    actor->work = 0;
    if (state == 5) {
        func_1502DF38(slot, 1);
        return;
    }
    if (actor->id == 255 || state == 3) {
        return;
    }
    if (state == 2) {
        func_1502C608(slot);
        return;
    }
    if (actor->prepare != 0) {
        func_1502FBE8(actor);
    }
    func_1502E4C4(slot);
    func_1502DF38(slot, 0);
    func_1503A08C(actor);
    if (actor->work == 0) {
        actor->status = 2;
    } else {
        func_150345E4(slot);
        func_1503A830(actor);
    }
    if (D_800C666F[slot * 16] != 0) {
        func_1503DF48(slot);
    }
    if (actor->active != 0) {
        func_1502EEF4(slot);
        func_1502F264(slot);
        if (actor->signal != 0) {
            func_1502EAFC(actor);
        }
        if ((actor->flags & 0x4000) != 0) {
            func_150A4B04(actor);
        }
        if (actor->optional != 0) {
            func_1517AD00(actor->eventA, actor->eventB, slot);
        }
    }
}'''


def candidates():
    forms = [('baseline', BASELINE), ('placeholder', 's32 func_1502BD84() { return 0; }')]
    forms.append(('wrong-omitted-slot-negative-control', BASELINE.replace('func_1502EEF4(slot)', 'func_1502EEF4()')))
    for name, before, after in (
            ('byte-state', '    s32 state;', '    u8 state;'),
            ('word-state', '    s32 state;', '    u32 state;'),
            ('late-clear', '    state = actor->state;\n    actor->work = 0;', '    actor->work = 0;\n    state = actor->state;'),
            ('wrong-work-one-negative-control', 'actor->work == 0', 'actor->work != 1'),
            ('shifted-flag', '(actor->flags & 0x4000)', '((actor->flags >> 14) & 1)'),
            ('reverse-id', 'actor->id == 255 || state == 3', 'state == 3 || actor->id == 255'),
            ('unsigned-slot', 's32 slot)', 'u32 slot)'),
            ('register-actor', 'ActorUpdate58F80 *actor,', 'register ActorUpdate58F80 *actor,')):
        forms.append((name, BASELINE.replace(before, after)))
    table_gate = '    if (D_800C666F[slot * 16] != 0) {\n        func_1503DF48(slot);'
    state_gate = '    state = slot;\n    if (D_800C666F[state * 16] != 0) {\n        func_1503DF48(state);'
    early = '    if (actor->active == 0) {\n        return;\n    }\n    {'
    forms += [
        ('index-state', BASELINE.replace(table_gate, state_gate)),
        ('index-temporary', BASELINE.replace('    s32 state;', '    s32 state;\n    s32 index;')
         .replace(table_gate, state_gate.replace('state', 'index'))),
        ('index-assignment', BASELINE.replace('D_800C666F[slot * 16]', 'D_800C666F[(state = slot) * 16]')
         .replace('        func_1503DF48(slot);', '        func_1503DF48(state);')),
        ('nested-nonzero', BASELINE.replace('    if (actor->active != 0) {', early)),
        ('index-state-early', BASELINE.replace(table_gate, state_gate).replace('    if (actor->active != 0) {', early)),
        ('typed-table-callback', 's32 func_1503DF48(s32 slot);\n' + BASELINE),
        ('void-table-callback', BASELINE.replace('        func_1503DF48(slot);',
                                              '        ((void (*)(s32))func_1503DF48)(slot);')),
        ('volatile-slot', BASELINE.replace('s32 slot)', 'volatile s32 slot)')),
        ('register-slot', BASELINE.replace('s32 slot)', 'register s32 slot)')),
        ('slot-home-pointer', BASELINE.replace('    s32 state;', '    s32 state;\n    s32 *home = &slot;')
         .replace('D_800C666F[slot * 16]', 'D_800C666F[*home * 16]')
         .replace('        func_1503DF48(slot);', '        func_1503DF48(*home);')),
        ('copy-home-before-active', BASELINE.replace('    if (actor->active != 0) {',
                                                   '    slot = *(volatile s32 *)&slot;\n    if (actor->active != 0) {')),
        ('slot-home-pointer-all', BASELINE.replace('    s32 state;', '    s32 state;\n    s32 *home = &slot;')
         .replace('D_800C666F[slot * 16]', 'D_800C666F[*home * 16]')
         .replace('func_1503DF48(slot)', 'func_1503DF48(*home)').replace('func_1502F264(slot)', 'func_1502F264(*home)')),
        ('signed-flag', BASELINE.replace('(actor->flags & 0x4000)', '((s32)actor->flags & 0x4000)')),
    ]
    rows = 'typedef struct { u8 pad[15]; u8 flag; } ActorSlotFlag;\nextern ActorSlotFlag D_800C6660[26];\n'
    forms.append(('structured-slot-flags', rows + BASELINE.replace('D_800C666F[slot * 16]', 'D_800C6660[slot].flag')))
    forms.append(('volatile-structured-flags', rows.replace('extern ActorSlotFlag', 'extern volatile ActorSlotFlag') +
                  BASELINE.replace('D_800C666F[slot * 16]', 'D_800C6660[slot].flag')))
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
    script.write_text('SECTIONS { .text 0x1502BD84 : SUBALIGN(4) { *(.text) } }\n')
    symbols = {name: int(name[5:], 16) for name in (
        'func_1502DF38', 'func_1502C608', 'func_1502FBE8', 'func_1502E4C4',
        'func_1503A08C', 'func_150345E4', 'func_1503A830', 'func_1503DF48',
        'func_1502EEF4', 'func_1502F264', 'func_1502EAFC', 'func_150A4B04', 'func_1517AD00')}
    symbols['D_800C666F'] = 0x800C666F
    symbols['D_800C6660'] = 0x800C6660
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1502BD84',
        *['--defsym=' + symbol + '=' + hex(value) for symbol, value in symbols.items()],
        '-o', str(elf), str(obj)], check=True, capture_output=True)
    functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
    words = functions['func_1502BD84']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 88 - size)
    retail = struct.unpack_from('>88I', (conker / 'conker.us.bin').read_bytes(), 0x59234)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    record = dict(name=name, body_words=size, frame=(-words[0]) & 0xFFFF if words[0] >> 16 == 0x27BD else 0,
                  real_differences=len(differences) + max(0, size - 88), differences=differences,
                  diagnostics=result.stdout + result.stderr)
    return record, slot


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-update-dispatch'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
