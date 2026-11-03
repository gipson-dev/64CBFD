# 2028 - Actor point transform matched as guarded C

Verified 2026-11-03. Production is **4,098/5,511 (74.36%)**; Game is
**3,425/4,838 (70.79%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,413 functions remain different. The active 80% target is
**4,409/5,511**, requiring **311 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_151606A8` replaces its zero-return placeholder and removes the stale
commented non-matching draft in `conker/src/game_18D770.c`. It is the actor
point transform at `0x151606A8`, ROM `0x18DB58..0x18DC54`, owned by
`game_18D770`. Its recovered interface is:

```c
s32 func_151606A8(struct225 *arg0);
```

The routine builds a floating-point rotation matrix from the three angles in
the linked transform at `arg0->unk18`. It deliberately reloads that link after
`func_150A8050`, converts the signed halfwords at transform offsets
`+0x10/+0x12/+0x14` into the matrix translation row, and transforms the shared
vector `D_800A66B4 = { 0.0f, -415.0f, 0.0f }` through `func_150A7960`. The
three resulting floats are truncated through the retail FPU conversion path
and stored as halfwords at `arg0->unk14 + 0xE/+0x10/+0x12`; the routine then
returns one.

The callback has no direct `jal` caller. Its sole aligned literal pointer is
in `D_8008B0F0` at ROM `0x22FBBC`.

## Guarded compiler and image closure

The recovered `-O2 -g3` source naturally emits a 62-word, 136-byte-frame body
with the two correct helper calls and the `D_800A66B4` address pair. Retail is
63 words. Eight strict expected-word rows close one compiler-selected pointer
and global-address register cycle at `+0x28`, `+0x2C`, `+0x30`, `+0x48`,
`+0x50`, `+0x54`, `+0x60` and `+0x78`; the first row inserts the one missing
pointer-base instruction. Relocations move symbolically with that insertion:

- `+0x20`: `R_MIPS_26:func_150A8050`
- `+0x30/+0x34`: `R_MIPS_HI16/LO16:D_800A66B4`
- `+0x98`: `R_MIPS_26:func_150A7960`

There is no assembly block and no compiler-profile change. All 77 other
functions in `game_18D770`, all 6,051 function addresses and the complete
allocated image outside this function remain fixed. Strict full-ELF
comparison uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural 62-word object payload | `66bfdbc7d75829a423e0d784bc00f79d74acc5a985e871cddc856f98d7e9f34b` |
| Retail linked 63-word payload | `5f113140efbdc725cc6df2e06c9d27e1bd9bd3c364319744cdd8b1160904948e` |
| Qualified relocation-normalized 63-word payload | `9226318efe51e802cd7ee5c94501eafda07d3796961a7517e38f8e3428c4d936` |
| Qualified/production owner | `fffa894cc0341e060b28029978fe0d70f4b0b10dd52cbd0f68f0e0abcbfccd49` |
| Predecessor linked ELF | `ff7b3420a82c34f7403ef495d3adfa3293349711905403bde9b5e54f8234b23e` |
| Qualified/production linked ELF | `8ea0bd5a33b798d4d39b1dc1fe0450ff6efb3db4ddabf7807633c63556bb0a38` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `fffe1a835fb2b55e8d20d6ebb5236ce2c3e2d2a38da108c892aed29300303618` |

## Semantic and production qualification

The big-endian guest oracle executes 32 cases spanning both stack phases,
signed halfword-to-float conversion, transform and destination mutation across
both helper calls, and truncation to the low stored halfword. Those cases
cover all 63 retail words. Native 32-bit O0/O2/O3 profiles pass 4,096 cases
each, for 12,288 executions, together with seven effective compiled controls.

The permanent four-test suite verifies the raw payload and all four relocation
bindings, sole callback pointer, 77 owner neighbors, strict whole-image
prediction, protected data, installed source/object/image coherence and
deliberate payload, guard and complete-image corruption rejection. The focused
installed suite passed in 128.538 seconds. The 19 shared progress, PC16,
padder and protected-layout tests passed in 16.974 seconds.

The protected Game-data audit remains exact at 189,088 bytes across 720
owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The actual `make all -j4` rebuilt the full corpus after the shared guard-table
change, linked `conker.us.elf`, and produced `conker.us.bin`; it stopped only
at the expected whole-ROM SHA mismatch because the overall decomp is
incomplete. The actual production ELF equals the independently predicted ELF
byte for byte, and a fresh recount credits exactly this function.

The candidate qualifier and permanent tests were committed first in the tools
submodule as `cbf9b02`. This is instruction-level and bounded semantic proof,
not natural whole-game or gameplay acceptance. The README changes only its
aggregate byte-exact rows. No Claude call was needed.

## Graph retention

The required Graphify update extracted 24,255 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim. Graphify
also reported the known local 0.9.20-skill/0.9.26-package warning and one
zero-node `devcontainer.json` source.

## Continuation

Continue the ordinary Game queue at `func_151C61A0` (60 words, 59 current real
differences), then re-rank before committing to `func_151CD3CC`. Keep
`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68` and `func_151AE2BC` outside an ordinary direct-C screen until
their existing boundaries are resolved. Every candidate still requires
source, ABI/caller, owner, guest/native, actual Make, complete-image,
protected-data, production recount and documentation gates before credit.
