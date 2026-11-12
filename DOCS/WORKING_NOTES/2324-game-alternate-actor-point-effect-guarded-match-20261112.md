# Alternate actor point effect guarded match

Date: 2026-11-12. `func_150BED4C` in
`conker/src/game/generated_EBE60.c` replaces a zero-return placeholder. The
89-word executable slot is VA `0x150BED4C..0x150BEEB0`, ROM
`0xEC1FC..0xEC360`; retail uses a `0x58`-byte frame. The retail symbol is
retained because a more specific original name is not established.

Like its matched companion `func_150BEACC`, this callback resolves a
mode-selected point and height result, submits slot 11 on success, and submits
an additional effect for amounts at least 76. It uses the alternate selector
`func_150BEC30` and its own scale and tag constants. Callback table
`D_8008A0B4` entry 18 contains its address and count 85; other runtime callers
are not ruled out. The first effect can modify the point and result metadata
before the second effect reads them.

A normal local `2.0f` multiplier makes IDO emit retail's floating multiply.
The semantic C has all 89 instructions and relocations, but its raw frame is
`0x60` rather than `0x58`. Seventeen expected-word guards normalize the frame
and corresponding incoming and local stack offsets; no instructions are
inserted. The selected source shape preserves the point and result addresses
passed to helpers relative to the incoming stack, unlike a shorter-guard
variant screened during investigation. Both padders reproduce all 89 retail
instructions and all seven padded owner functions. A modeled selector write to
the two private mode slots produces distinct raw and retail mode values; the
guarded output preserves retail's mode. That test stops before return because
the written raw slot overlaps retail's saved return address. Arbitrary stack
alias and fault equivalence is not claimed for the unadjusted C output.

The seven-check suite passed in mounted and staged sibling tools environments
before and after installation. It includes 16,384 bounded guest/reference
cases per raw, retail and guarded body, covering all 89 retail instructions,
all mode bytes, inactive/active paths, the 75/76 threshold, modeled helper
mutations and floating-point control behavior. SDK32 native tests ran 4,096
cases at each of O0/O2/O3 with trap UBSan and eight effective negative
controls, limited to finite in-range float-to-unsigned conversion. The suite
also checks 34 corrupt guard rejections, four GNU rebases, and 320 modeled cases
per body in the original dispatcher windows. The FCSR model is not proof of
hardware exceptions or NaN payloads; native out-of-range conversions, complete
helpers and gameplay are not claimed. Existing sibling dirty work was preserved.

Actual scoped Make produced the independently predicted complete ELF: 366
changed bytes, four audited symbol-order groups, zero exclusions, all 6,050
function addresses and six neighboring owner bodies unchanged, and all
189,088 protected Game-data bytes unchanged. The link held 1,453 other
existing objects and the linker script fixed; it was not a clean rebuild.
Make's binary matches independent objcopy output. ELF SHA-256
`d2e69ab2437db5ebf8f2faa112f40ddbd5438050cd53c473b6bfa69ffb9681f9`;
binary SHA-256
`8d8f8fa3963544eac5997229812f7a8fdd25b103ddd1dc6f55751e59b788aa9d`.
The duplicate `generated_12D630` Make recipe warning remains; a full ROM
checksum was not re-established.

Tools commit `adf7281` precedes the consumer change. A read-only host-port
spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; active-build applicability is
unknown. No host build or gameplay test was performed.

Fresh production recount: Game **3,713 / 4,840 (76.71%)**, overall
**4,386 / 5,513 (79.56%)**, zero drift. Game needs 159 more exact functions
to reach 80%.

The scoped graph refresh retained unrelated nodes: 59,906 before and 59,908
after, with no out-of-scope removals or changes; three relocated IDs matched
by signature. The fail-closed path retained 31,816 existing nodes. This was
not a full-corpus extraction.
