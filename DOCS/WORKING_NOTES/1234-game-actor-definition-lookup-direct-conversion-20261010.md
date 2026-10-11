# Actor Definition Lookup Direct Conversion

Date: 2026-10-10

Continue [Note 1233](1233-game-complete-actor-channel-transition-conversion-20261010.md).
Convert complete func_1507E908 from GLOBAL_ASM to byte-exact semantic C.
The wider Game matching goal remains active; this checkpoint is not host or
whole-game acceptance.

## Scope And Baseline

- Consumer starts clean at 20f89d73, mounted tools clean at 4da6c0b. Single
  Codex writer, zero Claude calls. Keep-committed authorization: tools first,
  consumer source/docs/tools pin second; no push.
- Owner conker/src/game/generated_AB760.c; VA 0x1507E908..0x1507E968,
  ROM 0xABDB8..0xABE18, 24 words / 96 bytes, original 0x18 frame.
  Preserve the original assembly and nonmatchings copy. Read all direct caller
  interfaces and actual classifier code rather than relying on graph coverage.
- Seven immutable before-* snapshots cover owner, ELF, guards, conversion CSV,
  protected rodata, tracked symbols and ignored undefined-function assignments.
  Baseline owner SHA-256
  d57a39f2f0a64817830af728e79a742c09fe86898940983cd197499876dfa976;
  ELF bf999834941dc6804caa011978298b58687ee6e9512c4649a766a49d2c57ec91.
  Recheck all snapshot hashes; never regenerate the baseline after installation.
- Older standalone tools remains ddbdd16, independently dirty: 231 native
  Windows Git entries before, 233 after two absent-path authored mirrors.
  Both exact mirrored Python parses pass. Preserve tracked-dirty fingerprints
  game_owner_pool.py
  159B8C009AF7B2D26BA5DCE29F0C46CA0805CF14DBB27E5C682D107E551CA50E and
  test_game_node_effect_registration_match.py
  C9195B44C4276E410CD6ABAB7F926E4C920363BF84505F5596681937397FBC71.
  No older-tools commit/reset, OGL/Release, editor, save or private-input changes.

## Recovered Behavior And Match

Typed arguments are actor pointer and full signed-word index; return a nullable
byte pointer. Save the entire index in the incoming O32 home across
func_150849A0(actor). Read the selected live D_800D1C90 entry after that call.
Null archive returns zero. Otherwise move the cursor back eight bytes and read
the records pointer. Null records also returns zero. Return records plus the
unsigned-word index times ten, retaining emitted modulo-32-bit arithmetic.
No index-range check or byte narrowing is present in retail.

The early-return C body emits all 24 words directly under normal O2/g3: zero
guards, insertions, omissions, diagnostics or pools, original 0x18 frame. JAL
relocation at +0x0C and global-table HI16/LO16 at +0x18/+0x20 are preserved.
The archive cursor local recovers retail's subtract-eight instruction; the
unsigned pointer-offset expression recovers its exact final ADDU operand order.
An integer-address return form differs by one commutative ADDU word; a direct
header expression loses one word. Do not credit either as the direct match.

Retail restores RA before reading the archive header. For nonnull archive it
reloads the saved index even when records is null; null archive skips both
reads. Qualification compares that private read order and returned pointer,
not just public state. Extreme guest indices may form pointers outside a real
C object: their emitted guest behavior is tested, but those synthetic addresses
are not claimed as portable native C acceptance.

Authored tools: [complete candidates](../../tools/experiments/game_actor_definition_lookup_candidates.py),
[qualification and linked audit](../../tools/tests/test_game_actor_definition_lookup_match.py).

## Fresh Qualification

- 3,075 cases / 6,150 original/C guest executions match an independent ordered
  reference and every private byte/event. Reach all 24 retail words. Cover
  nullable archive/records, full-word indices, byte boundaries, high/negative
  word bits, multiplication/address wrap, live callback changes to the selected
  table and saved index, and both stack phases. Clobber caller GP/FPR; verify
  stack, return address and callee-saved registers; compare pointer V0.
- 664 cases / 1,328 executions cover aliases and the actual banked 11-word
  func_150849A0. Its selector byte +0x1C9 and list pointer +0x2C4 select byte
  zero for selector zero, otherwise byte selector-1. All ten reachable words
  execute; its unreachable word is not falsely counted as executed.
- 136 fired access-fault pairs / 272 failed runs retain strict prefix memory,
  events and calls. Eight additional unmapped incoming-home alias pairs / 16
  failed runs assert the actual failed header address and access ordinal.
  Missing or different failures reject; these are emitted guest fault gates,
  not portable C fault semantics.
- Eight independent original/C links at four entry/classifier/table rebases,
  including signed LO carry boundaries, pass 288 cases / 576 runs. No guards
  or relocation replacement are needed.
- Complete production-profile copied-owner compile/post-process/actual padder
  passes with zero diagnostics. All target bytes, all 14 neighbors, function
  extents, relocations and pools remain exactly equal using the old manifest.
- Five freshly compiled effective IDO negatives reject byte-narrowed index,
  eight-byte stride, wrong header offset, fixed classifier and adjacent table
  entry. Native stride/header negatives also fail as intended.
- Complete native32 C at O2/O0 passes 786,432 cases per profile, 1,572,864 runs:
  all 256 classifier bytes and valid byte indices, both nullable pointers and
  live table/header mutation plans. Compare the full actor, table and header;
  typed two-argument ABI and returned pointer qualify. This uses synthetic
  buffers, not a claim that all 256 classes exist in real assets.
- Execute actual banked 73-word func_1507E7E4 caller, both 24-word lookup forms
  and actual 11-word classifier together in 768 cases / 1,536 runs. An
  independently replayed reference accounts for nested frames and all private
  events. Both zero/nonzero descriptor paths are retained. Four null-definition
  runs confirm the caller's original read at address 4 fails identically;
  invent no compatibility guard. Other deeper callbacks remain bounded models.
- Inspect direct func_1507E500, func_1507E5C8 and func_1502F01C interfaces;
  their complete executions, real resources, hardware and live gameplay remain
  separate open gates. Earlier broad qualification receipts remain historical.

## Linked Audit And Progress

All nine final post-install tests pass in 21.222 seconds. Root tools-check and
older standalone tools check pass. Source-only rebuild has zero changed-owner
compiler diagnostics; existing duplicate generated_12D630 Makefile recipe
warnings remain, so do not describe the global build as warning-free.

Whole linked ELF is byte-for-byte identical, including all addresses, extents,
symbols, headers and sections: 3,261,160 bytes, SHA-256
bf999834941dc6804caa011978298b58687ee6e9512c4649a766a49d2c57ec91.
Guards, protected rodata, tracked symbol file and ignored assignments are also
byte-identical. Protected data: 189,088 bytes / 720 owners / zero differences,
SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Only one CSV row changes asm -> c, 96 bytes; all other rows and both repeated
section headers remain exact. CSV SHA-256
907b8c4fa3f34dda1cfbd5d9f780a9c0263bf14c8e9d52cdc845d0d4559f092f.
Installed source SHA-256
2a54f461df2ce9a06698ed139c686598a9832d775aef7b51a40e97bed8dd0080.

Fresh conversion: total 5,492/6,043 (90.88%), 1,940,812/2,256,728 bytes (86.00%);
Game 4,819/5,322 (90.55%), 1,769,376/2,072,880 bytes (85.36%). Init/debugger
and denominators unchanged. Delta +1 converted function / +96 C bytes.
Fresh matching: Game 2,769/4,819 (57.46%), total 3,442/5,492 (62.67%), zero
drift / 2,050 different. Delta +1 matching credit; different count unchanged.

```sh
python3 -m unittest tools.tests.test_game_actor_definition_lookup_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Bank mounted tools 6bc9c5a before consumer source/docs/tools pin, no push.
Root README receives aggregate rows only. Eight added relative links pass,
zero broken. Native graphify update after final authored code edits refuses
unsafe shrink 39,514 -> 17,741 nodes, retaining 19,398 nodes from 2,972
excluded-but-existing files. Preserve that refusal, skill 0.9.20/package 0.9.26
and devcontainer.json zero-node warnings without force/purge/install. The
consumer hook is separate: verify fresh log growth/completion and zero workers
before reporting a clean checkpoint.

## Next And Boundaries

Next: complete 32-word func_1507E968, still GLOBAL_ASM in the same owner.
VA 0x1507E968..0x1507E9E8, ROM 0xABE18..0xABE98, original 0x18 frame.
Preserve actor byte +4 special ID 150, conditional classifier call, ID 255
return-zero, live nullable archive table, unsigned header word -4 divided by
ten and return contract. Qualify its actual connection to the channel caller
separately; do not infer completion from the currently bounded count model.
Other callers/deeper callbacks, real assets and live runtime remain open.
Zero Claude calls; no billing invocation or goal-completion claim.
