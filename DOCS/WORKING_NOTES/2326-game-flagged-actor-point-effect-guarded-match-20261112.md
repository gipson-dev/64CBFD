# Flagged actor point effect guarded match

Date: 2026-11-12. `func_15146BF8` in `conker/src/game/generated_173D40.c`
replaces a zero-return placeholder with the recovered callback. Its 90-word
slot is at VA `0x15146BF8`, ROM offset `0x1740A8`. The original symbol is
retained because its more specific original name is not established.

When the actor attachment at `+0x1D4` exists and `func_15146890` succeeds,
the callback emits a point effect in slot 11 or 12 according to the low byte
of its fourth argument. It scales the signed amount and the live actor value,
then emits a second slot-2 effect when the reloaded amount is at least 115.
Original wrappers `func_15146BB8` and `func_15146BD8` supply zero and one in
the call delay slot; both eight-word wrappers already match retail in the
production ELF. An aligned static ROM scan found these two direct JALs and no
literal pointer to the callback; this census does not establish every dynamic
route. Helpers can change actor, input homes, result metadata or position, so
the recovered code preserves the observed read and call order.

The compiler emits all 90 instructions and matching relocations using a
`0x60` frame, while retail uses `0x58`. Twenty-one expected-word guards adjust
the frame and stack offsets. Both padders agree on all 13 owner functions and
produce the retail callback. An adversarial selector write distinguishes the
raw and retail private mode slots; the guarded output matches retail. That
check stops before return because one adversarial write overlaps retail's
saved return address. Portable unguarded C is not claimed equivalent for
arbitrary private-stack aliases or faults.

The seven-check suite passed in the mounted tools environment before installation
and in staged sibling tools dependencies before and after installation. It compares 32,768 modeled
cases each for raw, retail and guarded code, visiting 89 of 90 retail words;
it covers every mode and flag byte, the threshold, helper mutations and
bounded FCSR conversion. There are 16,384 finite, in-range SDK32 native cases
at each of O0/O2/O3 under trap UBSan and nine effective negative controls.
The suite also checks 42 corrupted guard inputs, four independent rebases,
256 cases through the original wrappers, and the private mode-slot alias.
The mounted owner, native and connected-wrapper checks passed again after
installation. Helper and FCSR behavior is modeled; hardware FPU exceptions,
NaN payload behavior, native out-of-range casts and gameplay are not claimed.
The sibling run uses staged changed files with available sibling dependencies
and mounted fallbacks, preserving the sibling's existing dirty work.

Actual scoped Make produced the independently predicted full linked ELF:
336 changed bytes, two audited symbol-order groups, zero exclusions, all
6,050 function addresses and 12 neighboring owner bodies unchanged, and all
189,088 protected Game-data bytes unchanged. The link held 1,453 other
existing objects and its linker script fixed; this was not a clean rebuild.
The Make binary matches independent objcopy output. ELF SHA-256
`3748072ba0c84ef8a57ecf3267d6c98565c8ef101fdd97f45675c0b1e1d17928`;
binary SHA-256
`b76254eb38fa8c354edbbdb709310d672446cbdeeda4145e5397ecdcfc0964d0`.
The pre-existing duplicate `generated_12D630` recipe warning remains; a full
ROM checksum was not re-established. Tools commit `c4b860c` precedes the
consumer change.

A read-only host-port spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; its active-build applicability
is unknown. No host build or gameplay test was performed.

Fresh production recount: Game **3,717 / 4,840 (76.80%)**, overall
**4,390 / 5,513 (79.63%)**, zero drift. Game needs 155 more exact functions
to reach 80%. The nearby unmatched `func_15146E84` remains a possible next
investigation; its random-dependent branches require separate qualification.

A scoped Graphify refresh retained unrelated nodes: 59,910 before and 59,912
after; three relocated IDs matched by signature. Its fail-closed path retained
31,816 existing nodes. This was not a full-corpus extraction.
