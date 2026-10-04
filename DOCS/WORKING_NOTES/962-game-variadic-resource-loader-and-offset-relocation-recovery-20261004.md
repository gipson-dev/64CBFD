# Game Variadic Resource Loader And Offset Relocation Recovery

Date: 2026-10-04

## Scope And Result

Replace `func_1502B6BC` and `func_1502B4A8`'s zero-return placeholders with
complete semantic bodies in `conker/src/game_57FA0.c`. Use the repository's
existing `stdarg.h` for the real variadic path interface, not a fixed six- or
seven-argument approximation. Correct the four local caller declarations in
`game_2DF70.c`, `generated_49D30.c`, `generated_6A3D0.c` and `generated_15F680.c`.
Retain integer address storage with an explicit cast where the existing
caller owns that representation; use a pointer temporary in the lazy loader.
Correct lookup/block-load declarations and placeholder types, but do not claim
their bodies recovered. No new guards, data changes or compiler overrides.

| Function | Retail Slot | C Body | C Frame | Raw Word Differences |
| --- | ---: | ---: | ---: | ---: |
| Variadic loader `func_1502B6BC` | 77 words / 308 bytes | 77 words | 0x50 | 17 |
| Offset relocator `func_1502B4A8` | 72 words / 288 bytes | 65 words | none | 71 |

Loader retail frame is also 0x50. Retail loader extent:
`0x1502B6BC..0x1502B7F0`, ROM `0x58B6C..0x58CA0`. Relocator extent:
`0x1502B4A8..0x1502B5C8`, ROM `0x58958..0x58A78`. The relocator has seven
zero padding words in its full slot. Both remain non-matching.

Complete production-slot SHA-256:

- Loader: `88bc84ea5f8007358199c4f13b52e35d517419fd40230f9a25223139fe8bd1f5`.
- Relocator: `bcce58836363dffad7c081528b0be692fbdfc461a5cc8b71e9b3376e16b43262`.

## Loader Contract

Four fixed arguments are optional size output, signed relocation count,
optional relocated-count output and path depth. Remaining arguments are that
many signed 32-bit path components. When size output is NULL, use the local
fallback; write one before traversal. Begin at ROM table symbol `D_AB1950`
(`0xAB1950`). Positive-depth traversal consumes every component, even after
a missing lookup has closed the gate:

1. Read the next component using `va_arg(path, s32)`.
2. If the current size/status is nonzero, call
   `func_1502AC88(offset, component, &descriptor)` and add its returned
   offset delta with 32-bit unsigned wrapping.
3. Write `descriptor & 0x0FFFFFFF` to the size output after the callback.
   A zero value suppresses later lookups but not argument consumption.
4. Decrement depth and repeat until zero.

If traversal ends with zero size/status, return NULL and leave the optional
relocated-count output untouched. Otherwise call
`func_1502B350(offset, descriptor, size)`. Reload size/status after the call.
Invoke the actual offset relocator only when it is nonzero and the returned
pointer is nonnull. Otherwise publish relocation count zero. Write that count
only when its output pointer is nonnull, then return the block pointer even
when its post-load size/status is zero. Pointer success and size success are
independent. Size and count outputs may alias; the final count then wins.

**Unresolved domain:** retail reads an uninitialized descriptor for zero depth,
or when its lookup fails to write one. No invented zero initializer or depth
clamp is added. The current production `func_1502AC88` is still a placeholder
and does not write metadata, so ordinary production resource loading is not
qualified by this recovery either. The tests supply explicit lookup metadata;
they do not prove that missing production body works. Negative/zero depths,
too few variadic arguments and arbitrary invalid pointers are not executed or
claimed qualified. Recover lookup and block loading next.

## Relocation Contract

Each record is two words: relative address and flagged length. A zero signed
count first scans length bit 0x80000000 and includes the terminal record in
the discovered count; this scan happens before mutation. A positive explicit
count uses that many records without scanning. A negative count skips all
record accesses and returns unchanged, including with a NULL pointer.

For each selected record, strip length to `0x0FFFFFFF`. Set address to zero
for the 0xFFFFFFFF sentinel or zero stripped length; otherwise add the block's
32-bit base address with unsigned wrapping. Return the selected/discovered
count. No terminator bound, address validation, saturation or idempotence is
invented. Unterminated automatic scans and oversized counts are outside the
qualified domain.

## Verification

Fourteen new tests in `tools/tests/test_game_variadic_resource_loader.py` use
the actual loader and relocator. Host fixtures cover depths 1..16, signed
components, wrapping deltas, missing components, every consumed argument,
nullable/aliased outputs, independent pointer/status gates and live output
reads. Relocation models cover seven offset values, six flagged lengths and
counts 1..9 (378 combinations), twenty automatic-count terminal positions,
zero-length terminal/sentinel records and negative-count no-dereference cases.

Connections execute actual resource helper `func_151336A8`, actual table
caller `func_1501D1D4` and actual lazy caller `func_1503D774`. Another fixture
executes actual `func_1513264C` -> `func_151336A8` -> `func_1502B6BC` ->
`func_1502B4A8`, using only opaque lookup/block-load and setup/attachment
boundaries. Successful constructor trace is `ANQQDRSTCVVVVB`; record/node/
block failure traces are `A`, `ANRF` and `ANQQDRFF`. It checks resource-header
pointer relocation, count outputs, initialized constructor result, reference
counts, cleanup order and fences. Opaque fixtures are not implementation of
DMA, decompression, cache ownership, attachment or rendering.

The actual loader's host compilation narrowly suppresses GCC
`-Wmaybe-uninitialized` for retail's explicitly unqualified descriptor domain.
No production warning suppression or replacement initializer is introduced.
The existing constructor tests now use a true variadic opaque loader fixture;
their boundary remains explicit. These are 32-bit host/source contracts, not
64-bit native pointer portability or full guest differential execution.

Fresh standalone IDO O32 compilation with the actual repository `stdarg.h`
links both bodies and reproduces production slots, frames, differences and
full hashes. Corrected callers preserve complete retail-byte-exact slots:

| Caller | Words | Complete Slot SHA-256 |
| --- | ---: | --- |
| `func_1501D1D4` | 33 | `05f16c6812cc11dc9363f53b441b15cb02723d07be71832972168ba7fce45f85` |
| `func_1503D774` | 36 | `bfcfc1059accaaa23866d1a6053f997357809baec37e285c8617cdeaf900818b` |
| `func_15002FB4` | 86 | `2f9ea88fb14379ce3f10ff070199633db476a6d1e3a1a3667fe247bea38e2ec2` |

The constructor, resource helper and pointer wrapper keep Note 961's complete
identities. Fresh production compile/padding/relink/progress/matcher succeeds.
All **174 combined tests pass in 33.316 seconds, no skips**. Complete Init
code (164,048 bytes), Init data (17,376 bytes), Game data (189,088 bytes /
720 owners), prior parent/child/position-writer recoveries and exact neighbors
remain intact. Existing duplicate `generated_12D630` recipe warnings and
unrelated pointer/type warnings in `game_2DF70.c` and `generated_15F680.c`
remain; no warning cleanup is bundled.
Project tool and whitespace checks pass, and all 2,726 local links in the
touched working documents resolve. No runtime acceptance or push is claimed.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_patch_generated_slice_ld tools.tests.test_check_game_data_layout tools.tests.test_game_variadic_resource_loader tools.tests.test_game_extended_child_constructor tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_child_emission_callback tools.tests.test_game_descriptor_position_writer tools.tests.test_game_weighted_event_emitter tools.tests.test_game_event_payload_creators tools.tests.test_game_event_sound_dispatch tools.tests.test_game_world_emitter_dispatch tools.tests.test_game_curve_record_update tools.tests.test_game_random_curve_record tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_fill_value_mask -q -f
make tools-check
git diff --check
```

## Sibling Boundary And Next

Read-only audit of active sibling `recomp_out/.c` finds existing recompiled
lookup (line 202256), block loader (203390), relocator (204006) and variadic
loader (204477) bodies, with diagnostic probes. Scoped native-source matches
also discuss heap/DMA support; this is not an untouched-source or current
runtime-parity claim. No mechanical native-pointer transplant, sibling source,
host build, binary, save or frozen Release change is included.

- [x] Recover the real variadic loader and offset relocator without new guards.
- [x] Correct local caller interfaces and preserve three complete exact callers.
- [x] Connect actual constructor/helper/loader/relocation and other source callers.
- [x] Fit complete slots and preserve Init/Game-data and prior recovery identities.
- [ ] Recover lookup `func_1502AC88` (159 words) and qualify its metadata writes.
- [ ] Recover block loader `func_1502B350` (86 words), DMA/decompression and failures.
- [ ] Recover deeper setup `func_1510CE60` and attachment `func_15168E54`.
- [ ] Pursue raw byte matching separately and qualify natural guest effects.
- [ ] Synchronize the still-stubbed PC child through guest/RDRAM interfaces.

Init remains 492 C / 47 assembly. Game stays 2,609 and total 3,282 byte-exact
C functions, zero drift. Both recovered bodies were already counted as C:
README aggregates remain unchanged, with recovery updates in these working docs.
No complete resource-loading pipeline, compressed-ROM promotion or runtime
acceptance is claimed while its lookup/block-load bodies remain placeholders.
