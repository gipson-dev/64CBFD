# Game Owner Point Arc Endpoint Read Recovery

Date: 2026-10-09

## Baseline And Target

Continue after consumer 211c586a and tools 83c1d66a4cf1e50a4c9eb8c64370ca85696e05b6.
Both active checkouts started clean. The preceding goal turn made progress by
recovering delta-Y and complete final private memory in
[Note 1192](1192-game-owner-point-arc-delta-y-home-recovery-20261009.md).

func_151B3CF0: VA 0x151B3CF0..0x151B3F28, ROM 0x1E11A0..0x1E13D8,
142 words / 568 bytes, frame 0x88. Production
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c) is unchanged.
No installation, guard/profile changes, conversion or byte-matching credit.

Single Codex writer, zero Claude calls; follow the existing offline workflow,
scoped graph query, complete IDO output and existing parsers/oracles/padder.
No OGL, Release, saves or editor changes. README aggregates stay unchanged.

## Recovered Input Multiplicity

[Endpoint fitting](../../tools/experiments/game_owner_points_arc_endpoint_reads.py),
SELECTED_NAME = stage-retail-reuse-axis, snapshots all six endpoint words once.

Real stage reuse: hold end XYZ in nz/nx/angleStep, then overwrite them with
normalization/projection/step only after endpoint offsets have consumed them.
Hold start XYZ in along/angle/sine until midpoint/offset construction, before
their later helper-result uses. Axis-grouped statements shorten endpoint
lifetimes. This is ordinary semantic C with the retained diagnostic workspace
qualifiers, not recovered-original-source or original-FP-allocation proof.

Selected complete body: 144 words / frame136 / 138 raw differences, zero
diagnostics or pool bytes. Original frame, every saved-register home, nine
vector homes and SP+0x80 delta-Y store/load remain intact. Entire final memory
and private vector/delta-Y write multisets agree in qualified cases.

Fresh six-read gate: each actor endpoint at 0x14/18/1C/20/24/28 is read exactly
once, active and early-exit paths. The original also reads each once. This
removes all four redundant start-coordinate reads from the preceding diagnostic.
Read multiplicity is not full read-order or FCSR parity.

The older 144/frame136/135-difference body remains retained. Raw differences
increase by three in the new six-read form; do not claim byte-match progress.
The actual padder still rejects the two-word overflow.

## Source And Layout Discriminators

62 complete forms qualify their public contract against eight ordinary guest
fixtures each: 496 cases / 992 executions. Four existing profiles qualify the
selected public contract; frame/home claims apply only to selected O2/g3 output.
Other forms are not all private-memory-qualified.

| Complete Form | Words | Frame Bytes | Raw Differences |
| --- | ---: | ---: | ---: |
| Retained ten-read endpoint snapshots | 144 | 136 | 135 |
| Stage reuse, grouped coordinates | 144 | 136 | 139 |
| Selected stage reuse, axis coordinates | 144 | 136 | 138 |
| Dedicated starts, retail-role end reuse | 151 | 200 | 150 |
| Ordinary selected workspaces | 149 | 192 | 147 |
| Read-volatile selected workspaces | 146 | 192 | 144 |

Controls cover dedicated versus reused endpoint locals, load order, grouped/
axis/retail coordinate statements, register hints and ordinary versus read-only
volatile workspaces. Skip source mappings with overlapping live endpoint names;
do not treat overwriting an endpoint snapshot as a valid optimization.
Dedicated starts and altered workspace qualifiers fail the original layout.
Register hints and load order do not independently recover the desired fit.

Actual selected disassembly duplicates the Z-delta calculation across the
short-circuit test and emits a second half-constant setup on its Z-only path.
These are next fitting targets, not certified deletions. Counter/current-next
cursor allocation and retail branch-delay angle advance also remain open.

## Fresh Qualification

[Selected suite](../../tools/tests/test_game_owner_points_arc_endpoint_reads.py)
borrows the unchanged full-body delta-Y/native/dispatch/rebase/owner/fault
checks with scoped, class-cleaned target substitution and a separate receipt
directory. It extends the private-home gate with actual endpoint-read counts.

Fresh combined run: all 48 tests pass in 345.780s, zero skips. Run the twelve
endpoint-read tests first, then all 36 retained recovery/workspace/lifetime/
delta-Y tests; this also verifies scoped target substitution is cleaned up.

- Guest: 2,560 cases / 5,120 executions, all flag bytes, five geometries and
  both stack phases. Every 142 original / 144 candidate word reached; saved
  GPR/FP, all actor/canaries, full final memory/private writes and six reads.
- Add the Z-only active geometry to the all-flags set. The inherited four-
  geometry set missed candidate 0x151B3D7C. Expand coverage rather than
  dropping the all-word gate or pretending that address is unreachable.
- Boundaries/callback mutations: 48 cases / 96 executions, seven effective
  semantic negatives, signed zero/threshold/tiny/NaN/infinity and retained step.
- Actual selected native32 C: 512 finite cases versus complete original guest,
  bitwise helper arguments/order and every actor/canary byte.
- Actual original 81-word registered update: 18 cases / 36 executions,
  one-argument callback at 0x8008FAFC and success-return ABI.
- Four independent symbol sets / eight links: 32 cases / 64 executions, all nine
  original relocation uses, complete private memory and six reads preserved.
- Actual copied owner: 16 neighbors/pools/relative relocations unchanged,
  isolated/owner target equal, zero diagnostics; actual padder rejects 144 words.
- All six endpoint missing-byte faults in both phases: 12 cases / 24 executions
  retain public write/call prefixes. Retain six previous input/global/output
  faults / 12 executions and two unused-byte cases.
- Two effective read negatives pass public contracts: the retained ten-read body
  also passes full private-memory contracts, proving the independent multiplicity
  gate. The compiled ignored volatile seventh read additionally changes private
  storage; both its read and memory gates reject independently. A swapped-
  workspace declaration control passes public
  contracts and retains frame/saved homes but fails private memory.
- Source/ELF/guards/progress and all 189,088 protected bytes / 720 owners remain
  unchanged. Actual helper/registration audit is rerun.

The initial subclass audit also exposed inherited ten-read expectations and a
reload-assignment negative that itself spilled into private padding. An ignored
volatile read also alters storage. Record both observations instead of assuming
layout neutrality: the retained ten-read body provides the pure read-gate
discriminator. Override target-specific expectations and keep the memory gate.

Helpers remain bounded caller-clobbering contracts. Actual sinf/cosf still return
zero; the full 80-word angle-helper slot is exact. No retail trig math, hardware/
FCSR, general stack/input aliasing, full access ordering, portable-C faults or
live rendering/gameplay acceptance is claimed.

## Banked State And Resume

Fresh make tools-check passes. Fresh matcher: total3,417/5,489 (62.25%),
Game2,744/4,816 (56.98%), Init492/492 and Debugger181/181 exact; zero drift /
2,072 different. No production rebuild for unchanged source/profile/data/guards;
Note 1188's build receipt is explicitly reused, not called fresh.

Tools aafc0365a9cbc0a5a2e0b54eac1d564f7fef2b39 commits the two authored files before parent docs/pin.
Mirror only absent authored files to the older checkout. HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a, all 139 prior dirty entries and both
tracked dirty-file hashes stay unchanged; two additions yield 141. No reset,
conflicting overwrite, older commit or push.

Fresh scoped documentation audit: 15 documents / 3,971 relative links, zero
broken links. Thirteen affected initializer/arc tooling files parse in both
checkouts and have exact older mirrors; two are this turn's authored files.
Fresh graphify update . exits 1, refusing 39,138-to-17,366 node shrink and
preserving 19,398 nodes from 2,972 out-of-corpus files.
Keep version/zero-node warnings; no force/purge/install.
Await the detached parent hook's confirmed completion before a clean-bank report.

Ignored receipts: conker/build/game-owner-points-arc-endpoint-reads/ and
conker/build/game-owner-points-arc-endpoint-reads-test/.

- [x] Remove all four redundant input reads while retaining original frame,
  saved/vector/delta-Y homes and complete final private memory.
- [x] Qualify full bodies, all-word coverage including Z-only, actual native32/
  dispatch/rebases/owner/fault/data/helper gates and effective read/home negatives.
- [x] Commit tools first, parent docs/pin second; preserve independent older work.
- [ ] Fit the complete 142-word slot, including Z-delta/half-constant scheduling,
  original FP allocation, counter/cursor and branch-delay angle advance.
- [ ] Install only after whole linked owner/ELF/data/guard-history qualification.
- [ ] Recover real trig separately before hardware/live rendering acceptance.

The wider Game matching goal remains active.
