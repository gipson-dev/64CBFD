# Game Ribbon Alpha Defined Signed Scaling

Continue from [Note 1167](1167-game-ribbon-effect-constructor-direct-match-20261009.md).
Start clean at parentf06d6da9/tools468cd97. One Codex writer, zero Claude
calls. Older standalone HEADddbdd16 retains all88 initial status entries
and its two dirty tracked-file hashes. User requests ongoing local commits;
bank tools before the exact parent pin, no push.

## Result

**func_151490C8 was already byte-exact.** Both original and revised complete
bodies emit all15 retail words directly under O2/g3 and O2, frame0, pools0,
relocations0 and guards0. Do not award another match or conversion.
VA151490C8..15149104, ROM176578..1765B4; see
[owner](../../conker/src/game/generated_175250.c) and
[full retail assembly](../../conker/asm/175250.s).

The source's signed16 duration shifted left3 is undefined C behavior for
negative values. Replace just that expression with multiplication by8.
The entire signed16 domain produces signed32 products -262144..262136,
without overflow or a negative shift. IDO still emits the identical sll.
Preserve the upper clamp at256 and byte truncation; there is no lower clamp.
Values0..31 produce multiples of8; positive32 and above produce255;
negative values wrap the product's lowbyte. Return is always1 for valid
inputs. Retail itself contains the redundant bgez of an andi255 result;
retain it rather than inventing a C-only branch defect.

The callback is selector6 in D_8008A3F8, with the actual pointer at8008A410.
The dispatcher func_15147EB8 calls it after earlier processing when its
second selector is nonzero and the first phase has not failed. This turn
checks the actual table pointer and typed callback, not whole dispatcher
execution or hardware/gameplay acceptance.

## Focused Qualification

[Driver](../../tools/experiments/game_ribbon_alpha_candidates.py) and
[seven-test suite](../../tools/tests/test_game_ribbon_alpha_match.py) reuse
existing compiler, MIPS, native32, ELF, pool and padder helpers without
shared edits. Driver locally corrects the generic helper's first-word
frame heuristic for this frameless routine; no compiler profile changes.

Fresh pre-install tests: seven pass in16.020s.
Fresh installed tests: **seven pass in30.800s**, no skips.

- Original/revised O2/g3 and O2 match15 words directly; all four profiles
  for both bodies are screened. O1/g3 and O1 both emit22/frame8/21 differences.
  Final three-form/four-profile driver has12 complete rows.
- All65,536 halfword bit patterns,131,072 guest executions, full seeded
  memory and exact ordered access: signed16 load at actor+1C, pointer load
  at actor+98, one byte store at payload+1B. Both stack phases exercised.
- All13 reachable words covered. Words10/11 are retail's unreachable
  zero-return arm, not fabricated coverage.
- 192 boundary/alias/phase cases include writes overlapping duration and
  all four captured payload-pointer bytes. Seven missing-byte pairs compare
  fault prefixes and memory; these are emitted guest order, not C fault guarantees.
- 589,824 actual native32 calls through s32(*)(u8*) cover every halfword
  across nine disjoint/overlapping arrangements, complete256-byte actor
  and payload canaries and return1. Native fixture follows existing
  -fno-strict-aliasing configuration; no sanitizer/hardware claim.
- Copied-owner assembly postprocess and actual padder preserve all ten
  neighbors, complete text, pools and relative relocations. Four compiled
  negatives are effective: unsigned input, wrong scale, low clamp,
  wrong output byte. No suppressed compiler diagnostics.
- Four independently assembled/linked symbol sets, eight links and48
  boundary cases retain exact15-word bodies; no relocations are present.
- Whole installed ELF is **byte-identical**, including all symbols/metadata.
  Progress and guard CSVs are byte-identical. Protected Game data remains
  189,088 bytes/720 owners, zero differing bytes/owners. Callback selector6
  points to the actual routine in the linked ELF.

Whole-ELF audit needs the immutable local pre-edit baseline. In an otherwise
prepared clone without that ignored baseline, retail body/table checks run
but installation-history audit explicitly skips; do not call that a fresh
successful history audit. This checkout has the original baseline and no skips.
Older ribbon-renderer suites are historical, not rerun. Constructor evidence
is retained; its installed bytes and the complete linked ELF do not change.

## Build And Evidence

Fresh make -C conker -j4 build/conker.us.elf progress.csv and
make -C conker match-progress NON_MATCHING=1 both exit0. Existing
generated_12D630 duplicate-recipe warnings remain.
Total3,407/5,489 exact62.07%, Game2,734/4,816 exact56.77%,
Init492/492, Debugger181/181, zero drift and2,082 different.
Conversion totals unchanged; guards remain11,510. Root README unchanged.

Ignored conker/build/game-ribbon-alpha-test contains immutable before-source,
before-elf/guards/progress, baseline.json and shape/guest/aliases/native/
owner/rebases/audit receipts. Final driver catalog lives in game-ribbon-alpha.

| Artifact | SHA256 |
| --- | --- |
| Before source | 21fe841571ac73c81a0668183767ecd4b0c96c51cf5803b11e815a60c6e2fd24 |
| Revised source | 9f1e8e7759513691c9b835a41986066a3dbf1172cd8dbf3d51ee47476e6ca148 |
| Before/after ELF | 054e17ad283ea120ed7e8a370ceb5c378cad08f891cd88ee872150e6902f4751 |
| Before/after guards | 1d9d7c6c3c0f0905aa40cd9f58c1d39c2aa46ec1aad9c8e7f0d097cdca8fc030 |
| Before/after progress | 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24 |

Protected Game data SHA256:
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

## Next Actual Matching Target

Tools0269fbbef6e8b09d09fce0ca7bf12dccb3a3ab9e banks the driver/suite first, exact parent
pin follows. Both tools checks pass;55 AST/exact-mirror pairs and154
documents/4,342 relative links/zero broken pass. Older checkout ends with90
entries while preserving all88 initial entries and dirty hashes, HEAD unchanged.
Manual graphify update exits1 refusing17,120 nodes over retained38,898;
19,398 excluded-but-existing nodes remain, no force/reinstall/purge.
Existing version/devcontainer warnings remain; wait parent hook separately.

The live non-exact list distinguishes already-exact callbacks from targets
still needing recovery. Do not repeatedly audit151490C8 for new credit.
func_150A76F0 remains a handwritten live-register fragment with a jrV0
continuation contract, explicitly excluded from ordinary C matching.
Keep unresolved func_1514803C renderer register/FP work pending.

Move to **func_151B2F04**, VA151B2F04..151B2FA0, ROM1E03B4..1E0450,
39 words/156 bytes. Its current C is a false zero-return placeholder.
Complete retail is in [asm/1DF510.s](../../conker/asm/1DF510.s),
owner [generated_1DF510.c](../../conker/src/game/generated_1DF510.c).
The actual callback-table pointer is8008A920 in
[data/22EF80.rodata.s](../../conker/asm/data/22EF80.rodata.s).
Recover its kind0x2D gate, two endpoint/byte associations, repeated reads
and aliased pair-update order. A void(u8*,packet*,u8) interface is inferred
from this body; inspect the actual dispatcher and qualify it before installation.
Initial semantic observation, not a matched body.
Game goal stays active.
