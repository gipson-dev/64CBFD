# Game actor-associated updater match

Date: 2026-11-14. `func_1511473C` now matches all 91 retail words at
`0x1511473C..0x151148A8` (ROM `0x141BEC..0x141D58`). Its `void` C body
replaces the zero-return placeholder in `conker/src/game/generated_13D350.c`.

Given a non-null actor and an index below the signed record count, the routine
calls `func_15114348` with the index and three actor-field addresses. It then
adds a scaled record float to the actor's halfword at `0x76`, converts the
result to an unsigned integer, and stores the low halfword. When the actor's
byte at `0x137` is set and the associated table entry equals index plus one,
it also writes that value to `0x7A`. The actual caller at `0x151142C0` passes
the actor in `a0` and the index in `a1`, and ignores the return value. The
count check does not reject negative indices on its own.

`func_15114348` is still a production placeholder. The modeled checks below
use a bounded helper stub, so this match does not establish the complete
behavior of the enclosing actor update or restore that helper.

The production compiler emits 58 of 91 retail words directly at their retail
positions, with the retail frame and control-flow shape. Thirty-three
relocation-aware, expected-word guards restore the remaining register
allocation; no instructions are inserted or omitted. The C expression preserves
the retail floating-add operand order. Both padding paths and 12 GNU links
across four independent symbol layouts produce the retail instruction stream;
all 33 neighboring functions and normalized constant pools remain unchanged.

Retail, raw C and guarded streams agree with an independent model in 2,592
cases each, including null actors, signed count/index boundaries, halfword
values, branch outcomes and a helper mutation. Another 252 cases overlap the
record float with actor or global storage, and 72 have the helper mutate the
record pointer and/or scale before the updater reads them. Public access
traces agree in those cases. A three-instruction original caller window passed
48 cases. The retail and guarded streams agree at 74 modeled access-fault
prefixes. Fourteen exceptional floating inputs were screened using an explicit
FCSR conversion model, not a claim about complete target hardware behavior.

The actual C passed 2,592 native 32-bit cases in each of six O0/O2/O3 and
strict/no-strict-aliasing configurations with trapping UBSan. These native
cases use values whose float-to-unsigned conversion is representable. Three
altered source controls were rejected in both aliasing configurations. The
guest and native checks are bounded; they do not establish complete caller,
FCSR hardware, renderer or gameplay behavior.

The actual production Make rebuild is byte-identical to the independently
predicted shadow ELF. Its strict image audit accounts for all 271 changed bytes
with zero exclusions; all 6,051 function addresses and 189,088 protected Game
data bytes remain fixed. Only `generated_13D350.c.o` changed among the 698
frozen linked objects. All earlier guard rows and the conversion CSV remain
unchanged; 33 guard rows were appended. A scoped, fail-closed Graphify refresh
retained all 60,111 existing node IDs and was not a full-corpus re-extraction.

Tools commit `f3d5258` retains the fingerprinted pre-install screen and
installed regression tests. The pre-install screen is bound to its original
inputs and is not a test of the installed checkout. For the installed checkout:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_actor_associated_1511473c_installed -v
```

Both installed tests passed in the mounted tools checkout and an isolated
sibling overlay, with no skips; `make tools-check` passed. The sibling tools
checkout's prior dirty paths were preserved.

Fresh production recount: Game **3,789 / 4,843 (78.24%)**, total
**4,462 / 5,516 (80.89%)**, zero drift. **86** more Game matches are needed
for 80% at the current denominator.
