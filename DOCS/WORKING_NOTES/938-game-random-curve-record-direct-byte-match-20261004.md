# Game Random Curve Record Direct Byte Match

Date: 2026-10-04. Starting HEAD: `e4943f9f`.

## Result

Replace `func_150E7994`'s zero-return placeholder in
`conker/src/game/generated_113D60.c` with its typed curve-record builder.
The complete 194-word / 776-byte routine now emits directly from semantic C
and matches retail, including its original 0xC8-byte frame. No compiler-profile
change, instruction guard, function-address movement or extra padding is needed.

Retail reference: `conker/asm/113D60.s`, `0x150E7994..0x150E7C9C`,
ROM `0x114E44..0x11514C`.

## Recovered Contract

```c
void *func_150E7994(s16 count, f32 value, u8 slot, s32 context);
```

The signed 16-bit count gate returns null for counts below two, before any
external callback or global load. Otherwise, the builder:

1. Calls `func_1512D748(D_800DBFF0 + D_800BE9E8 * 0x9A0, 0, 1)`.
2. Submits an eight-byte `RandomPacket113D60`: kind 1, duration
   `(u32)func_150ADA20() % 11 + 30`, count 8, mode 1, index -1. Submission
   arguments are zero, 255, zero; its return value is ignored. The two
   unwritten packet padding bytes remain unwritten and are not inspected.
3. Calls `func_151491F4(300, -1, 16, 1, 12, count * 8 + 16, slot, context)`.
   A null result ends the operation without metadata copy or float sampling.
4. Copies exactly twelve bytes to record +0x28: caller float, positive zero,
   signed count and zero halfword. Record +0x34..+0x37 remains untouched.
5. Samples four control-point Y coordinates as `sample * 160.0f - 80.0f`.
   Control X coordinates are **-146, -50, 50, 146**, not the preceding
   edge emitter's +/-145 constants.
6. Writes `count` interleaved X/Y float pairs starting at record +0x38.
   Parameter starts at -1 and advances by repeated float addition of
   `3.0f / (count - 1)` after each point. It is not recomputed from the index.
7. Returns the allocated pointer unchanged.

The four weight calls are, in order, `func_15142B04`, `func_15142AC0`,
`func_15142A80`, `func_15142B44`. All four are called separately for each
coordinate. X is stored before the Y calls. Arithmetic retains the retail
grouping: fourth product plus ((first product plus second product) plus
third product). Explicit float prototypes preserve the o32 argument/return
contract; the caller's second argument is a float in the mixed argument list.

The retained caller in
`conker/asm/nonmatchings/game_A9D90/func_1507CD64.s` invokes this function at
`0x1507D13C`, with unsigned RNG remainder modulo three plus four (4..6 points),
the computed float value, slot 255 and context zero. This is a live caller
contract, not evidence that the whole caller is recovered in C.

## Matching Shape

The first semantic build already reproduced the length, frame and almost all
flow. Corrected endpoint literals and the declaration order of the record,
payload, packet and controls recovered the retail stack layout. Six words
then remained: two closed temporary-register choices and two commutative
floating-multiply operand orders.

An interleaved `f32 *` output cursor with `i * 2` / `i * 2 + 1` indexing,
together with the recovered operand expression, removes all six directly.
The loop counter remains signed 16-bit. No instruction substitution is used.

## Verification

New suite: `tools/tests/test_game_random_curve_record.py` (five tests).

- Signed-count and narrowing rejection cases produce no callbacks or global
  dereference, even with deliberately invalid global setup.
- Allocation-failure cases preserve packet order/unsigned modulo and stop
  before metadata copy, four float samples or weight calls.
- Success cases cover counts 2, 3, 4, 5, 6, 7, 31, 127, 256 and 32767.
  Callback observations check all eight weight calls per point, repeated
  parameter addition, X-before-Y publication, prior-point completion, copied
  metadata and untouched record regions. The large buffer is a host fixture,
  not proof of production allocator capacity for arbitrary counts.
- Out-of-range float samples, cancellation-sensitive arithmetic, negative
  zero metadata, high-bit unsigned RNG results and slot/count narrowing are
  exercised. The freestanding 32-bit harness uses SSE single-precision
  arithmetic, no FMA, and explicit stack realignment.
- A warning-clean independent IDO O2 build checks payload offsets, original
  frame, exact call targets/order and **all 194 words against pristine retail**.
  This independent path bypasses production padding and word-guard tooling.

```sh
python3 -m unittest tools.tests.test_game_random_curve_record tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters -q -f
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
```

All **26 focused tests pass in 3.716 seconds**, no skips. Production object
build and final link succeed. Fresh linked measurement confirms entry
`0x150E7994`, following entry `0x150E7C9C`, 194 body / 194 slot words,
200-byte frame, zero different positions and zero guard rows.
`git diff --check` passes.

| Section | Byte-exact / C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 3,277 / 5,463 (59.99%) | 0 | 2,186 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,604 / 4,790 (54.36%) | 0 | 2,186 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversion counts/bytes are unchanged because the function already had a C
placeholder. README changes are limited to the two affected matching rows;
recovery details stay in working docs. Host callback tests do not establish
whole-game, hardware or visual acceptance. No Init corpus rerun, sibling
build, Release change or push.

## Handoff

- [x] Recover caller ABI, packet, allocator and twelve-byte metadata contract.
- [x] Preserve control sampling, repeated weight calls and coordinate stores.
- [x] Match all 194 words directly from C and verify the final production link.
- [ ] Inspect adjacent placeholder `func_150E7C9C` and its callers before
  recovering its body or changing its signature.

Init ownership and the adoption gates in Notes 926-936 remain unchanged.
`func_150E76D0` remains a semantic recovery with 171 aligned word differences;
this new match does not change that preceding helper's status.
