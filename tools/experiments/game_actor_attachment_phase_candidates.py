"""Recover the live actor-reference coordinate phase and its five-argument ABI."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

DECLARATIONS = '''typedef struct ActorAttachment58F80 {
    s32 active;
    u8 pad4[0x10];
    f32 x, y, z;
    u8 pad20[0x160];
    f32 boundY;
    u8 pad184[0x1A];
    u16 joint;
    u8 pad1A0[0xD4];
    u8 reference;
    u8 pad275[0xB7];
} ActorAttachment58F80;
extern ActorAttachment58F80 D_800CC2D0[26];
extern ActorAttachment58F80 D_800D121C[];
s32 func_1502F490();
'''

BASELINE = '''void func_1502F3C8(void) {
    ActorAttachment58F80 *actor;

    actor = D_800CC2D0;
    do {
        if (actor->active != 0 && actor->reference != 0) {
            actor->y = actor->boundY;
            func_1502F490(D_800CC2D0 + actor->reference - 1,
                         &actor->x, &actor->y, &actor->z, actor->joint);
            if (actor->y < actor->boundY) {
                actor->y = actor->boundY;
            } else {
                actor->boundY = actor->y;
            }
        }
        actor++;
    } while (actor != D_800D121C);
}'''


def candidates():
    forms = [('baseline', BASELINE)]
    forms.append(('subtract-index', BASELINE.replace('D_800CC2D0 + actor->reference - 1',
                                                     'D_800CC2D0 + (actor->reference - 1)')))
    forms.append(('nested-gates', BASELINE.replace('if (actor->active != 0 && actor->reference != 0) {',
                                                   'if (actor->active != 0) {\n            if (actor->reference != 0) {')
                  .replace('        actor++;', '        }\n        actor++;')))
    for name, before, after in (
            ('register-actor', '    ActorAttachment58F80 *actor;', '    register ActorAttachment58F80 *actor;'),
            ('less-end', 'actor != D_800D121C', 'actor < D_800D121C'),
            ('base-end', 'D_800D121C', '(D_800CC2D0 + 25)'),
            ('byte-address', 'D_800CC2D0 + actor->reference - 1',
             '(ActorAttachment58F80 *)((u8 *)D_800CC2D0 + (actor->reference - 1) * 0x32C)'),
            ('index-address', 'D_800CC2D0 + actor->reference - 1', '&D_800CC2D0[actor->reference - 1]')):
        forms.append((name, BASELINE.replace(before, after)))
    forms.append(('for-loop', BASELINE.replace('    actor = D_800CC2D0;\n    do {',
                                               '    for (actor = D_800CC2D0; actor != D_800D121C; actor++) {')
                  .replace('        actor++;\n    } while (actor != D_800D121C);', '    }')))
    forms.append(('local-base', BASELINE.replace('    ActorAttachment58F80 *actor;',
                                                 '    ActorAttachment58F80 *actor;\n    ActorAttachment58F80 *base;')
                  .replace('    do {', '    base = D_800CC2D0;\n    do {')
                  .replace('func_1502F490(D_800CC2D0 +', 'func_1502F490(base +')))
    forms.append(('initialized-actor', BASELINE.replace('    ActorAttachment58F80 *actor;',
                                                        '    ActorAttachment58F80 *actor = D_800CC2D0;')
                  .replace('    actor = D_800CC2D0;\n', '')))
    forms.append(('reference-first', BASELINE.replace('    ActorAttachment58F80 *actor;',
                       '    ActorAttachment58F80 *actor;\n    ActorAttachment58F80 *referenced;')
                  .replace('            actor->y = actor->boundY;',
                           '            referenced = D_800CC2D0 + actor->reference - 1;\n            actor->y = actor->boundY;', 1)
                  .replace('func_1502F490(D_800CC2D0 + actor->reference - 1,', 'func_1502F490(referenced,')))
    forms.append(('coordinate-pointers', BASELINE.replace('    ActorAttachment58F80 *actor;',
                       '    ActorAttachment58F80 *actor;\n    f32 *x, *y, *z;')
                  .replace('            actor->y = actor->boundY;',
                           '            x = &actor->x;\n            y = &actor->y;\n            z = &actor->z;\n            actor->y = actor->boundY;', 1)
                  .replace('&actor->x, &actor->y, &actor->z,', 'x, y, z,')))
    forms.append(('typed-call', 's32 func_1502F490(ActorAttachment58F80 *, f32 *, f32 *, f32 *, s32);\n' + BASELINE))
    forms.append(('cached-bound-negative-control', BASELINE.replace('    ActorAttachment58F80 *actor;',
                   '    ActorAttachment58F80 *actor;\n    f32 bound;')
                  .replace('            actor->y = actor->boundY;', '            bound = actor->boundY;\n            actor->y = bound;', 1)
                  .replace('if (actor->y < actor->boundY)', 'if (actor->y < bound)')
                  .replace('                actor->y = actor->boundY;', '                actor->y = bound;')))
    forms.append(('omitted-joint-negative-control', BASELINE.replace(', actor->joint);', ');')))
    return forms


SELECTED = dict(candidates())['for-loop']


def production_body():
    return SELECTED.replace('func_1502F490(D_800CC2D0 + actor->reference - 1,',
                            'func_1502F490((ActorCopy58F80 *)(D_800CC2D0 + actor->reference - 1),').replace(
                            'D_800CC2D0', '((ActorAttachment58F80 *)D_800CC2D0)').replace(
                            'D_800D121C', '((ActorAttachment58F80 *)D_800D121C)')


def compile_candidate(root, output, name, body):
    conker = root / 'conker'
    path = output / (name + '.c')
    obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
    path.write_text('#include <ultra64.h>\n' + DECLARATIONS + '\n' + body + '\n')
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
    script.write_text('SECTIONS { .text 0x1502F3C8 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1502F3C8',
                    '--defsym=D_800CC2D0=0x800CC2D0', '--defsym=D_800D121C=0x800D121C',
                    '--defsym=func_1502F490=0x1502F490', '-o', str(elf), str(obj)],
                   check=True, capture_output=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_1502F3C8']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 50 - size)
    retail = struct.unpack_from('>50I', (conker / 'conker.us.bin').read_bytes(), 0x5C878)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    return dict(name=name, body_words=size, frame=(-words[0]) & 0xFFFF,
                real_differences=len(differences) + max(0, size - 50), differences=differences,
                diagnostics=result.stdout + result.stderr), slot


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-attachment-phase'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
