# Game event-payload dispatch match - 2026-09-28

## Result

`func_15108FFC` is byte-exact across its complete 26-word, 104-byte retail span
at `0x15108FFC..0x15109064`.

The fresh linked matcher reports 2,879 / 5,466 (52.67%) exact C functions
overall and 2,305 / 4,790 (48.12%) in Game, with one address-drift blocker and
2,586 genuinely different C rows overall.

## Recovery

The function copies the two-word event descriptor at `D_80088C50` into a local
record. It builds a second local payload from two 32-bit arguments and one byte
argument, then submits descriptor type 2, the payload pointer, and event `0x1D`
through `func_15169260`.

Declaring the payload before the descriptor reproduces IDO's reverse local
allocation order: the descriptor occupies `sp+0x1C`, while the payload begins
at `sp+0x24`. The complete retail schedule then emits directly from semantic C,
including the incoming argument spills, byte reload, and call-delay payload
store. No expected-word guards or compiler-profile override are required.

## Evidence

The linked span at `conker/build/conker.us.elf` file offset `0x148FFC` and the
pristine retail span at `conker/conker.us.bin` offset `0x1364AC` compare equal
across all 104 bytes. Both have SHA-256:

`31688bd417b4deec745cd5cf64c5aa8d32f8e1855fc456c99cf3a279e613e7ba`

## Validation

The focused replacement build, linked matcher, outer ROM build, project tool
checks, all nine focused Python tests, direct byte comparison, and whitespace
validation pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with ordinary unparked 26-word Game `func_15110360`, currently at 25
real differences. Keep the smaller documented special and near-match rows, the
Init SDK cache routines, address-drift-blocked `func_10012588`, and the larger
parked HUD renderers in their existing lanes.
