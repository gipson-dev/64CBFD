# Active-entry reset loop matched directly

Date: 2026-11-07. Continues [Note 2152](2152-game-seeded-sprite-timer-callback-match-20261107.md)
from consumer `867bc4fa07d304d311a4201de0e44fe830e87ef3` and tools
`e6650975b6187c3b17ccf5af569911b840b31e1e`. One additional qualified
Game function advances the active 80% total goal.

## Source, ABI and live data

`func_15191400` in `conker/src/game/generated_1BA1D0.c` replaces its
zero-return placeholder with the complete **72-word / 288-byte** reset
loop. VA is `0x15191400..0x15191520`, ROM `0x1BE8B0..0x1BE9D0`.
The recovered interface is `void (ActiveResetOwner15191400 *owner)`.
Normal O2/g3, MIPS2/O32 emits **every retail word directly, with no guards**,
including the original 64-byte frame and incoming-owner home.

Local types describe a 12-byte list entry, 20-byte preset with signed
base/range halfwords, and owner fields at 0x1C/20/24. Unknown owner fields
retain offset-qualified names `value1C` and `state20`. The source updates
the target's forward declaration and two wrapper argument types/casts;
the wrappers' emitted bodies stay fixed. No shared declaration changes.

The owner float at +0x1C and word at +0x20 are zeroed before capturing the
entry list at +0x24. Exactly 60 entries are scanned. For a non-NULL actor,
byte +0x130 selects a preset before three float words +0x110/114/118 are
cleared. The actor is reloaded from the live entry and passed to
`func_1513F680(actor,13,18,0,13)`, which configures bytes +0x70..73.

The integer RNG then runs. Only afterward are the captured preset's live
signed range/base read. The timer at the then-live actor +0x1C becomes
unsigned RNG modulo `(range + 1U)`, plus base, narrowed to s16. The actor
is reloaded once more before OR-ing its word +0x58 with 1: the timer store
itself may overlap the entry pointer. The loop retains its original list,
while the final 720-byte bzero reloads the owner home and current list.

An initial qualifier experiment emitted 74 words. A local snapshot restored
72 words but left 24 register-role differences. Twelve natural local/table
forms did not improve it. An ordinary parameter naturally recovers the
complete instruction stream and live home; no qualifier or frame padding
is needed. Both ordinary byte-pointer and typed-owner forms match, and the
clear typed form is selected. One rejected scratch probe changed unrelated
qualifiers; its neighbor gate rejected it. The corrected probe scopes all
substitutions to this target before any accepted qualification.

## Complete owner and closed image proof

All **60 raw and padded neighboring functions** remain fixed. Raw metadata
only adds S5 and the saved F20/F21 pair: GPR mask 0xA31FFFFE -> 0xA33FFFFE,
FPR 0x000FFFF5 -> 0x003FFFF5. These exact fields are checked in `.reginfo`
and `.options`; all other raw pool bytes/relocations remain fixed. Padded
pools, including options when present, are literal. Four inherited pointer/
integer diagnostics remain unchanged, with no new C warnings. The existing
duplicate generated_12D630 Makefile recipe warning also remains unrelated.

The 115 frozen inputs cover source/object/complete assembly, SDK headers,
IDO executables, retained retail input, linker/registry/layout, guards,
Makefile, conversion CSV, predecessor image and graph. The complete ELF
prediction changes **219 bytes with zero exclusions**: the target's
288-byte body, symbol extent 12 -> 288, and one closed GNU symbol/string
swap at ELF 0x2DE86C, `D_800A9D40` / `D_800A6CB8`. The two complete tables
are predicted; all named definitions otherwise agree. No metadata section
is excluded. Guards, compiler profiles and Makefile are byte-identical.

## Fresh focused qualification

Seven checks pass before and after installation in both tools
configurations. All new modules/imported dependencies are fingerprinted.
The sibling executes its available helpers using a disposable new-module
overlay. Missing `alloc_pools` and `RngInstructions` helpers use explicitly
recorded, hashed mounted fallbacks read-only. All 2,434 inherited dirty
sibling paths are independently fingerprinted and preserved.

* 753 guest cases per body compare retail and compiled C with an independent
  byte-memory reference and full machine/access traces. These cover all 256
  selector representations; empty/first/last/alternating/full/repeated-actor
  lists; signed base/range extrema; unsigned RNG values; all 64 provider
  mutation masks; incoming-home redirection; and five overlap layouts.
  71 words execute. The sole unvisited word is the retained BREAK 7.
* A sparse guest timer/entry-pointer overlap witnesses the post-store actor
  reload. Its bounded RNG also clears a future entry touched by the real
  configuration byte stores. This fixture is documented as an opaque
  provider mutation and is not claimed as portable native pointer behavior.
* 63 cases per body connect 74 original helper words: the complete 16-word
  configuration setter, 18-word integer RNG and 40-word bzero slot.
  Coverage is 16/18/33 respectively, including the full 720-byte aligned
  clear. Retained production helper bytes are checked against retail.
* The aligned 616,822-word retained input census contains exactly two
  direct target JALs, ROM 0x1BDCFC/0x1BDD28, and no raw pointers into the
  target. 64 cases execute both complete 11-word callers at 0x15190840
  and 0x1519086C. They pass one argument, ignore the target result, reload
  their own saved argument and call 0x15169804/0x15169824. Those final
  services remain bounded. Target-home replacement must not redirect the
  caller's retained argument.
* 275 fired access cuts, including three delay-slot cuts, compare complete
  private bytes, GPR/FPR/HI/LO, PC and access prefixes.
* O0/O2/O3 SDK native32 builds each pass 128 independently generated little-
  endian byte fixtures with layout assertions and UBSan traps. Six actually
  compiled negatives fail with exit 11: former stub, signed modulo, stale
  actor, early preset reads, 59-entry scan and stale final clear. Native
  fixtures retain provider pointer/field mutations; home poisoning and the
  exotic sparse overlaps remain guest-only.
* Two independent GNU links/rebases include signed low16 carry. Four
  header/body/symbol/string corruptions are rejected by the strict gate.

Signed range -1 produces an unsigned zero divisor. The source preserves
the literal original DIVU/MFHI, timer-store and eventual BREAK sequence.
The numeric fixtures use nonzero divisors; neither portable C division by
zero nor the R4300 trap's exact hardware effects are claimed. No gameplay
or hardware acceptance is inferred from these tests.

Initial harness failures were local fixture issues: a scratch list overlapped
the oracle's stack region, and native setup lacked the real structure header,
RNG prototype and freestanding startup entry. They were corrected before
all fresh receipts. Production source did not change to accommodate them.
Shared smoke checks pass freshly in both copies. Three unchanged shared
regression receipts per copy are explicitly reused after exact helper/test
fingerprint checks against Note 2152. Claude calls: zero; local evidence
settled the routine.

## Actual production build and next target

Actual Make recompiles only this owner with normal O2/g3 and equals the
independent complete-image prediction exactly. All 6,052 function addresses
stay fixed; only this body changes. All 189,088 protected Game data bytes
across 720 owners remain exact. The conversion CSV remains byte-identical:
the old zero-return stub already counted as C. Compile/link pass;
`make all` reaches the expected nonmatching image checksum, exit 2.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
|Total|4,223 / 5,512|76.61%|0|1289|
|Game|3,550 / 4,839|73.36%|0|1289|
|Init|492 / 492|100.00%|0|0|
|Debugger|181 / 181|100.00%|0|0|

The 80% threshold remains 4,410 / 5,512: **187 additional exact functions**
remain. Root README receives aggregate rows only; four current indexes
receive one concise lead. Refresh Graphify with old-node retention evidence,
preserving excluded-but-existing legacy nodes fail-closed. This is not a
fresh full-corpus extraction. Commit tools first, then consumer source/docs
and the exact tools pin; wait for the fresh post-commit hook and audit.

| Artifact | SHA-256 |
| --- | --- |
|Production ELF|`b4c4477345f00a331509c8e710913a395bf75b6128985b9ed93b08c30e432ce8`|
|Production binary|`f45252906228c8c05d015c66e7e1abcccf8f5cf572b2577e8d278ebafed0b8cb`|
|Padded owner|`42fa54a3c50f3d177e2c3179ce79f0d580a23d2bfd66c92a3d9e4e772a04403a`|
|Unchanged guard manifest|`66ad0ff1fb837b102250469a08f2fa8f7e862bde40868b3b8f0357346ca8571b`|

Separate qualification, caller census, pre/post suites, shared checks,
production, graph retention and post-commit receipts remain ignored under
`conker/build/game-active-entry-reset-15191400-match/`.

Next: **func_151D0F60**, a 69-word callback-position payload factory in
`conker/src/game/generated_1FA770.c`, VA 0x151D0F60..0x151D1074,
ROM 0x1FE410..0x1FE524. Its private complete-owner candidate recovers the
indexed position callback, fallback vector, 56-byte payload and conditional
factory copy. It already emits all 69 retail words directly in the original
112-byte frame, with all 51 raw neighbors fixed. It remains uninstalled and
uncredited pending caller/helper, guest/native, padding, whole-image and
actual Make gates. Screens are retained under
`conker/build/game-position-payload-151D0F60-private/`.
Preserve the established handwritten/hidden-ABI boundaries, explicitly
frozen 150A6FA0/150A76F0, private inputs/saves, unrelated work and frozen
host Release. Keep the wider 80% goal active.
