# Transition Burst Pointer And Flag Lifetime Recovery

Date: 2026-10-17

Continue consumer **bc059cd5**, tools **36eccea**, from
[Note 1486](1486-transition-child-motion-guarded-match-20261017.md) and
[the frame recovery](1485-transition-burst-frame-recovery-and-native-qualification-20261017.md).
**func_150CF800 improves from 91 to 47 raw word differences**, retaining
251 words and frame 0x108. It is **uninstalled**, with no new guards or
matching credit. The wider Game goal remains active.
Retail span: **150CF800..150CFBEC**, ROM **FCCB0..FD09C**, 1,004 bytes.

## Recovered Source Lifetimes

Two ordinary C changes recover the retail pointer/branch lifetime:

1. Form the typed transition view before the state gate and test its state
   byte. This retains one derived pointer across the completion path.
2. Express both outcomes of the first flag decision explicitly. Keep its
   byte-sized value, but use if/else rather than a zero initialization before
   an if. The branch now clears the flag in its own delay slot instead of
   hoisting that clear into an earlier RNG call's delay slot.

The raw routine now has the original **47-word prefix**, parent in **S4**,
payload pointer in **S3**, the transition save/reload at **SP+0x84**, the
first flag's original nine-word region, and the complete **41-word tail**.
There is no compensating extra tail address recomputation. This is actual
emitted instruction evidence, not source-level inference or a register hint.

The complete semantic candidate and immutable input gates live in
`tools/experiments/game_transition_pointer_lifetimes.py`.
Raw target SHA-256:
`d33c00e67089d81062e952c8cc23cf779f48ac15ca2b1fee3f63c06018a2df86`.
All 31 bindings are explicit. The later RNG/factory/copy call relocations
move **716 -> 720, 796 -> 800, 816 -> 820**, respectively, with the recovered
branch; these are real object bindings, not relocation suppression.
Raw and padded target words agree. All **24 raw/padded owner neighbors** and
the six-word retail float pool are unchanged. No compiler/profile changes.

## Remaining Differences

The 47 words are classified and fingerprint-checked, not patched:

- **36** words differ only by a four-byte stack displacement.
- **11** have remaining compiler scratch-register choices. One of these,
  word 192, also has the four-byte stack displacement.
- Descriptor remains **SP+0xB0**, payload **SP+0xA0**, versus retail's
  **SP+0xAC / SP+0x9C**. Saved pointer roles are fixed, but object homes are not.

Do not use arbitrary stack-word replacements, dummy fields or padding to
claim this is exact. The current screen still refuses installation. Independent
rebases, complete private/access-fault qualification and the first complete
image gate remain open, along with the actual remaining words.

## Compiler Evidence And Rejected Trials

Fresh owned CFE/UOPT/UGEN captures reproduce each selected normal candidate
owner's text/function/binding/pool inventory and complete producer/consumer/
driver lifetimes with probe cleanup. The automatic region remains **128 bytes**
in both the 91- and 47-difference forms. The anonymous **R / M-128 / four-byte /
level-1** home remains too; pointer recovery does not remove it.

The captured records show that home used for the float RNG result nested in
the direction helper's argument, then reused for the chained scale assignment.
It is not merely a scale temporary, nor a missing transition-pointer slot.
These are candidate compiler records, not a capture of the unavailable retail C.

Bounded ignored trials under `conker/build/game-transition-pointer-lifetimes/`
separate the contributing effects:

- Pointer gate alone restores roles/reload, but leaves 250 words.
- A shared integer/union RNG-flag/child lifetime reaches 251/0x108 and 65
  differences, but adds an unwanted saved-register move after allocation.
- Separate lexical scopes do not remove the object-home gap.
- Direct scale-field copies or reusing progress for scale do not remove the
  nested argument home. Some produce a one-word scratch/scheduling improvement
  without resolving the underlying object layout; they are not adopted.
- Staging the speed with literal 2.0f strength-reduces the multiply and loses
  the 251-word/frame shape (246 words / frame 0x100). Retaining a named multiplier
  restores the shape but worsens the register layout or literal ordering.
- Reusing the pointer parameter for allocation and deriving the parent again
  produces 255/0x108 or 251/0x100; neither is adopted.

No advisory call is needed for these locally discriminating questions. **Zero
Claude calls this turn**, no provider/account/model/dependency change.

## Fresh Qualification

All **eight tests pass in 61.553s**:

- **2,688 three-way guest cases**, retaining the actual 54-word factory,
  eleven-word SDK copy and both three-word tag leaves. Public bytes, calls,
  clobbers, allocations, callback mutation and live padding modes agree.
  The original naturally visits 249 words; its two BREAK words are unexecuted.
- Native32 **O2/O0 + UBSan**, **1,728 cases per profile**, full C and separate
  typed caller. Four effective count/copy/speed/stale-progress controls exit 22.
  Word gate/slot controls intentionally pass little-endian native checks but
  fail their actual big-endian MIPS guest checks; native-only success is not
  byte-width evidence. The gate control now targets the recovered typed view.
- Both actual compiler captures complete with unchanged candidate inventories.
- **195 protected entries / 179 distinct paths**, **390 positively fired
  live/frozen corruption controls**, plus **251 word / 31 binding controls**.
  Preserve the exact existing child-motion successor normalization; do not
  rewrite old baselines to admit arbitrary new bytes.
- The actual eleven-word kind-12 callback window passes **128 three-way cases**.
- Production source/image/guards/helper remain exactly the committed child-motion
  baseline, with func_150CF800 still a zero-return production placeholder.

The six inherited descriptor bytes remain representation limits outside the
explicit live-padding mode. RNG, direction results, sine and lower allocation
are scripted. This is not private stack, portable C padding, full dispatcher,
real heap, N64 FCSR/CP0, hardware or gameplay acceptance.

Eleven shared padder tests pass in the active checkout (0.055s) and mirror
(six in 0.030s, five in 0.019s); tools-check passes. Two task pairs match
exactly across both tools copies and all four ASCII/AST parses pass.
Broader unchanged suites remain prior receipts, not newly claimed tests.

## Bank And Resume

Tools **e12376f** commits the new recipe and its tests first. Preserve mirror
HEAD **ddbdd16b** and all **1,065 initial dirty-file hashes**; add only the two
task files, yielding **1,067 dirty paths**. No mirror commit, reset or push.
The consumer checkpoint updates only the tools pin and documentation. Main
README aggregates and all production source, ELF, manifests and profiles stay
unchanged. Existing duplicate generated_12D630 recipe warnings remain.

Fresh official matching remains Game **2,951/4,828 (61.12%)**, total
**3,624/5,501 (65.88%)**, **1,877** different, zero drift. Init **492/492**
and Debugger **181/181** remain exact. Normal ELF SHA-256 remains
`c8b6937388a52c546239100bfbef8ef676ba5d8cdf9f08e9cf8c94638d1d00f5`.

- [x] Recover the pointer gate, S4/S3 roles, first flag branch and exact tail.
- [x] Qualify bounded public/native/caller behavior and immutable compiler/input evidence.
- [x] Recover the real aggregate homes while retaining the multiplier and helper ABI in [Note 1488](1488-transition-burst-real-object-layout-and-guarded-match-20261017.md).
- [x] Close the scratch normalization and private/rebase/fault/image gates in that guard-assisted installation; raw compiler output still differs at eleven scratch words.
- [ ] Continue wider Game matching and deferred renderer/gameplay work. No host/frozen Release action.

Prepared-checkout commands:

```sh
python3 -m tools.experiments.game_transition_pointer_lifetimes
python3 -m unittest tools.tests.test_game_transition_pointer_lifetimes -v
make tools-check
make -C conker match-progress NON_MATCHING=1
```
