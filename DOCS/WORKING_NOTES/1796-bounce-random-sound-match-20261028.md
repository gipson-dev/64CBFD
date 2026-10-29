# 1796 - Bounce callback with randomized positional sound matched from C

Date: 2026-10-28

`func_15133C58` in `conker/src/game/generated_15F680.c` now implements its
original six-argument callback. It passes the actor, three float coordinates,
height and contact pointer to `func_15133B98`. When the next random word has
its low bit set, a second independent draw selects one of nine sound IDs
starting at `0x2DE`. The positional sound uses volume `0x2EE0`, truncated
coordinates and the original final arguments 500 and 1000. The callback
always returns one; it does not propagate either provider's return value.

The recovered signature is
`s32 func_15133C58(u8 *actor, f32 x, f32 y, f32 z, f32 height, void *contact)`.
The last argument is a pointer to the actor's `+0x114` contact storage in
both observed callers. Its internal type is deliberately left opaque.
Existing function names are preserved, and the source comment describes the
bounce and positional sound behavior.

All 50 words emit directly from the normal IDO `-O2 -g3` profile, including
the 0x30-byte frame, coordinate homes, branch-likely return update, unsigned
remainder, and audio-call delay-slot store. Four `R_MIPS_26` bindings cover
the bounce call, two random calls, and audio call. No guards, shared-header
changes or compiler-profile changes are needed.

## Qualification

| Check | Result |
| --- | --- |
| Target | VA `0x15133C58..0x15133D20`, ROM `0x161108..0x1611D0` |
| Body / slot / frame | 50 / 50 words, 48-byte frame |
| Complete owner | 31 functions; all 30 neighbors, retained assembly and pools unchanged |
| Actual Make | Five commands, including GLOBAL_ASM preprocessing and postprocessing, reproduce the qualified padded object |
| Direct guest execution | 1,726 cases; all 50 instructions, all nine sounds, both gates, unsigned random values and live coordinate homes |
| Connected original helpers | 960 cases; all words of the 48-word bounce, 18-word RNG and 29-word audio wrapper |
| Original indirect callers | 240 cases across two bounded dispatch windows, including the first route's zero-index gate |
| Native32 | 845 cases per `-O0`, `-O2`, `-O3`, 12 effective controls, actual SDK types and trapping UBSan |
| IDO negative controls | 12 compiled semantic counterexamples, each terminating without incidental faults |
| Access fault prefixes | 139 direct/connected + 147 caller prefixes; seven direct/connected delay-slot cuts |
| GNU layouts | Three independent layouts, 300 executions, 54 raw-body/binding corruption rejections |
| Tools copies | Eight fresh methods and tools checks in each; two fresh installed methods and six strictly fingerprinted semantic reuses |
| Strict whole image | 146 changed bytes: 145 target code bytes and one symbol-size byte; zero exclusions |
| Protected Game data | All 189,088 bytes across 720 owners preserved |
| Linked inventory | All 6,055 other bodies and all 6,056 canonical addresses preserved |
| Diagnostics | No new diagnostics; two pre-existing pointer/integer warnings in `func_151325C8` and the inherited duplicate Make rule warning remain |

The ROM census finds no direct JAL to this callback and exactly one aligned
pointer at ROM `0x22E424`: index 12 of `D_80089934`. The two dispatch windows
are at `0x15132FDC` (19 words) and `0x1513397C` (17 words). The first belongs
to `func_15132DDC`, passes the actor's height/contact fields and branches on
the callback result. The second belongs to retained-assembly `func_15133894`
and stores/reloads the returned byte. The parent routines are not converted
or credited by this change; these are bounded original instruction routes,
not a claim of complete parent or gameplay execution.

The retained bounce helper scales the actor's motion, reverses its vertical
component, sets its height, and clears motion/flags when the resulting
vertical speed is below four. The connected tests execute that actual
assembly. They also execute the original 64-bit RNG state update and audio
wrapper's signed-halfword argument handling. The low-level audio provider
is bounded; no audible/runtime acceptance is claimed.

Native float-to-integer cases are finite and within the signed-32-bit range.
Narrowing to the audio wrapper's signed 16-bit coordinate arguments is
checked on the prepared 32-bit ABI. Tests that deliberately alter incoming
argument homes or stop at access faults are guest instruction-order checks,
not portable C behavior. The first private run exposed missing FPU negate
handling in the test emulator and a native harness signedness warning;
both harness issues were corrected, with the candidate C unchanged.

## Banked progress

Tools commit `3056dec` precedes the consumer commit. The live adopted ELF
recount, with the original C inventory and guard CSV unchanged, is:

| Section | Byte-exact C | Address drift | Still different |
| --- | --- | --- | --- |
| Total | 3,874 / 5,506 (70.36%) | 0 | 1,632 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,201 / 4,833 (66.23%) | 0 | 1,632 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The 75% goal remains active: 256 more matches reach 4,130. Remaining queue
shapes are 1,503 placeholders, 120 semantic/other and nine unlocated.
Inspect `func_151E4314` next; no matching credit until it passes qualification.
`func_1514E920` remains parked and uncredited.

Only two aggregate rows change in the root README. A scoped eleven-file
Graphify AST refresh follows the consumer commit, with old-node and directed
relationship retention audited. Historical communities and centrality are
retained; this is not a full-corpus extraction or global recomputation.

Local evidence: `conker/build/game-bounce-random-sound-match/`. ELF SHA-256:
`3c483bc65c5f3bc93ff9bc603a3ddd6a51929554313b9be90d999d13599072ae`.
Padded object:
`556052a46e0346826c2c1ab32c6fbb7a0ec722f8d9162c9988e8df7060738a53`.
The older tools mirror retains 1,829 inherited dirty paths plus three new
qualification modules, 1,832 total. No mirror commit, reset, push or host-port
change is part of this recovery.
