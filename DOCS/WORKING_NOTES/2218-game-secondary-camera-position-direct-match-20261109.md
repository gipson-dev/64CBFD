# Secondary Camera Position Direct Match - 2026-11-09

`func_1512E4B0` replaces its false zero-return placeholder with the original
secondary camera position/heading update. All **77 body words /308 bytes**
emit directly from C under existing **O2/g3**, retaining the **0x28 frame**.
Three original alignment words complete its80-word/320-byte retail slot.
There are **no guards, profile changes or shared header changes**.

Production: Total **4,287 /5,513 (77.76%)**, Game **3,614 /4,840 (74.67%)**,
Init **492/492**, Debugger **181/181**, zero drift; **1,226** still different.
**124** more exact functions reach4,411/5,513 and80%. Conversion rows stay fixed.

## Recovered routine

Owner conker/src/game/generated_15B960.c, original conker/asm/15B960.s.
VA1512E4B0..1512E5E4 body, slot through1512E5F0;
ROM15B960..15BA94 body, slot through15BAA0. RA is saved at SP+0x14,
the angle at SP+0x18 and the input camera at the incoming SP+0x28 home.
No S registers are saved. Recovered interface: void(struct108 *camera).

- Select D_800CC2D0[0], except camera byte+0x23D==3 selects actor1.
  The actual26-record array has812-byte struct127 stride. Other selector
  bytes use actor0; no extra bound/clamp changes retail behavior.
- Copy selected actor x+0x14, y+0x18+150.0f and z+0x1C to camera+0x2BC,
  +0x2C0,+0x2C4 in original access order. The first position store can affect
  subsequent reads in guest alias fixtures, so the reference reads live memory.
- Read the first signed halfword at actor+0x2E4. Negate, narrow with16-bit
  wrap, add the actor float+0x40 times10.0f with single-precision rounding,
  truncate to a full signed word, and narrow again to signed16 bits.
  The float's role is not assigned a new official field name.
- Convert the adjusted heading to float, multiply by D_800A3730 and divide
  by1800.0f. PI is bits40490FDB at ROM2481F0/VA800A3730.
- Call sinf with the cached angle, then reload live camera x/y. Store
  +0x2FC=y and+0x2F8=x-sine*60.0f. Call cosf with that same cached angle,
  then reload live camera z and store+0x300=z-cosine*60.0f.
  The typed float helpers receive F12 and return F0 in the original o32 ABI.
  Both results are staged in full expressions before the camera-field reads.

## Natural match and source conversion contract

The private float-order draft already had77 words/frame40, but differed in
eight F6/F10 allocation/commutative-add words after fixing the angle spill.
Materialized float temporaries and register-qualified variants did not match.
The original compound heading update recovered all77 words directly.

A short-typed compound update also emitted those same words, but C converts
its float result directly to s16. That is undefined when truncation falls
outside the short range, even when a full signed-word conversion is valid.
The adopted source keeps heading as s32 for the compound update, then applies
the original signed-halfword narrowing. It still emits exactly the same77 words.
The extra temporary-variable alternative instead grew the frame to0x30 and
was rejected. No compiler-layout guards replace the natural source recovery.

The narrow same-IDO-word form is a separate native-only negative control.
All O0/O2/O3 binaries trip the explicit float-cast-overflow trap on an input
handled by the wide source. Native validation therefore enables that sanitizer
in addition to ordinary trap UBSan; byte identity alone is not the C-domain gate.

struct127 currently declares its+0x2E4 region as s32. A local signed-halfword
alias view reads the actual first two bytes without broadly changing that
unresolved shared field. GNU compilers get __may_alias__; IDO gets the plain
s16 view, with identical words. See the
[GCC alias contract](https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html).
The native fixture writes the first native halfword explicitly and places a
distinct sentinel in the other half. It does not assume this is the low half
of a portable s32 value. Removing the annotation fails an optimized two-pointer
alias probe at O2/O3; O0 passes. The no-alias form also retains identical IDO
words and is recorded separately from the14 semantic controls.

Native inputs use real, distinct struct108 and struct127 objects; their float
sum must be finite and convertible to s32. The fixture covers valid values
outside the s16 range and signed-word boundaries, with target/GNU halfword
narrowing. Invalid float conversions, wrapped pointers, overlapping actor/
camera layouts and incoming-home mutations are guest-only. No universal ISO
portability, FCSR/NaN payload/trap behavior or gameplay acceptance is claimed.

## Caller declaration repair and actual helper connections

The aligned retail entry/interior census has one direct call, no pointer values:
ROM155A88/VA151285D8 in func_15128540's secondary bit20 branch. The caller
passes its saved original camera address and ignores the helper return, then
calls the common update/finalization handlers and returns1.

That caller now has the proper local void(struct108*) declaration and pointer
cast. All **45 raw caller functions and bindings**, pools and register info
remain fixed. Its entire padded object remains byte-identical to the prior
production object; the actual five-command caller Make recipe confirms that.
No other unfinished helper is reconstructed or given matching credit.

**768 complete original dispatcher cases per body** execute the original or
compiled child against an independent nested model. They enter the helper272
times and skip it496 times, visiting all78 reachable caller words and all77
target words. All flag priorities, predicate signs, pre-call flag mutations,
post-trig effects and ignored child-return behavior agree. Other dispatcher
handlers stay bounded providers, not recovered engine implementations.

**96 original trig-connection cases per body** execute actual retail sine and
cosine code against the independent f32 reduction/polynomial reference.
All104 sine-slot words,88 cosine-slot words and their constants are baseline
byte-exact. These cases visit93 sine and67 cosine instructions and all77
target instructions within its finite signed-halfword angle domain. This is
not a claim to cover every helper branch. The real trig bodies stay unchanged;
the separate provider camera/global mutations are deliberate ordering tests,
not an observed mutation performed by those retail helpers.

## Qualification and production audit

- **465 frozen inputs** cover both owners, real trig sources/objects, original
  assembly/PI data, production headers, compiler, pristine image, layouts,
  guards, linker bindings and imported tool modules. All308 raw body bytes
  and bindings are pinned; every one-byte and binding-name corruption rejects.
- Both independent padders agree on the one-function target owner, including
  its three original alignment words. Its actual **three-command Make recipe**
  reproduces the object without diagnostics. The caller's inherited five
  warnings(four712, one709) remain; the declaration repair adds none.
- Canonical private input basenames reproduce the predecessor ELF literally.
  Independent whole-image prediction permits only this slot and its extent
  **12->308**: **260 changed bytes, zero exclusions and no metadata cycles**.
  The caller object stays identical. All **6,052 addresses**, every other body,
  **189,088 protected bytes across720 owners**, Makefile, guards, shared headers
  and progress CSV remain fixed. Out-of-scope image and retail-padding
  corruptions reject the strict guard.
- **1,192 guest cases per body** visit all77 instructions and cover all256
  selector bytes, both signed narrowings, fractional/large/invalid adjustments,
  post-call reloads, cached PI/angle behavior and deliberate provider effects.
  Complete literal GPR/FPR/HI/LO/condition, memory, calls/snapshots and access
  order agree. **115 fault-prefix pairs**, including ten delay-slot cuts, agree.
- Six GNU links independently rebase target, helpers and data for30 cases.
  All **14 compiled semantic controls** have public counterexamples on the
  defined native-input domain. Private frame/home differences are explicitly
  excluded as witnesses. The two same-word native controls remain separate.
- Native32 **O0/O2/O3 each pass433 cases** through a typed void(struct108*)
  callback, real26-record backing and strict aliasing. Assertions pin the812-
  byte actor,0x9A0-byte camera and every accessed field offset. All actor,
  camera/alternate-camera and PI bytes plus both helper snapshots are checked.
  All14 semantic controls fail in every native profile. No global alias
  option or float-cast overflow check is disabled.

Six focused checks pass in both tools environments before and after installation.
Fresh shared smoke runs accompany three exactly fingerprinted shared regression
reuses per copy. All isolated sibling-overlay dependencies and absent-file
fallbacks are recorded read-only; sibling2434 inherited dirty paths stay intact.

Production recompiles exactly the target owner and its declaration-repaired
caller, matches the independent ELF/object forecasts and recounts the actual
ELF. The inherited whole-ROM checksum mismatch still makes make all exit2.
The old duplicate Make warnings and five unrelated caller compiler warnings
remain. Routine review uses zero Claude calls. Tools commit before consumer;
host Release stays frozen. Graphify gets a scoped AST refresh with explicit
retention proof, not a full-corpus semantic extraction.

Fresh focused entrypoint under WSL:
python3 -m unittest tools.tests.test_game_secondary_camera_position_1512e4b0_match -v
Receipts: conker/build/game-secondary-camera-position-1512E4B0-match/.
Next queue: func_151563B8, subject to a fresh audit and no early credit.
The80% goal remains active.

Production ELF SHA-256: e494c3e480f462220135024ccdc70e96525b06df8aea2a83c926eacbe65a0528.
Guard SHA-256: 6a6094f04735cb3127833e50b21f98c3374916605acd7aa79ccdebd80d22dfe7(unchanged).
