# Game Random-Effect Timer Restoration

Date: 2026-10-09

## Result

Continue [Note 1147](1147-game-record-constructor-restoration-20261009.md)
under the [focused workflow](../AGENT_WORKFLOW.md), one Codex writer and zero
Claude calls. Restore complete `func_151D9EB0` in
[game_2062D0.c](../../conker/src/game_2062D0.c):
VA 0x151D9EB0..0x151D9FC0, ROM 0x207360..0x207470,
**68 words / 272 bytes / frame 0x60**. Replace the false zero-return C
placeholder with its semantic void callback body. **Every word emits directly
from C, no guards or normalizer**, under the existing O2/g3 profile.

Fresh full linked audit starts at parent 2d2fae54/tools ce159a5 and permits
only this target's original 272-byte instruction slot and its own symbol-size
field (12 -> 272) to change. All 6,058 slot addresses/extents, every other
function body and every other ELF byte remain unchanged. Protected data,
all 11,475 guards and progress CSV bytes are unchanged. No Makefile,
retail assembly, input, layout or guard edit. New ELF SHA-256:
`a5f34fcf2e18cf4081264157bc7e4fac0264b8bef3160a38756892bcfba455a1`.

The false C placeholder already counted as converted; **converted counts and
bytes do not increase**. Fresh match-progress measures:

| Section | Converted | Converted bytes | Byte-exact | Drift | Different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,484 / 6,042 (90.76%) | 1,938,336 / 2,256,728 (85.89%) | 3,397 / 5,484 (61.94%) | 0 | 2,087 |
| Init | 492 / 539 (91.28%) | 151,796 / 164,048 (92.53%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,811 / 5,321 (90.42%) | 1,766,900 / 2,072,880 (85.24%) | 2,724 / 4,811 (56.62%) | 0 | 2,087 |
| Debugger | 181 / 182 (99.45%) | 19,640 / 19,800 (99.19%) | 181 / 181 (100.00%) | 0 | 0 |

Root README updates its two affected exact rows only. The 6,042 main slots
exclude 16 overflow symbols; progress has 6,044 records because two section
headers repeat. The wider Game goal remains active.

## Recovered Contract

The routine is a **void owner callback**, consistent with D_8008A4E8 and the
actual dispatcher; do not invent a zero or fixed return. The record begins
at owner+0x28. Read the full step D_800BE9E4, subtract it from the signed
halfword timer, store the wrapped halfword and reload that stored value.
Unsigned 32-bit subtraction avoids signed-overflow undefined behavior while
retaining the retail subu/sh sequence. Halfword narrowing follows the prepared
IDO/GCC target implementations; this is not a portable hardware-fault claim.

A nonnegative stored timer exits without reading expiry-only data or calling
RNG/effect helpers. On expiry, call `func_150ADA68()` first, preserve its float
across `func_150ADA20()`, then load live D_800AB464/D_800AB468 and effect fields.
Compute the float as separately rounded multiply then add. Integer RNG words
are treated unsigned: `% 41U + 35` determines duration, and the second integer
RNG after the effect call supplies `% 111U + 30` for the final timer write.

The effect call has sixteen O32 argument words: owner+0x30, &D_800A5480,
unsigned record selector +0x16, computed float, s16 duration, record kind
+0x14, bit-preserved scale +4, zero flag, two 1.0f scales, record mode +0x15,
zero extra, active one, zero, owner channel +0xC and owner context byte +1.
Recover the local `func_151D9014` prototype's actual pointer/float/byte/short
types and pointer return; its retained assembly and all other owner functions
remain unchanged. RNG/effect mutations must affect later live reads. Keep
the original record pointer across calls and overwrite its timer only after
the final RNG returns.

## Fitting

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_random_effect_timer_candidates.py)
tests 29 complete forms, including declaration permutations, early/late record
pointer lifetime, typed/volatile alternatives and five effective compiled
negatives. A late record pointer emits 65 words/frame0x58 with 45 differences;
keeping it live from entry emits 68 words/frame0x60 with two float-save-slot
differences. Declaring the random integer before the float recovers the retail
SP+0x54 save/load. The complete selected stream has zero differences.

Retail private state is owner saved in s0 (SP+0x48), RA+0x4C, saved record
pointer+0x50 and saved random float+0x54. The outgoing area covers sixteen
argument words through SP+0x3C. A callee can overwrite all sixteen homes
without damaging the live pointer, float or saves. No new frame adjustment,
word patch, insertion, omission or padding is used. Twelve relocation uses
retain their original symbols/types. Four profile measurements: O2/g3
68 words/0 differences, O2 68/8, O1/g3 73/72 and O1 73/72. No profile edit.

## Qualification

The [eight-test suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_random_effect_timer_match.py)
reuses the existing Timer/Shaping/Triangle oracles, native32 harness, owner
compiler, object/pool parsers and padder. The independent reference models
the complete callback and public access order; no new instruction emulator.

- **8,092 cases / 16,184 executions** compare selected/retail with independent
  call arguments, public reads/writes, live mutation effects and memory.
  Cover signed timer boundaries, wide steps, unsigned RNG boundaries,
  all five byte fields, eight finite float bit patterns, six mutation/home
  clobber modes and both SP phases. All 68 words execute; selected/retail
  complete GP/FP/private-memory/event state agrees. No invented void result.
- **288 real missing-byte pairs** qualify public read/write fault prefixes.
  Non-expired trimmed fixtures need only stack, timer and step mapping;
  expiry-only fields/globals are not speculatively read. This is emitted-code
  model evidence, not portable invalid C behavior or hardware traps.
- **328,968 actual native32 C cases** exhaust all 65,536 timer values across
  five step values, all 256 values in each of five unsigned byte fields, and
  eight float bit patterns. Check call order, all sixteen typed effect
  arguments, timer reset and full 512-byte canaries. RNG and effect are
  bounded native stubs; physical FCSR exception/rounding modes are not proven.
- **120 connected cases / 240 executions** enter the complete linked
  45-word `func_15149264` dispatcher through actual D_8008A4E8 slot **74**,
  whose word at 0x8008A610 points to this callback. Qualify owner duration
  decrement flag and timer callback behavior; 30 dispatcher words and all
  68 callback words execute. Cleanup/deletion paths, effect implementation,
  RNG implementation and hardware/gameplay acceptance remain separate.
- Preserve **61 copied-owner neighbors**, all pools, relative relocations and
  six existing diagnostics, including retained GLOBAL_ASM functions. Actual
  pad_c_object emits exactly 272 bytes without `.space` or guards. Four
  independent GNU links qualify **144 cases**, including HI/LO carry and
  J26 regions. This is not a separately rebased original-assembly pair.
- Five effective compiled negatives: ignore the step, expire at zero,
  shorten the first random range, fix the reset without the final RNG call,
  and omit the float multiplier. Each changes observed public behavior.

Fresh pre-install eight-test run passes in **34.734s**, no skips. Fresh complete
post-install run passes in **36.990s**, no skips; fresh **24 shared padder/
linker tests pass in 0.490s** and both local tools checks pass. Production
build succeeds with the existing duplicate generated_12D630 recipe warning
and six unchanged C diagnostics, not a warning-free build. Prior unchanged
neighbor suites are historical receipts, not newly rerun wholesale.
Fourteen tool files parse and match the older mirror exactly. Scoped link
validation checks **134 documents / 4,150 relative links / zero broken**.

## Receipts And Banking

Ignored receipts live in `conker/build/game-random-effect-timer-test/`:
baseline.json, before.elf, before-retail_word_patches.us.csv,
before-progress.csv, slot.json, guest.json, faults.json, forms.json,
owner.json, native.json, caller.json, linked.json and after.json.
Do not commit binaries, progress CSV or temporary sources/receipts.

```sh
python3 -m unittest tools.tests.test_game_random_effect_timer_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Per "Keep commited", bank mounted tools
**061d2233cb1ca594084de4f0a133442d0ca570d3** first, then exact parent source/
docs/gitlink. Mirror only the two absent new files after exact-byte checks;
the older mirror's status changes only by those two paths. Preserve standalone
HEAD ddbdd16, independently dirty shared helper/effect test fingerprints and
all unrelated work. Do not reset, duplicate history or push.

No OGL/Release, runtime/save/editor, bridge, dependency or account changes.
Manual Graphify refresh refuses 16,909 nodes over retained 38,698 and preserves
19,398 nodes from 2,972 excluded files still on disk; do not force overwrite.
Graphify reduced-corpus repair and hardware/gameplay remain open. Keep the
wider Game goal active and root README function narratives out of scope.

## Next Work

Recover **func_151DA6F8** in the same owner:
VA 0x151DA6F8..0x151DA938, ROM 0x207BA8..0x207DE8,
**144 words / 576 bytes / frame 0xD0**. It remains a false zero-return C
placeholder with 143 differing linked words. Recover the complete mixed ABI,
request/payload construction, live table/flag choices, 15-argument
`func_15147DA0` call, optional 12-byte copy into created->payload+0x48 and
preserved returned pointer. Keep unspecified padding and allocation failure
explicit. Capture its actual owner/linked baseline before fitting; do not
infer completion from retained neighboring assembly or this callback's match.

Follow-up: [Note 1149](1149-game-table-driven-effect-constructor-restoration-20261009.md)
installs that complete semantic constructor, C144/frame0xD0, with 61 remaining
linked differences and no guards/progress credit. Continue its layout/
scheduling work from the qualified body, not the removed zero placeholder.
