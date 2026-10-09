# Game Owner Ribbon Renderer Shared Copy And GPR Proof

Date: 2026-10-09

## Result And Boundary

Continue complete func_151B32C8, VA 0x151B32C8..0x151B3A34,
ROM 0x1E0778..0x1E0EE4, from
[Note 1182](1182-game-owner-ribbon-renderer-induction-and-fp-proof-20261009.md).
The [shared-copy/register driver](../../tools/experiments/game_owner_ribbon_renderer_registers.py)
retains all 475 words /1,900 bytes, frame 0x148 /328 bytes and original private
cursor/point/origin/sync/material and saved-register homes.

Selected source before-last-helper recovers all three initial second-point loads
through the shared actor+0x48 base. Raw differences fall 163 to 161; the existing
FP-only remap leaves 149. A new certified 107-word GPR remap composes with the
13-word FP remap, changing 120 words total and leaving 44 retail differences.
All vertex/loop/epilogue phase words agree after certified normalization.

Still uninstalled and nonmatching. The zero-return placeholder in
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c) is unchanged.
No new literal-word guards, matching/conversion credit or README aggregate change.
Source/ELF/guards/progress and protected Game data remain unchanged.

Baseline parent 1d5ee1a4f170114ad51c4d0600c6d5190a02b9a3,
mounted tools 5a069ec8192680c4ba41c745640742db9ab5426d; both clean before edits.
Single Codex writer, zero Claude calls. Prior turn made committed progress;
this turn continues the same complete renderer. No OGL/Release/save/editor work.

## Direct Shared-Base Recovery

Move the real points=actor+0x48 address calculation before func_15142FBC. It
performs no actor-data read or write. Initial geometry still reads after that
helper and observes its mutations. The compiler now retains the shared-base
shape for second-point lw offsets 0x18, 0x1C and 0x20, not actor-relative
0x60, 0x64 and 0x68. The loop's original offset counter/two pointers are retained.

Fourteen complete source forms, 32 public-contract fixtures each /448 candidate
executions: zero contract failures, compiler diagnostics and literal pool bytes.
Typed/register/record/integer-base and advance/restore forms do not improve the
prior 163-word difference count. Earlier point-base address initialization forms
produce 161 differences with the same slot/frame. Selected before-last-helper
keeps the change close to the actual geometry setup.

Word-copy and float-copy controls emit 475 words/frame 320/468 differences and
473 words/frame 336/374 differences respectively. Passing bounded fixtures does
not make their incorrect frame/slot shape acceptable for installation.

## Closed GPR Certificate

Within offsets 0x26C..0x730, permute only architectural GPR operand fields:
T6/T7 exchange and T8/T9 exchange. Exactly 107 instruction words change.
No FP fields, operation bits, immediates, memory offsets, branch targets or
instruction order changes. The recipe never looks up retail words to generate
instructions. LDC1/SDC1 address fields and JALR operand classification are handled
explicitly; unexpected instruction forms fail closed.

Run the independently checked FP certificate first. The GPR proof then operates
on that FP-normalized full body, proving the actual composition rather than
assuming two independent raw-body checks imply the composed result. For every
ordered GPR input, symbolic provenance must agree before assigning identical
result tokens. Checked address/store/MTC1 inputs maintain memory/FP equality;
operation bits and ordered arithmetic are unchanged. Explore both FP branches
through the fixed nine-iteration loop, then require return and saved GPR state
to agree after the unchanged restore tail.

Measured GPR certificate: 1,024 paths, 320 reached words, 260,875 symbolic steps,
107 changed words. The fields are disjoint from the 13 FP changes; both remaps
commute and the composed body changes 120 words, closing 117 retail differences
relative to the new 161-difference raw body.

A colliding map still changes 107 words but fails a live GPR input. This is an
effective unsafe-lifetime control, not merely a rejected extent or changed-count
test. Stale loop-counter mutation also fails. Existing FP unsafe mapping and
frame/zero/counter controls still fail. Certificate scope is closed allocation
equivalence; it is not a hardware/FCSR, full-retail or live-gameplay proof.

## Qualification

[Fifteen-test suite](../../tools/tests/test_game_owner_ribbon_renderer_registers.py)
passes in 60.131s, zero skips. After making the GPR proof explicitly consume the
FP-normalized body, final focused test_15 passes in 1.348s. Source and emitted
candidate/normalizer output were unchanged by that proof-composition tightening;
the full renderer suite is not falsely reported as rerun after it.

- Raw guest: 512 cases /1,024 original/candidate executions, all 475 words,
  flags/lazy exits/geometry/UV aliases and hostile volatile/outgoing-home clobbers.
- Raw mutations: 385 cases /770 executions, signed view/unsigned selector,
  retained origin, live points/width/texture step and full material output widths.
- Actual complete native32 C: 7,680 cases, full actor/vertex/command bytes,
  ABI, aliases, finite binary32 geometry, untouched flag bytes and texture wrap.
- Four independent symbol sets/eight links: 64 cases /192 original/raw/combined
  normalized executions and all 17 original relocation uses retained.
- Raw installed 34-word material callback: 32 cases /64 executions; complete
  original 348-word graphics walker: 32 cases /64 executions.
- Six effective semantic negatives, including the adapted points-base late-origin
  injection; 12 missing-byte faults /24 executions plus three lazy fixtures.
  Fault checks compare public prefixes, not portable C/hardware exception order.
- Raw all-word/private-home/saved-FP test: 64 cases /128 executions, all 475
  words and 12 seeded incoming saved FP words; callback output addresses agree.
- Repeat guest/mutation/material/walker/fault/all-word FP qualification with
  the entire combined normalized body and the same counts. Native32 qualifies
  the actual C source, not a separate normalized C source.
- Copied actual owner: 16 neighbors, relative relocations and pools preserved,
  zero existing/new warnings. Raw target equals isolated output; actual padder
  accepts 1,900 bytes and emits it unchanged without padding/new guards.
- Production source/ELF/guards/progress hashes, registered renderer pointer and
  all protected Game bytes remain unchanged and exact.

Full helper and second material callback bodies, caller overflow/rollback,
SDK/hardware/live rendering/gameplay acceptance remain separate open gates.

## Remaining 44 Words

Counts at retail phase boundaries diagnose remaining fit, not permission to
substitute original words:

| Offsets | Phase | Raw differences | Combined normalized | Words |
| --- | --- | ---: | ---: | ---: |
|0x000..0x26C|Resource/material/graphics setup|30|30|155|
|0x26C..0x380|Initial copies and geometry|22|14|69|
|0x380..0x4CC|Initial vertex pair|47|0|83|
|0x4CC..0x5D4|Loop copies and geometry|10|0|66|
|0x5D4..0x730|Loop vertices and commands|52|0|87|
|0x730..0x76C|Return/restore|0|0|15|

The 44 remaining words separate into:

1. Nineteen setup words at 0xCC..0x12C: retained-origin arithmetic, sync and
   independent outgoing argument-home initialization scheduling.
2. Eleven words at 0x234..0x26C: render-mode intermediate lifetime and table
   address/value allocation, with a reversed read-only table pair order.
3. Eleven initial-copy words at 0x26C..0x298: point/stack cursor setup, zero
   initialization and independent load/store scheduling.
4. Three independent FP loads at 0x2B8..0x2C4.

Continue fitting these actual source lifetimes/schedules. Any residual recipe
needs closed-window operand/memory/ABI proof, effective negatives and full
combined-body independent rebase qualification before guards. Reversed public
table reads and private-home stores cannot be casually called unchanged access
order. Install only after all 475 linked words plus whole owner/ELF/data/guard
history checks pass. Never synthesize retail instructions to force agreement.

## Preservation And Checkpoint

Unchanged SHA-256:
source 33a6690f6229713ead48a1ba2fb2d826cb268a28c889671d378b4a1e94e1179b;
ELF 952b3100768e9ef8f6ff029c29bcfe1bba3bda03d66d6b97769b02313b77eac8;
guards 6dd23d98d3c335a91a185500d9336765fe2e3966f00f74b166e8dce9bfa15d9b;
progress 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.
Protected Game data 189,088 bytes /720 owners remains exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Game 2,742 /4,816 exact; total 3,415 /5,489, zero drift /2,074 different remain
the unchanged installed baseline. Root README aggregate rows stay unchanged.

Mounted tools ea649be2b5bb02dee460e1374ed93e9ca652abed commits the driver and
suite before parent documentation/tools pin. No push requested/performed.
Older standalone HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 118
preexisting dirty entries are preserved. Mirror only two absent authored files,
yielding 120; no older-checkout commit/reset/push or tracked dirty-file changes.

Ignored receipts: conker/build/game-owner-ribbon-renderer-registers/ and
conker/build/game-owner-ribbon-renderer-registers-test/. Validate current docs/
links, authored tooling parse/mirror bytes and scoped Git before consumer commit.
Validation passes: 169 documents /4,521 relative links /zero broken. All 85
authored tooling files parse and have exact mounted/older mirror bytes. Older
HEAD, both tracked dirty-file hashes and all 118 original dirty entries remain
unchanged; only the two intended new files raise that checkout to 120 entries.
Final focused production/data preservation test passes in 0.835s.
Graph query still identifies the production placeholder; preserve the existing
corpus on a shrink refusal and wait for the separate incremental commit hook.
Explicit graphify update . exits 1: refuses a 39,042-to-17,259 node shrink.
No force/purge/install. Retain local version/zero-node/scan-corpus warnings;
the consumer post-commit refresh has a separate completion receipt.
Wider Game matching goal remains active.
