# Complete Game Actor Renderer Original Private Layout

Date: 2026-10-10. Continue the same complete renderer from
[Note 1221](1221-game-complete-actor-renderer-recovery-and-private-layout-gates-20261010.md).
Consumer baseline a6067a2; mounted-tools baseline 4d76cac.
Codex is the single writer, zero Claude calls. Keep tools-first authorized
commits, no push, no host/Release builds, saves or editor changes.

## Closed Physical Layout

func_1502CCFC remains the complete eight-argument target:
VA 0x1502CCFC..0x1502D54C, ROM 0x5A1AC..0x5A9FC, 532 retail words.
The production placeholder, linked ELF, guards, conversion rows and rodata
remain byte-for-byte unchanged. This is a layout checkpoint, not a byte match.

[Complete layout experiment](../../tools/experiments/game_actor_renderer_layout.py)
separates the early model-gate flag from later lighting state. Capture mode
before the early three-mode test; reload it only after the actual identity/tier
helper branch. Preserve later incoming-mode reads. Reorder real scalar locals
and express history selection as its recovered conditional 10-or-2 value.
No unused frame filler, assembly body copy or missing-body padding is added.

Selected full semantic C: plain-masked-retail-homes-ternary-history.
It emits 531 words, original 0x150 frame, zero diagnostics and zero new pools.
All ten color outputs are exactly original SP +0x128 through +0x104, descending
four bytes each. Identity +0x140, tier +0x144, configuration +0x130 and
color-state +0x13C spills agree in the complete private access traces.
Saved s0..s6 homes are +0x40..+0x58; saved RA is +0x5C. Full runs validate
saved-register restoration and the original frame-relative lifetimes.

The portable selected body retains part & 31 before its variable shift.
An unmasked guest-only comparison emits 530 words with the same frame/homes
and 111 positional differences; it is not a native-C candidate for part >=32.
Selected masked C has 226 positional differences, many from shifted layout.
These counts do not mean 111 or 226 independent scheduling fixes are proved.

Two explicit mode-3 continue/goto exits emit 536 masked or 535 unmasked words,
but change the frame to 0x130. Reject these shapes despite equal absolute color
addresses. The earlier null-continue form likewise retains its wrong 0x148
frame. Exact colors or total word count alone do not close installation.

## Fresh Qualification

[Private-layout suite](../../tools/tests/test_game_actor_renderer_layout.py):

```sh
python3 -m unittest tools.tests.test_game_actor_renderer_layout -v
make tools-check
```

All eight tests pass in 16.392s. Fresh project tool checks pass.

- 273 primary cases / 546 complete original-and-C executions exercise all
  532 retail words. Independent public semantic reference agrees; complete
  private/public memory, access events and access counts are also exact.
- Cover the prior full graphics/mode/lighting/alpha/count/mask/callback sweep,
  including wrapped shifts at part 32 and both incoming stack phases.
- 16 alias/mutation cases compare parameter arrays overlapping public output,
  incoming argument homes and private color homes, plus callback writes to
  the incoming mode. Complete memory/events/cursor agree.
- 1,963 requested fault-prefix pairs across six complete fixtures all fire
  at the requested access index. Full memory, events and call prefixes agree
  before every fault, including private prologue/color/spill/epilogue accesses.
  These qualify emitted guest order, not portable C exception semantics.
- A freshly compiled old 524-word/0x148 layout is an effective negative:
  public reference passes, but full private memory and events fail.
- Copied owner preserves all 37 neighbor bodies and relative relocations,
  normalized pools and isolated target instructions; zero diagnostics.
- Six independent original/C links and nine cases retain full private memory
  and access order under three symbol sets with signed LO16 carries, including
  distinct virtual and physical matrix aliases.
- New immutable baseline matches the unchanged previous baseline exactly.
  Source SHA-256 remains
  6d3eb1946ce65477f56e8dea69a89812a6ebead86b7f980472dbf9ada660d216;
  linked ELF remains
  0e401ea0c0f8361e202571d92d18d8df6d43f96b9f6de77809c11dff894cdbb1.

Correct the previous documentation's arithmetic: the original recovery suite
has 112 graphics +131 early-gate/shift +14 mutation +16 lighting cases,
273 primary cases, not 417. Its three forms therefore execute 819 times,
not 1,251. Historical source, tests, baselines and receipts are not rewritten.
The four affected concise indexes and Note 1221 are corrected.

Callbacks remain explicit bounded ABI/effect models. Public/private agreement
does not claim the real color, lighting or matrix helper bodies execute.
No native32 SDK renderer, FCSR/trap, hardware or live acceptance is claimed.
Production matching stays Game 2,760/4,816 (57.31%), total 3,433/5,489
(62.54%), zero drift / 2,056 different. Root README aggregates stay unchanged.

## Bank And Resume

Tools 755a04d commits the two new authored files first. Mirror their previously
absent paths only; older tools HEAD ddbdd16 and both tracked-dirty fingerprints
remain unchanged. Native Git dirty entries rise 204 to 206 only for the mirrors.
Consumer commit banks this note, five concise indexes, corrected prior note
and the new tools pin. No push or independent older-tools commit.

Before the mirrors, fresh prior document/tool validation passes 43 documents,
4,254 relative links and 76 exact authored mirrors. Fresh validation afterward
passes seven affected documents / 4,075 relative links and two exact new mirrors
parsed in both copies; old validators and their receipts remain unchanged.
Manual graphify update exits 1 refusing 39,410 to 17,629-node shrink; retain
19,398 nodes from 2,972 excluded-but-existing files. Preserve version and
zero-node warnings, no force/purge/install. Verify the fresh detached hook
and its log growth after the consumer commit.

Continue this same full renderer, in order:

1. Close the complete 532-word instruction layout without weakening the
   frame/private-prefix proof. Inspect the redundant masked SLLV producer,
   mode-3 merged versus duplicated branch/LHU exits, independent geometry
   constants and closed loop-register allocation cycles. These are measured
   layout differences, not a certified guard recipe yet.
2. Qualify any recipe with every stale word/relocation dependency, actual
   copied-owner padding and independently assembled rebases. No ROM-word
   body replacement, unexplained padding or shifted-home normalization.
3. Run native32 SDK output and complete actual dispatcher/RGB/shading/renderer
   connections. Use the complete original func_1502CC34 color-helper body and
   actual contract; bounded callbacks are not restoration evidence.
4. Install only after those gates, rebuild, audit the whole linked ELF and
   protected data, and measure fresh matching credit.

Keep the separate curve rejection gates from
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md)
and the wider Game goal open.
