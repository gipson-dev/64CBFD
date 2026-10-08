# Game Palette Updater And Connected Color Qualification

Date: 2026-10-04. Starting HEAD: `d2400309`.

Subsequent [Note 982](982-game-viewport-command-helper-semantic-recovery-20261005.md)
recovers the complete initial command helper `func_1510B7B4` and qualifies its
twelve-packet cursor contract. The full `func_1510B9D0` renderer below remains
pending; historical placeholder statements describe this note's checkpoint.

## Decision

Continue [Note 972](972-game-palette-color-emitter-byte-match-and-segment-connection-20261004.md)
by replacing `func_1510CB10`'s zero-return placeholder with its actual void,
signed-slot palette updater. The body fits **168 words / 672 bytes in the
170-word / 680-byte retail slot**, retaining the original **0x68 frame**.
It remains non-matching at **135 raw aligned word positions**. No expected-word
guards, compiler override, ownership change or address drift are added.

The exact 42-word color emitter remains unchanged. Actual updater -> color ->
queued-writer source connections are qualified in bounded fixtures; the complete
render caller and physical RSP/RDP/natural effects remain separate gates.
README aggregates stay unchanged: this placeholder was already counted as C,
and the updater is not a new byte match. Production Init and sibling Release
are untouched.

## State And Table Contract

The record base is `D_800DBFF0`; each slot has a 0x9A0 stride. Read its word at
offset 0x5F0 and return without any palette/tick read or callback unless bit zero
is set. No NULL, slot-bound or pointer-validity guard is invented.

The qualified ordinary palette domain is slots 0..3. Existing storage is only
referenced, not redefined or moved:

| Table | Shape | Purpose |
| --- | --- | --- |
| `D_800D9E70` | Four rows of three u16 values | Channel phases |
| `D_800D9E88` | Four rows of three u8 values | Phase increments |
| `D_800D9E98` | Four rows of three u8 values | Channel amplitudes |
| `D_800D9EA8` | Four rows of three u8 values | Interpolated channel values |
| `D_800D9EB4` | Three u8 values | Shared default target |
| `D_800D9EB8` | Four rows of three u8 values | Custom target; first byte also selects custom mode |
| `D_800D9B68`, `D_800D9B78` | Four rows of three u8 values each | Primitive/environment RGB output |

Capture the low-word doubled tick step and custom row's first byte once before
the channel loop. A zero first byte selects the shared default for all channels,
even if the other custom bytes are nonzero. Process exactly three channels:

1. Capture the unsigned current value and chosen target. If unequal, snap only
   when absolute difference is strictly less than the signed captured step;
   otherwise add/subtract that step with retail low-word wrapping. Store the
   resulting byte only on an unequal path. Retain the full local value for the
   later adjustment, not a reload of its truncated stored byte.
2. Call existing `func_150489B0` with `(phase >> 4) & 255`. Read amplitude after
   the callback, multiply as single precision and truncate toward zero. Add the
   captured local value and subtract 127 with low-word arithmetic.
3. For a nonnegative adjustment, add it to the primitive byte; otherwise
   subtract it from the environment byte. **Wrap to a byte before clamping.**
   Clamp both resulting RGB bytes to 127 if their unsigned value is at least
   128, including the side not adjusted. This is not saturating addition.
4. Reload phase and increment after the callback. Store their u16 sum first,
   then store the same value masked to twelve bits. Preserve both ordered stores.

Finally clear only the custom row's first byte, not all three bytes. A repeated
call therefore selects defaults until that first byte is set again.

The native connected fixture uses the actual existing angle-helper C and the
checksum-verified 65-entry quarter-wave table at `0x8009A220`. The linked helper's
complete 36-word slot remains raw-exact. Callback-mutation fixtures separately
prove captures/reloads; they do not claim the ordinary helper actually mutates
these globals.

## Qualification

Fourteen new tests in
[`test_game_palette_updater.py`](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_palette_updater.py)
extract the actual production updater, color emitter, queue helpers/writer and
SDK macros. They do not substitute a duplicate updater implementation.

Native strict 32-bit fixtures qualify **398353 cases**:

- 196608 current/target cases: every byte pair under steps derived from ticks
  -1, 1 and 128, with independently calculated outputs.
- 196608 primitive/environment byte pairs under negative, zero and positive
  adjustments, independently asserting wrap-before-clamp behavior.
- 5120 actual angle-helper -> updater -> color -> writer workflows: all 256
  angle bytes, five amplitude boundaries and all four slots, using retail
  quarter-wave table values and independent reflected-index expectations.
- Sixteen disabled-gate cases and one callback-mutation workflow. The latter
  changes tick/base/selector after the first call, current/future channel data,
  amplitude, phase, increment and colors; captured values and late reloads are
  checked independently.

The bounded big-endian low-word instruction model qualifies **1251 complete
paired routine traces**: updater 1107, color 72 and queue writer 72. It compares
all mapped external memory, ordered external stores, callback arguments and
state snapshots, and saved-register/stack restoration. Stack contents may differ
between valid compiler layouts and are not falsely required to match.
Three additional invalid-slot prefixes stop at unmapped flag reads before
external stores/callbacks; these are not complete safe-invalid executions or
physical N64 fault acceptance.

The paired corpus covers all four rows, custom/default selectors, signed tick
and wrapping-step boundaries, finite fractional/negative helper results,
captured versus callback-mutated state, u16 addition/wrap/mask stores, and
three-frame updater -> color -> writer connections. Repeated calls explicitly
verify custom-first-byte clearing and subsequent default selection.

Reachable instruction coverage is separately asserted: **162 / 168 C body
words and 164 / 170 retail words execute**. The excluded six in each body are
four unsigned-byte float-correction instructions that cannot be reached from
LBU values and two branch-over duplicate instructions. Padding is not credited
as execution. Do not report all 170 retail words as executed.

This extends the existing low-word oracle only for these branches, arithmetic
shifts, finite signed float conversion and truncation. It is not a general
MIPS/FCSR emulator. NaNs, invalid/out-of-range float conversion, trap flags,
arbitrary table aliases, hardware timing and natural rendering are not qualified.
The actual ordinary helper/table workflow is tested separately from injected
callback values. Ordered source-read traces are not claimed identical; externally
observable stores and callback-state boundaries are paired explicitly.

Receipt: ignored `conker/build/game-palette-updater-qualification.json`, with
actual per-function/native counts and full-module completion flag. Partial
test selections do not receive complete-corpus credit.

## Build And Regression

The affected source freshly compiles, pads and links, then regenerates progress
and runs the matcher. Existing duplicate `generated_12D630` recipe warnings
remain; no new source warning. Independent isolated IDO compilation/linking
reproduces the full production slot, 0x68 frame, callback word, trailing padding,
retail symbol address and absence of updater guards.

**All 257 combined checks pass in 52.247 seconds, no skips.** This is Note 972's
243-check command plus the new fourteen-check module. The standalone module
also passes all fourteen in 6.568 seconds after fixing an unused native fixture
table warning; no production-body change was needed for that harness correction.

| Complete Slot | Words / Raw Differences | SHA-256 |
| --- | ---: | --- |
| Updater C | 170 / 135 | `0954376ea7ac52711bb8b9ccc922eb10c0a8cdb8164cb1d84caea013461922e4` |
| Exact color emitter, unchanged | 42 / 0 | `a1b386a82d28205880c5f04ac0e29057a9f2836f6b607d682b106490da0c2bc4` |
| Exact angle helper, unchanged | 36 / 0 | `11c6a3f191d36b5ad898a05a71b8a00489ebc54a7826794d54bc1f56134c93e1` |
| Queued writer C, unchanged | 44 / 38 | `f3a227545fc8d35dd017430e12f6fd1da0512c5746e400423358eee3a9566feb` |

Complete Init code/data, Debugger code and Game data remain raw retail-exact;
the 47 intentional/investigation Init ASM owners and all previous recovery
identities remain intact. The matcher stays total 3283 / 5463, Game 2610 / 4790,
Init 492 / 492, Debugger 181 / 181, zero drift and 2180 differing C functions.
No aggregate gain is inferred from replacing an already-counted placeholder.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_palette_updater -q -f
make tools-check
git diff --check
```

## Sibling And Next

Read-only sibling audit finds the full original recompiled updater in active
`recomp_out/.c` at line 820217, including its existing gated CBFDBLEND/CAT06BLEND
diagnostics and original call/epilogue. The scoped host src/CMake search finds no
named override. No host synchronization is inferred or performed; host source,
builds, saves and frozen Release are unchanged. Existing instrumentation/body
presence is not fresh PC runtime acceptance.

Retail's direct updater caller is **`func_1510B9D0`**, the 356-word renderer:
it calls updater at `0x1510BAD0`, then color emitter at `0x1510BAE4`. Both the
caller and its 105-word initial command helper `func_1510B7B4` remain zero-return
DECOMP placeholders. Continue with that complete caller and its command-helper
dependencies, preserving the signed-halfword slot and display-list cursor.
The larger `func_151137D4` color/writer caller remains another unqualified path.

The qualified synthetic updater -> color -> queue connection does not prove
either complete renderer, actual submission, RSP/RDP pixels or natural effects.
Keep queued-writer matching (38 differences), updater matching (135), staged
texture producer recovery and pending PC stubs as distinct open tasks.

- [x] Recover the complete updater and correct void/signed-slot interface.
- [x] Preserve interpolation, wrap/clamp, callback captures/reloads and phase stores.
- [x] Connect actual angle helper, updater, color and queue writer in native fixtures.
- [x] Qualify paired big-endian state/store/callback boundaries and reachable words.
- [x] Pass all 257 combined checks and preserve complete exact Init/Debugger/data.
- [ ] Recover full caller `func_1510B9D0` and required command-helper dependencies.
- [ ] Qualify complete render submission and natural RSP/RDP effects.
- [ ] Pursue updater/queued-writer raw matching without broad instruction guards.
- [ ] Recover staged texture producer and synchronize pending PC stubs separately.

Recovery narration remains in docs; README aggregates do not change. No broad
Init conversion, ROM promotion, sibling build, frozen Release change or push.
