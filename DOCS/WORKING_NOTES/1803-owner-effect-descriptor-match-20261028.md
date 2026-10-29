# Owner effect descriptor direct C match — 2026-10-28

`func_151AF270` is recovered in `conker/src/game/generated_1D92F0.c` as
`void *func_151AF270(u8 *owner, u8 selector, s32 category)`.
All **50 instructions (200 bytes)**, the **80-byte frame** and six symbol
bindings match directly from semantic C under the existing IDO O2/g3/mips2/o32
profile. No new guards, volatile parameters or artificial padding are needed.
Keeping the returned pointer in a local declared before the descriptor recovers
the original stack layout. All 32 neighboring functions remain unchanged.

The adopted ELF recount is **3,881/5,506 (70.49%)** total and
**3,208/4,833 (66.38%)** Game, with zero address drift. Init remains 492/492
and Debugger 181/181. There are 1,625 different C functions and **249 more
exact matches** needed for 4,130/5,506, the 75% threshold.

## Recovered behavior

- VA `0x151AF270..0x151AF338`; ROM `0x1DC720..0x1DC7E8`.
- Null owner returns null without notification or a descriptor submission.
- Otherwise call `func_1516962C(40, owner, 22)` **before** reading the owner's
  identity at `0x3B` or either float constant.
- Submit a 48-byte `OwnerEffectDescriptor1D92F0` with two zero words, owner
  identity and pointer, attachment 1, three zero vector components, the two
  float constants, duration 320, flags 6, kind 10, callback -1 and mode 9.
- Call `func_1513418C(&descriptor, 0, selector, category)` and return its
  pointer or null. The selector uses the unsigned byte lane.
- Bytes 9–11, 17–19 and 46–47 remain untouched padding. Native checks do not
  assign meanings or initial values to those bytes.

`D_800A9DCC` and `D_800A9DD0` remain external rodata bindings. Their original
words are `0x411CCCCD` and `0x3E126E98` at ROM `0x24E88C` and `0x24E890`.
Unknown scalar meanings retain offset-based field names. The function's
original address name is preserved for traceability.

The bindings are the notification call at `0x2C`, HI16/LO16 pairs at
`0x44`/`0x4C` and `0x50`/`0x54`, and the constructor call at `0xB0`.

## Caller and original helper qualification

The whole-ROM aligned scan finds one JAL at ROM `0x1C1CA8` / VA `0x151947F8`
and no full pointer words. Its caller, `func_15194794`, already matches all
31 words. It performs two setup calls, then reads the owner's state byte
at offset 4 and calls this target for states 0–4 with selector 255 and
category 1. The return value is ignored. Its source now has the correct
pointer-return prototype. All 29 functions and the complete padded caller
object remain identical; its existing unrelated pointer/integer warning
at `func_15194DA4(arg0, arg1, arg2)` is retained at the corresponding source line.

The original 15-word notification wrapper snapshots owner and identity for
`func_1516944C`. Its dispatcher is a bounded service; callbacks and the complete
notification subsystem are not recovered here.

The original 76-word descriptor constructor and 11-word `memcpy` are executed
together. Tests cover allocation failure, invalid owner, changed owner identity,
missing matrix, actor type 15 and the attachment-matrix transform path. The
constructor copies 48 bytes to allocation+16 and returns null after deleting an
invalid result. All 15 wrapper and 11 copy words, and 74 constructor words, are
covered. The unvisited constructor words are explicitly retained and checked:
the redundant load at `0x15134234` and flags-clear store at `0x15134284`, whose
branch is excluded by fixed flags 6.

Allocator, delete, transform, notification dispatcher and the caller's first
two setup calls remain bounded services. This is not complete subsystem,
native-provider or gameplay acceptance.

## Validation

Eight fresh checks passed independently in both tools copies, followed by
shared tools checks in both copies. After production, two installed checks
passed freshly in each copy; six semantic checks were reused only after
complete input/module/artifact fingerprint identity.

| Check | Measured result |
| --- | --- |
| Actual Make | Five owner commands and five caller commands, including assembly processing and production padding |
| Direct guest | 776 cases; all 50 target words; unsigned lanes, null gate, notification mutations, descriptor bytes and raw float bits |
| Original helpers | 128 connected cases; 102 literal words, 100 reachable words covered |
| Complete original caller | 2,048 cases; all 31 words; all state bytes, including changes during the second setup call |
| Native32 SDK | 20,480 direct and 2,048 caller cases per O0/O2/O3 profile with trapping UBSan |
| Negative controls | 12 effective native and compiled-MIPS semantic controls |
| Fault prefixes | 396 complete-state/PC/access-trace pairs; 118 delay-slot cuts |
| GNU rebases | Three layouts, 192 cases, signed-low address carry boundaries, 56 raw/binding rejections |
| Strict full image | 185 changed bytes: 152 code, one symbol-size byte, 32 metadata bytes; zero exclusions; 19 corruption controls |
| Protected Game data | 189,088 bytes across 720 owners unchanged |

Incoming argument-home mutations and fault-prefix behavior qualify the emitted
guest instructions, not portable C semantics. Native checks use valid backing
and canaries and exclude indeterminate padding from expected values. Negative
controls must terminate and differ semantically, rather than fail by accident.

## Image and provenance

Production reproduces the private image. Every one of the 6,056 canonical
function addresses and the other 6,055 bodies is unchanged. Guard CSV and
conversion inventory bytes are unchanged. The 32 metadata-byte changes are
three closed symbol/string swaps: `D_800A9DD0` / `D_8009CDD0`, `D_800A9DCC` /
`D_800AABFC`, and `D_800994AC` / `D_8009EEAC`. Each name, value, type, size and
section is checked; there is no blanket metadata exclusion.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor ELF | `712971ca8c175d1ccaa01a4a1ae99e00065d15835ebc66a6e508d62b40ba6368` |
| Adopted ELF | `75deb5dbe7476948dae75ebb12b5fb128e2842a0b7c5762d703833967ebbca95` |
| Adopted owner C | `00c604ba7d4790c7950f6c9cc629acc545d629b17ff288aaaa359b10a218b688` |
| Qualified padded owner | `6a83d6fd5b1c8d4f2141c52a910f75ce9f733e21b8134aef0f9eebbaa53dd7c6` |
| Raw relocatable body | `4cc2a252a2c7b8d8f884d655c489b5b7ec99fca7ae90b05a89208210e84d2e7d` |
| Retail body | `7c97225c4fe5c1139ee4120ea35f919638018a8d1adb9a119f659fc547d3cbd5` |

Tools were committed first as `591549d533ce1bd65a762f3d347dbaa54baf825d`.
The consumer predecessor is `06a4ee4a69441c811a137dec52f088faa811e35d`.
The older tools mirror's 1,850 inherited dirty paths are preserved; three
qualified modules are added without committing that mirror. No push is made.

Receipts are under `conker/build/game-owner-effect-descriptor-match/`:
463 focused inputs, a 16,519-path input seal, original artifacts, Make proof,
private and canonical qualification, production, live recount and final audit.
Initial harness stops exposed inherited assumptions about Make-command count,
entry address, metadata ordering and caller rodata binding; those were corrected
against the actual inputs. One negative-control return was rewritten to consume
its result local under native `-Werror`. The selected candidate stayed unchanged.

The scoped Graphify update retains old nodes and valid relationships, retiring
the placeholder's obsolete s32 return edge. It does not claim a full-corpus
re-extraction, clustering or centrality update.

## Continuation

Codex implemented and validated the recovery. Claude budget/attempted/completed:
0/0/0. The 75% goal remains active. Next inspect 50-word `func_151E327C` in
`conker/src/game/generated_20AE20.c`. `func_1514E920` remains parked and uncredited.
Remaining shapes: 1,496 placeholders, 120 semantic/other and nine unlocated.
Queue position alone is not matching qualification.
