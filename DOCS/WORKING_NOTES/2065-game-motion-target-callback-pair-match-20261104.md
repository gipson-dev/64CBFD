# Game Motion-Target Callback Pair Match (2026-11-04)

## Outcome

`func_150C84F4` and `func_150C851C` now replace two zero-return placeholders
with the semantic motion-target callback pair and match their complete 10-word
/ 40-byte and 57-word / 228-byte retail bodies. The former merged retail slot
is split at the real `0x150C851C` boundary. The wrapper emits directly from C;
four checked replacement rows normalize only the initializer's independent
fixed-point base/span register allocation and schedule.

This is a source/ABI/caller, boundary/inventory, raw and padded owner,
guest/native execution, assembly-truth whole-image, protected-data,
production-build, recount, and graph-retention result. It is not live motion,
camera, scene, save-state, or gameplay acceptance.

## Preserved semantic contract

`func_150C84F4` is the one-argument callback registered at
`D_8008CD04[9]`. It advances `func_150C8350` only when the signed frame-layer
index is zero. Nonzero layers return without calling the advance routine.

`func_150C851C` first tests the motion-table pointer `D_800BE4E0`. A null
table is a complete no-op. With a table present, it calls
`func_150CDB6C(intensity)`, derives the signed fixed-point base
`(intensity * 300) >> 8`, and derives the unsigned remainder span
`((intensity * 50) >> 8) + 50`. It then consumes exactly ten
`func_150ADA20()` results. Each result is interpreted as unsigned for the
remainder, added to the signed base, truncated to `s16`, and stored at offset
8 of ten consecutive 10-byte records.

The unsigned random cast is material. A signed-modulo control diverges on
high-bit random values and is rejected by the native corpus.

## Boundary, ABI, owner, and callers

The recovered boundaries are:

- `func_150C84F4`: VRAM `0x150C84F4..0x150C851C`, ROM `0xF59A4`, 40 bytes;
- `func_150C851C`: VRAM `0x150C851C..0x150C8600`, ROM `0xF59CC`, 228 bytes.

Their ABIs are `void func_150C84F4(s32 view)` and
`void func_150C851C(s32 intensity)`. The wrapper has a 24-byte frame and one
`R_MIPS_26:func_150C8350` binding. The initializer has a 48-byte frame and
four bindings: the `D_800BE4E0` HI/LO pair, `func_150CDB6C`, and
`func_150ADA20`.

Both functions are owned by `conker/src/game/generated_F5800.c`. The
qualifier freezes all 17 neighboring owner functions. Adding the real second
symbol changes the strict disassembly inventory from 6,051 to 6,052
functions, but an inventory-only split leaves every loaded section byte
unchanged.

The retail image contains no direct call or jump to the wrapper; its aligned
pointer at ROM `0x2317E8` is callback-table slot `D_8008CD04[9]`. The
initializer has three direct calls and no jump or aligned pointer literal:

- ROM `0xBC98`, from `func_1000BC28`;
- ROM `0x3D3B8`, from `func_1500FE30`; and
- ROM `0x53094`, from the script command `0x55` handler.

## Compiler normalization

The wrapper's natural 10 words already equal retail. The initializer's
natural body has the retail 57-word length, 48-byte frame, branch structure,
loop, calls, stores, and bindings. Four positional words differ:

- offset `0x070` moves the span fixed-point shift to retail's register;
- offset `0x074` moves the base fixed-point shift to retail's register;
- offset `0x078` carries the base through retail's `t8` lifetime; and
- offset `0x07C` carries the span through retail's `t7` lifetime.

Every row checks its expected natural word before replacement. There are no
inserted words, omitted words, changed branches, changed calls, changed
relocations, or patched semantic constants.

## Qualification and execution

The permanent candidate screen, qualifier, independent guest oracle, and
four-test suite were committed first as tools commit `01f8bac`
(`test(game): qualify motion target callback pair`). The installed-tree suite
passes all four tests in 97.097 seconds:

- the qualified owner object is byte-identical to an owner rebuilt with the
  two original assembly functions;
- the qualified full ELF is byte-identical to the corresponding
  assembly-truth ELF;
- only the two target bodies change, all function addresses remain fixed,
  there are zero strict-image exclusions, and all 17 neighbors remain exact;
- 288 initializer cases cover 12 signed intensity values, null/present table
  states, six random patterns, and two stack phases;
- those cases reach 56/57 initializer words; the remaining IDO
  divide-by-zero trap is skipped for every qualified nonzero span;
- eight wrapper cases cover four signed view values and two stack phases and
  reach every wrapper word;
- native 32-bit O0, O2, and O3 builds each pass 96 initializer cases with
  undefined-behavior checking enabled, for 288 native runs;
- nine independent semantic controls are rejected; and
- all 268 raw-byte mutations, four guard-preimage mutations, five relocation
  controls, and three boundary/symbol/fallback metadata controls fail closed.

The shared match-progress, guarded-object, generated-PC16, and protected-data
suite passes all 19 tests in 6.831 seconds. Protected Game data remains exact
at `0x80082760`: 189,088 bytes across 720 owners, zero different bytes or
owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Production closure and frozen evidence

The actual production ELF target rebuilt the complete object corpus because
the shared guard manifest changed. It compiled, padded, assembled, and linked
`generated_F5800` normally. The assembly-truth qualifier and installed
production artifacts have the same owner and full-ELF hashes. The subsequent
`make -C conker all -j2` generated `conker.us.bin` and stopped only at the
expected final retail-ROM SHA mismatch. There was no compile, padding,
assembly, link, or image-generation failure. The known duplicate
`generated_12D630` recipe warning remains unrelated.

| Artifact | SHA-256 |
| --- | --- |
| Natural wrapper compiler body | `fbd4957fdbbfd0aa1d1151d80ac4c9b855e9a50512e43a44e2dba6fed332829c` |
| Natural initializer compiler body | `ae64e70d706ac3da5e326de8f9805f0f09c51ff4a2972f9a48d6a889985a6e72` |
| Complete linked retail wrapper body | `dfc02278a0a839890e3995367c6854a32a7b781e046ff29e70eff0d6e8f8661b` |
| Complete linked retail initializer body | `a7824c362f513604e2da19bc96450f4981454abdf28af3debf90e5971f2d8e7d` |
| Installed semantic owner source | `fe559bed8f11b2d27abda91a9ec918a6825d5784cc28e0202275c80b3db35aaf` |
| Qualified / assembly-truth / production owner object | `ae7d06cdcdbeeb3d9fb51351158b0dae06a5b3a568dc82c9455b06f67adb721b` |
| Qualified / assembly-truth / production linked ELF | `cd79de5ea0cab3e9f1b7c0026b85ca2ee0e2ea8dfe0a7ba60983ce7966923b43` |
| Production rebuilt ROM image | `d31f7b4dce792a1e5ca65230d1beb63fdad211f56e938bdfb97940ba4dfed1e0` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Guard table | `2c94dfb97dbd6abd4bdab3c379ea92d6131a5a1f70a2d2c04d1608a4d80ab85a` |
| Retail layout | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |
| Added symbol catalogue | `f61c49d189e4cf0fedb56afa846db97d5f50ab58ad87a8bf90c202713d48bc5f` |
| Aggregate progress catalogue | `4f170efa6034414c9a2612153aac6ea69468b99f7523dde4a11370f8b07a2c99` |

## Recount

The fresh production ELF reports:

- Total: **4,136 / 5,512 (75.04%)**, zero address drift, 1,376 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,463 / 4,839 (71.56%)**, zero drift, 1,376 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory is 5,512 / 6,046 functions. Splitting the former
merged row adds one source and converted function but no bytes. The active 80%
threshold is 4,410 exact functions, so **274 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted nine uncached inputs but
proposed only 24,592 nodes against the retained 58,386-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph remained at 58,386 nodes / 112,247 links / 5,069
communities with SHA-256
`a9dd474567e69ff7c33badb354d732811dbfaaea74adfc53ddb2330306905b4e`.
No forced refresh was used.

An explicit 15-path incremental rebuild with `force=False` then produced
58,396 nodes, 112,256 links, and 5,076 communities. Against the saved
pre-change snapshot, 58,383 / 58,386 old node IDs were retained. The three
replaced IDs are line-number-derived `DOCS/UPDATE_LOG.md` headings, and each
has one uniquely relocated replacement two lines later. Thirteen IDs were
added: the three relocated headings plus the Note 2065 file and its nine
indexed headings. The nine-link net addition is confined to the explicitly
re-extracted owner, metadata, tools, and documentation. The explicit-refresh
graph SHA-256 is
`3891ad284167b2e0dcbcadf35a04500fb34790639f1df104993c12e1f9ffbc24`.
A final note-only refresh after recording this section adds only its new
heading and produces 58,397 nodes and 112,257 links. The same 58,383 old node
IDs remain retained, the topology otherwise stays within the explicitly
refreshed paths, and clustering completes normally.

## Continuation

Rerank the ordinary Game queue from the fresh production ELF. Keep the seven
documented non-ordinary boundary cases separate: handwritten/custom-ABI
`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC`, and `func_150A6760`. Every candidate still
requires source, ABI/caller, owner, guest/native, actual Make, complete-image,
protected-data, production recount, documentation, and graph-retention gates
before credit.
