# 2003 - Descriptor tag adjuster matched as guarded C

Verified 2026-11-02. Production **4,070/5,511 (73.85%)**; Game
**3,397/4,838 (70.21%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,441 different; one existing semantic C function is newly byte-exact.
The active 80% target is **4,409/5,511**, requiring **339 more**. This is
progress toward that goal, not completion.

## Private recovery promoted to production

`func_150174C0` is the 184-byte/46-word descriptor tag adjuster at VA
`0x150174C0`, ROM `0x44970`, in `conker/src/game_447B0.c`. It keeps its
natural 8-byte frame. The semantic reconstruction first qualified privately in
[Note 1968](1968-descriptor-adjustment-private-semantics-and-codegen-20261101.md);
that note deliberately left the source, declaration and matching credit
uninstalled while the remaining compiler-shape gap was unresolved.

The adopted `void func_150174C0(s32 adjustment)` walks signed descriptor
indices over 24-byte `DescriptorTagRow` records. It reloads the live table
pointer and row count while walking the eight halfword entry slots. Entries
whose high nibble is tag 2 receive the adjustment with guest-accurate low-16
wrapping. The sole original caller ignores the incidental retail `V0` loop
index, so the void interface is the caller-qualified ABI rather than a forced
return value.

The shared declaration for `D_800D23C0` is corrected from an integer to
`u8 *`, and the sole allocation assignment no longer casts the pointer to an
integer. This repair forced a full dependency rebuild and therefore also
audited every shared-header consumer.

## Guarded compiler match and symbolic closure

Fresh IDO emits the full 46-word function with the correct frame, loop shape,
loads, stores and branch structure. Thirteen checked expected-word rows
normalize one closed inner-loop register-allocation and scheduling cycle. They
do not insert or omit instructions. The normalized slot matches every retail
word, including the branch offsets and the store through the live entry
pointer.

All eight symbolic relocation sites remain at retail offsets:

- `D_80087380` at `0x00C/0x010` and `0x090/0x094`;
- `D_800D23C0` at `0x018/0x024` and `0x074/0x078`.

Independent rebases of the function and both globals confirm symbolic binding
rather than fixed-address coincidence. The relocation template SHA256 is
`27fbaa90d618da4e80e23cdaf8c5fca9d52eb079186ac48923577ea973bfd34f`.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor linked ELF | `0e1cc15dcf288623c7ad505aad3b4cd4ad8b1af762b5221f90c3578c398b32ca` |
| Qualified/production owner | `284a4a47018cfd190f45b5a68748e16a206dba847e2bc56fe8ffdf3c881b7a7c` |
| Production/expected linked ELF | `4e2f6b37c94c63806e8400c1cf95012ff941ce3dbe559d0ed6b3b5666d353234` |
| Raw candidate 46-word slot | `8e57209dd5813886c604aa2b29a938ddc3e8629b4052c3387b7b431d976ecea7` |
| Predecessor linked slot | `33b7e0067d518a2a347cf88a97b482aec4be48fd2878d9a7b6bead6bd6188e2f` |
| Retail/guarded linked slot | `af19389bcf0550852cf32e581d96bc8bab3e1ded574db01cede8ef7e31afaf0d` |

## Semantic, owner and whole-image qualification

The permanent five-test qualification suite passes after installation. Its
guest harness executes 1,014 cases against both candidate and retail, including
signed outer bounds, all tag classes, low-16 wrap boundaries, table aliases,
live pointer/count reloads, access ordering, incidental `V0`, saved registers
and three independently rebased layouts. Native 32-bit O0/O2/O3 controls and
canaries pass; five deliberately wrong semantic variants remain effective.
The sole caller, argument ABI, owner object, guard manifest, padder and
relocation behavior are covered by the same retained suite.

The private strict-image prediction contains 6,051 functions, changes only
`func_150174C0`, keeps every canonical address fixed and uses zero exclusions.
It accounts for the symbol extent increasing from the prior 152-byte semantic
body to the complete 184-byte retail slot. Actual Make reproduced both the
qualified owner and predicted ELF byte-for-byte. Protected Game data remains
exactly 189,088 bytes across 720 owners with zero different bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The shared-header change forced a complete padded-corpus rebuild. It completed
without stale guards, compiler, padder, assembler or linker failures.
`make all -j2` generated the development ROM and failed only the expected final
retail SHA-1 check because the wider decomp image is not yet byte-identical.
The fresh linker map keeps all canonical addresses fixed; its only difference
from the predecessor map is the non-address `.mdebug` input-size line for the
Debugger owner. Its SHA256 is
`0f9af6c3578cff80ed406b8510f09e8dd211b6d07abb0e1c6614b4640522165d`.

The qualification tool and tests were committed first as tools commit
`75eca94`; installed-state freeze handling is tools commit `0a45474`. The
retained private stage is
`conker/build/game-descriptor-tag-adjust-150174C0-guard-match/`. Converted-C
totals do not change because this function already had semantic C. The root
README changes only the aggregate byte-exact rows. No Claude call was needed.

## Graph retention and next step

Graphify's retained graph still contains `func_150174C0`, now implemented at
`conker/src/game_447B0.c:L51`. The required update extracted 24,076 nodes
versus the retained 58,384 and failed closed without `--force`, preserving
31,816 nodes from 3,754 still-existing files outside the reduced scan corpus.
The retained graph SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep
handwritten custom-ABI `func_150A76F0` in its separate assembly workstream and
keep each candidate private until the ABI, semantic, owner, actual-Make,
whole-image, protected-data, recount, documentation and graph-retention gates
pass.
