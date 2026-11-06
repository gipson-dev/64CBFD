# Matrix-batch draw matched with recovered frame and closed reorganization

Date: 2026-11-06. Continues [Note 2134](2134-game-three-row-table-payload-constructor-direct-match-20261106.md)
from consumer `6497106283d0aa5af12d4d3134b6186f1850bd25` and mounted tools
`f90c8c0e38fcc6a1e53698cb7874f04f1441c73d` toward the active 80% goal.

## Recovered body and interface

`func_151897A4` in `conker/src/game/generated_1B5CC0.c` now has a complete
semantic C body. All **71 words / 284 bytes match after 30 derived guards**;
raw C retains 30 word differences. VA `0x151897A4..0x151898C0`, ROM
`0x1B6C54..0x1B6D70`, no alignment tail. The default O2/g3/MIPS2/O32 profile
is unchanged. The proper interface returns Gfx* and receives a Gfx cursor,
20-byte local draw-record view and signed16 view index. The helper receives
a descriptor pointer, Mtx pointer, full-word signed view index and two zero
words in addition to the cursor. Its original LW of the view's home proves
the full-word helper argument; the earlier short prototype caused two
redundant sign-extension words inside the loop.

Count byte+2 zero returns the original cursor before reading other fields or
the global. Otherwise count, opacity step byte+3, matrix start from
D_800BE9C0*stride byte+1, and original descriptor byte+0x8A are captured. Each
iteration stores the fixed-point opacity high byte, reloads the live actor
pointer+0x10 and matrix buffer+8, submits matrix[start+index], and retains
the returned cursor. The source uses explicit integer<<6 before converting
the byte address to Mtx*: this preserves retail's element index increment,
rather than strength-reducing it to a running byte offset. Opacity begins
at step*96 and advances by step*32. Final restoration uses the final reloaded
actor pointer, including provider changes to that pointer.

All byte inputs are 0..255. The largest matrix index used is 65,279;
the post-loop index is at most 65,280. Opacity arithmetic stays positive
and below 2,105,281, so the signed shifts and additions do not overflow.
The source contains no inline ASM or frame padding. Shared headers and
original retail ASM are unchanged. All 14 raw/padded neighboring bodies
remain fixed. Raw .reginfo adds only S5/S6/S7 (A31FDFFE to A3FFDFFE);
every other raw pool byte/binding is fixed. Production padded data and all
register metadata remain byte-identical. All **112 frozen inputs** are audited.

## Frame provenance and the 30-word derivation

The exact frame is **0x68**, with S0..S7/RA saved at+0x1C..0x3C and the
original opacity word at+0x44. Three earlier source shapes were measured,
not installed: the initial frame0x58, an early-home shape frame0x48, and the
recovered frame0x68. Fingerprint-locked, read-only CFE/UOPT/UGEN observations
run only in owned compiler children; each producer, consumer and driver
terminates successfully and reproduces the normal complete-owner target.
The selected source has CFE M40 -> UOPT M36, rounded local reservation40,
saved area40 and outgoing area24: **40+40+24=104**. Its live saved-opacity
home is M-36, giving SP+0x44. Genuine step/start/next/count captures establish
this layout; unused declarations, fake arrays and frame-word patches are absent.

The normalizer accepts the exact complete raw body and all three bindings,
then derives its output without using retail instruction words as input:

1. The first LBU zero-extends count. Its later ANDI255 is a redundant copy
   on the positive path; there is no intervening count definition or provider.
2. The stride LBU moves into a branch-likely delay slot. The zero-count path
   annuls it and takes the unchanged empty exit. The positive target moves
   from word22 to23, retaining the original unreachable sibling stride load
   at22. An unsafe non-likely branch control demonstrably reads unmapped
   stride on the zero-count fixture and is rejected.
3. The same product MFLO is split into its volatile result and saved induction
   copy. Saved and scratch register-role cycles close within their live regions.
   Index/current and bound/increment roles, final actor restore, and copy/schedule
   words are derived from the emitted operations. Frame, call and epilogue words
   stay fixed. This is a branch-delay/load and register reorganization, not a
   direct/raw-C match claim or an arbitrary retail-body replacement.

Exactly 30 expected-word/relocation rows are appended. No CSV insertion or
omission is used. The D_800BE9C0 HI16 remains at44, LO16 moves58 to5C,
and the helper JAL remains atC4. Existing guard bytes are preserved as an
exact prefix. A qualifier initially expected the raw GPR-mask change in the
padded object too; direct pool comparison showed padded metadata stays fixed,
and that stronger equality is now required.

## Caller and behavior qualification

ROM0x232054 is the sole aligned pointer to the target: D_8008D590[1].
The full four-word table matches current protected Game data. Original
func_15188D00 traverses its selected list and performs a three-argument JALR
with a sign-extended view index. Both that production parent and the large
render helper151137D4 remain unrecovered placeholders; this change earns
one function's credit. Original caller execution and opaque helper contracts
are not whole rendering/gameplay or provider-body acceptance claims.

Eight checks pass before and after installation in both actual tools copies:

- **567 guest cases per body**, across original, raw C and normalized C,
  execute 46,563 helper calls per body. All count bytes and other byte axes,
  signed16 views, all 64 provider mutation modes, live pointer changes,
  captured fields, aliasing of the record count byte, null cursor returns
  and final-pointer restoration are covered. Raw C agrees on public behavior;
  normalized output agrees on complete literal machine state and traces.
  All **69 reachable words** are visited. The unreachable sibling at22 and
  annulled positive-guard load at38 are covered structurally in the full 71 words.
- **144 private opacity/stack alias cases per body** and **96 fired access-cut
  prefixes** compare complete normalized states. Private stack aliases and
  precise fault prefixes are emitted-instruction evidence, not portable C promises.
- **384 complete original-caller cases per body** visit all **82 parent words**,
  including empty/single/two-node lists, both list selectors, live cursor flow,
  mixed callbacks and signed view values. Independent target-entry/return
  contracts are checked 256 times per body. The other callback is opaque.
- **Six independent GNU links**, three symbol layouts and **144 cases per body**
  validate all three bindings, signed-low16 carry cases and standalone zero tail.
- SDK **native32 O0/O2/O3 with UBSan** executes **3,200 cases per profile /
  9,600 positive entry executions**. Including twelve wrong variants,
  **124,800 entry calls** run. The exact three-argument entry and six-argument
  provider types, full matrix-array bounds, mutable pointers, byte captures,
  opacity/return flow and output canaries are checked. All twelve controls
  fail by checked state/result comparison (mask4095), not by sanitizer traps.
- All 284 raw byte corruptions, all three binding corruptions, a production
  expected-word guard corruption, five whole-image corruptions and the old
  three-word stub are rejected. Guard derivation also pins the complete body,
  moved binding, conditional hoist, count-width invariant and live-region cycles.

Both tools smokes are fresh. Three unchanged shared suites per copy are
explicit exact-fingerprint reuses from Note 2124. The sibling uses an ignored
overlay for the five new modules and its actual helpers; six tracked edits
and 2,428 untracked files remain fixed.

One focused packet-only Claude advisory was attempted/completed through the
verified claude.ai/firstParty Pro route, with safe mode, tools=[], mcp_servers=[]
and no session persistence. Count-width, register-keyword and initialization-
order predictions were independently tested; none supplied a matching fix.
The source-derived reorganization and its tests are Codex's independent work.
No second call was made. Packet SHA:
`e9bf63e6f99ea8dddfb35e7aa728b57ad47b871c7fb6ce7a3eb9642b5a9bb167`.

## Actual production and recount

```sh
make -C conker -o retail_word_patches.us.csv -o Makefile --output-sync=target -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

Only generated_1B5CC0.c recompiles, exactly once, with zero C diagnostics.
Actual padded owner and ELF equal their independent predictions. The complete
ELF differs by **224 bytes**, with **zero exclusions or metadata permutations**:
only the target body and symbol size 12 to 284 change. All **6,052 addresses**,
conversion rows, progress.csv, Make rules and **189,088 protected data bytes
in 720 owners** remain fixed. The existing duplicate generated_12D630 recipe
warning and expected unfinished-image checksum failure remain.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,204 / 5,512 (76.27%) | 0 | 1,308 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,531 / 4,839 (72.97%) | 0 | 1,308 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**206 more** matches reach the current 4,410 threshold for 80%.

- ELF: `2d333adffe40d55c9cd604becb49ecf83af8786f61f2fbb6a517eb92df48a03c`.
- Owner: `a0b55ac12dfb56c6c76822ded23c8aea5df2aef42d6724494e01e004ec5c915b`.
- Code binary: `17caf22b30b46589f42b2afcb87fc4975b54a08d2fe8a63f7060227767409335`.
- Guard CSV: `66e044ccfd4d99b544ee362bc2db067d80e3d825bc5db9a5031c86d66e625054`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence: `conker/build/game-descriptor-record-draw-151897A4-match/`.
Tools are committed before source, guards, documents and consumer pin. Scoped
Graphify refresh retains old nodes outside changed paths; no full corpus
extraction is claimed. Root README changes aggregate rows only.

Next static target: **func_15195868**, generated_1C2C60, 71 words/frame8,
VA15195868..15195984, ROM1C2D18..1C2E34. It scans eight-byte signed-opcode
records, matches payload words against asset table D_800B0E58 (or ID 0 wildcard),
skips matching occurrences, seeks opcode -14 and counts paired markers.
Inspect all four argument types, sentinel/access order, count-output aliases,
the indexed table read and real callers before qualifying. It is uninstalled
and uncredited. Preserve unrelated work, private inputs/saves, handwritten
func_150A76F0 and frozen host Release. The full 80% goal remains active.
