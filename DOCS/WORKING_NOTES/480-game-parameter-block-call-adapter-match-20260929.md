# Game parameter-block call adapter byte match

Date: 2026-09-29

## Scope and behavior

`func_15133510` in `conker/src/game/generated_15F680.c` spans 30 words and
120 bytes at `0x15133510..0x15133588`. It forwards its first argument and
eleven fields from the parameter block supplied as its second argument to
`func_151424F4`:

- Three 32-bit integer fields at `0x18`, `0x1C`, and `0x20` become register
  arguments two through four.
- Eight float fields at `0x24..0x40` become outgoing stack arguments five
  through twelve.

The routine returns one after the call.

## Compiler shape

Giving `func_151424F4` its complete typed twelve-argument declaration lets IDO
recover the retail ABI directly. Repeated field access through the second
argument keeps the parameter-block pointer in saved register `s0`; the eight
float arguments produce the exact 64-byte frame and stack-store sequence.

The final float store occupies the call delay slot. The return constant,
saved-register restores, frame release, and return delay slot also match. All
30 words emit directly from semantic C; no expected-word guards or assembly
replacement are needed.

## Verification

- The focused generated-slice object builds with the complete retail
  instruction sequence.
- The complete ELF relink passes.
- Direct comparison passes all 120 linked bytes. Both spans share SHA-256
  `212f7aca0a9183382226942e0dfc15bbfd4c9606b7db86d79fa4b59e84d5381a`.
- The authoritative matcher reports `2,983 / 5,465 (54.58%)` overall and
  `2,408 / 4,789 (50.28%)` in Game, with zero address-drift rows.

## Resume boundary

Continue with the next ordinary small Game placeholder. Preserve the existing
parks for unresolved jump-table ownership, handwritten live-register
fragments, and the documented low-difference compiler-scheduling cases.
