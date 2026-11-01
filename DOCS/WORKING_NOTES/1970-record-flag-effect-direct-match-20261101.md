# 1970 - Record flag effect callback recovered directly from C

`func_15014144` now emits all **55 retail words** with its original **48-byte
frame**, three relocation sites and **zero word guards**. The actual Make and
independent full-image prediction pass. Fresh production and Native ELF recounts
confirm **4,038/5,507 (73.32%)**, Game **3,365/4,834 (69.61%)**, zero address
drift, 1,469 still different. The 75% threshold is 4,131: **93 more** are needed.
The wider goal remains active.

## Source and ABI recovery

Owner `game_40490`, VA `0x15014144..0x15014220`, ROM
`0x415F4..0x416D0`. Read the record word at `+0x18`. Translate its five low
bits to `(flags & 0x1F) ^ 2`: keep bits 0, 2, 3 and 4, invert bit 1, and discard
higher bits. Submit the selector byte at `+0x1F`, the record pointer and NULL
floating-position pointer to `func_151A9390`, followed by the raw float stored
at `D_8009667C`, 100.0f, -1, 255 and 1. Return 1 after the helper.

The previous C accumulated flags with five conditional statements and emitted
45 words. Recovered conditional terms preserve the retail compiler's branch
shape, temporary lifetimes and OR order, producing all 55 words directly.
Five bounded operand-order screens distinguish the exact form; no assembly
substitution, filler or expected-word patch is introduced. Shared declarations
and the existing u32-to-float storage view remain unchanged. Native qualification
uses the existing `-fno-strict-aliasing` profile for that storage view.

Raw payload SHA-256:
`dd2d838a7cb2a94ae483c4b53efa82bf1f5c1bfbe585c1b6522105c7bd0d3a84`.
Relocations: HI16 `D_8009667C` at `+0x14`, LO16 at `+0x84`, and
JAL `func_151A9390` at `+0xC0`. Original assembled object and isolated C payloads
and bindings are identical. Full owner diagnostics stay zero, all **31 neighbors**
and normalized pools remain unchanged before and after padding.

## Guest, native, helper and caller checks

- **12,288 guest cases / 24,576 executions**, three independent GNU link
  layouts: all 32 low-bit combinations, high signed-bit patterns, selectors
  0/8/9/255, positive and negative zero, finite and quiet-NaN global float bits,
  stack alignment phases and helper mutations. All **55 words** execute.
  All nine call arguments, public memory, GPR state and access traces agree
  between original and C; saved-state checks and return 1 after caller-saved
  clobbers pass. The scalar float is transported as raw bits, not reinterpreted
  through arithmetic. This is bounded instruction evidence, not FCSR/hardware
  or gameplay acceptance.
- **10 access-prefix cuts / 20 executions** compare memory and access order.
  They do not establish complete fault registers/PC or portable C fault behavior.
- Complete original **45-word `func_15013000` dispatcher**: **2,304 cases /
  4,608 executions**, all words covered, zero/one/two records, table index 18,
  null callbacks, live count/base reloads and four callback-return poisons.
  512 second-record reads follow a helper-replaced base pointer. The dispatcher
  ignores this callback's return value; the callback independently returns 1.
- Original **169-word `func_151A9390`** plus original **11-word memcpy**:
  **1,024 cases / 2,048 executions**. The helper executes 143 words and all copy
  words. The 26 unexecuted PCs are recorded explicitly: NULL record, non-NULL
  float-position and non-default lifetime alternatives are excluded by this
  target's fixed arguments. Lower factory `func_151A8B20` and secondary effect
  `func_1516284C` calls are stubbed, not claimed as complete engine execution.
  Their argument tuples and constructed payload fields are independently checked.
  Success/failure allocation routes, template copies, output flags and signed
  coordinates reloaded after lower-helper mutation all pass.
- Aligned ROM census finds no direct JAL/J encodings and one target pointer at
  ROM `0x227938`, `D_80082E30[18]`. Reviewed static source/ASM references agree.
  This inventory does not rule out arbitrary runtime pointer fabrication.
- Native32 **O0/O2/O3** each pass **2,560 cases / 20,480 executions**, UBSan,
  whole-record canaries, all nine arguments, helper mutations and return 1.
  Seven effective controls reject wrong bit inversion, missing bits 8 or 16,
  wrong selector byte, wrong global float, wrong 100.0f range and wrong return.
- Both tool copies pass **five fresh public tests** and standalone shared checks
  before and after installation. All original assembly remains available.
  No Claude call was needed for this routine.

## Production closure

The actual five Make commands produce exactly the qualified padded object.
Independent prediction changes only the complete 220-byte target slot and its
ELF symbol extent from 180 to 220 bytes. Actual private and production full links
are identical to that predicted ELF, with **zero excluded bytes**.
All **6,052 function addresses** and **6,051 other bodies** stay fixed, and the
complete named-definition multiset matches the expected one-size-field change.
ELF length, linker map, guard CSV and all **189,088 protected Game bytes across
720 owners** remain unchanged. There are no unplanned dependent object changes.

Production ELF SHA-256:
`af12e1ecafe8eba532a5fdbdb840b9f480c3fab078a50c72efd00fbf084d0bf4`.

## Evidence and continuation

Stage `conker/build/game-record-flag-effect-15014144-match/` retains 23 prepared
artifact pins, input snapshot, raw/padded/actual-Make objects, first-linked ELF
and map, `private-owner-qualification.json`, `private-guest-runtime.json`,
`private-dispatch-runtime.json`, `private-helper-runtime.json`,
`private-native-runtime.json`, `private-image-qualification.json`,
`caller-census.json`, both copies' preinstall/installed test receipts,
`production.json`, `native-install.json` and the final bank/handoff receipts.
Public tool modules are `experiments/game_record_flag_effect_match.py` and
its three test modules. Root README receives aggregate status rows only.

Next bounded adjacent candidate: `func_15014220`; inspect its original 35-word
body and partially initialized payload before using the current reconstruction.
Descriptor `func_150174C0` and peer-event `func_15164134` remain private and
uncredited. Their audit1968 snapshots need explicit rebasing before more screens;
this turn does not overwrite their historical evidence. Handwritten
`func_151F8870` belongs to a separate assembly-restoration audit.
The previous goal turn banked `func_15014094`; this turn adds one actual exact
C function. Host port, editor, frozen Release, private work and old archives
are preserved. No push is performed.
