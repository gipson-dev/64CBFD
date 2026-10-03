# Game Threshold-Scaled Record Update

Date: 2026-10-02

## Scope and Contract

`func_151A4900` in `conker/src/game/generated_1D0840.c` replaces a zero-return
placeholder with the complete semantic record update. Retail occupies
`0x151A4900..0x151A499C`, 39 words / 156 bytes, at ROM
`0x1D1DB0..0x1D1E4C`. The second argument is homed but otherwise unused.

The record-local layout is recovered from `conker/asm/1D0840.s`:

| Offset | Interpretation in this routine |
| --- | --- |
| `0x1A` | Signed halfword counter |
| `0x2B` | First byte output |
| `0x2C` | Second byte output |
| `0x38`, `0x3C` | Two float values |
| `0xAA` | Signed halfword second-output multiplier |
| `0xAC` | Signed halfword first-output threshold |
| `0xAE` | Signed halfword first-output multiplier |
| `0xB0` | Signed halfword float-update threshold |
| `0xB2` | Signed halfword float-increment multiplier |

If the counter is strictly below the first threshold, its product with the
first multiplier is narrowed to the first byte output. Otherwise that byte
is unchanged. Independently, below the second threshold, the low signed word
of `parameters[5] * D_800BE9E4` is converted to float and added to both float
values. The source uses unsigned multiplication followed by signed conversion
to preserve retail's low-word product without signed multiplication overflow.

The counter is reloaded on the float-update arm. The second byte is always
updated with the narrowed counter/multiplier product, and the routine returns
one. The local type does not change shared headers or claim a broader actor
identity for this payload.

## Compiler and Guard Boundary

The existing `-O2 -g3` slice profile emits the full 39-word semantic body.
Initial byte-pointer accesses and a subsequent local record type both retain
an early counter reload. An explicit conditional counter lifetime preserves
the retail arm, but IDO still schedules the load before the float publication.
A bounded volatile-read trial does not resolve that ordering and is not kept.

Eleven strict expected-word guards in `retail_word_patches.us.csv` normalize:

- Two commutative integer multiply operand orders, at `0x24` and `0x84`.
- One independent scheduling rotation at `0x58..0x78`: the counter reload
  moves after the two float stores while the same eight float computation
  and publication words retain their order.

The counter halfword and float destinations are disjoint within the same
record. No instruction is inserted or omitted, and no branch, arithmetic
operation, field offset, return value, or relocation is replaced with missing
semantics. No compiler profile override is added.

## Behavior Tests

`tools/tests/test_game_threshold_update.py` extracts and compiles the actual
local record declaration and function body. Seven tests verify:

- C field offsets and complete record size against the retail layout.
- Strict threshold equality and adjacent below/above cases.
- Independent combinations of the two threshold gates.
- Signed counters, negative multipliers, and byte narrowing.
- Low-word wrap before signed float conversion.
- Independence from the unused second argument.
- A deterministic 256-case signed parameter sweep.

Every behavior case compares the entire record against the reference result,
including untouched padding, counter, parameters, and gated-off fields. All
seven tests pass, and all 60 repository tool tests pass. `make tools-check`
also passes. These are host-source behavior tests, not gameplay qualification
or proof of arbitrary host-toolchain conversion portability.

## Linked Verification

The full `make -C conker NON_MATCHING=1 all match-progress -j4` rebuild passes.
Independent linked-byte comparison confirms all 156 bytes match the pristine
ROM. SHA-256:
`5a2c3d28bb6a3327e50160920a53027f2a88f554973cfb58bf66cd813f9cdc23`.
The next function `func_151A499C` remains at `0x151A499C`.

Both complete Init sections remain byte-exact after the shared-dependency
rebuild: `.init` is 164,048 bytes and `.init_data` is 17,376 bytes. Their
SHA-256 values remain:

- Code: `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf`.
- Data: `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239`.

This is linked code/data evidence, not BSS, gameplay, or a full-ROM match.

## Progress and Resume

Conversion totals remain 5,461 / 6,042 C rows. Exact C now totals
3,246 / 5,461 (59.44%); Game is 2,573 / 4,788 (53.74%). There are 2,215
different C functions and zero address drifts. Init retains 47 assembly rows;
the supported compiler-generated Init queue remains complete.

Next ordinary Game target: `func_151B1918`, 35 words / 35 real differences.
Keep `func_150A76F0` in the handwritten/register-contract workstream and
`func_150F631C` in its separate near-match cleanup queue. No sibling host-port
source, build, or runtime artifact was changed.
