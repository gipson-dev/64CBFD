# Secondary callback walker guarded match

Date: 2026-11-12. `func_151671E8` in `conker/src/game_1944C0.c` now
recovers the secondary registered-callback walker at VA
`0x151671E8..0x15167310`, ROM `0x194698..0x1947C0`. It traverses two
rows of 101 lists, preserves the next node across each callback, and tracks
nesting depth. The 74-word body matches retail with **35 expected-word guards**
and no inserted words. This is a guarded match, not a direct compiler match.

The shared `struct115` callback field and the caller declaration now use a
compatible `void (u8 *)` callback signature. `func_151AD174` remains an
unimplemented placeholder: its C signature was corrected, with one additional
guard preserving the previous placeholder's generated words. It is neither a
new retail restoration nor a credited match. The other two registered
callbacks, `func_151ACB60` and `func_151041E4`, already use the compatible
signature. All 16 functions in the caller owner and all 33 in the placeholder
owner retain their previous bytes.

The nine focused checks passed in the mounted and standalone sibling tools
environments after adoption.
They cover 96 modeled guest cases with all 74 instructions visited, 96 native
cases at each of O0/O2/O3 with undefined-behavior sanitization and negative
controls, 32 modeled original frame-loop call windows, 240 connected cases
using the production timer callback with modeled downstream helpers, 12 symbol
rebases, 270 modeled access-cut triples, both padders, and corrupt-guard and
wrong-replacement controls. Actual SDK layout checks cover IDO and native32,
including a negative control. Modeled callbacks and bounded cases do not prove
hardware behavior or gameplay.

The shared-header audit identified 293 possible source consumers, 292 existing
objects, and 301 Make-planned compilation profiles. An isolated before/after
overlay found no nondebug section, symbol, text relocation, or diagnostic
changes across those profiles, including 58 postprocessed generated inputs.
The include-graph scan left `PR/sptaskoff.h` unresolved; this audit is not a
claim that 301 production objects were rebuilt.

The actual Make build rebuilt the three affected owner objects and performed a
scoped link with 1,451 other existing linker-script objects and the existing
linker script held fixed. It is not a clean build. The resulting ELF exactly
matches the independently predicted image: 227 changed bytes, no exclusions,
all function addresses unchanged, and 189,088 protected data bytes unchanged.
The walker owner has 41 unchanged neighbors. Make's binary output matches the
independent objcopy. Production SHA-256: ELF
`7ef7a8774764d03c6abf45587a364a94d66158453c380a3ce8937d7444e0de68`, binary
`bb49a8834cfbb605d109da6b4cf82461cd3e6136f99a6c2ac5b38697d2687d64`.
The existing duplicate `generated_12D630` recipe and pointer/integer warnings
remain. A full ROM checksum was not re-established.

Tools commit `d88695c` precedes the consumer change. The standalone sibling
tools checkout's pre-existing dirty work was preserved; its staged checks use
its own padders and fall back to mounted timer-oracle helpers when absent.
A read-only host-port spot check found empty generated definitions for the
walker and `func_151AD174` in `64CBFDOGL/recomp_scene/frontend_room_out/.c`;
their active-build applicability is unknown. No host build was performed.

The fresh production ELF recount is **3,707 / 4,840 (76.59%)** Game and
**4,380 / 5,513 (79.45%)** overall, with zero address drift. Game needs 165
more exact functions to reach 80%.

The scoped graph refresh retained unrelated nodes: 59,889 before and 59,892
after, with no out-of-scope removals or changes. Three relocated IDs matched
by signature; the fail-closed path retained 31,816 existing nodes. This was
not a full-corpus extraction.
