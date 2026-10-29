# Working Note 1799 - Record timer update byte match

Date: 2026-10-28

`func_150A019C` replaces a zero-return placeholder with the semantic timer update in `conker/src/game/generated_CD5A0.c`. Its complete 200-byte slot matches retail after two checked array-end relocation normalizations. The caller's local declaration in `conker/src/game_45B80.c` is corrected from `s32` to `void`.

## Recovered behavior and interface

The routine is `void func_150A019C(void)`, at VA `0x150A019C..0x150A0264`, ROM `0xCD64C..0xCD714`. It has 50 instruction words, no stack frame, no arguments and no return value.

It scans ten 12-byte records at `D_800D3010`, stopping at `D_800D3088`. The two high flag bits must both be set. The next four bits select unsigned halfword period and limit values. The elapsed field accumulates the bit pattern of `D_800BE9E4` using unsigned 32-bit wrap. If it reaches the period, the routine subtracts one period, increments the value once and applies unsigned remainder when the limit is nonzero. A large delta still consumes only one period per update.

`GeneratedCD5A0Flags` gives the existing byte view, the timer bitfield view and a word view of the same header. The value and elapsed fields are unsigned. The four neighboring routines use the byte/word views and retain identical raw and padded instructions. IDO establishes the required N64 bitfield layout; native tests initialize the bitfields logically and do not establish cross-platform packed-byte layout compatibility.

The period label at ROM `0x22CFD0` precedes the limit label by 12 bytes. Its six named halfwords are `2, 6, 60, 3600, 20864, 0`. The oracle verifies 44 original bytes spanning the adjacent tables. Testing all four-bit kinds does not imply that the original period label defines a 16-element standalone C array.

## Compiler and relocation evidence

The complete owner was compiled with its existing IDO `-O2 -g3 -mips2 -o32` profile and the actual Make/padder/assembler recipe. All four target-owner neighbors remain unchanged. The original assembly and normalized object have ten matching relocation bindings.

Two expected-word guards rebind offsets `0x004` and `0x020` from `D_800D3010 + 120` to the original `D_800D3088` end label. The high word is unchanged; the low word's addend becomes zero. There are no scheduling guards, removed instructions, inserted instructions or profile changes. The inherited guard CSV is preserved byte for byte before the two appended rows.

The untouched IDO object links correctly through GNU at all three tested layouts, including signed-low-half carry boundaries. A separate diagnostic found that the generic assembly reconstruction helper loses the original relocation-pair order when start and end addends share a symbol. Its two carry-boundary failures are retained as negative controls. This is a reconstruction-helper limitation, not a compiler-object defect. The explicit retail end label makes reconstruction unambiguous; no shared helper was changed.

## Original caller and semantic qualification

The sole full-ROM direct call is the JAL at ROM `0x476B4`, VA `0x1501A204`, within `func_15019F20`. There are no aligned full-address pointer words for the target. Its six-word original call-and-return window is executed in 36 cases with the parent's existing 24-byte frame and an ignored return value. This is bounded caller-window evidence, not complete parent or gameplay acceptance. All 16 caller-owner routines and the entire padded caller object remain byte-identical after the declaration correction.

Eight fresh qualification methods pass in each tools checkout. The measured coverage is:

- 6,148 direct guest cases, covering every flag-byte pattern, unsigned wrap, thresholds, the one-period rule and suppression of the one-past header read.
- 49 reachable target words. The 50th word is the compiler's unreachable divide trap at `0x150A024C`; it remains part of the literal byte comparison.
- 36 original caller-window cases and 12 guest-only alias cases. The alias cases do not claim portable C behavior.
- 27,648 native 32-bit SDK cases at each of `-O0`, `-O2` and `-O3`, with trapping UBSan and nine effective semantic negative controls.
- 164 direct and 15 caller fault-prefix comparisons, including 46 direct delay-slot cuts, with state, PC and trace comparison.
- Three GNU address layouts, 90 rebased guest cases, 60 raw-word/binding corruption rejections and one incorrect-end-alias rejection. All three untouched IDO object links are exact.
- Nine compiled semantic controls, each terminating without incidental faults, and 59 strict-image corruption rejections.

Target-owner compilation is diagnostic-free. The caller owner retains the same three existing Warning 712 pointer/integer diagnostics at lines 567, 574 and 606. The existing duplicate `generated_12D630` Make recipe warning also remains; none was introduced by this recovery.

## Production, image and progress

The production Make run rebuilds both changed source owners and reproduces the private object and linked image. Both installed tools copies rerun the source/object and whole-image checks; six unchanged semantic checks per copy are reused only with exact input, module and qualified-artifact fingerprints.

The independent whole-image prediction accounts for all 167 changed bytes: 156 target code bytes, one target extent byte and a closed ten-byte symbol/string serialization permutation between `D_80088510` and `D_800D9910`. Named definitions retain their values and bindings. No image region is excluded. All 6,055 other canonical function bodies and all 6,056 addresses are fixed. All 189,088 protected Game data bytes across 720 owners remain exact.

The live audit preserves all static paths in the 16,491-file seal. The older tools mirror retains its 1,838 inherited dirty paths and receives only the three new qualification modules. Tools are banked first at `4a20d04`; the consumer commit includes the two sources, two guard rows, tools pin and seven documentation files. No push is performed.

| Section | Exact C | Drift | Different |
| --- | ---: | ---: | ---: |
| Total | 3,877 / 5,506 (70.41%) | 0 | 1,629 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,204 / 4,833 (66.29%) | 0 | 1,629 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The 75% threshold is 4,130 exact functions: **253 more are needed**. The remaining screen has 1,500 placeholders, 120 semantic/other entries and nine unlocated entries. Next inspect `func_150F0198` in `generated_11C2B0.c`; `func_1514E920` remains parked and uncredited. The root README changes only its two aggregate progress rows.

## Retained local evidence

The ignored stage is `conker/build/game-record-timer-update-match/`. It retains the frozen 433-input snapshot; original assembly; raw owner and caller compiles; actual Make commands and diagnostics; original, raw and normalized GNU links; both canonical qualification receipts; production and live-adoption audits; actual-ELF recount; canonical function inventory; and source-scoped Graphify refresh receipts. Graph refresh retains or uniquely relocates old nodes and accounts for old relationships; it does not claim a full-corpus extraction or recomputed global clustering.

- Retail slot SHA-256: `21aea7f2baa711c81d46743117b018df83184e2f2363094a63ca5a2f9882277f`.
- Untouched selected body SHA-256: `6d693f3f57972620bdb00204a56844b6bb578c32633e008b3a2ee4ff1b7295cc`.
- Qualified padded object SHA-256: `5be7fe310b84aa2e75d3964ed9ebefc51be10d91e299d5199f5bea124b872f7d`.
- Adopted ELF SHA-256: `e85af7c47fd8491a2d2fb28b8f025e0e5ff48e8bd529756b0476451fdec694ae`.

Committed qualification modules are `tools/experiments/game_record_timer_update_match.py`, `tools/tests/game_record_timer_update_oracle.py` and `tools/tests/test_game_record_timer_update_match.py`.
