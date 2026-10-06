"""Recover the actor buffer-copy gates, allocation ABI and live copy inputs."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

DECLARATIONS = '''typedef struct ActorCopy58F80 {
    u8 pad0[4];
    u8 id;
    u8 pad5[0xF3];
    u32 flags;
    u8 padFC[0xD8];
    void *source;
    void *buffer;
    u8 pad1DC[0x88];
    u32 copyState;
    u8 pad268[0xC4];
} ActorCopy58F80;
extern u16 D_800C4ED0[256];
s32 allocate_memory(s32, s32, s32, s32);
'''

BASELINE = '''void func_1502F948(ActorCopy58F80 *actor) {
    s32 id;

    if ((actor->flags & 0x4000) != 0 && actor->copyState != 0 && actor->source != NULL) {
        id = actor->id;
        if (actor->buffer == NULL) {
            actor->buffer = (void *)allocate_memory(D_800C4ED0[id] << 6, 1, 1, 2);
            if (actor->buffer == NULL) {
                return;
            }
        }
        bcopy(actor->source, actor->buffer, D_800C4ED0[id] << 6);
    }
}'''


def candidates():
    forms = [('baseline', BASELINE)]
    for name, before, after in (
            ('byte-id', '    s32 id;', '    u8 id;'),
            ('unsigned-id', '    s32 id;', '    u32 id;'),
            ('multiply-size', 'D_800C4ED0[id] << 6', 'D_800C4ED0[id] * 64'),
            ('reloaded-id-negative-control', 'bcopy(actor->source, actor->buffer, D_800C4ED0[id]',
             'bcopy(actor->source, actor->buffer, D_800C4ED0[actor->id]'),
            ('missing-state-negative-control', 'actor->copyState != 0 && ', '')):
        forms.append((name, BASELINE.replace(before, after)))
    forms.append(('cached-size-negative-control', BASELINE.replace('    s32 id;', '    s32 id, size;')
                  .replace('        id = actor->id;', '        id = actor->id;\n        size = D_800C4ED0[id] << 6;')
                  .replace('D_800C4ED0[id] << 6, 1, 1, 2', 'size, 1, 1, 2')
                  .replace('bcopy(actor->source, actor->buffer, D_800C4ED0[id] << 6)',
                           'bcopy(actor->source, actor->buffer, size)')))
    return forms


SELECTED = BASELINE


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
    script.write_text('SECTIONS { .text 0x1502F948 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1502F948',
                    '--defsym=D_800C4ED0=0x800C4ED0', '--defsym=allocate_memory=0x10003C40',
                    '--defsym=bcopy=0x10023A10', '-o', str(elf), str(obj)], check=True, capture_output=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_1502F948']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 45 - size)
    retail = struct.unpack_from('>45I', (conker / 'conker.us.bin').read_bytes(), 0x5CDF8)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    return dict(name=name, body_words=size, frame=(-words[0]) & 0xFFFF,
                real_differences=len(differences) + max(0, size - 45), differences=differences,
                diagnostics=result.stdout + result.stderr), slot


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-buffer-copy'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
