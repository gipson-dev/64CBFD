# Game release-first owner-event callback guarded match (2026-11-05)

## Outcome and acceptance boundary

`func_15191A84` replaces a false zero-return placeholder with a typed, void
owner-event callback. The natural C body has all 66 words, frame40, the
original S0/RA homes and the three original call locations. Thirty-nine
expected-word replacements fit its address calculations, register allocation
and instruction scheduling to retail. This is guarded exact C, not a natural
compiler word match or an assembly-body replacement. No instructions are
inserted or omitted, and no compiler profile or frame correction is applied.

Production matches the independently qualified image. The live recount is
4,159/5,512 total (75.45%) and 3,486/4,839 Game (72.04%), with zero address
drift. Private experiment sizes or passing semantic tests alone receive no credit.

## Retail behavior and ABI

| Item | Evidence |
| --- | --- |
| Function and owner | `func_15191A84`, `generated_1BA1D0` |
| Source / original assembly | `conker/src/game/generated_1BA1D0.c`, `conker/asm/1BA1D0.s` |
| Virtual interval | `0x15191A84..0x15191B8C` |
| ROM interval | `0x1BEF34..0x1BF03C` |
| Length / frame | 264 bytes / 40 bytes |
| Saved registers | S0 at frame+32, RA at frame+36 |
| Argument homes | event at incoming SP+4, command word at incoming SP+8 |
| Command byte | low eight bits; big-endian home byte at incoming SP+11 |
| Helper bindings | release at +0x60 and +0x7C; forwarding at +0xEC |
| Registration | `D_8008A8D8[8]`, VA `0x8008A8F8`, ROM `0x22F3B8` |
| Dispatcher | original complete `func_15149434`, 23 words, ROM `0x1768E4` |
| Direct JAL census | none; exactly one aligned pointer literal |

The managed record has flags at +0x0D, signed timer at +0x0E, owner pointer
at +0x28 and owner ID at +0x2C. Its event has an owner pointer at +0 and an
owner ID at +4. Either pointer equality **or** byte-ID equality qualifies an
owner match; requiring both would reject valid events.

Commands 0x0C, 0x0E and 0x50 release matching records through
`func_1516972C`. Command 0x4E releases unconditionally. Command 0x0D updates
only matching records: snapshot flags, store timer100, then set flag bit0.
Other commands forward the event, command byte, addresses of the two owner
fields, and the record to `func_15169850`.

The real dispatcher loads a signed selector from record+0x13, clamps values
outside 0..73 to slot0, skips a NULL entry, narrows the command to one byte
and invokes the three-argument callback. The recovered callback has a void
return. No source or ABI repair is needed in the already recovered caller.

## Source and fitting provenance

The body is independently recovered from the complete retail routine, its
74-entry registry, the original dispatcher and the adjacent owner-event
callback's established helpers. The neighboring `func_15191980` uses a
different record layout and tests the timer command first; its source and
45 existing guards are preserved.

The selected source uses an explicit flags snapshot inside a C89 declaration
block. This is live semantic data: the flag load precedes the timer write,
and the saved flag byte supplies the final bit-set store. The event parameter
and final command-byte access retain their argument-home reads. Candidate
screens without this flags local emitted65 words; an explicit owner-payload
pointer emitted67, or68 with the flags local. K&R, nested-field, reordered
comparison and early pointer captures did not produce a natural match. These
private screens remain ignored and uncredited.

All 39 replacements check exact compiler preimages. The complete raw body
and all three relocation tuples are fingerprinted before fitting. No guard
touches a helper call relocation. The fitting covers address materialization
as well as register/schedule changes; it is **not** claimed to be a pure
instruction bijection or a universal equality of natural and retail private
register states. Original/fitted instruction states are checked literally.

## Focused qualification

Permanent commands, from the consumer root under WSL PSBBN:

```sh
python3 -m tools.experiments.game_owner_event_release_first_candidates
python3 -m unittest tools.tests.test_game_owner_event_release_first_match -v
python3 -m unittest tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -v
make tools-check
```

The eight focused checks cover:

- 4,096 cases **per body**, executing original, natural C and fitted output:
  all 256 command bytes, four identity modes, two stack phases, varied upper
  command bits, signed timer contents, flags and retained storage patterns.
  Sixty-five retail words are dynamically reached; the redundant scheduling
  word at `0x15191B10` remains statically exact and is not claimed as reached.
- 1,008 alias cases per body, placing events at every aligned offset from
  record-16 through record+64, across release/timer/forwarding commands,
  identity modes and both stack phases. Every public backing byte is checked.
- Actual native32 O0/O2/O3, each 4,096 cases, for 12,288 positive executions,
  with trap UBSan and twelve compiled semantic wrong-C controls. Layout
  assertions establish pointer width and the recovered owner/timer/flags
  offsets. The little-endian native fixture encodes the command in the byte
  selected by the unmodified big-endian-home source expression.
- 432 connected phases per body through the complete original23-word
  dispatcher and the actual 74-entry registry: signed negative/out-of-range
  selectors, NULL slot0, selected slot8, representative other providers,
  command narrowing and both stack phases. Other callbacks/helpers are bounded
  contracts; this is not their complete gameplay or hardware acceptance.
- 286 fired root-memory fault prefixes compare complete original/fitted
  private registers, stack/RAM, events, calls and instruction visits. Natural
  C fault PCs and access order are deliberately not equated with retail.
- Nine independent GNU links of original, natural and fitted objects across
  three independent entry/helper-address layouts with J26 helper rebinding;
  72 rebased semantic cases per body and literal original/fitted word identity.
- Four actual IDO wrong-C controls have guest counterexamples: conjunction
  instead of alternative identity, wrong timer, wrong flag and wrong release
  record. All 264 single-byte body corruptions, three relocation changes,
  three actual padder guard-preimage changes and three inside/outside whole-ELF
  corruptions are rejected.
- The complete owner keeps 60 neighbors, normalized pools, addresses and all
  three bindings. Only the target changes among 6,052 linked functions. The
  independent literal ELF prediction changes 191 bytes, including the target
  symbol-size update from 12 to 264, with zero excluded bytes or sections.

The fresh pre-install eight-test suite passes in 45.873 seconds. A discarded
earlier run failed only because the wrong-release negative control passed an
incompatible pointer under native Werror; its corrected explicit void-pointer
conversion compiles and is rejected by behavior. No production defect was
inferred from that fixture error. Shared 19 regressions pass in 9.025 seconds;
`make tools-check` also passes.

## Production closure and recount

`make -C conker -j4 build/conker.us.elf progress.csv` completes successfully.
Because the guard CSV is a common prerequisite, this is a full production
rebuild, not a substituted private object. The production owner and complete
ELF equal the independently compiled/padded/linked qualified artifacts byte
for byte. The fresh installed eight-test suite passes in 77.399 seconds.

The original guard file survives as an exact byte prefix with precisely 39
appended rows. The frozen Makefile, conversion CSV and generated linker are
unchanged. The expected whole-image delta is 191 bytes, with no excluded
metadata, sections, dependent objects or function bodies. All 6,052 functions
keep their addresses; only this target's bytes and symbol size change.

`make -C conker all` produces the binary and then returns 2 at the existing
overall retail SHA check, as expected for the incomplete decompilation. The
duplicate `generated_12D630` recipe warning and existing SDK/owner warnings
are inherited. No new target declaration warning is introduced.

The fresh command is:

```sh
cd conker
python3 ../tools/match_progress.py progress.csv build/conker.us.elf conker.us.bin --version us --objdump mips-linux-gnu-objdump --list
```

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,159 / 5,512 | 75.45% | 0 | 1,353 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,486 / 4,839 | 72.04% | 0 | 1,353 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

The converted inventory remains 5,512/6,046. The 80% target is 4,410 exact
functions at this denominator, requiring 251 more. The root README updates
only its aggregate matching rows; this function's narrative stays here.

## Fingerprints and preserved scope

| Artifact | SHA-256 |
| --- | --- |
| Natural compact target | `99cdbf8e3c83c22f158ccd9a46f01f6c5413c5497a364809a35d05fd84b247bf` |
| Linked retail target | `07179b29dafa7c76cef0c171e9446f2638dabd4d423aad0c696fe6bd03cb1395` |
| Frozen predecessor ELF | `b06f9a049b7b71c57625b6bc887eb75be0105090cb401be32323fda84cae9c2b` |
| Qualified owner | `3ef0ee30cee035ced4490ba4e41516812f6be4db9029437245de62efa76f712e` |
| Qualified ELF | `557cd1685bfb53e29ce35d423d84c2ad62820bd56c4506c99c64910d3d3024b5` |
| Production code binary | `a32076e84039469ccfe37e3d274f31c9fce048a600e130d93b12756191cd3aa5` |
| Production guard CSV, working bytes | `d0f84bd1788847bace98029ed9c723dba63d4b77f971fd5e25c053d52914c6ee` |
| Production link map, unchanged | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Protected Game data | `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670` |

Frozen source, guard bytes, Makefile, progress CSV, owner, linker and graph,
the copied owner/image results and JSON receipts are retained under ignored
`conker/build/game-owner-event-release-first-15191A84-match/`. Protected data
stays 189,088 bytes across 720 owners with zero differences.

The main baseline is `ebef2c09e3873cab64a437ca908832d37a20a697`; mounted
tools baseline is `2ae13b33248dec5952a105d172406c260b023adf`. Both began clean.
The separate `64CBFD Tools` checkout at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`
has six pre-existing tracked changes and 2,428 untracked files. It is preserved, not overwritten
or used to claim a second fresh tools qualification. All fresh checks here
run against the consumer's mounted tools checkout. The qualified tools are
banked as `04191f14cfe10203fe1f723ddf9f724a502ea28b` before the consumer pin.

## Continuation and graph retention

Next ordinary target: `func_151A25E0`, 67 words and 64 real differences in the
predecessor ranking. Keep the seven documented boundary cases separate:
`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC` and `func_150A6760`.

The standard AST update refused a reduced 24,830-node extraction instead of
overwriting the frozen 58,622-node graph. Its existing corpus warning retains
31,816 nodes from 3,754 source files omitted by the current scanner. No force,
purge, package upgrade or full-corpus extraction is claimed. The existing
skill/package version warning (0.9.20/0.9.26) and zero-node `devcontainer.json`
warning remain recorded limitations.

An explicit AST refresh of the eight changed consumer paths produces
58,632 nodes, 112,394 links and 5,121 communities. Of the old IDs, 58,619
remain verbatim. Three Update Log heading IDs relocate when the new entry
is prepended; all three have replacement nodes. Thirteen IDs are added:
nine from this note, those three relocated headings and one shared reference.
**Zero nodes outside the changed paths are removed.** The retention receipt
is `graph-retention.json` under the ignored build directory. This is a scoped
AST refresh with no semantic LLM calls, not a full-corpus re-extraction.
HTML is skipped because this graph exceeds the 5,000-node visualization limit.

Qualified graph SHA-256:
`e1cd0ea7a2e67d74222fe1826e8d4298ee3eb7cda640485e945256cd61eeb28f`.
