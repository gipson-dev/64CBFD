# Actor burst semantic recovery and allocation boundary

Date: 2026-11-19. `func_150BBB5C` now has a complete, tested **private C
recovery**, banked in the tools manifest. Production
`conker/src/game/generated_E8C10.c` still contains its original zero-return
placeholder. **No source installation or matching credit** is claimed.

Retail spans VA `150BBB5C..150BC488`, ROM `E900C..E9938`: **587 words /
2,348 bytes**, **624-byte frame**, and **58 relocation sites**. The selected
normal O2/g3 candidate emits **589 words**, the same **624-byte frame** and
58 relocation sites. There are **539 unequal overlapping words plus two
extra raw words**. Equal frame size does not establish equal stack homes.

## Recovered behavior

The actor type is an **unsigned byte at offset 4**, read before the null
check. Types other than 32 explicitly return one. The active path also
requires non-null input and nonzero word0. The known caller discards the
result; the remaining gates and final sound path have no total source-level
return contract. Preserve that boundary rather than adding a default result.

Signed16 dimensions `E4/E6` are converted and cached before two RNG calls.
Their low two bits select **6..9 particles** and **10..13 trails**.
Heading halfword `76` is reloaded between two trig calls, followed by the
float motion read at `3C` and half-speed X/Z drift. Unlike `func_150BB760`,
missing actor model word `1D4` does **not** suppress emission: it selects
alpha255. A present model derives byte alpha from unsigned word `184`.

The **168-byte sprite** carries truncated X/Z, truncated `actor180+60`
for Y, cached dimensions, initial height from float `180`, texture46,
flags52, mode0 and tag-1. The original color call is exactly
`func_1516865C(&sprite,255,255,255,255)`, followed by
`func_15168800(&sprite,255,0)`. An unrelated F12 value is not an extra
argument. The actual installed helper declarations and original assembly
were inspected and frozen.

A **124-byte descriptor** first uses resource1, duration120, flags29E9,
zero owner/channel and unit scale. Each first-group particle obtains a
radial offset, independent randomized planar velocity, cached global-based
sizes, randomized rotations/height/upward velocity and two angular fields.
The size base `D_8009FEAC` is sampled once before this loop.

Each trail snapshots its position and velocity vectors and all **18 o32
argument words**, including float scale1.6, duration25..32, byte128..255,
the global/width-dependent scalar, selector2..5 and the constant tail.
The final RNG call precedes the `D_8009FEB0` read. The mutation fixtures
exercise that ordering and the earlier cached dimensions and size base.

The final descriptor uses resource0, randomized duration16..31, flags39E8,
actor rotation values `B8/40/C4`, actor position and size values `14C`.
Exactly two angular particles follow. A ten-word positional sound call
finishes the path: ID170, volume26000, truncated integer actor coordinates,
minimum200 and maximum2000. The caller passes those coordinate words
without adding new caller-side signed16 narrowing.

The adjacent reference project's automatic draft was used only as a
cross-check. It contains wrong actor access widths, incorrect float/integer
loads and a spurious argument to the color helper. A fresh typed m2c probe
also requires correcting a motion read moved ahead of the second trig call,
missing array declarations and first-field/whole-aggregate assignments.
Neither draft was imported into production.

## Measured fitting boundary

The initial semantic form was **589 words / frame632 / 561 overlapping
differences**. Reusing the radial trig scalars after the particle phase
ends reduces the frame to624 without changing behavior. Moving the final
signed-byte loop-index initialization to its recovered earlier source
position yields the selected **589/frame624/539** form.

Its raw SHA-256 is
`fcff86d378a42c7669aa505aeea5c376d3a523df1e5b69890b79f11f115638f8`.
The manifest retains every raw and original relocation binding.

The candidate saves an extra **S4**, hoists the descriptor address and uses
it across its loops. Retail saves S0..S3 and rebuilds that address from SP
at each factory call. Stack homes, temporary registers and schedules also
remain different. No binary normalizer, padding, inserted instruction,
omission, compiler-profile change or saved-register rewrite was adopted.

Field-address, array/union descriptor, scalar-field layout and declaration
order controls do not remove S4. The repository's existing no-unroll flag
was tested only on copied owners and produces the same raw payload for
the initial, reused-trig and earlier-index forms. It is not a profile fix.
The corrected typed-decompiler control regresses to593/frame656/571.
These screens are diagnostic evidence, not matching credit.

## Qualification and retained limits

The private packet freezes **1,859 input fingerprints**, extending Note2558's
committed baseline with three original helper assembly inputs. Full before/
after owner compiles preserve **all eight neighbors** and normalized pools.
The independently assembled original binds literally to all587 retail words.
The aligned retail census finds one JAL at ROM `AAF7C` and no aligned target
pointer literal. Original caller `func_1507D754` branches to its common exit
with zero in V0 after the call, discarding this routine's result.

The maintained four-test suite runs in both the primary tools checkout and
a curated sibling overlay. Fresh results and exact imported fingerprints
are retained in `primary-suite.json` and `sibling-suite.json` in the packet.
Both runs pass four tests with zero errors, failures or skips; each seals318
imported tool files. Runner elapsed times are40.893s primary and60.050s
sibling; unittest bodies take32.674s and37.735s respectively.

- **274 guest cases / 548 executions** compare raw C and original assembly
  with an independent descriptor/argument reference. They visit all **587
  original words**, cover all16 count pairs, four signed/float field patterns,
  helper mutations, two stack phases, rejected/inactive actors and two
  guest-only mapped-null cases. Saved integer/FP ABI state is preserved.
- **12 compiled negative controls** are effective: wrong type width,
  unsigned dimension, alpha shift, missing color call, both shortened groups,
  duration mask, late dimension/size-base reloads, final resource, pitch and
  sound volume. Each retains unchanged owner neighbors/pools.
- **Two unmapped-byte4 fault cases**, one per instruction stream, fault
  before any helper. Replacing the original byte read with a constant makes
  both controls stop faulting. This is a guest instruction boundary, not
  portable native-null semantics or full raw private-fault equivalence.

The **877-file overlay** comprises339 matching sibling files,533 primary
fallbacks, four task files and one bootstrap. Conflicting sibling edits are
not overwritten or claimed tested. The sibling's exact dirty status, HEAD
and343 dependency hashes are checked. Imported Python fingerprints are
sealed per run rather than assuming the overlay's entire contents were used.

Reserved descriptor/sprite bytes and concrete private pointer locations are
not compared by this recovery suite. Helpers are modeled ABI services, not
newly qualified complete implementations. SDK32 native tests, complete
caller execution, literal stack/saved-register relation, both production
padders, strict whole-image prediction and actual production adoption remain
open. No production Make/recount is needed or claimed for an uninstalled
candidate: all frozen production inputs, objects and ELF remain unchanged.

Installed totals therefore remain **4,558 / 5,514 (82.66%)**, Game
**3,885 / 4,841 (80.25%)**, Init492/492 and Debugger181/181, zero drift.
**129 more matches** are needed for85%. Root README aggregate tables remain
unchanged. No host, Release, save, capture or original ROM/ASM changes.

## Resume

Continue this function from the selected manifest and private packet
`conker/build/game-next-150bbb5c-private/`. Start with the extra descriptor
address/S4 lifetime and actual scalar stack homes; do not manufacture a
whole-frame normalizer from equal frame sizes. Once the source relation is
closed, finish native/caller qualification and all literal adoption gates
before credit. Preserve previous candidate/report directories.

Graphify's native update refused to shrink the existing graph and retained
all 67,048 old node IDs. A four-file scoped AST merge and explicit target
reference added the recovery tools without losing those IDs. This is a
scoped update, not a full-corpus re-extraction.

Routine work used zero Claude calls and no REA/WSL setup. Tools are committed
before the consumer pin and working note; there is no push or automatic pause.
