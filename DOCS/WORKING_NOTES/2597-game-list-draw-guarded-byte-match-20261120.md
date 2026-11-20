# Note 2597: Flare draw guarded byte match

Date: 2026-11-20. Consumer baseline `c3058e9d1aa5f0f6465302b8efd64796b4b20b8d`;
tools baseline `960493de889983dc907fafcea04ae69725df3e66`.
Qualified tools commit: `0eb259f38314ecdfe7df23e503c527d0fe137ff4`.

`func_1517E4A8` is installed as complete semantic C, replacing its zero-return
placeholder. Its **361-word / 1,444-byte body and original 184-byte frame** now
match retail after **162 expected-word and binding guards**. The existing
O2/g3 compiler profile is unchanged. The helper `func_15095A48` now declares and
returns its graphics cursor correctly; its complete padded owner is unchanged.

Fresh production recount: **4,581 / 5,528 (82.87%)** total and
**3,908 / 4,855 (80.49%)** Game, zero address drift and 947 still different.
Init 492/492 and Debugger 181/181 remain exact. **118 more** are needed for
85% at this denominator; the wider goal stays active. Conversion counts and
the entire progress CSV remain unchanged because the old placeholder was
already classified as C. Root README changes only its two aggregate match rows.

## Source and closed derivation

Owner `conker/src/game/generated_1AB530.c`, VA `0x1517E4A8..0x1517EA4C`, ROM
`0x1AB958..0x1ABEFC`. The typed seven-argument interface, 20-byte packet,
intensity/brightness smoothing, viewport gates, texture setup, palette sprites
and pipe-sync commands are the complete recovery described in
[Note 2596](2596-game-list-draw-private-recovery-20261120.md).
The sole aligned direct caller remains ROM `0x1AB8F8`; computed callers remain
unexcluded. The seven owner neighbors and all 19 raw helper-owner functions,
bindings and pools remain identical. All eight functions in this owner are now
byte-exact in the production ELF. No speculative packet initialization was added.

Raw source SHA-256 remains
`2353a48952e6704d107ac718cd215cb7c5d88b7fa70ff864249ef962434a0a15`:
361 words/frame 184, with 162 positional linked differences before normalization.
The executable derivation consumes only this raw payload and its exact binding
map. It does not read retail bytes or original assembly to generate output.
It retains **359 unique source origins**, omits source 42's unreachable duplicate
truncation and source 85's alternative intensity load, and adds a delay NOP plus
one unreachable duplicate SLT. The surviving intensity load moves to the common
continuation, preserving dynamic read multiplicity. Register roles, two modular
negated differences, one commutative sum, branch/likely scheduling and the two
counter-home accesses are derived explicitly. Branch displacements and moved
relocations follow their source origins.

The raw counter spill/reload at words 302/338 uses SP+0xA0; normalized retail
uses SP+0xB0. Both are unpassed private homes, disjoint from the packet at
SP+0x7C, the saved registers and incoming arguments. No frame-size guard is used.
Because output length remains 361 words, the CSV records positional guards
without CSV insertions or omissions. The origin accounting remains in the
independent derivation and proof rather than being hidden in a body replacement.

## Fresh evidence

**23 tests pass before and after installation in each tools configuration**:
nine draw tests plus six unlink and eight renderer tests. All
**348 imported Python fingerprints** agree. The overlay contains
**1071 files**: 347 matching sibling files,
714 primary fallbacks, nine task files and
one bootstrap. It is a hybrid overlay. The actual dirty sibling retains its
HEAD, exact status and **351 dependency fingerprints.

- Instruction-driven prefix relation: 432 null-intensity and 6,048 non-null
  paths per palette group, groups 0/1. Symbolic one-iteration relations cover
  arbitrary index/count values and both exit/continue outcomes; explicit
  recurrence assertions close the loop invariant. Fifty-six concrete iterations
  also exercise every valid index for counts 1..7 in both groups.
- The relation compares public stores, public read multiplicity, complete call
  arguments, executed FP operation order, control/rounding, sticky flags, cause
  and FCC. All 212 private/incoming bytes agree at calls and exits modulo only
  the two unpassed counter homes. Providers can change public state, retain and
  mutate the exposed packet, change FP control/rounding and clobber o32 volatile
  registers. Saved GPR/FPR/SP/RA restoration and home contents are checked.
- Each stream visits **352/361 words** in the symbolic proof. Its nine unseen
  words are explicitly accounted for: three structurally unreachable words,
  two unreachable constant-divisor overflow-test words, and four BREAK words
  outside the normal division domain. This supersedes the finite corpus's
  earlier unclassified 14-word coverage gap.
- Nine effective semantic controls reject a bad cutoff, brightness numerator,
  setup argument, saved return home, packet pointer, alpha byte, FP operation,
  counter home and pipe-sync word. A T0/T1 reallocation remains accepted.
  The conservative affine nonoverlap rule passes 4,563 independent range checks;
  unrelated unknown bases are never assumed disjoint.
- Independent GNU assembly and two distinct code/data/entry rebases agree on
  the full derived payload and bindings. Both padders reject all **162 word**
  and **12 relocation** corruption controls each.
- Raw C and normalized guest suites each pass 1,104 cases and 953 logical calls,
  with the complete 24-word retail INIT and 18-word draw wrapper connected.
  The normalized stream has **complete final guest memory equality in all
  1,104 cases**, closing the raw stream's two-home difference. Native SDK32
  O0/O2/O3 each pass 1,104 defined cases with strict aliasing and UBSan;
  three source controls and three concrete instruction controls remain effective.
- Both owner padders agree. Actual Make runs three natural commands per owner
  and reproduces both complete objects. The helper's entire padded object is
  byte-identical. Shared tools checks pass. Historical unlink/renderer fixtures
  accept only exact new source/guard snapshots and reconstruct their original
  sources and guard archives; their earlier full-image predictions stay unchanged.

## Whole image, production and limits

The complete predicted ELF matches the privately linked image and fresh
production ELF **byte for byte with zero exclusions**. Exactly **1,068 bytes**
change from the frozen baseline: the restored target instructions and its size,
plus two closed symbol/string permutations. The two functions `func_15005C80`
and `func_151F6970` swap serialization order; the three data names `D_800A131C`,
`D_800AA7CC`, `D_800AEB7C` rotate to `D_800AEB7C`, `D_800A131C`, `D_800AA7CC`.
The permutations preserve every named definition; the target's size change is
accounted for separately. No metadata section is excluded.
All 6,051 function slots are retained. Protected Game data remains exactly
189,088 bytes across 720 owners, with no changed bytes or owners.
The 2162 frozen inputs are checked against the explicit task plan.
The full build retains the existing duplicate-recipe warning for
`generated_12D630`; neither qualified owner introduces compiler diagnostics.

Production ELF SHA-256: `c671669f4bc135776b39bb19bac50daf4b286e95966a0aa5d2ed7e5b860885b2`.

These are normal-execution gates with mapped/aligned quiet ordinary memory,
valid private stack, no public/private or literal alias, normal implemented FP
operations with traps disabled, and normal nonzero/nonoverflow division.
The prefix proof covers groups 0/1; the symbolic loop requires readable palette
addresses. Providers cannot inspect code PCs, unpassed homes or nonargument
registers. Raw fault-prefix/interrupt state, arbitrary trapping FP behavior,
complete downstream rendering, hardware and gameplay acceptance are not claimed.
The finite native/guest domain remains separately bounded as in Note 2596.

The legacy `64CBFDOGL` path has no applicable Git/source checkout in this
workspace snapshot. No host files, Release artifacts, ROM inputs or saves change.
Graphify receives a scoped eight-source installed-match refresh with old
node/qualification retention. The native incremental command refused to replace
the 68,864-node graph with a smaller 27,425-node scan and preserved the original
graph; the scoped AST merge supplements that retained corpus. This is not a
full-corpus re-extraction. Zero Claude calls; no push.

Reproduce from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_list_draw_1517e4a8_match -v
python3 -m unittest tools.tests.test_game_list_unlink_1517e134_match tools.tests.test_game_list_render_1517e28c_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

Continue with `func_150F97EC`, owner `generated_124920`, VA `0x150F97EC`, ROM
`0x126C9C`, **89 words / frame 112**. Its current body remains a placeholder;
the complete retail body has a state-pointer gate, matrix/vector helper call,
three real RNG calls, two integer RNG calls and an effect submission. Recover
its full typed interface and packet before matching; it has no new credit.
The aligned direct-call census finds ROM `0x55DC0` and no aligned literal
pointer; computed callers remain unexcluded.

The smaller shortlist entries need classification work: `func_150AE280` begins
with a handwritten stack restore/jump into the preceding routine and also
contains an unlabeled ordinary entry at `0x150AE2A0`; `func_150A6760` contains
the global internal loop entry `func_150A67D0`; `func_150A70C0` is explicitly
handwritten with a nonstandard saved-register lifetime. Do not treat their
whole catalog slots as ordinary independent compiler-generated C functions.
Preserve the historical renderer/unlink/draw archives and apply the same
source/ABI/object/image gates to each next recovery.
