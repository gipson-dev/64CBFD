# Weighted Target Selection Complete Match

Verified: 2026-10-19. **func_1508B9BC is installed and all 153 linked words
are byte-exact**, with its original 96-byte frame and 612-byte slot.
VA1508B9BC..1508BC20, ROM B8E6C..B90D0, generated_B3020.
Consumer predecessor 0aa5df0b; tools predecessor 3457d8d. Bank tools
**c939d75** before the consumer source/guards/docs/pin commit. No push.

This is a **guarded match**, not direct compiler identity. The complete C
emits 151 words/frame64 with 36 differences. The production padder applies
151 expected-word/relocation guards and inserts two justified words, retaining
every source instruction and all 16 bindings. There are no new literal pools,
Makefile changes, dummy effects, volatile declarations or physical-register C
bindings. The original assembly stays preserved.

## Recovered Behavior

1. Capture signed count/current index and the initial active, neighbor,
   distance and current-target table bases before either helper call.
2. Call func_1508C5B8(0, pairBudget), with budget1 for count<9 and budget4
   otherwise; then call func_1508A1BC. Both calls occur even for nonpositive
   count, and both results are ignored.
3. Use the post-helper context for the current player's byte-weight row.
   Retain the initial count, current index and table bases, but read their
   current contents after the helpers. Positive count captures the two
   coefficients only after both calls.
4. Scan positive active rows other than the current player. Search at most
   16 neighbor entries, stopping at -1. A current-player match supplies the
   signed distance score; a supplied score -1 is also excluded.
5. Convert the weight byte as unsigned32 to float, multiply by the original
   1/255 coefficient and, for the cached current target, the 0.8 coefficient.
   Convert the signed score to float32, multiply and truncate back to signed32.
   Update only on strict improvement from the initial 10,000,000 sentinel,
   preserving the first exact tie.
6. Always publish the selected index at post-helper context + current*4+49C.
   If selected, publish truncated X/Z Euclidean distance; otherwise publish
   the best sentinel. The distance store reloads the global context after
   target publication, which matters for a backed publication/global alias.
   Return0 on both paths.

The other-source snapshot was a cross-check, not a byte-exact import: its
weight and coordinate casts lose the original byte/float/word distinctions.
Keep meaningful local names and the address-based exported name; no original
source identifiers or unproved record types are invented.

### Helper Boundary

The actual preparation helper saves full-word A0/A1 at its incoming homes,
uses A0 as the returned-mask slot, and decrements A1 as a pair-processing
budget. This establishes the call's two-word interface and improves the local
name from the initial misleading "step". Its full 261-word body, and the
336-word second helper, remain unfinished.

An explicit two-parameter definition of the existing zero-return placeholder
introduced two debug argument-home stores, growing that neighbor from12 to20
bytes. A generic register-parameter hint did not remove them. Both variants
were rejected by the whole-owner gate and removed. Leave the existing
unprototyped declaration/body untouched until the helper is recovered; do not
add guards or a profile override to disguise a neighboring placeholder change.
The native providers use the verified typed interface.

The broad build that included the rejected experiment completed, but its audit
correctly failed. After restoring the helper, a fresh owner rebuild/audit
reproduces the complete predicted image with every neighbor unchanged. Do not
reuse the intermediate failed build as an accepted checkpoint.

## Layout Proof

Removing the artificial named context local and explicitly caching the
post-helper coefficients recovers the retail GP roles. The final recipe
normalizes only:

- Frame64->96 and the three paired active/neighbor/distance spill homes,
  each four bytes lower within the recovered frame. Saved GP slots and the
  current-index spill home stay fixed.
- The closed F2/F12 coefficient colors, only at their two loads and two
  scalar-multiply uses. Subsequent coordinate/math FP fields remain unchanged.
- Independent budget/loop setup, actor-address and multiply setup scheduling.
- One MFC1 delay NOP and one extra result-zero word on mutually exclusive
  return edges. The former common zero remains the fallback edge's result;
  the selected edge gets its own delay-slot zero and branches to the epilogue.

All 151 source origins occur exactly once. Branch targets and all 16 bindings
are moved through the explicit origin map, never replaced by copied ROM code.
The actual padder and expanded seven-command Make path reproduce the same
qualified object, functions, bindings and pools.

A frame-only control still returns the correct public result but fails the
private-home gate at fired access8: retail writes STACK-48, the incomplete
edit writes STACK-44. The complete recipe passes the tested private states
and access prefixes. The original source's private frame remains different;
no raw/compiler-private identity is claimed.

Raw SHA256:

```text
d3dee48af9b6d8b7ffdcab9c72a13cbe98e5de4cb76b90bbe3a1a5c31cf01ccb
```

Normalized, unrelocated SHA256:

```text
a521bc0baa55a1a9a66a4a75a516a1bb598870415084ad4f03ca425bca75b306
```

## Fresh Qualification

**Eight installed tests pass in 36.885 seconds**, without skips:

- 107 fixtures/two phases give 214 retail/normalized/raw triples against an
  independent reference. Check complete public buffers, ordered helper ABI
  and stores, and the zero result. Retail/normalized also agree on all modeled
  GP/FP/LO/condition state, private bytes and ordered events.
- 1,060 fired access-cut pairs across ten edge/mutation profiles and two
  phases agree at the requested address/width and all modeled state. Providers
  deliberately overwrite the legal O32 argument area and clobber volatile
  GP/FP registers. Cuts exclude opaque provider internals.
- Native32 O0, O2 and O2+UBSan each pass all107 full-buffer fixtures. Eight
  effective negatives cover ties, signed versus unsigned weight, budget
  boundary, cached count/current/active/neighbor bases and sentinel handling.
  Every negative exits through a behavioral failure code, not a compile error
  or signal.
- A completed backed guest alias lets target0 overwrite D_800D23B0, then
  writes distance1500 through the freshly loaded zero context. An effective
  stale-context instruction control fails. This is not a native null-pointer
  or hardware-exception claim.
- 27 runs use the actual no-argument caller window at ROM CB5DC /VA1509E12C,
  inside func_1509DFC4. Retain JAL/NOP, branch/RA delay load and the original
  S0/SP/JR/NOP epilogue, with its72-byte caller frame as an explicit live-in.
  The aligned ROM JAL scan finds this single site. The upstream switch and
  actual preparation-helper bodies are not claimed as executed.
- Three independent GNU maps include HI/LO carry boundaries and rebase code,
  globals, contexts, actors and both providers. All normalized bytes agree
  with independently assembled retail;30 executed raw/normalized pairs agree.
- Mutating each151 raw source words or each16 bindings is rejected. The real
  padder rejects stale expected words/relocations; four strict whole-image
  corruptions are rejected. Canonical symbols differ only in target size.
- Both complete-owner profiles preserve72 other routines and pools, with empty
  target diagnostics. All73 owner addresses are fixed. The production audit
  preserves every other linked body and protected Game data.

Ordinary fixtures visit149/153 retail words. The four unsigned-correction
words behind the LBU-derived nonnegative branch remain preserved, not claimed
as freshly executed. Tests cover bounded valid rows/finite conversions, not
all native out-of-range indices, arbitrary FCSR modes, full helper semantics
or full gameplay. No Claude call, REA setup, dependency change or host work
was needed. Shared tools checks and both mirror syntax checks pass.

## Complete Image And Bank

The exact production image has546 changed bytes:467 target-code bytes,
two target-size bytes,35 symtab and42 strtab serialization bytes.
Eight named definitions in three bounded runs account for the symbol ordering;
canonical symbols remain identical except target size12->612. The initial
unpredicted-serialization failure remains archived, and no blanket metadata
exclusion was added.

All6,056 other bodies and every address are unchanged. The protected189,088
Game-data bytes from720 owners remain exact with zero differences. The
pre-existing guard CSV prefix, assembly, Makefile and conversion counts stay
fixed.

Installed owner SHA256:

```text
05899c7b26d31e5c0ff2cc13709a7df9055b65eab28f6abdaeb8a400dce122a2
```

Installed guard CSV SHA256:

```text
705662100309d5c1aae4b0ad71bbebc411ae6a4b2044314b4f0d576dd3129181
```

Production ELF SHA256:

```text
f56b8cca096731899df5ddecd2fcd8060cf57f53ac03508ab093929f7e14ee4d
```

The predecessor owner's SHA in Note1595 had a one-character transcription
error. Its corrected64-character value was verified against the live file and
the unchanged committed Git blob before this work; no predecessor code or
qualification gate was weakened.

Fresh matching: **Game3,008/4,832 (62.25%)**, **total3,681/5,505 (66.87%)**,
**1,824 different/zero drift**. Init492/492 and Debugger181/181 remain exact.
Owner **60/73 exact,13 remaining**. Root README changes only its two matching
aggregate rows; narrative updates stay in these docs.

Five new task files are mirrored identically. Preserve all1,369 pre-existing
standalone mirror hashes and its older HEAD, without committing that checkout.
Commit tools first, then the consumer pin/source/guards/docs. No push, real
save changes, host-port changes or frozen Release operations.

## Resume

Next: **func_1508BF14**,160 words/frame176,157 real differences,
VA1508BF14..1508C194, ROM B93C4..B9644. Freeze this new baseline and inspect
its actual caller, helper/cache boundaries, bounds and stores before source
recovery and qualification. The helper pair used above remains separate
unfinished work; do not infer its completion from the exact caller.

Commands from64CBFD under WSL:

```sh
python3 -m unittest tools.tests.test_game_weighted_target_selection_match -v
python3 -m tools.experiments.game_weighted_target_selection_integration --audit
python3 -m tools.match_progress conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
make tools-check
```

Ignored sources, objects, native fixtures, strict first-link diagnosis,
production build/audit, image accounting and remaining-owner inventory live
under `conker/build/game-weighted-target-selection/`.
The broader Game decomp/matching goal remains active.
