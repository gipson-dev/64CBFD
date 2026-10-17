# Sequence State Reset Installed Guarded Match

Date: 2026-10-16. Consumer predecessor **203c1dc9**, tools predecessor
**199b23f**. Continue the same-owner handoff from
[Note 1463](1463-priority-record-maximum-installed-guarded-match-20261016.md).

## Installed Contract

func_1501D044 in conker/src/game/generated_49D30.c replaces its false
zero-return stub with **void func_1501D044(s32 slot)**. All **100 linked
words / 400 bytes** match retail: VA **0x1501D044..0x1501D1D4**, ROM
**0x4A4F4..0x4A684**. The complete C emits 100 words, normalized by exactly
**13 guards**. This is a **guarded match, not direct compiler output**.

Preserve frame **0x18**, RA at **SP+0x14**, the existing O2/g3/no-unroll
profile and all **56 raw owner neighbors**, including the 105-word maximum
scan, 97-word loader and 239-word graphics-task parent. No inserted/omitted
instructions, frame growth, save-slot change or call-boundary repair.

The routine performs **34 ordered stores before its helper and two after**:

- Capture D_800969C0 before indexed stores. Its actual protected retail
  value is **999.0f / 0x4479C000**. Copy that captured value to both float
  limits later, rather than embedding a new literal or reloading it.
- Use a four-byte stride for the selected slot's word fields and a one-byte
  stride for byte fields. Correct the donor draft's incorrectly scaled
  pointer indexing instead of copying it as matching C.
- Preserve the signed **-100**, signed byte **-1**, signed halfword **-1**,
  unsigned byte **255**, active byte **1**, shared byte **100**, positive
  float-zero stores and the observed halfword/word widths.
- Keep the final **SH** of D_800C3C9E in the JAL delay slot at **0x1501D1B0**.
  The call at **0x1501D1AC** targets the already recovered void helper
  func_150233BC. Its ten retail words clear **0xA8 bytes** at D_800C3CA0
  through SDK bzero; its body remains unchanged and byte-exact.
- Clear D_8008FD84 and D_800C3670 **after** the helper returns. Comments name
  the capture/order boundary and the post-call clears. Keep address-based
  symbols; the state-reset description is a behavioral summary, not a
  speculative global or function rename.

The current caller in conker/src/game_34F20.c now has the proper local
**void(s32 slot)** declaration. All **six raw caller-owner functions** remain
identical, including the complete 33-word func_15008248. Do not regenerate
unrelated global headers or widen their historical declarations here.

## Bounded Matching

Seven source-shape screens retain the existing owner profile. The plain
body has 100 words / 73 differences; explicitly capturing the float limit
recovers 100 words / **13 differences**. Const/register variants do not
improve it. Chaining the limit stores grows to 102 words and is rejected.

Pin every raw word, **75 relocation bindings**, empty private pools and the
independently assembled original words/bindings. Normalize only:

- **Seven opening instruction positions**, target/source offsets
  **0x04/0x10, 0x08/0x04, 0x0C/0x14, 0x10/0x08, 0x14/0x0C,
  0x18/0x1C, 0x1C/0x18**. This moves independent initialization, including
  the RA store, without changing its save slot or crossing an outgoing call.
- A closed **F0/F2 allocation swap**, including the opening MTC1/LWC1 and
  six float stores at **0x7C, 0x84, 0x8C, 0x11C, 0x134, 0x13C**.

After that routing/swap, every complete instruction and relocation binding
must equal the original. No GPR repair, changed immediate, width, store
value, helper packet or new instruction is accepted. Preserve every existing
guard byte and its **298 CRLF lines**; append only the thirteen target rows.

Raw C SHA-256:
**8335ddc383022ef73f53ab03c77cdb4081fe2b92f1472f9cb5ec6f31ee5f801d**.
Original unlinked text:
**9e64f2b01a82d0f5481cc419d694b72f5a72e6794b4f6a2be3121c5448b8b1b8**.

## Fresh Qualification

All **eight pre-install tests pass in 24.308s**. After installation and the
normal rebuild, all **24 final tests pass in 170.864s**, no skips:
eleven reset tests, ten previous maximum-scan tests and three previous loader
installed-image/checkpoint tests. Other unchanged loader semantic/native/
startup receipts remain historical in Note 1463, not fresh tests this turn.

- **640 three-way guest cases** compare original, raw C and guarded reset
  emission with an independent ordered reference. Visit all 100 words in
  each form, preserve saved GPR/FPR/SP state and check the helper-entry
  snapshot and both post-call clears.
- **128 three-way real-helper cases** execute its actual ten words and
  verify the **(D_800C3CA0, 168)** bzero packet. SDK bzero is a bounded
  byte-clear/ABI hook, not instruction-level SDK or hardware emulation.
- **288 native32 cases each at O2 and O0 with UBSan**, separate actual
  body/caller/provider units and no fwrapv. Check all typed object, pointer,
  padding and canary bytes, plus the entire helper-entry snapshot. Use the
  actual SDK struct163 layout, **56 bytes per record / 168 total**.
- Four diagnostic mutation gates fire positively, including changing the
  captured limit after the call, changing pre-helper fields, setting the
  post-call flags and changing the cleared table's final byte. Native and
  guest checks verify the fired gates, not just configured mode values.
  These mutations belong to an **opaque diagnostic helper**, not retail
  bzero. Real-helper cases use its clear-only contract with no such mutation.
- **Eight effective native controls** fail with functional/protocol exits
  **21 or 22**: wrong word stride, wrong -100 sentinel, missing active byte,
  early flag clear, late halfword sentinel, missing float limit, missing
  helper call and byte-truncated halfword sentinel. All build and execute;
  no compile failure, signal or sanitizer trap counts as a control.
- Explicit guest-only signed/wrapped slots include two cases whose indexed
  stores overwrite the float-limit source. Both copies still use its entry
  value. The native valid-array domain is slots **0 and 1**; negative/high
  slots and non-retail float bit patterns are synthetic guest evidence,
  not portable C alias or natural gameplay acceptance.
- **119 fired original/guarded memory-access fault prefixes** preserve
  literal private memory, GPR/FPR, event, PC, delay and access state. Raw C
  is checked for public behavior, not identical opening private/fault state.
  Bulk provider writes are not claimed as emulated bzero instructions.
- **Three independent original/guarded links** compare all 100 words at
  HI16/LO16 carry boundaries. Raw/original word, binding, pool, routing, FPR
  scope and all **143 guard-field corruptions** fail closed.
- Verify the complete **33-word current caller** against ROM
  **0x356F8..0x3577C**. **144 three-way full-caller runs** execute both
  slot-0/slot-1 resets and its remaining table/flag loop, including the real
  helper chain in the clear-only domain. Its incoming argument is ignored.
- Independently assemble all **473 original words** of func_1501D348 and
  compare with ROM **0x4A7F8..0x4AF5C**. **24 three-way cuts** execute both
  branches of its real **0x1501D424..0x1501D458** window: S5-to-A0 branch
  delay, the two original argument spills, reset call, post-call reloads
  and next three-word packet. That next provider and the full 473-word
  caller remain unqualified; no return from the void reset is interpreted.

No full gameplay, host-port or hardware acceptance is inferred. Zero Claude
calls, no REA reinstall and no dependency/configuration change.

## First Whole Image Prediction

Independently reproduce the predecessor and predict every **3,257,636 ELF
bytes before installation**, replacing both padded owner inputs. The normal
**695-compile / 687-padder** rebuild equals that first prediction. Exactly
**651 bytes** change: **374 code bytes** inside the 400-byte reset slot,
**two extent bytes** changing size **12 to 400**, and **275 metadata bytes**.

Metadata is constrained to ten exact symbol/string permutations, not an
excluded section. The complete membership/order/definition tuples are pinned
in tools/experiments/game_sequence_state_reset_installation.py:SERIALIZATION.
All 24 affected named definitions remain identical. All other image bytes
and canonical definitions are unchanged except this function's size.

First predicted and normally rebuilt ELF SHA-256:
**17e327a95fcf43c50ac2611a19461980ad1d44664a3c3a218d593f35e26cd4ab**.
Installed source owner:
**98dd8f293ebdd3b47ced8a41c093f4ce5665bd3341fdf351699ebb37a22c0045**.
Caller source:
**b4dc09551e47e04e7f9fc80430b953050a0ccd74d899ab14e4bb3edb6e361e9a**.
Guard manifest:
**2e182911b8f362b3dc5fcf8e690b2fdb3d69ea2aa9ce0c459beb95bbcad79302**.

All **136 live inputs**, including **132 unchanged inputs**, pass the exact
successor audit. Unknown successors, all four before/after fixture pairs and
code/caller/guard/metadata corruptions fail closed. Protect **189,088 data
bytes / 720 owners / zero differences**. Existing Makefile/compiler warnings
remain; do not describe this as a warning-free build.

## Progress And Bank

Fresh official matching: Game **2,939/4,828 (60.87%)**, total **3,612/5,501
(65.66%)**, still different **1,889**, zero drift. Init stays **492/492** and
Debugger **181/181** exact among converted functions. Conversion remains
**5,501/6,044 functions / 86.04% bytes**; the previous stub already counted
as C. The regenerated conversion CSV is literally unchanged. Root README
changes only its two aggregate matching rows.

Tools **b7775f4** banks eleven files before the consumer pin. Synchronize
only nine new reset files and two exact previous scan checkpoint/test updates
to the older tools mirror. Preserve its HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **946 other initial dirty-file
hashes** and independently dirty history; **957 final dirty paths**. All
eleven pairs match. Across both copies, **22 Windows ASCII/AST checks** and
all eleven WSL padder tests per copy pass: active **0.030s + 0.019s**, mirror
**0.030s + 0.019s**. Consumer tools-check passes. No mirror commit/reset,
push, host-port or frozen Release action.

Reproduction in the prepared checkout:

```sh
python3 -m tools.experiments.game_sequence_state_reset_installation
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_sequence_state_reset_match \
  tools.tests.test_game_sequence_state_reset_native \
  tools.tests.test_game_sequence_state_reset_installed \
  tools.tests.test_game_record_maximum_match \
  tools.tests.test_game_record_maximum_native \
  tools.tests.test_game_record_maximum_installed \
  tools.tests.test_game_microcode_loader_installed -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Recover typed ordered stores, capture semantics, helper boundary and the actual void(s32) interface.
- [x] Qualify only opening/F0/F2 guards, real helper, both caller paths, native/guest behavior, rebases and fault prefixes.
- [x] Freeze the entire independent first image/owner/caller/guard prediction before installation.
- [x] Complete normal rebuild, all 24 final tests, exact successor/fixture gates and protected-data audit.
- [x] Measure official progress, update README aggregate rows only, preserve both tools copies and bank tools first.

Next: **func_1501D348**, still a zero-return stub in the same owner:
**473 words / 1,892 bytes**, frame **0x78**, VA **0x1501D348..0x1501DAAC**,
ROM **0x4A7F8..0x4AF5C**. Recover its gated resource/record setup, allocation
loops, signed/unsigned record fields and calls into the now-qualified reset,
count and maximum routines. Its two verified call windows are not a full-body
qualification. Timing's **141 differences**, wider Game/additional-source
recovery and full gameplay acceptance remain separately open.
