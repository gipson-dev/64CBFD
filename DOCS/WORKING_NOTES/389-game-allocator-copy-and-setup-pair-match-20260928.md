# Game allocator-copy and setup pair match - 2026-09-28

## Result

`func_15169900`, `func_1518E66C`, and `func_1518E6D4` are byte-exact across
their complete 26-word, 104-byte retail spans.

The fresh linked matcher reports 2,889 / 5,466 (52.85%) exact C functions
overall and 2,315 / 4,790 (48.33%) in Game, with one address-drift blocker and
2,576 genuinely different C rows overall.

## Allocator-copy recovery

`func_15169900` allocates a `0x4C`-byte record of kind `0x5E` through
`func_15167A68`, forwarding the caller's full-width owner argument. On success,
it copies 60 bytes from the caller's source into the new record at offset
`0x10`, then returns the allocated record. On failure, it returns null without
copying.

The full-width second argument is required: narrowing it to `u8` makes IDO
reload only the low stack byte, while retail forwards the complete argument
word. The recovered pointer return type and adjacent `func_15169968` pointer
argument describe the actual ABI and eliminate the former placeholder warning.

## Setup-pair recovery

`func_1518E66C` and `func_1518E6D4` are structural twins over the typed
`Generated1BA1D0Setup` record. Both call `func_1518D1C0` with the object at
offset `0x18`, owner byte at `0x0C`, selector byte at `0x01`, and zeroed middle
arguments. The first uses selector `3` and descriptor `D_800A7460`; the second
uses selector `4` and descriptor `D_800A749C`. Both then store `0x80` at offset
`0x1E`, `-1` at offset `0x21`, and return zero.

The semantic C naturally emits each retail frame, saved `s0` lifetime, stack-
argument order, call delay slot, descriptor relocation pair, final stores, and
return sequence. None of the three recovered functions needs an expected-word
guard or compiler-profile override.

## Evidence

The linked and pristine-retail spans compare equal across all 104 bytes for
each function:

| Function | Linked file offset | Retail file offset | SHA-256 |
| --- | ---: | ---: | --- |
| `func_15169900` | `0x1A9900` | `0x196DB0` | `9b7fffa578f7098497b1b1837a3df4e4904bc4349c30b5e8add32c76905d4202` |
| `func_1518E66C` | `0x1CE66C` | `0x1BBB1C` | `6759e4cb816ea2ec0ca97e5f2a84f381d3afbc62a6e436c7e7ee3b97cbf4d139` |
| `func_1518E6D4` | `0x1CE6D4` | `0x1BBB84` | `cdf2d17d77d661e6f1670be2664794e02e616b10c9ce2c7c893e28edf797e8b6` |

The fresh linked matcher no longer lists any of the three functions.

## Validation

Focused object builds and the full non-matching replacement build pass. The
linked matcher, three direct byte comparisons, outer ROM build, project tool
checks, focused Python tests, and whitespace validation are the completion
gate. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with ordinary unparked 26-word Game `func_151993E4`, currently at 25
real differences. Keep the documented smaller special and near-match rows,
Init SDK cache routines, address-drift-blocked `func_10012588`, and larger
parked HUD renderers in their existing lanes.
