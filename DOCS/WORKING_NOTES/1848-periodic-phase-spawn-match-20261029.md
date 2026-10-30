# 1848: Periodic phase spawn match

Date: 2026-10-29. Target `func_150D2374`, owner `generated_FF5C0`.
Body VA `0x150D2374..0x150D2448`, ROM `0xFF824..0xFF8F8`: **212 bytes / 53 words**.
The classifier slot extends through ROM `0xFF900`: two existing zero alignment
words follow the body. They are preserved padding, not compiler instructions.

The zero-return placeholder becomes `void func_150D2374(u8 *owner)`. The
periodic state starts at owner+0x28: unsigned base delay and delay range,
signed timer, signed 16-bit base lifetime and lifetime range, two float
durations and two unsigned color bytes. The timer at owner+0x30 subtracts
`D_800BE9E4` with explicit low-word wrap and signed interpretation. A
nonnegative result returns without reading the remaining state or calling
helpers. The updated timer is stored before the first helper on expiry.

On expiry, the unsigned bits returned by `func_150ADA20` select a lifetime
using an unsigned remainder by signed16(lifetimeRange)+1, then add the signed
base lifetime and narrow to s16. Existing matched `func_150D2110` receives
seven arguments: lifetime, two float durations, two unsigned color bytes,
owner priority byte+0xC and owner byte+1. A second PRNG call selects the next
timer using unsigned remainder by delayRange+1 plus baseDelay.

Both PRNG results are assigned in separate statements before subsequent
state reads. Native helper-mutation tests rejected the preliminary single
expression because C permits reading its divisor before the call. Explicit
sequencing preserves the retail live-field behavior across IDO and native
compiler profiles without changing any of the 53 emitted instruction words.

All 53 words and five relocations emit directly with the existing O2/g3
profile. The original 64-byte frame saves S0 at+40 and RA at+44, preserves
the state pointer at+52 across helper calls and supplies 28 outgoing bytes
for seven O32 arguments. No incoming argument homes are used by the target.
There are no guards, insertions, omissions, frame adjustments, profile changes
or shared-header edits. Inventory CSV and guard manifest bytes are unchanged.

- Eight fresh qualification methods pass independently in each tools copy,
  plus shared checks. Production reruns two installed methods per copy;
  six unchanged semantic checks are reused only by complete fingerprint
  identity. The older mirror's 1,982 inherited dirty paths are preserved;
  exactly three new qualification files are added there without committing it.
- Guest: **7,584 cases / 22,752 original/raw/padded executions** agree in
  literal full state and cover all 53 body words. Normal paths cover 51
  words; the two original `break 7` words are covered by bounded trap cases
  at offsets+0x78 (492 cases) and+0xB8 (524 cases). Zero-divisor HI/LO handling
  is an explicit guest-model boundary, not hardware behavior or native C
  acceptance. Native tests exclude reached zero divisions.
- The corpus checks signed timer and lifetime boundaries, unsigned remainders,
  32-bit wrap, all 256 values of each forwarded byte, signed-zero/subnormal/
  finite/infinity/quiet-NaN float argument bits, helper clobbers and state
  changes after each call. Float payloads are forwarded without arithmetic.
  There are 111 access-prefix comparisons, three sparse non-expired runs,
  and three alternate layouts / 144 rebased cases.
- Native32 O0/O2/O3 each pass **3,284** defined-input cases with UBSan.
  Eight deliberate defects are rejected on 2,524 fixtures safe for all
  controls: inclusive expiry boundary, division instead of remainder,
  lifetime narrowed to s8, swapped durations, wrong color, wrong priority,
  timer used as reset base, and a delay range cached before helper calls.
  Full actor bytes, global ticks, helper arguments/order and pre-call state
  observations are checked, including fields changed by helper stubs.
- Full-ROM scan finds no direct JALs and exactly one aligned pointer at
  ROM `0x22F068` / VA `0x8008A5A8`: **`D_8008A4E8[48]`**, in
  `conker/asm/data/22EF80.rodata.s`. This is the effect-update table;
  the separate preceding cleanup table `D_8008A4C0` is not its base.
- Actual parent `func_15149264` in `game/done/game_1765E0.c` dispatches from
  signed update byte owner+0x11. Its original 11-word window at VA
  `0x15149290` / ROM `0x176740` runs 48 cases and returns through
  `0x151492B8`, restoring owner from its caller home. Six executions check
  update byte -1 skips the callback. The earlier lifetime gate and later
  cleanup remain preconditions. A preliminary generic actor callback window
  was discarded; no complete parent, real PRNG/factory or gameplay execution
  is claimed by the bounded helper/caller model.
- Complete-owner compile/padding preserves six neighbors and pools, including
  already matched phase factory `func_150D2110`; three actual Make commands
  reproduce the exact object with zero C diagnostics. The inherited Make
  duplicate-recipe warning remains. All 217 raw-byte/binding controls and
  240 whole-image corruption controls reject.
- Independent prediction equals the production ELF: **145 changed bytes =
  144 target-code bytes + one symbol-extent byte**. The new symbol size is
  212, with the eight alignment bytes preserved. No metadata changes or
  exclusions. All 6,055 other linked bodies and all addresses remain fixed;
  protected Game data is exact across 189,088 bytes / 720 owners.

Fresh adopted-ELF count: **3,925/5,506 (71.29%)**, Game **3,252/4,833 (67.29%)**,
Init492/492 and Debugger181/181, zero drift. **205** more to 4,130.
Tools committed first: `992d9db958efd56e2c064d3eae8f6ed48ad660b1`. No push. Root README gets aggregate rows only.

The scoped eleven-file AST refresh retains or uniquely relocates all 50,005
prior nodes and preserves all 103,669 valid old directed relationships. One
obsolete s32 return relationship retires for the recovered void interface.
The actual registration/caller and helper bindings are separately recorded.
Outside manifest rows and analytics remain historical; no full-corpus claim.

Artifacts: `conker/build/game-periodic-phase-spawn-match/`. Next screened
target `func_15030F94` still needs full qualification. Other private candidates remain
uncredited. No host-port, frozen Release, save/editor, private-input or memory
changes. Zero Claude calls. The 75% matching goal remains active.
