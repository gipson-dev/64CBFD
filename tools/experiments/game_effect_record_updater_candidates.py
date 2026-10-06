"""Recover effect-record refresh/create with the actual SDK and private frame."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15141E38, 0x16F2E8, 80
FUNCTION = 'func_15141E38'
SYMBOLS = dict(D_8008A0B4=0x8008A0B4, func_1514ECE0=0x1514ECE0,
    func_15149130=0x15149130, memcpy=0x10022EC0, func_1514EC1C=0x1514EC1C)
LOCAL_DECLARATIONS = '''typedef struct { s32 index; u8 *actor; u8 identity; } GameEffectRefreshRequest;
s32 func_1514ECE0(u8 *, s16, u8 **);
s32 func_1514EC1C(s32, s32, s32);
'''
PROTOTYPE = 'void func_15141E38(u8 *actor, s32 index);'
SELECTED = '''void func_15141E38(u8 *actor, s32 index) {
    u8 *created;
    u8 *node;
    u8 *matched = NULL;
    u8 *record;
    GameEffectRefreshRequest request;
    node = *(u8 **)(actor + 0x2F4);
    while (func_1514ECE0(node, 0x1A, &node)) {
        record = *(u8 **)(node + 0x10);
        if (*(s32 *)(record + 0x28) == index) {
            matched = node;
            *(s16 *)(record + 0xE) = D_8008A0B4[index].unk4;
        }
        *(u8 *volatile *)&node = *(u8 **)(node + 0x14);
    }
    if (matched == NULL) {
        request.index = index;
        request.actor = actor;
        request.identity = actor[0x3B];
        created = (u8 *)func_15149130((s16)D_8008A0B4[index].unk4,
            -1, -1, -1, 1, 50, (struct37 *)12, 255, 1);
        if (created != NULL) {
            memcpy(created + 0x28, &request, 12);
            func_1514EC1C((s32)created, (s32)actor, 0x1A);
        }
    }
}'''


def candidates():
    for separate, cursor, scoped in itertools.product((False, True), repeat=3):
        body = SELECTED
        if not separate:
            body = body.replace('    u8 *created;\n', '').replace('created', 'record')
        if not cursor:
            body = body.replace('*(u8 *volatile *)&node =', 'node =')
        if scoped:
            body = body.replace('    GameEffectRefreshRequest request;\n', '')
            body = body.replace('    if (matched == NULL) {', '    if (matched == NULL) {\n        GameEffectRefreshRequest request;')
        yield 'shape-%d%d%d' % (separate, cursor, scoped), body


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output/(name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n#include "variables.h"\n'+LOCAL_DECLARATIONS+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics: raise ValueError(diagnostics)
    script = output/'updater.ld'
    script.write_text('SECTIONS { .text 0x15141E38 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
    _, functions, relocs = parse_object(obj)
    function = functions[FUNCTION]; text = sections(elf)['.text'][1]
    words = list(struct.unpack_from('>%dI' % (function['size']//4), text, function['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:]); words = words[:end]
    frames = [(-word)&65535 for word in words if word&0xFFFF0000 == 0x27BD0000 and word&0x8000]
    retail = struct.unpack_from('>80I', (root/'conker/conker.us.bin').read_bytes(), ROM)
    record = dict(name=name, profile=profile, body_words=end, object_words=function['size']//4,
        frame=frames[0] if frames else 0, diagnostics=diagnostics,
        differences=sum(a!=b for a, b in itertools.zip_longest(words, retail, fillvalue=0)), relocations=relocs)
    return record, words


def normalize(raw):
    """Close the pre-allocation register phase and relocate only private payload homes."""
    assert len(raw) == 80
    result = list(raw)
    cycle = {16: 18, 17: 16, 18: 17}
    for offset in range(0xC, 0xF4, 4):
        word = raw[offset//4]
        for shift in ((21, 16, 11) if word>>26 == 0 else (21, 16)):
            register = word>>shift&31
            if register in cycle: word = word&~(31<<shift) | cycle[register]<<shift
        result[offset//4] = word
    assert raw[1:3] == [0xAFB10030, 0xAFB0002C] and raw[7] == 0xAFB20034
    result[1], result[2], result[7] = 0xAFB20034, 0xAFB0002C, 0xAFB10030
    result[3], result[4] = result[4], result[3]
    before = list(result)
    movement = {0x78: 0x5C, 0x7C: 0x60, 0x5C: 0x64, 0x60: 0x68, 0x64: 0x6C,
                0x68: 0x70, 0x6C: 0x74, 0x70: 0x78, 0x74: 0x7C, 0xAC: 0xB0, 0xB0: 0xAC}
    for old, new in movement.items():
        word = before[old//4]
        if word>>26 in (4, 5, 20, 21):
            imm = word&65535; delta = imm if imm<32768 else imm-65536
            target = old+4+delta*4
            # Search arguments now precede the selector test; the skip resumes at the live next-link read.
            if old == 0x60:
                assert target == 0x78
                target = 0x80
            else:
                target = movement.get(target, target)
            word = word&0xFFFF0000 | ((target-new-4)//4&65535)
        result[new//4] = word
    assert result[0x84//4] == 0xAE4C0000 and raw[0x8C//4] == 0x8FA40058
    result[0x84//4], result[0x8C//4] = 0xAFAC0058, 0x01802025
    for offset, expected, replacement in ((0xA8, 0xAFB00044, 0xAFB00040),
        (0xAC, 0xAFA20048, 0xAFA20044), (0xF8, 0xA3AD004C, 0xA3AD0048), (0x108, 0x27A50044, 0x27A50040)):
        assert result[offset//4] == expected, (offset, hex(result[offset//4]))
        result[offset//4] = replacement
    return result


def guard_rows(raw, relocations):
    normalized = normalize(raw)
    assert not any(relocations.get(offset) for offset in range(0, 320, 4) if raw[offset//4] != normalized[offset//4])
    return [dict(filename='game_16EE20', function=FUNCTION, offset='0x%X'%offset,
        expected='0x%08X'%raw[offset//4], replacement='0x%08X'%normalized[offset//4],
        expected_relocations='-', replacement_relocations='-',
        note='Normalize effect updater closed register schedule and private payload/cursor homes',
        insert_after='', insert_after_relocations='', omit='false')
        for offset in range(0, 320, 4) if raw[offset//4] != normalized[offset//4]]


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-effect-record-updater'; output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name+'-'+profile, body, profile)
            records.append(record); print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    (output/'measurements.json').write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__': main()
