"""Uninstalled sampler exit/storage controls under the production O2/g3 profile."""

import itertools
import json
from pathlib import Path

from tools.experiments import game_area_sampler_candidates as screen


def candidates():
    for mask in range(16):
        body=screen.SELECTED
        for bit,name in enumerate(('x','z','top','bottom')):
            if mask & 1<<bit:body=body.replace('f32 *'+name,'volatile f32 *'+name)
        yield 'volatile-output-%X'%mask,body,screen.DECLARATIONS
    fields={'unk0':'direct1','unk4':'shifted1','unkB':'angle1','unk10':'direct0','unk14':'shifted0','unk1B':'angle0',
        'unk20':'span2','unk24':'direct2','unk28':'shifted2','unk2F':'angle2'}
    for reverse,word,local in itertools.product((False,True),repeat=3):
        body=screen.SELECTED.replace('    struct209 scratch;\n','')
        for old,new in sorted(fields.items(),key=lambda item:-len(item[0])):body=body.replace('scratch.'+old,new)
        declarations=['    f32 direct1;\n    f32 shifted1;\n    u8 angle1;\n',
            '    f32 direct0;\n    f32 shifted0;\n    u8 angle0;\n',
            '    f32 span2;\n    f32 direct2;\n    f32 shifted2;\n    u8 angle2;\n']
        if word:declarations=[d.replace('u8 angle','u32 angle') for d in declarations]
        if local:
            body=body.replace('        default:\n','        default: {\n')
            for case,decl in zip((1,0,2),declarations):
                body=body.replace('        case %d:\n'%case,'        case %d: {\n'%case+decl)
            for case in (2,0,1):body=body.replace('        case %d:'%case,'        }\n        case %d:'%case)
            body=body.rsplit('    }\n}',1)[0]+'        }\n    }\n}'
        else:
            if reverse:declarations.reverse()
            body=body.replace('    f32 distance;',''.join(declarations)+'    f32 distance;')
        yield 'scalars-reverse%d-word%d-local%d'%(reverse,word,local),body,screen.DECLARATIONS
    for chain,field in itertools.product((False,True),('y','height','flags')):
        declaration=screen.DECLARATIONS
        if field=='flags':declaration=declaration.replace('u8 pad14, flags;','u8 pad14;volatile u8 flags;')
        else:
            declaration=declaration.replace('    s16 x, y, z, radius, height, width;',
                '\n'.join('    %ss16 %s;'%('volatile ' if f==field else '',f) for f in ('x','y','z','radius','height','width')))
        yield 'field-%s-chain%d'%(field,chain),screen.BASELINE if chain else screen.SELECTED,declaration


def main():
    root=Path(__file__).resolve().parents[2]
    output=root/'conker/build/game-area-sampler-exits';output.mkdir(exist_ok=True)
    records=[]
    for name,body,declaration in candidates():
        record,_=screen.compile_candidate(root,output,name,body,declarations=declaration)
        records.append(record)
        print(name,record['body_words'],record['frame'],record['differences'],flush=True)
    assert len(records)==30 and all(r['differences'] for r in records)
    (output/'measurements.json').write_text(json.dumps(records,indent=2)+'\n')


if __name__ == '__main__':main()
