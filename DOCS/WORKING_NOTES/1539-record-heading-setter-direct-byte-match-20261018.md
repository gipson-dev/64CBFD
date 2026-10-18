# Record Heading Setter Direct Byte Match

Date: 2026-10-18. Consumer predecessor **834c4976**, tools predecessor
**f81bd64**. Restore **func_15087EF0**, owner `generated_B3020`, VA
**0x15087EF0..0x15087FC4**, ROM **0xB53A0..0xB5474**. The wider Game matching
goal remains active; this is one completed function.

## Semantic Recovery

Replace the false s32/no-argument zero-return placeholder with
**void(s32 recordIndex,u8 *actor)**. Check D_800872A0 for null, then capture
its 0x84-byte selected record. The existing compiler emits one table load
despite the repeated ordinary C expression. A null table skips record, mode,
actor and helper accesses, apart from ordinary stack setup/teardown.

Call existing **u16 func_1505A630(f32,f32,s32)** with record float+0x10/+0x0C
in F12/F14 and A2=0. Save the record and actor through the helper. After it
returns, load signed byte **D_800D23A8** and the captured record's float+0.
When mode==0, speed<0.5 selects helper angle+0x4A00; when mode!=0, speed>=0.5
selects+0x4A00. Otherwise select+0x3600. Narrow the result to u16 and store
actor+0x76. Both comparisons are false for quiet NaN: either mode selects
+0x3600. A negated comparison or mode/XOR simplification can change that path.
The label speed is descriptive, not a confirmed retail field name; its +0
offset, float load and ordered predicates are the established facts.

Default-then-override source first emitted51 words/frame0x28. Explicit
if/else arms recovered53 words; an unnecessary table local still enlarged
the frame. Reusing one initialized record pointer reached frame0x20 with four
register-role differences. Removing the redundant table local, while keeping
the distinct captured record, recovers the complete **53 words / frame0x20 /
zero differences** directly. Record declaration lifetime also reproduces its
original stack home+0x1C; actor uses incoming home+0x24. Both local angles are
u16. No guards, inserted/omitted instructions, assembly fallback, profile or
Makefile changes. Retain ordinary O2/g3 GLOBAL_ASM processing and the slice's
existing compiler-only no-unroll flag via the already-qualified B3020 wrapper.

## Qualification

New tools: `experiments/game_record_heading_setter.py` and
`tests/test_game_record_heading_setter.py`. Ignored artifacts:
`conker/build/game-record-heading-setter/`. Sixteen explicit hashes pin owner,
whole ELF, guards, ROM, original assembly, build/symbol/header inputs, four
compiler components, helper C and original/production caller sources. This is
the declared input closure, not every unlisted transitive dependency.

All **seven pre-install tests pass in28.458s** and **seven installed tests
pass in35.543s**:

```sh
python3 -m unittest tools.tests.test_game_record_heading_setter -v
```

**3,168 paired raw-C/retail guest cases** cover all256 mode bytes, seventeen
speed bit patterns, angle wrap boundaries, indices0/3/255 and two stack phases.
Patterns include signed zero, subnormals, adjacent floats around0.5, finite
extremes, infinities and positive/negative quiet NaNs. Check complete public
memory, exact ordered public reads and the one actor halfword write, helper
argument bits/call count, signed mode-load result, paired register/float state
and saved ABI state. All53 words execute across the corpus. **32 additional
cases** combine indices-1/0x10001, null/non-null table, stack phases and helper
effects. Wide-index memory models are not portable C array-object proofs.

Scripted helper effects separately flip mode, change the original record's
speed or redirect the global table to another bank. The latter demonstrates
the captured record lifetime; the first two demonstrate post-helper loads.
These are sequenced helper-side effects, not asynchronous/volatile/data-race
semantics. The helper clobbers caller-saved registers and its argument homes.

Native32 **O2/O0 with UBSan** each pass **403,712 cases**. Cover all65,536
returned angles, all256 mode bytes, seventeen intended speed patterns, valid
indices0..3, full edge crosses and helper/null cases. The independent result
reference classifies float bit patterns, instead of repeating the C float
predicates. Records contain real aligned float fields; actor heading is an
aligned u16 field. Verify every byte of both record banks and the actor,
table/mode results, exact float helper arguments and call count.

Nine inclusive/exclusive-half, unordered-negation, cached-mode, cached-speed,
reloaded-record, wrong-stride, wrong-offset and swapped-float controls fail
observable expectations in guest tests and return explicit status23 natively.
A crash or difference only in dead scratch state does not count. Native
failure receipts preserve a small tagged input/result packet for diagnosis.

The initial guest runner lacked LB; add signed-byte execution only in this
new local oracle, preserving tracking/access faults, and check its sign
extension across all256 mode bytes. Unselected native row initialization
initially XORed infinity bits into unintended signaling NaNs. The O0 record-
bit preservation assertion exposed that fixture problem. Initialize those
rows with the same intended speed instead; retain all17 intended patterns,
including infinities and quiet NaNs. Map guest guard bytes so the bad-stride
control demonstrates wrong observations rather than an unmapped read.
These are harness fixes, not changes to production C or the first prediction.
Signaling NaNs and N64 FCSR exception/flush behavior are not claimed qualified
by this host/guest comparison; the complete instruction bytes remain exact.

Six independent original/C links at three code/data placements pass **288
paired rebased cases**, crossing signed LO16 boundaries for both globals and
moving the helper JAL. All five bindings are pinned. **512 target-access fault
prefixes across64 states** preserve complete paired memory, registers, floats,
read/write traces, calls/events, PC/delay and access count. Helper internals
are excluded; this is not a hardware MMU or portable C fault proof. All53 raw
words, five bindings, **32 live/frozen input mutations** and nested historical
views are corruption-gated.

## Observed Caller

Aligned-word retail scan finds one exact JAL at ROM0x7EB3C/VA**0x1505168C**
in **func_15051558**, and no exact target-pointer/J words. This does not rule
out computed/encoded indirect references. Its production C parent remains
a zero-return stub, not claimed restored.

**576 actual bounded windows**,0x15051678..0x15051698, execute actor+0x89
gate, A1-from-S0 setup, selected record byte D_800C3E78 in the JAL delay slot,
the target and F0 reset. Check taken/skipped branch-likely delay behavior,
forwarded arguments, public memory/helper observations and preserved S0.
The caller ignores a meaningful target return; typed void C is appropriate
for this observed actor update. Other parent instructions/gameplay are not
executed by this window. No parent or shared-header edit.

The existing helper's **200 bytes/50 words** remain production/retail-exact;
its typed C supplies the interface. Its internal floating-point angle math
is not executed by these target tests; use a scripted u16 result and exact
F12/F14/A2 observations, with explicit helper lifetime effects.

## First Prediction And Build

Before production edits, replace only this qualified padded owner input in a
copied current linker script. Freeze the first complete **3,257,636-byte ELF**
and complete owner-source successor. Original fixtures and first successors
stay immutable. Install only that semantic body using the existing build:

```sh
make -C conker -o Makefile -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_B3020.c.o build/conker.us.elf progress.csv
make -C conker -o Makefile -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

Installed ELF equals the first prediction: **156 changed bytes =155 target-
code bytes +one symbol-size byte**, file offset2948923. Target extent changes
12->212 with **zero metadata exclusions**. Audit all **6,057 bodies/addresses**
and canonical symbol definitions: only this body and extent change. Preserve
all **72 raw owner neighbors**, pools/relative bindings and actual padded
owner equivalence. Guard CSV and Makefile stay fixed. Game data remains
**189,088 bytes /720 owners /zero differences**. No new compiler diagnostic;
the existing duplicate12D630 recipe warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Complete installed ELF | `c1e56f1d074a85813ef0e6cedd22b1d41f109ec0f60abdf43cd80914f7ec6407` |
| Complete owner source | `b087b1069a1e0db0629bffd448962a2c726a56b07099f1cc0735e3d5fcdfc0be` |
| Raw target | `00ecca182903df384b4ff5d0a6b25210dfbd2208d4ce0d9f7ce10add963c25d9` |
| Linked target | `2c476fce3d66c3a93777c1c493ab3fcd4dd34bc2fc2c0aeff0ab995a49357055` |
| Unchanged guard CSV | `8f709f6c1cb03108c0f1e6f7b460e624d76f29734c97ed5fe9739f411f2046a1` |
| Unchanged Makefile | `840897f11d9fea8109c4e67c57e927efa6e1686de2b399fec2c9025828b92d49` |

The exact two-member owner/ELF historical view is serial/non-nesting and rejects
unknown/mixed states. Physical raw reads remain available. Freeze this new
physical baseline directly for later work; never relax older fixture/helper
hashes or nest historical readers to accommodate stale tests.

## Bank And Next Action

Tools **e1ce81b** is committed before consumer source/docs/tools pin. Both
local tools copies pass eleven shared padder tests and project-tools smoke;
root tools-check passes. Four Windows ASCII/AST parses and two exact task-file
pairs pass. Preserve older standalone mirror **ddbdd16** and all **1,204**
initial dirty hashes, adding only two absent paths for1,206. No mirror commit/
reset, push, Claude call, host or frozen Release action.

Fresh official totals: **Game2,977/4,828 (61.66%)**, total **3,650/5,501
(66.35%)**, **1,851 different**, zero drift. Conversion counts/bytes remain
unchanged. Root README changes only its two aggregate matching rows.

Scoped Graphify refresh: **42,469 nodes /82,538 links /4,001 communities**.
Preserve **19,398 nodes from2,972 excluded-but-existing files**. Only three
line-disambiguated UPDATE_LOG heading IDs move; all three labels and all other
old IDs persist. The new note contributes seven nodes; target/next definitions
resolve to **L315/L410**. Preserve the original graph in the ignored task
build directory; graph outputs remain ignored. No full-scan purge or history
rewrite is performed.

Next **func_150882E4**, same owner, VA**0x150882E4..0x150883B0**, ROM
**0xB5794..0xB5860**, **51 words/no frame**, current sourceL410. Graph queried
and complete original body read. One exact aligned retail JAL occurs at
ROM0xCB9D4/VA**0x1509E524**, in **func_1509E3DC**, owner `generated_CB3D0`.
That containing production parent remains a stub. Its command branch loads
A0 from command+8 and A1 from command+0xC in the call delay, then forwards V0
through the common return; audit that boundary before defining the query ABI.

The routine returns sentinel0x10 for null table or no match. Snapshot signed
count D_800D2398; add the signed own-record ID byte+0x29 to the second argument.
Scan 0x84-byte records in order, skip own index and take the first matching
signed ID. Quantized heights combine signed halfword+0x24 times16 with
truncation of float+8 times16; preserve the original ordered difference,
absolute value and packed `(distance<<8)|slot` result. Audit finite conversion
domains, exceptional float/FCSR behavior and signed overflow/shift boundaries
instead of silently extending a native-C claim. Handwritten func_150A76F0,
fade gaps, stubbed parents and wider Game queues remain separate open work.
