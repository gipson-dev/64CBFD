# Game contact-effect update private screen

**Follow-up:** [Note 2361](2361-game-contact-effect-update-match-20261113.md)
records the subsequent caller qualification and production match. The counts
and pending work below describe this earlier private screen.

Date: 2026-11-13. `func_1516A3F4` remains a production placeholder and is
not counted as a match. Its 81-word retail body occupies VA
`0x1516A3F4..0x1516A538` and ROM `0x1978A4..0x1979E8`, in
`generated_197120.c`. A private typed C reconstruction refreshes a height
through two helpers when the current height reaches a signed threshold,
optionally constructs a 24-byte contact-effect descriptor, and otherwise
damps two signed motion halfwords. The threshold is captured before helper
calls; the helpers can change the record fields later read by the routine.
The helper `func_15167AD8` copies all 24 descriptor bytes, including bytes
not initialized by this function.

The selected candidate has the retail 80-byte frame, the retail saved
register positions, the threshold spill at incoming SP minus 8, and the
descriptor at incoming SP minus 36. It has 17 differing instruction positions
from compiler register allocation and one independent store/move schedule.
Seventeen relocation-aware checked words produce the exact retail body in
both supported padders; no production guards were installed. The three other
owner functions, constant pools and compiler diagnostics remain unchanged.

Tools commit `42b87d1` preserves the candidate and reproducible private tests:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_contact_effect_1516a3f4_match -v
```

The independent guest model passed 640 cases per stream across retail, raw C,
and both padded objects. It compares all 24 descriptor bytes and tests helper
mutations, threshold extremes and finite damping factors. The 32-bit native
model passed 160 cases at each of `-O0`, `-O2` and `-O3`, with UBSan and
seven effective negative controls. Retail and both padded streams agree at 94
access-boundary prefixes across four selected cases. Twelve GNU links across
three symbol layouts validate the guarded objects against rebased retail.
The suite passed with mounted tools and staged sibling dependencies. These
checks use modeled helpers; they do not prove full helper behavior, every
possible alias, floating-point exception behavior, or gameplay.

An actual-Make private owner build and independently predicted shadow link
changed only this body among 6,051 functions, with all addresses fixed, all
189,088 protected Game-data bytes unchanged, and 244 image bytes accounted for
without exclusions. The 1,454 production input objects remained unchanged.
No production source, linked image, guard manifest, or match count changed.

The function address is the eighth entry of the distinct data table at
`0x8008C9C8`. That table starts immediately after the 104 records of the
`0x34`-byte descriptor array beginning at `0x8008B4A8`. The retail dispatcher
`func_1516944C` clamps its descriptor index to 103, so its `+0x1C` callback
is not a call through this separate table. A subsequent census of the full
retail code image, including routines absent from the tracked assembly tree,
found indexed loads at `0x15167E98` and `0x151689EC`. Original caller windows
in `func_15167E0C` and `func_15168870` select entry 7 from the signed bytes at
record offsets `0x2F` and `0xB2`, respectively, and pass the record in A0.
Both windows passed 144 cases per instruction stream with entry 7 selected.
The tests start at the bounded dispatch windows and do not establish every
possible source of those record fields or qualify the complete parents.
Production adoption, a fresh linked recount, and the remaining integration
checks are still required before match credit.

Game remains **3,749 / 4,843 (77.41%)**, total **4,422 / 5,516 (80.17%)**,
with zero address drift and **126** additional Game matches needed for 80%.
