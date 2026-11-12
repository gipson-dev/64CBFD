# Resource update callback direct match

Date: 2026-11-12. `func_151572D0` in
`conker/src/game/generated_183640.c` replaces its zero-return placeholder.
The retail slot is VA `0x151572D0..0x15157420`, ROM
`0x184780..0x1848D0`: **84 words**, frame `0x20`. All instructions and
eight named relocations emit directly from C under the existing IDO O2/g3
profile, with **no new guards, insertions, or profile changes**. The retail
symbol is retained because a more specific gameplay name is not established.

The callback updates a signed halfword lifetime when flag 1 is set. It uses
the wrapped stored halfword to decide expiration, then invokes up to two
indexed callbacks if their signed indices are not -1. A zero return marks the
record for release; the second callback is still called if the first returns
zero. If still active it updates the linked object, applies the flag-0x20
alpha fade using signed halfwords, and releases the record if expired. Fields
are reloaded after calls, so callbacks can alter later decisions. The local
record view has a GNU may-alias annotation, and the two callback tables use
byte-pointer arguments consistent with the already-converted entries. Some
other table entries remain placeholders; these checks do not restore them.
Guest tests use valid callback-table indices; invalid-index C behavior is not
established.

The installed five-check suite passed in both mounted and standalone-sibling
tools environments. It includes 14,400 bounded guest/reference cases covering
all 84 retail instructions, callback results, timer wrapping and helper-driven
record mutations; 4,320 SDK32 native cases at each of O0/O2/O3 with trap UBSan
and four effective semantic negative controls; both padders and four rebased
GNU links; and 24 cases through the complete original primary list walker. The
walker uses descriptor columns 54, 76 and 91, in either list row. Downstream
callbacks and helpers are modeled; this is not a hardware or gameplay test.
The sibling run used staged new files and its own available dependencies with
mounted fallbacks where absent. Its pre-existing dirty work was preserved.

The actual Make owner compile, pad, and assemble produced the qualified
object, and a scoped Make link held 1,453 other existing objects and the
existing linker script fixed. This is not a clean rebuild. The complete ELF
equals the independently predicted image: **276 changed bytes**, zero
exclusions, one closed two-symbol metadata permutation, all 6,050 function
addresses and 25 owner neighbors unchanged, and all 189,088 protected Game
data bytes unchanged. Make's objcopy output equals the independent objcopy.
Production SHA-256: ELF
`43266c856c094940bd6970236d92cefad8b6178c5fe9eb0cb65903a775829af2`, binary
`0655dc430a43b0459d3d86b0aa8fe0f7fdfed14efc458f9fb20d258577564679`.
The existing duplicate `generated_12D630` recipe and unrelated owner
pointer/integer diagnostics remain. A full ROM checksum was not re-established.

Tools commit `ee46d43` precedes the consumer change. A read-only host-port
spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; its active-build applicability
is unknown. No host build or gameplay test was performed.

Fresh production ELF recount: **3,708 / 4,840 (76.61%)** Game and
**4,381 / 5,513 (79.47%)** overall, with zero address drift. Game needs 164
more exact functions to reach 80%. The three interpolation candidates in
[Note 2317](2317-game-interpolated-selector-zero-domain-20261112.md) remain
private.

The scoped graph refresh retained unrelated nodes: 59,894 before and 59,896
after, with no out-of-scope removals or changes. Three relocated IDs matched
by signature; the fail-closed path retained 31,816 existing nodes. This was
not a full-corpus extraction.
