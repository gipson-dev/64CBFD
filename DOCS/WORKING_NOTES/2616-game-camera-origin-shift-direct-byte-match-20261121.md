# Note 2616: Camera origin shift direct byte match

Date: 2026-11-21. Consumer baseline `af05391347232d39e93a76dd95fd0ecc7132451a`; tools baseline
`ac6d7d68dd291db9a6ece06254292aee6dfd5fe6`. Qualified tools commit: `b7f85adce6781b59eadbb94784076a6e4cd3494a`.

`func_15097798` replaces its zero-return placeholder with the complete gated
camera translation. All **93 body words / 372 bytes** emit directly from C,
including the **0x30-byte frame**, RA lifetime and eight relocation sites.
Its **94-word retail slot** includes one unchanged trailing alignment nop.
There are **zero guards, insertions or omissions**. All six owner neighbors,
pools and existing compiler diagnostics are unchanged; the existing O2/g3
profile is retained. Shared headers and compiler profiles are unchanged.

Fresh production recount: **4,599 / 5,528 (83.19%)** total and **3,926 / 4,855
(80.87%)** Game, zero address drift and **929** still different. Init 492/492
and Debugger 181/181 remain exact. **100 more matches** reach 85% at this
denominator. Conversion rows are unchanged because the placeholder already
counted as C. Root README changes only its Total and Game matching rows.

## Recovered behavior and layout

Owner `generated_C3E20`; source `conker/src/game/generated_C3E20.c`.
Body VA `0x15097798..0x1509790C`, ROM `0xC4C48..0xC4DBC`; the alignment
word extends the slot to VA `0x15097910` / ROM `0xC4DC0`. Original assembly
remains in `conker/asm/C3E20.s:1004`. The recovered interface is
`void func_15097798(s32 view)`; the caller uses an unsigned byte view.

The camera pointer `D_800DBFF0 + view * 0x9A0` is calculated before the signed
nonzero `D_800D2DB4` gate and retained across both helpers. The routine calls
`func_15048F90` to subtract origin from target, then `func_1504917C` to
normalize the resulting vector in place. It adds direction times -2.5 on X/Z
and -2.0 on Y, each multiplied by a fresh signed `D_800D2E30[view]` read,
first to origin (0x2A4/0x2A8/0x2AC), then target (0x2F8/0x2FC/0x300).
The source preserves `(component * coefficient) * float(scale)` before
addition, all six scale reads and the original cached camera lifetime.

The shared SDK `struct108` has the correct 0x9A0 extent but still declares
the origin Z word at 0x2AC as s32. A local `CameraShiftC3E20` view names both
float vectors while preserving their exact offsets and full extent. The
native harness asserts all six SDK offsets and both extents. No shared
structure declaration or data definition is changed. Ordinary O2 without
g3 gives 92 words; O1 gives 127 words/frame40. Both controls are rejected.
The first complete O2/g3 semantic draft already matches. Raw payload SHA256:
`58a134fb45806f9e8128e1eff4ef2e04d469f464702b42d6fc52ca96915e3ae8`.

## Qualification and limits

- Original, raw C and production-padded payloads and relocation bindings
  agree. All seven owner function addresses/extents are preserved except
  target symbol size 12 -> 372. The extra alignment nop is checked against
  both the padded object and original ROM. The natural Make recipe uses
  three commands and yields the independently prepared owner object exactly.
- The independent complete-image prediction matches the actual linked ELF:
  **340 changed bytes**, **zero exclusions**, across 6,051 slots. It accounts
  for two closed metadata swaps: `D_800D2E30`/`D_800915BC` and
  `D_800A13B8`/`D_800A56B8`, four symbol records / 44 string bytes. Named
  symbol attributes are preserved except target size; no table is excluded.
  Protected Game data stays **189,088 bytes / 720 owners exact**. ELF SHA256:
  `98b781877cb35b12ec09401c98d96179b338d5ea7b5cf018096e794ce7fa9f6f`.
- Guest execution passes **1,278 cases in each of three streams**, covers
  **all 93 target words**, and passes **105 target-access fault prefixes**.
  Full memory, private stack, GPR/FPR/HI/LO, calls and ordered accesses agree.
  It covers zero vectors, signed zero, asymmetric/tiny finite vectors, signed
  scale extremes and effectful helper contracts. Sparse extreme views and
  deliberate scale/vector/home overlaps are guest-only. Three instruction
  controls detect wrong coefficients and inverted gating.
- Connected execution uses the **53 actual original helper words**: 14 for
  subtraction, 28 for normalization and 11 for length, also checked against
  the current linked ELF. **96 cases per stream** cover all helper words and
  the real `sqrt.s` at 0x150AD958, without injected helper mutations. The
  oracle models default single rounding; FCSR exceptions and hardware are
  outside this proof.
- Native SDK32 execution passes **690 cases each at O0/O2/O3**, strict
  aliasing and UBSan. It uses actual recovered subtraction/normalization C
  with fingerprinted source, valid arrays and layout assertions. The length
  contract uses the original multiply/add order and SSE sqrtss; the original
  handwritten length is separately connected in the guest. Eight effective
  source controls catch wrong gating, unsigned scale, wrong X/Y coefficients,
  omitted normalization, wrong output, stale scale and refreshed camera.
- The original census finds one direct call, at **0x15122E74**, in
  `func_15122C5C`, and no aligned loaded function-pointer literal. Computed
  references are not excluded. The original **four-word call window** passes
  **396 cases per stream**, including its LBU view delay and the following
  helper's S0 argument delay. Skipped-target, wrong view byte and wrong next
  delay controls are effective. The parent remains unfinished and its
  current window differs from retail; this is original-window qualification,
  not complete current-parent or following-helper acceptance.
- Six independent GNU links at two code/data bases match the separate binding
  calculation for all target relocations, including R_MIPS_26/HI16/LO16 and
  signed-low carry. Unrelated raw-owner data is outside this isolated link
  scope and is covered by the independent production image audit.
- Five focused checks pass freshly in both primary and isolated sibling
  configurations before and after installation, plus shared `make
  tools-check`. Imported source/data fingerprints agree. The actual dirty
  sibling HEAD/status and all 352 dependency hashes are preserved. Older
  unchanged neighbor receipts are reused by fingerprint, not called fresh.

A final extra empty source line was removed during commit review. The
pre-format receipts are archived, the complete qualified object and predicted
ELF are verified unchanged, and both installed suites were rerun using the
final source/manifest fingerprints.

The build retains the pre-existing duplicate `generated_12D630` Make recipe
warning and untouched neighbor diagnostics. No warning-free build is claimed.
The available host configuration consumes binary words and symbols; no
identical target window is found and its configured symbols file is absent.
Host mapping/gameplay acceptance remains unknown. No host build or frozen
Release artifact is changed.

The keyed history callback `func_15188F84`, sequence query `func_15022024` and
noncanonical-return camera transition `func_15128030` remain private and
uncredited. Next inspect `func_1509759C` in this owner with a fresh ABI/caller
and profile screen. The wider 85% goal remains active. No push, model, ROM,
save or host changes are included.

Graph maintenance: the native update exited 1 with all
69,953 prior IDs retained. The subsequent serial scoped extraction
covers 6 C/Python files with no missing AST sources, producing
70,000 nodes / 159,761 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
