# Actor-snapshot accumulator emitter recovery and guarded byte match - 2026-11-17

`void func_151AB9C8(u8 *record)` replaces its zero-return placeholder with the
complete actor-snapshot validation and accumulated particle-emission callback.
Its **227-word / 908-byte retail slot and frame 0x118 are byte-exact**.
The complete semantic C also emits 227 words. **150 relocation-aware expected-word
guards** normalize register allocation, local-buffer placement, constant-address
materialization and loop scheduling. **77 words emit directly from C**; no
insertions, omissions, compiler-profile changes, dummy locals or handwritten
function replacement. This is a guarded C match. VA 151AB9C8..151ABD54,
ROM 1D8E78..1D9204.

Accepted total **4,531 / 5,514 (82.17%)**, Game **3,858 / 4,841 (79.69%)**,
Init 492/492, Debugger 181/181; zero drift, **983** different. **156 further
matches** are needed for the active 85% goal. Conversion stays 5,514/6,048
(91.17%), 86.19% of bytes. Root README changes only the Total and Game rows.

## Recovered behavior and interfaces

The existing `func_151AB930` producer copies a 28-byte snapshot to record+0x28
and selects callback 14. Its captured actor pointer, byte identity, full 32-bit
saved value, accumulator, base/range and byte selector have an explicit local
typed view. Validation checks the actor's live first word, identity at+0x3B
and zero-extended halfword at+0x84. The producer supplies a mapped actor pointer;
the live-word test is not a null-pointer guard. Invalid snapshots set the
record's signed lifetime at+0xE to -1 without drawing random numbers.

A valid record adds `(base + draw * range) * D_800BE9A4` to its accumulator
and enters only when the result is **strictly greater than 1.0f**. A 36-byte
surface result is initialized once. Each iteration sequences two integer
draws, four byte-angle lookups, a speed draw, a bias draw, two more integer
draws and a size draw before its 16-argument `func_151D9014` call. The particle
uses the actor's fresh coordinates, 30/75 position scales, randomized speed,
lifetime 32..57, opacity 100..200 and size 34*draw+52. Bias uses multiplication
then addition of -1.0, matching the actual retail FP operation order.
The emitter can mutate the accumulator; the decrement and repeat test reload it.
Calls remain explicitly sequenced in C. No loop cap changes retail behavior.

Actual callback table `D_8008A4E8`, slot 14, VA 8008A520 / ROM 22EFE0 contains this
routine. The complete original `func_15149264` record-tick caller and its table
are literal in production. Its ignored callback return supports the recovered
void interface. The emitter declaration agrees with its existing owner and
o32 argument widths. Providers are bounded contracts in the focused tests;
these checks do not execute the full renderer, allocator or gameplay.

## Independent relation and private-storage boundary

Twenty-nine complete source forms, v0..v28, are retained privately. V28 has the
retail length/frame without synthetic storage. An instruction-driven symbolic
comparison proves **five entry paths and both inductive loop successors**.
It compares ordered FP/FCSR, all public alias epochs, access multiplicities,
stores, helper arguments, passed buffer bytes, retained-provider mutations,
callee saves and return to the caller. Five actual semantic defects reject;
a closed T8/T9 register exchange passes. No instruction words or FP operands
are projected by this semantic comparison.

The raw position/velocity/surface buffers and byte flag sit **four bytes above
retail**, and its cached surface pointer has a separate unpassed home. The
proof maps exposed buffer roles explicitly. It **does not claim identical
unpassed private-stack bytes or scratch return registers**. The final guarded
227-word stream separately equals every original instruction and binding.
Normal execution assumes mapped/aligned memory and a disjoint private stack;
no portable C fault-state, universal C aliasing or padding initialization claim.

Both streams visit 222 of 227 words. Two compiler-duplicated loads are
unreachable, and three BREAK7 words guard divisors known to be 46, 26 and 101.
The loop relation covers arbitrary iterations without a termination claim:
infinity, sufficiently large binary32 values and provider mutations can prevent
the subtraction from ending the loop. Bounded prefix cases retain that behavior.

## Fresh maintained qualification

All **five checks** pass in primary tools, the isolated sibling overlay and
installed production, with identical **nine-file** task fingerprints.

- Both real padders preserve all 40 neighbors and normalized pools. Independent
  original assembly and **12 GNU links** agree across four code/data layouts,
  including independent global HI16 carries. All 20 original bindings are
  accounted. **247 raw-word/binding corruptions** and **600 stale CSV controls**
  reject. There are 150 guards and no insertions or omissions.
- **1,472 guest cases per retail/raw/strict/layout stream** cover all byte
  identities, all validation routes, both stack phases, exact/adjacent thresholds,
  NaN/infinities, mutable actor/rates/selector/time and retained local buffers.
  This includes **64 bounded nontermination prefixes per stream**. Every
  initialized public byte, complete call trace and exposed packet agrees.
- **1,408 SDK32 C cases at O0/O2/O3** pass with strict aliasing and UB traps.
  All five deliberately broken C variants compile and exit3. Nonterminating
  cases are excluded from native completion claims; eight executions have their
  expected outcome. Typed native records and actors preserve the original ABI.
- The **complete 45-word original caller** passes **192 cases per stream**,
  visiting every caller word through the literal slot 14 indirect call. Timer
  subtraction, disabled callbacks, invalid retirement, optional cleanup revival
  and free branches are covered. Two cleanup services remain bounded; a wrong
  callback-table entry rejects.

The caller test exposed an initial fixture error: actor 0x40000 overlapped the
emulator stack. Current actors at 0x60000/0x80000 are explicitly disjoint, and
all affected guest/native/caller gates were rerun. Earlier overlapping-fixture
receipts are superseded and uncredited. A native harness signed-index arithmetic
error was also corrected before acceptance; production C needed no such change.

## Whole-image adoption and reproducibility

Baseline consumer **f417c2b4**, tools **ba812e6**. The **1,464-input** snapshot
uses 1,455 verified immutable-snapshot links and nine copied task files, with
zero live-worktree hardlinks. Actual shadow Make and production Make compile
the C; no prebuilt object is installed. Exactly four inputs change: source,
guards, owner object and ELF. **1,460 inputs remain unchanged**. Only one of 698
objects changes; all 40 neighbors, all other **6,050 bodies** and all **6,051
addresses**, pools and register metadata remain fixed. The old guard CSV is an
exact byte prefix with 150 rows appended. Conversion/progress classification
and compiler profiles stay unchanged.

Every ELF byte equals the independent prediction: **732
changed bytes, zero exclusions**, with explicit metadata serialization groups.
All **20,289 named definitions** agree except the target's 908-byte
extent. Four actual symbol/name/data/code corruption controls reject. All
**189,088 protected data bytes  / 720 owners** remain exact. Shared progress and
tools checks pass; the duplicate generated_12D630 recipe warning is pre-existing.
Production ELF SHA256: `d54f29167c029522c57b33b4a5678ab2e3866b37820686566daeb73b35fea992`.

Selected raw SHA256:
`f34bc68246db0db91395420c1c7a32e7fc7325ab0443d8d5e50b12c09ae11e92`.
Retail SHA256:
`f821a29cc479ed0a2ad690f68eee970045a9dffb24043d377fc6797b56cf0cfb`.
Use a fresh owned path in `CBFD_ACTOR_ACCUMULATOR_WORK` and run
`python3 -m unittest tools.tests.test_game_actor_accumulator_151ab9c8_recovery -v`.
Receipts and exact imported origins are retained under
`conker/build/game-next-151ab9c8-private/adoption/`.

The sibling's 2,434 dirty paths and 339 dependencies are unchanged. At the host
path only diagnostic directories remain, with no available source checkout;
no host, Release, save, dependency update or push. Zero Claude calls for this
routine. Graphify is refreshed with scoped AST extraction, all old IDs retained
and an explicit tools-to-function reference; no full-corpus extraction claim.
Commit tools before source, documentation and the consumer pin.

Next inspect `func_151ACBD4` from the fresh unmatched list. The 85% goal remains active.
