"""Measure real vector lifetimes and SDK-aligned matrix storage, without patches."""

import itertools
import json
import sys
from pathlib import Path

from tools.experiments import game_oriented_matrix_candidates as prior

ENTRY, ROM, WORDS, FUNCTION = prior.ENTRY, prior.ROM, prior.WORDS, prior.FUNCTION
compile_candidate = prior.compile_candidate
BASELINE = dict(prior.inplace_candidates())['inplace0100']


def homogeneous_body(mask):
    body = BASELINE
    if mask:
        body = 'typedef struct { f32 unk0, unk4, unk8, w; } OrientedPoint;\n' + body
    for bit, name, start, row in ((0, 'direction', '    left.x =', 2),
            (1, 'up', '    up.unk8 =', 1)):
        if mask & (1 << bit):
            body = body.replace('    struct17 %s;' % name, '    OrientedPoint %s;' % name)
            body = body.replace(start, '    %s.w = 0.0f;\n' % name + start, 1)
            body = body.replace('matrix[%d][3] = 0.0f;' % row, 'matrix[%d][3] = %s.w;' % (row, name))
    return body


def storage_body(mask=0, aligned=False, scoped=False):
    body = homogeneous_body(mask)
    if aligned:
        body = 'typedef union { f32 f[4][4]; Mtx sdk; } OrientedMatrix;\n' + body
        body = body.replace('    f32 matrix[4][4];', '    OrientedMatrix matrix;')
        body = body.replace('matrix[', 'matrix.f[').replace('guMtxF2L(matrix,', 'guMtxF2L(matrix.f,')
    if scoped:
        declarations = {}
        for name in ('left', 'up', 'matrix'):
            declaration = next(line for line in body.splitlines() if
                (line.startswith('    ') and line.rstrip().endswith(' ' + name + ';')) or
                (name == 'matrix' and line == '    f32 matrix[4][4];'))
            declarations[name] = declaration
            body = body.replace(declaration + '\n', '', 1)
        boundaries = ('    left.x =', '    up.unk8 =', '    matrix.f[0][0]' if aligned else '    matrix[0][0]')
        for name, boundary in zip(('left', 'up', 'matrix'), boundaries):
            begin = body.index(boundary)
            if name == 'up' and mask & 2:
                begin = body.index('    up.w =')
            body = body[:begin] + '    {\n' + declarations[name] + '\n' + body[begin:]
        body = body.removesuffix('\n}') + '\n    }\n    }\n    }\n}'
    return body


def local_layout(obj):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'ultralib/tools'))
    from libelf import ElfFile
    from mdebug import EcoffSt
    elf = ElfFile(Path(obj).read_bytes())
    for fdr in elf.find_section_by_name('.mdebug').fdrs:
        for pdr in fdr.pdrs:
            if pdr.name == FUNCTION:
                return dict(frame=pdr.frameoffset, entry_relative={
                    s.name: s.value - 0x100000000 if s.value & 0x80000000 else s.value
                    for s in pdr.symrs if s.st == EcoffSt.LOCAL})
    raise ValueError('Missing oriented matrix debug procedure')


def candidates():
    for mask, aligned, scoped in itertools.product(range(4), (False, True), (False, True)):
        yield 'vectors%d-sdk%d-scoped%d' % (mask, aligned, scoped), storage_body(mask, aligned, scoped)
    declarations = ('    OrientedHorizontal left;\n', '    f32 matrix[4][4];\n',
        '    struct17 direction;\n', '    struct17 up;\n')
    for order in itertools.permutations(range(4)):
        body = BASELINE
        for declaration in declarations:
            body = body.replace(declaration, '')
        body = body.replace('    f32 inverse;\n', ''.join(declarations[i] for i in order) + '    f32 inverse;\n')
        yield 'inplace-order-' + ''.join(map(str, order)), body
    declarations = ('    f32 leftX;\n', '    f32 leftZ;\n', '    f32 matrix[4][4];\n',
        '    struct17 direction;\n', '    struct17 up;\n')
    for order in ((2, 0, 3, 1, 4), (2, 1, 3, 0, 4), (2, 0, 3, 4, 1), (2, 1, 3, 4, 0),
            (0, 2, 3, 4, 1), (1, 2, 3, 4, 0), (0, 1, 2, 3, 4), (2, 3, 4, 0, 1)):
        body = BASELINE.replace('    OrientedHorizontal left;\n', '')
        for declaration in ('    f32 matrix[4][4];\n', '    struct17 direction;\n', '    struct17 up;\n'):
            body = body.replace(declaration, '')
        body = body.replace('    f32 inverse;\n', ''.join(declarations[i] for i in order) + '    f32 inverse;\n')
        body = body.replace('left.x', 'leftX').replace('left.z', 'leftZ')
        yield 'scalar-left-order-' + ''.join(map(str, order)), body


SELECTED = dict(candidates())['scalar-left-order-20314'].replace(
    'typedef struct { f32 x, z; } OrientedHorizontal;\n', '')


def main():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-oriented-matrix-lifetimes'
    out.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, out, name, body)
        record['layout'] = local_layout(out / (name + '.o'))
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], record['layout'], flush=True)
    (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
