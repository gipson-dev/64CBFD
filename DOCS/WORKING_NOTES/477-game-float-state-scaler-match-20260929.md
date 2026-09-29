# Game float-state scaler byte match

Date: 2026-09-29

## Scope and behavior

`func_151339D4` in `conker/src/game/generated_15F680.c` spans 31 words and
124 bytes at `0x151339D4..0x15133A50`. It adds the fifth floating-point
argument to state field `0x10` and stores the result at `0x3C`. It then uses
field `0x14` as a scale for six fields from `0x44` through `0x58`; field
`0x48` alone is multiplied by the negated scale. The routine returns one.

The three otherwise-unused register arguments remain in the recovered
signature because the o32 ABI homes them before loading the fifth stack
argument, exactly as retail does.

## Compiler shape

Declaring `scale` without initializing it, storing the accumulated value, and
then assigning `scale` preserves retail's opening field/stack load order. IDO
also places the constant return value between the later field loads and
stores, reproducing the complete retail schedule. All 31 words emit directly
from semantic C; no expected-word guards or assembly replacement are needed.

## Verification

- The focused generated-slice object builds and matches the complete retail
  instruction sequence.
- The complete ELF relink passes.
- Direct comparison passes all 124 linked bytes. Both spans share SHA-256
  `7737373cb0aeb0a501b6af28c2e958084f14fbdc979e25e1ab83a2fe14f45c65`.
- The authoritative matcher reports `2,980 / 5,465 (54.53%)` overall and
  `2,405 / 4,789 (50.22%)` in Game, with zero address-drift rows.

## Candidate triage and resume boundary

Continue with the next ordinary small Game placeholder. Keep
`func_15015F40` parked: its control flow depends on an unresolved 38-entry
indirect table at `jtbl_800966C0_game`, and the checked-in data at that address
does not provide authoritative target membership. Keep `func_150A76F0` in the
raw-assembly queue because it is a handwritten fragment that consumes live
`t4`, `t9`, `s6`, and `s7` state and returns through `v0`, not an ordinary C
calling convention. Retain the previously documented compiler-scheduling
parks for `func_151A8584`, `func_151A85D4`, and `func_1506EF5C`.
