# View resource renderer matched directly through recovered SDK macros

Date: 2026-11-07. Continues [Note 2157](2157-game-resource-view-creator-match-20261107.md)
from consumer `a0d368972695420593fb95d2883835b10bedbd36` and tools
`a3b28488e7263ad5385baf6b7a7539642ee3046b`. One qualified Game function
advances the active80% total goal.

## Recovered callback and three-command draw

`func_1513B83C` in `conker/src/game_168A90.c` now emits all **75 words /
300 bytes directly from semantic C**, VA0x1513B83C..0x1513B968,
ROM0x168CEC..0x168E18. The ordinary O2/g3 MIPS2/O32 profile reproduces
the32-byte frame, saved S0/RA, signed16 view home SP+0x2A and cursor
home SP+0x20. No new word guards or compiler-profile overrides are used.

The interface is `Gfx *func_1513B83C(Gfx *displayList,u8 *resource,s16 view)`.
If resource byte+0x10 has bit0x02, require the corresponding view bit in
byte+0x49. Read signed callback index+0x12. Index-1 skips the callback;
otherwise call `D_80089C28[index](resource,view)` with the sign-extended
16-bit view. A zero result returns the incoming display-list cursor.
The local callback declaration records this exact two-argument call ABI.

On success, recovered SDK macros submit:

1. `gSPMatrix`, command0xDA380003, pointing to resource+0x78+(page<<6),
   with modelview/load/no-push flags.
2. `gSPSegment` for segment1, command0xDB060004, loading the word at
   resource+0x58+(reloaded page<<4)+view*4.
3. `gSPDisplayList`, command0xDE000000, using the live resource+0x54 word.

Return the cursor advanced by24 bytes. Preserve each command's first-word
store before subsequent live reads, both separate page-byte loads, callback
mutations and the final resource+0x54 reload. Aliasing through command
storage may change the page or resource field before it is read.

Raw target SHA-256:
`a186ae6d8427b7f23bf8288edc5a2058a219905745eb37fd328b47e12c17b710`.
All four relocations match: indexed callback HI16/LO16 and page HI16/LO16.
All12 raw and padded neighboring functions remain literal, including the
previously matched creator and fixed factory. Four inherited pointer
diagnostics remain identical; none are added. Guards and Makefile are unchanged.

The first source explicitly masked the shift count with31. That added an
ANDI and changed temporary allocation, producing76 words. Retail's unsigned
`1U << view` gives the original75 words, including bit31's defined result.
Portable native shift tests use view indices0..31 and sufficient record
backing. The dispatcher transports a signed16 view, and normal rendering
uses the existing per-view mapping. Out-of-range/negative guest shift and
array indices qualify emitted MIPS instructions only; they do not establish
portable C behavior or broaden the native contract.

Body word20 is a literal unreachable LB after an unconditional branch and
its delay slot. Both incoming likely branches target word21. It emits
directly and remains byte-exact; **74 reachable words** execute in tests,
not a claimed75-word execution total.

## Real indirect caller and callbacks

The complete aligned retained-input census finds no direct target JAL and
exactly two entry pointers, at ROM0x230AD0 and0x231080, VA0x8008C010 and
0x8008C5C0. There are no interior pointers. These are the+8 draw slots in
the52-byte registry records for kinds0x38 and0x54:
`0x8008B4A8 + kind*52 + 8`. They are the same kinds selected by the creator
restored in Note2157. The protected registry owner remains unchanged.

The original348-word dispatcher `func_151674F8` supplies cursor/resource
in A0/A1 and a sign-extended16-bit view in A2. Two connected original
windows at0x151677D8 and0x15167894 execute all10 and9 words, including
the authentic next-resource link store in each JALR delay slot. Together,
**96 cases per body** cover both registry kinds, signed-view truncation,
callback/sentinel paths and zero/nonzero callback returns. The rest of the
large dispatcher is frozen and inspected for context; these bounded windows
do not claim its full restoration or full gameplay validation.

**18 cases per body** connect the complete original16-word callback
`func_1513B968` and5-word zero-return callback `func_1513BAD4`. Every one
of those21 helper words executes, and both helpers already match in production.
The first submits the live resource matrix address to `func_150A7B80` and
returns1; the latter returns0. The matrix service remains a bounded provider.
The other five real callback table addresses are tested as two-argument
provider boundaries, without claiming their complete bodies are recovered.

## Independent qualification and exact linked metadata

Seven checks pass pre/post installation in both tools configurations:

* **1151 guest cases per body** compare retail/direct C against an
  independent byte/store model, ordered calls and return value. Cover all
  flag/mask bytes, signed callback indices, signed16 view transport, all
  three graphics commands, callback mutations, two private-home redirects,
  command/global/resource aliases and sparse wrapped addresses. Complete
  private memory, GPR/FPR/HI/LO, PC and access traces agree between emitted
  retail and C. Sparse index/address and private-frame probes are guest-only.
* **124 fired access cuts**, including 14 delay-slot cuts, compare full
  machine/access-prefix states, including original callback execution.
  This qualifies emitted guest instruction order, not portable C fault,
  hardware, graphics output or gameplay acceptance.
* Native32 SDK O0/O2/O3 each pass **116 independently hashed fixtures**,
  with Gfx8/Mtx64/pointer32 assertions, disjoint fixed arenas, valid unsigned
  shifts and UBSan traps. Nine compiled negatives fail with exit1: old stub,
  wrong flag, wrong mask, wrong callback, wrong callback argument/gate,
  wrong matrix stride, wrong buffer index and wrong returned cursor.
* Actual plain-owner `pad_c_object` reproduces every target word and all12
  neighbors without new guards. Decoded target GPR usage constrains raw
  register metadata; no new FPR usage occurs. Both padded owners retain
  literal zero register masks, fixed ABI flags and unchanged other pools.
* Two independent GNU links verify indexed LO16 callback lookup and both
  signed HI16/LO16 carry pairs. Ten altered raw words, a changed binding,
  two register-metadata corruptions and six full-image corruptions reject.

The first linked prediction exposed30 extra serialized metadata bytes.
The audit found exactly two adjacent symbol/string pair swaps:
`D_800DDC08`/`D_80087438` and `D_80089C28`/`D_800D2E45`.
The predictor pins their predecessor slots, exact name blocks and permutation,
then preserves all original value/type/section fields under each name. The
complete named-definition multiset remains identical except this function's
extent12->300. This is closed serialization accounting, not a metadata
exclusion. All other ELF bytes must match the independent prediction.

The initial caller fixture lacked ownership of the boundary instruction at
the authentic return address. The oracle rejected it as an unowned jump.
The fixture now includes that retained next instruction and stops before
executing it. No production code or unowned-jump guard was weakened.

The147 frozen inputs include all owner assembly, complete dispatcher and
render-pass source/assembly, both protected tables, current source/object/ELF,
ROM, compiler/SDK, registries/layout, guard history and graph. Imported
helpers/new modules are separately fingerprinted. The sibling uses a disposable
new-module overlay and its explicitly hashed read-only `alloc_pools` fallback.
All2,434 inherited dirty sibling paths remain unchanged. Shared smoke checks
pass freshly in both copies; three unchanged shared regression receipts per
copy are reused after exact helper/test hashes. Claude calls: zero.

## Production checkpoint and continuation

Actual Make recompiles only this owner and equals the independent full-image
prediction: **259 changed bytes, zero exclusions**. These comprise227 Game
body bytes,14 symbol-table bytes and18 string-table bytes, including the
target extent and two closed swaps. All6,052 function addresses and every
other body remain fixed. All189,088 protected Game bytes across720 owners
stay exact. Guard manifest, conversion CSV and Makefile are unchanged.
Compile/link succeed; the full ROM checksum remains the expected nonmatching
exit2, with the inherited duplicate generated_12D630 recipe warning.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,228 / 5,512 | 76.71% | 0 | 1284 |
| Game | 3,555 / 4,839 | 73.47% | 0 | 1284 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**182 more exact functions** remain to4,410/80%. Root README receives only
aggregate rows; four index leads retain the historical bodies. Scoped
Graphify refresh preserves old nodes outside changed paths and existing
excluded legacy files fail-closed. Commit tools before the consumer pin/source/
docs, then verify the fresh commit hook, clean trees and unchanged production.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `d6b18982fb0d18255216f90349ef497fc8c257e0ddc6e3e6b2dc4f9c6b613e1c` |
| Production binary | `663c878b9fee4f91dd681ade1418e45bd3996061674b564211af22b392dfefc8` |
| Padded owner | `2f02d7f65d93fa4e4a6682ef4a9efa6d67f46f702b3a0fb5348f9b7711a459b9` |
| Guard manifest (unchanged) | `5f6f9d9b935ceac0f3819711842f4d278bbaa5911c32214771aade923d984f87` |

Ignored receipts remain under `conker/build/game-view-resource-draw-1513B83C-match/`;
private source screens remain in its sibling `...-private/` directory.

Next: **func_1513BBFC**, the adjacent173-word callback, VA0x1513BBFC..
0x1513BEB0, ROM0x1690AC..0x169360. Recover its actual callback ABI and
semantic body before qualification. Keep the full80% goal active. The
separate `func_150A25D4` stays private and uncredited; preserve all frozen
handwritten/hidden-ABI boundaries, unrelated work, private inputs/saves and
the frozen host Release checkpoint.
