# Game effect-update callback direct match

Date: 2026-11-14. `func_151A8CEC` replaces the zero-return placeholder in
`conker/src/game/generated_1D4E00.c`. Its 140-word retail slot is
`0x151A8CEC..0x151A8F1C` (ROM `0x1D619C..0x1D63CC`). All words and
relocations emit directly from semantic C with the original 0x78-byte frame.
There are no new guards, inserted instructions or omitted instructions.

The public `void func_151A8CEC(struct260 *owner)` interface follows the
actor dispatcher `func_15149264`. The prepared ROM and unchanged protected
data select it through `D_8008A4E8[0x25]` at address `0x8008A57C`.
The local 88-byte payload view uses the same tagged `HeightResult71820`
definition as the ground-query provider, preserving that helper interface.

The callback performs the optional mode predicate, sets lifetime -1 when
the predicate rejects the actor, honors an optional spatial stop query, and
checks the emission-enable bit. It advances a floating accumulator using
the random sample, request parameters, timestep and scale. While the result
is strictly greater than one, it chooses the attached or free position
provider, resolves the vertical coordinate, dispatches the selected emitter,
and subtracts one. The position provider is selected once before the loop;
flags and emitter selector are read again after the position helper.

The random helper's return is explicitly snapshotted before mutable request
parameters are read. Native helper mutations rejected an earlier expression
whose C evaluation order let GCC read a parameter before that helper. The
explicit snapshot preserves all 140 original words and removes the unused
local word used in the initial fitting experiment. Narrow volatile accesses
retain the original two signed mode-byte reads; this records an emitted
access contract, not evidence that the original source used volatile or
that the byte is hardware memory.

Retail retains the local acceptance byte until a forced-height or fallback
path sets it to one. Guest fixtures seed and compare that byte, including
its carry between iterations. Native cases require it to be initialized
before an emitter observes it, or omit that emitter observation. They do
not establish portable C behavior for an indeterminate automatic byte.

Guest validation compares an independent bounded model with retail, raw C
and padded streams in 864 cases and 2,640 executions, including 16 windows
of the original dispatcher at `0x15149294..0x151492B8`. The window includes
the actual indirect table lookup and call; post-call lifetime/deletion
handling is outside it. Cases cover predicate rejection, spatial stopping,
enable bits, attached/free selection, signed emitter indices, strict loop
thresholds, multiple ticks, helper-visible mutations and retained flags.
All 139 reachable words are exercised. The original duplicate pointer
setup at `0x151A8D60` is unreachable from normal entry and remains present.
All three streams agree in modeled machine state at 164 fired access prefixes.

The predicate table's retail entry `D_8008F980[0]` is NULL. Predicate and
emitter entries in behavioral fixtures are stand-ins for bounded contract
checks, not proof that non-sentinel predicate modes are valid in the retail
configuration. The position, spatial, random, ground and emitter providers
are modeled. Their complete bodies and the complete actor lifecycle are not
executed by this suite. Prior unchanged provider receipts remain separate
from these fresh interface checks. Unrestricted owner/stack aliases,
nonfinite arithmetic, FCSR, hardware and gameplay are not qualified.

Native 32-bit C passes 124 cases in each of six O0/O2/O3 and
strict/no-strict-aliasing configurations with trapping UBSan. All seven
altered source controls are detected. Fixtures use typed, aligned,
disjoint objects, numeric host-order fields and initialized observed flags.
Pointer fields and numeric words are checked separately from unchanged
byte ranges so guest big-endian bytes are not mistaken for native layout.

Both padders pass 12 GNU links over four independent rebases, including
helper targets and global-address carry boundaries. The other 22 owner
functions and normalized pools remain unchanged. The target compile has
no diagnostics. Production Make uses the normal compile/pad/link rules:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The unchanged guard manifest is marked old for this scoped build so the
697 frozen neighboring objects can be reused. The production ELF equals
the independent shadow prediction. All 506 changed bytes are accounted
for, including three closed symbol/string-table ordering cycles, with zero
exclusions. All 6,051 function addresses and 189,088 protected Game-data
bytes remain fixed. Only the target owner changes in the 698-object census;
the conversion manifest, Makefile and complete guard history are unchanged.

Tools commit `95245c2` retains the installed regression suite. It passes in the
mounted checkout and an isolated sibling-tools overlay without changing
its 2,434 preexisting dirty paths. `make tools-check` passes as well:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_effect_update_151a8cec_installed -v
```

A scoped fail-closed Graphify refresh retains all 60,139 previous node IDs
and produces 60,139 nodes; it is not a full-corpus re-extraction. This is a
retail decomp change. The sibling host port needs no source update for this
match, its frozen Release is untouched, and no host runtime result is claimed.

Fresh production recount: Game **3,799 / 4,843 (78.44%)**, total
**4,472 / 5,516 (81.07%)**, zero drift. At the current denominator,
**217** additional exact matches are needed to reach 85% total.
Resume with the remaining effect callbacks in this owner, beginning with
`func_151A87F8`; qualify the full body and interfaces before adoption.
