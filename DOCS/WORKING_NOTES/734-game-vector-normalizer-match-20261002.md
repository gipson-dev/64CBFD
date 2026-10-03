# Game vector normalizer match

Date: 2026-10-02

`func_15145128` at `0x15145128..0x151451F0` now matches its complete 50-word /
200-byte retail slot in `conker/src/game_16EE20.c`. This refines an existing
semantic C body; conversion counts and original byte denominators do not change.

## Source Recovery

The function computes the squared length of a three-component vector, returns
zero without changing outputs when that length is zero, and otherwise publishes
the normalized vector and optional length/reciprocal outputs. A scalar local
provides the fallback reciprocal when the caller omits that output.

Retail computes the square root and reciprocal in separate optional-length
branches. The length-present branch uses
`*arg3 = 1.0f / (*arg2 = sqrtf(len))`; the absent branch writes just the
reciprocal. Output components multiply the stored reciprocal by the input
component, in that order. Restoring this structure reduces the original 35
word differences to three frame words, with all arithmetic, branches, delay
slots, loads, and stores emitted in their retail arrangement.

The remaining three expected-word guards form one leaf-frame correction:

| Offset | Compiler word | Retail word | Purpose |
| --- | --- | --- | --- |
| `0x000` | `27BDFFF0` | `27BDFFF8` | Allocate the original eight-byte frame |
| `0x00C` | `27A7000C` | `27A70000` | Point fallback output to stack offset zero |
| `0x0C4` | `27BD0010` | `27BD0008` | Restore the original eight-byte frame |

The function is a leaf and has no other stack-relative accesses. Guards leave
the semantic body intact and fail if the compiler's expected words change.
No compiler override, omission, insertion, or relocation patch is required.
The patch inventory is 10,382 rows, with three rows for this routine and zero
duplicate patch keys.

## Verification

`make -C conker NON_MATCHING=1 all match-progress -j4` passes and regenerates
the linked code binary and progress inventory. Direct comparison against
pristine bytes `0x1725D8..0x1726A0` confirms the linked function at its retail
address, with zero differences and SHA-256:

```text
6995502abe23fd9ee0d32fbbbe2e4a2e347d7c518bef15120905b12135e50589
```

The neighboring `func_151450B4` remains exact across all 116 bytes;
`func_151451F0` still starts at `0x151451F0`. Independent whole-section
comparison reconfirms zero differences across all 164,048 Init code bytes and
17,376 Init initialized-data bytes, with the hashes recorded in Note 733.

Nine host-C behavior tests in `tools/tests/test_game_vector_normalizer.py`
compile the actual function definition from the source file and cover length
and reciprocal outputs, zero-output preservation, omitted outputs individually
and together, in-place normalization, shared length/reciprocal output, and
each optional output aliasing input X. These tests exercise source semantics;
the independent linked-word comparison establishes N64 instruction matching.
All 25 tool unit tests, project tool checks, and whitespace checks pass.
Existing unrelated pointer-type warnings remain. No gameplay run or full
compressed-ROM build was performed; host-port Release is unchanged.

Fresh exact-C counts are 3,240 / 5,460 (59.34%) overall and 2,568 / 4,788
(53.63%) in Game. There are zero address-drift rows and 2,220 different Game
C rows. Init remains 491 / 491 exact, and Debugger remains 181 / 181 exact.

## Resume

Return to the ordinary Game queue with 36-word `func_15157FE8`, currently at
35 real differences. Its retail body emits two matrix display-list commands;
the existing source is still a zero-return placeholder. Preserve
`func_150A76F0` in the handwritten/register-contract workstream and
`func_150F631C` in its separate near-match cleanup queue.
