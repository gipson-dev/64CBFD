# Payload Link Swap Event Guarded C Match

Date: 2026-10-24. Consumer predecessor `555dec25`; tools predecessor
`d8ec9607`. Qualification tools committed first as
`af5ead1ead1c90221f9cd5c8bf22667c55bdabd4`. No push requested/performed.

## Recovered Routine

`func_151932E0`, owner `conker/src/game/generated_1BFDD0.c`:
VA `0x151932E0..0x1519338C`, ROM `0x1C0790..0x1C083C`.
These are exclusive body ends: 172 bytes / 43 words, frame 24, one binding.
The following four-byte NOP is alignment outside the function, making a
176-byte / 44-word slot. Preserve it without inflating the symbol extent.

Complete semantic C emits 39 matching words and four register-allocation
differences. Four expected-word guards close one A0/V1 role cycle and produce
the complete retail body. This is guarded C, not compiler-only. No inserted
or omitted instructions, branch-destination changes, relocation moves or
compiler-profile changes. Retain the original one unreachable body word;
the guest coverage visits all 42 reachable words, not a claimed 43.

Raw C SHA-256:
`00311607be3f803315d4dc1683cd884d1fe3dd2dd4cfc6aa0c38c74e301e89d2`.

Recover the actual `void(struct260 *, s32, u8)` callback interface. Reuse
the owner's existing `EmbeddedOwnerLink` and `OwnerLinkEvent` local views,
also used by the adjacent recovered `func_15193234`; add no global layout
or header changes. The incoming word is a guest packet address.

For byte command `0x2D`, compare the captured embedded owner pointer at
root+0x28 with the packet's before pointer, then its after pointer. Replace
it with the opposite pointer and corresponding identity byte +9 or +8.
First-match ordering matters when the pointers agree. For command zero,
release the root if the packet's first pointer equals the current link or
the link identity equals packet byte +4. That last byte is deliberately
not the packet's named identity fields +8/+9. Other byte commands ignore
the payload. Preserve narrowing, original access order and the late root
argument passed to `func_1516972C`.

## Checked Register Fit

| Offset | Expected C Word | Retail Word |
| --- | --- | --- |
| `0x028` | `8C430000` | `8C440000` |
| `0x02C` | `8CA40000` | `8CA30000` |
| `0x050` | `54790013` | `57240013` |
| `0x058` | `AC440000` | `AC430000` |

Derive these words by renaming A0/V1 throughout the closed words 10..24
window and commuting the two inequality operand pairs. The first comparison
is symmetric and remains byte-identical; only the four listed words change.
Pin the complete raw body hash and binding map before normalization, not
just the four local expected words. The sole binding at +0x94 remains
`R_MIPS_26:func_1516972C`.

Append exactly four rows while preserving every historical CSV byte and
existing line endings. No folds, inserted instructions, omissions or
relocation-bearing guard rows. Raw C is checked for public semantic
behavior; literal complete guest state, fault PC and branch-delay origin
equality are claimed only for original versus fitted code. Do not infer
portable native C behavior for guest private-home aliases or faults.

## Caller And Helper Boundaries

The sole aligned literal reference is slot 22 of the 74-entry
`D_8008A8D8` table, ROM `0x22F398`, pointer slot `0x8008A930`,
ROM `0x22F3F0`. No aligned direct JAL target references occur.

The actual parent is `func_15149434`, 23 words / 92 bytes / frame 24,
in `conker/src/game/done/game_1765E0.c`. Its byte selector is root+0x13.
Out-of-range selectors choose slot zero, NULL callbacks are skipped, and
the command is narrowed before indirect dispatch. Execute the complete
original parent for all selector bytes and relevant command/relationship
paths; preserve its source and complete object unchanged. Other callbacks
are bounded, not recovered or credited as part of this match.

Retain the currently byte-exact chain `func_1516972C` (28 words),
`func_151696DC` (20 words) and `func_15169804` (eight words). Execute every
word across signed count 0/1/3/127/128/255, type 0/1/2/7/255 and provider
selection. Preserve the cached scan bound and replacement semantics.
Lower type-specific callbacks and `func_15168B10` remain bounded services;
this is not complete native heap closure or hardware acceptance.

## Focused Qualification

Both tools copies pass eight fresh tests before and after installation,
zero errors/failures/skips, no reused checks. Primary/mirror pre-install:
27.168s / 27.370s; installed: 28.087s / 27.855s. Both shared tools checks
exit zero. Reuse the established event-family fixture/oracle and native
domain helpers without mutating their old target module or old receipts.

- 5,420 guest phases and 240 alias phases cover all commands, upper-word
  command inputs, pointer relationships, ordered writes, identity widths,
  helper effects and ignored/unmapped payloads. Visit all 42 reachable root
  words; retain the unreachable 43rd word byte-for-byte.
- Native32 O0/O2/O3 with trap UBSan: 2,631,680 cases per optimization,
  twelve effective defined wrong-C controls, and the actual C parent.
  Cover every selector byte. Use separately allocated owner storage and a
  typed event packet, explicit opaque bytes and fences; no undersized
  declared header object and no portable alias claim.
- 20,480 complete guest-parent phases visit all 23 words, including actual
  registration, unsigned selector bounds, fallback and NULL dispatch.
- 120 retained release-chain phases visit all 56 helper words; actual live
  helper bytes equal retail before qualification. Explicit lower-provider
  boundaries remain in place.
- Nine independent GNU links compare original, normalized raw and padded
  code at three root/helper placements. All 120 disjoint-rebase phases and
  866 fired literal root-access fault prefixes preserve complete fitted
  state, PC and delay origin. Nine raw-role negatives and seven strict
  whole-image corruption controls are rejected.

## Production And Preservation

Preserve all five raw/padded owner neighbors, including `func_15193234`,
owner pools and the complete caller object. Diagnostics remain unchanged;
the isolated function has none. The actual three-command Make recipe uses
normal IDO `-O2 -g3` and reproduces qualified raw/padded code and metadata.

Seal 15,926 initial native files, then add the two owned tools files in
both copies for 15,930 files / 30 focused inputs. Cover all 1,454 linker
objects. Verify every static/non-target byte in the Linux cache and native
checkout; only source, guard CSV, target object and ELF receive audited
overrides. Use native checked streams, not DrvFS source reads.

Independently predict and reproduce the entire ELF: exactly 119 changed
bytes, 118 target-code bytes and one symbol-size byte. Zero metadata
exclusions. The target extent grows from 12 to 172 bytes, not 176. Preserve
all other 6,054 function bodies, all 6,055 addresses and the alignment word.
Protected Game data remains exact: 720 owners / 189,088 bytes,
SHA-256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production Make exits zero in 0.526s, reproduces the independent image and
qualified object, then both copies pass the eight fresh installed tests.
Audit native adoption against all 15,930 manifest entries before and after
promoting the exact generated artifacts. Recapture the actual adopted live
ELF and recount that stream independently, rather than crediting a private
candidate or an inferred increment.

Installed ELF SHA-256:
`af5894403d84c78df0b9c28198bdc75a51a02adf229f3c711a83bb82edeee4e8`.
Installed object SHA-256:
`de10b6e63fa2ef3e752cc710f6bcab664bcb6065c36b62fba548f294cc1b328e`.

Preserve all 1,592 independently dirty older-mirror paths, statuses and
hashes and its HEAD. Add only the two new owned qualification files there,
leaving 1,594 dirty paths; do not reset or commit that older mirror.
Do not change host Release, saves, configurations, ROM inputs or providers.

## Measured Progress And Resume

| Section | Byte-exact C functions | Address drift | Still different |
| --- | --- | --- | --- |
| Total | 3,763 / 5,505 (68.36%) | 0 | 1,742 |
| Game | 3,090 / 4,832 (63.95%) | 0 | 1,742 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

One newly qualified function is removed from the ELF-pinned queue. Remaining
source-shape screens: 1,611 placeholders, 122 semantic/other definitions,
nine parser-unlocated entries. These screens are not ABI or C qualification.
`func_1510D8C0` already has a `Gfx *` definition missed by that simple parser;
its earlier private screen and `func_1518C850` remain unmatched/uncredited.
Continue the 44-word queue; keep the 862-word `func_1508CAD8` stub separate.
The 75% threshold is still 4,129 exact functions: 366 more, goal not complete.

Keep only the two aggregate matching-row changes in the root README.
Use the normal consumer commit hook for Graphify and audit the owned worker
completion, changed-file hashes/membership and old-node retention. No
forced reduced-corpus extraction or invented graph provenance stamp.

Ignored evidence: `conker/build/game-payload-link-swap-event/qualified/`.
Tools: `tools/experiments/game_payload_link_swap_event.py` and
`tools/tests/test_game_payload_link_swap_event.py`.
