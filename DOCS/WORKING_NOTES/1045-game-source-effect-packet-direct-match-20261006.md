# Game Source Effect Packet Direct Match

Date: 2026-10-06. Starting checkpoint: `e1ace32c`.

Recover **`func_1519ED84`, 96 words / 384 bytes**, VA
0x1519ED84..0x1519EF04, ROM 0x1CC234..0x1CC3B4, frame 0xA0, in
[generated_1CBE20.c](../../conker/src/game/generated_1CBE20.c).
All instructions emit **directly from semantic C under existing O2/g3**.
No new word guards, compiler profile, shared header, symbol, data or metadata.

## Recovered Contract

Five arguments: 32-byte source prefix, signed 32-bit selector word, signed
lifetime halfword, unsigned channel byte and signed context word. The local
byte field named `mode` transports the selector's low eight bits; this is a
working name, not a recovered original declaration. Source position is +0,
vector +0xC, width +0x18 and height +0x1C, reused from the previous wrapper.
Capture the **pointer value** separately before any callback.

Construct an **88-byte descriptor**:

| Offset | Value |
| --- | --- |
| +0 / +1 / +2 / +4 | selector byte / byte zero / halfword 0x3B03 / lifetime halfword |
| +8 / +0xC | zero words |
| +0x10..+0x13 | four bytes 255 |
| +0x14 / +0x18 | source width / height multiplied separately by 10.0f |
| +0x1C..+0x24 | three source position words |
| +0x28..+0x30 | three source vector words |
| +0x34 / +0x38 / +0x3C | float 1.0 |
| +0x40 | flags word 0x045C0081 |
| +0x44 / +0x45 / +0x46 / +0x47 | bytes 255 / 255 / zero / seven |
| +0x48 / +0x4C / +0x50 | zero word / byte 255 / zero word |
| +0x54 / +0x56 | halfwords one / 255 |

Exactly **five bytes remain untouched**: +6, +7, +0x4D..+0x4F. No invented
padding stores or memset. Descriptor and saved pointer begin at SP+0x48 and
SP+0x44 respectively. Saved S0/RA occupy SP+0x38/+0x3C, not descriptor storage.

Call retained `func_1513D2F0` with all **twelve arguments**:

```c
func_1513D2F0(&packet, (s32)&D_800A4AA0, 39, 0, 0, 23, 0,
             3, 255, 4, channel, context);
```

The second parameter retains the existing signed-word prototype; the explicit
cast transports the table's address in the 32-bit guest ABI. It is not a table
value load and does not establish portable 64-bit pointer handling. No shared
prototype churn. On null, do not publish anything. On success, copy exactly
four bytes from the saved pointer local to returned effect+0x110. This is not
a copy of the source's first word or of the packet itself.

The [retail caller](../../conker/asm/50D80.s), ROM 0x54F2C..0x54F7C, validates
selector below 0xCF, otherwise selects zero, indexes a source record with
0x44-byte stride, passes signed lifetime, byte channel and context one, then
ignores V0. The C wrapper returns void. Guest tests bound machine V0 transport
from null/copy callbacks without promising a C return API. Out-of-range byte
values in diagnostics do not prove real constructor table indexing is valid.

## Compiler Evidence

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_source_effect_packet_candidates.py)
screens **13 forms x four profiles = 52 controls**, plus **46 single-field
ordering controls** under O2/g3: **98 controls**, all isolated diagnostics empty.
The initial field-order form has correct 96-word length/frame 0xA0 but 16
temporary-allocation/scheduling differences. Move selector and lifetime stores
to their header-field positions: selector, field01, field02, lifetime, followed
by the other fields. IDO now emits **all 96 words directly** with the retail
temporary assignments, saves and branch-delay stores.

No one-field reorder alone matches. O2 header-order emits 94 words/frame 0xA0
and 94 differences. O1/g3 and O1 header-order emit 102 words/frame 0x98 and
99/100 differences. Named scale/unit locals grow the O2/g3 frame to 0xA8;
struct vector/position copies emit 97 words. Tests bind every measured length,
frame and difference count, including overflowing tails, rather than checking
only the winning profile. Selected C and the installed owner are bound too.

## Qualification

[Nine tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_source_effect_packet_match.py) use an
independent byte-packet reference and unchanged shared guest/native runners:

- **3456 guest cases / three bodies**: initial field-order, selected direct C
  and retail. Eight argument bundles, four contexts, two stack phases, three
  padding patterns, callback mutation, null/success/output-alias outcomes and
  three source patterns. Check all 88 packet bytes, twelve constructor
  arguments, four-byte copy arguments, complete external memory and ordered
  read/write/call traces. Saved GPR/FPR/SP/RA lifetimes hold; all **96 words**
  execute. Constructor remains an opaque callback in this test.
- **65536 additional selected guest cases** cover every lifetime halfword,
  all **65536 selector/channel byte pairs**, high incoming argument bits and
  both stack phases. Verify the complete packet, calls and external footprint.
- **128 guest cases / three bodies** cover signed zero, smallest subnormals,
  normal boundary, near-one and largest finite dimension inputs. Raw position/
  vector words include quiet/signaling NaNs and infinities without arithmetic
  on them. No hardware FCSR/exception-mode/native signaling-NaN claim.
- **576 guest cases / three bodies** connect the actual current constructor
  placeholder. Its four argument-home stores, zero return and return delay
  execute; there is **no source-pointer publication**. Exact coverage binds
  100 unique instruction addresses: 93 wrapper words and seven placeholder
  words. This explicitly confirms the missing downstream implementation.
- **131072 native cases** run actual selected C with the typed opaque
  constructor/copy callbacks. Every lifetime twice, every selector/channel byte
  pair, null/success, mutations and context widths. Check 32/88-byte layouts,
  four-byte pointers, all initialized fields and whole source/table/output
  storage. Native unspecified descriptor padding is not asserted.
- **192 connected native cases** run the selected wrapper followed by the
  actual retained `func_1519EF04` C after opaque successful construction. Four
  source patterns, three selectors, four lifetimes and four channel values.
  Mutate the source after pointer publication, then check the consumer's eight
  output stores and entire output storage. This is consumer qualification,
  not actual construction or full gameplay.
- Six compiled negative controls detect a stub, wrong flags, payload size,
  pointee instead of pointer copy, wrong channel and initialized padding.

Initial fixture expectations were corrected against observed evidence: the
null path skips three wrapper instructions (its branch delay still executes),
and the O1 dimensions-first control has 101 differences. Lifetime-at-zero/one
has 68 differences, versus the selector order's 66. Production code did not
change for those expectation corrections. All **34 focused post-link tests
pass in 497.803 seconds**, no skips: nine new packet tests, eight previous
source-backed actor packet, six configuration packet, six address-record
allocator and five core guard-relocation tests. The standalone driver also
finishes all 98 controls and writes its current measurements receipt.

## Linked Audit

`make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress`
passes. All **96 linked words** equal retail; target SHA-256:
`23a3d2bcc1fd10d1339230ff130d6c7bbef6bf0e562c7662c738cbbe8a422960`.
Across **6059 slots**, only `func_1519ED84` changes; all addresses/sizes stay
fixed. Protected `.init`, `.init_data`, `.debugger` and `.game_data` are
unchanged. All **720 Game-data owners / 189088 bytes** remain retail-exact.
All **10660 existing guard rows** are identical and in order; no new guard.
Baseline/current owner diagnostics empty. Existing Makefile duplicate-recipe
warnings for generated_12D630 remain unrelated and unchanged.

The retained `func_1519EF04` remains **27 words directly retail-exact**.
The **114-word** `func_1513D2F0` slot still contains only its seven-instruction
zero-return placeholder, followed by zero padding; it is not semantically
restored. No complete caller/FCSR/backend/hardware/gameplay/host adoption claim.

Measured totals: **3323 / 5462 (60.84%)**, Game **2650 / 4789 (55.34%)**
exact; **2139 different**, zero address drift. Init **492 / 492**, Debugger
**181 / 181** stay exact. Converted counts unchanged; the old stub counted
as C. README receives only aggregate totals. Ignored audit/control receipts
live under `conker/build/game-source-effect-packet[-test]/`; baseline snapshot
is `conker/build/game-actor-source-packet-test/after.json`.
Tools-check, compileall and diff-check pass; **3286 relative links across 28
documents**, zero broken.
No sibling source/build/save/frozen Release edit, runtime launch or push.

## Next Work

Recover retained **`func_1513D2F0`**, 114 words / 456 bytes, ROM 0x16A7A0,
frame 0x38, in [game_169510.c](../../conker/src/game_169510.c). Its
[retail body](../../conker/asm/nonmatchings/game_169510/func_1513D2F0.s) selects
allocator category from descriptor flags, copies 0x58 descriptor bytes to
result+0x18, initializes the actor's state/helper records and optional view
references, and returns the allocated pointer or null. Recover callback
ordering, widths, failures, live reloads and exact helper contracts before
installation. This is the current dependency gap, not a recovered function.
The other effect consumer `func_15152190`, extended constructor's match and
projection/pair-clamp frame work remain open. Broad Game matching goal active.
