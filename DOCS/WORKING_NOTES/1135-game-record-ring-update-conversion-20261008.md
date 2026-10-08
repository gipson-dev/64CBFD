# Game Record Ring Update Conversion

Date: 2026-10-08

## Result

Continue [Note 1134](1134-game-attachment-allocation-direct-conversion-20261008.md)
under the [focused workflow](../AGENT_WORKFLOW.md). Convert retained
`func_151D792C` in [generated_204660.c](../../conker/src/game/generated_204660.c)
to complete semantic C. Its **67 words / 268 bytes**, **frame 0x30**, match
retail in the linked ELF: **54 direct words plus 13 strict final-output
scheduling/register guards**. This is not an unguarded direct match.
VA 0x151D792C..0x151D7A38, ROM 0x204DDC..0x204EE8.

Replace only its retained directive and add its position layout and typed
declarations. Preserve [204660.s](../../conker/asm/204660.s) and
[per-function assembly](../../conker/asm/nonmatchings/generated_204660/func_151D792C.s).
No filler, pools, new globals, data, compiler-profile or Makefile changes.
All linked instruction bodies and other owner routines remain unchanged.

## Recovered Contract

Read signed state at owner+0x2C and unconditionally capture the ring buffer
at owner+0x94. If state < 2, read the unsigned 16-bit flags at +0x1E;
bit 8 returns 0. The captured pointer load is still required on this gate.
State >= 2 skips the flags read. Do not defer the pointer load until work.

Read signed current cursor +0x2E and signed goal +0x2D. Equal cursors skip
count, global delta and point-update accesses. Otherwise decrement before
each call, wrapping negative cursors to unsigned owner[0x25] - 1. The ring
stride is 28 bytes. Call the already qualified mixed-ABI integrator
func_151D8718(point, point+0xC, D_800BE9A4).

Keep the original buffer captured even if a callee changes owner+0x94.
Goal remains live after each call, count is reread only on wrapping, and
the global delta is loaded for every call. Reload state after work; the
no-work path can retain its original state read. When the final signed
state is positive, forward-copy the goal record's raw XYZ words to
owner+0x54/+0x58/+0x5C. Otherwise write three positive-zero float words.
Return 1 after either output path. Preserve this consumed return contract,
not only the resulting coordinates.

Zero wrap count can address the preceding record; the bounded guest fixture
maps it deliberately. Negative guest addresses and partially overlapping
raw copies qualify emitted retail behavior, not universal portable C.

## Fitting And Guard Closure

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_ring_update_candidates.py)
measures **47 complete source forms**: 37 ordinary and ten negative controls.
The natural inline-copy form emits 66 words/frame0x30 with 28 differences.
A meaningful block-local final position pointer recovers the full 67-word
slot with 13 differences. No direct exact form was found in this screen.
Candidate-only typed record layouts are not installed in production.

| Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 67 | 0x30 | 13 |
| O2 | 66 | 0x30 | 38 |
| O1/g3 | 79 | 0x28 | 78 |
| O1 | 78 | 0x28 | 77 |

Isolated candidates compile without diagnostics or pools. Three unchanged
symbolic relocation sites remain: HI16/LO16 for D_800BE9A4 at +0x54/+0x58,
and R_MIPS_26 for func_151D8718 at +0x88.

The 13 expected-word guards span +0xA0..+0xD0. Their closed transformation
normalizes the final stride initialization, branch-likely zero delay slot,
product/copy register allocation and common-return schedule. It does not
replace the algorithm: the unguarded complete semantic body already passes
the public state/call/result controls. There are no insertions, omissions,
or relocation changes. Stale frame/header and every guarded expected word
are rejected. Guard history rejects missing, extra or reordered new rows.

Append exactly 13 rows to [the manifest](../../conker/retail_word_patches.us.csv),
11,155 -> 11,168. Audit checks the previous parsed history and its entire raw
byte prefix, preserving pre-existing line endings instead of rewriting CSV.

## Qualification

[Eight focused tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_ring_update_match.py)
reuse the existing MIPS oracle, native32 runner, owner compiler/parser,
real padder and strict guard history. The independent public reference
models aligned mapped accesses, signed bytes, ring traversal, calls and
forward output copies; it does not compile the production body.

- **2,743 guest cases** cover all 256 state/current/goal byte patterns
  independently, gate/no-work/wrap, counts 0/1/127/128/255, raw special XYZ,
  partial-overlap final copies and two stack phases. Callee mutations change
  goal/state/count/delta/buffer, including combined changes and argument-home
  overwrites. Full normalized/retail GP/FP, private memory and access trace
  agree, alongside independent public state/call/trace expectations. The
  reached set is exactly **65 words**; +0x4C/+0xD4 are two original compiler-dead
  words, preserved as retail bytes. This is not a full Cartesian byte domain.
- **157 required fault prefixes** and **eight lazy cases** qualify the
  unconditional gate pointer load, skipped fields, required point/output
  accesses and unaligned captured storage. Complete normalized/retail partial
  state and independent public prefixes agree. Guest mapping checks do not
  model N64 CP0 exception metadata or portable C fault semantics.
- **404,131 actual native32 C executions** cover every unsigned flag pattern,
  all signed state/current byte patterns, wrap boundaries and seven callee
  mutation modes. A volatile typed call exercises pointer/pointer/float ABI.
  An independent numeric reference checks calls and all 512 or 8,192 arena/
  canary bytes with prepared valid buffer pointers. Partial-overlap copies,
  guest faults and universal pointer/NaN representations are not claimed.
- **47 compiled forms / 2,294 ordinary executions / ten effective negatives**
  discriminate unsigned state/cursors, signed count, wrong gate, cached
  goal/state/delta, live rather than captured buffer, wrong velocity offset
  and wrong stride. Unsupported instructions cannot count as successful
  negatives. Ordinary controls compare public state/calls/result; access-order
  differences are recorded separately. Normalized installed output still
  requires complete raw retail trace equality.
- Copied full owners preserve **22 neighbors**, relative relocations and
  normalized pools. Four existing pointer/integer warnings remain identical.
  Real padding emits 268 bytes with the exact guard closure and no filler.
  **Six independent links / 144 executions** check all three independently
  calculated HI16/LO16/JAL sites across low/high/carry-boundary rebases.
- **512 connected cases / 1,024 compiled-and-retail executions** install the
  actual 19-word integrator and optionally the full original 100-word
  func_15147740 dispatcher, including real epilogues. Callback-table index
  13 receives the owner, and false callback return reaches the release hook
  with that same owner. The linked callback table is independently checked.
  These cases scope timer flag off, flags 0/8, second kind zero, selected
  states/cursors and two stack phases, not every dispatcher branch.

The original dispatcher connection is separate from its **still-zero-return
linked C placeholder** in generated_174BF0.c. This conversion does not restore
it. Release remains a bounded hook. Main guest/native mutation fixtures use
controlled point updates; the actual 19-word integrator is connected separately
against its existing rounded reference. Hardware/FCSR, alternate dispatcher
branches and full gameplay parity remain open.

An initial ordinary-control assertion incorrectly required chained zero
stores to have retail's order; it was corrected before installation to
separate public behavior from scheduling. An older allocation fixture then
failed its declaration-placement reconstruction after new ring declarations
preceded its block. Preserve its existing block position when constructing
selected/baseline owners, and rerun affected copied-owner/installed checks.
These were fixture defects, not inferred production changes.

Fresh pre-install **eight tests pass in 85.418s**, no skips. Fresh installed
**eight tests pass in 113.683s**, no skips. **Six affected older checks pass
in 66.113s**: velocity copied owner/installed/caller, cleanup installed, and
allocation copied owner/installed. The initial five-check run had four passes
and the declaration-placement failure; do not report that run as passing.
Ten shared word-patch/PC16 tests
pass in 0.044s. Both tools project checks, candidate CLI help and six task
file syntax checks in both mirrors pass. Unchanged broad neighbor suites are
historical receipts, not newly executed full-suite or gameplay evidence.

## Linked Audit And Progress

`make -C conker -j4 build/conker.us.elf progress.csv` exits 0. The shared
manifest dependency triggers a broad padded-owner rebuild before relinking.
Existing compiler pointer/type/long-double warnings and duplicate
generated_12D630 recipe warnings remain; this is not a warning-free build.
`make -C conker match-progress NON_MATCHING=1` also exits 0.

Fresh audit compares `game-attachment-allocation-test/after.json`:

- All **6,058 function bodies, addresses and extents** unchanged: 6,042 retail
  rows plus 16 overflow symbols. Init/init-data/debugger/game-data unchanged.
- All **720 game-data owners / 189,088 bytes** remain exact. The target and
  actual linked velocity integrator match complete retail slots.
- All **11,155 prior guards and their raw CSV prefix** unchanged; exactly
  13 new guards. Reference assembly and Makefile fingerprints unchanged.
- Exactly one progress row changes: func_151D792C, 268 bytes, asm -> c.
- Total converted **5,479 / 6,042 (90.68%)**, bytes 1,934,364 / 2,256,728 (85.72%).
  Game **4,806 / 5,321 (90.32%)**, bytes 1,762,928 / 2,072,880 (85.05%).
- Byte-exact **3,390 / 5,479 (61.87%)** overall and **2,717 / 4,806 (56.53%)**
  Game; 2,089 still different, zero address drift. Init 492/492 and debugger
  181/181 remain exact.

Ignored receipts live in `conker/build/game-record-ring-update-test/`:
slot, guest, faults, native, controls, owner-padder, connected, installed,
audit-baseline, audit-installed, before-progress, before-manifest and new
`after.json` baseline. README updates aggregate tables only.

## Workflow And Next

Entry source `1edffc2bd5c89d8bec63ce5d576e748d0b2973ec`, mounted tools
`56c4132b93e75ef9a5a8944f15a9edd22afd255d`, both clean. Pre-edit SHA-256:

```text
source: b229355ddda29886a379a50b41fbfe3cc4b96cd37205c656a515dcbbacdec56d
reference ASM: 14c690097e848287eb8f9e5f3f1031cfa7c3fd65ebdb31075cdafc30a732fa48
Makefile: d5e4c8459b9bf1ac7485b913f559fe9e0242ec284d76cddf0650c210e2a73466
progress: aa68e9ed01f692c5269ba3dd88c6776b83e8b1b851f9f8fe3a36cba3929a3d05
guard CSV: d20b5a5057b8d3f58d2813799bb5e4be83e3b59772342a7d36a514ca93ded518
prior linked snapshot: 7ebc24fb7757558d7047c03dd6519cfdafae14842b071fc64b5cc355c6109210
```

Zero Claude calls; routine fitting and lifetime settled locally. No host/
runtime/save/editor/bridge/account changes; OGL Release remains frozen.
Preserve the older independently dirty standalone tools checkout; mirror task
files without reset or a duplicate divergent-history commit.

Graph query exits 0 without a matching node. Refresh exits 1: 16,777 new nodes
versus 38,565 existing; it refuses overwrite and retains 19,398 nodes from
2,972 excluded-but-existing files. No forced overwrite or ignore changes.
Graph refresh is not complete; a background hook is not completion evidence.

Next retained target **func_151D7A38**, **166 words / 664 bytes**, frame **0xC8**:
VA 0x151D7A38..0x151D7CD0, ROM 0x204EE8..0x205180. Fresh complete assembly
inspection identifies captured payload/buffer, actor gate and XYZ packets,
progress accumulation, time/position interpolation, per-point integrator
calls, and live cursor/count/state/goal updates. The second callback table's
index 16 points to this routine. No candidate installed or qualification
claimed. Keep its assembly until fitting and copied-owner/runtime-model
gates pass; dispatcher/constructor/hardware/gameplay work remains separate.

## Banking

Per "Keep commited", mounted tools
**74cbbdc47e4ea053728e22192b3fad728567cf16** banks the six task tools files
first. The parent source/manifest/docs checkpoint records that exact pin.
No push, reset, stash, unrelated staging or duplicate divergent tools commit.
Final verification checks **121 documents / 4,023 relative links / zero broken
links** and **31 byte-identical relevant tools files** across both checkouts.
Scoped diff checks pass. The wider Game goal remains active; this local
checkpoint does not imply a pause or publication.
