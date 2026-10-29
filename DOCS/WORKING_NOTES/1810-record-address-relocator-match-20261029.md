# Record address relocation: direct C match

Verified 2026-10-29. `func_15003120` replaces its zero-return placeholder in
`conker/src/game_305D0.c`. All **51 instructions** emit directly from semantic
C under the existing IDO `-O2 -g3` profile. The routine has no frame, helpers,
alignment words, inserted instructions or new guards.

The adopted ELF recount is **3,888 / 5,506 (70.61%)** byte-exact C functions:
Game **3,215 / 4,833 (66.52%)**, Init 492/492 and Debugger 181/181. There is
zero address drift and 1,618 C functions still differ. Reaching 75% requires
4,130 exact functions, leaving **242**. The conversion inventory is unchanged.

## Recovered behavior and interface

`void func_15003120(s32 index, u32 offset, u32 *records)` installs the incoming
list address into the selected pointer-table slot and clears its count byte.
For a nonnull input, it adds the relocation offset to that slot, walks the
12-byte records until the first word is zero, and adds the offset to the
first two words of each record. The third word and terminating record stay
unchanged. The final count is stored modulo 256.

The repeated global and table accesses matter when guest memory overlaps.
The source retains those reloads instead of caching the record pointer.
Unsigned address arithmetic also preserves the original 32-bit wraparound.

The shared declarations now correctly describe `D_800B0E30` as `u32 **` and
`D_800B0E34` as `u8 *`. They are pointer cells, not inline arrays: the original
instructions load a pointer from each global before indexing its backing.
Only those two lines change in `conker/include/variables.h`.

The full-ROM census finds one aligned direct call, at ROM `0x30804`, and no
aligned target pointers. Its original parent is `func_150031EC`, which remains
a C placeholder in the same owner. The 23-word window at
`0x15003314..0x15003370` supplies `S2` as the index, `S0` as the relocation
base, and the word at `S0 + 0x20` as the incoming list. It also relocates three
header fields and discards the target result. The caller's rejection branch
and both successor boundaries are covered; its complete 178-word routine is
not claimed recovered or fully qualified.

| Evidence | Value |
| --- | --- |
| Body and complete-slot VA | `0x15003120..0x150031EC` |
| Body and complete-slot ROM | `0x305D0..0x3069C` |
| Owner | Nine compact functions; all eight neighbors unchanged |
| Global relocations | Four HI16/LO16 bindings at offsets 0, 4, 8 and 12 |
| Raw/original object-body SHA-256 | `4e1da0c4aca1f610e094b44913958f14c6e3d30093b6336abac4de5e2ccea2bf` |
| Linked retail-body SHA-256 | `0878890f2971af6eaddb6dfb0b79e25055aa3a3da7b6cf6ddf352435ce6362c1` |
| Adopted ELF SHA-256 | `ac67fd82de83fdabaca9ae2eb56c9e9454e09a709f4906a3392dd4bc152eaac0` |

## Qualification

All eight focused methods and the shared tools checks pass in both tools
copies. After production, each copy passes two fresh installed checks and
reuses six semantic checks by complete module, input and artifact identity.

- **488 guest cases** cover all 51 target words, null and empty lists, counts
  through 257, unsigned offset wraparound, sparse full-word indices, and four
  overlapping-memory classes. Complete RAM, registers, access trace and the
  untouched stack agree with retail. A cached-pointer implementation fails.
- **52 original-caller cases** cover all 23 window words, including its
  branch-likely rejection load, conditional header relocations, actual target
  arguments and discarded return value. A missing initial coverage case was
  corrected in the fixture; no production instructions were changed for it.
- **240 native32 SDK cases per profile** pass at `-O0`, `-O2` and `-O3` with
  trapping UBSan, typed backing and canaries. Guest-only aliases and sparse
  indices are excluded from portable native claims. Six incorrect C bodies
  fail native checks; seven fail the compiled MIPS checks, including caching.
- **123 paired fault prefixes**, including eight delay-slot cuts, agree in
  complete memory, registers, trace, PC and delay state. These qualify emitted
  instructions, not portable C fault behavior.
- **27 cases across three GNU layouts** rebase all four bindings, including
  HI16/LO16 carry boundaries. Original, raw C, padded and actual-Make words
  agree. Fifty-one word corruptions and four binding corruptions are rejected.
- **225 strict-image controls** cover every target byte, its symbol record,
  adjacent code, the caller window and truncation. The unchanged guard
  manifest is separately fingerprinted and corruption-tested.

## Shared-header and production audit

The actual three-command owner Make rule compiles, pads from the retail
layout, and assembles. It reproduces the qualified object without target
diagnostics. Raw and padded neighbor bodies, bindings and pools stay fixed.

The shared-header audit follows transitive includes and rebuilds **209 linked
C owners**. Of these, 201 objects remain byte-identical. One is the intended
target; seven differ only in compiler metadata. Fresh before-and-after builds
prove that all seven preserve their code, function inventory, relocations,
pools, loaded sections and register information. Their only changed named
declaration sizes are the two corrected pointer cells. Some previously cached
objects also held older header metadata; that stale metadata is refreshed.

IDO embeds build time and output path in `.mdebug`. Consequently, comparing
private-build and production object hashes was too strict. The validator now
compares every other section literally and decodes the debug symbol, file,
procedure, auxiliary, line and string tables. It accounts for only the known
private output-path prefix and compiler timestamp. All other debug records
must agree. Fifty-six controls corrupt code, symbols, data or debug records
and are rejected. This is an object-metadata comparison, with no linked-image
exclusions or replacement instructions.

Both the relink using all rebuilt dependent objects and production reproduce
the independently predicted complete ELF. It changes by **147 bytes**:
146 target instruction bytes and one symbol-size byte, recording 204 bytes
instead of the old 12-byte placeholder. There are zero linked metadata changes
and zero comparison exclusions. All 6,056 function addresses, 6,055 other
bodies, and 189,088 protected Game data bytes across 720 owners remain fixed.
The conversion CSV, guard CSV and compiler profiles are unchanged. Production
completes with existing warnings in other owners; the target is diagnostic-free.

The audit checks 536 focused inputs and 16,568 sealed current inputs. The older
tools mirror retains its 1,871 inherited dirty paths plus the three target
modules. Tools are banked first: `9fde3ce72a8f97b88250b99eeaefe2b4719e0aa7`
adds qualification, and `a445ec0549787b8403d087f4680828fb843bd17b` handles
the observed IDO debug metadata. The consumer commit contains the recovery,
two declaration corrections, tools pin and measured docs. No push is included.

Ignored evidence is in `conker/build/game-record-address-relocator-match/`.
The independent final audit and banked seal record the adopted state. The
twelve-file Graphify refresh checks old-node and valid-relationship retention;
historical global analytics are not represented as a new full-corpus scan.

## Cash-label dependency and next work

The privately screened `func_151D7000` remains **uninstalled and uncredited**.
Its 51-word candidate has one commutative multiply operand-order difference,
but its live return contract depends on the variadic formatter chain.
`func_15042E3C` is currently declared `void`; the actual `func_15042ECC`
formatter remains an empty C placeholder.

The connected original-code audit in
`conker/build/game-cash-label-match/return-chain-v3.json` passes **120 cases**
through the 35-word callback caller, the cash callback, three actual setter
helpers, the 36-word variadic wrapper and the 252-word formatter. For the
fixed `$ %d` format it covers 177 formatter words, checks all 16 copied stack
words, and compares raw-candidate and retail state. Allocation and string
formatting remain explicit service boundaries.

Twenty cases reject forcing a success return: allocation failure returns zero,
which causes the caller to expire the record. Returning one incorrectly keeps
it active. The original formatter's empty-format return behavior also needs
care before establishing a general C interface. Recover that dependency rather
than assigning the callback a fabricated success value. No broad formatter or
complete gameplay claim follows from these bounded cases.

Next inspect **`func_150F6890`** in `generated_1228D0.c`, the next unparked
51-word placeholder. `func_1514E920` remains parked. The 75% goal stays active.
