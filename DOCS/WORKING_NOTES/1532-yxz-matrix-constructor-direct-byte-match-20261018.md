# YXZ Matrix Constructor Direct Byte Match

Date: 2026-10-18. Consumer predecessor **58d80d9f**, tools predecessor
**29952ff7**. Recover **func_151102CC**, owner `generated_13D350`, VA
**0x151102CC..0x15110360**, ROM **0x13D77C..0x13D810**. This is one completed
ordinary C function; the wider Game matching goal remains active.

## Direct Recovery

The empty void body becomes a typed, commented matrix constructor with named
output and x/y/z angles, one local f32[4][4], and five original helper calls:

1. Build Y rotation directly into the output through func_150A8050.
2. Build X rotation into the temporary matrix.
3. Compose output * temporary into the same output through func_150A7A48.
4. Reuse the temporary for Z rotation.
5. Compose output * temporary into the output again.

The first straightforward source emits all **37 words / 148 bytes /
frame0x68** directly under unchanged **O2/g3/MIPS2/o32**. There are **zero
raw differences, zero guards, no compiler override**, and no source-shape
search. Existing helper prototypes and the matrix/three-float ABI recovered in
[Note382](382-game-indexed-matrix-compose-match-20260928.md) stay unchanged.
All **33** owner neighbors, their relative relocations and owner pools remain
fixed, including the already exact 26-word func_15110360 wrapper.

The actual handwritten rotation helper's formula establishes the axis order;
the product kernel caches the complete right operand and reads/writes the left
operand row-wise. Neither helper nor the handwritten trigonometry slice is
converted or edited. The recovered C describes composition only, not a new
general matrix implementation or original authored source spelling.

## Fresh Qualification

Tools: `experiments/game_yxz_matrix_compose.py` and
`tests/test_game_yxz_matrix_compose.py`. Ignored artifacts:
`conker/build/game-yxz-matrix-compose/`. Fourteen pinned inputs cover the
whole source/ELF/guards/ROM, retail owner assembly, helper ownership sources,
Makefile, symbol anchors and all four prepared compiler components.

All **seven pre-install tests pass in 15.271s**. The actual-helper byte gate
then passes separately in **2.580s**. After installation all seven pass in
**23.455s**; strengthened distinct-angle wrapper coverage passes the complete
final suite again in **19.902s**:

```sh
python3 -m unittest tools.tests.test_game_yxz_matrix_compose -v
```

Fresh tests cover **544 guest cases**: 68 angle-bit triples across low/high
output addresses, two stack phases, and both ordinary/poisoned outgoing homes.
Angles include positive/negative zero, subnormal boundaries, finite extremes,
infinities and quiet NaN payloads. This target forwards their bits; no general
non-finite trigonometry or hardware exception claim is made. Opaque providers
write deterministic complete matrices and poison caller-saved GPR/FPR state.
The private matrix address/extent and five argument tuples are checked against
an independent ordered-call reference, including output guard bytes.

Native32 **O2/O0 with UBSan** each pass all **68** argument cases. Four
wrong-axis/order/omitted-product/destination controls fail observably in both
native and freshly compiled guest execution. The freestanding i386 harness
initially crashed a negative control on compiler-generated aligned stack
accesses; adding **-mstackrealign to this test only** fixes its entry boundary.
No crash is accepted as an effective semantic control, and no production
compiler/build configuration changes result.

Ten connected finite-angle sequences execute the actual retail-exact
**83-word rotation** and **78-word cached-right product** helpers, comparing
their complete output with separately rounded float32 matrix formulas. Their
actual linked bytes are checked against retail before connection. Only the
18 sine/cosine calls per sequence use controlled rounded math providers;
the retail lookup-table trig implementation and full gameplay are not claimed
as newly tested. Twelve real wrapper sequences cover three record indices,
disjoint/in-place-record outputs, two stack phases and three distinct angles.

All **180 target-memory fault prefixes / 18 states**, **37 raw word controls**,
**five relocation-binding controls**, **28 live/frozen input corruptions** and
the nested historical-view control pass. Provider/hardware faults remain
outside the prefix model. Unchanged neighbor-suite receipts are reused, not
called freshly rerun broad regressions.

## First Prediction And Actual Build

Before production edits, a copied current linker script substitutes only the
qualified padded owner and predicts the complete **3,257,636-byte ELF**.
The actual affected-owner/ELF/progress build reproduces that prediction exactly:
**119 changed bytes = 118 target-code bytes + one target symbol-size byte**.
The empty function's st_size changes **8 -> 148**, with zero metadata exclusions.

```sh
make -C conker -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_13D350.c.o build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

The manifest-old flag avoids rebuilding unchanged guard-dependent owners;
the guard manifest itself is unchanged. All **6,057** bodies/addresses are
compared; only the target body changes. Canonical symbol definitions differ
only in its expected extent. Actual production padded-owner bytes and all
relative relocations equal the qualified object, with five fixed call bindings.
Protected Game data remains **189,088 bytes / 720 owners / zero differences**.

| Prepared Artifact | SHA-256 |
| --- | --- |
| Complete installed ELF | `2d972c777f17469fec9c85c80f7ed5951bee4cc9e5b5c4c87706de2b4752a0b1` |
| Complete owner source | `750c682e2aac536d6a48f9b403e4b50d3cd65482c519b2658ea54d7a7bf1f05f` |
| Unchanged guard manifest | `625033dd1c2150ce2edb45badf13c05d09aa95b83a0c2b1231e092105d3fc2b3` |
| Raw target object | `1b696790f7ad55b68eb9bf1dd953d32614a8a717192d3283ad8150f13396a190` |

The exact two-member source/ELF historical view verifies immutable predecessors
and successors, maps only Path readers for research, rejects unknown/mixed
states and nesting, and restores readers on exit. Physical audit retains raw
reads. Older resource/rectangle/movement helpers and fixture hashes are not
weakened; future experiments should freeze the new live baseline directly.

## Bank And Next Action

Tools **61528c9** banks qualification, followed by **236d562** strengthening
distinct-angle wrapper coverage; both precede the consumer source/docs/pin.
Both copies pass eleven shared padder tests and project-tools smoke checks,
with four final Windows ASCII/AST parses and two exact task-file comparisons.
Preserve mirror **ddbdd16**, all **1,190** initial dirty hashes and its history;
add only two absent paths for **1,192** dirty paths. No mirror commit/reset,
push, Claude call or host/frozen Release edit/build/launch occurs.

Scoped graph refresh completes at **42,406 nodes / 82,509 links / 4,053
communities**, preserving **19,398 excluded nodes / 2,972 files**. Every old
node ID remains except three shifted Update Log heading IDs with equivalent
labels retained. The constructor resolves to source line22 and this note has
six graph nodes. No purge or full extraction is performed.

Fresh official totals: **Game 2,970/4,828 (61.52%)**, total
**3,643/5,501 (66.22%)**, **1,858 different**, zero address drift. Conversion
counts/bytes stay unchanged. Root README changes only two aggregate rows.

Next recover same-owner **func_15113180**, VA **0x15113180..0x15113218**, ROM
**0x140630..0x1406C8**, **38 words / no frame**. It clears flag0x40 at +0x6F
in each 0xA0-byte record, then sets it if (+0x6F low nibble nonzero OR +0x70
bit0x04 set) AND +0x38 nonnull. Count D_800DBEF0 and base D_800DBEF4 are
reloaded around writes; qualify possible aliasing before caching either.
Audit direct caller return-value use before choosing a void or count-return
signature: V0 is also the loop index. Preserve the newly matched constructor
and exact wrapper. Handwritten func_150A76F0, both fade gaps, other gate,
additional-source, caller and inherited-stack work remain separate and open.
