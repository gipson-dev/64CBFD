# 1817 - Payload owner command - 2026-10-29

`func_151D4C38` is recovered in `conker/src/game/generated_200930.c` as
`void (struct260 *owner, s32 eventAddress, u8 command)`. Its original name
is retained and its comment describes the recovered behavior.

## Behavior and interface

The link is owner+0x28. Command 60 releases the owner if either the link word
matches the event word or the identity byte at +4 matches. Command 4 uses the
same short-circuit comparison and clears bit zero at owner+0x38. Other commands
call `func_15149514(eventAddress, command, link, link+4, owner)`; its pair helper
handles release command 0 and reference/identity replacement command 45.
Ignored commands still pass through the wrapper. The original dispatcher
`func_15149434` selects slot 53 of the 74-entry `D_8008A8D8` table and ignores
the result. This establishes the void return and three-argument callback ABI.

## Compiler and normalization

The compiler emits 50 words / 200 bytes with the retail 40-byte frame and saved
S0/S1/RA lifetimes. Six expected-word guards restore the original 51-word /
204-byte sequence: four branch targets cross a restored epilogue word, and two
rows move the flag store before its branch and insert the original RA reload
into the branch delay slot. The two call bindings are retained; the second
moves from raw offset 172 to normalized offset 176. No words are omitted.
This is a guarded C match. The raw C is not a direct 51-word match.
Twenty-four natural flow/type variants were screened before selecting this form.

## Validation

Both tools copies pass eight fresh qualification checks and two fresh installed
checks, with six semantic checks reused only under exact artifact fingerprints.
Canonical v2 includes a byte-wise native reference correction; archived v1
receipts are historical. The production C and compiled artifacts are unchanged
by that test correction.

- 6,890 guest cases, seven alias layouts, all command/identity/flag byte values,
  incoming command high bits and 50 reachable words of the normalized routine.
- Raw C agrees on public memory/calls. Full original versus normalized guest
  state, access order, 88 fault prefixes and nine branch-delay cuts agree.
  No equivalence claim is made for raw C private stack/fault prefixes.
- Original 23-word caller: 200 cases; original wrapper/pair chain: 53 literal
  words with 52 reachable words, 200 connected cases. The release service is
  bounded at its canonical interface; its complete heap chain is not executed.
- Native 32-bit C: 655,360 cases per O0/O2/O3 profile with trapping UBSan and
  ten effective negative controls. Three GNU layouts provide 18 rebased cases.
- Six real guards fire; twelve stale-word/relocation mutations are rejected by
  the production padder. Six complete-image corruptions are rejected.
- Actual five-command Make build has no diagnostics; 27 compact neighbors and
  19 GLOBAL_ASM routines remain unchanged. All 6,056 function addresses and
  6,055 other bodies remain fixed. The entire ELF differs by 150 predicted
  bytes: 149 code bytes and one extent byte, zero exclusions or other metadata.

The inherited guard CSV prefix is byte-identical; exactly six rows are appended.
16,617 sealed inputs and 629 focused inputs are audited. The independently dirty
older tools mirror retains its 1,892 inherited paths plus three new test/tool
modules. Tools commit `24ea520` precedes the consumer commit.

ELF SHA-256: `00063b783ef3f0a050c6ca8e44015e9951ca90cfdf396580f62994f0caac6d64`.
Object SHA-256: `9e83cb12fe813b66ec8cea78ad5c817003162c7e27a8c64a84f4c88108dadb81`.

## Progress and continuation

Actual ELF recount: **3,895/5,506 (70.74%)** total; **3,222/4,833 (66.67%)**
Game; Init 492/492 and Debugger 181/181 remain exact. Zero address drift;
**235** more exact C functions reach 75%. Next screen `func_15080430` against
the current queue and original callers. `func_1514E920` and `func_151D7000`
remain parked and uncredited. No gameplay acceptance is inferred.

The local Graphify refresh is scoped to changed C, tools and Markdown, retains
old nodes and still-valid relationships, and retires the obsolete placeholder
s32 return relationship. Historical global communities/centrality are retained;
this is not full-corpus extraction or new global analytics.

Reproducible preparation, canonical, production, recount and final audit artifacts
are retained locally in `conker/build/game-payload-owner-command-match/`.
