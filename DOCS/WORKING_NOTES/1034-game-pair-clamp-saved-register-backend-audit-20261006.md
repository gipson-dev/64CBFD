# Game Pair Clamp Saved Register Backend Audit

Date: 2026-10-06. Starting checkpoint: `8ef236d6`.

Continuation: [Note 1035](1035-game-descriptor-shape-measure-direct-match-20261006.md)
qualifies and installs the adjacent 56-word direct recovery. This backend
audit was banked separately in `6474c718`; pair-clamp production stays unchanged.

**`func_15143D18` remains non-matching; no production change.** Continue
[Note 1033](1033-game-integer-pair-clamp-register-lifetime-audit-20261006.md)
without repeating its parameter/local register-hint matrix.

## Local Backend Evidence

Decode the embedded big-endian IDO literal words from the local recompiled
`cc`, `uopt` and `ugen` ELF64 `.rodata` sections. The uopt option table contains
the following spellings; acceptance and output are then measured, not inferred
from option names. An ignored decoder receipt is under
`conker/build/game-integer-pair-clamp-test/compiler-options.py`.

The [driver](../../tools/experiments/game_integer_pair_clamp_candidates.py)
adds `--saved-registers`, nine controls against the unchanged recovered O2/g3
body: `do_opt_saved_regs`, `noprecolor`, `noheurAB`, `no_r23`, `nogenvreg`,
`norlodrstropt`, `nordstore`, `no_const_in_reg`, `docopy`. Each uses
`-Wo,-<option>` only in its disposable build. All are accepted with empty
compiler diagnostics. Receipts:
`conker/build/game-integer-pair-clamp-saved-registers/`.

Seven controls emit the unchanged 29-word body. `nordstore` changes exactly
three words: the XOR temporary's definition/store/use move from T0 to T1;
the test binds that closed register-field cycle. `noprecolor` emits 35 words
with caller argument-home stores/reloads, still no saved-pointer frame.
All nine have frame zero and **36 aligned retail differences**. None is exact;
no control installs a flag, source change, guard or arbitrary frame padding.

## Qualification And Scope

The added [backend test](../../tools/tests/test_game_integer_pair_clamp_recovery.py)
checks every accepted control's exact shape and **108 corner guest runs**:
six signed/extreme/equal-pointer/reversed-bound cases times two stack phases
times nine controls. Ordered external reads/writes, complete external byte
footprints and saved register/SP/RA preservation match the independent
reference. This excludes MMIO, concurrent/read-mutating memory, private-frame
input pointers, full callers, hardware execution and gameplay acceptance.

The initial added test caught an overly broad expectation that eight controls
were byte-identical to the selected body. The corrected check explicitly
binds `nordstore`'s three-word lifetime; the isolated corrected test passes
in **1.080 seconds**, no skips. All **nine pair tests pass in 35.646 seconds**,
no skips. No production correction was required by that test failure.

All **6059 linked slots**, protected sections and **10646 guard rows** equal
the preceding checkpoint receipt. All **720 Game data owners / 189088 bytes**
remain retail-exact. No `conker/` source, header, profile, metadata or data
change. README remains 3313/5462 total and Game 2640/4789 exact, zero drift,
2149 different. No sibling source/build/save/frozen Release change or push.

## Next Candidate

The pair-clamp saved-pointer frame and upper shared restore remain open.
Do not install an artificial whole-slot replacement to inflate its match count.
Continue Game recovery at adjacent `func_1514462C`, still a false zero-return
placeholder. A bounded isolated screen of its complete descriptor calculation
finds a 56-word direct O2/g3 body, but this is **not yet a linked installation
or gameplay claim** at this checkpoint. Qualify signed halfwords, low-two-bit
shape dispatch, wrapped box multiplication and the ordered float operations
before source/header edits. The Game matching goal remains active.
