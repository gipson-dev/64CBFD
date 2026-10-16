# Packet Rectangle Macro Temporary Pool And Native Blockers

Date: 2026-10-16. Consumer predecessor **8456609e**, tools predecessor
**05ca56d**. Previous goal turn: **progress**, installing the qualified
71 -> 18-word improvement. Continue **func_15095D34**, owner
`conker/src/game/generated_C1D70.c`, VA **0x15095D34..0x1509629C**.

This turn is **evidence only**: no production C, guards, profile, helper,
ELF, progress CSV or root README edit; **no new byte-matched function**.
The installed routine remains **346 words / frame 0x88 / 18 pointwise
differences**, with literal first **148** and last **91** words. All 100
live/frozen inputs retain Note 1439's exact installed baseline.

## Selected Body, Not The Intermediate Form

`tools/experiments/game_packet_rectangle_macro_lifetime.py` freezes the
installed 18-word body in a new ignored build directory. Do not relabel
Note 1439's `compiler-inner-qualified` capture: that belongs to the earlier
19-word form. New captures under
`conker/build/game-packet-rectangle-macro-lifetime/` are:

```text
compiler-selected-qualified
compiler-selected-temp-pool
compiler-selected-pool-gates
allocation-selected-qualified-5
```

All four complete-owner/isolated captures reproduce the known 18-word raw
body, relative bindings and empty pools. Normal/traced objects match in each
capture; the three frontend/optimizer stream pairs are identical, containing
**1,362 CFE / 1,208 UOPT records**. CFE, UOPT, UGEN and the owned driver
terminate successfully; all four compiler hashes remain pinned. Compiler
debugging is scoped to private owned processes, not the game or editor.

The isolated source SHA-256 is
`9227400f8ff743be1839c55d4b574abd1b970397e83fd781fb8dacf7baf03f26`.
Raw target SHA-256 remains
`f95ee415f2eba533fa4076e5f6c42331367bf3444eb855a78b7816f598dc48c3`.
No new compiler signature is invented to accept an unknown body.

## Observed Temporary Pool

Read-only native breakpoints observe `f_spilltemps` entry/return, actual
temporary selection at **0x450902**, and `f_gettemp` entry/return. Validate
**24** sequenced events, one owned UOPT PID/inferior, exact probe/return PCs,
installation/cleanup order, bounded raw linked-node snapshots and matching
producer/consumer streams. The complete mode-5 allocation capture corroborates
the selected expression identities and integer interference constraints.
Its suppressed real-number printer remains invalid for numeric cost/timing
claims; this turn does not use those printed values.

CFE declares **120 bytes** of M storage. Spill-pool construction provisionally
reaches **144 bytes**, allocating six four-byte homes **M-124..M-144**.
That is **not** the emitted frame: final UOPT M extent and observed UGEN
frame are **136**, and the function remains frame 0x88. Do not infer a frame
regression from an intermediate allocator counter or assume a particular
compaction algorithm without its own evidence.

The first two homes are also assigned to expression ranges that ultimately
remain in registers: **73** (integer X) and **107** (integer Y). Range
**135** (fractional T) uses the third home provisionally; flag **145** uses
the fourth. Later macro X **347** selects the third home, **M-132**, and
macro Y **354** selects the fourth, **M-136**. These are the wrong SP+4/+0
homes already present in emitted UOPT, before UGEN.

| Selected Macro Range | Earlier-Home Blockers From Integer Graph | Actual Native Forbidden Temp IDs | Selected Home | Retail Home |
| --- | --- | --- | --- | --- |
| X 347 | Temp 0: 73/235; temp 1: 107 | 0, 1 | Temp 2 / M-132 / SP+4 | M-124 / SP+0xC |
| Y 354 | Temp 0: 235; temp 1: 107/349; temp 2: 347 | 0, 1, 2 | Temp 3 / M-136 / SP+0 | M-128 / SP+8 |

The last capture reads the **actual native forbidden bit vector**, rather
than treating an inferred graph explanation as direct execution evidence.
At each of 20 selections, its blocked IDs and first available home agree
with the observed selected node. X's first word is `0xC0000000`; Y's is
`0xE0000000`. The other captured vector words are zero. Removing a forbidden
bit or pointing outside the pool is rejected independently of any log hash.

A later `f_gettemp` call **does fire**. It reuses the first M-124 node without
growing the pool, changing availability from `[1,1,1,1,0,0]` to
`[0,1,1,1,0,0]`. This is UOPT evidence, distinct from Note 1439's observed
UGEN temporary-hook event set. Do not turn absence in one subsystem into
absence in the other.

## Bounded Source Decisions

Revalidate **29** unique complete-owner sources, actual objects, relative
bindings, pools, linked words, frame and complete pointwise difference lists.
Best remains **18**; SELECTED stays INITIAL, and there is no installation path.

| Source Decision | Result |
| --- | --- |
| Four coordinate phase splits using already-dead scalar roles | 348..351 words, 251..334 differences; reject |
| Named lower corners | 346 words, frame **0x90**, 31 differences; reject |
| Three unsigned quarter-coordinate products | Identical known 18-word body |
| Six defined wide product/shift forms | 424/430/485 words, frame **0xB0**; reject |
| Three explicit flip masks | Identical known body |
| Eight real-role declaration reorderings | Identical known body |
| Three unsigned descriptor-dimension forms | Identical known body |

The declaration and unsigned-dimension screens do not recover the twelve
flip-block scratch/schedule words. The coordinate screens do not recover the
six macro-home accesses while preserving retail shape. No arbitrary stack
padding, unused locals, physical-register bindings, shared-header changes,
new compiler profiles or bulk guards are installed.

## Final Qualification And Bank

All **ten final tests pass in 19.501s**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_packet_rectangle_macro_lifetime -v
```

Fresh checks cover all 29 complete source/object/binding/pool/linked-word
rows, all 100 live and frozen inputs and every frozen-input corruption,
both raw pool and direct native forbidden-bit captures, lifecycle/process/
PC/route/chain/displacement/availability controls, compiler/source/stream/table
controls, identical-but-invalid object/binding/pool controls and no-repeat
trace gates. Earlier eight-, nine- and ten-test intermediate passes are not
the final 29-form receipt.

Both tools copies are byte-identical, pass Windows AST parsing and all eleven
shared padder tests: consumer **0.062s**, standalone **0.049s**. The latter
uses discovery, not package-qualified imports. `make tools-check` passes.
Fresh official measurement remains **Game 2,922/4,828 (60.52%)**, **total
3,595/5,501 (65.35%)**, different **1,906**, address drift **0**. Init
492/492 and Debugger 181/181 converted C routines remain exact.

Note 1439's native32/UBSan, guest semantics and whole-image qualification are
**prior unchanged evidence**, not freshly rerun gameplay or broad runtime
claims. No production guest rebuild is necessary for this tools-only turn.
Conversions stay 5,501/6,044 (91.02%), bytes 86.04%; README stays unchanged.

Tools **e3dca0d246a7f4cb1c0da3ee49f7d00fdd89443f** banks the two new files
before consumer docs/pin. Preserve old mirror HEAD **ddbdd16** and all **826**
initial dirty hashes; add only the two absent files for **828** dirty paths.
Never commit/reset the mirror. Wait for the normal incremental graph hook;
retain 19,398 excluded nodes without full extraction or purge. No Claude/auth
retry, push or host-port/frozen Release edit, build or launch occurs.

## Next Action

Stay on **func_15095D34**. The first mismatch is still **+0x250**, and the
same twelve flip-block words plus six macro-home accesses remain open.
The new evidence rules out declaration order, mask spelling, unsigned
dimension arithmetic and simple corner phase splits on this baseline.

Map the last uses of original-coordinate ranges **73/107**, narrowed S-step
range **235** (`ucvtl` of the real M-40 S-step variable) and macro intermediates
against the CFE/UOPT clipping stages. Use that map for one typed-step or
explicit clipping-stage source hypothesis, preserving
the macro's full-width Y sign predicate as well as its signed-16 coordinate
uses. Do not recycle these 29 equivalent/worse forms or force the target
homes. Retain inherited-stack C deferrals, original caller backlog and all
wider Game/additional-source/raw-matching work.
