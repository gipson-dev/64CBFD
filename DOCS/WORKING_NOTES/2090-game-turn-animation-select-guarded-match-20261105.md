# Game turn-animation selector guarded match (2026-11-05)

## Outcome and acceptance boundary

`func_15056A00` replaces a false zero-return placeholder with a complete void
actor-state update. Its natural C body has all 66 words, no frame, the original
two table relocations and both observed flag stores. Ten checked replacements
derive five temporary GPR lifetimes and one commutative row-address ADDU.
No instructions, schedules, frames, profiles, opcodes, immediates or bindings
are inserted, omitted or changed by the fitting.

Production equals the independently qualified image. The live recount is
4,161/5,512 total (75.49%) and 3,488/4,839 Game (72.08%), with zero address
drift. Private source screens receive no matching credit.

## Retail behavior and ABI

| Item | Evidence |
| --- | --- |
| Function / owner | `func_15056A00`, `game_83300` |
| Source | `conker/src/game_83300.c` |
| Original assembly | `conker/asm/nonmatchings/game_83300/func_15056A00.s` |
| Virtual interval | `0x15056A00..0x15056B08` |
| ROM interval | `0x83EB0..0x83FB8` |
| Length / frame | 264 bytes / zero |
| Table | `D_80099A3C`, ten-byte rows |
| HI16 / LO16 | +0x10 / +0x14, unchanged |
| Direct JAL census | ROM `0x8528C` and `0xA550C`; no aligned pointer literals |
| First caller | `func_15056B08`, window `0x15057D98..0x15057DEC`, 21 words |
| Second caller | `func_15077F64`, window `0x15077FF0..0x15078068`, 30 words |

The routine receives an actor pointer, unsigned byte magnitude and unsigned
byte row selector. It returns void. Its entry retains the **full** incoming
A1/A2 words at incoming SP+4/+8, then narrows both arguments. There is no
stack-frame adjustment. Incoming-home aliases are qualified as emitted guest
behavior, not abstract portable C parameter-home requirements.

The ten-byte row supplies magnitude thresholds at +7 and +2. A strict +7
threshold hit selects base 5; otherwise a strict +2 hit selects base 2; otherwise
base 0 remains. The first threshold has priority even for nonmonotonic table
values. Bit15 of the wrapped difference between actor headings +0x78 and
+0x76 adds 3 on the negative side or 4 on the other side. The resulting selected
slots are 3/4, 5/6 or 8/9; no saturation or row bounds check is added.

A selected byte of 0xFF skips the reset block. Otherwise the routine steps the
pointer at +0x218 back five bytes with explicit 32-bit wrapping, stores 20000
at +0x21C, stores 13 at +0x223 and clears the float at +0x44. It then reads
the selected table byte **again**. That second value is captured before the
remaining stores; the actor's earlier writes can overlap the table in guest
memory. Caching the sentinel-test value is an independently rejected error.

The saved flags at +0xF4 first clear mask 0xE, then set bit 0x4, with both retail
stores retained. The cached +0x76 heading is written to +0x78 and +0x7A,
byte +0x138 is cleared, and the reloaded animation byte is stored as a
halfword at +0x244. The existing `struct216` is five bytes, consistent with
the pointer step; no signed-overflow arithmetic or pointer dereference is
introduced by that step.

The first caller window starts after its unrecovered floating eligibility
gate. It checks a table threshold, captures a heading, saves T0/F2, supplies
the three arguments, and restores T0/F2 after the call. The second window
computes the absolute wrapped high angle byte, checks its table threshold,
copies the notice byte to actor+0x250 and invokes the routine. Both skip
paths and both real call sites execute. Neither complete parent C body is
recovered or credited here.

## Source and normalization provenance

The C body is independently derived from the complete retail routine and
both actual callers. It uses the existing SDK `struct127` fields, repairs the
old unprototyped scalar declaration to `void(void *,u8,u8)`, and removes the
obsolete placeholder comment. The opaque input parameter with a local typed
actor pointer recovers the leaf ABI; a directly typed parameter emitted an
eight-byte frame. A ten-byte row view recovers both retail address calculations
without changing the shared `s16 D_80099A3C[]` declaration.

Flat byte views reused the row pointer and emitted 63 words after eliminating
the frame. Explicit observed flag stores emitted 64. Halfword-indexed views
emitted 67; the structured row view with a separate byte entry address emits 66.
The two flag stores use scoped volatile lvalues to retain the observed writes;
this is a matching constraint, not a claim that the flag word is hardware MMIO.
All source screens remain private and uncredited except the qualified body.

The normalizer pins the entire raw body and both relocations. It exchanges
the two commutative ADDU inputs at +0x80 and rewrites five scoped GPR
definition/use lifetimes: selected-entry pointer, saved flags, reloaded byte,
masked flags and final flags. Every non-register bit remains unchanged, and
the exact changed-word set must equal the ten guard rows. There is no schedule
permutation or frame correction. Original/fitted private states are checked
literally; natural C's temporary output registers are not equated with retail.

This regular owner uses the existing `pad_c_object` retail-layout padder,
including its already present overflow regions. The generated-slice padder
is not substituted. Every other owner body, binding, pool and address is
preserved, including the existing nonmatching and GLOBAL_ASM functions.

## Focused qualification

Commands from the consumer root under WSL PSBBN:

```sh
python3 -m tools.experiments.game_turn_animation_select_candidates
python3 -m unittest tools.tests.test_game_turn_animation_select_match -v
python3 -m unittest tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -v
make tools-check
```

The fresh pre-install eight-test suite passes in 64.972 seconds:

- 11,294 guest cases per original/natural/fitted body cover all byte magnitudes
  and selectors, upper incoming-word patterns, strict threshold boundaries,
  reversed thresholds, both heading signs, zero and wrap boundaries, sentinels
  and stack phases. All 66 retail words execute. Cases also use 2,560 bytes of
  the actual protected-data image beginning at the table address. This is a
  mapped-byte window, not an inferred declaration of the table's true extent.
- 4,224 alias cases per body cover 166 aligned actor offsets across the table
  and five private placements, including overlaps of incoming argument homes
  with velocity, flags, command cursor and current heading. Complete backing
  memory is compared, including prefix home stores before any table reads.
- Native32 O0/O2/O3 each execute 65,536 direct and 65,536 canonical typed calls,
  for 393,216 positive executions. Paired cases cover every byte-argument pair
  and every 16-bit heading delta. The actual SDK actor layout is checked;
  table storage is a fresh typeless allocation for 256 synthetic rows. Fifteen
  independently compiled semantic wrong-C controls fail under trap UBSan.
- Both authentic caller windows pass 256 connected phases per body apiece,
  covering taken/skipped gates, input narrowing, heading capture, notice copy,
  saved T0/F2 and incoming homes. The first window explicitly assumes its
  earlier floating eligibility gate has passed. Neither parent is credited.
- 416 fired root-memory access fault prefixes compare complete original/fitted
  private state. A sentinel path succeeds with all otherwise used reset fields
  unmapped. Natural temporary registers at faults are not equated with retail.
- Twelve independent GNU links of original, natural and fitted bodies use
  four function/table layouts, both HI/LO carry edges and a table overlapping
  the incoming argument homes. Seventy-two rebased cases per body pass.
- Three actual IDO semantic controls and a cached-entry control have guest
  counterexamples. The latter aliases the selected byte to the command cursor,
  whose five-byte step changes the later animation value. All 264 raw-byte
  corruptions, three binding changes, three real regular-padder preimage
  corruptions and three inside/outside whole-ELF corruptions fail closed.
- The copied regular owner preserves 88 neighbors and normalized pools. Both
  bindings, every address and protected Game data remain fixed. The literal
  whole-ELF prediction changes 217 bytes, including only the target body and
  its symbol size 12 -> 264, across 6,052 functions with zero exclusions.

Shared 19 regressions pass in 7.775 seconds; `make tools-check` passes. An
earlier caller fixture supplied 0x100 as an allowed input even though the real
caller masks it to zero, and ended the second window before its skip target.
The corrected fixture supplies a nonzero low byte and includes that target.
The isolated caller check passes before the accepted complete rerun. These
were fixture corrections, not production defects or weakened eligibility gates.

## Production closure and recount

`make -C conker -j4 build/conker.us.elf progress.csv` completes successfully.
The common guard prerequisite triggers a full rebuild. Production's regular
owner and complete ELF equal the independently compiled/padded/linked
artifacts byte for byte. The fresh installed eight-test suite passes in
77.879 seconds.

The old guard bytes are an exact prefix plus precisely ten appended rows.
The frozen Makefile, conversion CSV, retail layout, generated linker, shared
headers and complete retail input are unchanged. All 18 GLOBAL_ASM pragmas,
88 neighbors, old overflow regions and normalized pools are preserved.
All 6,052 functions retain their addresses; only the target body and its
symbol-size update from 12 to 264 account for the 217-byte ELF delta.
No metadata, section, function or dependent object is excluded.

`make -C conker all` writes the code binary and returns 2 at the existing
overall retail SHA check, expected for the incomplete decompilation. The
duplicate `generated_12D630` recipe warning and eight inherited owner
declaration warnings remain; no new target warning is introduced.

Fresh recount command:

```sh
cd conker
python3 ../tools/match_progress.py progress.csv build/conker.us.elf conker.us.bin --version us --objdump mips-linux-gnu-objdump --list
```

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,161 / 5,512 | 75.49% | 0 | 1,351 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,488 / 4,839 | 72.08% | 0 | 1,351 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

The converted inventory remains 5,512/6,046. The 80% threshold is 4,410
exact functions, requiring 249 more. The README changes only aggregate
matching rows; function detail stays here and in concise handoff entries.

## Fingerprints and preserved scope

| Artifact | SHA-256 |
| --- | --- |
| Natural compact target | `5f3efc4de35019ffbc1a7b23445006b36aae9193a89365dcd64d45194e5f2117` |
| Linked retail target | `f29ce9ba3bd3c791599d4e88882e95126d8e1ab1f60f58656a05e7740ed99cfe` |
| Frozen predecessor ELF | `4dfa62fd6f26d30aa472519a5bf2422e45faa0b9f1ac7cd88018ef2638ab0c96` |
| Qualified regular owner | `d0df1ce306bbcb52e6440b84e53d8d9fa8cda3aa89da07b27dc3f95607d5d92d` |
| Qualified ELF | `1d56f2554e0bc910fcec5498bfc78a5fd72c7711832be629b2037987fef5a9f9` |
| Production code binary | `02c8b1904a95f490ae09d70121d06316504b79380b15475e1ad5ce00b269b4d1` |
| Production guard CSV, working bytes | `1bb99ac99a4ee64a166ac72314f7af2b3d44d88cbfe954522f88242233415466` |
| Real table-address data window, 2,560 bytes | `45d7975e11bf3080b2a3f0aa67c692a2f97e7a901e28983780c1b1a8a9f0d498` |
| Protected Game data | `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670` |

Frozen source, owner, ELF, original routine/callers, complete retail input,
shared headers, retail layout, guard prefix, Makefile, conversion CSV, linker
and graph are retained under ignored
`conker/build/game-turn-animation-select-15056A00-match/`, together with the
copied-owner artifacts and JSON receipts. Protected data stays 189,088 bytes
across 720 owners without differences. Shared headers and original assembly
are not edited.

The main baseline is `9bde50096321de7639f86e7314a9c337920cad59`; mounted tools
baseline is `337d228fbae2525e74f4b98a054aab00af4cf005`. Both began clean.
The separate sibling tools checkout at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`
keeps its six pre-existing tracked changes and 2,428 untracked files;
fresh target checks use only the mounted tools checkout. No synchronization
or second-checkout qualification is claimed.

## Continuation and graph retention

The actual production rerank selects
`func_1509C8FC`, 69 words and 65 real differences. Keep the seven documented
boundary cases separate: `func_150A76F0`, `func_151F8870`, `func_150A613C`,
`func_150AE280`, `func_15115F68`, `func_151AE2BC` and `func_150A6760`.

Standard Graphify update refused a reduced 24,848-node extraction instead of
discarding the existing graph. The scoped changed-path refresh retains
58,638 nodes, replaces three relocated update-log headings by matching
label/source, and adds nine headings from this note. No node outside the
eight changed paths is removed. The resulting graph has 58,650 nodes,
112,408 links and 5,103 communities, SHA-256
`41e81ea555dbbbf12671771dd8107f852c72f224a2e78ecc4f4d921c88f4286c`.
This is scoped structural maintenance with old-node retention, not a new
full-corpus semantic extraction. The ignored `graph-retention.json` records
the exact before/after comparison.

Mounted tools are committed first as
`8dbfa7fe55759b1eecf4d1c2c0a09eac5a7b19ae`
(`test(game): qualify turn animation selector`). The consumer includes that
submodule pointer together with the source, ten checked guards and docs.
