# Game actor-position effect factory direct match (2026-11-04)

## Outcome

`func_151B6320` now replaces its zero-return placeholder in
`conker/src/game/generated_1E37D0.c` with the complete actor-position effect
factory. The typed semantic C emits all 64 retail words, the original
144-byte frame, and both call relocations directly. No expected-word guard,
inserted or omitted word, assembly body, function-specific compiler profile,
or address drift is needed.

This is source, ABI/caller, compact/padded owner, guest/native execution,
strict whole-image, protected-data, production-build, recount, and graph
evidence. It is not gameplay, visual-effects, rendering, save, hardware, or
PC-port runtime acceptance.

## Recovered behavior and ABI

The function accepts an actor pointer, an unsigned-byte channel, and a signed
context. It snapshots the actor's three coordinates and identity byte into a
request and a 0x2C-byte payload. The request uses duration 300, flags 6, kind
13, and count 10. It then calls `func_15147A80` with a 0x30-byte allocation,
0x1C-byte entry size, three active values of 11, zero resource/value fields,
no optional object, and the supplied channel/context. A null result ends the
function; otherwise `memcpy` copies the complete payload to the pointer at
the created record's `+0x98` field.

The original routine intentionally leaves request bytes `0x14` and
`0x16..0x17`, payload bytes `0x05..0x07`, and payload word `0x28` untouched.
Those bytes retain their incoming stack contents and are copied by the retail
helper/payload transfer. The named reserved fields and the enclosing local's
layout gap/tail document that behavior without clearing or inventing state.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x151B6320..0x151B6420` |
| Retail ROM range | `0x1E37D0..0x1E38D0` |
| Owner | `generated_1E37D0`, 16 neighboring functions |
| Body / retail slot | 64 / 64 words |
| Natural / retail frame | 144 / 144 bytes |
| Natural bindings | `func_15147A80` at `+0xD0`; `memcpy` at `+0xE4` |
| Direct caller | `func_1506AA08`; JAL at ROM `0x97EE0`; return ignored |
| Raw natural object SHA-256 | `fb4fc0ac22b7031bca52f48601446d2d3dd62faeb421c1225b1db5cfc047a06f` |
| Linked natural / retail body SHA-256 | `c4525273cad4a8e76fcf60658e3f63eb946d81e5f29209f02808026926d2532c` |

## Source provenance and compiler shape

The semantic fields were recovered from the retail body, the two call
relocations, the allocator's established interface, the sole direct caller,
and the created-record payload consumer. The raw pseudocode in the adjacent
`Another Source/CBFD-Recompiled` checkout was inspected as provenance only;
none of its anonymous stack-local declarations was copied into the installed
source. The final source uses purpose-specific position, request, payload, and
local-layout names and was accepted only after its owner-profile object
matched the retail slot independently.

The exact source order initializes X, Y, and Z before the scalar request
fields. With the original local spacing represented explicitly, IDO 5.3's
normal `-O2 -g3` profile reproduces the retail 0x90-byte frame and every
instruction naturally. Reversing the two equal bound assignments preserves
their retail store schedule. The unsigned-byte channel type is required for
the retail argument-home reload.

## Qualification

The permanent four-test focused suite establishes:

- 128 direct guest cases per body, across retail and natural C, cover all 64
  words and distinguish allocation failure/success, actor mutation after the
  snapshot, four channel patterns, four signed-context patterns, both stack
  phases, raw floating-point bit patterns, and the preserved request/payload
  stack bytes;
- actual 32-bit native O0, O2, and O3 each pass 4,096 cases, for 12,288
  positive executions, while twelve independently compiled controls alter a
  coordinate source, duration, flags, owner, identity, zero sign, bound,
  kind, count, helper size, copy size, or destination and all fail;
- the exact 16-word caller is executed in 64 connected cases, passes
  `(actor, 0xFF, 1)`, ignores the return, and survives caller-saved clobbering
  by the preceding helper and this factory's two callees; and
- 158 fault observations cover 42 unique `(PC, delay-of, cut)` active
  root-memory boundaries across retail and natural C.

Both relocations and all 16 owner neighbors are fixed. The strict
6,052-function image changes only `func_151B6320`, preserves every function
address with zero exclusions, and leaves all 189,088 protected Game-data
bytes across 720 owners exact. The installed focused suite passes all four
tests in 74.559 seconds. The shared match-progress, generated-PC16,
guarded-object, and protected-data suite passes all 19 tests in 7.415 seconds.

## Production closure

The actual Make owner rule rebuilt `generated_1E37D0`, and the production
owner and ELF equal the independently predicted qualified artifacts. The
broad `make all` path rebuilt the binary and stopped only at the expected
final retail SHA check. The inherited duplicate `generated_12D630` recipe
warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `f183aa7c5087cadd710f9b613a8e79c2afd6a9ccdf4d78c3a7f25cc7eea26d1e` |
| Qualified / production linked ELF | `b98b26ea27151b36f3e225f680ebe168442f44c005d4923341a08c0f1cbee7b2` |
| Production rebuilt ROM image | `0d2cef680b48402e43b5cd377db4bab1357fb7d0217662f791f0e98db9f7b435` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Installed owner source | `bf29ad8f0d32462c379a422ca566da0215c92f07fd35d5099eeb8b1484821b23` |
| Guard table, unchanged | `8516b4ea5fc16f8ad49f0108159cb5e4f7e5424d27cc38b758d1d45f76671c89` |
| Retail layout, unchanged | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |

## Recount

The fresh production ELF reports:

- Total: **4,149 / 5,512 (75.27%)**, zero address drift, 1,363 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,476 / 4,839 (71.83%)**, zero drift, 1,363 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **261 more** are needed.

## Continuation

The refreshed ordinary queue continues at `func_151C86AC` (64 words, 63 real
differences), followed by the 64-difference tier beginning with
`func_150C2700`. Keep the seven documented handwritten/custom-ABI/boundary
rows (`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC`, and `func_150A6760`) separate until their
specific boundaries are addressed. Every ordinary candidate still requires
source/ABI/caller, owner, guest/native, actual Make, complete-image,
protected-data, production recount, documentation, and graph-retention gates
before credit.

## Graph retention

The retained graph baseline was 58,533 nodes / 112,384 links with SHA-256
`ac748da69023b88aec78a632d87062eb0318344a81d07414345fbaee728d1a94`.
The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,740 nodes, so Graphify correctly refused to overwrite the
retained corpus. Its fail-closed report retained 31,816 nodes from 3,754
still-present files outside that reduced scan. The graph remained
byte-identical at the baseline hash.

An explicit ten-path incremental rebuild with `force=False` then produced
58,542 nodes, 112,389 links, and 5,069 communities. Against the saved
pre-change graph, 58,530 / 58,533 old node IDs were retained, including every
ID outside the changed-path set. The three replaced IDs are line-derived
`DOCS/UPDATE_LOG.md` headings, each with its corresponding replacement two
lines later. Twelve IDs were added: those three relocated headings and the
Note 2078 file, title, and seven indexed section headings. The nine-node and
five-link net additions are confined to the owned changes. This qualified
graph has SHA-256
`297bc21e04c3007f429a0fd6e653186ae7a3dcb99070c9b11963540e6f9d6adb`.

After adding this receipt, a one-path stabilization retained all 58,542
existing node IDs and added only the new `Graph retention` heading. The final
graph has 58,543 nodes, 112,390 links, 5,090 communities, and SHA-256
`8e9f65e87fac857b43db4cbffd8af512395786e6212ebf63a75efc19a4a20579`.
