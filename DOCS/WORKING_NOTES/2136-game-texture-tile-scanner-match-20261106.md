# Display-list texture scanner matched with closed register roles

Date: 2026-11-06. Continues [Note 2135](2135-game-matrix-batch-draw-match-and-frame-provenance-20261106.md)
from consumer `1af80fe06ce584917494a86dffc1408718be571a` and mounted tools
`03d55e34fb79b7cadd62afe0218e5e91e87db8ed` toward the active 80% goal.

## Recovered function and display-list meaning

`func_15195868` in `conker/src/game/generated_1C2C60.c` now has a complete
semantic C body and a four-argument interface: byte-addressed display list,
full-word asset ID, signed occurrence selector, and word-sized tile-count
output. It returns the selected command index or -1. All **71 words / 284
bytes match after 28 derived guards**. Raw C remains 28 words different.
VA `0x15195868..0x15195984`, ROM `0x1C2D18..0x1C2E34`, no alignment tail;
frame **0x08**, S0 saved/restored at SP+4. Default O2/g3/MIPS2/O32 is unchanged.

The SDK opcodes identify a texture display-list scanner, refining the initial
generic asset-command description in Note 2135. Signed byte -3 is G_SETTIMG,
-33 is G_ENDDL, -14 is G_SETTILESIZE, and -11 is G_SETTILE. The source uses
these named SDK constants. Each command is eight bytes; its second word is
compared with resource-address table D_800B0E58[assetId]. ID zero is a wildcard,
but **the table word is still read before that wildcard test**. G_ENDDL returns
-1 without accessing the table. Count output resets before the first command
read, including when it aliases a command or table word.

Matching texture occurrences are skipped while the old signed selector is
positive. The selected occurrence then scans to G_SETTILESIZE, returns that
index, and counts adjacent pairs. Every step increments the output count and
reads both following command bytes. Iteration continues only for
(G_SETTILE, G_SETTILESIZE). The second byte is read even when the first fails;
its retail load occupies a non-likely branch delay slot. Native fixtures have
finite valid streams, accessible terminal pairs, aligned words and valid
resource indices. Sparse full-word guest indices and integer wrap boundaries
are guest-machine evidence, not portable C array/overflow guarantees.

## Source fitting and input-derived normalization

The first typed-record draft strength-reduced indexed access into pointers,
emitting 58 words. Byte-addressed while loops restored the indexed scan; the
separate word-array payload expression recovers the full 71-word body. Reversed
resource/payload equality preserves retail's actual payload-then-table load
order. All rejected draft sources/objects remain in ignored build storage.
No inline ASM, frame padding, compiler-profile changes or retail instruction
array appears in the production C.

The normalizer takes only the fingerprinted **complete C-emitted body and its
two bindings**. It closes scratch-register live regions and commutes seven
equality/inequality operand pairs. Every opcode, immediate, branch displacement,
memory-access order, saved register, frame word, function extent and binding
stays fixed. It neither inserts nor omits words. All 28 CSV rows have explicit
expected words and empty relocation sets; both HI16/LO16 bindings remain at
offsets 0x0C and 0x18. This is a guarded match, not a direct/raw-C match claim.

A must-equality dataflow proof covers **78 instruction contexts and all 71
instructions**, converging after 139 transfers. It follows both conditional
edges and each taken/annulled delay context, checks every source-register use,
and closes the result and preserved ABI at return. Equal arbitrary initial
integer registers and immutable-code guest memory maintain equal load/store
addresses, values, access order, branch decisions and fault prefixes. Retail
words are not an input to that proof or transformation. Independent literal
comparison then accepts the complete result against retail.

## Fresh qualification

Eight target methods pass before and after installation in **both actual tools
configurations**. The sibling uses an ignored overlay for five new modules and
its existing compiler/parser/oracle/native helpers. Its six tracked edits and
2,428 untracked paths remain unchanged. No Claude call was used for this routine.

- **636 cases per body**, retail, raw C and normalized output: all 256 prefix
  opcode bytes, wildcard/matching/missing textures, signed and extreme selectors,
  sparse full-word guest resource indices, six count-output aliases, both stack
  phases and all pair-ending conditions. All 71 words are reached. Raw C agrees
  on public memory/result and complete access trace; normalized full machine
  state is literally identical to retail.
- **145 fired access prefixes** compare complete normalized state. Closed-list
  and wildcard fixtures distinguish required/annulled table reads. A deliberately
  omitted final-pair delay load demonstrably avoids an unmapped read and is rejected.
- **144 cases per body** execute both original nine-word caller windows at
  0x15195B08 and 0x15195E4C, including all four arguments, output SP+0x50,
  the signed -1 return test, captured index and missing-texture delay updates.
  All window words are reached. Independent entry/return checks verify saved
  integer registers, GP/SP/FP/RA, result and count. Full parents func_15195AA8
  and func_15195DD4 remain unrecovered; these windows do not qualify their bodies.
- **Six independent GNU links**, three entry/global layouts including signed
  low16 carry, and **108 cases per body** preserve both bindings and standalone
  zero tails. The actual retail function has no tail.
- **SDK native32 O0/O2/O3 with UBSan**: 12,288 positive cases per profile,
  **36,864 positive executions** and **331,776 total scanner calls** including
  eight wrong-source controls. All controls fail by checked result/state
  comparison (mask255), not sanitizer crashes. A separate native byte/word
  reference checks complete buffers and valid output aliases with host endianness.
- All 284 raw byte corruptions, both binding corruptions, a production expected-
  word guard corruption, five full-image corruptions and the old stub are rejected.
  All **68 raw and padded neighbors**, all data pools and all register metadata
  remain byte-identical. All **105 frozen inputs** are audited.

Both tools smokes are fresh. Three unchanged shared suites per tools copy are
explicit exact-fingerprint reuses from Note 2124, not fresh broad regressions.

## Actual production and progress

```sh
make -C conker -o retail_word_patches.us.csv -o Makefile --output-sync=target -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

Only generated_1C2C60.c recompiles, exactly once, with zero C diagnostics.
Actual padded owner and ELF equal the independent predictions. The complete
ELF changes by **215 bytes**, with **zero exclusions or metadata permutations**:
only this target body and symbol size 12 to 284 change. All **6,052 function
addresses**, conversion rows, progress.csv, Make rules and **189,088 protected
Game data bytes in 720 owners** stay fixed. The existing duplicate generated_12D630
recipe warning and expected unfinished-image checksum failure remain.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,205 / 5,512 (76.29%) | 0 | 1,307 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,532 / 4,839 (72.99%) | 0 | 1,307 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**205 more** matches reach the current 4,410 threshold for 80%.

- ELF: `87dea8d709b296170b7aa059bf1c5536b12f81aa8b31776a0c9e558ce38da2a1`.
- Owner: `53ffe94098e3181db9c253495e46a6956b35ad03001f922080a689ce80efe145`.
- Code binary: `144d901556044dfd521d6b383413af74f29bec80cad4478e498fe9a8bbcca42d`.
- Guard CSV: `c15388177b685143a54749a4611773ee2444c29bd631fca43e3236e31f8479ad`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence: `conker/build/game-asset-command-block-15195868-match/`.
Tools are committed before the source, guards, documentation and tools pin.
Scoped Graphify retention is audited; no full-corpus extraction is claimed.
Root README receives aggregate rows only. The host port needs no transfer
from this retail-only C reconstruction; its Release and source stay untouched.

## Resume boundary

Next: **func_151C5588**, generated_1F2730, 71 words/frame0x58,
VA0x151C5588..0x151C56A4, ROM0x1F2A38..0x1F2B54. It computes randomized
floating parameters, performs two integer RNG calls and forwards a fourteen-
argument effect submission to func_15102B38. Recover all five incoming widths,
the pointer-passed local pair, the second RNG side effect, original callers,
float rounding, real frame and helper ABI before qualification. It remains
uninstalled and uncredited. Preserve private inputs/saves, handwritten
func_150A76F0, unrelated sibling edits and frozen host Release. Keep the full
80% goal active; no pause is requested.
