# Damped Motion Snapshot Guarded C Match

Date: 2026-10-22

## Result

Recover `func_1514A4EC` in `conker/src/game/generated_176A00.c` from its
zero-return placeholder. Complete semantic C emits **42 words / 168 bytes,
frame 0 and two relocations**. Seven checked words normalize copy-register
lifetimes and an independent load schedule. The installed body is byte-exact.
This is guarded C, not compiler-only matching.

VA 1514A4EC..1514A594 / ROM 17799C..177A44, ends exclusive. Preserve
`conker/asm/176A00.s`. Keep the address-based name, descriptive actor
parameter and purpose comment. No inserted/elided instructions, frame patch,
dummy locals, shared-header changes or compiler-profile changes.

The old body was 12 bytes in its 168-byte slot. Converted-C totals do not
change; this earns one additional exact C match. Raw unlinked body SHA-256:
`e5569361b68ccd028e87d2094ec8aaf2d2f4cbc3365d94b773e997ba8ec58a12`.
Pin both D_800BE9A4 HI16/LO16 bindings as well as the complete raw body.

## Recovered Contract

Capture the damping float at actor+0x140 once. Snapshot the three raw position
words at +0x34/+0x38/+0x3C into +0x40/+0x44/+0x48 before integration.
Use explicit u32 copies to preserve every representation bit, including signed
zero and unusual float payloads, without arithmetic in the snapshot.

Multiply horizontal velocities +0x130 and +0x138 by the captured damping.
Update vertical velocity +0x134 by acceleration at +0x13C times the live
D_800BE9A4 timestep. Do not damp vertical velocity. Advance the three position
floats with their updated velocities and repeated live timestep reads.
Preserve separate single-precision operations and return the full integer 1.

Ordinary source/native evidence uses backed, aligned records and finite
numeric inputs. Guest aliases qualify emitted memory behavior when the global
timestep overlaps record fields. Unusual snapshot words qualify raw copies,
not general FCSR/NaN, MMU, portable C alias/fault or gameplay behavior.

Struct-copy forms have 24 differences; moving/initializing a return local does
not close them. Explicit words leave seven differences, with all arithmetic
already exact. Standard memcpy, including the pragma screen, introduces a
call and 32-byte frame and emits 48 words. Reject those forms before install;
no new vector type, string header or intrinsic pragma is installed.

## Copy Guards

| Offset | Expected | Replacement | Purpose |
| --- | --- | --- | --- |
| 0x010 | 0x8C8E0034 | 0x8C810034 | X word into AT |
| 0x014 | 0x8C8F0038 | 0x8C980038 | Y word into T8 |
| 0x01C | 0x8C98003C | 0xAC810040 | Store X before reusing AT |
| 0x020 | 0xAC8E0040 | 0x8C81003C | Z word into AT |
| 0x024 | 0xAC8F0044 | 0xAC980044 | Store Y from T8 |
| 0x028 | 0xAC980048 | 0xC488013C | Move independent acceleration load |
| 0x02C | 0xC488013C | 0xAC810048 | Store Z from reused AT |

Derive the replacements by permuting the seven source operations and changing
only copy-data register fields. Validate base A0, exact load/store opcodes,
source/destination offsets and the unchanged F8 acceleration load. Track the
value in each scratch register before every store: X must be stored before AT
is reused for Z, while Y remains in T8. Prove that all three source/destination
words occur once and that the acceleration field is disjoint.

Scan the entire raw body to prove its T6/T7/T8 uses are exactly the declared
copy lifetimes and that AT is vacant. Reject a changed raw hash, binding,
extent, expected word, duplicate operation or invalid value lifetime.
Append exactly seven rows with the old CSV prefix byte-identical.

Raw C has equivalent ordinary final results but different private scratch
registers and copy access order. At return, raw T6/T7/T8 hold snapshot X/Y/Z;
retail AT/T8 hold Z/Y, raw AT retains its incoming value, and retail T6/T7 retain
theirs. All other modeled registers, FPRs and memory agree. Guarded C agrees
literally with retail, including accesses and fired fault prefixes.
Do not claim literal raw-register or raw-fault-prefix identity.

## Caller Bounds

The aligned retail scan finds no direct JAL and one literal target pointer:
ROM 22E78C / VA 80089CCC, slot 5 of D_80089CB8. These are static observations,
not proof against dynamically constructed targets.

Execute the actual dispatcher window 1513D034..1513D070, stopping before the
mapped boundary word at 1513D070. Verify the byte slot load, table lookup,
JALR, actor/flag saves, leaf return, actor reload, nonzero-return branch and
signed flag reload. Ten phases cover two SP phases and five flag-byte values.
The integer-1 result preserves the restored flag rather than forcing it to 1.

The complete func_1513CFE4 dispatcher remains an unchanged 12-byte production
stub. Earlier gates and later stages are not executed. Flag-byte boundaries
extend the bounded window's entry contract; do not claim full caller or
natural gameplay acceptance.

## Qualification

Tools, identical in both local copies:
`experiments/game_damped_motion_snapshot.py` and
`tests/test_game_damped_motion_snapshot.py`.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 4.050s | 8 tests, 3.965s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 1.857s | 2 tests, 1.816s | 0 / 0 / 0 |

Explicitly reuse the other six pre-install checks per copy only under strict
source, raw/padded object, guard, helper/input and complete-image identity.
They are not fresh installed executions. Shared tools checks pass in both
copies (0.143/0.115s). Routine Codex work uses zero Claude calls.

- 2,304 finite guest phases visit all 42 words, cover live-step aliases, verify
  full fences, independent numerical results and the raw register relation.
  Eight additional phases preserve unusual snapshot words bit-for-bit.
- Native32 O0/O2/O3 each pass 96 selected-body cases with trap UBSan and
  whole-arena fences. Seven effective defined wrong-C controls cover late/
  narrow snapshots, missing horizontal damping, incorrectly damped Y, old Y,
  fixed timestep and wrong return. Keep the established generic-view alias
  flag and aligned freestanding entry; do not infer ISO layout portability.
- An actual compiled cached-timestep wrong-C body fails a bounded guest alias
  witness after the snapshot changes the timestep. This is emitted-read
  evidence, not portable C concurrency.
- Six independent GNU links cover three entry/global rebases and 24 phases,
  including signed-low relocation boundaries. Check 216 fired guarded
  root-data fault prefixes, twelve guard corruption controls and six strict
  whole-image corruptions. Raw fault-prefix identity is explicitly unclaimed.
- Pin 28 historical inputs, the retained GLOBAL_ASM input and old padded
  object. Preserve all 35 raw/padded neighbors and pools. Independent GNU
  assembly agrees with normalized words/bindings. Actual Make's five
  productive owner commands reproduce the qualified raw/padded output.

## Production

Commit tools first: `e9b7a5ed89a7e30c09307d81448978a5d8317565`. No push.
Preserve all 1,550 prior older-mirror dirty paths, statuses, hashes and HEAD;
add only two task files, leaving 1,552 dirty paths. Do not reset or commit it.

Seal 15,846 files, including all 1,454 linker objects. Normal Make in the
verified Linux copy completes in 0.529s. Mark only the verified target-only
guard append old to avoid unrelated rebuilds. The duplicate generated_12D630
recipe warning and existing owner pointer/integer warning at the
func_1514BF50 call remain. Owner diagnostics are unchanged and isolated target
diagnostics are empty; this is not a warning-free or clean-from-scratch build.

Every static input and non-target object remains byte-identical. Revalidate
live bytes before and after adopting only the owner object, ELF, linker script
and progress CSV; linker-script and conversion-CSV bytes remain unchanged.
Live adoption audit: 42.469s.

The independent full-ELF prediction is reproduced with zero exclusions:
**139 changed bytes =138 code bytes +1 target-size metadata byte**.
Preserve all other 6,054 bodies, all 6,055 addresses and all 720 protected
Game-data owners / 189,088 bytes. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
ELF SHA-256:
`e67fa8d07884ef2f7722b75813bd3490e7094a3c8d9af70c5b97eaff818baefd`.
Padded owner SHA-256:
`13421023ad95da185d2f46076169225489325f3fdcf19307afd39c45b46d4550`.

## Handoff

The standard matcher against the actual live ELF completes in 33.012s:
total **3,737/5,505 (67.88%)**, Game **3,064/4,832 (63.41%)**,
Init 492/492 and Debugger 181/181 exact. Zero address drift; 1,768 different.
The 75% threshold remains 4,129 exact, requiring **392 more matches**.
Queue shapes: 1,637 placeholders, 122 semantic/other and nine unlocated.
Next func_15192D48 is screened only, unmodified and uncredited.
Keep func_1508CAD8's 862-word stub queued.

Root README changes only its two aggregate rows. Details belong here and in
concise indexes. Post-commit graph-worker and every-old-node retention audits
remain private receipts; retain excluded-corpus/large-HTML caveats without
claiming full re-extraction or a fresh corpus-membership count.
Frozen host Release remains untouched.
