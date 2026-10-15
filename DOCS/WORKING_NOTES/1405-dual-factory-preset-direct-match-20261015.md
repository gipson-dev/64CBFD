# Dual Factory Preset Direct Match

Date: 2026-10-15. Continue the complete additional-source / Game objective
after [Note 1404](1404-table-fade-callback-frame-restoration-and-guarded-match-20261015.md).

## Result

Replace `func_1516F2F8`'s zero-return placeholder in
`conker/src/game/generated_19A8B0.c` with its complete six-input void routine.
**All 148 raw and production-padded words / 592 bytes match directly from C**,
VA `0x1516F2F8`, ROM `0x19C7A8`, original frame **0xD8**. No new guards,
profile changes, volatility, padding locals or shared prototypes.

The two calls each submit the complete 49-word `func_1516D99C` packet for
preset 0x2B. The first uses submode 2 and arg1; the second uses submode 3,
constant 7, arg2 and arg3. Preserve full-word arg1/arg2/arg3/arg5 forwards,
the first input's captured low byte, and both fifth-input byte reads. Keep
the address-based name and measured comment rather than inventing a gameplay
name. Both call sites execute regardless of the first allocation result.

## Source Fitting And Archive Evidence

Freshly compile the complete archived draft in the current owner context:
**149 words / 108 differences / frame0xE0**, zero diagnostics. It is not a
raw import match. Preserve the archive unchanged; use its intent only with
the original assembly and independent packet checks.

Screen **25 maintained source forms**. Ordinary scalar/cast uses keep the
converted fifth byte in a private home across the first call, producing
149/108/frame0xE0. Some mask/shift forms recover the frame but add instructions
and different field loads. Register hints, simple address/dereference forms,
parameter-width changes and scalar declaration changes do not close it.

The explicit second-call `(u8)(&arg4)[0]` retains the original live fifth
input read. That gives **148 words / two differences / frame0xD8**; only the
snapshot store/reload is at `SP+0xD0` instead of retail `SP+0xD4`. Reading
`(&firstType)[0]` at the second call retains the named snapshot's original
home and closes both words. All 148 words now emit directly. Two other
indexed snapshot forms tie the same function; do not count them as extra
matching functions. These are ordinary address-based C object accesses,
not fixed stack offsets, dummy locals or physical-register bindings.

The initial capture had 53 inputs. Discovering the second caller expands the
scope to **55 unique inputs** in the new owned
`conker/build/game-dual-factory-preset-complete-callers/` directory. Preserve
the original `game-dual-factory-preset/` manifest/captures; never rewrite a
frozen manifest to bless a changed scope.

## Caller Boundary

An ignore-inclusive source/assembly search finds **five original call sites
in two callers**, not just the first default-search result:

- `func_150265CC`: call at `0x15028664`; the seven-word setup window begins
  `0x15028650`, ROM `0x55B00`.
- `func_1506DE84`: calls at `0x1506E000`, `0x1506E02C`, `0x1506E058`,
  `0x1506E0C4`; setup windows begin at ROM `0x9B494`, `0x9B4C0`,
  `0x9B4EC`, `0x9B558`.

The original callers ignore the result, supporting the void interface.
Execute all five original setup windows over both stack phases and require
the actual CALL boundary to fire after its delay-slot stack store. Verify
all six physical words, including full-width actor quotient/delta/control
in the large dispatcher and the four small caller constant packets.

**All five corresponding current linked windows are placeholders**, with
zero matching words in these sampled windows. The test makes that boundary
explicit; it is retail-window ABI evidence, not current/full-caller execution
or gameplay acceptance. Both caller owners and their original assembly are
pinned and unchanged. No caller restoration is silently bundled into this
function match.

## Fresh Qualification

**All 14 installed checks pass in 158.928 seconds**, no skips:

- **4,120 paired guest cases** check both full 49-word packets, complete
  private RAM/registers, memory/call events, LO/FP state, stack restoration
  and all 148 visited instructions. Cover high-bit inputs, two stack phases
  and four provider modes. The first packet's final arg1 store and second
  packet's final arg5 store remain in their call delays.
- Preserve the first-byte capture and original post-call home reads when
  modeled providers overwrite outgoing homes, incoming parameter homes or
  the saved snapshot home. The latter is synthetic guest alias evidence;
  do not claim that a native C provider can access an unescaped local.
- **636 paired fired guest-memory faults** match literal partial states.
  Every injection fires. No affine stack normalization or portable C fault/
  hardware exception claim.
- **65,536 native32 cases per O2/O0 profile** execute the complete C with a
  two-packet 49-word capture provider. All **eight native negative controls**
  fail, including explicit narrowing of the three full-word forwards.
- **Seven effective compiled guest negatives** fail the packet checks:
  wrong snapshot, wide fifth input, wrong preset/submode/last input, cached
  fifth byte and changed snapshot home. The three narrowing-cast controls
  compile to zero word differences under current IDO; they are **native-only
  capture-contract negatives, not effective guest negatives**. Do not inflate
  counts or attribute the archive's machine mismatch to these discarded casts.
- **256 actual current factory/allocator-chain pairs** execute both real
  125-word factories and the 28-word allocator wrapper. Cover all four
  first/second null/success combinations with two separately backed records;
  check both full packets, initialized fields and untouched record padding.
  Lower heap and registration providers remain modeled.
- Three independent original/C links match all 148 words with both call
  bindings rebased. Ten original-caller setup cases fire their actual call
  boundaries, with the current placeholder distinction above.
- Preserve all 29 owner neighbors' raw sizes, bytes, relative relocations
  and pools. Reject unknown compiler shape/diagnostics and already-recovered
  source. Freshly check all **801 original archive fingerprints**.
- Verify all **55 live inputs**, all 55 immutable-before flips, source-text
  corruption, six physical target/symbol/factory/allocator/caller changes,
  and both exact successor inputs and before/after capture controls.

The corrected pre-install run passes ten checks in 24.845s. Its first run
incorrectly expected discarded narrowing casts to be guest negatives and
omitted backing for the second reference record's untouched padding. Correct
those fixture assumptions before installation; neither was a production fix.
Reuse established parsers, compiler/padder, guest/native and factory helpers;
no shared helper is modified. Zero Claude calls or dependency/account changes.

## Complete Image And Progress

Predict the entire **3,257,636-byte ELF** from the frozen predecessor plus
the original target slot and symbol extent **12 -> 592** before installation.
The normal build equals that independent prediction byte-for-byte. Exactly
**442 bytes change**, all target slot/extent. **Every other byte is fixed**;
there are zero metadata allowances or ignored symbol sections.

Only **ELF and owner** change among the 55 scoped inputs; all **53 others**
remain fixed. Preserve every guard CSV byte, all progress rows, original
assembly, shared headers, compiler profiles, both caller owners and
**189,088 protected data bytes / 720 owners**, zero differences.

| Installed Input | SHA-256 |
| --- | --- |
| ELF | 030d51f9d4b5a73f952fd8a47f76406a06316609a1b1948341666dc48492bc0f |
| Owner | daeb7baa0e9de73371b03d469ecaf3042f10fad753c9b4db997254cfc82f07dc |

Fresh official matcher: **Game 2,900/4,828 (60.07%)**, **total 3,573/5,501
(64.95%)**, **1,928 different**, zero drift. Init 492/492 and Debugger 181/181
remain exact. Converted counts/bytes do not grow because this replaces an
already-C-classified stub. Root README updates only two matching rows.

The normal build recompiles the one owner and succeeds with zero target
diagnostics. The existing duplicate generated_12D630 recipe warnings remain;
do not claim a warning-free complete build or fix unrelated warnings here.

## Banking And Next Work

Bank tools **28f7a09** first, then consumer source/docs/pin. Shared tools
checks and both Windows syntax/standalone checks pass. Preserve independent
older mirror HEAD **ddbdd16** and all **676 initial dirty fingerprints**;
copy only four absent owned paths for **680 final paths**, all equal active
tools. No older-mirror commit/reset/history copying, push, host source/build/
launch, installs, account changes or frozen Release operation.

Full Graphify update refuses **19,440 nodes against 41,219**, retaining
19,398 nodes from 2,972 excluded-but-present files. Preserve that fail-closed
result; await actual incremental commit workers separately.

Prepared WSL consumer-root reproduction:

```sh
python3 -m tools.experiments.game_dual_factory_preset --screen
python3 -m tools.experiments.game_dual_factory_preset
python3 -m unittest tools.tests.test_game_dual_factory_preset tools.tests.test_game_dual_factory_preset_installed -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
```

Next inspect **func_1516F548**, **199 words / 796 bytes**, ROM `0x19C9F8`,
frame `0xF8`, in the same owner. Recover its true incoming argument layout,
fixed-point shift/sign behavior and complete constructor packets before
choosing C types or copying the archived scratch locals/parameter numbering.
No next-function edit or full-caller restoration is included here.

The earlier 1,717-object audit remains historical, not freshly rerun. This
turn freshly compiles the one archived function and 25 source forms, verifies
55 inputs/801 archive hashes, and completes this one raw C match. Retain the
inherited-stack renderer deferral and complete
[failed-comment/binding/unanchored queues](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md).
The full additional-source / Game objective remains active and incomplete.
