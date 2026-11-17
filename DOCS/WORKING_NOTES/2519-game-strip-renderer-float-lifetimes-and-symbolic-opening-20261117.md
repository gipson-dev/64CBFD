# Strip renderer float lifetimes and symbolic opening - 2026-11-17

Private `func_151AD92C` v49 now recovers retail's six saved FP roles and
current Y/Z stack homes. It emits **469 words / frame 0x130**, against
**464 retail words / frame 0x130**. A **six-path symbolic opening relation**
passes after moving two scalar homes. The complete function remains private
and uncredited: five extra words, later FP scheduling and provider-frame
differences still need work. The earlier semantic baseline is
[Note 2518](2518-game-motion-sample-strip-renderer-private-recovery-20261117.md).

Accepted progress stays **4,533 / 5,514 (82.21%)**, Game
**3,860 / 4,841 (79.74%)**, Init 492/492 and Debugger 181/181, zero drift.
The active 85% goal still needs **154 matches**. Root README is unchanged.

## Source lifetime recovery

Owner `conker/src/game/generated_1D92F0.c`, VA151AD92C..151AE06C,
ROM1DADDC..1DB51C. The three-word callback, eleven-word texture provider,
unsigned field widths and SDK graphics semantics retain their prior recovery.

A real `currentYZ[2]` snapshot retains Y atSP104 and Z atSP100 while a
captured sample pointer avoids reloads of the record's point pointer after
local array stores. The current Y/Z values become the tangent components
after their position snapshots are retained. The initial X value is captured
once in the subsequently reused normal-X carrier and retained separately for
vertex output. These are real values and existing computations; no padding,
volatile declarations, dummy operations or compiler-profile changes are added.

At the first norm, v49 has the original roles: F20=zero, F22=deltaX,
F24=negativeY, F26=squareY, F28=four and F30=currentX. The first observed
nonempty FP-order mismatch moves from observation16 in v10 to observation19:
retail's Z addition versus the candidate's independent X subtraction.

A qualified mode5 capture of v10 preserves all 33 owner functions, bindings
and pools through the prepared normal compiler/GDB route. Its named-function
scope has 42 variable rows and 100 allocation rows, with producer/driver exit0.
Final integer colors/interference sets are retained; suppressed floating
diagnostic costs and times are not interpreted as evidence of allocation order.

One packet-only Claude review used the existing Pro/firstParty route, safe
mode, empty effective tools/MCP and no tool calls. Its packet contained one
incorrect premise: v35's saved-unity observation was carried forward to v36.
Direct execution shows v36 already drops saved unity and retains negativeY
in F24; v38/v41/v49 recover all six saved roles. The claim that dead-length
reuse caused unity hoisting is rejected. Packet, answer, receipt, corrected
observations and reconciliation remain ignored evidence. No second call was
made, and advisory agreement is not used as qualification.

## Partial symbolic relation

The derived stream changes only six checked stack operands, moving texture
shift SP120->SP118 and height-minus-one SP124->SP11C. Three stores occur in
the opening and three loads occur later. There are no inserted or omitted
instructions in this partial transformation, and no production guard rows.

The instruction-driven relation covers **six paths**, ending at the first
norm comparison on four paths or empty-strip setup on two. At those boundaries
it compares every **320 private/incoming-home bytes**, ordered FP operations,
their abstract status/condition transitions, stable public read multisets and
the required scalar/pointer/FP live roles. The original input/tangent values
and coordinate snapshots remain symbolic. This proves the opening only;
the later stores, row backedge and provider boundary remain outside the relation.

An independently renamed T6/T7 allocation passes all six paths. Seven controls
reject three incorrect opening homes, next-X stride, narrowed viewport store,
absolute instead of negative Y, or reversed norm-add operands. The three later
loads have separate effective finite rejection controls; their whole-function
symbolic relation remains open.

## Fresh qualification and retained limits

All **six final tests pass fresh in both tools configurations**, with no skips:
**122.210s primary / 126.148s sibling-overlay**, including fingerprint/import
recording. The final suite restores its shared engine bindings before returning.

- Complete owner compilation pins v49's raw bytes and relocations. All 32
  neighboring functions and normalized pools remain unchanged.
- **544 cases per retail/raw/home-adjusted stream** compare every declared
  public byte, all eleven provider arguments, returned pointers and preserved
  GPR/FPR state. Coverage is464/464 retail and469/469 in both derived streams.
  Moving the scalar homes preserves the complete raw FP trace.
- Full ordered FP agreement still holds only in the 20 empty cases out of 544.
  The matrix contains 306,846 retail FP observations. Complete provider frames
  agree in 0/544 cases, so the opening proof is not whole-function acceptance.
- The original 348-word caller and 47-word selector pass 64 literal-descriptor
  cases plus four separately labeled alternate-layer cases per source stream.
  Caller coverage 323/348 and selector coverage 13/47 retain their prior scope.
  Signed viewport forwarding, returned cursor, list retention and budget
  rollback agree; a wrong callback-record control rejects.
- Exact selected C/SDK macros pass 544 native32 cases at O0/O2/O3 with strict
  aliasing and UB traps. Four additional native runs reject wrong fallback,
  texture shift, helper-tail argument or captured-count reload behavior.
- Three stale later-home-load controls reject; the seven opening controls and
  independent allocation positive run in both tools configurations as well.

The scope remains finite guest/native disjoint objects plus the symbolic
nontrapping opening with stable public reads. No arbitrary stack aliases,
literal fault state, cycle timing, hardware or host gameplay acceptance follows.

Baseline consumer **802adcc6**, tools **8e99b18**. The **1,532-input** immutable
snapshot uses 1,525 prior-snapshot links and seven copied previous task files;
an identity check confirms zero live-worktree hardlinks. Every input remains
unchanged. The sibling's 2,434 dirty paths and 339 present scoped dependencies
are preserved. Actual imports are 338 distinct primary files and 340 distinct
overlay-run files; overlay rows are 5 adapters/task modules, 301 sibling and 36
primary fallback rows. Input, import and paired-report checks are sealed.

Production source, guard CSV, owner object and ELF remain unchanged; no Make
or whole-image adoption is claimed for this private candidate. Production ELF:
`9a3fca4a18c45119a77ad987895ba93c8f600ab46acbad5513147499567074b3`.
Selected raw SHA256:
`0418af51e8fc3f1b5c9632de208a59f57b41e57a8844f365c690a2e47ebbb6c1`.

## Continue this renderer

- [x] Recover the real FP lifetimes and coordinate snapshot homes.
- [x] Prove entry through the first norm, including full private bytes there.
- [x] Requalify complete public behavior, original caller and SDK32 C.
- [ ] Recover later ordered FP operations and prove the generic sample row,
  loop-live roles, remaining private homes and opaque-provider boundary.
- [ ] Remove the five-word excess through recovered source/normalization,
  then qualify both padders, independent GNU rebases and corruption checks.
- [ ] Complete actual Make, strict full-image prediction, protected data and
  address audits, actual ELF recount, documentation and production commits.

Run `python3 -m unittest tools.tests.test_game_strip_draw_151ad92c_lifetime -v`
with a fresh owned `CBFD_STRIP_DRAW_LIFETIME_WORK` path. Final paired reports
are in ignored `conker/build/game-next-151ad92c-private/lifetime-qualified/`;
the earlier semantic receipts and all experiments remain retained.
The local `64CBFDOGL` has no source checkout for applying this private work;
its frozen Release artifacts and saves are untouched.

The native Graphify update retains the existing graph after refusing a smaller
replacement. Scoped extraction covers the three new Python files, preserving
all 64,703 prior IDs and adding an explicit lifetime-recovery reference. This
is not full-corpus extraction; final hook/retention receipts stay in the packet.
