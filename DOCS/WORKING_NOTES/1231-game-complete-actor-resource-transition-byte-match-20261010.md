# Complete Actor Resource Transition Byte Match

Date: 2026-10-10

Continue [Note 1230](1230-game-complete-actor-animation-selector-byte-match-20261010.md).
Install complete func_150837D4. The wider Game matching goal remains active;
this checkpoint is not complete callback, gameplay or host-port acceptance.

## Scope And Baseline

- Consumer starts at clean 8cea690b, mounted tools at clean 0474fdc.
  Single Codex writer, zero Claude calls. User's keep-committed authorization
  applies: tools first, then consumer source/guards/docs/tools pin; no push.
- VA 0x150837D4..0x150838EC, ROM 0xB0C84..0xB0D9C, 70 words / 280 bytes,
  original 0x30 frame. Owner conker/src/game/generated_AEB40.c.
  Graph query and complete retail assembly, direct selector/tier caller
  interfaces and actual O2/g3 owner profile govern the recovery.
- Five immutable before-* snapshots: owner, ELF, guards, conversion progress
  and protected rodata. Hashes are asserted on each run. Prior selector/tile
  baselines and historical installation receipts are not rewritten.
- Older standalone tools stays at ddbdd16, independently dirty: native Windows
  entries 224 before, 227 after three absent-path mirrors. The tracked-dirty
  game_owner_pool.py and test_game_node_effect_registration_match.py hashes
  remain 159B8C009AF7B2D26BA5DCE29F0C46CA0805CF14DBB27E5C682D107E551CA50E
  and C9195B44C4276E410CD6ABAB7F926E4C920363BF84505F5596681937397FBC71.
  No older-tools commit/reset, OGL/Release, editor, save or private-input changes.

## Recovered Behavior

Use the low-word actor address D_800CC2D0 + slot*0x32C. Store the identity's
low byte at actor+4, but compare the complete 32-bit argument to 255.
Full-width values such as 0x1FF are not sentinel reset cases.

Sentinel 255 clears halfwords +0xE4/+0xE6/+0xE8/+0xD6/+0x160, writes 70 to
+0xD2/+0xD4 and positive float zero to +0xC8. Other identities capture the
address of D_800D1C90[identity], load its definition and signed halfword +6,
capture scale float words +0x14C/+0x150, and store the exactly representable
signed height as a float at actor+0xC8 in the call delay slot. Invoke
func_15062BDC(actor, scaleXZ, scaleY) using the mixed O32 float-in-GPR ABI.

Retain the table-entry pointer, not the definition pointer, across that call.
Reread the retained entry after callback mutation; copy the resulting
definition's unsigned byte +0x12 to actor+5. Do not re-index with mutated
actor.id or cache the earlier definition. Both paths call func_15084D00(actor),
store its return's low byte at actor+6 and use that byte for D_800C5A90.

Only a nonzero unsigned count calls the existing variadic archive-path resolver
func_1502B020(NULL, 2, 2, canonicalByte). This is not an allocator. Store the
returned address at actor+0x58 even when zero; leave the field unchanged when
count is zero. The routine is void. Preserve the unused third argument home,
saved S0/RA, retained entry-pointer home and callee-saved GP/FPR lifetimes.

## Complete C And Checked Guards

Thirty-two source shapes measured. Selected complete C emits all 70 words,
the original 0x30 frame, zero diagnostics/pool, and 15 word differences.
The normal O2/g3 profile is unchanged. The full source performs every store,
load, conversion and conditional call; padding does not supply missing behavior.

Twelve guard sites normalize closed resource/canonical/count register lives.
Two retain their existing D_800C5A90 HI/LO relocation dependencies. Three more
sites normalize the epilogue: raw C emits an annulled zero-count RA load and a
nonzero-count RA load as alternatives. Merge those alternatives at the already
emitted common epilogue RA load, move the emitted a2=2 producer earlier, and
copy the emitted move with the renamed canonical-byte source into a3.

This is deliberately not described as a pure permutation or retention of
every instruction producer. One alternative load is folded, one move copied;
the full raw/fitted/retail private access order and every selected fault prefix
prove the bounded equivalence. No ROM-loaded instruction recipe, fake zero
return, missing-body fill, instruction insertion or CSV omission is used.
The generator validates all 70 input words and all nine relocation sites;
every stale-word and stale-relocation control rejects. Append exactly 15 rows.

Authored tools: [source candidates](../../tools/experiments/game_actor_resource_transition_candidates.py),
[checked recipe](../../tools/experiments/game_actor_resource_transition_matching.py),
[complete qualification and linked audit](../../tools/tests/test_game_actor_resource_transition_match.py).

## Fresh Qualification

- 4,848 cases / 14,544 retail/fitted/raw executions match an independent ordered
  full private/public reference. Every retail word executes. Cover all identity
  bytes, full-word low-FF non-sentinels, signed height boundaries, zero/max
  unsigned counts, full callback-return narrowing, signed/wrapped guest slots,
  unused argument words and mixed O32 float bits. Callbacks clobber caller GP/FPR.
- Twenty-two live table/resource/count/actor/private-home alias cases, including
  a callback overwriting the retained table-entry home. All 428 selected access
  ordinals fire: 1,284 failed executions compare complete memory/events/calls
  across retail, raw and fitted. Missing faults fail. This is emitted guest
  ordering evidence, not portable C fault semantics or asset-validity proof.
- Nine independent retail/raw/fitted links under three symbol sets pass 48
  cases / 144 executions, with signed HI/LO carries and distinct JAL entries.
  Six further links qualify live count/actor and entry/argument-home aliases.
- Production-profile copied owner compiles/posts/pads with zero diagnostics.
  All 30 neighbors retain exact bodies, extents and relative relocations; pools
  are exact. Only the actual 280-byte target and its own relocation sites change.
- Nine fresh complete IDO semantic negatives and three native negatives are
  effective: full-word sentinel, signed height, float arguments, definition byte,
  live definition reload, canonical narrowing, count gate, path depth and output
  field. Guards cannot hide an incorrect semantic source.
- Actual banked 98-word selector and all three complete 70-word target forms
  execute in 48 cases / 144 runs; complete private traces and ABI agree.
  Scale, canonicalizer, resolver and other selector callbacks remain bounded.
- Complete native32 C at O2/O0 passes 105,472 cases each, 210,944 executions.
  Cover all 26 valid slots and identity bytes, all 65,536 signed-height halfword
  bit patterns, live table-mutating callbacks, zero/nonzero counts and resolver
  addresses, and actual mixed float ABI including supplied nonfinite bit patterns.
  Separate little-endian reference. Wrapped invalid guest indices are not native
  portable-pointer acceptance; actual scale arithmetic/FCSR is not executed.

The initial native fixture lacked stddef.h's NULL definition. Add the standard
header to the freestanding harness, then rerun all nine tests. No production
semantics, baseline snapshot or acceptance assertion was weakened.

## Installation And Bank

Full linked rebuild and conversion progress generation succeed. Shared guard
manifest triggers a broad rebuild. Existing duplicate generated_12D630 recipe,
unrelated C warnings and assembler/old-toolchain warnings remain; the target
owner is diagnostic-free, not the whole build. Nine final post-install tests
pass in 18.820s; root tools-check, older-copy standalone tools check and all
three exact mirrored Python parses pass.

Whole ELF audit permits only this 280-byte slot and symbol-size update. All
other bytes, addresses and extents are exact, with established symbol/string
ordering normalization only after complete metadata and symbol/name multisets
match. Original 1,864,867 guard bytes remain an exact prefix; append 15 rows.
Current guard file is 1,867,291 bytes. Preserve the existing CRLF-to-LF Git
warning; do not broadly rewrite line endings. Conversion CSV and protected
rodata are byte-identical. Protected data: 189,088 bytes / 720 owners / zero
differences, SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Current ELF SHA-256: 72afd676886e434a8de725d4ab8d20662212e93ccea70527591982149137cee2.

Fresh matching: Game 2,766/4,816 (57.43%), total 3,439/5,489 (62.65%), zero
address drift / 2,050 different. Delta +1 matching credit. Converted function
and byte totals are unchanged. Root README changes aggregate rows only.
Bank mounted tools 49e2558 first, then consumer source/guards/docs/tools pin.
No push requested/performed; the older independently dirty checkout stays dirty.

```sh
python3 -m tools.experiments.game_actor_resource_transition_candidates
python3 -m unittest tools.tests.test_game_actor_resource_transition_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Native graphify update after code edits refuses unsafe shrink 39,482 -> 17,699
nodes, retaining 19,398 nodes from 2,972 excluded-but-existing files. Preserve
the refusal, skill 0.9.20/package 0.9.26 warning and devcontainer.json zero-node
warning; no force, purge or installation. Consumer's existing post-commit hook
runs separately; verify fresh log growth/completion and zero workers before
reporting a clean checkpoint.

## Next And Boundaries

Next decomp target: full 28-word func_1507EABC, currently GLOBAL_ASM in
generated_AB760.c. VA 0x1507EABC..0x1507EB2C, ROM 0xABF6C..0xABFDC, 0x20 frame.
It calls func_1507E7E4(actor, actor[0x70], 3, 0xFFFF, 10), then rereads the actor,
clears +0x71/+0x72 and resets each +0x6C/+0x6A or +0x6D/+0x6B pair when the
corresponding unsigned byte is >=10. Qualify its five-argument ABI, callback
mutations and branch-delay/private-home lifetimes before conversion.

Actual resource-transition scale/canonical/archive helper connections,
nonfinite arithmetic/FCSR/traps, real asset domains and hardware/live gameplay
remain separate open gates. No OGL or frozen Release acceptance is inferred.

Workflow review: zero Claude calls attempted/completed; complete local assembly,
source experiments, independent references and focused tests settle the task.
No packet/model invocation or billing change. Prior unchanged neighbor receipts
remain historical, not relabeled fresh; this target's 30-neighbor and complete
banked-selector checks are fresh. The wider Game goal remains active.
