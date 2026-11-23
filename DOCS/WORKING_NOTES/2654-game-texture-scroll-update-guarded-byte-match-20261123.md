# 2654 - Texture scroll update guarded byte match

Date: 2026-11-23. The total 85% byte-matching goal remains active.

`func_15195FF0` replaces its zero-return placeholder with the complete
semantic C texture-scroll and tile-command update leaf. All **202 retail
words / 808 bytes / frame 128** are byte-exact through a closed allocation
and schedule transform. This is a **guarded C match**, not a direct compiler
match. Original: `conker/asm/1C2C60.s:630`, VA `15195FF0..15196318`,
ROM `1C34A0..1C37C8`.

Fresh production recount: **4,634 / 5,528 (83.83%) total**, Game
**3,961 / 4,855 (81.59%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift, **894 different**. At this denominator, **65 more
matches** reach at least 85%. Conversion rows and the denominator remain
unchanged because the old stub already counted as C. One match is credited.

## Interface and recovered behavior

```c
void func_15195FF0(s32 primaryList, s32 secondaryList);
```

The existing actual caller already declares this two-full-word void ABI.
The new local definition agrees with it; no shared header change is needed.
The owner keeps its default O2/g3/mips2/o32 profile, without a Make override.
Each linked record from `D_800E08E8` is processed as follows:

1. Read unsigned16 U/V phases at +0xE/+0x10 and signed16 width/height at
   +0xA/+0xC. Divide each phase by eight, add two, then subtract the dimension
   once when the coordinate reaches it. This is a single adjustment, not
   a modulo operation.
2. Generate at most eight `G_SETTILESIZE` command words in the original
   incoming-SP-minus-36 scratch array. Each packs the low twelve bits of
   both coordinates, then halves the coordinates using signed truncation.
   The maximum-tile byte +0x14 is reread after each generated word.
3. Multiply both dimensions by eight. When `D_800BEAC0` is zero, read the
   delta once from `D_800BE9E4` and add signed8 speeds +0x12/+0x13 times
   that delta. Explicit unsigned32 expressions preserve the original
   low-word arithmetic without native signed-overflow undefined behavior.
4. Add or subtract each span at most once, then store the low sixteen phase
   bits. Preserve the original first primary-index read before these stores.
5. Traverse up to five signed16 primary slots (+0x1C) and secondary slots
   (+0x26), stopping at -1. Their count bytes are at +0x30/+0x35. Copy each
   scratch word to display-list index*8 plus level*16, changing only the
   opening word of each tile command. Reread the live count after each store.
6. Traverse the associations at +0x18. Read each count before its unsigned16
   index, reload its display-list base at +8 on every iteration, and copy
   with the same command stride. Follow association +0x10 and record +4.

The code retains meaningful phase, tile, index, output and list locals.
There are no padding locals, artificial flag tests, physical-register
directives or broad volatile casts.

## Derived normalization and loop proof

The selected C emits **197 words / frame 128**. All 197 source words appear
exactly once in the derivation; none are dropped. The five added operations
restore the record-pointer copy, initial primary zero-index shift, two
command-index register copies, and the redundant association null-path join
branch. Address setup, the independent slot increment, scratch-cursor store
schedule and disjoint register lifetimes are translated explicitly. Both
phase additions exchange commutative operand order; multiplication remains
the original low-word operation. Branch offsets
are derived from the operation mapping, and all six symbol binding sites
retain their exact identities.

The normalizer consumes only pinned compiler words and relocations. It
does not read retail bytes to construct its output. Original ASM provides
an independent comparison after derivation. The physical CSV replacements
are the serialization of that proved stream, separate from the semantic
operation mapping.

Restricted symbolic block induction covers all **197 source and 202 retail
words**, including both signed-division correction paths. It checks two
entry paths and thirteen blocks: outer record preparation (32 paths),
tile generation (12), phase update (36), primary/secondary copy setup and
inner loops (4 each), and six two-path traversal/exit blocks. Ordered reads
are fresh symbolic values; matching addresses, stores and rereads preserve
public aliases outside the saved private frame. Live slot offsets account
for the original early increment, and the extra record copy is maintained
as an explicit invariant. All normal returns preserve saved registers.
**35 effective semantic/missing-operation controls** reject, including the
four added address/copy operations. The redundant join branch is retained
for byte identity, not claimed to add a new semantic effect.

## Fresh checks

The versioned task packet is
`tools/experiments/game_texture_scroll_update_15195ff0_{match,manifest,objects,make,image,qualification}`
and `tools/tests/game_texture_scroll_update_15195ff0_{normalizer,symbolic,guest,native}`.
Run from the prepared consumer root under WSL:

```sh
python3 -m unittest tools.tests.test_game_texture_scroll_update_15195ff0_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

| Tools phase | Elapsed | Checks |
| --- | ---: | --- |
| preinstall-primary | 99.645s | 5 fresh / 0 reused |
| preinstall-sibling | 104.387s | 5 fresh / 0 reused |
| installed-primary | 92.281s | 5 fresh / 0 reused |
| installed-sibling | 112.174s | 5 fresh / 0 reused |

Each phase executes all five checks freshly. Imported modules, tool data,
bindings and artifacts are fingerprinted in both the primary checkout and
a disposable sibling overlay; nothing is written to the dirty real sibling.
Final review changed the fixture's link fields to `u8 *`, matching the
source's byte-pointer lvalues while keeping the exact SDK32 offsets. The
earlier fixture receipts and first production build are archived separately;
they are not used for the four final phase receipts or matching credit.

- **660 cases per raw/normalized/padded/retail stream** compare independent
  phases, complete public memory and ordered public access traces. Final
  private memory also agrees. The normalized streams compare complete
  GPR/FPR/private memory/events/trace literally against retail.
- **660 valid native SDK32 cases at each O0/O2/O3** use typed linked records,
  association structures and display-list arrays with strict aliasing and
  UBSan. Nine effective C controls reject: wrong phase source, gate, speed
  signedness, tile cap/mask, slot limit, stride, output list and single-wrap
  arithmetic. All original dimensions and extreme delta signs are covered.
- **14 guest-only probes** exercise self-overwriting primary/secondary and
  association counts, a changing association display-list base, scratch and
  saved-slot output aliases, and seeded uninitialized scratch reads. Raw
  final memory/public access order agrees with retail. Fitted complete
  state agrees literally. Deliberately overwritten saved S0 is checked as
  guest corruption, not falsely reported as ABI preservation.
- **946 fired own-access prefixes** compare complete normalized/padded/
  retail state and access order, including those alias/private witnesses.
- **66 actual caller-window cases per stream** execute the original five
  words at `15174A10..15174A24`, including JAL `15174A1C` and its A1 load
  delay slot, then the complete leaf. Both arguments retain full words;
  the result is void. Surrounding providers and the full parent are outside
  this bounded execution claim.
- **194 reachable retail words execute**. The eight retained correction
  words 23/24/29/30/56/57/61/62 are statically unreachable: unsigned phase
  loads are 0..65535, giving 2..8193 after division/addition; the conditional
  signed16 dimension subtraction leaves 0..40961, and repeated halving
  keeps both coordinates nonnegative. The symbolic proof still covers
  both correction alternatives as modular instruction paths.
- **197 expected-word/binding rows**, five insertions and zero omissions,
  produce the original target through both full-owner padders. All **406**
  changed-word/binding controls reject, covering every source word and all
  six relocation sites through both padders. Oversized guarded bodies
  reject in both paths, including the generic overflow trampoline guard.
- **12 independent GNU links** over four code/global arrangements check
  symbol rebases and HI16/LO16 carries. All **68 neighbors**, literal pools
  and diagnostic sets remain fixed. Actual Make replay reproduces the
  entire independently padded owner. Shared `make tools-check` passes.

Native counts are bounded by generated scratch words. Counts above the
generated words, seeded uninitialized values and private-frame aliases in
the guest probes are observations, not portable C or hardware/gameplay
acceptance. Codex is the
only writer; Claude calls: zero.

## Production image, ownership and checkpoint

The independent full-image predictor first recompiles frozen old C with old
guards to recover the complete prior owner, then substitutes only original
target ASM. The actual C build equals that reference byte for byte: **613
changed ELF bytes, zero exclusions**. Only the target instructions and
declared size change; named symbol definitions and every string byte are
accounted for. All 189,088 protected Game data bytes and 720 data owners
remain exact. The old guard CSV is an unchanged prefix with precisely the
197 new rows appended. No compiler, layout, Make profile, header or
conversion row is changed.

```text
before ELF: 16cd219c7450841246b5c35a1bdf7d59d7d92b98dfe0c14f8ad9c9dac79d68dc
after ELF:  8d4cf1ee357e3d3d6d00af45876b95fb1befc348920c2955d9dfe5258145b88c
owner:      2b98fecc1d65a36ee164ca46db5c2a4a40415e09cb346dacae7c35cbe4920827
```

All 3038 frozen inputs are checked against the explicit adoption plan.
Existing compiler and duplicate generated_12D630 recipe warnings remain.
Root README changes only its two aggregate matching rows; this note owns
the detailed recovery narrative.

The sibling overlay has 1,699 files: 349 identical sibling files, 1,338
explicit primary fallbacks, 11 task files and one bootstrap. This is not a
standalone-clean-sibling claim. The real sibling HEAD, dirty state and
dependency hashes remain intact. Rechecked host scene configurations consume
binary artifacts and have no direct C-owner reference; the selected scene
still lists this function as a stub. No host edit, binary refresh, Release
action or gameplay claim is made.

Tools are committed first, then consumer source/guards/pin/documentation.
Nothing is pushed. Graphify keeps old IDs and qualifications, records the
actual installed void/two-word definition after observed producers finish,
and treats scoped retention as distinct from full-corpus re-extraction.

Next inspect `func_15196438`, the next unfinished Game routine in this owner,
with fresh ownership/caller/profile and complete matching gates. The 85%
goal remains open.
