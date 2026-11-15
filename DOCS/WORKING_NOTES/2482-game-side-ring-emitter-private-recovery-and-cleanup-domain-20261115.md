# 2482 - Private side-ring emitter recovery and cleanup domain

`func_1519F7F0` has a complete private semantic C candidate and independent
guest/caller evidence. It is **not installed, normalized, or credited**.
The production source remains its existing placeholder. Fresh actual-ELF
recount remains **4,511 / 5,514 (81.81%)** total, **3,838 / 4,841 (79.28%)**
Game, Init **492/492**, Debugger **181/181**, zero address drift and **1,003**
different. The 85% threshold remains 4,687: **176 more matches** are needed.

Baseline consumer `ea719324eb3d92fd32fddc7d51ab736eb969be49`, baseline tools
`50727d614d7925e8692e99834713557ff80b6666`. New screening tools commit:
`27df32c3b5ceead58f10455497f745ee76750e9b`. The **880-input** immutable packet is retained under
`conker/build/game-side-ring-emitter-1519f7f0-private/production-baseline/`.
All inputs are rehashed before/after compilation and after the focused suite.

## Complete interface and behavior

Owner `conker/src/game/generated_1CC440.c`; original `conker/asm/1CC440.s`.
Retail VA `0x1519F7F0..0x1519FE6C`, code-image offsets
`0x1CCCA0..0x1CD31C`: **415 words / 1,660 bytes**, frame **0x118**.
Recover `s32 func_1519F7F0(SideEmitter1519F7F0 *effect)`. The complete original
100-word `func_15147740` dispatches it through **slot 5 of D_8008A23C**,
using the second callback selector at effect +0x30. The entire 72-byte table
is checked against retail and the live ELF. This is not a complete computed-call
or asset-ROM census.

Capture the effect's +0x98 payload and +0x94 entry base, then its owner's
actor. Gate on actor word zero, actor +0x1D4 presence and matching identity
bytes. Return zero on a failed gate. Use effect +0x10 as the query point;
the published +0x54 point is a different field.

If flag 4 is clear, query and seed the payload's previous point, then set flag
4 from the live flags. An initialized object queries again on entry. Query
success updates the captured actor's X/Z reference values, measures the three
coordinate deltas and adds distance times payload scale to retained progress.
Emit only while **1.0f < progress**, preserving unordered/NaN behavior.

Compute transverse velocity with mode-dependent sign, keeping unary negation
and both multiplications in retail order. When smoothing is enabled, the
affected earlier entry is **tail minus two**, after both independent negative
wrap checks. Interpolate position, weight and elapsed time across emissions.
The entry stride is **0x24**; preserve signed head/tail/count bytes and the
unsigned capacity byte, including low-byte writes and subsequent reloads.

Each entry receives the two velocity words, X/Z, lifetime, phase, alpha, delay,
light and tag. RNG is declared **s32** and explicitly cast to **u32** for the
unsigned remainder. Reload payload counter and both random-step bytes after
the RNG provider; reload entry velocities before moving X/Z. The floor query
uses the captured actor's live height or Y, then **(height + 100) - 200** with
both binary32 operations retained. The full output result is **36 bytes**.
Only accepted entries advance the live ring. Finish by copying interpolated
position and remaining elapsed time back to the captured payload.

## Two state-domain boundaries

The retail no-motion path loads an **uninitialized private inverse-length
home**. Ordinarily retained progress is at most one on this path: construction
starts it at zero and each completed emission loop reduces it to at most one.
The candidate preserves the uninitialized local. It does not initialize it to
zero. Injected progress greater than one with zero/sub-threshold motion is
excluded from this valid-state screen; it needs a separate guest-private
provenance treatment before any broader equivalence claim. No portable C
claim is made for reading an uninitialized float.

On a forced initialized query miss, retail calls `func_1519F48C`, **reloads**
payload.state after cleanup, constructs an eight-byte transition and calls
`func_151491F4(300, -1, 11, 0, 6, 8, 255, 0)`. Copy all eight bytes to created
+0x28 on success; reload effect.mode after the factory/copy before selecting
owner second or fourth output.

The complete actual cleanup clears payload.state. Therefore a forced miss
followed by the real cleanup attempts an unmapped store at **0x5C** (mode 6)
or **0x64** (mode 7). Eight guest observations cover both modes, allocation
outcomes and instruction streams; all stop before that store is performed.
This is the local engine's unmapped-memory check, **not hardware fault/FCSR
emulation or portable C fault equivalence**. Do not cache the old owner pointer
to hide this retail behavior.

Under valid, disjoint ordinary storage with no asynchronous mutation, the
actual query's only failure gate is the same actor +0x1D4 check already passed
by the emitter. Its heading/sample helpers are read-only and its output is
the separate effect point. This explains why the cleanup transition is outside
that ordinary real-helper domain. Opaque-provider miss cases are nevertheless
screened separately with a valid retained owner, and real-cleanup low-address
behavior is explicitly retained as guest evidence. This inference does not
establish arbitrary-alias or concurrent-observer behavior.

## Measured screen and remaining differences

The normal O2/g3 complete-owner compile is clean. Raw C is **416 words**, frame
**0x110**, SHA-256
`ce398de9691b2d23a90fc7049aad3ce67c9c791b291154beff4c1ce8406fa84c`.
All **15 relocation bindings**, all **38 copied neighboring functions**, and
the raw owner's normalized data pools are pinned/unchanged. Four local-order
or byte-stride alternatives also emit 416 words; none is selected or credited.
No profile, shared header, production guard or source body is changed.

Private locations are relative to incoming SP:

| Exposed or retained local | Raw candidate | Retail |
| --- | --- | --- |
| Eight-byte transition | -0x30 | -0x2C |
| Twelve-byte floor-query point | -0x80 | -0x8C |

The transition initializes only its owner word and one mode byte. Its other
**three bytes stay untouched**. Across the corpus, **27 copied transition
packets differ between raw and retail** because those bytes come from different
incoming stack locations. Each stream independently matches its own expected
byte provenance. They are deliberately **not** called equivalent. Fix the
exposed homes with a justified source layout or proved normalization before
adoption; do not zero or discard the bytes.

Fresh focused checks, in the primary tools tree and an isolated overlay of
the dirty sibling tools checkout:

- **568 independent-model cases per stream**, including gate/initialization,
  ring wrap, smoothing, miss/allocation, provider mutations, signed counter
  boundaries, binary32 special values, bounds and retained padding.
- Six effective corrupted-instruction controls: identity byte, unsigned RNG
  operation, duration source, query span, transition home and tail cursor.
- **2,048 connected real-query cases per stream**, all 256 headings, both
  modes, both initialization states and moving/fallback query paths. The
  complete 94-word query and 7/27-word heading/sample helpers are checked
  against the actual ELF before execution.
- **32 original-dispatcher cases per stream**, including all three failed
  entry gates, modes, initialization states and incoming SP phases. Connected
  cases also exercise actual query success into the emitter loop.
- Eight original-cleanup unmapped-store observations described above.
- All 880 frozen production inputs remain identical. The dirty sibling's
  HEAD/status fingerprint and its **2,434 existing dirty paths** are unchanged;
  the five task files are tested through an ignored overlay.

Guest visitation is **407/415** retail words and **408/416** raw words. No
whole-CFG proof, ordered FP/FCSR equivalence, native32 acceptance, all-alias
claim, raw fault-scratch identity, production padding, actual-Make shadow,
strict full-image installation, or new production C match is claimed.

Reproduce the current private screen from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_side_ring_emitter_1519f7f0_recovery -v
```

The committed manifest and recovery module are authoritative; older disposable
stage setup scripts and alternative sources are historical probes.

## Next work

Continue this target. Recover the retail stack/local declaration shape and the
one-word instruction-count difference. Keep all exposed unknown-byte provenance
and the cleanup owner reload. Then establish complete checked transformations,
ordered FP behavior and remaining state/alias assumptions; add meaningful native
checks over the defined input domain. Qualify both padders, actual Make, strict
whole-image and production checks before installation and credit. Recount and
update aggregate README rows only after an actual new match.

Production ELF remains
`29d206f55163699565107bebaf610b9c9a383ddef1ca7292fd6370400e6fcd60`.
Source, guards, linked objects, code image, progress CSV and root README remain
at the accepted prior checkpoint. The host sibling has no applicable source
checkout here; Release artifacts and real saves are untouched.
