"""Recover the seven-argument address record allocator without instruction guards."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS, ALLOCATOR = 0x1519E970, 0x1CBE20, 37, 0x15167A68
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
RECORD = '''typedef struct {
    u8 header[0x10];
    u32 flags;
    s32 state;
    u8 *first;
    u8 *second;
    s16 lifetime;
    u8 pad22[2];
    u8 *owner;
    u8 mode;
    u8 pad29[3];
} AddressRecord1CBE20;'''
DECLARATIONS = 'void *func_15167A68(s32, s32, s32, s32, u8, u8);\n'
BASELINE = '''AddressRecord1CBE20 *func_1519E970(s16 lifetime, u8 *owner, u8 mode, u8 *first,
                                       u8 *second, u8 channel, s32 context) {
    AddressRecord1CBE20 *record;

    record = func_15167A68(0x26, context, sizeof(AddressRecord1CBE20), 1, channel, 1);
    if (record == NULL) {
        return NULL;
    }
    record->first = first;
    record->second = second;
    record->lifetime = lifetime;
    record->mode = mode;
    record->flags = 1;
    record->state = 0;
    record->owner = owner;
    return record;
}'''
SELECTED = BASELINE.replace('    record->owner = owner;\n', '').replace(
    '    record->flags = 1;', '    record->owner = owner;\n    record->flags = 1;')


def candidates():
    owner_first = SELECTED
    raw = BASELINE
    for member, offset, type_name in (('first', 0x18, 'u8 *'), ('second', 0x1C, 'u8 *'),
                                    ('lifetime', 0x20, 's16'), ('mode', 0x28, 'u8'),
                                    ('flags', 0x10, 'u32'), ('state', 0x14, 's32'), ('owner', 0x24, 'u8 *')):
        raw = raw.replace('record->'+member, '*(%s *)((u8 *)record + 0x%X)'%(type_name, offset))
    return [('early-null', BASELINE),
            ('nested-success', BASELINE.replace('    if (record == NULL) {\n        return NULL;\n    }',
                '    if (record != NULL) {').replace('    return record;', '    }\n    return record;')),
            ('flags-first', BASELINE.replace('    record->flags = 1;\n    record->state = 0;\n', '').replace(
                '    record->first = first;', '    record->flags = 1;\n    record->state = 0;\n    record->first = first;')),
            ('wide-lifetime', BASELINE.replace('s16 lifetime,', 's32 lifetime,')),
            ('wide-mode', BASELINE.replace('u8 mode,', 's32 mode,')),
            ('wide-channel', BASELINE.replace('u8 channel,', 's32 channel,')),
            ('explicit-size', BASELINE.replace('sizeof(AddressRecord1CBE20)', '0x2C')),
            ('register-result', BASELINE.replace('    AddressRecord1CBE20 *record;', '    register AddressRecord1CBE20 *record;')),
            ('owner-before-flags', owner_first),
            ('byte-view-mode', BASELINE.replace('record->mode', '((u8 *)record)[0x28]')),
            ('owner-first-byte-view', owner_first.replace('record->mode', '((u8 *)record)[0x28]')),
            ('raw-fields', raw)]


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n'+RECORD+'\n'+DECLARATIONS+body+'\n')
    compiled = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = compiled.stdout+compiled.stderr
    if compiled.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'record.ld'
    script.write_text('SECTIONS { .text 0x1519E970 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1519E970',
                    '--defsym=func_15167A68=0x15167A68', '-o', str(elf), str(obj)],
                   check=True, capture_output=True, text=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_1519E970']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>37I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    slot = words+[0]*max(0, WORDS-end)
    differences = [(i*4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-word)&65535 for word in words if word&0xFFFF0000 == 0x27BD0000 and word&0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=max(frames, default=0),
                differences=len(differences)+max(0, end-WORDS), different_words=differences,
                exact=slot == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-address-record-allocator'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name+'-'+profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
