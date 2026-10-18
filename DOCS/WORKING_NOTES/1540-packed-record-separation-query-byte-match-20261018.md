# Packed Record Separation Query Byte Match

Date: 2026-10-18. Consumer predecessor **7b2c768b**, tools predecessor
**e1ce81b**. Restore **func_150882E4**, owner `generated_B3020`, VA
**0x150882E4..0x150883B0**, ROM **0xB5794..0xB5860**. The wider Game matching
goal remains active; this is one completed function.

## Semantic Recovery

Replace the false zero-return placeholder with **u32(u32 recordIndex,u32
idOffset)**. These are full o32 word arguments/results: the observed command
caller passes both loaded words unchanged and forwards the entire result.
Capture table D_800872A0; return sentinel0x10 if null. Otherwise read signed
count D_800D2398 and own signed ID byte+0x29, even when count is nonpositive.
Add the ID to the offset modulo2^32; do not narrow the requested ID to a byte.
Scan 0x84-byte records in order and select the first equal signed ID at a
different slot. Signed count<=0 or no eligible match returns0x10.

For a match, quantized values combine signed halfword+0x24 times16 and
truncation of float+8 times16. Preserve the original ordered subtraction:
own integer part +own truncated float -candidate integer -candidate truncated
float. Unsigned word operations preserve subtraction, magnitude and packing
wrap, including the 0x80000000 magnitude. Return `(magnitude<<8)|slot` as a
complete word. The original index is dead once the match is accepted; source
reuses that argument as the arithmetic result. No stores or helper calls.

Native C pointer/index qualification uses real valid record objects. Float
casts are qualified only for finite scaled values representable as s32;
unsigned arithmetic does not make invalid float-to-s32 conversion portable.
The signed view used by the sign test follows this o32/two's-complement ABI.

An indexed cursor source recovers the exact **51-word/no-frame** control flow,
read order and float operations. Fifteen raw words still differ in register
allocation. No direct/guard-free match is claimed. Consulted alternate-source
draft has incorrect s32 accesses at byte/float fields; it is not imported.
Keep the original address-based symbol and a short semantic source comment.

## Register Normalization

**Fifteen expected-word guards** change only GPR roles. At word15, the incoming
offset is last used and its wanted-ID result moves to A1; word16 starts the
cursor in A2. Exchange raw A1/A2 roles for words17..47. Arithmetic temporaries
in words27..37 use the original dead input-index register and retail temporary
allocation. In particular, T9's own-halfword role is dead after word28, while
its candidate-float role starts only at word34; do not rename both lifetimes
as one. Packed-result temporary routing changes only words39..43.

The bounded opcode-aware transformation equals all51 retail words. All four
bindings are fixed and untouched by guards. No branch, branch displacement,
delay-slot order, arithmetic opcode, memory operation, literal or instruction
count is substituted. No inserted/omitted words, assembly fallback, compiler
profile or Makefile change. Existing O2/g3/MIPS2/o32 with compiler-only no-unroll
and ordinary GLOBAL_ASM processing remains intact.

Raw/normalized complete interrupted scratch states are not asserted equal:
the transformation deliberately reuses dead caller-saved roles. Functional
results/read traces and saved ABI state agree. Normalized/retail instruction
bytes and complete bounded fault states agree.

## Qualification

New tools: `experiments/game_record_separation_query.py` and
`tests/test_game_record_separation_query.py`. Ignored artifacts:
`conker/build/game-record-separation-query/`. Fifteen explicit hashes pin
owner/ELF/guards/ROM/assembly, build/symbol/header inputs, four prepared compiler
components and original/production caller sources. This is the declared input
closure, not all unlisted transitive dependencies.

All **seven pre-install tests pass in42.928s**; all **seven installed tests
pass in59.943s**:

```sh
python3 -m unittest tools.tests.test_game_record_separation_query -v
```

**6,402 three-way raw/normalized/retail guest cases** cover all256 count bytes,
signed ID boundaries and full-word offsets, own/outside-scan indices, first/
middle/last/multiple/self-only/no matches, both stack phases and numeric wrap
profiles. Verify complete allocated memory remains unchanged, exact ordered
read traces, return word and saved ABI state. All51 words execute, including
the null-table return. No opaque helper behavior is needed.

Native32 **O2/O0 with UBSan** each pass **115,457 cases**. Cross all256 count
bytes with match/ID/height patterns, extend full-word offsets and numeric
boundaries, and cover every65,536 own-halfword pattern. The independent
reference decodes float bit patterns to scaled integers instead of repeating
the source casts. Native records contain real aligned float/halfword/byte
fields, and every byte of the complete128-record object is compared before/
after each call. Globals and complete return words are also checked. Finite
boundary cases include valid scaled s32 minimum and the nearest valid upper
float, signed zero, negative fractions, word subtraction overflow and packing.

Nine unsigned-count/unsigned-ID/narrow-wanted/include-self/stride/float-scale/
integer-scale/magnitude/packed-slot controls change observable return values
in guest tests and exit with explicit status23 natively. A seeded negative-
count case contains a matching first row, proving the count control through
a valid result difference rather than an out-of-bounds walk. Crashes do not
count. The initial corpus-count assertion and unused harness helper were
corrected; two null cases complete instruction coverage. All prior guard rows
are retained in negative manifests, mutating only one target expectation at
a time and requiring the failure to identify this function.

Nine independently linked original/raw-C/actual-padded objects across three
code/data placements pass **288 three-way rebased cases**. HI16/LO16 carry
boundaries exercise all four bindings. **264 public target-access fault
prefixes across54 states** preserve memory/read prefixes for all three bodies;
normalized/retail complete register/float/event/PC/delay state agrees. The raw
dead scratch values are intentionally not claimed identical. Five nonfinite/
out-of-range inputs are rejected by the bounded model, not assigned invented
N64 results. This is neither FCSR emulation nor hardware MMU/portable C fault
equivalence. All51 raw words, four bindings, fifteen guard expectations,
**30 live/frozen input mutations** and nested historical views are gated.

## Observed Caller

Retail aligned-word scan finds one exact JAL at ROM0xCB9D4/VA**0x1509E524**,
in **func_1509E3DC**, owner `generated_CB3D0`; no exact target-pointer/J word.
That does not exclude computed/encoded indirect references. Its containing
production C parent remains a zero-return stub, not claimed restored.

**144 paired actual bounded caller windows** execute command+8 into A0,
command+0xC into A1 in the call delay, the complete raw/normalized query and
the common return epilogue. Check forwarded arguments, entire V0 result and
restored stack pointer. This is original entry0x1509E520 and common return
0x1509E62C, not execution of the whole command dispatcher/gameplay path.
No parent or shared-header edit.

## First Prediction And Build

Before production edits, freeze the first complete **3,257,636-byte ELF**,
owner-source successor and guard successor from one substituted padded owner
in a copied current linker script. Original fixtures and first successors
stay immutable. Install the complete source and fifteen guards with the
existing scoped build:

```sh
make -C conker -o Makefile -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_B3020.c.o build/conker.us.elf progress.csv
make -C conker -o Makefile -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

Actual whole ELF equals the first prediction: **154 changed bytes =153
target-code bytes +one target symbol-size byte**, file offset2882683. Target
extent changes12->204, with **zero metadata exclusions**. Audit all **6,057
bodies/addresses** and canonical symbol definitions: only this body and extent
change. All **72 raw owner neighbors**, pools and relative bindings stay fixed;
actual padded owner matches qualification. The complete old guard prefix is
unchanged, with fifteen appended rows. A mechanical formatting pass changes
only the new rows' LF terminators to the predicted CRLF; their values and
every old prefix byte were already identical. No broad newline normalization.
The Makefile stays fixed; Game data remains **189,088 bytes /720 owners /zero
differences**. No new compiler diagnostic; existing duplicate12D630 recipe
warning remains unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Complete installed ELF | `40f55fff85c81f794705962d4e5311ff4ad2bcdf29dbc5462036515135b00eb2` |
| Complete owner source | `eaee25d9babb94f5ae8ba8f6ffa9476c9118ff81749c5ef74b626a1bbf2ec208` |
| Raw target | `da80a9bd436b7cc0ed9fbea44ab74192c3ba9bae8f93ed1ba6664754b2d38b65` |
| Linked target | `94475ec579fc2033eaa9fdfbf20d7914f749f16846559803f7b764fb3b1d81b3` |
| Guard successor | `5beb07aa1970717fe8fcb1aef89c3381dc51ceb30cc35f0cc7ce9ee24edbc91a` |
| Unchanged guard prefix | `8f709f6c1cb03108c0f1e6f7b460e624d76f29734c97ed5fe9739f411f2046a1` |

The exact three-member owner/ELF/guards historical view is serial/non-nesting
and rejects unknown/mixed states, retaining physical raw reads. Freeze this
new physical baseline directly for later work; never relax old fixture/helper
hashes or nest historical readers to accommodate stale tests.

## Bank And Next Action

Tools **3f4b1c9** is committed before consumer source/guards/docs/tools pin.
Both tools copies pass eleven shared padder tests and project-tools smoke;
root tools-check passes. Four Windows ASCII/AST parses and two exact task-file
pairs pass. Preserve standalone mirror **ddbdd16** and all **1,206** initial
dirty hashes, adding only two absent paths for1,208. No mirror commit/reset,
push, Claude call, host or frozen Release action.

Fresh official totals: **Game2,978/4,828 (61.68%)**, total **3,651/5,501
(66.37%)**, **1,850 different**, zero drift. Conversion counts/bytes remain
unchanged. Root README changes only the two aggregate matching rows.

Scoped Graphify refresh: **42,479 nodes /82,547 links /3,976 communities**.
Preserve **19,398 nodes from2,972 excluded-but-existing files**. Only three
line-disambiguated UPDATE_LOG heading IDs move; all three labels and every
other old ID persist. The new note contributes eight nodes. Target/next
definitions resolve to **L411/L438**. Preserve the original graph in the
ignored task build directory; graph outputs remain ignored. No full-scan
purge or graph-history rewrite.

Next **func_150883B0**, same owner, VA**0x150883B0..0x1508855C**, ROM
**0xB5860..0xB5A0C**, **107 words/frame0x20**, current sourceL438. Graph queried
and full retail body read. Audit callers before assigning its four-argument
pointer/output ABI. The routine saves S0/S1 and complete F20/F22 pairs, builds
a directed projection from own-record floats+0x0C/+0x10 and source actor X/Z,
then chooses the strict smallest positive candidate projection below the
initial **10000.0f** limit, D_8009DA00 bits**0x461C4000**. Respect the
signed record/actor IDs, wildcard/nonzero tag filter and byte-wrapped excluded
actor ID derived from source actor+0x124 minus1. Accepted candidates write
record float+0 to output A2 and signed tag+0x2F as a word to output A3, then
produce the selected actor pointer. Null/no match leaves outputs untouched.
Reload table base each iteration, and re-read selected actor ID/count after
accepted output stores; output alias/order behavior needs explicit qualification. Strict float
predicates preserve tie/NaN behavior. Handwritten func_150A76F0, fade gaps,
stubbed parents and wider Game queues remain separate open work.

One aligned retail JAL occurs at ROM0x80EA0/VA**0x150539F0**, original
**func_150538CC** in `game_77AD0`. This parent is retained GLOBAL_ASM, not a
stub: its complete **4,108-byte**0x150538CC..0x150548D8 slot is currently
retail-exact. That byte check is not execution of the whole parent. The call
loads record/direction from stack+0xDC/+0xC0, supplies output pointers at
stack+0xC4/+0xBC, saves F16 at stack+0xCC in the call delay, then restores
F16 and consumes V0 as a pointer. Qualify that saved-float/output/return
boundary without assuming the parent's other callees or gameplay complete.
