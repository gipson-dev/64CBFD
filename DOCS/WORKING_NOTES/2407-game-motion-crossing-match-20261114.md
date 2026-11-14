# Game motion-crossing callback match

Date: 2026-11-14. `func_150E6230` replaces the zero-return placeholder in
`conker/src/game/generated_113480.c`. Its 92-word body at
`0x150E6230..0x150E63A0`, ROM `0x1136E0..0x113850`, now matches retail.
The compiler emits 90 words, with 50 at their retail positions; 29
expected-word guard rows restore the retail stack and instruction schedule,
including two inserted instructions.

The callback optionally compares the sign of a dot product with an
actor-embedded value and, when it differs, dispatches the configured effect
callback. The callback result is narrowed to a signed byte. It then advances
the actor's three position components using its velocity, speed and live frame
delta, and returns the resulting status. Retail's `D_80089CB8` table selects
this function at slot 15; the bounded `func_1513CFE4` window passes the actor
and examines its return. An aligned Game scan found no direct JAL and found
one literal table reference at ROM `0x22E7B4`; computed and external calls are
outside that scan.

Tools commits `a3cc063` and `dd3b43b` retain the qualification and installed
checks. The independent guest model covers 384 cases per stream, including
modeled helper mutations and signed callback returns, and rejects three
altered-instruction controls. Connected screens use the original 13-word dot
helper in 96 cases and the original caller window in 192. Native32 checks
192 cases at each of O0, O2 and O3 with both alias modes and trapping UBSan,
and rejects three source controls. These callback screens use selector -1 or
the valid table slot 0; arbitrary selector values are not qualified.

Both padders and 12 GNU links across four layouts agree. Retail and guarded
streams agree over 153 modeled fault prefixes and 195 deliberate
actor/private-stack overlaps; 22 overlap cases produced modeled assertion
exceptions in at least one stream. The raw C object differed in 116 overlap
cases. These are bounded tests, not a proof of unrestricted ISO C aliasing,
FCSR exception behavior, complete caller execution or gameplay.

The normal production Make build and independent whole-image prediction
passed with 270 changed bytes and zero exclusions. All 6,051 function
addresses and all 189,088 protected Game-data bytes remained fixed. Of 698
frozen linked objects, only `generated_113480.c.o` changed; its four
neighboring functions, the conversion CSV and earlier guard rows remain
unchanged. Mounted and isolated sibling-overlay installed checks passed, as
did `make tools-check`; the separate sibling checkout's prior dirty paths were
preserved. The pre-install suite is fingerprinted to its original inputs;
the installed checks can be run with:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_motion_crossing_150e6230_installed -v
```

The scoped Graphify refresh retained all 60,101 prior node IDs. It was
fail-closed and retained excluded existing nodes; it was not a full-corpus
re-extraction.

Fresh production recount: Game **3,786 / 4,843 (78.17%)**, total
**4,459 / 5,516 (80.84%)**, zero drift. **89** more Game matches are needed
for 80% at the current denominator.
