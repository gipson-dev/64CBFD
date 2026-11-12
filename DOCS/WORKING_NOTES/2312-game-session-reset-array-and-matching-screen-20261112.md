# Session reset array and matching screen

Date: 2026-11-12. Follow-up to [Note 2293](2293-game-session-reset-private-screen-20261112.md). `func_1500E5C0` remains uninstalled and uncredited.

The retail reset clears exactly 20 bytes beginning at `D_800E0950` and stops at
`D_800E0964`. Retail data table `D_800AB140` contains exactly 20 halfword
resource IDs. Existing `func_151D2AB0` and `func_151D2B4C` index the counter
range alongside this resource table; one direct retail caller uses index 6 and
another passes a value read from a resource record. These observations support
a 20-byte counter array for the normal indexed domain; they do not prove that
arbitrary runtime indices are valid or checked.

A private header overlay changes the scalar declaration to
`extern u8 D_800E0950[20]` and rewrites the two resource functions' existing
`(&D_800E0950)[arg0]` accesses as array indexing. In an isolated owner compile,
all 19 functions and their instruction relocations remain unchanged; after
normalizing scratch filenames, diagnostics match. The observed `.text`,
`.rel.text`, `.options`, and `.reginfo` bytes also match. This owner has no
NOBITS sections. Debug and symbol table bytes differ, so this is not a
byte-identical object claim. Other direct and indirect users of the shared
header, their metadata, and the linked image have not been qualified; the
production header has not changed.

A private reset implementation using the array overlay and a target-only
`-O2 -g3 -Wo,-loopunroll,0` profile emits the 83-word retail length, with 54
identical linked word positions. Five normal-profile owner neighbors are
unchanged. Its recovered operations call the three initialization helpers,
clear the 20 counters, the paired 12-byte ranges and related globals, call
`bzero` for five bytes, and clear the remaining records. The original startup
caller `func_1500E470` invokes the routine without using a return value.

The chosen raw candidate matches retail's external memory state, modeled
helper call order, and external access trace in 24 bounded guest cases. It
also matches 882 external-access interruption prefixes over 12 fixtures;
comparison excludes stack-private accesses and does not prove hardware fault
semantics. An earlier 83-word shape ended with the same bounded final state but
wrote the counter bytes in a different order and failed that prefix test. A
separate 32-bit freestanding native screen passes 24 initialized fixtures at
O0/O2/O3; shortening the counter loop is detected at every optimization level.
The source explicitly lists four pointer stores in descending order because
this IDO profile schedules them in retail's ascending order. Native C access
order is not claimed to match the retail instruction trace.

A private expected-word map has 31 changed word/relocation positions, including
nine relocation changes. The in-memory padded object emits all 83 retail words
and preserves the other five owner functions. This is a private normalized
object, not a qualified production match; the mappings, relocation movements,
source types, whole-image effects and both tools environments still need
independent qualification. In particular, the first retail loop uses the
adjacent `D_800E0964` address as its end; the candidate expresses the same
current bound as array base plus 20, so any relocation audit must account for
the relationship between those symbols.

Private scripts and receipts are under the ignored
`conker/build/game-counter-array-type-screen/`, including `result.json`,
`pointer-shapes.json`, `pointer-reversed.c`, `pointer-reversed.o`,
`reset_guest_reversed.py`, `reset_fault_reversed.py`, `native_reset.py`,
`retail-map.json`, and `private-padded.json`. Scratch can be cleaned. The
following source pattern describes the candidate, not an installed change:

```c
for (i = 0; i < 20; i += 4) {
    D_800E0950[i + 1] = 0;
    D_800E0950[i + 2] = 0;
    D_800E0950[i + 3] = 0;
    D_800E0950[i] = 0;
}
```

Next, audit the complete shared-header dependency set, including stored and
NOBITS metadata, postprocessed objects, and actual build rules. Qualify the
31 mappings with effective controls, relevant rebases and branch-delay/fault
checks; then validate native and guest behavior, both tools environments,
actual production Make and independent full-image prediction before adoption
and recount. The last verified Game checkpoint remains **3,704 / 4,840
(76.53%)**, 168 matches short of 80%.
