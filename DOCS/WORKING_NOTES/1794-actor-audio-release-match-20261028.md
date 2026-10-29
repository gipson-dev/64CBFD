# 1794 - Actor audio release matched directly from C

Date: 2026-10-28

`func_150E3514` in `conker/src/game/generated_1104D0.c` is now a recovered
`void func_150E3514(u8 *actor)`, replacing its zero-return placeholder. All
50 instructions (200 bytes) emit directly from the normal IDO `-O2 -g3`
profile. No guards, omissions, shared-header edits or profile changes were
needed. The tools qualification is committed as `b5f11e0` before the consumer.
No push was performed.

## Behavior and ABI

The function reads the unsigned byte at `actor + 0x48`, clears that
`D_800D99D0` entry only when it contains this actor, and then reads the live
unsigned sound handle at `actor + 0x4A`. With a nonzero handle it calls
`func_100111C8`, clears the handle after that callback, and reads three live
floats at offsets `0x28`, `0x2C`, and `0x30`. It truncates those coordinates
and submits sound `0x2D7` with volume `0x5DC0`, three zero arguments, and final
parameters 1000 and 6000 to `func_10010F88`. Finally it always calls
`func_1516972C` with the actor. Return values are unused.

The original redundant nonnegative check after an unsigned byte load is
preserved. Its taken negative branch is impossible for that load; all 50
instruction addresses are nevertheless covered across valid paths. Guest
tests exercise all 256 byte indices, including header/table overlaps.
Portable native tests restrict indices to the declared eight-element array
and use real typed objects with asserted offsets and 32-bit pointers.

The ten-argument audio prototype is recovered as
`u16 func_10010F88(s32, u16, s16, u8, s32, s16, s16, s16, s16, s16)`.
IDO places the full truncated 32-bit coordinate values in outgoing homes;
the original 29-word wrapper reads their signed low halves. Tests preserve
that distinction and verify the wrapper's actual eleven-argument downstream
call. Native conversion tests use finite floats in signed-32-bit range and
assert the host's signed-16-bit representation. They do not claim portable
behavior for invalid float conversions, out-of-array indices or guest aliases.

## Qualification

| Check | Result |
| --- | --- |
| Target | VA `0x150E3514..0x150E35DC`, ROM `0x1109C4..0x110A8C` |
| Body / slot / stack frame | 50 / 50 words, 56 bytes; saved `s0` and `ra` |
| Relocations | One HI16/LO16 table pair and three JAL bindings |
| Complete owner | 13 compact functions, 12 neighbors and all pools unchanged |
| Actual Make | Three commands reproduce the independently qualified padded object |
| Direct guest cases | 3,016; original, actual Make and raw C have equal state and traces |
| Connected helper cases | 1,152; all 86 words of stop/audio/release helpers covered |
| Original caller cases | 1,440 across five windows, all 38 window words covered |
| Native32 | 2,560 cases per `-O0`, `-O2`, `-O3`; trapping UBSan, 12 effective controls |
| IDO negative controls | 13 compiled, terminating semantic counterexamples |
| Access fault prefixes | 87 direct + 246 connected, including 25 delay-slot cuts |
| GNU relocation layouts | Three layouts, 144 executions, 55 body/binding rejections |
| Tools copies | Eight fresh methods and tools checks per copy; two fresh installed methods and six strictly fingerprinted semantic reuses per copy |
| Whole-image difference | 143 bytes: 142 code bytes plus one target symbol-size byte; zero exclusions |
| Protected Game data | All 189,088 bytes across 720 owners unchanged |
| Linked inventory | 6,056 canonical functions; all 6,055 other bodies and every address unchanged |
| Compiler diagnostics | Zero new owner warnings; inherited duplicate `generated_12D630` Make warning unchanged |

The ROM census has five direct calls and no aligned function-pointer uses.
They occur in `func_150E35DC` at VA `0x150E365C`, and in `func_150E3738` at
`0x150E37A4`, `0x150E37E4`, `0x150E392C`, and `0x150E3944`. Both parent C
bodies remain placeholders. The bounded windows verify selector filtering,
the signed timer and `-99` sentinel, null-record handling, and the timer
store in a branch delay slot. They do not establish complete parent behavior
or gameplay acceptance.

Original helpers are `func_100111C8` (29 words), `func_10010F88` (29), and
`func_1516972C` (28). Stop-table matching, low-half audio arguments, actor
reload after unlink, live type changes, and destructor selection are executed.
Deeper voice-stop/audio/unlink/fallback/destructor services remain bounded
hooks, including deliberate volatile-register, float-register and argument-home
clobbers. No new matching credit is attributed to those existing helpers.

## Measured checkpoint and continuation

| Section | Byte-exact C | Address drift | Still different |
| --- | --- | --- | --- |
| Total | 3,872 / 5,506 (70.32%) | 0 | 1,634 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,199 / 4,833 (66.19%) | 0 | 1,634 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The C inventory and inherited guard CSV remain byte-for-byte unchanged.
The active 75% goal needs 258 more matches to reach 4,130 / 5,506. Remaining
queue shapes are 1,505 placeholders, 120 semantic/other and nine unlocated.
Inspect `func_150969A0` next; it is only a queue candidate, without matching
credit. `func_1514E920` remains parked and uncredited.

The root README changes only its two aggregate matching rows. Detailed
progress belongs in this note and the DOCS indexes. A scoped eleven-file AST
graph refresh follows the consumer commit; historical nodes, relationships
and manifest rows must be audited before adopting it. This is not a full
corpus extraction or a recomputation of global communities or centrality.

Local evidence: `conker/build/game-actor-audio-release-match/`. The production
ELF SHA-256 is
`4e77e8f4ddfca730ae321924c88911828951417803b06e3a0fe860c172fc3f39`.
The padded object SHA-256 is
`5388fa67f392994941edaa7af49628c4cde5f021638d1b2e259191dd82fd658f`.
The guarded manifest remains
`efd6bd3f1e7efba51b4b566abfd447477133a8a52daa3804bc7550b32d273293`.
Preserve the independently dirty older tools mirror: 1,823 inherited paths
plus the three new qualification modules; no mirror commit or reset.
