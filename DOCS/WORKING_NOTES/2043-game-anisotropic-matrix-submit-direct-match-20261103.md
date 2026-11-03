# Game Anisotropic Matrix Submit Direct Match

Date: 2026-11-03

## Result

`func_151B9310` now replaces its zero-return placeholder with byte-exact direct
C. Its complete retail slot is **62 words / 248 bytes**, frame `0x68`, VA
`151B9310..151B9408`, and ROM `1E67C0..1E68B8`. A fresh production recount
credits exactly this function:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,113 / 5,511 (74.63%) | 0 | 1,398 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,440 / 4,838 (71.10%) | 0 | 1,398 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The active 80% target now needs **296 more** exact functions.

## Source recovery and direct closure

The callback receives a fixed-matrix output pointer and a state pointer. It
builds a floating rotation matrix through `func_150A8050`, with zero X/Y
angles and the live Z rotation at state offset `+0x170`. It then copies the
live XYZ translation at `+0x38/+0x3C/+0x40` into matrix row three. Matrix rows
zero and two use the horizontal scale at `+0x18`; row one uses the vertical
scale at `+0x1C`. All nine 3x3 basis elements are scaled in retail order before
`guMtxF2L` converts the result to the requested output. The callback returns
one so it remains active.

`MatrixWorkspace151B9310` retains one 32-bit prefix before its 4x4 floating
matrix. That prefix is not read or written; it preserves the original local
aggregate shape and places the matrix at `sp+0x28`. With that source-level
layout, IDO emits the retail `0x68` frame, saved-register lifetime, call
schedule, matrix accesses, and all 62 words directly. There are **zero word
guards** and no inserted or omitted instructions.

The compact-object payload, with relocation fields unresolved, has SHA-256
`655f861431d3fcfafbc276689131883ee4f015a3ca30e7023aa92f94f5091b06`.
The linked retail payload has SHA-256
`0a521ec318dff98a192fc3506fcb1acdd34bc02b808f90d9623325e6d67b198d`.
The only bindings are the J26 call to `func_150A8050` at `+0x24` and the J26
call to `guMtxF2L` at `+0xD8`.

## Semantic, registry, and production qualification

The big-endian guest oracle runs 512 executions with all 62 retail words
covered. It verifies both helper interfaces, callback clobbers, the captured Z
rotation, live post-rotation translation and scale reads, all nine basis
products, fixed-output conversion, return value, and stack-phase variants.
Native 32-bit O0, O2, and O3 builds pass, while ten independent
behavior-changing controls fail through semantic mismatch. The three focused
tests and 25 shared oscillator, progress, Game-data-layout, generated-PC16,
and guarded-padder tests all pass: 28 installed tests in 87.022 seconds.

There are no direct JAL callers. The sole aligned pointer literal is at ROM
`0x22E45C`, callback entry `D_8008998C[4]`. The complete five-function owner
preserves the other four functions. Strict qualified-versus-production
comparison retains all 6,051 function addresses, uses zero exclusions, and
reports only `func_151B9310` changed before installation and no changed
function afterward. Protected Game data remains exact at 189,088 bytes across
720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Qualified/production owner | `61642e47702d9260b3defb844709b4b843fa4115572880e44bc6c5fad0bf29c8` |
| Installed source | `d836fe93fa76f7a880b66e828353cc4f29b9d68cc16a4470032bcae9703e8108` |
| Predecessor linked ELF | `cb7cd39489d81a8e68f9b1d0851ee5f3bdfe12fa07bf1aee9243915ed0f335bc` |
| Qualified/production linked ELF | `1d77d5a61d9078475f2d7eeca2090c3300f2fb9165f1ac59b7eaad75c4b9a524` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Unchanged production guard table | `2da43f2c2acf5fed809fd5e948b1b1342a1a085801a78751b352a33cd7974664` |

The actual production Make rebuilt the changed owner, regenerated the linker
script, linked `conker.us.elf`, and generated `conker.us.bin`. Because this is
a direct match and the guard table did not change, no unrelated guarded owner
needed rebuilding. The build stopped only at the expected final whole-ROM SHA
mismatch while the decomp remains incomplete.

The permanent qualifier and evidence tools were committed before production
source as `564bd76` (`test(game): qualify anisotropic matrix submit`). The
post-install source-state correction was then banked as tools commit `08b7e04`
(`test(game): support installed matrix submit`).

## Graph retention

The required bounded Graphify update retained 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. It rebuilt the same
58,384-node graph with 120,125 edges and 5,069 communities; visualization was
skipped at the configured 5,000-node limit. The retained/refreshed
`graphify-out/graph.json` is 78,559,628 bytes with SHA-256
`ccd9c3fbb65185bab508ce53d461aa7e21e29b0afd33a8525e7f7764b69680fc`.
This is bounded old-node retention evidence, not a full-corpus extraction
claim.

## Continuation

The fresh ranking still begins with seven documented non-ordinary boundary
cases: handwritten/custom-ABI `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Continue the ordinary queue at `func_150B709C` (67 words, 61
real differences), the first ordinary row among the current 61-difference
tie. Every candidate still requires source, ABI/caller, owner, guest/native,
actual Make, complete-image, protected-data, production recount,
documentation, and graph-retention gates before credit.
