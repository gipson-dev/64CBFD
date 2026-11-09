# Sequence Time Advance Direct Match - 2026-11-09

`func_1501E400` replaces a false zero-return placeholder with the complete
sequence-time update. All **80 words /320 bytes** emit directly from semantic
C under the owner's existing **O2/g3/-Wo,-loopunroll,0** profile. The routine
has retail's **0x28-byte frame**, RA+0x14 and no saved S registers. There are
**no guards, padding additions, binding changes or profile changes**.

Production: Total **4,281 /5,513 (77.65%)**, Game **3,608 /4,840 (74.55%)**,
Init **492/492**, Debugger **181/181**, zero drift; **1,232** still different.
**130** more exact functions reach4,411/5,513 and80%. Conversion rows stay fixed.

## Interface and behavior

Owner `conker/src/game/generated_49D30.c`; original `conker/asm/49D30.s`.
VA1501E400..1501E540, ROM4B8B0..4B9F0; complete80-word body and slot. Interface:

```c
void func_1501E400(s32 slot);
```

The aligned ROM census finds exactly two entry JALs and no interior calls or
aligned address values. Both pass0 and ignore the return: frame coordinator
func_15019130 atVA15019160/ROM46610 and sequence catch-up func_1501E2F8 at
VA1501E398/ROM4B848. The same-owner forward declaration becomes void(s32);
the external declaration changes likewise in game_45B80.c. All16 functions
and the complete caller object remain identical. The caller's three inherited
Warning712 diagnostics are unchanged after path/line normalization. No shared
header/ABI edits are needed. func_1501E1B4's old source stub is not changed.

- Decrement byte D_800C3A58 only when nonzero, including inactive slots.
- Always copy current D_800C35B0[slot] to previous D_800C35B8[slot]. Only
  active byte D_800C35EA[slot] exactly1 enters the remaining work.
- Call func_1501E1B4(slot). Unless slot0 is paused by nonzero D_800BEAC0,
  add the live D_800BEA08 delta modulo32bits. The unsigned addition in C
  preserves the N64 low-word result without signed-overflow UB.
- If D_800C35C0[slot] is0 and the zero-extended16-bit event marker equals
  previous time but differs from current time, store-1 into previous.
  Keep the existing shared s16 marker declaration; local u16 casts recover
  retail LHU behavior, including marker32768..65535.
- Poll func_151F2CDC(void), and call func_15080228(void) only for result1.
  Reload current time and its live limit after provider effects. Clamp using
  a signed comparison. Equal, negative, wrapped and extreme values are covered.

Indexed array expressions recover the original captured offset and exact
stack reloads. Pointer-local variants have frame0x30 and15 word differences;
they are rejected. All source arithmetic/addresses assume the existing N64
32-bit ABI. Artificial guest aliases and instruction faults are qualified
separately from portable C and native behavior.

## Qualification

- **116 frozen inputs**, the complete320-byte raw body hash and all21
  relocation records are pinned. Every single-byte corruption, every
  binding-name corruption and strict-image corruption rejects. The separate
  retail body hash is checked. No ROM-word substitution or normalization.
- Both padders agree on all57 owner functions; all **56 raw and padded
  neighbors**, pools and the exact register-mask union are fixed. The actual
  three-command Game Make recipe reproduces the qualified owner under its
  no-unroll profile. The caller's separate three-command recipe reproduces
  its unchanged16-function object under its existing default O2/g3.
- Production also rebuilt the unchanged Init owner init_12560 because its
  source timestamp was newer after the preceding replay. A supplemental
  audit proves its complete seven-function object identical to Note2211,
  its source clean, and both Init sections (**181,424 bytes**) unchanged.
  Its one inherited Warning712 makes four production diagnostics in total.
  The original three-invocation Make log and extra-init-audit.json are kept;
  there is no exclusion or extra matching credit.
- Independent entire-ELF prediction allows only this320-byte slot and its
  symbol extent12->320: **255 changed bytes, zero exclusions, no metadata
  reorder**. All **6,052 addresses**, other function bodies and **189,088
  protected bytes across720 owners** remain fixed. Makefile, guards, data
  bindings, shared headers and progress CSV remain byte-identical.
- **3,442 guest cases per body** check all public memory, all provider calls
  and every pre-call snapshot. All80 words execute;53,132 accesses/body.
  Raw and retail full literal state, memory accesses and HI/LO agree.
- **Six independent GNU links /48 rebase cases per body** cover each HI/LO
  pair, signed LO carry and all R26 calls. **40 guest alias cases per body**
  and **238 fired fault-prefix pairs** compare GPR/FPR/HI/LO, all memory,
  calls/access traces, dispatched word, PC and delay origin. These do not
  claim portable C alias/fault semantics.
- Both complete original callers execute with the target connected:
  **24 frame-coordinator cases/body (185 words)** and **24 catch-up cases/body
  (66 words)**, through full returns and subsequent work. Both caller
  baselines are exact. The independent models include target effects in
  subsequent caller gates and compare inner calls/provider snapshots.
- **32 original-helper connection cases/body** execute the81-word gate
  helper,36-word audio getter and72-word command poller, with bounded OS-mask
  and queue providers. Audio values0,1,2,3,5,6,7,FFFFFFFF distinguish exact1
  dispatch. The gate helper uses only its state2 exit path (15 words visited);
  the command poller uses an empty queue (23 words visited). The audio getter
  visits34/36 words. The latter two baselines are exact; the gate helper's
  existing stub remains unmatched and receives no credit. This is bounded
  connection evidence, not full helper or hardware acceptance.
- Native32 **O0/O2/O3 each pass2,290 cases** with trap UBSan, both valid slots,
  all14 named scalar/array values, every provider snapshot and call argument.
  All **17 compiled incorrect bodies** fail observably in every native
  profile and in IDO guest execution. This includes signed marker, active
  inequality, countdown wrap, pause, event tests/sentinel, audio result,
  missing provider calls, increment and signed-clamp errors. Artificial
  global aliases/private stack effects stay outside native C claims.

Seven fresh target checks pass in each tools environment before/after
installation. Shared smoke is fresh in both; three unchanged regressions
per copy are reused by exact helper/test fingerprints. No shared helper
implementation changes. Production Make and recount agree with independent
prediction. The inherited whole-ROM checksum mismatch still makes make all
exit2. Its duplicate generated_12D630 Make recipe warnings remain.

Tools commit before consumer. Sibling tools retain2434 inherited dirty paths;
frozen host Release is untouched. Scoped Graphify refresh retains existing
unscanned nodes with evidence; it is not full-corpus extraction.

Receipts: conker/build/game-sequence-time-advance-1501E400-match/.

Next: **func_150B2340**, an80-word unmatched Game slot in generated_DF260.
A private source screen using existing struct108 emits its79-word body
directly, with one existing padding NOP. Caller/ABI, owner, guest/native and
full-image qualification are pending; no installation or credit. The80%
goal remains active.

Production ELF SHA-256: cad9d020f6a57c9e204aba389b44c542c913e5fca494ee60a13848d7fc939667.

Guard SHA-256: 6a6094f04735cb3127833e50b21f98c3374916605acd7aa79ccdebd80d22dfe7 (unchanged).
