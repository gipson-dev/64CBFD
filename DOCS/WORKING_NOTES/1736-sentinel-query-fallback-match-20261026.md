# 1736 - Sentinel Query Fallback Match - 2026-10-26

The adopted Native ELF measures **3,813/5,506 exact C functions (69.25%)**,
Game **3,140/4,833 (64.97%)**, zero address drift and 1,693 different.
Only `func_1503B708` gains credit. Inventory and converted-byte totals stay
fixed; 317 more matches reach the current 4,130-function 75% threshold.

## Complete C and observed interface

`func_1503B708`, owner `generated_64120`, occupies VA
`0x1503B708`..`0x1503B7C0`, ROM `0x68BB8`..`0x68C70`. It has a 45-word body,
one ordinary zero alignment word, a 64-byte frame, and saved S0/RA.
Retain the retail symbol and describe the observed sentinel/query behavior.
The zero-return placeholder becomes a complete void function with eleven
arguments: output pointer, two 32-bit words, player index, single float,
another word, a float pointer, and four final words. Shared headers stay fixed.

Load `D_800986EC` once, then initialize output[0..2] and `D_800C3FD0`[0..2]
in that order. The production constant is `0xC7C34F80` (-99999.0f).
Call `func_15037880`(playerIndex, output). Only a zero result calls
`func_150380C0` with all eleven arguments. Preserve reloading the argument homes
after the primary query, including the single-float and distance-pointer slots.
Nonzero results skip those stack reads and the distance access entirely.

The sole aligned direct JAL is ROM `0x64A94`, VA `0x150375E4`, in parent
`func_15036F34`. No aligned literal-address registration is found in the full
2,467,288-byte reference image. The caller immediately reads the output vector
and overwrites V0 before using it. This establishes the output-only interface;
the old stub's s32 spelling and Graphify return-type edge are not ABI evidence.
Graphify locates the original source/owner at `generated_64120`.c:L104.
The complete larger parent, query providers and gameplay remain uncredited.

## Typed calls and closed guarded fit

Provider definitions remain unchanged placeholders. Giving them typed formal
parameters causes IDO g3 to emit additional argument-home stores, including
when parameters are marked register. Scoped redeclarations are rejected by
CFE. Those experiments stay private. Typed function-pointer call views keep
the recovered single-float/pointer ABI without changing either provider body.

The complete C emits 49 words/frame 64 with eight bindings, raw SHA
310a95d9d824641bddb8a92a30f5a584f11dda7f1751039a931ac801de92906a.
Twenty-six expected-word/relocation rows derive the retail 45-word body:
fold two fixed HI16/LO16 function-address pairs into direct JAL bindings,
omit their four address-construction instructions, recompute the one branch
that spans the removed pair, and translate three complete argument-temporary
lifetimes. Restore the common sentinel load, argument homes, six stores,
late player-home read and primary-call delay-slot setup. No words are inserted.
The resulting six bindings and complete body match original assembly.
This is guarded semantic C; one zero alignment word remains ordinary padding.

All eighteen neighboring bodies, their bindings and pools stay fixed. Both
provider bodies remain byte-identical and receive no matching credit. Actual
Make uses its ordinary O2/g3/mips2/o32 compiler/padder/assembler path; all
nineteen compact functions agree, and the complete padded object equals
independent qualification. Every earlier guard byte remains an exact prefix.
The existing allocator Warning 712 is compared exactly between baseline,
candidate and actual Make, normalizing only file/line locations. No new warning
is accepted. The inherited `generated_12D630` duplicate-recipe warning persists.

## Qualification and actual caller

Both canonical tools copies pass six fresh checks and their shared tools
checks. Installed copies each run two fresh input/image checks and reuse four
unchanged semantic checks only under the sealed module/input/artifact identity.

- 5,120 guest cases cover eight word/float classes, four primary return classes,
  eight provider patterns, ten output aliases, and two stack phases. Compare
  raw public memory/calls with an independent reference; compare complete
  fitted/original states. Output aliases include scratch, the sentinel and
  incoming argument homes. All 45 body words execute. Six lazy-read cases
  remove unused stack arguments and distance memory on nonzero returns.
- SDK/native32 O0/O2/O3 each execute 12,288 cases with trap UBSan, all eleven
  forwarded argument slots, full logical-array canaries and three valid output
  aliases. Eight compiled gate, initialization, argument and float controls
  fail as intended. Signaling-NaN bit transport and stack-home effects are
  guest checks; native tests use valid finite float transport.
- Execute the actual 38-word caller window `0x15037594`..`0x1503762C` in 192 cases.
  The first instruction loads the mask; the JAL delay slot stores zero-based
  argument 5 (the sixth argument). Verify all eleven incoming slots, saved S0/S1/SP, the output read, and
  V0 overwrite. This is a bounded caller window, not full-parent execution.
- 744 fired access prefixes compare complete fitted/original states. Additional
  misaligned/unmapped outputs and saved-register aliases preserve emitted
  failure behavior. Raw fault states and portable C fault semantics are not
  claimed. Provider effects are bounded contracts, not provider emulation.
- Nine GNU links exercise original/raw/fitted code across three HI/LO and J26
  carry layouts. All 49 raw-word and eight binding corruptions reject changed
  inputs; all 52 stale expected-word/relocation controls fire in the actual padder.
  Seven full-image corruptions, including the alignment word, are effective.

Private failures were fixture/declaration boundaries, not installed changes.
GDB identified native MOVAPS at ESP modulo 16 = 4; force-align the freestanding
native entry before calls. Map the caller's player byte and include its real
mask load rather than assuming an incoming T8 value. Preserve failed receipts
and immutable raw executions. Five unchanged private checks were retained by
AST/core/artifact identity while confirming the corrected caller separately;
the final canonical executions run all six methods freshly in each copy.

## Production and committed continuation

Production Make exits zero in 5.730s and reproduces independent
ELF 121a867bbdd91f4266d6976aa7596d9337eb61e52bc2b913f50db3fb79f315ea. The complete delta is **135 bytes: 134 target-code bytes and one
symbol-size byte, zero exclusions**. Target extent changes from 12 to 180 bytes;
no symbol/string serialization allowance is needed. Preserve all 6,056 addresses,
6,055 other bodies and exact Game data: 720 owners / 189,088 bytes, SHA
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Source SHA: f78b43f907fef348a75a95cb48943eb93a0e053d73338ab096297001fa70e079.
Padded object SHA: 70744e37a652f45b72fed8bc3500ab37013480202da14927e581f7428a0047de.
Baseline consumer be3214b5, tools 6b2f3e80, ELF 59d3bd42.
Tools efb8378fab3ff0a8a1d056c62dd100a455d6d50f are committed first; the consumer pins that commit.
The seal covers 16,111 Native inputs and exactly five qualified adoption outputs.
Preserve all 1,682 pre-existing dirty paths and the older tools mirror's history;
only the new pair is added there. No push or host-port work is performed.

The scoped native no-cluster graph refresh updates eight changed C/Markdown
sources and must retain or uniquely relocate all 44,311 previous nodes.
Preserve historical manifest freshness outside that scope and historical
community labels. No global clustering/centrality recomputation or full-corpus
extraction is claimed. Tools AST extraction remains separate from the parent.

The actual Native ELF queue contains 1,564 placeholders, 120 semantic/other
entries and nine unlocated screens. Next screened placeholder is `func_1509F284`
(`generated_CBDB0`), uncredited until source/ABI, guest/native, owner/Make and
production qualification closes. The unresolved pointer/NULL factory remains
a placeholder. Keep the 75% goal active. Routine Claude calls: zero.

Prepared-checkout focused command:

```sh
python3 -m unittest tools.tests.test_game_sentinel_query_fallback_match -v
```
