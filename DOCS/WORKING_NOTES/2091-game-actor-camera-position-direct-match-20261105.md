# Actor camera-position forwarding directly byte-exact

Date: 2026-11-05. Target: `func_1509C8FC`, owner `generated_C98F0`.
Source: `conker/src/game/generated_C98F0.c`; original: `conker/asm/C98F0.s`.

## Result and scope

The false zero-return placeholder is replaced by semantic C which emits all
66 retail body words directly under the existing IDO O2/g3 profile. Its
24-byte frame, five bindings and three trailing alignment words match.
No guards, compiler-profile changes, assembly replacement or shared-header
edits are needed. The matcher describes the complete 69-word slot; the
executable body itself is 264 bytes.

Production is **4,162/5,512 (75.51%)** total and **3,489/4,839 (72.10%)**
Game, with zero address drift. Init remains 492/492 and Debugger 181/181.
Converted inventory stays 5,512/6,046; 1,350 converted functions still differ.
The current 80% threshold is 4,410 exact functions, requiring **248 more**.

## Retail contract and recovered source

The body spans VA `0x1509C8FC..0x1509CA04`, ROM
`0xC9DAC..0xC9EB4`. The slot continues through `0x1509CA10`, ROM
`0xC9EC0`, with three zero alignment words. Entry arguments are full words
`s32 key, s32 alternate`; return is unused by both observed call sites.

The routine calls `func_1505EEF4(key & 0xFFF)`. A null result returns without
reading actor coordinates or camera state. A successful lookup reads
`D_800DBFF0`, tests bit `0x100` at offset `0x2C`, and selects the single at
offset `0x760` when set or `0x37C` otherwise. It loads actor position singles
at `0x14/0x18/0x1C`, truncates each to a signed word and narrows to signed
16 bits. Nonzero `alternate` calls `func_150221E8`; zero calls
`func_15022190`. The fourth argument is the selected single plus `180.0f`,
passed as float bits in A3 under the mixed o32 signature.

The names camera/heading reflect the existing state usage and 180 addition;
no new gameplay or hardware interpretation is claimed. Both output routines
are also inspected and executed from original retail instructions: the first
stores position at `D_800C358C` and the single at `D_800C3594`, then sets
`D_800C3663=1`; the second uses `D_800C3598` and `D_800C35A0`.

Actual SDK `struct127` supplies the actor position members; `struct108`
supplies the flag and `unk37C`. The unnamed `0x760` single uses a local byte
offset view. Local typed externs recover the pointer return and all helper
argument widths without changing shared declarations. Explicit `(s16)(s32)`
casts expose the two-stage retail conversion and emit the same words as
the original direct-short-cast screen. Native qualification uses finite
coordinates representable as signed 32-bit integers, including values beyond
signed 16-bit range; it does not claim portable C conversion of NaNs,
infinities or out-of-range signed-word values.

The second incoming word is stored at incoming SP+4 before the lookup and
reloaded afterward. Qualification includes an opaque lookup which changes
that home, changes actor coordinates/flags, or replaces the camera pointer,
while clobbering volatile GPR/FPR state. These changes must be observed by
the recovered wrapper.

Five bindings stay at `+0x10` (lookup JAL), `+0x20/+0x24` (camera-pointer
HI16/LO16), `+0x98` (alternate helper JAL), and `+0xF0` (primary helper JAL).
The complete aligned retail census has direct calls only at ROM `0xC99AC`
and `0xC9BD0`, both in `func_1509C440`, and no target-pointer literals.

## Focused qualification

The new tools are `game_actor_camera_position_candidates.py`,
`game_actor_camera_position_match.py`, and
`tests/test_game_actor_camera_position_match.py`. Existing parsers, compiler,
padder, native32 and MIPS helpers are reused; no shared helper is edited.

```sh
python3 -m tools.experiments.game_actor_camera_position_candidates
python3 -m unittest tools.tests.test_game_actor_camera_position_match -v
python3 -m unittest tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
```

All nine pre-install checks pass in 51.606 seconds. The fresh installed
nine-test suite passes in 47.204 seconds. Shared 19 regressions pass in
30.220 seconds, and `make tools-check` passes.

- 6,688 cases per original/direct body cover all 4,096 low keys, upper key
  bits, full mode words, both flags, coordinate truncation/wrap boundaries,
  heading arithmetic, null lookup and three post-lookup mutation modes.
  All 64 reachable words execute. The two duplicate LWC1 words at
  `0x1509C940/0x1509C9A4` follow unconditional branches and are unreachable;
  their active counterparts are branch-likely delay slots. Both unreachable
  words remain byte-exact and are never deleted from comparison.
- 360 actor/camera/argument-home alias cases per body compare complete guest
  backing memory and private state. Some aliases overwrite the saved return
  address or turn the camera pointer into an unmapped address. Their actual
  redirected return or fired partial read state is compared; unmapped reads
  also require the independent reference to encounter the same missing byte.
  They are not called successful ordinary returns. A null lookup succeeds
  with camera pointer/state and actor bytes unmapped.
- 216 connected cases per body execute the original 55-word lookup and
  22/19-word output routines, exercising every eligible actor slot and
  exclusion of reserved slot 25. The connected inventory is 96 words;
  89 are reached by this corpus. Previously matched helpers gain no new
  function credit from this connection.
- Both authentic call windows in `func_1509C440` pass 40 cases per body:
  `0x1509C4E8..0x1509C514` (11 words) and
  `0x1509C70C..0x1509C73C` (12 words), with the latter stopping at its
  existing `0x1509C7B8` continuation. Their earlier mode gate is assumed.
  Opcode mask `0xF000==0x2000`, modes zero/one, the first caller's saved-word
  reload and the second caller's alternative byte store/RA reload are checked.
  The large placeholder parent remains uncredited.
- 312 fired root-memory access prefixes compare complete private state.
  This is emitted guest access-order evidence, not portable C fault behavior.
- Six independent GNU links compare separately assembled original and
  compiler bodies over three function/global layouts, including HI/LO carry
  edges and relocation of all three call targets. Forty-eight cases per body
  pass across those rebases.
- Native32 O0/O2/O3 execute 65,536 direct and 65,536 typed indirect calls
  each, totaling 393,216 positive executions. Actual SDK layouts and finite
  signed-word conversion boundaries are checked with trap UBSan and explicit
  float-cast-overflow instrumentation. Six independently compiled wrong-C
  controls fail; six actual IDO controls also have guest counterexamples.
- Whole-ELF corruptions outside the routine, in metadata and in the preserved
  alignment tail are rejected. The copied raw/padded owner preserves both
  neighbors, normalized pools and all five target bindings.

Early fixtures incorrectly counted the unreachable duplicate loads as live,
stopped the second caller before its continuation, and assigned camera memory
the oracle's stack address. The fixtures were corrected before the accepted
full runs. An unused native helper was removed under `-Werror`. Product C,
retail bytes and shared tools were unchanged by these corrections.

## Production closure and recount

Actual Make completes with exit zero for the ELF and progress CSV. The
production owner equals the independently compiled/padded owner, and the
complete production ELF equals its independently linked prediction.
Only the target body and its symbol-size change from 12 to 264 account for
the entire **202-byte** ELF delta. All 6,052 function addresses and every
other body remain fixed; no section, symbol, metadata or owner is excluded.
The complete 69-word linked target slot equals retail, including alignment.

Guard CSV bytes are unchanged, with zero appended rows. The frozen retail
input, original assembly, layout, linker, Makefile, conversion CSV and three
shared headers remain exact. Protected Game data stays 189,088 bytes across
720 owners, with zero differences. No new warning is introduced.

`make -C conker all` generates the code binary and then returns 2 at the
existing overall retail SHA check, as expected for the incomplete decomp.
The duplicate `generated_12D630` recipe warning remains.

Fresh authoritative recount:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,162 / 5,512 | 75.51% | 0 | 1,350 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,489 / 4,839 | 72.10% | 0 | 1,350 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

The README changes aggregate matching rows only. Detailed recovery evidence
stays here; current indexes receive concise continuation entries.

## Fingerprints and preserved work

| Artifact | SHA-256 |
| --- | --- |
| Raw compiler target | `12c37669dabaa8f7c2ebc28cb84dbdd5fea06c617b62cdb1bdb9fd4a8d6f6a70` |
| Linked retail body | `29607fc33920695bb0741b090816807d0b0acc1757ae5c788bfe24166e785188` |
| Frozen predecessor ELF | `1d56f2554e0bc910fcec5498bfc78a5fd72c7711832be629b2037987fef5a9f9` |
| Qualified/production owner | `48feaaded5dc1cbc0d44b774e771be6b30f75b5343315f021d64b14a080049f3` |
| Qualified/production ELF | `0547aedf1ed72a2ee2dc86c0b28a5f40d33f098984f9b078c5d11ce4f53afcde` |
| Production code binary | `101946badb5a57c42e293ee9042a8109bda45871ba4769fd93d356c7f531939d` |
| Guard CSV, unchanged working bytes | `1bb99ac99a4ee64a166ac72314f7af2b3d44d88cbfe954522f88242233415466` |
| Protected Game data | `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670` |

Frozen inputs, copied raw/padded owners, independent images, original target,
native sources/binaries, JSON receipts, Make logs and live recount are kept
under ignored `conker/build/game-actor-camera-position-1509C8FC-match/`.
No pre-existing checkpoint is overwritten or credited as a fresh test.
No fresh old-neighbor suite is claimed; both neighbors' raw/padded bytes,
bindings and pools provide unchanged-scope reuse evidence.

Main baseline is `fe5a0dcd085f23926988b0eebdf2f30f1cf77119`; mounted tools
baseline is `8dbfa7fe55759b1eecf4d1c2c0a09eac5a7b19ae`.
Native Windows Git reported both clean before new work. The separate sibling
tools checkout remains at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with
six pre-existing tracked changes and 2,428 untracked files untouched.
The WSL snapshot's Git status normalization differs from native Git;
content edits and staged scope are reviewed using native Git. Fresh target
checks use only the mounted checkout; second-checkout qualification is not
claimed.

## Continuation and graph retention

Actual production ranking selects `func_150EB090`, 76 words and 65 real
differences. Keep the seven documented boundary cases separate:
`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC` and `func_150A6760`.

Standard Graphify update refused a reduced 24,856-node extraction, retaining
the existing graph. Scoped maintenance of seven changed paths produces
58,658 nodes, 112,416 links and 5,124 communities. It retains 58,647 old
nodes and replaces three relocated update-log headings by the same
label/source; eight nodes are added from this note. No node outside the
changed paths is removed. The graph SHA-256 is
`f73a6ebf1514d14f4a9b947c2ea66fd957ee190dccd00a73c6d17effebf3fe3a`.
Existing exclusions retain 31,816 nodes from 3,754 still-existing files.
This receipt establishes scoped structural maintenance and old-node
retention, not full-corpus re-extraction or fresh extraction of excluded
source files. The ignored `graph-retention.json` records the comparison.

Mounted tools are committed first as
`f66a70a74094586c7b8ea88295f7f14c4e26b120`
(`test(game): qualify direct actor camera-position forwarding`). The
consumer includes that pointer, the recovered C and documentation; guard
CSV bytes remain untouched.
