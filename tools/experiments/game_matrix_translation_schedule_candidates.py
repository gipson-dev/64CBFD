"""Measure typed matrix views and locally evidenced assembler schedule controls."""

import itertools
import json
from pathlib import Path

from tools.experiments import game_matrix_translation_candidates as screen

MATRIX_VIEW = '''typedef union {
    s16 half[2][4][4];
    f32 floating[4][4];
} TranslationMatrix;
typedef char TranslationMatrixSize[(sizeof(TranslationMatrix) == 64) ? 1 : -1];
'''


def typed_candidates():
    for kind, common, left in itertools.product(range(4), (False, True), (False, True)):
        body = screen.SELECTED
        declarations = screen.DECLARATIONS
        if common:
            body = body.replace('        ' + screen.ADDRESS + '\n', '')
            body = body.replace('    u8 *selected;', '    u8 *' + screen.ADDRESS)
        if kind == 0:
            body = body.replace('u8 *selected', 'TranslationMatrix *selected')
            body = body.replace('selected = (u8 *)', 'selected = (TranslationMatrix *)')
            declarations += MATRIX_VIEW
        elif kind == 1:
            body = body.replace('u8 *selected', 's16 *selected').replace('selected = (u8 *)', 'selected = (s16 *)')
        elif kind == 2:
            body = body.replace('u8 *selected', 'f32 (*selected)[4]').replace('selected = (u8 *)', 'selected = (f32 (*)[4])')
            body = body.replace('(*selected)[4] = (u8 *)', '(*selected)[4] = (f32 (*)[4])')
        else:
            body = body.replace('u8 *selected', 'Mtx *selected').replace('selected = (u8 *)', 'selected = (Mtx *)')
        for axis in range(3):
            high, low, offset = 0x18 + axis * 2, 0x38 + axis * 2, 0x30 + axis * 4
            if kind == 0:
                high_view, low_view = 'selected->half[0][3][%d]' % axis, 'selected->half[1][3][%d]' % axis
                float_view = 'selected->floating[3][%d]' % axis
            elif kind == 1:
                high_view, low_view = 'selected[%d]' % (high // 2), 'selected[%d]' % (low // 2)
                float_view = '((f32 *)selected)[%d]' % (offset // 4)
            elif kind == 2:
                high_view, low_view = '((s16 *)selected)[%d]' % (high // 2), '((s16 *)selected)[%d]' % (low // 2)
                float_view = 'selected[3][%d]' % axis
            else:
                high_view, low_view = '((s16 *)selected->m)[%d]' % (high // 2), '((s16 *)selected->m)[%d]' % (low // 2)
                float_view = '((f32 *)selected->m)[%d]' % (offset // 4)
            body = body.replace('*(s16 *)(selected + 0x%X)' % high, high_view)
            body = body.replace('*(s16 *)(selected + 0x%X)' % low, low_view)
            body = body.replace('*(f32 *)(selected + 0x%X)' % offset, float_view)
            if left:
                old = '((f32)(%s * 65536) + (f32)%s) * scale' % (high_view, low_view)
                body = body.replace(old, 'scale * ((f32)(%s * 65536) + (f32)%s)' % (high_view, low_view))
        yield 'view%d-common%d-left%d' % (kind, common, left), body, declarations, ()


def backend_candidates():
    # Options are present in the local IDO 5.3 as1/ugen option tables.
    for flag in ('-no_branch_target', '-noxbb', '-nobopt', '-noglobal', '-nopeep', '-noswpipe', '-O0', '-O1'):
        yield 'assembler-' + flag[1:], screen.SELECTED, screen.DECLARATIONS, ('-Wab,' + flag,)
    for flag in ('-notailopt', '-nooffsetopt'):
        yield 'generator-' + flag[1:], screen.SELECTED, screen.DECLARATIONS, ('-Wc,' + flag,)


def main():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-matrix-translation-schedule'
    out.mkdir(exist_ok=True)
    records = []
    for name, body, declarations, flags in itertools.chain(typed_candidates(), backend_candidates()):
        try:
            record, _ = screen.compile_candidate(root, out, name, body, declarations=declarations, extra_flags=flags)
        except ValueError as error:
            record = dict(name=name, rejected=True, diagnostics=str(error))
        records.append(record)
        print(name, record.get('body_words'), record.get('differences'), record.get('diagnostics'), flush=True)
    (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
