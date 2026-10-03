# Context Forwarding: Explicit C Interface Recovery

Date: 2026-10-03. Baseline: `dd0e154`.

Follow-up: [Note 790](790-game-actor-dimension-helper-semantic-recovery-20261003.md)
recovers the then-pending empty dimension helper. Matching, preparation stack
provenance, and whole-chain acceptance remain separate/open.

## Result

`func_1510F800` now explicitly takes `s32 context` and forwards it to the
retained `func_150A49F4(s32 context)` setter. Its original eight-word / 32-byte
wrapper remains byte-exact directly from C. No guards, compiler profiles,
assembly substitutions, validation, or argument normalization were added.

The previous C body already called the setter, but declared neither wrapper
input nor setter input and passed no C argument. Its guest instructions happened
to retain `$a0` through the prologue. Matching bytes did not make the context
forwarding explicit at the source level. This change recovers that interface
without misreporting an empty-body recovery or a new byte-exact row.

The declaration is local to `generated_13BB20.c`; shared headers and existing
implicit context-wrapper declarations in other slices are unchanged. This
avoids repeating the unrelated register-allocation change caught in Note 785.

## Retail Contract

The complete wrapper at `conker/asm/13BB20.s:1243` allocates a `0x18` frame,
saves `$ra`, calls the setter with `$a0` unchanged and a nop delay slot, restores
the frame/return address, and returns with a nop delay slot. No meaningful return
value is recovered or consumed by the C wrapper.

The retained setter uses the context index to select five table entries for
`D_800DBE3C`, `D_800DBE40`, `D_800DBE44`, `D_800DBE48`, and `D_800DBE4C`,
then publishes the index to `D_800DBE50` in its return delay slot. It remains
assembly and includes an interior entry after that return in the inventory
interval; this task does not rewrite or qualify that interior interface.

## Verification

| Item | Verified result |
| --- | --- |
| Wrapper interval | `0x1510F800..0x1510F820` |
| ROM interval | `0x13CCB0..0x13CCD0` |
| Words / bytes | 8 / 32, all exact, no guards |
| SHA-256 | `a67c1f8cccfb7b7488718eda712a7980b8a3d5201f94abc858af8b41421d79ab` |
| Following symbol | `func_1510F820 = 0x1510F820`, unchanged |

Fifteen tests in `tools/tests/test_game_context_forwarding_wrapper.py` extract
the actual wrapper. Fourteen reuse the dispatcher event-trace cases while
replacing its context-switch mock with the actual wrapper and an instrumented
setter. They cover context bounds/order, flags, eligibility, saved-byte timing,
mutation, accumulation, and actor publication through the recovered forwarding
path. One isolated test checks all 32 argument bits and exactly one setter call.

The isolated passthrough test includes negative/large inputs only against a mock
setter. It proves absence of invented wrapper validation, not that those inputs
are valid for the real setter's table indexing. The integrated tests cover the
dispatcher's contexts 0 through 3. No actual setter execution or gameplay is
qualified by these host tests; preparation/dispatch helpers remain instrumented.

All 431 repository tool tests pass, as do full build/matcher, project checks,
and whitespace checks. Twenty-six previous exact slots remain identical,
including the three neighboring argument wrappers and the vertex transform.
Nine previous non-matching hashes are unchanged. The restored collector,
producer, and return closure remain exact. Both complete Init sections match
retail with the lengths/hashes in Note 782.

The function loader did not expose the setter under `func_150A49F4`, so a direct
ELF section extraction independently verifies its full retained 256-byte interval
`0x150A49F4..0x150A4AF4` / ROM `0xD1EA4..0xD1FA4`. All bytes match; SHA-256:
`1c2a7a194a42a18060d44fa4620a1f7f319137f6bfd0fc0c28d2d8233c306dd4`.
An absent loader key is not evidence of absent code or permission to replace
this retained assembly.

## Progress And Next

Aggregate counts and README tables are unchanged: 5,462 / 6,042 C rows;
3,269 / 5,462 exact (59.85%); Game 2,596 / 4,789 exact (54.21%);
zero drift and 2,193 different C rows. The wrapper was already counted as
byte-exact C before its interface was repaired. Detailed progress stays in DOCS.

Next recover the full dimension helper `func_1507C3E0` in `generated_A9260.c`,
using the original class/subtype branches and signed-halfword publication.
Its current body remains empty. Context-dispatcher and earlier matrix/query
matching also remain open; actor preparation still retains the special-type
stale-stack index boundary from Note 784. The explicit forwarding change does
not establish whole-chain acceptance or resolve those separate contracts.

No compressed-ROM build, guest execution, host-port build, or gameplay test
was performed. The sibling port and frozen Release artifacts were untouched.
