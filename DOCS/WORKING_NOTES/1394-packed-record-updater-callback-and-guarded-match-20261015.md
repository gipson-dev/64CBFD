# Packed Record Callback Update And Guarded Match

Verified 2026-10-15. Continue from the committed factory in
[Note 1393](1393-small-record-factory-direct-match-20261015.md). This recovers
its neighboring updater; the whole additional-C / Game goal remains active.

## Target And Contract

| Item | Value |
| --- | --- |
| Function / owner | func_1516D678 / generated_19A8B0 |
| VA / ROM | 0x1516D678 / 0x19AB28 |
| Complete slot / frame | 48 words, 192 bytes / 0x18 bytes |
| Callback table / time step | D_8008CBA0 / D_800BE9E4 |
| Cleanup | func_1516972C, unchanged byte-exact 28-word C body |
| Consumer / tools predecessor | 548318e3 / b545f58 |
| Profile | Existing O2/g3, unchanged |

The archive `game/game_19A8B0.c` gives the broad flow but has incorrect word
loads, a word-sized secondary clear, and a call to the callback table's
address rather than its selected function pointer. Recover the real byte
countdown and selector, signed Y/velocity halfwords, fractional byte and
secondary pointer. Use a typed callback-pointer array and the existing
`struct102` type for cleanup through a local `structs.h` include; no shared
header content or helper definition changes.

The first countdown update is gated by a nonzero byte. Subtract the global
word modulo 32 bits, interpret that result as signed and clamp negative values
to zero before storing the low byte. Invoke the selected callback with the
record, and remove **only when its result is exactly 1**. On that path, reload
the secondary pointer after the callback and clear its **halfword** lifetime
at offset 4 before cleanup. On every other result, reload the time step and
live Y/velocity/fraction fields and advance the 24.8 coordinate modulo 32 bits.
Use unsigned arithmetic for the wrapping operations and multiplication;
replace a negative signed left shift with bounded signed multiplication by
256. No signed-overflow or negative-shift compiler relaxation is required.

The real static callback table has nine entries. Tests also use a deliberately
backed 256-entry fixture to exercise unsigned byte indexing; this does not
declare selectors 9..255 valid in retail gameplay.

## Compiler Shape And Guards

The initial corrected body is 48 words / 16 differences. A single countdown
value removes three allocation differences. Staging the coordinate base and
shift yields the original instruction order and all but three final words.
Bounded expression and six local-order screens retain those three differences.
Inlining the final expression twice emits 53 words, including a necessary
global reload, and is rejected. The older archive's 50 words / 38 differences
is historical lead evidence, not the installed form.

Three expected-word guards preserve one closed final temporary lifetime:

- 0xA0: `addu v1,t4,v0` becomes `addu t6,v0,t4`.
- 0xA4: the arithmetic shift reads t6 instead of v1.
- 0xAC: the fractional-byte store reads t6 instead of v1.

All other words are fixed. The guards touch no relocation, load width,
callback lookup, branch, pointer, arithmetic operation or memory order. Pin
the full raw object hash and all seven relocations; reject every one of 48
individual raw-word flips and every missing relocation. Preserve the entire
previous guard file byte prefix and append only three rows.

This is a **guarded C match**, not direct compiler identity. Raw C remains
three words different. Raw and guarded executions agree on memory, accesses
and calls; only the guarded complete guest state is claimed retail-exact.

## Fresh Qualification

All **14 focused checks pass in 26.586 seconds** across
`test_game_packed_record_updater`, `_candidates` and `_installed`.

- 1,536 guest cases cover all byte counters/selectors, full-word wrap/sign
  boundaries, callback results 0/1/2/-1/extremes, post-callback mutations and
  record/stack/global aliases. An independent memory/call reference agrees.
  A zero-countdown removal case explicitly proves no time-step load occurs.
- 152 paired, fired access-fault prefixes preserve the complete retail guest
  order. This is not portable C fault semantics or N64 hardware acceptance.
- Actual selected C passes 4,096 native32 cases per O2/O0 profile with live
  callback data, counter observations, secondary/null/alias pointers and
  halfword canaries. Six compiled negatives fail in guest and native fixtures:
  truthy callback result, signed byte countdown, cached pre-callback time step,
  stale binding, word-sized clear and lost fractional byte. Mutants receive
  no matching guards. Reuse the existing CopyOracle signed-byte handler.
- The first native control run exposed correlated provider-mode/result samples
  that missed a word clear. Decorrelate those samples and add the adjacent
  halfword canary; rerun all six effective controls. No production behavior or
  acceptance check was weakened to pass the fixtures.
- Independently assemble all original words for three text/table/time-step/
  cleanup rebase pairs, including signed-low carry boundaries and both paths.
- 128 lifecycle cases execute the real 100-word constructor, 28-word allocator,
  37-word binding creator, recovered 48-word updater and unchanged 28-word
  cleanup, with the nine real callback-table words. Check null binding,
  callback selection, unlink, type-dependent destructor/default dispatch and
  the lifetime clear observed before unlink. Lower heap, registration,
  record-builder, callback, unlink and destructor providers remain opaque.
  These are bounded models, not complete gameplay or host-port acceptance.
- All 29 other owner functions retain raw bytes, extents, relative relocations
  and normalized pools despite the new local type include. The real production
  generated-owner padder is exercised. Reuse unchanged earlier broad-suite
  receipts explicitly; do not call them fresh runs.

## Complete Image And Progress

The guard dependency triggers the normal broader generated-owner/SDK rebuild,
which succeeds. Construct the entire expected ELF independently from the pinned
predecessor, 192 retail bytes and only symbol extent `12 -> 192`. The installed
ELF equals it: **140 changed bytes**, target slot/extent only, zero metadata
allowances. Every other ELF byte and all **189,088 protected bytes / 720
owners** remain fixed. Known duplicate generated_12D630 recipe warnings remain.

| Input | SHA-256 |
| --- | --- |
| ELF | 42f179ad6efccc701900d9345de5a57c80aab7254e0c48d06c98d0f47e1f5422 |
| Owner | ebbba82f26704db4a11c78c43986dfd535f242c96965a2e637568fa33b814275 |
| Guards | 148fb6500b75e725b6b98fe056c45b72d111eab0c93567e1beb397e9fd2741a4 |
| Unchanged progress CSV | 595443d0129e7d6ccd1f824b050854d5759c0f45c1af5b0818ef7cde682528ee |

Check all **46 inputs**: three changes, 43 fixed. Effective corruption controls
cover every current input, source text, six physical code/symbol/table/data
sites and every before/after capture. The exact-input inverse rejects unknown
or corrupt artifacts; current image and lifecycle acceptance use no inverse.
All **801 original archive fingerprints** are checked freshly and unchanged.
Progress CSV remains ignored and is not force-added.

Fresh matcher: Game **2,893/4,828 (59.92%)**, total **3,566/5,501 (64.82%)**,
different **1,935**, zero drift. Init stays 492/492 and Debugger 181/181 exact.
Conversions stay total **5,501/6,044 (91.02%), bytes 86.04%**, Game
**4,828/5,323 (90.70%), bytes 85.41%**. The stub was already counted C: this
adds one exact body, not another converted function. README changes only its
two affected aggregate rows; function narratives stay in working docs.

## Banking And Next Work

Bank tools **6ee5fbe** before the consumer pin/source/guards/docs. Shared tools
checks, standalone five-file syntax and all three ROM-free checks pass.
Preserve the independent older-mirror ddbdd16 HEAD and all **633 initial dirty
fingerprints**; copy only five absent owned paths and verify all **638 final
fingerprints**. No mirror commit/reset, push, host source/build/launch,
save/configuration or frozen Release action. Claude calls: zero. Ignored
receipts live under `conker/build/game-packed-record-updater/`.

The full Graphify update refuses 19,326 nodes against 41,105 curated nodes,
retaining 19,398 nodes from 2,972 excluded-but-present files. Preserve the
fail-closed result and await the incremental commit worker; do not force it.
Seven documents / 4,955 relative Markdown links validate with zero broken.

Next recover **func_1516D738**, the still-stubbed **153-word routine** in this
owner. Its older archive screen emits 150 words / 150 real differences.
Re-establish its full retail behavior, arguments and active compiler shape
before adoption. Keep the whole additional-source/binding queue, handwritten
Init hardware routines and func_1510BF60 open; no full-game completion claim.

## Post-Bank Verification

Consumer **26623707** banks the source, three guards, tools 6ee5fbe pin,
README aggregates and working documentation. All **14 post-bank checks pass
in 31.496 seconds**, including the independent complete current image, all 46
input states and fresh hashes for all 801 archive files. The normal ELF /
progress build is up to date. Raw C still has three differences; only the
guarded complete slot/state is claimed retail-exact.

Both active checkouts are clean before this receipt. All 638 final older-mirror
fingerprints, including the 633 initial fingerprints and independent ddbdd16
HEAD, remain fixed. The source commit's incremental graph worker completes at
**41,114 nodes / 81,211 edges / 3,930 communities**, without forcing the refused
smaller full scan. No push or host/Release operation. Continue the whole
additional-C / Game goal at func_1516D738, not a narrower completion claim.
