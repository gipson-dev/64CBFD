# Interpolated callback zero-count selector screen

Date: 2026-11-12. This extends [Note 2311](2311-game-callback-return-normalization-screen-20261112.md).
`func_1500B8F4`, `func_1500BAB8`, and `func_1500BC7C` remain private and
uncredited; no production function or match count changed.

The previously examined table `D_8008CF00` has five declared rows of eight
pairs. The setter `func_1500AD84` stores `savedOptions & 0x7f` into the row
byte when the preset is not 255. In the original `func_1500BEC0` dispatcher,
the row byte is multiplied by 32, the encoded three-bit column by four, and
the resulting pair supplies the callback index and signed count. This creates
a potential 0..127 row domain from that setter, not a demonstrated 0..4 bound.
This observation does not show which options occur in actual gameplay, and
other writers, aliases and out-of-bounds accesses can affect memory.

A static scan of the current linked ELF's 1,024 pairs across those 128 rows,
with the declared table cross-checked against the retail decompressed image,
finds 34 pairs selecting callback indices 2, 3, or 5. Twenty are within the
five declared rows and have positive counts. **Fourteen are outside those rows
and have count zero**: rows 65, 66, 67, 104, 105, 106, and 107, columns 3 or
7, at addresses `0x8008D72C..0x8008DC7C` in the linked image. They select all
three callbacks. They are adjacent unrelated linked data, not additional
declared table entries; initial contents do not prove runtime contents or
reachability. Independently inspected objdump section bytes agree for both
address clusters. The ELF SHA-256 is
`7ef7a8774764d03c6abf45587a364a94d66158453c380a3ce8937d7444e0de68`.

In 56 bounded modeled executions of the original dispatch instruction window,
using each of the fourteen static pairs with four cursor/slot fixtures, the
original callback stores the incoming `v0` (the column, 3 or 7) back to
`D_800DDD20`. The existing private explicit-return candidate instead stores
the incoming cursor, chosen as 100..103. All 56 disagree; neither callback
invokes the helper in these zero-count cases. This establishes a concrete
window-level difference under those constructed inputs, not that those rows
occur during gameplay or that the entire parent executes correctly.

Two earlier IDO source arrangements for `func_1500B8F4` were also screened.
Both fall off a non-void C function at count zero and therefore have no defined
portable C return there. Each generated body preserves the retail return in
16 modeled cases for each count 0, 1, 2, and 3, with modeled helper effects.
The 116-word fallthrough arrangement additionally reads the incoming cursor
stack slot on the zero path; a guest access cut at that slot stops it while
retail returns. The 117-word return-inside arrangement returns without that
read in the same cut. These screens do not qualify either candidate's source
contract, aliases, fault behavior generally, guards, other two variants, or
production build. The return-inside shape is a lead for further investigation,
not a match. For that first callback, the return-inside machine code also
agrees with retail on the stored return, slot counter, and helper-call count
in 20 modeled zero-count dispatch-window cases covering its five out-of-table
pairs. The C zero-count return remains undefined despite this target output.

The reusable static census and its focused tests are in tools commit `7d45d01`.
Run `python3 -m tools.experiments.game_interpolated_selector_census
conker/build/conker.us.elf conker/conker.us.bin` from the repository root.
Two tests passed in the mounted environment and in a sibling-padder environment;
the latter used the mounted new module and test with the standalone sibling's
`pad_generated_object`, without modifying the sibling checkout. Synthetic
first/last-row and signed-count checks, truncation rejection, and a changed
retail-table negative control passed. The standalone sibling's 2,434 prior
dirty paths and three recorded fingerprints were preserved.

Transient scripts and receipts are in ignored
`conker/build/game-three-interpolated-callbacks-screen/`, including
`dispatch_zero_extent_20261112.py`, `fallthrough_zero_screen_20261112.py`,
`return_inside_dispatch_20261112.py`, and `selector-sibling-validation.json`.
They may be cleaned; this note retains
their bounded outcomes. Recheck the actual image and candidate fingerprints
before reusing them. Next, investigate a defensible zero-return interface and
the return-inside shape, compare stack and live-register schedules, and qualify
all three bodies and the linked image before adoption.

The latest production recount remains **3,707 / 4,840 (76.59%)** Game and
**4,380 / 5,513 (79.45%)** overall, zero drift; 165 more Game matches are
needed for 80%.

The scoped graph refresh retained unrelated nodes: 59,892 before and 59,894
after, with no out-of-scope removals or changes. Three relocated IDs matched
by signature; 31,816 existing nodes were retained by the fail-closed path.
This was not a full-corpus extraction.
