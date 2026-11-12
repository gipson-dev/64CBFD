# Actor script selection direct match

Date: 2026-11-12. `func_15079FBC` in `conker/src/game_A28B0.c`
replaces a zero-return placeholder with the recovered script-command handler.
The 81-word slot spans VA `0x15079FBC..0x1507A100`, ROM
`0xA746C..0xA75B0`. The existing symbol remains because its original descriptive
name is not established. The stale commented draft was removed after recovery.

For an inactive first object or speed below 5, the handler copies the script ID
byte to the current object, looks up a script and rewinds its pointer by one
five-byte script record. The original dispatcher advances the pointer by five
bytes immediately after the callback, so this resumes at the returned script.
Otherwise the handler copies the referenced movement value, derives a signed
speed using the `chased` flag and scale `D_8009A1E4`, updates command bytes,
invokes `func_15075F40`, and sets the current object's `0x40` flag. It reloads
the current-object pointer after helper calls as retail does. The existing
commented draft's pointer decrement of one represents five bytes because the
script record is five bytes; the lookup helper's verified interface takes two
arguments. The production scale word is `0x3F333333` (approximately 0.7).

`D_80086730[196]` contains the handler, and the connected original
`func_1507BC14` window loads its four command bytes, calls it, and advances the
script pointer. The original dispatcher is byte-identical to the live ELF;
this observed window does not prove all dynamic paths. The table declaration
uses a `void` callback, consistent with the restored function and the observed
caller, which does not consume its return value.

IDO O2/g3 emits all 81 retail words and 22 relocation sites directly from C,
with no new guards. Two independent padders agree on an isolated target, and
the production generic padder preserves all 210 other owner functions. Raw
owner neighbors, normalized constant pools, register metadata and compiler
diagnostic categories are unchanged. The semantic C is qualified on finite,
representable float-to-signed-halfword inputs and valid script-array pointers;
unrestricted portable-C conversion, pointer and fault behavior is not claimed.

The seven focused checks passed in both tools environments before installation;
after installation the mounted suite and staged sibling suite passed again with
expanded coverage of the actual 0.7 scale. The guest model compares 2,304 cases
per raw, retail and padded body, visiting 80 of 81 words. It tests the 5 and 17
boundaries, speed scaling, byte wrapping, overlapping first/current object,
and current-object changes during helpers. SDK32 native checks run 3,072 cases
per O0/O2/O3 with trap UBSan and reject 12 incorrect controls. There are four
independent GNU rebases, 256 original dispatcher-window cases and 96 cases
connected to the real 59-word lookup helper, covering 52 of its words across
null resource/table, local and fallback lookups. Ninety-three guest access-cut
prefixes check instruction-boundary behavior. Other helper effects and bounded
floating arithmetic are modeled; hardware FPU exceptions and full gameplay are
not claimed. The staged sibling uses its available dependencies with mounted
fallbacks; its existing dirty work was preserved.

Actual scoped Make produced the independently predicted complete ELF: 250
changed bytes, no metadata groups or exclusions, all 6,050 function addresses
and 210 neighboring owner functions unchanged, and all 189,088 protected
Game-data bytes unchanged. Owner literal pools and register metadata were also
checked. The link held 1,453 other objects and the linker script fixed; this
was not a clean rebuild. Make's binary matches an independent objcopy. ELF
SHA-256 `dc45b9902903fd428effdad879f70739dc5cf9440a7bcd001c65b456f434068d`;
binary SHA-256
`f8ff2ff2e0c766ce0b92650b7a192183da75fbc4434a1f19550a5ccfeb66f943`.
The owner retains pre-existing IDO warnings and the duplicate
`generated_12D630` recipe warning; warning categories did not change. A full
ROM checksum was not re-established. Tools commit `e3e24d2` precedes the
consumer change.

A read-only host-port spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; its active-build applicability
is unknown. No host build or gameplay test was performed.

Fresh production recount: Game **3,720 / 4,840 (76.86%)**, overall
**4,393 / 5,513 (79.68%)**, zero drift. Game needs 152 more exact functions
to reach 80%. Handwritten/custom-register routines remain in their separate
assembly-restoration workstream; the next C candidate requires a fresh audit.

A scoped Graphify refresh retained unrelated nodes: 59,916 before and 59,918
after; three relocated IDs matched by signature. Its fail-closed path retained
31,816 existing nodes. This was not a full-corpus extraction.
