# Route Dispatcher Direct Byte Match

Date: 2026-10-18. Consumer predecessor: `c05b9d65`; tools committed first as
`b0a32ea09d3dc1aac7af3bc19f1e48507026adde`. Continues
[Note1558](1558-route-projection-native-qualification-and-installed-byte-match-20261018.md).

## Installed Result

`func_15087CC0`: VA15087CC0..15087DCC, ROMB5170..B527C,
**67 words /268 bytes /frame48, directly byte-exact**. Replace its zero-return
stub in `generated_B3020.c` with complete `void func_15087CC0(void)` C and a
semantic comment. Keep the address-derived name rather than inventing one.
The routine resets the request byte, walks live route records and dispatches
the projection or either alternate-mode update.

No new guards, normalizer or Makefile/profile change. Raw unlinked SHA-256:
`42bfc05284be2e0cbe657b8925287fb5b43ab4c150edb1d1092538d83180e2a8`;
all17 relocation bindings are pinned. The existing no-unroll primary emits
the retail body, including its two unreachable duplicate-load words. Public
test paths visit65 words; literal byte comparison separately checks all67.

## Recovered Contract

- Clear D_800D23A9 before the null-table gate. A null D_800872A0 returns without
  reading the signed count D_800D2398.
- Walk0x84-byte records. Reload D_800872A0 for each iteration, retaining the
  monotonically increasing offset if a helper replaces the table.
- Sign-extend record[0x31] before multiplying by the0x32C actor stride; use
  actor base0x800CC2D0, not800DC2D0. Skip records whose actor+0x318 pointer is0.
- Sign-extend record[0x30]. State>=2 calls func_150891E8(record,actor). Otherwise,
  zero record[0x48] calls func_150896EC(record,actor,0); nonzero record[0x48]
  and nonzero signed record[0x49] call it with third argument1.
- Reload the signed count after each call, allowing shrink, growth or negative
  termination. Preserve the cached loop count on paths with no helper call.
  Do not clear the request again after a helper sets it.

The pointer-add baseline emits67/frame48 with five differences. Among six
source screens, `&D_800CC2D0[signedSlot * 0x32C]` restores the original S2
actor base/S3 stride, setup schedule and operand order directly. Integer-cast
forms retain four differences; swapped add, explicit stride and captured base
retain five. No physical register forcing or guards are used.

The one direct retail caller is func_15019130 at15019208. Its next instruction
after the call/delay is another JAL at15019210, without consuming V0. Correct
the caller declaration in `game_45B80.c` from s32 to void. All16 caller-owner
functions, bindings and pools remain unchanged. This is a call-window/ABI
check, not complete execution qualification of the large upstream function.

func_150896EC remains an unrecovered zero-return placeholder. A strict new
three-argument declaration conflicts with that old zero-parameter definition
in CFE, so retain its existing unspecified-argument declaration without
changing the unrelated stub. Its call arguments are checked here; its return
type and complete semantics remain a separate recovery task.

## Qualification

Eight tests pass before installation in57.566s and **after installation in
47.469s, no skips**. The installed run reads the real linked67-word body;
its historical context validates immutable predecessor/successor fingerprints
without rewriting the live source or ELF.

- **1850 paired guest cases** compare complete memory, GP/FP registers, calls,
  restored saved registers and stack. **1844** also compare an independent
  public-memory/call/ordered-access reference. The other **six** are deliberate
  private-stack aliases, not independent portable-C reference claims.
- Cover all256 signed count, state and actor-slot byte values, both gate bytes,
  nonzero high-bit object words, null table, empty/negative counts and request-
  byte aliasing. Effectful opaque helpers shrink/grow/negate the count, redirect
  the table, mutate pending fields/object pointers and set the request byte.
  They clobber caller-saved GP/FP registers and outgoing homes.
- **396 fired root access-fault prefixes across12 cases** compare complete
  memory, GP/FP registers, calls, PC and delay ownership. Opaque provider memory
  accesses are deliberately excluded. These are synthetic boundaries, not
  hardware exception/FPU/gameplay acceptance.
- **40 connected cases** execute the actual321-word projection,91-word selector
  and41-word enqueue with the new dispatcher. This covers states2/3, five signed
  actor slots, flags0/64 and two stack phases. The other callee remains opaque;
  do not claim its two modes are restored by these connected cases.
- Four independently assembled/linked data/call rebases pass **96 cases**, with
  low-half carry boundaries, signed slots and distinct code entries.
- **1824 native32 cases per O0/O2/O2+UBSan build** compare the complete aligned
  host-endian0x80000-byte arena, globals and effectful provider call log with an
  independent C reference. Private-stack, misaligned and unmapped aliases and
  hardware behavior are excluded. Native helpers are explicit opaque providers.
- Seven compiled O2+UBSan negatives fail by ordinary mismatch: unsigned slot22,
  unsigned state22, unsigned count21, wrong alternate22, cached table22, cached
  count21 and late request clear22. Crashes/sanitizer traps are not accepted.
- **84 effective raw controls** cover all67 words and17 removed bindings;
  all19 input fingerprints, three successor artifacts and three mixed live
  stages fail closed when changed.

The first test run exposed a fixture initialization issue: the inherited
oracle replaces its symbol dictionary, so install the dispatcher dictionary
after its base constructor. The next run exposed an unintended alternate-table
overlap with the private stack. Move that ordinary table to0x90000 and add an
explicit interval rejection, retaining the separate deliberate stack aliases.
Both fixes concern test fixtures, not production game defects.

## Owner And Linked Audit

Use the unchanged mixed-profile rule from Note1558. Compile the complete
primary and normal owner, run both GLOBAL_ASM passes and use the actual padder.
Preserve72 primary neighbors/pools and the projection's exact335-word raw
fingerprint/bindings in the normal override; all four assembly routines remain.
Reuse Note1558's unchanged seven-command Make qualification and nine-test
receipt explicitly, rather than calling them fresh tests for this turn.

The real build succeeds and exactly reproduces the immutable first linked
prediction: **214 changed ELF bytes**, only this target's instructions and
12->268 symbol size. All6057 function addresses,6056 other bodies and every
other ELF byte remain fixed. The actual padded owner equals qualification.
Protected Game data: **189088 bytes /720 owners /zero differing bytes**.
Makefile and guard CSV hashes remain5d18b217 and07994470 respectively; no EOL
normalization, guard append or fixture-baseline replacement is performed.
Existing game_45B80 pointer/integer warnings and the generated_12D630 duplicate
recipe warning are unchanged; qualification compares old/new caller diagnostics.

Successor SHA-256:

- ELF: `dfa6424d042a037e643108a051757e78515e4b89ac9772a95b8b9845938742e2`.
- Owner: `4fee3adb19dd5ee7f6d9e62994c948472365705afd6867d46fc7634aa260e1fe`.
- Caller: `f507c0c211e4990894bef42047f05dd40df85d9fe7a8996b887a547104cdc1ba`.

Fresh matching: **Game2988/4828 (61.89%)**, **total3661/5501 (66.55%)**,
Init492/492 and Debugger181/181, **1840 different /zero drift**. Conversion
remains5501/6044 (91.02% functions,86.04% bytes), Game4828/5323 (90.70%
functions,85.41% bytes). Fresh byte sums remain1941784/2256728 total and
1770348/2072880 Game. The old C stub already counted as converted; claim one
new exact function, not one new C conversion. Root README aggregate rows only.

## Reproduction And Resume

```sh
python3 -m unittest tools.tests.test_game_route_dispatcher_match -v
python3 -m tools.experiments.game_route_dispatcher_match --audit
make -C conker match-progress NON_MATCHING=1
```

Prepared consumer/retained receipts are required. Ignored evidence lives under
`conker/build/game-route-dispatcher-match/`: source screens, real compiled owner,
caller before/after, unchanged guards, first predicted ELF, native/guest/fault/
rebase/connected/control receipts and the installed audit. The historical view
is self-managed by the suite; do not wrap a nested view around it.

Shared padder/PC16 checks pass eleven per tools copy; both smoke checks and
consumer tools-check pass. Three task pairs are byte-identical and ASCII/AST
valid. Preserve all1251 pre-existing mirror dirty leaf hashes and mirror
HEADddbdd16, adding only three previously absent files (1254 dirty paths).
No mirror commit/reset, push, new Claude/debugger call, host-port/frozen Release
action or save/config change. Older source points/captures remain unchanged.

Scoped Graphify refresh:42657 nodes,82713 links,3991 communities. Retain42645
old IDs and uniquely relocate three duplicate UPDATE_LOG headings by their
line offsets. Preserve19398 nodes from2972 excluded-but-existing files, without
a full-scan purge. Tools remain outside the current graph corpus; no new Python
AST coverage is claimed. Before graph and ID audit remain ignored receipts.

Next recover **func_150896EC**, VA150896EC..15089BB0, ROMB6B9C..B7060,
**305 words /frame248**. Inspect its complete retail body and all direct caller
interfaces before choosing a return type or reconstructing either alternate
mode. This caller's two0/1 modes do not qualify the callee. Vector15088F30 and
the wider Game queue remain open; this function does not complete the goal.
