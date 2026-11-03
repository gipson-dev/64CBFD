# Game Point-Record Search Guarded Match

Date: 2026-11-03

## Result

`func_1515EB84` now replaces its zero-return placeholder with byte-exact
guarded C. Its complete retail slot is **61 words / 244 bytes**, frame
`0x360`, VA `1515EB84..1515EC78`, and ROM `18C034..18C128`. A fresh
production recount credits exactly this function:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,107 / 5,511 (74.52%) | 0 | 1,404 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,434 / 4,838 (70.98%) | 0 | 1,404 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The active 80% target now needs **302 more** exact functions.

## Source recovery and guarded closure

The recovered five-argument ABI takes signed point coordinates `x`, `y`, and
`z`, a record mask, and the head of a linked-node list. It constructs the
original large `struct127` query at `sp+0x34`, writes current and old XYZ as
single-precision values, and writes the second Y field at `sp+0x1B4`. It then
walks the list and returns the first record which:

- has a clear status byte at `record+0x14`;
- passes the optional mask against the high byte of `record+0x18`;
- has `(record[0x15] >> 2) == 24` or a clear sign bit in `record+0x18`; and
- is accepted by `func_150A1DA0(query, record, 0)`.

The body naturally emits the exact frame, saved-register lifetime, linked-list
loop, branch-delay updates, return paths, and the original J26 helper
relocation at function offset `0x0B0`. Its only four positional differences
are one independent floating-point temporary allocation at the opening point
conversion:

| Raw offset | Compiler word | Retail word | Qualified action |
| ---: | ---: | ---: | --- |
| `0x020` | `44852000` | `44853000` | Convert Y through retail temporary F6. |
| `0x024` | `44843000` | `44842000` | Convert X through retail temporary F4. |
| `0x02C` | `46802020` | `46803020` | Complete the Y conversion from F6. |
| `0x038` | `468030A0` | `468020A0` | Complete the X conversion from F4. |

Each row checks its expected compiler word and fails closed when stale. No
branch, call, data relocation, instruction insertion, or instruction omission
is normalized. The unqualified C body has SHA-256
`d11e4f45a3d99c989d91924585621a0ddda78043fef2b6aada1066ad41eb9591`;
the qualified retail body has SHA-256
`b1a1865fd83d62120ed64b5299d3affc6b97b7def9ab4e0c2da5fb128ac46780`.

## Semantic, caller, and production qualification

The big-endian guest oracle runs 242 cases spanning the status bytes, record
classes, mask bytes, sign gate, all coordinate edge fixtures, first-record
acceptance, helper rejection followed by second-record acceptance, and a null
list. It checks the helper arguments and all seven query values after volatile
caller-register clobbers. Coverage reaches every executable retail word; only
the structurally unreachable word at `ENTRY+0xC8` is excluded.

The same semantic corpus runs as native 32-bit code under O0, O2, and O3 with
UBSan and explicit stack realignment. Ten independent source mutations prove
the status offset, mask byte and gate, type shift and class, sign bit, helper
polarity, two Y query fields, and list traversal are all effective. The three
focused installed tests pass in 34.260 seconds. The 19 shared progress,
complete Game-data-layout, generated-PC16, and guarded-padder tests pass in
5.886 seconds.

The live linked caller census contains exactly two direct JAL sites and no
aligned pointer literals:

| Caller | ROM call site |
| --- | ---: |
| `func_1515E278` | `0x18B758` |
| `func_1515E43C` | `0x18B904` |

Both callers pass all five arguments and consume the returned record pointer.
The complete 35-function owner preserves the other 34 functions. Strict
qualified-versus-production comparison retains all 6,051 function addresses,
uses zero exclusions, and reports only `func_1515EB84` changed before
installation and no changed function afterward. Protected Game data remains
exact at 189,088 bytes across 720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Qualified/production owner | `b210cb6a5e6ed4f6841ced18ee3f4d345d0181fbad1b81f9e8fce705199a8be3` |
| Predecessor linked ELF | `3ba75ce7ff9c686009dc1f8d1cb3814d8067c68c6a9d08bae52399a520d85d34` |
| Qualified/production linked ELF | `90b315f46491d60912ae9db12c5ba8dea367cd93a63fc25ff2f459bdf450ef01` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `984e71d342748d55df34c6975bb24d250a315893cea5d09e346b8b878ea8bd14` |

The actual `make all -j4` rebuilt the complete guarded corpus, regenerated the
linker script, linked `conker.us.elf`, and generated `conker.us.bin`. Every
existing guard remained valid. The build stopped only at the expected final
whole-ROM SHA mismatch while the decomp remains incomplete.

The permanent qualifier and evidence tools were committed first in the tools
submodule as `afccdda` (`test(game): qualify point record search`). Production
source and the four checked rows were installed only after that tools commit.

## Graph retention

The required bounded Graphify update extracted 24,313 nodes versus the
retained 58,384. It failed closed without `--force`, preserving 31,816 nodes
from 3,754 still-existing files outside the reduced scan corpus. The retained
`graphify-out/graph.json` remains 77,250,386 bytes with SHA-256
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim. The
existing Graphify 0.9.20-skill/0.9.26-package and empty `devcontainer.json`
warnings remain non-blocking and did not replace the graph.

## Continuation

The fresh ordinary Game ranking keeps the same seven documented boundary
cases outside the direct-C queue: `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Continue with ordinary candidate `func_15190F9C` (60 words,
60 real differences), followed by the remaining 60-difference ties. Every
candidate still requires source, ABI/caller, owner, guest/native, actual Make,
complete-image, protected-data, production recount, documentation, and graph
retention gates before credit.
