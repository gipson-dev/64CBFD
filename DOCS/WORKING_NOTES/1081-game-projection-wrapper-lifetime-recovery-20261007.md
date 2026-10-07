# Game Projection Wrapper Lifetime Recovery

Date: 2026-10-07. Baseline: `44ef1423`,
[Note 1080](1080-game-secondary-halfword-output-direct-match-20261007.md).
Continue `func_15144CEC` from the
[earlier ABI/frame audit](1036-game-projection-wrapper-abi-and-frame-audit-20261006.md).
Production remains the explicit zero-return placeholder. No source, shared
header, compiler profile, padder or retail-word guard is installed or changed.

## Recovered Contract

Retail: 101 words / 404 bytes, frame0x48, VA `15144CEC..15144E80`,
ROM `17219C..172330`. Six argument positions:

```c
s32 func_15144CEC(struct17 *point, f32 *xy, f32 *optionalZ,
    f32 *optionalW, f32 *optionalReciprocal, u8 viewIndex);
```

The point supplies three float words at offsets0/4/8. Missing Z, W and
reciprocal outputs use entry-SP-4/-8/-12, respectively. Saved s0 owns the XY
pointer through the complete wrapper; saved ra and the original0x48 frame
are retained by the selected experimental body.

The low unsigned byte of incoming index selects a64-byte matrix in
`D_800D9D10`. The eight-position helper call carries matrix, three float words
in integer argument registers, XY/XY+4, Z and W. Execute the original helper
chain, not an ordinary replacement XYZ call:

- `func_150A7960`:40 matrix-leaf words.
- `func_150A7A00`:5 trampoline words, saves caller ra in t9 and supplies a
  synthetic return into `func_150A7A14`.
- `func_150A7A14`:13 continuation words, consumes live a0/f0/f2/f4 and t9.

XYZ inputs and relevant XYZ coefficients are captured before their stores.
W coefficients are read after those three stores. Outputs overlapping the
fourth column can therefore change W. The tested matrix overlap changes
seeded W=2 to actual W=6; the wrapper must consume6.

After the helper, cache W once from its reloaded pointer home. Reject if
`D_800A56B0 <= W`; only otherwise read `D_800D9B20` and reject `W <= lower`.
Then reject zero. The upper retail constant is6000.0f; lower is a live BSS
float, not a ROM constant. Rejection preserves the helper's output stores.

Acceptance stores reciprocal1/W and rereads the unsigned index home. View
stride is explicitly0x180, not `sizeof(struct140)`; the legacy complete type
does not have that asserted size. Read the current pointer word
`D_800BE628`, then scales at0xC/0x10 and offsets at0x34/0x38.
Capture the Y product before storing X. X uses the live reciprocal. After X,
reread both reciprocal and view-base word before finishing Y.

## Compiler Evidence

[Maintained driver](../../tools/experiments/game_projection_lifetime_candidates.py)
retains140 lifetime forms:32 local-elimination/register-hint,36 depth-reuse/
index/control-shape,48 partial-zero/temp,16 reuse-partial and8 comma-placement
controls. All140 were compiled under the retail O2/g3 profile with actual
SDK/structure headers, zero diagnostics. None is byte-exact.
Frame counts:80 at0x48,56 at0x50 and4 at0x58. The only two101-word forms
have frame0x50; no screened form combines101 words with the original0x48 frame.

The previous101-word seed had frame0x50 and85 aligned differences. The selected
faithful recovery reuses the cached-depth local for the Y product, reloads the
index home through a volatile byte parameter and retains the separate zero
return block. It has102 words, frame0x48 and46 aligned differences.
Its null-output call vectors retain the original three private addresses.

The accepted path has an extra pipeline NOP at offset0x158; the epilogue begins
at0x184 instead of0x180. Register allocation and other scheduling/operand
differences also remain. This is not a claim that removing one NOP alone
would produce a match. No oversized body or broad instruction normalization
is installed. Candidate pointer-view declarations are local experiments only;
the production legacy pointer-word declaration is unchanged.

Some screen controls deliberately lose alias-sensitive behavior. The tempting
inline-Y control is102 words/frame0x48 with44 aligned differences, but fails:
with XY at view+0x10, retail and selected return Y=26.5, while inline-Y returns
Y=2.5 because X overwrites the Y scale before the late read. A lower word-diff
score is not qualification.

## Qualification

[Ten tests](../../tools/tests/test_game_projection_lifetime_recovery.py):

- 36864 paired guest cases: all256 low-byte indices with poisoned high words,
  eight optional-output masks, nine output/input/view/matrix alias layouts and
  two stack phases. Retail and selected agree with an independent float/output
  reference on complete mapped external memory, ordered external writes,
  eight-argument helper vectors, return status and preserved register state.
- 384 depth/bound/mask/phase fixtures cover accepted, near/far rejection and
  zero-seeded paths. Rejected views are unmapped; upper rejection also leaves
  the lower bound unmapped. All58 helper words and100 reachable wrapper words
  execute. The remaining duplicate MTC1 at0xD8 is dead and structurally pinned.
- 512 helper-boundary index-home probes distinguish the original matrix index
  from the post-helper view index. Eight view-pointer overlap probes and a
  reciprocal/XY overlap prove the live post-X reload dependencies.
- 24 missing-required-field probes fail closed for point/matrix coefficients,
  bounds, view pointer/scales/offsets, XY stores and reciprocal output.
- 92160 actual freestanding32-bit native C calls cover256 indices, eight null
  masks, nine aliases and five depth paths. Pointer/view sizes are asserted;
  all136 words of the bounded point/XY/output/matrix/view footprint, helper
  arguments and statuses agree with a separate reference. Private fallback
  pointer identities are not compared between separate native calls.
- Three compiled behavioral negatives detect late Y-scale capture, cached
  post-X reciprocal and cached post-X view base. These fail actual final
  output values, not just compiler word comparisons.

The guest helper executes all58 original words; native helper arithmetic is
a bounded C model of the same XYZ-store/late-W contract. Helper-boundary home/
pointer mutations are seeded probes, not claims that this helper writes those
homes naturally. Full raw read ordering differs between the selected and
retail accepted-path schedules. Qualification covers finite single-precision
values, observable writes and live-read dependencies, not identical independent
read schedules, FCSR/exceptions, NaN payloads, hardware execution, complete
callers, gameplay or host-port adoption.

Focused recovery/earlier-audit/matrix-helper regression:26 tests pass in211.955
seconds (runner elapsed), zero skips/errors/failures. This is the ten new tests,
three original projection-audit tests and thirteen existing triangle-transform/
matrix-tail tests. The earlier production164-test result is not claimed as a
new full-suite run for this tools-only checkpoint.

## Production Boundary

The retained US ELF is re-audited against Note1080's post-link receipt:
all6059 slots/addresses/extents/bytes unchanged, all protected .init/.init_data/
.debugger/.game_data sections unchanged, all10916 historical guards unchanged.
All720 Game-data owners/189088 bytes remain exact. No production rebuild is
needed for this tools/tests/docs-only recovery.

Matching remains total3352/5465 (61.34%), Game2679/4792 (55.91%),2113 different,
zero address drift. Conversion remains5465/6042, Game4792/5321. Root README
aggregate rows stay unchanged; function details belong here and in the update
log. No sibling/OGL/editor/frozen Release/save/runtime changes or push.
Project-tool smoke checks, Python syntax and whitespace checks pass.
Documentation gate:63 files/3714 relative links, zero broken.

## Resume

1. Reduce the qualified102-word/frame0x48 body to101 without moving Y capture
   after the X store, caching post-X reciprocal/view base, widening index,
   or replacing the real helper's synthetic-return continuation.
2. Resolve the remaining46 aligned word differences with evidence of the
   original schedule, registers and floating lifetimes. Check exact body
   length independently of zero alignment padding.
3. Only after a fitting qualified body exists, run copied-owner/relocation/
   guard/alternate-carry checks, install narrowly, rebuild and audit every
   slot/data owner/historical guard. Then run full production regressions
   and update aggregate matching counts.

Broader matching goal remains active. Sampler `func_151432BC` exit/circle-byte
scheduling and oriented `func_15142600`'s27 private-layout differences remain
open. Ignored receipts: `conker/build/game-projection-lifetime/` and
`conker/build/game-projection-lifetime-test/`. The latter holds the unchanged
production audit and focused regression runner/receipts.
