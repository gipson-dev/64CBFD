# Game line-camera consumer stack screen

Date: 2026-11-13. This is a private screen of `func_1512DEA4`, not a
production match. Its retail body has 166 words at
`0x1512DEA4..0x1512E13C`; the following word is slot alignment. The function
updates a camera from the inline line record restored in Note 2388. Its
`func_151283B8` caller dispatches it for camera mode `0x800000`.

The routine calculates the distance between the line endpoint and the camera,
uses the normalized line direction to calculate a target, and offsets that
target according to the line kind. When `camera+0x23C` is nonzero it copies
the target into the camera position and sets two smoothing fields to 40. When
the flag is zero, it invokes `func_150495B0` five times to smooth the rate,
damping, and three coordinates. These descriptions follow the retail body;
they do not establish complete caller or gameplay behavior.

Kinds 0 through 3 each assign the two horizontal offsets. For all other kind
bytes the retail default branch assigns neither: it reads the words already at
entry-stack offsets `-0x14` and `-0x0C`. A bounded retail guest screen varies
those words and observes four different output pairs for each of kinds 4 and
255. That is an observed guest-machine dependency, not proof that an ordinary
ISO C read of an uninitialized local is defined. The original assignment at
`0x151297DC` in `func_15128CB0` copies the word at loaded-record offset `0x18`
to `camera+0x718`; the initializer copies its low byte to the line kind. No
range check appears in that assignment. The data source and all other routes
have not been qualified sufficiently to restrict kinds to 0–3.

Six complete-owner C shapes are retained in ignored
`conker/build/game-line-consumer-1512dea4-screen/`. They preserve the existing
initializer, its pools and compiler diagnostics, and produce 171 or 175 words
with a `0x60` frame rather than retail's 166-word body and `0x68` frame. Their
default locals are uninitialized, so **none is installable**. In the immediate
branch, all six agree with retail for the 32 tested cases with kinds 0–3, and
all disagree for the 16 tested kind-4/255 cases. A separate 12-case screen
connects the actual 54-word retail smoothing helper: all candidates agree for
the eight tested kind-0–3 cases and disagree for all four tested kind-4/255
cases; retail executes five helper calls in every case. These are bounded
fixtures, not exhaustive aliases, FPU edge cases, caller-stack, fault-order or
native-portable-C qualification.

All six orders of the three local declarations still produce the `0x60`
frame and 171 words. They place their three stack loads at entry-relative
offsets `-0x14`, `-0x18` and `-0x1C` in varying order; retail's three are
`-0x14`, `-0x10` and `-0x0C`. Source and helper inputs are pinned by the
manifest in tools commit `17ea050`. The reproducible screen is:

```sh
python3 -m unittest tools.tests.test_game_line_consumer_1512dea4_screen -v
```

The focused checks passed in mounted tools and an isolated sibling overlay
that uses mounted fallback modules. `make tools-check` passed. The sibling's
pre-existing dirty work was preserved. Production source and matching counts
are unchanged: Game **3,774 / 4,843 (77.93%)**, with **101** more matches to
80% at the current denominator. Continue by establishing the source record's
reachable kind domain and caller-stack requirements, or investigate another
candidate while those questions remain open. Do not replace the placeholder
or apply guards merely to conceal this unresolved default case.
