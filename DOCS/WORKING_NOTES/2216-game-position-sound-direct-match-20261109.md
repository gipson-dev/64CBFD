# Position Sound Direct Match - 2026-11-09

`func_150F20F0` replaces a false zero-return placeholder with the original
position threshold, shared cooldown and spatial sound submission. All
**80 words /320 bytes** emit directly from C under existing **O2/g3**, with
original **0x58 frame**, no padding and **no guards or profile/binding changes**.

Production: Total **4,285 /5,513 (77.73%)**, Game **3,612 /4,840 (74.63%)**,
Init **492/492**, Debugger **181/181**, zero drift; **1,228** still different.
**126** more exact functions reach4,411/5,513 and80%. Conversion rows stay fixed.

## Recovered body

Owner `conker/src/game/generated_11C2B0.c`; original `conker/asm/11C2B0.s`.
VA150F20F0..150F2230, ROM11F5A0..11F6E0. RA is saved at SP+0x2C;
there are no saved S registers. Output words use SP+0x4C/+0x48/+0x44.

```c
void func_150F20F0(s32 index);
```

- Select D_800CC2D0[index] with the actual0x32C-byte struct127 stride.
  Load x_position+0x14 and z_position+0x1C, square each, then square those
  results and add them with single-precision rounding. Retail computes
  **x^4+z^4**, including before the cooldown test, not a usual squared norm.
- D_800D98F0 is one shared byte cooldown. If nonzero, compare signed
  D_800BE9E4 with that byte. Smaller subtracts with32-bit wrap before
  narrowing to u8; otherwise clear. Explicit unsigned subtraction preserves
  negative ticks/INT_MIN without introducing signed C overflow.
- With zero cooldown, require a strict greater-than comparison against
  D_800A191C=6760000.0f, bits0x4ACE4C80 at ROM2463DC. Equality does not
  submit a sound. The earlier float work is not moved into this branch.
- Truncate the live y_position+0x18 and call
  func_100114D0(0,y,0,32767,20000,19000,&output0,&output1,&output2).
  Add128 to the entire output0 word before the first RNG call, using an
  unsigned operation and the fixed32-bit target's signed representation.
- The first random result sets the cooldown to(random&127)+128 before
  the second draw. Stage that second draw's unsigned remainder and sound
  ID in s32 soundId: random%3+108. Only then read the retained output's low
  byte and call func_10010F30(soundId,24000,(u8)output0,0,0).
  The target returns void; helper return values are not consumed.

The original82-word/frame0x58 drafts deferred the quartic sum into the
conditional branch. Materializing the sum first recovers80 words, initially
with eight/six differences. Declaring the two floats before the three output
words recovers their original stack slots and removes all six remaining
differences. The preferred source also makes output0's addition unsigned.
No normalization of compiler scheduling is needed.

## Native testing exposed a source sequencing problem

The initial direct match put the second RNG call inside the audio call's
first argument. Although IDO emitted the correct80 instructions, C leaves
the order of separate argument evaluations unspecified. GCC read the pan
argument before the RNG call. A provider retaining the still-live output
pointer could change output0 during that draw, exposing an observable
difference from retail instruction ordering. These are deliberate provider
effects, not an observed behavior of the unchanged retail RNG. They are
valid retained-pointer tests, so those cases were kept.

The adopted source assigns soundId in a separate full expression before
the audio call. This guarantees the required later output-byte read. A
normal s32 local, a u32 local and register-qualified variants all retain
the exact80 words/frame0x58; s32 matches the audio helper's first argument.
A block-scoped initialization emits81 words, and reusing the incoming index
shrinks the frame to0x50; both are rejected.

The old unsequenced form is retained as a **native-only control**. Its
complete IDO raw body and14 bindings are explicitly checked as identical
to the adopted body's. It nevertheless fails the retained-output contract
at native O0/O2/O3. This is a concrete reason that an isolated byte match
alone cannot qualify a portable C recovery. The staged source passes all
profiles with those effects enabled.

## Callback ABI and defined native domain

There are no aligned direct calls or interior entries. The sole aligned
address value is ROM231828/VA8008CD68, D_8008CD04[25]. Its consumer
func_151749F8 uses FrameLayerCallback=void(*)(s32), compatible with the
adopted definition. The complete28-entry table and43-word caller remain
unchanged and baseline byte-exact.

The caller makes three provider calls, reloads D_800B0DF0's byte+0xB,
and invokes that entry with its s32 view argument when the byte is nonzero.
Afterward it conditionally invokes two more providers and advances a
wrapping phase using the live tick word. Tests qualify reloads after those
calls, target and callback skips, an artificially changed incoming view
home, late tick changes and the final phase wrap.

The caller has **no view-range gate**; no whole-program0..25 invariant is
assumed. Native validation uses the declared26-record backing and finite,
representable height conversions. Guest checks cover negative/wrapped
indices, a record/cooldown alias, invalid height conversion, NaN/infinite
quartic values and the exact threshold boundary. These cases do not claim
portable C outside the array, hardware FCSR/NaN/trap behavior or gameplay
acceptance. No new runtime bound or clamp changes retail behavior.

## Qualification and full-image audit

- **111 frozen inputs** cover the complete owner, callback table/caller,
  Init helper source/object, original spatial helper/RNG, struct/prototype
  headers, compiler, ROM, layout/guards and linker bindings. All320 raw
  bytes and14 relocation sites are pinned. Every single-byte and binding-name
  corruption rejects, as do retail-slot, named-metadata and out-of-scope
  image corruptions.
- All **43 raw/padded neighbors**, literal pools and register-mask union
  remain fixed. Both padders agree on all44 owner functions. The actual
  **three-command Make recipe** reproduces the qualified object with zero
  compiler diagnostics. There is no neighboring helper or signature change.
- Independent whole-ELF prediction permits **339 changed bytes, zero
  exclusions**: this retail body and extent12->320, plus three closed
  symbol/string ordering permutations. They swap(D_800D98F0,func_15000000),
  rotate(D_800A191C,D_800A154C,func_1519E61C), and swap(D_80095BD8,D_8009D440).
  Every named value/type/size/section is retained. These are seven predicted
  metadata rows, not altered code/data bindings. All **6,052 function
  addresses**, other bodies and **189,088 protected bytes across720 owners**
  remain fixed, as do Makefile, guards, headers and progress CSV.
- **1,348 guest cases per body**, all80 words visited, qualify all256
  cooldown bytes, full signed ticks, wrapped subtraction, actual-threshold
  below/equal/above values, two arbitrary random words, retained output
  mutations and late public effects. Raw/retail GPR/FPR/HI/LO/condition,
  memory, calls/snapshots and access order agree literally.
- Six independent GNU links pass **30 rebased candidate cases**. **64
  paired fault prefixes** compare complete modeled state, trace, dispatched
  word, PC and delay origin. Wrapped/negative indices and the cooldown alias
  remain guest-only; retained local output pointers are valid native C.
- **384 complete caller cases per body** execute all43 caller words with
  the actual table, zero/25 descriptor selection, full view words, stack
  phases and64 provider-effect plans. The complete caller source/object and
  all28 table entries are byte-identical before and after adoption.
- **36 original-helper connection cases per body** execute all85 spatial
  helper words and all22 audio-wrapper words, both baseline exact. The
  spatial loop's inclusive count, first tie, three outputs and unsigned
  volume scale agree with an independent model. The audio wrapper forwards
  all seven words, including its live voice byte. Low-level spatial math,
  playback and RNG remain bounded providers. The RNG's18-word baseline
  is exact; this task does not claim complete64-bit RNG-state execution.
- Native32 **O0/O2/O3 each pass520 cases** through a correctly typed
  void(s32) callback. Assertions pin struct127 size812, position offsets
  20/24/28 and26 records. All record bytes/word fields and public globals,
  nine spatial arguments, live outputs, both RNG snapshots and five audio
  arguments are checked with trap UBSan. All16 semantic controls fail in
  IDO and every native profile; differing private frame-pointer addresses
  alone are explicitly excluded as a counterexample. The seventeenth,
  unsequenced control is native-only and also fails all three profiles.

Seven fresh target checks pass in both tools environments before and after
installation. Shared smoke checks are fresh; three unchanged regressions per
copy are explicitly reused by exact helper/test fingerprints. New modules
use an isolated sibling overlay; absent nested dependencies are read from
mounted tools with exact fingerprints, never written into sibling work.

Production compiles only this owner, with zero compiler diagnostics, and
agrees with prediction/recount. The inherited whole-ROM checksum mismatch
still makes make all exit2; existing duplicate Make recipe warnings remain.
Routine review uses zero Claude calls. Tools commit before consumer; sibling
tools2434 inherited dirty paths and frozen host Release stay untouched.

Graphify uses scoped AST refresh with retained-node evidence and zero
semantic API calls, not full-corpus extraction. Fresh target entrypoint:
`python3 -m unittest tools.tests.test_game_position_sound_150f20f0_match -v`
under WSL. Receipts: conker/build/game-position-sound-150F20F0-match/.
Next queue: func_15128540, subject to fresh audit and no early credit.
The80% goal remains active.

Production ELF SHA-256: 626bf98d487b9dd5167a7415bda8f316c6df245765fab9dca2a476d2af1c2226.
Guard SHA-256: 6a6094f04735cb3127833e50b21f98c3374916605acd7aa79ccdebd80d22dfe7(unchanged).
