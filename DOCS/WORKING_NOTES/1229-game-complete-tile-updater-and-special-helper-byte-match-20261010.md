# Complete Tile Updater And Special Helper Byte Match

Date: 2026-10-10

Continue [Note 1228](1228-game-actor-texture-tile-updater-qualified-schedule-and-padding-20261010.md).
Install complete func_1502F9FC and its real special helper func_150C3160.
The wider Game matching goal remains active; this is not whole-game completion.

## Scope And Baseline

- Consumer starts clean at 7761004d; mounted tools starts clean at f2dd1c3.
  Single Codex writer, zero Claude calls. User's keep-committed authorization
  applies; tools commit first, then consumer source/guards/docs/tools pin.
- Tile updater: VA 0x1502F9FC..0x1502FBE8, ROM 0x5CEAC..0x5D098,
  123 words / 492 bytes, original 0x20 frame. Source generated_58F80.c.
- Special helper: VA 0x150C3160..0x150C3230, ROM 0xF0610..0xF06E0,
  52 words / 208 bytes, leaf/no frame. Source game_EF410.c, still a false
  zero-return placeholder before this recovery. Graph lookup located that
  placeholder at line 241; complete assembly and live source govern evidence.
- Six immutable before-* snapshots include both owners, ELF, guards, progress
  and protected rodata. The other five equal the original Note 1227 snapshots
  exactly. Baseline receipts reject; never replace snapshots to pass a test.
- Older tools stays independently dirty at ddbdd16; two tracked-dirty hashes
  are preserved. No OGL/Release/save/editor changes and no push.

## Recovered Helper

Read the signed actor divisor at +0x2E8; if nonzero, convert numerator +0x2E4
and divisor separately to single precision and divide. Otherwise ratio is 1.
Compute single-precision (1-ratio)*500+2 and truncate toward zero. Capture
the previous +0x2EC word before replacing it with coordinate/3, signed division
toward zero. Compute wrapped low-word 2-previous; add 64 while it is negative.
Emit tile 4 command F2, coordinate/wrapped phase masked to 12 bits, constant
second word 0x041FE03E. Return the cursor advanced by eight bytes, not the
earlier bounded model's arbitrary 16-byte advance/mutations.

The complete normal O2/g3 C emits all 52 retail words directly, with no guards,
frame, relocations, pool or diagnostics. Five source shapes/two profiles were
measured. Four O2 forms are exact; ratio-first is 49 words/50 differences.
All O1 forms differ and use a 0x10 frame. Preserve the normal retail profile.
Use explicit unsigned subtraction plus signed interpretation for previous
phase, avoiding signed subtraction overflow in the recovered C.

The updater retains the previously qualified full 120-word C, all 120 checked
rows and three copies of existing address/move producers from Note 1228.
No omitted producer, missing behavior, extra memory access or missing-body
fill is introduced. Its fitted body is all 123 original words.

Authored tools: [complete helper candidates](../../tools/experiments/game_actor_special_tile_candidates.py)
and [actual helper/updater qualification and linked audit](../../tools/tests/test_game_actor_special_tile_match.py).

## Fresh Qualification And Installation

- 1,680 special-path cases / 5,040 original/raw/fitted executions: both actor
  types, six signed/wrapped slots, ten integer-to-float pairs, seven previous
  phases, two stack phases. Full private/public memory, events and calls match
  an independent rounded single-precision and ordered-memory reference.
  All 51 reachable helper words execute; standalone MTC1 at word 12 is
  unreachable from either branch and remains byte-exact in the complete body.
- 240 live alias cases / 720 executions cover output and actor +0x2E0/+0x2E4/
  +0x2E8/+0x2EC, plus private output. All 2,592 selected fault prefixes fire,
  7,776 failed executions; full private/public prefix bytes/events/calls agree.
  Missing faults or a modeled helper substitute fail.
- Twelve independent links / four symbol sets pass 480 cases / 1,440 executions
  with real helper execution at changed entry addresses and signed HI/LO carries.
  Helper has no absolute dependencies; all private order and fitted words agree.
- Complete actual banked dispatcher/renderer/color/RGB/shading/identity-matrix
  paths pass 80 cases / 240 executions with real helper body. Independently
  check the captured updater boundary; no saved-PC adjustment. Other unrelated
  callbacks remain explicitly bounded.
- Complete native32 helper and updater C with actual SDK macros passes 812
  cases at each O2/O0, 1,624 executions. All 256 types/null roots plus signed
  conversion, wrap and live actor aliases; independent little-endian reference.
  Native valid slots are 0/25; invalid wrapped slots remain guest-only evidence.
- Six fresh complete IDO negatives and three fresh native negatives are effective.
  Three fixture corrections: reference/model exception types; real layout
  filename retail_layout.us.txt; map the constant pool introduced by a freshly
  compiled negative. Installation patch emission also needed root PYTHONPATH,
  native Windows patch paths and bare apply_patch hunk markers. No snapshots
  or acceptance gates changed to accommodate these corrections.
- Copied special owner compiles/posts/pads with zero diagnostics. Its 17
  neighbors, extents, relative relocations and pools stay exact; only 208-byte
  target changes. Prior updater's 37-neighbor/copied-padding/stale dependency
  receipt is reused from Note 1228 with unchanged source/profile/recipe inputs,
  not claimed as freshly rerun. New whole-linked audit covers both owners.
- Production uses typed helper/updater prototypes and full bodies. Append
  exactly 120 updater guards; special helper has no guards. Preserve all
  original 1,843,199 guard bytes as an exact prefix.
- Full linked rebuild and progress regeneration succeed. The shared manifest
  triggers a broad rebuild; existing duplicate generated_12D630 recipe,
  unrelated C warnings and MIPS3 warnings remain. Do not call it warning-free.
- All eight final post-install tests pass in 29.436s; root tools-check passes.
  Whole ELF audit permits only two instruction slots and two symbol-size
  updates, 700 bytes. All other linked bytes/addresses/extents remain exact
  apart from established symbol/string-table ordering normalization, whose
  complete symbol/name multisets and ELF headers are independently equal. Conversion CSV
  and protected rodata stay byte-identical; original six snapshots remain exact.
- Protected data: 189,088 bytes / 720 owners / zero differing bytes, SHA-256
  0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

```sh
python3 -m unittest tools.tests.test_game_actor_special_tile_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Fresh matching credit: Game 2,764/4,816 (57.39%), total 3,437/5,489 (62.62%),
zero drift / 2,052 different. Both gain two; conversion counts/bytes unchanged.
Root README updates aggregate rows only, not this narrative.

## Bank And Resume

Tools 041a6fa commits the two new authored files before consumer commit/pin.
Mirror only these absent paths; older native dirty entries 219 to 221, same
HEAD and tracked-dirty hashes. No older-tools commit/reset and no push.
Fresh handoff validation passes nine documents / 4,135 relative links, zero
broken links, both exact new mirrors parsed, unchanged older HEAD/fingerprints/
221 dirty entries, all six snapshots and original five copies exact.
Current qualified ELF SHA-256:
906827b2d10cce160f49fafcd70a890c5ab00bb20eeaed3e057669d8f702d160.
Refresh native graphify after final code edits; preserve unsafe-shrink,
retention, version and zero-node warnings, no force/purge/install. Verify fresh
consumer-hook log growth and absence of workers before finishing.
Native refresh exits 1, refusing 39,461 to 17,681-node shrink and retaining
19,398 nodes from 2,972 still-existing excluded files. Preserve the original
graph; version mismatch and devcontainer.json zero-node warnings remain explicit.

Next target is func_1502FBE8 in this owner: VA 0x1502FBE8..0x1502FD70,
ROM 0x5D098..0x5D220, 98 words / 392 bytes, original 0x40 frame. Still empty C.
Inspect complete pending/current selector bytes, selected-resource comparisons,
actor index division, all three callbacks and repeated mode reads before C
recovery. Keep callback/alias/private-order and full installation audit gates.

Finite conversion qualification is explicit: out-of-range/nonfinite conversions
are rejected by both reference and instruction model, not treated as MIPS/FCSR
or portable C acceptance. Extreme long wrap loops, FCSR/traps, cosine/other
callbacks and hardware/live-game acceptance remain open. Separate threshold
curve gates from [Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md)
also remain open. Do not infer host-port acceptance from retail byte matching.
