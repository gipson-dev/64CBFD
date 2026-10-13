# Game Actor Command Finalizer Secondary Value Register Restoration

Date: 2026-10-13

## Scope And Baseline

Continue `func_15034860`, VA `0x15034860`, ROM `0x61D10`, in
[generated_61D10.c](../../conker/src/game/generated_61D10.c). Consumer baseline
`6eac9ba2`, mounted tools `a71abb7`; both active trees initially clean.
[Note 1334](1334-game-actor-command-finalizer-tag-dependency-canonicalization-20261013.md)
leaves 405 words, the original 72-byte frame and 267 literal differences.
Preserve the complete source/ABI, first 14 words, jitter load words 81/82,
six live slots, caller homes and all previously exact sampled fault states.

The session restart is separately verified: live REA 6.4.0 identity aligns
with its configured path/version/catalog and Ghidra/Java checks pass. Windows
REA native admission is x86/x64 PE, not the N64/MIPS target. No REA target,
Claude advisory, host build, ROM replacement or OGL Release action is used here.

## Source Recovery

Retail secondary selection loads its signed halfword into `v0`. The banked C
instead reuses the primary clamp's `s32 current`, making the compiler retain
that role in `a0`. Replace only the secondary lookup and its comparisons with
the existing `s16 value` local. The loaded value is already signed 16-bit;
no input, selector or arithmetic is newly narrowed.

The compiled complete routine restores these physical secondary roles:

| Role | Before | Recovered / Retail |
| --- | --- | --- |
| Sign | a3 | a2 |
| Choose | a2 | a0 |
| Reverse | t0 | a3 |
| Secondary current value | a0 | v0 |

Extent stays **405 words / 1,620 bytes** and frame stays **0x48**. Literal
differences decrease **267 -> 266**. Fifty emitted words change, including
primary temporary allocation; this is not a one-word-only scheduling edit.
The secondary block remains four bytes early, so matching role instructions
at corresponding positions does not establish address or full-byte equality.

The six live homes remain reverse SP+18, sign SP+20, noise SP+24,
primaryBias SP+2C, upper SP+30 and lower SP+34. Owned, read-only compiler
observations retain frame writes 8 -> 24 -> 72, locals/saved/outgoing 48/8/16,
M definition 48 and offsets -48,-40,-36,-28,-24,-20. Normal/traced objects
remain identical. No compiler, profile, layout or guard change is made.

## Discriminating Screens

[Secondary screen](../../tools/experiments/game_actor_command_finalizer_secondary.py)
compiles 19 complete source bodies from the exact banked body. Moving a
default +1 before/after scale selection produces a **404-word** branch-likely
shape, not retail's 405-word sequence. Existing-local scale captures do not
repair it. The complete if/else sign shape remains installed.

The ternary sign form emits the banked word array. Inverted sign and reused
suppression forms both score 267 but change three and 19 words respectively;
equal scores are not literal identity. Reusing secondaryBias regresses the
restored opening. A primaryIndex lookup emits the same selected 266 array,
but the existing signed value local expresses the recovered load directly.
None of the shorter/default or opening-regression forms is installed.

## Qualification And Linked Audit

[Focused suite](../../tools/tests/test_game_actor_command_finalizer_secondary.py)
reuses the existing guest/native/owner/oracle helpers. Fresh qualification
includes 15,288 guest cases, 385 output/selector aliases, 80 live-slot cases
with 16 effective old-body failures, 160 incoming-home cases, 8,192 native32
O2/O0 cases and six fresh compiled negative controls. Nine owner neighbors,
relocations/pools/both padders, 480 independent carry-sensitive rebases and
200 actual 119-word parent cases remain qualified.

Across all 52 sampled paths and **2,938 actually fired fault pairs**, represented
exact states increase **1,086 -> 1,322**. Every previously exact cut remains
exact; no access count changes. First divergence remains primary cut10 on
44 paths and disabled-primary cut7 on eight paths. Hardware PC/BD/FCSR,
complete private RAM, actual PRNG and full gameplay are not proven.

All 14 pre-install checks are qualified: the first 13 pass in the 77.390s
run, followed by the corrected screen check in 13.243s. Initial fixture errors
(19-form count and a warning-producing negative) and an incorrect literal
equality assumption are corrected without changing production acceptance.
The installed whole-image check then passes in 2.076s: only **55 bytes**
inside this function's existing 1,620-byte ELF slot differ. All other ELF
bytes, metadata, protected inputs, progress and guards are exact. All
189,088 Game-data bytes / 720 owners remain exact, SHA256 `0bbc00e1...`.

Production source SHA256:
`b6b23e5b354ee79fb67f67aef212fffc3ca25d04855775f1f1ff7f76f1e2fa6f`.
Production ELF SHA256:
`c25a2f5ee0e9c056d10f79f83b8d1060a94948740a386e347103f5033b6d06c2`.
Guards SHA256:
`420eb4c5458868e6b19f5a7eb45f04b38ef96532216f283689eec7e0c5e8d796`.
No target guard or matching/conversion credit is added.

After the independent literal audit, archive the previous protected-text
manifest/ELF under the new ignored target test directory. Advance only its
ELF pin/readback; all eight other inputs stay fixed. Historical finalizer
fixtures remain unchanged. All **16 installed target/protected-text checks
pass in 77.702s**, no skips. Both local tool checks, Windows syntax checks
and scoped whitespace checks pass. Historical neighbor receipts outside this
target are reused only where the complete linked image proves no change.

## Bank And Next Work

Game remains 2,823 / 4,823 (58.53%), total 3,496 / 5,496 (63.61%); zero drift,
2,000 still different, converted 5,496 / 6,044. Root README already agrees
and is unchanged. Detailed narrative belongs here and in short docs indexes.

Mounted tools are committed first as `6217aa4`, followed by the exact consumer
source/docs/gitlink in the authorized bank. No push is requested/performed.
Older tools HEAD `ddbdd16b` and all 421 pre-existing dirty-path hashes are
preserved except the independently verified, task-owned protected-text ELF
pin edit. Add only two absent task files, bringing dirty paths to 423; do not
commit/reset/stash that checkout or push any repository.

Next: keep the recovered secondary roles and investigate the primary clamp's
branch orientation and register allocation, then the missing secondary-block
alignment word. Primary lower=40 cut10 and disabled-primary selector cut7
remain open. Retain all 1,322 exact sampled states, first 14/jitter words,
six homes and complete owner/image gates. Do not repeat the rejected default
sign forms, pad a shorter candidate into acceptance, or normalize unresolved
states with guards. Full Game, retained text/translator and hardware goals
remain active.
