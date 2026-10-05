"""Screen source-only local lifetimes for the immediate texture release slot."""

import itertools
import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


def main():
    root = Path(__file__).resolve().parents[2]
    conker = root / 'conker'
    output = conker / 'build/game-immediate-release-frame'
    output.mkdir(exist_ok=True)
    source = (conker / 'src/game/generated_139FC0.c').read_text()
    body = re.search(r'void func_1510D7AC\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
    if 's8 state = D_800BC448[arg0];' in body:
        body = body.replace('    s8 state = D_800BC448[arg0];',
            '    s8 *priority = &D_800BC448[arg0];\n    s8 state = *priority;\n'
            '    u8 *activity;\n    s32 count;\n    u32 *cache;')
        body = body.replace('        if (D_800D9F68[arg0] != 0) {',
            '        activity = &D_800D9F68[arg0];\n        count = *activity;\n'
            '        if (count != 0) {')
        body = body.replace('D_800D9F68[arg0] = D_800D9F68[arg0] - 1;', '*activity = count - 1;')
        body = body.replace('if (D_800D9F68[arg0] == 0)', 'if (*activity == 0)')
        body = body.replace('                func_10004074((void *)D_800B0E58[arg0]);',
            '                cache = &D_800B0E58[arg0];\n                func_10004074((void *)*cache);')
        body = body.replace('D_800B0E58[arg0] = 0xFFFFFFFF;', '*cache = 0xFFFFFFFF;')
        body = body.replace('D_800BC448[arg0] = 0;', '*priority = 0;')
    types = ('typedef signed char s8; typedef unsigned char u8; typedef int s32; '
             'typedef unsigned int u32;\nextern s8 D_800BC448[]; '
             'extern u8 D_800D9F68[]; extern u32 D_800B0E58[]; '
             'void func_10004074(void *);\n')
    variants = [('baseline', body), ('full-width-state', body.replace('s8 state', 's32 state'))]
    for order in itertools.permutations(('u8 *activity;', 's32 count;', 'u32 *cache;')):
        declaration = '\n'.join('    ' + line for line in order)
        variants.append(('order-' + '-'.join(line.split()[-1].strip('*;') for line in order),
                         body.replace('    u8 *activity;\n    s32 count;\n    u32 *cache;', declaration)))
    scoped = body.replace('    u8 *activity;\n    s32 count;\n    u32 *cache;\n', '')
    scoped = scoped.replace('    if (state != 0) {',
                            '    if (state != 0) {\n        u8 *activity;\n        s32 count;')
    scoped = scoped.replace('            if (*activity == 0) {',
                            '            if (*activity == 0) {\n                u32 *cache;')
    variants += [('scoped', scoped), ('scoped-full-width-state', scoped.replace('s8 state', 's32 state'))]
    for variable in ('priority', 'state', 'activity', 'count', 'cache'):
        variants.append(('register-' + variable, re.sub(
            r'(^    )(s8|u8|s32|u32)( \*?' + variable + r'\b)',
            r'\1register \2\3', body, flags=re.M)))
    for state in ('s8', 's32'):
        for count in ('s32', 'u32'):
            for qualifiers in ('', 'const '):
                candidate = body.replace('s8 state', qualifiers + state + ' state')
                candidate = candidate.replace('s32 count', count + ' count')
                variants.append(('types-' + state + '-' + count + '-' + (qualifiers.strip() or 'plain'), candidate))
    cache_inline = body.replace('    u32 *cache;\n', '')
    cache_inline = cache_inline.replace('                cache = &D_800B0E58[arg0];\n', '')
    cache_inline = cache_inline.replace('(void *)*cache', '(void *)D_800B0E58[arg0]')
    cache_inline = cache_inline.replace('*cache =', 'D_800B0E58[arg0] =')
    variants.append(('inline-cache', cache_inline))
    count_inline = body.replace('    s32 count;\n', '').replace('        count = *activity;\n', '')
    count_inline = count_inline.replace('count != 0', '*activity != 0').replace('count - 1', '*activity - 1')
    variants.append(('inline-count', count_inline))
    both_inline = cache_inline.replace('    s32 count;\n', '').replace('        count = *activity;\n', '')
    both_inline = both_inline.replace('count != 0', '*activity != 0').replace('count - 1', '*activity - 1')
    variants.append(('inline-count-cache', both_inline))
    activity_inline = body.replace('    u8 *activity;\n', '')
    activity_inline = activity_inline.replace('        activity = &D_800D9F68[arg0];\n', '')
    activity_inline = activity_inline.replace('*activity', 'D_800D9F68[arg0]')
    variants.append(('inline-activity', activity_inline))
    for name, base in (('count', count_inline), ('cache', cache_inline), ('both', both_inline)):
        inline = base.replace('    u8 *activity;\n', '')
        inline = inline.replace('        activity = &D_800D9F68[arg0];\n', '')
        inline = inline.replace('*activity', 'D_800D9F68[arg0]')
        variants.append(('inline-activity-' + name, inline))
    for name, base in list(variants):
        if name in ('baseline', 'inline-count-cache', 'inline-activity-both'):
            inline = base.replace('    s8 *priority = &D_800BC448[arg0];\n', '')
            inline = inline.replace('*priority', 'D_800BC448[arg0]')
            variants.append(('inline-priority-' + name, inline))
    for name, base in (('base', body), ('count', count_inline), ('cache', cache_inline),
                       ('both', both_inline), ('activity', activity_inline)):
        variants.append(('block-state-' + name, base.replace('    s8 state = *priority;\n', '')
                        .replace('    if (state != 0) {',
                                 '    if (*priority != 0) {\n        s8 state = *priority;')))
        for order in itertools.permutations(('s8 *priority = &D_800BC448[arg0];', 's8 state;')):
            prefix = '\n'.join('    ' + line for line in order)
            variants.append(('late-state-' + name + '-' + str(order.index('s8 state;')),
                             base.replace('    s8 *priority = &D_800BC448[arg0];\n    s8 state = *priority;',
                                          prefix).replace('    if (state != 0) {',
                                                          '    state = *priority;\n    if (state != 0) {')))
    for name, candidate in list(variants):
        if name in ('inline-cache', 'inline-count', 'scoped'):
            variants.append((name + '-wide', candidate.replace('s8 state', 's32 state')))
    retail = list(struct.unpack_from('>46I', (conker / 'conker.us.bin').read_bytes(), 0x13AC5C))
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1510D7AC : SUBALIGN(4) { *(.text) } }\n')
    records = []
    for name, candidate in variants:
        path = output / (name + '.c')
        obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
        path.write_text(types + candidate + '\n')
        relative = lambda value: str(value.relative_to(conker))
        command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
                   '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
                   '-mips2', '-o32', '-O2', '-g3', '-o', relative(obj), relative(path)]
        result = subprocess.run(command, cwd=conker, capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stderr)
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
            '-e', 'func_1510D7AC', '--defsym=D_800BC448=0x800BC448',
            '--defsym=D_800D9F68=0x800D9F68', '--defsym=D_800B0E58=0x800B0E58',
            '--defsym=func_10004074=0x10004074', '-o', str(elf), str(obj)],
            check=True, capture_output=True)
        functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
        words = functions['func_1510D7AC']
        size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
        words = words[:size]
        differences = [(i * 4, f'{a:08X}', f'{b:08X}')
                       for i, (a, b) in enumerate(zip(words, retail)) if a != b]
        record = dict(name=name, body_words=size, frame=(-words[0]) & 0xFFFF,
                      real_differences=len(differences) + abs(size - len(retail)),
                      differences=differences, diagnostics=result.stdout + result.stderr)
        records.append(record)
        print(name, size, hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
