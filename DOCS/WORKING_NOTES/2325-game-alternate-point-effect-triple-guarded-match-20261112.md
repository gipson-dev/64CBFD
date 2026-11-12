# Three alternate actor point effects guarded match

Date: 2026-11-12. `func_15147318`, `func_15147478` and `func_151475D8`
in `conker/src/game/generated_173D40.c` replace zero-return placeholders.
Their executable slots each contain 88 retail words, at VAs `0x15147318`,
`0x15147478` and `0x151475D8`, respectively. The third layout slot also has
two padding words. The retail symbols are retained because more specific
original names are not established.

All three resolve the selected actor point and optional height result through
`func_15146890`, call an indirect effect-slot provider, and submit the main
point effect. At amounts of at least 115, `func_15147318` submits an extra
slot-0 effect before the provider; the other two submit slot-6 and slot-11
extra effects after the main effect. Their provider pointers are read from
`D_8008FD04`, `D_8008FD1C` and `D_8008FD30`. The source explicitly sequences
the provider call before reading the main effect arguments: a native test of
an earlier unsequenced expression exposed a difference when the provider
mutated actor and scale data. Original callback table `D_8008A0B4` entries 6,
15 and 16 contain these functions, each with count 130; this identifies the
examined routes rather than proving every runtime caller.

Each semantic body emits 88 instructions and the retail relocations. IDO uses
a `0x60` frame rather than retail's `0x58`; 19 expected-word guards per body
normalize the frame and stack offsets, for 57 guards and no insertions. Both
padders preserve all 13 owner functions and reproduce the three retail bodies.
An adversarial selector write demonstrates that the raw and retail private
mode slots differ; the guarded output restores retail's behavior. That check
stops before return because the written raw slot overlaps retail's saved return
address. Arbitrary stack alias and fault equivalence is not claimed for the
unadjusted compiler output.

The nine-check suite passed in the mounted environment after installation and
in the staged sibling environment before and after installation; the mounted
pre-install run covered the first eight checks together and the added alias
check separately. A later whitespace-only source and manifest cleanup rebuilt
to the identical owner object, ELF and binary; the owner and native checks
were rerun in the mounted environment and all nine in the staged sibling. It includes 4,608 modeled guest/reference cases per target
and per raw, retail and guarded body, covering all mode bytes and 87 of 88
retail words per target. Another 120 cases per target cover actor overlap with
the provider pointer or constants. SDK32 native tests run 1,440 cases per
target at each of O0/O2/O3 under trap UBSan, with five effective negative
controls per target. They use finite in-range float-to-unsigned conversions.
There are 114 guard-corruption rejections, twelve GNU relocation rebases and
320 original dispatcher-window cases per target. Another 112 cases per target
execute the actual retail provider bodies, reaching all 30, 22 and 22 provider
words respectively; only the random-number return is modeled there. Other
helpers and FCSR behavior are modeled. These checks do not prove hardware FPU
exceptions, NaN payloads, native out-of-range conversions, complete dispatch
or gameplay. The staged sibling used available sibling dependencies with mounted
fallbacks; its existing dirty work was preserved.

Actual scoped Make produced the independently predicted complete ELF: 1,016
changed bytes, eight audited symbol-order groups, zero exclusions, all 6,050
function addresses and ten neighboring owner bodies unchanged, and all 189,088
protected Game-data bytes unchanged. The link held 1,453 other existing
objects and the linker script fixed; it was not a clean rebuild. Make's binary
matches independent objcopy output. ELF SHA-256
`4430041ecbe8cf64f94e937f467a9982ca4d1f4b03425c1eb658ab604eb7f9f2`;
binary SHA-256
`78709f9e2323916f97952f595721917e95e793e61cdc49acd577488a97626015`.
The existing duplicate `generated_12D630` recipe warning remains; a full ROM
checksum was not re-established.

Tools commit `3963a2d` precedes the consumer change. A read-only host-port
spot check found empty generated definitions for all three functions in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; active-build applicability is
unknown. No host build or gameplay test was performed.

Fresh production recount: Game **3,716 / 4,840 (76.78%)**, overall
**4,389 / 5,513 (79.61%)**, zero drift. Game needs 156 more exact functions
to reach 80%.

The scoped graph refresh retained unrelated nodes: 59,908 before and 59,910
after, with no out-of-scope removals or changes; three relocated IDs matched
by signature. A second refresh after whitespace cleanup found no topology
changes and retained all 59,910 nodes. The fail-closed path retained 31,816
existing nodes. Neither refresh was a full-corpus extraction.
