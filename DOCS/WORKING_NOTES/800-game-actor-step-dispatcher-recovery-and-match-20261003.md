# Game Actor Step Dispatcher Recovery And Match

Date: 2026-10-03. Baseline: `8bf34ba`; Init experiment checkpoint: `52aec99`.

## Result

`func_1507C22C` in `conker/src/game/generated_A9260.c` replaces its zero-return
placeholder with the recovered actor scan and conditional update dispatch.
All 62 words / 248 bytes now match retail. Seven stale-checked, relocation-aware
guards reorder only the independent opening address-setup block. No compiler
profile, padding, insertion, omission, or shared header change is added.

This is semantic recovery and a new byte match of an already C-counted row,
not an assembly-to-C ownership conversion. C counts/bytes remain unchanged;
exact-C totals rise by one, and different-C totals fall by one.

The connected `func_1507BDB0` updater and `func_150229E4` predicate remain
unrecovered placeholders. Matching their caller does not make those callees
functional or establish gameplay behavior. They are the next connected work,
not hidden behind a completed-system claim.

## Retail Contract

The dispatcher scans exactly 25 `0x32C`-byte actor records, starting at
`D_800CC2D0` and stopping before `D_800D121C`. The stop address is 25 records
after the start; this is not the entire 26-element shared declaration and is
not controlled by the dimension refresh routine's `D_8008FD8C` count.

For each record, in ascending order:

1. Require nonzero word `0x00`, and clear flag `0x200` in word `0x25C`.
2. If mode is nonzero, require byte `0x05` to equal four. The mode is passed
   through unchanged, not converted to a boolean for the eventual call.
3. Bypass the predicate if `D_800C3638` is zero or the first addressed byte at
   `D_800C3654` is nonzero; otherwise require `func_150229E4(actor)` nonzero.
4. After that predicate returns, require pointer `0x2D0` and byte `0x2FA`
   nonzero. A callback can change either field before these checks.
5. Call `func_1507BDB0` with nested pointer, float-step bits from `0x48`, the
   actor pointer, and the original mode. Ignore its result and advance.

`D_800C3654` is word-declared in the existing shared header, but retail uses
`lbu` at its first address. The local byte view preserves that access instead
of testing the complete word or changing unrelated consumers' declarations.
Global gates and subsequent actors are read afresh as the scan progresses.
The dispatcher itself performs no actor stores; its callees may mutate state.

## Argument Representation And Preserved Callee

The updater begins with `mtc1 a1,f12`; both known retail callers supply the
float's raw word in a1. Its complete original body has 287 words and uses
additional actor/nested-state contracts that are not yet recovered.

An initial typed placeholder definition caused IDO to spill all four incoming
arguments into the caller's home area. That unintended placeholder change was
removed. The final updater definition remains the original untyped zero-return
body, and the recovered dispatcher uses a read-only `s32` view of actor `0x48`
to pass the original word without default float-to-double argument promotion.
This compiler-specific word view is checked against the actual emitted guest
`lw a1,0x48(s0)`. Host fixtures use the existing `-fno-strict-aliasing` profile;
no general strict-aliasing portability guarantee is made.

A union transfer was also tested, but IDO emitted a temporary stack spill,
expanded the frame/body, and correctly failed the retail-span guard. It is not
the final source. The final caller retains the `0x30` frame and original
register/argument lifetimes; the updater retains its original three-word
zero-return body plus padding, with no argument-home stores added.

## Scheduling Guard Proof

The unguarded caller already emits the complete retail control flow, stack
frame, saved registers, calls, loop prefetch, branch-likely delay updates, and
argument loads. Only offsets `0x28..0x40` differ, seven contiguous words in
the opening address setup.

Both schedules contain the same four LUI/ADDIU address pairs:

| Register | Address |
| --- | --- |
| s0 | `D_800CC2D0` |
| s2 | `D_800D121C` |
| s4 | `D_800C3638` |
| s5 | `D_800C3654` |

Every high half precedes its own low half. Neither schedule accesses memory,
branches, or calls within this block. The guard test compares the complete
instruction-plus-relocation multiset, executes both setup schedules from the
same seeded register state, and requires identical complete register output.
All other words are unchanged; no loop or arithmetic behavior is normalized.
The project's stale-word/relocation checks also pass on actual IDO output.

An inline stop-address expression changes the saved-register allocation;
the final named endpoint local gives the smaller independent-schedule proof.
No broad source/profile sweep is needed for this recovery.

| Measurement | Value |
| --- | --- |
| VMA slot | `0x1507C22C..0x1507C324` |
| ROM slot | `0xA96DC..0xA97D4` |
| Body / slot | 62 words / 248 bytes, no padding |
| Unguarded differences | Seven address-setup scheduling words |
| Linked differences | Zero |
| Relocated unguarded SHA-256 | `ec04b65f456b1cbfe168042cec6b7ed2ed030147b033b8e4e69aa0b9f98d5406` |
| Linked / retail SHA-256 | `99c75a16c81b369df422b2c9d038c4bf0b58bc24b57b353b856d8828b6a44bf1` |

## Verification

Ten tests in `tools/tests/test_game_actor_step_dispatcher.py` compile the
actual production body with the existing freestanding 32-bit actor layout.
They cover offsets; all 25 records and exclusion of record 25; order/repeats;
192 gate combinations; null/disabled nested states; byte-only overrides;
predicate changes to current state/step/enable; updater changes to global
gates or the next actor; signed active values and nonboolean modes; other
flag bits; quiet-NaN/signed-zero argument payloads; unchanged caller-owned
records; and the complete independent-schedule guard proof. Callees are
controlled stubs, not recovered implementations or retail execution.

All ten new tests, forty focused dispatcher/copy-clamp/dimension tests, and
all 532 tool tests pass. The final raw-word argument form passes a further full
532-test rerun (84.079 seconds), ten-test dispatcher rerun, and build/matcher
check. Project tool checks and
`git diff --check` pass. The broad rebuild triggered by the shared guard CSV
completed successfully; known recipe/source warnings remain.

Structured CSV comparison preserves all 10,505 prior guard rows unchanged;
only the seven dispatcher scheduling rows are added.

Independent final linked-ELF extraction confirms:

- Dispatcher: all 248 bytes retail-exact, hash above.
- `func_1507C324`: all 76 bytes exact, retained hash
  `4f58821a6f1badee3a246fd97e1d128ae0b5ac03df33ef508633478fc2aedc85`.
- `func_1507C370`: all 112 bytes exact, hash
  `f76ebf3e5c54848c244a826c349a9b156683e93f088e363b88d3e31ccab607af`.
- `func_1507C3E0`: unchanged 1,280-byte hash
  `d81006ca7298e61f20e168b71d899205a5fbb50c8661aec1abb59a74a3e64cbb`,
  still 312 differing word positions.
- `func_1507BDB0`: preserved zero-return placeholder and padding, hash
  `450a7a8797c5a58afdae18fa474c3bbf9ced0ceaeb7f017d2a708732fd2b4f95`.
- Whole `.init`: 164,048 bytes exact, SHA-256
  `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf`.
- Whole `.init_data`: 17,376 bytes exact, SHA-256
  `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239`.

No gameplay, MIPS runtime, predicate/updater correctness, host-port build, or
Release acceptance is claimed.

## Progress And Next

Fresh matching reports total 3,271/5,463 (59.88%), Game 2,598/4,790 (54.24%),
Init 492/492, Debugger 181/181, zero address drift, and 2,192 different C rows,
all Game. C ownership counts/bytes do not change. README changes only these
aggregate match rows; function history stays here and in the update log.

Next recover `func_1507BDB0` together with its predicate/callee interfaces,
including its standalone non-actor caller. Preserve the now-exact dispatcher
while replacing the updater placeholder and qualifying its float/state
behavior. Do not describe this caller match as finishing that connected system.
Init's new failed scheduling experiment is banked separately in
[Note 799](799-init-bitmap-volatile-store-scheduling-trial-20261003.md).
