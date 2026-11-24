# Randomized spray callback byte match - 2026-11-24

`func_150C2558` replaces its zero-return placeholder with the complete
**106-word / 160-byte-frame** event spray callback. Production increases
from 4,653 to **4,654 / 5,528 (84.19%)**; Game **3,981 / 4,855 (82.00%)**.
Init 492/492 and Debugger 181/181 remain fixed. Zero address drift, 874 still
different, **45 more matches reach 85%**. Only this callback receives credit.

Owner `conker/src/game_EF410.c`; original
`conker/asm/nonmatchings/game_EF410/func_150C2558.s`. VA
`150C2558..150C2700`, ROM `EFA08..EFBB0`, 424 bytes. The first draft's separate
float temporary emitted an incorrect frame 168. Reusing `descriptor.z` as the
temporary recovers frame160 and all call/data bindings; it leaves seven
independent scheduling words. No insertion, omission or arithmetic patch.

## Typed event interface and packet

Whole pristine aligned-ROM census finds zero direct JALs and exactly one
entry pointer: ROM22F4C4 / VA8008AA04, `D_8008AA00[1]`. Already recovered
`func_1514C2F0` consumes that registry. Its live 96-word body and the original
25-word handwritten RNG are independently checked against retail ROM.

The callback exactly matches `RadialCallback176A00`:
`s32(s32, s16, f32, f32, f32, f32, f32, f32, u8, u8, f32, s32,
f32, s32, u8)`. Unused parameters retain these real types; a native function
pointer assignment checks compatibility without casts. Changing the initial
word-only draft to this type signature preserves every generated word.

Capture x/y into the shared 136-byte descriptor before `func_150ADA68()`.
After the provider, load stacked z and compute three ordered single-precision
operations: `(z + 15) - (random * 30)`. Store that position in `descriptor.z`.
The signed halfword at +0x28 receives the low 16 bits of
`(u32)(s32)(descriptor.z * D_800A0270) - 64u`. The factor is protected word
`3D8F9C19` (about 0.0701219514), loaded after RNG. Explicit unsigned subtraction
preserves ADDIU wrapping at INT32_MIN without signed C overflow; emitted
instructions remain identical. Native narrowing assumes the verified SDK32
two's-complement implementation.

Other request fields are typed literal stores; offsets remain named by their
known layout where meaning is not established. Retail leaves reserved bytes
and +0x84..0x87 unwritten, as in Note 2673. The existing helper still reads its
last word. Guest tests compare all 136 coupled entry-stack bytes; native tests
read only defined fields. The helper ABI and original RNG implementation are
unchanged and receive no added credit. RNG is a bounded float-return provider
in the execution tests, not a claim to execute its original 64-bit PRNG body.

## Scheduling, floating-point and caller evidence

Seven guards normalize the nine-word closed integer block 38..46. Retail moves
LUI AT,0x4230 to the opening position and moves an independent LI t7,40 past
the angle store. An independent symbolic evaluator proves equal complete
GPR state and the same ordered byte/halfword store values for arbitrary entry
registers and private bytes at the join. All other 99 words and four relocation
sites already match. No branch, provider or FPU instruction occurs inside
the block. The floating-point/conversion prefix and the entire suffix are
identical, preserving arbitrary guest FCSR behavior compositionally. Valid
mapped/aligned stack accesses are assumed; raw fault/interrupt prefixes
inside the reordered block are not claimed identical.

* 1,028 cases per four guest streams exercise all 106 instructions, all 256
  channels, high argument bits, stack phases, varying retained bytes, ordered
  RNG/global mutations, INT32_MIN wrapping and both providers' clobbers.
* Four invalid-conversion preboundary quads compare the identical prefix
  before conversion handling. They do not invent a native C result for NaN,
  infinity or an out-of-range float-to-int cast. Native coverage requires a
  finite representable float-to-s32 value; guest exception modes follow the
  independent unchanged-prefix/block/suffix relation.
* The original 16-word dispatcher window 1514C3C4..1514C404 marshals and checks
  all 15 argument words for five cases per stream. Return 1 continues the loop;
  four effective return 0 instruction controls instead reach1514C42C. Complete
  enclosing dispatcher execution is not claimed by these bounded windows.
* Native SDK32 O0/O2/O3, strict aliasing and UBSan: 1,028 cases each. Eight
  source controls return observed comparison exit 42, with no trap/signal
  counted as success. Typed callback calls and valid INT32_MIN conversion
  are included; uninitialized descriptor fields are never read natively.
* 110 raw-word/binding pins, 14 corrupted guarded-word rejections, 206 other
  visible word/binding corruptions, two oversized rejections, 16 real GNU
  links and 32 guest rebases, including adjusted HI, negative LO and JAL regions.

Both padders preserve all 17 raw/padded neighbors, pools and diagnostics,
including Note 2673's 101-word constructor and its existing guards. The ordinary
owner's second-padder geometry uses the same frozen slot layout, not an
independent layout. Actual Make replays all six owner commands, including the
unchanged motion-pool check. The unchanged five-word helper ABI's qualification
is reused from Note 2673, with its source/object fingerprints fixed.

## Independent image and committed bank

A separate before-C/original-target-ASM reference reconstructs every named
ELF definition and string from the frozen baseline, changing only this body
and its justified size. The C and production images equal its prediction:
**333 changed bytes, zero exclusions**. All 189,088 protected Game data bytes
across 720 owners, registry pointers, unrelated objects, other function bodies,
addresses/extents, conversion CSV and the complete old guard prefix remain
fixed. Exactly seven target rows are appended.

ELF SHA256: `41341af553108f6df5b271c007a6a1156c19cda76a4e1154429aad41746f5eb7`.
Padded owner: `b4aa0e95f6b3412318b60e1a0bab92753f85127adc8f884b845ed176b804340c`.

| Phase | Time | Gates |
| --- | --- | --- |
| preinstall-primary | 108.562s | 5 fresh / 0 reused |
| preinstall-sibling | 76.379s | 5 fresh / 0 reused |
| installed-primary | 68.688s | 5 fresh / 0 reused |
| installed-sibling | 85.580s | 5 fresh / 0 reused |

Exploratory development receipts are not credited here. Shared tools-check
passes. Tools commit `41357aebb75d8857afcbd5a9a5aca0136d5b4794` precedes
the consumer commit. The real dirty sibling checkout is preserved. Root
README changes only aggregate rows; old DOCS index bytes are retained.
Normal Graphify update, actual hook completion, scoped refresh, old-ID and
qualification retention and current-definition audit have separate receipts;
this is not full-corpus extraction. Host scene configuration inspection finds
no direct C owner consumer or complete host build root. No host/Release
edit/build, push, WSL restart or Claude model request. Keep the 85% goal active.
Dimensions 15015FBC and the older renderer 15197148 remain private/uncredited.
