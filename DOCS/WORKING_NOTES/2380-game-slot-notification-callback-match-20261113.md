# Game slot-notification callback match

Date: 2026-11-13. `func_15156028` replaces the zero-return placeholder in
`generated_182C30.c`. The complete 88-word body spans VA
`0x15156028..0x15156188`, ROM `0x1834D8..0x183638`, followed by two alignment
words. It releases a matching record for event 0 and updates its actor slot
for event `0x2D`. Signed division by `0x32C` truncates toward zero, including
non-aligned values immediately below the actor-table base.

The source uses the existing `struct127 D_800CC2D0[26]` declaration and the
dispatcher-compatible `void (*)(void *, s32, u8)` callback signature. Its
raw compiler output has the retail 88-word extent but only 37 same-position
words. **51 expected-word guards**, seven involving relocation bindings,
restore retail's register allocation, instruction schedule and branch layout.
No instruction is inserted or omitted. Both padders reproduce the complete
original payload and bindings; the eight other owner functions stay fixed.
The raw candidate computes the second quotient later than retail on some
paths, so private HI/LO state and fault timing should not be conflated with
the guarded instruction stream. See [Note 2370](2370-game-slot-notification-private-screen-20261113.md)
for the earlier uncredited screen.

The live retail descriptor table contains the target at `0x8008C504`, offset
`0x1C` of type 80 in `D_8008B4A8` with 52-byte entries. The current linked
`func_15169070` range dispatcher and `func_15169040` wrapper match retail;
the matching actor-swap packet builder `func_15146508` and removal-packet
builder `func_151695F0` were also executed into the target. The original
assembly list/direct dispatchers `func_15169260` and `func_1516944C` were
executed as additional caller contexts, but their current C placeholders
remain unmatched and receive no credit here. Removal cases also execute the
retail `func_1516972C` release helper with bookkeeping and destructor as
bounded providers.

Tools commits `5393d0c` and `4b0b4d2` provide reproducible checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_slot_notification_15156028_match -v
```

The suite covers 6,144 cases per retail/raw/padded body, another 192 signed
boundary cases and every opcode byte, input/record aliases and caller-stack
inputs. Connected checks include 160 actor swaps, 40 removal packets, 40
removal paths through the original release helper, and 108 original list or
direct dispatch cases per body. The guest fault model compares 1,416
retail/padded memory-access prefixes. Native 32-bit builds pass 2,048 cases
per profile at O0/O2/O3 with trapping UBSan and eight effective semantic
controls. Both padders reject 102 individually corrupted guards, and 12 GNU
links exercise four symbol layouts. These bounded models do not establish
portable fault semantics, hardware behavior or live gameplay.

The prior `test_game_node_range_walker_15169070_match` suite was checked on
the unmodified baseline and could not start because its saved `conker/Makefile`
fingerprint is stale. It is not reported as a fresh passing regression; the
connected tests above independently execute the current matched dispatcher.
All eight checks passed after installation in the mounted tools environment
and through an isolated standalone-checkout overlay. The overlay uses mounted
fallbacks for unavailable modules, so it is a hybrid result rather than a
complete standalone checkout run. Its 2,434 pre-existing dirty paths remain
untouched.

The normal production build passed. Strict comparison with the frozen prior
ELF accounts for 244 changed bytes, with **zero exclusions**; only this
function changes among 6,051 functions, all addresses remain fixed, and all
189,088 protected Game-data bytes match. Of 698 fingerprinted linked source
objects only the intended owner changed; the separately frozen debugger
object remained byte-identical. Conversion CSV bytes are unchanged.

Fresh production recount: Game **3,765 / 4,843 (77.74%)**, total
**4,438 / 5,516 (80.46%)**, zero drift; **110** more Game matches are needed
to reach 80% at the current denominator. The host port was not modified or
runtime-tested for this decompilation match.

The scoped Graphify refresh retained all 60,036 prior node IDs, producing
60,036 nodes and 113,306 links without reclustering. Its fail-closed path
retained 31,816 existing nodes; this was not a full-corpus re-extraction.
