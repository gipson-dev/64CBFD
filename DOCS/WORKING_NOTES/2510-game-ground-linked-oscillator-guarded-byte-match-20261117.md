# Ground-linked oscillator recovery and guarded byte match - 2026-11-17

`void func_151AADF8(u8 *owner)` now replaces its zero-return placeholder with
the complete ground-linked effect constructor and existing-effect notifier.
Its **166-word / 664-byte retail slot and frame 0xC0 are byte-exact**.
The C emits 165 words. **50 relocation-aware guard rows** normalize the early
exit, initialization schedule and four private spill accesses, with **one
inserted ra reload** and no omissions. **115 words emit directly from C**.
This is a guarded C match, not an unguarded compiler match.
VA 151AADF8..151AB090, ROM 1D82A8..1D8540. No dummy locals, explicit register
bindings, compiler/profile changes or handwritten function replacement.

Accepted production total **4,530 / 5,514 (82.15%)**, Game **3,857 / 4,841
(79.67%)**, Init 492/492, Debugger 181/181; zero drift, **984** still different.
**157 further matches** are needed for the active 85% goal. Conversion remains
5,514/6,048 (91.17%), 86.19% of bytes. Root README changes only Total/Game
matching rows; detailed recovery stays in the working notes.

## Recovered behavior and explicit sequencing

The [private recovery](2509-game-ground-linked-oscillator-private-recovery-and-sequencing-qualification-20261117.md)
records the interfaces and first 71 source forms; three further return-type
probes compile identically, giving 74 retained complete source forms.
An existing owner+0x70 effect receives a notification at effect+0xB4.
Otherwise the callback queries below its attached actor, selects a color and
random scale, constructs the 40-byte descriptor and 32-byte oscillator payload,
calls `func_1513C73C`, stores its result in owner+0x70, then copies the payload
to effect+0xB0 on success. Query miss and allocation failure retain the original
behavior. The owner pointer, byte selector, floats, halfwords and o32 address
arguments use their audited widths.

Selected **v42** preserves explicit first/second PRNG calls; only the third
remains inside the factory expression. V48's three nested draws are retained
as an effective GCC ordering counterexample, never as the installed source.
The query point may change through retained helper access; ground Y is freshly
read after the selector, and coefficients are freshly read after the float
provider. The copied payload has **27 defined bytes plus five unwritten holes**;
the descriptor prefix has **27 defined bytes plus one unwritten hole**.
Those holes get no portable initialization or semantic-value credit.

## Independent relation before guard generation

Earlier fitting assumed that the missing word had to emit directly from C. The accepted [paired constructors](2348-game-paired-ground-effect-constructor-match-20261112.md)
already use the same padder insertion mechanism. Reusing that mechanism avoids
dummy storage or an unsequenced C fit. The raw 165-word stream differs in private
state on four of seven paths because its two saved random results use +0x50/+0x54
rather than retail +0x4C/+0x50. This difference is measured, not hidden.

Four explicit expected-word adjustments move **two stores and their matching
loads** to the original private homes. Independently interpreting the otherwise
unmodified 165-word stream then proves **all seven complete paths**, ordered
FP/FCSR, arbitrary public alias epochs, retained query/descriptor mutations,
**all 208 private/incoming-home bytes at every call and return**, complete return
registers and callee saves. Five semantic/private-home controls reject; a
closed T8/T9 allocation cycle passes all seven paths. Pre-first-RNG scratch
register differences are clobbered by that provider; the full return relation
and call interfaces are compared rather than claimed equal at every instruction.

The emitted retail stream is independently assembled from the original source.
Fifty expected-word/relocation rows include the four spill adjustments and
the single early-return ra reload insertion after raw+0x30. The remaining rows
preserve the original notification/branch shape, private initialization order,
constant-register allocation and data-address materialization. Expected source
words and exact binding ownership must match. There is no whole-function shift
table or omission. Both complete-owner padders emit the full original 166 words
and original bindings. Two compiler-duplicated delay loads are unreachable;
normal proof/guest coverage is 163 raw and 164 retail/normalized words.

Selected raw SHA256:
`4dec087dfca51cb62d484617f6868d4f7e5b9eea93edcd92bbf1ef15fd668dec`.
Retail SHA256:
`3d88584dae34894b92b32e118466c9fdc699aaafe7a6ac05eef7f067af4bff39`.

## Fresh focused qualification

All **five maintained checks** pass in primary tools, isolated sibling overlay
and installed production with identical eight-file task fingerprints.

- Both actual padders preserve all **40 owner neighbors**, their addresses and
  normalized pools. **181 raw-word/binding corruptions** and **200 stale CSV
  controls** reject. **Twelve independent GNU links** compare both owners and
  independently assembled original code over four code/data layouts, including
  independent coefficient/table HI16 carries. All 16 original bindings are accounted.
- **1,094 guest cases per retail/raw/strict/layout stream**, all 256 selector
  values, existing/query-miss/allocation-null/allocation-success routes, two
  stack phases, threshold equality/NaN/infinity and mutable providers. Full
  initialized public memory, ordered calls and defined packet bytes agree.
  Four semantic instruction defects reject.
- **608 SDK32 C cases at each O0/O2/O3**, strict aliasing enabled and UB traps,
  pass for the selected sequenced body. Five broken C forms and the unsequenced
  v48 control compile and exit code 3 as expected; all nine runs have the expected
  outcome. Native creation uses the actual 13-color table domain; backed wide
  guest indices are not advertised as portable array-bound coverage.
- The **complete 158-word original `func_15158D2C` dispatcher** executes the
  full constructor through its real indirect table call: **228 cases per
  stream**, covering all classification paths, 28 selection slots, enabled and
  masked-out cases, callback placement, two stack phases and callee saves.
  It visits 156 reachable words; +AC/+C0 are duplicated unreachable delay loads.
  The actual callback table is literal in production. The dispatcher itself
  remains an unrelated production placeholder, clearly reported as nonliteral.
  Five classifier services are bounded; a wrong callback-table entry rejects.

Helpers remain bounded services in these tests, not a claim that the complete
allocation/query systems or gameplay were rerun. The symbolic relation covers
normal mapped/aligned memory with disjoint private stack; it does not assert
portable C fault-register identity, universal C aliasing or initialized padding.
The guarded production instructions separately have exact retail bytes.

## Whole-image and production adoption

Baseline consumer **7a4b03cf**, tools **d1a2f59**. The **1,455-input** snapshot
uses 1,442 verified immutable-snapshot links and 13 copied task files; zero live
worktree hardlinks. Actual shadow Make and production Make compile the C;
no prebuilt object is installed. Exactly four frozen inputs change: source,
guard CSV, owner object and ELF. **1,451 inputs stay unchanged**. Only one of
698 objects changes; all 40 neighbors, all other **6,050 function bodies**,
all **6,051 addresses**, normalized pools and register metadata stay fixed.
Conversion/progress CSV and build profiles remain unchanged. The old guard
CSV is an exact byte prefix with 50 appended rows.

Complete production ELF equals its independent prediction: **617
changed bytes, zero exclusions**, with three explicit metadata serialization
groups. All **20,289 named definitions** agree except target
extent 664. Four symbol-value/name, protected-data and target-word corruption
controls reject. All **189,088 protected data bytes / 720 owners** remain exact.
Production ELF SHA256: `2711331d57051de4023bf9bbcaba159b2e44db87631e454b2862428d4a5d8d39`.
The existing duplicate `generated_12D630.c.o` Make warning remains pre-existing.
Shared progress/tools checks and the fresh production recount also pass.

Prepared qualification uses the retained snapshot and a fresh owned output
path in `CBFD_GROUND_LINK_WORK`:
`python3 -m unittest tools.tests.test_game_ground_link_151aadf8_recovery -v`.
Receipts, actual module origins and final primary/sibling/installed runs are
under `conker/build/game-next-151aadf8-private/adoption/`.
The sibling's 2,434 dirty paths and 339 dependencies stay untouched. At the host
path only `.codex`/`recomp_scene` remain; no source checkout can be synchronized.
No host, Release, save, dependency update or push.

## Bounded advisory review and next target

One Claude analysis was attempted/completed on the existing claude.ai /
firstParty / Pro route, without a model/account/provider switch. Its emitted
init and final stream show tools=[],mcp_servers=[] and no tool use. Packet
SHA256 `0371d68ea024b4cfa1c61f5ca9016b1cca000c93da1b7c82040631ff7adc828a`.
The suggestions repeat scoped-initializer/PRNG-residency probes already tested;
their proposed instruction-count/frame-word causality is unsupported. No
review-suggested patch is adopted by agreement. Independent complete-state
proof and the existing insertion-capable constructor precedent settle the
implementation. No second request is made.

Graphify is refreshed with scoped AST extraction and old-ID retention, without
claiming full-corpus re-extraction. Commit tools before source/docs/consumer pin.
Next inspect `func_151AB9C8` from the actual unmatched list. The 85% goal stays active.
