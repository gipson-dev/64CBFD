# Random Packet Burst Direct Byte Match

Date: 2026-10-16. Resume from consumer **08a19623**, tools **a9f3606**,
both initially clean. Bank tools **baff8d3** before the consumer. Continue
[Note 1427](1427-table-debris-direct-byte-match-20261016.md) by replacing
**func_15171200**'s zero-return placeholder with complete semantic C.
All **256 retail words / 1,024 bytes** match directly, frame **0xE0**,
packet **SP+0x7C**. **No target instruction guards, inserted/omitted words,
new compiler profile or Makefile change.**

## Steps

1. [x] Freeze the actual source, tools, ELF, original caller/data/assembly and reference boundaries; reuse the existing packet and compiler/oracle helpers.
2. [x] Audit all fourteen arguments, signed and unsigned RNG uses, count gate, escaped packet fields and the word-to-byte duration conversion.
3. [x] Recover the original length, frame, homes, saved-register roles and schedule with genuine locals, literals and initialization order. Preserve all eight owner neighbors and all prior guards.
4. [x] Pass eleven pre-install qualification checks, including independent reference arithmetic, native32, effective negatives, actual caller windows, rebases, literal fault prefixes and connected consumers.
5. [x] Capture a complete full-link prediction before installation, rebuild only the changed owner/guest ELF, and require every predicted byte with no exclusions.
6. [x] Pass all fourteen final target/install checks, refresh official aggregates and README rows, preserve the older tools mirror and commit tools before consumer source/pin/docs. No push.
7. [x] Recover func_15171600's byte switch and full rectangle-emitter ABI in [Note 1429](1429-rectangle-preset-dispatch-direct-byte-match-20261016.md), matching all 127 words / frame 0x40 directly without instruction guards.
8. [ ] Restore original caller func_15169C70 and retain func_1511C638, func_1516D400, inherited-stack func_1516FE1C and the broader Game/additional-source/raw-matching queues.

## Recovered Contract

The original span is VA **0x15171200..0x15171600**, ROM **0x19E6B0**,
with no separate padding word. Retain its address-based name in
[generated_19E040.c](../../conker/src/game/generated_19E040.c):

```c
void func_15171200(s32 count, s32 kind, f32 x, f32 y, f32 z,
                  f32 verticalBase, f32 minimumScale, f32 maximumScale,
                  f32 spread, s32 variant, s32 lifetime, f32 coefficient,
                  u8 flags, s32 context);
```

The initial two integers mean x/y arrive in **A2/A3**, not F12/F14.
Preserve the full-word kind at lookup; only the packet kind/variant and
submit flags narrow to bytes. Context and lifetime stay full words. The
reference narrows kind incorrectly and aliases the actual signed integer
RNG as an unsigned draw; neither error is imported.

Before the positive-count test, initialize fixed fields once, snapshot the
scale range and vertical spread, and compute the scaled base. The emitted
code writes the scaled incoming base only on the positive path. Nonpositive
counts make no RNG, lookup or submit call and do not read x/y/z or the
flags/context homes; they still perform the original other input reads and
packet setup. There is no ring call or actor-flag store.

Each positive iteration makes exactly **twelve zero-argument signed RNG
calls**. Positions, horizontal velocities and spin use arithmetic signed
high halves. Vertical velocity and three scales use unsigned low halves.
The lookup occurs after three position draws, and its asset result is
stored before subsequent RNG calls. Position inputs and scaled vertical
base remain live incoming-home reads; scale range, minimum scale and
normalized spread retain their saved lifetimes.

After the final scale draw, reread the escaped packet's first two scales,
add the third temporary, multiply by the original duration constant and
add 20. Convert through **u32** before byte narrowing. Then write the third
scale in the submit delay slot. Preserve provider changes to fixed fields,
earlier packet values and the six reserved bytes rather than resetting the
packet on each iteration.

## Direct Compiler Recovery

The first candidate has the correct 256-word length but frame **0xD8**,
154 differences and the wrong literal order/last literal bit. Real
declaration, parameter-lifetime and statement-order screens recover frame
**0xE0**, packet **SP+0x7C**, and reduce differences **51 -> 21 -> 14 ->
6 -> 3 -> 0**. Use real low-half draw temporaries, normalize spread in its
actual parameter, initialize the scale range first and place variant before
kind/control stores. Move the genuine scaled-base calculation before the
count gate. No dummy padding local, volatile workaround, fixed register or
compiler modification is used. No new compiler debugger observation is
claimed in this note.

Retain the source's scale-add expression order: this produces the original
two escaped loads and FP roles. Source mathematical symmetry alone would
not establish the exact compiler schedule or arbitrary NaN behavior.

The compiler's complete pool is:

```text
3DCCCCCD 3E6B851F 3DB851EC BE4CCCCD
36CCCCCD 3F4CCCCD 40D55556 00000000
```

The existing first three table-debris literals stay at offsets 0/4/8;
the new four literals occupy C/10/14/18. The first **28 bytes** equal
retail ROM **0x24BA64..0x24BA80**, VA **0x800A6FA4..0x800A6FC0**.
The final four alignment bytes are not emitted over the next routine's
constant. Reuse **RETAIL_RODATA_SYMBOL := D_800A6FA4**, already installed
by Note 1427. The long decimal 6.666666666666667f emitted 0x40D55555 under
this IDO; the qualified 6.666667f emits the actual **0x40D55556**.

Raw target SHA-256:
`0209fc91d9d4d484ddb791c7e415c6cd550ba3ea973d39d0d87eb5b4524e17ce`.
All 22 relative relocations and 32 pool bytes are locked. The existing
guard manifest is byte-identical and contains no row for this function.
All eight neighbors retain identical raw words, lengths and relative
relocations, including the earlier recovered packet producers.

## Fresh Qualification

The eleven pre-install tests pass in **51.632s**. After installation,
all **14 final tests pass in 88.956 seconds**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_random_packet_burst tools.tests.test_game_random_packet_burst_installed -v
```

- **384 whole paired sequences** cover negative/zero/positive counts, high-bit/full-word kinds, twelve-draw rotations, both stack phases and six provider modes. Compare all 96 packet bytes and literal guest state. Count-gate no-read checks fire. Six further raw-stream cases execute the compiler's own pool before production aliasing.
- **Native32 O2/O0, 512 cases each**, separate translation units and selected-C UBSan, compare all 90 initialized bytes, call counts/order, kind/flags/context widths and provider-seeded reserved bytes. All nine guest/native negatives reject: narrow lookup, unsigned high halves, wrong vertical half, position scale, scale range, duration, fixed-field reset, reserved reset and short count. Native initial indeterminate bytes and special/out-of-range float-to-integer conversions are excluded.
- **24 guest conversion cases** cover ordinary duration, byte wrap, upper unsigned range, negative values, infinity and NaN across three saved FCSR patterns. Check truncation control and FCSR restoration, not complete hardware FP arithmetic/exception flags. Ordinary sequence coverage visits 224 words; unreachable masked-negative correction arms and all conversion paths are not claimed covered by that sequence test.
- **160 fired instruction-fault prefix pairs** compare literal memory/register/event state. This qualifies identical guest instructions, not portable C fault ordering or native FP environment behavior.
- All **256 raw-word, 22 binding and 32 pool-byte corruptions** reject. A wrong production pool alias changes observed packets. Three independently assembled original rebase sets / **48 paired cases** change all callee/constant bindings, including signed-low carries and pool addends.
- **Six original caller-window captures** cover all three func_15169C70 call sites: count/kind 4/0xB, 3/0xB and 2/0xCB, original coefficient/range values, byte flags/context promotion and all fourteen arguments. The current func_15169C70 remains a zero-return placeholder with padded zero-filled call windows; this is not current caller or gameplay acceptance.
- **16 connected current consumer/allocator runs** execute 54 actual words and compare all 96 copied bytes, zero assets and every-third allocation failure. RNG, lookup, heap, registration and bcopy remain bounded or opaque.
- All **82 frozen/live input keys** and capture/initial-prediction/successor corruption checks are qualified. Protect every unaffected source, conversion CSV, manifest and toolchain input. Physical code/callee/data/symbol/string corruption tests reject without metadata exclusions.

Qualification-only corrections: observe provider-seeded reserved bytes
after the first submit; assert the actual OR/JR/NOP padded caller stub;
and separate opaque provider mutations from the real connected consumer,
which does not perform those synthetic writes. Final tests pass after all
three corrections. No production behavior was changed to satisfy a test.

Both local tools copies pass Windows syntax and all eleven shared WSL
padder tests; consumer `make tools-check` passes. No shared helper is
modified. Previous neighbor-suite receipts remain prior unchanged evidence,
not freshly rerun suites. Routine Claude calls: zero.

## Complete Image And Progress

Capture the old link script and padded owner before production edits.
The baseline full link reproduces the frozen predecessor exactly. A second
full link with only the qualified owner selector predicts exactly the
target-slot replacement and symbol extent **12 -> 1,024**. The first complete
prediction is recorded before installation. The production rebuild equals
it byte-for-byte: **793 changed bytes**, **zero** additional serialization
bytes, every other ELF byte and **80 unaffected inputs** fixed, no exclusions.
Protected data remains **189,088 bytes / 720 owners**, zero differences.

```text
before ELF 13196f6d2e9516c7bab5b9b4ad21f68812e40da2ae48b9b8b6a8d75fe1484141
after ELF  0f335a16152a5bed2e84ed2061e240b0bbd063130b761f6228bb42e7ebe7609e
after C    6647ef44eeb6ffda08b8fa5779240eef4d17686647502a93fe897da263a48533
```

Fresh official measurement: **Game 2,915/4,828 (60.38%)**, **total
3,588/5,501 (65.22%)**, different **1,913**, drift **0**. Init 492/492 and
Debugger 181/181 remain exact. Conversions remain 5,501/6,044 (91.02%),
converted bytes 86.04%. README changes only the aggregate matching rows.
The existing duplicate generated_12D630 Makefile recipe warning recurs;
the build exits zero and it is unrelated to this source-only recovery.

Tools **baff8d3** contains six new experiment/oracle/native/checkpoint/test
files. The older tools mirror stays at **ddbdd16**; preserve all **771**
initial dirty-file hashes and add only these six previously absent files,
ending at **777** dirty paths. Do not commit or reset that mirror. Bank
the consumer's C/tools-pin/docs separately, with no push. Its normal
incremental Graphify commit hook owns the graph refresh; do not force a
full scan or drop retained excluded nodes. No host build/launch or frozen
Release action occurs. The broader matching goal remains open.
