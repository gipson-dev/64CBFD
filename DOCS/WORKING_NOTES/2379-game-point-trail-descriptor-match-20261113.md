# Game point trail descriptor match

Date: 2026-11-13. `func_151382E0` replaces its zero-return placeholder in
`game_161520.c`. Its 81-word body spans VA `0x151382E0..0x15138424` and ROM
`0x165790..0x1658D4`. It selects the effect category, skips category 2, and
otherwise submits a point and fixed parameters to the angular trail factory.
The known original caller's unused return declaration is corrected to `void`.

The C descriptor has compatible angular and localized subobjects for the
factory. Its raw IDO output differs from retail in four frame/argument-home
words; four checked guards restore the retail `0x70`-byte frame. The helper's
declarations were standardized across active C callers, and five existing
helper guard preimages were updated while their replacement words were
preserved. The helper and the other two affected caller objects remain
section-identical after padding. The three bytes following the descriptor's
selector remain unwritten. The pre-existing flat descriptor view in
`func_15142180` is not established as a portable C aliasing guarantee.

Tools commit `c1d9daf` supplies fingerprinted, reproducible checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_point_descriptor_151382e0_match -v
```

All 11 checks passed before and after production installation. They include
640 guest point cases, 512 connected original-caller cases, 256 guest helper
cases, and 496 matched retail/padded guest fault prefixes. Native checks at
`-O0`, `-O2`, and `-O3` cover 20,480 point cases with six effective negative
controls per profile; the helper and revised existing trail preset also pass
their independent native models. Both helper padders reject corrupted guard
preimages, and 15 GNU links cover three symbol layouts. Guest fault and stack
alias observations describe the modeled instruction streams, not portable C
fault behavior or live gameplay. See [Note 2378](2378-game-point-descriptor-interface-qualification-20261113.md)
for the private screens and limitations.

The separate tools checkout was tested using an isolated overlay without
modifying its 2,434 existing dirty paths. The pre- and post-install hybrid runs
passed all 11 checks using available sibling modules and mounted fallbacks; it is not a
standalone sibling-checkout result. Three older affected test suites already
failed before this change because a retained snapshot was missing or their
historical source fingerprints were stale. The older scaled-descriptor suite
had nine passes and two pre-existing failures: an old constant-pool comparison
and an expected guard count of 10,809 rather than the current 30,952. These
failures are not counted as successful regressions.

The production build and independent shadow link agree. A strict comparison
against the frozen prior ELF accounts for 367 changed bytes, including symbol
ordering, with **zero exclusions**; only this function changes among 6,051
functions, all addresses remain fixed, and all 189,088 protected Game-data
bytes match. Conversion CSV bytes are unchanged. Of 698 fingerprinted linked
source objects, the intended point owner and `debugger_258ED0.c.o` changed.
The latter's exact pre-build object was not retained, so a direct old-versus-
new object-section comparison is unavailable. Three identical-input repeat
builds differed from each other and from the production debugger object only
in `.mdebug`; two retained older debugger objects differed from the current
object only in `.mdebug` and `.symtab`. The strict linked-ELF comparison
still checks every byte, including the linked debugger region. This evidence
does not prove the discarded object's exact metadata.

Fresh production recount: Game **3,764 / 4,843 (77.72%)**, total
**4,437 / 5,516 (80.44%)**, zero drift; **111** more Game matches are needed
to reach 80% at the current denominator. The host port was not modified or
runtime-tested for this decompilation match.

The scoped Graphify refresh retained all 60,033 prior node IDs and produced
60,034 nodes and 113,309 links without reclustering. Its fail-closed path
retained 31,816 existing nodes; this was not a full-corpus re-extraction.
