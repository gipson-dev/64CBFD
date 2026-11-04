# Game packed-layout record allocator guarded match (2026-11-04)

## Outcome

`func_15195984` now replaces its zero-return placeholder in
`conker/src/game/generated_1C2C60.c` with the complete packed-layout record
allocator. The typed semantic C and 46 fail-closed expected-word replacement
rows match all 64 retail words and the original 24-byte frame. All five
relocations emit naturally from the source; none of the guard rows inserts or
omits a word or carries relocation metadata. No assembly body, source-level
compiler override, or address drift is needed.

The natural owner-profile body is already 64 words/frame24 and differs at 46
positions. A no-loop-unroll control emits 63 words/frame24 and differs at 48
positions, so the normal owner profile was retained: it preserves the retail
extent and keeps the qualification to checked replacement rows without adding
a Makefile exception.

This is source, ABI/callers, compact/padded owner, guest/native execution,
strict whole-image, protected-data, production-build, recount, and
graph-retention evidence. It is not caller gameplay, allocation-pressure,
rendering, save, hardware, or PC-port runtime acceptance.

## Recovered behavior and ABI

The function accepts a key, two packed 12-bit coordinate pairs, and a flag
that optionally doubles the first pair. It allocates a 0x3C-byte record through
`func_151957B0` and the original `D_800E08E8`/`D_800E08EC` list state. An
allocation failure returns null without touching a record.

On success it clears the link at `+0x18`, initializes both five-entry signed
16-bit index groups at `+0x1C..+0x2E` to `-1`, stores the low 16 bits of the key
at `+0x08`, and unpacks the size pair from bits 12..23 and 0..11. Each size
component receives the retail `+2` border and is doubled only when the fourth
argument is nonzero. The second packed pair is unpacked in the same order,
scaled by eight, and stored at `+0x0E/+0x10`; the size pair is stored at
`+0x0A/+0x0C`. The active byte at `+0x14` is set to one and the new record is
returned.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x15195984..0x15195A84` |
| Retail ROM range | `0x1C2E34..0x1C2F34` |
| Owner | `generated_1C2C60`, 68 neighboring functions |
| Body / retail slot | 64 / 64 words |
| Frame | 24 bytes |
| Bindings | `func_151957B0`; HI16/LO16 pairs for `D_800E08E8` and `D_800E08EC` |
| Direct callers | `func_15195AA8` at ROM `0x1C3038`; `func_15195DD4` at ROM `0x1C3394` |
| Natural compact normalized SHA-256 | `a79590c6d920e9375a20e45562ff18a99f1603a2c45b2a665f14d4c9806f8bf2` |
| Linked retail body SHA-256 | `0bd6770d9f681f6353cd70092ff12e76dfb1b2595eaa0b4892202aa04dc340a5` |

## Source provenance and compiler shape

The adjacent `Another Source/CBFD-Recompiled` checkout contains a decompiler
body for this function and its callers. It was used only as provenance and a
cross-check: its stale field types and two-argument allocator declaration do
not describe the retail ABI. The installed source was derived independently
from retail assembly, the five relocation bindings, both direct callers, and
the surrounding list-management helpers.

The recovered structure gives names and widths only to the fields this
routine owns and retains the untouched bytes explicitly. The repeated primary
loop and original secondary-store order preserve the retail memory contract.
The 46 checked rows close only IDO register allocation and scheduling
differences; every row verifies its compiler preimage before it can apply.

## Qualification

The permanent four-test focused suite establishes:

- 1,024 guest cases cover 512 packed-value combinations across two stack
  phases, successful allocation, 32 allocation-failure cases, optional size
  doubling, callback-clobbered caller-saved state, and every one of the 64
  retail words;
- actual 32-bit native O0, O2, and O3 each pass 4,096 cases, for 12,288
  positive executions, while nine independently compiled semantic controls
  fail;
- both direct JAL sites and their `func_15195AA8`/`func_15195DD4` ABI windows
  are retained, with no aligned pointer literals; and
- 124 exercised fault observations cover 30 unique active root-memory access
  boundaries without weakening the instruction or branch-delay contract.

All five relocations and 68 owner neighbors are fixed. The strict
6,052-function image changes only `func_15195984`, preserves every function
address with zero exclusions, and leaves all 189,088 protected Game-data
bytes across 720 owners exact.

The installed focused suite passes all four tests in 34.641 seconds. The
shared match-progress, generated-PC16, guarded-object, and protected-data suite
passes all 19 tests in 6.417 seconds.

## Production closure

The actual Make owner rule rebuilt `generated_1C2C60`, and the production
owner and ELF equal the independently predicted qualified artifacts. The broad
`make all` path rebuilt the binary and stopped only at the expected final
retail SHA check. The inherited duplicate `generated_12D630` recipe warning is
unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `31c31271a31c9ab790d9a27df4d70cfe57b009d1aa36082d68f31c42a663e2a7` |
| Qualified / production linked ELF | `b37ca1afa73738d09e6d1a1b9bb4f5ae316cdca2816ca60033599b18c64ca14a` |
| Production rebuilt ROM image | `13eba15796bbbc5c9d79b5c9111a6bc6f32d1a0d45e7c544a8a279de5f7fc4fc` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Installed owner source | `408a014b0b3362c0f11ec0e3c7ab5d92b79ff168a364e64f3dee5a33b570cd85` |
| Guard table | `99130129241508bed87c084c23d06f08cd6c63da2ab09bf125a6b8d8e72ce018` |
| Retail layout | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |

## Recount

The fresh production ELF reports:

- Total: **4,147 / 5,512 (75.24%)**, zero address drift, 1,365 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,474 / 4,839 (71.79%)**, zero drift, 1,365 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **263 more** are needed.

## Continuation

The fresh production rerank selects ordinary Game candidate `func_1519E464`,
whose 67-word slot has 63 real differences. Keep the seven documented
handwritten/custom-ABI/boundary rows (`func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`) separate until their specific boundaries are addressed.
Every ordinary candidate still requires source/ABI/caller, owner,
guest/native, actual Make, complete-image, protected-data, production recount,
documentation, and graph-retention gates before credit.

## Graph retention

The retained graph baseline is 58,511 nodes / 112,364 links with SHA-256
`3c7df2b10522339f2cea62d2d0e2ce5e012e489b644979981f583ad0bcc0dc1f`.
The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,720 nodes, so Graphify correctly refused to overwrite the
retained corpus. Its fail-closed report retained 31,816 nodes from 3,754
still-present files outside that reduced scan. The graph remained
byte-identical at the baseline hash.

An explicit eleven-path incremental rebuild with `force=False` then produced
58,522 nodes, 112,374 links, and 5,073 communities. Against the saved
pre-change graph, 58,508 / 58,511 old node IDs were retained, including every
ID outside the changed-path set. The three replaced IDs are line-derived
`DOCS/UPDATE_LOG.md` headings, each with its corresponding replacement two
lines later. Fourteen IDs were added: those three relocated headings; the
Note 2076 file, title, and eight indexed section headings; and the retained
`PackedLayoutRecord15195984` type. The eleven-node and ten-link net additions
are confined to the owned changes. This qualified graph has SHA-256
`147762780640aff4a9b31483038c35ecc8fa47297985201a8ede88de166fcca3`.

After adding this receipt, a one-path stabilization retained every node ID and
found no code-graph topology change.
