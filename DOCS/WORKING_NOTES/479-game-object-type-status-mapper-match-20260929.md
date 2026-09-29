# Game object type/status mapper byte match

Date: 2026-09-29

## Scope and behavior

`func_150B66DC` in `conker/src/game/generated_E2DA0.c` spans 30 words and
120 bytes at `0x150B66DC..0x150B6754`. It reads the type byte at `0x68` from
the source object referenced by field `0x18`, subtracts 15, and applies the
result to the target object referenced by field `0x14`:

- Selector zero sets target byte `0x09` to one.
- Selector one clears byte `0x09` and sets byte `0x2F` to 20.
- Selector two and all other values clear byte `0x09` and set byte `0x2F`
  to 40.

The routine returns one.

## Compiler shape

The explicit temporary for the source-object pointer is essential. IDO then
loads that pointer through `v0`, loads the type selector through `v1`, and
reuses the dead `v0` lifetime for the constant return value before subtracting
15. The explicit case-two/default fallthrough preserves retail's third
comparison and shared status-40 block.

This source shape also reproduces retail's branch-likely delay slots, repeated
target-pointer loads, scheduled unreachable load, temporary registers, and
shared return. All 30 words emit directly from semantic C; no expected-word
guards or assembly replacement are needed.

## Verification

- The focused generated-slice object builds with the complete retail
  instruction sequence.
- The complete ELF relink passes.
- Direct comparison passes all 120 linked bytes. Both spans share SHA-256
  `f517d090f9e18290dc22a4267a688ec99b90b73ce0f1ae41b6af86a2cce35d78`.
- The authoritative matcher reports `2,982 / 5,465 (54.57%)` overall and
  `2,407 / 4,789 (50.26%)` in Game, with zero address-drift rows.

## Resume boundary

Continue with the next ordinary small Game placeholder. Preserve the existing
parks for unresolved jump-table ownership, handwritten live-register
fragments, and the documented low-difference compiler-scheduling cases.
