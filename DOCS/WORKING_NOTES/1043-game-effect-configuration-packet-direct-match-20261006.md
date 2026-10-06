# Game Effect Configuration Packet Direct Match

Date: 2026-10-06. Starting checkpoint: `47fd9a35`.

**`func_1519EA78` matches all 69 words / 276 bytes directly from C.**
VA 0x1519EA78..0x1519EB8C, ROM 0x1CBF28..0x1CC03C, frame 0x70.
Replace the false zero-return stub in
[generated_1CBE20.c](../../conker/src/game/generated_1CBE20.c) with a typed
five-argument wrapper and local 60-byte configuration view. Existing O2/g3;
no new instruction guards/profile/shared header/symbol/metadata/data edits.

## Recovered Handoff

Incoming arguments are a three-float position address, unsigned-halfword
selector, float scale, unsigned-byte channel and signed context. Copy the
three position words into the configuration. Capture selector in a 32-bit
local and scale in a **separate float local**, then call:

```c
func_15152190(&packet, &selected, &selectedScale, 1, 0.0f, 0, channel, context);
```

All 60 packet bytes are initialized; no invented padding stores:

| Offset | Stored Value |
| --- | --- |
| +0x00 / +0x04 | signed words 10 / 7 |
| +0x08..+0x10 | three copied position words |
| +0x14 / +0x16 / +0x18 / +0x1A | signed halfwords 0 / 255 / -53 / 24 |
| +0x1C / +0x20 | float bits 0x41200000 / 0x41000000 (10 / 8) |
| +0x24 / +0x28 | D_800A8CC0 / D_800A8CC4 float words |
| +0x2C / +0x2E | signed halfwords 50 / 20 |
| +0x30 / +0x34 / +0x38 | D_800A8CC8 / D_800A8CCC / D_800A8CD0 float words |

The five [retail anchors](../../conker/asm/data/24D640.rodata.s) retain raw
words BFA978D6, 3F3E76C9, 3F19999A, 3F4CCCCD and 41D174BD. Do not substitute
rounded decimal constants for those global reads. Local field names such as
speed, vertical and spread are descriptive interpretations of callee usage,
not a recovered original struct declaration.

[Retail caller](../../conker/asm/50D80.s), ROM 0x56244..0x562C8, constructs
a local three-float position, validates selector below 0xE9, computes scale
from a signed short or uses 1.0, passes channel/context one, and ignores the
return register. The wrapper has no meaningful returned C value. Retail's V0
survives the call/epilogue; tests check this register transport as a machine
fact, not a promised C return API. Full caller execution is not qualified.

**Important remaining dependency:** the 228-word retail `func_15152190`
configuration consumer remains a false zero-return C placeholder in
[generated_17CAF0.c](../../conker/src/game/generated_17CAF0.c). Its retail
[assembly](../../conker/asm/17CAF0.s) uses RNG, angle/vector generation and
effect allocation. This checkpoint restores the wrapper, not the complete
effect path. The callee is not installed, linked as retail, or qualified here;
guest/native tests use a typed opaque callback.

## Compiler Evidence

[Driver](../../tools/experiments/game_effect_configuration_packet_candidates.py)
screens eight forms under four profiles, **32 controls**, empty isolated
diagnostics. The initial direct `&scale` parameter-address form emits 68
words/frame 0x68, with 40 different words under O2/g3. Retail instead captures
incoming A2 through F12 and stores a separate float local at SP+0x2C.
Recovering this local gives exactly 69 words/frame 0x70, all retail instructions.

Moving that capture to the start of source keeps 69/frame 0x70 but has 41
differences. Selector-first, reordered local declarations, wider arguments and
scalar position stores do not fix the frame/body. Baseline profiles produce
66..68 words/frame 0x68; selected plain O2 produces 68/frame 0x70/62 differences.
Selected O1/g3 and O1 produce 70 words with 35 and 38 differences, counting
the overflowing word. Tests bind the full inventory. No schedule guards.

Ignored receipts: `conker/build/game-effect-configuration-packet/` and
`conker/build/game-effect-configuration-packet-test/`.

## Qualification

[Six tests](../../tools/tests/test_game_effect_configuration_packet_match.py):

- **1296 two-body guest cases** compare selected/retail with an independent
  packet-byte reference. Vary source versus global aliases, three memory
  patterns, high-bit selector/channel words, context, both stack phases,
  callback mutation and zero/nonzero V0. Check all 60 packet bytes and eight
  call arguments, complete external read/write/call traces and memory,
  exact private-local addresses and saved GPR/FPR/SP/RA lifetimes.
- **65536 selected-body guest cases** cover every selector halfword, every
  channel byte repeatedly, unrelated incoming high bits, both stack phases
  and ten raw float patterns. No float arithmetic in this wrapper.
- **100 additional two-body guest cases** vary source/global raw float patterns
  and incoming scale, including signed zero, subnormal boundaries, infinity,
  quiet and signaling NaNs. The bounded runner transports bits; this does not
  prove FCSR or hardware exception behavior.
- **131072 native cases** execute the actual selected C against a typed callback:
  every selector halfword twice, callback mutation disabled/enabled, all channel
  bytes, contexts with high bits and finite/quiet-NaN patterns. Check 60-byte
  configuration/12-byte position layouts, pointer size four, important offsets,
  all fields/scalars and the full 12-byte source plus all five globals.
  Signaling NaNs/subnormal host handling is deliberately not claimed.
- Five compiled negative controls detect stub, wrong count, signed selector,
  incremented channel and lost incoming scale. No shared runner changes.
- All **69 wrapper words** execute. The production check binds the complete
  direct slot/source, no target guards, and the unchanged callee placeholder.

No arbitrary private-stack aliases, invalid-memory access, MMIO/concurrency,
full caller/effect consumer, hardware/FCSR/gameplay or host adoption acceptance.

All **26 focused post-link tests pass in 219.250 seconds, no skips**: new
configuration wrapper, same-owner address allocator, conditional packet
allocator and earlier effect packet wrapper. This follows the 77-test baseline
regression pass in 468.864 seconds banked in `47fd9a35` before this recovery.

## Linked Audit

NON_MATCHING ELF/progress/match-progress rebuild passes. Across **6059 slots**,
only `func_1519EA78` changes; all addresses and sizes remain fixed. Init,
Init data, Debugger and Game data are unchanged. All **720 Game-data owners /
189088 bytes** stay retail-exact; all **10646 guard rows** retain content/order.
Previous `func_1519E970` direct match and the callee slot are unchanged.
Target SHA-256:
`19690b8633ed96859ece33614e0beebae245aa981bc3ec206356da531450d71e`.
Baseline/current complete owners compile independently through the normal
assembly processor with empty diagnostics. Existing duplicate recipe warning
remains; no project-wide warning-free claim.

| Section | Byte-Exact Converted Functions | Drift | Different |
| --- | --- | --- | --- |
| Total | 3321 / 5462 (60.80%) | 0 | 2141 |
| Game | 2648 / 4789 (55.29%) | 0 | 2141 |
| Init | 492 / 492 (100%) | 0 | 0 |
| Debugger | 181 / 181 (100%) | 0 | 0 |

Converted counts/bytes unchanged because the stub already counted as C.
README changes aggregates only. Tools-check, Python compile checks and
diff-check pass. All **3259 relative links across 26 documents** resolve,
zero broken. No sibling source/build/
save/frozen Release edits or push. Broad Game matching goal remains active.

## Next Work

Inspect `func_1519EB8C` in this owner, still a stub: **102 retail words**,
ROM 0x1CC03C, frame 0xB8. Five incoming arguments; it retains the first pointer
in S0, constructs a larger actor/effect packet with two scaled floats and two
copies of D_800A5480, calls `func_1513264C`, and conditionally copies the source
pointer to returned actor+0x170. Recover the exact packet/layout, signed versus
unsigned shorts, helper ABI and untouched bytes before installation. These are
static facts, not an installed recovery. The 228-word effect consumer and
projection/pair-clamp compiler-frame work also remain open.
