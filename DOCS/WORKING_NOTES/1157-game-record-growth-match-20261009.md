# Game Record Growth Match

Verified locally: 2026-10-09. Complete `func_151488C4` is now semantic C
and directly byte-exact across **140 words / 560 bytes / frame0x10**.
No guards, filler, inline assembly or profile override. This credits an
already exact GLOBAL_ASM function to C; it does not change the guest ELF.

## Baseline And Scope

Parent **173fdaed42135d193d181c9ea19ef3250c37b427**, mounted tools
**741b4055bf8dd9394c3ea64c107d0bf82b7b7787**, both clean before edits.
Older standalone HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a** and
all **66 pre-existing status lines** are independent and preserved.

Owner [generated_175250.c](../../conker/src/game/generated_175250.c),
original [complete assembly](../../conker/asm/nonmatchings/generated_175250/func_151488C4.s),
VA **0x151488C4..0x15148AF4**, ROM **0x175D74..0x175FA4**.
Actual protected **D_8008A3E0[1] at 0x8008A3E4** points to this function;
the complete banked 100-word timer calls the 97-word payload dispatcher
through **D_8008A200[1] at 0x8008A204**.

Before-source SHA-256:
**8a3afc98c34bc50f802db7a9ec4e45ea6d73296a4b85cb5c346661b63a09a940**.
Before/after complete ELF SHA-256:
**9882610856cfd36a0022c543d536b8b6817c335a3b74a95ce1c24abaea0e143e**.
All **6,058 linked slots** and **11,507 guard rows/bytes** are unchanged.
Guard SHA-256 remains
**a75754c128d68f1a901860e0f73f6f5ac87545d485f47bac76cedc52c3e0d748**.
No assembly/layout/compiler/profile/shared-helper/OGL changes.

## Recovered Contract And Fitting

Capture records at actor+0x94 and payload at actor+0x98. Integrate forward
from signed actor+0x2D to live signed actor+0x2E with 20-byte records,
live unsigned count at +0x25 and four fresh D_800BE9A4 loads per record.
Ordered float32 gravity, updated velocity-Y, X, Y and Z operations preserve
public access order, overlap behavior and signed full-width local index.

Read signed active at +0x2C after integration. Below count-1, choose initial
phase 0/4096 from payload+0x18 bit0x20. Only nonzero active initializes
**u16 step at SP+0** to narrowed signed 4096/active. Append the actor's three
position words bitwise, increment active as a stored byte, then reload head
for initial vertical velocity from payload+8. Reload live head/count before
incrementing/reloading/wrapping the stored signed head byte. Shape each
record+0x10 halfword with live flags/count/head. At full capacity, change
payload+0x20 to 3 when flags&0x17, otherwise 2. Return signed word 1.

Retail deliberately skips step initialization at active zero. Do not repair
it with a guessed zero or alternate divisor. Tests separately qualify
emitted prior-stack behavior; this is not a portable-C promise for an
uninitialized read or a PC-port safety claim. No production iteration limit,
empty-count exit, clamp or null check is invented.

Initial complete candidate already emitted 140 words but frame0x20 with
107 differences. Pointer-first setup, live head expressions rather than an
extra cached local, indexed records, phase-before-step declarations,
count-first equality and explicit selector if/else recover all words with
ordinary O2/g3 C. Two original HI16/LO16 time-symbol relocations remain
at offsets0x1C/0x20. IDO candidate/owner diagnostics and added pools: zero.

## Fresh Qualification

[Candidate driver](../../tools/experiments/game_record_growth_candidates.py)
and [eight-test suite](../../tools/tests/test_game_record_growth_match.py)
reuse existing compiler/parser, float, guest oracle, native32 and owner
helpers; no shared helper edits or Claude calls.

- **2,806 cases / 5,612 executions**, all public metadata byte patterns,
  finite float/signed-zero samples and four prior-step patterns at two
  incoming stack phases. Raw/retail full register/float/LO/events/memory
  agree; independent ordered reference agrees on public trace/state.
- **135 reachable words**; natural dead indices **66,72,115,128,136** are
  retained. **994 bounded prefixes** are observed, not production exits.
- **265 missing-byte pairs**, lazy full-capacity empty integration, and
  **49 live alias cases / 98 executions** including global time overlap.
  These qualify emitted fault prefixes, not portable C fault behavior.
- **Nine effective compiled negatives / ten samples**: signedness of active,
  start, count and head, guessed-zero step, phase direction, initial velocity,
  selector mask and cached time. Each changes observable behavior.
- **81,534 actual native32 defined cases**, no FMA or strict-alias assumptions,
  full **256 actor /128 payload /11,200 record-byte canaries**. Exclude
  zero-active uninitialized-step and cyclic cases from native execution.
  Locally suppress only GCC's maybe-uninitialized warning around the
  deliberately retained candidate; IDO production has no new warning.
- Ten fully asm-postprocessed owner neighbors, pools and relative relocations
  unchanged, zero diagnostics. Actual padder emits all **560 bytes** without
  filler or guards. Four independent GNU links, **64 cases**, relocate both
  entry and time including HI/LO carry cases.
- **24 connected cases /48 executions** use complete **100+97+140 words**
  through actual table identities, including zero-active prior-stack and
  selector transitions. No external callback/cleanup hooks. The complete
  dispatcher still publishes the actual record position afterward.

Fresh normal builds succeed; preserve the existing duplicate generated_12D630
recipe warnings. One premature post-install run read the ELF while the
linker was writing it; classify that as an artifact race, not a source defect.
Wait for the terminal build, then rerun all eight tests against the finished
ELF. Baseline ELF/guards/progress are captured once and never recaptured.
Whole-ELF exact audit includes every byte/symbol/metadata/data section;
exactly one progress row changes asm -> c, no audit exception.
Final complete eight-test run passes in **32.874s**, after the final
comment-only incremental build is terminal. The earlier successful complete
pre-install run was **32.355s**; the first terminal-build post-install run
was **39.077s**. Do not count the concurrent-link race as a passing run.

Fresh **35 shared tests pass in 9.590s** and both `make tools-check` and
mounted `check_project_tools.py` pass. Prior unchanged neighbor-suite
receipts remain historical, not fresh reruns; whole-ELF identity is the
unchanged-evidence basis. Core matching acceptance is not hardware/gameplay.
Documentation checks **143 documents /4,241 relative links /zero broken**;
all **33 mounted/mirrored tool files** parse and have identical bytes.

From the prepared parent root, fresh acceptance commands are:

```sh
wsl --exec make -C conker -j4 build/conker.us.elf progress.csv
wsl --exec python3 -m unittest tools.tests.test_game_record_growth_match -v
wsl --exec make -C conker match-progress NON_MATCHING=1
wsl --exec make tools-check
```

Run the test only after the build has terminated. The standalone tool check
is `wsl --exec python3 check_project_tools.py` from the mounted tools root.

## Measured Progress

Fresh matcher: Total **3,405 /5,488 exact (62.04%)**; Game **2,732 /4,815
(56.74%)**; Init492/492 and Debugger181/181 exact. Zero drift, **2,083
different**. Converted counts Total **5,488 /6,042 (90.83%)**, Game
**4,815 /5,321 (90.49%)**; converted bytes **85.95% /85.31%** respectively.
CSV byte totals **1,939,740 /2,256,728**, Game **1,768,304 /2,072,880**.
One function /560 bytes gained; Init/Debugger unchanged. Root README gets
aggregate rows only, detailed recovery stays here and in doc indexes.

## Banking And Open Boundaries

Per "Keep commited", commit the two mounted tool files first, then parent
source/docs/exact gitlink. Mirror only absent new files into the independently
dirty older checkout without replacing its work, committing or resetting it.
Preserve both dirty-file hashes and all 66 initial status lines. No push,
pause, dependency/account change, OGL Release, runtime, save or editor work.
Ignored `conker/build/game-record-growth-test/` retains original before ELF,
source fingerprint, guard/progress snapshots and detailed qualification
receipts; exploratory candidates remain in game-record-growth/. Commit no
ROM/ELF/native binary/progress CSV/probe artifact.
Mounted tools **9d3bfa0ac0ccdd351a63584d63914e0f2537dee3** is committed first
with exactly the candidate driver and focused suite; the parent pins that
exact revision second.

Manual Graphify refresh refuses **17,006 nodes** over retained **38,793**;
fail-closed keeps **19,398 nodes from 2,972 excluded files still on disk**.
Existing version/zero-node warnings remain. No force or reinstall. Await
the specific parent post-commit hook separately before reporting clean state.

## Next Work

Recover complete first-stage **func_15148BA4**, still GLOBAL_ASM in this
owner, **D_8008A3E0[3]**: VA **0x15148BA4..0x15148DE0**, ROM
**0x176054..0x176290**, **143 words /572 bytes /frame0x58**. It conditionally
copies the old position when flags&7, integrates backwards with live time,
then uses flags&0x17 for a height comparison/query through func_15046C80.
Preserve that distinct gate: bit0x10 alone can reach a stack snapshot that
was not initialized. Actor+0x7D selects payload+0x24/D_8008A450 or
payload+0x23/D_8008A430 six-argument response callbacks, including float
arguments passed as word bits, stack extras and callback result conversion.
No guessed position defaults; qualify private lifetime, callback mutations,
ABI and the complete dispatcher connection before installation. The owner
renderer func_1514803C and trail constructor func_151DA6F8's unchanged
61 differences remain open, as do other callback/cleanup/upstream/hardware/
gameplay and graph-corpus gates. Wider Game completion is not claimed.

Follow-up 2026-10-09: the full 143-word height-response callback above is
now linked byte-exact C with three closed guards. Retain its narrower
snapshot gate/private lifetime; do not call the raw source directly exact.
See [Note 1158](1158-game-record-height-response-match-20261009.md) for fresh
qualification and the next complete 546-word renderer target.
