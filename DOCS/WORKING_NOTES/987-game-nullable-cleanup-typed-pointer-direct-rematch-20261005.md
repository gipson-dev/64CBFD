# Game Nullable Cleanup Typed Pointer Direct Rematch

Date: 2026-10-05. Starting HEAD: `8527382d`.

## Result

`func_150F631C` once again matches all nineteen words / 76 bytes directly
from semantic C at its retail address. No expected-word guards, padding words,
compiler override, shared prototype changes or assembly replacement were added.
The default IDO 5.3 O2/g3 profile emits the original 0x18 frame.

The live inventory had four real differences despite the historical direct
match recorded in [Note 147](147-game-nullable-field-cleanup-match-20260926.md).
The current callee prototype is `void func_1516972C(struct102 *)`; the owner
still read integer fields. Change the offset-0x30 reads to
`struct102 * volatile *` and the offset-0x34 reads to `struct102 **`, using
`NULL` for the tests. The owner lifetime and first-field volatile reload remain.
This avoids integer-to-pointer argument conversion and recovers retail's
second-field allocation in `a0` instead of `v0`.

| Offset | Previous C | Retail And New C |
| --- | --- | --- |
| 0x14 | `8CA20034` | `8CA40034` |
| 0x28 | `8CA20034` | `8CA40034` |
| 0x2C | `50400004` | `50800004` |
| 0x38 | `00402025` | `00000000` |

Raw slot SHA-256, independently compiled C, linked production and pristine ROM:
`3d01686575967f832331b203dee11e677b94a8f8dc7ef88d6a270e2d887e1cdc`.
Retail reference offset: `conker/conker.us.bin+0x1237CC`.

## Qualification

New fixture: [test_game_nullable_cleanup.py](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_nullable_cleanup.py).
It extracts the actual production function instead of maintaining a C copy.

- Forty-nine nullable pointer pairs cover zero, low values, the signed boundary,
  KSEG-like values and `0xFFFFFFFF`, forwarded to non-dereferencing callbacks.
- Another 294 cases change the second field inside the first callback, including
  clearing, inserting and replacing it. The later read observes the replacement;
  owner and unrelated callback mutations persist, with neighboring bytes intact.
- Fresh isolated IDO compilation and relocation link match all nineteen words
  without warning or normalization. The final standalone alignment NOP is
  checked separately, not credited as part of the function.
- An independently compiled integer-field rejection control reproduces exactly
  the four old differing words above. It is not a production alternative.
- Fresh production bytes and addresses match retail. No patch-table row exists
  for this function. Six surrounding function spans retain their checkpoint
  hashes and retail addresses, including both cleanup wrappers.
- The existing texture fixture checks complete Init code/data, Debugger code
  and Game data against pristine retail after the production relink.

All 62 final combined checks pass in 18.025 seconds, no skips, including the
warning-free typed-body assertion. `make tools-check` also passes.
The initial production-byte test was run while the linker was still
working and observed the old ELF; it was rerun successfully after link completion.
The full owner rebuild has only its existing neighboring pointer/integer
warnings and the existing duplicate `generated_12D630` recipe warning.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
make tools-check
git diff --check
```

This is bounded callback forwarding and exact guest-code qualification, not
real allocator cleanup or natural PC gameplay acceptance. Invalid pointer
values are never dereferenced by the fixture.

## Progress And Next

Subsequent checkpoint: [Note 988](988-game-immediate-texture-release-direct-frame-match-20261005.md)
completes the immediate release near-match identified below, directly from C.

| Section | Exact C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3284 / 5463 (60.11%) | 0 | 2179 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2611 / 4790 (54.51%) | 0 | 2179 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

This is one recovered byte match, not a newly converted function. Conversion
counts and the remaining 47 Init ASM owners are unchanged. Update README
aggregates only; recovery details stay in dedicated docs.

Read-only sibling audit finds a complete older generated cleanup body in
`64CBFDOGL/recomp_out/.c:762604`, with the old one-read first-field schedule.
The scoped `src`/`CMakeLists.txt` search finds no named maintained override.
Do not claim it has these new retail-exact instructions. No host source,
build, save or frozen Release changes are made; any host synchronization needs
separate qualification.

Next near-match: 46-word `func_1510D7AC`, still four frame/spill differences
under its qualified semantic body from [Note 969](969-game-immediate-texture-cache-release-recovery-20261004.md).
Recover the original 0x28 frame and corresponding incoming-ID spill lifetime
without weakening its callback mutation contract. The experimental light
selector from [Note 986](986-game-light-selector-candidate-fitting-and-connected-frame-witness-20261005.md)
remains unadopted; its connected stack-seed gate is unchanged.
