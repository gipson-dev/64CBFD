# Game Record Ring Renderer Frame Fitting

Date: 2026-10-08

## Result

Continue the same complete `func_151D80C4` target from
[Note 1139](1139-game-record-ring-renderer-recovery-20261008.md), using the
[focused workflow](../AGENT_WORKFLOW.md). VA 0x151D80C4..0x151D8718,
ROM 0x205574..0x205BC8: **405 words / 1,620 bytes / retail frame 0xD0**.
Keep the [original assembly](../../conker/asm/nonmatchings/generated_204660/func_151D80C4.s)
and [complete owner slice](../../conker/asm/204660.s).

The fitted complete C now emits **405 words, frame 0xD0 and 198 raw word
differences**, down from the natural recovery's frame 0xE0 and 319 differences.
Its escaped cursor, sync byte, captured buffer, both XYZ blocks, saved GP/FP
slots, loop start and memcpy call offset match retail. This is genuine fitting
progress, **not a byte match or installed conversion**. Do not normalize the
remaining 198 words as a broad batch.

Fresh **21 tests pass in 148.226s**, without skips: nine original recovery
tests plus twelve fitted-body tests. The entire production ELF, source,
assembly, Makefile, progress and **11,275 guards** remain unchanged. No new
guard or production source edit. The installed target remains retained,
byte-exact assembly; no conversion credit or root README change.

Converted totals stay **5,481 / Game 4,808**; exact **3,392 / Game 2,719**,
zero drift and 2,089 different. The last installed conversion remains
[Note 1138](1138-game-record-ring-shaping-conversion-20261008.md).

## Source And Layout Findings

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_ring_renderer_candidates.py)
retains the fourteen original forms and adds **37 complete fitting forms**.
Use `FITTED_NAME = retail-local-order-wide-scaled-factor`, not the older
natural `SELECTED`, as the next fitting baseline. No dead locals, inserted
instructions, raw instruction bodies or smaller substitute targets.

The useful changes are a byte opacity factor, factored 28-byte addressing,
meaningful local declaration order and a signed integer seed-alpha lifetime.
The factor expression `(signedOpacity * 3) * 4` is narrowed by its `u8`
assignment, preserving retail's low byte. Signed opacity's full halfword
domain cannot overflow that intermediate. Keep the retail 255*255 -> 254
alpha result and captured factor across memcpy.

| Complete O2/g3 Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Original natural recovery | 405 | 0xE0 | 319 |
| Factored stride, byte alpha locals | 403 | 0xD0 | 319 |
| Byte factor | 405 | 0xD0 | 251 |
| Byte factor, retail private-local order | 405 | 0xD0 | 224 |
| Private-local order, signed seed alpha | 405 | 0xD0 | 215 |
| Private-local order, reversed factor branch | 405 | 0xD0 | 211 |
| Signed seed alpha, factored opacity multiplication | 405 | 0xD0 | 198 |

| Fitted Body Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 405 | 0xD0 | 198 |
| O2 | 405 | 0xD0 | 275 |
| O1/g3 or O1 | 490 | 0x90 | 486 |

Verified emitted layout: cursor SP+0x8C, sync SP+0xA7, captured ring
buffer SP+0xA8, previous XYZ SP+0xB4 and current XYZ SP+0xC0. S0..S7
save at SP+0x48..0x64, GP FP at +0x68, RA at +0x6C; F20/F22 at
+0x38/+0x40. The loop begins at +0x3E4 and memcpy is at +0x56C.
Call-clobbering tests preserve these saved lifetimes and factor in GP FP.

Remaining measured differences include output/index in S3/S2 instead of
retail S2/S3, seed alpha/phase in A2/A0 instead of A0/A2, width-array index
in A0 instead of V3, temporary-register choices, stride temporary reuse,
and hoisted default-factor initialization. Saving the same register set
does not mean all register roles or the instruction schedule match.
Original declaration/type recovery is still open.

## Fresh Qualification

The [renderer suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_ring_renderer_recovery.py)
now parameterizes the existing complete-body tests, preserving the original
natural recovery's assertions and independently exercising the fitted body:

- **988 guest cases for each body** compare complete public memory, return
  cursor, ordered output stores, callback arguments and saved GP/FP lifetime
  against retail and an independent pair/command reference. Fitted/retail
  ordinary coverage reaches 392/392 words, not all 405 instructions.
- **512 current/count cases plus three lazy layouts for each body** cover
  all byte values, mapped negative/count-zero records, inactive pointer
  laziness and null-allocation record-read laziness.
- **1,086 native32 cases for each body** use an independent offset reference,
  volatile typed call and all 65,536 arena bytes. Cover state/current/count,
  flag patterns, opacity limits, views and eleven mutations plus baseline.
  Invalid float-to-integer casts and native alias layouts remain excluded.
- **22 missing-byte gates / 44 executions for each body** fail closed at
  required reads/stores, including five next-record reads after the final
  segment. Equal raw/retail fault prefixes and portable C fault semantics
  are still unqualified; do not upgrade a fail-closed gate to that claim.
- The fourteen original and **37 fitting forms** each pass a complete
  ordinary captured-buffer-mutation fixture. Four profiles for each chosen
  body pass ordinary memory/callback/result checks. These are not deep
  domain sweeps for every alternative. Eight compiled negative witnesses
  remain effective for each chosen body; assert each mutation changes C.
- **256 connected cases / 512 executions for each body** run the complete
  original 52-word `func_15147C4C` and actual 52-word `func_151D5D60`.
  Render-table callback 16, signed-view forwarding, nine transform arguments,
  allocation gates and both framebuffer halves qualify. All backend and
  47/52 caller words execute; alternate dispatch/release branches stay open.
- **64 guest alias cases / 128 executions** compare the fitted and retail
  bodies with the independent reference across vertex/record/owner storage
  and Gfx/record/payload/vertex overlaps, two SP phases and final lookahead.
  These bounded terminating layouts do not validate arbitrary invalid aliases.
- **Four independent symbol sets / 768 executions** GNU-link the complete
  original assembly and fitted IDO object separately. Verify all sixteen
  relocation type/symbol uses, canonical bytes, HI16 carry/LO16 sign and
  JAL regions, full memory/calls/results/store order under six mutation modes.
  No retail-word substitution or guard normalization participates.
- Both copied-owner comparisons preserve **22 neighbors**, relative
  relocations, normalized pools and all four existing diagnostics. Isolated
  and copied target bytes agree. The real padder accepts the full 1,620-byte
  fitted body without slot padding or new guards; this is not match proof.
- Fresh complete ELF SHA-256 remains
  `f240ca73721dfd7a24c0a85fd5697d45ea1ebc724a11ebd76d965e6b3cd86e99`.
  Preserve all **6,058 linked bodies/addresses/extents** and protected data,
  plus the recorded source/assembly/Makefile/progress/guard fingerprints.

Two initial new-test fixture failures are corrected: exclude incoming A2's
home store from the GP-save map, and map all four width-array entries so
view-three plus a view-zero width mutation has backing memory. Neither
failure was a production-code defect. Re-run the full 21-test suite afterward.

Shared checks pass **14 matcher/padder/repository-setup tests in 0.538s**,
both tools project checks and CLI help. No shared production helper changes.
Previous unrelated neighbor-suite receipts remain historical, not fresh runs.
Both reviewed files pass syntax/mirror checks. Scoped documentation checks
pass **126 documents / 4,081 relative links / zero broken links**. Remote
publication is not verified or authorized by local checks.

Graphics setup, deep allocation and memcpy remain bounded hooks. The linked
dispatcher and combiner are still zero-return placeholders; executing their
original interface does not restore them. No emulator, hardware FCSR/traps,
gameplay, host integration or OGL/Release change.

## Banking And Workflow

Entry parent `b565e7024b292b8fe6bd4a441adaabfe5b4f7108`, mounted tools
`a22175b6c672a0275fa1a6ac6f77b2df3ba4a17a`: clean. Per **"Keep commited"**,
bank tools first at **`9d466ca8891f3e1f452791db1be342ecdee74337`**, then parent
documentation and that exact gitlink. No push.

The older standalone tools HEAD remains
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`. Mirror only the two reviewed
renderer files after checking their exact previous fingerprints. Its full
pre-existing dirty status is unchanged; no reset/stash or duplicate commit.
Ignored receipts stay under `conker/build/game-record-ring-renderer/` and
`conker/build/game-record-ring-renderer-test/fitted/`; no ROM/artifact tracked.

Graph query precedes investigation. Fresh `graphify update .` exits one,
refusing 16,830 nodes over the retained 38,619-node graph. Preserve 19,398
nodes from 2,972 still-existing excluded files. No force, upgrade, changed
ignore policy or graph-repair claim. One Codex writer, zero Claude calls.

## Resume This Target

1. Start from **FITTED**, its complete 405-word/frame0xD0 source and the
   qualified private layout. Do not repeat the natural frame investigation.
2. Fit output/index, seed alpha/phase, width index, temporary allocation and
   default-factor schedule. Use `--fit --form` for a discriminating full-body
   experiment. Do not install a broad 198-word normalization batch.
3. Qualify any proposed closed register/schedule transformation, private
   state and raw/retail fault prefixes; retain independent rebases, aliases,
   caller/backend and native32 evidence for the revised complete body.
4. Only then install/rebuild/audit all bodies/data/guards/progress, refresh
   README aggregates, and bank tools before the exact consumer pin. The
   wider Game goal, actual linked setup chain and hardware/gameplay stay open.

```sh
python3 -m tools.experiments.game_record_ring_renderer_candidates --fit
python3 -m tools.experiments.game_record_ring_renderer_candidates --fit --form retail-local-order-wide-scaled-factor --profiles
python3 -m unittest tools.tests.test_game_record_ring_renderer_recovery -v
```
