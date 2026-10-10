# Object Phase-Updater Byte Match - 2026-10-10

## Scope And Baseline

Resume [Note 1208](1208-game-object-color-mode-helper-byte-match-20261010.md).
Target func_1502EAFC: VA 0x1502EAFC..0x1502EC34, ROM 0x5BFAC..0x5C0E4,
78 words / 312 bytes, leaf with no frame. Owner:
[generated_58F80.c](../../conker/src/game/generated_58F80.c).
Replace its false zero-return placeholder with complete void semantic C;
update the declaration and explicit u8-pointer cast at func_1502BD84's call.
That caller ignores the return value and remains byte-exact.

Consumer baseline 56f1c2a380c9b982af64f7c11a9a3538a70ef90f; mounted tools
9f71a62b9606e51149c53315bc571074a8c63213. Both start clean. A fresh scoped
baseline is saved under ignored conker/build/game-object-phase-update-match-test;
do not overwrite historical color, adapter or curve baselines. Single Codex
writer, zero Claude calls. No OGL, Release, saves, editor or push work.

## Recovered Semantics

Mode byte +0xA4 dispatches modes 2..7; 0, 1 and >7 are no-ops. The protected
table jtbl_80096F04 is at ROM 0x23B9C4. Its six target offsets from entry are
40, 40, 144, 96, 180, 256. Tick is signed word D_800BE9E4; rate, phase and
blend are bytes +0xA6, +0xA5 and +0xA7.

- Modes 2/3 subtract the low product from phase or store zero.
- Mode 4 stores phase plus the low product with byte wrapping.
- Mode 5 subtracts ten ticks from blend or clears mode, leaving blend intact
  on that clear path. It then falls through to a fresh tick/rate/phase read and
  the mode-4 phase increment. Char stores can alias the global tick.
- Mode 6 compares phase against signed low32(255 - product), stores the
  increment or 255, then changes mode to 7.
- Mode 7 subtracts the low product or clears mode, without clearing phase.

Unsigned multiplication/addition/subtraction explicitly implement wrapping
32-bit arithmetic; s32 conversion retains the original signed comparisons.
Do not replace these with undefined signed-overflow expressions, unsigned
comparisons, cached tick reads, or phase clears on the mode-clear paths.

## Compiler And Closed Layout

[Candidate driver](../../tools/experiments/game_object_phase_update_candidates.py)
measures fourteen complete forms/profiles. Selected O2/g3 emits 75 words /
300 bytes, no frame, zero diagnostics and 58 isolated-link differences.
O2 is the same; O1/g3 emits 94 words / 92 differences and O1 94 / 91.
Selected .rodata is 32 aligned bytes. Compiler/profile changes do not close
the retail schedule, so the complete selected semantic body is retained.

[Matching driver](../../tools/experiments/game_object_phase_update_matching.py)
certifies all 75 raw words and all twelve relocation sites before deriving
the output from compiled instructions. It does not read/copy the retail body.
The owner guards have 19 changed words and 56 unchanged dependencies; three
insertions, zero omissions and zero tail padding recover the 78-word extent.
The adjustment schedules two byte stores before returns with explicit delay
NOPs, separates the mode-6 255 constant producers, renames their closed
register lifetimes and shifts the entry no-op branch. It binds the jump table
directly to jtbl_80096F04_game with zero addend, preserving the original data.

The actual owner inserts six compact switch entries at .rodata+0x100. The
neighboring color table moves by 24 bytes to +0x118; total section growth is
32 bytes because of alignment padding. Every old target identity and pool
byte is preserved after relocating that 28-byte table. The matching driver
certifies the neighbor's full 148-word raw body and seven relocation sites,
then reuses the previously closed recipe. Only the existing color CSV row
at +0x24 changes its expected word from 0x8C2F0100 to 0x8C2F0118. Replacement
and direct protected-table relocation remain unchanged. This is not an exact
old-CSV byte-prefix claim. Future pool shifts require another explicit full
qualification, not a looser guard or a rewrite of the historical driver.

## Fresh Qualification

[Focused suite](../../tools/tests/test_game_object_phase_update_match.py): ten
tests pass before installation (37.551s) and after final installation (55.695s).

- 7,868 cases / 23,604 executions compare original, fitted and complete raw C:
  every mode, phase/rate boundaries, eleven tick corners, signed low products
  and object/global aliases spanning seven overlapping positions. Every one
  of the 78 retail words is reached. Original/fitted complete memory and ordered
  accesses agree; raw C public memory and access order agree with an independent
  reference. Mode-5 stores precede the fresh tick read.
- 168 access-fault prefixes / 336 executions compare complete memory and event
  prefixes. Every gate is verified; no portable C fault-semantics claim.
- Twelve independent links over four entry/table/tick symbol sets exercise
  signed LO16 carries; 64 mode/stack cases agree for all three bodies.
- All 37 copied-owner neighbors preserve bodies/relative relocations except
  the one certified raw color addend. Actual padded owner bytes outside the
  312-byte target are identical, including the full 600-byte color helper.
- Actual padder rejects all 75 stale word controls and twelve stale relocation
  controls. The closed recipe also rejects every stale raw word.
- Actual native32 complete-C fixture passes 720,896 mode/phase/rate/tick cases.
  Unsigned products preserve wrapping; no native big-endian alias claim.
- Five fresh complete compiled negative controls are effective: cached tick,
  unsigned comparison, wrong phase clear, missing fall-through and wrong
  mode-6 threshold. The cached-tick alias fixture changes a low tick byte.
- Actual banked 88-word func_1502BD84 connects to the installed 78-word helper:
  64 cases, fourteen verified helper entries, active/signal and state-5 early
  return gates. Other callbacks are bounded, not gameplay acceptance.
- Fresh adjacent renderer regression passes (7.314s): 64 independent-strip
  cases connect the banked 475-word renderer and 89-word adapter to the actual
  unchanged installed 150-word color helper. Graphics/cosine remain bounded.

Early fixture failures were corrected before qualification: GCC needed its
recognized fall-through comment, the negative cache case needed a low-byte
overlap, caller state 5 returns early, and the source installer needed to avoid
an extra declaration blank line. No failed run is counted as acceptance.

## Linked Audit And Bank

Fresh build/progress, match-progress and tools-check pass. Shared guard changes
trigger the normal wider rebuild. Existing duplicate generated_12D630 recipe,
legacy pointer/type, long-double and old assembler/compiler warnings remain;
target/copied owner compiles are clean, not the whole project warning-free.

Whole rebuilt ELF agrees with the fresh baseline after changing only the
312-byte target slot and symbol extent, with decoded symbol/string metadata
normalized. Every other linked function/data byte remains identical. Original
rodata assembly and conversion CSV are byte-identical. Guard history changes
only the one certified existing expected field and appends 75 target rows.
Protected data is exact: 189,088 bytes / 720 owners, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Source SHA-256 76b3d92a29b823e34c3a1e5a75cd0591bfc2fc8e87366ca6fd10d33a37d4deb5.
ELF SHA-256 a981316075394849f780e16a6f8e70647485a12ab7767ab52a56092d615eb058.

Fresh matcher: Game 2,752/4,816 (57.14%), total 3,425/5,489 (62.40%),
Init 492/492 and Debugger 181/181 exact. Zero drift / 2,064 different.
Converted counts/bytes stay unchanged because the placeholder counted as C.
Root README changes only the two aggregate match rows, not function narratives.

Bank tools 7ae085c6c68b250b0f9dc719b99f04b7a7fd2195 first, then consumer
source/guards/docs/aggregate rows/pin. Mirror only the three absent authored
files; older HEAD ddbdd16 and both independently dirty tracked fingerprints
remain unchanged. No older commit and no push. Verify the fresh consumer
post-commit hook separately, rather than relying on the preceding receipt.

Scoped validator passes: 31 documents / 4,129 relative links, zero broken links;
47 authored tools have exact older mirrors and AST parsing in both copies.
Older HEAD and both tracked-dirty fingerprints remain unchanged.

Manual graphify update exits 1, refusing a 39,292 to 17,511-node shrink;
retention keeps 19,398 nodes from 2,972 excluded-but-existing files. Existing
package/skill version and zero-node devcontainer.json warnings remain.
No force, purge, install or policy changes.

## Next: Two Slot Bytes

func_1502EEF4 remains a zero-return placeholder in this owner. Its complete
retail span is 74 words / 296 bytes, VA 0x1502EEF4..0x1502F01C,
ROM 0x5C3A4..0x5C4CC, frame 0x30 with s0..s5 and ra saved. Input is the slot
index, not an actor pointer. Recover a void typed declaration and preserve
the banked dispatcher call. Actor base is D_800CC2D0 + slot*0x32C.

Two iterations update bytes +0x6C/+0x6D. Skip values >=10 without calling
func_1502EE8C(slot,index). Otherwise interpret the returned low byte: zero
decrements a positive byte; one increments when the freshly reread byte <2;
other values store one. Keep callback-sensitive byte reloads and the two
distinct one-valued saved lifetimes. Finish with func_1507E3C0(actor), including
the retail repeated slot address calculation and complete saved-home order.
Qualify bounded slots, byte boundaries, real banked classifier connection,
hostile/mutating callbacks, frame/ABI, copied owner and whole linked audit.

Take a fresh baseline before this authorized neighbor change; retain the
historical receipts. Preserve the uninstalled curve handoff in
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
The wider Game matching goal stays active; this checkpoint is not completion.
