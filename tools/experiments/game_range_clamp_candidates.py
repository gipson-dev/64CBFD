"""Range ordering/clamping with the original live XOR stores and saved pointers."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15143D18, 0x1711C8, 36
FUNCTION = 'func_15143D18'
PROTOTYPE = 'void func_15143D18(s32 *arg0, s32 *arg1, s32 arg2, s32 arg3);'
SELECTED = '''void func_15143D18(s32 *arg0, s32 *arg1, s32 arg2, s32 arg3) {
    s32 value1;
    s32 value0;

    if (arg3 < arg2) {
        s32 tmp;
        s32 newArg3;

        tmp = arg2 ^ arg3;
        newArg3 = arg3 ^ tmp;
        arg3 = newArg3;
        arg2 = tmp ^ newArg3;
    }

    value1 = *arg1;
    value0 = *arg0;
    if (value1 < value0) {
        s32 tmp;

        tmp = value0 ^ value1;
        *arg0 = tmp;
        value1 = *arg1 ^ tmp;
        *arg1 = value1;
        value0 = *arg0 ^ value1;
        *arg0 = value0;
    }

    if (value0 < arg2) {
        *arg0 = arg2;
    }
    if (arg3 < *arg1) {
        *arg1 = arg3;
    }
}'''
BASELINE = SELECTED.replace('    s32 value1;', '    s32 *ptr1;\n    s32 *ptr0;\n    s32 value1;').replace(
    '    if (arg3 < arg2)', '    ptr1 = arg1;\n    ptr0 = arg0;\n    if (arg3 < arg2)').replace('*arg0 =', '*ptr0 =').replace(
    '*arg1 =', '*ptr1 =').replace('= *arg0', '= *ptr0').replace('= *arg1', '= *ptr1').replace('arg3 < *arg1', 'arg3 < *ptr1')


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj = (output / (name + suffix) for suffix in ('.c', '.o'))
    source.write_text('#include <ultra64.h>\n' + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics: raise ValueError(diagnostics)
    text, functions, relocs = parse_object(obj)
    target = functions[FUNCTION]
    words = list(struct.unpack_from('>%dI' % (target['size'] // 4), text, target['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:]); words = words[:end]
    retail = struct.unpack_from('>36I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frame = (-words[0]) & 65535 if words[0] & 0xFFFF0000 == 0x27BD0000 else 0
    return dict(name=name, profile=profile, body_words=end, frame=frame, diagnostics=diagnostics,
        relocations=relocs, differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0))), words


def owner_guards():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-range-clamp'; output.mkdir(exist_ok=True)
    _, words = compile_candidate(root, output, 'guard-source')
    retail = struct.unpack_from('>36I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    return [dict(filename='game_16EE20', function=FUNCTION, offset='0x%X' % (i * 4),
        expected='0x%08X' % a, replacement='0x%08X' % b, expected_relocations='-', replacement_relocations='-',
        note='Normalize range clamp temporary register allocation', insert_after='',
        insert_after_relocations='', omit='false')
        for i, (a, b) in enumerate(zip(words, retail)) if a != b]


def main():
    root=Path(__file__).resolve().parents[2]
    output=root/'conker/build/game-range-clamp';output.mkdir(exist_ok=True)
    records=[]
    for name,body in (('baseline',BASELINE),('selected',SELECTED)):
        for profile in PROFILES:
            record,_=compile_candidate(root,output,name+'-'+profile,body,profile)
            records.append(record)
            print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    (output/'measurements.json').write_text(json.dumps(records,indent=2)+'\n')


if __name__ == '__main__':main()
