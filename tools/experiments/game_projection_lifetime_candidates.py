"""Projection compiler controls; never install candidates, profiles or guards.

Some controls intentionally change alias-sensitive behavior. SELECTED is the
bounded qualified recovery, not a byte match or a fitting production body.
"""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments import game_projection_wrapper_candidates as prior
from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = prior.ENTRY, prior.ROM, prior.WORDS
FUNCTION = 'func_15144CEC'
SYMBOLS = prior.SYMBOLS
DECLARATIONS = prior.DECLARATIONS
PROTOTYPE = '''s32 func_15144CEC(struct17 *arg0, f32 *arg1, f32 *arg2,
    f32 *arg3, f32 *arg4, volatile u8 arg5);'''


def make_body(live_index=True, live_inverse=True, nested=True, pointer_view=False,
              depth_hint=False, offset_hint=False):
    body=prior.SELECTED
    body=body.replace('f32 *arg4, u8 arg5)',
        ('volatile f32 *arg4' if live_inverse else 'f32 *arg4')+', '+('volatile u8 arg5' if live_index else 'u8 arg5')+')')
    body=body.replace('    f32 depth;',('    register f32 depth;' if depth_hint else '    f32 depth;'))
    body=body.replace('    struct140 *view;',
        '    struct140 *view;\n    '+('register ' if offset_hint else '')+'s32 offset;')
    body=body.replace('    view = (struct140 *)((u8 *)D_800BE628 + arg5 * 0x180);',
        '    view = (struct140 *)((u8 *)D_800BE628 + offset);')
    body=body.replace('    *arg4 = 1.0f / depth;',
        '    *arg4 = 1.0f / depth;\n    offset = arg5 * 0x180;')
    if nested:
        body=body.replace('''    if (depth == 0.0f) {
        return 0;
    }
    *arg4''','''    if (depth != 0.0f) {
    *arg4''')
        body=body.replace('    return 1;\n}', '    return 1;\n    }\n    return 0;\n}')
    if pointer_view:
        body=body.replace('struct140 *view','ProjectionView *view').replace('(struct140 *)','(ProjectionView *)')
    return body


def declarations(pointer_view=False):
    if not pointer_view:return DECLARATIONS
    return DECLARATIONS.replace('extern s32 D_800BE628;', '''typedef struct {
    u8 pad0[0xC]; f32 unkC, unk10; u8 pad14[0x20];
    f32 unk34, unk38; u8 pad3C[0x144];
} ProjectionView;
extern ProjectionView *volatile D_800BE628;''')


def partial_body(temp,index,pointer,inverse,partial,reuse=False):
    """Vary depth caching, index homes, zero-block shape and float-local reuse."""
    body=make_body(True,inverse,False,pointer)
    body=body.replace('    f32 depth;\n','').replace('    depth = *arg3;\n','').replace('depth','*arg3')
    body=body.replace('    f32 xProduct;\n','').replace('    xProduct = arg1[0] * (view->unkC + 5.0f);\n','')
    body=body.replace('xProduct','(arg1[0] * (view->unkC + 5.0f))')
    if temp==1:
        body=body.replace('    f32 yProduct;\n','').replace('    yProduct = arg1[1] * (view->unk10 + 5.0f);\n','')
        body=body.replace('yProduct','(arg1[1] * (view->unk10 + 5.0f))')
    if temp==2:
        body=body.replace('    f32 yProduct;','    f32 yProduct;\n    f32 cachedDepth;')
        body=body.replace('    if (D_800A56B0 <= *arg3', '    cachedDepth = *arg3;\n    if (D_800A56B0 <= cachedDepth')
        body=body.replace('*arg3 <= D_800D9B20','cachedDepth <= D_800D9B20')
        body=body.replace('if (*arg3 ==','if (cachedDepth ==').replace('1.0f / *arg3','1.0f / cachedDepth')
    if index==0:
        body=body.replace('    if (arg4 == NULL)', '    offset = arg5;\n    if (arg4 == NULL)')
        body=body.replace('(arg5 << 6)', '(offset << 6)')
    else:
        body=body.replace('volatile u8 arg5)', 'u8 arg5)').replace('offset = arg5 * 0x180;', 'offset = *(volatile u8 *)&arg5 * 0x180;')
    if partial:
        term='cachedDepth' if temp==2 else '*arg3'
        body=body.replace('''    if ('''+term+''' == 0.0f) {
        return 0;
    }
    *arg4 = 1.0f / '''+term+''';''', '''    if ('''+term+''' != 0.0f) {
        *arg4 = 1.0f / '''+term+''';
    } else {
        return 0;
    }''')
    if reuse:
        assert temp==2
        body=body.replace('    f32 yProduct;\n','')
        body=body.replace('    yProduct = arg1[1] * (view->unk10 + 5.0f);','    cachedDepth = arg1[1] * (view->unk10 + 5.0f);')
        body=body.replace('yProduct','cachedDepth')
    return body


SELECTED = partial_body(2,0,False,False,True,True)


def lifetime_candidates():
    """Reproduce the 32/36/48/16/8 measured lifetime-control families."""
    for x,y,view,depth,index in itertools.product((False,True),repeat=5):
        body=make_body(index,True,False,False,depth,False)
        for remove,name,expression in ((x,'xProduct','arg1[0] * (view->unkC + 5.0f)'),
                                       (y,'yProduct','arg1[1] * (view->unk10 + 5.0f)')):
            if remove:
                body=body.replace('    f32 '+name+';\n','').replace('    '+name+' = '+expression+';\n','')
                body=body.replace(name,'('+expression+')')
        if view:body=body.replace('    struct140 *view;','    register struct140 *view;')
        yield 'local-x%d-y%d-view%d-depth%d-index%d'%(x,y,view,depth,index),body,False
    for index,branch,pointer,inverse in itertools.product(range(3),range(3),(False,True),(False,True)):
        body=make_body(index==0,inverse,branch==0,pointer)
        body=body.replace('    f32 xProduct;\n','').replace('    f32 yProduct;\n','')
        body=body.replace('    xProduct = arg1[0] * (view->unkC + 5.0f);\n','')
        body=body.replace('    yProduct = arg1[1] * (view->unk10 + 5.0f);','    depth = arg1[1] * (view->unk10 + 5.0f);')
        body=body.replace('xProduct','(arg1[0] * (view->unkC + 5.0f))').replace('yProduct','depth')
        if index==1:body=body.replace('offset = arg5 * 0x180;', 'offset = *(volatile u8 *)&arg5 * 0x180;')
        if index==2:
            body=body.replace('    s32 offset;\n','').replace('    offset = arg5 * 0x180;\n','')
            body=body.replace(' + offset',' + arg5 * 0x180').replace('u8 arg5)', 'volatile u8 arg5)')
        if branch==2:
            body=body.replace('''    if (depth == 0.0f) {
        return 0;
    }
    *arg4''','''    if (depth != 0.0f) {
    *arg4''').replace('    return 1;\n}', '    return 1;\n    } else {\n        return 0;\n    }\n}')
        yield 'reuse-index%d-branch%d-pointer%d-inverse%d'%(index,branch,pointer,inverse),body,pointer
    for temp,index,pointer,inverse,partial in itertools.product(range(3),range(2),(False,True),(False,True),(False,True)):
        name='partial-temp%d-index%d-pointer%d-inverse%d-branch%d'%(temp,index,pointer,inverse,partial)
        yield name,partial_body(temp,index,pointer,inverse,partial),pointer
    for index,pointer,inverse,partial in itertools.product(range(2),(False,True),(False,True),(False,True)):
        name='reuse-partial-index%d-pointer%d-inverse%d-branch%d'%(index,pointer,inverse,partial)
        body=partial_body(2,index,pointer,inverse,partial,True)
        yield name,body,pointer
        if index==0 and partial:
            for variant in range(2):
                changed=body.replace('    cachedDepth = arg1[1] * (view->unk10 + 5.0f);\n','')
                if variant==0:
                    changed=changed.replace('+ view->unk34;', '+ (cachedDepth = arg1[1] * (view->unk10 + 5.0f), view->unk34);')
                else:
                    changed=changed.replace('*arg4 * (arg1[0] * (view->unkC + 5.0f))',
                        '(cachedDepth = arg1[1] * (view->unk10 + 5.0f), *arg4 * (arg1[0] * (view->unkC + 5.0f)))')
                yield name.replace('reuse-partial','comma%d'%variant),changed,pointer


def candidates():
    for flags in itertools.product((False,True),repeat=6):
        yield 'index%d-inverse%d-nested%d-pointer%d-depth%d-offset%d'%flags,make_body(*flags),flags[3]


def compile_candidate(root,output,name,body=SELECTED,profile='o2g3',pointer_view=False):
    """Compile with real headers and bind only the existing retail externals."""
    source,obj,elf=(output/(name+suffix) for suffix in ('.c','.o','.elf'))
    source.write_text('#include <ultra64.h>\n#include "structs.h"\n'+declarations(pointer_view)+body+'\n')
    result=subprocess.run(['ido/ido5.3_recomp/cc','-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
        '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32',
        '-I','conker/include','-I','conker/include/2.0L','-I','conker/include/2.0L/PR',
        '-D_LANGUAGE_C','-D_FINALROM','-DF3DEX_GBI_2','-D_MIPS_SZLONG=32',*PROFILES[profile],
        '-o',str(obj.relative_to(root)),str(source.relative_to(root))],cwd=root,capture_output=True,text=True)
    diagnostics=result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics or 'IDO failed with status %d' % result.returncode)
    script=output/'projection-lifetime.ld'
    script.write_text('SECTIONS { .text 0x15144CEC : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',FUNCTION,
        *['--defsym=%s=0x%X'%item for item in SYMBOLS.items()],'-o',str(elf),str(obj)],check=True,capture_output=True)
    _,functions,rel=parse_object(obj);meta=functions[FUNCTION]
    words=list(struct.unpack_from('>%dI'%(meta['size']//4),sections(elf)['.text'][1],meta['value']))
    end=max(i for i,w in enumerate(words) if w==0x03E00008)+2
    assert not any(words[end:]);words=words[:end]
    retail=struct.unpack_from('>101I',(root/'conker/conker.us.bin').read_bytes(),ROM)
    frames=[(-w)&65535 for w in words if w&0xFFFF0000==0x27BD0000 and w&0x8000]
    return dict(name=name,profile=profile,body_words=end,frame=frames[0] if frames else 0,
        differences=sum(a!=b for a,b in itertools.zip_longest(words,retail,fillvalue=0)),
        exact=words==list(retail),diagnostics=diagnostics,relocations=rel),words


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--family',choices=('initial','lifetime'),default='lifetime')
    parser.add_argument('--profiles',nargs='+',choices=tuple(PROFILES),default=['o2g3'])
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[2];out=root/'conker/build/game-projection-lifetime';out.mkdir(exist_ok=True)
    records=[]
    forms=candidates() if args.family=='initial' else lifetime_candidates()
    for name,body,pointer in forms:
        for profile in args.profiles:
            record,_=compile_candidate(root,out,name+'-'+profile,body,profile,pointer)
            records.append(record);print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    (out/(args.family+'-measurements.json')).write_text(json.dumps(records,indent=2)+'\n')


if __name__=='__main__':main()
