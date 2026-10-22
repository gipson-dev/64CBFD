# Five-Field Motion Callback Direct C Match

Date: 2026-10-22

## Result

Recover `func_150BA37C` in `conker/src/game/generated_E7380.c` from its
zero-return placeholder. All **42 words /168 bytes, frame0 and four
relocations** emit directly from C under the existing O2/g3 profile.
No guards, inserted instructions, dummy locals or compiler-profile changes.

VA150BA37C..150BA424 / ROME782C..E78D4, ends exclusive. Preserve the original
`conker/asm/E7380.s`. Keep the address-based name, descriptive actor parameter
and purpose comment; use local float declarations, not shared ABI changes.
The prior body was12 bytes in its168-byte slot. Converted-C totals do not
change; this earns one additional exact C match.

Raw unlinked body SHA-256:
`07ac720d5bad10b3ba758e5d4e17f587821f2c77cbde91d8b5405e780c94645e`.
Pin the four HI16/LO16 bindings to D_800BE9A4 and D_8009FE2C as well as bytes.
A literal -0.6f screen has the same raw words but a different constant-pool
binding, so raw bytes alone do not qualify that alternative.

## Recovered Contract

Take one backed actor byte pointer. Add D_8009FE2C * D_800BE9A4 to the float
at actor+0x114, then advance these destination/source pairs in order:

| Destination | Source |
| --- | --- |
| +0x34 | +0x110 |
| +0x38 | +0x114, after acceleration |
| +0x3C | +0x118 |
| +0x40 | +0x11C |
| +0x44 | +0x120 |

Each update adds source * the live D_800BE9A4 timestep to its destination.
Preserve distinct single-precision multiply/add rounding and all repeated
timestep loads. D_8009FE2C is the existing BF19999A float
(-0.6000000238), not a newly emitted constant pool. Return the full integer1.
Do not collapse the repeated loads into a cached timestep or use the old
vertical value for the +0x38 update. Both global and explicit pointer source
forms match; install the simpler direct-global form.

Ordinary numerical/native evidence is bounded to finite float inputs,
including signed zero, adjacent values and subnormals. Guest alias cases
qualify emitted accesses when the timestep overlaps record fields. They do
not establish arbitrary portable C global-object aliasing, fault semantics,
MMU behavior, FCSR/NaN behavior or gameplay parity.

## Callback Bounds

The aligned retail scan finds no direct JAL and one literal function pointer,
at ROM22E788 /VA80089CC8: slot4 of D_80089CB8. These are static observations,
not proof against dynamically constructed references.

Execute the actual dispatcher window starting at1513D034 and stopping before
1513D070. Map the real boundary word for the leaf return but do not execute it.
This covers the byte slot load, table lookup, actual JALR, actor/flag saves,
leaf return, actor reload, nonzero-result branch and signed flag reload.
Ten phases cover two SP phases and five flag-byte patterns. The nonzero
return must preserve the restored flag instead of setting it to1.

The full parent `func_1513CFE4` remains an unchanged12-byte production stub.
Its earlier activity/timer gates and later dispatcher stages are not executed.
Flag-byte boundaries extend the bounded window's entry contract; do not claim
that every boundary pattern is produced naturally by the parent.

## Qualification

Tools, identical in both copies:
`experiments/game_five_field_motion.py` and
`tests/test_game_five_field_motion.py`.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 7 tests,104.060s | 7 tests,79.537s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests,1.997s | 2 tests,1.986s | 0 / 0 / 0 |

Explicitly reuse the other five pre-install checks per copy only under strict
source, raw/padded object, helper/input and complete-image identity. They are
not fresh installed executions. Shared tools checks pass in both copies
(0.115/0.107s). Routine Codex work uses zero Claude calls.

- 2,304 guest phases visit every target word and check independent numerical
  effects, live-step aliases, literal modeled register state and full fences.
- Native32 O0/O2/O3 each pass96 selected-body cases with trap UBSan, separate
  multiply/add and whole-arena fences. Five effective defined wrong-C controls
  reject wrong acceleration sign, source, destination, return and old vertical
  value. Use the existing generic-view alias flag; do not infer ISO object
  layout portability from that compiler configuration.
- An actual compiled cached-timestep wrong-C control fails a bounded guest
  alias witness after the vertical store changes the timestep.
- Six independent GNU links cover three entry/global rebases and24 phases,
  including signed-low relocation boundaries. Check192 fired root-data fault
  prefixes with exact partial state/accesses and eight strict image corruptions.
- Pin28 historical inputs and the old padded object. Preserve all three
  raw/padded neighbors and pools. Independent GNU assembly agrees in words
  and bindings; actual Make's three productive owner commands agree too.

Harness bring-up corrected a five-command recipe assumption, missing relocation
anchors, connected-code map shape and native32 process-entry stack alignment.
GDB identified the native fault as a misaligned MOVAPS; force_align_arg_pointer
on the freestanding _start fixes that fixture. The successful fresh runs above,
not earlier failed attempts, are the qualifying receipts.

## Production

Commit tools first: `a185029074d75e6e4174c4944d8a62daabc9fd1f`. No push.
Preserve all1,546 prior older-mirror dirty paths, statuses, hashes and HEAD;
add only two task files, leaving1,548 dirty paths. Do not reset or commit it.

Seal15,838 files, including all1,454 linker objects. Normal Make in the
verified Linux copy completes in17.610s. The unchanged guard manifest's newer
timestamp also refreshes stale objects: the log contains695 C compiler
invocations. Existing-source pointer/type and toolchain warnings, plus the
duplicate generated_12D630 recipe warning, are visible; this is not a
warning-free build. Target isolated/owner diagnostics remain empty.

After the build, every static input and non-target object is byte-identical to
its sealed predecessor. Revalidate live bytes before and after adopting only
the owner object, ELF, linker script and progress CSV. Linker-script and
conversion-CSV bytes are unchanged. Adoption audit:44.437s.

The strict independent full-ELF prediction is reproduced with zero exclusions:
**154 changed bytes =136 code +1 target-size +17 serialization bytes**.
GNU ld rotates the three adjacent absolute-symbol/string slots D_800D9910,
D_800D1340 and D_80088510. Validate their original values, flags, absolute
section,16-byte symbol stride and11-byte strings before predicting that
rotation. All symbol meanings remain fixed except the target size12->168;
do not ignore metadata sections.

Preserve all other6,054 bodies, all6,055 addresses and all720 protected Game-data
owners /189,088 bytes. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
ELF SHA-256:
`82c750ce6f092244dbcadb960ad4ffdf7d1bce4fe21ee619508fddbb34ce2f9c`.
Padded owner SHA-256:
`fdf0b384afe218ae919c9ca75c9f558cdd0a4edc16eb6c8ad388f4dccf508f54`.

## Handoff

The standard matcher against the actual live ELF completes in29.864s:
total **3,735/5,505 (67.85%)**, Game **3,062/4,832 (63.37%)**,
Init492/492 and Debugger181/181 exact. Zero address drift;1,770 different.
The75% threshold remains4,129 exact, requiring **394 more matches**.
Next `func_15110600` is screened only, unmodified and uncredited.
Keep `func_1508CAD8`'s862-word stub queued.

Root README changes only its two aggregate rows. Detailed progress belongs
here and in concise indexes. Post-commit graph-worker and every-old-node
retention audits remain private receipts; retain the excluded-corpus/large-HTML
caveats without claiming full re-extraction or a fresh corpus-membership count.
Frozen host Release remains untouched.
