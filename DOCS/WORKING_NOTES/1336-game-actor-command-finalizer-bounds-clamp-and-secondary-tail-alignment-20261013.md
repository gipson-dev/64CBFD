# Game Actor Command Finalizer Bounds, Clamp And Secondary Tail Alignment

Date: 2026-10-13

## Scope And Baseline

Continue `func_15034860`, VA `0x15034860`, ROM `0x61D10`, in
[generated_61D10.c](../../conker/src/game/generated_61D10.c). Consumer baseline
`742c9d42`, mounted tools `6217aa4`, both active checkouts clean. The
[previous checkpoint](1335-game-actor-command-finalizer-secondary-value-register-restoration-20261013.md)
retains 405 words, original frame 0x48, 266 differences and 1,322 exact sampled
states. Preserve its secondary a2/a0/a3/v0 roles, opening/jitter words, all
six live slots, full-width selectors, caller homes and every earlier exact cut.
No REA target, Claude call, compiler installation, ROM replacement or host
build/Release action is used for this source-matching pass.

## Recovered Source Shapes

[Candidate screen](../../tools/experiments/game_actor_command_finalizer_clamp.py)
first tests primary clamp orientation. `value >= 256 ? limit : value` restores
retail's branch direction but leaves 266 literal differences: source and retail
blocks are still displaced. Instruction-shape comparison locates the missing
branch before the clamp, in category-specific bounds setup.

Replace the default upper=60 followed by one conditional arm with explicit
category arms: category 0x42 sets lower=80/upper=120; the other arm sets upper=60.
This restores retail's ordinary conditional branch, its nop delay slot and
the unconditional branch carrying upper=120 in its delay slot. It correctly
aligns the secondary block, but initially gives 406 words / 112 differences.
The sole extra structural instruction is a `move v1,v0` near the secondary tail.

Express the secondary velocity directly as the signed byte at actor+0x209 in
the halfword update and the two sign-crossing predicates. IDO retains the
velocity in v1 and eliminates that copy without adding memory accesses. The
halfword at actor+0x204 and velocity byte at actor+0x209 are disjoint; the update
does not change the byte subsequently referenced by those predicates.
Native32 O2/O0 and original-instruction alias/write-order tests qualify this
source shape, not a portable C fault-sequence claim.

The installed result is **405 words / 1,620 bytes**, original **0x48 frame**,
and **266 -> 76 literal differences**. All four primary clamp words 210..213
are now byte-exact at their original addresses; the secondary block is aligned.
Retail secondary roles remain intact. There are 237 changed emitted words,
not only the three source constructs or a single scheduling edit.

All six physical live slots remain reverse SP+18, sign SP+20, noise SP+24,
primaryBias SP+2C, upper SP+30, lower SP+34. Owned read-only compiler traces
retain frame writes 8 -> 24 -> 72, locals/saved/outgoing 48/8/16, M definition
48 and offsets -48,-40,-36,-28,-24,-20, with normal/traced object identity.
No guard, compiler profile, ABI or layout change is made.

## Rejected Alternatives

The screen contains 25 complete bodies. Default-value/default-limit clamps
produce 404 words. Explicit bounds alone produce 406; renaming the cached
tail velocity does not remove the extra instruction. Reusing secondaryBias
regresses the restored opening. Noise-assignment placement variants do not
reduce the 76 score or improve the exact sampled-state count.

An early-lower variant scores **70**, but still changes primary cut9's GPR7
and FPR16. It has the same aggregate 1,598 exact states as the selected body
while losing earlier exact cuts. Reject it: a lower difference count or equal
state total does not establish monotonic fidelity. Do not pad 404/406 bodies
or normalize unresolved states to gain matching credit.

## Qualification And Installed Image

[Focused suite](../../tools/tests/test_game_actor_command_finalizer_clamp.py)
reuses the existing guest/native32/frame/owner/relocation/alias oracles. All
**15 pre-install tests pass in 69.287s**, no skips. An initially overstrict
temporary-register equality assertion and an inherited historical screen
fixture are corrected before installation; neither remaining register-word
difference is hidden or counted as exact.

Fresh coverage includes 15,288 guest cases, 385 full-width/output aliases,
80 live-slot cases with 16 effective old-body failures, 160 incoming-home
cases, 8,192 native32 O2/O0 cases, six original effective negative controls
and three new signed-velocity/category-bound/clamp controls. Nine owner
neighbors, relocations/pools/both padders, 480 independent carry-sensitive
rebases and 200 actual 119-word parent cases remain qualified.

Across **52 paths / 2,938 actually fired fault pairs**, represented exact states
increase **1,322 -> 1,598**, with every previously exact cut preserved and
all access counts unchanged. First divergence remains primary cut10 on 44
paths and disabled-primary cut7 on eight paths. Hardware PC/BD/FCSR, complete
private RAM, actual PRNG and full gameplay remain unproven.

Rebuild only the linked ELF and progress. The installed literal whole-image
check passes in 2.046s: only **792 bytes inside the existing 1,620-byte target
slot** change; every other ELF byte, metadata and protected input is exact.
All **189,088 Game-data bytes / 720 owners** stay exact, SHA256 `0bbc00e1...`.
Progress, guards, layouts, caller and pool source remain fixed.

Source SHA256:
`ce9efbb40671a56699d587183f31b9c72cfa835441af6809dfe729ad2d0402ee`.
ELF SHA256:
`687cfa25054d239a1a081d23b91b1e199ecf1b595972824cfc32df751319d6e2`.
Guards SHA256:
`420eb4c5458868e6b19f5a7eb45f04b38ef96532216f283689eec7e0c5e8d796`.

Archive the previous protected-text baseline under this new ignored test
directory, then advance only its ELF pin/readback after the independent audit;
the other eight protected inputs stay fixed. Historical finalizer fixtures
are not rebased. All **17 installed target/protected-text checks pass in
63.247s**, no skips. Both local tools/syntax checks and scoped whitespace
checks pass. Unchanged historical neighbors outside this target retain their
prior receipts, supported by the complete target-only linked-image audit.

## Bank And Next Work

Game remains 2,823 / 4,823 (58.53%), total 3,496 / 5,496 (63.61%); zero address
drift, 2,000 still different, converted 5,496 / 6,044. Root README is unchanged
because its date/aggregate tables already agree. No matching/conversion credit
is awarded to a non-matching body.

Tools `56a0cee` are banked before consumer source/docs/gitlink, with no push.
Older tools HEAD
`ddbdd16b` and all 423 pre-existing dirty-path fingerprints are preserved except
the independently verified task-owned protected ELF-pin update. Add only the
two absent task files, bringing dirty paths to 425; do not commit/reset/stash
the older checkout.

Next: the remaining **76 literal word differences**. Structural differences
are confined to category/noise constant-and-copy ordering at offsets 0x38..0x78
and primary lower=40 scheduling at 0xD4..0xF8; other differing words still need
literal register/operand-allocation investigation, not masking as exact.
Recover scalar promotion/lifetime and independent scheduling while preserving
all 1,598 exact states, first14/jitter words, six slots and the now-aligned
clamp/secondary blocks. Primary cut10 and disabled-primary cut7 remain open.
Full Game, retained text/translator and hardware goals remain active.

Post-bank consumer `11742aef` / tools `56a0cee`: five extent/image/fault/
protected-text integrity checks pass **9.292s**, no skips. Seven documents /
4,660 relative links have zero broken targets. The source commit's graph hook
finishes with 40,460 nodes / 80,955 edges and zero live workers; known retained-
node/HTML-size warnings remain. Both active checkouts are clean. This note-only
verification leaves source/ELF/guards/totals unchanged; the 70-score control is
not promoted.
