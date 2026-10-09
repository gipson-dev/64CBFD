# Game Camera Ribbon Private Slots And View Staging

## Scope And Baseline

Continue complete `func_1514803C` matching from
[Note 1162](1162-game-camera-ribbon-renderer-retail-frame-save-slots-20261009.md).
Owner `conker/src/game/generated_175250.c`, VA `0x1514803C..0x151488C4`,
ROM `0x1754EC..0x175D74`: retail **546 words / 2,184 bytes / frame 0x120**.
Actual 52-word dispatcher remains `func_15147C4C`, protected table entry
`D_8008A2A4[1]` at `0x8008A2A8`.

Parent starts clean at `cc70a270e46ea4d546a3468543b41ec9b5c5e6cb`, tools
clean at `df3bbd1319bf9b60746a0a7d7bfd04c4abd84699`. Independent older
checkout stays at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with 78
initial status entries and both dirty tracked hashes preserved. One Codex
writer, zero Claude calls. "Keep commited" authorizes tools-first local
banking and the exact consumer pin, not a push or older-checkout commit.

Reuse the immutable Note 1159 baseline. Source, entire ELF, guard CSV and
progress CSV hashes remain unchanged. Production is still GLOBAL_ASM:
no installation, guards, conversion or exact-match credit.

## New Private-Slot Constraint

The [staging driver](../../tools/experiments/game_camera_ribbon_renderer_staging.py)
keeps the complete renderer, including all setup calls, signed gates,
cross-product width, SDK vertex/triangle commands, wrap and final prefetch.
Separating the incoming argument from its clipped local view gives:

| Fully Qualified Form | Words | Frame | Raw Differences | Padder |
| --- | ---: | ---: | ---: | --- |
| `selected-short-input-local-view` | 547 | 0x120 | 433 | Rejects |
| `selected-wide-input-local-view` | 545 | 0x120 | 519 | Accepts |

Both preserve four GPR save slots and five FP save pairs, and now match
**five retail private slots**: previous XYZ at SP+0xFC, current XYZ at
0x108, origin at 0xF0, sync at 0x117 and cursor at 0x118. Hard emitted-word
assertions verify these locations, not inferred debug homes. The short-input
form keeps the 16-bit view parameter and improves the prior selected
form's 463 raw differences to 433. It remains one word too large.

The color homes still differ: primitive SP+0xD4..0xDA and environment
SP+0xCC..0xD2 versus retail 0xBC..0xC2 and 0xB4..0xBA. Candidate payload
is S3 and records S2; retail payload is S2, records T5 with setup spills,
and S3 carries view/texture/stride. Frame/slot agreement is **not matching
register lifetime or schedule**. No broad guards or padding-based credit.

## View And Callback Boundary

The recovered caller declares `D_8008A2A4` as
`u8 *(*[])(u8 *, u8 *, s16)` and its own view parameter as `s16`.
The wide-input form is an isolated layout experiment, not proof of an
original 32-bit parameter. Prefer the short-input form for subsequent
matching, and reconcile the complete callback signature before installation.

A byte-buffer callback-type projection emits 549 words/frame0x128 and is
not slot-fit. Native32 GCC checks an exact recovered-type function-pointer
assignment and invokes it through that pointer for 14 view values, with
full helper arguments, vertices, commands and canaries. It also receives
56 guest cases/112 executions. This is a bounded leaf/type projection,
not a complete native caller, recovered SDK callees or gameplay acceptance.

## Final Qualification

[Fourteen final tests](../../tools/tests/test_game_camera_ribbon_renderer_staging.py)
pass in **204.038s**. Each of the two primary forms receives:

- **804 guest cases / 1,608 executions**, ordered public writes, callbacks,
  return value and full public memory; bounded nontrapping float/FCSR model.
- **92 setup-mutation cases / 184 executions**, captured/live fields,
  signed views and helper scratch/FP/argument-home clobbers.
- **94 missing-byte pairs**, five record-pointer aliases and two cyclic
  prefixes bounded at 200 public writes. No production bounds; these are
  emitted-prefix checks, not portable C fault semantics.
- **536 actual native32 cases**, full vertex/command fields and pointers,
  callback arguments, output tails and actor/payload/record canaries.
- **128 additional nonlinear cases**, seed `0x1514803C`, 256 guest
  executions and 128 actual native32 cases per form. No native alias,
  mutation, cyclic or invalid-cast acceptance is claimed.
- **14 raw view values**, 56 guest cases/112 executions across both banks
  and stack phases, plus 14 native32 cases. Both view-taking helpers receive
  the expected signed low halfword, including high-bit and wrap boundaries.
  The native short-parameter call narrows at the caller; guest direct-entry
  tests separately exercise raw register values.
- **16 cases / 32 executions** through the actual 52-word dispatcher and
  protected pointer, with transform/graphics helpers still bounded hooks.
- Ten unchanged postprocessed owner neighbors, pools and relative
  relocations; zero diagnostics; actual short rejection versus wide padder
  acceptance. Neither primary form is exact or installed.

Two effective compiled negatives reject an unclipped view and a premature
normal-input overwrite. Earlier runs exposed two fixture defects: the
negative generator revisited a just-swapped line, and native tests passed
out-of-range literals directly to a short parameter. Fix the generator's
indices and pass a real 32-bit local through the declared caller conversion.
Do not suppress compiler warnings; the final complete suite passes with
warnings as errors unchanged.

## Ruled-Out Directions

The final catalog has **20 complete source forms / 60 profile rows / 34
distinct instruction streams**, with three finite final-memory/callback
controls per row. This is not full qualification or ordered-write acceptance
for every row. Profiles are O2/g3, O2 and O2/g3/no-unroll; the profile registry
is restored after every compile. No-unroll is byte-identical to O2/g3 for
all 20 forms, so do not pursue it as this mismatch's cause. No build-profile
change. The prior O1 measurements are retained evidence, not a fresh run.

Explicit view/texture/stride staging and union storage do not recover S3's
retail role. A word-sized records base emits the same bytes as the typed
pointer form. Keep source/word hashes rather than reinvestigating duplicates.

Two compact complete arithmetic forms each pass 128 nonlinear guest/native32
cases, but fail matching constraints: inlined rays yield 543/frame0x108 with
only three GPR saves; retained rays yield 551/frame0x118 with an extra FP pair.
They reuse only dead inputs after each cross component is computed. An
effective negative demonstrates that overwriting deltaZ before computing
normal X changes public output. These forms have limited qualification,
not the primary forms' full byte/fault/alias coverage. Do not add unused
locals or padding to compensate for their frame/register mismatches.

## Next Matching Step

Use `selected-short-input-local-view` as the complete reference. Preserve
its five retail slots and 16-bit parameter while recovering retail's
active/cursor exit CFG, S2 payload, T5 record spills, S3 phase lifetime and
color homes. Resolve the full 546-word raw schedule before independent
rebases, remaining alias/mutation domains, installation and whole-ELF audit.
The complete callback signature remains an explicit integration gate.

No shared helper/profile/production input changes. Earlier broader receipts
are reused, not reported fresh. Root README unchanged. Totals stay **5,489
converted / 3,406 exact**, Game **4,816 / 2,733**, zero drift, 2,083 different
and 11,510 guards. The full Game matching goal remains active.

## Banking

Tools **d940c7e9dcb028002cba435888b02696840ca88d** banks exactly the new
driver and tests first; this note, short indexes and exact parent gitlink
follow separately. Preserve all 78 older-checkout status entries, its HEAD
and dirty hashes; copy only the two absent new paths, yielding 80 entries.
Both project tools checks pass. Syntax/exact mirrors pass for all 45
retained tool-file pairs; documentation validation passes **149 documents /
4,294 relative links / zero broken**. No push, older commit, pause or
OGL/Release/save/editor work.

Graphify query finds no exact function node. Manual update refuses 17,066
nodes over retained 38,854, keeping 19,398 nodes from 2,972 excluded files
still on disk. Existing package/skill version and zero-node warnings remain.
Do not force/reinstall; inspect the fresh post-commit hook separately.

```sh
wsl --exec python3 -m tools.experiments.game_camera_ribbon_renderer_staging --form selected-short-input-local-view
wsl --exec python3 -m unittest tools.tests.test_game_camera_ribbon_renderer_staging -v
wsl --exec make tools-check
```
