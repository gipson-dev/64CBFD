# Game Owner Captured-Object Metadata Adapter Byte Match

Date: 2026-10-10

## Baseline And Result

Continue after consumer18c6cb8581e3044d021e4453c6c031315d841c4f and mounted
tools1e345c1b87bf105eaeb0c0033fd98ac3fdad1be2, both active checkouts clean.
[Note 1205](1205-game-owner-fixed-span-point-initializer-byte-match-20261010.md)
banked the neighboring fixed-span initializer. The independently dirty older
tools checkout remains at ddbdd16b53ce60b054fb6e11bf0649a41f48375a, with166
existing dirty entries. Mirror only the two absent newly authored files;
preserve its HEAD and both tracked-dirty fingerprints, with no older commit.

func_151B4A14: VA0x151B4A14..0x151B4B78, ROM0x1E1EC4..0x1E2028,
89 words /356 bytes, frame0x68. Replace its zero-return placeholder in
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c) with the complete
fourteen-argument metadata adapter. All89 linked words match through a closed
register-renaming recipe. This is semantic C plus89 dependency guards, not a
plain-C match. No added accesses, scheduling changes, pools, omissions or padding.

Scoped Graphify queries and complete retail routines inform the existing
compiler/parser/MIPS/native32/padder/ELF/data workflow. Single Codex writer,
zero Claude calls; no shared helper/profile changes, OGL, Release, saves,
editor work or push. Keep the wider Game goal active. Root README gets only
aggregate row updates.

## Recovered Contract

Accept owner, eleven32-bit output pointers and two byte outputs. Capture the
object pointer at owner+0x150 once. Call func_1502EC34 with that object and
four local32-bit output addresses. Only after the call, read the captured
object's mode byte at+0xA4. Do not cache that mode before the call or reload
owner+0x150 afterward: the helper can mutate either field independently.

For an odd mode, write mode words0x200005/0x60600, full-width local red/green/
blue, alpha255, then opacity into primB/primG/primR in that order. Write primA255,
render mode0x100000, byte bank5 and byte combine0x2F. Output aliases make this
ordering observable. Return the saved unsigned byte result, initially1.

For an even mode, forward all fourteen original arguments to the already
recovered func_151B498C. Truncate its return to an unsigned byte before returning
it as s32. The fallback's actual34-word retail body remains unchanged.

Registration is D_8008FB10[1] /0x8008FB14, ROM0x2345D4. The complete475-word
func_151B32C8 renderer dispatches through owner+0x2E with the recovered output
interface; the table and caller stay unchanged.

## Compiler And Physical Homes

[Candidate driver](../../tools/experiments/game_owner_metadata_adapter_candidates.py)
measures18 complete forms /21 compiles including four selected-form profiles.
Existing O2/g3 is retained. Compact locals already emit89 words but frame0x58
with46 differences. Reordered locals with three consecutive unused words emit
89/frame0x68/24 differences but place the colors/object four bytes too low.
Split the three reserved words around the used locals to recover every home:

| Value | Relative To Incoming SP |
| --- | --- |
| Saved RA | -0x2C |
| Opacity, blue, green, red | -0x20, -0x1C, -0x18, -0x14 |
| Captured object | -0x10 |
| Saved unsigned result | -0x1 |
| Unaccessed reserved words | -0x24, -0xC, -0x8 |
| Four incoming register argument homes | +0x0, +0x4, +0x8, +0xC |

The selected complete C body emits89 words, original frame0x68, no diagnostics/
pools and15 raw word differences. Reserved names describe measured allocation,
not recovered original variable names. They are never read/written; all three
words can be unmapped in guest qualification. A scratch-record alternative
matches frame size but emits88 words with77 differences and changes result
store/read lifetime; it is not installed. Other optimization profiles do not
satisfy the selected full-shape gates.

The recipe consumes all89 expected compiler words, allowing only relocated
JAL target bits at+0x3C/+0x144. It reads no retail bytes to construct replacements.
Rename15 branch-local register fields for the255 constant, opacity value,
final combine pointer and fallback output-pointer producers. All accesses,
physical homes, branch offsets, delay slots and instruction order are unchanged.
All89 manifest rows certify15 changed words and74 unchanged dependencies,
including both R_MIPS_26 relocations. No stale-layout bypasses.

## Fresh Qualification

[Focused suite](../../tools/tests/test_game_owner_metadata_adapter_match.py):
all ten tests pass before installation in20.265s and after in22.991s.

- 8,192 guest cases /24,576 executions cover every mode byte, four full-width
  callback output patterns, four independent mode/owner-pointer mutations and
  both stack phases. All89 original/raw/normalized words execute. Entire memory,
  calls, return, saved GP/FP/SP and full ordered access events agree with an
  independent physical-home reference.
- 72 positive alias/status cases cover outputs overlapping each other, object
  mode, owner pointer and private red/opacity homes. A callback can mutate the
  saved result byte. Six effective complete compiled negatives reject an early
  mode read, object reload, narrowed color, wrong custom word, reversed aliased
  stores and untruncated fallback return.
- 166 three-body fault-prefix comparisons include public, private frame and
  incoming/outgoing argument homes. Unmap all three reserved words without
  affecting behavior. This qualifies emitted guest order, not portable C faults
  or real hardware exception behavior.
- Actual native32 selected C passes8,192 complete-memory cases and4,096 output
  alias cases, with hostile callback mutations and a full-width0x102 fallback
  return. Only the expected unused-padding-variable warning is suppressed in
  that GCC fixture; the selected body itself is unchanged. Callback helpers are
  bounded models, not a claim that the production mode helper is restored.
- Twelve independent links/four entry-helper-default symbol sets and32 guest
  rebase cases qualify both JAL relocations. Original and padded objects agree.
- 240 connected cases execute the complete original150-word func_1502EC34 and
  34-word fallback across modes0..7/254/255, scalar/pointer opacity inputs,
  negative/zero/positive bounded cosine returns and both stack phases. Full
  private memory, calls and events agree. No-output helper modes preserve the
  same prior private bytes; this does not promise defined portable C outputs
  for an invalid odd mode with uninitialized locals.
- 64 full caller cases /192 executions connect the complete original475-word
  renderer,89-word adapter,150-word mode helper and34-word fallback. Modes0..7,
  two geometries, signed view boundaries and both stack phases agree with an
  independent nine-quad strip/metadata reference. Graphics and cosine callbacks
  remain bounded; this is not live rendering or actual trig/FCSR acceptance.
- Actual copied owner preserves all16 neighbors, raw bodies, relative
  relocations and pools with zero diagnostics. Actual padder preserves every
  other owner byte and the original func_151B4B78 address. It rejects each of89
  individually stale words at its exact offset and a stale JAL relocation spec.

Prior unchanged renderer/point receipts remain prior evidence, not fresh broad
reruns. Fresh copied-owner and entire-ELF audits prove their current bodies
unchanged. Preserve historical curve owner/ELF fingerprints; authorized neighbor
changes require a fresh scoped baseline for later curve work, not overwritten
historical receipts. No live game/emulator/hardware qualification.

## Linked Installation And Bank

Fresh build/progress and make tools-check pass. Updating the shared guard
manifest triggers the normal wider rebuild. Existing duplicate generated_12D630
recipes, pointer/long-double and old compiler fullwarn warnings remain. Isolated
and copied target-owner compiles are clean, not the entire project build.

The complete rebuilt ELF equals the baseline after replacing only the356-byte
target slot and symbol extent. Normalize symbol/string order; decoded metadata
agrees. Old guard bytes remain an exact prefix, with only89 qualified target
rows appended. Conversion CSV is byte-identical. Protected data remains exact:
189,088 bytes /720 owners, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
The registered pointer, original helper stub and all other functions stay unchanged.

Fresh matcher: Game2,750/4,816 (57.10%), total3,423/5,489 (62.36%),
Init492/492 and Debugger181/181 exact. Zero address drift /2,066 different.
Converted counts/bytes remain unchanged because the placeholder was already C.
Bank tools89d71af552e07736258575124f969d7a01e56008 first, then consumer source,
guards, docs, aggregate rows and pin. Both new files are exact older mirrors;
its HEAD/tracked-dirty fingerprints stay unchanged. No push.

Manual graphify update exits1, refusing a39,263 to17,482-node shrink. Retention
keeps19,398 nodes from2,972 excluded-but-present files. Existing0.9.20/0.9.26
and zero-node devcontainer.json warnings remain. No force/purge/install or policy
changes; qualify the fresh consumer post-commit hook separately.

## Next Target: Mode Helper

func_1502EC34 remains a zero-return placeholder in
[generated_58F80.c](../../conker/src/game/generated_58F80.c). The connected tests
above use its original retail body, not the current production stub. Restore
this next to make the captured-object metadata path meaningful in production.

VA0x1502EC34..0x1502EE8C, ROM0x5C0E4..0x5C33C,150 words /600 bytes,
frame0x28. Accept object and four32-bit output pointers; return value is unused.
Mode byte+0xA4 selects seven cases; mode0/>7 returns without output writes:

- Mode1: RGB bytes+0xA5/+0xA6/+0xA7. Unsigned word+0xA0 below256 is direct
  opacity; otherwise dereference it as f32, clamp to0..255, multiply by the
  protected2.55f constant and truncate.
- Modes2/3: zero RGB, opacity from+0xA5; mode3 uses255-opacity. Preserve the
  mode reload after output stores, which can be observable under aliases.
- Modes4/5: capture high packed byte from+0xA0, with fresh packed RGB reads
  after preceding output stores. Call cosf on phase+0xA5 times the protected
  pi/128 constant; preserve rounded arithmetic and the post-opacity-store
  +0xA7 reload used by the final blend.
- Modes6/7: packed RGB with fresh reloads; opacity is255 minus the captured
  high byte times the later phase byte, shifted right8.

Protected jtbl_80096F1C has seven entries at ROM0x23B9DC, followed by
D_80096F38=0x40233333 /2.55f and D_80096F3C=0x3CC90FDB /pi/128.
Owner rodata anchor is jtbl_80096DF8_game in the existing generated_58F80 profile.
Recover complete C, table/pool ownership, alias order,0x28 frame/private homes,
cosine ABI and all150 words; preserve every other owner function and data byte.
Requalify the newly matched adapter/renderer against the actual installed helper.

Preserve the separate uninstalled curve func_151B3FDC handoff in
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
Its186-word/frame0x120 diagnostic qualifies fourteen float homes but shifts
saved writes8 bytes downward and overflows32 bytes. One complete form must
combine original frame0x118/saved homes, private accesses/lifetimes and178-word
extent before full matching. No curve matching credit is added here.
