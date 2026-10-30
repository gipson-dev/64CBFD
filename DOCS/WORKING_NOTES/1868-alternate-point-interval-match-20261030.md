# 1868: Alternate actor-point interval and promoted mode interface

Verified 2026-10-30. `func_15146890` replaces its zero-return placeholder in
[`generated_173D40.c`](../../conker/src/game/generated_173D40.c).
All 56 body/slot words and three call relocations emit directly from C, with
the original 56-byte frame, S0 at SP24, RA at SP28, local array at SP44 and
incoming homes at SP60/64/68. There are no guards, inserted/omitted words,
frame adjustments, alignment words, profile/Makefile/layout changes or shared
header edits. Twelve raw/padded neighbors and all owner pools are preserved.

Actual linked recount: **3,945/5,506 (71.65%)** total,
**3,272/4,833 (67.70%)** Game, Init 492/492, Debugger 181/181, zero drift.
The active 75% goal needs **185** more to 4,130/5,506. The C inventory and
progress CSV remain unchanged.

## Behavior and recovered C interface

This routine shares the qualified `func_150EAF50` interval algorithm from
[Note 1867](1867-actor-point-interval-match-20261030.md), selecting point0x13
for mode1 and point0x17 for mode2. Other low-byte modes return zero without
pointer dereferences. It resolves the actor's matrix point into the output,
returns one for a null result, or captures `(x,y+10,z)`, initializes the result
and queries down to the live `y-50`. The last Y read follows initialization.

The original parameter-promotion interface matters. A normal u8-mode prototype
matched the isolated target but changed the already restored `func_15147040`.
The accepted definition uses K&R syntax with named, typed parameters
`f32 *position`, `u8 *actor`, `HeightResult71820 *result`, `u8 mode`. This preserves
the caller's default-promoted mode while narrowing it in the callee, and emits
the complete retail body. The existing empty redeclaration is retained.

`func_15147040` now passes `(HeightResult71820 *)0` instead of an integer zero
for the unprototyped result-pointer argument. The entire caller remains
byte-identical. No other caller/source file is changed. SDK `s32` is `long`,
while `u8` promotes to `int`; identical 32-bit widths do not make those C types
interchangeable. A later s32-mode prototype triggered IDO warning642. A compatible
int prototype changed the target's emission. Neither is adopted. An explicit
word-mode cast also failed the frame/body gates. No normalization hides these
rejected shapes.

## Qualification

Ignored artifacts live in `conker/build/game-point-interval-15146890-match/`.

- Raw body SHA-256:
  `9a81020167c5c9bff613c1a5fb8a1ddcefcc656b2eb87ff1abcf0ceb31a93b6d`.
  Three actual Make commands reproduce the qualified padded object. All
  selected/owner/actual-Make diagnostics are empty; all twelve neighbors and
  pools are fixed. The dead duplicate LWC1 at VA0x15146908 / offset0x78 is retained
  as body code, not padding: 55 of 56 body words are reachable.
- Guest: 3,136 cases / 9,408 executions cover all 256 low-byte modes, position/
  result aliases, helper mutations, float words and return payloads. Original,
  raw and padded programs agree on complete state and traces; independent
  public/visible-output references check every call, packet and result. There
  are 93 fired access prefixes (13 delay-slot cuts), 192 cases in three rebased
  layouts, and 35 private-home/alias cases. Raw controls cover the dead word too.
- Callers: the aligned full-ROM census finds eight direct JALs and no function
  pointers. Original windows in `func_15146A98`, `func_15146BF8`, `func_15146D60`,
  `func_15146E84`, `func_15147040`, `func_15147318`, `func_15147478` and
  `func_151475D8` each run 192 cases per program: 1,536 cases total. Matrix gates,
  low-byte loads in delay slots, parent-stack objects, six return-dependent
  routes and two null-result/ignored-return routes are checked. The ignored
  parents' invalid-context paths stop before later use of an unfilled position.
  Their portable context domain is1/2; complete parents are not claimed.
- Helpers: 864 cases execute 121 original initializer/query words with 88/89
  and 29/32 words covered. The resolver, entity check and lower-query services
  remain bounded; query statuses cover0/1/2. The current initializer remains
  non-matching and the query exact. Original-helper execution does not claim
  the current initializer is retail-identical; neither helper gains credit.
- Native32: 61,440 finite/alias cases per O0/O2/O3 profile pass trapping UBSan
  and eleven effective semantic controls. Four full-word integer mode carriers
  check narrowing, including signed/high-bit forms. Compile-time checks prove
  32-bit int/pointers, compatibility with an int-mode function pointer and
  incompatibility with a u8-mode prototype for the K&R definition. The harness
  uses the correct promoted int carrier. Native checks cover four position and
  three result layouts, initialized output effects and the late lower read.
  Private homes, portable fault order, FCSR and hardware NaN payloads are not
  claimed.
- Full image: production equals the independent complete-file prediction,
  ELF SHA-256 `a93cac0ec3ca52b364e0972e6fd2a81946dd9269728ad3732a8ba5bcede75878`.
  Exactly163 bytes change:162 target-code bytes and one target symbol-size byte.
  Metadata reorderings0, exclusions0. All6,055 other bodies, every function
  address and189,088 protected Game bytes across720 owners are fixed.
- Both tools copies run eight fresh canonical checks and their project-tools
  check. Production is followed by two fresh installed checks per copy; six
  unchanged semantic checks are explicitly reused via identical module/input/
  artifact fingerprints. The full16,968-file seal preserves all other inputs.

## Banking and continuation

Tools commit **55edb207b983a083a34f52c33f8e55fa07171dce** precedes the consumer's exact tools pin. No push occurs.
The independently dirty older mirror remains preserved. Root README changes
only its two aggregate exactness rows. Details remain in this note and the
documentation indexes. The scoped AST graph refresh validates the K&R signature,
all eight original call windows and the typed-null caller change while retaining
old nodes/relationships; it is not a full-corpus extraction.

Next private screen: **func_1500A7E8**. Existing parked candidates remain uncredited
until the complete source, ABI, semantic, owner, production and documentation gates.
