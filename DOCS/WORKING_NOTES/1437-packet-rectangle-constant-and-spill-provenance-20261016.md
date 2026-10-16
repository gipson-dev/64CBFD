# Packet Rectangle Constant And Spill Provenance

Date: 2026-10-16. Consumer predecessor **c74e44f2**, tools predecessor
**aff42ac**. Continue **func_15095D34** in
`conker/src/game/generated_C1D70.c`, VA **0x15095D34..0x1509629C**, ROM
**0xC31E4..0xC374C**. This is an **evidence-only checkpoint**: no production
C, guard, compiler profile, shared helper, ELF or progress CSV change, and
**no new byte-matched function**. The wider Game goal remains active.

## Frozen Production Boundary

Retain Note 1436's **346 words / frame 0x88 / 71 pointwise differences**,
literal **104-word prefix** and **91-word suffix**. All remaining differences
are in the **151-word middle**, offsets **+0x1A0..+0x3FC**. Revalidate every
one of the new experiment's **100 immutable before inputs** and live inputs.

```text
ELF    cfa4611d4151c21bc820ea5a16ec2bfcf91d0daf897259469a8a314a0e80791f
owner  b145ca1b2ddd80f63ae8ea7113cf738e0758d7cf0fbc69a399622d39ed6ef90b
guards 197a60801a08f0db3ed2afa2461b3d692bd215cf21f78870609589fb06df9c41
```

Keep transient screens/captures under ignored
`conker/build/game-packet-rectangle-middle/`. The experiment has no production
installation API; SELECTED remains INITIAL, the existing 71-difference body.

## Complete-Owner Screens

Revalidate **45 measured source forms**, their complete-owner sources,
raw object fingerprints and independently linked words against retail.
Changing constant spellings, signedness, safe wide arithmetic, flip assignment
order, byte-test caching, animation delta shape and branch layout yields no
better candidate. Representative results:

| Form | Words | Frame | Differences |
| --- | ---: | --- | ---: |
| Selected production body | 346 | 0x88 | **71** |
| Mixed integer-32 product / float outer constant | 347 | 0x88 | 226 |
| Mixed outer constant control | 347 | 0x88 | 226 |
| Inline height | 352 | 0x88 | 296 |
| Unsigned-halfword animation delta | 348 | 0x88 | 114 |
| Linear flip/goto, mixed constant | 346 | 0x88 | 123 |

Equal counts are not identity. Several signed/shift source controls also have
undefined-C limits; none is eligible merely because it emits the same words.
The production body retains safe unsigned wrapping arithmetic. Do not install
the shorter/worse branch control or manufacture frame padding with locals.

## Qualified Compiler Capture

Reuse the existing actor-callback frame and text-measurer UOPT observation
helpers without changing them. Compile the complete owner first. A narrow
diagnostic isolation removes the other 18 functions using the existing balanced
function-span parser; a same-length parser-only view recognizes pointer returns
without changing compiled spelling. Require isolated versus complete-owner
target words, relative bindings and all pools to be identical.

The new wrapper locks all four cc/cfe/uopt/ugen fingerprints. It records actual
CFE completion before UOPT reads its output, actual UOPT completion before
UGEN consumes that output, initialized descriptor/type table hashes, fired
frame observation, successful child/driver exits, source identity and complete
normal/traced object, relocation and pool identity. Known raw-body/binding
signatures reject two identically corrupted objects, not just unequal pairs.

Qualified fresh captures, all exit zero:

```sh
python3 -m tools.experiments.game_packet_rectangle_compiler_trace --candidate selected --name qualified-selected
python3 -m tools.experiments.game_packet_rectangle_compiler_trace --candidate mixed-product --name qualified-mixed
python3 -m tools.experiments.game_packet_rectangle_compiler_trace --candidate selected --name final-selected --mode 5
python3 -m tools.experiments.game_packet_rectangle_compiler_trace --candidate mixed-product --name final-mixed --mode 5
```

These labels are already used. Revalidate receipts rather than rerunning them;
the wrapper rejects existing receipts and paths outside `conker/build`.
Only `compiler-qualified-selected`, `compiler-qualified-mixed` and
`allocation-final-{selected,mixed}-5` are acceptance evidence. Earlier preserved
captures lack the final gates and are not substituted for these receipts.

| Form / Stream | Bytes | Records | SHA-256 |
| --- | ---: | ---: | --- |
| Selected CFE | 26,392 | 1,355 | a1a4c16b372948e327a80d9c513ce012546b812ab066670b02a0fc4d5bff0ad1 |
| Selected UOPT | 24,168 | 1,205 | bab874866ac9b59af2f0903aa6f9c0ae8b3168864efc0fa75a44bab967b00c76 |
| Mixed CFE | 26,424 | 1,355 | 946de3a755fa15345f1f4f307a99a883e44e2daa559ff4b8538044a003415078 |
| Mixed UOPT | 24,232 | 1,205 | fd1847353d6a7ab8ec1c67635ce5ad277f26b43bbf01b11d042bdac04f912857 |

Both UGEN captures observe frame-watch installation at frame/locals/temp zero,
then the frame write at **136/136/0**, with an empty observed pool. No named
`f_temp_*` events fire, but those specific probes lack a positive control here:
do **not** infer that every UGEN spill path is absent. The stronger measured
fact is that the relevant storage already exists in captured UOPT output.

Mode 5 is an opt-in diagnostic on newly owned compiler processes, not a purely
passive trace: the reused helper supplies a runtime diagnostic stream buffer
and suppresses the real-number printer. Both gates fire during the actual
UOPT lifetime, cleanup precedes driver completion and emitted code is unchanged.
No compiler files are modified. Real costs/timings are **not valid**. Mode 6
is not exposed by this wrapper. Per-run dump hashes are receipt-specific;
temporary filenames/diagnostic serialization can vary.

## Measured Causes

**Constant sharing:** selected CFE contains four `32.0` real payloads. The
mixed-product integer `32` folds to `3.2000000000000000e+01`, distinct from the
outer `32.0` text. Selected UOPT has `rldc` real records for `2.0`, `32.0`,
`1.0`; mixed UOPT additionally retains two `ldc` records with the scientific
text. This explains the separate constant roles/load multiplicity. It does
**not** establish the original source spelling or match the 347-word control.

**Independent GPR spill:** selected and mixed mode-5 dumps have 35 variables
and respectively 72/73 allocation constraints. Both give the flag cache
**expression 123, abstract color 12, forbidden 1..11**; converted fractional-T
is **computed `ucvt` expression 137, color 0, forbidden 1..12**. Color zero
is an allocator result, **not hardware register zero**. The source fractional-T
local at M-60 / expression 128 is eliminated; the computed conversion is the
actual candidate. Merely adding a register hint to that local is not a fix.

CFE declares **116** M bytes; UOPT declares **132** and already emits the
fractional-T conversion store/load at **M-128**. That home is later reused
for clip-X; quarter-Y uses **M-132**. In frame 136 these are SP+8 / SP+4,
with the Y low half at SP+6. Six actual macro accesses remain wrong:

| Function Offset | Current Access | Retail Home |
| --- | --- | --- |
| +0x334 | SW SP+8 | SP+0xC |
| +0x348 | SW SP+4 | SP+8 |
| +0x34C | LH SP+6 | SP+0xA |
| +0x380 | LW SP+8 | SP+0xC |
| +0x3C8 | LW SP+8 | SP+0xC |
| +0x3F8 | LW SP+4 | SP+8 |

Retail spills the flag word at SP+0 at +0x218. Current code instead spills
fractional-T to SP+8 at +0x23C and reloads at +0x288. These observed differences
persist with the mixed constant; FP text alone cannot recover the flag copy.

## Validation And Limits

All **12 diagnostic tests pass in 15.687s**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_packet_rectangle_compiler_trace -v
```

They revalidate both qualified compiler/allocation pipelines, raw stream/table
and four-engine fingerprints, normal/traced objects, exact constant payloads,
M homes, allocation witnesses and all 45 complete-owner screens. Negative
controls remove/reorder fired stage markers, alter sources/streams/tables,
corrupt both objects identically, change bindings/pools, and remove allocation
gates with the log hash updated. All 100 frozen-input corruptions are rejected;
all 100 live inputs and the unchanged production 71/104/91 boundary pass.
The final focused live-input/body check passes again in **0.595s**, and all
five new documentation-index links resolve before the consumer commit.

Both tools copies have byte-identical new files, pass Windows syntax and all
eleven shared padder tests; `make tools-check` passes. Fresh read-only official
progress measurement, from `conker/`, exits zero:

```sh
python3 ../tools/match_progress.py progress.csv build/conker.us.elf conker.us.bin --version us --objdump mips-linux-gnu-objdump
```

No production guest rebuild or native/gameplay suite is rerun. Note 1436's
15 semantic tests / 125.719s remain **prior unchanged evidence**, not fresh
qualification. This checkpoint proves compiler provenance within the stated
gates, not later full private/fault state, hardware FCSR or natural gameplay.

## Next Work And Banking

Continue **the same 151-word middle**. Investigate UOPT computed-expression
retention/priority and the semantic use graph needed to keep fractional-T live
while recovering retail's flag spill/copy. Then close branch scheduling and
the six macro-home accesses under all existing semantic/private/image gates.
This is the next hypothesis to test, not a recovered source solution. Avoid
more speculative UGEN scratch-pool probing, unused locals, physical-register
bindings or bulk instruction guards. Broader Game/additional-source work and
inherited-stack C deferrals remain open.

Fresh totals remain **Game 2,922/4,828 (60.52%)**, **total 3,595/5,501
(65.35%)**, different **1,906**, drift **0**. Init 492/492 and Debugger 181/181
converted routines remain exact; conversions 5,501/6,044 (91.02%), bytes
86.04%. Root README already has these same verified figures/date and remains
unchanged. No progress is inferred from diagnostic work alone.

Tools **9533be8** commits the three new experiment/trace/test files before the
consumer documentation/pin commit. Preserve old mirror HEAD **ddbdd16** and
all **815** original dirty-file hashes; add only the three absent files for
**818** dirty paths. Do not commit/reset that mirror. Wait for the incremental
consumer graph hook; no full scan or purge of retained excluded nodes.
Claude calls: **zero**. No push or host-port/frozen Release build, modification
or launch occurs.
