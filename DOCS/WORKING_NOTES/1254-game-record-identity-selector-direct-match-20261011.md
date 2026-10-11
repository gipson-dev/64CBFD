# Record Identity Selector Direct Match

Verified 2026-10-11. Consumer baseline
7f8f539bc6db2550fec2af8e7ed4cbe3da63cf8c; mounted tools baseline
69e37a6b9be51a78ef688bce2571c439beba59bc. New tools
e2237b9260e1aed8d8958a00088425c88cfc3b9d committed first. No push.
Single Codex writer, zero Claude calls; DOCS/AGENT_WORKFLOW.md applies.
Previous goal turn banked the complete actor-identity lookup. This finishes
another complete routine; the wider Game goal remains open.

## Recovery And Direct Match

Recover func_15083DA0, VA 0x15083DA0..0x15083E0C,
ROM 0xB1250..0xB12BC, in conker/src/game/generated_AEB40.c.
Replace the 12-byte zero-return placeholder with s32 (void). All 27 words /
108 bytes emit directly from C, no frame, four relocations, no new guards,
pools or compiler profiles. Move the existing IndexRecord15083E0C typedef
and D_800D20FC declaration just above the selector so it shares the query's
already recovered 48-byte record type. Do not duplicate globals or change
other routines' interfaces. The complete first selected candidate matches.

- Start candidate identity at signed word 1 and cursor at zero. Read unsigned
  byte D_800D2100 once. Zero count returns 1 without reading D_800D20FC.
- Positive count caches the record pointer. Read identity at +0x28 using
  48-byte indexed records. Do not add active/occupancy filtering.
- A match increments the candidate and resets cursor to zero; the common
  loop increment then resumes at index one. Preserve the retail quirk.
  For identities [2, 1, 0], return 2, not an idealized unused-ID answer 3.
- Keep the candidate as a word so a table containing 1..255 can reach 256.
  After traversal, values >= 0x100 are capped to 0xFF. No byte wrap to zero.
- Preserve cached global accesses, multiply/address arithmetic, branch-likely
  cursor update and return paths. This leaf does not write stack or records.

Unsigned candidate compiles to 27 words with one instruction difference;
it is not labeled a behavior-changing negative for this bounded domain.
Restarting at -1 also gives one difference but changes behavior. A byte
candidate emits 29 words/20 differences and breaks the saturated result.

The sole direct retail caller is complete 477-word func_150169A0 in
asm/43D00.s, VA 0x150169A0..0x15017114, ROM 0x43E50..0x445C4.
It invokes this no-argument helper only for a record with zero identity,
stores the returned low byte at +0x28, reloads count and advances 48 bytes.
Its current C body in generated_43D00.c remains a zero-return stub. The
complete original caller is exercised below, not its installed C placeholder.

## Fresh Qualification

Nine final tests pass after installation/rebuild, 51.842 seconds.
Immutable snapshots and fresh independent receipts live in
conker/build/game-record-identity-selector-test/. Consumer make tools-check
and mounted standalone check_project_tools.py both pass under WSL.

- 65,823 independent-reference cases / 131,646 original/C guest runs:
  all 65,536 two-record byte pairs, every count byte, empty/one/max counts,
  duplicate and reversed identities, restart quirks, complete 1..255 tables,
  two stack phases and wrapped record pointers. Reach all 27 retail words,
  including the saturated cap. Full memory/access order/return/GP/FPR agree;
  no helper calls or writes. Wrapped/private behavior is guest-only.
- Keep the existing proven TriangleOracle runner and instruction execution.
  A local, restored globals patch raises only its finite range(50000) loop
  budget to 400000 for complete saturated traces. No shared oracle edits or
  instruction-logic rewrite. The saturated reference has 32,642 accesses;
  its cap path is actually executed, not treated as unreachable.
- Ten alias/short-circuit cases / 20 runs and 434 fired all-access fault
  pairs: empty count accepts unmapped pointer, count/pointer/record fields
  overlap, low pointer byte aliases count, records overlap stack, unsigned
  128/255 counts and restart order. Every selected gate fires; full partial
  memory/events/calls/GP/FPR agree. Four additional saturated fault pairs
  fire at ordinals 0/1/2/32641. These are sampled cap-trace faults, not an
  exhaustive claim for every saturated access. No portable C fault claim.
- Three independent symbol sets / nine original/C/production-padded links,
  15 cases / 45 runs. Both global HI16/LO16 pairs are independently rebased
  with code across signed low-half carry boundaries.
- Actual copied-owner preprocessing, IDO compilation and asm post-processing
  preserve all 30 neighbors' full fingerprints, extents, relocations and
  normalized pools with zero owner diagnostics. The existing record typedef
  moves without changing the completed record query or actor lookup. Both
  production padding routes preserve all non-target text/relocations and
  existing guard fingerprints. Historical suites are reused only through
  fresh complete fingerprint equality, not claimed as freshly rerun tests.
- Twelve effective fresh IDO controls: ten result-changing start/restart/
  skip-one/comparison/byte-candidate/cap-bound/cap-value/count-sign/field/
  stride negatives, plus two cached count/pointer access-order negatives.
  The volatile controls preserve result here but add observable reads and
  fault points. Reuse existing local signed-byte and unsigned-divide oracle
  execution for controls/caller; no shared helper modifications.
- Native32 O2/O0 each pass 66,560 cases, 133,120 total: exhaustive pairs,
  every count with four record patterns, restart and saturation. Check
  32-bit pointer/integer widths, 48-byte record size, complete canary-filled
  pool bytes and globals unchanged. An effective native restart negative
  fails. Native qualification excludes wrapped pointers/private fault order.
- Execute complete 477-word retail caller with original/C selectors in
  90 cases / 180 runs, 228 helper calls per form. Independently compute the
  identity sequence published into initially zero-ID records and verify
  no calls for nonzero records, plus both downstream partition calls. Cover
  counts 5/8/16/128/255, scene-entry counts 0/1/2 and two stack phases.
  Fully empty tables are tested through count 16; larger caller tables use
  at most two zero IDs. Leaf saturation at max count is separately complete.
- Caller qualification uses category zero and zero scene presence mask;
  resource/copy/allocation/reset/partition peers are bounded callbacks.
  Initial scene entries may execute the inactive-record branch, not deep
  actor geometry/float processing. Current caller C, other category jump
  tables, real resources, allocation and gameplay remain unqualified.
  Do not claim full initialization/gameplay acceptance from this connection.

Initial fixture corrections: declare the native helper before its runner
uses it, and map the complete caller global word at D_800D2110 rather than
only its first byte. Populate native padding with canaries. Explicitly bound
large caller empty-record patterns to avoid a cubic repeated-fill stress run;
do not change the complete helper, bypass saturation or weaken any ELF gate.
All nine final tests are fresh after the corrected pre-install suite passed.

## Linked Audit And Progress

Only 77 ELF bytes change, inside the target's 108-byte slot and its
12 -> 108 ST_SIZE field. Every other ELF byte and metadata field is exact.
ELF 3,261,160 bytes, SHA-256
86ed17bd1d085bbf806272c197f38010c7cea69b6c0f9614be2b28c9e71a5800.
Protected data: 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
New owner: 13,306 bytes, SHA-256
4845983a3be0018788520f73d60e491fcc846d864e13f4c86796e87e41b77c1c.

Guards stay byte-identical at 1,940,850 bytes, SHA-256
5e50f8952c0e5d4ba39b7e9054b7ac5727517d021ba8e92d3b10c8a2f07b2f19.
Conversion CSV stays byte-identical at 317,252 bytes, SHA-256
32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.
Rodata, layout, symbol addresses and ignored auto assignments remain exact.
Linked rebuild succeeds with existing duplicate generated_12D630 recipe
warnings; no warning-free full-build claim. README changes two matching
rows only; function-by-function recovery details remain in DOCS.

Fresh matching: Game 2,786/4,822 (57.78%), total 3,459/5,495 (62.95%),
zero drift / 2,036 different. +1 matching only, no converted credit.
Converted stays 5,495/6,044 (90.92%), Game 4,822/5,323 (90.59%), converted
bytes total 86.01% / Game 85.37%. Init 492/492 and Debugger 181/181
already-converted functions remain exact.

```sh
python3 -m tools.experiments.game_record_identity_selector_candidates
python3 -m unittest tools.tests.test_game_record_identity_selector -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
cd tools && python3 check_project_tools.py
```

Older standalone tools HEAD ddbdd16 stays unchanged: 277 existing dirty
entries plus two absent-only byte-identical new mirrors = 279. Protected
older helpers remain exact; no existing paths overwritten or committed.
Native Graphify query found 31 nodes, showed 22 and truncated nine. Native
update exits 1, refusing unsafe shrink 39,691 -> 17,909 and retaining
19,398 nodes from 2,972 excluded-but-existing files. Preserve version and
devcontainer.json zero-node warnings; no force, purge or install. Require
fresh post-commit log growth/Rebuilt tail and zero actual workers before
reporting clean. Retail-only matching, not a host repair. No OGL/Release,
saves, editor or private inputs changed.

## Next

Recover complete 194-word func_15084044 in the same owner,
VA 0x15084044..0x1508434C, ROM 0xB14F4..0xB17FC.
Current no-argument stub returns zero. Original uses actor pointer and channel
index, original 0x60 frame/S0..S5 lifetime, actor/parent configuration mode,
identity table lookup and two pointer slots at actor+channel*8+0x28C/+0x290.
Identity zero forces mode 2, overriding the configuration's low two mode bits.
Inspect early complete-pair/resource-NULL exits; mode 0 shared pair/count+2;
mode 1 mirror/share or allocate-copy; mode 2 independent pair preparation.
Preserve live shared-count/source/pointer reloads across callbacks, 16-byte
size scaling, allocation failure stores, second-buffer failure free/count
rollback/first-pointer clear and failure flag result. Mode 3 does no work.
Qualify complete caller contract, all modes, aliases, callback mutations,
private faults, both padding routes and protected sections before installing.
Broader timeline matching and real caller/resource/initializer/allocator/
hardware/renderer/gameplay acceptance remain open; keep the wider Game goal active.
