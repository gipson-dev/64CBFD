# Game Integer Pair Clamp Register Lifetime Audit

Date: 2026-10-06. Starting checkpoint: `fe925393`.

Continuation: [Note 1034](1034-game-pair-clamp-saved-register-backend-audit-20261006.md)
banks nine accepted backend controls; the saved-pointer frame remains open.

Continue `func_15143D18` after banking its ordered XOR access recovery in
[Note 1032](1032-game-integer-pair-clamp-xor-access-recovery-20261006.md).
**No direct match or production change in this follow-up.** Its 36-word slot
still contains 29 emitted words, no frame, seven zero padding words and 36
aligned differences. Retail saves S0/S1 in frame 0x10 and restores them with
the upper branch-likely/shared return tail.

## Bounded Controls

[Existing driver](../../tools/experiments/game_integer_pair_clamp_candidates.py)
adds optional `--register-lifetimes`, preserving the default 92-control mode.
Sixteen subsets of parameter register hints cross four local groups:
none, pointers only, values only, both. Each of the 64 source forms compiles
under O2/g3 and O1/g3: **128 controls**, empty compiler diagnostics.
No explicit physical-register binding, assembly insertion, extra operation,
profile installation or artificial frame forcing.

| Local Hints | O2/g3 Words / Frame / Differences | O1/g3 Words / Frame / Differences |
| --- | --- | --- |
| None | 29 / 0 / 36 | 50 / 0x20 / 50 |
| Pointers | 29 / 0 / 36 | 47 / 0x20 / 47 |
| Values | 29 / 0 / 36 | 46 / 0x20 / 46 |
| Both | 29 / 0 / 36 | 40 / 0x20 / 40 |

All 64 O2/g3 bodies are word-for-word identical to the committed recovery.
Within each O1/g3 local group, all 16 parameter masks also emit identical
words. Every O1/g3 form is oversized and still misses the retail frame;
none is eligible for installation. No hypothesis that these parameter hints
alone recover the allocation is retained as a next step.

Receipts: ignored `conker/build/game-integer-pair-clamp-register-lifetimes/`.
The prior 36-word O1 full-register-hints control also changes the block
temporaries; it is not one of these 64 forms and remains frame 0x20 with
35 differences. Do not confuse body length with byte identity.

## Qualification And Audit

[Register-lifetime test](../../tools/tests/test_game_integer_pair_clamp_recovery.py)
compiles all 128 controls and checks the complete byte groups, sizes, frames,
differences and empty diagnostics. Six corner inputs across two stack phases
for every control give **1536 guest runs**, verifying independent full
external-memory footprints, ordered reads/writes, no helper calls and saved
register/SP/RA preservation. Includes reversed bounds/pointers, signed extrema,
equal pointers and intervals outside the clamp. The isolated added test
passes in **12.381 seconds**, no skips. The suite now contains eight pair
recovery tests; the complete combined rerun passes **all 51 tests in 93.572
seconds**, no skips. This includes the indexed state-save, timer, packet,
linked-record tail/position, random-range and position/sound regression suites.

The existing 24576-case guest/12288-case native qualification remains for the
unchanged selected production C. The new corners are bounded compiler-shape
checks, not additional full caller-domain, MMIO, concurrent memory, unaligned
access, hardware or gameplay acceptance.

Compare the current ELF snapshot against the banked `fe925393` receipt:
all **6059 slots**, protected sections and **10646 guards** remain identical;
all **720 Game data owners / 189088 bytes** stay retail-exact. `git diff
fe925393 -- conker` is empty. No source, header, profile, metadata or data edit.

Counts remain total **3313/5462 exact (60.66%)**, Game **2640/4789 (55.13%)**,
zero drift, 2149 different. README aggregate rows therefore need no edit;
detailed progress stays in these documents. No sibling source/build/save or
frozen Release change, no push. The Game matching goal remains active.
Root `make tools-check` and `git diff --check` pass. Documentation check:
3137 relative links across 16 documents, zero broken.

## Resume Point

Continue the saved-pointer allocation/frame and upper return-tail problem
with a different evidenced source/backend shape. Do not repeat the separate
parameter/local register-hint matrix: it leaves O2/g3 unchanged and O1/g3
oversized. Keep `func_15143D18` explicitly non-matching until its complete
36-word slot is proven exact. Adjacent scalar-clamp production stays unchanged.
