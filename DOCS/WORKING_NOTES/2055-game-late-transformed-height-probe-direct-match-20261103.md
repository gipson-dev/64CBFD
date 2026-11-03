# Game Late Transformed-Height Probe Direct Match (2026-11-03)

## Outcome

`func_151AF5C0` is restored from a zero-return placeholder as semantic C. The
complete 64-word / 256-byte retail slot emits directly under the owner's
`-O2 -g3` profile with its original 0x38-byte frame, seven relocations, and
zero expected-word guards, insertions, or omissions.

This is a source, caller-ABI, guest/native execution, owner, complete-image,
protected-data, production-build, and recount result. It does not claim live
gameplay, renderer, collision-world, or hardware acceptance.

## Recovered contract and source shape

The routine accepts a position output, actor, optional height-result record,
and unsigned mode byte. Modes other than one and two return zero without
touching the output. Mode one selects point `D_800AA0FC` and actor-matrix
offset `+0x800`; mode two selects point `D_800AA0F0` and offset `+0x640`.
Both routes call `func_15143134` to transform the selected point into the
caller output.

When the result pointer is null, the function returns one immediately after
the transform. Otherwise it snapshots a three-float query start with Y plus
100, initializes the result through `func_1504715C`, and returns
`func_15046C80(start, 0, live_position_y - 500, result)`. Reloading the lower
endpoint after initialization is intentional because that helper may mutate
the aliased output.

The exact source keeps point selection and matrix selection as two separate
mode branches. A ternary form remains 64 words but differs at 24 positions; a
combined branch emits 62 words and differs at 46 positions; moving result
initialization ahead of the query-start snapshot differs at 20 positions.
The selected semantic form emits all 64 retail words directly.

## Bindings, caller, and frame evidence

All seven bindings remain semantic:

- HI16 `D_800AA0F0` at `+0x048`;
- HI16 `D_800AA0FC` at `+0x04C`;
- LO16 `D_800AA0FC` at `+0x054`;
- LO16 `D_800AA0F0` at `+0x058`;
- J26 `func_15143134` at `+0x07C`;
- J26 `func_1504715C` at `+0x0BC`; and
- J26 `func_15046C80` at `+0x0E4`.

The sole direct call is at ROM `0x1DCBBC` in `func_151AF6D4`; there are no
aligned pointer literals. Its complete eight-word window passes stack+0x124
as position, the actor pointer as argument two, stack+0x100 as optional result,
and the unsigned stack+0x137 byte as mode, then consumes the return as a
Boolean. This independently fixes the recovered
`s32 (f32 *, u8 *, HeightResult71820 *, u8)` ABI.

The 0x38 frame preserves S0 at 0x18, RA at 0x1C, the 12-byte query start at
0x2C, and incoming argument homes at 0x3C, 0x40, and 0x44. The duplicate
`lwc1` at `+0x98` is unreachable: the non-null branch-likely executes the
earlier load in its delay slot, while the null route branches directly to the
epilogue.

## Execution, controls, and reusable donor

The permanent qualifier was committed before production source as tools
commit `47387a1` (`test(game): qualify late transformed height probe`). It adds:

- `tools/experiments/game_late_transformed_height_probe_candidates.py`;
- `tools/experiments/game_late_transformed_height_probe_match.py`;
- `tools/tests/game_late_transformed_height_probe_oracle.py`; and
- `tools/tests/test_game_late_transformed_height_probe_match.py`.

The shared `game_transformed_height_probe_oracle.py` now accepts point names,
addresses, matrix offsets, entry, ROM location, and owner object as explicit
configuration. The original `func_150CB0E0` donor suite still passes all six
tests after that generalization in 70.289 seconds.

The pre-install target suite passes six tests in 85.275 seconds; the installed
production suite passes the same six in 138.812 seconds. Its 15,360 guest cases
produce 46,080 equal retail/compact/owner executions across all 256 mode-byte
values, six position layouts, four result layouts, null and populated results,
two stack phases, helper clobbers, aliases, initializer mutations, live lower
endpoint reloads, and four query returns. All 63 reachable words execute.

Native 32-bit O0, O2, and O3 UBSan builds each pass 15,360 cases. Twelve
independent controls alter the mode gate, either point, either matrix offset,
null-result return, upper or lower interval, initializer call, query selector,
query return, or live-height timing; every control fails as intended. Another
263 controls reject every raw payload byte and relocation mutation, and five
freshly compiled source controls reject the principal constants and gates.

## Image, data, and production closure

The strict reconstruction compares all 6,051 linked functions, reports only
`func_151AF5C0` changed from the predecessor, fixes every address, uses zero
exclusions, and preserves all six owner neighbors. Protected Game data remains
exact at address `0x80082760`: 189,088 bytes across 720 owners, zero different
bytes, zero different owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The actual production owner and linked ELF reproduce the independent
predictions exactly. Make then emits the rebuilt ROM image and stops only at
the expected final whole-ROM SHA mismatch while the decomp remains incomplete.
The pre-existing duplicate `generated_12D630.c.o` recipe warning remains
unchanged; there are no compile, assembly, padding, or link errors. The shared
match-progress, generated-word-patch, PC16, and protected-data suite passes all
19 tests in 19.220 seconds.

## Frozen evidence

| Artifact | SHA-256 |
| --- | --- |
| Natural compact body with relocation fields normalized | `d8a8c47c3e87f1329ddde3ad5f2d1fe857cc14661f97e491243ed6567227e0e8` |
| Complete linked retail body | `6ca039999591d943e14da27d3a7da11c812440b87bd19b0770263231ecdc5fc9` |
| Installed owner source | `00fbacd84b1d12edef2b46e0bece5346653e239b27f44e7ee66074358779aeb9` |
| Qualified/production owner object | `01cdd718eb63cb9c0a510f7fffcf3d73211b02d86100651f2ead61f101f7f10a` |
| Predecessor linked ELF | `c1609b5795c7be856dea52e03b7870054b3feb35fd672a65ef7f8a588341dacb` |
| Qualified/production linked ELF | `069120cef62c648808f2d9dbe9d6347d42d952cb74c8d3e9a5f501738e3980ca` |
| Production rebuilt ROM image | `bb63f443f54b3f9f31b83ae244cd0a22777e48d3bd38ea9ff504eaaec1f9a9fc` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Unchanged guard table | `5dca6cbb64815f8cfbb474e08fa06488691252ad0bc25ae7beaf4af0449ec59c` |
| Generated aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

## Recount

The fresh production ELF reports:

- Total: **4,125 / 5,511 (74.85%)**, zero address drift, 1,386 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,452 / 4,838 (71.35%)**, zero drift, 1,386 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **284 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted the nine changed inputs but
produced only 24,488 nodes versus the retained 58,281-node corpus, so Graphify
correctly refused to replace `graph.json`. Its fail-closed report retained
31,816 nodes from 3,754 still-present files outside the reduced scan corpus.
No forced refresh was used.

An explicit nine-path incremental rebuild with `force=False` then produced
**58,292 nodes, 112,237 edges, and 5,061 communities**. Against the saved
pre-change snapshot, **58,278 / 58,281** old node IDs were retained; three
line-number-derived `DOCS/UPDATE_LOG.md` IDs were replaced, and 14 IDs were
added. The resulting `graph.json` is 75,520,379 bytes with SHA-256
`3bb98f149707c7072ac57990dac5b8d59bbe5165a1338a9fe8069e5ec86eed23`.

## Continuation

The seven smaller entries remain in their documented handwritten/custom-ABI
lane: `func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC`, and `func_150A6760`. The fresh ordinary
queue now starts at `func_151DA6F8` (144 words, 61 real differences), followed
by `func_1504A620`, `func_15172D80`, `func_1519E1F4`, and `func_151DE6D4` in
the 62-difference tier. Every candidate still requires source, ABI/caller,
owner, guest/native, actual Make, complete-image, protected-data, production
recount, documentation, and graph-retention gates before credit.
