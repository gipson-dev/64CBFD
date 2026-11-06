# Table payload spawn direct match and private copy layout

Date: 2026-11-06. Continue the 80% goal from consumer
`1129343a6ba0ab55b2603c093b1798a8f1ea5a60` and mounted tools
`ee15c0e578ea5c99aac8282b5b3b468f9b8bfe78`.
This completes the next target in
[Note 2120](2120-game-dual-extent-approach-direct-match-and-byte-setter-abi-20261106.md).

## Installed result

`func_1515A974`, owner `generated_185560`, now emits all **68 retail words**
directly from semantic C: VA `0x1515A974..0x1515AA84`, ROM
`0x187E24..0x187F34`, frame `0x88`, saved RA at SP+`0x1C`.
All four bindings match, with **no new guards or compiler profile changes**.
The callback is `void(u8 * volatile owner, s32 unused)`, consistent with its
actual dispatcher; the second argument is retained in its incoming home.

Only owner byte `0x1F == 0` enters the constructor. The unsigned selector
retains retail's indexed 52-byte table-entry calculation and signed comparison
after integer promotion. Every other byte skips all table data and helper work.
The request at SP+`0x60` has kind 15, the live owner pointer, two table floats,
five zero floats, enabled 0, mode -1 and flags 2. It is 40 bytes, including
four retained padding bytes at offsets 1, 2, 3 and 39. The callback does not
initialize those bytes. Descriptive local types preserve pointer width and
layout without changing the SDK's older integer-owner `struct183` definition.

The separate 44-byte payload at SP+`0x2C` consists of an opaque four-byte
header with alignment 1 and a 40-byte aligned value structure. Both come from
table bytes 8..51. The first assignment produces the original LWL/LWR and
SWL/SWR pairs; the second produces the three-iteration 12-byte loop and final
word. The source performs byte-preserving aggregate copies, with no arithmetic
or integer-to-float conversion of the retained table values.

It calls `func_151A8B20(&request, -1, 44, 255, 0)` using the recovered
`(request *, s16, s32, u8, s32)` interface. The fifth argument occupies SP+`0x10`.
On successful allocation it copies the complete local payload to result+`0x80`.
The original registration is `D_8008F984[6]`, the sole aligned literal pointer
at ROM `0x23445C`. The complete original dispatcher `func_151A9060` ignores the
callback's result and returns 1.

## Recovery of the original frame and schedule

The first ordinary 44-byte structure assignment emitted 64 words/frame `0x80`.
A byte-array replacement emitted 69 words and used unaligned loads throughout.
Splitting the header from the aligned values recovered the exact 68-word copy
inventory. A named table pointer recovered frame `0x88`; placing the payload
after the pointer locals recovered SP+`0x2C` instead of the rejected SP+`0x34`.
Keeping the kind and live-owner assignments before selecting the table entry
recovered every remaining register role and load/store schedule directly.
No rejected frame, body, register mapping or schedule is normalized into a match.

All screens remain in the ignored target directory. The adjacent reference
source was inspected for context; final types and code were recovered and
validated against the retail assembly. Codex is the single writer. Claude
calls attempted/completed: **0/0**. Local source/compiler evidence settled the fit.

## Fresh qualification

Run from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_table_payload_spawn_match -v
```

All **eight installed checks** pass in both tools configurations. An ignored
overlay exercises the dirty standalone sibling's actual compiler fixture,
object parser, timing/FP engine and native32 command builder. Helper paths and
hashes, the five overlaid modules and mounted fallbacks are recorded. The
sibling's six tracked edits and 2,428 untracked files are preserved.

- **8,192 cases per guest body**, original/raw/padded, check an independent
  byte reference, all 256 unsigned gate values, all 68 words, both allocation
  results, provider effects, incoming homes and saved-register ABI. All table
  bit patterns, including signed zero and NaNs, are copied verbatim.
- **1,112 aliases per body** cover 129 table/frame offsets, both stack phases,
  live request/payload/incoming homes and forward-copy output overlap. The
  independent reference follows the original word-by-word table copy after
  request stores. **190 own-access fault prefixes** preserve literal state.
  Guest-only writes to the private payload do not claim portable C semantics.
- The complete **24-word original parent** runs 192 cases per body, covers
  every word, rejects invalid signed indices/null entries, dispatches slot 6
  and overwrites two poisoned callback return values with 1.
- The complete **115-word original factory** is connected for 16 cases per
  body, covering 98 factory words across success and failure. The actual
  **11-word memcpy** executes all its words, including the factory's complete
  40-byte request copy with retained padding. The nine-argument allocator ABI
  is checked: lifetime -1 selects 300 and allocator flag 0. The allocator and
  three geometry providers remain bounded models; this is not gameplay proof.
- **Nine GNU links** and 96 rebased cases per body verify the table HI16/LO16
  pair across carry boundaries and both helper R26 bindings.
- **147,456 native32 positive calls** run 24,576 rows per path/profile through
  direct and compatible callback calls at O0/O2/O3, with SDK headers and UBSan.
  Layouts are request40/payload44/table52, with header alignment1 and values
  alignment4. Defined request bytes, complete payloads, owner/table output
  aliases and provider mutations are checked; native padding values stay
  unspecified. Nine effective controls reject signed gating, wrong fields,
  factory arguments, destination and copy length.
- Fail-closed gates reject 272 raw-byte corruptions, four altered bindings,
  six complete-image corruptions and the former zero-return placeholder.

The first alias fixture omitted rebinding its data relocation, and the first
factory assertion expected allocator flag 1. Both fixture assumptions were
corrected against the original instructions and rerun successfully; the C
reconstruction did not change. Both tools smoke checks are fresh. Prior shared
progress, word-guard and PC16 regression receipts are reused only after checking
unchanged helper hashes; those broad suites are not claimed as freshly run.

## Production closure

All **36 raw and padded neighboring functions**, compact allocated pools and
register metadata, padded pools and guard CSV bytes remain unchanged. The
**99 frozen inputs** preserve source, headers, build inputs, original caller,
registry and table evidence. Existing Warning 712 diagnostics and the duplicate
Make recipe warning are unchanged apart from shifted source lines.

The entire ELF equals the independently predicted image with **249 changed
bytes** and **zero exclusions**. The prediction accounts for the target slot,
its symbol size from 12 to 272 and one closed GNU hash-chain permutation of
`func_15075BB8` and `D_8009E4D4`, including both complete name blocks and records.
All 6,052 function addresses remain fixed; this is the only changed body.
All **189,088 protected data bytes in 720 owners** match.

Actual `make -C conker -j4 build/conker.us.elf progress.csv` equals the exact
prediction. `make -C conker all` retains the expected checksum exit 2 while
the wider decomp image differs from retail. The fresh recount is:

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,190 / 5,512 (76.02%) | 0 | 1,322 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,517 / 4,839 (72.68%) | 0 | 1,322 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversion rows are unchanged. **220 more** matches reach the current 4,410
threshold for 80%. Production fingerprints:

- ELF: `82fccdfd53396b9c26b55c704324e3d79d87596f95e7c7e5e651878f214f6987`.
- Owner: `9d4e49d6effbb1a3e68bcf1cfec7bf2daa37c7aa0bcd8b640f06ce2ef6665355`.
- Code binary: `7a786179c2733cd9ec8e44327e3b3db369e80b720e1f3b91141eeddbdd6da994`.
- Unchanged guards: `b53721d727660eca66ed2771ba8fd8597642b08a123168033628a26ff92fd46b`.

Ignored evidence lives under `conker/build/game-table-payload-spawn-1515A974-match/`.
Graphify receives a scoped refresh with old-node retention accounting, without
claiming full-corpus re-extraction. Its existing package/skill warning remains.
Tools are committed before the consumer pin, source, aggregate README rows and
concise indexes. No push, dependency upgrade or host-port acceptance is included.

Next: `func_1518894C` in `generated_1B5CC0`, a 67-word keyed-list registration
routine with an existing-node update and two-allocation rollback path. Qualify
its signed timer comparison, low-byte mode, list insertion and complete caller
interface. Keep handwritten `func_150A76F0` separate, preserve earlier documented
boundaries and keep the 80% goal active.
