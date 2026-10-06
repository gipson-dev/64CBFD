# Game Indexed State Save Direct Match

Date: 2026-10-06. Starting checkpoint: `fd30ea2a`.

Continuation: [Note 1032](1032-game-integer-pair-clamp-xor-access-recovery-20261006.md)
recovers the next pair-clamp function's ordered accesses; its saved-pointer
frame and return tail remain non-matching. This state-save match is unchanged.

**Game func_15123934 matches all 38 words / 152 bytes directly from C.**
Slot: 0x15123934..0x151239CC, ROM 0x150DE4..0x150E7C, frame 0x18.
The zero-return stub and obsolete commented draft are replaced in
[game_14FF90.c](../../conker/src/game_14FF90.c). Existing O2/g3 profile;
no guards, profile override, header/metadata/data change or overflow.

## Indexing And Callback Contract

The fifth argument is a 32-bit index, not a whole-actor stride. The recovered
halfword pointer advances by index*2; saved word lanes advance by index*4.
The neighboring restore routine already uses these same two scales.
Existing `struct108` and public prototypes remain unchanged.

If the halfword at actor+0x20C+index*2 is nonzero, return zero without writing
or calling. Otherwise, perform the following **sequential** copies:

| Source Offset | Destination Offset | Width |
| --- | --- | --- |
| 0x000 | 0x002 + index*2 | 16 bits |
| 0x02C | 0x030 + index*4 | 32 bits |
| 0x084 | 0x088 + index*4 | 32 bits |
| 0x0DC | 0x0E0 + index*4 | 32 bits |
| 0x134 | 0x138 + index*4 | 32 bits |
| 0x1B4 | 0x1B6 + index*2 | 16 bits |
| 0x1E0 | 0x1E2 + index*2 | 16 bits |

Then install arguments 1/2/3 at actor+0x2C/+0xDC/+0x134, mark the indexed
halfword one, call `func_15125394(actor)`, and return one regardless of the
callback's V0. Marking occurs in the original call delay slot, before the
callback observes memory. Callback mutations are not overwritten afterward.

The old draft used incorrect whole-struct indexing and omitted the callback's
actor argument. Both mistakes are removed rather than retained as guidance.
No new clamp, slot validation, snapshot-before-copy or alternate return API.

Index 21 is a useful guest overlap counterexample: the saved ID overwrites
part of the current mask, and successive word destinations overlap later
source fields. The reference therefore reads each source after earlier
writes, not from a pre-captured record. These diagnostic indexes do not
establish valid gameplay slots or a portable out-of-bounds C contract.

## Compiler Controls

[State-save driver](../../tools/experiments/game_indexed_state_save_candidates.py)
compiles with the **real repository actor definitions and function headers**.
Eight forms under O2/g3, O2, O1/g3 and O1 give **32 controls**, empty compiler
diagnostics. The selected halfword-pointer form emits all 38 retail words.
Named word-pointer, explicit byte-offset and register-index forms also match.
An unsigned slot changes the retail signed halfword load and loses one word;
direct array gates/saved-ID expressions and early return lose the match.

Plain O2 emits 38 words with two differences. O1/g3 emits 69 words, frame
0x20, 68 differences and is oversized. None of those controls is installed.
Receipts are ignored under `conker/build/game-indexed-state-save/`.

## Qualification

[Eight state-save tests](../../tools/tests/test_game_indexed_state_save_match.py)
compare retail, direct C and the independently scheduled plain-O2 body with
an independent sequential byte-memory reference:

- **7680 opaque-callback cases**: 32 index patterns, six gate halfwords,
  five old/new field patterns, both stack phases and four mutation modes.
  Include all 21 declared slots, bounded negative/outside indexes and guest
  shift-wrap patterns. Check every non-stack byte, exact ordered reads/writes,
  callback snapshots/argument/count and return result. All 38 words execute.
- **4736 connected-callback cases**: 32 indexes, 37 nonzero masks including
  every bit position, blocked/open gates and both phases. Execute the original
  14-word bit selector as well as all 38 wrapper words. The unchanged
  production callback matches those same 14 words, bound by production tests.
- **Six zero-mask prefixes**, each through three wrapper bodies: the existing
  connected callback remains in its wrapped bit-search loop until the bounded
  instruction budget is exhausted. Pre-call state persists, no callback ID
  store or wrapper return. This is not a successful-return/gameplay claim.
- **2520 native 32-bit cases**: 21 declared indexes, six gate values, five
  field patterns and four opaque callback mutations. Bind the fixture prefix
  offsets and check all 1024 backing bytes, callback-entry snapshot, argument,
  call count and return. This uses a minimal native prefix fixture; real
  production layout is independently bound by the IDO/header/linked match.
- Negative controls detect the old stub, wrong stride, early install and
  marking after callback. Production checks bind the exact source/slot,
  absence of target guards and removal of the obsolete draft.

The existing TriangleOracle is unchanged. A local signed-halfword execution
path preserves the raw read trace and sign-extended register result. Normal
returns check saved GPR/FPR/SP/RA state. Opaque callbacks clobber caller-saved
registers; connected tests execute the actual callback instructions.
No hardware timing, full callers, zero-mask termination, valid-domain
expansion or full gameplay acceptance is claimed.

Six pre-install tests pass in **26.313 seconds**, no skips. The additional
zero-mask test passes before installation in **2.400 seconds**. All **43
post-link tests pass in 48.052 seconds**, no skips: eight state-save tests
plus the preceding 35 timer/packet/linked-tail/linked-record/random-range/
sound tests. No shared oracle or generated-slice/guard tool change.

## Linked Audit

Before receipt equals the preceding **6059-slot** checkpoint. All names,
addresses and lengths survive. **Only func_15123934 changes**; all other
6058 slots, including the 34-word restore and 14-word callback, stay identical.
Target SHA-256:
`0ca5f88382a7ed410db1fe4d28048c4f5fa4d3600feff7980effddc1c1b58880`.
Ignored before/after/audit/behavior/connected/warning receipts live under
`conker/build/game-indexed-state-save-test/`.

Init 164048 bytes, Init data 17376 bytes, Debugger 19800 bytes and Game data
189088 bytes remain unchanged. All **720 data owners** are retail-exact,
zero different bytes/owners. All **10646 guard rows** remain identical and
ordered. Build/progress/match-progress pass. The existing duplicate
generated_12D630 recipe warning remains.

Owner compilation emits five unrelated warnings: four 712 pointer/integer
warnings and one 709 pointer-assignment warning. Independent compilation of
the committed baseline and current owner proves identical warning IDs,
messages and source expressions. No new target warning or unrelated fix.

Fresh measurements: total **3313/5462 exact (60.66%)**, Game **2640/4789
(55.13%)**, Init **492/492**, Debugger **181/181**, zero drift, **2149**
different Game C functions. Converted function/byte totals stay unchanged.
README gets aggregate rows only; recovery detail remains in docs.
No sibling source/build/save/frozen Release change or push.

Project-tool and whitespace checks pass. **3114 relative links across fourteen
documents** pass, zero broken. No generated build/screen/receipt output is
committed.

## Reproduction And Next

```sh
python3 -m tools.experiments.game_indexed_state_save_candidates
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_indexed_state_save_match tools.tests.test_game_random_reload_timer_match tools.tests.test_game_effect_packet_wrapper_match tools.tests.test_game_linked_record_tail_match tools.tests.test_game_linked_record_position tools.tests.test_game_random_range_position tools.tests.test_game_object_position_sound_adapter -q -f
make tools-check
git diff --check
```

Wait for relinking before production tests. Next inspect **func_15143D18**
in [game_16EE20.c](../../conker/src/game_16EE20.c), confirmed to have an
existing temporary-swap C body, not a placeholder. Live ELF: 24 emitted
words, no stack frame, 36-word slot, all 36 aligned words differ.
[Retail](../../conker/asm/nonmatchings/game_16EE20/func_15143D18.s) uses a
0x10 frame, saved S0/S1 pointer lifetimes, XOR argument/value swaps and
sequential lower/upper clamps. Recover that source/access shape, qualify
equal/aliased pointers and signed extrema, and use adjacent exact
`func_15143DA8` as a local XOR/volatile-pointer reference, not a guard template.

The edge helper remains at 102 differences; full Game matching stays active.
No push.
