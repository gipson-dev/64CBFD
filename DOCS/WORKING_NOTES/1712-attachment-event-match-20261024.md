# Attachment Identity Event Match

2026-10-24. Fully qualified, installed, production-built, adopted and freshly
recounted. Complete semantic C passes its checked operand normalization.
This is guarded semantic C, not a compiler-only match. The wider 75% exact-C
goal remains active.

## Target And Baseline

- Function `func_150C5D0C`, owner `generated_F2820`.
- Body VA `0x150C5D0C..0x150C5DB8`; ROM `0xF31BC..0xF3268`.
- Body: 172 bytes / 43 words, frame `0x18`, one call binding.
- Preserve the two alignment words through VA `0x150C5DC0` / ROM `0xF3270`:
  the complete slot is 180 bytes / 45 words.
- Consumer predecessor `9138a01d58b64a194a06816ab7362e50b7beaaf5`.
- Tools-first commit `e451e2c251362806533adab08d36120622d38e89`.
- Original assembly stays in `conker/asm/F2820.s`; normal O2/g3 is unchanged.

Capture verifies 16,014 native/cache files, including all 1,454 linker objects,
and 44 focused immutable inputs. WSL uses the existing PSBBN stdin/tar bridge,
not project reads through DrvFS. Snapshot SHA-256:
`d3f1e5a4bbf383151d77e70996e1f0861aa66556acdbab789a84f22c9cc20b49`.

## Recovered Semantics

[The source](../../conker/src/game/generated_F2820.c) now implements
`void func_150C5D0C(u8 *owner, s32 eventAddress, u8 command)`.
Private `AttachmentIdentityF2820` exposes only the saved word at owner `+0xC8`
and key byte at `+0xCC`; it does not invent a complete shared object schema.
The identity word remains opaque signed 32-bit storage.

For command zero, compare the saved word with the event's first word. If equal,
release through `func_1516972C(owner)` without reading the key. Otherwise compare
the saved key with event byte four and release if equal. This is an OR gate.
Preserve the owner-word-before-event-word and owner-key-before-event-key reads.

For command `0x2D`, capture the saved word before reading the event's first
word. If the first event word matches, store its second word as the identity,
then load event byte nine as the key. Otherwise, if the second event word
matches, store the first word, then load event byte eight as the key. The first
match wins when both match. The word store must precede the key read: aliases
can change the event byte. Unsupported command bytes read neither the saved
state nor the packet. The guest stores the full incoming A2 word at incoming
SP+8 before masking its low byte.

The existing 18-word `func_150C5CC4` dispatcher already declares the canonical
`void (u8 *, s32, u8)` callback interface. No caller/header edit is needed.
Actual registry `D_800887C8` has NULL at VROM `0x22D288` and the target at
`0x22D28C`. The aligned prepared-ROM scan finds this one literal function
pointer and no direct JAL. The frozen ELF has the same table words. The caller
and all 14 other owner functions remain unchanged, with no second credit.

## Checked Normalization

Four initial source forms and six valid lifetime forms preserve 43 words but
leave five differences. A parameter-reuse control leaves eleven differences.
A private C89 mixed-declaration fixture was corrected and rerun; it was not a
production defect. The selected source keeps the complete retail control flow.

The five derived expected-word guards close one A0/V1 lifetime exchange:
word 24 loads the current identity into A0 rather than V1; word 25 loads the
first event word into V1 rather than A0; word 26 compares those renamed roles;
word 36 stores the renamed first-word role. Word 34 applies the same role
mapping and exchanges the operands of its commutative BNEL comparison.
No instructions are inserted or omitted; no branch displacement or binding
moves. Keep unreachable duplicate load word 33 literally, not just the 42
reachable words. All 43 payload words and the complete 45-word linked slot
match after the actual padder/assembler.

The complete raw-body hash and sole `R_MIPS_26` binding at `+0x44` to
`func_1516972C` are checked before derivation. Append exactly five guard rows,
preserving the complete previous CSV prefix byte-for-byte.

- Raw body SHA-256:
  `35fbff4b98bdaa7fe5279da1dcb01e4dfad42ce3c8909d88961c47f3d323950e`.
- Retail 45-word slot SHA-256:
  `9834a745b0f021073d9c56d1e7dfa21f240d9866adb41ba8905e476fbf23945c`.
- Qualified padded object SHA-256:
  `6b83f561c63e088f705aae6007b9f3949b91865e92abb8a92a618f3a95d0b633`.

## Qualification

Permanent tools are `experiments/game_attachment_event_match.py` and
`tests/test_game_attachment_event_match.py`. Both local copies pass eight
fresh checks before and after installation, with no skips or reused checks.
Pre-install runs take 246.693s / 246.474s; installed runs take 201.780s /
214.742s. The earlier primary development run also passes all eight in
257.126s. Shared tools checks pass in both copies, 1.370s / 1.448s.

- 18,408 guest cases cover all command/key bytes, full incoming command homes
  and eight alias layouts, including SP+8. Raw C has the public semantics;
  fitted retail preserves complete private state. All 42 reachable words
  execute and the dead word is checked literally.
- 32 connected release cases visit all 28 original and retained helper words,
  including the late kind reload, callback and fallback paths. Pre-bookkeeping,
  destructor and fallback providers remain bounded contracts, not recovered
  full helpers or new matching credit.
- 2,048 caller cases connect the original and retained 18-word dispatchers
  to the actual two-entry registry and canonical callback. Validate byte
  masking before the indirect call, not a guessed callback signature.
- Native32 O0/O2/O3 with trap UBSan each pass 786,432 target cases and 131,072
  dispatcher cases, with ten effective semantic controls. Include the actual
  retained release C. Typeless heap-backed fixtures avoid claiming portable
  struct/alias behavior from a differently typed backing object.
- 59 paired guest fault prefixes qualify emitted access order. Ignored modes
  need no mapped owner state or packet. An actually compiled MIPS early-read
  negative fails effectively. This is not portable C fault semantics.
- Six independent GNU links across three layouts rebase the call binding.
  Reject all 43 raw-word perturbations, binding/extent/history controls, an
  actual padder corruption and seven full-image corruptions.

These are bounded semantic, ABI and binary checks, not whole-parent gameplay,
hardware acceptance or complete lower-provider execution. Routine local
evidence suffices: zero Claude calls and no provider/configuration changes.

## Production And Image Audit

Normal shadow Make uses three commands. All 15 compact owner functions agree
with the qualified counterparts, the complete padded object agrees, and all
14 neighbors and pools remain fixed. No compiler profile change is required.

The independent full link and actual production Make agree on exactly 119
changed ELF bytes: 118 inside the target slot and one target symbol-size byte
(`12 -> 172`). There are no metadata exclusions or symbol permutations.
Production Make exits zero in 15.089s. All 6,054 other linked bodies and every
address stay fixed. Protected Game data stays exact across 720 owners /
189,088 bytes, SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Qualified production ELF SHA-256:
`f3a35907cc1d00c745215320d28623d4e495ae14c38ac9a8c459501e270fb0bb`.
All 16,014 inputs pass the post-production audit with only four mutable paths:
target source, guards, target object and ELF. The link script and progress CSV
remain byte-identical. Preserve the older tools mirror's 1,634 existing path
statuses/hashes and HEAD, adding only the two owned modules. Do not commit or
reset that independently dirty mirror.

## Fresh Progress And Next Work

The native adoption audit verifies all 16,014 captured inputs against the four
qualified overrides. Actual native ELF bytes are captured, streamed back and
freshly recounted with `match_progress.py`; only `func_150C5D0C` leaves the
unmatched queue. The recount exits zero in 5.364s.

| Section | Byte-Exact C | Different | Address Drift |
| --- | ---: | ---: | ---: |
| Total | 3,788 / 5,505 (68.81%) | 1,717 | 0 |
| Game | 3,115 / 4,832 (64.47%) | 1,717 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The threshold is 4,129 / 5,505: 341 more matches to 75%. The ELF-pinned queue
has 1,588 placeholders, 120 semantic/other entries and nine parser-unlocated
entries. These remain triage screens, not semantic or ABI qualification.
Next ordinary placeholder is `func_151A1E34` in `generated_1CC440`, 45 words.
Keep existing semantic-C `func_15014094` separate, and do not count existing
`Gfx *` body `func_1510D8C0` as a missing C definition because of its parser miss.

Focused validation uses the sealed Linux cache, the target unittest module
and each tools copy's `check_project_tools.py`. Equivalent root commands:

```sh
python3 -m unittest tools.tests.test_game_attachment_event_match -v
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin --version us --objdump mips-linux-gnu-objdump
(cd tools && python3 check_project_tools.py)
```

Use the captured Make inputs/guard timestamps from the production runner, not
an unrelated broad rebuild. The actual report uses the captured native ELF
bytes as `qualified/live-recount.elf`; it is byte-identical to the adopted ELF.

The root README receives aggregate rows only. Graphify was queried for the
target/caller neighborhood; the normal code-only commit hook refreshes the
parent graph. Audit old-node retention explicitly. The parent intentionally
filters `tools/`; separate zero-API-token AST extraction covers the two tools
modules without claiming parent membership. The existing filtered-corpus
warning is not a clean full-corpus re-extraction or proof of old-edge retention.
No push, host/Release or dependency changes.
