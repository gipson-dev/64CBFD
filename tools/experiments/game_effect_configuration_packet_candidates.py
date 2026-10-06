"""Screen the five-argument configuration packet wrapper without word guards."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS, CALLEE = 0x1519EA78, 0x1CBF28, 69, 0x15152190
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
PACKET = '''typedef struct { f32 x, y, z; } Position1CBE20;
typedef struct {
    s32 count;
    s32 countRange;
    Position1CBE20 position;
    s16 angle;
    s16 angleRange;
    s16 pitch;
    s16 pitchRange;
    f32 speed;
    f32 speedRange;
    f32 vertical;
    f32 verticalRange;
    s16 lifetime;
    s16 lifetimeRange;
    f32 scale;
    f32 scaleRange;
    f32 spread;
} Configuration1CBE20;'''
DECLARATIONS = '''extern f32 D_800A8CC0, D_800A8CC4, D_800A8CC8, D_800A8CCC, D_800A8CD0;
void func_15152190(Configuration1CBE20 *, s32 *, f32 *, s32, f32, u8, u8, s32);
'''
BASELINE = '''void func_1519EA78(Position1CBE20 *position, u16 selector, f32 scale, u8 channel, s32 context) {
    Configuration1CBE20 packet;
    s32 selected;

    packet.count = 10;
    packet.countRange = 7;
    packet.position = *position;
    packet.angle = 0;
    packet.angleRange = 255;
    packet.pitch = -53;
    packet.pitchRange = 24;
    packet.speed = 10.0f;
    packet.speedRange = 8.0f;
    packet.vertical = D_800A8CC0;
    packet.verticalRange = D_800A8CC4;
    packet.lifetime = 50;
    packet.lifetimeRange = 20;
    packet.scale = D_800A8CC8;
    packet.scaleRange = D_800A8CCC;
    packet.spread = D_800A8CD0;
    selected = selector;
    func_15152190(&packet, &selected, &scale, 1, 0.0f, 0, channel, context);
}'''
SELECTED = BASELINE.replace('    s32 selected;', '    s32 selected;\n    f32 selectedScale;').replace(
    '    selected = selector;', '    selected = selector;\n    selectedScale = scale;').replace('&scale, 1,', '&selectedScale, 1,')


def candidates():
    return [('field-order', BASELINE),
            ('selector-first', BASELINE.replace('    selected = selector;\n', '').replace(
                '    packet.count = 10;', '    selected = selector;\n    packet.count = 10;')),
            ('local-order', BASELINE.replace('    Configuration1CBE20 packet;\n    s32 selected;',
                '    s32 selected;\n    Configuration1CBE20 packet;')),
            ('wide-selector', BASELINE.replace('u16 selector,', 's32 selector,')),
            ('wide-channel', BASELINE.replace('u8 channel,', 's32 channel,')),
            ('scalar-position', BASELINE.replace('    packet.position = *position;',
                '    packet.position.x = position->x;\n    packet.position.y = position->y;\n    packet.position.z = position->z;')),
            ('local-scale', SELECTED),
            ('local-scale-first', SELECTED.replace('    selectedScale = scale;\n', '').replace(
                '    packet.count = 10;', '    selectedScale = scale;\n    packet.count = 10;'))]


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n' + PACKET + '\n' + DECLARATIONS + body + '\n')
    compiled = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = compiled.stdout + compiled.stderr
    if compiled.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'configuration.ld'
    script.write_text('SECTIONS { .text 0x1519EA78 : SUBALIGN(4) { *(.text) } }\n')
    symbols = {'func_15152190': CALLEE, **{name: int(name[2:], 16) for name in
        ('D_800A8CC0', 'D_800A8CC4', 'D_800A8CC8', 'D_800A8CCC', 'D_800A8CD0')}}
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1519EA78',
        *['--defsym=%s=0x%X' % item for item in symbols.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True, text=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_1519EA78']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>69I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    slot = words + [0] * max(0, WORDS - end)
    differences = [(i * 4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    return dict(name=name, profile=profile, body_words=end, frame=(-words[0]) & 65535,
        differences=len(differences) + max(0, end - WORDS), different_words=differences,
        exact=slot == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-effect-configuration-packet'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
