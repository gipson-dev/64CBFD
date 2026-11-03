# Game Transformed Height Probe Direct Match

Date: 2026-11-03

## Result

`func_150CB0E0` now replaces its zero-return placeholder with byte-exact direct
C. Its complete retail slot is **64 words / 256 bytes**, frame `0x38`, VA
`150CB0E0..150CB1E0`, and ROM `F8590..F8690`. A fresh production recount
credits exactly this function:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,116 / 5,511 (74.69%) | 0 | 1,395 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,443 / 4,838 (71.17%) | 0 | 1,395 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The active 80% target now needs **293 more** exact functions.

## Source recovery and direct closure

The routine accepts a position output, actor, optional height-result record,
and unsigned mode byte. Modes other than one or two return zero without touching
the output. Mode one selects point `D_800A05EC` and matrix offset `+0xA00`;
mode two selects point `D_800A05E0` and matrix offset `+0xBC0`. Both routes call
`func_15143134` to transform the selected point into the caller's output.

When the result pointer is null, the function returns one immediately after the
transform. Otherwise it snapshots a three-float ray start with `Y + 100.0f`,
initializes the result through `func_1504715C`, then returns
`func_15046C80(start, 0, live_position_y - 500.0f, result)`. The post-initializer
height reload is intentional: callback mutation can change the lower endpoint.

The critical source shape uses two separate mode branches, one for the point
and one for the matrix. A ternary form leaves 24 positional differences, a
combined branch leaves 46, an inline call leaves 12, and moving result
initialization before the ray snapshot leaves 38. The separate semantic form
emits the retail 56-byte frame, `s0` lifetime, branch-likely null-result route,
three helper calls, and all **64 words directly from C**. There are zero guards,
insertions, or omissions.

The compact-object payload, with relocation fields unresolved, has SHA-256
`862a9af6d07f9c08a190a0a189353d58ccfb32d28cae3ce30f5628ff5b4fb789`.
The linked retail payload has SHA-256
`7842a0d1c596d002e2fab875d5e660b2b8ab8eeb55ef85a3d2473d020ddf5e73`.
All seven original bindings remain semantic: HI16 `D_800A05E0` at `+0x048`,
HI16 `D_800A05EC` at `+0x04C`, LO16 `D_800A05EC` at `+0x054`, LO16
`D_800A05E0` at `+0x058`, J26 `func_15143134` at `+0x07C`, J26
`func_1504715C` at `+0x0BC`, and J26 `func_15046C80` at `+0x0E4`.

## ABI, caller, and semantic qualification

The sole direct JAL is at ROM `0xF86D4` in `func_150CB1F4`; there are no
aligned pointer literals. The caller passes its `sp+0x124` position object,
actor pointer, `sp+0x100` optional result object, and low mode byte, then consumes
the return as a boolean. This fixes the recovered
`s32 (f32 *, u8 *, HeightResult71820 *, u8)` ABI independently of the body.

The big-endian guest oracle runs **15,360 cases / 46,080 executions** across
retail, compact C, and padded owner code. It covers all 256 mode-byte values,
six output layouts, four result layouts, null and populated results, two stack
phases, helper clobbers, output/result aliases, initializer mutations, live
lower-endpoint reloads, and four query returns. Ninety-six access-prefix pairs,
including thirteen delay-slot cuts, preserve the same partial state. Every
structurally reachable word executes. The duplicate `lwc1` at `+0x98` is
unreachable because the non-null branch-likely executes the earlier load in its
delay slot while the null route branches directly to the epilogue.

Native 32-bit O0, O2, and O3 UBSan builds each pass 15,360 selected cases.
Twelve independent controls alter the mode gate, either point, either matrix
offset, null-result return, upper or lower interval, initializer call, query
selector, query return, or live-height timing; every control fails as intended.
Another 263 controls reject every raw payload byte and relocation mutation,
and five freshly compiled source controls reject the principal semantic
constants and gates.

The complete pre-install suite passed six tests in 207.518 seconds. On the
installed run, the semantic, native, frame, and closure tests passed; the old
predecessor-only source-control constructor was the sole scaffolding failure.
After making that constructor state-aware, its corrected focused test passed in
77.212 seconds. No source or production artifact changed during that harness
correction.

## Image, data, and production closure

The complete owner preserves all nine neighboring functions. Strict
qualified-versus-production comparison retains all 6,051 function addresses,
uses zero exclusions, and reports only `func_150CB0E0` changed before
installation and no changed function afterward. Protected Game data remains
exact at 189,088 bytes across 720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Qualified/production owner | `e38e7262b0f1229eb847edcde8f25a1eb9d1cc8dd76fae8d49b096964dbca031` |
| Installed source | `c1297b8830a81e916e48783cfcffc34420e8d4adb5c8dae06153cf7c433eb088` |
| Predecessor linked ELF | `c4058a6c3c89494a1fa4458a77124343908aa9fabd4ac7ae42eff135d871700f` |
| Qualified/production linked ELF | `fbdbf2afb3437885c26e06b87e6f4d1154c7d1ac795fb2c466741d856b75a297` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Unchanged production guard table | `2da43f2c2acf5fed809fd5e948b1b1342a1a085801a78751b352a33cd7974664` |

The actual production Make used the owner's retail `-O2 -g3` profile, rebuilt
the padded object and linked ELF, generated `conker.us.bin`, and stopped only at
the expected final whole-ROM SHA mismatch while the decomp remains incomplete.
The permanent candidate screen, strict qualifier, guest/native oracle, ABI
checks, and controls were committed before production source as tools commits
`eea8849` (`test(game): qualify transformed height probe`) and `fe986a4`
(`test(game): support installed height probe controls`).

## Graph retention

The required bounded Graphify update retained 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. It rebuilt a 58,200-node
graph with 112,162 edges and 5,051 communities; visualization was skipped at
the configured 5,000-node limit. The retained/refreshed
`graphify-out/graph.json` is 75,494,589 bytes with SHA-256
`730c3217c7f8c19137b3858514030432704461aa017a1d5d334d6f10149356d5`.
The initial unscoped refresh correctly refused a 24,391-node replacement; the
successful update used Graphify's incremental changed-path mechanism and no
force flag. This is bounded old-node retention evidence, not a full-corpus
extraction claim.

## Continuation

The seven documented handwritten/custom-ABI boundary cases remain outside the
ordinary queue. The fresh ordinary ranking now starts at `func_15123070` (67
words, 61 real differences), followed by the other 61-difference tie members.
Every candidate still requires source, ABI/caller, owner, guest/native, actual
Make, complete-image, protected-data, production recount, documentation, and
graph-retention gates before credit. This static and bounded qualification does
not claim full gameplay or hardware acceptance.
