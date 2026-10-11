# Game Record Mask Teardown Guarded Match

Date: 2026-10-11. Recover complete func_1503E260 in
conker/src/game/generated_6B320.c, replacing its zero-return placeholder.
VA 0x1503E260..0x1503E3C4, ROM 0x6B710..0x6B874: 89 words / 356 bytes.
The existing O2/g3 profile emits 89 words, frame 0x50, 87 direct retail words.
Two expected-word guards relocate a closed private actor-address spill pair
from +0x38 to +0x3C. All 89 linked words are exact; this is not direct C.
No instruction drops, handwritten replacement or compiler recipe changes.
Matching +1 only; conversion counts/bytes unchanged. Full Game goal active.

## Baseline And Contract

Consumer c836bbb5fc555c78339678fae77962fe8bb0f2f5 and mounted tools
72fe85784a2d61bf53e174f110af7b6055f05485 were committed at entry.
[Note 1277](1277-game-record-state-dispatcher-direct-match-20261011.md)
left this genuine 89-word / 89-difference target. Read the complete retail
body, sole retail caller, actual data and owner profile after the scoped
Graphify query. Reuse IDO 5.3, structured ELF/CSV/object/pool parsers, MIPS and
native32 fixtures, assembly processor and both production padders. Codex is
the single writer; zero Claude calls, no bridge/install/account changes.

Recover void func_1503E260(s32 slot). Retail establishes no status result and
its caller ignores V0. Keep the full-width incoming slot and existing struct106
(16 bytes) and struct127 (812 bytes), without synthetic bounds gates or header
changes. The buffer address remains the existing signed 32-bit record field.

- Read record state +0xF once. Zero returns without table, count, buffer or
  actor accesses. Nonzero reads the unsigned group +0xE and optional pointer
  D_80084460[group]. A NULL table bypasses the count read completely.
- For a non-NULL table, cache its base and unsigned D_80098914[group] count
  across callbacks. Iterate indices 0..count-1. Only byte 255 skips; other
  high selectors retain the guest's low-five-bit variable-shift behavior.
- Call actual func_1503E1F4(index, slot). On nonzero, reread the selector after
  the predicate and reread actor +0x94 before ORing its mask. Callback changes
  to the current/next selector, masks, group, count table and table pointer
  distinguish cached inputs from live reads. Do not cache the selector.
- After scanning, read the live buffer before clearing state +0xF. Compute
  the actor address before free and preserve it across that boundary. A
  nonzero buffer calls func_10004074((void *)buffer) while the public record
  still contains that buffer address and its state has already become zero.
- After free, read the actor flag +0x74, clear record buffer +0, and write the
  flag with only bit 0x80 removed. A state byte written by free must survive;
  do not repeat the state clear. Flag changes made by free remain live.

The actual ELF's three initial D_80084460 pointers are all NULL; real counts
are 27/31/45. Non-NULL behavior is qualified with explicit mapped fixtures,
not claimed as initial runtime state. The linked 27-word predicate remains
exact and unchanged; its duplicate zero at +0x60 is unreachable.
The free routine remains unchanged. Its hook is a bounded boundary model,
not qualification of the allocator, SDK hardware or gameplay.

## Source And Closed Spill Pair

The initial pointer-cursor source emits 88 words, frame 0x58 and 69 word
differences. Indexed selector access recovers 89 words / four differences;
inlining the final actor access recovers frame 0x50 and leaves only two.
Scoped signed-mask, explicit masked-shift, nesting, local-width/order,
buffer/group/flag temporaries and pointer variants do not remove the pair.
The selected compact no-unroll diagnostic gives the same 89/2/frame 0x50;
it is not installed. This is a bounded measurement, not an exhaustive search.

RA +0x34, S0..S7 +0x14..+0x30, loop/control flow and all public instruction
ordering already match. Only this closed private store/reload home differs:

| Offset | Raw C | Guarded Retail |
| --- | --- | --- |
| +0x120 | AFA20038, sw V0,+0x38(SP) | AFA2003C, sw V0,+0x3C(SP) |
| +0x124 | 8FA20038, lw V0,+0x38(SP) | 8FA2003C, lw V0,+0x3C(SP) |

Append precisely two relocation-free expected-word rows. Both refer to the
computed actor address, neither changes frame size or touches another spill.
Single-half mutations fail effectively; stale expected words are rejected.
No artificial dead local, volatile padding, source projection or hidden
raw-instruction body. Preserve all original assembly and old guard bytes,
including the manifest's existing mixed line endings. Direct guard removal
remains open; do not represent this as an unguarded compiler match.

## Fresh Qualification

New tools: experiments/game_record_mask_teardown_candidates.py and
tests/test_game_record_mask_teardown_match.py. Immutable before-inputs and
receipts: conker/build/game-record-mask-teardown-match-test/.

- Eleven complete pre-install tests pass in 27.927 seconds. A one-test
  actual initial-table/count check passes in 1.819 seconds. All eleven
  installed tests, including that check, pass in 12.184 seconds.
  A final two-test literal-audit/integrity-control rerun passes in 2.236
  seconds after documentation changes.
- The 526-case retail/raw/guarded guest matrix covers all state bytes,
  counts 0/1/3/4/5/27/31/45/128/255, empty pointers, both mask words, high
  selector bytes, groups and stack phases. All 89 target words and 26
  reachable predicate words execute with the predicate hook removed.
  NULL-table/state-zero fixtures leave the unused count/table unmapped.
- Twenty callback-lifetime/public-alias cases cover selector reload, cached
  count/base, live mask/buffer/flag reads and free state preservation.
  External hooks clobber all caller-saved GPR/FPRs. Actor-mask/flag and
  record-mask aliases and invalid slots are mapped guest-only evidence.
- Two independently linked placements rebase six symbols, with HI16/LO16
  carries; 32 cases compare all forms. Predicate is a bounded hook only
  for rebases, separately executed as actual MIPS at retail addresses.
- All 81 fired fault triplets preserve retail/guarded private and public
  memory/events/registers. Raw C preserves the public prefixes, not the
  private spill addresses. This qualifies emitted guest order, not portable
  C fault semantics or undefined shifts/aliases outside their valid domain.
- Six freshly compiled semantic controls fail: wrong sentinel, cached
  selector, lost actor mask, early buffer clear, repeated late state clear
  and stale final flag. Both half-guard controls and the stale expected-word
  control fail. Separate stale/duplicate installs, source, target/neighbor/
  extent and old guard-prefix corruption are rejected without production
  mutation. The controls must fire; absent output is not acceptance.
- Both copied complete owners pass production GLOBAL_ASM post-processing
  and both real padders. All 21 neighboring functions, normalized pools,
  other slots/relocations and the 171-word dispatcher/27-word predicate
  remain exact. The selected isolated and complete-owner raw bodies agree.
- Native32 O2/O0 each pass 61,440 cases: 256 state bytes, ten counts, table/
  buffer gates and six callback modes. A sentinel control fails. Only
  selectors 0..31 and skipped 255 are native fixtures. The predicate is a
  defined unsigned masked-shift hook, not the existing helper C's shifts
  outside its portable domain. No host-port portability claim is made.
- Execute the complete retail 85-word func_1503F2B0 caller with all three
  target forms, actual predicate and linked 30-word func_1503EF4C query,
  their hooks removed, in 64 timer/mask/phase/free-mutation cases. Positive
  timer exits and expired teardown followed by live mask queries agree.
  Query's two existing commutative guards remain unchanged. This reaches
  87 target words in the caller fixtures; the separate guest matrix reaches
  all 89. Caller C is still a placeholder, not installed qualification;
  preparation/free are bounded models, not newly recovered implementations.

Initial harness failures were fixed before installation: an unused native
helper under -Werror, the reference model's inherited symbols, native case
receipt and a missing positive-timer fixture. No production workaround or
baseline refresh was used to pass them. Prior unchanged neighbor-suite
receipts remain historical, not described as freshly rerun.

```sh
python3 -m tools.experiments.game_record_mask_teardown_candidates --profiles
python3 -m unittest tools.tests.test_game_record_mask_teardown_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Linked Audit And Checkpoint

Full rebuild exits zero. The literal whole-ELF comparison changes exactly
287 bytes: 285 target-slot bytes and two function-size bytes, 12 -> 356.
Every other byte, function body/address/extent and metadata entry remains
exact; no projection, generic metadata ignore or permitted permutation.
Guard history is the complete original byte prefix plus only two rows.
Six other inputs remain unchanged: progress CSV, rodata assembly, symbol
addresses, undefined functions, retail layout and Makefile.

Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | 2dec3adb58a154d8be55eade61a66857a381e1b45886d8c9d5cc75535b487d4b |
| Source after | f9e9a919dfbae01d337e9a7c5130e52d5f6f518070f8822f2dd72247535150ef |
| ELF before | f529e1b3dbe2f252a309438b8a3e84bfb587d7f39db0199e48c8627569db62c1 |
| ELF after | 25dd5c57a0dfcffa127574c1a9402176167c67cfe3b4ef1b74e93d5066b46d54 |
| Guards before | 2c86d53acedfcb94ac1e3fcd03bab86a3b0854c6813f07dfb080f415b26255a7 |
| Guards after | 75a00e8d566bd1f737d2d4bd2bbbc5c01eb7ec6c33f9789a422b5aa73bc1d5ed |

Fresh match-progress: Game 2,799/4,822 (58.05%), total 3,472/5,495 (63.18%),
Init 492/492 and Debugger 181/181. Zero drift / 2,023 still different.
Matching +1 only; root README gets aggregate rows, not a recovery narrative.

Consumer, mounted and older tools shared checks plus native py_compile pass.
Bank mounted tools 1c81a02 first, then source/guards, this note, five current
indexes, aggregate README and consumer gitlink. Older sibling HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 47 recorded fingerprints
are unchanged. Copy only two absent new paths with identical hashes:
dirty count 324 -> 326. Do not commit/reset/push that independent history.
The function suite runs in the mounted consumer, not the standalone mirror.
Active consumer/mounted checkouts must finish committed and clean. No push.

Native graphify update . exits one on protective shrink refusal: 18,142
candidate nodes versus 39,922 saved. Preserve 19,398 nodes from 2,972 existing
excluded files; no force/purge/install. Version and empty-source warnings
are separate from compiler diagnostics. The wider manifest rebuild emits
existing source warnings and the duplicate generated_12D630 recipe warning;
copied target-owner compilations are diagnostic-free. After consumer commit
require a fresh terminal Rebuilt, advanced log bytes/UTC and zero workers,
not merely a hook-launch message. Precommit log: 534,443 bytes.

## Next Game Body

Live recheck: func_1503DF48 171/zero, func_1503E1F4 27/zero,
func_1503E260 89/zero linked differences. Next genuine unmatched body is
func_1503E3C4: 141 words / 136 differences, still a placeholder, same owner.
VA 0x1503E3C4..0x1503E5F8, ROM 0x6B874..0x6BAA8. Recover its complete five-
argument record/matrix setup, signed type selection, ten-argument output
decomposition and normalized actor-relative vector before installation.
Preserve the adjacent func_1503E5F8 GLOBAL_ASM body. The dispatcher's bounded
setup hook does not qualify this implementation or its floating-point cases.

Removing this spill pair, the third-loader scheduling and parent/pair guards,
and deeper callbacks/SDK/allocator/hardware/renderer/gameplay remain open.
No OGL Release build/change, private input/save mutation or active editor/
debugger changes. Keep the full Game goal active; no completion claim.
