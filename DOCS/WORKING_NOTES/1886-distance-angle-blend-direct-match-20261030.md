ï»¿# 1886 - Distance-triggered angle blend direct C match - 2026-10-30

`func_1512C068` replaces its zero-return placeholder in
`conker/src/game/generated_157840.c`. All **58 words / 232 bytes** and both call
bindings match directly under the existing O2/g3 profile. There are no new
guards, inserted/omitted instructions, compiler-profile changes or shared-header
changes. The 24-byte frame saves RA at `SP+20` and the live actor home at `SP+24`.

Tools commit: `7666891386bdefbb5614b67623596a75f09880ff`. Ignored evidence:
`conker/build/game-distance-angle-blend-1512C068-match/`.

## Recovered behavior and declaration boundary

The actor is required; retail has no null-actor gate. An angle at actor `+0x390`
strictly below 180 selects direction +2; all other ordered/unordered comparisons
select -2. Types exactly `0x80` or `0x40` skip the distance calculation.

Other types compute single-precision X/Z deltas from fields `2F8-2BC` and
`300-2C4`, square each delta, add the rounded products, take `sqrt.s`, and store
the planar distance at `+0x370`. The shared SDK still names that four-byte area
`pad370`; a local float access preserves the measured store without a broad
shared-structure edit.

A distance strictly below 42 writes `384 = 37C - 45 * direction`, clears blend
phase `5CC`, calls `func_15123A54`, reloads the actor home, and sets bit 2 in that
actor's live `240` word. Every route then calls the already matched
`func_1512C150` updater. Provider mutations may therefore affect the bit update
and final updater target. The routine returns void; original callers ignore the
result.

The current provider C remains a zero-return placeholder declared `s32
func_15123A54()`. This owner uses a compatible `s32` return declaration with its
observed actor argument and ignores the result. Its eventual recovered return
contract is not inferred from the placeholder. The provider is not converted or
credited here. Existing caller and shared-header declarations are unchanged.

Word 14 is retail's unreachable duplicate `mtc1` setup, also emitted naturally
by IDO. It remains byte-exact. Only **57 of 58 target words** are reachable; the
branch-likely delay setup at word 9 and the duplicate word 14 are distinguished.

## Qualification evidence

- **1,824 guest cases / 5,472 executions** compare original, raw C and padded
  bodies, complete RAM/registers, accesses, call observations and fault context.
  They exercise all 57 reachable target words, both exact type exclusions,
  heading boundaries, signed zeros, infinities/NaN headings, near/exact/far
  distance thresholds, cancellation, subnormals, phase states and full flag words.
- The original **44-word updater** and **24-word one-fold angle helper** are
  connected. Their reachable coverage is 42 and 23 words respectively, preserving
  their known unreachable duplicates. Their C implementations are also used in
  native validation, not replaced with fresh simplified production providers.
- The original **839-word orientation provider** is present on selected runs.
  Its nonzero `D_800C3671` route executes 16 words: captured field `374`, byte
  clear at `600`, float copy at `604`, and return. Other orientation routes remain
  outside this bounded qualification. Scripted provider variants separately
  mutate angle/phase/flags and redirect the incoming actor home to a second actor.
- **105 access cuts**, including ten delay-slot cuts, compare literal prefixes
  and fault context across all three identical instruction streams. Twelve
  rebase cases use three independent root/callee layouts across address boundaries.
  Rebased updater behavior is bounded; retail-address tests connect the originals.
- The aligned ROM census finds only JALs at **`0x150484` and `0x1504B0`**, and no
  aligned literal pointer words. **256 cases** execute original 19-word and
  eight-word windows inside `func_15122C5C`, ending at `0x15123020`. All 19 distinct
  caller words execute, including the live byte gate for the optional second
  invocation. Adjacent services are bounded. The parent C remains a placeholder;
  full-parent execution and matching are not claimed.
- Native SDK32 **O0/O2/O3 each pass 147,456 cases** with trapping UBSan, real
  updater and angle-helper C, ten heading representations, twelve coordinate
  patterns, six actor types, four phases and provider mutation. Every actor byte
  is checked. Native reference square root uses SSE double precision followed
  by float rounding; the selected single-precision service uses `sqrtss`.
- **15 effective controls** successfully compile and fail semantically through
  IDO/guest and native execution: heading strictness, direction, type exclusion,
  X/Z source, missing square root, missing distance store, distance strictness,
  threshold, angle sign, phase reset, flag-before-provider order, flag bit,
  omitted provider and omitted updater. Compiler/interpreter failures are not
  accepted as successful controls.
- Both tools copies pass eight fresh canonical checks and shared checks.
  Production repeats two installed checks per copy and reuses six prior semantic
  checks only after exact module/input/artifact fingerprint equality.

These are bounded guest/native validations. No general FCSR, portable private
stack alias, complete orientation-provider, full-parent or hardware/gameplay
acceptance claim is made.

## Complete owner, image and progress

The actual three-command Make recipe reproduces the qualified object. All
**14 neighboring owner functions**, their bindings and pools remain identical;
selected, complete-owner and executed-command diagnostics are empty.

The independent image prediction, first link and adopted ELF agree:
**177 changed bytes = 176 code bytes + one symbol-size byte**, metadata 0,
exclusions 0. All **6,055 other bodies**, all **6,056 function addresses**, the
entire guard manifest, C inventory CSV and protected Game data
(**189,088 bytes / 720 owners**) remain fixed.

Raw C SHA-256: `c7d8999758f9df554a75c2230d81be9ac21c42a702fb628d96283d1133c88a7d`.
Owner source SHA-256: `6d73f2324808931d68488cb23dfd6271b9abec2690d13f49d8d7f7bf59a3986b`.
Padded owner SHA-256: `58ff37e85e66ba6eae2c26c67fdd03a3e02dce23db00908752b8aaea2353b2ca`.
Adopted ELF SHA-256: `0628306859314815f346f4c3f76088aa2e897d6bddcbd85424f3ddce9569b018`.

Fresh recount: **3,963 / 5,506 (71.98%)** total exact C;
**3,290 / 4,833 (68.07%)** Game; zero drift. Init remains 492/492 and Debugger
181/181. The 75% goal remains active with **167 more** matches needed for 4,130.
Next private screen: `func_15016588`. Root README changes are its two aggregate rows only.

All 2,096 inherited mirror dirty paths and its HEAD are preserved; three new
qualification modules are added there. Tools are committed before the consumer;
nothing is pushed. The scoped eleven-file Graphify refresh retains old nodes
and valid relationships and retires the obsolete signed placeholder return.
Historical communities remain historical; no full-corpus re-extraction or global
clustering is claimed. Routine work used zero Claude calls or dependency changes.
