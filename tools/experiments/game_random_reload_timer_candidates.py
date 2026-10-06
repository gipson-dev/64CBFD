"""Screen bounded source forms for the flag-gated random-reload timer."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


ENTRY, ROM, WORDS = 0x150D26F0, 0xFFBA0, 39
TYPES = 'typedef unsigned char u8; typedef unsigned int u32; typedef int s32;\n'
DECLARATIONS = ('extern s32 D_800BE9E4;\ns32 func_150D278C();\n'
                's32 func_150ADA20(void);\n')
RECORD_TYPE = '''typedef struct ReloadRecord {
    u32 command;
    u32 base;
    u32 range;
    u32 timer;
    u8 parameters[1];
} ReloadRecord;
'''
SELECTED = '''void func_150D26F0(u8 *object) {
    u32 *record = (u32 *) (object + 0x28);

    if (object[0x78] & 1) {
        record[3] -= (u32) D_800BE9E4;
        if ((s32) record[3] < 0) {
            func_150D278C(record[0], record + 4, object[0xC], object[1]);
            record[3] = (u32) func_150ADA20() % (record[2] + 1) + record[1];
        }
    }
}'''
DIRECT = '''void func_150D26F0(u8 *object) {
    ReloadRecord *record = (ReloadRecord *) (object + 0x28);

    if (object[0x78] & 1) {
        record->timer -= (u32) D_800BE9E4;
        if ((s32) record->timer < 0) {
            func_150D278C(record->command, record->parameters, object[0xC], object[1]);
            record->timer = (u32) func_150ADA20() % (record->range + 1) + record->base;
        }
    }
}'''
PROFILES = {'o2g3': ['-O2', '-g3'], 'o2': ['-O2'], 'o1g3': ['-O1', '-g3'], 'o1': ['-O1']}
SYMBOLS = {'D_800BE9E4': 0x800BE9E4, 'func_150D278C': 0x150D278C, 'func_150ADA20': 0x150ADA20}


def candidates():
    forms = [('unsigned-record', SELECTED),
            ('signed-record', SELECTED.replace('u32 *record = (u32 *)', 's32 *record = (s32 *)')
             .replace('record[2] + 1', '(u32) record[2] + 1')),
            ('explicit-store', SELECTED.replace('record[3] -= (u32) D_800BE9E4;',
                                               'record[3] = record[3] - (u32) D_800BE9E4;')),
            ('early-exit', SELECTED.replace('    if (object[0x78] & 1) {',
                                            '    if (!(object[0x78] & 1)) { return; }\n    {')),
            ('signed-modulo', SELECTED.replace('(u32) func_150ADA20() % (record[2] + 1)',
                                               'func_150ADA20() % ((s32) record[2] + 1)'))]
    forms.extend([
        ('separate-pointer-assignment', SELECTED.replace('u32 *record = (u32 *) (object + 0x28);',
                                                        'u32 *record;\n\n    record = (u32 *) (object + 0x28);')),
        ('register-pointer', SELECTED.replace('u32 *record', 'register u32 *record', 1)),
        ('void-argument', SELECTED.replace('u8 *object', 'void *argument', 1)
         .replace('    u32 *record', '    u8 *object = argument;\n    u32 *record', 1)),
        ('reverse-addends', SELECTED.replace('(u32) func_150ADA20() % (record[2] + 1) + record[1]',
                                             'record[1] + (u32) func_150ADA20() % (record[2] + 1)')),
        ('signed-count', SELECTED.replace('record[2] + 1', '(u32) ((s32) record[2] + 1)')),
        ('scope-pointer', SELECTED.replace('    u32 *record = (u32 *) (object + 0x28);\n\n', '')
         .replace('    if (object[0x78] & 1) {',
                  '    if (object[0x78] & 1) {\n        u32 *record = (u32 *) (object + 0x28);')),
        ('named-random', SELECTED.replace('    u32 *record', '    u32 randomWord;\n    u32 *record', 1)
         .replace('            record[3] = (u32) func_150ADA20()',
                  '            randomWord = (u32) func_150ADA20();\n            record[3] = randomWord')),
        ('register-random', SELECTED.replace('    u32 *record', '    register u32 randomWord;\n    u32 *record', 1)
         .replace('            record[3] = (u32) func_150ADA20()',
                  '            randomWord = (u32) func_150ADA20();\n            record[3] = randomWord')),
    ])
    reversed_body = dict(forms)['reverse-addends']
    for name, body in (('typed-record', SELECTED), ('typed-record-reversed', reversed_body)):
        body = body.replace('u32 *record = (u32 *)', 'ReloadRecord *record = (ReloadRecord *)')
        for old, new in (('record[0]', 'record->command'), ('record[1]', 'record->base'),
                         ('record[2]', 'record->range'), ('record[3]', 'record->timer'),
                         ('record + 4', 'record->parameters')):
            body = body.replace(old, new)
        forms.append((name, RECORD_TYPE + body))
    assert dict(forms)['typed-record'] == RECORD_TYPE + DIRECT
    forms.extend([
        ('void-return-declaration', 'void func_150D278C();\n' + reversed_body),
        ('no-public-return', reversed_body.replace('void func_', 's32 func_', 1)),
        ('volatile-pointer', reversed_body.replace('u32 *record', 'u32 * volatile record', 1)),
        ('volatile-object', reversed_body.replace('u8 *object', 'u8 * volatile object', 1)),
    ])
    return forms


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    declarations = DECLARATIONS
    if body.startswith('void func_150D278C();\n'):
        declarations = declarations.replace('s32 func_150D278C();', 'void func_150D278C();')
        body = body.removeprefix('void func_150D278C();\n')
    source.write_text(TYPES + declarations + body + '\n')
    command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
               '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
               '-mips2', '-o32', *PROFILES[profile], '-o', str(obj.relative_to(root)), str(source.relative_to(root))]
    compiled = subprocess.run(command, cwd=root, capture_output=True, text=True)
    diagnostics = compiled.stdout + compiled.stderr
    if compiled.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'timer.ld'
    script.write_text('SECTIONS { .text 0x150D26F0 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_150D26F0',
                    *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
                   capture_output=True, text=True, check=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_150D26F0']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    if any(words[end:]):
        raise ValueError('nonzero tail after return')
    words = words[:end]
    retail = list(struct.unpack_from('>39I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    slot = words + [0] * max(0, WORDS - end)
    differences = [(i * 4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    return dict(name=name, profile=profile, body_words=end, frame=(-words[0]) & 65535,
                differences=len(differences) + max(0, end - WORDS), different_words=differences,
                exact=words == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-random-reload-timer'
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
