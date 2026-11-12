# Actor point effect guarded match

Date: 2026-11-12. `func_150BEACC` in
`conker/src/game/generated_EBE60.c` replaces a zero-return placeholder. Its
89-word executable slot is VA `0x150BEACC..0x150BEC30`, ROM
`0xEBF7C..0xEC0E0`; the frame is `0x58` bytes. The retail function symbol is
retained because its original name is not established.

When the actor's attached pointer is present, the routine calls the already
matched `func_150BE9B0` to resolve a mode-selected point and query result. On
success it submits effect slot 11, using the requested amount, live actor tag,
point and result. For amounts at least 76 it also calls `func_15142180` with
the point and the current result metadata; the first effect may update those
values before the second call. Retail callback table `D_8008A0B4` entry 17
contains this address and count 85. This identifies the examined table entry,
not every possible runtime caller.

The compiler emits 87 of the 89 instructions and all relocations directly.
Two checked guards move the saved mode temporary from stack offset `0x20` to
retail's `0x24`; there are no inserted words. Both padders reproduce the exact
retail body and all seven padded owner functions. A modeled helper deliberately
writing both private slots exposes different raw and retail modes; the guarded
body preserves retail's result. Thus arbitrary stack alias/fault equivalence
is not claimed for the unadjusted C output.

The seven-check tools suite passed in mounted and staged sibling environments
before and after installation. The bounded guest/reference screen ran 16,384
cases for each raw, retail and guarded body, covering all 89 retail words,
all mode bytes, active and inactive actors, the 75/76 threshold, helper
mutations, non-finite test values, and a modeled floating-point control
register. The native SDK32 checks ran 4,096 cases at each of O0/O2/O3 under
trap UBSan and rejected eight semantic negative controls; these native cases
use finite, in-range float-to-unsigned conversions. Four corrupted-guard
rejections, four GNU relocation rebases, and 320 modeled cases per body through
original dispatcher windows also passed. The FCSR model is not a hardware
exception or NaN-payload proof; native C conversions outside the representable
unsigned range and full gameplay are not claimed. Helpers and dispatcher
windows are modeled or bounded. Existing sibling dirty work was preserved.

Actual scoped Make produced the independently predicted complete ELF: 387
changed bytes, four audited symbol-order groups, zero exclusions, all 6,050
function addresses and six neighboring owner bodies unchanged, and all 189,088
protected Game-data bytes unchanged. The link held 1,453 other existing objects
and the linker script fixed; it was not a clean rebuild. Make's binary matches
independent objcopy output. ELF SHA-256
`463bc2fa46b845f8110f1a9235aa61472663bbd5a9b60c831b67aee91ac5b144`;
binary SHA-256
`235897e464597f4def0eb0051abbbaeba4254e90c5909d871a19a9ebb9406adf`.
The duplicate `generated_12D630` Make recipe warning remains; a full ROM
checksum was not re-established.

Tools commit `bfae0bf` precedes the consumer change. A read-only host-port spot
check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; active-build applicability is
unknown. No host build or gameplay test was performed.

The related `func_150BED4C` remains a placeholder. A private semantic C screen
emitted 85 words against its 89-word retail body because the compiler used a
different frame and optimized multiplication by `2.0f`; it is not counted.
See ignored `conker/build/game-actor-point-effect-pair-screen/` for the
candidate and variant receipts, which may be cleaned. Next: investigate the
second routine's valid source shape and qualify its call/alias/FPU behavior
and complete linked image before adoption.

Fresh production recount: Game **3,712 / 4,840 (76.69%)**, overall
**4,385 / 5,513 (79.54%)**, zero drift. Game needs 160 more exact functions
to reach 80%.

The scoped graph refresh retained unrelated nodes: 59,904 before and 59,906
after, with no out-of-scope removals or changes; three relocated IDs matched
by signature. The fail-closed path retained 31,816 existing nodes. This was
not a full-corpus extraction.
