"""Source-only screening of the resource helper's final pointer handoff."""

import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


def main():
    root = Path(__file__).resolve().parents[2]
    conker = root / 'conker'
    output = conker / 'build/game-resource-helper-schedule'
    output.mkdir(exist_ok=True)
    source = (conker / 'src/game/generated_15F680.c').read_text()
    body = re.search(r's32 func_151336A8\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
    types = ('typedef int s32; typedef unsigned int u32;\n#define NULL ((void *)0)\n'
             'typedef struct { void *data; } ExtendedResource15F680;\n'
             'typedef struct { ExtendedResource15F680 *resource; } ExtendedResourceNode15F680;\n'
             'extern s32 D_800A3880[], D_800DC640[];\n'
             'void *func_1502B6BC(s32 *,s32,s32 *,s32,...);\n'
             's32 func_1510CE60(void *,s32,s32,s32,s32 *);\n'
             'void func_15168E54(void *,void *);\n')
    call = '    func_15168E54(node->resource->data, node->resource);'
    # Normalize a recovered explicit handoff back to the pre-match control.
    body = body.replace('    s32 resource;\n', '')
    body = body.replace('    resource = (s32)node->resource;\n'
                        '    func_15168E54(*(void **)resource, (void *)resource);', call)
    body = body.replace('    /* Retail passes the resource address through a 32-bit word. */\n', '')
    for kind in ('s32', 'u32'):
        body = body.replace('(void *)(' + kind + ')node->resource', 'node->resource')
    variants = [('baseline', body)]
    for kind, load, data, argument in (
            ('typed', 'ExtendedResource15F680 *', 'resource = node->resource;',
             'resource->data, resource'),
            ('void', 'void *', 'resource = node->resource;', '*(void **)resource, resource'),
            ('signed', 's32 ', 'resource = (s32)node->resource;', '*(void **)resource, (void *)resource'),
            ('unsigned', 'u32 ', 'resource = (u32)node->resource;', '*(void **)resource, (void *)resource'),
            ('signed-word', 's32 ', 'resource = (s32)node->resource;',
             '(void *)*(s32 *)resource, (void *)resource'),
            ('unsigned-word', 'u32 ', 'resource = (u32)node->resource;',
             '(void *)*(u32 *)resource, (void *)resource')):
        for where in ('top', 'block'):
            declaration = '    ' + load + 'resource;\n'
            candidate = body.replace(call, '    ' + data + '\n    func_15168E54(' + argument + ');')
            if where == 'top':
                candidate = candidate.replace('    s32 output1;\n', '    s32 output1;\n' + declaration)
            else:
                candidate = candidate.replace('    ' + data, '    {\n' + declaration + '    ' + data)
                candidate = candidate.replace('    return 1;', '    }\n    return 1;')
            variants.append((kind + '-' + where, candidate))
    for name, second in (('signed-cast', '(void *)(s32)node->resource'),
                         ('unsigned-cast', '(void *)(u32)node->resource'),
                         ('char-cast', '(char *)node->resource')):
        variants.append((name, body.replace(call, '    func_15168E54(node->resource->data, ' + second + ');')))
    variants.append(('volatile-node', body.replace(call,
        '    func_15168E54(node->resource->data, *(ExtendedResource15F680 * volatile *)node);')))
    for kind in ('s32', 'u32'):
        variants.append((kind + '-field', body.replace(call,
            '    func_15168E54(*(void **)*([TYPE] *)node, (void *)*([TYPE] *)node);'
            .replace('[TYPE]', kind))))
    retail = list(struct.unpack_from('>46I', (conker / 'conker.us.bin').read_bytes(), 0x160B58))
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x151336A8 : SUBALIGN(4) { *(.text) } }\n')
    records = []
    for name, candidate in variants:
        path = output / (name + '.c')
        obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
        path.write_text(types + candidate + '\n')
        command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
                   '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
                   '-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)),
                   str(path.relative_to(conker))]
        result = subprocess.run(command, cwd=conker, capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stderr)
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
            '-e', 'func_151336A8', '--defsym=D_800A3880=0x800A3880',
            '--defsym=D_800DC640=0x800DC640', '--defsym=func_1502B6BC=0x1502B6BC',
            '--defsym=func_1510CE60=0x1510CE60', '--defsym=func_15168E54=0x15168E54',
            '-o', str(elf), str(obj)], check=True, capture_output=True)
        functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
        words = functions['func_151336A8']
        size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
        slot = words[:size] + [0] * max(0, 46 - size)
        differences = [(i * 4, f'{a:08X}', f'{b:08X}')
                       for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
        record = dict(name=name, body_words=size, frame=(-words[0]) & 0xFFFF,
                      real_differences=len(differences) + max(0, size - len(retail)),
                      differences=differences, diagnostics=result.stdout + result.stderr)
        records.append(record)
        print(name, size, hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
