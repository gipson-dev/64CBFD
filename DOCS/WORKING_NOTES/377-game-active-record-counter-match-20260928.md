# Game active-record counter match - 2026-09-28

## Result

`func_1509CB68` is byte-exact across its complete 27-word, 108-byte retail
span at `0x1509CB68..0x1509CBD4`.

The fresh linked matcher reports 2,875 / 5,466 (52.60%) exact C functions
overall and 2,301 / 4,790 (48.04%) in Game, with one address-drift blocker and
2,590 genuinely different C rows overall.

## Recovery

The function counts active records in the table from `D_80087430` through
`D_80088420`. Each record is `0x14` bytes and is active when its first signed
word is nonzero. The recovered loop explicitly checks four records per pass,
advances by `0x50`, and therefore scans 51 groups and all 204 records before
returning the count.

IDO otherwise recognizes the fixed endpoint distance and unrolls the already
unrolled body again, adding a remainder path. The `generated_C9EC0` object now
uses `-Wo,-loopunroll,0`, which emits retail's 27-word loop. Twenty-three words
then emit directly from semantic C. Four expected-word guards swap two pairs
of independent opening instructions: the two table-address `lui` operations
and the count initialization with the endpoint `addiu`. All affected `HI16`
and `LO16` relocations are explicitly required and preserved.
The guard table contains 1,671 rows with zero duplicate keys.

## Evidence

The linked span at `conker/build/conker.us.elf` file offset `0xDCB68` and the
pristine retail span at `conker/conker.us.bin` offset `0xCA018` compare equal
across all 108 bytes. Both have SHA-256:

`72a2e52720832a296ecb457630ad93be79ec67897aeb96a7116b333c7911b5fa`

The focused object disassembly preserves the complete branch-likely load
chain, `0x50` cursor update, loop-back delay-slot load, and return sequence.

## Validation

The focused object build, full linked matcher, replacement build, outer ROM
build, project tool checks, all nine focused Python tests, guard-table audit,
direct byte comparison, and whitespace validation pass. Fresh gameplay was
not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with ordinary unparked 26-word Game `func_150A3330`, currently at 25
real differences. Keep `func_10003BD0`, the Init SDK cache routines, the
address-drift-blocked `func_10012588`, and the larger parked HUD renderers in
their documented lanes.
