# Random approach motion recovered as byte-exact guarded C

Verified 2026-11-01. `func_1511AF30` replaces its zero-return placeholder with
the complete command approach and filtered random-offset callback. All
**83 retail words match**, using eight checked FP register/operand guards.
Ordinary C supplies the original 32-byte frame, branches, calls and accesses;
there are no inserted/omitted words, volatile filler or compiler-profile changes.

Fresh production and independent Native actual-ELF recount report
**4,031/5,507 (73.20%)** total and **3,358/4,834 (69.47%)** Game, zero address
drift and 1,476 different. Init remains 492/492; Debugger remains 181/181.
Converted inventory remains 5,507/6,045, Game 4,834/5,324. The 75% threshold
is 4,131: **100 additional exact C functions are needed**.

## Routine and recovered behavior

- Source `conker/src/game/generated_142560.c`, owner `generated_142560`.
- Original `conker/asm/142560.s` remains unchanged.
- VA `0x1511AF30..0x1511B07C`; ROM `0x1483E0..0x14852C`.
- 332 bytes, 83 words, 32-byte frame, nine relocation bindings.
- Correct callback interface `void func_1511AF30(u8 *state)`.

The signed command word at`+0x3C` is converted to float before any call.
The target is 75 times that converted command times`D_800A3188`; it is compared
with phase`+0x7C`. When unequal, strict`fabsf(delta)<1.0f` snaps to target.
Otherwise a signed one-unit step approaches it. Offset`+0x80` is cleared to
positive zero in either unequal path.

When equal, `func_150ADA20` supplies a 32-bit random word. Its existing signed
return declaration is retained and an explicit`(u32)` cast selects unsigned
remainder by 1000. The resulting signed sample lies in 0..999. Samples strictly
below 500 update desired offset`+0x84` through sample*5*saved command*
`D_800A318C`*`D_800A3190`, rounded at each original multiplication.
The command's converted float survives the call in the original stack slot;
a helper mutation of command memory must not replace it.

Live offset`+0x80` then filters toward live desired offset`+0x84` using
`D_800A3194`. The final output at`+0` reloads phase`+0x7C` and offset`+0x80`.
The coefficients have original bits 3C23D70A,3B03126F,3C23D70A,3ECCCCCD
for 3188/318C/3190/3194 respectively. Their distinct accesses remain live.

## Compiler shape and eight derived guards

The initial if/assignment sign selection emits 82 words and 58 differences.
A ternary sign choice restores 83 words. Separate resting/adjustment locals
reduce differences to 10. Reversing the final commutative field-sum spelling
matches the retail field-load order, leaving eight differences.

Six words exchange F2 and F12 over the closed target/delta lifetime
`0x30..0x7C`. Neither FP color is live on entry to the region. The target and
delta reads, comparison, snap store and sign comparison are all transformed
consistently. These are caller-saved dead values after that region. Two more
words, at`0x9C/0x128`, restore the original floating-add operand order.
The transformation is derived from instruction fields, then checked against
the complete normalized payload. It does not read replacement instructions
from retail. All nine bindings and the complete raw payload are pinned.

Raw SHA-256:
`bc40fb0ac41265744b4e485e32d3043dbf887581927485ab8eca2748899dd40d`.

Corrupt payloads, missing bindings, stale expected words and repeated guard
installation reject. All predecessor guard CSV bytes remain intact; eight
rows append. The owner already enables intrinsic`fabsf`; its declaration/
pragma is reused rather than adding a duplicate intrinsic warning. No shared
header, Makefile, profile, guard history or other function is changed.
Early target-target zero probes are preserved as rejected semantic variants;
the selected source retains literal 0.0f.

## Runtime and original call interface

- **6,144 guest cases / 30,720 executions**, three symbol layouts, four
  coefficient/record aliases and two stack phases. Signed commands include
  both32-bit extremes, while delta cases cover equality, both one-unit
  directions, strict snapping and random threshold branches. Providers mutate
  command, phase, offsets and coefficients while clobbering caller-saved GPRs,
  FP registers and outgoing homes.
- All **82 reachable root words** execute. The duplicate zero initialization
  at`0x70` is unreachable after the preceding unconditional branch; it remains
  present and byte-exact in the complete 83-word slot.
- Original ASM, padded owner, actual Make and guarded isolated C agree in
  complete modeled states and access traces. Unguarded C agrees in public
  memory and preserved ABI state; its dead FP register contents differ.
- **65 access prefixes / 260 executions** agree across the four exact programs.
  These qualify guest instruction order; no raw-C fault-order claim is made.
- **1,024 connected cases / 5,120 executions** use the original 18-word
  random generator at`0x150ADA20`, ROM`0xDAED0`, pinned against baseline ELF.
  The corpus invokes it 448 times per program and reaches every helper word.
  Its complete 64-bit seed store at`D_800885B0` agrees with an independent seed
  transition. Coefficients are pinned against the original ELF as well.
- Both original JALR sites`0x15113EE8/0x15113FC0` execute their complete
  seven-/nine-word windows: **96 cases / 480 executions**, four ignored return
  poisons. The larger dispatcher is bounded, not fully emulated.
- The original **22-word installer** at`0x1509EBBC` installs row 52 of
  `D_80088C90`: callback`+0x38`, secondary zero`+0x78`, mode zero`+0x92`.
  All installer words execute. Census finds one aligned pointer at ROM
  `0x22D9C0`, VA`0x80088F00`, and no direct JAL/J to this root.
- Native O0/O2/O3 each pass **2,048 cases**, UBSan and full record canaries.
  Eight compiled controls are effective: wrong target scale, wrong snap
  threshold, wrong step sign, missing offset clear, signed remainder,
  inclusive random gate, lost command snapshot and cached resting offset.

Native globals are disjoint; aliases are guest-qualified. Full FCSR behavior,
arbitrary NaN payloads, hardware and gameplay acceptance are outside these tests.

## Owner, full image and production

All 83 raw/padded neighboring functions and normalized pools remain fixed;
owner warnings stay zero. The actual five-command Make recipe produces the
independently qualified object under the unchanged O2/g3/mips2/o32 profile.

Literal complete-ELF prediction matches first link and production at
**333 changed bytes**, with zero exclusions. It updates the target slot and
symbol extent 12->332, and predicts four closed GNU symbol/string ordering
groups involving the four newly referenced coefficients. Complete named
symbol definitions stay fixed. Every changed metadata byte is predicted;
text, all four symbol/string groups and unrelated-image corruption controls
reject. All 6,056 function addresses, 6,055 other bodies and 189,088 protected
Game bytes across 720 owners remain fixed. Production ELF SHA-256:
`78b75a647842e90bf3af632a8761064999a87791aee8e00bbddee5e1ed1b4eb1`.

Production Make, the 17,607 predecessor sealed inputs, six public tests per
copy before and after installation, both shared checks and independent Native
recount pass. Only source, owner object, guard CSV and ELF change. No dependent
object changes occur. Reusable modules are`game_random_approach_motion_match.py`,
`game_random_approach_motion_oracle.py` and`test_game_random_approach_motion_match.py`.
Existing mirror dirt is preserved; only these three identical owned files are added.

## Continuation

Self-contained evidence lives under
`conker/build/game-random-approach-motion-1511AF30-match/`: 1,050 frozen focused
inputs, 24 canonical artifacts, source screens, derived guard proof, original
RNG/caller tests and production/bank receipts. Historical archived checkpoints
require explicit restoration. This candidate is now adopted; early private
screen records remain historical and do not supersede BANKED_STATUS.

Next audit`func_15117DA4`, same owner, 102 words/frame48,
VA`0x15117DA4..0x15117F3C`, ROM`0x145254..0x1453EC`. Inspect its five-argument
position-transform interface, special actor/category replacement, captured
angles across sine/cosine calls, output/actor aliases and signed translation.
No next-target credit. Other private candidates remain uncredited. Commit
tools before the consumer pin; no push. Root README gets aggregate rows only.
The wider 75% goal remains active.
