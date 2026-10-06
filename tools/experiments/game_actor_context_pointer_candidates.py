"""Measure explicit live context-byte pointers and saved-context stack homes."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'conker/src/game/generated_71820.c'
TEXT = SOURCE.read_text()
PREAMBLE = TEXT.split('void func_15044370()', 1)[0]
BASELINE = '''s32 func_15044380(f32 x, f32 y, f32 z, ContextActor71820 *actor,
                  s32 mode, s32 secondPass) {
    s32 context;
    s32 savedContext;
    s32 total;

    D_800CBDF4 = -32768.0f;
    D_800CBDF8 = -32768.0f;
    total = 0;
    actor->state = 0;
    func_15044660(actor, x, y, z);
    savedContext = D_800CBDD3;
    for (context = 3; context >= 0; context--) {
        if (D_80089120[context] == 1) {
            if (context != 3 || !(actor->flags & 0x200)) {
                func_1510F800(context);
                if (D_800DBE62 != 0) {
                    total = (s32)((u32)total + (u32)func_150AB1F0(x, y, z, actor, mode));
                }
            }
        }
    }
    if (secondPass != 0) {
        for (context = 0; context < 3; context++) {
            if (D_80089120[context] == 1) {
                func_1510F800(context);
                if (D_800DBE62 != 0) {
                    func_150AC3E4(x, y, z, actor, 0);
                }
            }
        }
    }
    func_1510F800(0);
    D_800CBDD3 = savedContext;
    return total;
}'''


def replace(body, before, after):
    if body.count(before) != 1:
        raise ValueError('context dispatcher anchor no longer binds: ' + before)
    return body.replace(before, after, 1)


def candidates(baseline=BASELINE):
    forms = [('checkpoint', baseline)]
    declarations = '    s32 context;\n    s32 savedContext;\n    s32 total;'
    for mask in (1, 2, 3):
        pointers = ('    u8 *enabled;\n' if mask & 1 else '') + ('    u8 *eligible;\n' if mask & 2 else '')
        for placement in ('before', 'middle', 'after'):
            locals_ = {
                'before': pointers + declarations,
                'middle': '    s32 context;\n' + pointers + '    s32 savedContext;\n    s32 total;',
                'after': declarations + '\n' + pointers.rstrip(),
            }[placement]
            body = replace(baseline, declarations, locals_)
            if mask & 1:
                for loop in ('for (context = 3; context >= 0; context--) {', 'for (context = 0; context < 3; context++) {'):
                    body = replace(body, loop, loop + '\n' + ('        ' if 'context = 3' in loop else '            ') +
                                        'enabled = &D_80089120[context];')
                body = body.replace('D_80089120[context] == 1', '*enabled == 1')
            if mask & 2:
                body = replace(body, '    savedContext = D_800CBDD3;',
                                    '    savedContext = D_800CBDD3;\n    eligible = &D_800DBE62;')
                body = body.replace('D_800DBE62 != 0', '*eligible != 0')
            for flipped in (False, True):
                changed = body
                if flipped:
                    changed = replace(changed, '(u32)total + (u32)func_150AB1F0(x, y, z, actor, mode)',
                                              '(u32)func_150AB1F0(x, y, z, actor, mode) + (u32)total')
                forms.append((f'pointers-{mask}-{placement}-' + ('call-first' if flipped else 'sum-first'), changed))
    return forms


def compile_candidate(output, name, body):
    conker = ROOT / 'conker'
    source, obj, elf = [output / (name + suffix) for suffix in ('.c', '.o', '.elf')]
    source.write_text(PREAMBLE + body + '\n')
    command = [str(ROOT / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
               '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
               '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', '-woff', '649,838']
    for include in ('.', 'include', 'include/2.0L', 'include/2.0L/PR', 'include/libc'):
        command += ['-I', include]
    command += ['-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)), str(source.relative_to(conker))]
    result = subprocess.run(command, cwd=conker, capture_output=True, text=True, check=True)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x15044380 : SUBALIGN(4) { *(.text) } .rodata 0x800916B0 : { *(.rodata*) } }\n')
    definitions = dict(D_800CBDF4=0x800CBDF4, D_800CBDF8=0x800CBDF8, D_800CBDD3=0x800CBDD3,
                       D_80089120=0x80089120, D_800DBE62=0x800DBE62, func_15044660=0x15044660,
                       func_1510F800=0x1510F800, func_150AB1F0=0x150AB1F0, func_150AC3E4=0x150AC3E4)
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_15044380',
                    *[f'--defsym={key}=0x{value:X}' for key, value in definitions.items()], '-o', str(elf), str(obj)],
                   capture_output=True, check=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_15044380']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 107 - size)
    retail = list(struct.unpack_from('>107I', (conker / 'conker.us.bin').read_bytes(), 0x71830))
    differences = [(i * 4, f'{actual:08X}', f'{wanted:08X}') for i, (actual, wanted) in enumerate(zip(slot, retail)) if actual != wanted]
    return dict(name=name, body_words=size, frame=(-words[0]) & 65535,
                real_differences=len(differences) + max(0, size - 107), differences=differences,
                diagnostics=result.stdout + result.stderr), slot


def main():
    output = ROOT / 'conker/build/game-actor-context-pointers'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
