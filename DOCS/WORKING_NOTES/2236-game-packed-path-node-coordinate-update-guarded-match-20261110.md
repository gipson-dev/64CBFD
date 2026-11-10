# Game packed path-node coordinate update guarded match - 2026-11-10

`func_15078544` now matches its complete **150-word / 600-byte** retail slot,
VA **15078544..1507879C**, ROM **A59F4..A5C4C**. The semantic C emits152 words
with retail's natural **0x50 frame**, saved F20/F22 pairs and RA lifetime.
**132 checked guard rows** close register roles, private homes and scheduling,
including two redundant private float-load omissions and one NOP repurposed
as a required byte-argument copy. No insertion or compiler-profile change.

Fresh production counts: **4,306 / 5,513 (78.11%)** overall; Game **3,633 /
4,840 (75.06%)**; Init492/492 and Debugger181/181. Drift0, different1,207.
The active80% goal needs **105** more matches to4,411/5,513. Conversion counts
and conversion CSV stay fixed. README changes only aggregate rows and date.

## Recovered behavior

Owner `conker/src/game_A28B0.c`; object `conker/build/src/game_A28B0.c.o`.
Original assembly `conker/asm/nonmatchings/game_A28B0/func_15078544.s` remains
unchanged. The ordinary asm-processor/IDO O2-g3/postprocess/generic-padder/
assembler route stays fixed. No Makefile or shared declaration change.

The old131-word C body used a shifted150489B0 lookup in place of the retail
15048A40 wrapper call. The wrapper performs that same shifted lookup, so
restoring it recovers the original call structure rather than changing its
mathematical result. The functional errors were writing the current
record's0/2/4 fields through one cached node. Retail writes the **next**
8-byte record's coordinates at8/10/12 and reloads actor/group/table/index
between each component. The recovered C fixes both errors. Explicit signed
multiplication replaces undefined negative left shifts, and float narrowing
uses `(s16)(s32)` to preserve the SDK's word-truncate/halfword-store shape.

Save the original command byte D_800D1890, then publish command&63. Select
the target actor from the26-entry D_800CC2D0 array using current actor+0x222.
Decode signed upper bytes D_800D1891/2 and the high/low nibbles ofD_800D1893
as two signed12-bit integers, then multiply by8 and convert tofloat. Capture
target X/Y/Z before any helper. The original command's upper2bits select:

- Mode0: derive `(target.heading_u16>>8)-64`, narrow tobyte, call15048A40
  and150489B0 with that same byte, retaining both float results.
- Mode1: use sine0 and cosine1 without helpers.
- Modes2/3:150484A0(currentX-targetX,currentZ-targetZ), then sinf/cosf of
  the saved angle. Preserve target coordinates across all helper effects.

Rotate the decoded X/Z offsets using the original float32 operation order.
Write truncated X, captured Y, then truncated Z into path entry command+1.
After each halfword publication, reload D_800D154C, actor group+0x13F,
pointer global D_800D2104, its group row and the live command byte. Helpers
may change the actor, table or command. X/Y stores may physically overlap
these selectors; the following component must observe the changed value.
The public interface remains `void(void)`.

## Natural source and closed normalization

Correcting the helper and repeated next-record stores first emitted152 words
with the0x50 frame, but spilled the target coordinates. Updating the cached
X/Z variables recovered F20/F22. Inline packed-offset expressions and removal
of the separate mode local recover the natural0x50 frame and float homes.
Bounded source probes, including register hints and explicit byte arguments,
remain private. No artificial volatile, source padding or profile override.

Raw SHA256:
`f75a4aed63a182c267769773e962d3a4adaa0fb765c90333fa9f3cb6148219f8`.
The normalizer pins all608 source bytes, all31 binding sites and owner/function.
Its explicit instruction-origin map preserves every source instruction except
two redundant private LWC1s at raw words128/129. Z arithmetic moves before X
publication, preserving the already loaded offset values across the stores.
The freed Z-store hazard NOP at raw145 becomes a pure angle-byte A0 copy at
normalized56. The remaining NOP retains its required first-store schedule.

All other edits are register-operand fields, recomputed branch displacements
and a closed private-home mapping:2B->2F,2C->30,34->38,3C->48,44->3C,48->40.
No frame or saved-register-home change. Relocation identities move with their
source instructions; expected/replacement binding maps are recorded separately.
Both independent target padders, complete owner padding and original assembly
agree on all150 words. This includes lifetime/load-elimination and private-home
closure, beyond ordinary register renaming.

A deliberately tested guest extension points path output into private stack
spills. Raw late reloads then differ; normalized and retail store traces agree.
The C floats have no escaped addresses. Portable native tests exclude physical
private-home aliases and invalid float-to-word conversions. Guest invalid
conversions use the modeled MIPS indefinite word; no FCSR/hardware claim.

## Qualification and production

The owner has211 functions, with retained ASM15079B30. All **210 non-target
neighbors**, pools and reginfo remain unchanged in raw/padded comparisons.
The13 inherited owner warnings stay13; none are added. Actual five-command
Make output equals the independently padded owner. Strict full-ELF prediction
accounts for **516 changed bytes**, only the600-byte target and st_size524->600.
All6,051 function addresses stay fixed. Protected189,088 bytes across720 owners
remain exact with SHA2560bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
No unexplained bytes or exclusions. Existing checksum failure (`make all`
exit2) and duplicate12D630 Make warnings remain.

- Guest:348 cases per raw/normalized/retail body =**1,044 executions**, plus16
  rebases. Every152 raw and150 normalized/retail word is visited. All public
  bytes, helper observations, exact three store addresses/order, saved ABI,
  signed packing, all command bytes, valid target slot25, float boundaries,
  physical selector aliases and the separate private-home profile pass.
- Native SDK32:333 defined cases at O0/O2/O3, UBSan and14 effective semantic
  controls per profile. Canonical26-actor layout, all retained actor/path/table
  bytes and helper observations pass with explicit endianness normalization.
- IDO:16 effective controls, including cached-node and reversed-publication
  errors. All152 word and31 binding corruptions are rejected. The generic
  padder rejects132 stale expected rows, including both omission rows. Seven
  literal image corruptions are rejected. Four independent GNU links and16
  executions cover HI/LO carry boundaries. Compiler/interpreter errors never
  count as semantic control witnesses.
- Dispatch:ROM has no direct JAL/J and one entry pointer at22B490, protected
  VA800869D0 =D_80086730[A8]. The complete unchanged byte-exact C dispatcher
  1507BC14 has100 body words plus3 alignment words.138 executions /126 target
  invocations against all target forms cover99 body words; word67 is the dead
  duplicate byte load. Script decoding, FF-marker skips, pointer advancement,
  null lookup, signed countdown, timer/flag branches and real JALR ABI pass.
  Script lookup1507BB28 and next handler1507735C are bounded providers, as are
  target trig helpers. Whole helper algorithms and gameplay are not claimed.

Six fresh focused tests run before/after installation in both tools environments.
The sibling uses a read-only overlay for new modules; dependency origins/hashes
are recorded. Native Git inventories2,434 dirty paths; the earlier WSL inventory
also flagged five nested submodules. The native baseline is preserved exactly;
no sibling source is edited. Shared smokes are fresh; three unchanged regression
checks per copy are explicitly fingerprinted reuses.719 inputs are frozen.

Graphify refresh requests the owner and six modules. All210 active C definitions,
the retained ASM and nodes outside changed paths are audited; new-module node
coverage is recorded as observed. This is a scoped AST refresh. Tools are
committed before consumer source/guards/docs/pin. No push or host-port change.
Ignored evidence lives in `conker/build/game-path-offset-15078544-match/`.

Next: `func_1507AA48` in the same owner,154 retail words /145 screened
differences. Recheck the owner/ABI before qualification. Hard private1510D404
remains uncredited. Keep the full80% goal active.
