# Packed cosine motion recovered as byte-exact guarded C

Verified 2026-11-01. `func_151163C0` replaces its zero-return placeholder
with the complete packed cosine motion callback. All **83 retail words match**
with six checked dead-temporary and independent-store guards. The natural C
already has the retail 48-byte frame, all calls, arithmetic and branches;
no profile changes, inserted/omitted words or volatile filler are used.

Fresh production and independent Native actual-ELF recount report
**4,029/5,507 (73.16%)** total and **3,356/4,834 (69.42%)** Game, zero address
drift and 1,478 different. Init stays 492/492; Debugger stays 181/181.
Converted C inventory remains 5,507/6,045, Game 4,834/5,324. The 75%
threshold is 4,131: **102 additional exact C functions are needed**.

## Routine, data and capture lifetimes

- Source `conker/src/game/generated_142560.c`; owner `generated_142560`.
- Original ASM `conker/asm/142560.s` remains unchanged.
- VA `0x151163C0..0x1511650C`; ROM `0x143870..0x1439BC`.
- 332 bytes / 83 words, 48-byte frame, eight relocation bindings.
- Correct interface `void func_151163C0(u8 *state)`; A0 is the state record.

Four bytes of the signed packed word at `+0x3C` are captured before either
cosine call. Bits 0..7 supply the first amplitude. Bits 8..15, converted
through the original unsigned-to-float shape and multiplied by 1.40625,
supply the angle amplitude. Bits 16..23 and 24..31 supply the two unsigned
phase increments. The previous signed Y at `+0x12` and float angle at `+0`
are also captured before the calls.

The first cosine receives signed phase `+0x7C` converted to float and scaled
by `D_800A2FB0`; its result times the first amplitude is stored at `+0x18`.
The second receives the live post-call phase `+0x80` scaled by
`D_800A2FB4`; its result times the captured angle amplitude is stored at `+0`.
Both retail coefficients have bits `0x38C90FDB`, approximately `2*pi/65536`.
They remain distinct loads: the second coefficient is read after the first
output store.

Both phase bases are read after the cosine calls. Each phase advances by its
captured byte increment times the live tick word, with unsigned 32-bit wrap.
The tick word is read again after the first phase store. This matters when
the global aliases that phase field. Y delta at `+0x5C` subtracts the saved
pre-call Y from live Y; angle delta at `+0x60` subtracts the saved angle from
the new angle. The real cosine helper leaves Y unchanged; provider mutations
separately qualify the retained snapshot rather than simplifying the store.

## Compiler shape and six guards

An explicit packed temporary allowed IDO to keep the packed integer across
calls and defer conversions, producing a 56-byte frame. Direct field captures
restore the 48-byte frame. Ordering the two phase-step captures between the
first amplitude and the angle-amplitude conversion yields 83 words and only
six differences. The selected source uses ordinary locals throughout.

The guard derivation changes the first amplitude's dead integer temporary,
then the first phase-step temporary after that amplitude has moved to FP.
The two independent stack stores at `SP+0x28` and `SP+0x2C` exchange slots.
Their addresses and values are unchanged. Guards do not alter arithmetic,
branches, call locations, relocations or any later memory operation.

Raw SHA-256:
`21fa35697d8e80ff339c60af33cd9cc14d3fcec9c8941dc8268da4c54521cd35`.

The raw payload and eight bindings are pinned before independently deriving
the six rows. Corrupted payloads, missing bindings or stale expected words
reject. All predecessor guard-manifest bytes are retained; six rows append.

## Runtime and original caller qualification

- **6,144 guest cases / 30,720 executions** at three symbol layouts, four
  global alias arrangements and two stack phases. All 256 values of every
  packed byte are covered. Helper effects mutate packed data, phases, Y,
  angle, coefficients and ticks while clobbering caller-saved registers and
  outgoing homes. Captured bytes and previous values survive both calls.
- Original ASM, padded owner, actual Make and guarded isolated C have equal
  complete modeled states and traces. Unguarded C has equal public memory and
  preserved ABI state, allowing different dead temporaries and store order.
- All **80 reachable root words** execute. The three unsigned-conversion
  correction words at `0x4C/0x50/0x54` are unreachable after the byte mask,
  but remain present and byte-exact in the full 83-word slot.
- **140 access prefixes / 560 executions** agree across the four exact
  programs. These are guest instruction-order checks; unguarded-C and portable
  C fault-order equivalence are not claimed.
- **1,024 connected cases / 5,120 executions** run the original 88-word
  cosine slot, pinned against ROM and the baseline ELF with its original
  constants. The slot contains an 85-word body and three alignment words;
  this finite corpus reaches 74 body words and agrees with an independent
  cosine polynomial reference. It does not claim all cosine branches, full
  FCSR behavior or arbitrary NaN payloads.
- Both original JALR sites at `0x15113EE8/0x15113FC0` run their complete
  seven-/nine-word windows: **96 cases / 480 executions**, with four result
  poisons. S0 is passed as A0 and the result is ignored.
- The original **22-word installer** at `0x1509EBBC` installs row 59 of
  `D_80088C90`, with callback at `+0x38`, zero secondary callback at `+0x78`
  and mode byte zero at `+0x92`. Census finds one aligned pointer at ROM
  `0x22DA14`, VA `0x80088F54`, and no direct JAL/J to this root.
- Native C passes **2,048 cases per profile** at `-O0/-O2/-O3`, using
  32-bit SSE, disabled contraction, UBSan and full record canaries. Eight
  compiled controls are effective: wrong first byte, signed angle byte, wrong
  angle scale, wrong second phase, entry-cached ticks, wrong first step, lost
  Y snapshot and lost angle snapshot.

Native globals are disjoint; global aliases are guest-qualified. Complete
larger-dispatcher execution and hardware/gameplay acceptance remain outside
the bounded tests.

## Owner, complete image and production

All 83 other raw/padded functions and normalized pools stay fixed. Owner
warnings remain zero. The actual five-command Make recipe produces exactly
the independently qualified object under ordinary O2/g3/mips2/o32.

The independent literal entire-ELF prediction changes only the target slot
and symbol size, 12 to 332 bytes. First link and production match at
**252 changed bytes**, with zero exclusions or metadata serialization
exceptions. All 6,056 addresses, 6,055 other function bodies and 189,088
protected Game bytes across 720 owners remain fixed. Production ELF SHA-256:
`129eb8fb267665051c47daae2a7448a42f01513487c573b48da7b11593b1bb78`.

Production Make, all 17,593 predecessor sealed inputs, six public tests per
tools copy before and after adoption, both shared tool checks and the fresh
Native recount pass. Only source, owner object, guards and ELF change; no
dependent objects change. No shared headers or Makefile changes are used.
Reusable modules are `game_packed_cosine_motion_match.py`,
`game_packed_cosine_motion_oracle.py` and
`test_game_packed_cosine_motion_match.py`. Preserve the older tools mirror's
previous dirty work; only these three identical owned modules are added there.

## Continuation

Evidence is self-contained under
`conker/build/game-packed-cosine-motion-151163C0-match/`: 1,041 frozen focused
inputs, 24 canonical artifacts, capture-order screens, original cosine and
caller checks, guard derivation, production audits and bank receipts. The
earlier 56-byte-frame, unsigned-byte-local, volatile and alternate record
screens remain preserved. The selected six-difference body stays unchanged
through all qualification gates.

Next audit `func_1511C548`, a 60-word placeholder in the same owner. Inspect
both sine calls, saved result lifetime, gate and output fields before
conversion. Other private candidates remain uncredited. Commit tools before
the consumer pin; no push. Root README contains aggregate rows only, and the
wider 75% goal remains active.
