# Height-offset response recovered as byte-exact guarded C

Verified 2026-11-01. `func_1511617C` replaces its zero-return placeholder with
the complete height query, signed offset relaxation and halfword Y feedback.
All **86 retail words match**, with 27 checked words for private frame layout,
FP temporary allocation and one commutative add. No instructions are inserted
or omitted and the production compiler profile is unchanged.

Fresh production and independent Native actual-ELF recount report
**4,028/5,507 (73.14%)** total and **3,355/4,834 (69.40%)** Game, zero address
drift and 1,479 different. Init remains 492/492; Debugger remains 181/181.
Converted C inventory remains 5,507/6,045, Game 4,834/5,324. The 75%
threshold is 4,131: **103 additional exact C functions are needed**.

## Routine and recovered behavior

- Source `conker/src/game/generated_142560.c`; owner `generated_142560`.
- Original ASM `conker/asm/142560.s` remains unchanged.
- VA `0x1511617C..0x151162D4`; ROM `0x14362C..0x143784`.
- 344 bytes / 86 words, retail frame 40, seven relocation bindings.
- Interface `void func_1511617C(u8 *state)`; A0 is the state record pointer.

The routine captures the original signed Y halfword at `+0x12`, then calls
`func_1510F648` with the signed X/Y/Z coordinates converted to floats. The
o32 packet uses F12/F14 for X/Y and A2 for the third float. It stores the
returned height at `+0x7C`. If its distance from the live, post-helper Y
exceeds 200, the signed field at `+0x3C` is cleared.

When flag bit 4 at `+0x4F` is clear, the offset approaches zero using
`D_800A2FA8` (retail bits `0x3E4CCCCD`, approximately 0.2). Otherwise its
target is -20, or -40 when unsigned `D_800CC354 == 0x4B`, using
`D_800A2FAC` (`0x3E99999A`, approximately 0.3). Integer negation and
subtraction wrap before conversion to float, including INT_MIN. Each result
is truncated back to signed 32 bits. Height plus the resulting offset is
truncated and stored as a halfword Y; `+0x5C` receives the halfword change
from the original pre-query Y.

The source uses unsigned arithmetic followed by the target signed conversion
to express the original wrapping integer differences without signed-overflow
UB. The pre-query Y snapshot remains distinct from the live Y used by the
distance gate. Helper mutations must not be silently cached away.

## Compiler normalization

The selected semantic C already has 86 words and all retail branches and
memory operations. Its private frame is 32 bytes; retail uses 40. Four guards
enlarge the frame and adjust the incoming A0 save/reload offsets so that its
saved argument still names the entry home. RA and the saved Y retain their
retail offsets relative to the new frame. The raw and retail private stack
bytes are not claimed to be identical.

The remaining guards reconstruct FP allocation by following each definition
and live use through the ordinary branch, special branch and final Y update.
The versioned mapping handles reused FP registers rather than applying a
blanket register substitution. One final floating add exchanges its two
operands. Raw payload and relocation bindings are pinned before deriving all
27 rows; corrupted payloads, missing bindings or stale expected words reject.

Raw SHA-256:
`1acb45a8623cff04d963dc892a1c7a0d88c11764158857580ad7fe2a92a09f3a`.

Two changed FP destinations occur in LO16 loads. Those guards retain checked
`R_MIPS_LO16` bindings to the appropriate coefficient; linked addresses are
never hard-coded into the raw manifest. All predecessor manifest bytes are
retained and 27 rows are appended. The original intrinsic `fabsf` declaration
is local to this owner; no shared header or Makefile changes are used.

## Qualification

- **3,072 guest cases / 15,360 executions**, three symbol layouts, four
  global alias arrangements and two stack phases. Original ASM, padded owner,
  actual Make object and guarded isolated C have equal complete modeled states
  and traces. Unguarded C agrees on public memory and preserved ABI state;
  its private frame and caller-saved FP temporaries may differ.
- All **86 root words execute**. Cases cover both flags, unsigned type checks,
  the strict 200 boundary, wrapping integer extremes, truncation, signed
  halfword feedback and helper mutations of live Y, offset, flags, type and
  coefficients. Aliases put either coefficient on the returned-height field
  or the type halfword on the live Y field.
- **83 access prefixes / 332 executions** agree across the four exact
  programs. This is emitted guest instruction-order evidence; no portable C
  or unguarded-C fault-order equivalence is claimed.
- **1,024 connected cases / 5,120 executions** run the complete original
  54-word `func_1510F648`, pinned against ROM and the baseline ELF. All 54
  words execute, including success/fallback branches, correct FP packets and
  private output-pointer lifetimes. Its four query subservices remain bounded
  providers; this does not establish complete world-query behavior.
- Both original JALR callback sites at `0x15113EE8/0x15113FC0` run their
  complete seven-/nine-word windows: **96 cases / 480 executions**, including
  four result-register poisons. S0 is passed as A0 and the result is ignored.
- The original **22-word installer** at `0x1509EBBC` installs row 51 of
  `D_80088C90` at record `+0x38`, with the original zero secondary callback
  and mode. Census finds one aligned pointer at ROM `0x22D9B4`, VA
  `0x80088EF4`, and no direct JAL/J to this root.
- Native C passes **2,048 cases per profile** at `-O0/-O2/-O3`, using 32-bit
  SSE, disabled contraction, UBSan traps and full record canaries. Eight
  compiled controls are effective: cached live Y, inclusive 200 gate, wrong
  damping coefficient, wrong unsigned type, wrong flag, wrong target speed,
  lost pre-call feedback snapshot and wrong helper Z.

Native casts stay within signed-32 range and globals are disjoint. Invalid
float conversions and global aliases are guest-model checks only. Full FCSR,
arbitrary NaN payloads, the complete larger dispatcher and hardware/gameplay
acceptance are outside this qualification.

## Owner, complete image and production

All 83 other raw/padded functions and normalized pools remain fixed. Owner
warnings are zero before and after. The actual five-command Make recipe
produces exactly the independently qualified object with ordinary O2/g3.

The literal entire-ELF predictor changes the root slot and symbol size from
12 to 344 bytes. New coefficient references also rotate the closed group
`D_800A2FA8 / D_800907A8 / func_15112520` left and swap
`D_800A2FAC / D_800907AC` in GNU symbol/string serialization. Both groups are
reconstructed entirely from pinned baseline bytes, retaining every definition
and metadata field. No regions are excluded from comparison.

First link and production match the prediction at **323 changed bytes**.
All 6,056 function addresses, 6,055 other function bodies and 189,088 protected
Game bytes across 720 owners remain fixed. Production ELF SHA-256:
`2efb08f7b5e074126e40815fe101d5297eaa5f4e6e5a0519079f6b7df1d22fd8`.

Production Make, all 17,586 predecessor sealed inputs, six public tests per
tools copy before and after adoption, both shared tool checks and the fresh
Native recount pass. Only source, its object, guards and ELF change; no
dependent objects change. Tools modules are `game_height_offset_response_match.py`,
`game_height_offset_response_oracle.py` and
`test_game_height_offset_response_match.py`. Preserve the older tools mirror's
existing dirty work; only these three identical new modules are added there.

## Continuation

Evidence is self-contained under
`conker/build/game-height-offset-response-1511617C-match/`, with 1,036 focused
inputs, 24 canonical prepared artifacts, original-helper and caller checks,
guard derivation, installed audits and bank receipts. Early screens retain
the 85-word shared-Y form and unsuccessful array/volatile forms. The correct
86-word shape reads the query Y from the record separately from its saved
feedback snapshot. The first link exposed the two closed metadata groups;
the native negative fixture needed its intentionally unused saved-Y local
removed under Werror. None changed the selected candidate during qualification.

Next audit `func_151163C0`, an 83-word placeholder in the same owner. Inspect
its packed component extraction, helper call and output deltas before
conversion. Other private candidates remain uncredited. Commit tools before
the consumer pin; no push. Root README contains aggregate rows only. The
wider 75% goal remains active.
