# Game Entity Height Wrapper: Direct C Match

Date: 2026-10-03. Baseline: `46e7bdc`.

## Recovery

`func_15045780` replaces its retained assembly ownership with semantic C in
`conker/src/game/generated_71820.c`. All 32 words / 128 bytes match retail
directly, with no new word guards or compiler-profile changes.

- VMA: `0x15045780..0x15045800`.
- ROM: `0x72C30..0x72CB0`.
- SHA-256: `455aefd9652fcdc030893b9d05c944e3f4bc157e10b3db55c6c5f45291b6dcb1`.

If `position[1] < threshold`, clear only result flag bit `2` and return zero
without calling either helper. Otherwise allocate two local count words:
secondary at index zero, primary at index one. Call `func_15045714` with
primary/secondary output pointers, then forward the same buffer to
`func_15045F8C` and return its raw signed result. The selector is a halfword.
The buffer and calls preserve the retail 0x20-byte frame, spill schedule,
and branch-likely behavior directly from C.

Equality and unordered float comparisons do not reject early. Helper-side
position/result mutations remain visible downstream without a second gate.
The original assembly reference is retained unchanged for comparison.

## Verification

Five tests in `tools/tests/test_game_entity_height_wrapper.py` compile the
actual production definition and result layout in the existing 32-bit host
harness, mocking only the two callees. They check all 256 initial flags,
surrounding result-byte preservation, both count pointers and values, equality,
raw integer returns, helper mutations, NaNs, all 65,536 selectors, and a
bit-preserved negative-zero threshold.

All 218 repository tool tests pass with no skips; `make tools-check` passes.
The full `NON_MATCHING=1 all match-progress` code build passes. Independent
linked byte extraction confirms the complete wrapper slot against the ROM.
The next symbol remains at `0x15045800`.

Regression checks confirm these spans remain exact:

| Span | Bytes |
| --- | ---: |
| `func_15045714` | 108 |
| `func_150A6500` | 56 |
| Both context-3 height queries | 456 each |
| Producer and shared return closure | 520 |
| Collector/context group | 5,712 |
| Complete `.init` | 164,048 |
| Complete `.init_data` | 17,376 |

`func_15045F8C` remains unchanged at 72 word differences, with SHA-256
`b574cdd78a8c4921af83d6ca6393ee65f0bf0a3757df0ad2d4565cfadab8ff49`.
No guest execution or natural gameplay acceptance is claimed.

## Progress / Next

Fresh classified inventory: 5,455 / 6,042 C rows (90.28%),
1,928,344 / 2,256,728 C bytes (85.45%). Game is 4,782 / 5,321 C rows
(89.87%), 1,756,908 / 2,072,880 bytes (84.76%). The CSV contains repeated
header rows; count only `c`/`asm` records, not those headers.

Linked matcher: total 3,258 / 5,455 exact (59.73%); Game 2,585 / 4,782
(54.06%); zero drift and 2,197 different Game rows. Init stays 492 / 492
exact and Debugger 181 / 181 exact.

Next ordinary Game target is retained wrapper `func_15045800`: its first
callee is `func_15047004`, and only its zero-result path calls this wrapper.
Audit that callee's status/return contract before recovery. It is not merely
an opposite-threshold version of this routine. Reopen Init only under the
gates in [Note 768](768-init-remaining-assembly-current-decision-20261003.md).
The sibling host port and frozen Release artifacts remain untouched.

Follow-up: [Note 769](769-game-cached-height-query-and-dispatch-direct-match-20261003.md)
completes the then-pending dispatch wrapper and cached-query callee, both
directly matching from semantic C. Gameplay qualification remains separate.
