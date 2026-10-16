# Randomized Ring Emitter Guarded Byte Match

Date: 2026-10-16. Resume from consumer **4794112d**, tools **b88e200**,
both initially clean. Tools **6f03b11** is banked first. Restore the complete
**func_151718F0**, matching all **193 retail words** after eight checked
temporary-register guards. **This is not a raw compiler match.** Resolve
the typed-ring prerequisite from Note 1423 without pretending the debris
caller or wider Game work is finished.

## Steps

1. [x] Audit the entire original ring, the reference, existing factory types, staged color bytes and all four direct caller windows.
2. [x] Recover the ten-input float/word/byte ABI, three RNG draws per particle, complete 31-word factory packet, empty-count path and field lifetimes.
3. [x] Recover the 193-word / frame-0x140 shape and actual color home using real locals; normalize only eight closed initialization temporary-register words.
4. [x] Pass all 15 final checks, including native32, literal/public packets, fault prefixes, rebases, direct callers, current helper connections and corruption controls.
5. [x] Replace only the ring placeholder, append 193 guards, rebuild and close the complete initially predicted ELF/input audit with no exclusions.
6. [x] Refresh official numbers, keep README changes to aggregate status/date, preserve the older mirror and bank tools before consumer source/pin/docs.
7. [ ] Resume func_15170B90's 205-word / frame-0x120 shape and saved lifetimes using the now-genuine void ring definition. Its debris stub remains untouched.
8. [ ] Continue func_1516D400, inherited-stack func_1516FE1C and every wider Game/additional-source, unconverted-caller and raw compiler-matching queue.

## Recovered Contract

**func_151718F0**, VA **0x151718F0**, ROM **0x19EDA0**, has **193 words /
772 bytes**, frame **0x140**, ending at **0x15171BF4**, with no separate
padding word. Its owner is [generated_19E040.c](../../conker/src/game/generated_19E040.c).
The original callers ignore its return value; replace the false zero-return
stub with the genuine effect-only definition and keep the address name.

```c
void func_151718F0(f32 x, f32 y, f32 z, f32 radius, s32 lifetime,
                  f32 spread, s32 palette, s32 count, u8 flags, s32 context);
```

Copy **three bytes** from D_8008CC20 into a real local object at frame
**SP+0xF4** before testing count. The emitted LWR reads an aligned word,
then SWR stores only the three-byte prefix. Zero/negative count returns
without reading lifetime/spread/palette/flags/context or converting Y.
X and Z incoming homes are written even on the empty path.

For positive count, snapshot radius, truncated signed-halfword Y, float
lifetime base, palette pointer, byte flags and **65535/count** phase step.
Keep X/Z/spread/context homes live at their original read sites, and reread
count after each factory call. All four direct original call sites pass
**palette zero**. Only that selector is within the copied three-byte C
object; nonzero selectors are guest private-stack observations, not a
native-C or host-port supported palette API.

Each iteration calls sine then cosine using **(phase >> 8) & 255**. Form
Z from radius*cosine plus the live Z home before RNG. Split trunc(200*cosine)
into masked high/low bytes. The three zero-argument func_150ADA20 draws are:

- Unsigned low 16 bits times 2^-16, plus 100, retained as a float delay until the factory's integer conversion.
- Unsigned low 16 bits times the live float spread, plus the snapshotted float lifetime, truncated to a word and narrowed to signed halfword extents.
- Low four bits plus 10 for the tail/count byte.

After the draws, form X from radius*sine plus the live X home and split
trunc(200*sine). Submit **all 31 physical func_1516D4E8 words**: signed
coordinates, type 0xD, three staged color bytes, mode 2, X/Z fixed-point
high/low bytes, preset 5, duplicate signed extents, tail 10..25, truncated
delay, zero optional bindings, byte flags and full-word context. Increment
index and phase, then compare index with the live count home.

For stable positive count n, step=floor(65535/n), so k*step stays within
0..65535 for 0<=k<=n. Count above 65535 gives a zero phase step. This is
the arithmetic boundary, not permission to claim that bounded prefix tests
execute arbitrarily long loops.

The reference's unrelated void-pointer local and wide color reads are not
imported. Reuse the existing typed small-factory ABI,
proper func_150ADA20 name and real color struct. The actual color bytes are
**45 53 68**, VA **0x8008CC20**, ROM **0x2316E0**; its complete 64-byte
ELF/ROM window matches uniquely. The real 65-float trig table is at VA
0x8009A220 / ROM 0x23ECE0.

## Compiler And Guard Boundary

The first corrected body already emits **193 words / frame 0x140**, but its
color object is at SP+0x13C and it has nine word differences. Eighteen
real-local declaration screens move that object down to SP+0xF8 while
preserving shape. Naming the actual first unsigned RNG draw and putting
the color object after the real scalar locals recovers **SP+0xF4**. Six
initializer-order screens leave eight or ten differences; adopt the
eight-difference ordering, without artificial padding, volatile workarounds,
fixed registers, invented parameters or production profile/header changes.

Selected raw SHA-256:
`4673c5ad1944b94409da4d02d2ad7740d3aaefedf974492d956da6895dc2ba99`.
It has no diagnostic or data/rodata pool. The [experiment](../../tools/experiments/game_randomized_ring_emitter.py)
pins the complete raw stream and all eight relocation sites. Transform only
indices **44,47,48,50,51,52,54,55**, a closed allocation cycle among temporary
GPRs T4..T9. No instruction is inserted, omitted or rescheduled; no frame,
home, opcode, immediate, FP operation, branch or call/table binding changes.

The expression checker verifies equal live GPR/FPR roles and ordered reads
for arbitrary incoming words, including the palette pointer and narrowed
height. Changed scratch values are dead before the first provider's defined
inputs. Seven effective instruction negatives fail. This is a checked
initialization-region argument under ordinary-memory/O32 provider assumptions,
not a general C/IEEE/FCSR, fault-state or hardware proof. No FP commutation
lemma is needed because the guarded words change only GPR allocation.

Append **193 expected-word guards: 185 identity fingerprints and eight
transforming rows**. The production padder/assembler emits the complete
772-byte symbol and retail body. All **eight owner neighbors**, their sizes,
relative relocations and normalized pools remain unchanged, including the
debris stub and installed rectangle wrapper. Preserve the old guard CSV as
a byte-identical prefix, including its existing CRLF-prefix/LF-append
working-copy behavior. Fresh checkout newline normalization requires explicit
fixture requalification; do not globally rewrite the manifest.

## Fresh Qualification

All **15 final tests pass in 91.919 seconds**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_randomized_ring_emitter tools.tests.test_game_randomized_ring_installed -v
```

- **864 whole-loop cases / 2,592 stream runs** independently check raw, normalized and retail packets/reference behavior, literal final model state, all 31 physical factory words, colors staged once, empty counts and legal outgoing-home clobbers. Incoming parameter-home poison is guest-only, outside the native framed contract.
- All **182 reachable instructions** execute. Retain and guard all eleven unreachable division-trap/unsigned-correction instructions at indices 35,39,40,41,83,84,85,98,99,100,101; do not count them as visited.
- **514 fired fault-prefix pairs** compare normalized/retail literal state. Empty count 0/-1/INT_MIN succeeds with every unused incoming stack parameter unmapped after model initialization. The table's LWR still fires; native C does not promise that extra-byte read or literal fault order.
- **Native32 O2/O0, 1,024 cases each**, use separate translation units, selected-C UBSan traps, the correct ten-input function pointer, finite/representable conversions and palette zero. Check every formal factory field, all byte flags, signed/narrow coordinate and extent boundaries, full-word contexts, high color bytes and global-color mutation without changing the staged local.
- **Ten compiled guest and native negatives fail effectively**: wrong phase step, wrong angle shift, swapped trig, wrong delay base, wrong RNG half, five-bit tail, wrong mode, live instead of staged colors, wrong Z and byte-truncated extents.
- All **193 raw-word flips, 193 production-padder word flips and 193 padder binding flips** fail, as do all eight external binding changes and a changed guard predecessor. Every input/fixture/manifest/successor/image corruption control fires.
- **Three independently assembled original rebase sets / 48 whole cases** change the entry, all four call bindings and color-table address. Six additional three-factory prefixes cover counts 65535/65536/INT_MAX and zero-step behavior; full huge loops are not claimed executed.
- **Four original caller windows / eight captures** check the complete physical float/word/byte ABI, palette zero, radii 50/30/20/70, lifetimes 40/40/50/500, counts 20/10/4/10 and byte/full-word context tails. Whole callers remain unconverted.
- **216 connected cases** execute **176 actual current helper words** from sine, cosine, small factory and allocator, plus the real trig table. Check every one of each 52-byte record's bytes, including fields, preserved holes and every-third allocation failure. RNG, heap and registration remain opaque; this is not full gameplay or hardware qualification.
- All **801 archive fingerprints**, **75 frozen/live input gates** and the initial prediction remain fixed. Both tools copies pass Windows syntax and all eleven shared WSL padder tests; consumer `make tools-check` passes. New target suites run in the consumer layout.

Qualification corrections were confined to the fixtures: select the later
SELECTED body at call time rather than freezing the initial Python default;
allow the existing unaligned-word runner's three-byte SWR through the generic
byte store rather than the unrelated halfword alignment check; distinguish
an executed branch delay from unreachable unsigned correction words; use
count two to make the phase-step negative effective; format signed native
input words as unsigned hex; and include the first caller's complete
argument-setup window. Full final qualification reruns every corrected gate.
These are not production profile or behavioral changes.

## Whole Image And Banking

The guest build exits zero with inherited compiler and duplicate
generated_12D630 recipe warnings. The full rebuilt ELF matches its **initial
pre-install prediction**, with **602 changed bytes** only within the
772-byte ring slot and symbol extent **12 -> 772**. Every other ELF byte
and all **72 unaffected inputs** are fixed, with **no metadata exclusions**.
Protected layout remains **189,088 bytes / 720 owners / zero differences**.

| Input | SHA-256 |
| --- | --- |
| ELF | 42f7aaa72746fe4815290922d9aa5b907528865ec34294dd6e5d6ed936311f1c |
| Owner | 43f273ed63bb2c1a129a5c7bd95089d3d24bf8586b0965ad5ca3e8536f02f10f |
| Guards | fee1a24bdf16c415bcf302814da4dec0293c5883f4aad9d0fe6fe96df5dc4f6f |

Fresh official matching: **Game 2,912/4,828 (60.31%)**, **total
3,585/5,501 (65.17%)**, different **1,916**, drift **0**. Init 492/492 and
Debugger 181/181 remain exact. Conversion data stays 5,501/6,044 (91.02%),
byte coverage 86.04%. Root README changes only the aggregate snapshot/date.

Tools **6f03b11** contains six new experiment/oracle/native/checkpoint/test
files. Preserve the older mirror at HEAD **ddbdd16** and all **751 initial
dirty-file hashes**; copy six absent owned files hash-equal, giving **757
paths**. Do not reset or commit that independent checkout. Bank tools first,
then consumer source/guards/pin/docs. No push or Claude call.

Resume **func_15170B90** from Note 1423 with this genuine void ring definition
and its unchanged ABI. Its previous 210-word / frame-0x128 candidate still
does not fit retail's 205 / 0x120, and no debris matching credit is taken.
Use a new successor-phase directory and the strict ring checkpoint; preserve
old captures rather than rewriting them. Older fixed-live-stage suites are
historical receipts, not fresh current-image audits. Keep every wider queue
active. No host-port build, launch, gameplay or frozen Release operation.
