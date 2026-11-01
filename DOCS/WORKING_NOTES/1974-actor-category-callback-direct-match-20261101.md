# 1974 - Actor category event callback recovered directly from C

`func_1513DF9C` now emits all **53 retail words** with its natural **24-byte
frame and zero word guards**. Production Make and the independent Native ELF
recount confirm **4,041/5,507 (73.38%)**, Game **3,368/4,834 (69.67%)**, zero
address drift and 1,466 still different. Exactly one match is added. The 75%
threshold is 4,131: **90 more** matches are needed; the wider goal remains active.

## Recovered behavior and caller interface

Owner `game_169510`, source `conker/src/game_169510.c`, VA
`0x1513DF9C..0x1513E070`, ROM `0x16B44C..0x16B520`. Replace the false
zero-return placeholder and local prototype with:

    void func_1513DF9C(void *actorPointer, s32 eventAddress, u8 command);

Read the actor flag word at +0x58. If bit 22 is clear, call callback table entry
zero without reading category byte +0x19. Otherwise map categories 0..12 to
indices `0,1,0,4,8,2,3,5,6,7,0,9,10`; out-of-range categories also select zero.
Invoke `D_80089F64[index](actor, eventAddress, command)`. The eleven-entry table
retains its original slot-6/slot-7 alias. Actor validity and mapped selected
tables are preconditions; the function does not add a null-actor check.

The second parameter is an opaque full-width event address word, rather than a
recovered pointee type. The third parameter is a byte. Existing `struct115.unk1C`
uses `void (*)(void *, s32, u8)`. Three original generic caller windows prepare
exactly those three argument slots, and a bounded CFG audit proves no callback
V0 result is consumed before overwrite, another call or return. Equal object
words alone did not resolve the interface: preliminary integer-return and
pointer-carrier variants also emitted identical code. No fourth argument or
meaningful C return is inferred from leftover registers.

## Owner, switch table and actual Make

The complete raw and padded owners preserve **58 neighboring functions**.
The raw owner formerly had no pools; the recovered switch contributes 13
relocations to offsets inside this function, plus standalone alignment:
**52 meaningful table bytes / 64 raw pool bytes**. Every relocation target is
checked against the independently retained retail table. The 12 alignment bytes
are not inserted into production data.

Add only this owner-specific Make binding:

    $(BUILD_DIR)/$(SRC_DIR)/game_169510.c.o: RETAIL_RODATA_SYMBOL := jtbl_800A5188_game

The existing padder redirects the C table references to the retained retail
switch-table symbol. The padded object has the same absent rodata and empty data
section as its predecessor. No shared padder or compiler profile changes are
needed. All five actual root-owner recipe commands reproduce the qualified
padded object. The owner retains exactly **43 inherited diagnostics**, with no
new or removed diagnostics after source/line normalization. Existing unrelated
duplicate Make recipe warnings remain recorded in the full production log.

Raw isolated C payload SHA-256:
`e637d580f5562fe3b4f256d2b11b25721ff09d4b7f952e8d8ec853001dd86ec3`.
Four raw relocation sites are checked; the two local rodata bindings become the
retained retail table symbol in the padded object. All 53 emitted words match
at three independent GNU link layouts, including HI/LO carry boundaries. The
selector load at offset **0x2C** is unreachable: 52 words execute, all 53 emit.

## Runtime qualification and limits

- **32,256 guest cases / 64,512 executions** cover all 256 categories and command
  bytes, poisoned upper command bits, both stack phases, opaque event words,
  actor/context aliases, callback mutations, caller-saved GPR/FPR/HI/LO clobbers,
  and actual aliased versus independent callback tables. An independent semantic
  reference checks public state, callback arguments and logical table index;
  original/C complete bounded machine state, memory and access traces agree.
- **25 access-prefix pairs** preserve literal bounded state and traces. Two
  sparse flag-clear executions omit the category byte mapping entirely while
  still invoking callback zero. This is guest instruction-order evidence, not a
  portable C fault-behavior or hardware acceptance claim.
- Native32 **O0/O2/O3 each pass 7,680 cases / 69,120 executions**, with UBSan,
  complete 384-byte actor/64-byte context comparisons, aliased/unique callback
  tables and eight effective controls: wrong flag bit, wrong category byte,
  wrong category-12 handler, skipped disabled callback zero, narrowed event word,
  altered command byte, wrong actor address and wrong table index.
- **1,600 cases / 3,200 executions** connect four original callback bodies,
  all equal to their retained production slots: `func_1513E070` (5 words),
  `func_15102D50`, `func_151BE604` and `func_150F31D4` (16 words each). Every word
  in these helpers executes. Logical indices 0, 2, 6, 7 and 10 are exercised.
  The common lower function `func_15169850` is stubbed; its five outgoing slots
  `(eventAddress, command, actor+0x110, actor+0x114, actor)` are checked. Two sparse
  executions connect the real no-op helper. Complex remaining callbacks and
  complete gameplay are not qualified by these bounded helper tests.
- A full aligned ROM census finds **zero direct JALs, zero direct Js and three
  pointer registrations** at ROM `0x230534`, `0x230E58`, `0x2310FC` / VA
  `0x8008BA74`, `0x8008C398`, `0x8008C63C`. Descriptor records are 27, 72 and 85,
  stride 52, callback +40 from base `0x8008B4D0`. The actual generic lookup view
  is base+12 (`0x8008B4DC`), callback +28. The initial truncated two-result search
  was superseded by the complete three-registration census before adoption.
- **2,268 caller cases / 4,536 executions** connect the three original generic
  windows at `0x15169160` (5 words), `0x15169340` (10), `0x15169514` (5), all
  three registration cells, both roots and mutating callbacks. Actual table
  selection and A0/A1/byte-A2 setup agree with full bounded model state. Return
  liveness visits 42/52/52 instructions respectively. These are original ROM
  windows, not the older nonmatching ECTS parent implementations; full parent
  functions and their preceding filters remain outside this claim.
- Both tools checkouts pass **five target tests and shared checks before and
  after installation**. The first public test run incorrectly expected an absent
  padded data section; inspection confirmed the inherited empty section. The
  corrected test checks exact predecessor pool equality. Failed and successful
  receipts are retained. Routine work uses **zero Claude calls**.

## Whole-image preservation, adoption and continuation

The independent prediction starts only from frozen production ELF
`860997333f77ca8592380dc62a6be70141037cd54e8ae01e8455036e0d9e68fe`.
It changes the 212-byte target slot, root symbol extent **12 to 212 bytes**, and
one explicitly guarded bounded symbol/string ordering: adjacent definitions
`func_151A6B3C` and `D_8009E698` swap with their adjacent 25-byte string group.
The predictor checks original adjacency, string bytes, shared string base and
complete named-definition multiset. No actual-output region is copied into the
prediction; no ELF region is excluded. No unverified linker-hash causal claim
is required for this measured metadata permutation.

Private and actual production full links equal that prediction literally.
All **6,052 canonical addresses**, **6,051 other bodies**, complete named symbol
definitions (apart from the declared root extent), ELF length, normalized map
and guard CSV are fixed. All **189,088 protected Game bytes across 720 owners**
remain exact. Review of all **17,696 prior sealed inputs** finds only the
expected source, Makefile, owner object and ELF changes; no dependent object
change is excluded. Native actual ELF recount independently confirms one match.

Production ELF SHA-256:
`82be01b39fa42cbc62f1ec773ca0e38b838018630dd35b3631cc0acd03f93a20`.

Stage `conker/build/game-actor-category-callback-1513DF9C-match/` retains the
frozen inputs, **33 immutable preparation artifact pins**, public test receipts,
actual Make commands/object, full-image predictor, production and Native
recounts, seal, graph proof and handoff. Four new public modules cover source
and image gates, guest/helpers/callers, native controls and integration tests.
The graph refresh covers thirteen changed files with zero LLM tokens, retaining
old nodes and valid edge occurrences while explicitly archiving the false
integer return-type edge. It is not a full-corpus extraction or reclustering.
Root README changes only aggregate matching rows. Commit tools before consumer;
no push. Original assembly and unrelated mirror work remain preserved.

Next verified ordinary C target from the actual unmatched inventory:
**`func_151A084C`**, 55 words/frame48 in `generated_1CC440`, currently a false
zero-return stub. Inspect its actor/state validation, helper-produced value,
mode-dependent output and invalidation path before claiming a match. It has not
been screened or credited here. `func_150A613C` is a handwritten T4/FPR/S2 ABI
routine and belongs to the separate assembly restoration stream. The private
initializer `func_15187EC0` stays uncredited at 52/frame24/25 differences, with
its early argument-read counterexample. Its historical whole-image fixture,
other parked candidates and old checkpoint tests require explicit rebasing or
restoration before reuse. The separately requested cleanup archived only the
superseded active-ID checkpoint and previous cleanup record; this current stage,
initializer bank, filtered-node checkpoint and private work remain in place.
