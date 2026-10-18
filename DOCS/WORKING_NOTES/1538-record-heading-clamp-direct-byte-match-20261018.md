# Record Heading Clamp Direct Byte Match

Date: 2026-10-18. Consumer predecessor **600aa69e**, tools predecessor
**5abdd73**. Restore **func_15087E54**, owner `generated_B3020`, VA
**0x15087E54..0x15087EF0**, ROM **0xB5304..0xB53A0**. The wider Game matching
goal remains active; this is one completed function.

## Semantic Recovery

Replace the false s32/no-argument zero-return placeholder with
**void(s32 recordIndex,u8 *actor)**. Capture D_800872A0 once; a null table
skips all record/actor accesses and the helper call. Otherwise index 0x84-byte
records, pass float fields +0x10/+0x0C in F12/F14 and integer zero in A2 to
the existing **u16 func_1505A630(f32,f32,s32)**. Preserve actor across that
call in the incoming argument home, then read its u16 heading at +0x76.

Both local angles are **u16**: target is helper result +0x4000, delta is
target-current, each modulo65536. If delta has bit0x8000 set, update only
when **delta<0xDBFF**, storing target+0x2400. Otherwise update only when
**delta>=0x2401**, storing target-0x2400. In particular, delta0xDBFF remains
unchanged while0xDBFE updates. Do not simplify the asymmetric negative edge
to signed abs or substitute threshold0xDC00.

The bounded source search first emitted38 words using s32 locals and explicit
masks. Ordinary pointer aliases/reused index forms did not help. Recovering
the actual u16 lifetimes emits the complete **39 words / frame0x18 / zero
differences** directly. Raw u32/s32 target with u16 delta retained six register
differences; the selected u16/u16 body needs **no guards, inserted/omitted
instructions, assembly fallback or new compiler profile**. The existing
O2/g3/MIPS2/o32 slice retains its no-unroll CFLAGS; GLOBAL_ASM preprocessing
still receives ordinary O2/g3 only. No build helper/profile is weakened.

## Qualification

New tools: `experiments/game_record_heading_clamp.py` and
`tests/test_game_record_heading_clamp.py`. Ignored artifacts:
`conker/build/game-record-heading-clamp/`. Sixteen explicit input hashes pin
owner/ELF/guards/ROM/assembly, build/symbol/header inputs, four compiler
components, helper C, original caller assembly and its production C parent.
These are explicit inputs, not a claim to hash every transitive dependency.

All **seven pre-install tests pass in20.682s** and **seven installed tests
pass in72.832s**:

```sh
python3 -m unittest tools.tests.test_game_record_heading_clamp -v
```

**810 paired C/retail guest cases** cover nine wrapped targets, fifteen delta
boundaries, record indices0/3/255 and two stack phases. Check complete public
memory, helper argument bits/call count, saved ABI state and paired register/
float/read state. Non-stack write traces separately require exactly the
expected actor halfword store, or none. All39 words execute across the corpus.
**24 additional cases** combine indices-1/0x10001, null/non-null table, two
stack phases and helper-side actor/table effects. The actor is read after
the helper, not cached before it. The helper may clear the table pointer
after arguments have been delivered. These wide-index fixtures qualify
guest word-address behavior, not portable out-of-bounds C object access.

Native32 **O2 and O0 with UBSan** each pass **262,876 cases**: all65,536 deltas
at four targets, rotated valid record indices/helper modes, full edge crosses
and null-table cases. Native record objects contain real float fields and
the actor contains an aligned u16 heading; indices are0..3. Check complete
actor bytes, every record byte, table pointer, helper call count and exact
float argument bits. Seven wrong-negative-bound/wrong-positive-bound/stride/
actor-field/quarter-turn/float-order/cached-heading controls return explicit
observable-failure status23 in native tests and also fail guest expectations.
Crashes or only dead-register differences do not count as effective controls.

The initial positive control lowered0x2401 to0x2400, which merely stores the
already-current value at delta0x2400. Replace that ineffective final-memory
control with threshold0x2402 and check guest write traces separately. An early
fixture case-count assertion and a collision with the inherited `writes`
diagnostic list were corrected in the test harness only. Production source
and the first whole-link prediction did not change in response to those fixes.

Six independent original/C links at three code/data placements pass **540
paired rebased cases**, crossing signed LO16 boundaries and moving the helper
JAL. All three bindings are pinned. **272 target-access fault prefixes across
48 states** preserve complete paired memory, registers, floats, reads, calls,
events, instruction/delay PCs and access count. Helper internals are scripted
and excluded from the fault domain; this is not hardware MMU or portable C
fault equivalence. All39 raw words, three bindings, **32 live/frozen input
mutations** and nested historical views are corruption-gated.

## Observed Caller

The C graph alone did not show the caller. An aligned-word scan of the entire
retail image finds one exact JAL at ROM0x7A834/VA**0x1504D384** and no exact
target pointer/J word. Original **func_1504CB98** supplies actor in A1 from S0
at0x1504D26C and loads the selected record byte from **D_800C3E78** in the
target call's delay slot. The setup pair is checked as actual retail words.
This scan is not a proof that no computed/encoded indirect reference exists.

**96 actual bounded caller windows**,0x1504D384..0x1504D3A8, execute the call/
delay slot, helper ABI boundary and updated actor-angle consumer. Check the
forwarded two arguments, actor+0x76, subtraction of D_800CC280 into stack+0x1BC,
preserved S0 and the following actor+0x31C/+0x4E lookup. The earlier intervening
parent instructions are not executed by this window test. The complete
containing production **func_1504CB98 remains a zero-return stub**; no claim
is made that its gameplay path has been restored. No parent/header edit.

The existing helper **func_1505A630 is200 bytes/50 words retail-exact** in the
current production ELF; its typed C return/prototype supplies the interface.
Its internal floating-point angle math is not executed by this qualification.
The target tests use a scripted u16 return, exact F12/F14/A2 observations,
volatile-register clobbering and declared actor/table side effects.

## First Prediction And Build

Before editing production, replace only the qualified padded owner input in
a copied current linker script and freeze the first **3,257,636-byte** whole
ELF plus complete source successor. Original fixtures/first successors remain
immutable. Install only that semantic source body and use the existing build:

```sh
make -C conker -o Makefile -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_B3020.c.o build/conker.us.elf progress.csv
make -C conker -o Makefile -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

The installed whole ELF equals the first prediction. **126 changed bytes =
125 target-code bytes + one symbol-size byte** at file offset2915275. The
target extent changes12->156, with **zero metadata exclusions**. Audit all
**6,057 bodies/addresses** and canonical symbol definitions: only this body
and extent change, with zero address drift. All **72 raw owner neighbors**,
relative bindings and normalized pools remain fixed; the actual padded owner
matches qualification. Makefile and the entire existing guard CSV stay fixed.
Game data remains **189,088 bytes /720 owners /zero differences**. No new
compiler diagnostic; the pre-existing duplicate12D630 recipe warning remains.

| Artifact | SHA-256 |
| --- | --- |
| Complete installed ELF | `6f4bfb1be74457784dde6ad0f497d131956d7b110017c92357b0ad43a9cc0b7c` |
| Complete owner source | `576b4ce003c0b1a625864fbd2d5f1313e048593bcd4e972221ed59bc18a0d5f3` |
| Raw target | `a304c18e4118445cedd0dde67af888f0f0744ea2d151d690dbc0813cb087b7ae` |
| Linked target | `187f39f40c330a9652c35854186be6aa60956f2269feec2369e29716d5232d5b` |
| Unchanged guard CSV | `8f709f6c1cb03108c0f1e6f7b460e624d76f29734c97ed5fe9739f411f2046a1` |
| Unchanged Makefile | `840897f11d9fea8109c4e67c57e927efa6e1686de2b399fec2c9025828b92d49` |

The exact two-member owner/ELF historical view is serial/non-nesting and rejects
unknown/mixed states. Physical raw reads remain available. Future work should
freeze this new physical baseline directly; do not relax older hashes,
fixtures/helpers or nest historical readers to make stale tests pass.

## Bank And Next Action

Tools **f81bd64** is committed before the consumer source/docs/tools pin.
Both local tools copies pass eleven shared padder tests and project-tools
smoke checks; root tools-check passes. Four Windows ASCII/AST parses and two
byte-identical task pairs pass. The standalone mirror uses unittest discovery
to avoid a conflicting installed `tests` package. Preserve mirror **ddbdd16**
and all **1,202** initial dirty hashes, adding only two absent paths for1,204.
No mirror commit/reset, push, Claude call, host or frozen Release action.

Fresh official totals: **Game2,976/4,828 (61.64%)**, total **3,649/5,501
(66.33%)**, **1,852 different**, zero drift. Conversion counts/bytes remain
unchanged. Root README changes only the two aggregate matching rows.

Scoped Graphify refresh: **42,460 nodes /82,529 links /3,932 communities**.
Preserve all **19,398 nodes from2,972 excluded-but-existing files**. Only
three line-disambiguated UPDATE_LOG heading IDs move; their labels persist
and all other old IDs remain. The new note contributes seven nodes. Current
target/next definition locations resolve to **L290/L314**. Preserve the old
graph under the ignored task build directory; graph outputs remain ignored.
No full re-extraction purge or graph-history rewrite.

Next **func_15087EF0**, same owner, VA**0x15087EF0..0x15087FC4**, ROM
**0xB53A0..0xB5474**, **53 words/frame0x20**, currently a stub at sourceL314.
Graph queried and full retail body read. One aligned retail JAL occurs at
ROM0x7EB3C/VA**0x1505168C** in original **func_15051558**. Its production parent
is also a zero-return stub. Actor setup at0x15051680 and the selected record
byte in the call delay slot are read, but not yet qualified as a full caller
window. Audit that interface before assigning the return/actor ABI. The routine null-checks the
same table, saves its 0x84-byte record pointer across func_1505A630, then reads
D_800D23A8 and float record+0. When mode==0, speed<0.5 selects wrapped helper
result+0x4A00; when mode!=0, speed>=0.5 selects+0x4A00. Otherwise use+0x3600.
Both comparisons are false for NaN, selecting+0x3600 in either mode. Finally
store actor u16+0x76. Preserve the live post-helper loads and separate float
predicates instead of a boolean rewrite that changes unordered behavior.
Handwritten func_150A76F0, both fade gaps, stubbed parents and other open Game
queues remain separate work; no wider completion claim.
