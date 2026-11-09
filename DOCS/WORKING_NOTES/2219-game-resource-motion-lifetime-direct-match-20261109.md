# Game resource motion and lifetime: direct match - 2026-11-09

func_151563B8 replaces its zero-return placeholder with the resource update
callback for types44 and83. All **80 body/slot words** emit directly from C,
with frame0x18, RA atSP+0x14, no saved S registers, no padding, no guards and
the existing O2/g3 compiler profile. All25 raw/padded owner neighbors remain
fixed. Source: conker/src/game/generated_183640.c.

Production total **4,288 / 5,513 (77.78%)**, Game **3,615 / 4,840 (74.69%)**,
Init492/492, Debugger181/181, zero address drift and1225 still different.
**123** more accepted matches are needed for80%. The wider goal stays active.

## Original routine and interface

VA151563B8..151564F8, ROM183868..1839A8, original conker/asm/183640.s.
The full aligned retail-file census finds only two entry values: ROM230858 /
VA8008BD98 and ROM231044 / VA8008C584. They are offset0 in the0x34-byte
D_8008B4A8 entries44 and83. No J/JAL encoding or literal interior address
points into the320-byte slot. Census results are tied to the frozen retail hash.

The original74-word func_151670C0 dispatches offset0 callbacks with one resource
pointer in A0, stores the next link in the JALR delay slot and reloads that
pending link after the callback. It ignores the return register. Its two row
passes each cover101 types. The existing struct115 callback type is
void(struct102*), so the restored definition uses that ABI without changing
shared headers, registries or caller source/object. Unrecovered callers stay
uncredited; the connection check runs their complete original assembly.

The original constructor func_15156190 selects type0x2C or0x53, obtains
arg2+0x98 bytes through func_15167A68, copies both triples at10..18 and28..30,
sets the six motion increments at1C..24 and34..3C, and initializes flags40,
remaining42, alpha4C, fadeStart4E and fadeRate50. Static original constructor
and allocator traces establish this local layout; a full constructor/emulated
allocator execution is not claimed. Allocation bounds require a valid input
size, and no universal struct102 subtype or layout repair is inferred.

## Recovered C behavior

Flag1 subtracts the full32-bit D_800BE9E4 tick count, stores low16 bits, then
tests the signed-halfword reload. A negative remaining value expires the record.
Explicit unsigned subtraction preserves retail SUBU wrapping without signed C
overflow, including INT_MIN ticks. Conversion to signed16 follows the measured
IDO/GNU representation; no implementation-independent signed-narrowing claim.

Non-expired records update six float components using D_800BE9A4. The six global
loads remain independent. The original flag8 read precedes the float stores,
and the last float store occupies a branch delay slot. Optional fading runs
only when signed remaining < signed fadeStart. The signed16 product is narrowed
to signed16 before comparison to the unsigned alpha byte; a smaller value is
stored as a byte. There is no clamp: negative narrowed values can wrap into
the byte. The signed16 multiplication itself fits signed32 range.

Expired records skip motion/fade and call func_1516972C with the original pointer.
There is no post-call record access. That helper prunes traversal state and
dispatches a type-specific removal callback or fallback; it is not renamed as
a simple free. The connection test deliberately leaves that provider opaque.

ResourceMotion183640 is a local0x54-byte partial view. The descriptive field
names identify measured offsets; they are not purported retail type names.
GNU may_alias qualifies access over the generic resource storage. Native tests
use actual0x1D8-byte struct102 backing, layout assertions and a typed callback.
The relevant GNU alias semantics are documented in
[GCC Common Attributes](https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html).

## Qualification evidence

- **1,278 guest cases per body** cover every flag byte, timer/tick sign and
  wrap boundaries, fade equality, signed product narrowing, zero/negative/large
  steps, post-removal effects, guest-only global aliases and wrapped pointers.
  An independent memory reference checks complete public bytes, calls and
  call-time record/global snapshots. All80 original words are visited.
- **147 fault-prefix pairs**, including eight branch-delay cuts, compare literal
  retail and emitted words. Retail symbol rebases use a separate fixed-offset
  patcher; source relocation bindings are checked independently. Complete
  literal GPR/FPR/HI/LO/condition, memory, calls and access traces agree.
- **320 complete original dispatcher cases per body** use the actual retail
  registry, both rows and101 types, empty/skipped/linked lists and effects that
  invalidate record contents or alter the pending link. They make568 target
  callbacks and104 removals, visiting all74 caller and80 target words.
- Native32 O0/O2/O3 each pass **1,252 cases** with strict aliasing, contraction
  disabled, UBSan traps, complete record/global byte comparisons and call-time
  snapshots. Ten compiled semantic controls have public counterexamples in
  every native profile and in the MIPS oracle. Private frame/home changes do
  not count as witnesses.
- The also-byte-identical signed-subtraction control traps on native overflow
  in all three profiles. Removing may_alias preserves IDO words/bindings but
  breaks the explicit alias probe at O2/O3 (O0 passes). These two native-only
  controls are recorded separately from the ten semantic controls.
- Six GNU links independently rebase target/helper/data for30 cases. All raw
  bindings and original literal words agree. Both owner padders, pools and
  all25 neighbors agree; the actual three-command Make recipe reproduces the
  expected object. Six existing owner warnings persist, with zero new warnings.
- The independent whole-ELF prediction permits only this target body and its
  symbol extent12->320. **233 bytes change, zero exclusions, zero metadata
  permutations**, all6052 function addresses fixed and no other body change.
  Protected data and all guards/conversion rows remain fixed.

The bounded IEEE-single models and native finite-input domain do not establish
N64 hardware FCSR, NaN payloads, exception handling or gameplay acceptance.
Guest aliases/fault probes are separate from portable native C semantics.
Two early dispatcher-fixture issues were corrected before formal qualification:
the provider marker overlapped the test stack, and a fixture mode name collided
with a base-oracle attribute. They were harness defects, not production defects.

## Production and repository state

Five focused checks pass before and after installation in both tools environments.
The sibling runs use an isolated six-module overlay, explicit consumer roots and
fingerprinted read-only dependencies/fallbacks. All2434 inherited sibling dirty
paths are preserved. Fresh shared smoke runs accompany three exactly fingerprinted
shared regression reuses per copy; those reused checks are not fresh runs.

Production rebuilds only the target owner and exactly matches the independent
object/ELF prediction. Actual ELF recount supplies the accepted numbers above.
The inherited whole-ROM checksum mismatch still makes make all exit2. Existing
Make recipe warnings and six unrelated owner compiler warnings remain.
No shared declarations, guard profiles or host-port Release artifacts change.
Routine review uses zero Claude calls. Tools commit before consumer; no push.
Graphify receives a scoped AST refresh with explicit old-node retention, not a
full-corpus semantic extraction. Root README changes only aggregate rows.

Focused check under WSL:
python3 -m unittest tools.tests.test_game_resource_motion_151563b8_match -v
Receipts: conker/build/game-resource-motion-151563B8-match/.
Next queue: audit func_15157DEC; it remains uncredited until all gates pass.

Production ELF SHA-256: abaeb7625c627ac608923eb852fd703328e3ceb2e56ccd6bb216c56858415fac.
Guard SHA-256: 6a6094f04735cb3127833e50b21f98c3374916605acd7aa79ccdebd80d22dfe7 (unchanged).
