# Game template-effect constructor guarded match

Date: 2026-11-14. `func_151A9390` replaces the zero-return placeholder in
`conker/src/game/generated_1D4E00.c`. Its 169-word retail slot is
`0x151A9390..0x151A9634` (ROM `0x1D6840..0x1D6AE4`). The C body preserves
the 0x98-byte frame, register allocation and control flow. It emits 159
original words directly; ten expected-word guards move three temporary
stack slots and their paired stores/reloads up by four bytes. Both padded
outputs match every original word and relocation.

The constructor accepts byte flags and a byte selector. Selectors 9 and above
return immediately; the other selectors choose a 20-byte template from
`D_8008F9AC`. It builds a 40-byte allocation request with template floats,
an optional float position, two caller-supplied floats and fixed tags.
`func_151A8B20` receives the request, signed-halfword lifetime, 44 extra
bytes, byte channel and context. On success it copies the template's 44-byte
payload to the result at offset 0x80 and applies two optional flag bits.
Another input flag independently enables a secondary effect, including when
allocation fails. That effect uses truncated float coordinates when a
position is supplied, otherwise signed-halfword coordinates from the owner.

Four request bytes and one secondary-header byte retain their previous
stack contents. Guest checks seed and compare them. Native checks inspect
the initialized fields and exclude those indeterminate bytes.

Guest validation compares an independent bounded model with retail, raw C
and padded streams in 1,794 cases. It covers selector rejection, upper input
bits, flag combinations, null optional inputs, lifetime truncation and the
-1 sentinel, allocation failure, changed template payload pointers and late
reads after helper mutations. Sixteen cases execute windows of both original
callers at `0x15025208` and `0x15027740`. Twelve guest-only overlap cases
include the payload source, template table and request position. All 169
instructions are exercised. Retail and padded modeled machine state also
agree at 291 fired access prefixes; raw C is checked for the same behavior
with its different private temporary offsets.

Native 32-bit C passes 450 cases in each of six O0/O2/O3 and
strict/no-strict-aliasing configurations with trapping UBSan. Seven altered
source controls are detected. Native fixtures use typed, aligned, disjoint
objects and finite coordinates representable as signed integers. The three
helpers are modeled; `func_151A8B20` remains a production placeholder.
Guest stack aliases and incoming-home mutations do not establish portable
C parity for those cases. Full caller/helper execution, unrestricted aliases,
invalid floating-point conversions, hardware and gameplay are not qualified.

Both padding implementations pass 12 GNU links across four independently
rebased layouts. The other 22 owner functions and normalized pools are
unchanged, and the target compile has no diagnostics. Production Make builds
the changed owner using its ordinary compiler and padding rules. Since all
ten appended guards belong to this target and prior rows are unchanged, the
guard manifest is marked old for this scoped build to reuse the 697 frozen
neighboring objects:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The resulting ELF equals the independent shadow prediction. The strict
whole-image audit accounts for 492 changed bytes with zero exclusions.
All 6,051 function addresses and 189,088 protected Game-data bytes remain
fixed. Only the target owner changed among 698 frozen linked objects; the
conversion manifest is unchanged and all prior guard rows are preserved.

Tools commit `0cc2f7e` retains the installed regression suite. It passes in
the mounted tools checkout and an
isolated sibling tools overlay, preserving the sibling's existing edits.
`make tools-check` also passes:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_template_effect_151a9390_installed -v
```

A scoped fail-closed Graphify refresh retained all 60,134 prior node IDs
and produced 60,135 nodes. This was not a full-corpus re-extraction.

Fresh production recount: Game **3,797 / 4,843 (78.40%)**, total
**4,470 / 5,516 (81.04%)**, zero drift. At the current denominator,
**219** additional exact matches are needed to reach 85% total.
