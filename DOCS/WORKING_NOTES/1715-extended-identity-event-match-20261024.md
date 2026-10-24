# Extended Identity Event Match - 2026-10-24

## Result

Recover `func_150F1020` in `conker/src/game/generated_11C2B0.c` from its
zero-return placeholder. The complete semantic C body, plus eleven checked
register/read-order normalizations, matches all 45 retail words. This is a
guarded match, not a direct compiler-only match.

The production object and ELF were adopted on Windows and freshly recounted:

| Section | Exact C functions | Matching |
| --- | --- | --- |
| Total | 3,791 / 5,505 | 68.86% |
| Init | 492 / 492 | 100.00% |
| Game | 3,118 / 4,832 | 64.53% |
| Debugger | 181 / 181 | 100.00% |

Address drift is zero; 1,714 C functions still differ. The 75% threshold is
4,129 / 5,505, requiring 338 more matches. Only `func_150F1020` receives new
credit. The retained dispatcher and release helper were already exact.

## Original And Interface

- Original: `conker/asm/11C2B0.s`, VA `150F1020..150F10D4`,
  VROM `11E4D0..11E584`.
- Body and slot: 45 words / 180 bytes, frame `0x18`, no alignment tail.
- Binding: one `R_MIPS_26` at `+0x9C`, to `func_1516972C`.
- Canonical interface: `void(u8 *, s32, u8)`. Keep the existing two identical
  `func_1516972C(struct102 *)` declarations; no shared header changes.
- Private payload view exposes the saved word at owner `+0xA8` and byte key
  at `+0xAC`. It makes no claims about the owner's remaining fields.

Command `0x2D` exchanges the saved identity against the event's two words.
The first match wins. Store the replacement word before reading event byte
9 or 8, since aliased storage can change that byte. Commands zero and `0x43`
release through `func_1516972C` when the first event word or event byte 4
matches the saved word/key. A word match skips both key reads. Other command
bytes must not dereference the packet or payload in the emitted guest code.

The actual caller is `func_15131C2C`, in
`conker/src/game/generated_15D730.c`. Its existing complete 22-word/frame-24
C body remains byte-exact, and its entire owner object is unchanged. It first
tests owner word `+0x68` bit `0x4000`, then reads selector byte `+0x75`,
loads `D_80089878[selector]`, and skips NULL callbacks. There is no active
selector bounds clamp. Native active indices are therefore qualified only
over the actual 14-entry table; disabled selectors cover every byte value.

The target occupies table index 10. The one literal pointer is at
VROM `22E360` / VA `800898A0`; no encoded direct-JAL sites were found.
The immutable table is VROM `22E338..22E370`. Other table providers are
bounded argument/mutation/clobber contracts, not recovered full routines.

## Compiler Boundary

The complete isolated and owner-compiled C body has its original length,
frame and call binding, with eleven linked word differences. Derive only:

- Words 10, 11, 12, 20 and 22: exchange the retarget path's A0/V1 roles,
  commuting the second equality's operands.
- Words 31 and 32: restore the event-before-state read order.
- Words 33, 35, 36 and 37: close the following event/key register roles and
  commute the word equality's operands.

The full raw body hash and sole relocation are checked before deriving any
rows. No insertion, omission, frame change, branch displacement, or call
binding change is allowed. Preserve the original unreachable duplicate load
at word 19; the other 44 words are visited by qualified cases.

This owner's normal Make path has three commands: IDO `-O2 -g3`, the real
padder, and the assembler. There are no GLOBAL_ASM routines in this owner.
The Make shadow reproduces all 44 compact functions and the complete padded
object. All 43 neighbors, pools and non-target owner bytes are unchanged.
Existing warnings about another owner's duplicate Make recipe are retained;
the Makefile is not changed.

## Qualification

Both actual tools copies pass eight fresh pre-install checks, with zero
errors, failures, skips or reused checks. Final timings are 80.642 seconds
for the active copy and 78.831 seconds for the older mirror. Both shared
tools checks pass, in 0.108 and 0.106 seconds respectively.

- 9,728 partitioned guest cases cover every command/key byte, all supported
  commands, nine aliases, two stack phases, full incoming A2 homes, first-match
  priority and late key reads. Raw C has the expected public behavior; fitted
  and original code have identical complete private state.
- 13,920 connected original/retained dispatcher cases cover the real table,
  flags, byte argument masking and nested incoming homes. Active indices are
  0..13; every selector byte is covered when dispatch is disabled.
- 64 connected release cases execute all 28 original/retained helper words
  and verify late kind reloads after bookkeeping. Bookkeeping, callback and
  fallback providers remain explicitly bounded contracts.
- Native32 `-O0`, `-O2` and `-O3` with trapping UBSan each pass 786,432 target
  cases and 232,448 dispatcher cases. Use typeless heap-backed fixtures and
  canonical callback types. Runtime counters verify all 32 pattern/match
  combinations per command. Fourteen semantic controls and a compiled
  missing-flag dispatcher control are effective.
- 85 paired fault prefixes and 1,536 sparse disabled-caller pairs preserve
  emitted access order. Disabled dispatch needs no selector/table/packet
  mapping. Compiled early-payload, missing-flag, hoisted-selector and NULL-call
  negatives are rejected. These are guest instruction-fault checks, not
  portable C fault semantics or hardware acceptance.
- All 45 raw word corruptions, binding/extent/history corruptions and a real
  padder corruption are rejected. Six independent GNU links cover three
  entry/helper layouts. Seven strict-image corruptions are rejected.

Preflight corrections were fixture-only: preserve both existing release
declarations, expect the actual three-command Make path, and use the typed
pointer comparison in the native harness. EOF whitespace cleanup caused a
new seal and fresh suites; prior successful receipts remain archived. No
incomplete run earns matching or fresh-test credit.

After production installation, each copy passes two fresh checks: literal
owner/Make/table identity and strict full image/frozen inputs. Six unchanged
semantic checks are explicitly reused only under identical sealed inputs,
module hashes and qualified artifacts, plus exact actual source/object/ELF
identity. Do not describe these as eight fresh installed checks.

## Production And Preservation

Normal production Make passes in 0.464 seconds and reproduces the independent
prediction byte for byte. The complete ELF changes exactly 125 bytes:
124 target-code bytes and one symbol-size byte, from 12 to 180. There are
zero exclusions or metadata permutations. All 6,054 other linked bodies and
all addresses are fixed. All 720 protected Game data owners, totaling 189,088
bytes, remain exact.

The 16,026-file Native/cache seal covers all 1,454 linker input objects.
Native adoption verifies the complete closure before and after promotion,
with only four overrides: source, guard CSV, target object and ELF. The
adopted Native ELF's fresh recount takes 1.118 seconds and removes only this
function from the unmatched queue. Existing-C `func_15014094` and parser-missed
`Gfx *func_1510D8C0` remain separate, uncredited tasks.

Tools are committed first as `add059c3287b3f1e64f3feaeb604ea1d2c36ed05`.
The older tools mirror's 1,640 pre-existing changed paths and HEAD are
preserved; its only additions are the two owned qualification modules.
No mirror commit, push, package/global/provider configuration changes,
Claude calls, or host/Release changes are made.

| Artifact | SHA-256 |
| --- | --- |
| Snapshot | `3487b4f714aeac90ddda45b361b43d6459778326d465e0b171a1c142eb376912` |
| Raw 45-word body | `3012a2a5f78935a61829aca0d5511246cdd595eef2b1e8a09f236e7b407673b5` |
| Retail 45-word slot | `e550498c9d7ea950479f65f6cd857e731af11397ce1e239e3dbc39830ddafd79` |
| Qualified source | `1f930648ed76a6a1ba7ce62c11ff2963b46116c66b30ccd6a8dd384ef9d890bb` |
| Qualified guard CSV | `6e5bba5f5e904d7ee919822cb96414bf00fe5038a87ef2dbe04699ea561c0456` |
| Qualified target object | `e9456ee36d6e5a00a5e2dd6f3bc62b4d810f5cc617873f2eaa9b4906fffb5491` |
| Adopted ELF | `37453ffe5c12ed22d3ef731ac0f583111d3f792bffe94bc80dcb33238fb4e182` |

## Next

The ELF-pinned queue now contains 1,585 placeholder-shaped C definitions,
120 semantic/other definitions, and nine parser-unlocated entries.
`func_1517E080` is the next ordinary placeholder. Its private tail-walk/list
constructor C matches all 45 linked words directly, without guards, but
caller/ABI/guest/native/fault/owner/padder/Make/whole-image qualification and
production adoption remain pending. It is not counted. Keep the wider 75%
goal open. The root README carries only aggregate rows.
