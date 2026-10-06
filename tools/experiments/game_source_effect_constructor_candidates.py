"""Recover the source effect constructor's live callback and view contracts."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x1513D2F0, 0x16A7A0, 114
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
SYMBOLS = {'func_15167A68': 0x15167A68, 'memcpy': 0x10022EC0, 'bzero': 0x100226F0,
           'func_1513FFF4': 0x1513FFF4, 'func_151400D0': 0x151400D0,
           'func_1515D480': 0x1515D480, 'func_1515D440': 0x1515D440,
           'D_80082FA0': 0x80082FA0, 'D_800A5184': 0x800A5184}
DECLARATIONS = '''extern s32 D_80082FA0;
void func_1513FFF4(u8 *, u8, u8);
s32 func_151400D0(s32, s32);
'''
BASELINE = '''void *func_1513D2F0(void *descriptor, s32 table, u8 kind, u8 mode, u8 first,
                      u8 setup, u8 variant, s32 resource, s32 extra, s32 payload,
                      u8 channel, s32 context) {
    extern f32 D_800A5184;
    extern void *func_15167A68(s32, s32, s32, s32, u8, u8);
    extern u8 *func_1515D480(s32);
    extern u8 *func_1515D440(void);
    u8 *result;
    u32 flags;
    s32 category;
    u8 allocationMode;
    s32 i;

    flags = *(u32 *)((u8 *)descriptor + 0x40);
    if ((flags & 0x800000) != 0) {
        category = 0x56;
    } else if ((flags & 0x2000000) != 0) {
        category = 0x49;
    } else {
        category = 0x1C;
    }
    allocationMode = (s32)flags < 0 ? 2 : 1;
    result = func_15167A68(category, context, payload + 0x110, 1, channel, allocationMode);
    if (result == NULL) {
        return NULL;
    }
    memcpy(result + 0x18, descriptor, 0x58);
    result[0x70] = kind;
    result[0x71] = mode;
    result[0x72] = first;
    result[0x74] = 0;
    result[0x73] = setup;
    bzero(result + 0x100, 0x10);
    func_1513FFF4(result + 0xC0, result[0x18], variant);
    func_151400D0((s32)(result + 0xC0), table);
    *(s32 *)(result + 0x10) = 1;
    *(s32 *)(result + 0x14) = 0;
    *(s32 *)(result + 0x98) = 0;
    result[0x95] = 0;
    result[0x94] = 0;
    *(s32 *)(result + 0x90) = 0;
    *(s32 *)(result + 0x9C) = resource;
    *(f32 *)(result + 0x78) = D_800A5184;
    result[0xA0] = 0;
    *(s32 *)(result + 0xB8) = extra;
    for (i = 0; i < 4; i++) {
        *(u8 **)(result + 0xA4 + i * 4) = NULL;
    }
    *(u8 **)(result + 0xB4) = NULL;
    if (resource != 0) {
        for (i = 0; i <= D_80082FA0; i++) {
            *(u8 **)(result + 0xA4 + i * 4) = func_1515D480(resource);
        }
        *(u8 **)(result + 0xB4) = func_1515D440();
    }
    return result;
}'''

ACTOR = '''typedef struct {
    u8 header[0x10];
    s32 flags;
    s32 state;
    u8 descriptor[0x58];
    u8 kind;
    u8 mode;
    u8 first;
    u8 setup;
    u8 field74;
    u8 pad75[3];
    f32 scale;
    u8 pad7C[0x14];
    s32 field90;
    u8 field94;
    u8 field95;
    u8 pad96[2];
    s32 field98;
    s32 resource;
    u8 fieldA0;
    u8 padA1[3];
    u8 *views[4];
    u8 *viewOwner;
    s32 extra;
    u8 padBC[4];
    u8 helper[0x40];
    u8 scratch[0x10];
} SourceActor169510;'''


def typed_body(body=BASELINE):
    body = body.replace('    u8 *result;', '    SourceActor169510 *result;')
    for offset, field in ((0x70,'kind'),(0x71,'mode'),(0x72,'first'),(0x73,'setup'),(0x74,'field74'),
                          (0x94,'field94'),(0x95,'field95'),(0xA0,'fieldA0')):
        body = body.replace('result[0x%X]'%offset, 'result->'+field)
    for offset, field in ((0x10,'flags'),(0x14,'state'),(0x90,'field90'),(0x98,'field98'),
                          (0x9C,'resource'),(0xB8,'extra')):
        body = body.replace('*(s32 *)(result + 0x%X)'%offset, 'result->'+field)
    return body.replace('result + 0x18', 'result->descriptor').replace('result + 0x100', 'result->scratch').replace(
        'result + 0xC0', 'result->helper').replace('*(f32 *)(result + 0x78)', 'result->scale').replace(
        '*(u8 **)(result + 0xA4 + i * 4)', 'result->views[i]').replace('*(u8 **)(result + 0xB4)', 'result->viewOwner').replace(
        'result[0x18]', 'result->descriptor[0]')


def scheduling_candidates():
    body = BASELINE.replace('(s32)flags < 0', '(flags & 0x80000000) != 0')
    fields = body.replace('    result[0x74] = 0;\n    result[0x73] = setup;',
                          '    result[0x73] = setup;\n    result[0x74] = 0;')
    captured = body.replace('    s32 i;', '    s32 i;\n    f32 scale;').replace(
        '    *(s32 *)(result + 0x98) = 0;', '    scale = D_800A5184;\n    *(s32 *)(result + 0x98) = 0;').replace(
        '*(f32 *)(result + 0x78) = D_800A5184;', '*(f32 *)(result + 0x78) = scale;')
    combined = captured.replace('    result[0x74] = 0;\n    result[0x73] = setup;',
                               '    result[0x73] = setup;\n    result[0x74] = 0;')
    return [('byte-order',fields),('captured-default',captured),('combined-schedule',combined),
            ('typed-combined',typed_body(combined)),
            ('bound-pointer',combined.replace('    s32 i;', '    s32 i;\n    s32 *bound;').replace(
                '    if (resource != 0) {\n', '    if (resource != 0) {\n        bound = &D_80082FA0;\n').replace(
                'i <= D_80082FA0', 'i <= *bound')),
            ('register-bound',combined.replace('    s32 i;', '    s32 i;\n    register s32 *bound;').replace(
                '    if (resource != 0) {\n', '    if (resource != 0) {\n        bound = &D_80082FA0;\n').replace(
                'i <= D_80082FA0', 'i <= *bound'))]


def default_candidates():
    body = dict(scheduling_candidates())['byte-order']
    line = '    *(f32 *)(result + 0x78) = D_800A5184;\n'
    stripped = body.replace(line, '')
    anchors = ('    *(s32 *)(result + 0x14) = 0;', '    *(s32 *)(result + 0x98) = 0;',
               '    result[0x95] = 0;', '    result[0x94] = 0;', '    *(s32 *)(result + 0x90) = 0;',
               '    *(s32 *)(result + 0x9C) = resource;')
    for i, anchor in enumerate(anchors):
        yield 'default-before-'+str(i), stripped.replace(anchor, line+anchor)
    combined = dict(scheduling_candidates())['combined-schedule']
    yield 'a0-after-extra', combined.replace('    result[0xA0] = 0;\n', '').replace(
        '    *(s32 *)(result + 0xB8) = extra;', '    *(s32 *)(result + 0xB8) = extra;\n    result[0xA0] = 0;')
    yield 'register-default', combined.replace('    f32 scale;', '    register f32 scale;')
    direct = stripped.replace('    *(s32 *)(result + 0x98) = 0;', line+'    *(s32 *)(result + 0x98) = 0;')
    yield 'early-default-late-a0', direct.replace('    result[0xA0] = 0;\n', '').replace(
        '    *(s32 *)(result + 0xB8) = extra;', '    *(s32 *)(result + 0xB8) = extra;\n    result[0xA0] = 0;')


def candidates():
    return [('field-order', BASELINE),
            ('direct-schedule', SELECTED),
            ('narrow-category', BASELINE.replace('s32 category;', 'u8 category;')),
            ('wide-allocation-mode', BASELINE.replace('u8 allocationMode;', 's32 allocationMode;')),
            ('separate-mode', BASELINE.replace('    allocationMode = (s32)flags < 0 ? 2 : 1;',
                '    if ((s32)flags < 0) { allocationMode = 2; } else { allocationMode = 1; }')),
            ('bit-allocation-mode', BASELINE.replace('(s32)flags < 0', '(flags & 0x80000000) != 0')),
            ('typed-actor', typed_body()),
            ('typed-bit-mode', typed_body(BASELINE.replace('(s32)flags < 0', '(flags & 0x80000000) != 0'))),
            ('typed-narrow-category', typed_body(BASELINE.replace('s32 category;', 'u8 category;'))),
            ('split-category', BASELINE.replace('    } else if ((flags & 0x2000000) != 0) {\n'
                '        category = 0x49;\n    } else {\n        category = 0x1C;\n    }',
                '    } else {\n        category = 0x1C;\n        if ((flags & 0x2000000) != 0) { category = 0x49; }\n    }')),
            ('explicit-cursor', BASELINE.replace('    s32 i;', '    s32 i;\n    u8 *cursor;').replace(
                '    for (i = 0; i < 4; i++) {\n        *(u8 **)(result + 0xA4 + i * 4) = NULL;\n    }',
                '    cursor = result;\n    for (i = 0; i < 4; i++) {\n        *(u8 **)(cursor + 0xA4) = NULL;\n        cursor += 4;\n    }').replace(
                '        for (i = 0; i <= D_80082FA0; i++) {\n            *(u8 **)(result + 0xA4 + i * 4) = func_1515D480(resource);\n        }',
                '        cursor = result;\n        for (i = 0; i <= D_80082FA0; i++) {\n'
                '            *(u8 **)(cursor + 0xA4) = func_1515D480(resource);\n            cursor += 4;\n        }')),
            ('do-clear', BASELINE.replace('    for (i = 0; i < 4; i++) {\n'
                '        *(u8 **)(result + 0xA4 + i * 4) = NULL;\n    }',
                '    i = 0;\n    do {\n        *(u8 **)(result + 0xA4 + i * 4) = NULL;\n        i++;\n    } while (i < 4);')),
            ('direct-flags', BASELINE.replace('    flags = *(u32 *)((u8 *)descriptor + 0x40);\n','').replace(
                'flags &', '*(u32 *)((u8 *)descriptor + 0x40) &').replace(
                '(s32)flags < 0', '*(s32 *)((u8 *)descriptor + 0x40) < 0')),
            ('unit-first', BASELINE.replace('    *(s32 *)(result + 0x10) = 1;\n', '').replace(
                '    *(s32 *)(result + 0x14) = 0;', '    *(s32 *)(result + 0x14) = 0;\n    *(s32 *)(result + 0x10) = 1;')),
            ('default-first', BASELINE.replace('    *(f32 *)(result + 0x78) = D_800A5184;\n', '').replace(
                '    *(s32 *)(result + 0x10) = 1;', '    *(f32 *)(result + 0x78) = D_800A5184;\n    *(s32 *)(result + 0x10) = 1;')),
            ('resource-first', BASELINE.replace('    *(s32 *)(result + 0x9C) = resource;\n', '').replace(
                '    *(s32 *)(result + 0x10) = 1;', '    *(s32 *)(result + 0x9C) = resource;\n    *(s32 *)(result + 0x10) = 1;'))]


SELECTED = dict(default_candidates())['early-default-late-a0']


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output/(name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n'+ACTOR+'\n'+DECLARATIONS+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output/'effect-constructor.ld'
    script.write_text('SECTIONS { .text 0x1513D2F0 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1513D2F0',
        *['--defsym=%s=0x%X'%item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True, text=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_1513D2F0']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>114I', (root/'conker/conker.us.bin').read_bytes(), ROM))
    slot = words+[0]*max(0, WORDS-end)
    differences = [(i*4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    return dict(name=name, profile=profile, body_words=end, frame=(-words[0]) & 65535,
        differences=len(differences)+max(0, end-WORDS), different_words=differences,
        exact=slot == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-source-effect-constructor'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name+'-'+profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    for name, body in scheduling_candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name+'-'+profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    for name, body in default_candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (output/'measurements.json').write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
