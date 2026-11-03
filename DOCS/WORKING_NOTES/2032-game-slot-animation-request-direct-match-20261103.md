# 2032 - Slot animation request matched directly from C

Verified 2026-11-03. Production is **4,102/5,511 (74.43%)**; Game is
**3,429/4,838 (70.88%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,409 functions remain different. The active 80% target is
**4,409/5,511**, requiring **307 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_1507F54C` replaces its zero-return placeholder in
`conker/src/game/generated_AC030.c`. It is the slot-selected actor animation
request at VA `0x1507F54C`, ROM `0xAC9FC..0xACAF0`, owned by
`generated_AC030`. Its recovered interface is
`void func_1507F54C(u8 *actor)`.

Actor byte `+0x13C` selects the route. Values below 100 start animation
`0x0F` at scale `1.0f` and blend `3.0f`. Higher values index
`D_800B85A4` with the retail `0x32C`-byte stride, then map descriptor kinds
`0x57`, `0x8C`, `0xA8/0xA9`, and `0x89/0xBA` to animation requests
`0x115`, `0x1A5`, `0x1AF`, and `0x1FA`; all other kinds use `0xD8`.
That route uses scale `1.0f` and blend `4.0f`. Both routes pass zero for the
remaining two floating arguments and mode word to `func_1505E650`.

Retail contains exactly two direct JALs from `func_1507F640`, at ROM
`0xACE2C` and `0xACF1C`, and no aligned pointer literals. Both call sites
branch away without reading `v0`, confirming the recovered void return.
Alternate Source contains no `func_1507F54C` donor.

## Natural compiler and image closure

The semantic `-O2 -g3` body naturally emits all 61 retail words with the
retail 40-byte frame and all four original relocations. No expected-word
guards, inserted words, omissions, or compiler patches are used. The only
source-layout sensitivity is the order of semantically independent switch
case groups: placing them in retail block order makes IDO emit the complete
routine directly.

The two HI16/LO16 words bind `D_800B85A4`; the two J26 words bind
`func_1505E650`. All fifteen other owner functions and normalized pools remain
unchanged. Across the linked image, only `func_1507F54C` changes; all 6,051
function addresses remain fixed, and strict comparison uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural relocation-masked 61-word payload | `aaac11ae0af6521e041ecea665bc5dca4dd3b84b857d97daca65f5a0aa3e7241` |
| Retail linked 61-word payload | `7780fc9e928d71998ded20a41b800f5048d3bfc22a5b875dfa069e1dcf13cc90` |
| Qualified/production owner | `72efcb5449e75b729ca866174669a1c75b7b9648d91d47d12abb43b4a1bb238f` |
| Predecessor linked ELF | `d40a3b3f73d4802ac72ca9a990b6222bed99d88931911ca1b3dd5861af9d94e1` |
| Qualified/production linked ELF | `9d0032f108590c4cdf40e6dabaca153caa2dbb8a9c58aa01fc517af4c9493818` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Unchanged production guard table | `dd2518e2b31669cd85237eb72b3fc24d79f59789301cd63d39b28551a2ae470f` |

## Semantic and production qualification

The big-endian guest oracle executes 2,056 connected cases. It covers low-slot
boundaries 0, 1, 98 and 99; high slots 100, 101, 127 and 255; every one of the
256 descriptor-kind bytes; and both stack phases. Every one of the 61 retail
words executes, and the complete seven-argument mixed O32 helper packet
matches the independent reference model.

Native 32-bit O0/O2/O3 profiles exhaust all 256 slot bytes crossed with all
256 kind bytes, 65,536 cases per profile and 196,608 total, with warnings as
errors and UBSan trapping. Twelve compiled controls independently reject the
wrong actor field, threshold, table stride, default request, each mapped
request family, high scale/blend, and low request/blend. The predecessor
payload, target-body corruption and target-size corruption fail closed.

The installed four-test suite passes in 48.390 seconds. Thirteen shared
progress, generated-PC16 and protected-layout tests pass in 10.012 seconds;
the six guarded-padder tests pass in 0.049 seconds. Protected Game data remains
exact at 189,088 bytes across 720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The actual `make all -j4` rebuilt the changed owner, regenerated the linker
script, linked the production ELF and generated the binary. Make stopped only
at the expected whole-ROM SHA mismatch while the decomp remains incomplete.
The production owner and ELF equal their independently predicted qualified
artifacts byte for byte. A fresh production recount credits exactly this
function.

The candidate qualifier and permanent tests were committed first in the tools
submodule as `a73725e`. The existing `func_1507EA44` animation-request tools
were preserved byte-for-byte under their original names; this function's
suite uses the distinct slot-animation filename. This is instruction-level
and bounded semantic proof, not natural whole-game or gameplay acceptance.
The README changes only its aggregate byte-exact rows. No Claude call was
needed.

## Graph retention

The required bounded Graphify update produced a candidate graph with 58,383
nodes versus the retained 58,384. It failed closed without `force=True`,
preserving 31,816 nodes from 3,754 still-existing files outside the scan
corpus. The retained graph SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

The fresh ordinary Game ranking still keeps the six documented boundary cases
`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68` and `func_151AE2BC` outside the direct-C queue. The next
ordinary candidate is `func_150A6760` (64 words, 60 current real differences),
followed by the other 60-difference ties. Every candidate still requires
source, ABI/caller, owner, guest/native, actual Make, complete-image,
protected-data, production recount and documentation gates before credit.
