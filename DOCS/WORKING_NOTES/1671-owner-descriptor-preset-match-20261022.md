# Source-Backed Descriptor Preset Guarded C Match

Date: 2026-10-22

## Result

Recover `func_151A4590` in `conker/src/game/generated_1D0840.c` from its
zero-return placeholder. Complete semantic C emits **42 words / 168 bytes,
frame 72 and three relocations**. Eighteen checked scheduling words and a
corresponding low-relocation move make the installed body byte-exact.
This is guarded C, not compiler-only matching.

VA 151A4590..151A4638 / ROM 1D1A40..1D1AE8, ends exclusive. Preserve
`conker/asm/1D0840.s` and its retained func_151A5170 GLOBAL_ASM input.
Keep the address-based name and add a purpose comment. Add one private typed
48-byte descriptor, the float declaration and a typed constructor prototype;
do not change shared headers, profiles, frame size or the instruction count.

The old emitted body was twelve bytes in its 168-byte slot. Converted-C totals
and conversion rows remain unchanged; this earns one additional exact match.
Raw unlinked body SHA-256:
`27bda6bd1307115c17b901dff63d08112f9be14d11961ded5e9bf2a4acffff1e`.

## Recovered Contract

A null owner performs no constructor call or owner/global memory read.
Otherwise create this stack descriptor, preserving all unwritten bytes:

| Offset | Value |
| --- | --- |
| +0x00 / +0x04 | Two full zero words |
| +0x08 | Captured byte from owner+0x3B |
| +0x09..+0x0B | Three unwritten bytes |
| +0x0C | Captured owner pointer |
| +0x10 | Attachment index 1 |
| +0x11..+0x13 | Three unwritten bytes |
| +0x14 / +0x18 / +0x1C | Three positive-zero floats |
| +0x20 | Captured D_800A8D5C float representation |
| +0x24 | Float 3.0 |
| +0x28 | Signed halfword 100 |
| +0x2A / +0x2B / +0x2C / +0x2D | Bytes 10 / 1 / 255 / 0 |
| +0x2E..+0x2F | Two unwritten alignment bytes |

Submit `func_1513418C(&descriptor, 0, variant, 0)` with the unsigned low byte
of variant. The wrapper is void: do not invent an integer-1 or null return.
Use a signed byte initialized to -1 for +0x2C, preserving its 0xFF wire value
and retail's signed immediate. Leave uncertain scalar fields neutrally named
value20/value24/value28 rather than guessing their gameplay meanings.

The constructor uses attachment as a matrix-entry index. Its fuller behavior
is distinct from this wrapper's fixed descriptor contract.
After frame reservation, RA is at SP+0x14, the descriptor at +0x18 and incoming
homes at +0x48/+0x4C. Volatile owner views retain both original home loads;
this is not proof of the original author's source keywords.

## Scheduling And Relocations

Move the first owner-pointer store after the following seventeen operations:
destination word indices 13..29 take original indices 14..30, while word30
takes word13. Validate every expected word and a closed permutation; no
register field, branch, call, frame, insertion or omission is changed.

The D_800A8D5C HI16 remains at +0x1C. Move its LO16 binding from +0x40 to
+0x3C with the LWC1 instruction. The func_1513418C R_MIPS_26 stays at +0x90.
Pin the complete raw body and all three bindings. CSV rows explicitly check
the old/new relocation lists, including the removed and added LO16 slots.
Append exactly eighteen rows; preserve the old CSV byte prefix and line endings.

Raw C stores the owner before reading its selector; retail reads the selector
first. A constructed alias into the callee's private stack descriptor exposes
a real difference, which the qualifier requires as an effective witness.
Raw public-result evidence is restricted to disjoint backed objects and the
ordinary global. Only guarded C claims the tested private-state, stack/global
alias and fired root-fault-prefix agreement. Do not claim raw local-alias,
private-state, fault, portable concurrency or MMU identity.

The unqualified-owner screen loses a word; introducing a separate captured
pointer or chained vector assignment grows the frame to 80. Reject those
forms. No dummy local, aggregate blanket clear or frame patch is installed.

## Qualification

Tools, identical in both local copies:
`experiments/game_owner_descriptor_preset.py` and
`tests/test_game_owner_descriptor_preset.py`.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 3.879s | 8 tests, 3.747s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 1.925s | 2 tests, 1.888s | 0 / 0 / 0 |

Explicitly reuse the remaining six pre-install checks only under strict source,
raw/padded object, guard, helper/input and complete-image identity. They are not
fresh installed runs. Shared tools checks pass in both copies (0.161/0.104s).
Routine Codex qualification uses zero Claude calls.

- 1,212 guest phases visit all 42 words and cover every variant byte, raw
  register boundaries, descriptor holes, unusual float representations,
  effectful callees, null gates and stack/global aliases. Another 1,152 raw
  executions qualify only the disjoint public contract.
- Native32 O0/O2/O3 each pass 4,096 selected-body cases with trap UBSan,
  canonical typed inputs and full owner fences. Nine effective wrong-C
  controls cover a dropped variant, wrong owner byte/vector/global/scalar/
  halfword/flags/sentinel and changed call variant. Preserve existing typed
  32-bit alias views. Unwritten native bytes are not assigned portable values;
  float transport is not a general FCSR/NaN arithmetic claim.
- Six independent GNU entry/callee links cover 24 phases and signed-low
  boundaries. Fourteen additional GNU links qualify seven stack-global
  addresses. The first alias-fixture attempt mapped a new address without
  relinking its code and correctly failed; accepted fixtures actually rebase
  both original and C images. Do not weaken the alias check.
- Check 112 fired guarded root-data fault prefixes, twenty guard corruption
  controls and five strict whole-image corruptions. Preserve all 22 raw/padded
  neighbors and pools, 27 historical inputs and the old padded object.
  Independent GNU assembly agrees with normalized words/bindings. Actual
  Make's five productive GLOBAL_ASM-owner commands reproduce the qualified
  raw and padded results under the normal O2/g3 profile.

## Caller And Constructor Bounds

The aligned retail scan finds one direct JAL at ROM 1D08FC / VA 151A344C and
no literal target pointers. This does not exclude constructed targets.
Execute the original caller window 151A3448..151A3458 across sixteen phases,
stopping before the following extended-effect call. Verify S0 owner transfer,
the variant load in JAL's delay slot and the owner reload afterward.
The complete func_151A3390 remains an unchanged twelve-byte production stub.

The current func_1513418C GLOBAL_ASM body is already byte-exact across all
76 words. Connect that actual code across 64 phases, with explicit allocator,
memcpy and deletion contracts. Verify the six-argument allocation packet,
48-byte copy, allocation failure, invalid-owner deletion, valid no-matrix
path, and finite reciprocal values 0.5/0.25 plus the final zero store.
Matrix-transform branches, general FCSR behavior, full parent execution and
natural gameplay are not claimed. This wrapper does not recover constructor C.

## Production

Commit tools first: `3a491adf02b59d54b4f9c371276ec2d04ebc10ad`. No push.
Preserve all 1,554 prior older-mirror dirty paths, statuses, hashes and HEAD;
add only two task files, leaving 1,556 dirty paths. Do not reset or commit it.

Seal 15,854 files, including all 1,454 linker objects. Normal Make completes
in 0.538s in the verified Linux copy. Mark only the verified target-only guard
append old to avoid unrelated rebuilds. Existing duplicate generated_12D630
recipe warnings remain. Owner diagnostics are unchanged and isolated target
diagnostics are empty; this is not a warning-free clean-from-scratch build.

Every static input and non-target object remains byte-identical. Validate live
bytes before and after promoting only the owner object, ELF, linker script and
progress CSV; linker-script and conversion-CSV bytes remain unchanged. Live
adoption audit: 44.781s.

Reproduce the strict independent full-ELF prediction with zero exclusions:
**127 changed bytes =126 code bytes +1 target-size metadata byte**.
Preserve all other 6,054 bodies, all 6,055 addresses and all 720 protected
Game-data owners / 189,088 bytes. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
ELF SHA-256:
`a7dddd4be56547f972507c8bd4cad37dbad7e1113e6dc06ba9c5129ea5e46645`.
Padded owner SHA-256:
`1405212d57a828bb1f727051e54e57bbfb3afb6a1d7bf566267b10550d276de4`.

## Handoff

The standard matcher against the actual live ELF completes in 35.160s:
total **3,739/5,505 (67.92%)**, Game **3,066/4,832 (63.45%)**,
Init 492/492 and Debugger 181/181 exact. Zero address drift; 1,766 different.
The 75% threshold remains 4,129 exact, requiring **390 more matches**.
Queue shapes: 1,635 placeholders, 122 semantic/other and nine unlocated.
Next func_15043A20 is screened only, unmodified and uncredited.
Keep func_1508CAD8's 862-word stub queued.

Root README changes only its two aggregate rows. Detailed updates belong here
and in concise indexes. Post-commit graph-worker and every-old-node audits
remain private receipts; retain excluded-corpus/large-HTML caveats without a
full re-extraction or fresh corpus-membership recount claim.
Frozen host Release remains untouched.
