# Linked-event callback matched with a closed branch-edge split

Date: 2026-11-06. Continues [Note 2140](2140-game-record-position-query-match-20261106.md)
from consumer `ecc728162229df96a8e1499289c6c6b5ef8738da` and tools
`86d5cce0c6c0d4f5eb0313b76fea6a18958c3422`, toward the active 80% goal.

## Recovered interface and behavior

`func_15133588`, `conker/src/game/generated_15F680.c`, now matches all
**72 words / 288 bytes after five derived guard rows with one inserted word**.
Raw semantic C emits 71 words. VA `0x15133588..0x151336A8`, ROM
`0x160A38..0x160B58`, frame `0x30`, no alignment tail. The default
O2/g3/MIPS2/O32 profile, all 30 compact/padded neighbors, loaded pools and
register metadata remain fixed. Three bindings retain the helper and callback
table symbols; both table bindings move four bytes after the edge split.

All owner/payload/stack and guard offsets below are hexadecimal.

The recovered interface is `void (u8 *owner, u8 *pair, u8 event)`. Event 0x1B
with owner halfword66 equal to0x22 calls `func_151B9660(owner)`. Its original
11-word body writes three float fields at188/18C/190. Owner/pair/event survive
that call. A promoted selector snapshot, real key/current locals and the index
recover the original 48-byte frame and SP+18 saved-selector home, without fake
padding, unused locals, frame guards or an ABI/profile change.

Event0x2D compares pair word0 with owner word7C. A match replaces word7C with
pair word4 and byte80 with pair byte9. Otherwise, matching pair word4 replaces
word7C with the captured first word and byte80 with pair byte8. Event0 clears
word7C/byte80 when pair word0 or the byte at pair+4 matches. That byte is the
big-endian byte at offset4, not the second key's low byte or the pair's byte8.

The final flags60 load remains after all writes. Bit0x100 selects owner byte68
as the callback index; otherwise index0 is used. Reload the live
`D_800899F8[index]`; invoke only a nonnull pointer with owner/pair/byte event.
The helper and callback may mutate their visible fields/table. No result is
consumed. The table has ten original entries: nonnull1,5,6,8; other entries0.
Guest fixtures beyond those ten entries qualify the byte index expression
against an explicit bounded callback model, not retail reachability or the
validity of arbitrary executable addresses.

The **outer** descriptor table is separate: base `D_8008B4A8`, stride52,
event callback offset1C, **class entries25 and72**, giving pointers at
8008B9D8/8008C364 (ROM230498/230E24). An earlier private calculation from the
biased D_8008B4D0 base gave entries24/71 at offset0x28; those are equivalent
addresses, not the actual dispatcher's class indexes. Three original JALR
windows in func_15169070, func_15169260 and func_1516944C establish the
owner/payload/unsigned-byte interface and void result. No direct JAL or tail
entry exists in the ROM census. Complete list-dispatch parents and inner
callback reconstruction are outside this function's acceptance boundary.

## Guard derivation and access-order proof

The complete raw71-word SHA and all three bindings are pinned. The normalizer
uses only emitted instructions and local branch destinations, never retail
words as derivation inputs. Raw offsets98/9C contain an unconditional branch
to D0 followed by the tag store in its delay slot. D0 is the shared flags load.
The derived form is the same tag store, then the branch, with a **copy of the
existing flags load** in its delay slot. That branch skips the shared copy.
Other incoming edges retain the original shared load. Every path still executes
one flags load after the same stores, including overlapping owner/pair/table
fixtures. No extra memory access or padding is introduced.

Rows58/7C repair crossing branch displacements; row88 exchanges only the two
commutative BNEL comparison operands and its relocated displacement; rows98/9C
perform the edge split and insertion. All other local branches and symbol
bindings are remapped from old to new PCs. Exactly five rows append to the
inherited CSV byte prefix; no omissions or relocation replacements occur.
Both HI16/LO16 table bindings move by four bytes through the actual padder.

Raw and normalized C agree on visible state and memory-access prefixes. The
raw PCs/delay markers differ at27 of62 injected access cuts; **literal raw
fault-PC parity is not claimed**. Normalized and retail states, including
fault PCs/delay markers, are identical. These are guest instruction tests,
not portable C fault semantics, MMIO timing or hardware acceptance.

## Qualification and production

Eight methods pass before/after installation in both tools configurations.
The dirty sibling uses a disposable overlay for new modules with its own
existing compiler/parser/oracle helpers; its 2,434 status paths are preserved.
All111 core/header snapshots remain checked.

- 8,128 semantic guest cases per body: all256 event/index bytes, upper argument
  bits, flag/type gates, both key directions, byte tags, null callbacks and
  live post-helper state. Retail, raw and normalized C agree. Unreachable
  duplicate-load word33 is retained and is not counted as executed coverage.
- 1,152 alias cases per body cover owner/pair, key/tag/flags and callback-table
  overlaps. 62 fired access cuts compare normalized literal state and raw
  memory/call/observation prefixes; the closed store-then-load order remains.
- 288 connected helper cases per body execute the original11 instructions,
  including all three stores and both live constant loads. The original ten
  inner table words are checked independently.
- 90 caller cases per body execute all three original JALR windows for classes
  25/72, including stride52 arithmetic and unsigned-byte argument narrowing.
- Six independent GNU links across three layouts and72 cases per body check
  all three bindings, signed-low16 carries, JAL regions and shifted table sites.
- SDK native32 with UBSan at O0/O2/O3 runs4,240 cases per profile. Pointer/word/
  halfword/byte widths are asserted. All nine controls fire: event, type, first
  update, second tag, clear tag, flags, missing helper, wrong callback event,
  and the former stub. Repeated second-key bytes remove host-endian ambiguity;
  big-endian alias/fault proof remains guest-only.
- 284 raw-byte corruptions, three binding corruptions, five actual-padder
  stale-word controls and six ELF corruptions fail closed. Both copies pass
  fresh tools smoke checks; three unchanged shared regression receipts are
  reused only after exact helper/test fingerprints match.

Only generated_15F680.c recompiles once under the existing profile. Its two
pre-existing Warning712 diagnostics remain normalized-identical; no new
warnings/errors appear. They concern the unrelated legacy func_100043B4
arguments and are not hidden by broadening that API. The duplicate
12D630 recipe warning and unfinished-ROM checksum failure remain expected.

Actual Make equals the **complete211-byte ELF prediction**, with zero excluded
ranges. In addition to the recovered body and symbol size12 to288, adding the
callback-table reference swaps two existing absolute symbols, D_800899F8 and
D_8008A3F8, in one GNU symbol/string bucket. Six metadata bytes are predicted
from frozen BEFORE records/strings. All named definitions and file geometry
are preserved. Every other function body, all6,052 addresses, progress.csv,
Makefile and189,088 protected Game bytes across720 owners remain fixed.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,210 / 5,512 (76.38%) | 0 | 1,302 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,537 / 4,839 (73.09%) | 0 | 1,302 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**200 more** matches reach the current4,410 threshold for80%.

- ELF: `9dca25bb40d84489fcddaf9a2c74f425b835610143b3059fd1d23526eb85b8b2`.
- Owner: `14c6571c9f9c4e998bbdc3a0596b5a20668d210d6dc6b4b2d00e52328d8b8c35`.
- Binary: `963ddca159d9433d70127acad79f435b1ba3e1c92ce597a3d530f0572cb99b84`.
- Guard CSV: `9892912f5423eb5e518da147fb0bf7e358de56260cb3d59e6b2e6d1bcff0c4ab`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Reproduction: `python3 -m unittest tools.tests.test_game_linked_event_callback_match -v`.
Actual Make uses `-o retail_word_patches.us.csv -o Makefile`, followed by the
production ELF/progress, expected unfinished-image `all`, and
`match-progress NON_MATCHING=1` targets. Receipts, rejected source screens and
strict predictors are retained in
`conker/build/game-linked-event-callback-15133588-match/`.

Tools commit precedes consumer/source/guards/docs/pin. Root README gets only
aggregate rows. Graphify refresh retains old nodes outside the changed paths;
this scoped fail-closed update is not a full-corpus extraction. Claude calls:0.
No live gameplay/hardware acceptance was performed.

Next: **func_15146A98**, generated_173D40,72 words/frame0x68,
VA15146A98..15146BB8, ROM173F48..174068. Recover the owner+1D4 gate,
func_15146890 position query and the real stack effect descriptor passed to
func_15150F90. Its caller interface is not yet qualified; keep it uncredited.
Preserve handwritten func_150A6FA0/func_150A76F0, unrelated work, private
inputs/saves and frozen host Release. Keep the full80% matching goal active.
