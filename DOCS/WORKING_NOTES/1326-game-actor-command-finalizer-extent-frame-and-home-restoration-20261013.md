# Game Actor Command Finalizer Extent Frame And Home Restoration - 2026-10-13

## Scope And Result

Resume consumer `8f58c327` / tools `b6ba284` from
[Note 1325](1325-game-actor-command-finalizer-semantic-recovery-and-matching-boundary-20261013.md).
Both active checkouts were clean. Query the focused graph and retain the complete
original, existing caller ABI, O2/g3/MIPS2/o32 profile and prepared toolchain.
No host/runtime/Release work, dependency switch or broad conversion. Zero Claude calls.

[func_15034860](../../conker/src/game/generated_61D10.c) now emits the full
405-word/1620-byte retail extent and original0x48 frame:
VA0x15034860..0x15034EB4 / ROM0x61D10..0x62364.
**Real linked differences398->342; it is still not byte-exact and receives no
matching credit.** No expected-word guards, source padding, fabricated fields,
physical-register bindings or profile change. The first five prologue words and
last four epilogue words match, including the original incoming word stores.

The complete public two-channel contract remains qualified. Keep32-bit selectors
and s32 pointer-result representation; top-level volatile on the first parameter
does not change the compatible function type or caller ABI. No caller edit.
Full private storage, scratch-role lifetimes and own-access fault/scheduling
parity remain unfinished; equal frame size alone does not establish them.

## Source Fitting

[Fitting tool](../../tools/experiments/game_actor_command_finalizer_fitting.py)
reuses the banked recovery/compiler/observer APIs.86 corrected unchanged-profile
screens cover halfword/command cursors, local views of verified actor fields,
width diagnostics, declaration groups, word snapshots and control-flow shapes.
Only the accepted sign-0 body gets complete qualification. Other forms are
diagnostic controls; narrow selector forms do not satisfy the banked full-word
contract. The shared actor struct has incompatible widths in this area and is
not changed; prefix-only views are experimental, not an invented full actor type.

Representative fresh measurements:

| Source | Words | Frame | Differences |
| --- | ---: | ---: | ---: |
| Banked complete body |395|0x40|398|
| Halfword cursor local |398|0x48|397|
| Verified field view |395|0x48|395|
| Captured tag-index snapshots |400|0x48|373|
| Snapshots plus clamp intermediate |402|0x48|373|
| Explicit bounds/tail and captured numeric input |404|0x48|368|
| Explicit negative/positive sign arms, accepted |405|0x48|342|
| Qualified-parameter removal control |403|0x48|383|

The source snapshots first's full word for each tag, caches the unsigned numeric
input before conversion, uses a real clamp intermediate and keeps the strict
`scale < 0.0f` predicate with explicit sign arms. Both bounds paths and separate
post-update signed-halfword reads retain original semantics. No dead synthetic
work is introduced to inflate the frame or word count.

A pre-install exhaustive sweep rejects an early tail transform: a broad textual
replacement also changed the earlier bounce condition to use stale `value`
rather than its just-loaded `current`. The production body is untouched at that
point. Restrict transformation after the unique velocity/store marker, rerun
the15,288-case sweep successfully, and regenerate all86 screen measurements.
Do not reuse pre-correction measurements as accepted evidence.

The qualifier-removal control is not a functional negative: its sampled public
output, cursor and three first-home reads agree. It emits403 words and different
instructions. Therefore the qualifier alone is not proven necessary for the home
behavior or proven to be an original-source declaration. It is part of the
qualified405-word shape, not a narrower API or asserted compiler-cause fact.

## Frame And Incoming Homes

Reuse the fingerprint-locked read-only CFE/UOPT/UGEN observer through a scoped
adapter; no shared observer edit. Newly owned compilers complete successfully,
all four executable hashes stay fixed, and normal/traced text, functions,
relocations, pools and complete objects agree. Fired frame writes:

- Old:0->8->24->64, saved8/outgoing16/locals40/temp0.
- Fitted:0->8->24->72, saved8/outgoing16/locals48/temp0.
- Old CFE/UOPT input bytes26472/24240; fitted26816/24624.
- Six missing-gate/driver-failure/input-corruption controls reject.

Intermediate snapshots also reproduce the8-byte local-area increase before the
final sign shape. These are observations of source allocation, not a trace of
the unknown original source or permission to rewrite stack words with guards.

160 guest cases put the output at finalizer-entrySP+0,+8,+10,+12,+14 across two
phases, four types and four full-word selector pairs. Original and fitted code
agree on public RAM, output bytes, cursor and provider calls. The first/second
incoming homes are preserved; earlier output can change later reads of them.
The banked395-word body fails50 output witnesses. Entire private RAM/events and
fault prefixes are intentionally not claimed equal.

## Qualification

```sh
python3 -m tools.experiments.game_actor_command_finalizer_fitting
python3 -m unittest tools.tests.test_game_actor_command_finalizer_fitting -v
make -C conker -j4 build/conker.us.elf progress.csv
```

[Focused tests](../../tools/tests/test_game_actor_command_finalizer_fitting.py):
ten pre-install tests pass39.116 seconds; ten installed tests pass58.012 seconds,
no skips. Reuse existing generic references/oracles through scoped adapters,
without editing historical target suites or treating their old image fixtures
as fresh current-image proof.

Final diff review corrects one clamp indentation in source and its generator.
The following rebuild has the identical complete ELF hash; unchanged semantic
receipts remain applicable. Final focused home/frame/image/text tests are fresh.

- 15,288 all-type/byte-field/signed-boundary/timer/mutation guest cases and385
  full-word-selector/actor/output/global/float aliases pass. Original387 visited
  words remains the execution scope, not a claim that all405 words execute.
- Native32 O2/O0 each passes4096 vectors,8192 total. Five fresh width, signedness,
  suppression, sign and PRNG-modulo negatives fail. Host-endian numeric halfwords
  are normalized; private stack aliases are guest-only, not a portable-C claim.
- All nine copied-owner neighbors retain bytes/relative relocations/pools and
  equal diagnostics. Both whole-owner padders agree; the target size is1620.
- Three independent original assembly/source links pass480 code/global-rebased
  semantic cases with HI/LO carries. The source remains visibly different.
- Two hundred cases execute the real119-word parent and complete original/fitted
  finalizer, preserving calls and the parent's terminator. Lookup/PRNG providers
  remain opaque. Finite conversion bounds, no hardware/FCSR/gameplay acceptance.

The corrected transform failure and ineffective functional-control hypothesis
are retained explicitly rather than deleting coverage or claiming passing
shapes are necessarily correct. No full physical/saved-role/fault-prefix credit.

## Image And Protected Inputs

Build succeeds; retain the known duplicate generated_12D630 recipe warnings.
No ROM replacement/build or host operation. Literal ELF comparison needs **no
new metadata exception**:1,317 changed target bytes across387 words plus one
size byte (1580->1620) =1,318 changed ELF bytes. Every other instruction, data
and metadata byte remains fixed. Prior closed serialization from Note1325 is
already part of the preserved baseline, not newly normalized here.

Guards14,694 rows, Makefile/profile, conversion CSV, layout/rodata and caller
source remain byte-identical. All189,088 Game-data bytes /720 owners are exact,
SHA0bbc00e1. After independent image proof, archive the protected text manifest/
ELF and advance only the ELF fingerprint. Eight other inputs remain fixed.
Fresh text integrity/corruption tests05/06 pass1.749 seconds.

| Artifact | SHA256 |
| --- | --- |
| Source |cd27048bac86b8f2a5738377864c7b36b56d12211445ff5efde4b65ea2576aed|
| ELF |16fca5103add879221c24838e7b45b504930c26c4a9cc27221d307af48c403a5|
| Guards, unchanged |420eb4c5458868e6b19f5a7eb45f04b38ef96532216f283689eec7e0c5e8d796|

Matching stays Game2,823/4,823 (58.53%), total3,496/5,496 (63.61%), drift0/
different2,000, converted functions/bytes fixed. Re-measure rather than infer
credit from a405-word body or correct frame. Root README rows already agree;
no unnecessary number churn or detailed narrative there.

## Banking And Next

Bank tools966c8fd and formatting follow-upda7ddac before source/docs/exact
consumer pin. WSL consumer and
both tools checks, both Windows syntax and scoped whitespace checks pass.
Older HEADddbdd16b and124 unrelated saved hashes remain unchanged. Copy only two
absent task files plus verified text pin, dirty402->404/fingerprints125->127;
no older commit/reset/stash or push. Verify links, clean active checkouts,
terminal Graphify and post-bank integrity before reporting the checkpoint.

Continue **this same func_15034860**. The extent/frame and bounded incoming-home
behavior are restored, but342 word differences still include scratch allocation,
temporary stack slots, independent schedules and control/delay shape. Compare
actual roles and literal accesses; the opcode-shape matcher is diagnostic only
and never writes a binary normalization recipe. Require full source/ABI/public/
private/fault/owner/rebase/image proof before byte-exact credit.
Full Game, previous guard elimination, retained text218/114/cut27, translator49/
34 and hardware/runtime goals stay open.
