# Lifetime Envelope Ramps Match

2026-10-24. Fully qualified, installed, production-built, adopted and freshly
recounted. Complete semantic C matches with two checked commutative multiply
guards. This is guarded semantic C, not a compiler-only match. The wider 75%
exact-C goal remains active.

## Target And Baseline

- Function `func_151A1E34`, owner `generated_1CC440`.
- Body VA `0x151A1E34..0x151A1EE8`; ROM `0x1CF2E4..0x1CF398`.
- Complete slot: 180 bytes / 45 words, frame zero, no bindings or alignment tail.
- Consumer predecessor `c031bb27fb936b6895603a6d2705657c911f6a59`.
- Tools-first commit `01d48085ca62fa5b1ffa2e334e44996ff0830f5b`.
- Original assembly stays in `conker/asm/1CC440.s`; normal O2/g3 is unchanged.

Capture verifies 16,014 old native/cache files and 49 focused immutable inputs.
The subsequent seal covers 16,018 files, including all 1,454 linker objects.
WSL uses the existing PSBBN stdin/tar bridge, not project reads through DrvFS.
Focused snapshot SHA-256:
`d395f30f9ef14d1e569f22f79c8b0fc8b222926f4570d7dd03584e4c56659832`.

## Recovered Semantics

[The source](../../conker/src/game/generated_1CC440.c) now implements
`void func_151A1E34(u8 *effect)`. Capture signed time at `+0x38` once, then
evaluate four independent strict gates using ten signed-halfword parameters
at `+0x50..+0x62`. Later matching ramps intentionally override earlier ramps.

| Gate | Result |
| --- | --- |
| `parameters[2] < time` | Store `parameters[0] * (parameters[1] - time)` to byte `+0x3F`. |
| `parameters[5] < time` | Store `parameters[3] * (parameters[4] - time)` to halfwords `+0x36`, then `+0x34`. |
| `time < parameters[6]` | Store `parameters[7] * time` to byte `+0x3F`. |
| `time < parameters[8]` | Store `parameters[9] * time` to halfwords `+0x36`, then `+0x34`. |

Preserve the signed comparisons, low-byte/halfword stores and independent
priority. Do not add clamps, NULL checks or a guessed full object schema.
The products remain within signed 32-bit range for signed-halfword inputs.

The prepared retail image has one literal target pointer at VROM `0x2314CC`,
VA `0x8008CA0C`: slot 17 of the 22-entry `D_8008C9C8` table. Slots 3, 4 and 8
are NULL; no direct JAL targets this function. Actual table-load sites are
VROM `0x195348` / VA `0x15167E98` and VROM `0x195E9C` / VA `0x151689EC`.
Use the ignored extracted originals under `asm/nonmatchings/game_1944C0/`
with scoped `rg --no-ignore`; default searches miss these files.

Both original callers pass A0 as the owner pointer and ignore the result:

- `func_15167E0C`: qualify the 17-word window `0x15167E80..0x15167EC4`,
  signed selector byte `+0x2F`, -1 sentinel, NULL gate, saved owner/death-byte
  homes and late `+0x38` reload.
- `func_15168870`: qualify the 13-word window `0x151689D4..0x15168A08`,
  signed selector byte `+0xB2`, -1 sentinel, NULL gate, saved owner home and
  late `+0x98` reload. The target still reads its own time at `+0x38`.

The original class table `D_8008B4A8` also registers these parents at classes
5, 14, 59 and 66 through its existing void-pointer callback interface.
No caller or shared-header edit is needed. Both larger parent C placeholders
remain unchanged and uncredited; these are bounded original caller windows.

## Checked Normalization

Fifteen complete private O2/g3 forms reduce the differences from 33 to 26 to
two. Mixed multiply source ordering does not improve the best complete body.
Derive exactly two expected-word guards by exchanging the `rs` and `rt`
operands of checked R-type `MULTU` instructions, with zero `rd` and shift:

| Word | Offset | Raw | Retail |
| --- | --- | --- | --- |
| 30 | `+0x078` | `03030019` | `00780019` |
| 39 | `+0x09C` | `01230019` | `00690019` |

Check the complete raw-body hash and empty binding set before derivation.
No instructions are inserted or omitted, and no branch or relocation moves.
All 45 words are reachable and match after the actual padder/assembler.
Append only these two rows, preserving the complete old guard CSV prefix.

- Raw body SHA-256:
  `d839fd0b5eb25ce4ca1bfdf6ceb98f3f8629f60b69c3326574a44b78c4bd43fb`.
- Retail body SHA-256:
  `8a87379f297099c2d78e634c31bf1e85c05d438ebe7cb8033ab911e8a3d7282b`.
- Qualified padded object SHA-256:
  `48a68d6b4c0cafb9b4f228b323319ba446fab3a69438a2072602d7f9b3894de8`.

## Qualification

Permanent tools are `experiments/game_envelope_gates_match.py` and
`tests/test_game_envelope_gates_match.py`. Both tools copies pass eight fresh
checks before and after installation, with no errors, failures, skips or
reused checks. Pre-install runs take 80.849s / 23.495s; installed runs take
64.095s / 57.408s. The earlier primary development run passes all eight in
74.676s. Shared tools checks pass in both copies, 0.263s / 2.745s.

- 4,352 guest cases cover four layouts, two phases, signed boundaries and all
  feasible gate masks. Raw and fitted execution agree on complete private
  state; every one of the 45 reachable words executes.
- 1,992 caller-window cases cover all 22 valid table slots and the -1 sentinel,
  saved owner homes, late reloads and stack-home input aliases. Other callbacks
  use bounded mutating/clobber contracts, not executions of all providers.
- Native32 O0/O2/O3 with trap UBSan each pass 1,048,576 target cases and 5,888
  dispatcher cases, with twelve effective semantic controls. Cover every
  16-bit timer pattern, eight presets and two halfword alignments. Typeless
  heap-backed fixtures use corresponding signed/unsigned halfword views;
  no portable stack-alias or fault semantics are claimed.
- 366 paired guest fault prefixes qualify emitted access order. Inactive
  coefficients and outputs may be unmapped. An actually compiled MIPS volatile
  early-read negative fails effectively.
- Six independent GNU links across three layouts verify the position-independent
  body. Reject all 45 raw-word corruptions, unexpected bindings, extent/history
  controls, an actual padder corruption and seven strict full-image corruptions.
- Four effective signed-selector/missing-reload controls qualify both caller
  windows. The -1 sentinel needs no table mapping.

These are semantic, ABI and binary checks, not whole-parent gameplay, hardware
acceptance or full-provider execution. Routine local evidence suffices: zero
Claude calls and no provider, package or configuration changes.

## Production And Image Audit

The normal GLOBAL_ASM owner Make recipe has five pre/compile/post/pad/as
commands. All 39 compact functions agree with qualified counterparts, the
complete padded object agrees, and 38 neighbors, six GLOBAL_ASM routines and
all pools remain fixed. The first copied fixture incorrectly expected three
commands; correcting that assertion required no production or profile change.
The inherited duplicate `generated_12D630` Make warnings remain.

Independent full link and actual production Make agree on exactly 122 changed
ELF bytes: 121 inside the target and one target symbol-size byte (`12 -> 180`).
There are zero exclusions or metadata permutations. Production Make exits zero
in 14.742s. All 6,054 other linked bodies and every address remain fixed.
Protected Game data stays exact across 720 owners / 189,088 bytes, SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Qualified and adopted production ELF SHA-256:
`b3ef88337d099ab44332d1abefdc183a5f7526a7c3e00ed98a84faa693fa2040`.
All 16,018 sealed files pass production and native adoption audits with only
four mutable paths: target source, guards, target object and ELF. Link script
and progress CSV remain byte-identical. Preserve the older tools mirror's
1,636 existing path statuses/hashes and HEAD, adding only the two owned modules.
Do not commit or reset that independently dirty mirror.

## Fresh Progress And Next Work

The adopted native ELF bytes are captured, streamed back and freshly recounted
with `match_progress.py`; only `func_151A1E34` leaves the unmatched queue.
The recount exits zero in 7.962s.

| Section | Byte-Exact C | Different | Address Drift |
| --- | ---: | ---: | ---: |
| Total | 3,789 / 5,505 (68.83%) | 1,716 | 0 |
| Game | 3,116 / 4,832 (64.49%) | 1,716 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The threshold is 4,129 / 5,505: 340 more matches to 75%. The ELF-pinned queue
has 1,587 placeholders, 120 semantic/other entries and nine parser-unlocated
entries. Unchanged source shapes are reused only under the strict source and
whole-image identity audit; this queue is triage, not semantic/ABI qualification.
Next ordinary placeholder is `func_151B1FAC` in `generated_1DD500`, 45 words.
Keep existing semantic-C `func_15014094` separate, and do not count existing
`Gfx *` body `func_1510D8C0` as missing because of its parser miss.

Equivalent focused commands from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_envelope_gates_match -v
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin --version us --objdump mips-linux-gnu-objdump
(cd tools && python3 check_project_tools.py)
```

Use the captured Make inputs/guard timestamps, not an unrelated broad rebuild.
The actual recount uses `qualified/live-recount.elf`, identical to the adopted
native ELF. Private receipts remain under `conker/build/game-envelope-gates-match/`.

The root README receives aggregate rows only. Graphify was queried for the
target/caller neighborhood; the normal code-only commit hook refreshes the
parent graph, with explicit old-node retention auditing. The parent filters
`tools/`; separate zero-API-token AST extraction covers the two tools modules
without claiming parent membership. The existing filtered-corpus warning is
not a clean full-corpus re-extraction or proof of old-edge retention.
No push or host/Release changes.
