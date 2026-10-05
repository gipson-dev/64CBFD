"""Resource block-loader source/profile screening with fixed retail relocations."""

import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


BASELINE = r'''void *func_1502B350(u32 arg0, u32 arg1, s32 *arg2) {
    u32 amount;
    u32 expanded;
    void *compressed;
    void *result;

    amount = ((arg1 & 0x0FFFFFFF) + 1) & ~1;
    compressed = allocate_memory(amount, 1, 2, 2);
    result = compressed;
    if (compressed == NULL) {
        return NULL;
    }
    func_10004514(arg0, compressed, (amount + 15) & ~0xF, 1);
    if ((arg1 & 0x70000000) == 0x10000000) {
        expanded = *(u32 *)compressed & 0x7FFFFFFF;
        *arg2 = expanded;
        result = NULL;
        amount = 0;
        if (expanded != 0 && expanded < 1000000) {
            result = allocate_memory(expanded, 1, 2, 2);
            if (result != NULL) {
                amount = func_10006240(compressed, result, D_8003809C);
            }
        }
        func_10004074(compressed);
    }
    *arg2 = amount;
    return result;
}'''


def candidates():
    forms = [('baseline', BASELINE)]
    separate = BASELINE.replace('    u32 amount;', '    u32 aligned;\n    u32 amount;')
    separate = separate.replace('    amount = ((arg1', '    aligned = ((arg1')
    separate = separate.replace('    compressed = allocate_memory(amount,',
        '    amount = aligned;\n    compressed = allocate_memory(aligned,')
    separate = separate.replace('(amount + 15)', '(aligned + 15)')
    forms.append(('separate-sizes', separate))
    for name, body in list(forms):
        for result_reg, expanded_reg in ((True, False), (False, True), (True, True)):
            candidate = body
            if result_reg:
                candidate = candidate.replace('    void *result;', '    register void *result;')
            if expanded_reg:
                candidate = candidate.replace('    u32 expanded;', '    register u32 expanded;')
            forms.append((name + ('-register-result' if result_reg else '') +
                          ('-register-expanded' if expanded_reg else ''), candidate))
    for mask in range(1,16):
        candidate = separate
        declarations=('u32 aligned;', 'u32 amount;', 'void *compressed;', 'void *result;')
        for i,decl in enumerate(declarations):
            if mask & (1 << i):
                candidate = candidate.replace('    '+decl, '    register '+decl)
        forms.append(('register-mask-'+str(mask),candidate))
    all_register = dict(forms)['register-mask-15']
    nested = '''        expanded = *(u32 *)compressed & 0x7FFFFFFF;
        *arg2 = expanded;
        if (expanded != 0) {
            result = NULL;
            if (expanded < 1000000) {
                result = allocate_memory(expanded, 1, 2, 2);
                if (result != NULL) {
                    amount = func_10006240(compressed, result, D_8003809C);
                } else {
                    amount = 0;
                }
            } else {
                amount = 0;
            }
        } else {
            result = NULL;
            amount = 0;
        }
'''
    start = all_register.index('        expanded =')
    end = all_register.index('        func_10004074(',start)
    nested_body = all_register[:start] + nested + all_register[end:]
    forms.append(('all-register-nested',nested_body))
    for name,base in (('all-register',all_register),('all-register-nested',nested_body)):
        candidate = base.replace('    u32 expanded;\n','')
        candidate = candidate.replace('        expanded = *(u32 *)compressed & 0x7FFFFFFF;\n        *arg2 = expanded;\n',
                                      '        *arg2 = *(u32 *)compressed & 0x7FFFFFFF;\n')
        candidate = re.sub(r'\bexpanded\b', '(u32)*arg2',candidate)
        forms.append((name+'-output-expanded',candidate))
    nested_result = nested_body.replace('register u32 aligned;', 'u32 aligned;')
    nested_result = nested_result.replace('register u32 amount;', 'u32 amount;')
    nested_result = nested_result.replace('register void *compressed;', 'void *compressed;')
    nested_result = nested_result.replace('    u32 expanded;\n', '')
    nested_result = nested_result.replace('        expanded = *(u32 *)compressed & 0x7FFFFFFF;\n        *arg2 = expanded;\n',
        '        *arg2 = *(u32 *)compressed & 0x7FFFFFFF;\n')
    nested_result = re.sub(r'\bexpanded\b', '(u32)*arg2', nested_result)
    old = '    u32 aligned;\n    u32 amount;\n    void *compressed;\n    register void *result;'
    arranged = '    u32 amount;\n    void *compressed;\n    register void *result;\n    u32 aligned;'
    for name,base in (('nested-result',nested_result),
                      ('nested-result-layout',nested_result.replace(old,arranged))):
        forms.append((name,base))
        init = '''    aligned = ((arg1 & 0x0FFFFFFF) + 1) & ~1;
    amount = aligned;
    compressed = allocate_memory(aligned, 1, 2, 2);
    result = compressed;
    if (compressed == NULL) {'''
        for label,replacement in (
                ('arg-assign', '''    compressed = allocate_memory(aligned = amount = ((arg1 & 0x0FFFFFFF) + 1) & ~1, 1, 2, 2);
    result = compressed;
    if (compressed == NULL) {'''),
                ('call-condition', '''    aligned = ((arg1 & 0x0FFFFFFF) + 1) & ~1;
    amount = aligned;
    if ((result = compressed = allocate_memory(aligned, 1, 2, 2)) == NULL) {'''),
                ('combined', '''    if ((result = compressed = allocate_memory(aligned = amount = ((arg1 & 0x0FFFFFFF) + 1) & ~1, 1, 2, 2)) == NULL) {''')):
            forms.append((name+'-'+label,base.replace(init,replacement)))
    forms.append(('nested-no-register',nested_result.replace('register void *result;', 'void *result;')))
    candidate=nested_result.replace('    u32 aligned;\n','')
    candidate=candidate.replace('    aligned = ((arg1', '    amount = ((arg1')
    candidate=candidate.replace('    amount = aligned;\n','').replace('allocate_memory(aligned,','allocate_memory(amount,')
    candidate=candidate.replace('(aligned + 15)', '(amount + 15)')
    forms.append(('nested-one-size',candidate))
    forms.append(('nested-one-size-no-register',candidate.replace('register void *result;', 'void *result;')))
    return forms


def compile_candidate(root, output, name, source, profile):
    conker = root / 'conker'
    path = output / (name + '-' + profile + '.c')
    obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
    prefix = ('typedef int s32; typedef unsigned int u32;\n#define NULL ((void *)0)\n'
              'void *allocate_memory(s32,s32,s32,s32);\n'
              'void func_10004514(u32,void *,u32,s32);\n'
              's32 func_10006240(void *,void *,u32); void func_10004074(void *);\n'
              'extern u32 D_8003809C;\n')
    path.write_text(prefix + source + '\n')
    flags = {'o2g3': ['-O2', '-g3'], 'o2': ['-O2'], 'o1g3': ['-O1', '-g3'], 'o1': ['-O1'],
             'o2g2': ['-O2', '-g2'], 'o2g1': ['-O2', '-g1'], 'o0g3': ['-O0', '-g3'],
             'g': ['-g']}[profile]
    result = subprocess.run([str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
        '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
        '-mips2', '-o32', *flags, '-o', str(obj.relative_to(conker)),
        str(path.relative_to(conker))], cwd=conker, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1502B350 : SUBALIGN(4) { *(.text) } }\n')
    targets = {'allocate_memory': 0x10003C40, 'func_10004514': 0x10004514,
               'func_10006240': 0x10006240, 'func_10004074': 0x10004074,
               'D_8003809C': 0x8003809C}
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
        '-e', 'func_1502B350', *(f'--defsym={k}=0x{v:X}' for k,v in targets.items()),
        '-o', str(elf), str(obj)], check=True, capture_output=True)
    functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
    words = functions['func_1502B350']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 86 - size)
    retail = struct.unpack_from('>86I', (conker / 'conker.us.bin').read_bytes(), 0x58800)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}')
                   for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    record = dict(name=name, profile=profile, body_words=size,
                  frame=(-words[0]) & 0xFFFF if words[0] >> 16 == 0x27BD else 0,
                  real_differences=len(differences) + max(0, size - len(retail)),
                  differences=differences, diagnostics=result.stdout + result.stderr)
    return record, slot


def main():
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prefix',default='')
    parser.add_argument('--profiles',default='o2g3,o2,o1g3,o1,o2g2,o2g1,o0g3,g')
    args=parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    production = re.search(r'void \*func_1502B350\([^;{}]+\) \{\n.*?\n\}',
        (root / 'conker/src/game_57FA0.c').read_text(), re.S).group(0)
    assert production == dict(candidates())['nested-one-size-no-register']
    output = root / 'conker/build/game-block-loader'
    output.mkdir(exist_ok=True)
    records = []
    for name, candidate in candidates():
        if not name.startswith(args.prefix):
            continue
        for profile in args.profiles.split(','):
            record, _ = compile_candidate(root, output, name, candidate, profile)
            records.append(record)
            print(name, profile, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    report = 'screen.json' if not args.prefix else 'screen-' + args.prefix + '.json'
    (output / report).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
