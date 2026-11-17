# Strip-update callback private recovery and qualification - 2026-11-17

`void func_151AD174(u8 *record)` now has a complete private C draft for the
registered motion-sample strip update. Selected v20 emits **487 words**,
versus retail's **494**, with the original **frame 0x308**. All **32 owner
neighbors** and normalized constant pools remain unchanged. This is private
recovery: the production empty callback stays untouched, no guards are added,
and **no matching credit** is awarded.

Accepted totals remain **4,532 / 5,514 (82.19%)**, Game **3,859 / 4,841
(79.71%)**, Init 492/492 and Debugger 181/181, zero drift and 982 different.
**155 more matches** are needed for the active 85% goal. Root README and its
aggregate figures are unchanged. The accepted constructor is [Note 2513](2513-game-motion-sample-strip-constructor-guarded-byte-match-20261117.md).

## Complete retail window and interface

VA **151AD174..151AD92C**, ROM **1DA624..1DADDC**, 1,976 bytes. Original
instruction comments agree with the retained retail image, independently of
the compiled C. The protected `D_8008B4A8` table registers this exact routine
at descriptor +4 for classes **0x2F and 0x4E**. The complete original
`func_151671E8` secondary-list walker invokes the one-pointer void interface.
No shared struct179/struct180, provider ABI, compiler profile or production
guard is changed. The existing constructor's 88-byte record and 24-byte
sample views are reused locally.

The draft updates the signed halfword countdown at +0x52 with wrapped
subtraction and a negative-result clamp. It captures the unsigned sample
count before providers. An attached owner supplies a byte sample index,
angle and amplitude through owner+0x31C. Trig calls retain the captured
index/amplitude while reloading the live record, owner, sample pointer and
later angle at their actual boundaries. The effect's unsigned +0xAD byte
counts down and clears its float amplitude at zero. An optional +0x4C
impulse uses bytes +0x50/+0x51 and decays by the retained 0.9 float.

Two twenty-by-three float arrays retain the position and velocity snapshots.
The reverse sample loop applies gravity, 0.96 damping, the original **1.24
double-precision** smoothing, the category-0x39 X ceiling of 1150, and the
spacing constraint against the already updated next sample. The movement
score sums the absolute X and Z **velocities**. Above 250, an absent or
finished sound handle allows an unsigned random remainder modulo nine,
sound ID 0x507..0x50F and the original eleven-word submission. Coordinates
are truncated to full signed words at the call site; the sound provider
performs its own later narrowing. Its u16 result is stored at +0x54.

## An effective movement-threshold correction

The initial private draft and its initial reference both misidentified
SP+0x2E4 as the Z force. The ordered retail trace showed it is the Z
velocity. Earlier 496-case receipts passed because their movement scores
fell on the same side of the sound threshold. They are retained as rejected
preliminary evidence, not treated as sufficient qualification.

A new independent retail-backed witness starts with zero X/Z positions,
linear Y positions, no owner/impulse and Z velocity 14. Retail requests sound
with twenty samples and remains quiet with nineteen. Both old force-Z
drafts reject; the corrected draft passes. Forty-eight threshold cases
extend the complete corpus to **544**. The maintained test compiles the
incorrect body as an effective MIPS negative, rather than trusting only
the corrected reference or a literal instruction count.

## Native fixture diagnosis and repair

The first O0 native run faulted on a sample velocity store. GDB identified
a pointer corrupted by the fixture's mutation replay: it applied a changed
guest-pointer byte to an already translated host pointer. The replay now
replaces the complete canonical pointer word before translating it. The
recovered C was unchanged for this repair. The failed executable, vectors
and read-only GDB receipt remain in the ignored private directory.

Canonical fixtures retain numeric float/halfword/word fields, map only the
declared pointer fields, and compare every declared public byte at return.
After that repair, the same **544 finite cases** pass at native32 **O0, O2
and O3**, using SSE single/double arithmetic and UB traps. Four compiled
negative variants each fail as expected: force-Z movement, wrong impulse
decay, signed effect countdown and wrong smoothing coefficient. These are
native public-output/call checks, not a claim about N64 FCSR or stack bytes.

## Fresh maintained checks in both tools configurations

All **six tests** pass freshly in primary tools and the isolated sibling
overlay, with identical seven-file task fingerprints and actual imported
origins recorded. Existing instruction-model primitives are reused; the
target, guest, native, threshold and caller runs are fresh.

- Complete owner compilation checks **487 words / frame 0x308**, every
  relocation, all 32 neighbors, constant pools, both registration rows and
  the actual protected float/double constants.
- **544 guest cases per retail/raw stream** compare public memory, complete
  provider arguments and preserved registers. Cases include both stack
  phases, count 0..20, owner and impulse paths, category gates, wrapped
  countdowns, mutable providers, full unsigned PRNG outputs and audio gates.
  Sample indices stay within the allocated twenty entries. Coverage is
  **489/494 retail words and 482/487 raw words**; this is not full path proof.
- The retail threshold witness rejects the compiled old force-Z score.
- Native O0/O2/O3 and the four effective negative executions pass their
  expected outcomes, with the entire canonical public arena and calls checked.
- **64 cases per retail/raw stream** execute the complete **74-word**
  original secondary-list walker, with measured
  coverage **73/74**. Both registered classes, both rows and entry depths
  0/3 are exercised. Complete public RAM, one-pointer callback invocation,
  retained-next bookkeeping and restored depth agree. A changed callback
  pointer rejects. The list-depth field is a **signed byte**; the first
  caller fixture incorrectly initialized it as a word and was corrected
  after inspecting the original one-byte stores. Adjacent bytes are retained.
- A separate private/ordered trace deliberately records the remaining
  matching differences. It does not turn them into an acceptance claim.

The domain is fresh, disjoint mapped objects and bounded finite coordinate
fixtures, with declared mutable numeric/audio provider contracts. This does
not prove arbitrary object aliases, out-of-range sample accesses, every NaN
payload or fault prefix, hardware behavior, actual trig-table values, or
host gameplay. Full FP-status and private-state relations remain open.

## Remaining matching boundary and next work

On the sampled full path, the first six provider boundaries have identical
private bytes and ordered FP operations. At return only four private words
differ: **SP+0x7C, +0x84, +0xAC and +0xB0**. The empty-count case agrees in
private bytes and FP sequence. These are concrete observations, not a proof
for all inputs. The full-path retail trace contains **1,671 FP operations**
versus **1,669** in the draft. Retail retains `9*9` and unary negation of nine;
the draft folds them. Other operand and independent scheduling differences
also remain. Do not discard those operations or infer FCSR parity from
matching outputs, frame size or word counts.

The gravity-variable v19/v22 probes retain those two operations but use
frame 0x310, so they are not qualified replacements. Continue this same
function's original private homes, gravity operations and FP scheduling,
then qualify both padders/rebases, complete state and actual production
image before adoption and recount. There is no installable guard plan yet.

Selected raw SHA256:
`2f1cad4e327a679e0b41b167942a7b8f3b9c8609c754be0dec5450c2d330ab3d`.
Run with a fresh owned `CBFD_STRIP_UPDATE_WORK` path:
`python3 -m unittest tools.tests.test_game_strip_update_151ad174_private_recovery -v`.
Receipts are under `conker/build/game-next-151ad174-private/qualification/`.

## Baseline and preservation

Consumer **d274648f**, tools **d9cff57**. The qualification snapshot links
1,499 immutable input files and copies the seven new task files: **1,506
verified inputs**, with zero live-worktree hardlinks. All remain unchanged,
including all **698 production objects**, source, headers, compiler profile,
guard CSV and ELF. Fresh recount remains 4,532/5,514. All **189,088 protected
data bytes / 720 owners** remain exact; shared tools checks pass. Production
ELF SHA256 remains
`7c1c2f7ef67741c05a3d512530e777e9e4e4de6f29df28ebc8a22e9b95e4af90`.

The sibling's 2,434 dirty paths and 339 scoped dependencies are unchanged;
the overlay never writes there. The host path contains retained diagnostics
without a source checkout; no host, Release or save work was done. Zero
Claude calls were needed for this callback milestone. Graphify's native
update refused corpus shrink; the scoped refresh retains prior IDs. Bank
the tools before the consumer's documentation and pin. The 85% goal stays active.
