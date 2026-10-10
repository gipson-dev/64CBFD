# Game Linked Node Endpoint Transform Direct Match

Date: 2026-10-10

## Baseline And Result

Resume from consumer 77c6fadb0b0a6ae012e0eda0712943c30fae5a24 and mounted
tools b71d5d023cc3959e2506ac306eefb00b7dc48a49, both active checkouts clean.
The older standalone tools checkout remains at
ddbdd16b53ce60b054fb6e11bf0649a41f48375a with 160 pre-existing dirty entries.
Preserve its independent tracked work and mirror only the two absent new files.

func_151B47D8: VA0x151B47D8..0x151B48DC, ROM0x1E1C88..0x1E1D8C,
65 words / 260 bytes, frame0x18. Replace the false zero-return C placeholder
in [generated_1E0560.c](../../conker/src/game/generated_1E0560.c) with the
complete linked-node endpoint transform updater. All 65 words emit directly
from semantic C under the existing O2/g3 profile. No new guards or padding.

Single Codex writer; zero Claude calls. Use the scoped graph query and existing
compiler/parser/MIPS/native32/padder/ELF/data helpers. No shared helper/profile,
OGL, Release, save or editor changes. Root README gets aggregate rows only.
The wider Game matching goal remains active.

## Recovered Contract

Arguments are actor, typed 40-byte link record, destination XYZ pointer and
unsigned byte endpoint selector. First node/epoch/matrix-index/input XYZ are
at record+0/+4/+5/+8; second equivalents are at+0x14/+0x18/+0x19/+0x1C.
Both node pointers are captured before any flag store. There are no invented
null-node guards. Each node has a lifetime word+0, epoch byte+0x3B and palette
pointer+0x1D4. The selector tests only its low eight bits; the complete incoming
A3 and destination A2 words are saved at incoming SP+12/+8.

If either palette is absent, OR actor+0x10 with0xC and return1 without calling
the helper. The first absent palette short-circuits the second palette read.
Otherwise require both lifetime words nonzero and both epochs equal. Failure
returns0 without changing flags or calling the helper, retaining retail's
short-circuit order.

Success clears flag0x4 for a nonzero byte selector or0x8 otherwise. Select the
stored first/second input XYZ, reload that node's palette after the flag store,
then add the unsigned byte matrix index times64. The actual helper contract is
func_15143134(inputPoint, destination, matrix), not destination-first. Call it
once and return1 independently of its caller-saved return register.

A scratch union gives the mask and later matrix pointer separate named members
with non-overlapping lifetimes. It avoids keeping an integer mask and pointer
live as separate compiler roles, while each member is written before use.
No integer flag value is dereferenced as a pointer.

The actual 12-word func_151B2FA0 wrapper passes actor+0x150 as the record.
D_8008FAF0[1] /0x8008FAF4, ROM0x2345B4, registers that wrapper. The complete
81-word func_151B3184 calls it twice, with actor+0x14/mode1 and actor+0x20/mode0,
and removes the owner if either validated update returns0. Missing palettes
set flags but do not cause that removal. Wrapper/dispatcher/registration unchanged.

## Fresh Qualification

[Candidate driver](../../tools/experiments/game_owner_link_matrix_candidates.py):
selected shared union and shared-word control both emit65/frame24/zero differences.
Separate mask/pointer locals emit65/frame24/32 differences; explicit byte cast
of a word parameter emits64/62 differences. Six independently compiled semantic
negatives demonstrably change memory, flags, helper arguments or return.
Isolated and copied-owner compiles produce no diagnostics or new pools.

[Focused suite](../../tools/tests/test_game_owner_link_matrix_match.py): all nine
tests pass before installation in12.721s and after installation in12.653s.

- 3,200 guest cases /6,400 executions compare complete retail/raw C bodies and
  an independent public reference: selector widths, seven gate states, both
  stack phases, all byte indices/flags and boundary indices0/1/127/255.
  Entire memory, ordered reads/writes, calls, return, argument homes and saved
  GP/FP/SP agree. Reach63 words; repeated loads+0x4C/+0xD8 are unreachable but
  remain in the complete65-word byte match.
- 21 aliases include overlapping points/destinations, palette/index updates
  through the flag byte, captured node pointer and epoch overlap. Six effective
  compiled negatives cover full-word mode, wrong flag/point/index, missing epoch
  and premature palette caching. Bounded helper copies preserve sequential raw
  word access; they are not a claim about actual unaligned hardware accesses.
- 14 paired fault prefixes and two short-circuit cases qualify emitted guest
  access order, not portable C fault semantics or hardware trap/FCSR behavior.
- Native32 executes the complete selected C in14,336 independent cases plus two
  matrix-index aliases, checking 40-byte record layout, helper arguments, flags,
  sentinel outputs and raw coordinate words with byte narrowing.
- Four independent entry/helper symbol sets /84 guest cases preserve the sole
  R_MIPS_26 relocation at+0xE8. Complete original wrapper42 cases and dispatcher14
  cases qualify connected endpoint calls and removal behavior.
- Sixteen connected cases execute the complete original98-word point-transform
  helper for float/packed matrices, zero/nonzero input and in-place destination.
  Lower SDK/matrix helpers remain bounded models. Retail's packed translation
  path uses signed low halves: this fixture yields (3.25,-5.5,4.75), versus
  float translation (3.25,-4.5,5.75); do not silently change that behavior.
- Actual copied owner preserves all16 neighbors, raw bodies, relative
  relocations and pools. Actual padder retains every other byte, emits260 bytes
  with no padding and preserves the following func_151B48DC address.

Fixture corrections: add local NOR handling without changing shared oracles;
keep native alias pointers inside a padded backing object and avoid a macro
colliding with the function's parameter. Restore the measured signed-low
packed translation expectation. These were test issues, not production fixes.

## Linked Installation And Bank

Fresh build/progress, focused post-install suite and make tools-check pass.
The known duplicate generated_12D630 Makefile recipes still warn; isolated and
copied target-owner compiles are clean, not a claim of a warning-free full build.
The entire ELF equals baseline after replacing only the260-byte target slot and
symbol extent; symbol/string ordering is normalized and decoded metadata agrees.
Guards and conversion CSV remain byte-identical. Protected data189,088 bytes /
720 owners remains exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Fresh matcher: Game2,747/4,816 (57.04%), total3,420/5,489 (62.31%),
Init492/492 and Debugger181/181 exact. Zero address drift /2,069 different.
Converted counts/bytes unchanged because the prior placeholder already was C.
Wider unchanged neighbor suites use prior receipts from
[Note 1196](1196-game-linked-owner-position-provider-match-20261010.md), not fresh
claims; fresh copied-owner/whole-ELF gates establish their unchanged bodies.

Bank mounted tools b4e101ab91697aa1c134e8803e506fbedf27f9ac first, then consumer
source/docs/aggregate rows/pin. No push requested or performed. Both new tools
are byte-identical in the older checkout; existing HEAD/tracked dirty hashes
remain unchanged. Keep graph refresh warnings/refusal and any fresh hook result
separate from matching evidence.

Manual graphify update exits1 rather than overwrite the existing39,232-node
graph with a17,452-node scan. The existing fail-closed rule retains19,398 nodes
from2,972 excluded-but-present files. Version0.9.20/0.9.26 and zero-node
devcontainer.json warnings persist. No force, purge, install or policy changes.

## Next Target And Curve Handoff

Next adjacent source-only target: func_151B48DC,44 words /176 bytes, leaf,
VA0x151B48DC..0x151B498C, ROM0x1E1D8C..0x1E1E3C. It lays out the ten-point
straight interpolation and clears flag0x2. Inspect complete owner/caller,
constant D_800AA3C4, unrolled loop and exact floating operation order first.

The curve remains uninstalled and non-matching; preserve
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md)
and its squared-copy/private/frame rejection gates. No curve matching credit.
Historical curve harnesses fingerprint the whole pre-this owner/ELF: future
curve work must record a fresh isolated baseline while proving this qualified
neighbor unchanged, not overwrite old receipts or mistake the authorized neighbor
change for a curve regression. Actual trig, hardware, FCSR and gameplay acceptance
remain separate from this static matching checkpoint.
