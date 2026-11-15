# Game configurable particle constructor guarded match

Date: 2026-11-14. `func_15175390` is recovered in
`conker/src/game/generated_1A20A0.c`. Its complete **370 words / 1,480
bytes** are byte-exact after **219 relocation-aware expected-word guards**.
The semantic C body emits the original **0xB8-byte frame**, saved-register
roles and private homes before normalization. This is a guarded match;
**219 raw words differ**, and 151 already agree. Owner **3 / 9 C-exact**.

VA **0x15175390..0x15175958**, ROM **0x1A2840..0x1A2E08**.
The earlier private milestones are retained in
[Note 2443](2443-game-configurable-particle-recovery-and-frame-fit-20261114.md)
and [Note 2444](2444-game-configurable-particle-original-roles-and-normalization-20261114.md).
All their remaining adoption gates have now passed for this function.

## Recovered contract

The void interface carries **18 transport words**: count, slot, X/Y/Z,
outer radius, view, vertical range, inner radius, flags, base type/range,
base model/mask, state, base scale, scale range and ground flags. The five
existing calls in `func_15183290` already describe this interface and
ignore a return value. No caller/header changes are needed.

The complete source preserves the early flag-0x40 vertical-range gate,
cached heading flag and inner radius, optional type draw before allocation,
signed radius remainders, and live homes after providers. The query gate
is **state == 0 OR captured ground bit != 0**. State zero truncates the
queried height; other states retain Y or add the unsigned vertical draw.
Model indexing retains its full word width, while only the stored variant
byte narrows. The first non-type-10 record retains its sound handle; later
records clear it. Source coordinate/range halfwords, material classification
and final state clears keep their original widths and order.

The owner's PRNG declaration is corrected to signed `s32`, consistent with
the primary interface and the signed radius divisions. Explicit unsigned
modulus expressions retain the other draws. Independent raw recompilation
and the actual Make path preserve all **eight other owner functions and
named bindings**, including the preceding two matches. Pools stay absent.
Inline comments identify the reused divisor/Z value and the surface local
that a failed query may leave untouched.

## Checked normalization

The static source-derived normalizer remains in
`tools/experiments/game_configurable_particle_15175390_normalization.py`;
`game_configurable_particle_15175390_match.py` derives the actual guard rows
and both object candidates. It accepts only raw SHA-256
`8055bc014c509dfc595ad13ad0ac1045b6136aa2e094a2d3e3decb6b427f8aec`
and all **27 named bindings**. All **397 source-word/binding corruption
controls** are rejected. No retail body is read by the transform itself.

The closed 370-slot inventory preserves saved/FPR fields, constants and
bindings. It changes caller-temporary allocation in 76 words and moves
168 word slots. Three redundant source operations become explicit branch
edges; another becomes a NOP. The four removed operations are the second
remainder copy, an extra mutually exclusive state-home load, a duplicate
ordinary surface-local load and a duplicate material shift. Two BEQL forms
become BEQ, and three explicit edge redirects preserve their joins. These
are CFG lowerings as well as scheduling; they are not described as direct
C emission. No words are inserted or omitted.

The local proof retains both symbolic surface paths, the second-remainder
copy's single consumed use and dead lifetime, and **54 executed query
branch/delay cases** with arbitrary provider changes to the later state
home. Both the kind-offset and query-register controls are effective.
All existing guard bytes/rows are preserved; exactly **219** task rows
are appended.

## Qualification completed

- [x] **1,152 independent guest cases**, **63 directed cases** and eight
  emitted break/conversion boundaries compare retail, raw C and the actual
  guarded object against the observable-memory/helper-packet model.
- [x] Three effective recompiled controls reject unsigned radius sampling,
  the reversed query gate and incorrect first-record sound behavior.
- [x] **639 native32 cases per profile** at O0/O2/O3 pass with undefined-
  behavior traps enabled. Each compares all **992 seeded particle bytes**,
  full helper packets, all sixteen model records and relevant shared globals.
  Effective wrong lifetime, repeated sound and material-stride controls fail.
- [x] **720 executions through all five original caller windows** compare
  all eighteen transported words and verify saved registers across retail,
  raw and guarded bodies. The windows contain 33/34/35/35/33 words at
  JALs **0x15183480, 0x15183658, 0x1518370C, 0x151837A8, 0x1518383C**.
  These start after their setup providers; no complete parent/provider
  execution is claimed.
- [x] **24 retained-surface cases** execute retail and guarded streams.
  **48 additional cases** connect the original 215-word ground helper's
  actual failure branch, visiting nineteen words with bounded reset and
  predicate providers. The prior SP+0x80 surface reference is retained.
- [x] **363 memory-access prefixes** compare full guest memory, GPRs, FPRs,
  HI/LO, calls, traces and current delay-slot state for retail versus guarded
  code. Raw C fault order is not claimed. A query that leaves its local
  unwritten remains outside portable native-C qualification.
- [x] Both complete-owner padders and **four independent GNU layouts**
  pass twelve links, including independent function/data rebases and low-half
  carry/sign boundaries. All nine owner functions and pools agree between
  guarded/padded objects.
- [x] The **three actual Make recipe commands** reproduce the independently
  compiled/padded owner. The predicted complete image has zero exclusions.
- [x] Post-install focused suite passes in the mounted tools checkout and
  the isolated sibling overlay. Shared `make tools-check` passes.

The semantic corpus visits **366 / 370 retail words**. The unvisited offsets
remain `0x140`, `0x200`, `0x3A8`, `0x578`; literal object/link comparisons
cover all 370. Guest boundaries and bounded-provider checks do not claim
emulator, hardware, complete provider or host-gameplay acceptance.

Reproduce the focused suite at the prepared consumer checkpoint:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_configurable_particle_15175390_match -v
make tools-check
```

The suite retains its before-source snapshot under the ignored target
`production-baseline` directory; preserve that qualification fixture.
The isolated replay uses **fourteen byte-identical task files**, sibling
dependencies and mounted fallback, rather than changing the dirty sibling.
Its HEAD stays `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`; all **2,439** dirty paths and
status SHA-256 `a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb` are unchanged. Zero Claude calls.

## Production image and measured progress

The rebuilt production ELF exactly equals the independent prediction.
All **6,051 function addresses** are fixed; only the target body/extent
changes. The complete **1,089-byte** difference is accounted for by that
slot, its 12-to-1,480-byte symbol-size correction and the closed metadata
ordering of `D_800A7178` / `D_800AC278`. Strict exclusions: **zero**.

All **189,088 protected data bytes** across 720 owners remain exact.
Of **698 production objects**, only `generated_1A20A0.c.o` changes, in
`.text`, `.rel.text`, `.symtab` and `.strtab`; its other eight functions and
pools stay fixed. All **82 headers**, conversion rows and **801 other
frozen inputs** remain unchanged. The allowed source/object/ELF/guard
changes are verified explicitly.

Production ELF SHA-256:
`1de835430a23936cd53056b5d1367389580c35203c1f3b1ca3256ac102e8be86`.
Fresh actual-ELF recount:

| Section | Byte-exact C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | **4,488 / 5,515 (81.38%)** | 0 | 1,027 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | **3,815 / 4,842 (78.79%)** | 0 | 1,027 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

This adds exactly **one** C match. Converted functions remain 5,515 / 6,048; the converted-byte percentage
remains 86.17%. **200 more matching functions** reach 85% at the
current denominator; the wider goal remains active.

Scoped Graphify AST refresh covers six tools files and the owner, retaining
all **60,728** existing IDs: **60,756 nodes /
114,301 links**, zero lost nodes. This is not full-corpus extraction.
Tools commit `e03a618ede756b5f2c9535dc8f4419492494bfff` precedes the consumer commit. The root README gets
aggregate row changes only; detailed recovery updates stay here. No push.
The sibling `64CBFDOGL` has no source checkout here, so there is no host
adoption or build; Release stays frozen.

Next focused target: **101-word `func_151770C8`**, the same owner's display
callback at ROM **0x1A4578..0x1A470C**, VA **0x151770C8..0x1517725C**,
with frame **0x90**. Start with its culling call, signed-halfword view home,
state-zero matrix/display-list path and delegated `func_15176DF0` path.
The new production baseline for the next recovery is the SHA above.
