# Complete Game Actor Renderer Recovery And Private Layout Gates

Date: 2026-10-10. Continue the full renderer after
[Note 1220](1220-game-actor-alpha-shading-byte-match-20261010.md).
Consumer baseline 6d4c9c23, mounted-tools baseline 89e8ece.
Codex is the single writer; zero Claude calls. Keep authorized tools-first
commits, no push, no host/Release builds, saves or editor changes.

## Full Target And Recovered Contract

func_1502CCFC: VA 0x1502CCFC..0x1502D54C, ROM 0x5A1AC..0x5A9FC,
532 words / 2,128 bytes; original 0x150 frame. Its complete eight arguments
are commands, slot, view, matrix, alpha, four-channel parameters, mode, extra.
It returns the advanced Gfx cursor, or the incoming cursor on either early gate.
The production zero-return placeholder is deliberately still unchanged.

[Complete candidate](../../tools/experiments/game_actor_renderer_candidates.py)
recovers the entire renderer, not only its early gates:

- Capture actor identity; modes 3/4/5 call func_150849CC for identity and tier,
  while other modes read actor +0x1C8. Call func_1503DA9C with mode != 3.
  Reject its nonzero result or a null selected tier/page matrix pointer.
- Emit the optional opening display list, otherwise pipe sync. Thread the
  cursor through func_1502F01C and func_1502F9FC. Set segments 3 and 1;
  segment 1 uses the re-read selected model pointer minus 0x38.
- Call func_1502CC34 with fourteen arguments: actor/view/alpha/parameter array
  plus ten private color outputs. Select segment 8 from mode and signed alpha.
- Set culling, capture the signed halfword at configuration +0x3E, and select
  geometry/lighting from actor +0x66, mode, and global lighting enable.
  Retail's custom geometry bit is 0x400000, not this SDK's G_FOG value.
- Submit all fourteen func_1515D914 arguments, including truncated coordinates,
  actor flags, full-width view-indexed value, active-page light pointer,
  count/output pointers, and history/force flags 2 or 10.
- Iterate the live unsigned-halfword part count. Actor masks +0x94/+0x98
  select skipped parts and override colors. State transitions emit pipe sync,
  fog, primitive and environment commands. Preserve byte masking and signed
  alpha comparison. Primitive control is 0xFA00F200, not 0xFA0000F2.
- Mode 3 uses the optional D_800C48F0 part array; other modes call
  func_151EFE88, emit the identity matrix, and use D_800C4488 part lists.
  Re-read count, masks and part-table entries across callbacks.
- Call func_1502FD70, set actor +0x2FE to one, optionally call func_15030F94
  for mode zero, emit the optional closing list, and restore culling.

Use the existing SDK graphics macros. Assembly and undefined_syms_auto.txt
retain separate D_800C3E98 virtual and D_C3E98 physical matrix symbols.
The candidate uses the real physical alias instead of synthesizing a mask.
Initial compilation caught the SDK fog/control-byte discrepancies; both were
corrected before the passing semantic proof. Negative controls reject them.

## Fresh Complete Behavioral Proof

[Focused suite](../../tools/tests/test_game_actor_renderer_recovery.py):

```sh
python3 -m tools.experiments.game_actor_renderer_candidates
python3 -m unittest tools.tests.test_game_actor_renderer_recovery -v
make tools-check
```

All nine tests pass in 13.441s. Fresh project tool checks pass.
273 primary guest cases execute all 532 original words and two complete
compiled C forms: 819 executions. Independent semantic reference checks
complete command words, callback ABI, returned cursor and public memory;
original/candidate public access traces also agree in those cases.

Cover seven modes, first/last actor slots, four geometry flag classes,
signed configuration/alpha boundaries, first/last identities, active pages,
history/force lighting, optional lists, zero/1/4/33 part counts, null gates,
wrapped part shifts, full-width views, color-state transitions and stack phases.
Fourteen callback-mutation cases distinguish live count/masks/table pointers
from captured page, configuration and identity. All requested paths execute.

Eight fresh complete compiled negatives are effective: wrong fog bit,
primitive control byte, inclusive/signed alpha mistakes, wrong skip mask,
wrong part array, missing actor-tail state and a cached count.
Six independently assembled links / nine cases exercise original and candidate
under three symbol sets with signed LO16 carries, including virtual/physical
matrix aliases. Public semantics and order agree; this is not a byte-match claim.

Copied-owner qualification preserves all 37 neighbor bodies and relative
relocations, normalized pools, and the target's isolated instructions.
Both copies compile with zero diagnostics. The temporary owner updates the
renderer and pointer-returning func_1502F9FC declarations only as needed.
Do not type the still-empty color helper's definition incidentally: the measured
typed-empty variant emitted four new incoming-argument stores. The final copy
preserves that neighbor's old-style declaration and exact body instead.
The earlier prototype/neighbor failures were test-copy findings, not production
edits or reasons to weaken the neighbor gate.

Callbacks remain explicit bounded ABI/effect models. The complete 532-word
renderer executes; lighting, colors, identity-matrix and other helper bodies
are not claimed recovered or connected by this suite. No native32 renderer,
FCSR/trap, hardware or live gameplay acceptance is claimed.

## Physical Installation Gates

Fourteen complete source forms were measured with no diagnostics or new pools.
Selected body: 524 words / 0x148 frame. Volatile-mode form: 533 / 0x148.
Volatile mode plus unmasked guest shift: 532 / 0x148; matching word count alone
does not close its private layout. An unused-matrix declaration expands to
0x1C8 and is rejected, not an installation recipe.

The retail color outputs are original SP +0x128 down to +0x104 in four-byte
steps. Selected raw outputs are raw SP +0x138 down to +0x114. Accounting for
the eight-byte smaller frame, all ten raw addresses are 24 bytes above retail.
The fresh physical test confirms full private memory differs even where
public traces agree. Original identity/tier homes, saved-register map, private
color/state lifetime and access-fault prefixes remain hard gates.

No guard recipe, frame padding, missing-body fill or production installation
was added. Immutable before-source/ELF/guards/progress/rodata fingerprints
all remain exact in conker/build/game-actor-renderer-test/baseline.json.
Before-source SHA-256:
6d3eb1946ce65477f56e8dea69a89812a6ebead86b7f980472dbf9ada660d216.
The full linked ELF fingerprint remains
0e401ea0c0f8361e202571d92d18d8df6d43f96b9f6de77809c11dff894cdbb1.
Matching stays Game 2,760/4,816 (57.31%), total 3,433/5,489 (62.54%),
zero drift / 2,056 different. Root README aggregates therefore stay unchanged.

## Bank And Resume

Tools 4d76cac commits the two new authored files first. Mirror only their
absent paths to older tools; older HEAD ddbdd16 and its two tracked-dirty
fingerprints remain exact. Dirty entries rise 202 to 204 only for these mirrors.
Commit this note, five concise indexes and the new consumer tools pin; no push.

Manual graphify update exits 1 refusing 39,402 to 17,621-node shrink.
Retention keeps 19,398 nodes from 2,972 excluded-but-existing files.
Preserve version/zero-node warnings; no force, purge or install. Check the
fresh detached consumer hook and log growth after committing.

Resume this same complete renderer. Recover 0x150 frame and exact private
color/identity/tier homes and saved-register lifetime before closing scheduling.
Then qualify aliases, fired full fault prefixes, actual padding and rebases,
native32 SDK output, and the complete dispatcher/RGB/shading/renderer/helper
chain. Use the full original color-helper body/contract when connecting it;
do not accept the bounded hook as helper restoration. Install only after
those gates, then rebuild, audit linked changes and measure fresh progress.
Keep the separate uninstalled curve gates from
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md)
and the wider Game goal open.
