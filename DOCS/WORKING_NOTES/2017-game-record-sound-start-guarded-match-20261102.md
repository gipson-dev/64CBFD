# 2017 - Record sound-start matched as guarded C

Verified 2026-11-02. Production is **4,087/5,511 (74.16%)**; Game is
**3,414/4,838 (70.57%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,424 functions remain different. The active 80% target is
**4,409/5,511**, requiring **322 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_150A23E4` replaces its zero-return placeholder in
`conker/src/game/generated_CDE80.c`. It is the record sound-start routine at
`0x150A23E4`, ROM `0xCF894..0xCF970`, owned by `generated_CDE80`. The recovered
interface is `void (GeneratedCDE80Record *)`; both original caller windows
ignore its result.

The existing 0x34-byte record type supplies signed origins at offsets 0, 2 and
4, flags at 0x15, selector byte 0x17, word flags at 0x18, packed sound and
parameter halves at 0x1C, and full-word state at 0x20. An inactive record calls
the typed twelve-argument `func_1000FA64` audio submitter with its packed sound,
coordinates, `327 * (selector & 0x7F)`, conditional flag `0x8000`, packed low
halfword and mode 8 or 0x108. State 1 is published only after the call. An
already active record skips the call but is normalized to state 1.

This adopts the semantic recovery privately qualified in [Note 1980](1980-record-sound-start-private-qualification-20261101.md).
That note correctly rejected manufacturing retail's extra epilogue instruction
through unsupported source constructs. The semantic C remains natural here;
the independently qualified fail-closed guard layer now records the compiler
schedule difference explicitly.

## Guarded compiler closure

IDO emits **54 words/frame64** while retail has **55 words/frame64**. The call
preparation and the unguarded `R_MIPS_26` binding to `func_1000FA64` already
match. Nine checked rows normalize the opening branch displacement and one
closed epilogue schedule at offsets `0x018`, `0x0B8`, `0x0BC`, `0x0C0`,
`0x0C4`, `0x0C8`, `0x0CC`, `0x0D0` and `0x0D4`; the final row inserts retail's
one additional zero delay-slot word. All rows are relocation-free. Mutating
each expected candidate word causes the padder to fail closed.

The resulting owner matches all **55 retail words**. All 27 owner neighbors
and normalized pools remain fixed. A literal full-image prediction changes
only `func_150A23E4`, expands its symbol extent from the old 12-byte placeholder
to 220 bytes, preserves all 6,051 other function bodies and all function
addresses, and uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural 54-word candidate payload | `c543a36df03e35fa34f5f8fe30d2cae9649ad718370a723e6b24494cb141801d` |
| Retail/guarded 55-word payload | `7dd86eaa37304feb641883029b5d159fcd7b46457b17f107522e4b13e2d5f375` |
| Qualified/production owner | `c498cda434de53868bb15a1a3458fae2a8ac2386cf32cc78671412357df3bbf0` |
| Predecessor linked ELF | `eba8c0724344020251b40f67f7b48d9a4bb51d4999518ac66fca24ccb2919207` |
| Qualified/production linked ELF | `461d741a53e52ce70ec2163e1a71eff75c0ac788b254a3a8e23f15f5e4ddaa8c` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `8ad5f9369b6da6409d62591e6f430c67cb05913b7216b56b2cc29e748e5049cd` |

## Semantic and production qualification

The retained semantic corpus covers 2,580 cases across three layouts, for
7,740 cases and 15,480 original/candidate executions. It covers selector and
flag bytes, state and packed-word boundaries, signed coordinates, helper
mutations, incoming stack phases and 48 fired access-prefix pairs. Native
32-bit O0/O2/O3 runs pass every case with seven effective controls per profile.
The retained 109-word enqueue helper is byte-exact and runs 756 connected
cases/1,512 executions. Both original caller windows execute 120 cases each
and ignore the return value as recovered.

The new five-test guard suite passes and checks the nine guard mutations,
owner/pool closure, literal full-image prediction, protected data and installed
source/object/image coherence. The five retained semantic tests also pass from
the installed state without mutating live production artifacts. Shared progress
and padder suites pass 12 tests; the protected Game-data audit remains exact at
189,088 bytes across 720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The actual `make all -j4` rebuilt the generated, converted and libultra corpus,
linked `conker.us.elf` and produced `conker.us.bin`. It stopped only at the
expected whole-ROM SHA mismatch because the overall decomp is incomplete. A
fresh independent recount credits exactly this function. The permanent guard
experiment and tests were committed first in the tools submodule as `45347ce`.
Retained stage: `conker/build/game-record-sound-start-150A23E4-guard-match/`.

This is instruction-level and bounded semantic proof, not natural whole-game or
gameplay acceptance. The README changes only its aggregate byte-exact rows.
No Claude call was needed.

## Graph retention

The required Graphify update extracted 24,174 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

Continue from a fresh ordinary Game ranking. Keep handwritten/custom-entry
`func_150A76F0`, `func_150A613C`, `func_151F8870` and stack-resume
`func_150AE280` outside ordinary C screens. `func_15115F68` and
`func_151AE2BC` remain private and uncredited until their unresolved compiler
and ABI boundaries are closed. Every new candidate still requires source,
ABI/caller, owner, guest/native, actual Make, complete-image, protected-data,
production recount and documentation gates before credit.
