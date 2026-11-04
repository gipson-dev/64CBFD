# Game extended random payload callback guarded match (2026-11-04)

## Outcome

`func_1515AA84` now replaces its zero-return placeholder in
`conker/src/game/generated_185560.c` with a typed effect-payload callback. It
matches all 65 retail words with the original 128-byte frame. Nineteen checked
word rows normalize one closed compiler-local difference after the random
number call: the owner pointer, lifetime fields, remainder result, outgoing
arguments, and divide guard occupy different temporary registers and schedule
positions. No words, calls, branches, or effects are inserted or omitted.

This is a source, callback-registry, compact/padded owner, guest/native
execution, strict whole-image, protected-data, production-build, recount, and
graph-retention result. It is not visual effect, particle lifetime, rendering,
save, gameplay, or PC-port runtime acceptance.

## Recovered behavior and ABI

The O32 callback takes an owner pointer, a three-float position, a scalar, and
an unused fourth argument. It builds a 60-byte payload on the stack: floating
zero, the copied position, the scalar, and the owner's 40 bytes at offsets
`+0x84..+0xAB`. It then calls `func_150ADA20` and computes a narrowed unsigned
16-bit lifetime as:

```text
(random % (*(s16 *)(owner + 0x82) + 1)) + *(s16 *)(owner + 0x80)
```

The callback calls `func_15149130` with that signed-16 lifetime, category
`0x3F`, payload-size marker `0x3C`, and the live owner bytes at `+0x0C` and
`+0x01`. If allocation succeeds, the complete 60-byte payload is copied to
the created record at `+0x28`; allocation failure performs no copy.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x1515AA84..0x1515AB88` |
| Retail ROM range | `0x187F34..0x188038` |
| Owner | `generated_185560`, 36 neighboring functions |
| Body / retail slot | 65 / 65 words |
| Frame | 128 bytes |
| Bindings | 3 calls: RNG, record factory, and `memcpy` |
| Natural compact normalized SHA-256 | `348476bfb8dc1e3916ccae5691e24920b9d2cab8974ebb4f0651fa311b8f8e35` |
| Linked retail body SHA-256 | `6e62ce718edb8be90e7bfe301a517c46f15fe40c3967a284cbc6b9b37e113d90` |

## Callback and binding evidence

The aligned function pointer is callback-table slot `D_8008F970[2]`, at retail
ROM `0x234438`. There is no direct `jal` caller. The original dispatch window
selects slot two and supplies the owner, position, scalar, and fourth argument.
All three linked calls resolve to their retail targets, and the real table and
dispatch window pass the focused execution gate.

## Guarded-match boundary

The semantic source naturally emits the correct 65-word size, 128-byte frame,
all three calls, payload construction and copy, and the complete epilogue. Its
first 30 words through the RNG call's delay slot already match retail. The 19
remaining positional differences form one closed post-RNG owner/lifetime
register-and-schedule cycle. The checked rows require both the natural compiler
word and exact retail replacement, so source drift, guard-preimage drift,
offset drift, or a different compiler allocation fails closed.

The retail divide-by-zero break remains present. It is unreachable for the
qualified owner range where the signed range field plus one is nonzero; the
test suite records that boundary rather than claiming portable behavior for
invalid owner data.

## Qualification

The permanent five-test suite establishes:

- 1,424 guest cases exercise both allocation routes, alias layouts, signed
  lifetime ranges, and all 64 reachable words; only the invalid-divisor break
  is deliberately outside the qualified domain;
- the real callback table and original ten-word dispatch window select slot
  two and preserve the recovered argument contract;
- native 32-bit O0, O2, and O3 each pass 8,192 cases, for 24,576 executions;
- eleven independently compiled semantic controls are rejected;
- all three bindings, 19 checked rows, and all 36 owner neighbors are fixed;
- the strict 6,052-function image changes only `func_1515AA84`, preserves all
  function addresses with zero exclusions, and changes no other body; and
- all 189,088 protected Game-data bytes across 720 owners remain exact.

The installed focused suite passes all five tests in 43.495 seconds. The
shared match-progress, generated-PC16, guarded-object, and protected-data suite
passes all 19 tests in 8.354 seconds. Qualification tools were banked first in
tools commit `9bfbee8`.

## Production closure

The actual Make rule rebuilt every padded owner that depends on the shared
guard table, then linked `build/conker.us.elf` successfully. This broad rebuild
is the section-level guard audit: no unrelated guard preimage or owner padding
failed. The installed report confirms `source_installed: true`; the production
owner and full ELF equal the independently qualified artifacts. `make all`
then generated the binary and stopped only at the expected final retail SHA
check. The inherited duplicate `generated_12D630` recipe warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `896b9195400610a33e8ad02277f4c484bb414ed0a85032773c67cf9d20d55576` |
| Qualified / production linked ELF | `ab924562febf40151fb5366fbf2b266b4eb47a1b7450d244d11cfe785b9c5014` |
| Production rebuilt ROM image | `0146fa2d3c6d6f1c8f3170a9373f31c5fb14eabf49e93055b8d522527a7f8f6b` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Installed owner source | `bfeb56332a0ce822b9e008c1ba96af2b4ecc4c8b4f06adae8049d77459a6fc08` |
| Guard table | `86559f1ec5fd731636f9ffc1a9960d9fc427cbdc5466bdff7289ea6800f800ab` |
| Retail layout | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |

## Recount

The fresh production ELF reports:

- Total: **4,142 / 5,512 (75.15%)**, zero address drift, 1,370 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,469 / 4,839 (71.69%)**, zero drift, 1,370 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **268 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,663 nodes against the retained 58,453-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph remained byte-identical with SHA-256
`381e2fe19fb71e1ef5c9a60a33327277043930ebe9ddf3b8967d51bf0cc21696`.
No forced refresh or dependency update was used.

An explicit eleven-path incremental rebuild with `force=False` then produced
58,465 nodes, 112,323 links, and 5,084 communities. Against the saved
pre-change graph, 58,450 / 58,453 old node IDs were retained, including every
ID outside the changed-path set. The three replaced IDs are line-derived
`DOCS/UPDATE_LOG.md` headings, and each has one uniquely relocated replacement
two lines later. Fifteen IDs were added: those three relocated headings, the
Note 2071 file and its ten indexed headings, and the
`PayloadVector1515AA84` type. The twelve-node and thirteen-link net additions
are confined to the owned changes. The explicit-refresh graph SHA-256 is
`bf2fa6683582a5b508274e2db8b54a8e5ec1f30866ff8a5c33b5c278d8746bbf`.
A one-path refresh after recording this receipt retained all 58,465 scoped
node IDs and all 112,323 links with zero loss or replacement.

## Continuation

The seven smaller rows ahead of the ordinary queue remain the documented
handwritten/custom-ABI/boundary cases: `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Continue with ordinary Game candidate `func_1515BE50`.
Every candidate still requires source/ABI/caller, owner, guest/native, actual
Make, complete-image, protected-data, production recount, documentation, and
graph-retention gates before credit.
