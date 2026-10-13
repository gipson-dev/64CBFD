# Game Actor Command Finalizer Live Temporary Slots - 2026-10-13

## Scope And Result

Resume consumer d9882ff1 / tools da7ddac from
[Note 1326](1326-game-actor-command-finalizer-extent-frame-and-home-restoration-20261013.md).
Both active checkouts were clean. Keep the complete semantic body, caller ABI,
prepared compiler and original O2/g3/MIPS2/o32 profile. Zero Claude calls.
No host/runtime/Release operation, dependency switch or broad conversion.

[func_15034860](../../conker/src/game/generated_61D10.c) remains405 words/1620
bytes with the original0x48 frame: VA0x15034860..0x15034EB4 /
ROM0x61D10..0x62364. **Real word differences342->307; still not byte-exact,
no matching credit.** No new guards, source padding, fabricated state,
physical-register binding or profile/ABI change. First five prologue and last
four epilogue words remain exact.

## Recovered Roles

[Role-fitting tool](../../tools/experiments/game_actor_command_finalizer_roles.py)
reorders existing declarations and promotes the cached actor-type value into
the existing32-bit delta local in the noise predicate. Delta is overwritten
before later numeric use. No actor access, selector width or caller changes.

| Live Role | Original And Fitted SP Offset | Optimizer M Offset |
| --- | ---: | ---: |
| reverse |0x18|-48|
| sign |0x20|-40|
| noise |0x24|-36|
| primaryBias |0x2C|-28|
| upper |0x30|-24|
| lower |0x34|-20|

These are observed call-time values and literal emitted accesses, not only
declaration-offset predictions. Final frame72 plus optimizer M offset gives
each SP-relative address. Owned normal/traced compiler objects agree. Both
frame-write sequences are8->24->72, locals48/saved8/outgoing16. The optimizer
M definition changes44->48;8-byte rounding already gave the old body48 locals.
Old/fitted frontend inputs are26816/26848 bytes; UGEN inputs both24624 bytes.
Equal frame size did not imply equal live temporary placement.

Regenerate all34 unchanged-profile screens. Reordering alone stays342 word
differences, because its modified operands were already different; integer
promotion produces the accepted307. Early delta cache emits309; moving the
lower initialization leaves331/333/363. Removing the first-parameter qualifier
emits403/404 words with381..386 differences. Six register-keyword and nine
unsigned-local controls offer no improvement and are not installed. Diagnostic
shapes are not automatically semantically qualified or original-source proof.

## Qualification

```sh
python3 -m tools.experiments.game_actor_command_finalizer_roles
python3 -m unittest tools.tests.test_game_actor_command_finalizer_roles -v
make -C conker -j4 build/conker.us.elf progress.csv
```

[Focused tests](../../tools/tests/test_game_actor_command_finalizer_roles.py):
eleven pre-install tests pass40.548 seconds; fresh installed rerun passes
eleven tests38.859 seconds, no skips. The interrupted session receipt is not
used as terminal proof. Reuse existing references, compiler observers, parsers,
guest oracle and padders through scoped adapters; no shared oracle weakening.

- 15,288 guest all-type/ten-byte/signed-boundary/timer/provider-mutation cases,
  385 full-word-selector/actor/output/global/float aliases and8192 native32
  cases pass. O2/O0 each4096; all five fresh semantic negatives fail.
- 80 temporary-slot cases cover48 normal snapshots and32 private-provider
  mutations. Original/fitted public memory, cursor and calls agree; the old
 342-difference body fails16 effective witnesses. Compare all six first-call
  values and only actually live roles at later calls.
- 160 original/fitted incoming-home/output aliases retain the prior contract.
  Entire private RAM, scratch registers and own-access fault prefixes are
  deliberately not claimed equal.
- Nine owner neighbors retain bytes, relative relocations, pools and equal
  diagnostics; both padders agree. Three independent original/source links
  pass480 carry-sensitive rebase cases.200 cases execute the real119-word
  parent plus complete finalizer with opaque lookup/PRNG providers.

The private mutation provider writes saved caller words for bounded machine-
storage probes. It is **not retail PRNG behavior**, hardware acceptance or a
portable-C guarantee. Native numeric halfwords retain their endian adaptation
and finite conversion domain. Do not label all remaining307 words independent
scheduling or give private/fault parity credit from these bounded witnesses.

## Image And Protected Inputs

Build succeeds with the known duplicate generated_12D630 recipe warnings;
no ROM replacement/build. Whole-ELF literal comparison changes exactly269 bytes
inside the same1620-byte target slot. Size, all metadata and every other ELF
byte remain fixed: no metadata exclusion or serialization exception.

Guards14,694 rows and target guards0, caller, rodata, layout, Makefile/profile
and conversion CSV remain byte-identical. All189,088 Game-data bytes /
720 owners are exact, SHA0bbc00e1. After independent image proof, archive the
protected text manifest/ELF and advance **only** the ELF fingerprint; eight
other inputs remain fixed. Fresh text integrity/corruption tests05/06 pass
1.910 seconds. Historical text semantic receipts remain historical, not
blanket fresh current-image qualification.

| Artifact | SHA256 |
| --- | --- |
| Source |f4a7922c5317deaaec503865d0e0af59bfb29b6d31d1377c31b67b24e0d77024|
| ELF |6b3a795a43992b6ac9d8ffb736c8d80360a3416936d5ae7708db7c54aa3ecb86|
| Guards, unchanged |420eb4c5458868e6b19f5a7eb45f04b38ef96532216f283689eec7e0c5e8d796|

Game remains2,823/4,823 (58.53%), total3,496/5,496 (63.61%), drift0 /
different2,000, conversion totals fixed. Root README date/rows already agree;
detailed recovery updates remain here, not in the main README.

## Banking And Next

Bank tools cf06d70 before consumer source/docs/exact gitlink. Consumer and both
tools checks, both Windows syntax and scoped whitespace checks pass. Copy only
two absent task files plus the verified shared text pin into the older mirror.
Older HEADddbdd16b and126 unrelated hashes remain unchanged; dirty404->406 /
fingerprints127->129. No older commit/reset/stash or push. Check documentation
links, clean active checkouts, terminal commit-hook Graphify and post-bank
integrity before reporting the bank.

Continue **this same func_15034860**. Six bounded caller-live slots and prior
extent/frame/homes are restored;307 differences still require literal scratch
allocation, other private storage, control/delay scheduling and fault-prefix
work. Require complete source/ABI/public/private/fault/owner/rebase/image proof
before byte-exact credit. Full Game, previous guard elimination, retained
text218/114/cut27, translator49/34 and hardware/runtime goals stay open.
