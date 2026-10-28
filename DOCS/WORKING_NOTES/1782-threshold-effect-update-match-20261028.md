# Threshold effect update - guarded C match

Verified 2026-10-28. Restore func_151A483C in generated_1D0840:
VA 0x151A483C..0x151A4900, ROM 0x1D1CEC..0x1D1DB0, 49 words / 196 bytes.
Normal O2/g3 emits 49 words with no frame. Eleven expected-word guards
normalize two commutative integer multiplies and one independent counter
reload, producing all original instructions without insertions or omissions.

## Recovered interface and fields

The interface is s32 func_151A483C(ThresholdEffectRecord1D0840 *record,
void *unusedContext). It always returns 1. The unused second pointer is
still stored at incoming SP + 4. The typed record is 0xB4 bytes; its fields
and offsets are verified in native32 tests.

| Record offset | Recovered use |
| --- | --- |
| +0x18 signed halfword | State code; set to 0x5203 on transition |
| +0x1A signed halfword | Remaining counter |
| +0x2B byte | First scaled output |
| +0x2C byte | Second scaled output |
| +0x38 / +0x3C float | Two accumulated values |
| +0x70 / +0x71 byte | Mode selectors; both set to 2 on transition |
| +0x72 byte | Update callback selector; set to 1 on transition |
| +0xA8, +0xAC, +0xB0 signed halfwords | Transition, first-output and float thresholds |
| +0xAA, +0xAE, +0xB2 signed halfwords | Second-output, first-output and float scales |

When the counter is below the first-output threshold, narrow counter times
its signed scale into the first output byte. Independently, below the float
threshold, multiply the signed scale by D_800BE9E4 with 32-bit unsigned wrap,
reinterpret the product as signed32, convert to float32 and add it separately
to both float fields. Reload the counter after publishing those fields.
Below the transition threshold, select callback 1, set both mode bytes to 2,
write the second scaled byte and set state 0x5203. Preserve each inactive
output. The two byte products fit signed32 because both inputs are signed16.

The initial private draft treated the ignored argument as an integer and
+0x72 as an active flag. Inspection of the actual dispatcher established the
pointer interface and callback-selector meaning before qualification. Nine
operand-expression screens retained the same eleven differences; the final
source keeps the straightforward semantic expressions.

## Closed guard proof

The two multu instructions at offsets 0x24 and 0xA8 exchange their input
register order only. Unsigned multiplication is commutative for both HI and LO.
The other nine guards rotate the counter load at raw offset 0x5C to 0x7C,
retaining the intervening mflo, conversion, arithmetic and two stores exactly.
The counter at record +0x1A cannot overlap the float fields at +0x38/+0x3C.
Neither the instruction count nor either clock relocation changes.

The raw C, normalized object and original instructions agree on complete
memory and return values for the qualified guest cases. Only normalized and
retail execution are equated at instruction/access/fault boundaries. Raw
reordered fault prefixes are not claimed identical. The HI16/LO16 clock
bindings remain at offsets 0x10/0x4C. Eleven deliberately stale expected
words are rejected by the real production padder; prior guard rows remain
byte-for-byte unchanged.

## Actual caller and callback transition

A full ROM census finds no direct J/JAL to the target and one pointer literal:
slot 0 of the 40-word D_80089760 table at VA 0x80089760 / ROM 0x22E220.
Slot 1 contains the already byte-exact 39-word func_151A4900.

The original 428-word func_151303EC calls through this table at VA 0x15130A38.
A0 is the record; A1 points to the caller's saved position at SP + 0x48.
The caller tests the returned value at 0x15130A44: zero requests the release
path, while the recovered result 1 keeps the record alive. An independently
compiled zero-return mutation is rejected through this actual caller path.

768 cases enter the complete original parent and follow low flags 0..7,
zero animation rate, callback/disabled/expiry routes through its return.
They visit 105 of the parent's 428 words. The remaining animation paths are
not qualified; the parent's production placeholder stays unchanged and
uncredited. Exit and release services are bounded providers.

24 two-tick sequences verify the slot-0 to slot-1 transition. 22 execute the
next callback; two expire first and correctly take the release path. The
next-callback cases visit 37 of its 39 words, while its complete current body
and table bytes remain literally equal to retail. This is bounded original-
instruction integration evidence, not a claim of full-game acceptance.

## Qualification and strict integration

Both tools copies pass eight fresh canonical methods and shared tools checks.
After production, each passes two fresh installed methods; six semantic
methods are reused only with exact module, input and artifact fingerprints.

- 1,534 guest cases visit all 49 target words, covering signed boundaries,
  wrapped clock products, default float32 behavior, all byte arguments and
  ten aligned argument-home alias offsets. Guest nonfinite values and private
  stack aliases are kept separate from native and hardware claims.
- 480 fired access-prefix pairs compare normalized and retail complete state,
  trace, PC and delay slots. Inactive thresholds skip their scale/clock reads.
- Native32 O0/O2/O3 each pass 262,144 cases, including all 65,536 counter
  encodings. Check the two-pointer ABI, typed layout, whole-record/context
  fences and trapping UBSan. Twelve native and twelve separately compiled
  IDO semantic mutations fail observably.
- Seven GNU layouts run 224 cases, including four clock/record alias layouts
  and HI16/LO16 carry cases. Three raw/binding corruptions, eleven real-padder
  stale guards and six whole-image corruptions are rejected.
- The actual five-command Make recipe includes GLOBAL_ASM preprocessing and
  postprocessing. It reproduces the qualified owner, preserving all 22 other
  functions, their bindings, constant pools and the one retained GLOBAL_ASM
  routine. Target and owner emit no compiler diagnostics; Make retains its
  known unrelated duplicate generated_12D630 recipe warning.

The immutable qualification seal covers 16,372 paths and 376 focused inputs.
Independent image prediction permits precisely 132 changed bytes: 131 code
bytes and one symbol-size byte (12 -> 196), with zero exclusions. All 6,056
function addresses, 6,055 other bodies and 720 protected Game owners /
189,088 bytes remain fixed. Shared declarations, caller and next-callback
source, Makefile, layout, conversion CSV and inherited guards stay unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Raw compiler body | fe9b4221c61a90a9ff546e917119a84e3442ef99fb39795426c96c624877ec9e |
| Linked retail slot | 9b7679467c3fb18c8a8897ba6c844f88e15b9df885d8e065d47c384a2c5b458a |
| Adopted ELF | 157166a0b932851d5e72143dbf25f4aa78299dd941aaa98a556aa5fbefe5008b |
| Appended guard manifest | c9f2d82d72afcd7be14278dbc076ff6b8aa1330ca0f42e11d3bcf51b76923225 |

## Bank and measured progress

Predecessor consumer: 2c14a41a8cd845f16e0db06f3ec1ed1dc95ca375.
Tools committed first: ce80285a380010700d3de25948a6d2dd6231c351.
Preserve 1,787 inherited dirty paths in the older tools mirror and add only
three qualification modules there. No push. Routine Claude calls: zero.
Graph work is scoped AST refresh with old-node and valid-relationship
retention, not full-corpus extraction or global reclustering.
Raw receipts: conker/build/game-threshold-effect-update-match/.

| Section | Byte-exact C | Different | Address drift |
| --- | ---: | ---: | ---: |
| Total | 3,860 / 5,506 (70.11%) | 1,646 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,187 / 4,833 (65.94%) | 1,646 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

270 more exact C functions are needed to reach 4,130 / 75%.
Next inspect func_1519E754; the queue is a screen, not qualification.
func_1514E920 remains parked and uncredited.
