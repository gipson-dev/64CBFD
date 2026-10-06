"""Bound the grid updater's byte-loop and pointer/register lifetimes."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x151412BC, 0x16E76C, 96
SYMBOLS = dict(D_800DCE50=0x800DCE50, D_800DD190=0x800DD190,
               D_800A5168=0x800A5168, D_80082FA0=0x80082FA0,
               D_800BE620=0x800BE620, D_800BE624=0x800BE624,
               D_800BE9C4=0x800BE9C4)
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',)}
DECLARATIONS = '''extern u8 D_800DCE50[], D_800DD190;
extern s32 D_800A5168[], D_80082FA0, D_800BE620, D_800BE624;
extern u16 *D_800BE9C4;
typedef struct {
    u8 reserved[0x24];
    s32 x[4];
    s32 y[4];
    u8 gap[8];
    u16 value[4];
} GridPayload;
'''
LOCALS = {'row': 'u8 *row;', 'node': 'u8 *node;', 'payload': 'u8 *payload;',
          'bucket': 'u8 bucket;', 'channel': 'u8 channel;', 'x': 's32 x;',
          'y': 's32 y;', 'flags': 'u32 flags;'}
PAYLOAD_CONTROL = '''void func_151412BC(void) {
    u8 *row;
    u8 *node;
    u8 *payload;
    u8 bucket;
    u8 channel;
    s32 x;
    s32 y;
    u32 flags;
    row = D_800DCE50;
    do {
        bucket = 0;
        do {
            node = ((u8 **)row)[D_800A5168[bucket]];
            if (node != NULL) {
                do {
                    flags = *(u32 *)(node + 0x58);
                    if (flags & 0x2000) {
                        *(s16 *)(node + 0x162) = 0;
                        *(s16 *)(node + 0x160) = 0;
                        *(s16 *)(node + 0x15E) = 0;
                        *(s16 *)(node + 0x15C) = 0;
                        if (flags & 0x10) {
                            payload = node + 0x110;
                            for (channel = 0; channel <= D_80082FA0; channel++) {
                                x = *(s32 *)(payload + 0x24 + channel * 4);
                                if (x >= 0 && x < D_800BE620 &&
                                    (y = *(s32 *)(payload + 0x34 + channel * 4)) >= 0 && y < D_800BE624) {
                                    *(u16 *)(payload + 0x4C + channel * 2) = D_800BE9C4[y * D_800BE620 + x];
                                } else {
                                    *(u16 *)(payload + 0x4C + channel * 2) = 0x7FFF;
                                }
                            }
                        }
                    }
                    node = *(u8 **)(node + 8);
                } while (node != NULL);
            }
            bucket++;
        } while (bucket < 4);
        row += 0x1A0;
    } while (row != &D_800DD190);
}'''

SELECTED = PAYLOAD_CONTROL.replace('u8 channel;', 's32 channel;').replace(
    '                            payload =', '                            channel = 0;\n                            payload =').replace(
    '                            for (channel = 0; channel <= D_80082FA0; channel++) {',
    '                            if (D_80082FA0 >= 0) {\n                                do {').replace(
    '                            }\n                        }',
    '                                channel = (u8)(channel + 1);\n'
    '                                } while (channel <= D_80082FA0);\n                            }\n                        }')
SELECTED = SELECTED.replace(
    '                                x =', '                                    x =').replace(
    '                                if (x', '                                    if (x').replace(
    '                                    (y =', '                                        (y =').replace(
    '                                    *(u16 *)', '                                        *(u16 *)').replace(
    '                                } else {', '                                    } else {').replace(
    '                                }\n                                channel',
    '                                    }\n                                    channel')
OWNER_BODY = SELECTED.replace('D_800A5168[bucket]', '((s32 *)&D_800A5168)[bucket]').replace(
    'D_800BE9C4[y * D_800BE620 + x]', '(*(u16 **)&D_800BE9C4)[y * D_800BE620 + x]').replace(
    'row != &D_800DD190', 'row != (u8 *)&D_800DD190')


def candidates():
    declarations = '\n'.join('    '+value for value in LOCALS.values())
    for order in itertools.permutations(('row', 'node', 'bucket')):
        names = (*order, 'channel', 'payload', 'y', 'x', 'flags')
        body = PAYLOAD_CONTROL.replace(declarations, '\n'.join('    '+LOCALS[name] for name in names))
        for shape in ('payload', 'explicit-byte', 'direct-fields'):
            source = body
            if shape == 'explicit-byte':
                source = source.replace('channel++', 'channel = (u8)(channel + 1)')
            elif shape == 'direct-fields':
                source = source.replace('    u8 *payload;\n', '').replace(
                    '                            payload = node + 0x110;\n', '')
                for a, b in ((0x24, 0x134), (0x34, 0x144), (0x4C, 0x15C)):
                    source = source.replace('payload + 0x%X'%a, 'node + 0x%X'%b)
            for result in ('void', 'bucket'):
                variant = source
                if result == 'bucket':
                    variant = variant.replace('void func_', 's32 func_').replace(
                        '    } while (row != &D_800DD190);\n}',
                        '    } while (row != &D_800DD190);\n    return bucket;\n}')
                yield '-'.join((*order, shape, result)), variant


def loop_candidates():
    typed = PAYLOAD_CONTROL.replace('u8 *payload;', 'GridPayload *payload;').replace(
        'payload = node + 0x110;', 'payload = (GridPayload *)(node + 0x110);')
    for a, b in (('*(s32 *)(payload + 0x24 + channel * 4)', 'payload->x[channel]'),
                 ('*(s32 *)(payload + 0x34 + channel * 4)', 'payload->y[channel]'),
                 ('*(u16 *)(payload + 0x4C + channel * 2)', 'payload->value[channel]')):
        typed = typed.replace(a, b)
    for layout, body in (('byte-payload', PAYLOAD_CONTROL), ('typed-payload', typed)):
        for channel_type in ('u8', 's32', 'u32'):
            source = body.replace('u8 channel;', '%s channel;'%channel_type)
            for loop, update in (('increment', 'channel++'),
                                 ('cast', 'channel = (u8)(channel + 1)'),
                                 ('mask', 'channel = (channel + 1) & 255')):
                yield '%s-%s-%s'%(layout, channel_type, loop), source.replace('channel++', update)
        early = body.replace('                            payload =',
                             '                            channel = 0;\n                            payload =').replace(
            'for (channel = 0;', 'for (;')
        yield layout+'-early-byte', early
        for kind in ('u8', 's32'):
            source = early.replace('u8 channel;', '%s channel;'%kind)
            for shape in ('bottom-mask', 'bottom-comma', 'bottom-cast', 'bottom-assignment'):
                opening = '                            for (; channel <= D_80082FA0; channel++) {'
                closing = '                            }\n                        }'
                source_variant = source.replace(opening,
                    '                            if (D_80082FA0 >= 0) { do {')
                if shape == 'bottom-mask':
                    ending = '                                channel++;\n                            } while ((channel & 255) <= D_80082FA0 && (channel = (u8)channel, 1)); }'
                elif shape == 'bottom-comma':
                    ending = '                                channel++;\n                            } while ((channel = (u8)channel) <= D_80082FA0); }'
                elif shape == 'bottom-cast':
                    ending = '                                channel++;\n                            } while ((u8)channel <= D_80082FA0); }'
                else:
                    ending = '                                channel = (u8)(channel + 1);\n                            } while (channel <= D_80082FA0); }'
                yield '%s-%s-%s'%(layout, kind, shape), source_variant.replace(closing, ending+'\n                        }')


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3', declarations=DECLARATIONS):
    source, obj, elf = (output/(name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n'+declarations+body+'\n')
    command = ['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
               '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
               '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
               '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32',
               *PROFILES[profile], '-o', str(obj.relative_to(root)), str(source.relative_to(root))]
    result = subprocess.run(command, cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output/'grid-channel.ld'
    script.write_text('SECTIONS { .text 0x151412BC : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_151412BC',
                    *['--defsym=%s=0x%X'%item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
                   check=True, capture_output=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_151412BC']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>96I', (root/'conker/conker.us.bin').read_bytes(), ROM))
    slot = words+[0]*max(0, WORDS-end)
    differences = [(i*4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-word)&65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
                differences=len(differences)+max(0, end-WORDS), different_words=differences,
                exact=slot == retail, diagnostics=diagnostics), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', choices=tuple(PROFILES))
    parser.add_argument('--family', choices=('declarations', 'loops'), default='declarations')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-grid-channel-updater'
    output.mkdir(exist_ok=True)
    records = []
    for name, source in candidates() if args.family == 'declarations' else loop_candidates():
        for profile in (args.profile,) if args.profile else PROFILES:
            record, _ = compile_candidate(root, output, name+'-'+profile, source, profile)
            records.append(record)
            print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    (output/(args.family+'-measurements.json')).write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
