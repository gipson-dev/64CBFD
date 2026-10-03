# Actor Preparation: Exact Restoration And C-Recovery Boundary

Date: 2026-10-03. Baseline: `474feb3`.

## Result

`func_15044660` no longer returns a fabricated zero from an empty C body.
Its complete original assembly is extracted into the established GLOBAL_ASM
ownership pattern. All 156 words / 624 bytes match retail directly, without
new compiler profiles or word patches. This is assembly restoration, not C
decompilation progress. The recovered interface is
`void func_15044660(void *actor, f32 x, f32 y, f32 z)`.

The routine calls `func_1507C3E0` for three halfword dimensions and publishes
two global float extents. Its ordinary path adjusts the first dimension by
the absolute Y displacement, truncates the result to an integer, and retains
the low signed halfword. Actor class/category/flags select the later extent
formula, including arithmetic-shift halves and type `0x25`'s distinct
divide-toward-zero half. No output formulas were replaced with a generic
radius or clamped to positive values.

## Why Not Ordinary C Yet?

Retail allocates a `0x30` frame. Actor types `0x2C`, `0x2D`, and `0x2E`
take an early branch that publishes the first dimension and zero, then loads
`$a3` from `0x20($sp)` at `0x150446CC`. The routine never initializes this
word. It lies sixteen bytes below the entry stack pointer, not in an explicit
caller argument slot. The ordinary branch instead computes an index from
`(actor - D_800CC2D0) / 0x32C` using signed division.

Later category 5, nonzero byte `actor+0xAD`, and subtype `0x53`/`0x28` paths
finish without consuming that index. Otherwise, the branch at `0x150447FC`
tests it against zero and the signed byte `D_8008FD8C`; actor float `+0x28`
then participates in the half-height choice before subtype `0x25` handling.
Therefore the static body alone does not justify initializing the special
types' index to zero, minus one, or the ordinary array index.

The dimension helper receives addresses `sp+0x2E`, `sp+0x2C`, and `sp+0x2A`,
not the `sp+0x20` word. Its current Game source is itself an empty placeholder
in `generated_A9260.c`; the restored caller does not make that helper or the
whole actor/context cluster functional. Real actor invariants may render the
index-consuming special-type path unreachable, but that remains unproven.
No uninitialized C local or guessed defensive fallback was introduced.

## Linked Evidence

| Item | Verified result |
| --- | --- |
| Guest interval | `0x15044660..0x150448D0` |
| ROM interval | `0x71B10..0x71D80` |
| Complete slot | 624 bytes / 156 words, all exact |
| Following symbol | `func_150448D0 = 0x150448D0`, unchanged |
| SHA-256 | `d5a49547ad263ec4f509c34c0a8eb7a5c415a0bb90a84c7ef5a297c0693d8c6d` |

Three tests in `tools/tests/test_game_actor_preparation_assembly.py` check
the complete slot/hash and source ownership/interface, the retained special
stack read and lack of a routine-local initialization, and independent
assembly/linking at retail addresses. They do not execute guest instructions
or prove dynamic reachability, stack provenance, or helper behavior.

The first build rejected an unnecessary `.include` directive in the extracted
file. Removing it follows the existing GLOBAL_ASM format; the successful
rebuild then regenerates the object, link, inventory, and matcher normally.
No tool behavior was altered to accommodate the source.

## Regression And Counts

The full suite passes all 391 tool tests, including the three new assembly
checks. Full build/matcher, project tool checks, and whitespace checks pass.
This does not establish actor-chain or gameplay acceptance.

The complete restored slot, nineteen earlier exact routines, and both matrix
wrappers are retail-identical. Eight previous non-matching hashes remain
unchanged: both matrix builders, the actor-result builder, four entity queries,
and the terrain query. The 5,712-byte collector, 504-byte producer, and 16-byte
return closure remain exact. Both complete Init sections remain exact with
the lengths/hashes in
[Note 782](782-init-pause-resume-conversion-assessment-20261003.md).

Fresh CSV and matcher results:

| Item | Current measurement |
| --- | --- |
| Total C rows / bytes | 5,462 / 6,042 (90.40%); 1,930,848 / 2,256,728 (85.56%) |
| Game C rows / bytes | 4,789 / 5,321 (90.00%); 1,759,412 / 2,072,880 (84.88%) |
| Assembly rows | 580 total; 532 Game; Init 47 and Debugger 1 unchanged |
| Exact C | 3,268 / 5,462 (59.83%); Game 2,595 / 4,789 (54.19%) |
| Drift / different C | 0 / 2,194 |

The lower C counts accurately remove a false placeholder from the C inventory;
the exact-C numerator does not increase for an assembly restoration. README
contains only updated aggregate tables. Detailed explanations stay in DOCS.

## Next Work

1. Recover `func_15044380`'s true floating-argument/actor/context interface and
   complete descending/optional ascending context passes. Its preparation
   dependency is now exact assembly, while the dimensions helper remains open.
2. Recover `func_1507C3E0` from its full original body before claiming the
   actor-preparation chain is behaviorally usable. Audit each actor class and
   signed-halfword output, not only ordinary actor dimensions.
3. Reopen C recovery of `func_15044660` only with actor-type reachability or
   stack-provenance evidence explaining the stale index. An exact retained
   implementation is the baseline, not permission to invent that value.

No compressed-ROM build, guest execution, host-port build, or gameplay test
was performed. The sibling port and frozen Release artifacts were untouched.
