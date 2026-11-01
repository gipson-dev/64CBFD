# Height-gated vertical velocity restored directly from C

`func_1506BCC8` emits all **72 retail words directly from C**, with the original
24-byte frame and no guards, assembly inserts, omissions or compiler-profile
change. Its complete 288-byte slot is exact under the existing O2/g3 profile.

Production Make and the live Windows-checkout recount agree on **4,020/5,506
(73.01%)**, Game **3,347/4,833 (69.25%)**, Init 492/492 and Debugger 181/181,
zero drift and 1,486 different. **110 more matches** are needed for the active
4,130/5,506 threshold. Tools were committed first at `205d1c3`.

## Recovered operation and interface

Owner/source `game_981E0`, `conker/src/game_981E0.c`.
VA **1506BCC8..1506BDE8**; ROM **99178..99298**.
The false no-argument integer-return placeholder becomes
`void func_1506BCC8(void)`. Its only aligned ROM pointer reference is
D_800863FC[2], at VA80086404 / ROM22AEC4. There is no aligned direct JAL or
second pointer literal. The original indirect caller ignores the result.

For interaction_state 22, the actor's y_position must equal reference-height
field +0x180 exactly. Call the existing signed random helper and take signed
remainder by 8. Add that remainder to the live command word D_800D1580 with
32-bit wrap, interpret the sum as signed and convert it to float. Store the
result to current actor y_velocity (+0x20), then reload current actor.
If its xz_velocity is nonzero, multiply y_velocity by **xz_velocity / 40.0f**,
with a separately rounded division before multiplication. Otherwise store
positive zero. The actor and command word are reloaded after the helper;
state/height conditions are not rechecked on a helper-selected replacement actor.

For other interaction states, subtract reference height from y_position in
binary32. Only a difference strictly between -5 and +5 sets y_velocity to
signed D_800D1580 converted to float. Exact boundaries, unordered comparisons,
and out-of-range differences leave velocity unchanged. Shared headers remain
unchanged; a local signed no-argument prototype describes the existing helper.

The source uses explicit unsigned addition followed by a signed cast to preserve
the retail word wrap without native signed overflow. A combined random-call
expression and the recovered comparison shape emit the original schedule and
register allocation naturally. There is no volatile, filler or word patch.

## Compiler, owner, Make and complete image

The isolated C is warning-free. Raw body SHA-256:
`7ac56b788c854481e4c10b829530f2cc4fa4cc4fbcc4cbd02a507199bcadf9e0`.
All 9 raw relocation fields and body words match the original assembly.
All **327 other raw/padded owner functions** and owner pools remain unchanged,
including the actor lookup, health command and random choice. The 36 inherited owner warnings
are unchanged. The actual five-command Make recipe emits the qualified padded
object byte for byte. Makefile, word guards, layout and C conversion inventory
are unchanged. Shadow linking preserves the original object basename for its
synthesized overflow FILE symbol.

An independent literal whole-image prediction changes only the target slot and
symbol extent from 12 to 288 bytes: **208 changed bytes**, with no exclusions or
metadata reordering. All **6,056 function addresses**, **6,055 other linked
bodies**, and **189,088 protected Game data bytes / 720 owners** remain fixed.
Production ELF SHA-256:
`c5481db684aba3e151677335b0274e567bfcfe4b20fcbb1f79fba9ce204071da`.
Native installation changes exactly source, padded owner object and ELF.
All other prior **17,527 sealed inputs** remain unchanged before the explicit
new tools/documentation refresh. **1,008 focused inputs** are frozen.

## Original helper, instruction and native qualification

- **3,963 guest cases / 15,852 executions** compare original assembly,
  isolated C, padded owner and actual Make object at three code/global layouts.
  Memory, ordered accesses, registers, floating registers, helper observations
  and saved state agree across the four programs.
- All **71 reachable words** execute. The duplicate height load at +0xBC
  follows an unconditional branch and is structurally unreachable; it remains
  present and is not counted as executed.
- **144 cases / 576 executions within the totals** connect the complete
  original **11-word func_151EF610**. All helper words execute. For seed s,
  t=4*s modulo 2^32 and the new seed/result is the low-word product of
  (t+2)*(t+3), shifted right two. Eight seed patterns, speed classes and signed
  command values verify the stored seed and returned result. This helper is
  executed unchanged as assembly; it is not adopted as C or separately credited.
- The original helper always returns a nonnegative word after that shift.
  Separate adversarial signed helper results exercise the retail compiler's
  negative-remainder paths. Other provider cases retarget current actor and
  change command/speed after the original actor passed its gates. They also
  clobber caller-saved registers, float registers and outgoing homes.
- A guest-only current-pointer/velocity alias makes the first float store
  select a different aligned actor. A separately compiled cached-actor control
  fails this case. Its frozen object stays immutable while fresh controls
  compare payload and bindings before execution.
- **96 cases / 1,536 executions** qualify the original 19-word indirect
  dispatch window at VA1506AEB0..1506AEFC and callback slot 2. Four injected
  callback-return values are ignored before v0 is overwritten. Both script-index
  paths, including the caller's own +0x138 increment, are checked. This is not
  a full dispatcher reachability/gameplay claim.
- **1,320 native cases each at O0/O2/O3**, with UBSan, structure-offset assertions
  and seven effective controls: wrong state, inverted exact-height gate,
  unsigned remainder, inclusive proximity boundary, inverted zero-speed gate,
  cached actor and reassociated float multiplication/division. In particular,
  step 17 and speed 3 distinguish divide-then-multiply from multiply-then-divide.
- Signed zero, neighboring height boundaries, infinities, quiet NaNs, subnormal
  samples and wrapping integer extremes are included. NaNs are compared by
  class in the reference/native checks; exact guest-program states still agree.
  The oracle does not model hardware FCSR flags/modes or prove visual acceptance.
- Both tools copies pass six fresh tests before and after installation, plus
  shared checks. Body/binding and literal-image corruption controls reject
  changes. Prior unchanged neighbor suites are reused through exact body/pool
  identity and are not reported as freshly executed.

## Artifacts and next boundary

`conker/build/game-height-gated-velocity-1506BCC8-match/` retains frozen inputs,
source screens, original/selected/owner objects, Make commands, independent first
link, original-helper execution, caller census, runtime qualification, immutable
negative object, installed recount, Graphify proof, seals and bank receipts.
Public modules are `game_height_gated_velocity_match.py`,
`game_height_gated_velocity_oracle.py` and `test_game_height_gated_velocity_match.py`.

Graphify receives an eleven-file scoped AST refresh preserving prior nodes and
valid edge occurrences; the two obsolete integer-return edges are archived.
No full-corpus extraction or reclustering is claimed.

Next ordinary C placeholder: **func_1506D958**, same owner, VA1506D958,
ROM9AE08, 72 words and no frame. Audit its packed command-byte extraction,
actor-pool scan, caller interface and writes before reconstruction. Scalar
smoothing and other private stages remain uncredited. No Claude calls,
host/editor/Release changes or network push.
