# Game Record Actor Position Conversion

Date: 2026-10-08

## Result

Continue [Note 1145](1145-game-record-callback-update-conversion-20261008.md)
with the [focused workflow](../AGENT_WORKFLOW.md), one Codex writer and zero
Claude calls. Recover complete `func_151D75C4` in
[generated_204660.c](../../conker/src/game/generated_204660.c):
VA 0x151D75C4..0x151D7724, ROM 0x204A74..0x204BD4,
**88 words / 352 bytes / retail frame 0x30**. Retain original assembly.
The selected raw C emits 88 words/frame0x38 with exactly six differences.
A closed owned-frame mapping derives six expected-word guards, preserving
all seven relocation-bearing words and every other instruction. No insertion,
omission, padding, register remap or retail-word lookup. This is not guard-free.

Fresh production audit confirms **88 / 88 retail words**, no differences or
address drift, **every byte of the complete ELF unchanged**, and all 6,058
symbols' bodies/addresses/extents plus protected data unchanged. ELF SHA-256
remains `f240ca73721dfd7a24c0a85fd5697d45ea1ebc724a11ebd76d965e6b3cd86e99`.
Exactly one 352-byte progress row changes asm -> c; the original 11,469 guards
remain an identical byte prefix, with six appended guards for **11,475**.
Makefile, original assembly and retail inputs are unchanged.

| Section | Converted | Converted bytes | Byte-exact | Drift | Different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,484 / 6,042 (90.76%) | 1,938,336 / 2,256,728 (85.89%) | 3,395 / 5,484 (61.91%) | 0 | 2,089 |
| Init | 492 / 539 (91.28%) | 151,796 / 164,048 (92.53%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,811 / 5,321 (90.42%) | 1,766,900 / 2,072,880 (85.24%) | 2,722 / 4,811 (56.58%) | 0 | 2,089 |
| Debugger | 181 / 182 (99.45%) | 19,640 / 19,800 (99.19%) | 181 / 181 (100.00%) | 0 | 0 |

The 6,042 main slots exclude 16 overflow symbols; raw CSV has 6,044 records
because two section headers repeat. Root README changes its four affected
aggregate rows only.

## Recovered Contract

The callback takes owner and returns s32. Dereference owner+0x40 without an
invented null-actor guard. Read actor's active word first; only if nonzero
compare owner identity +0x44 against actor identity +0x3B. Inactive or mismatched
actors return zero without touching the position flag or optional fields.

Load actor matrices at +0x1D4. Null matrices clear bit 0 of owner+0x2D and
return one. Otherwise read actor+0x31C, its optional byte +0x197 and actor+0x318
in short-circuit order. A nonnull secondary with nonzero byte and nonnull
linked pointer also clears the flag and returns one. Only after that gate
read actor byte +7; a value other than 0xFF takes the third clear/one-return path.
Other flag bits are preserved. No branch speculatively reads later optional data.

Unsigned owner joint byte +0x45 selects a 12-byte vector in D_800AB280 and a
byte in D_800AB2D4. Pass that vector, owner position +0x30 and actor matrix base
plus mapped joint *0x40 to the complete `func_15143134` transform.
After its return, OR the live owner flag with one, then read signed callback
byte +0x46. -1 returns one; every other signed value indexes D_8008FCA8 and
forwards the secondary callback's full s32 return unchanged. Transform mutations
to the live flag and callback selector must remain observable.

Keep original owner, owner+0x40 binding and owner+0x28 record pointers across
the transform; do not reload the actor from a possibly mutated owner+0x40.
Raw/private frame differences are separate from public read/write order and
callback return propagation. Test fabricated valid tables across all 256 byte
selectors; this does not establish the retail-valid selector domain.

## Fitting And Frame Closure

The initial complete form is 84 words/frame0x38 with 62 differences. Sharing
the actual record pointer lifetime fits 88 words with only six differences.
Test 38 complete forms, including 24 real declaration permutations, and four
compiler profiles. Five compiled semantic negatives are effective: signed joint,
unsigned secondary callback, overwritten flag, fixed return and early selector.
No production profile change.

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_actor_position_candidates.py)
requires the complete 88-word relocation-masked source SHA-256
`0ea420bbf1dcdd9d19793777724c0051565686c7d51f6d3c7f12dae6c8e8e844`
and all six exact frame words. Seven relocation uses are separately checked
against their original symbols/types; their instruction words stay unchanged.
Map the frame allocation/deallocation 0x38 -> 0x30, record save/load slot
0x18 -> 0x20, and incoming owner save/load home 0x38 -> 0x30. Leave RA+0x14
and binding+0x1C unchanged. The three saved locations remain distinct; the
outgoing area is untouched and the incoming owner home stays at the caller's
original SP. Enumerate all eleven SP-base instructions and the two call paths.

Reject wrong extent, all 88 stale opcode controls and all six stale padder
guards. Six effective omitted-adjustment controls witness saved-SP mismatch,
real unmapped reads, a write outside the incoming argument home, or changed
callback arguments. None relies on timeout or unsupported instruction.

Raw/retail private memory identity is not claimed. For complete nested helpers,
require an exact +8 translation of owned scratch pointers in call arguments;
preserve pointer distinctions rather than replacing them with an opaque token.
Public memory read/write events and values remain unnormalized and exact.
Normalized/retail complete GP/FP/memory/event state agrees, including private state.

## Qualification

The [focused suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_actor_position_match.py)
reuses the existing Shaping/Triangle/Point oracles and native32 harness, with
an independent typed reference for the complete entry. No new instruction emulator.

- **14,912 cases / 44,736 executions** compare raw C, normalized C and retail,
  including all unsigned joint and signed secondary callback bytes, eight
  gate shapes, flag bits, live transform mutations, zero/nonzero callback
  results and both stack phases. All 85 reachable words execute; the three
  compiler-generated pre-likely duplicate loads at +0x38/+0x5C/+0x98 are unreachable.
- **1,404 missing-byte pairs**, 48 lazy trimmed cases and **32 table/owner
  alias cases** qualify public access order and fault prefixes. They are
  emitted-instruction model evidence, not portable invalid C access or hardware traps.
- **73,728 actual native 32-bit C cases** cover all 65,536 flag/joint pairs and
  every signed callback byte across eight gates/four mutation modes. Check
  full 512-byte owner canaries, coordinates, sign-distinct indirect targets,
  live flag/selector changes and forwarded s32 returns. Transform and secondary
  callback remain bounded stubs in this native test.
- **56 cases / 168 executions** use the actual seven retail position vectors
  and map bytes `0f110f0206060e00`, complete 98-word point helper, 46-word SDK
  conversion (45 reachable), 40-word matrix helper plus 13-word continuation,
  and 49-word translation helper. Check float/fixed matrix paths and independent
  expected transformed coordinates. All 45 reachable SDK words execute.
- **160 cases / 480 executions** enter complete 81-word `func_151D7264` through
  actual primary callback table slot 0, connecting this 88-word body, point
  helper, 12-word magnitude and 26-word attached clear. Qualify captured/live
  flags, failure marking and concrete slot/nested clear writes. Secondary
  callback remains bounded; this is not complete gameplay acceptance.
- Preserve **22 copied-owner neighbors**, pools, relative relocations and
  the four existing diagnostics. The actual padder emits 352 bytes without
  `.space`; four independent GNU symbol sets qualify **96 execution cases**,
  with joint-map/function-table HI/LO carry controls. This is not a separately
  rebased original-assembly pair.

Fresh pre-install ten-test run passes in **143.377s**, no skips. Then strengthen
the two connected tests to exact +8 scratch-pointer translation in call records;
their corrected selector passes in **2.867s**. Only call arguments are mapped,
not coincidentally pointer-sized integer data in public events. Fresh 24 shared
padder/linker tests pass in **0.318s**; mounted and older tools checks pass.

Earlier runs failed on fixture issues: inherited signed-byte support, an
undersized native actor buffer, one exploratory record-pointer lifetime,
unguarded execution of intended semantic negatives and ineffective assumptions
about individual home stores/loads. Correct the fixtures before clean runs;
do not label those earlier commands passing. Prior renderer/neighbor suites
remain historical, not newly rerun wholesale. Full production audit passes
after installation; all ten focused tests pass again in **134.082s**, no skips,
including the exact nested scratch-pointer mapping. Fresh post-install 24 shared
tests pass in **0.302s** and both tools checks pass. Ten tool files parse and
match the older mirror; **132 documents / 4,133 relative links / zero broken**.
Production build succeeds with the existing duplicate generated_12D630 recipe
warning and existing C diagnostics, not a warning-free build.

## Receipts And Banking

Ignored receipts are in `conker/build/game-record-actor-position-test/`:
`baseline.json`, `before.elf`, `before-manifest.csv`, `slot.json`, `guest.json`,
`faults.json`, `forms.json`, `owner.json`, `linked.json`, `native.json`,
`connected.json`, `partial-negatives.json` and `caller.json`. Do not commit
ELF, progress CSV, temporary sources or private receipts.

```sh
python3 -m unittest tools.tests.test_game_record_actor_position_match -v
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_record_actor_position_match.GameRecordActorPositionMatchTests.test_06_linked_baseline_or_installed_closure -v
make -C conker match-progress NON_MATCHING=1
```

Per "Keep commited", bank tools
**de603efbce5035d9304776f345e5e1b4c1bffef5** first, then parent source/manifest/
docs and exact gitlink. Mirror only the two new files after absent-path and
exact-byte gates. Preserve older standalone HEAD ddbdd16 and independently
dirty shared helper/effect test and unrelated paths; do not reset, duplicate
its history or push. Root README changes aggregate rows only.

Manual Graphify refresh after installation refuses 16,890 nodes over retained
38,678; retain 19,398 nodes from 2,972 still-existing excluded files without
forcing a reduced-corpus overwrite. Graph repair stays open. No OGL/Release,
runtime/save/editor, bridge or account changes. The wider Game goal stays active.

## Next Work

Recover **func_151D71B0**, VA 0x151D71B0..0x151D7264,
ROM 0x204660..0x204714: **45 words / 180 bytes / frame 0x50**.
Its C body is still a false zero-return placeholder, not retained GLOBAL_ASM.
Recover the signed type, byte arguments, float threshold, 24-byte initial record,
nine-argument creation call and conditional memcpy into owner+0x28; preserve
uninitialized/private payload padding rather than inventing initialization.
Its allocator/constructor callees remain separate boundaries.

`func_151D7538` is already restored and byte-exact as a 35-word three-argument
event handler through D_8008FCA4, not an unqualified one-argument primary
callback. Do not infer valid primary callback indices from adjacent words in
the shared data pool. Likewise, `func_151D8718` is already converted. No
GLOBAL_ASM remains in this owner, but that does not make its false C placeholders
semantic or complete. Hardware/gameplay and remaining linked setup stay open.
