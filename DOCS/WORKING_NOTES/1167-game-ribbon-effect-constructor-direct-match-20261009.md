# Game Ribbon Effect Constructor Direct Match

Continue from [Note 1166](1166-game-camera-ribbon-register-lifetime-exclusions-20261009.md).
Parent1ca73b46 and mounted tools5f4973d were clean before installation.
One Codex writer, zero Claude calls; tools-first local commits, no push.
Preserve older standalone tools HEADddbdd16 and all84 initial status entries
and dirty tracked hashes. Register-screen copies already added two entries.

## Installed Result

**func_15148F1C matches all107 words directly from semantic C**, with zero
guards, zero pools and the original0xB8 frame. Replace its false12-byte
zero-return placeholder with the complete428-byte routine in
[generated_175250.c](../../conker/src/game/generated_175250.c).
Retail VA15148F1C..151490C8, ROM1763CC..176578; reference is
[asm/175250.s](../../conker/asm/175250.s).

The [complete-body driver](../../tools/experiments/game_ribbon_effect_constructor_candidates.py)
uses the existing scoped compiler helper without shared helper/profile edits.
Final ten-form/four-profile screen has40 rows. Selected O2/g3 and O2 both
emit107/0xB8/zero differences; selected O1/g3 and O1 emit117/0xB8/105.
Moving gravity/threshold assignments before ordered velocity products
recovers the original schedule. Grouping real float locals also matches.
No dummy locals, guards, padding or fabricated work is introduced.

The real allocator func_15147A80 copies28 request bytes. Recovering its
actual trailing s32 value field corrects the initial24-byte request hypothesis;
it is not dummy alignment padding. The original partial field writes leave
that field and reserved holes uninitialized, exactly as retail does.
Do not replace them with zeros or claim defined native padding.

## Recovered Contract

Typed12-argument mixed ABI:
u8 kind; f32 x/y/z; s32 count/yaw/pitch; f32 speed; s16 duration;
f32 gravity/threshold; u8 channel. Return is u8 pointer, preserving NULL
and nonzero delegate results. Only RA is saved at SP44; no savedGPR/FP pairs.
Request28 at SP9C, payload32 at SP7C, render32 at SP4C. Lookup values spill
at SP78/74/70; the fourth result remains F2.

Four byte-index lookups preserve order: pitch, pitch minus0x40, yaw, yaw
minus0x40. Unsigned32 subtraction followed by u8 truncation preserves
wraparound without signed C overflow. No approximate trigonometry is used.
Count is lowbyte of unsigned count+3; duration is signed low16.
Request active/mode are1 and XYZ remain bit-preserving inputs.

Payload flags8 become0x28 only for kind10, channel255, alpha255,
kind/gravity/threshold from inputs. Velocity products preserve float32
order: (speed*pitchValue)*yawQuarter, -speed*pitchQuarter,
(speed*pitchValue)*yawValue. Render words are0,1,0x160600,3,0x10,0x80,0x20;
bytes28/29 are0/9, remaining holes stay retail-uninitialized.

All15 func_15147DA0 arguments are preserved, including original channel
in argument14 and final1. The sole found script caller is the JAL at
15029740/ROM56BF0 in [asm/50D80.s](../../conker/asm/50D80.s).
That whole script caller is not executed by this bounded qualification.

## Qualification

The [eight-test suite](../../tools/tests/test_game_ribbon_effect_constructor_match.py)
passes after installation in **37.223s**:

- All107 words/frame/pools/diagnostics and five relocation uses match, no target guards.
- 5,504 guest cases/11,008 executions cover all107 words: all byte values,
  signed/unsigned width patterns, twelve float bit patterns, two stack phases,
  NULL/nonzero results, caller-scratch and argument-home clobbers. Compare
  raw28/32/32 packets, including seeded retail holes, and full result canaries.
- 512 connected cases execute actual27-word func_151423D8 and70-word
  func_15147DA0 with actual65-float D_8009A220 data. Allocator and memcpy
  remain bounded hooks; verify NULL and full descriptor/flags/render outputs.
- Copied-owner asm-processor/postprocess and real padder preserve ten
  neighbors, pools and relative relocations with zero compiler diagnostics.
- Five compiled negatives are effective: lookup order, missing kind10 flag,
  count+2, wrong Y sign and wrong channel.
- Whole-ELF audit permits only the target428-byte slot and its verified
  st_size12->428 field. All other bytes, symbols, addresses and metadata
  remain unchanged; conversion CSV and guard CSV are byte-identical.
- 688 native32 calls through the typed12-argument factory pointer verify
  defined fields, lookup order, both return paths and256-byte canaries.
  Native padding is not compared; NaN geometry is classified rather than
  asserted as hardware-exact payload bits.
- Four independently assembled/linked original/candidate symbol sets,
  eight links/five relocation uses/512 cases/1,024 executions preserve
  exact107-word equality across JAL regions.

Guest floating behavior is a bounded model, not hardware FCSR acceptance.
Neither whole allocator/script integration nor visible gameplay is proved.
The complete func_1514803C renderer remains assembly-backed and pending;
its historical pre-install whole-source/ELF hashes are deliberately
superseded, not recaptured. Its old suites were not rerun against this install.

Fixture corrections are explicit: initial copied-owner test lacked actual
asm-processor postprocessing; initial native harness failed GCC indentation
warning gates; initial installed audit omitted the required st_size change.
Fix these local fixtures without suppressing warnings or relaxing other bytes.
Direct script invocation lacked package context; run driver with python3 -m.

## Build And Progress

Fresh make -C conker -j4 build/conker.us.elf progress.csv and
make -C conker match-progress NON_MATCHING=1 both exit0.
Existing Makefile generated_12D630 duplicate-recipe warnings remain.

| Section | Converted Functions | Exact | Drift | Different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,489/6,042 (90.85%) | 3,407/5,489 (62.07%) | 0 | 2,082 |
| Init | 492/539 | 492/492 (100%) | 0 | 0 |
| Game | 4,816/5,321 (90.51%) | 2,734/4,816 (56.77%) | 0 | 2,082 |
| Debugger | 181/182 | 181/181 (100%) | 0 | 0 |

This was already counted as C: **one new exact function, no new conversion
row or byte credit**. Converted bytes remain total85.98%, Game85.33%.
Root README receives only its two aggregate match-row updates.
Guard CSV remains11,510 rows. Protected Game data at2148018976 remains
189,088 bytes/720 owners, zero differing bytes or owners.

## Immutable Evidence

Ignored receipts live in conker/build/game-ribbon-effect-constructor-test:
baseline.json, before-source/ELF/guards/progress, shape.json, guest.json,
connected.json, owner.json, negatives.json, audit.json, native.json and
rebases.json. Candidate catalog is in game-ribbon-effect-constructor.

| Artifact | Before SHA256 | Installed SHA256 |
| --- | --- | --- |
| Owner source | 176546c15a2cfbe36d0ff2335c0791ca1be737abc69679d88a232dc7735f8b89 | 21fe841571ac73c81a0668183767ecd4b0c96c51cf5803b11e815a60c6e2fd24 |
| ELF | 9882610856cfd36a0022c543d536b8b6817c335a3b74a95ce1c24abaea0e143e | 054e17ad283ea120ed7e8a370ceb5c378cad08f891cd88ee872150e6902f4751 |
| Guards | 1d9d7c6c3c0f0905aa40cd9f58c1d39c2aa46ec1aad9c8e7f0d097cdca8fc030 | unchanged |
| Progress CSV | 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24 | unchanged |

Protected Game data SHA256:
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

## Checkpoint And Next

Bank the two authored tools files before the exact parent pin, source and
documentation. Mirror only those absent files into the older checkout;
preserve all84 initial entries plus the two register files, ending at88.
No older commit/reset/push; no OGL/Release/save/editor changes.

Tools468cd973f1deb2a2f48c77e6a178fef9881595bc banks exactly the driver and
suite before the consumer pin. Both tools checks pass;53 AST/exact-mirror
pairs and153 documents/4,329 relative links/zero broken pass.
Manual graphify update exits1, refusing17,112 nodes over the retained38,888
and retaining19,398 nodes from2,972 excluded-but-existing files. Existing
version/devcontainer warnings remain; no force/reinstall or graph purge.
The parent post-commit hook is waited separately before final handoff.
The first parent hook completed with38,898 nodes/79,490 edges/3,620
communities; the final documentation-only amendment is waited separately.

Next audit complete func_151490C8: retail also retains the redundant
unsigned-byte negative gate. Audit its signed-shift C behavior and compiler
shape before changing it; do not mistake that branch for a C-only defect.
Keep the qualified13-home
renderer reference and its unresolved register/FP schedule. Game goal stays
active; no claim that all Game matching is finished.
