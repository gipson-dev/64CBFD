# Game World-Emitter Dispatch: Direct Byte Match

Date: 2026-10-04. Starting HEAD: `68c0c98e`, clean tracked checkout.

## Production Recovery

Replace `func_150E81A8`'s zero-return placeholder in
`conker/src/game/generated_113D60.c` with its complete semantic body.
All **129 words / 516 bytes** emit directly from C under the existing O2/g3
profile, including the original **0x90-byte frame**. No new instruction guards,
compiler overrides, data owners or layout changes are needed.

The routine takes a low-byte selector, low-byte slot and full 32-bit context.
Only selectors 4, 5, 6 and 7 perform work:

1. Copy the selected twelve-byte world position from `D_800A1290` and add
   200.0f to Y before calling `func_151D3FF4` with the local snapshot.
2. Initialize the world-emitter descriptor, copying the local position **after**
   that call. Preserve the signed halfwords, integer fields, fixed floats and
   five external float loads, then submit it through `func_1514FCE8`.
3. Set packet kind 1, call integer RNG and set signed-halfword duration to
   `(u32)rng % 11 + 30`. Set count 8, index -1 and mode 1, then call
   `func_151D8868(&packet, 0, 255, 0)`.

No callback or RNG is invoked for other selector bytes. Return value is not
given semantic meaning: the retained direct caller at `0x1509D6D8` passes
context 1, then reloads `v0` from its own stack, discarding the callee result.
The recovered declaration is `void func_150E81A8(u8, u8, s32)`.

## Layout And Data Evidence

The new `WorldPosition113D60` is three floats / twelve bytes; the existing
two-float emitter position type is not reused for this different interface.
`WorldEmitterDescriptor113D60` is 0x5C bytes, with its position at 0x10,
last initialized signed byte at 0x58 and three unwritten tail bytes at 0x59.
The consumer `func_1514FCE8` reads individual fields through `lb 0x58($s0)`;
this is an observed field extent, not a claim that it copies the entire struct.
Descriptor field names remain offset-based where domain meaning is uncertain.

The descriptor tail and packet padding bytes 1/7 remain uninitialized, matching
retail. Neither local object is blanket-zeroed. Global data is declared only,
not redefined or moved. Retail float-pool words are:

| Address | Word | Value |
| --- | --- | ---: |
| `0x800A1354` | `0x442EC000` | 699.0 |
| `0x800A1358` | `0x43FF8000` | 511.0 |
| `0x800A135C` | `0x3F483128` | 0.7820000648498535 |
| `0x800A1360` | `0xBF6E147C` | -0.9300000667572021 |
| `0x800A1364` | `0x3F3AE148` | 0.7300000190734863 |

The complete routine at ROM `0x115658..0x11585C` and the new linked slot have
the same SHA-256, without normalization:

```text
b0e576afb054d463f65658487256ecaf1f667576948aa0d7906745b150e01a02
```

## Focused Tests

New `tools/tests/test_game_world_emitter_dispatch.py` extracts the actual
production body and layouts for six tests:

- All 256 selector bytes across 1,024 widened-input calls, slot truncation and
  a context whose high bytes must survive. Unsupported selectors call nothing.
- Four supported selectors, thirteen unsigned RNG boundary words and five
  full-width contexts: 260 combinations, verifying every initialized descriptor
  field, packet duration and helper order.
- Four adversarial position-helper cases: stub mutation of the local position
  and globals verifies the post-helper position copy and constant-load timing.
  This does not claim the real assembly helper performs those mutations.
- Native 32-bit layout assertions, and retained consumer field-extent evidence.
- Retail slot hash, four-call sequence, direct caller's discarded return and
  absence of explicit padding initialization.
- Independent IDO compile/link: all 129 words match pristine retail directly.

The first isolated linker used `-Ttext=0x150E81A8`, which aligned the input to
`0x150E81B0` and added two leading nops. That was a fixture placement error,
not a 131-word production body. The corrected script uses `SUBALIGN(4)`, as
the production slice linker does, and compares the complete correctly placed
body. No source reduction or word replacement was used to resolve it.

## Production Qualification

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 tools/check_game_data_layout.py conker/build/conker.us.elf
python3 -m unittest tools.tests.test_patch_generated_slice_ld tools.tests.test_check_game_data_layout tools.tests.test_game_world_emitter_dispatch tools.tests.test_game_curve_record_update tools.tests.test_game_random_curve_record tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters -q -f
```

Fresh production relink succeeds. **59 tests pass in 13.044 seconds, no skips**.
`make tools-check` and `git diff --check` also pass.
The existing duplicate Makefile recipe warnings for `generated_12D630` remain.
Independent raw section/slot checks use the SHA-1-validated pristine ROM:

| Linked region | Verified retail-exact extent |
| --- | ---: |
| Complete Init code | 164,048 bytes |
| Complete Init initialized data | 17,376 bytes |
| Complete Game data | 189,088 bytes / 720 owners |
| `func_150E7994`, curve builder | 194 words |
| `func_150E7C9C`, curve update | 212 words |
| `func_150E7FEC`, retained assembly | 111 words |
| `func_150E81A8`, new semantic C | 129 words |
| `func_150E83AC`, retained assembly | 49 words |
| `func_150E8470`, retained assembly | 237 words |

Fresh matcher: **Game 2,606 / 4,790 exact (54.41%)**, total **3,279 / 5,463
exact (60.02%)**, zero drift, 2,184 still different. Init remains 492 / 492
and Debugger 181 / 181 exact. The placeholder already counted as C, so this
is a semantic recovery and one additional byte match, not a representation
count increase. Only achieved matching rows change in the README.

## Handoff

- [x] Recover the complete descriptor/packet body and narrow argument types.
- [x] Match all words directly, with original frame and no guards.
- [x] Qualify production link, physical data and neighboring code ownership.
- [x] Update aggregate matching rows and keep detailed progress in working docs.
- [ ] Next inspect `func_150E8930`, the adjacent verified zero-return placeholder.

The callees remain retained assembly; native tests substitute bounded interface
stubs and do not execute the complete guest emitter pipeline. Static byte/data
matching is not gameplay acceptance. No Init conversion, sibling build, Release
change, real save modification, compressed-ROM promotion or push is claimed.
