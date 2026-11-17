# Motion-sample strip renderer guarded byte match - 2026-11-17

`Gfx *func_151AD92C(Gfx *output, u8 *record, s32 viewport)` now replaces the
zero-return placeholder with the complete crossed-quad strip renderer. Its
**464-word / 1,856-byte slot and frame 0x130 are byte-exact in production**.
Semantic C emits 469 words; **379 relocation-aware checked guard rows**, three
insertions and eight omissions recover the original private state, allocation
and scheduling. This completes the private work in
[Note 2521](2521-game-strip-renderer-complete-geometry-order-and-loop-relation-20261117.md).

Live progress is **4,534 / 5,514 (82.23%)**, Game **3,861 / 4,841 (79.76%)**,
Init 492/492 and Debugger 181/181, zero drift and 980 still different. The active
85% goal needs **153 further matches**. Root README changes are aggregate rows
only; function narratives remain in these notes.

## Recovered source and transformation

Owner `conker/src/game/generated_1D92F0.c`, VA151AD92C..151AE06C,
ROM1DADDC..1DB51C. The original registered descriptors are classes 47 and 78,
with the three-word renderer callback and returned display-list cursor.
Unsigned count/texture/dimension widths, full-word incoming viewport storage,
the eleven-word texture-helper call and SDK display-list macros are recovered.
The viewport argument remains unused after its original incoming-home store.

Both coordinate bases preserve their distinct norm fallbacks. Saved current
coordinates, tangent components and six saved FP roles retain their real
lifetimes. First/second basis schedules preserve the combined public-store/FP
order, explicitly recovering operand order rather than assuming FP commutativity.

Captured count moves from `SP+0x94` to `SP+0x124`; the zeroed segment cursor is saved and
reloaded at `SP+0x128`. The UV terminal index uses `SP+0x94`. Packed U stays in freed S6,
with the second modify-vertex header rematerialized in a dead scratch register.
This preserves the original arbitrary bytes at `SP+0x90` and `SP+0x12C`. After those scheduling stages, five vacant slots
and a redundant UV guard are removed; two header constants move to their use.
All branch destinations are explicitly rebuilt from instruction origins.

The adopted derivation separates its two header insertions across adjacent
positions, matching the CSV's one-word insertion capability. Its464-word stream
has SHA256 `ac32a2687ef236c7582c16e7da61f0ad2abfc48659dc23c1e36a82496882632e`.
No retail instruction range is embedded in the C source. Raw C SHA256 is
`0418af51e8fc3f1b5c9632de208a59f57b41e57a8844f365c690a2e47ebbb6c1`.

## Complete relation and execution qualification

The composed instruction-driven relation has **four geometry-entry paths,
eight complete generic geometry paths, two provider/setup paths, four generic
UV paths and one unrestricted return path**. It compares every320 private and
incoming-home bytes, combined ordered public stores/FP operations and abstract
status, stable public-read multisets, public bytes and required live roles.
Both loop invariants advance their indices, cursors and coordinate roles.

The opaque provider may alter public state, all eleven argument homes,
caller-saved GPR/FPR values and FP status. Captured locals remain protected;
post-call record, bank and mode reads use a new public-memory epoch. The return
relation also covers empty/single-sample exits without a UV-loop domain bound.
A word is rejoined only when its four actual bytes round-trip to one origin;
the helper does not erase mismatched byte origins.

An independent T6/T7 allocation passes. Ten provider/UV/return negatives reject
wrong homes, missing cursor save, wrong eleventh argument, reloading mutated
count, a private width spill, wrong UV header/limit and broken stack/FPR restores.
Two additional geometry negatives reject a wrong point stride or cached-Z home.
All469 bound source-word corruptions reject before derivation.

All **five final tests pass fresh in both tools configurations**, with no skips:
**413.595s primary / 409.264s sibling-overlay**, including input/import recording.

- Both real padders produce the original unbound body and nine bindings. Twelve
  independent GNU links cover four code/data layouts and HI/LO carry boundaries.
  All32 owner neighbors and normalized pools remain unchanged.
- **478** raw/binding, **1,516** stale-CSV and **385** replacement/insertion/omission
  corruption controls reject. No old guard rows are retired; prior CSV bytes
  remain intact and 379 target rows are appended.
- Retail/raw/derived each execute544 cases. Derived RAM, private/provider frames
  and all **306,846 ordered FP observations** agree with retail; coverage is
  464/464 retail/derived and 469/469 raw. Exact padded-byte identity reuses the
  retail execution for the two padded streams rather than calling it fresh.
- The complete original 348-word caller and 47-word selector pass 64 literal
  descriptor cases per stream; derived full RAM/private stack agree. Caller
  coverage is 282/348. No new synthetic alternate-layer coverage is claimed.
- Seven existing native32 binaries execute fresh after source/binary/fixture
  fingerprint checks: selected C at O0/O2/O3 and four rejecting controls.
  Compilation is explicitly reused from Note 2519; no native FP-status claim.

The symbolic domain is ordinary mapped, disjoint, stable objects, valid counts
0..20, nontrapping FP and a conforming opaque provider. It does not establish
arbitrary aliases, literal fault state, cycle timing or host gameplay acceptance.

## Actual build, image and production gates

The independent Make shadow compiles the complete owner through five real
commands. Production then installs only source/CSV and runs actual Make for the
owner, linked ELF and progress CSV; no prebuilt object is copied into production.

The strict complete-image prediction has **1,454 changed bytes and zero
exclusions**, with no metadata reorder groups. All other **6,050 bodies and all
addresses** remain unchanged. Exactly one of 698 frozen objects changes, retaining
all 32 owner neighbors. All **189,088 protected data bytes / 720 owners** remain
exact. Named-symbol, name-string, protected-data and target-word controls reject.
The production ELF exactly equals the independently predicted image:
`52f67516795ef31a9308728a3357957a1bd16989343abe69e1c54f50e6e26b26`.

Fresh post-install checks compile the installed source and match all 33 compact
owner functions, then execute the actual production target over 544 guest and 64
original-caller cases. Full RAM/provider frames and FP order agree; all 464
production words are visited. The source/padder/symbolic/native receipts reused
at this stage are explicitly fingerprinted. Production `match-progress`,
`tools-check` and an independent actual-ELF recount pass.

The first post-install adapter expected a compact object removed by normal Make
cleanup. It was corrected to use a fresh source compile in a new output folder;
the failure did not indicate a production-image difference.

## Preserved inputs, graph and next target

The 1,547-input production snapshot links 1,542 earlier immutable files and copies
five banked geometry tools; it has zero live-worktree hardlinks. Six new task
files and actual imported helpers are fingerprinted separately. Primary imports
have 351 rows/349 unique tool files; sibling-overlay has 353 rows/351 unique files:
seven overlay, 301 sibling and 45 primary rows. The sibling's 2,434 dirty paths and
339 present scoped dependencies remain intact. Exactly four frozen production
inputs change: source, guard CSV, owner object and ELF. Progress classification
and the retail binary remain unchanged.

The host sibling path currently contains only `.codex` and `recomp_scene`, with
no Git/source checkout available to synchronize or validate. It is untouched;
Release, saves and gameplay are not built, modified or claimed accepted.

Evidence lives under `conker/build/game-next-151ad92c-private/adoption-final/`:
paired sealed suites/imports, both padders/links, symbolic and native receipts,
Make prediction/plan/run, metadata controls, production audit/focus and recount.
The normal Graphify update is fail-closed; the scoped code merge retains old
IDs and an explicit target reference. It is not full-corpus re-extraction.
Commit tools before consumer source/guards/notes/pin, locally only; no push.

Next inspect **func_151AE0E4**, the still-different 96-word neighbor. Its 30-word
dispatcher `func_151AE06C` is already exact; preserve that caller and its current
commutative-operand guard while recovering the next routine. The 85% goal stays
active rather than ending at this checkpoint.
