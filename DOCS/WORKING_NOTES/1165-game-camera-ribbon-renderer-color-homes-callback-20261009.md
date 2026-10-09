# Game Camera Ribbon Color Homes And Callback Representation

## Baseline And Scope

Continue complete `func_1514803C` from
[Note 1164](1164-game-camera-ribbon-renderer-exit-flow-qualification-20261009.md).
Owner `conker/src/game/generated_175250.c`; VA `0x1514803C..0x151488C4`,
ROM `0x1754EC..0x175D74`. Retail remains 546 words / 2,184 bytes / frame0x120.
Start with clean parent `7d4a52238ec8da9545b8a021e9061ae44fd52827` and mounted
tools `8a71e515744bb8f515f0d2885e178e55c63b4b14`. Older standalone tools stays
at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, preserving its82 initial
status entries and both dirty tracked hashes. One Codex writer; zero Claude
calls. User's "Keep commited" authorizes local tools-first banking and the
parent pin, not push, reset or older-checkout commits.

Reuse the immutable Note1159 source/whole-ELF/guard/progress hashes; never
recapture the baseline. Production remains GLOBAL_ASM. No installation,
guards, profile, aggregate progress or root README changes.

## Measured Constraint

The [representation driver](../../tools/experiments/game_camera_ribbon_renderer_representation.py)
retains the complete renderer and retail-shaped exit flow. Scope eight
real color locals plus `normalX`, `normalY`, `normalZ` and `length` inside
the existing cursor-valid block. These are used FP locals, not dummy frame
padding. Declaration scope changes their physical homes without changing
the rendering work. Moving only colors overshoots by16 bytes; moving all
ten FP locals moves them40 bytes higher. The four-local grouping recovers
the measured retail color constraint.

| Complete Form | Words | Frame | Raw Differences | Save Slots |
| --- | ---: | ---: | ---: | --- |
| Prior selected-outer | 545 | 0x120 | 509 | Retail-shaped |
| typed-gfx-cursor-local-colors-normals-length | 545 | 0x120 | 509 | Retail-shaped |
| byte-callback-cursor-local-colors-normals-length | 537 | 0x120 | 538 | Different |
| byte-callback-capture quartet | 541 | 0x128 | 542 | Different |

The primary typed-Gfx form now matches **13 private homes**: primitive
R/G/B/A at SP+C2/C0/BE/BC; environment R/G/B/A at BA/B8/B6/B4; cursor118,
sync117, originF0, previous XYZ FC and current XYZ108. Hard emitted-opcode
assertions check every home, the retail backend-call index, four GPR save
slots and five FP save pairs. It still has509 fixed-address raw differences:
payloadS3/recordsS2/view initiallyS2, versus retail S2 payload/T5 records
with spills/S3 context. FP roles and the full546-word schedule remain open.
Matching these homes does not prove complete stack layout or byte matching.

The byte-buffer form directly uses the actual caller-table signature
`u8 *(*)(u8 *, u8 *, s16)`, with typed casts at existing Gfx helper/SDK
boundaries. It recovers the same eight color homes, but saves three GPRs
and shifts FP pairs to SP60/58/50/48/40. Do not call those retail save slots
or claim all13 private homes for this form. Native fixtures assign the
candidate directly to the exact typed callback; an adapter changes only
fixture call syntax. The complete native dispatcher/callees are not run.

The texture resource must remain32-bit: recovered `func_1514306C` in
`conker/src/game_16EE20.c` returns full table/pointer values, agreeing with
its50-word retail routine. A decompiler's16-bit texture suggestion is not
an authoritative source interface.

## Qualification And Limits

The [focused suite](../../tools/tests/test_game_camera_ribbon_renderer_representation.py)
passes all **12 tests in212.922s**. It qualifies both complete primary
forms, not truncated stand-ins:

- Per form804 guest cases/1,608 executions; full public memory, ordered
  writes and callbacks. Retail's infeasible second-cursor-zero exit remains
  unexecuted; no claim every retail word executes.
- Per form92 setup mutations/184 executions; scratch GPR/FP and argument
  home clobbers. Captured versus live fields retain their prior contract.
- Per form94 missing-byte pairs, five record-pointer aliases and two cyclic
  prefixes bounded by200 public writes. No production loop bound is added.
- Per form536 native32 cases plus128 nonlinear guest/native32 cases,
  seed0x1514803C, complete vertices/commands/pointers and canaries.
- Per form14 raw view values/56 guest cases/112 executions plus14 native32
  cases; signed low-halfword helper arguments remain correct.
- Per form16 cases/32 executions through the actual52-word guest dispatcher
  and protected `D_8008A2A4[1]` pointer at0x8008A2A8. Callees are bounded hooks.
- Per form ten copied-owner neighbors/pools/relative relocations unchanged,
  zero diagnostics, actual padder acceptance. Neither form is byte-exact.
- Effective compiled negatives retain signed-active and origin-before-record
  capture requirements. Catalog51 complete forms/36 instruction streams
  receives three finite final-memory/callback controls per form, not full
  ordered-write/fault/native qualification for every catalog entry.

Fresh primary-source rebases independently assemble/link the original and
candidate under four symbol sets: eight links/25 relocation uses/184 cases/
368 guest executions, including HI16 carries, signed LO16 and JAL regions.
Byte-buffer independent rebases remain a separate gate. Native mutation,
alias, cyclic and invalid-float-cast domains, FCSR/hardware, actual callees
and gameplay are not proved by these bounded fixtures.

An initial representation screen applied color scoping after changing
helper-call syntax, leaving an unmatched brace. Apply scope transforms
before pointer conversion; do not suppress diagnostics. The initial11-test
run finished in196.472s with ten semantic checks passing and one incorrect
FP-save expectation. Correct the fixture to record the byte-buffer variant's
actual shifted slots; that run is not a passing full-suite receipt.

## Next Matching Step

Retain the new13-home primary reference and the lower-raw-difference547-word
short-input reference. Recover retail S2 payload/T5 captured-record spills,
S3 view/texture/stride lifetime and FP roles without losing the13 homes,
signed input or full renderer. Settle raw schedule and exact native callback
integration before installation and the whole-ELF/progress audit. The wider
Game goal remains active; no matching/conversion credit this turn.

## Banking

Tools **426c56cfaba215d7c3ded51ec64cb42ddf9ad569** banks only the new
driver/test pair first. This note, five short indexes and exact consumer pin
follow. Mirror only these two absent authored files into the older checkout,
yielding84 status entries and preserving all82 original entries, its HEAD
and dirty hashes. Both project tools checks pass. Syntax/exact-mirror checks
pass49 retained tool-file pairs; documentation checks pass151 documents/
4,310 relative links/zero broken. No older-checkout commit or push. Production
totals remain5,489 converted/3,406 exact, Game4,816/2,733, zero drift,
2,083 different and11,510 guards. OGL/Release/saves/editor untouched.

Manual Graphify update refuses17,087 nodes over38,875; preserves19,398
nodes from2,972 excluded files still on disk. Existing version and
devcontainer warnings remain; no force/reinstall. The fresh parent
post-commit hook must be checked independently before closing this turn.

```sh
wsl --exec python3 -m tools.experiments.game_camera_ribbon_renderer_representation --scope-quartets
wsl --exec python3 -m unittest tools.tests.test_game_camera_ribbon_renderer_representation -v
wsl --exec make tools-check
```
