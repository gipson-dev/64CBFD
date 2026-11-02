# 1979 - Signed interpolated angle lookup recovered directly from C

`func_150488C8` now emits all **55 body words** directly from semantic C, with
**no frame or guards**. Its retail slot contains another three alignment words.
The production build and independent Windows-checkout ELF recount confirm
**4,046/5,507 (73.47%)**, Game **3,373/4,834 (69.78%)**, zero address drift and
1,461 different functions. This adds one exact match; **85 more** are needed
for 4,131/5,507 and the wider 75% objective, which remains active.

## Recovery and ABI

The owner is `conker/src/game_75C90.c`, entry `0x150488C8`, retail ROM
`0x75D78..0x75E54`; three alignment words extend the slot to `0x75E60`.
The source contained a zero-return placeholder and commented nonmatching donor.
Both are replaced by the full signed interpolation routine. The existing
shared declaration remains `f32 func_150488C8(f32 arg0)`; F12 carries input and
F0 carries the result. The leaf routine uses caller-saved temporaries only.

The recovered order is: scale the absolute input, truncate the index, compute
the fractional part, load the unsigned table value, select the next value or
endpoint, interpolate, convert to radians, and restore the input sign. Computing
the fraction before loading the base recovers the original schedule. Reusing
the base local for the final result recovers F16 and its last three instructions.
Removing the unused result declaration preserves the complete raw payload.
No register bindings, inserted instructions, guard rows or compiler changes
are needed. Both unsigned-conversion correction blocks remain in the output.

The actual ELF contains the 256-entry `u16` table at `D_80098E00` and constants
`D_8009900C = 255.99998474121094f`, `D_80099010 = 65535.0f`, and
`D_80099014 = 1.5707963705062866f`. The base table read precedes the endpoint
branch. Preserve the unchecked index; the recovery adds no clamp. Negative
zero follows the nonnegative return path, as in retail.

A complete aligned ROM census found no direct J/JAL transfer to this entry
and no literal function pointer to it. The graph likewise supplies its owner,
two sibling functions and existing float interface, with no caller edge.
Computed indirect callers remain unknown. There is no claimed real caller
window or whole-game input-domain proof; typed native calls independently
exercise the declared float interface.

## Fresh qualification

The raw 220-byte payload and all eight HI/LO bindings equal an independently
assembled retail routine. Three code/data layouts, including HI/LO carry
boundaries, produce identical original and candidate instructions.

The guest corpus contains 4,096 finite input patterns, both signs, signed zero,
tiny values and ULP boundaries around every table cell. Two tables (retail and
a nonmonotonic full-range unsigned control table), across three layouts, give
24,576 reference comparisons covering all 256 cells and all 47 reachable words.
Each arithmetic operation is rounded independently to binary32. Eight words
are unreachable after zero-extending LHU: offsets `4C,50,54,78,7C,80,84,88`.
They remain byte-exact rather than being deleted.

Seventy-two fired access-prefix pairs compare original/candidate available
registers, memory, calls, trace, PC and delay location. Removing accessed fields
also fires the expected sparse-memory read failures. Six guest-only prefixes
for the first representable magnitude above one prove that the base read is
not silently clamped. Those cases are excluded from native C tests because
their index exceeds the declared array. NaNs, infinities, FCSR exception state,
hardware denormal behavior and gameplay acceptance are not qualified here.

Native 32-bit typed function-pointer calls pass at O0, O2 and O3, using both
tables and all 4,096 inputs. SSE binary32 operations, disabled contraction,
stack realignment, undefined-behavior/float-cast sanitizers and unchanged-table
checks are enabled. Each profile rejects seven effective controls: omitted
sign, signed base conversion, omitted fraction, early endpoint, wrong divisor,
wrong endpoint and the old zero-return stub.

The two owner neighbors, pools and relocations are preserved. Owner diagnostics
remain zero. All three commands from the real Make recipe independently
reproduce the qualified padded object, including the three alignment words.
Both tools copies pass five focused methods and shared checks before and after
installation. The normal production Make build matches the private link.

## Complete-image accounting

The independent prediction replaces the full 232-byte slot and changes only
this symbol's extent from 20 to 220 bytes. Four closed linker metadata groups
permute 13 complete symbol records and their adjacent strings:

| Original order | Predicted order by original index |
| --- | --- |
| `D_8009900C`, `D_800A72AC`, `D_800A330C` | 1, 2, 0 |
| `D_80099014`, `D_80090128` | 1, 0 |
| `D_80099010`, `D_8009E540`, `D_800A72B0`, `D_800A3310` | 1, 2, 3, 0 |
| `.L150320B4_game_data`, `func_150238D0`, `D_8009E690`, `D_8009EB80` | 2, 3, 0, 1 |

Every definition field is retained; only record/string ordering changes.
The literal complete ELF prediction passes with **zero exclusions**. All 6,052
function addresses, all 6,051 other function bodies, section geometry, the map,
guards, build profiles and shared declarations remain fixed. Protected data
matches all 189,088 bytes across 720 owners. Production ELF SHA-256:
`c1ba81dadb31b6a5e1cbbb16d5444ebca6bd85da0b4326ab78e5059a70997e34`.

## Harness corrections and retained evidence

The inherited focused snapshot initially omitted this new owner source/object.
They were added from the still-unchanged 17,741-file banked seal, retaining the
old snapshot and a separate extension proof. The final snapshot has 1,086
inputs; no baseline hash was silently replaced.

The first public checks exposed a whitespace-only shared-declaration assertion
and reusable compiler outputs overwriting immutable test artifacts. Inspection
proved the object/rebased-ELF changes confined to `.mdebug` source timestamps
and filenames, with code, bindings and pools unchanged. The original pinned
artifacts were restored from verified Windows copies. Public recompilation and
relinking now use separate filenames. The final before/after suites pass with
all 27 immutable preparation pins intact; failed attempts and correction
receipts remain available.

Evidence directory:
`conker/build/game-signed-interpolated-lookup-150488C8-match/`.
Key receipts include `private-guest-v8.json`, `private-native-v6.json`,
`private-owner-image-v11.json`, `production.json`, `native-install.json`,
`prepared-artifacts.json`, and the final bank/handoff records. Run the focused
suite with `python3 -m unittest tools.tests.test_game_signed_interpolated_lookup_match -v`.

Source, the four owned qualification modules and documentation are committed
tools first, then consumer pin. The older tools mirror retains all inherited
work plus the four new untracked modules. README changes contain aggregate
status rows only. The graph refresh is scoped AST extraction with prior nodes
and valid edge occurrences retained, no obsolete interface edges, and zero
LLM tokens; it does not claim full-corpus extraction or reclustering. No push,
host Release change, or archive change is part of this matching adoption.

Next ordinary candidate: `func_150A23E4`, currently a zero-return placeholder in
`conker/src/game/generated_CDE80.c`. Original `conker/asm/CDE80.s` contains its
55-word/frame64 body: an initial-state gate, packed sound fields, original
audio submission and state publication. Qualify its callback ABI, live record
fields, helper/caller behavior, actual generated-owner padding and complete
image before installation or credit. `func_150AE280` needs separate entrypoint
qualification because its slot begins with a non-linking stack-restoration jump;
do not treat that slot as an ordinary single C routine.
