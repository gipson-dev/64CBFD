# Game dual event-byte dispatcher match - 2026-09-28

## Result

`func_150F9720` is byte-exact across its complete 26-word, 104-byte retail span
at `0x150F9720..0x150F9788`.

The fresh linked matcher reports 2,878 / 5,466 (52.65%) exact C functions
overall and 2,304 / 4,790 (48.10%) in Game, with one address-drift blocker and
2,587 genuinely different C rows overall.

## Recovery

The function masks its argument to eight bits and uses it to select a two-byte
pair from `D_800A1C40`. It clears the first word of an eight-byte local event
buffer, writes the pair's first byte at offset 4, and submits the buffer through
`func_151494E0` with command `0x42`. It then replaces that byte with the pair's
second value and submits the same buffer again.

IDO emits retail's complete 26-word instruction schedule from that semantic C,
including the pair-pointer lifetime, both call delay-slot byte stores, and the
`HI16`/`LO16` table relocations. Its aggregate allocation is eight bytes larger
than retail's compact frame. Eleven function- and offset-scoped expected-word
guards normalize only the frame size and affected non-relocating stack
immediates. The guard table contains 1,682 rows with zero duplicate keys.

## Evidence

The linked span at `conker/build/conker.us.elf` file offset `0x139720` and the
pristine retail span at `conker/conker.us.bin` offset `0x126BD0` compare equal
across all 104 bytes. Both have SHA-256:

`8409e6478553ee9e4836d46383122bb217dc9d13befd2ebefb479c1eb5e4252a`

## Validation

The focused object build, complete guarded replacement rebuild, linked matcher,
outer ROM build, project tool checks, all nine focused Python tests, direct byte
comparison, guard-table duplicate audit, and whitespace validation pass. The
full-ROM SHA gate is not applicable to the `NON_MATCHING=1` replacement build.
Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with ordinary unparked 26-word Game `func_15108FFC`, currently at 25
real differences. Keep the smaller documented special and near-match rows, the
Init SDK cache routines, address-drift-blocked `func_10012588`, and the larger
parked HUD renderers in their existing lanes.
