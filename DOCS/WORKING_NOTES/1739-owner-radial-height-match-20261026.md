# 1739 - Owner Radial Point And Height Outputs - 2026-10-26

The adopted Native ELF measures **3,816/5,506 byte-exact C functions (69.31%)**,
Game **3,143/4,833 (65.03%)**, zero address drift and 1,690 different.
Only func_151A8F6C gains credit. The converted inventory and byte totals stay
fixed; 314 more matches reach the 4,130-function threshold for 75%.

## Recovered body and interface

func_151A8F6C belongs to generated_1D4E00 and occupies VA
0x151A8F6C..0x151A9024 / ROM 0x1D641C..0x1D64D4. All 46 words belong to the
body, with no alignment word. The frame is 48 bytes; S0 and RA retain their
original lifetimes, and the original argument homes are preserved.

The void interface takes an owner pointer, a three-float output vector and two
float output pointers. Draw an integer angle and a floating radius factor from
the existing PRNGs, mask the angle to its low byte, and call func_15143874 with
the scaled radius and the vector's X/Z output addresses. Add the owner's X/Z
origin, copy its Y coordinate, then copy the two height values through the
remaining outputs. Preserve the repeated Y read and output ordering when the
outputs overlap owner fields or each other. Shared headers stay unchanged.
The original function name is retained; the source has an explanatory comment.

The complete parent func_151A8CEC materializes this callback at 0x151A8E10/
0x151A8E14 and calls S7 at 0x151A8E48. Its selector can choose func_151A8F1C
instead. The full parent remains a placeholder; its callback window is qualified
separately. The complete retail code inventory has no direct JAL to this target,
and the complete reference image has no aligned literal registration.

## Compiler and guard proof

Ordinary O2/g3 C emits all 46 semantic words with three R_MIPS_26 bindings at
0x1C, 0x24 and 0x5C. Raw SHA-256:
351a23424f0d56cb3b356ab9b938cc68bf507b6fe7969e53552fa819ca4beebc.
Two expected-word guards change the integer temporary's complete store/reload
lifetime from SP+0x28 to SP+0x24, at function offsets 0x28 and 0x30. All other
44 words, every binding, the frame and saved registers already match.
There is no inserted or omitted instruction, assembly body or compiler override.
This is guarded C. Every previous guard-manifest byte is an unchanged prefix.

The complete owner preserves all 22 neighboring routines and its data pools.
The normal compiler/padder/assembler reproduces all 23 compact functions and
the complete independently padded object. Owner diagnostics are empty. The
inherited generated_12D630 duplicate-recipe Make warning is unchanged.

## Fresh canonical qualification

Both tools copies pass six fresh canonical methods and their shared tools
checks. Each production copy subsequently runs two fresh input/image methods
and reuses four semantic methods only after complete module, snapshot and
qualified-artifact fingerprints agree.

- Expected-word, relocation and actual padder corruption controls reject six
  malformed guard cases, including an already-guarded input manifest.
- 2,816 guest cases cover all 256 angles and 16 output/owner alias shapes.
  Execute the original 25-word direction helper and 27-word trig lookup with
  the frozen 65-entry table. All 98 target/helper words are reached. Compare
  complete original/normalized states and traces, plus raw C public state
  and calls against an independent reference. All 184 fault prefixes fire.
- Native32 O0/O2/O3 each pass 4,096 finite cases with typed layout assertions,
  complete State canaries, SSE single precision and trap UBSan. Eight compiled
  semantic negatives fail with the intended status 23.
- The actual 17-word selector runs 1,024 cases, 768 choosing this target, with
  real caller stack output locations. Eight unused V0 values support the void
  interface. Unused selector fields have no mapped backing. S7 is a checked
  selector output; a declared two-word JR FP/NOP adapter ends the observation,
  and RA is excluded only there. The target's own frame/return still execute.
- Six independent GNU links cover three layouts and 288 rebased guest cases.
  All three bindings and both local stack guards remain correct.
- The shared literal whole-image checker rejects seven corruptions and three
  wrong input fingerprints, including file extent, a neighboring body, Game
  data and symbol size. No metadata exclusion is permitted.

The two PRNGs are bounded 64-bit seed-step contracts inspected against their
handwritten assembly. Their instructions are not claimed as executed 64-bit
MIPS emulation. Native inputs are valid aligned objects. The alternate callback,
full parent, arbitrary hardware faults/FCSR/MMU and gameplay remain separate.
The old private zero-count fault fixture is preserved and rejected; canonical
access() overrides the inherited counter and explicitly requires 184 fired
prefixes. The shared strict checker supersedes the earlier inequality screens.

## Production and continuation

Production Make exits zero in 12.302s and reproduces the independent ELF
a091b59b96890ff5f280310170a13db9f13df2106734eeaad900aa8001f69e40. The complete image delta is **134 bytes: 133 target-code bytes and one
symbol-size byte, zero exclusions**. Target extent changes from 12 to 184.
All 6,056 addresses, 6,055 other bodies and exact protected Game data remain
fixed: 720 owners / 189,088 bytes, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Source SHA-256: c8b5ce5bf19090cdf08665a89ac75bfdbc7fbf4f3b7990f8a1605b5c57ace26a.
Padded object SHA-256: 8456c6241131114558d59e48718132e185a2882f217f88cc7933527471f38a92.
Tools a5afa26fb1772a2f05e64d84ccb1b0641adfae87 are committed first, then pinned by the consumer.
Baseline consumer 7e3d0f07, tools af1ffab1, ELF 93b75e60.
The fresh Native seal contains 16,123 inputs and five qualified adoption outputs.
Preserve all 1,688 inherited dirty paths and the older tools mirror's history;
only the new owned pair is added there. The preparation driver's stale expected
hash and missing Native-to-cache receipt were corrected without recompiling
frozen objects; the original failures remain in the ignored stage. Three
indented blank lines in the test file were then cleaned, and all six canonical
methods were rerun freshly in both copies before the tools commit.

The scoped graph refresh covers eight changed C/Markdown files and must retain
or uniquely relocate all 44,332 prior nodes. Preserve historical communities and
out-of-scope manifest freshness. Tools AST extraction is separate from the
parent graph; no full-corpus extraction or global clustering is claimed.

The adopted queue has 1,561 placeholders, 120 semantic/other entries and nine
unlocated screens. Next is `func_151D08F0` (`generated_1FA770`), uncredited until its source/ABI,
guest/native, owner/Make and production gates close. The unresolved pointer/NULL
factory remains a placeholder. The 75% goal stays active. Routine Claude calls: 0.

Prepared-checkout focused command:

~~~sh
python3 -m unittest tools.tests.test_game_owner_radial_height_match -v
~~~
