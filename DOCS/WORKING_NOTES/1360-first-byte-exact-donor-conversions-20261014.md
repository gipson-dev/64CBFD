# First Byte-Exact Donor Conversions

Verified locally: 2026-10-14. The user authorizes using proven byte-exact C,
with proper names and comments, after the read-only source audit bank
`6e561dcd`; see [Note 1359](1359-alternative-source-byte-match-audit-20261014.md).
This first coherent group converts three existing retail assembly routines
to direct C. It does not import the whole alternative project or its headers.

## Installed Functions

| Retail Export | Active Owner | ROM | Words | Frame | Recovered Role |
| --- | --- | --- | ---: | --- | --- |
| `func_15125628` | `src/game_14FF90.c` | `152AD8` | 26 | 0 | Tick four nonzero timer bytes |
| `func_1507D158` | `src/game_A9D90.c` | `AA608` | 32 | `20` | Submit command3 with actor selector and four payload words |
| `func_151411E4` | `src/game_16DC80.c` | `16E694` | 27 | `18` | Release attachment, decrement count and dispatch subtype |

All three emit every retail word directly under the existing O2/g3 profile,
with no new guard, inline assembly, fake padding or shared-header change.
Retain `func_` export identities because the linker/layout/callback tables
resolve those exact symbols. Use descriptive `slot`, `actorIndex`, `selector`,
payload-value and actor/object locals, plus `ActorReleaseCallback16DC80`.
Comments describe proven operations, not speculative sound/gameplay names.

## Donor Adaptation And Comments

The archive's four-iteration byte-array loop matches all26 words in the
active toolchain. Its unrolled accesses reproduce retail's repeated address
materialization without aliases, volatile or guards. Remove the old disabled
draft and the unsupported assertion that this must be handwritten assembly.
The previous failed straight-line forms did not prove that no C form exists.

The selector wrapper preserves record stride812, an unsigned byte load,
command3, selector OR2000 and all four full-width payload words. Keep its five
incoming arguments and the outgoing six-word call, including stack arguments.
Do not invent semantic names for the payload words before their roles are known.

The release wrapper keeps both volatile attachment-pointer reads, the actor
home across the release call, a late count load and late subtype/table load.
Use the active release helper's proven second actor argument. The global table
has a legacy extra-argument declaration; a local unary callback view preserves
this dispatch's actual one explicit actor argument without changing the shared
header. Calling it with two explicit arguments instead emitted29 words and27
differences; reject that candidate. An unsigned view of the live counter keeps
modulo-32 decrement defined, including zero/minimum/high-bit fixture words.
The final body is27 words, directly byte-exact.

## Qualification

The corrected pre-install suite passes9 checks43.960s. Its isolated padder
fixture initially used a whole-owner layout for a one-function object; replace
that fixture with the exact one-slot layout, without weakening production checks.
The installed donor/audit/history run passes **25 checks47.390s**. Add explicit
independent carry links and rerun that gate: one check7.650s. Final complete
donor suite passes **9 checks12.526s**; the refreshed audit's four checks pass
6.749s. Both tools copies pass project smoke and Windows byte-compilation.

- 1,024 guest timer cases cover every byte value in each position, including
  zero and255. All26 words execute; independent final-memory results agree.
- 80 selector domains cover four valid actor indices, unsigned selector edges,
  two SP phases and zero/high-bit payloads. Observe all six exact call arguments.
- 96 release domains cover null/non-null attachment, callback mutation,
  wrapping count words, byte-subtype edges and two SP phases. Verify one/two
  attachment reads, live post-release count/subtype and ordered calls. All27
  words execute; callbacks remain explicitly bounded hooks.
- Thirty fired root-access prefix pairs preserve complete modeled state,
  instruction PC and modeled branch-delay owner. No hardware fault/IRQ claim.
- Native32 O2/O0 each pass65,536 timer pairs, checking all four results.
  Wrapper/handler native gameplay and actual full helpers are not claimed.
- Three freshly compiled bad-source controls fail: wrong timer predicate,
  selector flag and count decrement. ELF/guard/progress corruptions also fail.
- Seventy-four complete-owner neighbors stay fixed:44 timer-owner,15 selector-
  owner and15 release-owner. Compare raw words, relative relocations, normalized
  pools and warning statements after the actual assembly post-processor.
- Both real isolated padders and complete-owner padding qualify. Independently
  assemble retail and compare both padded outputs at retail and rebased entries,
  including the timer array crossing `7FFF..8002` and independent data carries.

## Closed Image And Fresh Progress

The **entire ELF is byte-for-byte unchanged**, including every section,
symbol record and string. Before/after SHA256:
`294eba92c9b31ea335a560d67f8536a30993fc1fa429796df1c486fb532f7ddd`.

The complete raw guard CSV also stays unchanged:
`59473e88b9a02be589d8c72465716753aa8802f1908cba79b771f2c8fbf952d0`.
All189,088 protected data bytes /720 owners remain exact. Original assembly,
layouts, compiler profile, shared headers and all unrelated source stay fixed.

Only three generated progress rows change language `asm` -> `c`; all other
CSV bytes remain fixed. Before CSV14d10014 becomes
`c1fd11fe3c2891b50cd9c3f20ed9936e6d3c90a75b17e81c50ca45cad65526e6`.
Older history checks retain their snapshots and apply only those three exact
conversion-field changes. Do not reset their pins or tolerate unrelated edits.

Fresh legacy-table counts:

- Converted total5,499/6,044 (90.98%), converted bytes86.05%.
- Converted Game4,826/5,323 (90.66%), converted bytes85.41%.
- Byte-exact Game **2,839/4,826 (58.83%)**; total **3,512/5,499 (63.87%)**.
- Real differences1,987, address drift0; Init/Debugger remain unchanged.

As documented in Note1359, the legacy Debugger denominator includes140 data
labels. The executable-C-only comparison is now3,372/5,359 (62.92%) overall,
with41/41 Debugger and2,839/4,826 Game. This checkpoint does not silently alter
that older progress methodology. Root README updates aggregate rows only.

Installed owner hashes:

- `game_14FF90.c`:4741c101b8e6406c9e870ff56c7c185f67bcb2030d64e53495223ca93b7cd0a1.
- `game_A9D90.c`:6372ec8438d2b7238507026c84b94df84689049bbf5c79869dcde52b528dbddd.
- `game_16DC80.c`:48500431bc85a41ebb7833a93fc09f6b3b2704312b83316ca547b32a8fc3a966.

## Banking And Remaining Queue

Bank tools `fb5470eaa1077dd3b7a0a7ebabe9c22444b304d9` first, then the source/
docs/consumer pin. The older mirror stays at `ddbdd16`: verify all470 starting
hashes, copy only ten owned modules, preserve462 other hashes and add two
new files, leaving472 dirty paths. Do not reset or duplicate its history.
No push. The supplied archive remains untouched; only qualified C bodies are
adapted into the active project. Audit-tool output is explicitly scoped as
read-only even after the project adopts these functions.

The updated `adoption-after.json` comparison retains the candidate's1,478
exact executable C functions and removes these three from the donor queue.
**Nineteen reviewed byte-exact candidates remain to be independently transferred**.
Next investigate `func_15008870` (48 words, `game_35D20.c`), then the other
small event/actor routines before the larger streaming-audio group. Existing
active-source ABI, owner profiles, raw guards and whole-image effects must be
requalified; original-donor matching alone is not installation proof.

Read-only PC-port check: its selected generated file already contains all
three routines, with a different timer schedule. Since this decomp conversion
changes no guest-image byte, do not mechanically rewrite that independently
dirty file or claim a host repair. No host build/launch or frozen Release work.

```sh
python3 -m unittest tools.tests.test_game_byte_exact_donors -v
make -C conker build/conker.us.elf NON_MATCHING=1 -j4
make -C conker match-progress NON_MATCHING=1
```
