# Game height emitter match

Date: 2026-11-14. `func_150E971C` replaces the zero-return placeholder in
`conker/src/game/generated_113D60.c`. Its 91-word body at
`0x150E971C..0x150E9888` now matches retail after 24 expected-word guards;
67 words emit directly from C at their retail positions. Two alignment words
follow the body. The guards restore the retail stack frame, local offsets and
descriptor-store schedule.

The callback advances the actor through `func_151337C0`, then tests its
height against an embedded threshold. When it is below that threshold and
the low five flag bits equal 10, it constructs an effect descriptor, draws
two random values and calls `func_1513C73C`. The integer random result is
captured before evaluating the actor fields used in the final call. Retail's
`D_800898B0` table supplies this callback in slot 17; the bounded
`func_151321D0` dispatch window passes the actor and examines the result.

The constructor copies 40 bytes, including eight bytes retail leaves
uninitialized. The extra four bytes of local C storage and the stack guards
preserve the observed retail descriptor position. As shown in
[Notes 2402](2402-game-height-emitter-private-screen-20261113.md),
[2403](2403-game-height-emitter-qualified-screen-20261114.md) and
[2404](2404-game-height-emitter-frame-screen-20261114.md), this behavior is
significant in the guest; native portability of indeterminate stack bytes is
not established.

The qualification tools are in commits `1bcc62d`, `f6bf7fc` and `73b1cb1`.
Before installation, the independent guest reference checked 160 cases per
stream and rejected three altered-instruction controls. Connected tests used
the 53-word retail movement helper in 72 cases and the original dispatch
window in 48. Native32 tested 24 cases at each of O0, O2 and O3 with both
alias modes and trapping UBSan; it rejected an unsequenced C variant and three
additional controls. Both padders and 12 GNU links across four layouts agreed.
The retail and guarded streams agreed over 142 modeled fault prefixes and
195 deliberate actor/private-stack overlaps; two overlap cases produced
modeled assertions in at least one stream. These bounded tests do not prove
unrestricted C aliasing, FCSR exception behavior, complete caller execution
or gameplay.

The normal production Make build and independent whole-image prediction
passed with 270 changed bytes and zero exclusions. All 6,051 function
addresses and all 189,088 protected Game-data bytes remained fixed. Of 698
frozen linked objects, only `generated_113D60.c.o` changed; its 28 neighboring
functions, the conversion CSV and earlier guard rows remain unchanged.
Mounted and isolated sibling-overlay installed tests passed, as did
`make tools-check`; the separate sibling checkout's prior dirty paths were
preserved. The pre-install qualification screen is intentionally fingerprinted
to its original inputs; the installed checks can be run with:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_height_emitter_150e971c_installed -v
```

The scoped Graphify refresh retained all 60,097 prior node IDs. It was
fail-closed and retained excluded existing nodes; it was not a full-corpus
re-extraction.

Fresh production recount: Game **3,785 / 4,843 (78.15%)**, total
**4,458 / 5,516 (80.82%)**, zero drift. **90** more Game matches are needed
for 80% at the current denominator.
