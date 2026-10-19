# Actor State Tick Frame, Captures And Native Qualification

Date: 2026-10-19. Consumer predecessor: `ee8c237c`; tools predecessor: `e831838`.
Tools checkpoint: `01e3b05`, committed before the consumer docs/pin.

## Recovered Shape

Continue complete **func_1508A6FC**, VA 1508A6FC..1508B194, ROM B7BAC..B8644,
from [Note 1615](1615-actor-state-tick-recovery-and-layout-boundary-20261019.md).
The selected experimental C now emits **all 678 words and frame 288** on the
existing primary profile. Normal-profile words/bindings are identical.
There are still **607 aligned word differences**: this is not a byte match,
production installation or new matching credit. Its 12-byte production stub
and every existing guard remain unchanged.

[Lifetime candidates](../../tools/experiments/game_actor_state_tick_lifetimes.py)
retain 27 bounded source forms and select `reused-timer-reload`. Capturing each
table address from the global integer base before the loop recovers all eleven
eager table-base definitions and stack stores. It prevents IDO from collapsing
those bases into the earlier shared byte-pointer context. The normal compiled
result still captures the global once; no per-iteration global table query is
substituted.

Removing redundant named row cursors and reusing the completed actor-loop
cursors for drawing recovers frame 288 through real source declarations only.
No dummy storage, added public access, physical register binding, volatile,
instruction array, compiler override or production structure is introduced.
Aggregate, index, for-loop and register-keyword controls do not close matching.

One important missing access is also recovered. After clearing an indexed
timer, the source reads it through the retained byte-offset cursor. Both
cursors denote the same row, but IDO retains the real read instead of replacing
it with zero. The earlier 676-word/frame 288 form loses seven timer reads in
the dedicated sixteen-slot fixture; this control is effective. The recovered
read produces the complete 678-word extent without instruction padding.

## Fresh Qualification

[Eight tests](../../tools/tests/test_game_actor_state_tick_lifetimes.py) pass
in **28.227s primary / 25.359s mirror**, no skips. The complete selected source,
not the older 658-word candidate, is used in the new suites.

- 262 completed retail/source fixtures agree with the independent state-machine
  reference on ordered public stores, all public memory, helper arguments,
  changed masks and restored saved GPR/FPR state. The corpus visits 660/678
  retail words; complete instruction coverage remains open.
- All thirty requested mutations reach their opaque providers. Captured
  count/mask/table inputs and live globals stay distinguished. These are
  bounded helper models, not recovered helper implementations.
- Twenty-four sixteen-slot pairs span three categories, four difficulties and
  both stack phases. The public read multisets, including values and widths,
  are equal. This does not claim equal read order or fault prefixes.
- Fifty-seven native32 fixtures execute the actual complete C at O0/O2/O3 with
  trap-mode UBSan. Typed cell serialization translates guest big-endian data
  into native field values and relocates only actual pointer fields. Every
  public buffer, result and helper argument is checked against the independent
  reference. No guest frame aliases or out-of-domain native indices are used.
- Three compiled native negatives reject a widened actor flag, four-word
  cursor stride and inclusive random comparison through explicit event/data
  errors, not crashes. The signed-overflow sanitizer control fires SIGILL -4.
- Both full owner profiles preserve all 72 other functions and normalized
  pools. Target raw words/bindings equal isolated output. The old-style
  unrecovered callee declaration remains owner-fixture-only, as in Note 1615.
  All seven pinned production inputs are byte-identical after qualification.

The first optimized native run faulted on an unaligned `movaps` stack store.
A bounded GDB run of the owned fixture confirmed the kernel-to-C `_start`
alignment mismatch. Applying `force_align_arg_pointer` to this fixture's
entrypoint fixes the actual ABI setup; the recovered C and shared startup
helper are unchanged. An effective negative produced the explicit extra-call
error 32, which the final check accepts along with the other defined trace/data
errors. Failed harness runs are not final acceptance receipts.

## Remaining Literal Boundary

The tests deliberately retain a failing-to-match boundary instead of treating
equal shape or read counts as byte identity. At `func_150859AC(slot=1, field=4)`
in the sixteen-slot B9 fixture:

| Role | Retail | Current Source |
| --- | --- | --- |
| Byte offset 4 | S0 | S3 |
| Global address 800D23B0 | S1 | S1 |
| Slot 1 | S2 | S0 |
| Actor 800CC5FC | S3 | S2 |
| Latch pointer 20360 | S6 | S7 |
| Elapsed pointer 20220 | S7 | S6 |
| Slot bit 2 | FP | FP |

This is a measured call-site role permutation, not a proof of a closed mapping
over every lifetime. The eleven source table homes are contiguous from
SP+108 down to SP+E0; retail uses SP+DC..SP+AC with two intervening slots.
Private-home placement and scheduling are still wrong.

In the same fixture both versions make 916 public reads, but fourteen trace
positions differ: the difficulty-byte load and timer reload exchange order
for seven rows. Preserve this concrete boundary when recovering the final
source homes/schedule. No fault, private-frame or alias equivalence is claimed.
Independent original-assembly/GNU rebases, complete coverage, actual padding,
Make, strict first-image and installed-state gates also remain open.

## Preservation And Resume

Tools checks and Python syntax checks pass. Two absent task files are copied
into the independent mirror; HEAD `ddbdd16b` and all **1,436 older dirty leaf
hashes** remain intact. There is no mirror commit/reset/stash/clean, push,
dependency/advisory operation, host change/build or frozen Release access.
Only tools and documentation/pin change; no N64 production rebuild is needed.

Installed totals remain the unchanged Note 1614 checkpoint: Game
**3,017/4,832**, overall **3,690/5,505**, 1,815 different/zero drift, owner
**69/73** exact. These are not a new recount or matching increment. Root README
and production C/CSV/ELF/Makefile/progress fingerprints are unchanged.

```text
Selected raw: 78444a63df0e30b12773ae5adc217ab832ea09b1b9e9296da8c6e6a16eece5c9
```

Ignored receipts live in `conker/build/game-actor-state-tick/lifetimes/`, with
separate `test/` and `mirror/test/` owners/native artifacts, both final logs,
the remaining-layout diagnostic and Graphify before/audit snapshots. The
consumer commit hook refreshes the graph; preserve all prior protected nodes.

Next: recover the real declaration/home permutation and whole-function saved
roles, then close the observed timer/difficulty read schedule. Keep the new
source extent/frame/captures and native qualification intact. Do not install
or generate broad word guards from shape alone. The wider Game goal stays open.
