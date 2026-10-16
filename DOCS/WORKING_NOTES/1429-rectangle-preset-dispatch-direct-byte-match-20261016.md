# Rectangle Preset Dispatch Direct Byte Match

Date: 2026-10-16. Resume from consumer **374d65a2**, tools **baff8d3**,
both initially clean. Bank tools **20f2701** first. Continue
[Note 1428](1428-random-packet-burst-direct-byte-match-20261016.md): replace
**func_15171600**'s zero-return placeholder with complete semantic C.
All **127 retail words / 508 bytes** match directly, original frame
**0x40**, with **no target instruction guards, new pool or compiler profile**.

## Steps

1. [x] Freeze the live source/ELF/tools and original caller/data/reference boundaries; inspect the complete original routine and real callee interface.
2. [x] Recover the unsigned byte switch, four presets, live offset loads and true three-input-to-thirteen-input ABI.
3. [x] Match every original instruction directly from the first semantic C compile, keeping all eight neighbors, pools and prior guards unchanged.
4. [x] Pass ten pre-install checks, including the complete selector domain, native32, effective negatives, aliases/faults, independent rebases, original caller and current rectangle emitter.
5. [x] Preserve the rejected slot-only prediction, explain its 53 metadata bytes, then predict and reproduce the full linked ELF without exclusions.
6. [x] Pass thirteen final target/install checks, update fresh aggregates and README rows, preserve the older mirror and commit tools before consumer source/pin/docs. No push.
7. [ ] Recover next func_15171BF4: VA 0x15171BF4, ROM 0x19F0A4, frame 0x28, 43-word retail slot / 172 bytes (42 instruction words plus one padding nop), ending at 0x15171CA0. It is the last placeholder in this owner. Audit the actor +4 byte and actual helper signatures first.
8. [ ] Restore caller func_150265CC and retain func_15169C70, func_1511C638, func_1516D400, inherited-stack func_1516FE1C and all broader Game/additional-source/raw-matching queues.

## Recovered Interface

The complete original span is VA **0x15171600..0x151717FC**, ROM
**0x19EAB0**, without a separate padding word. Keep the address-based name:

```c
void func_15171600(u8 *actor, u8 flags, s32 context);
```

Use the existing rectangle emitter's actual thirteen arguments:

```c
void func_151717FC(u8 *actor, f32 halfWidth, f32 halfDepth, f32 offsetX,
                  f32 offsetY, f32 offsetZ, s32 kind, s32 preset,
                  s32 xCount, s32 zCount, f32 scale, u8 flags, s32 context);
```

The actor occupies A0, so the first three floats travel in A1/A2/A3 as
raw words. Preserve flags as a byte and context as a full word. The reference
misreads the selector width and shifts/mistypes callee arguments, even
omitting the actor in its reconstructed calls; those mistakes are not adopted.
The actual selector is the unsigned byte **actor[0x72]**, not the separate
actor +4 discriminator used by the next routine.

| Selector | Half Width / Depth | X / Y / Z Offset | Kind / Preset | X / Z Count | Scale |
| --- | --- | --- | --- | --- | --- |
| 0xEB | 400 / 500 | 0 / D_800A6FC0 / 0 | 2 / 5 | 20 / 20 | 1 |
| 0xF6 | 200 / 400 | -1800 / -1000 / -1200 | 2 / 5 | 4 / 10 | 1 |
| 0xF8 | 100 / 160 | -2500 / D_800A6FC4 / 0 | 2 / 5 | 4 / 4 | 0.5 |
| 0xF9 | 200 / 100 | 100 / -300 / 0 | 1 / 5 | 4 / 4 | 1 |

Each recognized selector emits exactly one call. Others make no call and
do not read either offset global. Keep **D_800A6FC0** and **D_800A6FC4** as
live float loads; their initial values are -1270 and -650, but constant
substitution is not the full source contract.

Install only the semantic body, its descriptive comment and the two float
externs/minimal callee declaration in
[generated_19E040.c](../../conker/src/game/generated_19E040.c).
The first compile already matches all 127 words, including the save homes,
sparse dispatch, argument setup and return schedule. No normalization is used.

Raw target SHA-256:
`44dec27557512b82f9b476f19212083ea7684fb2b68c4e1a600e65d713d9ce73`.
Lock all **eight** relative relocations. The prior 32-byte compiler pool,
existing D_800A6FA4 pool alias, Makefile/profile and complete guard CSV stay
byte-identical. All eight owner neighbors retain their words, lengths and
relative relocations, including the newly recovered random burst.

## Fresh Qualification

All **10 pre-install tests pass in 44.376s**. After production installation,
all **13 final tests pass in 84.073 seconds**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_rectangle_preset_dispatch tools.tests.test_game_rectangle_preset_dispatch_installed -v
```

- **4,096 paired sequences** cover all 256 selector bytes, both stack phases, four original/mutated offset patterns and effectful/ordinary callees. All **127 instructions execute**. Check all thirteen argument words, bit-preserving live offset loads and default-path no-read behavior. Callee writes cannot cause a second dispatch.
- **Native32 O2/O0, 768 cases each**, separate translation units with selected-C UBSan, cover every selector, finite/signed-zero offset changes, flags/context widths and effectful callee behavior. All nine compiled guest/native negatives reject: halfword/signed selector, null actor forwarding, baked/wrong offset, swapped counts, wrong last kind, shifted flags and narrowed context.
- **142 fired fault-prefix pairs** compare literal guest memory/register/event state. **16 guest-only incoming-home aliases** qualify the original flag/context saves before selector reads. These are not portable C alias/fault or native FP-environment claims. Guest quiet-NaN/infinity bit copies are separate from the native finite/zero fixture.
- All **127 raw-word, eight relocation-binding and 32 inherited-pool byte corruptions** reject. Three independently assembled original rebase sets / **90 paired cases** change every global/callee binding, including signed-low carry at the offset globals.
- **Six original caller captures** execute func_150265CC's 0x15029914 window with actor from SP+0x768, flags from SP+0x773 and context zero. The current caller is still a C zero-return placeholder, and the 32-byte call window remains zero-filled. This does not claim a working current caller or gameplay acceptance.
- **16 current rectangle-emitter connections** execute its 61 actual words, verify the complete quad and all ten forwarded edge-emitter arguments, and cover signed coordinate extremes. The downstream four-edge emitter is opaque in this test; no staged-original or full gameplay claim is made.
- All **82 frozen/live input keys**, capture/initial-prediction/successor checks and physical code/data/callee/symbol/string corruption tests pass. Preserve every unaffected source, guard, conversion row and toolchain input. Protected data is exact across **189,088 bytes / 720 owners**.

Qualification-only corrections: fix a recursive local harness adapter;
use an aligned halfword width negative instead of an unsupported unaligned
load-pair probe; allow the intentional signed-selector negative's compiler
range warning, while requiring the selected compile to be diagnostic-free.
Execute semantic negatives against their own compiler pool, not the
production alias: the alias can map a baked literal back onto the live
retail offset and erase the intended difference. No shared helper or
production behavior is changed for these corrections.

Both tools copies pass Windows syntax and all eleven shared WSL padder
tests; consumer `make tools-check` passes. Prior unchanged neighbor-suite
receipts remain prior evidence rather than newly rerun tests. Claude calls:
zero.

## Complete Linked Image

Before production edits, capture the old linker script and padded owner.
The baseline full link reproduces the frozen predecessor exactly. The
first slot-only calculation predicts **396 changed bytes** for the restored
body and symbol extent **12 -> 508**, but fails the full-link audit.
Preserve it as `slot-only-rejected.elf`; do not silently accept or overwrite it.

The pre-install full link predicts exactly **53** additional symbol/string
bytes in one contiguous three-record/name cycle:

```text
before: D_800A6FC0, .L1513145C_game_data, D_80098D90
after:  .L1513145C_game_data, D_80098D90, D_800A6FC0
```

Require the exact initial hash, record positions, string extents and named
definitions, then rotate this one group. All named definitions remain
unchanged apart from the target function extent. The complete structural
plus cycle prediction equals the pre-install link and final production ELF:
**449 changed bytes**, every other ELF byte and **80 unaffected inputs**
fixed, no metadata or section exclusions.

```text
before ELF     0f335a16152a5bed2e84ed2061e240b0bbd063130b761f6228bb42e7ebe7609e
rejected slot  57c50865c57901ea19d3a535e3e5df5a7e14b662c91b25eabf7a5ba98f9c2c01
qualified ELF  5877233ddf6a78bc55b80b102f47d8736e8678351e5937e3ba1b3e77066a8533
qualified C    7a985b3eadfe194efac55d5b42f0401cbb09e6694d6e05936f6bf20bae3fec08
```

Fresh official numbers: **Game 2,916/4,828 (60.40%)**, **total 3,589/5,501
(65.24%)**, different **1,912**, drift **0**. Init 492/492 and Debugger
181/181 remain exact. Conversions remain 5,501/6,044 (91.02%), converted
bytes 86.04%. Root README changes only aggregate matching rows.
The existing duplicate generated_12D630 recipe warning remains unrelated;
the guest build exits zero.

Tools **20f2701** banks five new experiment/oracle/checkpoint/test files
before the consumer. Preserve all **777** initial older-mirror dirty-file
hashes and its **ddbdd16** HEAD, copying only these five absent files to end
at **782** dirty paths. Do not commit/reset that independent mirror.
Bank consumer C/tools pin/docs separately; no push. Let the normal incremental
Graphify commit hook finish without forcing a full scan or dropping retained
excluded nodes. No host build/launch or frozen Release action occurs.
The broader Game matching goal remains open.
