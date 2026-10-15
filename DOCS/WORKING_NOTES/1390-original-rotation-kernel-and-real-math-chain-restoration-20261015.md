# Original Rotation Kernel And Real Math Chain Restoration

Date: 2026-10-15. Continue the rotation-provider boundary from
[Note 1389](1389-actor-world-matrix-builder-direct-match-20261015.md) and the
whole additional-source/Game objective. This checkpoint restores original
assembly and removes one false C conversion; it is **not a new C byte match**.

## Scope And Source Evidence

`func_150A8050`, owner `conker/src/game_D5500.c`, retail VA
`0x150A8050..0x150A81A0`, ROM `0xD5500..0xD5650`: 83 instructions and one
alignment NOP, full slot 84 words / 336 bytes. The old empty C definition has
a 24-byte linked symbol and never initializes its destination matrix.

Start with clean consumer `69438b6d` and tools `3e43b4a`. Freeze 38 named
inputs under ignored `conker/build/game-rotation-matrix-leaf/before-*`.
The predecessor ELF is
`3772196e96e4e1e09cbc7234ce6532e4d84e73661b4524a4c82cc31765158777`.
Every frozen input/manifest is pinned, not recaptured after restoration.

The archive `conker/src/game_D5500.c` supplies GLOBAL_ASM, not C, SHA-256
`e17cd6462cefe6063a339fcdebd1f25084ac364c7efd42ab39bda6c52ea2cb50`.
The local SDK `tools/ultralib/src/gu/rotaterpy.c` confirms the rotation formula
but does not establish this retail stack/register layout. Keep both references
read-only and preserve all original 801 archive fingerprints.

Retail saves F24 before decrementing SP, holds the destination at SP+8 through
six math calls, releases 16 bytes midway at `0x150A80E0`, and finally releases
32 bytes after restoring six even FP registers. Preserve that physical lifetime,
the original arithmetic order and final homogeneous store in the return delay
slot. Do not replace it with an assumed ordinary C ABI frame or standard sin/cos.

## C Screen And Restoration Decision

Bounded complete semantic C screens, all with zero diagnostics:

| Profile | Emitted Words | Real Word Differences | SP Adjustments |
| --- | ---: | ---: | --- |
| O2/g3 | 87 | 83 | -72 / +72 |
| O2 | 87 | 83 | -72 / +72 |
| O1/g3, isolated pure C fixture | 135 | 133 | -56 / +56 |
| O1 | 135 | 133 | -56 / +56 |
| Original assembly adapter | 84 | 0 | -48 / +16 / +32 |

Use the existing isolated compiler helper for the private O1/g3 pure-C screen;
the asm-processor wrapper rejects that combination. No production profile is
changed. The C reference is functionally qualified below but remains uninstalled:
it does not fit the retail slot and has no matching private frame. This bounded
screen is not proof that every conceivable C recovery is impossible.

Restore the archived GLOBAL_ASM adapter, retain the existing exported function
name/declaration, and replace the stale question/placeholder comments with a
short measured-layout comment. Original assembly, headers, guards, Makefile and
data remain untouched. Both existing padders reproduce all 84 words, with the
original eight relocations. No new guards, copied literal instruction arrays,
dummy locals, truncation or broad conversions.

## Fresh Qualification

All 14 final top-level checks pass in 97.427 seconds:

```sh
python3 -m tools.experiments.game_rotation_matrix_leaf
python3 -m unittest tools.tests.test_game_rotation_matrix_leaf \
  tools.tests.test_game_rotation_matrix_leaf_candidates \
  tools.tests.test_game_rotation_matrix_leaf_installed -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- 512 root guest cases cover both stack phases, all 83 dispatched instructions,
  six ordered FP call packets, finite returned coefficients and mutation of the
  degree-conversion global after its captured read. Complete modeled private
  states agree, including even/odd saved-FP preservation and the split release.
  The final alignment NOP is compared separately, not falsely counted as reached.
- 198 paired, fired parent-access cuts agree in complete modeled state. Three
  returned word controls reject the wrong math call, missing pitch sign and
  zero homogeneous matrix element. No hardware-exception/FCSR claim.
- Native32 O2/O0 execute the **uninstalled semantic C reference** for 256 finite
  cases/profile, checking six FP packets, coefficient capture, all matrix words
  and canaries. Three effective returned controls fail. This validates the
  formula/interface only, not C byte identity or private-frame matching.
- 256 guest cases connect the actual 76-word math span at `func_150AD780`:
  cosine adds its phase offset and falls directly into the sine routine. The
  original 13 coefficient words and separate finite polynomial/reduction oracle
  agree. Reuse the existing exact finite RNE integer converter; no libm
  substitution or assumption that truncation equals CVT.W.S rounding.
- 128 builder and 128 position-consumer cases connect **all providers as actual
  guest instructions**: freshly compiled C builder/angle wrapper/actor lookup,
  unchanged guarded scale, original product/point transform, restored rotation
  and real math helpers. No opaque lookup, rotation or math callback is used in
  these chain tests. Compare independent matrix/coordinate results and complete
  modeled state. This remains a bounded low-word finite/RNE model, not gameplay
  or full VR4300/FCSR acceptance.
- Three independent original-assembly rebase pairs preserve constant signed-low
  carries, all six external calls and the complete padded slot.

## Literal Image And Classification

Construct the entire expected ELF independently from the pinned predecessor,
the 336 retail target bytes and only symbol extent `24 -> 336`. The normal
build equals it byte for byte: **280 changed bytes**, target slot/extent only,
no metadata exclusions or allowances. Every other ELF byte and all 189,088
protected data bytes / 720 owners remain fixed.

The generated progress CSV round-trips through the standard CSV reader/writer
without unrelated byte changes. Exactly one row changes `c -> asm`; its owner,
name, address and length do not change. Progress CSV remains an ignored build
artifact, not a newly force-added repository file. This corrects classification
instead of inflating C recovery totals.

| Input | SHA-256 |
| --- | --- |
| ELF | b6d087530249e76ea8bd684c32f8b5ebf0dfc7c631283931ae1611d3b5fd372a |
| Rotation owner | 6cf42acdb32617b934d526cabc47e3e5e58eb3352b5175dd19ff4b6c4ffa071d |
| Progress CSV | 595443d0129e7d6ccd1f824b050854d5759c0f45c1af5b0818ef7cde682528ee |
| Unchanged guards | 311c81d50de789b4a51e3d27ac3ad2d0e0aabb9b07393ce004d34fdd1c822af2 |

All 38 current inputs are checked: three deliberate changes and 35 unchanged.
Effective controls flip every input, text reads, six real in-file code/symbol/
caller/math/coefficient locations and all before/after captures. Only the three
exact known changed inputs are inverted for historical gates; unknown/corrupt
inputs are not mapped. Four preceding installed checks and one explicit
historical provider-boundary check pass, embedding earlier caller/image gates
and freshly validating all 801 archive files. Current image and actual connected
chains never use that inverse.

Fresh converted counts: total **5,501/6,044 (91.02%), bytes 86.04%**; Game
**4,828/5,323 (90.70%), bytes 85.41%**. Byte-exact C numerators are unchanged:
total **3,562/5,501 (64.75%)**, Game **2,889/4,828 (59.84%)**; different **1,939**,
zero drift. Those percentage changes come from removing one false C stub,
**not new C matching credit**. Init and Debugger remain unchanged. README changes
only the affected aggregate rows. The known duplicate generated_12D630 recipe
warnings remain; no warning-free-project claim is made.

## Banking And Next C Work

Bank tools `18698b3` before the consumer pin/source/docs. Shared tools checks,
six-file standalone syntax and the three ROM-free checks pass. Preserve the
independent `ddbdd16` mirror HEAD and all 612 initial dirty fingerprints before
copying only six absent owned paths; all 618 final fingerprints are verified.
Seven documents / 4,931 relative Markdown links validate with none broken.
No mirror commit/reset, push, host source/build/launch, save/configuration or
frozen Release action. Claude budget/calls: zero.

Full `graphify update .` refuses 19,285 nodes against 41,067 curated nodes,
retaining 19,398 nodes from 2,972 excluded-but-present files. Preserve the
fail-closed result and await the incremental commit worker; never force it.

## Post-Bank Verification

Consumer `51eb0dad` banks the original adapter, tools `18698b3` pin, corrected
README aggregates and working documentation. All 14 post-bank checks pass in
93.223 seconds, including actual finite math/consumer chains, the independent
complete current image, historical gates and fresh 801-file archive hashes.
All 38 installed input states remain pinned: three deliberate changes and
35 unchanged inputs. The normal ELF/progress build is up to date.

Both active checkouts are clean before this receipt. All 618 final mirror
fingerprints and independent `ddbdd16` HEAD stay fixed, including all 612
initial fingerprints; the six owned copies remain exact. The source commit's
incremental graph worker completes at 41,075 nodes / 81,169 edges / 3,862
communities, without forcing the smaller full scan. No push, host/Release
operation or new C-match credit. Keep the full C-source/Game goal active.

## Next C Target

Return to the whole additional-C queue at `func_1516F1C0` in
`generated_19A8B0.c`, confirmed still a zero-return stub. The archive has a
large factory-call wrapper; its older isolated screen records 78 emitted /
78 retail words and two differences. That old survey is a lead, not adoption
proof. Freshly compile the complete current owner with recovered argument
widths/prototypes, then qualify packet, delay-slot, owner and linked-image gates.
The wider failed-source/binding queue, handwritten Init hardware routines and
unmatched `func_1510BF60` remain open. Do not mark the full C goal complete.
