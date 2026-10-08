# Game Context Classifier Match

Date: 2026-10-06
Baseline: `a1c20f4d` ([Note1062](1062-game-actor-classifier-match-20261006.md)).
Continue the Game matching goal with the world/context helper called by the
banked effect dispatcher. Original N64 source recovery, not host-port adoption
or complete gameplay acceptance.

## Retail Contract

`func_15141CC0`: **57 words /228 bytes**, no frame, VA
**0x15141CC0..0x15141DA4**, ROM **0x16F170..0x16F254**, owner
[`game_16EE20.c`](../../conker/src/game_16EE20.c). Typed ABI:
`s32 func_15141CC0(s32 context)`. Read signed32-bit `D_800BE9F0` once;
no calls or writes. World47/66/39/25 overrides return6/7/8/5 respectively,
before context range checks or table accesses.

| Context | Result when no world override applies |
| --- | --- |
| 10 | 0 |
| 7 | 2 |
| 11 | 1 |
| 15 | 3 |
| 2,8,12 | world2 ?7 :4 |
| 5 | world20 ?5 :9 |
| 0 | 9 |
| All others | 9 |

The helper accepts a full32-bit context, although the dispatcher normally
supplies flags masked to five bits. Negative/high-bit/high-half aliases do
not truncate into the low table range. The16-entry switch table contains
function-interior code targets at **800A5430**, not category integers.

## Direct Source And Pool Ownership

[Maintained driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_context_classifier_candidates.py)
screens global/local world reads, inside/outside defaults and four actual-SDK
profiles:16 controls, empty standalone diagnostics. All eight O2/g3 or O2
controls match57 words directly. Select the explicit signed32-bit local and
outside default under the owner's existing O2/g3. O1 global forms emit68 words/
59 differences; O1 local forms64 words/64 differences. No new word guards,
insertions, omissions, compiler profile or shared padding-tool changes.

The compiler's full-owner pool concatenates the actor classifier's134 targets
with this classifier's16 targets. Context addend **0x218 (536 bytes)** from
`jtbl_800A5218_game` reaches the original800A5430 table. The combined private
pool is608 bytes:600 target bytes plus eight final alignment bytes. Those
bytes are discarded, not added to or substituted for original Game data.
The existing640-byte `build/assets/249CC0.bin.o(.data)` owner remains pinned
at800A5200..800A5480, ROM249CC0..249F40.

Copied full-owner qualification compares all150 unlinked target offsets
against original ROM addresses, proves exactly six pool relocations, and
compares the banked45-word actor classifier and100-word dispatcher with their
previous unlinked words and relocation metadata. New context words equal the
standalone object after subtracting only the proven0x218 pool addend. Existing
owner warnings remain the same three, including code/statement/caret, not just
count. Both local context prototypes and the dispatcher experiment are typed.
No owner Makefile edit or data replacement is required.

## Bounded Qualification

[Eight maintained tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_context_classifier_match.py):

- Compare all57 compiled words and all16 table targets with retail; screen all
  16 controls and measure frame size from actual stack instructions.
- Actual padding emits exactly228 code bytes, maps only the two pool
  relocations and retains the world relocations. Alternate world90018004 and
  table90007FFC exercise signed-low carry behavior independently. No compiled
  `.rodata` remains in the padded object.
- **15822 paired guest cases** cover27 world values, every low byte plus
  signed/high-half context edges, two SP phases and surrounding poison.
  Return categories, all storage, saved registers and complete ordered reads
  agree. Exactly one4-byte world read, no calls/writes. Both bodies reach53
  words; four duplicate comparison preludes are structurally unreachable at
  relative1C/30/44/58, not silently counted as covered.
- **5308551 actual32-bit native cases** cover every16-bit low half with zero,
  0x10000 and0x80000000 upper patterns, plus five signed edges, across27 worlds.
  Compare an independent semantic reference and the complete32-bit world
  storage before/after; no fabricated invalid native pointers.
- Minimal guest storage contains only the world word on override/out-of-range
  paths; valid small contexts require the table. Missing world and corrupted
  table target fail strict mapped-read/owned-jump gates. No hardware-exception
  acceptance is inferred.
- Eight compiled semantic negatives: zero placeholder, missing/wrong world
  override, byte-truncated context, short-truncated world, wrong default and
  missing world2/world20 distinctions. Each must change a bounded return
  result, not merely differ in compiler bytes or fault on unsupported ISA.
- **2688 connected dispatcher cases** execute both compiled classifiers,
  original100-word dispatcher, mask and list-search instructions. Vary seven
  identities, eight worlds, eight actor-flag inputs, two list shapes and three
  mutation modes. Complete external storage and calls agree with the
  independent effect reference; callbacks remain bounded models.
- Full-owner and production gates bind typed source/prototypes, all150 original
  targets, context addend, existing warnings, complete original640-byte owner,
  neighboring linked code and unchanged10785 guard rows.

The first preinstallation bundle passed four positive tests and all copied
owner gates, then correctly failed the production-source assertion because the
placeholder was still installed. The remaining three guest/connected tests
passed separately before source installation. This was a staging failure,
not a compiler/source mismatch; final post-link regression is required below.

## Production Verification

Explicit ELF rebuild passes. Compared with `a1c20f4d`, all6059 slot addresses/
extents remain fixed and **only func_15141CC0 changes**. All57 linked words
equal retail; actor45/dispatcher100 words remain byte-exact. Target SHA-256:
`8c2208291eed47fdd5f33142ea20d52f7f1672a0cabaa5f3f409c4e7f37ab653`.
All10785 guard rows are unchanged, none for this function. Protected `.init`,
`.init_data`, `.debugger` and `.game_data` addresses/hashes remain unchanged.
All720 Game-data owners /189088 bytes match, zero differing owners/bytes.
Owner warnings remain3->3, zero new warnings; the build is not warning-free.

Refreshed converted counts/byte coverage are unchanged:5464/6042 total,
4791/5321 Game,85.57% total bytes/84.89% Game bytes. Exact total:
**3338/5464 (61.09%)**; Game **2665/4791 (55.63%)**, **2126 different**,
zero drift. Init492/492 and Debugger181/181 stay exact. This is a linked-function
measurement, not an overall matching-ROM checksum claim.

All **32 focused post-link tests pass in277.833 seconds**, no skips/errors/
failures: eight context tests, eight actor tests,11 dispatcher tests and five
actual padding-tool tests. **45 documents /3497 relative links /zero broken**;
`make tools-check`, syntax and diff checks pass. Ignored audit, compiler,
native/guest and test receipts are under `conker/build/game-context-classifier-test/`.

## Next Function

The intervening **func_15141DA4 is already exact across37 words**; skip it,
do not count it as another recovery. Continue **func_15141E38**,80 words /
320 bytes, frame0x60, VA15141E38..15141F78, ROM16F2E8..16F428. Its production
placeholder currently differs in all80 words.

1. Recover the void actor/index ABI and callers without disturbing banked slots.
2. Search the live actor+2F4 list for type1A using a private cursor. Every record
   with selector+28 equal to the index receives the live table count's low16
   bits at record+E; retain the last matching node. Do not stop at the first.
3. If any match exists, finish without allocation. Otherwise construct the
   12-byte index/actor/actor-byte3B payload at SP+40; byte tail padding is not
   initialized wholesale in retail.
4. Call func_15149130 with signed table halfword+6 and the original nine
   arguments. On non-null result, memcpy12 bytes to returned record+28, then
   func_1514EC1C(record,actor,0x1A). Preserve actor reloads and helper mutations.
5. Qualify native/guest alias and cursor lifetimes, failure paths, negative
   controls, actual relocations/padding and full production-slot audit before
   installing another function. Existing connected dispatcher proof models
   this helper; it does not restore its C body or prove allocator gameplay.

Ignored `next-updater.py` screens normal/private-volatile cursor assignments
across four actual-SDK profiles, eight controls with empty diagnostics.
Normal O2/g3 emits79 words/frame0x58/64 differences; private-cursor O2/g3
fits80 words/frame0x58/37 differences. O2 private form also fits80 words but
41 differences; O1/private80/frame0x48/79. The fitting length is not matching
acceptance: retail frame0x60, actor home, payload/cursor offsets, register
schedule and live-read/semantic/native/negative qualification remain. No
updater source/profile/guard installation or additional progress increment.

Root README stays aggregate-only. No sibling source/build/save, frozen
Release, runtime launch, host adoption, hardware/gameplay acceptance or push.
