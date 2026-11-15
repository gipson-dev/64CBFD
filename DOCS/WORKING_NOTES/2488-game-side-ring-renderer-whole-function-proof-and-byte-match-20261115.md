# 2488 - Side-ring renderer whole-function proof and byte match

`func_1519FE6C` is installed and matches all **632 retail words / frame 0xF0**.
Its complete typed C replaces the zero-return placeholder with the backward
three-vertex ribbon renderer: forward/backward fades, six graphics providers,
initial seed, signed texture interval, vertices, repeated segments and lookahead.
The original symbol is retained, with a descriptive renderer comment.

The actual production recount is **4,513 / 5,514 (81.85%)**, Game
**3,840 / 4,841 (79.32%)**, zero address drift, **1,001** still different.
Init remains **492 / 492** and Debugger **181 / 181** exact. Conversion rows remain
**5,514 / 6,048 (91.17%)**, **86.19%** bytes. **174** more matches reach the unchanged
85% goal (4,687 required); the goal remains active.

## Connected whole-function relation

The seven maintained component checkers from Note 2487 are now composed across
all **72 component outcomes** using actual predecessor output states. An
instruction decoder discovers live GPR/FPR/HI/LO/FCSR inputs, private reads
before writes and carried values; undefined or dead inputs cannot be silently
equated. Shared logical roles unify at each successor, including loop backedges.
Exposed sync-byte inputs are compared before opaque calls. Surviving o32 saved
registers and protected entry-frame words have explicit custody obligations.
Seven provider targets and arities are fail-closed; their recovered declarations
use integer/pointer arguments. Explicit FP-argument lanes are supported and tested.

Eight deliberately inconsistent cut fixtures are rejected at composition:
sync, vertex texture, segment position, lookahead pointer, return FCSR, fade
count, preserved F24 and a synthetic F12 provider input. Independent role naming,
scratch allocation and unreachable-word changes are positive controls. The
existing components retain their **59 effective semantic corruptions**.

Independent static CFG traversal exactly equals the union of instruction fetches:
**635 / 637** raw words and **630 / 632** retail words. Raw offsets 0x2F4/0x424 and
retail 0x420/0x9A8 are unreachable. Separate processed-entry and delay-word sets avoid
losing a delay instruction that is also a jump target. Three toy controls cover
delay targets and always/never taken likely branches. Finite guest cases alone
are not presented as complete reachable-code coverage.

The relation applies to mapped ordinary RAM, nonaliasing public/private stack,
immutable code/literals and the documented opaque o32 providers. Public aliases,
ordered writes/calls and FP opcode/operand/FCSR effects are checked. Proven stable
ordinary reads can commute or be reused; this does not establish MMIO/async
behavior, raw fault-PC/register timing, portable-C undefined inputs, gameplay or
hardware acceptance. FP traps are not assumed disabled.

## Constrained normalization and exact guards

The selected source remains **637 raw words**, frame 0xF0, S0-S3, with 621 positional
differences including five extra words. The accepted 632-word projection derives
operations from compiler words: 627 ordinary projections, four proved byte-mask
elisions to retained moves and one private halfword reload to its retained move.
It selects 628 unique source words, omits nine provenance words and duplicates
four. Allowed edits are decoded operand fields, qualified private stack offsets,
branch form/target scheduling and those five explicit elisions. Both streams
satisfy the composed relation; no wholesale retail-body copy is used.

**637 expected-word/relocation guards** cover every input position, including
unreachable words; the final five output slots are omitted, with zero insertions.
Five omitted output slots differ from the nine omitted provenance words.
All 637 word corruptions and 13 changed binding maps fail closed (**650 controls**).
The complete raw source and 13 relocations are pinned. A different scratch GPR
allocation passes the relation, so it is not a retail-word identity oracle.

Both owner padders match, preserving all **38 neighbors** and pools. Three
independent symbol rebases pass, including literal HI16 carries at 0x800AFFFC and
0x80117FF4. The compact 16-byte literal pool binds D_800A8CF4; the added epsilon
uses addend 12 (D_800A8D00), while the preceding 12 literal bytes stay fixed.
Exposed incoming-SP cursor -4 and sync -95 homes remain intact.

## Fresh production and regression evidence

Preinstall, isolated sibling and installed-state suites each pass **10 tests**.
All 18 task-file hashes stay fixed across the runs. Each freshly compiles the
complete owner and 637/639/648-word recoveries, then checks **299 guest cases per
five streams**, 299 native cases across six O0/O2/O3 alias profiles, UBSan and
twelve source controls, **128 connected allocator/dispatcher cases per stream**,
lazy pointers, component/composition/CFG checks, both padders and three rebases.
`make tools-check` also passed; no unchanged broad suite is described as fresh.
The new `_match` suite is the maintained installed-state reproduction; the old
`_recovery` suite preserves its historical strict private-input freeze. Total
elapsed times, including startup, are **94.226 s** preinstall, **90.570 s**
sibling and **96.979 s** postinstall (final unittest run itself: 93.364 s).

Isolated actual Make and the real production Make both compile the semantic
owner, apply the new CSV and link. Production uses `-o retail_word_patches.us.csv
-o Makefile` to avoid rebuilding unrelated objects solely for a global guard-file
timestamp; the changed owner still reads that CSV in its actual recipe. No
prebuilt object is substituted. Existing duplicate generated_12D630 recipe
warnings remain. The production ELF is byte-identical to the independent image.

The strict prediction accounts for all **1,857 changed ELF bytes**, with **zero
exclusions**: target instructions/size plus a closed GNU metadata permutation
of D_800429B0,D_800D2DB0,D_80085EB0,D_800859A0 to
D_800859A0,D_800429B0,D_800D2DB0,D_80085EB0, with equal named definitions.
All **6,050 other linked functions/addresses**, 697 other objects and 38 owner
neighbors stay fixed. All **189,088 protected bytes** remain exact. Of the
immutable 881 frozen inputs, only the declared C/CSV/owner object/ELF four change;
877 stay fixed. Existing guard bytes and progress classification rows are unchanged.

The sibling Tools HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 2,434 dirty
paths are preserved by an isolated 18-file overlay. The adjacent 64CBFDOGL directory
currently has no .git or src tree, so no host source adoption/build was possible;
retained captures, Release artifacts and saves were untouched.

One packet-only Claude Pro advisory was attempted/completed, with tools=[] and
mcp_servers=[], no edits, fallback or auth change. Packet SHA-256:
d19d184852da0ba4c5ab5560364c450d193d7c7a5f281cc6bf7b4a0b785604a8.
Its FP-argument concern was not a demonstrated renderer defect (all real targets
use integer/pointer args); explicit fail-closed signatures and a synthetic F12
control were added. Saved-frame checks already existed; explicit surviving saved
state demands and an effective F24 bad-cut control close the generic concern.
Both findings were independently reconciled. No second advisory was used.

Production ELF SHA-256:
`0612730947bf3afe8477fa4ba1ea8410b91ab7d484056df259a11b926d282510`.
Protected data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Raw source SHA-256:
`4f1d014df4dccc1d394183098667e837cda18e904d9992ad952a134af72b9b0a`.
Receipts: `conker/build/game-side-ring-renderer-1519fe6c-private/frame-2488/`.
The 881-input baseline remains immutable; adoption-plan.json records only the
four audited overrides instead of refreezing history.

```sh
python3 -m unittest tools.tests.test_game_side_ring_renderer_1519fe6c_match -v
make tools-check
make -C conker match-progress NON_MATCHING=1
```

The native Graphify update failed closed (62,657 existing vs 26,747 proposed
nodes). No force or upgrade was used. Scoped AST extraction of 17 files retained
all 62,657 prior IDs and produced 62,699 nodes / 117,658 links, including the
explicit matching-module-to-target reference. This is not a full-corpus
re-extraction. Commit-hook retention is checked separately before final banking.

Next: `func_151A0C0C`, the next unmatched owner stub (141 words / frame 0x80).
The intervening func_151A084C is already exact. Recover its complete caller ABI
and behavior before fitting or credit; preserve this renderer checkpoint.
