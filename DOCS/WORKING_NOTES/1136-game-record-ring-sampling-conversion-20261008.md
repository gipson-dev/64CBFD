# Game Record Ring Sampling Conversion

Date: 2026-10-08

## Result

Continue [Note 1135](1135-game-record-ring-update-conversion-20261008.md)
under the [focused workflow](../AGENT_WORKFLOW.md). Convert retained
`func_151D7A38` in [generated_204660.c](../../conker/src/game/generated_204660.c)
to complete semantic C. Its **166 words / 664 bytes**, **frame 0xC8**, match
retail in the linked ELF: **129 direct words plus 37 strict closed register,
private-spill and loop-scheduling guards**. This is not an unguarded direct
match. VA 0x151D7A38..0x151D7CD0, ROM 0x204EE8..0x205180.

Replace only its retained directive and add its position/payload layouts and
typed declaration. Preserve [204660.s](../../conker/asm/204660.s) and
[per-function assembly](../../conker/asm/nonmatchings/generated_204660/func_151D7A38.s).
No filler, pools, new globals/data, compiler-profile or Makefile changes.
All linked instruction bodies and other owner routines remain unchanged.

## Recovered Contract

Unconditionally capture payload at owner+0x98 and buffer at owner+0x94.
Read the captured payload's actor pointer, then unsigned actor byte+0x2D.
A clear low bit returns 0 before XYZ, global-delta or ring-work accesses.
The payload is a 24-byte native32 layout: actor pointer, XYZ position,
residual time at +0x10 and progress at +0x14.

Capture actor XYZ+0x30 and forward-copy the raw words to owner+0x10.
Accumulate payload progress by 0.25f * D_800BE9A4. Work only when progress
is strictly greater than 1.0f; equality and unordered comparisons skip work
and return 1. Positive-infinite progress is nonterminating in retail and is
explicitly excluded from bounded fixtures, not repaired or clamped.

Use reciprocal progress to interpolate from captured payload position to
the captured actor position. Residual time uses a second live global-delta
read. Preserve separate float subtractions, products and per-axis increments,
not algebraically regrouped or fused arithmetic.

Each iteration uses the live signed current byte+0x2E and 28-byte stride
into the captured buffer. Copy private XYZ, clear float fields +0xC/+0x10/
+0x18 and byte+0x14, and preserve the three padding bytes +0x15..+0x17.
Call the already qualified mixed-ABI integrator func_151D8718(record,
record+0xC, residualTime).

After the call, reload signed current and unsigned count+0x25, increment
the current byte, then compare its reloaded signed value with the count.
For example, 127 -> -128 does not equal unsigned count 128. Increment live
signed state+0x2C. If live signed goal+0x2D equals current, increment/wrap
goal and undo the state increment. Byte updates preserve wrapping storage.

Keep payload and buffer captured even if a callee changes owner pointers.
The payload progress remains live after each call; time and position steps
remain private captures. Finish by copying the interpolated XYZ back to the
captured payload and storing residual time. Return 1 after the active gate;
the actual original dispatcher consumes this callback result.

Deliberately mapped negative signed guest indices and actor/payload-overlap
ring storage qualify emitted retail behavior, not universal ISO C semantics.
Native checks use prepared valid native32 arenas and no-strict-aliasing
representation boundaries. Hardware FCSR/CP0, NaN payloads and gameplay
parity are not inferred.

## Fitting And Guard Closure

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_ring_sampling_candidates.py)
measures **64 complete forms**, including eleven effective negatives.
The natural form emits 167 words/frame0xA8 with 122 differences. Explicit
signed-byte updates recover 166 words, then meaningful staged axis deltas,
used position pointers and private declaration placement recover frame0xC8.
Computing residual time before the old-position copy leaves 37 differences.
No artificial padding, dead locals, assembly scaffolding or direct exact form.

| Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 166 | 0xC8 | 37 |
| O2 | 166 | 0xC8 | 54 |
| O1/g3 | 198 | 0x68 | 194 |
| O1 | 198 | 0x68 | 194 |

Isolated candidates compile without diagnostics or pools. Three unchanged
symbolic sites remain: D_800BE9A4 HI16/LO16 at +0x6C/+0x78 and
func_151D8718 R_MIPS_26 at +0x188.

The 37 expected-word guards normalize closed GP copy/index/state cycles,
the captured position pointer's paired private spill/reload (0x74 -> 0x70),
commutative comparison operands and the loop's branch-likely/head-load
schedule. All FP arithmetic, frame and saved-register lifetime emit directly.
No instructions are inserted or omitted; relocations are unchanged.
The raw complete C already passes independent public behavior/access-prefix
checks. Guarded output additionally requires complete retail GP/FP, private
memory and access-trace equality. Stale header and every expected guarded word
are rejected; history rejects missing, extra and reordered target rows.

Append exactly 37 rows to [the manifest](../../conker/retail_word_patches.us.csv),
11,168 -> 11,205. Preserve every previous parsed row and the entire raw CSV
prefix, including its existing line endings.

## Qualification

[Seven focused tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_ring_sampling_match.py)
reuse the existing MIPS oracle, native32 runner, owner compiler/parser, real
padder and strict guard history. The independent public reference models
fixed offsets, aligned mapped accesses and scalar rounded f32 operations;
it does not compile or invoke production C.

- **1,889 guest cases** cover all 256 actor-flag/current/goal/count/state bytes
  independently, gate/no-work/multiple-sample paths, wrap/truncation, two stack
  phases, ten callee-mutation modes and two actor/payload overlap layouts.
  Signed-zero/subnormal/quiet-NaN no-work cases and finite signed deltas are
  bounded. This is not the full Cartesian byte or float domain. Raw C,
  normalized and retail agree with the independent public memory/calls/result/
  access expectations. Normalized/retail complete private state and trace
  agree. Exactly **165 reachable words** are covered; the original compiler-dead
  +0x60 word is preserved, not claimed executed.
- **314 required fault prefixes / eight lazy cases** cover required pointer,
  packet, state and output accesses, captured unaligned storage, and callee
  mutations. Independent public prefixes and normalized/retail complete partial
  state agree. CP0 exception metadata and portable C faults are not modeled.
- **264,704 actual native32 C executions** cover three full current/count-byte
  domains (inactive, no-work, emitting), all state/goal pairs and every actor
  flag under ten mutation modes. A volatile typed call exercises the real
  pointer/float ABI. Independent numeric expectations compare calls, result,
  global delta and all **16,384 arena/canary bytes**. Guest fault/overlap and
  universal hardware or pointer representations are not native acceptance.
- **64 compiled forms / 848 ordinary executions / eleven effective negatives**
  discriminate unsigned current, signed count, live buffer/payload, wrong
  threshold/quarter/velocity offset, cached current/progress, omitted state
  undo and uncleared record+0x18. Ordinary forms compare public behavior;
  supported scheduling differences do not become algorithm failures.
  Unsupported instructions cannot count as effective negatives.
- Copied full owners preserve **22 neighbors**, pools, relative relocations
  and four identical existing pointer/integer warnings. Real padding emits
  664 bytes with the exact closure and no filler. **Six independent links /
  120 executions** verify all three independently calculated HI16/LO16/JAL
  sites across low/high/carry-boundary addresses.
- **96 connected cases / 288 raw-C, normalized and retail executions** use the
  actual 19-word integrator and optionally the full original 100-word
  func_15147740 dispatcher with real epilogues. Callback table index 16 receives
  the owner; a false result reaches the bounded release hook with that owner.
  The linked table word is independently checked. Scope is first-kind zero,
  timer/player flags off and bounded sampling paths, not every dispatcher arm.

The connected original dispatcher is separate from its **still-zero-return
linked C placeholder** in generated_174BF0.c. This conversion does not restore
that body. Main mutation fixtures use controlled point updates; actual
integrator connections use its existing independently rounded reference.
Alternate dispatcher branches, full release behavior and hardware/gameplay
remain open.

The first raw suite failed two fixture setup checks: actor-overlap mapping
was too short for its second record, and native reference formatting tripped
-Werror=misleading-indentation. Retail/raw-C/reference agreed on the guest
fault. Fix the mapping/reference formatting, not production semantics.
The corrected raw suite passed seven tests in 68.763s; the stronger raw plus
normalized pre-install suite passed seven in **107.178s**. The installed suite
passes seven in **104.050s**, with no skips.

An initial nine-check regression run had eight passes and one failed older
ring copied-owner reconstruction: removing its whole header also removed
the shared global/integrator declarations needed by the new sampler.
Preserve those declarations in its baseline and preserve later sampling
guards in its proposed whole-owner manifest; target-row negative controls
remain strict. No production neighbor change is inferred from this failure.
The corrected nine affected checks pass in **112.141s**, with no skips:
ring copied owner/connection/installed checks, velocity copied owner/installed/
caller checks, cleanup installed, and allocation copied owner/installed.
The initial eight-pass/one-failure run took 87.852s; do not report it as passing.

Ten shared word-patch/PC16 tests pass in 0.044s. Both mounted tools checks,
the older standalone project check, candidate CLI help and all six task
files' syntax/byte identity in both checkouts pass. Unchanged broad neighbor
suites are historical receipts, not newly executed full-suite/gameplay proof.

## Linked Audit And Progress

`make -C conker -j4 build/conker.us.elf progress.csv` exits 0. Shared manifest
dependencies trigger a broad padded-owner rebuild. Existing compiler pointer/
type/long-double and duplicate generated_12D630 recipe warnings remain;
this is not a warning-free build. `make -C conker match-progress NON_MATCHING=1`
also exits 0.

Fresh audit compares `game-record-ring-update-test/after.json`:

- All **6,058 bodies, addresses and extents** remain unchanged: 6,042 retail
  rows plus 16 overflow symbols. Init/init-data/debugger/game-data unchanged.
- All **720 game-data owners / 189,088 bytes** remain exact; target and linked
  integrator match their complete retail slots.
- All **11,168 prior guards and raw CSV prefix** remain unchanged; exactly 37
  new rows. Reference assembly and Makefile fingerprints unchanged.
- Exactly one progress row changes: func_151D7A38, 664 bytes, asm -> c.
- Total converted **5,480 / 6,042 (90.70%)**, bytes 1,935,028 / 2,256,728 (85.74%).
  Game **4,807 / 5,321 (90.34%)**, bytes 1,763,592 / 2,072,880 (85.08%).
- Byte-exact **3,391 / 5,480 (61.88%)** overall and **2,718 / 4,807 (56.54%)**
  Game; 2,089 still different and zero drift. Init 492/492 and debugger 181/181
  remain exact.

Ignored receipts are in `conker/build/game-record-ring-sampling-test/`:
slot, guest, faults, native, controls, connected, owner-padder, audit-baseline,
audit-installed, before-progress, before-manifest and new `after.json`.
Root README updates aggregate tables only.

## Workflow And Next

Entry source `c841538b12788507d0520200fc8e1239f39bd6cd`, mounted tools
`74cbbdc47e4ea053728e22192b3fad728567cf16`, both clean. Pre-edit SHA-256:

```text
source: 7a21550c195ea94906d3c19c5521cb503786be0af2282916afa97fdf64f76245
reference ASM: 14c690097e848287eb8f9e5f3f1031cfa7c3fd65ebdb31075cdafc30a732fa48
Makefile: d5e4c8459b9bf1ac7485b913f559fe9e0242ec284d76cddf0650c210e2a73466
progress: 3a9a5e3e64aba55028cfb8d4644dc48efa6a82fc5e6b26d005e901ae4de2c99f
guard CSV: db0d1812214a8a5f940b8f3e3e6da899a726dda480438e400f61904ac5233d3f
prior linked snapshot: ad51b315a9c9fa47ae6c9ec24a03ddf4476729ca5dcf7ef402c4d87153bf0c0d
```

Zero Claude calls; routine fitting and lifetime decisions settled locally.
No host/runtime/save/editor/bridge/account changes; OGL Release frozen.
Preserve independently dirty older standalone tools history; mirror task
files without reset or a duplicate divergent commit.

Fresh graph refresh exits 1: 16,789 new nodes versus 38,577 existing. It refuses
overwrite and retains 19,398 nodes from 2,972 excluded-but-existing files.
No force or ignore changes. Refresh remains incomplete; extraction messages
and background hooks are not completion evidence.

Next retained target **func_151D7CD0**, **253 words / 1,012 bytes**, frame **0xB8**:
VA 0x151D7CD0..0x151D80C4, ROM 0x205180..0x205574. Complete original assembly
was inspected. It captures payload/buffer before its signed state gate, then
performs backward ring passes for vector-result accumulation/80.0f limiting,
scalar updates and record-byte fading. Its unsigned float-to-integer lowering
explicitly saves/changes/restores FCSR. First inspect both real callees'
interfaces and the extended payload, then recover the complete semantic body
and qualify the conversion lowering before fitting. Do not assume the current
sampler oracle models those FCSR operations. No candidate installed or next
target qualification claimed; linked dispatcher/constructor and gameplay
remain separate.

## Banking

Per "Keep commited", mounted tools **9fb0eb272cde06487681603eff7e3de24e6fe725** banks the six
task tools files first. The parent source/manifest/docs checkpoint records
that exact pin. No push, reset, stash, unrelated staging or duplicate
standalone-history commit. Final verification checks **122 documents / 4,036
relative links / zero broken links** and **33 byte-identical relevant tools
files** across both checkouts. Scoped diff checks pass. This local checkpoint
does not finish the wider Game work or authorize publication.
