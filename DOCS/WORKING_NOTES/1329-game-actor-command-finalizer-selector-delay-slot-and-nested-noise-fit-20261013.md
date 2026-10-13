# Game Actor Command Finalizer Selector Delay Slot And Noise Fit - 2026-10-13

## Scope And Result

Resume consumer `0b58317e` / tools `b04caa1` from
[Note 1328](1328-game-actor-command-finalizer-opening-fault-boundary-and-fit-rejections-20261013.md).
Both active checkouts were clean. Continue the same `func_15034860`, prepared
toolchain, O2/g3/MIPS2/o32 profile, complete original and existing caller ABI.
No broad conversion, host/runtime/Release operation or installation.

[Production function](../../conker/src/game/generated_61D10.c) remains
405 words / 1620 bytes, original frame `0x48`, VA0x15034860..0x15034EB4 /
ROM0x61D10..0x62364. **Real differences307->299; still not byte-exact and
receives no matching credit.** No guards, padding, fabricated fields/state or
physical-register binding. First five prologue and last four epilogue words
remain exact. The first-selector load now matches retail word9 and executes in
the suppression branch's delay slot, instead of the banked word27 placement.

## Source Recovery

[Opening experiment](../../tools/experiments/game_actor_command_finalizer_opening.py)
combines four genuine source-shape changes, without adding locals:

- Remove the first parameter's top-level volatile qualifier. The compatible
  function type, o32 argument representation and caller source remain unchanged.
- Separate the noise predicate's first two category tests from its final
  category test, retaining two actual conditional zero-setting paths.
- Initialize lower=40 inside the primary channel before capturing its numeric
  byte in the existing delta local; preserve explicit unsigned conversion.
- Initialize upper=60 before its type0x42 override, retaining lower80/upper120.

All other fields, full-word selectors, tag snapshots, signed/unsigned arithmetic,
clamps, timers and pointer-result representation remain intact. The qualifier
removal alone is a403-word control, not proof of the original declaration.
The combined body retains the original extent and actual input-home semantics.

Regenerate all49 unchanged-profile screens. Representative fresh results:

| Form | Words | Frame | Differences |
| --- | ---: | ---: | ---: |
| Banked body |405|0x48|307|
| Ordinary first parameter only |403|0x48|386|
| Ordinary first plus nested noise |405|0x48|310|
| Nested noise and late bound, current numeric input |405|0x48|303|
| Nested noise and late bound, delta numeric input, selected |405|0x48|299|
| Noise/bias block reorder, qualified first |406|0x48|279|
| Reorder plus original-style upper default |405|0x48|331|

The279-difference body exceeds the slot by one word and is not installed.
Wider-value and fully split predicates also fail the intended shape/score.
Reusing lower=0x7C for actual category comparisons emits identical code after
constant propagation; it does not restore the desired physical constant holder.

One focused advisory receives a verified, flattened source/assembly packet in
safe mode, with tools disabled and no persistence. Its redundant s16 cast emits
identical code; its block-order suggestion overflows or regresses. Reject its
reversed word-count premise and causal/proof claims. Codex's nested predicate
and combined fit are accepted only after local source/machine qualification.
No second advisory or Claude edit/build/test/Git operation.

## Qualification And Remaining Fault Boundary

[Focused tests](../../tools/tests/test_game_actor_command_finalizer_opening.py)
reuse existing generic helpers through scoped adapters, without weakening
historical fixture assertions or editing the shared oracle.

Eleven pre-install tests pass38.614 seconds; additional fault/image tests pass
18.956 seconds. All twelve installed tests pass40.910 seconds, no skips.
A later four-test observation/text check passes4.578 seconds and adds the
thirteenth target test for accurate diagnostic labeling.

- 15,288 guest field/type/timer/provider-mutation cases and385 full-word-selector/
  actor/output/global/float aliases pass. No selector narrowing.
- Native32 O2/O0 each passes4096 vectors,8192 total. All five fresh width,
  signedness, suppression, sign and PRNG-modulo negatives fail.
- All six live temporary slots remain exact: reverseSP18, signSP20, noiseSP24,
  primaryBiasSP2C, upperSP30, lowerSP34.80 slot probes and16 effective old342-body
  failures pass.160 original/selected incoming-home/output aliases pass.
- Owned normal/traced objects and compiler fingerprints agree. Both frame-write
  sequences remain8->24->72 with locals48/saved8/outgoing16, M definition48 and
  offsets -48/-40/-36/-28/-24/-20. Frontend inputs26848->26928 and UGEN inputs
 24624->24640 bytes; no frame/layout increase.
- Nine owner neighbors, relative relocations, pools and both padders agree.
  Three independent original/source links pass480 carry-sensitive rebase cases.
 200 cases execute the real119-word parent and complete finalizer.

All52 sampled paths still first differ at access cut5. The differing GPR set
narrows from1/3/6/7/9/10 to3/7; memory, events, FPRs and RA agree there.
Sweep all2,938 fired cut pairs:260 represented states agree, unchanged from
the prior body. **Full private/fault parity is still rejected**, not inferred
from fewer differing registers or the restored selector-load location.

For a rejected value-local control, cut5 dispatches a float-constant load,
not a selector load. Split the observer's dispatched-word positions from the
literal retail selector-load positions, and add an effective regression.
An empty selector-position list is legitimate; never mislabel a non-selector
fault as a restored load. No hardware PC/BD/FCSR, actual PRNG or gameplay claim.
Native conversion bounds and guest-only private aliases remain explicit.

## Image And Protected Inputs

Build succeeds with the known duplicate generated_12D630 recipe warnings;
no ROM build/replacement. Whole-ELF literal proof permits exactly254 changed
bytes inside the same1620-byte target slot. Every other instruction, data,
metadata and size byte stays fixed; no metadata exception.

Guards14,694 rows, target guards0, caller, layout, rodata, Makefile/profile and
conversion CSV remain byte-identical. All189,088 Game-data bytes /720 owners
are exact, SHA0bbc00e1. Archive the protected text manifest/ELF and advance only
its ELF pin after image proof; eight other inputs remain fixed. Historical
finalizer immutability receipts remain historical, not silently rebased.

| Artifact | SHA256 |
| --- | --- |
| Source |d321a244fd33ccda7232f4bff3721e736b46cccb713117afc2ea26a0268d6896|
| ELF |5d2bb92c40d9b4d2d75f8270d7f9bd803fe198e139b4c0632107b10447820e39|
| Guards, unchanged |420eb4c5458868e6b19f5a7eb45f04b38ef96532216f283689eec7e0c5e8d796|

Game remains2,823/4,823 (58.53%), total3,496/5,496 (63.61%), zero drift /
2,000 different. Conversion totals and root README date/rows remain correct.

## Banking And Next

Bank tools `e37e4b3` before consumer source/docs/exact gitlink. Consumer and
both tools checks, both Windows syntax and scoped whitespace checks pass.
Mirror only two absent task files plus the verified shared text pin.
Older HEADddbdd16b and130 unrelated hashes stay fixed, dirty408->410 /
saved hashes131->133. No older commit/reset/stash or push. Verify links,
terminal hook Graphify, fresh post-bank integrity and clean active checkouts.

Continue **this same func_15034860**. Resolve the constant-holder/cached-value
roles in GPR3/7 at cut5, retain word9's real delay-slot load and six physical
slots, then finish the remaining299 literal allocation/control/scheduling and
complete private/fault/owner/rebase/image gates. Full Game, prior guard
elimination, retained text218/114/cut27, translator49/34 and hardware/runtime
goals remain open.
