# 2004 - Weighted event emitter matched as guarded C

Verified 2026-11-02. Production **4,071/5,511 (73.87%)**; Game
**3,398/4,838 (70.24%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,440 different; one existing semantic C function is newly byte-exact.
The active 80% target is **4,409/5,511**, requiring **338 more**. This is
progress toward that goal, not completion.

## Existing semantic recovery promoted to a complete match

`func_150E8B1C` is the 576-byte/144-word weighted event emitter at VA
`0x150E8B1C`, ROM `0x115FCC`, in
`conker/src/game/generated_113D60.c`. It retains the complete 0xC8-byte retail
frame and its caller-qualified `void (u8 *record)` interface.

[Note 950](950-game-weighted-event-emitter-semantic-recovery-20261004.md)
replaced the original placeholder with the complete semantic body, documented
the weighted-list and child-event contract, and left the remaining 44-word
compiler gap explicit. [Note 956](956-game-child-emission-callback-recovery-and-fitting-20261004.md)
subsequently connected and qualified the code-0x34 child updater. This pass
does not rewrite that established behavior: it closes the remaining compiler
allocation and scheduling gap around the existing C.

The function resolves the live origin, advances the payload accumulator from
the sampled rate, walks the weighted descriptor chain using the strict retail
boundary, fills a child position, applies the distance gate, allocates a
code-0x34 child and copies the complete 24-byte payload. Allocation failure,
callback clobbers and payload reload timing retain the retail behavior; no
defensive clamps, null checks or loop caps were invented.

## Guarded compiler closure and relocations

Fresh IDO emits the complete 144-word slot with the correct frame, control
flow, calls and delay slots. Forty-four checked expected-word rows normalize
closed S2/S3, S0/S1, floating-register, private-local and independent schedule
allocation. Every row replaces one existing instruction: there are no
insertions or omissions.

Twelve guarded words carry an expected or replacement relocation. Nine moved
replacement relocation sites keep the bindings for `D_800BE9A4`,
`D_800DCD90`, `D_800DCDC4`, `D_800A1384` and `D_800A138C` at the retail
instruction offsets. The complete function contains 21 relocation entries
covering all data and callback bindings. The original link plus three
independent code/data rebases reproduce the symbolically relocated slot, not
a fixed-address coincidence. Every one of the 44 expected-word checks and 44
expected-relocation checks is also corrupted independently; all 88 variants
fail closed.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor linked ELF | `4e2f6b37c94c63806e8400c1cf95012ff941ce3dbe559d0ed6b3b5666d353234` |
| Qualified/production owner | `ab0410da1906778cf85b416f24dd125a81e0b9020bc012cac97808fc62b4634d` |
| Production/expected linked ELF | `f513df5a777677b9ecd6da36d1bd009619d1131e8804559530709160d17323c2` |
| Raw linked C slot | `e7be4237d5fe90c7581ac913539001c5b38b07fc59a1025bd2896afda8239ff9` |
| Retail/guarded linked slot | `bc9cb51d1ee078762a7fc912c002c67bc3b9beb620499dace7a20888f55e33de` |

## Semantic, owner and whole-image qualification

The two permanent suites contain 16 installed-state tests. The new raw-C
guest differential harness executes 28 candidate/retail runs across both stack
phases and covers 143 of 144 retail words. The sole unvisited instruction is
the impossible divide-by-zero break at `+0x1B4`; normal execution proves the
nonzero divisor before that path. Cases cover no-emission gates, weighted
multi-hop selection, near/far distance results, allocation failure, parameter
and metadata reloads, callback clobbers, strict boundaries and both successful
and failed child creation. The retained host/native suite separately exercises
the connected creator, updater, payload, list and child behavior.

The real owner contains this function plus 28 neighbors. The qualification
object preserves every neighbor and relocation byte-for-byte. The strict
full-image prediction changes only this target slot while retaining all 6,051
function addresses and zero exclusions. Actual Make reproduced both the
qualified owner and the predicted linked ELF byte-for-byte.

Changing the shared guard manifest intentionally forced the complete padded
corpus to rebuild. It completed without stale guards, compiler, padder,
assembler or linker failures. `make -C conker all -j2` generated the
development ROM and failed only the expected final retail SHA-1 check because
the wider decomp image is not yet byte-identical. The production map keeps all
canonical addresses fixed and has SHA256
`0f9af6c3578cff80ed406b8510f09e8dd211b6d07abb0e1c6614b4640522165d`.

Protected Game data remains exactly 189,088 bytes across 720 owners with zero
different bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Converted-C totals do not change because the function already had semantic C.
This is instruction-level and bounded semantic proof, not a claim of natural
whole-game effect acceptance.

The permanent experiment and qualification suite were committed first in the
tools submodule as commits `fc94123` and `7f27acb`. The retained qualification
stage is
`conker/build/game-weighted-event-emitter-150E8B1C-match/`. The root README
changes only its aggregate byte-exact rows. No Claude call was needed.

## Graph retention and next step

The required Graphify update extracted 24,082 nodes versus the retained
58,384 and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep each
candidate private until the ABI, semantic, caller, owner, actual-Make,
whole-image, protected-data, recount, documentation and graph-retention gates
pass.
