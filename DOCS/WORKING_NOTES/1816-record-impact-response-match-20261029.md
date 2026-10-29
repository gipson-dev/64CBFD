# 1816 - Record impact response - 2026-10-29

`func_151AC550` now emits all 51 retail words / 204 bytes directly from
semantic C in `conker/src/game/generated_1D92F0.c`. Its original 72-byte
frame, two call bindings and six-argument callback interface are preserved.
No guards, padding instructions or custom compiler profile are used. The
original name remains, and the comment describes effect submission followed
by marking the captured payload as handled.

## Recovered behavior and interface

The callback interface is `s32 (u8 *, f32, f32, f32, f32, void *)`: actor,
previous XYZ, queried height and query-result pointer. The existing exact
`func_15148BA4` caller and its `D_8008A450` declaration establish these types.
The first three floats are unused; height and result arrive in the fifth
and sixth argument words at incoming SP+0x10/+0x14.

Capture payload from actor+0x98 and the 20-byte motion-record table from
actor+0x94. Construct a three-float position from the signed cursor at
actor+0x2D: record X, queried height, and record Z. Reload the signed cursor
for Z after the first stores, matching retail access order. The local typed
motion-record view preserves the captured table base without another load.

Call `func_151D8E20` to select an effect, then load the current scale and
alpha from the captured payload and group/context from the actor. Submit
`func_151DBCBC(selector, scale * 7.0f, alpha, result, position, group, context)`.
The result pointer is forwarded as its 32-bit word, following the existing
service declaration. Finally write byte 4 to captured payload+0x20 and return
1. An actor+0x98 redirect by either provider does not change that final target.

The position is at frame+0x34 / incoming SP-20; captured payload survives at
frame+0x44 / incoming SP-4. Guest probes deliberately mutate the result home,
position bytes and captured-payload slot. These qualify emitted instructions;
they are not claims about portable C writes into a caller's stack frame.

## Source fitting and native-order correction

The first byte-pointer source emitted 52 words with a redundant table-base
load. Twelve typed/byte views and declaration orders were tested; the typed
payload/table/position order matched all 51 words. A private native test then
rejected the nested selector call: C leaves the other service argument loads
unordered relative to that call, while retail performs them afterward.

The final source gives the selector its own statement and a local `u8`.
Three of nine natural sequencing/declaration variants match directly. The
selected variant retains the exact object and complete ELF while defining
the required C evaluation order. The original private source, artifacts and
failed receipts remain in `pre-sequenced-selector/`.

The overlapping-actor reference also needed the opaque provider's four
outgoing-home stores before later context reads. The assembly inventory
expectation was corrected to six GLOBAL_ASM routines. These fixture repairs
and the source sequencing fix were completed before installation; all eight
private-v2 methods and both fresh canonical runs then passed. A receipt label
was clarified to describe the measured effect descriptor rather than infer
an unsupported allocation type. Routine work used zero Claude calls.

## Original caller and retained helpers

The full ROM census finds no aligned direct JAL/J and one pointer at ROM
0x22EF18 / VA 0x8008A458: slot 2 of eight-entry `D_8008A450`. The original
143-word `func_15148BA4` parent remains byte-exact and unchanged. Its nineteen
words at 0x15148D30 dispatch the six arguments through the selected table
entry, skip selector zero, and consume the nonzero callback result. Tests
execute that window, not the full parent's motion/height-query behavior.

Both current helper bodies equal their original retail bytes: the 19-word
selector and 113-word effect service. Forty-eight connected cases cover all
132 words, selector state/query branches, null/non-null result tags, three
bounded random calls, both final constructor routes, the descriptor fields
and all fourteen constructor argument words. The effect service remains its
original assembly; this recovery gives it no C-conversion credit.

The graph separately records the assembly provider's literal definition,
GLOBAL_ASM ownership and source/binding-validated call. This fills its missing
function node using source evidence. It does not claim an AST extraction of
the assembly file. Query, randomness and final effect constructors remain
bounded providers. Full provider, FCSR, hardware and live gameplay acceptance
are outside this qualification.

## Qualification and production audit

Eight target methods plus shared project-tool checks passed freshly in each
tools copy. After installation, two owner/image checks ran fresh per copy;
six semantic checks were reused only with identical complete input, module,
compiler-adapter and qualified-artifact fingerprints.

| Evidence | Result |
| --- | --- |
| Retail/compiled guest comparison | 3,083 cases, all 51 words, complete state and access traces |
| Index and data coverage | All 256 signed cursors and byte arguments, raw copied XYZ/height words, two actor and three payload layouts |
| Provider effects | All 64 bounded mutation modes, captured pointers, late field reads, stack argument and local-slot redirects |
| Original caller window | 112 cases, nineteen words, six arguments, selector-zero skip and consumed success result |
| Retained original helpers | 48 connected cases, all 19 selector and 113 effect-service words |
| Native SDK / 32-bit execution | 262,144 cases each at O0/O2/O3 with trapping UBSan and actor/payload/alternate fences |
| Effective bad-body controls | Ten native variants and ten independently IDO-compiled variants rejected by values, calls, packet or return |
| Fault prefixes | 232 fired prefixes, including sixteen delay-slot cuts; complete state/access/PC/delay equality |
| GNU links and rebases | Three layouts, eighteen cases, both external call bindings preserved |
| Corruption controls | Three raw/binding mutations and six complete-image mutations rejected |
| Full owner / actual Make | 33 compact functions, 32 unchanged neighbors, six retained assembly routines, five commands, no owner diagnostics |

The production Make build reproduces the independent complete-image
prediction: 152 changed bytes, comprising 151 code bytes and one symbol-size
byte, with no other metadata changes or exclusions. All 6,056 addresses and
6,055 other bodies stay fixed, as do 189,088 protected Game bytes /720 owners.
Shared headers, guard CSV, conversion inventory and linker map are unchanged.

- Before: total 3,893/5,506 (70.70%); Game 3,220/4,833 (66.63%).
- After: total **3,894/5,506 (70.72%)**; Game **3,221/4,833 (66.65%)**.
- Init 492/492 and Debugger 181/181 remain exact; address drift is zero.
- The 75% threshold is 4,130 exact C functions: **236 more** are needed.

Tools were committed first as `d3c3f14b8e256200e9aeba2a104e80c247db430a`.
The consumer contains this note, source, tools pin and aggregate README rows.
Prior consumer/tools were `359e3fba` / `7d79ac6`. The older tools mirror retains
its 1,889 inherited dirty paths plus three new qualification modules.
No push or host-port/Release change is part of this recovery.

Evidence is retained in `conker/build/game-record-impact-response-match/`:
625 focused frozen inputs, 16,610 sealed active inputs, private and canonical
receipts, actual Make, complete-image prediction, production/recount and
scoped Graphify retention evidence. No full-corpus extraction or refreshed
global clustering/centrality is claimed.

Next inspect `func_151D4C38` in `generated_200930.c`, the next unparked
51-word placeholder in the refreshed queue. It has no matching credit yet.
`func_1514E920` and `func_151D7000` remain parked and uncredited.
