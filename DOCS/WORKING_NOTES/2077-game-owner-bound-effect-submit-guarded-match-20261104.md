# Game owner-bound effect submit callback guarded match (2026-11-04)

## Outcome

`func_1519E464` now replaces its zero-return placeholder in
`conker/src/game/generated_1CA420.c` with the complete owner-bound effect
submit callback. The typed semantic C and 28 fail-closed expected-word
replacement rows match all 67 retail words and the original 56-byte frame.
All three call relocations emit naturally from the source; none of the guard
rows inserts or omits a word or carries relocation metadata. No assembly body,
source-level compiler override, or address drift is needed.

The natural owner-profile body is already 67 words but uses a 64-byte frame
and differs at 28 positions. Raw-pointer, alternate-width, temporary-order,
result-type, and helper-prototype controls did not improve that closed
compiler allocation/scheduling difference. The typed form was retained because
it preserves the exact retail extent, complete behavior, and every natural
binding while keeping the normalization to checked replacement rows.

This is source, ABI/registry, compact/padded owner, guest/native execution,
strict whole-image, protected-data, production-build, recount, and
graph-retention evidence. It is not caller gameplay, rendering, effect-system
load, save, hardware, or PC-port runtime acceptance.

## Recovered behavior and ABI

The callback accepts one record pointer. Its payload at `+0x28` contains the
owner pointer, the captured owner-identity byte, and the effect preset. An
inactive owner or identity mismatch retires the callback. A still-valid owner
whose matrix pointer at `+0x1D4` is not ready leaves the callback active so a
later invocation can retry.

Once the matrix exists, the callback submits one effect through
`func_1519D030` with the stored preset, duration, low flag bit, slot, and
context, then retires regardless of allocation success. A non-null result is
offered to `func_1514ED3C` with the owner's attachment at `+0x2F4` and the
callback record. Successful attachment links the effect back to the owner
through `func_1514EC1C` in mode `0x10`. Retirement stores duration `-1` and
sets flag bit zero.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x1519E464..0x1519E570` |
| Retail ROM range | `0x1CB914..0x1CBA20` |
| Owner | `generated_1CA420`, 22 neighboring functions |
| Body / retail slot | 67 / 67 words |
| Natural / retail frame | 64 / 56 bytes |
| Bindings | `func_1519D030`, `func_1514ED3C`, `func_1514EC1C` |
| Callback registry | pointer literal at ROM `0x22EFC8`, `D_8008A4E8[8]`; no direct JAL callers |
| Raw natural object SHA-256 | `81123f0cb37ffdf30188869b0788820f00a2f180ac809d2f37b95755bf48b6d4` |
| Linked natural body SHA-256 | `7aba504e11e1bd0307f7e1ba3c82f4a57d53bd19582fd7d54a56cb702fb725a1` |
| Linked retail body SHA-256 | `b6b9d29e64f59a13d8495a4c742338a7ec23986e4249ad02611f871cfab5cf43` |

## Source provenance and compiler shape

The source was recovered from the retail body, its three call relocations,
the callback-table pointer, the record's producer/consumer relationships, and
the attachment/link helpers. The two local structures name and type only the
fields this callback owns; all intervening bytes remain explicit reserved
storage. The helper declarations preserve the owner's existing old-style ABI
surface while the recovered callback itself has a typed `void` signature.

The natural compiler body exactly reproduces the first 22 words and all three
relocations. The 28 checked rows close only the later frame, saved-register,
argument-setup, result-lifetime, and retirement scheduling differences. Each
row verifies its compiler preimage before replacement, so source or compiler
drift fails closed.

## Qualification

The permanent four-test focused suite establishes:

- 64 guest cases cover every one of the 67 retail words and all 67 natural-C
  words, issue 14 helper calls, preserve callback-clobbered caller-saved state,
  and distinguish inactive, identity-mismatch, matrix-retry, failed submit,
  failed attach, and successful link paths;
- actual 32-bit native O0, O2, and O3 each pass 4,096 cases, for 12,288
  positive executions, while twelve independently compiled controls invert
  attachment/liveness or alter attachment, duration, flag mask, identity,
  link mode, matrix, preset, retired duration, retired flag, or slot semantics
  and all fail;
- the sole aligned callback pointer at ROM `0x22EFC8`, registry slot
  `D_8008A4E8[8]`, no-direct-JAL census, and all three helper bindings are
  retained; and
- 251 exercised fault observations cover 61 unique `(PC, delay-of, cut)`
  active root-memory boundaries across both retail and natural C without
  weakening the instruction or branch-delay contract.

All three relocations and 22 owner neighbors are fixed. The strict
6,052-function image changes only `func_1519E464`, preserves every function
address with zero exclusions, and leaves all 189,088 protected Game-data
bytes across 720 owners exact.

The installed focused suite passes all four tests in 31.071 seconds. The
shared match-progress, generated-PC16, guarded-object, and protected-data suite
passes all 19 tests in 61.572 seconds.

## Production closure

The actual Make owner rule rebuilt `generated_1CA420`, and the production
owner and ELF equal the independently predicted qualified artifacts. The broad
`make all` path rebuilt the binary and stopped only at the expected final
retail SHA check. The inherited duplicate `generated_12D630` recipe warning is
unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `a5c1e8563569c8e9d81a2316ed35fe37d05d2eaafbefcd54bf1ecffe95ea25be` |
| Qualified / production linked ELF | `0a82da0c4b6fd9f4bd863fce648e4f313dc89482b1e7cf34c43d2ca2e1604381` |
| Production rebuilt ROM image | `d2a4c66fd246e97cc82649c953dbd140950e0644ecb805439381b1f76a18fd0f` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Installed owner source | `946a7618ae4d82a37bc91a4da070964e26599cfa7e316bf8094672a5aacda5c1` |
| Guard table | `8516b4ea5fc16f8ad49f0108159cb5e4f7e5424d27cc38b758d1d45f76671c89` |
| Retail layout | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |

## Recount

The fresh production ELF reports:

- Total: **4,148 / 5,512 (75.25%)**, zero address drift, 1,364 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,475 / 4,839 (71.81%)**, zero drift, 1,364 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **262 more** are needed.

## Continuation

After the seven documented handwritten/custom-ABI/boundary rows, the fresh
production rerank has a 63-real-difference tie between ordinary Game
candidates `func_151B6320` and `func_151C86AC`, each with a 64-word slot.
Start with `func_151B6320`, retaining `func_151C86AC` as the tied fallback.
Keep the boundary rows (`func_150A76F0`, `func_151F8870`, `func_150A613C`,
`func_150AE280`, `func_15115F68`, `func_151AE2BC`, and `func_150A6760`)
separate until their specific boundaries are addressed. Every ordinary
candidate still requires source/ABI/caller, owner, guest/native, actual Make,
complete-image, protected-data, production recount, documentation, and
graph-retention gates before credit.

## Graph retention

The retained graph baseline was 58,522 nodes / 112,374 links with SHA-256
`147762780640aff4a9b31483038c35ecc8fa47297985201a8ede88de166fcca3`.
The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,731 nodes, so Graphify correctly refused to overwrite the
retained corpus. Its fail-closed report retained 31,816 nodes from 3,754
still-present files outside that reduced scan. The graph remained
byte-identical at the baseline hash.

An explicit eleven-path incremental rebuild with `force=False` then produced
58,533 nodes, 112,384 links, and 5,095 communities. Against the saved
pre-change graph, 58,519 / 58,522 old node IDs were retained, including every
ID outside the changed-path set. The three replaced IDs are line-derived
`DOCS/UPDATE_LOG.md` headings, each with its corresponding replacement two
lines later. Fourteen IDs were added: those three relocated headings; the
Note 2077 file, title, and eight indexed section headings; and the retained
`OwnerEffectRecord1519E464` type. The eleven-node and ten-link net additions
are confined to the owned changes. This qualified graph has SHA-256
`ac748da69023b88aec78a632d87062eb0318344a81d07414345fbaee728d1a94`.

After adding this receipt, a one-path stabilization retained every node ID and
found no code-graph topology change.
