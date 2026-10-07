"""Recover the eleven-field range query without caching its live table accesses."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x151438D8, 0x170D88, 272
FUNCTION = 'func_151438D8'
SYMBOLS = dict(func_15143D18=0x15143D18, D_800D3094=0x800D3094, D_800D3098=0x800D3098)
DECLARATIONS = '''typedef struct {
    s16 x, y, z, radius, height, width;
    f32 valueC, value10;
    u8 value14, flags, value16, value17;
    s32 word18, word1C, word20;
    u8 pad24[0x10];
} GameQueryRecord;
extern s32 D_800D3094;
extern GameQueryRecord *D_800D3098;
void func_15143D18(s32 *, s32 *, s32, s32);
'''
OWNER_DECLARATIONS = DECLARATIONS
OWNER_INCLUDE = '''/* This owner uses the retail pointer, not the legacy inline-array declaration. */
#define D_800D3098 D_800D3098_legacy_array
#include "variables.h"
#undef D_800D3098'''
PROTOTYPE = 'GameQueryRecord *func_151438D8(s32 start, s32 end, u16 flags, GameQueryRecord *query);'
FIELDS = (
    ('x', 'y', 'z'), ('radius', 'height', 'width'), ('valueC',), ('value10',),
    ('value14',), ('flags',), ('value16',), ('value17',), ('word18',), ('word1C',), ('word20',))


def body(mask_type='u16', loop='for', order=False, flags_type='u16'):
    declarations = '    %s pass;\n    %s match;\n' % (mask_type, mask_type)
    if order: declarations = '    %s match;\n    %s pass;\n' % (mask_type, mask_type)
    source = '''GameQueryRecord *func_151438D8(s32 start, s32 end, %s flags, GameQueryRecord *query) {
    GameQueryRecord *result = NULL;
    s32 index;
%s
    if (query == NULL) {
        return NULL;
    }
    func_15143D18(&start, &end, 0, D_800D3094);
''' % (flags_type, declarations)
    if loop == 'for': source += '    for (index = start; index < end; index++) {\n'
    else: source += '    index = start;\n    if (index < end) {\n        do {\n'
    source += '        pass = 0;\n        match = 0;\n'
    for i, fields in enumerate(FIELDS):
        flag = '0x%X' % (1 << i)
        comparisons = []
        for field in fields:
            value = 'D_800D3098[index].' + field
            if field == 'flags': value = '(' + value + ' >> 2)'
            comparisons.append('query->%s == %s' % (field, value))
        source += '''        if (flags & %s) {
            if (%s) {
                pass |= %s;
                match |= %s;
            }
        } else {
            pass |= %s;
        }
''' % (flag, ' &&\n                '.join(comparisons), flag, flag, flag)
    source += '''        if (flags & 0x1000) {
            if (pass == 0x7FF) {
                result = &D_800D3098[index];
            }
        } else if (match != 0) {
            result = &D_800D3098[index];
        }
'''
    if loop == 'for': source += '    }\n'
    else: source += '        index++;\n        } while (index != end);\n    }\n'
    return source + '    return result;\n}'


BASELINE = body()
SELECTED = BASELINE.replace('    GameQueryRecord *result = NULL;\n    s32 index;',
    '    s32 index;\n    GameQueryRecord *result = NULL;')


def storage_candidates():
    original = '    GameQueryRecord *result = NULL;\n    s32 index;\n    u16 pass;\n    u16 match;\n'
    for i, sequence in enumerate(itertools.permutations(original.strip().split('\n'))):
        yield 'decl-%02d' % i, BASELINE.replace(original,
            '\n'.join('    ' + item.strip() for item in sequence) + '\n')
    yield 'late-init', BASELINE.replace('GameQueryRecord *result = NULL;', 'GameQueryRecord *result;').replace(
        '    if (query == NULL)', '    result = NULL;\n    if (query == NULL)')
    yield 'null-result', BASELINE.replace('return NULL;', 'return result;')
    yield 'index-start', BASELINE.replace('    s32 index;\n', '').replace('index', 'start').replace('start = start;', ';')
    yield 'void-result', BASELINE.replace('GameQueryRecord *result', 'void *result')
    yield 'word-result', BASELINE.replace('GameQueryRecord *result = NULL;', 's32 result = 0;').replace(
        'result = &D_800D3098[index]', 'result = (s32)&D_800D3098[index]').replace('return result;', 'return (GameQueryRecord *)result;')
    yield 'early-range-gate', BASELINE.replace('    for (index = start; index < end; index++) {',
        '    if (start >= end) return result;\n    for (index = start; index < end; index++) {')


def compile_candidate(root, output, name, source_body=SELECTED, profile='o2g3', declarations=DECLARATIONS):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n' + declarations + source_body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn',
        '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2',
        '-o32', '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I',
        'conker/include/2.0L/PR', '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2',
        '-D_MIPS_SZLONG=32', *PROFILES[profile], '-o', str(obj.relative_to(root)),
        str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics: raise ValueError(diagnostics)
    script = output / 'query.ld'
    script.write_text('SECTIONS { .text 0x151438D8 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, relocations = parse_object(obj)
    meta = functions[FUNCTION]
    pools = sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:]); words = words[:end]
    retail = struct.unpack_from('>272I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frame = (-words[0]) & 65535 if words[0] & 0xFFFF0000 == 0x27BD0000 else 0
    return dict(name=name, profile=profile, body_words=end, object_words=meta['size'] // 4,
        frame=frame, diagnostics=diagnostics, relocations=relocations,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0))), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-record-query'; output.mkdir(exist_ok=True)
    records = []
    for mask_type, loop, order, flags_type in itertools.product(('u16', 'u32'), ('for', 'do'), (False, True), ('u16', 'u32')):
        name = '%s-%s-%s-%s' % (mask_type, loop, int(order), flags_type)
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name + '-' + profile,
                body(mask_type, loop, order, flags_type), profile)
            records.append(record)
            print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    for name, candidate in storage_candidates():
        record, _ = compile_candidate(root, output, name, candidate)
        records.append(record)
        print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    for profile in PROFILES:
        record, _ = compile_candidate(root, output, 'selected-' + profile, SELECTED, profile)
        records.append(record)
        print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__': main()
