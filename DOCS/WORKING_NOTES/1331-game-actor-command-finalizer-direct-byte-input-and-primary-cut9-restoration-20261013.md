# Game Actor Command Finalizer Direct Byte Input And Primary Cut9 - 2026-10-13

## Scope And Result

Resume consumer `79248b31` / tools `79fe8a8` from
[Note 1330](1330-game-actor-command-finalizer-scalar-predicate-and-cut5-restoration-20261013.md).
The consumer is clean except the interrupted, untracked input experiment in
mounted tools. Preserve that work and the independently dirty older tools copy.
Continue the same complete `func_15034860`, existing caller ABI and prepared
IDO O2/g3/MIPS2/o32 profile. Zero Claude calls, installs or host/Release changes.

[Production function](../../conker/src/game/generated_61D10.c) retains 405 words,
1620 bytes and frame 0x48. **Real word differences decrease 298->269; the body
is still non-matching and receives no matching credit.** First14 and last four
words remain exact, including the real word9 selector delay-slot load. No
guards, padding, physical-register binding, invented fields or profile changes.

Recover the direct unsigned numeric-byte conversion instead of capturing that
byte in the signed delta local. Initialize lower=40 after the value expression.
Both full-word selector snapshots and all later signed math remain intact. The
compiler now emits the retail T7 byte temporary and T4 primary tag-home read.
The unsigned conversion branch remains emitted; this does not delete its
correction path merely because the byte's real input domain is 0..255.

## Source Screens And Fault Evidence

[Input experiment](../../tools/experiments/game_actor_command_finalizer_inputs.py)
retains the interrupted screen and adds a reusable, actually fired 52-path fault
sweep. Freshly screen seven direct-input forms and five comma/float-carrier
forms, without changing the compiler or ABI. Complete represented state means
memory, events, GPRs, FPRs, condition, HI/LO and provider calls, not hardware PC,
branch-delay exception state or FCSR.

| Form | Words / Frame | Differences | Exact States / 2938 | First Cut, Primary / Disabled |
| --- | --- | ---: | ---: | --- |
| Banked scalar |405 / 0x48|298|452|9 / 7|
| Direct byte, early lower |405 / 0x48|263|720|9 / 7|
| Direct byte, lower after conversion, selected |405 / 0x48|269|720|10 / 7|
| Lower assignment in scale operand |405 / 0x48|264|720|9 / 7|
| Lower assignment in constant operand |405 / 0x48|281|452|9 / 7|
| Three float-carrier orderings |405 / 0x48|280|496|10 / 7|

The lower-score263 form leaves GPR7 different at primary cut9. Select269 to
restore that prefix too. All44 primary-active paths agree through cut9; all
eight disabled-primary paths retain agreement through cut6. Every cut actually
fires, and each path's complete access count remains equal. The52 paths produce
2938 pairs and720 exact represented states, up from452. This is partial
restoration, not full private-storage/fault or gameplay equivalence.

The next primary boundary is cut10: both dispatch C4267D48, the D_80097D48
float load, but GPR7 differs because lower=40 is scheduled after that load in
the source and before it in retail. Memory/events/FPRs agree there. Disabled
primary first differs at cut7: original8FAB0054 loads second into T3/register11;
selected8FB90054 uses T9/register25. Selector capture and volatile-second
screens do not repair that allocation.

## Qualification And Image

[Focused suite](../../tools/tests/test_game_actor_command_finalizer_inputs.py)
reuses the existing full-contract checks through scoped adapters. It has its
own ignored pre-install baseline, not a broad rebase of historical fixtures.
All13 pre-install tests pass42.357s; all13 installed tests pass44.410s, no skips.

- 15288 guest field/type/timer/provider-mutation cases and385 full-word
  selector/actor/output/global/float aliases pass.
- Native32 O2/O0 each4096,8192 total, and five fresh semantic negatives pass.
- All80 live-slot probes,16 effective old342-body failures and160 incoming-home
  aliases retain their contracts. Six physical slots stay18/20/24/2C/30/34.
- Owned compiler observations retain M48 and offsets -48/-40/-36/-28/-24/-20;
  frame writes8->24->72, locals48/saved8/outgoing16, normal/traced code identity.
- Nine owner neighbors, relative relocations, pools and both padders agree.
  Three independent links pass480 carry-sensitive rebase cases.200 cases execute
  the real119-word parent and complete finalizer.
- All2938 fault pairs fire; no full fault or hardware acceptance is inferred.

The linked build succeeds with the existing duplicate generated_12D630 recipe
warnings. No ROM is built/replaced. Literal whole-ELF comparison permits exactly
181 changed bytes within the same1620-byte target slot. Every other code, data,
metadata, size and address byte is fixed, without an exception or normalization.
All189088 Game-data bytes /720 owners are exact, SHA0bbc00e1. Guards14694 rows,
target guards0; caller, layout, rodata, Makefile/profile and conversion CSV fixed.

Archive the protected text manifest/ELF under the new test's ignored directory
before advancing only its ELF pin. Its eight other inputs remain fixed. Fresh
text integrity and effective corruption controls pass1.670s. Both tool checks,
both Windows syntax checks and task-scoped whitespace checks pass.

| Artifact | SHA256 |
| --- | --- |
| Source |b53f5e1b36f268f51ff6560664a07923449229a95845234c4f67179e381e9301|
| ELF |3c14e2b16246c2c33855e82c1cb8218311d0490af26f71f2b2f7d0891d4c81f8|
| Guards, unchanged |420eb4c5458868e6b19f5a7eb45f04b38ef96532216f283689eec7e0c5e8d796|

## Banking And Continuation

Fresh match-progress remains Game2823/4823 (58.53%), total3496/5496 (63.61%),
zero address drift /2000 different. Conversion5496/6044 is unchanged. Root
README date and aggregate rows already agree, so do not add function prose there.

Tools `9cd126b` are committed before the consumer's source/docs/gitlink. Copy
only two absent task files and the independently verified text pin to the older
tools checkout. Its HEADddbdd16b and411 unrelated hashes remain fixed;
dirty412->414. No older commit/reset/stash or push. Verify the consumer commit
hook's graph completion, relative links and fresh post-bank tests before closing.

Continue **this same func_15034860**: recover the primary cut10 lower-bound
schedule and disabled-primary cut7 second-selector allocation, then all269
remaining literal differences under full private/fault/owner/rebase/image gates.
Full Game, previous guard elimination, retained text218/114/cut27, translator
49/34 and hardware/runtime goals remain open.
