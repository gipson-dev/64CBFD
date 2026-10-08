# Game Actor Event Dispatch Match

Date: 2026-10-06
Baseline: `ed507ac5` ([Note 1056](1056-game-piecewise-envelope-match-20261006.md)).

## Source And Compiler Recovery

Replace the false zero-return `func_151416E8` and its local prototype in
[`game_16DC80.c`](../../conker/src/game_16DC80.c). Recovered signature:
**`void func_151416E8(u8 *actor, u8 *event, u8 command)`**. Complete
**55 words / 220 bytes**, frame **0x18**, VA **0x151416E8..0x151417C4**,
ROM **0x16EB98..0x16EC74**, existing **O2/g3**. All words compile directly;
**no guards**, copied assembly, insertion, omission, profile or shared-header
change. Callback type and `D_8008A02C` declaration remain owner-local.
Cleanup adapts to the SDK's `struct102 *` type locally.

Preserve two volatile reads of the selector byte at actor+0x168, and two
independent callback-table lookups. The first pointer only gates dispatch;
the second is the actual call target. Forward actor, event, and the low byte
of command. After the optional callback, commands0x22/0x24/0x25 compare the
live event byte with actor+0x168. On equality: call `func_1516972C`, store
signed byte-1 at actor+0x169, or store byte2 there. Other commands do not
dereference the event. Retain unchecked second-target behavior, not a new
second null check. Void C has no scalar-return contract; guest V0 equality
is tested separately and is not presented as a native return value.

An inner switch, signed status stores, and repeated volatile selector reads
recover the complete callback prefix and55-word frame, but ordinary pointer
addition leaves ten real tail differences. Use the explicit **unsigned N64
address subtraction** `payload = (u8 *)((u32)actor - (u32)-0x110)` to retain
the payload base and retail branch/delay lowering directly. Ordinary/signed
pointer forms remain ten words different. This is deliberately32-bit guest
address arithmetic, not a portable64-bit pointer idiom. Native qualification
uses a real32-bit executable and valid allocated storage.

[Maintained driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_actor_event_dispatch_candidates.py):
eight source forms/four profiles, **32 controls**, actual SDK, empty diagnostics.
Only selected and equivalent unsigned-hex subtraction under O2/g3 are exact.
No driver installation. Historical16 initial controls remain intact. Ignored
families add32 selector/table/status/switch,16 tail,16 flow,16 payload-type,
32 ABI,48 address/profile, and16 subtraction/SDK controls. Their overlapping
forms are not claimed as a unique-source-form count.

## Qualification

[Nine tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_actor_event_dispatch_match.py):

- **60724 guest cases / two bodies**, actual compiled C and retail instructions:
  full external storage, ordered owner accesses/call records, saved GPR/FPR/
  SP/RA and incidental V0 agreement. **53/55 words reached**; the unreachable
  switch-default branch/delay at15141790/15141794 is not artificially forced.
  The complete55-word identity independently binds those instructions.
- **27648 selector/command-class cases**: every selector byte, nine command
  classes, three callback-table modes, match/mismatch and two SP phases.
- **32768 all-command mutation/alias cases**: every command byte, four selector
  boundaries, eight callback mutation modes, event/selector/status/table-byte
  aliases. Callback effects and all fixture storage are compared independently.
- Remaining **308 cases**: live selector/table changes between lookups, saved
  actor/event/command-home callback mutations, wrapped guest addresses and
  noneligible commands with a null opaque event. Saved-home/volatile-provider
  probes are guest-only evidence, not legal native private-frame alias claims.
- **262144 actual32-bit native C cases**:196608 every selector/command pair
  across three table modes, plus65536 mutation/alias/match cases. Independent
  reference, full actor/event/table storage and ordered callback snapshots.
  Native table-byte aliases use native little-endian object representation;
  this is not an assertion that native and N64 pointer bytes are identical.
- **Nine compiled semantic negatives /90 cases each**: placeholder, command
  gate, event gate, selector/status offsets, status values, cached callback,
  and word-wide command. Every negative changes storage/calls or faults on a
  strict mapped access/invalid target; unsupported ISA never counts as rejection.
- **Six invalid-second-target setups / two bodies** fault at the modeled call
  boundary. No execution of undefined native function pointers or hardware
  exception claim. Callback and cleanup are bounded mutation models, not
  connected acceptance of their complete implementations or gameplay.
- Production source/prototype, full slot, unchanged10760-row guard file and
  raw object HI16/LO16/call relocation records are bound explicitly.

Initial five-method pre-install invocation: four pass, native harness fails
`-Werror=misleading-indentation` before execution. Fix the harness formatting;
the subsequent four-method exhaustive invocation passes in83.944 seconds.
The original invocation is not claimed green.

The first bare `make` invocation checked an already-current object instead of
the ELF. The audit correctly rejected its unchanged target. Rebuild explicitly
with `make -j4 VERSION=us build/conker.us.elf`, then rerun the audit successfully.
No build receipt from the bare command is used as acceptance.

Audit against `ed507ac5`: only **`func_151416E8`** changes across **6059 fixed
slots**, no address/extent changes. `.init`, `.init_data`, `.debugger`,
`.game_data` unchanged; **720 owners /189088 Game-data bytes** retail-exact.
All **10760 guards unchanged**, none for this function. Owner warnings **0->0**,
zero new warnings. Target SHA-256:
`afbaf438a8085a1ebd1357f97d7454a578ebb8935c1d8cefc85436724e5e5a49`.

Converted counts/bytes unchanged: **5464/6042**, Game **4791/5321**;
**85.57% total /84.89% Game** converted bytes. Exact **3334/5464 (61.02%)**,
Game **2661/4791 (55.54%)**, **2130 different**, zero drift. Init492/492 and
Debugger181/181 exact unchanged. Root README changes aggregate rows only.

All **28 focused post-link tests pass in246.167 seconds**, no skips: nine new,
complete nine-test retained envelope suite, and ten retained production/metadata
methods. Not a rerun of every historical suite. Ignored build/audit/after,
controls/behavior/negative/regression receipts live under
`conker/build/game-actor-event-dispatch-test/`.

**39 documents /3432 relative links /zero broken**; compileall and diff checks
pass. All required build/test sessions terminate successfully before checkpointing.

## Next Work And Boundaries

Next **`func_1514182C`**, **63 words /252 bytes**, frame **0x80**, VA
0x1514182C..0x15141928, ROM0x16ECDC..0x16EDD8. Its source-coordinate copies
populate the local4x4 matrix's translation row, not three unused temporaries.
Build rotation from angleX/zero/angleZ, transform (zero,height,zero) into actor
position, then compute three output coordinates using live origin, scale and
the original ordered multiplications by500. Return the transformed X value.
Height must forward float bits to `func_150A7960`; review the current integer
prototype and `func_15141928` caller together. Matrix helper/live callback
effects, alias behavior, arithmetic rounding, return and ABI need qualification.
The placeholder and caller remain untouched; initial controls are ignored
investigation only, not source installation or semantic acceptance.

Ignored `next-position.py` screens two matrix representations, float/integer
height and four profiles: **16 controls**, empty diagnostics. Float-height
O2/g3 emits **63 words/frame0x80/31 differences**; integer-height emits
**66/frame0x80/54 differences**. No next-function word guards or installation.
The first adapted scratch screen misreported frames after an overbroad numeric
replacement also changed its16-bit mask. Preserve that receipt as
`next-position/measurements-incorrect-frame-mask.json`; correct the replacement
and recompile all16 controls. Only corrected `measurements.json` supplies these
frame measurements; neither invocation is semantic/native qualification.

No sibling source/build/save/frozen Release, runtime launch, host adoption,
hardware/FCSR/gameplay or push change. Continue the Game matching goal.
