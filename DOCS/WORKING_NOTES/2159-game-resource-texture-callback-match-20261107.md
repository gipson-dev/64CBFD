# Resource texture callback recovered and byte matched

Date: 2026-11-07. Continues [Note 2158](2158-game-view-resource-draw-match-20261107.md)
from consumer `1f0b791ba3fe428e44c9bc61165df26ccb1c37a5` and tools
`e704b82a895497bc8cc50c45f60e89d21b4bca28`. One qualified Game function
advances the active 80% total goal.

## Recovered texture-coordinate calculation

`s32 func_1513BBFC(u8 *resource, s16 view)` in
`conker/src/game_168A90.c` replaces the zero-return stub. Its complete
**173 words / 692 bytes** match at VA 0x1513BBFC..0x1513BEB0,
ROM 0x1690AC..0x169360. The 88-byte frame preserves S0/S1/S2/RA and
six floating-point pairs F20/F22/F24/F26/F28/F30.

The callback sets up the resource's current matrix through `func_1513B968`,
then captures its payload at resource + live word 0x50 + 0xF8. Two sine
calls use payload angles 3 and 4. Four retained float coefficients produce
the S/T scales. `func_15144B34(view)` supplies the viewer position.
Scroll values 0 and 1 wrap by subtracting the truncated quotient times
1024, retaining the original single-precision operation order.

Nine retained center vectors at `D_800A49C0` pair with first/count records
at `D_800A4A2C`. Their counts cover **140 vertices**: 12 in the first group,
then 16 in each remaining group. The range endpoint is the adjacent scalar
`D_800A4A74`; the native layout check preserves this exact retained adjacency.
For each center, the viewer's horizontal displacement determines a
normalized perpendicular direction. Coincident horizontal positions use
direction (1,0). Each vertex receives:

* S: truncated `((x-centerX)*directionX + (z-centerZ)*directionZ)*scaleS - wrappedS`.
* T: truncated `(y-centerY)*scaleT - wrappedT`.

Stores retain the low 16 bits at SDK Vtx offsets 8 and 10. The callback
reloads the page byte and resource buffer pointer for every vertex, and
reloads first/count after both stores. Center values also remain live.
Return 1 after all nine groups. These reloads matter when output storage
aliases a later input.

The matrix helper's unused second parameter is declared s16 instead of s32
to recover the caller's signed-16 conversion pair. All 16 helper words
remain literal; this qualifies the call shape without claiming a recovered
historical source spelling. No other helper body changes.

## Compiler schedule and guarded normalization

The selected semantic C emits **172 raw words**, frame 88, under the
unchanged ordinary O2/g3 MIPS2/O32 profile. Raw target SHA-256:
`75c81591344e54fef5db0b2a1160f94915655357b6559d7a4a5bf450c526294a`.
An explicit derivation produces the full 173-word retail sequence, with
**60 exact expected-word/relocation guards** and **20 bindings**.

The derivation folds one redundant address ADDIU into a scalar load's
signed LO16 displacement, reorders independent setup and comparisons,
commutes integer additions, and closes one T4/T5 allocation pair. Existing
raw NOPs 103 and 155 move to the required slots. The first-index and page
loads are copied into specific branch-delay paths, with their join/likely
branch adjusted accordingly. Every remaining source instruction identity
is retained once; there are two explicit static path copies and one folded
address word. No synthetic alignment NOP supplies missing semantics.

**All floating-point operation words remain literal.** There are no FP
arithmetic or FP-register replacements. The raw C body is qualified against
the independent public memory/call/result model. Only the normalized body
claims complete private machine-state agreement with retail; raw private
PC, FCSR and fault identity are not claimed.

Original word 105 is a literal unreachable MTC1 between an unconditional
branch and the zero-vector label. All 173 words compare; **172 reachable
words** execute. The unreachable instruction remains exact.

Raw IDO register metadata changes its FPR allocation mask from 1 to
0xFFFFFFFF, matching the decoded even/odd O32 allocation pairs. The mirrored
24-byte `.options` record must agree exactly, with header and geometry fixed.
Other metadata fields and allocatable pools remain unchanged. Both padded
owners retain literal zero register masks. Corruptions of either raw record
are rejected; no metadata exclusion is introduced.

## Caller, helper and semantic qualification

The complete aligned retained-input census finds no direct target JAL,
one entry pointer at ROM 0x22E6FC / VA 0x80089C3C, and no interior pointers.
This is slot 5 of `D_80089C28`, used by the renderer restored in Note 2158.
Its resource/view ABI agrees with the recovered callback.

Seven checks pass both before and after installation in both tools copies:

* **85 guest cases per body**, across retail, normalized C and raw C,
  use an independent float32 vertex model. Cover all nine groups, negative
  and signed-zero scroll, truncation around 1024, signed positions, low-16
  output, and live page/buffer/range/center aliases. Signed views and sparse
  wrapped addresses are guest-only. Normalized/retail private memory,
  GPR/FPR/HI/LO, PC and access traces agree.
* **36 connected cases per body** execute all 16 original matrix-helper
  words and all 13 original viewer-getter words. Both helpers already match
  in production. The viewer helper dereferences the pointer at D_800DBFF0,
  using stride 0x9A0 and position offset 0x2F8. Matrix service and sine
  implementations remain bounded providers.
* **12 connected renderer cases per body** run the complete retained
  75-word renderer through callback slot 5, texture stores and three graphics
  commands. This path executes 64 renderer words; its other paths were
  qualified separately in Note 2158.
* **774 fired access cuts**, including 33 delay-slot cuts, compare the
  full normalized/retail private state and access prefix. All six saved FP
  pairs and S0/S1/S2 survive. This is emitted guest ordering evidence,
  not hardware exception or portable C fault equivalence.
* Native32 O0/O2/O3 each pass **68 independently modeled finite fixtures**,
  with SDK Vtx16/ST8/range8/pointer32 assertions, fixed disjoint banks,
  retained data adjacency, explicit single-precision SSE square root,
  controlled sine responses and UBSan traps. All 12 compiled negatives
  fail with exit 1: stub, omitted matrix, wrong angle/scale/zero axis/wrap/
  view, payload reload, wrong page/direction, missing last group and wrong
  result. Aliases, sparse indices, private homes and invalid conversions
  remain guest-only.
* Two independent GNU links verify all 20 bindings, including signed LO16
  carry in the coupled nine-group data and the folded scalar load. Altered
  source/bindings/register metadata and six full-image corruptions reject.

Nonfinite guest conversion fixtures use an explicit bounded invalid-word
convention. The oracle is not a FCSR emulator. These cases do not establish
hardware exception behavior, portable invalid-conversion semantics, actual
sine implementation accuracy, visual graphics output or gameplay acceptance.

## Complete owner, linked image and production gates

All **149 frozen inputs** remain accounted for. All 12 raw and padded
neighbor functions are literal, including the matrix helper; four inherited
compiler diagnostics remain identical and no warning is added. Source,
compiler/SDK, retail data and assembly, bindings, layout, guards, prior ELF,
protected registries and graph are pinned. New modules and imported helpers
have separate exact fingerprints.

Actual Make recompiles only `game_168A90.c` and equals the independent
full-image prediction: **590 changed bytes, zero exclusions**. The changes
are 533 Game bytes, 27 symbol-table bytes and 30 string-table bytes. Two
closed adjacent serialization swaps account for the metadata:
`func_15128774`/`D_80087434` at file offset 2752124, and
`D_800A4A2C`/`D_800A7668` at 2818140. Their predecessor slots, complete name
blocks and permutations are pinned. All value/type/section fields stay with
their names; the full named-definition multiset changes only this target's
extent from 12 to 692. The strict predictor excludes no bytes or sections.

All **6,052 addresses** and other bodies stay fixed. All **189,088 protected
Game bytes across 720 owners** remain exact. The conversion CSV and Makefile
are unchanged; exactly 60 guard rows append to the retained history. Compile
and link succeed. The whole-ROM checksum still returns its expected
nonmatching exit 2, with the inherited duplicate generated_12D630 recipe warning.

Both tools copies run fresh shared smoke checks. Three unchanged shared
regression receipts per copy are reused only after exact helper/test hashes.
The sibling receives a disposable new-module overlay and an explicitly
fingerprinted read-only alloc_pools fallback. Its 2,434 inherited dirty paths
are preserved. Claude calls: zero.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,229 / 5,512 | 76.72% | 0 | 1283 |
| Game | 3,556 / 4,839 | 73.49% | 0 | 1283 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**181 more exact functions** remain to 4,410/80%. The root README receives
only aggregate rows. Four new index leads preserve all historical text.
Refresh Graphify on the changed paths, retaining existing excluded legacy
nodes fail-closed; this is not a fresh full-corpus extraction. Commit tools
before consumer source/docs/pin, then verify the fresh hook, clean trees and
unchanged production artifacts.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `808da67ff39fe632686aed746fcbe9c899300e9b0d6d2fc468cf79d446e9b7a4` |
| Production binary | `f10ceb594e9d9de10746e7ba38593c43a51965c3b14c98174b0d4c3e2ba875f3` |
| Padded owner | `99aafa779ddf1826ea26c507e9f39e50df1e707c3d8c345c708167ca40824bab` |
| Guard manifest | `dab5f202cc6484dffce6e625382d0a56b9d819d15dfe564dc3b857cab8d78336` |

Ignored receipts remain under
`conker/build/game-resource-texture-callback-1513BBFC-match/`; source screens
and the independent schedule derivation remain in its sibling private directory.

Next: inspect **func_1513BEB0**, the adjacent unfinished callback, including
its complete retail window and actual callers before recovering its C body.
Keep the 80% goal active. Other private candidates remain uncredited. Preserve
the frozen handwritten/hidden-ABI boundaries, unrelated work, private inputs,
saves and host Release checkpoint.
