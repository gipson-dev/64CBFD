# Game Actor Command Finalizer Semantic Recovery And Matching Boundary - 2026-10-13

## Scope And Result

Resume from consumer `93c5a680` / tools `1943c4d` and
[Note 1324](1324-game-actor-command-dispatch-direct-match-and-table-layout-20261013.md).
Both active checkouts were clean. Query the focused graph, inspect the complete
original405-word routine and its directly matched119-word caller. Retain the
existing O2/g3/MIPS2/o32 profile, prepared compilers, private inputs, independent
older tools work and frozen host Release. Zero Claude calls.

[func_15034860](../../conker/src/game/generated_61D10.c) replaces its zero-return
placeholder with the complete two-channel command finalizer: VA0x15034860..
0x15034EB4 / ROM0x61D10..0x62364,405-word/1620-byte retail slot/frame0x48.
Keep the existing four arguments and s32 pointer-result representation, compatible
with the caller's explicit32-bit cast. No caller ABI/source change.

**This is semantic recovery, not byte matching.** Accepted C emits395 words/
1580 bytes/frame0x40, with398 differences across the fixed405-word retail slot.
The placeholder had372 differences; the raw exact-word score does not improve.
Length/frame/parameter-home/register/scheduling fitting remains unfinished.
No guards, profile changes, arbitrary source padding, fabricated state,
physical-register bindings or matching credit. Normal owner slot padding retains
the fixed1620-byte layout; it does not manufacture the missing original code.

## Recovered Contract

- Read the actor type even when both full32 channel selectors equal0xFF.
  Only exactly0x000000FF skips a channel; values with the same low byte do not.
- Cache type-derived primary suppression for0x70, tag biases4/0 for0x7C versus
  0/2 otherwise, and jitter0 for0x69/0x7C/0x87 versus10 otherwise.
- Primary channel uses unsigned byte+0x201 as an optional gain: zero selects
  existing8191.875f; otherwise multiply by182.04444885253906f. Multiply unsigned
  byte+0x1FE by the gain and existing1/255 constant, with single rounding at each
  operation, truncate32 then narrow signed16.
- Unless cached suppression applies, append tag6*first+bias and that value.
  Always store it to D_800C3EF0. Then re-read signed byte+0x202 and unsigned
  byte+0x1FE, signed integer-divide their product by255, multiply by existing
  65535f and1/255 constants, truncate/narrow and conditionally append the second
  command using its separate tag bias.
- Re-read type for primary random bounds40..59 or80..119 for0x42. State byte
  +0x1FF zero sets negative upper velocity;2 sets positive upper and clears
  signed jitter+0x202. Other states reroll on zero velocity or current0/255.
  Use full unsigned32 PRNG modulo, re-read current after the call, negate at255,
  and make an independent jitter call at0 when cached jitter range is nonzero.
- Add signed byte velocity+0x203 to unsigned current+0x1FE, clamp0..255.
  State3 consumes unsigned timer byte+0x200 using signed D_800BE9E4 comparison;
  equality retains state3 with zero timer, underflow clears timer and state.
- Secondary channel uses signed byte+0x208 as optional gain. Derive sign before
  taking absolute magnitude. Read signed halfword+0x204 and calculate its scaled
  value **before** the header store, then append the negated truncated result.
  This ordering matters when output overlaps+0x204.
- State+0x206 zero/2 sets velocity+0x209 opposite/along the gain sign. Other
  states select a new40..59 velocity at zero or signed255 boundary, or reverse
  when motion continues past the opposing zero side. Preserve separate choose/
  reverse flags across the PRNG call and live signed-byte reloads after stores.
- Add velocity to the signed halfword, retaining16-bit wrap before direction-
  sensitive zero/255 clamps. State3 timer+0x207 uses the same equality/underflow
  boundary as the primary timer. Return the advanced output cursor, no terminator;
  the actual parent supplies its own0x1000 terminator.

Live constants and actor fields are read at their original semantic points,
including output/global/float overlaps and provider mutations. Wrapped command
arithmetic and timer subtraction use explicit unsigned32 expressions; signed
products/velocity sums remain bounded by their real byte/halfword widths.
Retain the repo's fabsf intrinsic declaration, not a new library call.

## Source Screens And Matching Boundary

[Candidate tool](../../tools/experiments/game_actor_command_finalizer_candidates.py)
reuses prepared compiler/object helpers and complete GLOBAL_ASM owner processing.
Fourteen unchanged-profile source screens are recorded, including an unchanged
tail-read control. These are shape measurements, not independently qualified
public/physical contracts.

| Form | Words | Frame | Differences |
| --- | ---: | ---: | ---: |
| selected / unsigned-type / byte-scale / unchanged tail control |395|0x40|398|
| byte-type |398|0x40|389|
| volatile signed first |400|0x40|376|
| unsigned first |397|0x40|396|
| volatile unsigned first |402|0x40|377|
| late lower / late lower plus volatile first |395 /399|0x40|398 /391|
| clamp local / clamp local plus volatile first |397 /402|0x40|395 /377|
| inverted noise / inverted noise plus volatile first |396 /400|0x40|400 /376|

The accepted body keeps non-volatile parameters, the current ABI and complete
public contract. A better word score alone does not justify a volatile contract
change or install another screen without all gates. Original first-parameter
home writes/loads and a0/a2/a3 scratch-role lifetimes differ from the current
compiler result. Empty-channel literal private RAM/events differ and explicitly
reject frame equivalence. No compiler trace proves the allocation cause yet.

## Qualification

```sh
python3 -m tools.experiments.game_actor_command_finalizer_candidates
python3 -m unittest tools.tests.test_game_actor_command_finalizer_recovery -v
make -C conker -j4 build/conker.us.elf progress.csv
```

[Focused tests](../../tools/tests/test_game_actor_command_finalizer_recovery.py):
ten pre-install tests pass39.191 seconds. Ten installed tests pass32.272 seconds
after the independently diagnosed metadata accounting below, no skips.

- 15,288 guest cases cover all256 types and all256 values of ten byte fields,
  channel gates, signed-halfword extremes, velocity signs, state modes and
  signed32 timer extremes. Compare original and actual compiled candidate to an
  independently stated reference: complete public RAM, cursor, PRNG calls and
  public write order.387 original words are visited; do not claim all405 executed.
- 385 full32-selector/actor/output/global/float overlap cases retain alias reloads
  and live constants. A fresh compiled late-secondary-read negative fails at
  an actual header/halfword overlap; the accepted source passes the same witness.
- Native32 O2/O0 each passes4096 reference-derived vectors,8192 total. Compare
  complete actor backing, every output halfword/untouched byte, global result,
  cursor and provider count. Normalize numeric halfwords to host endianness;
  native actor/output overlaps are not a retail-endian portability claim.
- Five fresh native unsigned-byte, narrow-selector, wrong-suppression/sign and
  signed-PRNG-modulo negatives fail observably. PRNG providers return full32
  values and clobber caller-saved GPR/FPRs; mutation modes alter actor type/
  current/state/timer after calls. The real PRNG body is not emulated.
- Both full-owner padders agree. All nine other functions retain exact bytes,
  relative relocations and normalized pools; diagnostics stay equal.
- Three independent original GNU assembly links and source links pass480
  semantic cases across code/global rebases and signed HI/LO carries. They are
  not claimed equal instructions.
- Two hundred cases execute the real119-word parent with either complete405-word
  original or395-word candidate finalizer and verify lookup/finalizer/PRNG calls,
  final cursor and parent's terminator. Lookups/PRNG remain opaque.
- Both channels disabled need only type/private-stack backing. A fired literal
  private witness rejects source/retail frame agreement. No matching private
  storage, full GPR/FPR identity, own-access fault prefixes, hardware FCSR,
  arbitrary NaN/out-of-range conversion or full gameplay claim.

Fixture corrections: import the real signed32 helper; keep float constants and
hex-E-plus tokens valid in native C; use actual parser byte slices for neighbors;
retain live constant reads in the reference. The initial fabsf declaration
without the established intrinsic is rejected as an unresolved helper call.
The draft late halfword calculation is corrected before installation and retained
as the effective negative. No shared oracle or production helper edits.

## Whole Image And Protected Inputs

Build succeeds; the existing duplicate generated_12D630 recipe warnings remain.
No ROM replacement/build, host runtime or Release operation.
The first installed image audit rejects79 additional metadata bytes. Inspect
actual ELF symbol records/string offsets: only func_15034860's named definition
changes, size12->1580. Diagnose three adjacent record/string ordering swaps:

- D_80097D4C / .L1508E838_game_data.
- D_800DDDA0 / D_800A5F14.
- D_80097D58 / D_80082BC0.

The checker reconstructs only those exact reversed pairs from prior fields and
fixed definitions, checks contiguous record/string spans and validates values/
sizes/types/sections. All79 bytes are accounted; three changed-definition controls
reject. No wholesale symbol/string exclusion or unknown-byte allowance.

Final delta1,161 target bytes across364 changed words, two size bytes and79 closed
metadata bytes =1,242 ELF bytes. Every other instruction/data/metadata byte stays
fixed. Guards14,694 rows, Makefile/profile, conversion CSV, retail layout/rodata
and caller source remain byte-identical. All189,088 Game-data bytes /720 owners
remain exact, SHA0bbc00e1.

| Artifact | SHA256 |
| --- | --- |
| Source |857798159dcc3926c37ccfa036a7656bdbe0280f557b34a2d518a561097959f4|
| ELF |01964e578da2a53344602c7c1bcaa2f21f53df2114125b22b8f9665faaa7f2e8|
| Guards, unchanged |420eb4c5458868e6b19f5a7eb45f04b38ef96532216f283689eec7e0c5e8d796|

After independent image proof, archive the prior protected text manifest/ELF
and advance only its ELF fingerprint. Eight other inputs remain fixed. Fresh
text integrity/corruption tests05/06 pass1.508 seconds. Historical target suites
keep their prior whole-image fixtures; unchanged semantic receipts are reused
explicitly, not reported as fresh full-image acceptance.

Fresh totals unchanged: Game2,823/4,823 (58.53%), total3,496/5,496 (63.61%),
drift0/different2,000, converted functions/bytes fixed. The root README's existing
2026-10-13 rows already agree; no narrative or unnecessary number edit there.

## Banking And Next

Bank toolsb6ba284 first, then source/docs/exact consumer pin. WSL consumer and
both tools checks, Windows syntax and scoped whitespace checks pass. Preserve
older HEADddbdd16b and122 unrelated saved fingerprints; copy only two absent
task files and verified text pin, dirty400->402/fingerprints123->125.
No older commit/reset/stash, push, dependency/profile switch or broad conversion.
Verify clean active checkouts, links, terminal Graphify and final integrity.

Continue **this same func_15034860**, not an easier neighbor. Resolve the10-word
extent difference, original first-parameter home,0x48 frame and register/scheduling
shape. Requalify complete semantics plus exact saved lifetimes, stack addresses,
own-access fault prefixes, owners/padders/rebases and literal image before credit.
Current398 differences are not merely frame words. Full Game, prior guard
elimination, retained text218/114/cut27, translator49/34 and hardware/runtime
acceptance remain open.
