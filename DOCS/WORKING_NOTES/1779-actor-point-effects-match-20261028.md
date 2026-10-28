# Actor point effects - direct C match

Verified 2026-10-28. Restore `func_15138BC0`, owned by `game_161520`:
VA 0x15138BC0..0x15138C80, ROM 0x166070..0x166130, 48 words / 192 bytes.
The normal O2/g3 compiler emits every original word and all six J26 bindings.
The frame is 96 bytes; S0, S1 and RA retain their retail lifetimes. No guards.

## Recovered behavior and interface

`void func_15138BC0(struct102 *actor, u8 group, s32 context)`

Select the actor's effect type through `func_15134070`. Type 99 returns
immediately. Otherwise, query a point through `func_151380B4`, retain the
low byte of its result, and always run `func_15138120(actor, type, 1)`.
If the saved byte is nonzero, build the 36-byte surface description through
`func_1504715C`, then submit `func_151382E0` and `func_15138424` with
the point, surface, group and context. The second submission also takes actor.
The wrapper ignores all helper results except the selector and point query.

The 12-byte point and 36-byte surface have typed local storage. Relative to
incoming SP, point is -16, availability is -17 and surface is -56. Group and
context retain incoming homes at +4/+8. Retail reloads the group byte and
context after the first point effect; deliberate guest home mutations verify
those emitted loads. Helpers can also mutate the escaped point and surface.
Native checks cover valid object mutations, not private stack aliases.

## Isolated translation unit and owner preservation

Implementation: `conker/src/game/translation_units/161520_actor_point_effects.c`.
The original owner keeps a forward declaration and a comment locating it.
The Makefile uses the existing `pad_c_object.py --function-object` mechanism
to place the independently compiled function into its original slot.

The original owner's unprototyped helper calls produced 49 words and frame104.
Typed helper interfaces and the local order type / position / available /
surface recover all 48 words and frame96. Adding narrow typed definitions to
the main owner changed an unrecovered neighbor; function-pointer casts produced
52 words. Those experiments are rejected. A separate translation unit gives
this routine accurate interfaces while preserving the other 64 compiled bodies,
relocations, GLOBAL_ASM payloads and pools.

The six-command Make recipe reproduces the qualified object exactly. The new
unit has no compiler diagnostics. The owner retains its two existing Warning712
pointer/integer diagnostics; the full build also retains its known duplicate
`generated_12D630` recipe warning. Neither is introduced by this conversion.

| Call offset | Binding |
| --- | --- |
| +0x1C | func_15134070 |
| +0x38 | func_151380B4 |
| +0x4C | func_15138120 |
| +0x64 | func_1504715C |
| +0x80 | func_151382E0 |
| +0xA4 | func_15138424 |

Raw C/original-object body SHA-256:
`8efc0e2faf71469d4b0bbb0ddcb3d5e2c0637f7ce508305676fe9a2fa64ef36d`.
Linked retail slot SHA-256:
`6ffe7b23057f93cec1e949c26947798594c578436adcc6f5e265bc85cb70f088`.

## Caller and helper evidence

The complete ROM census finds one call, at VA0x15194A8C / ROM0x1C1F3C,
and no target-address literals. Caller `func_15194A68` is 19 words at
VA0x15194A68 / ROM0x1C1F18. Its current ELF bytes equal retail. All 19 words
execute in 160 cases, including entry, setup call, target(actor,255,1), final
three-argument submission and return. Caller source and object are unchanged.

Original helper checks cover the selector's 256 actor bytes / all63 words,
the retained point query's 96 cases / 26 of27 words, and the surface builder's
36 cases / 88 of89 words. The query and surface each contain one unreachable
copy of a load; their full original windows are still retained and compared.
The surface checks preserve both padding gaps, nine signed coordinate fields,
metadata, state, flags and entity-table offset.

Only the query is currently byte-exact C. The selector and surface runs use
original ROM instructions; their current implementations remain outside this
match's credit. The large base/point effect helpers and caller setup/finalizer
are bounded providers. This is not full gameplay, hardware or provider recovery.

## Qualification and production audit

Both tools copies pass eight fresh canonical methods and shared tool checks.
Each then passes two fresh installed checks, reusing six unchanged semantic
checks only under exact source, fixture, module and artifact fingerprints.

- 928 guest cases cover all48 target words, every group byte, low-byte query
  results, escaped-object mutations and literal incoming-home reloads.
- 544 fired fault-prefix pairs compare complete registers, memory, calls,
  trace, PC and branch-delay state. These are emitted-instruction checks.
- Native32 O0/O2/O3 each pass 98,304 cases with trapping UBSan and the actual
  three-argument void function pointer. Seven effective negative controls fail.
- Three independent GNU layouts pass 42 guest cases using original, compiled
  and actual Make objects. Three raw/binding corruptions and a missing override
  fail their guards. Five actually compiled IDO semantic mutations fail.
- Six strict image corruptions are rejected; no bytes or sections are excluded.

The input seal covers 16,350 existing paths and 362 focused frozen inputs, with
the new translation unit separately fingerprinted. The independent prediction
accounts for exactly155 changed ELF bytes:154 code bytes plus one symbol-size
byte (12 ->192). All6,056 function addresses, the other6,055 bodies and720
protected Game-data owners /189,088 bytes stay fixed. The progress CSV, shared
headers, callers, other objects and complete guard manifest remain unchanged.

## Bank and measured progress

Predecessor consumer: `d9b36f5eafebcc74d1c8148740dc9525995b679a`.
Tools committed first: `3e7be03e56eb0527c5e9d736a686ad8a9943a20e`.
Preserve all1,778 inherited dirty paths in the older standalone tools mirror;
only the three new qualification modules are added there. No push performed.
Routine Claude budget/calls:0. Graph refresh is scoped AST work with old-node
and source-validated relationship retention; it does not claim a full-corpus
re-extraction or new global clustering.

Adopted ELF SHA-256:
`16d504990da019ce31d571869191ff7813556c3d04b638d487ed91a712eb0737`.
Unchanged guard manifest SHA-256:
`4d5db7992914b7209e0976f4569be48fd6b3b36a850fc0b35140fc097209b840`.
Raw receipts: `conker/build/game-actor-point-effects-match/`.

| Section | Byte-exact C | Different | Address drift |
| --- | ---: | ---: | ---: |
| Total | 3,857 / 5,506 (70.05%) | 1,649 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,184 / 4,833 (65.88%) | 1,649 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The live ELF recount leaves273 more exact C functions to reach4,130 /75%.
Next inspect the49-word `func_150F55C8` in `generated_1228D0`; this queue
entry is only a screen. `func_1514E920` remains parked and uncredited.
