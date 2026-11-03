# 2033 - Dual menu-record replacement matched directly from C

Verified 2026-11-03. Production is **4,103/5,511 (74.45%)**; Game is
**3,430/4,838 (70.90%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,408 functions remain different. The active 80% target is
**4,409/5,511**, requiring **306 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_150B7560` replaces its zero-return placeholder in
`conker/src/game/generated_E4070.c`. It is the fixed dual menu-record
replacement at VA `0x150B7560`, ROM `0xE4A10..0xE4B0C`, owned by
`generated_E4070`. Its recovered interface is `void func_150B7560(void)`.
The sole direct caller is command-state case 6 in `func_150B6BC0`, at ROM
`0xE40E8`; that caller does not consume `v0`. Retail contains no aligned
pointer literals to the entrypoint.

The routine first releases and clears the record stored at `D_800D9898` when
present. It constructs a 60-byte `MenuRecordDescriptorE4070` on its 88-byte
stack frame with asset `D_800918DC`, identity 77, screen dimensions 88 by 88,
scale values `60.0f`, 4096 coordinate fields, and byte configuration
`0,15,255,0,0,255,7,17,1,0`. It then releases the record at `D_800D98A4`
when present, replaces that slot with the result of `func_15169968`, and sets
menu command state `D_800D9890` to 3.

The first release callback is allowed to mutate both globals: the routine
still clears `D_800D9898` after that callback and observes the then-current
`D_800D98A4`. The second release callback may mutate `D_800D98A4`, but the
factory result overwrites it. The factory may mutate the state byte, but the
final state-3 store wins. These are live sequencing properties, not assumptions
from a static field list.

## Natural compiler and image closure

An isolated screening translation unit initially showed twelve differences,
all independent descriptor-store orderings. Compiling the same readable body
inside the complete `generated_E4070.c` owner with its retail
`-O2 -g3 -Wo,-loopunroll,0` profile naturally emits all 63 retail words. No
expected-word guards, inserted words, omissions, compiler patches, or source
distortions are used. This owner-context result supersedes the isolated
screening schedule.

The natural payload retains all fifteen original relocations: six HI16/LO16
pairs for `D_800D9898`, `D_800D98A4`, `D_800918DC`, and `D_800D9890`, plus
three J26 calls to `func_1516972C` twice and `func_15169968` once. All twenty
other owner functions and normalized pools remain unchanged. Across the linked
image, only `func_150B7560` changes; all 6,051 function addresses remain fixed,
and strict comparison uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural relocation-masked 63-word payload | `5677e7783af303c4029a9647447893ca4e4ccf580dc9bac47e2cbd4d69d869ea` |
| Retail linked 63-word payload | `f4476a36e465c88b78cc9a8faab2b241bc75847e559d38b4cecec43ceb10c6a2` |
| Qualified/production owner | `bd707e1b666779082d434f96fd77119282c99aaf4ad7a2495b4363dcaf116ae5` |
| Predecessor linked ELF | `9d0032f108590c4cdf40e6dabaca153caa2dbb8a9c58aa01fc517af4c9493818` |
| Qualified/production linked ELF | `b51f10a96c977eaad1da4dab466420ece3e4bf3339f377a18d8c5a425cdf16f1` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Unchanged production guard table | `dd2518e2b31669cd85237eb72b3fc24d79f59789301cd63d39b28551a2ae470f` |

## Semantic and production qualification

The big-endian guest oracle covers both record slots null and non-null, first
callback mutations that create or replace the second record, second callback
mutations, factory mutations, and both stack phases. It validates every
defined descriptor field at the factory boundary, release order and pointer
identity, final overwrite precedence, saved-register lifetime, and all 63
retail words across 16 cases. Reserved stack-private descriptor bytes are not
claimed as initialized.

Native 32-bit O0/O2/O3 profiles execute all eight null/mutation combinations
per profile with warnings as errors and UBSan trapping. Ten compiled controls
independently reject a missing first clear, wrong identity, configuration,
asset, coordinate, float, second release, or final state. A separately compiled
wrong-state owner fails the checked payload gate. The frame, return epilogue,
sole JAL, absence of pointer literals, source-state reconstruction, production
object, and production ELF are checked explicitly.

The private five-test suite passes before installation in 119.016 seconds and
against the installed production object/ELF in 143.464 seconds. Thirteen shared
progress, generated-PC16 and protected-layout tests pass in 29.061 seconds;
the six guarded-padder tests pass in 0.045 seconds. Protected Game data remains
exact at 189,088 bytes across 720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The actual `make all -j4` rebuilt `generated_E4070`, regenerated the linker
script, linked the production ELF and generated the binary. Make stopped only
at the expected whole-ROM SHA mismatch while the decomp remains incomplete.
The production owner and ELF equal their independently predicted qualified
artifacts byte for byte. A fresh production recount credits exactly this
function.

The qualifier and permanent tests were committed first in the tools submodule
as `bfbdfee`. This is instruction-level and bounded semantic proof, not natural
whole-game or gameplay acceptance. The README changes only its aggregate
byte-exact rows. No Claude call was needed.

## Graph retention

The required bounded Graphify update extracted 24,284 nodes versus the retained
58,384. It failed closed without `force=True`, preserving 31,816 nodes from
3,754 still-existing files outside the reduced scan corpus. The retained graph
SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

The fresh ordinary Game ranking keeps seven documented boundary cases outside
the direct-C queue: `func_150A76F0`, `func_151F8870`, `func_150A613C`,
`func_150AE280`, `func_15115F68`, `func_151AE2BC`, and `func_150A6760`.
The newly parked `func_150A6760` is a 64-word handwritten-style bitstream
decoder with shared interior label `func_150A67D0`; defined semantic C expands
the body and worsens its current difference count. The next ordinary candidate
is `func_15133A94` (65 words, 60 current real differences), followed by the
other 60-difference ties. Every candidate still requires source, ABI/caller,
owner, guest/native, actual Make, complete-image, protected-data, production
recount and documentation gates before credit.
