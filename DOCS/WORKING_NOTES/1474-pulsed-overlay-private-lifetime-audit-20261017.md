# Pulsed Overlay Private Lifetime Audit

Date: 2026-10-17. Consumer baseline **cfe67ab2**, tools baseline **33dda28**.
Continue [Note 1473](1473-color-overlay-draw-direct-match-20261017.md)'s exact
next target, not a substitute function. Codex owns the investigation and
validation; **zero Claude calls**. **No C adoption or new matching credit.**

## Retail Lifetime

**func_1517F564**, owner `conker/src/game/generated_1AC2F0.c`, has **111 words /
444 bytes**, frame **0x30**, VA **0x1517F564..0x1517F720**, ROM
**0x1ACA14..0x1ACBD0**. Its complete independently assembled original matches
the retail ROM with **16 bindings**. Raw object text SHA-256:
**ab1f9976ec863dc785c9f4296cc38f795487aec73a6c6c630485cd3ad9ea4bd9**.

The full prologue saves RA at SP+0x1C and the cursor at SP+0x30. After timer
and alpha gates, the pulse branch at **0x1517F5B0** executes **LWC1 F2,
SP+0x20** in its delay slot at **0x1517F5B4**. No preceding local store writes
those four bytes. The complete routine's other stack stores are outgoing
channel at +0x14 and blue at +0x10. The pulse-on path later sets F2 to zero
at **0x1517F600**; pulse-off retains the inherited bits for RGB interpolation.

The complete **175-word func_150198FC** caller has frame **0x28**. The word is
therefore at **caller-entry SP-0x38**, below its current SP, not in an incoming
argument home or saved-register slot. No pulse helper executes on the off
path, so its output cannot initialize this earlier read. Caller providers'
complete historical stack writes remain outside the bounded oracle contract.

The read-only additional source also declares `f32 sp20;` then uses
`var_f2 = sp20;` without an assignment. That is evidence of the same unresolved
local, not usable C source or an established portable lifetime.

## Positive Witnesses

Execute actual retail code, not replacement helper hooks:

- **6,480 wrapper cases**, timer/alpha bypasses, both stack phases, palette
  indices 0/1/255, pulse bytes 0/1/255, five angle values and six finite blend
  seeds, including signed zero. An independent rounded-FP/literal-command
  reference checks returned cursors, complete public memory, helper entries
  and six-word drawing packets. Use the actual 65-entry linked wave table.
- **3,240 fired inherited reads** are observed before any local write;
  **2,160** cases execute the real **12-word phase-shift slot** (11-word
  function plus its retained tail), **36-word wave lookup** and **197-word
  renderer. No opaque pulse/wave/draw provider. Natural wrapper paths visit
  **96 words**; 15 retained unsigned-byte-negative conversion-arm words are
  unreachable in these fixtures. The full 111-word object remains checked.
- **24 actual setter/updater cases** execute **15-word func_1517F720** and
  **24-word func_1517F7B4** before the wrapper. The setter accepts pulse zero
  with an active timer/alpha; the updater preserves that pulse byte. Eight
  cases positively distinguish the actual compiled zero-initialized candidate.
- **512 complete caller cases** execute every one of the caller's 175 words,
  with the actual wrapper/lookup/draw chain and independent full public-state/
  cursor/call expectations. Other scene providers retain their existing
  bounded opaque contracts. This is not full provider-stack-history proof.
- **40 bounded sequence-packet cases** execute all ten retail words at
  **0x15025EA4..0x15025ECC** and the real setter. Both signed speed routes
  pass fifth argument **1**, including the branch-delay initialization of T8.
  Changing that initialization to zero is an effective fired negative. This
  proves the named packet, not a whole-program pulse-one invariant or full
  sequence-engine acceptance. The unrecovered outer query engine is not
  represented as newly installed code.
- **308 positively fired access-fault prefixes**, including eight faults at
  the inherited read, compare literal state through independently assembled
  versus ROM words. These qualify bounded emitted order, not CP0 or portable
  C faults. FP behavior uses the existing nontrapping conversion model;
  native C, hardware FCSR/exception enables, arbitrary nonfinite conversions,
  final pixels and gameplay are not acceptance claims.

Concrete palette witness, after the actual setter and updater:

| Inherited Blend | Retail RGB | Zero-Initialized C RGB |
| --- | --- | --- |
| 0.0 | 10, 40, 80 | 10, 40, 80 |
| 0.25 | 60, 65, 100 | 10, 40, 80 |
| 1.0 | 210, 140, 160 | 10, 40, 80 |

The compiled candidate is tested, not merely a hypothetical changed reference.
Matching the pulse-on subset does not establish the full wrapper's semantics.

## Rejected Source Screens

Compile complete owner bodies under the existing profile. All **27 other raw
owner routines** remain unchanged. These are diagnostic screens only:

| Form | Words | Ordinal Word Differences | Disposition |
| --- | ---: | ---: | --- |
| Zero-initialized blend | 93 | 101 | Defined source, but changes retail output |
| Uninitialized blend | 112 | 101 | Undefined read; not installable |
| Explicit inherited local | 110 | 80 | Undefined read; not installable |

All three happen to produce empty IDO diagnostic output. Absence of a compiler
warning does not make the local initialized or the body acceptable. The tool
has **no selected candidate or installation API**; every row explicitly records
`installable=False` and `matching_credit=False`. Do not manufacture zero blend,
silently rely on undefined C, or add a semantic word patch for matching credit.
This follows the analogous prior [renderer deferral in Note 1395](1395-packed-fade-scale-callback-and-renderer-deferral-20261015.md).

## Validation And Bank

All **10 final checks pass in 134.517s**: seven new audit tests and the three
previous overlay installed-image tests. Earlier exploratory failures were
test-harness issues: missing NEG.S routing, an unmapped setter byte, caller
dimension canaries overlapping pointer-cell canaries, and the bounded packet
join missing from the owned code map. Fix those locally without production
edits or weakened acceptance. Both corrected focused tests passed again before
the final run. Keep those failures distinct from a retail/source regression.

Protect **154 input entries / 145 distinct paths**, including source, ELF,
conversion CSV, guards, complete caller/setter assembly, trig source and the
read-only archive. Every entry's corruption rejects; all live bytes remain
equal to the captured baseline. The ELF remains
**cab895122f114cbfe41572410c714d016d6b75244bd3434fb6d26c453d60c1c1**;
the original wrapper's production placeholder is unchanged. No normal rebuild
is necessary or claimed for this tools-only audit.

Fresh official matcher still reports Game **2,945/4,828 (61.00%)**, total
**3,618/5,501 (65.77%)**, different **1,883**, no address drift. Init **492/492**
and Debugger **181/181** remain exact. Root README is untouched because none
of its aggregate rows changed. Existing duplicate-recipe warnings remain.

Tools **381d541** banks three new files before the consumer pin. Both copies
have **three exact pairs / six ASCII/AST checks**. Eleven standalone padder
tests pass in each copy: active **0.032s + 0.021s**, mirror **0.031s + 0.019s**;
tools-check passes. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a** and all **1,008 initial dirty-file
hashes**; three new task files produce **1,011 final paths**. No conflicting
task files existed before copying. No mirror commit/reset, push, dependency/
configuration change, host build/launch or frozen Release action.

Prepared-checkout reproduction, sequentially:

```sh
python3 -m tools.experiments.game_pulsed_overlay_audit
python3 -m unittest tools.tests.test_game_pulsed_overlay_audit \
  tools.tests.test_game_color_overlay_draw_installed -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Audit all 111 original words, stack offsets and both pulse paths.
- [x] Execute actual setter/updater/lookup/draw and complete caller chains.
- [x] Positively distinguish zero substitution and reject undefined-local adoption.
- [x] Qualify the named pulse-one packet without claiming a global invariant.
- [x] Pass target/checkpoint/input/tool/mirror gates and bank tools first.
- [ ] Recover supported C for this same wrapper without inventing its blend lifetime.

## Next Boundary

Keep **func_1517F564** open. Audit remaining direct/indirect writes to the pulse
byte and timer, startup/reset ordering and real provider stack provenance before
claiming a pulse-one precondition or inherited-value producer. The one named
constant-one packet is insufficient. Do not spend a broad scheduling batch on
an undefined candidate. If preservation of the original bug ultimately requires
assembly, make that a separate, honestly assembly-classified restoration with
no C-match credit; it does not satisfy the still-open C recovery. Wider Game/
additional-source matching, query/sequence engines, timing's 141 differences
and full gameplay acceptance remain open.

Follow-through: [Note 1475](1475-overlay-projection-direct-match-20261017.md)
adds six actual reset cases and two guest-only indexed-writer witnesses.
Reset clears the timer, not the pulse byte; channel -16 can alias the alpha
store onto that byte while the timer is active. The invalid native index is
not natural-gameplay evidence, and startup inspection does not prove all-path
initialization. No defined C lifetime or all-program invariant is established.
Keep this wrapper unchanged/deferred, with no matching credit. Wider matching
now installs the adjacent 120-word projection; next is the 106-word rectangle.
