# Game Record Matrix Update Direct Match

Date: 2026-10-11. Recover complete func_1503E82C in
conker/src/game/generated_6B320.c, replacing its zero-return placeholder.
VA 0x1503E82C..0x1503EA54, ROM 0x6BCDC..0x6BF04: 138 words / 552 bytes.
All 138 words emit directly under the existing O2/g3 owner profile, frame
0xB8. No guards, drops, handwritten replacement, caller-body, shared-header
or compiler-recipe changes. Matching +1 only; conversion counts/bytes stay
unchanged. Keep the full Game goal active.

## Baseline And Contract

Consumer 4bc57f50d866955133e6aab4e9d15c1c285e740f and mounted tools
036e55cdc0bc5e0e0bdc9f2fa76a4027b301c189 were committed at entry.
[Note 1279](1279-game-record-transform-setup-direct-match-20261011.md)
left this genuine 138-word / 138-difference target. Read the complete retail
body, sole 171-word dispatcher caller, actual structures and matrix helper
interfaces after a scoped Graphify query. Reuse the existing compiler,
MIPS/native32, ELF/object/pool, post-processor and both padder fixtures.
Codex is the single writer; zero Claude calls, no bridge or installs.

Recover void func_1503E82C(s32 slot). Retail establishes no status result.
The existing caller already ignores V0; only its forward declaration changes.
Keep the existing 812-byte actor, 16-byte control and 104-byte element types.

- A NULL actor bank exits before any control/group/count/type/buffer reads.
  Otherwise cache the original unsigned count and signed type-table cursor.
  Count zero still loads the table pointer but never dereferences its bytes.
- Only initial signed -2 skips an element. Other selectors read the live
  control buffer and unsigned element flag +0x64; zero skips all helpers.
  Initial count/cursor survive group/table/count callback changes.
- For an active element, reread the live group/type and bank. Cache the
  destination bank + index*64 before calling any helper. Only this live -1
  selects the absolute path; the initial -2 and live -1 gates are distinct.
- Relative path: build translation in private matrix +0x64 from full raw
  words +0x24/+0x28/+0x2C. Reread the bank after translation and multiply
  temporary * live type-bank matrix into temporary. Reread the record buffer
  for rotation +0x30/+0x34/+0x38, build the cached destination rotation, then
  multiply destination * temporary into destination. Reread the record buffer
  again for scale +0x3C/+0x40/+0x44, build temporary scale, and multiply
  temporary * destination into the same cached destination.
- Absolute path: build cached destination rotation, then reread the record
  buffer and pass scale and position to func_15043EC8's full seven-argument
  O32 interface. The three position floats occupy stack +0x10/+0x14/+0x18.
- Keep raw-word translation/scale builder interfaces and float rotation/
  finish interfaces. Shared struct04 declares halfwords at +0x24/+0x28;
  those member accesses would truncate these full float payloads. Use local
  raw/float views, not numeric integer-to-float conversion or a header rewrite.

All saved-register slots, loop branch-likely updates and call delay slots
match. The duplicate load at +0x1A0 is unreachable: the relative path jumps
past it, and the absolute branch executes its earlier delay-slot load.
All 138 words match, while qualification executes 137 reachable words.

## Direct Source Recovery

Initial semantic source has the correct 138-word length, frame 0xC0 and
32 differences. Recover full-word payload reads, the outer switch and the
destination-before-type assignment to reduce this to seven private layout
words. Meaningful actor/control address inlining recovers frame 0xB8 and
leaves five. Put count first and scope the element local inside the bank
gate to recover the final private matrix/count homes, yielding 138/zero.
No padding locals, volatile forcing, assembly body or word normalizations.
The compact no-unroll diagnostic also matches; O1/g3 and O1 emit 197 words
and do not match. No diagnostic profile is installed. This is a bounded
source screen, not an exhaustive proof that other forms cannot match.

## Fresh Qualification

New tools: experiments/game_record_matrix_update_candidates.py and
tests/test_game_record_matrix_update_match.py. Immutable before-inputs and
receipts: conker/build/game-record-matrix-update-match-test/.

- Thirteen complete pre-install tests pass in 21.496 seconds. All thirteen
  installed tests pass in 20.492 seconds. A final two-test literal-audit and
  integrity-control rerun passes in 2.399 seconds after documentation edits;
  all 4,377 relative links across seven checkpoint docs pass. Prior unchanged neighbor suites
  are historical receipts, not described as freshly rerun.
- The 176-case retail/raw/padded guest matrix covers counts
  0/1/3/4/5/27/31/45/128/255, flags, -2/-1/0/-128/127 types, groups, stack
  phases and NULL banks. Unused tables stay unmapped on NULL-bank paths.
  Invalid slots and negative/high type-bank mappings are guest-only evidence.
- Forty-four callback/public/private-alias cases distinguish cached count,
  cursor, type and destination from live group/bank/buffer reloads. Replacement
  buffers have different position, rotation and scale payloads. All external
  boundaries clobber caller-saved GPR/FPRs. Aliases remain guest-only.
- Two independent placements rebase nine symbols with HI16/LO16 carries;
  24 cases preserve all forms, private matrix identity and seven-argument
  payloads. All 219 fired fault triplets preserve public/private memory,
  events and registers for the emitted target and modeled boundary accesses.
  This is not portable C fault semantics or hardware/FCSR qualification.
- Six freshly compiled controls fail on public results/arguments, not private
  layout: wrong outer/inner sentinel, halfword position, lost buffer reloads,
  reversed multiplication and lost absolute position. Stale/duplicate installs
  and source/target/neighbor/extent/guard corruption are rejected effectively
  without production mutation. Longer controls use a separate code address.
- Both copied complete owners pass GLOBAL_ASM post-processing and both real
  padders. All 21 other functions, pools, slots/relocations, the dispatcher,
  141-word setup and 141-word assembly decomposer stay unchanged.
- Thirty-six cases execute actual linked translation/scale/finish helpers
  (20/20/41 words), plus retail rotation/multiply references (84/76 words).
  Only sine/cosine leaves remain bounded host-float models. The rotation
  factor is actual linked D_8009F6C0 = 0x3C8EFA35. The current rotation and
  multiply C placeholders are not changed or newly qualified implementations.
- Forty-eight cases execute the actual dispatcher171/setup141/predicate27/
  update138 chain against an independent composed reference, with states
  1/2/3, counts 0/1/3/4, phases and a tail callback changing the record buffer.
  Setup's fifth O32 home is explicitly populated before reference calls,
  including the relative setup path. Remaining callees/tails are boundary
  models, not full gameplay or allocator acceptance.
- Twelve payload cases preserve full position words through GPRs or all three
  stack homes, including signed zero, subnormal, infinity and NaN payloads.
  Arithmetic is modeled; do not claim hardware NaN propagation or FCSR parity.
- Native32 O2 and O0 each pass 1,944 valid finite cases: nine counts, three
  slots, three type patterns, flags/bank gates and six callback modes. Check
  both complete banks, all three record buffers, command payload trace and
  public pointer/group outcomes. Three controls fail with actual mismatch
  receipts. Rotation is an explicit native boundary model; invalid banks,
  aliases, stack-home mutation and trig/hardware behavior are not native claims.

Pre-install fixture fixes: replacement buffers initially had identical
rotation/scale values, masking a reload control; the composed setup reference
omitted its fifth argument home; the native fixture needed NULL and removal
of an unused helper under -Werror. No production workaround, baseline refresh
or generic metadata exception was used to pass qualification.

```sh
python3 -m tools.experiments.game_record_matrix_update_candidates --profiles
python3 -m unittest tools.tests.test_game_record_matrix_update_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Linked Audit

Rebuild exits zero, retaining the existing duplicate generated_12D630 recipe
warning. Literal whole-ELF comparison changes exactly 460 bytes: 458 target
bytes and two function-size bytes, 12 -> 552. Every other ELF byte, body,
address, extent and metadata entry stays exact; no projection or permutation.
All seven other inputs remain byte-identical: guards, progress CSV, rodata
assembly, symbols, undefined functions, retail layout and Makefile. Preserve
all existing guard history, including the preceding teardown spill pair.

Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | 7eb13c78160b463708784daeca18041496c8f48939092ce55c3636b93d86324f |
| Source after | d6392a89c3f3d6b935549e56ab00c0f737b51e21a6e451ff32f6d483fe4916c2 |
| ELF before | f464f3d3e466ee2be9c4a2b012d21475c48d2676f9e556823d109adc9d17ebf8 |
| ELF after | d0111ec67ddfe4c6b836061caaa483457e2d38ee6b582a087d45b2d5397672cd |
| Guards, unchanged | 75a00e8d566bd1f737d2d4bd2bbbc5c01eb7ec6c33f9789a422b5aa73bc1d5ed |

Fresh progress: Game 2,801/4,822 (58.09%), total 3,474/5,495 (63.22%),
Init 492/492 and Debugger 181/181. Zero drift / 2,021 still different.
Matching +1 only; root README gets aggregate rows, no recovery narrative.

## Checkpoint And Next Body

Consumer, mounted and older standalone shared checks and native py_compile
pass. Bank mounted tools 73745f6 first, then source, this note, five current indexes,
aggregate README and exact consumer gitlink. No push. Older sibling HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 51 recorded fingerprints
remain unchanged; only two absent paths are copied with identical hashes.
Dirty count 328 -> 330. Do not commit/reset its independent dirty history.
The target suite runs in the mounted consumer, not the standalone mirror.

Native graphify update . exits one on protective shrink refusal: 18,161
candidate nodes versus 39,940 saved. Preserve 19,398 nodes from 2,972 excluded
but still existing files; no force/purge/install. Version/empty-source warnings
are separate from compiler diagnostics. After consumer commit require fresh
terminal Rebuilt, advanced log bytes/UTC
and zero workers, not just a hook-launch message. Precommit log: 535,752 bytes.

Fresh live recheck: func_1503E82C 138/zero. Next genuine placeholder is
func_1503EA54: 73 words / 71 differences, VA 0x1503EA54..0x1503EB78,
ROM 0x6BF04..0x6C028, same owner. Inspect its complete auxiliary update and
actual caller before recovery. The following func_1503EB78 is 74/72.
Remaining decomposer/callee recoveries, existing guard removal and deeper
callbacks/allocator/hardware/FCSR/renderer/gameplay remain separate and open.
No OGL Release change/build, private input/save or active editor/debugger
mutation. Keep the full Game goal active; no completion claim.
