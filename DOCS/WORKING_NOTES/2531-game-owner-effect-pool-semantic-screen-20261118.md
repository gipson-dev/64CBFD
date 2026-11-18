# Owner effect pool semantic screen - 2026-11-18

## Status: recovered behavior, exact match still pending

`func_151B0B88` has a complete, tested C draft. It is **not installed** in the
decomp source and earns **zero new matching credit**. The packaged draft emits
**389 words / 1,556 bytes** with the original **0x138-byte frame**; retail is
**385 words / 1,540 bytes**. Its current positional comparison still reports
361 differing words including the four excess words. This is a control-flow,
allocation and scheduling problem, not four independent words left to patch.
No guards, frame padding, inserted retail words or production objects are added.

The accepted checkpoint stays **4,542 / 5,514 (82.37%)**, Game **3,869 / 4,841
(79.92%)**, zero drift and 972 different converted functions. **145 further
matches** are needed for the active 85% goal. Root README remains unchanged.

Source owner: `conker/src/game/generated_1DD500.c`. Original assembly:
`conker/asm/1DD500.s:774`. VA `0x151B0B88..0x151B118C`, ROM
`0x1DE038..0x1DE63C`. Baseline consumer `85894cbf88a615c9a60d29fe311607d367afc282`,
tools `f52d9c4ff41d6e084bae298c43591a69ded73f78`. Original O2/g3/MIPS2/o32
profile, source placeholder, all existing guard bytes and the production image
remain unchanged.

## Recovered interface and access widths

The callback interface is `void func_151B0B88(u8 *record)`. Its state starts at
record+0x28 and matches the preceding constructor's 152-byte payload:

| State offset | Content |
| --- | --- |
| 0x00 | Owner pointer |
| 0x04 | Saved owner identity byte |
| 0x08 | Signed live-child count |
| 0x0C..0x8F | Eleven 12-byte slots: child pointer, signed ticks, next pointer |
| 0x90 | Floating accumulator |
| 0x94 | Selector byte |

The initial gate reads the **word at owner+0**, not a null-owner-pointer test.
The pointer itself must be valid for this routine's nonfaulting contract.
It then compares the saved identity byte with owner+0x3B. Failure sets the
**signed halfword** at record+0x0E to -1. The alternate-source draft's word
accesses at byte/halfword fields are rejected; none of it is adopted wholesale.

If the identity is valid, owner+0x1D4 must be nonnull and the low nibble of
owner+0x74 must differ from 15. Otherwise, a nonzero live count invokes the
existing cleanup callback `func_151B1918(record)`.

## Eleven-slot update and free-list construction

Each active child copies the three raw position words at +0x34 into its
previous position at +0x40. For each index, the 16-byte point record comes from
`D_800AA1DC` when the current owner's identity at +4 is 0x36, or `D_800AA12C`
otherwise. Its first byte selects a 64-byte matrix; the three floats at +4
are transformed into the child's current position. Owner and child pointers
are reloaded at the observed boundaries.

The slot's tick subtraction wraps in 32 bits and is tested as signed.
Only a **negative** result expires the child; zero remains active. Expiry
sets velocity+4 to positive zero and fills planar velocity from the position
delta times the live `D_800BE9A8`. It then calls
`func_1513F680(child,16,27,0,16)`, reloads the child, sets its +0x58 flag bit0,
clears the slot and decrements the live count. A helper may retarget the slot
before that reload; the screen checks this boundary explicitly.

Empty/expired slots are linked in reverse scan order. The first free slot is
the tail, the last becomes the head. A zero free count exits before RNG.
Otherwise the accumulator adds the ordered single-precision product
`rng_float * D_800AA2E0 * D_800AA2E4 * D_800BE9A4`. Retail values of the first
two coefficients are 307 and about 0.001. Replenishment requires accumulator
**strictly greater than 1.0f**, then closes the circular list.

## Replacement request and retained payload

The common 88-byte allocation descriptor initializes 67 bytes. Its kind is
`D_800AB310[selector]`, mode 0x1001, duration `rng_u32 % 51 + 52`, flags/value 0,
RGB 0/alpha255, scale(1,1,1), allocation flags0 and two zero floats. Selector
and a random low bit are captured into a separate 40-byte payload. That
payload also carries floats5,25,2,8 and two zero bytes.

Each attempt advances through the circular free list by `rng_u32 % freeCount`.
It derives the slot index from its 12-byte stride and always uses the normal
`D_800AA12C` point table for new children, even if the earlier update used the
alternate table. Two descriptor bytes use unsigned remainders modulo 101 plus
100/155; two payload bytes use modulo 5 plus 4. Another float is
`(rng_float * 506 + D_800AA2E8) * D_800AA2EC`, with retail constants -703 and
about 0.001. Transformed position is copied into descriptor previous position.
The otherwise unused RNG call immediately before allocation remains present.

The nine arguments to `func_1513D524` are descriptor,17,0,0,16,2,40,
**record+0x0C byte**, **record+1 byte promoted to a word**. Success copies the
40-byte payload to child+0x110, sets ticks to `rng_u32 % 31 + 20`, removes the
selected free node, decrements availability and increments the live count.
Failure retains the free node. Both outcomes subtract one from the
accumulator; iteration continues only while it exceeds 1 and free nodes remain.

The payload's first 12 and final 2 bytes are unwritten. The descriptor has 21
unwritten bytes. Native/semantic comparisons credit **26 payload bytes** and
**67 descriptor bytes**, and exclude those holes. Their complete literal
stack-byte relation is still an adoption gate. No blanket initialization is
added, and this screen does not claim portable values for uninitialized bytes.

## Fresh evidence and limits

Seven maintained files under `tools/experiments/game_owner_pool_update_151b0b88*`
and `tools/tests/*owner_pool_update_151b0b88*` preserve the draft and its screen.
Both final configurations pass **four fresh tests**, without skips/errors:
**78.882s primary / 85.579s private sibling overlay**.
Both record 314 observed imported tool files with exact fingerprints.

After those runs, one whitespace-only blank line was normalized in the native
Python runner. Its parsed AST and compiled Python bytecode are identical;
generated native sources and fixtures are unchanged. Original execution
fingerprints remain intact, with separate final artifact hashes and an explicit
whitespace-equivalence receipt. The unchanged checks are reused on that basis.

- Complete owner compilation preserves all **15 compact neighbors** and
  normalized pools. The draft's raw bytes and relocation identities are pinned.
- Original and draft each pass **179 guest cases**, with ordered helper calls,
  all arguments and defined descriptor/payload observations. Fixtures cover
  owner rejection, matrix/flags gates, each slot's expiry, mixed/full/empty
  pools, zero and signed tick boundaries, wrapping subtraction, accumulator
  boundaries, allocator success/failure and four helper-mutation bits.
- Original target coverage is **380 / 385 words**. The five uncovered words
  are the division-by-zero `break 7` checks: availability is gated positive,
  and the other divisors are constants 101/5. All **11 original memcpy words**
  execute. Raw target coverage is 384/389 with the same five unreachable checks.
- Native32 compiles the actual draft at **O0/O2/O3**, each passing 179 cases with
  strict aliasing and UBSan traps. Eight effective negative variants reject
  the owner-word/null-pointer substitution, misaligned identity word load,
  zero-expiry boundary, ten-slot scan, inclusive accumulator threshold,
  wrong duration modulus, short copy and selector reload. Only the width
  negative accepts the specifically observed SIGILL from a UBSan trap; other
  negatives require the controlled failure exit, not an arbitrary crash.
- The real table word at **ROM0x22EFF4 / VA0x8008A534**, entry19 of
  `D_8008A4E8`, equals this callback. The complete original **45-word
  func_15149264 dispatcher** is byte-verified against the frozen ELF and ROM
  and connected to each stream for **537 cases**. The selected entry/countdown
  and lifetime paths cover 38 caller words. Other table modes and destructor
  callback paths are not qualified; the final free provider remains modeled.
- A separate fresh **179-case check per stream** verifies explicit SP/RA,
  preserved GPRs and FPRs. This is bounded ABI evidence, not an induction proof.

Classification, transformation, RNG, allocation, cleanup and free remain
modeled providers. The original memcpy executes in the guest. No hardware,
whole-game runtime, full alias contract or complete arbitrary-path proof is
claimed. No new source match is inferred from these bounded cases.

The baseline freezes **1,643 inputs**, using 1,627 links to immutable snapshots
and 16 copies, with zero links to live files. Every frozen live input is
unchanged. The production ELF remains
`d3caaa0bd472f25769a9ea5f9de1fcd23cdd35cf5c25aa1ae78344fc0159fe4b`; a fresh production match-progress count
and tools-check pass. The sibling's 2,434 dirty paths and 343 previously scoped
dependencies are preserved. The private overlay contains 339 exact sibling
files, 351 fingerprinted primary fallbacks and seven task files. It never
overwrites the actual sibling. Host Release and saves are untouched.

Native Graphify update refuses its reduced scan without overwriting the
existing graph. Scoped AST merging of five Python files retains all 65,450
prior IDs and adds an explicit semantic-screen target reference; it is not
full-corpus extraction. Commit tools first, then this note/indexes and the
consumer pin. The main README receives no function narrative or count change.

## Next matching work

1. Resume from the packaged 389-word draft and `byte-pre-shape.json` under
   `conker/build/game-next-151b0b88-private/`. Keep the current four-test screen
   as the behavior gate while changing source shape.
2. Recover the retail inner countdown loop. The current form unrolls four
   links; the retail block at 0x151B0F1C..0x151B0F50 retains a post-decrement
   snapshot and a single traversal body. Straight post-decrement alternatives
   emit 374/376 words, so changing just the loop is insufficient.
3. Recover first-pass pointer reloads, category/table address lifetimes and
   the explicit continuation temporary. The retail zero at 0x151B1090 and
   counter snapshot at 0x151B0F40 are concrete lifetime clues. Preserve real
   object extents; add no synthetic padding or retained instruction blocks.
4. Reach 385 words/frame 0x138, then prove the private byte/address relation and
   complete loops/branches independently. Add only independently derived,
   guarded normalization if still required. Qualify both padders and rebases.
5. Run the independent complete-image prediction, actual production Make,
   linked/protected-data audit, installed-source/caller checks, actual ELF
   recount and paired tools gates before any adoption or progress credit.

The 85% goal stays active. This checkpoint banks reusable investigation and
validation, while `func_151B0B88` remains unfinished in production.
