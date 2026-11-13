# Game randomized impact callback direct match

Date: 2026-11-13. `func_151AC408` in `generated_1D92F0.c` replaces its
zero-return placeholder with the recovered impact-effect callback. Its
82-word body occupies VA `0x151AC408..0x151AC550` and ROM
`0x1D98B8..0x1D9A00`. Every instruction and relocation emit directly from C;
both supported padders match retail without added guards.

The callback captures the actor's payload and two coordinates from a signed
record index, combines them with the supplied height, and obtains an effect
selector. A random bit chooses between two effect submissions; the first
branch makes another random draw for a bounded parameter. The callback then
marks the originally captured payload as handled and returns 1. Its typed
record layout is shared with the previously recovered `func_151AC550`.
The tests allow helpers to change actor fields, payload contents and the
captured position after those values are read.

The target is entry 6 of `D_8008A430`. The original indirect callback window
in `func_15148BA4` passes the actor, three prior coordinates, height and the
address at actor offset `0x64`; 192 cases per stream exercised the bounded
window with the retail table entry checked. This does not qualify the complete
parent or every source of the selector.

Tools commit `ab3a2e3` provides the focused checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_impact_random_151ac408_match -v
```

An independent guest model passed 1,200 cases per stream across retail, raw
C, and both padded bodies, including both random branches, signed indices and
helper mutations. An earlier private sweep passed 2,880 cases per stream.
All streams agree at 126 injected access-boundary prefixes. Native 32-bit
checks passed 48 cases at each of `-O0`, `-O2` and `-O3`, with UBSan and seven
effective negative controls. Twelve GNU links across three symbol layouts
verified every stream against rebased retail. The suite passed before and
after installation with mounted tools and staged sibling dependencies;
project tool checks passed. The effect and random helpers are modeled here,
and the checks do not establish complete helper behavior, floating-point
exception flags, all possible aliases or live gameplay.

The production object and ELF equal the independently audited Make-planned
shadow; the other 1,453 linked objects remain unchanged. The strict image
prediction accounts for 247 changed bytes with zero exclusions. Only this
body differs among 6,051 functions; all addresses and all 189,088 protected
Game-data bytes remain fixed. The 32 other owner functions, constant pools and
compiler diagnostics are unchanged.

The production recount reports Game **3,753 / 4,843 (77.49%)**, total
**4,426 / 5,516 (80.24%)**, zero address drift, and **122** further Game
matches required for 80%.
