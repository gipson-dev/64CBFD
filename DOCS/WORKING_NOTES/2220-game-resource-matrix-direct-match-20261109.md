# Game resource matrix update: direct match - 2026-11-09

func_15157DEC now rebuilds and scales a selected resource matrix page instead
of returning zero. All **101 body/slot words** emit directly from C, with the
original frame0x20, S0 atSP+14, S1 atSP+18 and RA atSP+1C. There is no padding,
no instruction guard and no compiler-profile change. Source is
conker/src/game/generated_183640.c; original assembly is conker/asm/183640.s.

Production total **4,289 / 5,513 (77.80%)**, Game **3,616 / 4,840 (74.71%)**,
Init492/492 and Debugger181/181, zero address drift and1224 still different.
**122** further accepted matches are needed for80%; the wider goal stays active.

## Routine, layout and caller interface

VA15157DEC..15157F80, ROM18529C..185430. The frozen full aligned-word census
has two direct JAL encodings: ROM185280 / VA15157DD0 in func_15157DC8 and
ROM12867C / VA150FB1CC in func_150FB188. Both are actual original call sites;
there are no aligned literal entry/interior address values into the404-byte slot.

The nine-word func_15157DC8 forwards the resource pointer and object+0x120
in its JAL delay slot, ignores the child return and returns1. The24-word
func_150FB188 in generated_126F60.c writes object54/58/5C to -95/-80/0,
builds three zero angles and two D_800A1DC0 scales in a five-field structure
at SP+1C..2C, passes that address in its delay slot and likewise returns1.
The constant is exactly0x3E99999A in the frozen image.

Both declarations are now void(u8*,void*). A local ResourceTransform183640
view describes the five fields (angles X/Y/Z and scales XZ/Y). It does not
pretend the caller-local structure is a float array. ResourceMatrix183640
describes position54/58/5C and two64-byte matrices at7C. Both views use GNU
may_alias and preserve IDO's plain structure declarations. Shared headers,
the caller's existing five-field type and the original matrix kernel stay fixed.
These local names are descriptive, not purported original retail names.

The routine calls func_150A8050 on matrix[page] with the three angle fields,
then reloads the page byte D_800BE9C0 and copies position into row3. It scales
rows0/1/2 by scales XZ/Y/XZ, preserving each page and scale reload. The helper
receives the pre-call page and angles; post-call writes observe provider changes.
Parameter storage may overlap matrix bytes, so caching scales changes behavior.

The native domain has two matrix pages and valid aligned backing. Guest-only
all-byte page indices, global-byte aliases and wrapped/null pointers qualify
the emitted instructions; they do not extend the portable C array domain.
GNU alias behavior is qualified by native probes, not claimed as generic ISO C
type punning. Documentation:
[GCC Common Attributes](https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html).

## Focused behavioral qualification

- **1,433 guest cases per body** cover all256 page bytes, both normal pages,
  separate/embedded/overlapping transform blocks, all32 provider-effect masks,
  signed/zero scales, call snapshots, global aliases and wrapped pointers.
  An independent byte-memory reference checks full public state and arguments.
  All101 words are visited. Literal retail rebases use a separate fixed-offset
  patcher rather than source relocation records.
- **220 fault-prefix pairs**, including four delay-slot cuts, compare complete
  literal memory/register/FPR/HI/LO/condition state, calls, snapshots and access
  traces between original and emitted code. They are instruction-order checks,
  not ISO C fault or N64 exception guarantees.
- **768 cases per body** run both complete original callers, visiting all9
  wrapper,24 second-caller and101 target words. Both current padded caller bodies
  are independently byte-exact. Embedded parameters and the five-field stack
  structure, provider effects and ignored child returns are qualified.
- **32 connected cases per body** run the original83-word rotation kernel,
  visiting all83 words and checking its entire84-word slot and factor
  D_8009F6C0=0x3C8EFA35 against the frozen image. An independent rounded rotation
  equation supplies expected matrices. The six trig services remain controlled
  math providers; their full retail approximation paths and hardware FCSR are
  not emulated by this check. The first entry150AD780 adds a phase and falls
  through to the leaf sine route150AD78C, so the kernel requests cosine then
  sine for each angle. These leaf routes do not write caller argument homes.
- Native32 **O0/O2/O3 each pass591 cases** with a typed void(u8*,void*) callback,
  actual0x1D8-byte struct102 backing, a separately declared five-field structure
  and embedded/overlapping views. Layout assertions pin the20-byte transform,
 0xFC-byte resource view and relevant offsets. All record/parameter/page bytes
  and call-time snapshots agree, with strict aliasing, no contraction and UBSan
  traps enabled. Invalid guest page indices are excluded from the native domain.
- All **ten compiled semantic controls** have public counterexamples in the
  native domain and MIPS oracle: wrong page/angles/translation/scales, omitted
  stores, addition instead of multiplication and pre-call page/scale caching.
  Private frame differences do not count as witnesses. Removing either alias
  annotation leaves IDO words/bindings identical but fails its dedicated native
  probe at O2/O3; O0 passes. These two native-only controls stay separate.
- Six GNU links independently rebase target/helper/data symbols for30 cases.
  All raw words and bindings agree with original literals. Native/guest/kernel
  models do not establish full gameplay, N64 NaN payload or hardware acceptance.

Early exploratory harness issues were fixed before formal qualification: a
generic trig provider overwrote a private slot used by the handwritten kernel,
and its two trig roles were initially reversed. Dedicated alias probes also
avoid an optimized-away whole-test fixture's false null-write diagnostics.
Those fixes change test providers only; production was still untouched.

## Owner, image and repository gates

All25 raw/padded target-owner neighbors remain fixed. All18 raw functions,
bindings, pools and register metadata in generated_126F60 stay fixed; its full
padded object is byte-identical after the declaration repair. Both actual
three-command Make recipes reproduce the independent objects. Six existing
target-owner warnings remain unchanged; the second caller has no diagnostics.

The independent complete-ELF prediction permits only the target body and symbol
extent12->404: **319 changed bytes, zero exclusions and zero metadata
permutations**. All6052 function addresses and all other bodies, protected data,
guards and conversion rows remain fixed. Production recompiles exactly the two
owners and reproduces the predicted ELF/objects; the actual ELF supplies the
recount above. The inherited whole-ROM checksum mismatch still makes make all
exit2. Existing duplicate Make recipe warnings remain.

Six focused checks pass before and after installation in both tools environments.
The sibling uses an isolated six-module overlay and explicit consumer roots;
dependency hashes and absent-file fallbacks are recorded read-only. All2434
inherited sibling dirty paths remain intact. Fresh shared smoke runs accompany
three exactly fingerprinted regression reuses per copy; reuses are not fresh runs.
The package freezes575 inputs. A local cache avoids reparsing the same object
for each guest case; source/object fingerprints and all semantic gates remain.

Tools commit before consumer; no push. Root README changes only aggregate rows.
Graphify receives a scoped AST refresh with explicit old-node retention, not a
full-corpus semantic extraction. No host-port Release artifact is touched.
Routine review uses zero Claude calls. The80% goal remains active.

Focused WSL check:
python3 -m unittest tools.tests.test_game_resource_matrix_15157dec_match -v
Receipts: conker/build/game-resource-matrix-15157DEC-match/.
Next queue: func_150DE32C, currently private and non-matching; no early credit.

Production ELF SHA-256: 94ada63c6859543740e50c321ac61e8d0af14f2ea13ac0198ca57eb0230b8d21.
Guard SHA-256: 6a6094f04735cb3127833e50b21f98c3374916605acd7aa79ccdebd80d22dfe7 (unchanged).
