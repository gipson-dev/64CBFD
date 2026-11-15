# Game particle material renderer guarded match

Date: 2026-11-14. `func_15176DF0` is recovered in
`conker/src/game/generated_1A20A0.c`. The complete **182-word / 728-byte**
retail body matches after **75 checked guard rows**, including **one inserted
register copy**. The semantic C emits **181 words** before normalization;
this is guarded matching, not 182 words directly emitted by C. The original
**0xD8-byte frame**, saved-register roles and both matrix homes already match.
The owner is now **5 / 9 C-exact**.

VA **0x15176DF0..0x151770C8**, ROM **0x1A42A0..0x1A4578**.
Derivation: `tools/experiments/game_particle_material_15176df0_match.py`.
Raw text SHA-256:
`c8c9605fe8db5638f32ca47c83578287e4e4c97b78fd81b6440882eb0de685fd`.

## Recovered contract and behavior

The routine returns `Gfx *` and takes commands, a 248-byte particle record
view and a signed-halfword view. The last argument is unused, but its O32
home store is retained. The typed declaration and definition preserve all
eight neighboring raw bodies and named bindings, including the explicit
cursor cast in `func_151770C8`.

The opening short-circuit gate snapshots the byte variant, tests the first
model word at `D_800DDE80[variant * 5]`, then the signed control word at
`D_800DDF78[variant]`. A failed gate returns the original cursor. The active
path builds heading and tilt matrices with `func_150A8050`, then invokes
`func_150A7A48(tilt, matrix, matrix)` with the actual second-input/output
alias. It replaces only the three translation components and scales the
nine 3-by-3 entries, retaining the original live scale reloads.

`guMtxF2L` writes the selected 64-byte matrix page inside the record. The
emitted matrix command rereads the page after that provider. Segment 1 uses
the record's live model pointer. A pipe sync precedes the shade update.
The target shade comes from the four-entry palette selected by surface flags
bits 5..6. Arithmetic wraps as unsigned 32-bit before signed comparisons:
brightening clamps at the target; darkening clamps below zero at **zero**.
The byte field is stored only when the current shade differs from its target;
the full working word remains available to the three color saves.

The material call receives modes `0x82CA0` and `0x504A50` and an initially
zero sync byte. It returns the advanced command cursor. Environment RGB
uses the three saved full-word colors; alpha is read from the record after
the provider. The final display-list lookup likewise uses the late live
variant and the five-word table stride at `D_800DDE8C`.

## Guard derivation and boundaries

The normalizer pins all **181 raw words** and **21 named bindings** and
rejects all **202 altered-word/binding controls**. It does not read retail
words to transform a candidate. Its static ledger accounts for every source
instruction once, plus one ordinary `OR T0,V0,zero` copy:

- Six RGB stores/loads move the private homes from SP+0x40/0x44/0x48 to
  SP+0x48/0x4C/0x50. The sync byte/address move from SP+0xD7 to SP+0x33.
  Both matrices remain at SP+0x54 and SP+0x94.
- Sixty-eight instruction words adjust only caller-temporary register fields.
  Saved registers, floating registers, operations, constants and named
  bindings retain their roles. The home edits overlap some of these words;
  these counts are not separate guard-row totals.
- The inserted copy at normalized offset 0x238 preserves the blue snapshot
  through its store in the material JAL delay slot at 0x258. All three shade
  joins enter that copy; no branch enters its straight-line live interval.
- A closed instruction inventory, with private homes accounted for, equals
  the original inventory plus precisely that copy. Branch displacements
  follow the source permutation and the three explicitly checked joins.

Exactly **75 rows** are appended, with **one insertion** and **no omissions**.
Every previous guard byte is preserved. Raw C fault-register order is not
claimed. Retail and the actual guarded stream receive the full-state prefix
comparison; raw C receives the applicable public semantic comparison.

## Completed qualification

- [x] **1,024 guest cases** compare retail, raw C and actual guarded code,
  including gate combinations, all shade bytes, wraparound steps, provider
  mutations, sparse indices/pages, packed views and two stack phases.
  Matrix providers capture all 32 multiply-input words and all 16 conversion
  input words. Caller GPR/FPRs and outgoing homes are deliberately clobbered.
- [x] **24 private-color probes** overwrite the original three private RGB
  homes with distinct full words. These run retail/guarded only and prove
  the separate saves and loads. They are not portable native C tests.
- [x] Command buffers alias the record and model table in guest probes,
  exercising late alpha/list reads and opcode-store/table-read ordering.
  **229 target-memory prefixes** compare complete guest machine state for
  retail versus guarded code. Public cases visit **181 / 182 retail words**;
  the duplicate load at offset **0x60** remains unreachable. Literal matching
  and corruption controls still cover all 182 words.
- [x] **704 native32 cases per O0/O2/O3 profile**, with undefined-behavior
  traps, compare 248 record bytes, 256 command bytes, helper packets, matrix
  snapshots and valid shared tables. Five effective controls reject the
  wrong darkening clamp, ninth scale, matrix-input order, alpha field and
  display-list stride. Native cases use variants 0..3, pages 0..1, distinct
  command storage and ordinary provider mutations.
- [x] **192 original registry-dispatch executions** exercise all eight ROM
  slots and the authentic eight-word dispatcher at
  **0x15167898..0x151678B8**. The slots are 0x8008B6B8, 0x8008B8C0,
  0x8008B8F4, 0x8008B928, 0x8008B95C, 0x8008B990, 0x8008C280 and
  0x8008C2B4. All three argument words, bookkeeping and saved registers
  qualify.
- [x] **96 connected executions** run the original complete 101-word
  `func_151770C8` and its actual JAL at ROM **0x1A46E8**, through culling
  rejection or nonzero-state delegation. They compare the post-cull signed
  view packet and cursor result. Three emitted controls reject the missing
  blue copy, wrong red home and wrong alpha field.
- [x] Both complete-owner padders pass **four independent GNU layouts /
  twelve links**, including code/data rebases and low-half carry boundaries.
  All nine owner functions and pools agree. Actual Make's three recipe
  commands reproduce the independently compiled/padded owner.
- [x] Strict whole-image prediction, installation, production build/audit and
  fresh actual-ELF recount pass. The post-install suite passes in mounted
  tools and the isolated sibling overlay; shared `make tools-check` passes.

Providers are bounded deterministic models, not full trigonometric,
matrix-multiply or conversion implementations. Guest sparse/alias/home probes
do not expand the native C contract. No emulator, hardware or host-gameplay
acceptance is claimed. Routine Claude calls: zero.

Reproduce in the prepared consumer, retaining the ignored baseline fixture:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_particle_material_15176df0_match -v
make tools-check
```

The sibling overlay uses six byte-identical task files, sibling dependencies
and mounted fallback without writing to `64CBFD Tools`. Its HEAD remains
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`; all **2,439 dirty paths** and
before/after status SHA-256
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`
are preserved.

## Linked image and progress

The 806-input baseline includes 698 objects and 82 headers. The **802
immutable inputs** are unchanged; only the declared source/object/ELF/guard
inputs differ. Only `generated_1A20A0.c.o` changes, in `.text`, `.rel.text`,
`.symtab` and `.strtab`. All eight neighboring functions/bindings and pools
remain fixed. Conversion rows are byte-identical.

The production ELF equals the independent prediction. All **6,051 function
addresses** remain fixed; only this body and its 12-to-728-byte symbol extent
change. Exactly **623 image bytes** differ, with **zero exclusions**. The
fully accounted metadata permutation is:

```text
D_800DDE8C, D_800DDAAC, func_151B3A7C
    -> D_800DDAAC, func_151B3A7C, D_800DDE8C
```

All **189,088 protected bytes across 720 owners** remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production ELF SHA-256:
`59c204ea9d391dc0e0890439eb3fabb9b90fdb6ade992f02dd8563779bd34800`.

| Section | Byte-exact C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | **4,490 / 5,515 (81.41%)** | 0 | 1,025 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | **3,817 / 4,842 (78.83%)** | 0 | 1,025 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

One new C match is credited. Converted functions remain **5,515 / 6,048
(91.19%)**, converted bytes **86.17%**. **198 more matches** reach 85% at
this denominator. Keep the wider goal active.

The scoped Graphify AST merge covers the six tools files and owner, retaining
all **60,803 old IDs** with **zero lost nodes**: **60,847 nodes / 114,444
links**. This is a scoped refresh, not full-corpus re-extraction.
Tools commit `a69d646b556d082ef8dc307fe87d57789a92e978` precedes the consumer commit. Root README changes
are aggregate rows only; no push. `64CBFDOGL` has no source checkout here;
Release remains frozen and no host adoption/build is performed.

Next focused target: **106-word `func_1517725C`**, VA
**0x1517725C..0x15177404**, ROM **0x1A470C..0x1A48B4**, frame **0x30**.
Preserve its three alignment words through 0x15177410. Inspect its byte slot,
56-byte state indexing, model lookup, two trigonometric vertex-update paths
and one-step angle wrap before qualifying a replacement. Use the production
SHA above as the next baseline.
