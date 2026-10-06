"""Screen the four-record, alias-sensitive vertex attribute initializer."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x151400D0, 0x16D580, 48
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
SELECTED = '''void func_151400D0(u8 *out, u8 *input) {
    s32 i;
    for (i = 0; i < 4; i++) {
        *(u16 *)(out + 6) = *(u16 *)(input + 8);
        out[12] = *(s16 *)(input + 0);
        out[13] = *(s16 *)(input + 2);
        out[14] = *(s16 *)(input + 4);
        out[15] = *(s16 *)(input + 6);
        *(u16 *)(out + 6) = 0;
        out += 16;
        input += 10;
    }
}'''


def candidates():
    named = SELECTED.replace('    s32 i;', '    s32 i;\n    s32 alpha;').replace(
        '        out[15] = *(s16 *)(input + 6);\n        *(u16 *)(out + 6) = 0;',
        '        alpha = *(s16 *)(input + 6);\n        *(u16 *)(out + 6) = 0;\n        out[15] = alpha;')
    typed = '''void func_151400D0(Vtx *out, s16 *input) {
    s32 i;
    s32 alpha;
    for (i = 0; i < 4; i++) {
        out->v.flag = (u16)input[4];
        out->v.cn[0] = input[0];
        out->v.cn[1] = input[1];
        out->v.cn[2] = input[2];
        alpha = input[3];
        out->v.flag = 0;
        out->v.cn[3] = alpha;
        out++;
        input += 5;
    }
}'''
    direct_typed = typed.replace('    s32 alpha;\n', '').replace(
        '        alpha = input[3];\n        out->v.flag = 0;\n        out->v.cn[3] = alpha;',
        '        out->v.cn[3] = input[3];\n        out->v.flag = 0;')
    indexed = named.replace('        out += 16;\n        input += 10;', '').replace(
        'out + 6', 'out + i * 16 + 6').replace('out[', 'out[i * 16 + ').replace('input +', 'input + i * 10 +')
    return [('named-alpha', named), ('vertices', typed), ('direct-colors', SELECTED),
            ('direct-vertices', direct_typed), ('short-alpha', named.replace('s32 alpha;', 's16 alpha;')),
            ('indexed', indexed)]


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output/(name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n'+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output/'vertex-attributes.ld'
    script.write_text('SECTIONS { .text 0x151400D0 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_151400D0',
                    '-o', str(elf), str(obj)], check=True, capture_output=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_151400D0']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>48I', (root/'conker/conker.us.bin').read_bytes(), ROM))
    slot = words+[0]*max(0, WORDS-end)
    differences = [(i*4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-word)&65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        differences=len(differences)+max(0, end-WORDS), different_words=differences,
        exact=slot == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-vertex-attribute-initializer'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name+'-'+profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    (output/'measurements.json').write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
