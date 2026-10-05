# Game Immediate Texture Release Direct Frame Match

Date: 2026-10-05. Starting HEAD: `30415066`.

## Result

`func_1510D7AC` now matches all 46 words / 184 bytes directly from semantic
C at retail address `0x1510D7AC`. The original 0x28 frame and incoming-ID
spill/reload are recovered, completing the four-word near-match from
[Note 969](969-game-immediate-texture-cache-release-recovery-20261004.md).
No guards, assembly replacement, compiler override, data change or padding
word was added. The profile remains default IDO 5.3 O2/g3.

Keep only the captured signed `s8 state` local and index the priority, activity
and cache tables directly. The earlier explicit pointer/count locals inflated
the frame. Merely changing their declaration order, scopes, qualifiers or
integer width did not recover it. Partial inlining either retained a larger
frame or changed the saved pointer slots. Complete table-indexed C emits
retail's pointer preservation around both free calls itself.

| Offset | Previous C | Retail And New C |
| --- | --- | --- |
| 0x00 | `27BDFFC8` | `27BDFFD8` |
| 0x68 | `AFA50038` | `AFA50028` |
| 0x6C | `8FA50038` | `8FA50028` |
| 0xAC | `27BD0038` | `27BD0028` |

The other 42 words are unchanged. Independently linked isolated C, production
and pristine ROM slot `conker/conker.us.bin+0x13AC5C` share SHA-256:
`21edadf96d05d36e293a9788fe9cfb4dba5a4b5c7b916d978b3b21755070046e`.

## Qualification

The opt-in source-only screen is
[game_immediate_release_frame_candidates.py](../../tools/experiments/game_immediate_release_frame_candidates.py).
It builds 51 named variants into ignored `conker/build/game-immediate-release-frame/`.
Some variants emit identical bodies; do not count these as 51 independent
algorithms or semantic qualifications. It reconstructs the former explicit-local
control from the current semantic body, making the old failure reproducible.
Only `inline-priority-inline-activity-both` matches every retail word.

| Selected Screen | Body Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Former explicit locals | 46 | 0x38 | 4 |
| Inline count and cache | 46 | 0x30 | 4 |
| Inline activity, count and cache | 46 | 0x28 | 6 |
| Inline priority, count and cache | 46 | 0x28 | 6 |
| Adopted full table-indexed form | 46 | 0x28 | 0 |

Three new checks in
[test_game_immediate_release_frame.py](../../tools/tests/test_game_immediate_release_frame.py)
reproduce the screen, pin both partial-frame rejection controls, prove the
exact candidate is the production source and retain five neighboring
maintenance/queue byte hashes and addresses. No screen result is normalized.

The existing actual-body
[texture lifecycle fixture](../../tools/tests/test_game_texture_metadata_and_maintenance.py)
now requires the smaller retail frame, zero differences and retail digest in
its independent fresh compiler/link check. It still covers all 65536 signed
priority/unsigned activity byte pairs and all 7762 valid IDs. It qualifies
direct and staged callback ordering, cache replacement between frees, final
sentinel/priority clearing, unrelated callback mutations, zero gates and the
connected actual resolver -> retain -> release -> maintenance -> reload path.
Opaque allocator, DMA and decoder callbacks remain mocks. Invalid pointer
values are forwarded only to non-dereferencing callbacks; real malformed
allocator inputs are not qualified.

Complete Init code/data, Debugger code and Game data remain raw retail-exact.
The preceding nineteen-word nullable cleanup rematch also remains exact.
Fresh production owner compilation, padding, link, progress and matcher pass
without source warnings; the duplicate `generated_12D630` recipe warning is
pre-existing. All 65 final combined checks pass in 42.717 seconds, no skips.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_immediate_release_frame tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
make tools-check
git diff --check
```

## Progress And Next

| Section | Exact C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3285 / 5463 (60.13%) | 0 | 2178 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2612 / 4790 (54.53%) | 0 | 2178 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

This is one new byte match, not a newly converted function. Conversion counts
and 47 Init ASM entries are unchanged. README changes are aggregate-only.

Read-only sibling audit finds `64CBFDOGL/recomp_out/.c:822784` still contains
the zero-return placeholder, with no named override in the scoped maintained
`src`/`CMakeLists.txt` search. The PC synchronization task remains separate;
do not claim its cleanup behavior is implemented. No host source, build,
save or frozen Release artifact is changed.

Next matching candidate: `func_151336A8`, the recovered resource helper from
[Note 961](961-game-extended-child-constructor-and-resource-helper-recovery-20261004.md).
It currently differs at nine words in a 46-word slot, with a matching 0x30
frame but a 45-word body plus padding. Preserve its qualified resource-helper
connections while recovering the full retail schedule. `func_15168E54` is
another nine-word near-match; neither is credited as completed here.
The experimental light selector's connected stack-seed gate remains open.
