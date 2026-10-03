# Game Nested Float Copy/Clamp Conversion And Match

Date: 2026-10-03. Baseline: `6982d0f`.

## Result

`func_1507C324` is converted from its retained assembly pragma to semantic C
using the existing actor and nested-state layouts. Its complete nineteen-word
/ 76-byte slot remains byte-exact with eight expected-word guards restricted
to one closed floating-register allocation permutation. No compiler profile,
padding, insertion, omission, or shared header change is added.

The original `.s` file stays as a reference and independent guard-test input;
it is no longer the production owner of this function. This is an actual
assembly-to-C conversion: C count rises by one and C bytes by 76. The dimension
helper recovery from Note 790 and the Init allocator correction are preserved.

## Retail Contract

The field-mutating interface takes destination and source actors. It loads
both nested pointers at actor offset `0x2D0` before checking either pointer.
If either is null, it performs no stores. Actor pointers themselves must be
valid; no root-pointer null fallback is invented.

For valid nested pointers, retail:

1. Loads source float `0x08`, then destination float limit `0x18`.
2. Stores the source value to destination `0x08`.
3. Reloads destination `0x08`.
4. Subtracts 1.0f from the previously loaded destination limit.
5. If `limit - 1.0f <= copied value`, stores the adjusted limit to destination
   `0x08`; otherwise leaves the copied value.

The C output pointer is volatile to preserve the retail copy, reload, and
conditional second store. Source and limit loads occur before that copy in
the emitted guest instructions. The adjusted-limit expression is reused by
IDO for the compare and conditional store; it emits one subtraction.

The comparison is inclusive, not strict, and unordered comparisons do not
clamp. A quiet-NaN source therefore retains its copied payload; a NaN limit
does not replace a finite source. With source -0.0f and limit 1.0f, equality
takes the clamp and stores the subtraction's +0.0f result. A generic min helper
or a strict greater-than check would not preserve all these cases.

Both captured pointers survive actor/nested-storage aliasing. The tests include
a destination output overlapping the source actor's nested-pointer field:
the original source pointer is used even after the copy overwrites that field.

## Compiler And Guard Proof

The candidate emits all nineteen operations in the exact retail order. All
integer registers, offsets, constants, branches, delay slots, and instruction
kinds match directly. Eight differing words contain floating-register fields:

| Source FPR | Retail FPR |
| --- | --- |
| f0 | f4 |
| f2 | f6 |
| f4 | f8 |
| f6 | f10 |
| f12 | f0 |

Complete the permutation on otherwise unused registers with f8 -> f2 and
f10 -> f12. This closes one cycle; it does not split a live value or add a
new computation. The full-function guard test reconstructs the unguarded
nineteen words from the expected fields, decodes FPR operand positions, applies
only that permutation, and requires the entire result to equal the original
reference. Comparison condition-code bits and GPR fields are not renamed.

The eight guarded byte offsets are `0x18`, `0x1C`, `0x20`, `0x24`, `0x28`,
`0x2C`, `0x30`, and `0x40`. There are no relocations in this leaf. Structured
CSV comparison confirms all prior guards remain unchanged.

An initial candidate using an in-place `limit -= 1.0f` also emits nineteen
words, but reuses one register across different source/result lifetimes. The
final expression form gives the simpler complete permutation above; no broad
compiler matrix or unrelated slice change is introduced.

## Measurements

| Item | Measurement |
| --- | --- |
| VMA slot | `0x1507C324..0x1507C370` |
| ROM slot | `0xA97D4..0xA9820` |
| Body / slot size | 19 words / 76 bytes; no padding |
| Unguarded differences | Eight FPR allocation words |
| Linked differences | Zero |
| Unguarded SHA-256 | `c8789c23e681626c5fac78c0aa1931958fbe8754c38db1bec922dda64a6f0646` |
| Linked and retail SHA-256 | `4f58821a6f1badee3a246fd97e1d128ae0b5ac03df33ef508633478fc2aedc85` |

The adjacent refresh wrapper remains byte-exact at all 112 bytes. The
dimension helper remains unchanged at hash
`d81006ca7298e61f20e168b71d899205a5fbb50c8661aec1abb59a74a3e64cbb`,
with its existing 310-word body, ten padding nops, and 312 differences.

## Verification

Fourteen tests in `tools/tests/test_game_nested_float_copy_clamp.py` compile
the actual production function and existing layouts in the shared freestanding
32-bit SSE fixture. They cover layout offsets, null nested pointers, below/
equal/above limits, negative/fractional limits, repeated calls, shared actor
and state pointers, overlapping output/pointer storage, quiet-NaN payloads,
NaN limits, infinities, signed zero, surrounding-byte preservation, and the
complete nineteen-word register-only guard proof.

All fourteen new tests, all thirty focused copy/clamp/dimension tests, and
all 475 tool tests pass. The full `NON_MATCHING=1 all match-progress -j4`
rebuild, project tool checks, and `git diff --check` pass. The shared CSV
dependency triggers a broad object rebuild; existing recipe/source warnings
remain, with no stale guards left.

Twenty-nine exact Game regression slots and ten prior non-matching hashes
are preserved. Independent setter, return-closure, producer, and collector
span checks remain retail-exact. Both full Init sections retain their exact
retail hashes from Note 789. No host-port build, MIPS execution, FCSR exception/
rounding-mode qualification, or gameplay acceptance is claimed. NaN cases are
quiet NaNs; signaling-NaN trap behavior is not covered by the host fixture.

## Progress

| Section | C functions | Assembly | C bytes |
| --- | ---: | ---: | ---: |
| Total | 5,463 / 6,042 (90.42%) | 579 | 1,930,924 / 2,256,728 (85.56%) |
| Init | 492 / 539 (91.28%) | 47 | 151,796 / 164,048 (92.53%) |
| Game | 4,790 / 5,321 (90.02%) | 531 | 1,759,488 / 2,072,880 (84.88%) |
| Debugger | 181 / 182 (99.45%) | 1 | 19,640 / 19,800 (99.19%) |

Fresh matching: total 3,270 / 5,463 (59.86%); Init 492 / 492; Game
2,597 / 4,790 (54.22%); Debugger 181 / 181. Address drift remains zero and
different C remains 2,193, all Game. README changes only aggregate tables;
recovery details stay in working notes and the update log.

## Next

Inspect the connected zero-return placeholders `func_1507BDB0` and
`func_1507C22C` from the same slice. Read the full callee and its actor-scan
caller before choosing parameter types or implementing either interface;
recovering only the caller would still invoke an empty body. Dimension matching
and the preparation routine's special stack provenance remain separate/open.
The remaining Init bitmap/MMIO matching work retains its new-evidence gate.
The sibling port and frozen Release artifacts are untouched.
