# Game Integer Pair Clamp XOR Access Recovery

Date: 2026-10-06. Starting checkpoint: `2fd52b05`.

**`func_15143D18` has its retail ordered access sequence recovered, but is
still non-matching.** Slot 0x15143D18..0x15143DA8, ROM 0x1711C8..0x171258,
36 words / 144 bytes. Only its body in
[game_16EE20.c](../../conker/src/game_16EE20.c) changes. Existing O2/g3 profile;
no guards, profile override, public signature/header, metadata or data change.

## Recovered Contract

1. Sort the two signed bounds using the retail XOR exchange.
2. Read the second pointed value, then the first. If second < first,
   exchange through three XOR stores with the intervening pointed reads.
3. Clamp the cached lower endpoint only against the lower bound.
4. Read the upper endpoint again and clamp it only against the upper bound.

The old conventional temporary swap produces the same final outputs on the
qualified stable-memory corpus, but not the retail read/write sequence.
Intermediate XOR stores are retained explicitly; no snapshot of both values
is substituted for the sequential reads.

The function does not clamp both endpoints against both bounds or sort them
again afterward. An interval wholly outside the bounds may leave lower >
upper. Equal pointers skip the exchange under stable memory and perform the
two clamps sequentially. No arithmetic overflow is introduced by the XORs.
The public return type remains void; incidental caller-saved V0 is not a
return contract. There are no helper calls.

## Compiler Evidence

[Driver](../../tools/experiments/game_integer_pair_clamp_candidates.py):
23 forms under O2/g3, O2, O1/g3 and O1, **92 controls**, empty isolated compiler
diagnostics. Pointer/value declaration and capture order, register hints,
volatile pointer/pointee variants, explicit XOR stores, lower reload and
shared temporaries were screened. None is directly exact.

| Body | Raw Words | Frame | Aligned Slot Differences |
| --- | --- | --- | --- |
| Previous temporary swap, O2/g3 | 24 | 0 | 36 |
| Selected XOR access recovery, O2/g3 | 29 | 0 | 36 |
| Retail | 36 | 0x10 | 0 |

The selected body fits its original slot with seven zero padding words.
The 24-word operation core corresponds to retail words 5..28 under explicit
live-register-field renaming; the test preserves opcodes, immediates and
branch/delay shape. This is analysis-only evidence, **not** a production
word normalizer or direct match. Retail saves S0/S1 in a 0x10 frame and uses
an upper branch-likely/shared restore tail; the selected raw body does not.

Full register hints under O1/g3 or O1 emit 36 words but frame 0x20 and 35
differences, not the retail frame or match. Selected O1 forms emit 50 words
and are oversized. No experimental profile or arbitrary frame padding is
installed. Receipts: ignored `conker/build/game-integer-pair-clamp/`.

## Qualification

[Seven tests](../../tools/tests/test_game_integer_pair_clamp_recovery.py)
use a local guest XOR implementation without changing shared runners.
Independent signed-bound and sequential byte-memory references compare:

- **24576 guest cases**, three bodies: retail, recovered C, previous C.
  Eight signed/extreme values per endpoint/bound, forward/reverse/equal
  pointers and two stack phases. Complete external memory footprints match.
  Recovered and retail ordered reads/writes match; the old body differs in
  **7168 access traces** despite equal final footprints. All 36 retail words
  execute; preserved registers/SP/RA are checked on normal return.
- **12288 native cases** exercise the actual selected C and compare all
  24 backing bytes, including sentinels, signed extrema and pointer equality.
- Structural source/slot/no-guards/signature checks, 23 existing-profile
  compiler forms, core correspondence and negative swap/clamp controls.

Five pre-install tests passed in 14.378 seconds and the subsequent core
correspondence test passed in 0.207 seconds, no skips. The first post-link
run stopped after five tests on an incorrect test assumption that a shared
header declaration existed. The corrected test binds the unchanged source
signature and existing absence of that declaration; no header was added.
The corrected combined suite passes **all 50 tests in 64.519 seconds**, no
skips: pair clamp, indexed state save, random-reload timer, packet wrapper,
linked-record tail/position, random-range position and position/sound adapter.
Root `make tools-check` passes. (`tools-check` is a root target, not a
`conker/` target.)

These cases qualify aligned mapped object words and stable ordinary memory.
They do not qualify unaligned access, MMIO, concurrent/read-mutating memory,
pointers into the private callee frame, full caller-domain expansion,
hardware execution or gameplay acceptance.

## Linked Audit And Status

The NON_MATCHING ELF/progress/match-progress build passes. Audit all **6059
linked slots** against the preceding checkpoint: only `func_15143D18` changes;
all addresses and slot sizes stay fixed. Init, Init data, Debugger and Game
data are byte-for-byte unchanged; all **720 Game data owners / 189088 bytes**
remain retail-exact. All **10646 existing guard rows** stay identical and
ordered; no guard is added for this target. Linked target SHA-256:
`62dee4f581e6fb94f436db80bae91cf187c98b2d57158c0d4d06bd89cdba83d6`.

The owner's three warning ID/message/source-expression triples are equal
to an independently compiled committed-source baseline: 709 at
`func_1516972C(arg0)`, 712 at `func_15141E38(arg0, arg2)`, and 709 at
`func_15144B34(arg0)`. Target isolated controls have no diagnostics.
The existing duplicate generated_12D630 Makefile recipe warning is unrelated.

README aggregates are already current and remain unchanged:

| Section | Exact Converted Functions | Drift | Different |
| --- | --- | --- | --- |
| Total | 3313 / 5462 (60.66%) | 0 | 2149 |
| Game | 2640 / 4789 (55.13%) | 0 | 2149 |
| Init | 492 / 492 (100%) | 0 | 0 |
| Debugger | 181 / 181 (100%) | 0 | 0 |

Detailed progress belongs here and in the working indexes, not the root
README. No sibling host source/build/save/frozen Release edits or push.
Documentation check: 3127 relative links across 15 documents, zero broken.
`git diff --check` passes; the existing source CRLF-to-LF notice is not a
compiler or matching failure.

## Next Work

Continue `func_15143D18`: recover the saved-pointer frame/lifetimes and upper
branch-likely/shared return tail. Keep the routine explicitly non-matching
until the complete linked slot is proven exact. The neighboring scalar clamp
`func_15143DA8` is unchanged and already exact through nine existing guards,
not a direct raw-C match; see
[Note 319](319-game-integer-range-clamp-match-20260927.md).
The Game matching goal remains active.
