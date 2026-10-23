# Masked Record Fields Direct C Match

Date: 2026-10-22. Predecessor consumer `eebfd7f5`, tools `a83687e`.
Qualification tools committed first as `ee347ee`.

## Recovery

Recover `func_150A3398` in `conker/src/game/generated_CDE80.c`:
VA `150A3398..150A3444`, ROM `D0848..D08F4`, 43 words / 172 bytes,
frame zero and four HI16/LO16 bindings to `D_800D3098`.
All words emit directly under the existing O2/g3 profile. No guards,
compiler-profile changes, shared-header changes or original-assembly edits.

Reuse the owner's existing `GeneratedCDE80Record`, size 0x34. The six-argument
void interface takes a signed index, unsigned 16-bit mask and four word-sized
values. Mask bits 1/2/4/8 independently select byte +0x17 and words
+0x18/+0x1C/+0x20. The first value is deliberately s32, not u8: assignment
provides the byte truncation. Its narrow-argument alternative emits 46 words
and fails raw matching; this is a shape control, not a functional negative
for ordinary defined inputs.

Retain the complete incoming mask home before truncation, the captured
normalized mask, repeated global-pointer loads after stores and late fifth/
sixth argument loads. Sparse large indices qualify emitted 32-bit address
arithmetic only, not portable C out-of-array indexing. The leaf's incidental
V0 mask lifetime is not a recovered C return-value contract.

Raw text SHA-256:
`1a386fb81ce4c3a1c28e6382dc9fd2f9e0e07ef2c1f8ac3aec1ebfd61eb43a15`.
Bindings are HI16/LO16 at +0x20/+0x24 and +0x38/+0x40.

## Caller Boundary

Aligned retail scanning finds exactly one JAL, ROM `CD910` / VA `150A0460`,
and no literal target pointers. Its parent is the unrecovered six-way
`func_150A03B0` dispatcher, 74 words/frame 0x28 in `asm/CD860.s`.

Execute the original parent entry, jump-table selection, selected mask-update
case and return in 108 phases. The nine-word setup/call window is
`150A0444..150A0468`, stopping before the branch at 0468. It takes index from
S1 and packet from S0; packet +A is an unsigned halfword, +C/+10 are full
register values, and +14/+18 become outgoing SP+10/+14. The second outgoing
store is the actual JAL delay slot. Verify all six arguments, both outgoing
homes, saved-register restoration and the parent's explicit zero result.

The other five dispatcher cases are not dynamically qualified here. Its
production twelve-byte stub remains unchanged and uncredited. No existing
C/header caller declaration needs correction. This does not establish full
dispatcher, helper, gameplay or host-port acceptance.

## Qualification

Each tools copy passes eight pre-install tests, then two fresh installed
checks. Explicitly reuse six unchanged behavioral checks only under exact
source, raw/padded object, helper, guard and whole-image identity.

- 1,280 ordinary guest phases: every low mask combination, full-word values,
  incoming mask high bits, signed/high indices and both stack phases.
  All 43 instruction words are visited; complete original/C machine states
  and independent final memories agree.
- 66,176 defined native32 cases per O0/O2/O3 build, including all 65,536 u16
  masks, valid negative/positive indices, byte truncation and word patterns.
  Trap UBSan passes. Assert the complete record layout and compare every byte
  of all seven records plus surrounding fences.
- Twelve effective wrong-C native controls are rejected: four wrong mask
  bits, four wrong values, unconditional byte write, any-nonzero-mask gate,
  backed next-index selection and an incorrect byte clamp.
- Nine independent GNU links cover original, C and padded C at three entry/
  global rebases, including HI16 carry boundaries; 96 rebase phases pass.
- 416 fired root-access fault prefixes match complete state, PC and delay
  identity. These qualify emitted guest order, not portable C fault semantics.
- 512 guest alias phases cover global byte/word/late-word pointer redirects,
  mask-home byte/word overlap and both late stack arguments. Compare against
  an independent ordered-memory reference. A compiled cached-pointer control
  is rejected by a changed destination value, not private-frame differences.
  Do not infer native private-stack/global-object alias legality.
- Seven strict whole-image corruptions/extent negatives are rejected; all
  27 historical input fingerprints and complete guard bytes remain checked.

The initial caller fixture accidentally shared the oracle stack address with
the ordinary record table. Review caught that exclusion gap before install.
Move the table to a disjoint address, assert separation, explicitly model the
parent's outgoing argument stores, expand the caller masks, and rerun all
eight tests in both copies. Only the strengthened run is final evidence.

## Owner And Image

Preserve all 27 neighboring functions, raw/padded pools, addresses and extents.
The owner retains two GLOBAL_ASM neighbors: run the actual five-command Make
recipe, including preprocessing/postprocessing, under its normal O2/g3 flags.
Isolated diagnostics are empty; owner diagnostics remain unchanged.

The independent full link and normal production Make agree byte for byte:
122 changed bytes, comprising 121 code bytes and one symbol-size byte.
No excluded metadata or other-byte normalization. The target's symbol size
advances from 12 to 172; the existing reserved slot and every address remain.

ELF SHA-256:
`6fd87e9c5431f2a0145609d0d9e9bc31038189fba802074b5e6770919dbdd24d`.
Owner object SHA-256:
`34c134c851f6d24f7d2dc52032b460a0bb61df55d6c522dcf9185c416ff3428a`.

Seal and verify 15,878 files, covering all 1,454 linker objects. Preserve
all other 6,054 bodies, all 6,055 addresses and all 720 protected Game-data
owners / 189,088 bytes. Protected-data SHA-256 remains
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Recheck every live static input and non-target object before/after adoption.
Only the owner object, ELF, linker script and progress CSV are promoted;
the last two remain byte-identical. The C source equals the qualified proposal.

Both copies pass shared tools checks. Preserve all 1,566 older-mirror dirty
paths and its HEAD, adding only the two identical target tool files. Commit
the primary tools before the consumer pin; no push.

## Handoff

Fresh standard matching against the adopted live ELF reports total
**3,746/5,505 (68.05%)**, Game **3,073/4,832 (63.60%)**,
Init 492/492 and Debugger 181/181 exact. Zero drift; 1,759 different.
The 75% threshold is still 4,129 exact, requiring **383 more matches**.
The refreshed queue has 1,628 placeholders, 122 semantic/other and nine
unlocated definitions. Next `func_150CE694` is queued only, unmodified and
uncredited. Keep the 862-word `func_1508CAD8` stub queued as well.

README changes only its two aggregate rows. Post-commit graph-worker and
every-old-node retention audits remain private receipts. Incremental retention
is not a fresh full-corpus extraction; retain the excluded-corpus and
large-HTML caveats. Host Release, saves and configuration stay untouched.
