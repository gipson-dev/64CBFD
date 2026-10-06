"""Bound pointer lifetimes and random-expression shapes in the timed updater."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x15141478, 0x16E928, 59
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
SYMBOLS = {'D_800BE9A4': 0x800BE9A4, 'func_150ADA68': 0x150ADA68, 'func_150ADA20': 0x150ADA20}
DECLARATIONS = 'extern f32 D_800BE9A4;\nf32 func_150ADA68(void); s32 func_150ADA20(void);\n'
INLINE = '''s32 func_15141478(u8 *actor) {
    u8 *runtime;
    u8 *payload;
    payload = actor + 0x110;
    runtime = actor + 0x170;
    *(f32 *)(actor + 0x180) -= D_800BE9A4;
    if (*(f32 *)(actor + 0x180) < 0.0f) {
        *(f32 *)(runtime + 0x10) = func_150ADA68() * *(f32 *)(runtime + 0x14);
        if (func_150ADA20() & 3) {
            *(f32 *)(runtime + 0xC) = func_150ADA68() * (*(f32 *)(runtime + 0) - *(f32 *)(runtime + 4)) + *(f32 *)(runtime + 4);
        } else {
            *(f32 *)(runtime + 0xC) = func_150ADA68() * (*(f32 *)(runtime + 8) - *(f32 *)(runtime + 0)) + *(f32 *)(runtime + 0);
        }
    }
    *(f32 *)(payload + 0x48) += (*(f32 *)(runtime + 0xC) - *(f32 *)(payload + 0x48)) * *(f32 *)(runtime + 0x18);
    return 1;
}'''
SELECTED = INLINE.replace('    u8 *runtime;', '    f32 sample;\n    u8 *runtime;').replace(
    '        *(f32 *)(runtime + 0x10) = func_150ADA68()',
    '        sample = func_150ADA68();\n        *(f32 *)(runtime + 0x10) = sample').replace(
    '            *(f32 *)(runtime + 0xC) = func_150ADA68()',
    '            sample = func_150ADA68();\n            *(f32 *)(runtime + 0xC) = sample')


def candidates():
    payload = '    payload = actor + 0x110;\n'
    runtime = '    runtime = actor + 0x170;\n'
    late_payload = SELECTED.replace(payload, '').replace('    *(f32 *)(payload', payload+'    *(f32 *)(payload')
    late_runtime = SELECTED.replace(runtime, '').replace('    if (*(f32 *)(actor', runtime+'    if (*(f32 *)(actor')
    late_runtime = late_runtime.replace('    *(f32 *)(payload', runtime+'    *(f32 *)(payload')
    both_late = SELECTED.replace(payload, '').replace(runtime, '').replace(
        '    if (*(f32 *)(actor + 0x180) < 0.0f) {',
        '    if (*(f32 *)(actor + 0x180) < 0.0f) {\n        runtime = actor + 0x170;').replace(
            '    *(f32 *)(payload', payload+runtime+'    *(f32 *)(payload')
    scoped = SELECTED.replace('    f32 sample;\n', '').replace(
        '    if (*(f32 *)(actor + 0x180) < 0.0f) {',
        '    if (*(f32 *)(actor + 0x180) < 0.0f) {\n        f32 sample;')
    direct = SELECTED.replace('    u8 *payload;\n', '').replace(payload, '').replace('payload + 0x48', 'actor + 0x158')
    product = SELECTED.replace('*(f32 *)(payload + 0x48) +=', '*(f32 *)(payload + 0x48) =').replace(
        '* *(f32 *)(runtime + 0x18);', '* *(f32 *)(runtime + 0x18) + *(f32 *)(payload + 0x48);')
    return [('selected', SELECTED), ('late-payload', late_payload), ('late-runtime', late_runtime),
            ('both-late', both_late), ('inline', INLINE), ('scoped-samples', scoped),
            ('direct-output', direct), ('product-first', product)]


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output/(name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n'+DECLARATIONS+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output/'interpolation.ld'
    script.write_text('SECTIONS { .text 0x15141478 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_15141478',
                    *['--defsym=%s=0x%X'%item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
                   check=True, capture_output=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_15141478']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>59I', (root/'conker/conker.us.bin').read_bytes(), ROM))
    slot = words+[0]*max(0, WORDS-end)
    differences = [(i*4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-word)&65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
                differences=len(differences)+max(0, end-WORDS), different_words=differences,
                exact=slot == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-timed-interpolation'
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
