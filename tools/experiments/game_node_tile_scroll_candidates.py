"""Fit the fourth tile-size command's signed one-step coordinate scrolling."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x150334B8, 0x60968, 68
FUNCTION = 'func_150334B8'
STUB = 's32 func_150334B8() {\n    return 0;\n}'
SELECTED = '''s32 func_150334B8(u8 *node, u8 *actor) {
    Gfx *commands;
    s32 remaining;
    s32 shift;
    s32 index;
    s32 first;
    s32 last;
    s32 original_s;
    s32 original_t;
    s32 span_s;
    s32 span_t;
    s32 wrapped_s;
    s32 wrapped_t;

    commands = 0;
    remaining = 0;
    shift = 0;
    if (node[1] == 0x37) {
        commands = *(Gfx **)*(u8 **)(node + 0x24);
        remaining = 4;
        shift = -100;
    }
    if (commands == 0) {
        return 0;
    }
    index = 0;
    if (remaining != 0) {
        do {
            remaining--;
            while (*(s8 *)&commands[index] != (s8)G_SETTILESIZE) {
                index++;
            }
            if (remaining != 0) {
                index++;
            }
        } while (remaining != 0);
    }
    first = commands[index].words.w0;
    last = commands[index].words.w1;
    original_s = ((first >> 12) & 0xFFF) + shift;
    span_s = ((last >> 12) & 0xFFF) + 2;
    original_t = first & 0xFFF;
    wrapped_s = original_s;
    wrapped_t = original_t;
    if (original_s >= span_s) {
        wrapped_s = original_s - span_s;
    }
    if (wrapped_s < 0) {
        wrapped_s += span_s;
    }
    span_t = (last & 0xFFF) + 2;
    if (original_t >= span_t) {
        wrapped_t = original_t - span_t;
    }
    if (wrapped_t < 0) {
        wrapped_t += span_t;
    }
    commands[index].words.w0 = _SHIFTL(G_SETTILESIZE, 24, 8) |
        _SHIFTL(wrapped_s, 12, 12) | (wrapped_t & 0xFFF);
    return 0;
}'''

EARLY_RETURN = SELECTED
opening, processing = SELECTED.split('    if (commands == 0) {\n        return 0;\n    }\n',1)
processing = processing.rsplit('    return 0;\n}',1)[0]
SELECTED = opening+'    if (commands != 0) {\n'+''.join('    '+line+'\n' for line in processing.splitlines())+'    }\n    return 0;\n}'
SEPARATE_COPIES = SELECTED
SELECTED = SELECTED.replace('''        original_s = ((first >> 12) & 0xFFF) + shift;
        span_s = ((last >> 12) & 0xFFF) + 2;
        original_t = first & 0xFFF;
        wrapped_s = original_s;
        wrapped_t = original_t;
''', '''        span_s = ((last >> 12) & 0xFFF) + 2;
        original_s = wrapped_s = ((first >> 12) & 0xFFF) + shift;
        original_t = wrapped_t = first & 0xFFF;
''')


def candidates():
    yield 'selected',SELECTED
    yield 'separate-copies',SEPARATE_COPIES
    yield 'early-return',EARLY_RETURN
    yield 'register-arguments',SELECTED.replace('u8 *node, u8 *actor',
        'register u8 *node, register u8 *actor')
    yield 'unsigned-command-words',SELECTED.replace('    s32 first;', '    u32 first;').replace(
        '    s32 last;', '    u32 last;')
    yield 'for-countdown',SELECTED.replace('            do {\n                remaining--;',
        '            for (; remaining != 0;) {\n                remaining--;').replace('            } while (remaining != 0);','            }')
    yield 'negative-wrong-action',SELECTED.replace('node[1] == 0x37','node[1] == 0x36')
    yield 'negative-third-command',SELECTED.replace('remaining = 4;', 'remaining = 3;')
    yield 'negative-zero-shift',SELECTED.replace('shift = -100;', 'shift = 0;')
    yield 'negative-minus99',SELECTED.replace('shift = -100;', 'shift = -99;')
    yield 'negative-plus3-spans',SELECTED.replace(' + 2;', ' + 3;')
    yield 'negative-signed-opcode',SELECTED.replace('(s8)G_SETTILESIZE', 'G_SETTILESIZE')
    yield 'negative-no-store',SELECTED.replace('    commands[index].words.w0 =', '    first =')
    yield 'negative-strict-boundaries',SELECTED.replace(' >= ', ' > ')
    yield 'negative-repeated-wrap',SELECTED.replace('if (original_s >= span_s)',
        'while (wrapped_s >= span_s)').replace('wrapped_s = original_s - span_s;',
        'wrapped_s -= span_s;').replace('if (wrapped_s < 0)', 'while (wrapped_s < 0)').replace(
        'if (original_t >= span_t)', 'while (wrapped_t >= span_t)').replace(
        'wrapped_t = original_t - span_t;', 'wrapped_t -= span_t;').replace(
        'if (wrapped_t < 0)', 'while (wrapped_t < 0)')


def compile_candidate(root, out, name, body=SELECTED, profile='o2g3'):
    out.mkdir(exist_ok=True)
    source, obj, elf = (out / (name+suffix) for suffix in ('.c','.o','.elf'))
    source.write_text('#include <ultra64.h>\n'+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc','-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
        '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32',
        '-I','conker/include','-I','conker/include/2.0L','-I','conker/include/2.0L/PR',
        '-D_LANGUAGE_C','-D_FINALROM','-DF3DEX_GBI_2','-D_MIPS_SZLONG=32',*PROFILES[profile],
        '-o',str(obj.relative_to(root)),str(source.relative_to(root))],cwd=root,capture_output=True,text=True)
    if result.returncode or result.stdout or result.stderr:
        raise ValueError(result.stdout+result.stderr)
    script = out / 'tile-scroll.ld'
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % ENTRY)
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',FUNCTION,
        '-o',str(elf),str(obj)],check=True,capture_output=True)
    _,functions,relocs = parse_object(obj)
    meta,pools = functions[FUNCTION],sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size']//4),pools['.text'][1],meta['value']))
    end = max(i for i,word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % WORDS,(root / 'conker/conker.us.bin').read_bytes(),ROM)
    frames = [(-word)&65535 for word in words if word&0xFFFF0000 == 0x27BD0000 and word&0x8000]
    return dict(name=name,profile=profile,body_words=end,frame=frames[0] if frames else 0,
        differences=sum(a != b for a,b in itertools.zip_longest(words,retail,fillvalue=0)),
        diagnostics='',relocations=relocs,pool_bytes=sum(len(v[1]) for n,v in pools.items()
            if n in ('.rodata','.data'))),words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profiles',action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-node-tile-scroll'
    forms = [('profile-'+p,SELECTED,p) for p in PROFILES] if args.profiles else (
        [(name,body,'o2g3') for name,body in candidates()])
    records = []
    for name,body,profile in forms:
        record,_ = compile_candidate(root,out,name,body,profile)
        records.append(record)
        print(name,record['body_words'],hex(record['frame']),record['differences'],record['pool_bytes'],flush=True)
    (out / ('profiles.json' if args.profiles else 'measurements.json')).write_text(json.dumps(records,indent=2)+'\n')


if __name__ == '__main__':
    main()
