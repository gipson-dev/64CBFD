# Actor State Tick Homes And Ordered Reads

Date: 2026-10-19. Consumer predecessor: `8120b470`; tools predecessor: `01e3b05`.
Tools checkpoint: `59b52f1`, committed before the consumer documentation/pin.

## Recovered Boundary

Continue complete **func_1508A6FC** from
[Note 1616](1616-actor-state-tick-frame-captures-and-native-qualification-20261019.md).
The selected experimental C retains **678 words/frame 288**, now recovers
**seventeen observed named homes**, and closes the measured public-read order
boundary. Raw differences are **600**, not zero. Production remains the same
12-byte zero-return stub; no installation, guard additions or matching credit.

[Home candidates](../../tools/experiments/game_actor_state_tick_homes.py) use
the existing ECOFF parser to read actual IDO local offsets. A closed permutation
of 39 real declarations recovers these homes without adding storage:

```text
changed 100       previousTimer F8     active EC       seen E8       count E4
groups DC        latches D8           actions D4      states CC     elapsed C8
timers C4        cooldowns C0         timeouts BC     events B8     groupCounts B0
scores AC        idle AB
```

All offsets are relative to the current SP. The parser's negative local offsets
are added to the measured 288-byte frame, then checked against emitted code and
guest aliases. Debug metadata alone is not treated as runtime proof.

The completed group selector is also reused to retain the current difficulty
selector through the timer-reset path. It reloads difficulty after the indexed
timer store and before reading back through the byte cursor. This emits the
retail difficulty-before-timer read order directly from C. The reused local is
named `selector`, rather than retaining the misleading group-only `owner` name.

The exact bridge from Note 1616 is checked: **101 stack-immediate fields** change,
with every corresponding opcode/register field unchanged; then the independent
LW/LB words at source offsets **640/644** exchange order. The difficulty LO16
binding moves from 644 to 640; every other binding is identical. No word patch,
physical register binding, volatile, dummy variable or compiler override is used.

Eighteen bounded forms retain the rejected investigations. Explicit spilled
cursor variables, scalar compaction, word-sized action locals and indexed output
arrays do not improve all required gates together. The selected body is the
closed declaration permutation plus the real selector lifetime, not those
larger-frame or changed-length alternatives.

## Fresh Qualification

[Eight tests](../../tools/tests/test_game_actor_state_tick_homes.py) pass in
**30.900s primary / 47.316s mirror**, no skips. Both copies compile the complete
selected source with separate owner/native receipts.

- All 262 completed fixtures now compare **ordered public reads**, including
  addresses, widths and values, as well as ordered stores, all public memory,
  helper arguments, results and restored saved GPR/FPR state. This closes the
  earlier fourteen unequal read positions in the sixteen-slot B9 fixture.
- The corpus retains all thirty fired helper mutations and visits 660/678
  retail words. It does not establish full instruction or exception coverage.
- Thirty-four completed guest alias pairs exercise each of the seventeen homes
  in both stack phases. Retail and new C agree on public reads/stores, memory,
  helper calls and return masks. Every requested private write fires, and every
  retail fixture has an observable effect compared with its unmodified run.
- All thirty-four old-home controls reject the predecessor. Some old controls
  encounter unmapped guest accesses, but only after the requested mutation has
  fired. This is an effective wrong-home control, not hardware fault acceptance.
- Twenty-four additional sixteen-slot public-read footprint pairs pass. The
  prior 676-word no-reload control still loses seven actual timer reads.
- Fifty-seven native32 fixtures pass O0/O2/O3 with UBSan on the newly selected
  C. Three compiled semantic negatives and the SIGILL -4 overflow control
  remain effective. Guest frame aliases are not passed to native C.
- Both complete owner profiles preserve 72 other function bodies and normalized
  pools; isolated words/bindings equal complete-owner output. The seven pinned
  production inputs remain byte-identical. The inherited unrecovered callee's
  old-style declaration stays confined to the owner fixture.

The initial group/action/counter alias pilots used identical alternate data or
did not enter a transition, so they were not accepted as effective controls.
The final fixtures change the alternate group/action rows or open the actual
transition latch, and explicitly require a retail effect before counting a pair.
No ordinary C guarantee that an opaque provider can access unescaped locals is
claimed; these are bounded guest-stack ABI probes.

## Still Open

Three named output-cursor homes remain wrong: source `reset/status/band` use
SP+A4/A0/9C, rather than retail SP+84/60/5C. Anonymous cursor/call-save slots,
whole-function register lifetimes and scheduling also remain unrecovered.
The source still has the saved-role permutation described in Note 1616; the
101 stack changes and two-load swap do not restore those register operands.

Ordered public accesses do not imply identical private memory, PC/fault-prefix
state, all-input alias behavior, FCSR or hardware behavior. Complete instruction
coverage, remaining private/fault/alias gates, independent original-assembly/GNU
rebases, actual padding/Make/strict first image and installed-state gates remain
open. Do not install or generate broad guards merely because shape and these
seventeen homes now agree. Keep the wider Game goal active.

## Preservation And Resume

Tools checks and Python syntax checks pass. Only two absent task files are
copied into the independent mirror; HEAD `ddbdd16b` and all **1,438 older dirty
leaf hashes** remain intact. No mirror commit/reset/stash/clean, push, host or
frozen Release operation, dependency update or advisory-agent call is performed.

Production C/guards/ELF/Makefile/progress and root README remain unchanged.
Installed totals are still the Note 1614 checkpoint, not a new recount: Game
**3,017/4,832**, overall **3,690/5,505**, 1,815 different/zero drift; owner
**69/73** exact. There is no new conversion or matching increment.

```text
Selected raw: 260a9fc2acbfa79a5348dda1a6589ca3ac73b81ea6aeda4c90798a4f9c52fb51
```

Ignored receipts: `conker/build/game-actor-state-tick/lifetimes/homes/`, including
the source screens, ECOFF home maps, final primary log, separate `mirror/` log
and owner/native artifacts. The consumer commit hook refreshes Graphify; retain
and audit its prior protected nodes before closing the checkpoint.

Next: recover the remaining three output-cursor homes and anonymous spill
ownership, then the whole-function saved-role/schedule mapping. Preserve the
seventeen homes, ordered-read checks and effective alias negatives while doing so.
