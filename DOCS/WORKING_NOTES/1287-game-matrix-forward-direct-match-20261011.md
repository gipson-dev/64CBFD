# Game Matrix Forward Direct Match

Date: 2026-10-11. Recover complete func_1503F404 in
conker/src/game/generated_6B320.c, replacing its zero-return placeholder.
VA 0x1503F404..0x1503F4B0, ROM 0x6C8B4..0x6C960: 43 slot words / 172 bytes.
All 40 executing words emit directly from semantic C under existing
O2/g3/frame 0x70. Preserve three original zero tail words. Function size
is 160 bytes, distinct from its 172-byte slot. No added guards, instruction
drops/insertions, shared headers, callers, profiles or recipes. Add only
required local u8 selector and typed memcpy declarations. Matching +1 only;
converted counts/bytes unchanged. Full Game goal remains active.

## Baseline And Contract

Consumer 365b2dc69063ec8f696011d7dd0cfe7a36ce9e8c and mounted tools
a96b414446006f75e696249a510fa8098513e862 were clean at entry.
[Note 1286](1286-game-record-mask-active-direct-match-20261011.md)
left this genuine 43-slot-word / 38-difference target. Read workflow, query
Graphify, inspect full retail wrapper, sole original caller func_151D4408,
existing SDK conversion/copy and owner profile. Reuse IDO, structured
ELF/object/pool parsers, MIPS/native32, GLOBAL_ASM and both actual padders.
Codex is the single writer; zero Claude calls, no bridge/install/account changes.

Recover void func_1503F404(void *input, f32 *x, f32 *y, f32 *z,
f32 *rx, f32 *ry, f32 *rz, f32 *sx, f32 *sy, f32 *sz).
Input represents either a fixed Mtx or a 64-byte float matrix. Read the
unsigned byte D_800C3E90 once; every nonzero value chooses guMtxL2F,
zero chooses memcpy(matrix,input,64). Forward the prepared local matrix
and all nine output pointers to the existing func_1503E5F8. No synthetic
NULL/range gate or meaningful return result.

Retail first homes A0..A3 in the caller's incoming area, saves only RA,
and puts the local 64-byte matrix at SP+0x30 in its 0x70 frame. The source
pointer is loaded before preparation; all nine output pointers are loaded
after preparation from their original O32 homes, including six stack
arguments. A first helper that changes a home changes that later pointer.
Changing home zero does not retarget the already-submitted source.
Changing the selector during preparation does not reselect the branch.
Preserve register/FPR clobber tolerance, load schedule and delay-slot stores.

The complete original caller constructs these nine destinations in its
own 0xD0 frame, consumes the matrix-derived values and exports a packet.
It ignores V0. It is not the group-one active callback: original active
table remains EEC0, EEC0, F2B0. Matrix decomposition, random and export
leaves remain bounded models here, not newly recovered math/gameplay.

## Fresh Qualification

Straightforward named-argument C matches all 40 words on the first profile
screen. Compact no-unroll is identical; O1/g3 emits 40 words with nine
differences, O1 emits 39 with 38. Keep the existing O2/g3 profile; no
object-profile boundary or variadic source is needed.
Ten pre-install tests pass in 18.926 seconds; ten installed tests pass in
19.262 seconds. Final two literal-integrity/corruption-control gates pass
again in 2.415 seconds. Receipts: conker/build/game-matrix-forward-match-test/.

- 800 retail/raw/padded cases cover all 256 selector bytes, eight fixed/
  float/NaN/infinity/raw-bit patterns, three output alias layouts and both
  stack phases. Execute all 40 wrapper words, all 45 executable SDK
  conversion words and all 11 memcpy words. Original conversion's zero
  tail word is preserved and never runs. Linked SDK bodies are compared
  with their full ROM spans before connecting them; their hooks are removed.
- Fifty lifetime/alias cases include all nine effective late-home pointer
  mutations, cached source home, selector change and live matrix input
  mutations. Two actual byte-copy cases use an unaligned source. Missing
  required final source bytes fail both branches. Home/private aliases
  and unaligned guest fixtures do not claim portable C or hardware faults.
- Two independent links rebase four symbols with HI16/LO16 carries in
  36 cases. All 458 fired fault triplets preserve complete memory/events/
  GPR/FPR state, including actual SDK and bounded projection accesses.
  No portable C fault, hardware or FCSR claim.
- Six compiled semantic controls fail effectively: reversed gate, one-only
  gate, short copy, swapped first output pointers, wrong last pointer and
  passing the original input instead of the local prepared matrix.
- Both complete owners are diagnostic-free, pass GLOBAL_ASM and both real
  padders. All 21 neighbors, extents, relocations and normalized pools are
  identical. Compare unlinked code and relocation records independently;
  all three original tail words remain zero, no metadata projection.
- Literal source/full-ELF/eight-input gates reject stale/duplicate source,
  source corruption, four ELF corruptions (including original tail), and
  guard corruption without production mutation or baseline refresh.
- Eighteen cases execute all 152 words of the sole original caller, with
  the wrapper and SDK copy/conversion actual. Check its complete ten-arg
  call, six-arg export interface, low-byte argument and final packet.
  A fresh rotation-pointer control changes the exported packet effectively.
  Decomposer projection, random and export leaves remain bounded;
  agreeing packets are not complete gameplay or FCSR acceptance.
- Native32 O2/O0 each pass 12,288 cases using the recovered SDK conversion C:
  all selector bytes, eight patterns, three output aliases and two selector
  mutation modes. Check all ten arguments, complete matrix payload, full
  source/output canaries and call counts. Five native controls fail with
  mismatch receipts. GCC32/fno-strict-aliasing qualification is not a
  private-home alias, hardware/FCSR or actual decomposer proof.

Initial fixture issues were fixed before installation: the missing local
selector declaration, an unlinked-object versus linked-address comparison,
unused native helper and misleading native indentation under -Werror.
No production workaround or frozen-baseline refresh was used.

~~~sh
python3 -m tools.experiments.game_matrix_forward_candidates --profiles
python3 -m unittest tools.tests.test_game_matrix_forward_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
~~~

## Linked Audit

Source-only rebuild compiles one owner and relinks, exiting zero with the
known duplicate generated_12D630 recipe warning. Target owner is
diagnostic-free. Literal whole-ELF comparison changes exactly 119 bytes:
118 target bytes and one size byte (12 -> 160). The original 12-byte tail
and every other body/address/extent/metadata/string/section/header/pool/data
byte remain unchanged. Eight other inputs are identical: guards, progress
CSV, rodata assembly, symbol definitions, undefined functions, retail
layout, Makefile and SDK matrix conversion source.

Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | aa141c65ad29d29a1ff7d7b52e96d8115df088fa27b52244e610d1bfb34d69f8 |
| Source after | 48adc4b96517a4d4efe101817e092d6b343dbfa5aa462d2d639ddd85c17960c5 |
| ELF before | 407aad745988d43056465c75d3cf2ac866787e70ab431e8d316d82fdc2a5f1cc |
| ELF after | 4b4bece866646b9f453b958c1dccdd2f37e31f65dc2abaaa810b71f72a5d4071 |
| Guards unchanged | 92f39fbf0bf509614ecff961e3a654e01d30c98666c3c65f224884f57102206e |

Fresh progress: Game 2,808/4,822 (58.23%), total 3,481/5,495 (63.35%),
Init 492/492 and Debugger 181/181. Zero drift / 2,014 still different.
Matching +1 only; README gets aggregate rows, no function narrative.

## Checkpoint And Next Body

Consumer, mounted and older standalone shared checks and native py_compile
pass. Bank mounted tools dbc0f0d first, then source, this note, five current
indexes, aggregate README and exact gitlink. No push. Preserve older sibling
HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 65 prior hashes;
copy only two absent files with identical hashes, dirty count 342 -> 344.
Final read-only snapshot records 67 hashes, including both identical copies.
Do not commit/reset independent older history. Target tests run mounted
in the consumer, not the standalone mirror. Prior unchanged neighbor suites
are reused from Notes 1286/1285/1284/1283/1282/1281/1280/1279/1278 on
unchanged literal evidence, not called fresh runs.

Native graphify update . exits one on protective shrink refusal: 18,221
candidate nodes versus 40,001 saved. Preserve 19,398 nodes from 2,972
excluded but still existing files; no force/purge/install. Version and
empty-source warnings remain separate from compiler diagnostics.
Require a fresh post-consumer-commit terminal Rebuilt receipt, advanced log
bytes/UTC and zero workers; launching the hook is not completion.

Fresh scope scan compares all 22 generated_6B320 rows with their complete
ROM slots: zero differences for all 21 converted C functions (including
their existing guards), and zero differences for the one remaining ASM.
No zero-return placeholders remain in this owner. Existing guard removal
is still open; do not call the entire slice direct C.

Next: recover full 141-word / 564-byte matrix decomposer func_1503E5F8
from GLOBAL_ASM, VA 0x1503E5F8..0x1503E82C, ROM 0x6BAA8..0x6BCDC.
Its assembly is already linked-exact, but it is not C-converted. Inspect
its complete bcopy/normalization/determinant/angle/scaling contract and
caller aliases before recovery; replace the bounded projection model
with actual helper qualification as appropriate. A graph query did not
resolve this assembly helper; use the original routine and live owner
rows as authoritative evidence. Do not add another broad conversion batch.

Independent SDK/hardware/FCSR/renderer/gameplay acceptance remains open.
No OGL Release build/change, private input/save or active editor/debugger
mutation. Keep the full Game matching goal active.
