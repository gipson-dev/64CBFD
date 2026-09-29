# Game audio DMA reader byte match

Date: 2026-09-29

## Scope and behavior

`func_151F3C4C` in `conker/src/libultra/audio/game_21FC90.c` occupies 75 words
and 300 bytes at `0x151F3C4C..0x151F3D78`. An explicit nonnegative cursor
argument replaces `D_800E0DE4`. The routine clamps the requested byte count to
the remaining `D_800E0DE0` extent, obtains the synthesizer DMA callback, and
requests data from `D_800E0D80 + D_800E0DE4`. A null DMA result returns zero.
Otherwise, it converts the result to its cached address, invalidates that
range, copies it to the destination, advances the cursor, and returns the
actual byte count.

## Source recovery

The previous C kept separate `state` and `ret` locals. That forced IDO to use
a 40-byte frame, placing the callback state, callback pointer, DMA result, and
incoming argument homes eight bytes above retail's locations. The callback
state is dead after `n_syn->dma(&state)` returns, so retail reuses that same
slot for the subsequent DMA result.

Assigning the DMA callback result back to `state` restores retail's 32-byte
frame and every stack offset. The complete control flow, callback dispatch,
cache invalidation, copy, global cursor update, call relocations, and delay
slots then emit directly from C.

## Compiler normalization

Eleven stale-checked guards normalize two closed register-allocation cycles:
seven words around the cursor-plus-request extent comparison and four words
around the DMA-result null check and cached-address conversion. The four
address-bearing guards verify unchanged `D_800E0DE4` and `D_800E0DE0`
relocations. No instruction is inserted or omitted.

## Verification

- The focused `game_21FC90` object accepts all eleven new stale checks.
- A complete guarded-object rebuild and ELF relink pass.
- The authoritative matcher reports `3,000 / 5,463 (54.91%)` overall and
  `2,422 / 4,789 (50.57%)` in Game, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 300 bytes.
- Both spans share SHA-256
  `761449b54f35127e444756f8e17dfbd58f03c91ae450b500a21b39f6710e5814`.
- Project tool checks and all 10 tool unit tests pass.

## Resume boundary

Continue with the next ordinary C candidate from the authoritative matcher
queue. Keep `func_15015F40` parked behind its unresolved indirect-table
ownership, keep handwritten `func_150A76F0` in the assembly lane, and retain
the `func_15168F08` signed-opcode/index-loop evidence until its original typed
record shape is identified.
