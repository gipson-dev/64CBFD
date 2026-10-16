# Scaled Random Spray Guarded Byte Match

Date: 2026-10-15. Resume from consumer **21838ece**, tools **bce2d08**,
both initially clean. Tools **de7c6d8** is committed first. Restore the
complete **func_151709B4**, matching its **119-word retail slot** after
checked normalization. It is **not a raw compiler match**. Keep the full
Game/additional-source objective open.

## Steps

1. [x] Audit the complete original, additional source, typed direction/factory definitions and three actual caller windows.
2. [x] Recover the seven inputs and all 31 physical factory words, including scaled values in all three escaped output objects.
3. [x] Screen coordinate widths, real local layouts and FP expression spellings; recover the original frame/homes without artificial padding or fixed registers.
4. [x] Check the arbitrary-index loop obligations with explicit finite/framed assumptions, then qualify bounded literal/public, native, fault, caller, rebase and current-helper behavior.
5. [x] Replace only the target stub, append all 118 closed guards, rebuild and account for every ELF/input byte.
6. [x] Pass all 15 final checks, preserve the older mirror and bank tools before consumer source/pin/docs. README changes only aggregate rows.
7. [ ] Continue func_15170B90 and all remaining Game/additional-source, unconverted-caller, inherited-stack and raw-matching queues.

## Recovered Contract

**func_151709B4**, VA **0x151709B4**, ROM **0x19DE64**, has **118 body
instructions / 472 bytes**, followed by **one padding NOP** in its **119-word /
476-byte slot**, ending at 0x15170B90. Its frame is **0xF8**. The owner is
[generated_19A8B0.c](../../conker/src/game/generated_19A8B0.c).
Retain its address name and disclose normalization in its descriptive comment.

```c
void func_151709B4(s32 x, s32 y, s32 z, s32 count, f32 scale,
                  u8 flags, s32 context);
```

The coordinates arrive as **word values** from float-to-integer truncators;
narrow them for the signed-halfword factory inputs only on the positive-
count path. Original caller captures include **50000, -59980 and 32768**
before that narrowing. Count <=0 performs no provider call and does not
read the scale, flags or context stack homes. Positive paths snapshot the
coordinate projections, count, scale, doubled scale, byte flags and word
context before the loop.

For each record, call **func_15170034(0x40, &xOut, &yOut, &zOut)**. The
objects reside at frame **0xF0 / 0xEC / 0xE8**. Scale X/Z by the original
scale and Y by its precomputed double, truncate the values and **write all
three scaled floats back into those same escaped objects** before the
factory. These stores are observable by a provider that retains the output
pointers, even though the factory receives scalar arguments.

The complete **func_1516D4E8** packet contains signed coordinates; type
0x2F; color bytes 255 at indices 5/6/7/9; mode 7 at index 12; full signed
X/Z high words and fractional low bytes at 13..16; zeros at 17..22;
extents 512/512, value 40 and truncated vertical word at 23..26; zeros at
27/28; byte flags and full-word context at 29/30. Preserve the physical
upper bits separately from the factory formals' byte/halfword projections.

The unchanged additional source at
`Another Source/CBFD-Recompiled/conker/conker/src/game/game_19A8B0.c`
is reference-only. It inserted a converted float ahead of shifted factory
arguments and lost the final context. Correct the entire packet against
assembly rather than copying that source as-is.

## Compiler And Normalization

The first corrected halfword-coordinate body emits **121 words / frame
0xE8**, including coordinate processing before the count gate and extra
incoming-home stores. Word coordinate inputs recover **118 words / frame
0xF8**. Moving the real index declaration ahead of the float locals recovers
all three original output homes. Nineteen argument/expression/layout screens
were measured; addressed-coordinate, wider-local and in-place variants are
not adopted. No artificial local, volatile workaround, forced register,
extra argument, shared header or production profile change is introduced.

Selected raw C still has **47 real word differences**. The experiment's
length-inclusive comparison reports **48** because it also counts the
retail padding NOP outside the 118-word C body. Do not present that padding
as an omitted compiled operation or inflate the function symbol to 476.

The [experiment](../../tools/experiments/game_scaled_random_spray.py) pins
the complete raw stream to SHA-256
`4b4cb351904ac7241612626c230982855308fa4b49f8d0e1d04b1c373e561b7a`
and both JAL relocations. A closed permutation retains every compiled
operation exactly once. Change register fields, independent scheduling and
the vertical multiply's commutative operand order. Frame, private homes,
opcodes, constants, branch positions/spans and both call bindings stay fixed.
Append **118 guards: 71 identity fingerprints and 47 transforming rows**;
there are no inserted or omitted operations. The actual padder/assembler
retains the final alignment NOP and the **472-byte function symbol**.
The entire previous guard manifest remains a byte-identical prefix.

The [loop checker](../../tools/experiments/game_scaled_random_spray_proof.py)
checks both empty entries and arbitrary-index continue/exit obligations.
Its invariant is **0 <= index < count <= INT_MAX**, so the signed increment
is defined. Check all 31 physical words, exact output-object identities,
pre-factory scaled observations, arbitrary provider changes to escaped
objects and all **31 legal factory argument-home clobbers**. Snapshot roles,
saved state and continuation predicates remain equal. Six effective
dependency negatives fail; a legal multiply-operand commutation passes.

The numeric lemma is **finite non-NaN multiplication commutation**, not an
IEEE solver result. Products/conversions must be finite and representable;
memory is ordinary/nonvolatile, and providers cannot inspect unpassed GPRs
or unescaped parameter/saved homes. The first direction call initializes
all outputs; later valid providers may retain or partially update them.
No raw private-RAM, FP-environment/FCSR, NaN-payload, fault-order or hardware
exception equivalence is claimed. Literal normalized-retail tests below
are separate from that conditional raw-value argument.

## Final Qualification

All **15 final tests pass in 100.717 seconds**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_scaled_random_spray tools.tests.test_game_scaled_random_spray_installed -v
```

- **3,000 complete loop cases** compare normalized/retail literal word-model state and independently check raw/public packets and escaped observations. Cover counts -3/0/1/2/5, zero/positive/negative scale, flags/high coordinate words, two phases, partial direction writes and factory output poisoning. All **118 body instructions** execute; the separate padding NOP is not falsely credited as executed. Incoming-home overwrites are guest-only, outside the native framed contract.
- **1,260 fired memory-fault prefix pairs** compare complete literal model state. Empty counts, including INT_MIN, skip all three stack inputs even when unmapped. Four invalid-conversion/NaN/infinity singletons compare **normalized versus retail only**; they are not raw-C or native acceptance cases.
- All **118 raw-word flips, 118 production-padder word flips and 118 padder binding flips** fail, as do both external binding changes and a changed guard predecessor. All 29 owner neighbors, sizes, relative relocations and pools are unchanged.
- **Nine compiled guest negatives** fail: skipped count-one, short loop, wrong direction flag, undoubled Y, wrong Z source, swapped coordinates, missing escaped writeback, wrong type and byte-truncated context.
- **Native32 O2/O0, 1,048,576 cases each**, cover all 65,536 bit patterns per coordinate projection, all byte flags, full-word context, empty/positive loops and the legitimate escaped-object provider contract. Use the correctly typed seven-argument pointer, compare every formally projected factory field and all three scaled float observations, and enable selected-C UBSan traps. All nine compiled native negatives fail effectively. Do not infer physical upper-bit, fault or FCSR acceptance from native results.
- **Three independent original/raw/normalized rebase sets / 48 cases** verify both call bindings, full original body/padding and public behavior. Literal equality is normalized/original, not raw scratch-register equality.
- **Three original caller windows / six captures** verify the physical seven-input ABI, full word-coordinate truncations, counts 4/10, scales 300/2000 and the flag/context tail. Complete callers are not claimed restored.
- **640 connected cases** execute **217 actual current helper words** from direction, cosine/sine, small factory and allocator, plus the real 65-float table. Independent references check packets/escaped floats through allocation failure and counts up to ten. RNG, heap and registration remain opaque; this is not full gameplay qualification. The table's unique matching ROM location is **0x23ECE0**, VA 0x8009A220.
- All **801 archive fingerprints**, **69 frozen/live input gates** and capture/manifest/successor/image corruption controls pass. The two caller pages extend the prior 67-input set in a new match-phase directory; preserve the initial screen captures without rewriting them. Both copies pass Windows syntax and all eleven shared WSL padder checks; `make tools-check` passes. New target suites run in the consumer layout.

Initial gates correctly rejected qualification mistakes: the function-symbol
expectation incorrectly included the padding NOP; inspecting its actual
472-byte symbol and identical 476-byte slot resolved that distinction. The
first native fixture faulted at an unaligned **MOVAPS** in freestanding
`_start`; GDB/objdump confirmed ESP alignment, and the fixture now uses the
existing native-test `-mstackrealign` convention. An initially guessed trig
ROM offset failed; locate the complete 260-byte table uniquely in the ROM
and rerun with 0x23ECE0. These corrections affect qualification, not guest
compiler flags or production behavior. The final suite reruns every gate.

## Whole Image And Banking

The rebuilt guest ELF matches its **initial pre-install prediction**, no
amendment: **365 changed bytes** within the **476-byte target slot** and
symbol extent **12 -> 472**. Every other ELF byte and all **66 unaffected
inputs** are fixed; **no metadata exclusion or symbol-order exception**.
Protected layout remains **189,088 bytes / 720 owners / zero differences**.

| Input | SHA-256 |
| --- | --- |
| ELF | 2721ebd301a677eedb468dbebcd2cef9d685dfd313aded8c4785177d8a54afb4 |
| Owner | 5d185b496b158910ff0a7b1f1fc69077602d2abb9f9bb2db4126b77c443456c6 |
| Guards | dc3969cde15479bc33254ab470242a65a80496e14fee28d7512ec2bb54d40399 |

The shared guard prerequisite causes a wide guest rebuild. It exits zero
with inherited compiler and duplicate generated_12D630 recipe warnings;
the target qualification has no diagnostic or pool. Preserve the existing
CSV CRLF-prefix/LF-append working-copy behavior, not a global rewrite.
Checkout newline normalization requires explicit fixture requalification.

Tools **de7c6d8** contains only six new experiment/proof/oracle/checkpoint/
test files. The older mirror keeps HEAD **ddbdd16** and all **741 initial
dirty-file hashes**. Copy six absent owned files hash-equal, giving **747
final paths**; only those owned additions receive subsequent qualification
edits. Do not reset or commit that independent checkout.

Fresh official matching: **Game 2,911/4,828 (60.29%)**, **total
3,584/5,501 (65.15%)**, different **1,917**, drift **0**. Init 492/492 and
Debugger 181/181 remain exact. Conversions stay 5,501/6,044 (91.02%), byte
coverage 86.04%. README changes only its two matching aggregate rows;
function narrative remains in the documentation.

Claude budget: **zero calls**. No push, emulator/gameplay acceptance or
host-port/Release action. Use the normal incremental Graphify commit hook
and preserve excluded-but-present nodes, not a forced smaller full scan.

Next **func_15170B90**, VA **0x15170B90**, ROM **0x19E040**, **820 bytes /
205 words**, frame **0x120**, in generated_19E040.c. Its return delay word
at 0x15170EC0 ends directly at the next function 0x15170EC4. Fold this
checkpoint's three successor hashes into a fresh experiment and audit its
caller ABI and complete body before adopting additional source. This does
not finish generated_19A8B0.c: **func_1516D400** and the inherited-stack
**func_1516FE1C** remain open, along with every broader Game/additional-
source and raw-matching queue.
