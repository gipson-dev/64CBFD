"""Screen texture resolver switches against the original code and jump table."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments import game_texture_cache_candidates as cache
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x1514306C, 0x17051C, 50
FUNCTION = 'func_1514306C'
TABLE, ANCHOR = 0x800A562C, 'jtbl_800A562C_game'
SYMBOLS = dict(D_800915B0=0x800915B0, D_80091514=0x80091514,
    D_80091564=0x80091564, D_80090B60=0x80090B60)
SOURCE_DECLARATION = cache.DECLARATIONS.split('extern s32', 1)[0]
DECLARATIONS = '''extern s32 D_800915B0, D_80091514;
extern s32 D_80091564[];
extern GameTextureSource D_80090B60[];
'''
PROTOTYPE = 's32 func_1514306C(GameTextureSource *source, s32 index, s32 subindex, u8 kind);'
BASELINE = '''s32 func_1514306C(GameTextureSource *source, s32 index, s32 subindex, u8 kind) {
    s32 result;
    u32 word;
    switch (kind) {
        case 4:
            result = D_800915B0;
            break;
        case 3:
            result = D_80091514;
            break;
        case 1:
            result = 0;
            break;
        case 2:
            result = D_80091564[index];
            break;
        case 5:
            result = index;
            break;
        case 6:
            word = source->unk0;
            if (word >= 0x10000000U) {
                result = ((s32 *)word)[subindex];
            } else {
                result = word;
            }
            break;
        default:
            result = ((s32 *)D_80090B60[index].unk0)[subindex];
            break;
    }
    return result;
}'''
INDEX_BODY = BASELINE.replace('    u32 word;\n', '').replace('word = source->unk0;',
    'index = source->unk0;').replace('word >=', '(u32)index >=').replace('(s32 *)word',
    '(s32 *)index').replace('result = word;', 'result = index;')
CONDITION_BODY = INDEX_BODY.replace('            index = source->unk0;\n', '').replace(
    '(u32)index >=', '(u32)(index = source->unk0) >=')
WORD_BODY = BASELINE.replace('word = source->unk0;', 'word = source->unk0;\n            index = word;').replace(
    'result = word;', 'result = index;')
POINTER_BODY = WORD_BODY.replace('u32 word;', 's32 *word;').replace('word = source->unk0;',
    'word = (s32 *)source->unk0;').replace('index = word;', 'index = (s32)word;').replace(
    'word >=', '(u32)word >=').replace('((s32 *)word)[subindex]', 'word[subindex]')
SELECTED = INDEX_BODY.replace('((s32 *)index)[subindex]', '((s32 *)source->unk0)[subindex]')


def owner_guards():
    return [dict(filename='game_16EE20', function=FUNCTION, offset='0x%X' % offset,
        expected='0x%08X' % expected, replacement='0x%08X' % replacement,
        expected_relocations=kind + ':.rodata', replacement_relocations=kind + ':' + ANCHOR,
        note='Bind texture resolver switch to its preserved retail jump table',
        insert_after='', insert_after_relocations='', omit='false')
        for offset, expected, replacement, kind in (
            (0x20, 0x3C010000, 0x3C010000, 'R_MIPS_HI16'),
            (0x28, 0x8C2F0258, 0x8C2F0000, 'R_MIPS_LO16'))]


def candidates():
    for returns, local, low_first in itertools.product((False, True), repeat=3):
        body = BASELINE
        if not local:
            body = body.replace('    u32 word;\n', '').replace('            word = source->unk0;\n', '')
            body = body.replace('word >=', 'source->unk0 >=').replace('(s32 *)word', '(s32 *)source->unk0')
            body = body.replace('result = word;', 'result = source->unk0;')
        if low_first:
            value = 'word' if local else 'source->unk0'
            body = body.replace('if (%s >= 0x10000000U) {\n'
                '                result = ((s32 *)%s)[subindex];\n'
                '            } else {\n                result = %s;' % (value, value, value),
                'if (%s < 0x10000000U) {\n                result = %s;\n'
                '            } else {\n                result = ((s32 *)%s)[subindex];' % (value, value, value))
        if returns:
            body = body.replace('    s32 result;\n', '').replace('result =', 'return')
            body = body.replace('            break;\n', '').replace('    return result;\n', '')
        yield 'return%d-local%d-low%d' % (returns, local, low_first), body
    yield 'reuse-index-high', INDEX_BODY
    yield 'reuse-index-low', INDEX_BODY.replace('if ((u32)index >= 0x10000000U) {\n'
        '                result = ((s32 *)index)[subindex];\n'
        '            } else {\n                result = index;',
        'if ((u32)index < 0x10000000U) {\n                result = index;\n'
        '            } else {\n                result = ((s32 *)index)[subindex];')
    yield 'condition-index-high', CONDITION_BODY
    yield 'condition-index-low', CONDITION_BODY.replace(
        'if ((u32)(index = source->unk0) >= 0x10000000U) {\n'
        '                result = ((s32 *)index)[subindex];\n'
        '            } else {\n                result = index;',
        'if ((u32)(index = source->unk0) < 0x10000000U) {\n                result = index;\n'
        '            } else {\n                result = ((s32 *)index)[subindex];')
    yield 'else-index-expression', BASELINE.replace('result = word;', 'result = (index = word);')
    yield 'else-index-statements', BASELINE.replace('result = word;', 'index = word;\n                result = index;')
    yield 'word-and-index', WORD_BODY
    yield 'pointer-and-index', POINTER_BODY
    yield 'index-reload', SELECTED
    yield 'condition-reload', CONDITION_BODY.replace('((s32 *)index)[subindex]', '((s32 *)source->unk0)[subindex]')


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n' + SOURCE_DECLARATION + DECLARATIONS + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn',
        '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2',
        '-o32', '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I',
        'conker/include/2.0L/PR', '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2',
        '-D_MIPS_SZLONG=32', *PROFILES[profile], '-o', str(obj.relative_to(root)),
        str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'resolver.ld'
    script.write_text('SECTIONS { .text 0x1514306C : SUBALIGN(4) { *(.text) } '
        '.rodata 0x800A562C : SUBALIGN(4) { *(.rodata) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, relocations = parse_object(obj)
    meta = functions[FUNCTION]
    pools = sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>50I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    table = pools.get('.rodata', (TABLE, b''))[1]
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, object_words=meta['size'] // 4,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        diagnostics=diagnostics, frame=frames[0] if frames else 0, relocations=relocations, pool_bytes=len(table)), words, table


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-texture-resolver'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _, _ = compile_candidate(root, output, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], record['differences'], record['pool_bytes'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
