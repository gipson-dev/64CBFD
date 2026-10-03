# Game Actor Dimension Helper Semantic Recovery

Date: 2026-10-03.

## Result

`func_1507C3E0` replaces its empty C body with the complete retail-grounded
dimension selection, state overrides, attachment expansion, optional scaling,
and three nullable halfword outputs. The existing refresh wrapper
`func_1507C370` now calls a real implementation rather than an empty helper.

The helper remains non-matching. No word guards, compiler profiles, shared
header changes, or assembly ownership changes are added. This is semantic
recovery of a row already counted as C, not a new converted-function count.
Init and README aggregate tables remain unchanged.

## Retail Contract

Parameters are an actor and optional outputs in order: height, base radius,
and potentially expanded radius. Retail computes all dimensions before
publishing in that order. Conversion is signed truncation toward zero followed
by storing the low halfword, not saturation or unsigned rounding.

Early paths bypass subtype dispatch, attachment expansion, and scaling:

| Actor condition, in precedence order | Height | Both radii |
| --- | --- | --- |
| Word at offset zero is zero | 180 | 60 |
| Word is `0x2D` | Nested float `0x960` | Nested float `0x95C` |
| Word is 4 | Signed halfword `0xE6` times six | Signed halfword `0xE4` times three |
| Word is `0x2C` | 160 | 80 |
| Category byte at offset five is 5 | Signed halfword `0xE6` doubled | Signed halfword `0xE4` |

Type `0x2D` requires its nested pointer as retail does; no null fallback is
invented. Type `0x2E` has no special early branch in this helper.

All other actors dispatch by the unsigned subtype byte at offset four.
Mappings are decoded from all three retail tables at `0x8009B4A0`,
`0x8009B5B8`, and `0x8009B674`, not inferred from adjacent case labels:

| Subtypes | Height / radius before expansion | Scale afterward |
| --- | --- | --- |
| `0..4`, `0x3B`, `0x75`, `0x80`, `0x82`, `0x88`, `0x90`, `0x96`, `0x98`, `0x9C`, `0x9D`, `0x9F`, `0xA0`, `0xB0..0xB2`, `0xB4` | State-dependent rules below | Yes |
| `0x25`, `0x2E` | 70 / 90 | Yes |
| `0x36` | Float global `D_8009B688` / 90 | Yes |
| `0x9A` | 60 / 45 | No |
| `0xAC` | 90 / 30 | No |
| `0x89`, `0xBA` | 60 / 30 | No |
| `0x53` | Global flag nonzero: 300 / 150; zero: 250 / 90 | Yes |
| All others | Signed `0xE6` doubled / signed `0xE4` | No |

Retail `D_8009B688` has bits `0x43808000` (257.0f). C preserves the global
load rather than substituting a literal. Retail table/constant decoding and
host fixtures are not proof of linked Game-data or gameplay parity.

### State-dependent path

The pointer at actor `0x31C` controls these rules, in order:

1. Nonzero word at state `0x04`: height 80, radii 60.
2. Nonzero byte at state `0x17`: height 300, radii 70.
3. Nonzero actor water byte `0xAD`: height 180, radii 90.
4. Otherwise height 180, radii 60. With state present, either a nonzero signed
   halfword at nested `0x73C`, state byte `0x197`, or state byte `0x1B3` widens
   both radii to 120. Add unsigned halfword state `0x1A6` to height.

After any rule, state low nibble at `0x4E` equals one, byte `0x4F` equals zero,
and actor float `0x3C < 40.0f` overrides height to 500 and radii to 110.
The comparison is strict; 40 and unordered/NaN do not trigger it.

Local state/camera views expose only needed offsets. The shared `struct126`
does not expose several retail fields, including byte `0x1B3`; shared
declarations are not broadened speculatively.

### Expansion and scaling

For non-early paths, actor byte `0x13C >= 101` and byte
`D_800B85A4[index * 0x32C] == 0x13` add `120 * xz_scale` to the expanded
radius and `100 * y_scale` to height. The base radius is unchanged.

Only scalable subtype families then multiply height by `y_scale` and both
radii by `xz_scale`. Attachment additions are therefore multiplied again
in scalable cases; they remain unscaled in fixed/default cases. Do not
collapse the radii or reorder expansion after scaling.

## Measurements

| Item | Measurement |
| --- | --- |
| Retail slot | VMA `0x1507C3E0..0x1507C8E0`, ROM `0xA9890..0xA9D90` |
| Slot size | 320 words / 1,280 bytes |
| Retail body | 317 words plus three padding nops |
| Recovered IDO body | 310 words, frameless, plus ten padding nops |
| Current aligned word differences | 312 |
| Previous empty-placeholder differences | 303 |
| New guards/profiles | None |
| Current complete slot SHA-256 | `d81006ca7298e61f20e168b71d899205a5fbb50c8661aec1abb59a74a3e64cbb` |

The increased difference count is not a semantic regression: the previous
body did no dimension work. Matching is separate; the frameless body does not
reproduce retail's `0xA0` frame and saved f20 lifetime. The slot fits without
overflow or a trampoline.

Adjacent routines are unchanged and independently byte-exact:

| Routine | Bytes | SHA-256 |
| --- | ---: | --- |
| Retained `func_1507C324` | 76 | `4f58821a6f1badee3a246fd97e1d128ae0b5ac03df33ef508633478fc2aedc85` |
| Refresh wrapper `func_1507C370` | 112 | `f76ebf3e5c54848c244a826c349a9b156683e93f088e363b88d3e31ccab607af` |

## Verification

Sixteen tests in `tools/tests/test_game_actor_dimension_helper.py` compile
the actual helper, actual refresh wrapper, production actor layout, and local
views in a freestanding 32-bit SSE host fixture. The exhaustive subtype oracle
is independently decoded from retail table bytes and tests every subtype with
both global-flag values. Other cases cover layout offsets, branch precedence,
signed dimensions, unsigned extra height, each widening trigger, strict/NaN
velocity comparisons, expansion/scaling order, threshold/index gates, null and
aliased outputs, fractional/negative truncation, low-halfword wrap, global
constant reads, and wrapper count/null-state behavior.

All sixteen focused tests and all 461 tool tests pass. The full
`NON_MATCHING=1 all match-progress -j4` build, project tool checks, and
`git diff --check` pass. Existing duplicate-recipe warnings remain.

Twenty-nine earlier/adjacent exact Game slots and nine prior non-matching
hashes are unchanged. Independent setter, return-closure, producer, and
collector comparisons remain retail-exact. Both full Init sections match
retail with the same hashes recorded in Note 789; the allocator correction is
preserved. Fresh matcher totals stay at 3,269 / 5,462 exact C, Init 492 / 492,
Game 2,596 / 4,789, Debugger 181 / 181, all with zero drift.

No MIPS guest execution, exceptional float conversion qualification, linked
Game-data acceptance, or gameplay acceptance is claimed. Host float tests use
finite, signed-word-representable outputs; NaN is tested only as velocity.
The preparation routine's special stack provenance from Note 784 remains
unresolved, so whole-chain acceptance is still open.

## Next

Adjacent retained `func_1507C324` is a bounded nineteen-word ordinary-ABI
candidate: it copies nested float `0x08`, loads the destination limit at `0x18`
before the store, then conditionally clamps to `limit - 1.0f`. Recover its
alias/read-order and unordered-comparison behavior before attempting C.
Keep exact assembly until the complete slot is proven.

Dimension matching is deferred separately; do not normalize hundreds of words
to turn semantic recovery into a nominal match. `func_1507BDB0` and
`func_1507C22C` still contain zero-return placeholders and need connected
interface recovery, not a whole-slice completion claim. Remaining Init bitmap
and MMIO work retains its new-evidence gate. The sibling port and frozen
Release artifacts are untouched.
