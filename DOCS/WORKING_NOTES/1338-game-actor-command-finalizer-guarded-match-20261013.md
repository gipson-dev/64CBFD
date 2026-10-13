# Game Actor Command Finalizer Guarded Match

Date: 2026-10-13

## Scope And Baseline

Resume the full Game matching goal from consumer `24adbdc7`, tools `ce3980b`
and [Note 1337](1337-game-actor-command-finalizer-category-promotion-cache-provenance-20261013.md).
The consumer has no source edits; the tools checkout contains two interrupted
experiment helpers. Preserve the older tools mirror's HEAD `ddbdd16` and all
427 existing dirty-path fingerprints. No host changes, Release work or push.

Target [func_15034860](../../conker/src/game/generated_61D10.c):
VA `0x15034860..0x15034EB4`, ROM `0x61D10..0x62364`, 405 words / 1,620 bytes,
original frame `0x48`. The semantic C and compiler profile are unchanged.
Raw C still has **76 differences**. The source-derived guarded candidate
matches all 405 retail words; it is **not a direct C match**.

The installed ELF audit and fresh project-wide matcher pass. Game increases
from 2,823 to **2,824 / 4,823 (58.55%)**; total increases from 3,496 to
**3,497 / 5,496 (63.63%)**. There are zero address-drift blockers and 1,999
different converted functions. Conversion remains 5,496 / 6,044. The wider
Game goal remains active; eliminating guards is a future direct-source fit.

## Source Screens And Derivation

[Bias/home screens](../../tools/experiments/game_actor_command_finalizer_bias.py)
compile 15 complete bodies: six incoming-home qualifier forms and eight
shared-constant placements plus the baseline. No eligible improvement. The
retained 405-word/opening-exact forms are literally the original raw array;
other forms change the opening or length. No rejected body is installed.

[Derivation helper](../../tools/experiments/game_actor_command_finalizer_matching.py)
reads only the emitted source object. Its complete unrelocated text hash is
`cef29a96dfe1d477d242f6d6236c0e3e450976359dd1a3237e581c1cd32c0a09`.
All 25 target relocation entries must also match. Retail bytes are used for
independent comparison in tests, never to generate replacement instructions.

The 76 expected-word rows derive these bounded transformations, with zero-based
instruction indices:

- Opening words 14..29: place the independent 105 constant, cached category
  copy and limit-255 constant at their retail delay/join positions. Use the
  still-identical category value in the first noise equality predicate. All
  source branch destinations retain their corresponding blocks.
- Words 53..61: move the independent lower-40 definition ahead of the numeric
  conversion. The scale HI16 moves from byte `0xEC` to `0xF0`; its LO16 moves
  from `0xF0` to `0xF4`. Preserve the symbol and both addends, not linked addresses.
- Words 31/230/231: map the two incoming second-home definitions and joined use.
- Words 152/181/183/201/203: map four mutually exclusive primary velocity
  definitions and their final use. Exchange the final integer addition operands.
- Words 204/205, 215/216 and 225/227: map the bounded sum-extension, clamp and
  timer temporary lifetimes separately.
- Words 252..256, 257..276 and 281..295: map the secondary snapshot, scale-row
  scratch cycle and mutually exclusive default-velocity constants.
- Word 315: exchange the two operands of integer inequality.
- Words 345..397: map the closed secondary-tail scratch cycle.

Register transformations admit only a bijection within `v1`, `t3..t7`, `t8`
and `t9`. They do not change argument, saved, stack, return-address or FPR
fields. There is no inserted/deleted instruction, frame patch, changed memory
offset, copied retail body, arbitrary padding or compiler-profile change.
Unchanged source retains the full32 selectors, six real live slots, signed
velocity/halfword conversions, unsigned PRNG modulo and alias-sensitive reads.

## Qualification

[Focused suite](../../tools/tests/test_game_actor_command_finalizer_match.py)
passes **18 tests in 89.835 seconds before installation**. A first run exposed
an isolated-test manifest containing neighbor guards; the corrected test uses
target-only rows for isolated links and the complete manifest for owner checks.

- 15,288 guest cases check all category bytes, channel gates, field boundaries,
  signed halfwords, timers and opaque helper mutations. Guarded output has full
  modeled RAM/events/GPR/FPR/condition/HI/LO/call equality and identical visits.
  The raw C is separately checked for its public contract.
- Full-word selectors, output/actor/global overlaps, live provider-mutated slots,
  160 incoming-home aliases and the actual original 119-word parent are retained.
  Original parent execution still uses opaque lookup and PRNG providers.
- The actual C passes native32 O2/O0 qualification and effective signedness,
  modulo, alias, velocity, category-bound and clamp controls. These native
  tests do not make guest-only sparse/overlapping backing portable C.
- Owned compiler traces preserve normal/traced object identity, frame writes
  8 -> 24 -> 72, final locals/saved/outgoing 48/8/16 and all six physical slots.
- Both complete owner padders agree, preserve neighbors/pools, and emit the
  complete target with the derived relocation map. Three independently linked
  original/guarded layouts match every instruction; 480 rebase cases retain
  their contract across signed LO16 carries.
- All **2,938 fired fault pairs across 52 paths** match the complete modeled
  state and dispatched instruction, versus 1,598 raw-C agreements. No affine
  private-frame rebasing or observer-generated fault is used.
- Every one of 76 dropped guards breaks independently linked byte identity.
  Every stale expected word is rejected by both complete owner padders (152
  controls). All 76 corrupted source objects and 25 omitted relocations are
  rejected. Unknown opcodes and nonclosed/argument/saved-register cycles fail.

Literal instruction identity is checked across the complete slot, including
words not reached by these sampled executions. No live hardware/emulator,
actual PRNG implementation, arbitrary FP/FCSR or whole-gameplay acceptance is
claimed. Routine work uses zero Claude calls.

## Installed Audit And Banking

`make -C conker -j4 build/conker.us.elf progress.csv` completes successfully.
The guard-manifest dependency rebuilds existing owners and retains the existing
duplicate generated_12D630 recipe and legacy compiler warnings; this is not a
warning-free build. No ROM or host executable is built or launched.

The installed audit compares the **entire ELF** against the archived baseline
with only the 1,620-byte target slot replaced. Exactly **145 bytes differ**,
all within that slot. There is no symbol-size or metadata exclusion. All
189,088 Game data bytes and 720 owners remain exact, with SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The unchanged historical CSV bytes are followed by exactly 76 derived rows:
14,694 -> 14,770 total rows, no insertions or omissions.

| Input | Installed SHA-256 |
| --- | --- |
| Source, unchanged | `ce9efbb40671a56699d587183f31b9c72cfa835441af6809dfe729ad2d0402ee` |
| ELF | `38ac5d5272b5800ff666bb1d284ccfa12409f3a25fa06b38068cd9d337973561` |
| Guards | `cb084753c4a5b27cd425a8eddd4f906c457d4feeaf5a66e7ac0e987518550358` |
| Conversion CSV, unchanged | `14d100143c0654609b3cd7d97798dbeccd52551a77ad6b4ff1f826acde91482b` |

After the independent image proof, archive all nine current text-recovery
fixture inputs and its manifest under the ignored target test directory's
`text-before-rebase/`. Advance only the text fixture's ELF and guard pins;
the other seven protected inputs and all corruption gates remain unchanged.
Three freshly installed shape/image/guard tests pass in 1.981 seconds.
The complete installed target suite and two immutable text tests pass:
**20 tests in 117.798 seconds**. The retained source/ELF/guard corruption
controls still reject their real mutations. ROM-free wrapper checks pass in
both tools copies; Windows byte-compilation and scoped diff checks pass.
All ten newly added relative documentation links resolve.

Tools commit **c0ca061** banks the three completed helpers/tests and the
verified two-line protected text-pin update before the consumer pin. The older
mirror remains at `ddbdd16`: all 426 unrelated initial fingerprints are fixed,
the protected test changes only its two verified hashes, and three previously
absent files are added. Its original 427 dirty paths become 430; no history is
duplicated or reset. No push is performed.

`graphify update .` attempts AST-only extraction but returns status1: its
shrink guard rejects 18,698 proposed nodes against 40,469 existing nodes. The
existing graph is preserved; the separate retained-corpus diagnostic reports
19,398 nodes from 2,972 excluded files still on disk. Do not force a destructive
overwrite or claim a successful graph refresh. The skill/package mismatch
(0.9.20/0.9.26) remains a tooling warning, not a compiler failure.

## Next Function

Continue the full Game goal with `func_15034F30`, the next unmatched routine in
the same source slice. Its retail body is **486 words / 1,944 bytes**, VA
`0x15034F30..0x150356C8`, ROM `0x623E0..0x62B78`, frame **0x190**. Production
still contains a zero-return placeholder.

Initial assembly inspection identifies matrix operations, 64-byte matrix
iteration, mode-dependent paths and 16 helper call sites. Two original call
sites occur within `func_15035808`; recover their complete argument layout
before choosing a prototype. Next recover the full body with existing SDK
matrix helpers and qualify its callers, buffers, modes, frame and linked
extent. This inspection is not a conversion or matching claim.
