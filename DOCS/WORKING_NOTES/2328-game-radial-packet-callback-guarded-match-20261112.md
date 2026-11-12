# Radial packet callback guarded match

Date: 2026-11-12. `func_151470FC` in `conker/src/game/generated_173D40.c`
replaces a zero-return placeholder with the recovered 15-argument radial
callback. Its 135-word slot spans VA `0x151470FC..0x15147318`, ROM
`0x1745AC..0x1747C8`. The original symbol is retained because a more specific
name is not established. `D_8008AA00[22]` points to it; an aligned ROM scan
found that table pointer and no direct JAL. The recovered dispatcher
`func_1514C2F0` passes a byte angle and uses the callback's return to decide
whether to continue its loop. Other table users and full dynamic dispatch are
not exhaustively qualified.

The callback initializes selected fields of a 112-byte effect descriptor,
consumes five integer and two floating random values in retail order, obtains
a direction, and submits the descriptor. On successful allocation it copies a
four-byte parameter to offset `0xA8` of the returned object, then returns 1;
the null path also returns 1. The factory copies the complete descriptor,
including reserved bytes that retail leaves uninitialized, so the source does
not zero or invent those fields. The position, color, flags, dimensions and
parameter reads retain retail order. Constants and helper names remain the
existing project symbols.

IDO O2/g3 emits 135 words with the retail `0xA0` frame and 16 relocation sites.
Ten expected-word guards normalize a closed floating-register allocation group.
The eleventh restores retail's signed-halfword reload of the angle argument:
the existing dispatcher interface passes a byte. In an adversarial guest test,
a helper changes the incoming home to `0x12348001` after the call begins;
the raw byte-typed C emits angle `1`, while retail and guarded output pass
`0xFFFF8001`. The guarded result preserves retail in this case; unrestricted
portable-C stack alias and fault equivalence is not claimed. Both padders agree
on all 13 owner functions and reproduce all target words; all 12 other raw
owner bodies and their diagnostics are unchanged.

The eight-check suite passed in the mounted and staged sibling tools
environments before installation, and the full staged sibling suite passed
again after installation. It compares 1,920 modeled cases per raw,
retail and guarded body, visiting all 135 retail words. The model checks the
full 112-byte descriptor snapshot and allocation-success/null paths, helper
mutations, flags, random order and copy contents. SDK32 native checks run
4,096 defined cases at each of O0/O2/O3 with trap UBSan and reject 14 wrong
variants. The suite includes 22 expected-word corruption rejections, four GNU
relocation rebases, 80 cases through the original dispatcher window, the
argument-home alias above, and 80 cases through the real factory wrapper,
factory body and memcpy. The connected factory visits 18/18 wrapper, 41/61
factory and 11/11 memcpy words; allocation is modeled. The mounted owner,
native, dispatcher, alias and connected-factory checks passed after install.
Other helper returns and bounded floating arithmetic are modeled; hardware
floating exceptions, full dispatcher/factory paths and gameplay are not
claimed. Sibling validation uses staged changed files with sibling dependencies
and mounted fallbacks, preserving its pre-existing dirty work.

Actual scoped Make reproduced the independently predicted linked ELF: 483
changed bytes, two audited symbol-order groups, zero exclusions, all 6,050
function addresses and 12 neighboring owner bodies unchanged, and all 189,088
protected Game-data bytes unchanged. The link held 1,453 other objects and the
linker script fixed; this was not a clean rebuild. Make's binary matches an
independent objcopy. ELF SHA-256
`195f017efdbcf8505336e5ee68ac7939eac10356cd7efcdd8bdd1c5dac75b695`;
binary SHA-256
`46c2f02e7c376330662ede453171eb132e7bab68ddeb00efbe598de45e709958`.
The pre-existing duplicate `generated_12D630` recipe warning remains; a full
ROM checksum was not re-established. Tools commit `d71abba` precedes the
consumer change.

A read-only host-port spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; its active-build applicability
is unknown. No host build or gameplay test was performed.

Fresh production recount: Game **3,719 / 4,840 (76.84%)**, overall
**4,392 / 5,513 (79.67%)**, zero drift. Game needs 153 more exact functions
to reach 80%. The previously unresolved interpolated callback group in
[Note 2310](2310-game-interpolated-callback-dispatch-and-return-20261112.md)
remains a separate candidate with return-contract and qualification work open.

A scoped Graphify refresh retained unrelated nodes: 59,914 before and 59,916
after; three relocated IDs matched by signature. Its fail-closed path retained
31,816 existing nodes. This was not a full-corpus extraction.
