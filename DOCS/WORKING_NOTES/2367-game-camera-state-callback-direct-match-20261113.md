# Camera-state callback direct C match

Date: 2026-11-13. `func_15125924` in `game_14FF90.c` now matches all
82 retail words at VA `0x15125924..0x15125A6C`, ROM `0x152DD4..0x152F1C`.
All four helper relocation bindings emit directly from C; the owner padder
reproduces the retail body without guards. The recovered 48-byte frame and
structured pair of temporary values also retain the retail stack slots.
This resolves the private two-word and stack-overlap boundary in
[Note 2366](2366-game-camera-state-private-screen-20261113.md).

The callback reads an optional state pointer at camera offset `0x3D4`, a
float at state offset `0x1C` and a byte at `0x4E`. Camera flags and an actor
byte gate a helper call. Depending on that result and the captured values,
the routine may request state 13 and set camera flag `0x1000`; on another
path it may clear a float and publish a coordinate difference to two fields.
Names describe the observed accesses rather than a fully established gameplay
meaning. The two identified original caller windows at `0x15005718` and
`0x15122F50` pass their saved camera pointer; other computed or external
callers are not ruled out.

Tools commit `003a158` provides the focused checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_camera_state_15125924_direct -v
```

The independent guest model passed 2,304 non-overlapping cases per stream;
the two original two-instruction call windows each passed 192 modeled cases
per stream. Retail, raw C and the padded body have identical modeled machine
states in 2,112 deliberately overlapping camera/stack cases, including 32
identical modeled exceptions per stream. The earlier private candidate
differed in camera bytes in 508 of those cases. Eighty-nine injected access
prefixes agree across the three instruction streams. Native 32-bit checks
passed 3,072 defined-domain cases at each of `-O0`, `-O2` and `-O3` with
UBSan and six effective negative controls. Nine GNU links across three layouts
verify the original helper bindings. The suite passed before and after
installation with mounted tools and staged sibling dependencies; project tool
checks passed. Helpers are modeled, the caller windows are bounded, and these
checks do not establish exceptional float conversion, full callers, hardware
fault behavior or live gameplay.

The actual production object and ELF equal the independently audited
Make-planned shadow. Its strict prediction accounts for 253 changed ELF bytes
with zero exclusions: only this body changes among 6,051 functions, all
addresses remain fixed, and all 189,088 protected Game-data bytes are
unchanged. The 44 other owner functions, constant pools, normalized compiler
diagnostics, existing guards and the other 1,453 linked objects are unchanged.

The actual recount is Game **3,755 / 4,843 (77.53%)**, total
**4,428 / 5,516 (80.28%)**, zero drift, with **120** more Game matches
required for 80%.
