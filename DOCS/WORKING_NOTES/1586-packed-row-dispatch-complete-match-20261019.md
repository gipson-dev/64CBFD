# Packed-Row Dispatch Complete Match

Verified: 2026-10-19. **Installed complete C recovery: all 91 instructions /
364 bytes match retail, with both existing tail NOPs retained.** The complete
93-word slot, frame0x30 and saved S0-S5/RA lifetime match.

Finish `func_1508EE0C`, generated_B3020, VA `1508EE0C..1508EF78`, ROM
`BC2BC..BC428`; alignment ends at VA1508EF80 / ROMBC430. Follow
[Note1585](1585-packed-entry-peer-lookup-complete-match-20261019.md).
Consumer predecessor **8e0f1d02**, tools predecessor **825aaa5**. Bank tools
**7a6f9fa** before the consumer source/guards/docs/pin. No push.

## Complete Source And Interface

Search unsigned row count D_80087380 through pointer D_800D23C0. PackedPeerRow
is the existing local24-byte layout view: u16 count+2, u16 entries+8, with
unknown fields+0/+4 left honestly named. Form the truncated key using
`(u16)((group <<12) + value)`, not OR. Find the **first matching row**, reset
the entry index and dispatch all its entries, including the matching entry.
Type2 calls func_15114B94; type3 calls func_1503DDD0; pass the low12 bits.
Other types perform no call. There is no distinct-peer exclusion here.

After either handler, **reload the table pointer and this row's count**.
Preserve original row index/byte offset while following the updated table;
do not cache the pre-call table or continue using its old count. After that
row's dispatch, call the already-exact20-word func_1508EDBC(originalRowIndex)
and return immediately. That helper rechecks the global count and rereads
the current table between its ordered count+2, word+4 and halfword+0 clears.
No matching row or zero global count performs no helper calls.

Use `void func_1508EE0C(u16 group, u16 value)`, retaining the address name and
concise purpose comment. The retail routine has no consistent numerical V0
result. The original prologue still stores both **full incoming words** into
caller argument homes at frameSP+0x30/+0x34, before using unsigned low16 views.

Three retained direct calls establish A0=2 and a low16 record quotient in A1:

| Call VA | ROM | Original delay | Retained assembly |
| --- | --- | --- | --- |
| 1511A264 | 147714 | NOP | 142560.s |
| 150BFF48 | ED3F8 | A0=2 | EC420.s |
| 150BFF74 | ED424 | NOP | EC420.s |

No site explicitly reads V0 before the next call or its flag/epilogue work.
The last caller physically propagates residual V0 through its epilogue; this
does not establish a meaningful success result. Do not claim a complete
recovered caller from the bounded two-word JAL/delay windows.

The type3 helper already has semantic `void func_1503DDD0(s32)` C. The type2
helper's assembly consumes one complete index word; its local s32 declaration
is sufficient for this nonnegative0..4095 domain, not proof of original
signedness. **func_15114B94 still has an unrelated production C stub.** Its
original implementation/side effects are inspected, not restored by this
change and not executed in the handler-provider tests.

## Explicit Layout

Selected ordinary C emits **91 words/frame48**,11 bindings, empty diagnostics
and15 real word differences in both existing owner profiles. Source screens
compare separate/reused indices, if/switch forms, signed/unsigned packed
locals, shared-ID locals and byte/typed views. No dummy padding, volatile,
physical-register binding, compiler-option change or shared padder change.

`game_packed_row_dispatch_layout.py` derives the remaining normalization:

- Reorder the independent row-offset and key-address work at words22..31.
  Keep both branch instructions in their positions; all destinations remain
  outside the moved nonbranch group, so no branch displacement repair.
- Apply opcode-aware GPR mappings for that closed address schedule and the
  dispatcher type/ID roles. Commute the equivalent type2 BEQ operands.
- Share the low12 extraction in the old branch-delay NOP at49; replace the
  duplicate per-call extractions at55/62 with argument moves. This is explicit
  common-subexpression/allocation normalization, not merely instruction
  scheduling and not additional gameplay logic.
- Retain all91 source positions once, with no inserted or omitted position,
  and keep all11 existing binding locations unchanged. Normalize only15
  expected-word/expected-relocation manifest rows; preserve the complete old
  manifest prefix and both alignment NOPs.

The complete raw hash, exact binding dictionary, opcode/operand checks and
normalized hash gate the recipe. Guard installation also requires the exact
qualified owner and strict first-image receipt. No original assembly,
retained data, Makefile or compiler executable changes.

```text
raw:        44b0c2eb531f5b3b30da2f7ca213838cdc20f6af6c5540f247963572be422916
normalized: 55b4439f2255412264316483b94b36c9b6cae113683edc9ee5277d887385e08e
```

## Fresh Qualification

All **10 pre-install tests pass in27.799 seconds** and **10 installed tests
pass in30.758 seconds**, without skips. The first test run exposed an
overlong huge-count fault fixture reaching an unmapped fifth row before the
requested cut. Correct the probe to a backed, fired14-access prefix; do not
interpret that fixture failure as a production bug or as parity evidence.

- **1,908 fixtures/two phases:3,816 paired literal executions** agree in full
  GP/FP/LO state, private/public memory, ordered events and helper calls.
  Dynamically visit all91 words; statically compare all91 and both tail words.
  The same corpus checks raw C's public effects/calls against an independent
  first-row numeric reference. It is reused coverage, not an additional
  independent domain, and does not assert a numerical return value.
- Six explicit bounded handler modes: no mutation, table replacement,
  shrinking current count to0, table replacement plus global count0,
  replacement/count growth to8 with a clear-rejecting global bound, and
  future-entry edits. Poison caller-saved GP/FP/LO state after helpers.
  These are provider contracts, not execution of the two retail handlers.
- **340 fired root access-cut pairs**, with every requested cut confirmed.
  Provider-internal stores are excluded from root cuts. Empty global count
  does not read TABLE. These are modeled guest access prefixes, not hardware
  exceptions or portable C fault guarantees.
- **594 selected pairs execute the actual20-word clear helper**, including
  all six mutation modes. Its complete bytes also match the retained ELF.
  Five unsigned-width probes cover high u16 row counts through an early
  shrinking callback, plus three huge u32 global-count fired prefixes; do
  not claim completed huge scans or native arrays larger than eight entries.
- Native32 **O0, O2 and O2+UBSan** each pass all1,908 numeric fixtures, checking
  112 logical observation words, plus **131,072 extra calls** sweeping all
  65,536 values in each input view against fixture-specific expectations.
  Connect the existing semantic clear C; handler mutations remain explicit
  providers. Five executed negatives (OR key, wrong handler, wrong payload
  mask, later-row continuation, cached table) exit21; positives exit0.
  Retain the existing stack-realignment/no-strict-aliasing harness policy.
- **108 actual call-window pairs** preserve saved registers, both original
  argument homes and public effects. Execute the real two-word windows,
  followed by a synthetic stop; the upstream quotient is a declared valid
  live-in, not executed. **48 extra high-word entry pairs** prove complete
  homes coexist with unsigned low16 consumption.
- **Three independent GNU layouts** agree for all91 instructions and11
  bindings, including HI/LO carries and call addresses. Execute **552 mapped
  cases** with code, globals, handlers and both row banks rebased. Actual
  clear instructions are connected only at the default map; rebased helper
  calls use bounded providers. Selected fixtures are reused, not new inputs.
- Sixteen raw/binding/recipe corruptions reject. Six manifest corruptions
  fire the actual padder's stale-word/relocation checks; three changed-image
  controls fire the strict verifier. Both owner profiles preserve72 other
  routines and normalized pools; actual padding preserves those bodies,
  addresses and pools. All seven expanded shadow Make commands agree.

## Production And Commits

First private link exactly matches the independently predicted complete
3,257,636-byte ELF on its first attempt. Actual Make reproduces that identical
image: **287 changed bytes =285 target-code bytes +two target-symbol size
bytes** (12 ->364). No symbol-order/string permutation or metadata exception.
All other6,056 bodies, every address, all189,088 protected Game-data bytes /
720 owners, historical guards and other frozen inputs remain fixed.

The wider manifest-triggered rebuild succeeds with inherited duplicate
generated_12D630 recipe warnings and diagnostics from untouched code. Both
target owner profiles have empty diagnostics; the whole build is not claimed
warning-free. Full build log: ignored
`conker/build/game-packed-row-dispatch/integration/production-build.log`.
Git's existing CRLF advisory is not a build or CSV-parser failure.

```text
owner:  683e47b76b3db771b532b1959ad0e9f642b29b013d87777026020d62b38065c7
guards: 3126566e693decebd75d4ad1c088626c63ec19de18d3f3572882f4c830e70fd1
ELF:    da178d6b0ea5c11261fce0de32475e3b13287696034b80e2d10d592ee721dcc9
```

Fresh matching: **Game3001/4832 (62.11%)**, **total3674/5505 (66.74%)**,
Init492/492, Debugger181/181, **1,831 different / zero drift**. Conversion
counts/bytes stay5505/6044 (91.08%),86.08% overall and4832/5323 (90.78%),85.44%
Game: the old placeholder was already counted as C. README aggregates only.

Both tools copies pass three repository-setup tests and smoke checks;
consumer `make tools-check` passes. The five new files are identical,
ASCII/Python-valid in the standalone mirror. Preserve its ddbdd16 HEAD and
all1,328 prior dirty leaf hashes; add only five files for1,333 dirty leaves,
without a mirror commit/reset. Post-commit graph preservation is a separate
gate in ignored `integration/graph-audit.json`. No compiler capture, Claude
call, REA setup, sibling host or Release action.

```sh
python3 -m unittest tools.tests.test_game_packed_row_dispatch_match -v
python3 -m tools.experiments.game_packed_row_dispatch_integration --audit
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Remaining Owner And Next Target

Reaching the last function does **not** finish generated_B3020. Fresh slot
audit: **53/73 exact,20 different**, no remaining GLOBAL_ASM. Retain the full
numeric receipt in ignored `integration/owner-completion.json`. Open names
(all retain their1508 prefix):

```text
func_15085BE8  func_15086098  func_15086364  func_15086D94
func_15089BC0  func_15089F9C  func_1508A1BC  func_1508A6FC
func_1508B3F8  func_1508B9BC  func_1508BC20  func_1508BF14
func_1508C1A4  func_1508C5B8  func_1508C9CC  func_1508CAD8
func_1508D850  func_1508DA1C  func_1508DAEC  func_1508DC24
```

Resume **func_1508C9CC**, the smallest remaining owner slot: VA
`1508C9CC..1508CA88`, ROM `B9E7C..B9F38`, **47 words/frame0**,45 current real
differences and a false zero-return stub. Original code advances a signed
byte cursor at D_800D23B0+1702, wraps against signed byte D_8008FD8C, checks
0x32C-stride actor presence, nested+31C pointer and byte+84, then excludes
masked slots through u16 D_800D18A0. Keep do/while first-iteration behavior,
signed-byte wrapping, final cursor store and -1 fallback. Inspect callers
and valid shift/array domains before source fitting and installation.

The following physical owner starts at **func_1508EF80**, game_BC430:55 actual
instructions plus one tail NOP, frame0x40, still a stub. Its float X/Z rotation
is separate work, not a finished neighbor or the next generated_B3020 member.
The broader Game decomp/matching goal remains active.
