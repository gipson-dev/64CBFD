# 1804 - Scene-state reset callback: direct C match

Verified: 2026-10-29. `func_151E327C` replaces its false zero-return placeholder
with the recovered scene reset and transition callback in
[`generated_20AE20.c`](../../conker/src/game/generated_20AE20.c).

## Accepted result

- VA `0x151E327C..0x151E3344`; ROM `0x21072C..0x2107F4`.
- All 50 words / 200 bytes emit directly from C, frame 32, 32 external
  bindings, no alignment words and **no new guards**.
- The complete owner has 60 functions. All 59 neighbors, normalized pools,
  existing guard bytes and the actual three-command Make path are preserved.
- Live ELF recount: Total **3,882 / 5,506 (70.51%)**, Game **3,209 / 4,833
  (66.40%)**, Init 492/492 and Debugger 181/181. Zero address drift;
  1,624 still different. **248 more** exact C functions are needed to reach
  4,130/5,506 and the 75% goal. This is one new match, not a new C inventory row.

## Recovered behavior and interface

`void func_151E327C(void)` initializes the scene flags, chooses `3` or `0x33`
from bit `0x200` of `D_800E9D00`, and submits
`func_1501C730(6, D_800BE3DF, D_800BE3E0, 0, 1)`. The scene selector is a
signed byte; the next selector is unsigned. After that call it sets
`D_800E0B99` and `D_800E0BB1`, then invokes `func_151E7EF8`.

The write to `D_8008FD94` changes **only its first representation byte**;
its shared word declaration stays intact. Signed character views recover the
retail common constant and scheduling at this field, `D_800BE618` and
`D_800E0BB1`. A full word assignment is wrong. Native checks compare object
bytes instead of treating the first byte as the same logical word lane on
little- and big-endian machines. No volatile qualifiers, artificial padding
or assembly replacement were introduced.

The original `func_151DFF38` materializes the callback at `0x151E0250/260`
and stores it in `D_800E0A88` at `0x151E0278`. The original
`func_151E4EE8` loads that slot at `0x151E5014/18` and invokes it with
`jalr` at `0x151E501C`; its result is ignored. Qualification covers the
30-word registration window and eight-word dispatch/epilogue window, not
the complete parents. Both parent C bodies remain placeholders. A complete
aligned ROM scan contains no direct JAL or full pointer word for this callback.

The original `func_1501C730` consumes five full words. Jump-table entry six
at `0x800969B8` reaches `0x1501C784`, storing both trailing parameters and
the signed scene/unsigned channel values. Its current C provider remains an
unrecovered zero-return placeholder; the local typed declaration captures
the used call interface and ignored result, without claiming provider recovery.
All pre-existing calls in this owner still emit unchanged words and bindings.

The existing integrity routines `func_151E7E9C` and `func_151E7EF8` remain
unchanged. Their original guest code selects the platform mode, sums 749
code words and compares against `0xBFC924E3`. The original checksum pass
and a private corrupted-fixture failure are tested. The failure-side write
to the private fixture for `osSpTaskLoad` is modeled; production integrity
code and data are not changed. This is bounded guest validation, not native
execution of code-as-data or a hardware/gameplay acceptance claim.

## Qualification

Canonical target tests passed all eight methods in both the tools submodule
and the older standalone tools mirror. Shared tools checks passed in both.

- 624 direct guest cases: every signed/unsigned selector byte, all 32 single
  flag bits, both stack phases, call mutations, partial-word/array canaries,
  call-boundary state and all 50 target instructions.
- 16 connected original-helper cases: 39/74 transition words on command six,
  26/26 integrity words and 23/23 mode-selector words. Other transition
  commands are outside this callback's scope.
- Four original registration cases and 32 indirect dispatch cases; two
  effective callback-route negative controls. No fabricated current C caller.
- 16,384 native32 SDK cases per `-O0`, `-O2` and `-O3` profile, with trapping
  UBSan, valid objects, byte preservation and 12 effective semantic controls.
- The same 12 semantic changes compile under IDO and each has an observable
  failing witness; incidental faults, private stack bytes and unused return
  values are not used to distinguish them.
- 156 guest access-fault prefix pairs, including eight delay-slot cuts;
  complete registers, memory, trace and PC are compared. No portable C fault
  semantics are inferred.
- Three independent GNU link layouts / 96 cases, including signed-low address
  carries. Original, selected and actual Make objects agree. All 50 raw-word
  corruptions and all 32 binding corruptions are rejected.
- Sixteen whole-image corruption controls, including protected data, symbol
  records/strings, size, neighboring code, ELF header and truncation.

After installation, both tools copies passed two fresh owner/image checks.
Six unchanged semantic checks per copy are explicitly reused through exact
source, module, input and artifact fingerprints; they are not reported as
fresh installed runs.

## Independent image and preservation audit

Production `make -C conker -j4 -o retail_word_patches.us.csv -o
retail_layout.us.txt build/conker.us.elf progress.csv` reproduced the private
image exactly. All 6,056 disassembly function addresses and all 6,055 other
bodies are preserved, along with 189,088 protected Game bytes across 720 owners.

The complete ELF changes 205 bytes: 174 target bytes, one function-size byte
and a closed 30-byte serialization change. The four existing symbol/string
records rotate from `D_800E0B99, D_80099324, D_800A3624, D_8009ED24` to
`D_80099324, D_800A3624, D_8009ED24, D_800E0B99`. Every named definition and
the complete fixed-width records/strings are checked. **No image exclusions**
or symbol-table-wide allowance are used.

The qualification freezes 467 focused inputs and audits a 16,526-path seal.
The independently dirty mirror retains all 1,853 inherited paths and gains
only these three qualified modules; it is not committed. Sibling host/editor
projects and frozen Release outputs are outside this change.

| Artifact | SHA-256 |
| --- | --- |
| Raw selected/original body | `0d9d961ab77b9360b94e2744fa4734d54a27b7ab2f100dc8c107e04b064bb66e` |
| Retail linked slot | `4cbe3654f97806718f6304c10b86c7c23a921aafb1eadb0141257481210e47c1` |
| Installed source | `728e128a1ecb9a650407b059c1fdbea73519b910d34c6401ad545ec45261295e` |
| Padded owner | `70e02239ea55903466507e2f1a1a263b6c5535643578db9fc93c210e2986dbdb` |
| Accepted ELF | `3676b6521dfc597c66c7bfb24b009cba4b2d23854e8fa8064ac6bb41f5facff7` |
| Unchanged native guard CSV | `1678dac601e1def3df3c6438b7a8b4bb0914ce5ef73a929921f12916f7ead9f2` |

Evidence is retained under `conker/build/game-scene-state-reset-match/`.
The initial isolated candidate failed; signed byte views produced the exact
variant. Preparation also caught a copied fixture entry address and the
closed metadata rotation. The first private image-corruption test incorrectly
treated a BSS symbol as file-backed data; it was corrected to check that
symbol's record and protected jump-table bytes. The final canonical run
also requalifies the exact module bytes after removing one trailing blank
line. Failed receipts remain separate from accepted evidence.

Tools were committed first as `83a89e9366bfd24e7b83104790c86ce53e4acb4f`.
The consumer commit contains this source, tools pin and documentation only;
no push is performed. Root README changes are the two aggregate matching rows.
The scoped graph refresh preserves old nodes and valid relationships, retires
the two obsolete target `s32` return relationships, and records bounded
assembly callback routes separately from current C calls. It does not claim
a full-corpus extraction or recomputed global clustering.

## Continue

Next inspect `func_150E3208` in `generated_1104D0.c` (50 words). Its queue
entry is a screen, not ABI or semantic qualification. `func_1514E920` remains
parked and uncredited. The 75% goal remains active.
