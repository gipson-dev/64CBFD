# Owner phase/state callback - guarded byte match

2026-10-31. `func_15108C38` in `generated_135D00` is recovered from its zero-return
placeholder as `s32 func_15108C38(u8 *owner)`. Its complete 236-byte slot at VA
`0x15108C38..0x15108D24`, ROM `0x1360E8..0x1361D4`, matches all 59 words after
one expected-word guard. There are no inserted, omitted or alignment words.

## Behavior and ABI

Capture the embedded state at `owner + *(s32 *)(owner+0x50) + 0xF8`. Advance its
two phases with `D_800A2480`/`D_800A2484` and the original repeated clock reads,
wrap each phase, then compute two sine offsets scaled by `D_800A2488`/`D_800A248C`.
Call the timer and lookup-value updaters with the original owner. Finally read
the live byte at saved state+0x20, publish owner+0x12 as 4 when nonzero or 2 when
zero, and return 1 so the callback remains active.

Both owner and state pointers retain their original lifetimes across all six
calls. A helper changing the owner's offset does not redirect the saved state;
guest incoming-home mutations do not replace the owner retained in S1. A flag
change by either final helper is observed before publishing the mode byte.

The callback is table index 1 of `D_80089C18`, with its single aligned literal
pointer at ROM `0x22E6DC` / VA `0x80089C1C`. There are no aligned direct JALs.
The complete original 41-word `func_1513B798` dispatcher executes in 320 cases,
covering active, disabled, expired-lifetime and callback-result paths. No caller
source or unrelated prototype sweep is needed.

## Compiler and guard

The existing O2/g3 owner profile emits all 59 semantic words, the 32-byte frame,
and all 16 bindings. RA is saved at SP+0x1C, state/S0 at SP+0x14, owner/S1 at
SP+0x18. The only raw difference is word 13 / offset 0x34:

- Compiler: `addu S0,T6,S1`, expected word `0x01D18021`.
- Retail: `addu S0,S1,T6`, replacement `0x022E8021`.

The opcode, destination, both input registers and all other words/bindings are
identical. Unsigned ADDU is commutative for every 32-bit input and cannot trap
on signed overflow. No scheduling, frame, memory-access, FPU or control-flow
normalization is performed. Two actual padder controls reject stale word or
relocation preimages. The entire previous guard manifest remains an exact prefix.

## Qualification and image accounting

- 650 scripted guest cases / 1,950 executions compare original, raw C and padded
  C, exercising all 59 words with literal full machine-state agreement. The
  corpus includes signed zeros, nonfinite operands, helper mutations and guest
  aliases. All 139 access prefixes and 24 delay-slot cuts agree; two independent
  symbol layouts supply six rebase cases.
- 640 connected cases execute 174 original helper words: sine, phase wrapping,
  timer and value lookup. Dynamic word coverage is 84/104 for sine, 24/24 for
  wrap, 16/16 for timer and 30/30 for value lookup. Multiple positive and negative
  wrap iterations are exercised. Finite connected cases do not claim infinite
  wrap completion, complete sine coverage, FCSR parity or hardware acceptance.
- Native32 C passes 2,048 finite scripted cases per O0/O2/O3 profile with UBSan.
  It checks owner/state canaries, all four flag representations (0,1,128,255),
  live flag changes after both helpers, float operation order and return 1.
  Eleven effective native controls fail with semantic check codes. All twelve
  compiled guest controls fail; the cached-clock alias control is guest-only.
- Eight fresh canonical tests pass in each tools copy, plus both shared tools
  checks. Two installed tests per copy run fresh, with six unchanged semantic
  checks reused only through exact input/module/artifact fingerprints.
- Three actual Make commands reproduce the qualified object with zero C
  diagnostics. All ten neighboring definitions and all owner pools agree.
- Strict complete-image prediction accounts for all 296 changed bytes: 195
  target code bytes, one target extent byte and 100 metadata bytes. The latter
  are three closed named symbol/string permutations: the `D_800A2480`,
  `D_800D2C28`, `D_8008FE20` group; `.L15172474_game_data`/`D_8009E6C4`; and
  `func_151668B8`/`D_8009E6C0`. All named values, types, bindings and extents are
  preserved except the declared target extent. No bytes/regions are excluded.
  All 6,055 other bodies, all 6,056 addresses and 189,088 protected Game data bytes
  across 720 owners remain fixed.

## Banking and continuation

Tools commit: `9626826a58b4f2bc0d3e66c8e91563343b9993e6`. Production ELF SHA-256:
`34565398868c2c09d4f03b9d6cc9bd22150128f46855df7f5266ac9a35cc955e`.
Actual recount: **3,997/5,506 (72.59%)** total, **3,324/4,833 (68.78%)** Game;
Init remains 492/492, Debugger 181/181, and address drift is zero.
**133** more functions are needed for 75% (4,130 total).

Detailed receipts are in ignored `conker/build/game-owner-phase-state-15108C38-match/`.
The root README changes only its aggregate rows. The graph update covers the
source, three tools modules and seven documents, retaining all old valid
relationships; it does not claim full-corpus extraction or global reclustering.
Next queued screen: `func_151C9DE8`. Private candidates remain uncredited.
No push or host-port/Release changes are included.
