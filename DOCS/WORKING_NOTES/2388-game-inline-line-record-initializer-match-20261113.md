# Game inline line-record initializer match

Date: 2026-11-13. `func_1512DD50` replaces the zero-return placeholder in
`conker/src/game_15B200.c`. The 85-word retail body occupies
`0x1512DD50..0x1512DEA4`, ROM `0x15B200..0x15B354`.

The routine constructs an inline record at owner offset `0x870`. It derives an
endpoint from the owner's signed coordinates and direction fields, forms the
opposite displacement, calls `func_150AD930` for its length, and stores the
reciprocal and normalized direction. It converts two integer fields from the
inline record at `0x6FC`, clears two floats and copies a kind byte. The former
commented draft treated both inline records as pointers; the recovered body uses
their actual inline addresses. The local overlay types use GCC's `may_alias`
attribute when available; the original IDO compiler sees ordinary structs.

The signed-convert-then-add-2^32 sequence matters for native rounding. For
example, `0x80000081` yields `0x4F000000` under retail's two single-precision
roundings, while a direct native unsigned-to-float cast yields `0x4F000001`.
The source retains the retail conversion shape and its saved Z-coordinate
lifetime. Note 2387 raised a question about the length helper mutating the
owner: the connected 11-word retail helper only reads its three float inputs,
squares and sums them, and returns the square root. The vector itself can still
overlap caller stack storage, which is why the stack-overlap screen matters.

IDO emits 84 words from the semantic C body. Sixty-nine expected-word and
relocation guards normalize the closed float/register scheduling and inline
address calculations, inserting two derived instructions and omitting one
compiler scheduling NOP. The resulting 85 words and relocation bindings match
retail. These guards are not a claim that unguarded C directly emits the retail
instruction stream. The original call at `0x1512F5A4` in `func_1512E8E0`
passes the owner in `a0`; the tested caller window continues at `0x1512FDF0`.

Tools commit `aa150d6` supplies the reproducible qualification:

```sh
python3 -m unittest tools.tests.test_game_line_record_1512dd50_match -v
```

The guest screen checks 240 finite, nonzero-length cases each against retail,
raw C and guarded C with the actual retail length helper connected. The
independent native32 screen checks 1,118 integer pairs at each of O0/O2/O3
with trapping UBSan and rejects four intentionally incorrect variants. The
helper is modeled in the native test. The bounded caller window covers 24
cases; 76 retail/guarded guest memory-access fault prefixes agree. A stack
overlap screen compares 483 cases: all three streams terminate and agree on
the 48-byte output and helper input vector in 447, while the remaining 36 are
unresolved and are not counted as passes.
Zero-length and non-finite floating-point inputs, FPU exception flags and
hardware/gameplay behavior were not qualified by these finite-value screens.
The guest fault-prefix check applies to the guarded instruction stream, not
portable C fault ordering.

Eight GNU links cover four address layouts. Both padders reject all 276 stale
word and relocation checks; the generated-padder layout is synthesized from
retail slot boundaries. The focused suite was run with mounted tools and with
an isolated overlay using the independent sibling tools checkout plus mounted
fallback modules. `make tools-check` passed; the sibling's 2,434 pre-existing
dirty paths remained untouched.

The production Make build and independent whole-image audit account for 279
changed bytes with zero exclusions. Only this function changes among 6,051;
all addresses and all 189,088 protected Game-data bytes remain fixed. Only
`game_15B200.c.o` changed among 698 fingerprinted linked objects. The
conversion CSV and previous guard rows are unchanged. The scoped Graphify
refresh retained all 60,060 prior node IDs; fail-closed retained out-of-scan
files, so this was not a full-corpus extraction.

Fresh production recount: Game **3,774 / 4,843 (77.93%)**, total
**4,447 / 5,516 (80.62%)**, zero address drift. **101** more Game matches are
required for 80% at the current denominator. The adjacent `func_1512DEA4`
reads this line record and remains a zero-return placeholder; it is a possible
next consumer to investigate, not a newly qualified match.
