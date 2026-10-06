# Game Float Reference Packet Wrapper Direct Match

Date: 2026-10-06. Starting checkpoint: `66a5e069`.

**Game func_150C2804 now matches all 37 words / 148 bytes directly from C.**
Slot: 0x150C2804..0x150C2898, ROM 0xEFCB4..0xEFD48, frame 0x38.
The zero-return placeholder in [game_EF410.c](../../conker/src/game_EF410.c)
is replaced by a six-argument float-reference packet dispatcher. No new
word guards, compiler profile, assembly, header, symbol metadata or overflow.
The existing `-O2 -g3` profile emits the complete retail slot directly.

## Recovered Contract

The 28-byte local packet contains three float pointers at +0/+4/+8, captured
float parameters at +0xC/+0x10, a signed 16-bit delta at +0x14, bytes
5/6/3 at +0x16/+0x17/+0x18, and signed sentinel -1 at +0x19. The final two
alignment bytes remain untouched, as in retail; do not zero-initialize the
packet or copy coordinate values in place of pointers.

Global anchors `D_800A0280` and `D_800A0284` already have real data owners and
symbol aliases. Local externs suffice; neither data nor metadata changes.
The call is `func_15134908(&packet, 0, channel, context)`: channel narrows to
8 bits, context retains 32 bits, delta stores its low 16 bits.

The sole known retail caller in [50D80.s](../../conker/asm/50D80.s) passes
adjacent float addresses, a narrowed difference, an incoming channel and
zero context. It overwrites V0 with 1 immediately afterward. The selected
public return type is therefore void, not the old placeholder's invented
status return. The machine wrapper incidentally preserves the callee's V0;
tests check that instruction-level property without declaring a C return API.

Packet parameters retain neutral names: the downstream reciprocal use does
not establish a complete gameplay meaning for every field.

## Compiler Controls

[Packet driver](../../tools/experiments/game_effect_packet_wrapper_candidates.py)
freezes the recovered body and measures six source forms under four profiles:
**24 controls**, all with empty compiler diagnostics. Retained-order and
field-order forms emit 37 exact words under both O2/g3 and O1/g3. Plain O2
emits 34 words with 24 aligned slot differences; plain O1 emits 37 with 17.
Flags-first, globals-first and wide-delta forms lose the direct match.
A pointer-return form also matches, but is not needed by the known caller.
No profile override is installed. Receipts are ignored under
`conker/build/game-effect-packet-wrapper/`.

## Qualification

[Packet tests](../../tools/tests/test_game_effect_packet_wrapper_match.py)
compare retail, exact C and independently scheduled plain-O2 instructions:

- **2304 opaque-callback cases**: four pointer-word patterns, six delta
  words, eight channels, six contexts and both stack phases. Check all
  28 packet bytes, untouched padding, full non-stack memory, ordered call
  arguments, V0 and saved GPR/FPR/SP/RA state. All 37 retail words execute.
- **256 float-anchor cases**: +/-zero, retail constants, +/-infinity and
  quiet/signaling NaN payload bits, two stack phases and null/non-null
  callback results. Capture occurs before callback mutations. Guest load/
  store bit preservation is tested, not FCSR, exception or NaN-mode behavior.
- **288 connected-retail-callee cases**: allocation success/null, delta,
  channel, context, stack phase and callback mutation. Execute all 37 wrapper
  words and all 50 original callee words, comparing every non-stack byte.
- **14400 native 32-bit cases**: packet size/offsets, initialized fields,
  valid coordinate pointers, narrowing, call count and callback mutations.
  Native tests do not inspect indeterminate padding or signaling NaNs.
- Negative controls detect the old zero-return stub, wrong flags and
  coordinate-value copies. Production checks bind the exact source body,
  all linked words, float-anchor instructions and absence of target guards.

Six pre-install tests passed in 3.125 seconds, no skips. All **92 combined
post-link tests pass in 233.716 seconds**, no skips: eight packet tests plus
the preceding 84 linked-record, random-range, sound, edge/root/parent/visitor
regressions. After adding the live callee equality assertion, all eight
packet tests pass again in **6.375 seconds**, no skips.
No shared guest oracle changes.

### Callee Audit And Qualification Boundary

Connected qualification executes the **original retail**
[func_15134908.s](../../conker/asm/nonmatchings/game_161520/func_15134908.s),
whose complete 50 words also match the unchanged production callee.
The C body in [game_161520.c](../../conker/src/game_161520.c) already implements
allocation, packet mutation/copy and coordinate/reciprocal output. A leftover
placeholder comment caused the preceding handoff to misclassify it. Live
source and ELF inspection supersede that claim in Note 1028: **50/50 exact,
frame 0x28, zero differences**, unchanged by this pass. Production tests bind
that equality; the modeled connected instruction path is therefore also the
current production instruction path.
Allocator and copy callbacks are bounded models, not complete helper engines.

Retail allocates with `(42, context, 64, 1, channel, 1)`, returns null on
failure, ORs bit 1 into packet flags, and copies all 28 bytes to result+0x10.
It then reads through the three copied float pointers, storing coordinates
at result+0x2C/+0x30/+0x34, the reciprocal of twice captured parameter0 at
result+0x38, and zero at result+0x3C. Mutation cases distinguish captured
parameter values from coordinate pointers read later. Opaque invalid/null
pointer words are not claimed valid for successful connected/native calls.
Full production helper-chain, gameplay and FCSR acceptance remain separate.

## Linked Audit

Before receipt equals the preceding **6059-slot** checkpoint. All names,
addresses and lengths survive relinking; **only func_150C2804 changes**.
All other 6058 slots remain byte-for-byte identical. Target SHA-256:
`a1b92f8ea248e125f4f7f1b32d6d481d941baa246151a9ca6227d67f52be0267`.
Before/after/audit/behavior/connected receipts are ignored under
`conker/build/game-effect-packet-wrapper-test/`.

Init 164048 bytes, Init data 17376 bytes, Debugger 19800 bytes and Game data
189088 bytes remain unchanged. All **720 Game-data owners** remain exact,
zero differing bytes or owners. All **10646 guard rows** remain identical
and ordered. Build/progress/match-progress and project tool checks pass;
the existing duplicate generated_12D630 recipe warning remains.
No sibling source/build/save/frozen Release change or push.

Whitespace and documentation-link checks pass: **3085 relative links across
twelve documents**, zero broken. No generated output is committed.

Fresh measurements: total **3311/5462 exact (60.62%)**, Game **2638/4789
(55.08%)**, Init **492/492**, Debugger **181/181**, zero address drift,
**2151** different Game C functions. Converted function/byte totals stay
unchanged. README updates are aggregate-only; recovery details live here.

## Reproduction And Next

```sh
python3 -m tools.experiments.game_effect_packet_wrapper_candidates
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_effect_packet_wrapper_match -v -f
make tools-check
git diff --check
```

Wait for relinking before linked-image tests. Next inspect **39-word
func_150D26F0**, still a zero-return placeholder in
[generated_FFBA0.c](../../conker/src/game/generated_FFBA0.c), against its
[retail assembly](../../conker/asm/FFBA0.s). The already-exact packet callee
needs no conversion. The edge helper's 102-difference frame/lifetime boundary
remains open in [Note 1027](1027-game-graph-edge-crossing-scope-audit-20261006.md).
The full Game matching goal remains active. No push.
