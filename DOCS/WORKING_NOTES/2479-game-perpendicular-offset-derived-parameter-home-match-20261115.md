# Note 2479: Perpendicular-offset query and derived parameter home

Date: 2026-11-15. Consumer baseline `6a3ad044eb618e1944c4c7cd06b8ee390260ae68`,
tools baseline `836b220ac68153663cd41c869425e3007949e4d7`.
Tools implementation/qualification: `74f04ea06485803a06c30dd5811fe330ee274a1b`.
Continues [Note 2478](2478-game-selector-mask-defined-shifts-and-guarded-match-20261115.md).

`func_1519EF90` is adopted and **byte-exact across all 94 words / 376 bytes**,
with its original **0x40-byte frame**. Its complete typed C emits 92 words.
**29 expected-word guards**, including **two inserted words and no omissions**,
restore the derived parameter home, original private locations and independent
register/scheduling choices. This earns **one C match**. No compiler profile,
header or shared padder implementation changes.

## Recovered behavior and types

Owner `conker/src/game/generated_1CC440.c`; VA `0x1519EF90..0x1519F108`,
ROM/code-image offsets `0x1CC440..0x1CC5B8`. The first argument points to a
record containing a state pointer. State+0x18 holds the actor, and an embedded
parameter block at +0x58 holds its floating offset at +0x10. A missing actor
attachment at +0x1D4 returns zero without writing the output.

The routine subtracts reference X/Z at record+0x20/+0x24 from actor X/Z.
When either absolute delta exceeds `D_800A8CE0`, it computes the perpendicular
unit direction using ordered binary32 products, addition, SQRT.S and division.
Otherwise it samples the actor's byte heading and its quarter-turn counterpart.
Mode byte 6 applies the positive offset; other bytes negate it. Output stores
occur in **X, Z, Y order**, retaining their live overlap behavior. Height below
`D_800A8CE4` selects actor Y; other values, including unordered comparisons,
retain the height field. Successful queries return one.

The actual literals are **0x38D1B717** (approximately 1e-4) and **0xC6147000**
(-9500). The source keeps the original global reads. `func_15143E08` has its
real **s32** return and `struct127 *` argument; the root narrows its result to
a byte. `func_151423D8` accepts a byte and returns a float. Complete original
**seven- and 27-word helpers** are checked against the live ELF before use.
Native static layout checks verify the recovered actor/state/record offsets.

The first private source emitted 92 words/frame0x48. Removing the unnecessary
height temporary and expressing the owner/parameter fields with real types
recovers frame0x40. A volatile-pointer experiment happens to emit 94 words but
is not the canonical source. The adopted implementation has **no volatile
local**. The existing fabsf intrinsic declaration preserves inline ABS.S;
SQRT.S remains inline through the existing SDK profile.

## Guard normalization and independent proof

IDO folds the derived parameter address into state+0x68 and retains that base
across callbacks. Retail instead caches state+0x58 before the attachment gate
and later reads +0x10. The two added instructions restore that derived address
and its original private home. Each padder supports one insertion per guarded
source slot, so the packet distributes the address/store/actor-load schedule
across two adjacent expected-word guards. No padder API is extended.

An independent symbolic interpreter executes the actual **92-word C** and
**94-word original** streams. It does not use the guard map as a transfer
template. All **13 paths** have identical ordered public accesses, helper
arguments, return values, saved-register/frame behavior, and ordered floating
operations with abstract FCSR effects. Callbacks may change public memory,
incoming mode homes, caller-saved registers and FCSR. Four effective controls
reject multiply-operand reversal, wrong offset sign, a changed height address,
and an incorrect derived parameter address. **99 word/binding corruption
controls** reject all compiled-word and relocation changes.

The proof assumes mapped storage and public outputs outside the callee's
unpassed private frame; providers do not inspect implementation PCs or locals.
Raw C and retail private local bytes are **not equated**. Their layouts differ
before normalization. Exact guarded instruction identity restores the original
private accesses. Raw asynchronous fault-register identity and a numerical
hardware FCSR emulator remain outside these claims.

## Fresh qualification

- **1,827 finite cases per stream / three streams** compare retail, raw C and
  guarded instructions with an independent scalar reference. They cover both
  attachment outcomes, modes including full incoming words, normalization
  thresholds, height boundaries, callback mutations and seven output aliases.
  Public memory, ordered accesses, calls and ordered root FP operations agree.
- **504 exceptional modeled cases per stream** exercise infinities, quiet NaN
  payloads, signed zero and subnormal inputs under two explicit NaN-priority
  rules. This is modeled instruction evidence, not hardware-FCSR acceptance.
  Six effective original-instruction controls reject behavioral changes.
- **512 cases per stream** execute both original phase helpers, covering all
  256 byte headings in both directions. Every reachable root word is exercised:
  **91/94 retail**, **88/92 raw**, **91/94 guarded**. The remaining three/four
  words are structurally unreachable duplicate slots, verified by CFG walk.
- **576 original caller-window cases per stream** execute the three direct
  calls, using **19-, 19- and seven-word** original windows. They qualify stack
  and record output destinations, all result branches, vector copies and flag
  updates. The second window's failure route deliberately sets parent V0=1;
  its branch-delay update is executed. Full parent functions remain unqualified.
- The aligned census of the complete **2,467,288-byte pristine code image**
  finds JALs at 0x1CC788 / 0x1CCD48 / 0x1CCDA0 and no literal entry-pointer
  words. This is a code-image census, not a complete asset-ROM or computed-call
  census. All three observed direct sites are included in the caller checks.
- **544 fired public memory-prefix checks / three streams** preserve the
  requested access, prior public memory/calls and prior FP operations. Private
  local locations are excluded from that relation, and scratch fault registers
  are not claimed identical.
- **761 native32 cases per configuration** pass O0/O2/O3 with strict and
  non-strict aliasing and trapping UBSan, plus **12 effective compiled source
  controls**. Native checks use actual typed actor/state objects and a separate
  three-float output. Guest output aliases and mode-home mutations are not
  represented as native C parameter mutations.

Both full-owner padders and two independent symbol rebases pass, preserving
all **38 neighbors** and normalized pools. Focused command:

```sh
python3 -m unittest tools.tests.test_game_perpendicular_offset_1519ef90_match -v
```

Fresh complete suites: **36.179 s mounted preinstall**, **40.556 s isolated
sibling overlay**, plus a separate installed-source pass. `make tools-check`
passes. Ten task files are tested through an ignored overlay; the sibling's
HEAD, exact Windows status digest and **2,434 prior dirty paths** remain fixed.
Unchanged neighbor suites are reused through exact source/object/image
identity, not represented as fresh tests. Claude calls: **zero**.

## Production audit and progress

The private audit executes all five actual Make recipe commands and links the
complete image. Production rebuilds with:

```sh
make -C conker -j4 -o Makefile -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

Independent whole-file prediction accounts for **292 changed ELF bytes**:
target body/size and the order of the two symbol-table labels `D_800A8CE0` /
`D_800968B0`. Those labels retain their names, addresses and extents. The exact
metadata permutation is separately pinned; there are **zero exclusions**.
All **6,050 other linked functions** and every function address remain fixed.
All **189,088 protected data bytes** are unchanged. Of **698 objects**, only
the target owner changes; all 38 neighbors, prior pools and existing guards stay
fixed. The **873-input** audit changes exactly source, guards, owner object and
ELF, retaining **869 other inputs**. The conversion CSV is unchanged. Production
ELF equals the independently predicted image, SHA-256:
`9e5b3641603fd1cad25dbb595fd17cf2107699a8eeee62eaf32a4b07651eb6d4`.
The existing duplicate generated_12D630 recipe warning is unchanged.

Actual recount: total **4,509 / 5,514 (81.77%)**, Game **3,836 / 4,841 (79.24%)**,
Init **492 / 492**, Debugger **181 / 181**, **zero address drift**, **1,005 still
different**. Converted totals remain **5,514 / 6,048 (91.17%) / 86.19% bytes**.
The 85% total goal stays active: **178** more matches at this denominator.

Evidence is retained in `conker/build/game-perpendicular-offset-1519ef90-private/`:
frozen inputs, rejected source/layout probes, both manifests, full proof/guest/
native/caller/prefix reports, padder outputs/rebases, three suite logs, actual
Make commands, strict image, production audit, recount and sibling/graph audits.
The historical `private` folder suffix does not mean the adopted body is still
uninstalled. Nine-file scoped AST refresh retains all **62,128 prior IDs**;
it is not full-corpus extraction. Five DOCS indexes get one concise entry;
the root README changes aggregate rows only. The sibling host folder still has
only `.codex` and `recomp_scene`; no host build applies. Frozen Release, saves
and private inputs remain untouched. No push.

Next: **`func_1519F1C8`**, the **124-word** zero-return parent in the same owner,
VA `0x1519F1C8..0x1519F3B8`, ROM `0x1CC678..0x1CC868`. Its side-offset query
dependency is now exact. Recover the complete parent and its interface, then
qualify its callers, frame, packet/state effects and strict image before credit.
The existing small selector/copy callers in Notes 121/122 and linked-state
refresh in Note 1975 provide starting context, not fresh qualification.
