# Game Resource Helper Address Word Direct Match

Date: 2026-10-05. Starting HEAD: `e90d44f5`.

## Result

`func_151336A8` now matches all 46 words / 184 bytes directly from C at
retail address `0x151336A8`, with the original 0x30 frame. This completes
the nine-word near-match from
[Note 961](961-game-extended-child-constructor-and-resource-helper-recovery-20261004.md).
No instruction guards, compiler override, assembly replacement, interface
change or data change was added. The complete body now occupies the slot;
the former 45-word body had one trailing padding word.

Only the final attachment argument changes:

```c
func_15168E54(node->resource->data, (void *)(u32)node->resource);
```

The explicit O32 address-word round-trip recovers IDO's retail handoff through
`v1`, followed by the resource data load and `a1` move in the call delay slot.
It preserves all 32 address bits. The public API remains typed pointers;
this source is guest 32-bit C, not a portable host pointer conversion.
The attached source comment documents that compiler-sensitive representation.

The old form loaded the header directly into `a1` and loaded its data in the
delay slot, shortening the body by one word. That also displaced the success
return/epilogue and changed the failure branch displacement. The original
opening/table/output/local sequence was already exact and remains unchanged.

Independent isolated C, complete production slot and pristine ROM at
`conker/conker.us.bin+0x160B58` share SHA-256:
`bcc5a75d799670a4fe870c852b34ab2a2162245941d52b98e5ba20e301106322`.

## Source Screen And Tests

Opt-in screen:
[game_resource_helper_schedule_candidates.py](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_resource_helper_schedule_candidates.py).
It rebuilds nineteen named forms in ignored
`conker/build/game-resource-helper-schedule/`. Source-identical/emission-identical
forms are not independent algorithms. Screen results are raw words, never
instruction-normalized. Both signed and unsigned inline address-word casts
match exactly; adopt the unsigned form to represent the address word.

| Screen Form | Body Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Previous direct pointer argument | 45 | 0x30 | 9 |
| Explicit typed resource local | 45 | 0x30 | 11 |
| Character-pointer cast | 45 | 0x30 | 9 |
| Volatile second node read | 46 | 0x30 | 4 |
| Inline signed address-word cast | 46 | 0x30 | 0 |
| Adopted inline unsigned address-word cast | 46 | 0x30 | 0 |

Three new checks in
[test_game_resource_helper_schedule.py](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_resource_helper_schedule.py)
reproduce the screen, reject pointer/volatile near-matches, prove the selected
candidate is the production body, verify all retail bytes and preserve five
constructor/wrapper/adjacent hashes and addresses. Standalone linker alignment
NOPs outside the function are excluded from the 46-word match.

The existing actual-body
[constructor/helper fixture](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_extended_child_constructor.py)
now independently requires 46 body words, zero differences and the retail
digest. Its 234 indexed helper cases retain load failure, store-before-test,
setup arguments and resource/data reload after setup mutation. Actual child,
wrapper, constructor and helper connections remain qualified. Variadic loader,
asset lookup/block loading and actual texture setup/resolver/attachment
connections all rerun with this actual helper.

**All 148 final combined checks pass in 67.751 seconds, no skips.** The
preceding nullable-cleanup and immediate-release matches remain exact.
Complete Init code/data, Debugger code and Game data remain raw retail-exact.
Fresh owner compilation, assembly processing, padding, link, progress and
matcher pass. The two neighboring `func_100043B4` pointer/integer warnings
and duplicate `generated_12D630` recipe warning are pre-existing; isolated
adopted helper compilation is warning-free. `make tools-check` and
`git diff --check` pass.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_resource_helper_schedule tools.tests.test_game_extended_child_constructor tools.tests.test_game_variadic_resource_loader tools.tests.test_game_asset_table_lookup_and_block_load tools.tests.test_game_texture_resource_setup tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
make tools-check
git diff --check
```

The existing fixtures retain opaque allocation/DMA/decode/RNG/math boundaries.
This is exact guest code plus bounded connected source qualification, not
natural gameplay, real malformed-pointer handling or final rendering proof.

## Progress And Next

Subsequent checkpoint: [Note 990](990-game-attachment-walker-guarded-register-match-20261005.md)
completes the attachment linked-slot match identified below with nine guarded
register/equality normalizations. It is not a direct compiler match.

| Section | Exact C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3286 / 5463 (60.15%) | 0 | 2177 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2613 / 4790 (54.55%) | 0 | 2177 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

This is one additional byte match, not a newly converted function. Conversion
totals and the 47 Init ASM entries are unchanged. README is aggregate-only;
recovery details remain in dedicated docs.

Read-only sibling audit finds the full retail-sequence helper in
`64CBFDOGL/recomp_out/.c:935834`, including the `v1`/`a1` attachment handoff
at lines 935924..935933 and complete epilogue. No named maintained override
is found in scoped `src`/`CMakeLists.txt` search. No synchronization change is
needed for this helper, and no host source/build/save/frozen Release change
is made. This does not qualify the sibling's downstream runtime behavior.

Next matching target: 45-word `func_15168E54`, the resource attachment walker
from [Note 965](965-game-texture-resource-setup-resolver-and-attachment-recovery-20261004.md).
It retains its 0x38 frame and differs at nine words. Preserve command filtering,
terminator behavior and repeated reads while recovering its retail schedule.
Constructor `func_1513264C` remains non-matching at 184 differences, and the
experimental light selector's connected stack-seed gate is still open.
