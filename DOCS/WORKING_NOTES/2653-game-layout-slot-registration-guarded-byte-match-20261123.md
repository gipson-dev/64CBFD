# 2653 - Layout slot registration guarded byte match

Date: 2026-11-23. The 85% total matching goal remains active.

`func_15195AA8` replaces its zero-return placeholder with a complete semantic
C texture-command registration routine. Its **150 retail words / 600 bytes /
frame 96** are byte-exact after a closed register, slot and ABI-home
normalization. Original: `conker/asm/1C2C60.s:235`, VA
`15195AA8..15195D00`, ROM `1C2F58..1C31B0`.

Fresh production recount: **4,633 / 5,528 (83.81%) total**, Game
**3,960 / 4,855 (81.57%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift, **895 different**. At this denominator, **66 more
matches** reach at least 85%. Conversion rows and the denominator do not
change: the old stub already counted as C. One new exact match is credited.

## Recovered interface and behavior

```c
void *func_15195AA8(s32 displayList, s32 assetId, s32 doubleSize,
                  s32 occurrence, s32 state, s32 secondary,
                  s32 field12, s32 field13);
```

The existing shared header already has the eight full-word arguments and
pointer result. This change makes the local definition agree with that
interface without a shared-header edit. The function:

1. Returns zero for a null display list, with the original argument-2 spill.
2. Calls `func_15195868` for the chosen occurrence, or repeatedly from zero
   when occurrence is -1. A first miss returns the initialized null record.
3. Resolves asset zero through the live token, then searches the linked list
   for a **zero key**. This differs from the related asset-key registration.
4. Constructs a record through `func_15195984`, or binds an existing record
   through the signed-halfword index interface of `func_15195A84`.
5. Sets new-record bytes +0x12/+0x13, updates the maximum tile byte +0x14,
   and records the command in the first empty five-slot array element.
   Primary indices/tile bytes are at +0x1C/+0x30; secondary at +0x26/+0x35.
   Full arrays skip their writes. The first empty entry is the signed -1.
6. Reloads the current global token before the conditional decrement and
   returns the last record, retaining original early-failure behavior.

No unrelated global disable gate is invented. The original global reads,
record writes and helper argument widths/order are preserved. C uses the
owner's existing default **O2/g3/mips2/o32** profile; no Make override is
added. Source names describe the recovered roles and offset fields.

## Original state home and normalization

Raw C is **147 words / frame 96 / 111 raw word differences**. It is not a
direct compiler match. The earlier private source packet remains the basis,
with exact raw instruction and relocation fingerprints checked.

The original S6 lifetime is concrete:

| Original VA | Effect |
| --- | --- |
| 15195B00 | Load incoming argument 4 from incoming SP+0x10 |
| 15195B9C | Clear S6 after successful new-record construction |
| 15195BD0 | Clear S6 on the existing-record binding path |
| 15195CBC | Write S6 back to incoming SP+0x10 on normal common exit |

No other original value-dependent use exists. Null-list and constructor-
failure returns bypass the writeback. A first search miss writes back the
original incoming value; any earlier successful binding makes it zero.
The C compiler removes this by-value parameter's home lifetime and coalesces
its zero with the slot cursor. The matching layer explicitly restores this
**o32 ABI home effect**; it is not presented as a literal raw C memory action.

The derived normalizer preserves all 146 other source operations and folds
the duplicated conditional A0 copy. Its four additions are the state-home
read/write and the two selected-branch slot-cursor zero initializations;
one duplicate A0 copy is omitted, giving 147 + 4 - 1 = 150 words. It translates
the disjoint asset, search, record, index, packed-size and slot-register
lifetimes, swaps the corresponding physical save ordering correctly, and
retargets the four affected branch destinations. Independent address setup
and search-cursor updates move without changing public access order.

The restricted symbolic decoder rejects unknown operations. Three entry
paths and inductive blocks for the outer loop (**119 paths**), list traversal
(**58**) and primary/secondary slot scans (**7 each**) compare ordered
public effects, all four helper arguments, loop-carried roles, saved
registers and the explicit ABI-home contract. This is a 32-bit modular GPR
proof under ABI-conforming providers. Providers may change public data while
preserving saved registers and the callee's private frame/home. Seventeen
effective operand/missing-operation controls reject, including all four
state-home load/clear/store sites.

No dummy flag test, padding local, register directive or broad volatile
qualification is added to force code shape. Replacing `slot = state` with
literal zero was screened and emits identical words/bindings; it does not
solve the ABI lifetime or earn separate credit.

## Fresh qualification

The task packet and modules are
`tools/experiments/game_layout_slot_registration_15195aa8_{match,manifest,objects,make,image,qualification}`
and `tools/tests/game_layout_slot_registration_15195aa8_{normalizer,symbolic,guest,native}`.
From the prepared decomp root under WSL:

```sh
python3 -m unittest tools.tests.test_game_layout_slot_registration_15195aa8_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

| Tools phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 120.742s | 5 fresh / 0 reused |
| preinstall-sibling | 120.94s | 5 fresh / 0 reused |
| installed-primary | 96.096s | 5 fresh / 0 reused |
| installed-sibling | 104.212s | 5 fresh / 0 reused |

The pre-install primary receipt predates the requested pause; its 326 imports,
303 data files, 11 artifacts and every frozen input were revalidated after
resume. It is reused as that exact receipt, not called a fresh post-resume
execution. The other three phase runs execute their five checks freshly.

- **804 guest cases per raw/generic/generated/retail stream** check the
  independent public-memory, full-result, helper-call and access-order
  reference. Raw/public comparison excludes only the actual 96-byte frame
  and incoming argument-4 home. The normalized streams compare complete
  GPR/FPR/private memory/events/trace literally against retail, including
  that home. **706** cases take its normal writeback path.
- **804 valid SDK32 native cases at each O0/O2/O3** use typed linked records,
  actual five-element signed-halfword/byte arrays, strict aliasing and UBSan.
  They cover bounded defined C arithmetic and ordinary backing, not arbitrary
  private-frame aliases or signed-overflow behavior. Eight effective C
  controls check list key, array/slot selection, state reset, new-record byte,
  tile comparison, token update and signed index conversion. The MIPS home
  writeback is separately qualified as an ABI effect.
- **101 cases per stream** execute the actual 14-word caller prefix
  `1500EF20..1500EF58` and the first connected call with eight full arguments.
  Its complete 748-byte linked parent equals pristine ROM; the full parent
  is not executed or claimed recovered by this bounded test.
- **374 fired access prefixes** compare normalized complete state, dispatched
  word and trace with retail, including null, failed allocation, repeated
  scan, full primary/secondary arrays and helper public-data mutations.
- All 149 reachable retail words execute. Word **108**, `15195C58`, is the
  original unreachable duplicate secondary load after an unconditional
  branch/delay pair; no direct branch enters it. It is retained byte-exact.
- **147 expected-word/binding rows**, four insertions and one omission,
  reproduce the same exact target through both full-owner padders. All
  **312** changed-word/binding controls reject: every one of 147 source
  words and all nine binding sites through both padders. The generated
  padder rejects an oversized body; the generic padder's overflow trampoline
  fails the pinned first-word guard, as explicitly checked.
- **12 GNU links** across four global/code arrangements verify independent
  relocations and HI16/LO16 carries against original ASM. All **68 neighbors**,
  literal pools and owner diagnostic sets remain fixed. The real Make replay
  equals the complete independently padded owner.

The disposable sibling overlay has 1,688 files: 349 identical sibling files,
1,327 explicit primary fallbacks, 11 task files and one bootstrap. This is
not a standalone-clean-sibling claim. The real sibling HEAD, existing dirty
state and dependency hashes remain unchanged. `make tools-check` passes.
Codex is the only writer; Claude calls: zero.

## Complete production image and commit boundary

An independent reference first recompiles the frozen old C with old guards
and reproduces the entire previous owner. It then substitutes only original
target ASM, independently of the new C and guards. The complete actual
linked ELF equals the predicted baseline-plus-target image: **457 changed
bytes, zero exclusions**. Named symbol definitions and every string byte
are accounted for; only the target's declared size changes. The protected
189,088-byte Game data region and all 720 data owners remain exact.

```text
before ELF: 1ad1e388f0d80ae610987531978597e680975ba404688cd144d5166485448fd2
after ELF:  16cd219c7450841246b5c35a1bdf7d59d7d92b98dfe0c14f8ad9c9dac79d68dc
owner:      236a4b72064e49b765632aa653ccb63493b5c9952899d465680c0925aed632c6
```

The production build reapplies the CSV-dependent owners; all **3,026 frozen
inputs** are checked against the explicit change plan. Old guard bytes are
an unchanged prefix with exactly these 147 rows appended. No header, layout,
compiler, Makefile/profile or conversion row changes. Existing compiler and
duplicate generated_12D630 recipe warnings remain. Root README changes only
the two aggregate matching rows; detailed recovery updates stay here.

The `64CBFDOGL` scene configurations were rechecked: they consume the same
binary artifact and do not reference this C owner; the selected scene still
lists this function as a stub. That path has no complete host Git/build root
or direct C consumer. No host edits, binary refresh, Release action or gameplay
acceptance is claimed. Tools are committed first, then consumer source,
guards, pin and documentation. Nothing is pushed. Graphify retains all old
IDs and qualifications and marks the actual definition installed only after
observed post-commit producers finish; scoped retention is not full-corpus
re-extraction.

Next inspect `func_15195FF0`, the remaining 202-word texture-command update
leaf in this owner. Qualify its ownership, actual profile, callers and complete
semantics before any source installation or credit. The 85% goal stays open.
