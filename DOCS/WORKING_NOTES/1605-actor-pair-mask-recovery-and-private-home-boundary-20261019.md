# Actor Pair Mask Recovery And Private Home Boundary

Date: 2026-10-19

## Scope And Result

Continue `func_1508C1A4` after
[Note1604](1604-mode-context-initializer-complete-match-20261019.md).
Retail is261 words/1,044 bytes, frame168, VA1508C1A4..1508C5B8,
ROM B9654..B9A68. Production still contains its12-byte zero-return C stub.
The complete experimental body now emits **261 words/frame168/225 word
differences**, without compiler diagnostics, under both existing owner
profiles. It is **not installed and not byte-exact**.

Consumer predecessor87240c78 and tools predecessor23cce29 were clean.
Tools **8361e6f** is committed first, then the consumer documentation/pin.
No push, host/frozen Release operation, dependency change, REA setup or
Claude call is involved. Zero advisory calls suffice for this bounded
source/assembly/compiler/ABI qualification.

## Recovered Contract

Keep the original symbol name with a concise pair-mask comment. The
higher-level subsystem name is not established here. Recover the two signed
32-bit arguments and **void return** from the full routine and both actual
caller windows in `func_1508C5B8`; neither caller consumes V0 as a result.

Both actor lookups execute, even if the first returns NULL. Clear bits12..15
only in the lookup keys using FFFF0FFF; retain the original full-word indices
for the later rows and shift counts. No index clamp or invented early return
is added. A missing actor leaves the context masks alone.

The reference source is not imported unchanged: its s32 coordinate loads,
word-sized byte flags, float-valued signed-halfword fields and17-argument
collision call are wrong. Assembly establishes float positions14/18/1C,
u8 active/type fields84/75, signed16 height114 and fallback coordinates
1A4/1A6/1A8. The real collision interface is **15 arguments**: six float
components, two zero integers, three pointer-output addresses, a distance
output, two zero integers and zero float. Its third/fourth floats occupy
O32 A2/A3; no nested pointer or active flag is passed there.

For each endpoint, prefer active height `y + signedHeight*0.75`, subtracting
50 when the low seven type bits equal9. Otherwise type1F uses y+80. Otherwise
an active opposite endpoint and a signed mode-table value other than-1 select
the signed16 coordinates; the remaining case uses y+40. Preserve the actual
table access gates and signed mode. Do not reinterpret the cached first-active
byte as a newly loaded flag for the second endpoint.

Compute float32 delta and rounded squared-distance sum before sqrt. A zero
collision result or **distance strictly less than hit distance** sets the
query-clear flag. Only then run the five-float restored barrier routine.
A strictly positive barrier result clears the low-mask flag, **not** the
query-clear flag. Thus the high mask can still be set when the low mask is
blocked. NaN/equality behavior follows those ordered comparisons.

OR symmetric low1 and high10000 masks into context+16C0, reloading the
context before each row update. Preserve existing bits, same-row overlap and
the real context-pointer alias. Explicit unsigned shift masks cover all32
MIPS shift counts without claiming portable signed-shift behavior.

## Source Shape Recovery

The initial corrected complete body emits258/frame184/257 differences.
Its signed-row-offset control is identical; implicit shifts emit254/frame184
but are not selected as a portable replacement for the masked shifts.
Eleven bounded source/declaration screens are retained:

- Single live clear flag:259/frame184/240 differences.
- Split query-result branches alone:260/frame184/257 differences.
- Both:261/frame184/237 differences.
- Remove redundant coordinate copies from the live-flag form:259/frame168/234.
- Add split query-result branches:261/frame168/230.
- Declare the real clear flag before query-clear: **261/frame168/225**, selected.
- Two scalar-declaration moves retain261/frame168 with225/224 differences.
  These remain diagnostics, not evidence of private or complete word identity.

The selected source directly recovers frame168, RA at44, incoming homesA8/AC,
both flag homesA4/A0 and the first actor home9C. No dummy storage, volatile,
physical-register binding, frame patch or word guard is introduced.

```text
Initial raw:  bb9a0503096f55686774936a1a953be6d0051959b1b8f785736f65471fa2fd6e
Selected raw: 47c32436c59af38d13f62bf3a2e5ab11f07d3b25ad6b3b0fd33c378bf4c6de16
```

## Fresh Qualification

All **eight tests pass in46.439s**, no skips:

- 430 fixtures/860 retail/raw public pairs across two stack phases. Compare
  every public byte, ordered stores and full logical provider arguments.
  Cover all256 signed mode bytes, all32 shift counts, signed field extremes,
  missing actors, both height paths, equality/NaN/infinity query/barrier gates,
  provider mutations, overlapping rows and a completed live context alias.
- Native32 O0/O2/O3 with UBSan, complete buffers and ordered provider calls.
  Nine effective negatives catch key masking, unsigned height/coordinates,
  wrong type mask/query ABI, inclusive hit equality, clearing both flags,
  zero-inclusive barrier rejection and cached context. The context alias is
  backed and completed natively too; private-frame aliases are not claimed.
- 12 runs execute the actual55-word actor lookup, including backed inactive
  records in its unrolled scan. Eight runs execute the207-word
  restored barrier function with empty/crossing graphs and an opaque height
  provider returning category2. The large collision query remains opaque.
- 32 actual returning-caller runs execute the first window's delayed mask
  store and both JALs. Every instruction-fetch stop at1508C7E4/1508C958 fires;
  check arguments, returned public effects, SP and saved GP/FP state. This
  is not acceptance of the complete pair scheduler or gameplay.
- Three independently assembled GNU maps/36 rebased public pairs retain
  all16 bindings and include HI/LO carries. Compare raw C and original
  assembly against the independent public reference, not literal word identity.
- Both copied owner profiles and actual padding preserve all72 neighbors,
  all73 addresses and existing pools. The actual seven-command Make shadow
  reproduces both raw profiles, padded bytes and metadata with the existing
  three normal overrides intact. No production build or new guards occur.

258/261 retail words are visited. The duplicate/dead words at1508C274,
1508C2A0 and1508C300 remain explicitly unvisited. NaN helper arguments are
compared by classification, not payload/FCSR or hardware exception behavior.
Out-of-range mode probes have explicit synthetic table backing; they do not
establish actual retail array bounds. Full-word index probes that would leave
native row backing use missing actors, while completed native shifts0..31
have valid backing. No full collision-provider or complete-game claim follows.

## Matching Boundary

**Fired access13** is the first differing requested memory access: retail
stores start-Z at **SP+64**, raw C at **SP+80**, with the same168-byte frame.
Both gates fire and public state remains identical. Earlier matching memory
requests do not mean identical temporary GPR/FP state; those allocations
already differ. Public/native agreement and equal length/frame are not
permission to patch the frame or install this body as a match.

Continue this same function's scalar homes, FP/GP lifetimes, query schedule
and branch-delay layout. Preserve the independently justified mask semantics,
provider ABI, aliases and the distinction between low/high flags. Only after
complete matching/private/owner/image gates should production C, guards or
matching credit change. `func_1508C5B8` remains a later separate target.

## Preserved Baseline

All frozen production inputs, including source, Makefile, guard manifest,
ELF and progress CSV, are checked byte-for-byte unchanged. The previous full
linked audit is reused by identical ELF/input fingerprints, not called a new
production rebuild. Shared `make tools-check`, whitespace and Python syntax
checks in both tools copies pass. Three absent task files were copied to the
standalone mirror; HEAD ddbdd16 and all1,404 pre-existing dirty leaf hashes
remain fixed, with no mirror commit/reset/stash/clean.

Fresh matching is unchanged: **Game3013/4832 (62.36%)**, **total3686/5505
(66.96%)**,1,819 different/zero drift; owner65/73 exact. Conversion remains
5505/6044 (91.08%),86.08% bytes. Root README is unchanged. Exact predecessor
fingerprints remain those in Note1604; no matching credit is assigned here.

```sh
python3 -m tools.experiments.game_actor_pair_visibility_candidates --screens
python3 -m unittest tools.tests.test_game_actor_pair_visibility_recovery -v
python3 -m tools.match_progress conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
make tools-check
```

Ignored source/profile screens, frozen inputs, native/private/helper/caller/
GNU/owner/Make receipts and graph evidence belong under
`conker/build/game-actor-pair-visibility/`. The current selected receipt is
`recovery/selected.json`; earlier top-level `selected` files describe the
initial258-word screen and are not the accepted current candidate.
