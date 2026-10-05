"""Screen the live actor pass and its captured predecessor ordering."""

import argparse
import itertools
import json
import re
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_update_dispatch_candidates import DECLARATIONS as ACTOR_DECLARATIONS
from tools.match_progress import load_elf_functions

DECLARATIONS = ACTOR_DECLARATIONS + '''
extern ActorUpdate58F80 D_800CC2D0[26];
extern ActorUpdate58F80 D_800D121C[];
extern u32 D_800C3E74;
extern u8 D_800C3E90, D_800C3E70, D_800BEAC0;
void func_1502BD84(ActorUpdate58F80 *actor, s32 slot);
void func_1503F964(void);
s32 func_1502F3C8();
s32 func_1502F948();
s32 func_15030468();
s32 func_1507C22C();
'''
BASELINE = '''void func_1502BEE4(void) {
    u8 depths[25];
    u8 ordered[25];
    ActorUpdate58F80 *actor;
    ActorUpdate58F80 *cursor;
    s32 slot, level, maxDepth, count, index;

    func_1503F964();
    D_800C3E90 = 0;
    D_800C3E74 = 0;
    maxDepth = 0;
    for (actor = D_800CC2D0; actor < D_800D121C; actor++) {
        if (actor->maskId != 0) {
            D_800C3E74 |= 1u << ((actor->maskId + 31) & 31);
        }
    }
    bzero(depths, 25);
    for (slot = 0, actor = D_800CC2D0; slot < 25; slot++, actor++) {
        if (actor->active == 0) {
            continue;
        }
        if (actor->predecessor != 0) {
            cursor = actor;
            depths[slot] = 0;
            while (cursor->predecessor != 0) {
                depths[slot]++;
                cursor = D_800CC2D0 + cursor->predecessor - 1;
            }
            if (maxDepth < depths[slot]) {
                maxDepth = depths[slot];
            }
        } else {
            func_1502BD84(actor, slot);
        }
    }
    count = 0;
    if (maxDepth != 0) {
        for (level = 1; level <= maxDepth; level++) {
            for (slot = 0; slot < 25; slot++) {
                if (depths[slot] == level) {
                    ordered[count++] = slot;
                }
            }
        }
        for (index = 0; index < count; index++) {
            func_1502BD84(D_800CC2D0 + ordered[index], ordered[index]);
        }
    }
    func_1502F3C8();
    for (actor = D_800CC2D0; actor != D_800D121C; actor++) {
        if (actor->active != 0) {
            func_1502F948(actor);
        }
    }
    func_15030468();
    if (D_800BEAC0 == 0) {
        func_1507C22C(0);
    }
    D_800C3E70 = 0;
}'''


def candidates():
    forms = [('baseline', BASELINE)]
    for a in (25, 26, 28, 32):
        for b in (25, 26, 28, 32, 40, 48):
            forms.append((f'arrays-{a}-{b}', BASELINE.replace('depths[25]', f'depths[{a}]')
                          .replace('ordered[25]', f'ordered[{b}]')))
    for name, before, after in (
            ('subtract-index', 'D_800CC2D0 + cursor->predecessor - 1',
             'D_800CC2D0 + (cursor->predecessor - 1)'),
            ('count-not-equal', 'index < count', 'index != count'),
            ('slot-not-equal', 'slot < 25', 'slot != 25'),
            ('level-not-equal', 'level <= maxDepth', 'level != maxDepth + 1'),
            ('base-end', 'D_800D121C', '(D_800CC2D0 + 25)'),
            ('wrong-shift-negative-control', '((actor->maskId + 31) & 31)', '(actor->maskId & 31)'),
            ('wrong-recheck-negative-control',
             '            func_1502BD84(D_800CC2D0 + ordered[index], ordered[index]);',
             '            if (D_800CC2D0[ordered[index]].active)\n'
             '                func_1502BD84(D_800CC2D0 + ordered[index], ordered[index]);')):
        forms.append((name, BASELINE.replace(before, after)))
    shape = BASELINE.replace('    u8 depths[25];\n    u8 ordered[25];',
                             '    u8 ordered[25];\n    u8 depths[25];')
    shape = shape.replace('    for (actor = D_800CC2D0; actor < D_800D121C; actor++) {',
                          '    actor = D_800CC2D0;\n    do {').replace(
        '    bzero(depths, 25);',
        '    bzero(depths, 25);')
    shape = shape.replace('    }\n    bzero(depths, 25);',
                          '        actor++;\n    } while (actor < D_800D121C);\n    bzero(depths, 25);')
    shape = shape.replace('    for (actor = D_800CC2D0; actor != D_800D121C; actor++) {',
                          '    actor = D_800CC2D0;\n    do {').replace(
        '    }\n    func_15030468();',
        '        actor++;\n    } while (actor != D_800D121C);\n    func_15030468();')
    for subtract in (False, True):
        for cached_link in (False, True):
            body = shape
            if subtract:
                body = body.replace('D_800CC2D0 + cursor->predecessor - 1',
                                    'D_800CC2D0 + (cursor->predecessor - 1)')
            if cached_link:
                body = body.replace('s32 slot, level, maxDepth, count, index;',
                                    's32 slot, level, maxDepth, count, index, link;').replace(
                    'while (cursor->predecessor != 0)',
                    'while ((link = cursor->predecessor) != 0)').replace(
                    'D_800CC2D0 + cursor->predecessor - 1', 'D_800CC2D0 + link - 1').replace(
                    'D_800CC2D0 + (cursor->predecessor - 1)', 'D_800CC2D0 + (link - 1)')
            forms.append((f'do-reversed-{int(subtract)}-{int(cached_link)}', body))
    shape = shape.replace('D_800D121C', '(D_800CC2D0 + 25)')
    shape = shape.replace('    u8 ordered[25];\n    u8 depths[25];',
                          '    u8 depths[25];\n    u8 ordered[25];')
    shape = shape.replace('for (level = 1; level <= maxDepth; level++)',
                          'for (slot = 1; slot <= maxDepth; slot++)').replace(
        'for (slot = 0; slot < 25; slot++)', 'for (index = 0; index < 25; index++)').replace(
        'if (depths[slot] == level)', 'if (depths[index] == slot)').replace(
        'ordered[count++] = slot;', 'ordered[count++] = index;').replace(
        'for (index = 0; index < count; index++)', 'for (slot = 0; slot < count; slot++)').replace(
        'ordered[index], ordered[index]', 'ordered[slot], ordered[slot]').replace(
        's32 slot, level, maxDepth, count, index;', 's32 slot, maxDepth, count, index;')
    shape = shape.replace('    for (slot = 0, actor = D_800CC2D0; slot < 25; slot++, actor++) {',
                          '    slot = 0;\n    actor = D_800CC2D0;\n    do {').replace(
        '        if (actor->active == 0) {\n            continue;\n        }\n',
        '        if (actor->active != 0) {\n').replace(
        '    }\n    count = 0;',
        '        }\n        slot++;\n        actor++;\n    } while (slot < 25);\n    count = 0;')
    for subtract in (False, True):
        for cached_link in (False, True):
            for masked in (False, True):
                body = shape
                if subtract:
                    body = body.replace('D_800CC2D0 + cursor->predecessor - 1',
                                        'D_800CC2D0 + (cursor->predecessor - 1)')
                if cached_link:
                    body = body.replace('s32 slot, maxDepth, count, index;',
                                        's32 slot, maxDepth, count, index, link;').replace(
                        'while (cursor->predecessor != 0)', 'while ((link = cursor->predecessor) != 0)').replace(
                        'D_800CC2D0 + cursor->predecessor - 1', 'D_800CC2D0 + link - 1').replace(
                        'D_800CC2D0 + (cursor->predecessor - 1)', 'D_800CC2D0 + (link - 1)')
                if not masked:
                    body = body.replace('((actor->maskId + 31) & 31)', '(actor->maskId + 31)')
                forms.append((f'fixed-do-{int(subtract)}-{int(cached_link)}-{int(masked)}', body))
    shape = dict(forms)['fixed-do-1-0-1']
    for arrays_first in (False, True):
        for reverse_arrays in (False, True):
            for advance_first in (False, True):
                for external_end in (False, True):
                    body = shape
                    if not arrays_first:
                        body = body.replace('    u8 depths[25];\n    u8 ordered[25];\n', '').replace(
                            '    s32 slot, maxDepth, count, index;',
                            '    s32 slot, maxDepth, count, index;\n    u8 depths[25];\n    u8 ordered[25];')
                    if reverse_arrays:
                        body = body.replace('    u8 depths[25];\n    u8 ordered[25];',
                                            '    u8 ordered[25];\n    u8 depths[25];')
                    if advance_first:
                        body = body.replace('                depths[slot]++;\n'
                                            '                cursor = D_800CC2D0 + (cursor->predecessor - 1);',
                                            '                cursor = D_800CC2D0 + (cursor->predecessor - 1);\n'
                                            '                depths[slot]++;')
                    if external_end:
                        body = body.replace('(D_800CC2D0 + 25)', 'D_800D121C')
                    forms.append((f'layout-{int(arrays_first)}-{int(reverse_arrays)}-'
                                  f'{int(advance_first)}-{int(external_end)}', body))
    return forms


def compile_candidate(root, output, name, source):
    conker = root / 'conker'
    path = output / (name + '.c')
    obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
    path.write_text('#include <ultra64.h>\n' + DECLARATIONS + '\n' + source + '\n')
    command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
               '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
               '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32',
               '-woff', '649,838']
    for include in ('.', 'include', 'include/2.0L', 'include/2.0L/PR', 'include/libc'):
        command += ['-I', include]
    command += ['-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)),
                str(path.relative_to(conker))]
    result = subprocess.run(command, cwd=conker, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1502BEE4 : SUBALIGN(4) { *(.text) } }\n')
    symbols = {name: int(name[5:], 16) for name in (
        'func_1502BD84', 'func_1503F964', 'func_1502F3C8', 'func_1502F948',
        'func_15030468', 'func_1507C22C')}
    symbols.update(D_800CC2D0=0x800CC2D0, D_800D121C=0x800D121C,
                   D_800C3E74=0x800C3E74, D_800C3E90=0x800C3E90,
                   D_800C3E70=0x800C3E70, D_800BEAC0=0x800BEAC0, bzero=0x100226F0)
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
                    '-e', 'func_1502BEE4',
                    *['--defsym=' + symbol + '=' + hex(value) for symbol, value in symbols.items()],
                    '-o', str(elf), str(obj)], check=True, capture_output=True)
    functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
    words = functions['func_1502BEE4']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 176 - size)
    retail = struct.unpack_from('>176I', (conker / 'conker.us.bin').read_bytes(), 0x59394)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    record = dict(name=name, body_words=size, frame=(-words[0]) & 0xFFFF,
                  real_differences=len(differences) + max(0, size - 176),
                  differences=differences, diagnostics=result.stdout + result.stderr)
    return record, slot


RECOVERY = '''void func_1502BEE4(void) {
    ActorUpdate58F80 *actor;
    ActorUpdate58F80 *cursor;
    s32 slot, maxDepth, count, index;
    u8 depths[25];
    u8 ordered[25];

    func_1503F964();
    D_800C3E90 = 0;
    D_800C3E74 = 0;
    maxDepth = 0;
    actor = D_800CC2D0;
    do {
        if (actor->maskId != 0) {
            D_800C3E74 |= 1u << ((actor->maskId + 31) & 31);
        }
        actor++;
    } while (actor < (D_800CC2D0 + 25));
    bzero(depths, 25);
    slot = 0;
    actor = D_800CC2D0;
    do {
        if (actor->active != 0) {
            if (actor->predecessor != 0) {
                cursor = actor;
                depths[slot] = 0;
                while (cursor->predecessor != 0) {
                    cursor = D_800CC2D0 + (cursor->predecessor - 1);
                    depths[slot]++;
                }
                if (maxDepth < depths[slot]) {
                    maxDepth = depths[slot];
                }
            } else {
                func_1502BD84(actor, slot);
            }
        }
        slot++;
        actor++;
    } while (slot < 25);
    count = 0;
    if (maxDepth != 0) {
        for (slot = 1; slot <= maxDepth; slot++) {
            for (index = 0; index < 25; index++) {
                if (depths[index] == slot) {
                    ordered[count++] = index;
                }
            }
        }
        for (slot = 0; slot < count; slot++) {
            func_1502BD84(D_800CC2D0 + ordered[slot], ordered[slot]);
        }
    }
    func_1502F3C8();
    actor = D_800CC2D0;
    do {
        if (actor->active != 0) {
            func_1502F948(actor);
        }
        actor++;
    } while (actor != (D_800CC2D0 + 25));
    func_15030468();
    if (D_800BEAC0 == 0) {
        func_1507C22C(0);
    }
    D_800C3E70 = 0;
}'''


def production_body():
    return SELECTED.replace('D_800CC2D0', '((ActorUpdate58F80 *)D_800CC2D0)')


def followup_candidates():
    """Separate local-storage experiments after the semantic checkpoint."""
    forms = []
    for pointers in (False, True):
        for scalars in (False, True):
            body = RECOVERY
            if pointers:
                body = body.replace('    ActorUpdate58F80 *', '    register ActorUpdate58F80 *')
            if scalars:
                body = body.replace('    s32 slot, maxDepth, count, index;',
                                    '    register s32 slot, maxDepth, count, index;')
            forms.append((f'register-locals-{int(pointers)}-{int(scalars)}', body))
    for depth_size in (25, 28):
        for ordering in ('depth-first', 'queue-first'):
            fields = ('u8 depths[%d]; u8 ordered[25];' % depth_size if ordering == 'depth-first'
                      else 'u8 ordered[25]; u8 depths[%d];' % depth_size)
            body = RECOVERY.replace('    u8 depths[25];\n    u8 ordered[25];',
                                    '    struct { ' + fields + ' } scratch;')
            body = body.replace('bzero(depths,', 'bzero(scratch.depths,').replace(
                'depths[slot]', 'scratch.depths[slot]').replace(
                'depths[index]', 'scratch.depths[index]').replace(
                'ordered[count++]', 'scratch.ordered[count++]').replace(
                'ordered[slot]', 'scratch.ordered[slot]')
            forms.append((f'scratch-{depth_size}-{ordering}', body))
    return forms


def schedule_candidates():
    forms = []
    chain = '''                cursor = actor;
                depths[slot] = 0;
                while (cursor->predecessor != 0) {
                    cursor = D_800CC2D0 + (cursor->predecessor - 1);
                    depths[slot]++;
                }'''
    chains = [
        ('while', chain),
        ('clear-first', chain.replace('                cursor = actor;\n                depths[slot] = 0;',
                                     '                depths[slot] = 0;\n                cursor = actor;')),
        ('for', '''                for (cursor = actor, depths[slot] = 0;
                     cursor->predecessor != 0; depths[slot]++) {
                    cursor = D_800CC2D0 + (cursor->predecessor - 1);
                }'''),
        ('do', '''                cursor = actor;
                depths[slot] = 0;
                do {
                    cursor = D_800CC2D0 + (cursor->predecessor - 1);
                    depths[slot]++;
                } while (cursor->predecessor != 0);''')]
    for name, replacement in chains:
        for reverse in (False, True):
            for post_end in (False, True):
                body = RECOVERY.replace(chain, replacement)
                if reverse:
                    body = body.replace('    u8 depths[25];\n    u8 ordered[25];',
                                        '    u8 ordered[25];\n    u8 depths[25];')
                if post_end:
                    body = body.replace('    } while (actor != (D_800CC2D0 + 25));',
                                        '    } while (actor != D_800D121C);')
                forms.append((f'phase-{name}-{int(reverse)}-{int(post_end)}', body))
    for reverse in (False, True):
        for for_loop in (False, True):
            body = RECOVERY.replace('    s32 slot, maxDepth, count, index;',
                                    '    s32 slot, maxDepth, count, index;\n    u8 *depth;')
            replacement = chain.replace('                cursor = actor;',
                                        '                cursor = actor;\n                depth = depths + slot;').replace(
                'depths[slot]', '(*depth)')
            if for_loop:
                replacement = '''                depth = depths + slot;
                for (cursor = actor, *depth = 0;
                     cursor->predecessor != 0; (*depth)++) {
                    cursor = D_800CC2D0 + (cursor->predecessor - 1);
                }'''
            body = body.replace(chain, replacement).replace('if (maxDepth < depths[slot])',
                                                             'if (maxDepth < *depth)').replace(
                'maxDepth = depths[slot];', 'maxDepth = *depth;')
            if reverse:
                body = body.replace('    u8 depths[25];\n    u8 ordered[25];',
                                    '    u8 ordered[25];\n    u8 depths[25];')
            forms.append((f'depth-pointer-{int(reverse)}-{int(for_loop)}', body))
    return forms


def declaration_candidates():
    forms = []
    base = RECOVERY.replace('    u8 depths[25];\n    u8 ordered[25];',
                            '    u8 ordered[25];\n    u8 depths[25];').replace(
        '    } while (actor != (D_800CC2D0 + 25));', '    } while (actor != D_800D121C);')
    for ordering in itertools.permutations(('slot', 'maxDepth', 'count', 'index')):
        for reverse_pointers in (False, True):
            body = base.replace('    s32 slot, maxDepth, count, index;',
                                '    s32 ' + ', '.join(ordering) + ';')
            if reverse_pointers:
                body = body.replace('    ActorUpdate58F80 *actor;\n    ActorUpdate58F80 *cursor;',
                                    '    ActorUpdate58F80 *cursor;\n    ActorUpdate58F80 *actor;')
            forms.append(('declarations-' + '-'.join(ordering) + '-' + str(int(reverse_pointers)), body))
    return forms


def interleave_candidates():
    header = '''    ActorUpdate58F80 *actor;
    ActorUpdate58F80 *cursor;
    s32 slot, maxDepth, count, index;
    u8 depths[25];
    u8 ordered[25];'''
    base = RECOVERY.replace('    } while (actor != (D_800CC2D0 + 25));',
                            '    } while (actor != D_800D121C);')
    forms = []
    for cut in (3, 2, 1):
        for ordering in itertools.permutations(('slot', 'maxDepth', 'count', 'index')):
            lines = ['    ActorUpdate58F80 *actor;', '    ActorUpdate58F80 *cursor;']
            lines += ['    s32 ' + name + ';' for name in ordering[:cut]]
            lines += ['    u8 ordered[25];', '    u8 depths[25];']
            lines += ['    s32 ' + name + ';' for name in ordering[cut:]]
            forms.append(('interleave-' + str(cut) + '-' + '-'.join(ordering),
                          base.replace(header, '\n'.join(lines))))
    return forms


def workspace_candidates():
    forms = []
    for grouped_arrays in (False, True):
        for before in (False, True):
            for external_end in (False, True):
                lines = ['    ActorUpdate58F80 *actor;', '    ActorUpdate58F80 *cursor;',
                         '    s32 slot, index;']
                fields = 's32 maxDepth; s32 count;'
                if grouped_arrays:
                    fields += ' u8 depths[28]; u8 ordered[25];'
                record = '    struct { ' + fields + ' } scratch;'
                arrays = [] if grouped_arrays else ['    u8 ordered[25];', '    u8 depths[25];']
                lines += ([record] + arrays) if before else (arrays + [record])
                declarations = '\n'.join(lines)
                commands = RECOVERY[RECOVERY.index('\n\n    func_1503F964();'):]
                for name in ('maxDepth', 'count') + (('depths', 'ordered') if grouped_arrays else ()):
                    commands = re.sub(r'\b' + name + r'\b', 'scratch.' + name, commands)
                body = 'void func_1502BEE4(void) {\n' + declarations + commands
                if external_end:
                    body = body.replace('    } while (actor != (D_800CC2D0 + 25));',
                                        '    } while (actor != D_800D121C);')
                forms.append((f'workspace-{int(grouped_arrays)}-{int(before)}-{int(external_end)}', body))
    return forms


def cursor_candidates():
    header = '''    ActorUpdate58F80 *actor;
    ActorUpdate58F80 *cursor;
    s32 slot, maxDepth, count, index;
    u8 depths[25];
    u8 ordered[25];'''
    body = RECOVERY.replace('cursor = actor;', 'cursor = (u8 *)actor;').replace(
        'cursor->predecessor', '((ActorUpdate58F80 *)cursor)->predecessor').replace(
        'cursor = D_800CC2D0 + (((ActorUpdate58F80 *)cursor)->predecessor - 1);',
        'cursor = (u8 *)(D_800CC2D0 + (((ActorUpdate58F80 *)cursor)->predecessor - 1));')
    body = body.replace('''            for (index = 0; index < 25; index++) {
                if (depths[index] == slot) {
                    ordered[count++] = index;
                }
            }''', '''            for (cursor = depths; cursor < depths + 25; cursor++) {
                if (*cursor == slot) {
                    ordered[count++] = cursor - depths;
                }
            }''').replace('    } while (actor != (D_800CC2D0 + 25));',
                         '    } while (actor != D_800D121C);')
    forms = []
    for cut in range(4):
        for ordering in itertools.permutations(('slot', 'maxDepth', 'count')):
            lines = ['    ActorUpdate58F80 *actor;', '    u8 *cursor;']
            lines += ['    s32 ' + name + ';' for name in ordering[:cut]]
            lines += ['    u8 ordered[25];', '    u8 depths[25];']
            lines += ['    s32 ' + name + ';' for name in ordering[cut:]]
            forms.append(('cursor-' + str(cut) + '-' + '-'.join(ordering),
                          body.replace(header, '\n'.join(lines))))
    return forms


SELECTED = dict(interleave_candidates())['interleave-3-slot-maxDepth-index-count']


def lifetime_candidates():
    header = '''    ActorUpdate58F80 *actor;
    ActorUpdate58F80 *cursor;
    s32 slot, maxDepth, count, index;
    u8 depths[25];
    u8 ordered[25];'''
    chain = '''                cursor = actor;
                depths[slot] = 0;
                while (cursor->predecessor != 0) {
                    cursor = D_800CC2D0 + (cursor->predecessor - 1);
                    depths[slot]++;
                }'''
    forms = []
    for mode in ('actor', 'index'):
        for index_type in ('s32', 's16', 'u8'):
            for max_after in (False, True):
                for counter_order in (False, True):
                    body = RECOVERY
                    if mode == 'actor':
                        body = body.replace(chain, chain.replace('                cursor = actor;\n', '').replace('cursor', 'actor'))
                        body = body.replace('''    slot = 0;
    actor = D_800CC2D0;
    do {''', '''    for (slot = 0; slot < 25; slot++) {
        actor = D_800CC2D0 + slot;''').replace('''        slot++;
        actor++;
    } while (slot < 25);''', '    }')
                    else:
                        replacement = '''                index = slot;
                depths[slot] = 0;
                while (D_800CC2D0[index].predecessor != 0) {
                    index = D_800CC2D0[index].predecessor - 1;
                    depths[slot]++;
                }'''
                        body = body.replace(chain, replacement)
                    lines = ['    ActorUpdate58F80 *actor;', '    s32 slot;',
                             '    ' + index_type + ' index;']
                    if not max_after:
                        lines.append('    s32 maxDepth;')
                    lines += ['    u8 ordered[25];', '    u8 depths[25];']
                    counters = ['    s32 maxDepth;', '    s32 count;'] if max_after else ['    s32 count;']
                    lines += list(reversed(counters)) if counter_order else counters
                    body = body.replace(header, '\n'.join(lines)).replace(
                        '    } while (actor != (D_800CC2D0 + 25));', '    } while (actor != D_800D121C);')
                    forms.append((f'lifetime-{mode}-{index_type}-{int(max_after)}-{int(counter_order)}', body))
    return forms


def scope_candidates():
    header = '''    ActorUpdate58F80 *actor;
    ActorUpdate58F80 *cursor;
    s32 slot, maxDepth, count, index;
    u8 depths[25];
    u8 ordered[25];'''
    forms = []
    for indexed in (False, True):
        for max_after in (False, True):
            for reverse in (False, True):
                body = RECOVERY.replace('''            if (actor->predecessor != 0) {
                cursor = actor;''', '''            if (actor->predecessor != 0) {
                ActorUpdate58F80 *cursor = actor;''')
                if indexed:
                    before = '''    slot = 0;
    actor = D_800CC2D0;
    do {'''
                    start, sep, remainder = body.partition(before)
                    region, ending, suffix = remainder.partition('''        slot++;
        actor++;
    } while (slot < 25);''')
                    assert sep and ending
                    region = region.replace('actor->', 'D_800CC2D0[slot].').replace(
                        '*cursor = actor;', '*cursor = D_800CC2D0 + slot;').replace(
                        'func_1502BD84(actor, slot);', 'func_1502BD84(D_800CC2D0 + slot, slot);')
                    body = start + '    for (slot = 0; slot < 25; slot++) {' + region + '    }' + suffix
                lines = ['    ActorUpdate58F80 *actor;', '    s32 slot, index;']
                if not max_after:
                    lines.append('    s32 maxDepth;')
                lines += ['    u8 ordered[25];', '    u8 depths[25];']
                counters = ['    s32 maxDepth;', '    s32 count;'] if max_after else ['    s32 count;']
                lines += list(reversed(counters)) if reverse else counters
                body = body.replace(header, '\n'.join(lines)).replace(
                    '    } while (actor != (D_800CC2D0 + 25));', '    } while (actor != D_800D121C);')
                forms.append((f'scope-{int(indexed)}-{int(max_after)}-{int(reverse)}', body))
    return forms


def pointer_home_candidates():
    header = '''    ActorUpdate58F80 *actor;
    ActorUpdate58F80 *cursor;
    s32 slot, maxDepth, count, index;
    u8 depths[25];
    u8 ordered[25];'''
    base = RECOVERY.replace('    } while (actor != (D_800CC2D0 + 25));',
                            '    } while (actor != D_800D121C);')
    declarations = {
        'actor': '    ActorUpdate58F80 *actor;',
        'cursor': '    ActorUpdate58F80 *cursor;',
        'arrays': '    u8 ordered[25];\n    u8 depths[25];',
        **{name: '    s32 ' + name + ';' for name in ('slot', 'index', 'maxDepth', 'count')},
    }
    forms = []
    for cursor_position in range(6):
        for ordering in itertools.permutations(('slot', 'index', 'maxDepth', 'count')):
            names = ['actor', *ordering[:2], 'arrays', *ordering[2:]]
            names.insert(cursor_position + 1, 'cursor')
            lines = '\n'.join(declarations[name] for name in names)
            forms.append(('pointer-home-' + str(cursor_position) + '-' + '-'.join(ordering),
                          base.replace(header, lines)))
    return forms


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    screens = {
        'initial': (candidates, 'screen.json'),
        'followup': (followup_candidates, 'followup-screen.json'),
        'schedule': (schedule_candidates, 'schedule-screen.json'),
        'declarations': (declaration_candidates, 'declaration-screen.json'),
        'interleave': (interleave_candidates, 'interleave-screen.json'),
        'workspace': (workspace_candidates, 'workspace-screen.json'),
        'cursor': (cursor_candidates, 'cursor-screen.json'),
        'lifetime': (lifetime_candidates, 'lifetime-screen.json'),
        'scope': (scope_candidates, 'scope-screen.json'),
        'pointer-home': (pointer_home_candidates, 'pointer-home-screen.json'),
    }
    for name in screens:
        if name != 'initial':
            group.add_argument('--' + name, dest='screen', action='store_const', const=name,
                               help='screen ' + name + ' forms')
    parser.set_defaults(screen='initial')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-update-pass'
    output.mkdir(exist_ok=True)
    records = []
    make_forms, filename = screens[args.screen]
    for name, body in make_forms():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / filename).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
