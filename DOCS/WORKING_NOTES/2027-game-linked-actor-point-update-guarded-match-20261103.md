# 2027 - Linked actor point update matched as guarded C

Verified 2026-11-03. Production is **4,097/5,511 (74.34%)**; Game is
**3,424/4,838 (70.77%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,414 functions remain different. The active 80% target is
**4,409/5,511**, requiring **312 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_15107924` replaces its zero-return placeholder in
`conker/src/game/generated_133190.c`. It is the linked-actor point updater at
`0x15107924`, ROM `0x134DD4..0x134ED0`, owned by `generated_133190`. Its
recovered interface is:

```c
s32 func_15107924(u8 *owner, u8 *changed);
```

The routine resolves the owner's link at `+0x60` and the linked actor stored
at the head of that record. It returns false without touching `*changed` when
the actor is inactive or the link's identity byte at `+4` no longer matches
the actor byte at `+0x3B`. A valid link clears `*changed`, saves the owner's
three-float point at `+0x14`, and calls `func_15107A20` with the actor and the
link's signed yaw/pitch halfwords at `+6/+8`. If any point component changes,
it sets `*changed` and calls `func_15107AE0` to rebuild the two fractional
points at `+0x20/+0x2C` toward the endpoint at `+0x38`. It returns true for a
valid link whether or not the point moved.

The callback has no direct `jal` caller. Its sole aligned literal pointer is
the first entry of `D_80088C10` at ROM `0x22D6D0`.

## Guarded compiler and image closure

The recovered `-O2 -g3` body naturally emits all **63 words** with the two
correct helper bindings:

- `+0x7C`: `R_MIPS_26:func_15107A20`
- `+0xDC`: `R_MIPS_26:func_15107AE0`

IDO selects a 72-byte natural frame, while retail uses 64 bytes. Eleven
strict expected-word guards change only the frame allocation/deallocation and
the corresponding stack-local offsets at `+0x00`, `+0x10`, `+0x1C`, `+0x34`,
`+0x54`, `+0x80`, `+0x84`, `+0x8C`, `+0x98`, `+0xB0` and `+0xF0`. The other 52
words and both relocations emit naturally. There are no inserted or omitted
instructions, no assembly block, and no profile change.

All 36 other functions in `generated_133190`, normalized owner pools, all
6,051 function addresses and the complete allocated image outside this
function remain fixed. The qualified ELF is the predecessor ELF with the
literal 252-byte retail body and its symbol size changed from the placeholder
extent to 252 bytes. Strict full-ELF comparison uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural relocation-normalized 63-word payload | `636bec741ef2e2ce328130a529f68e8c61baeda92620242606cbc681a980938f` |
| Retail linked 63-word payload | `835b33ad801fb40a2081dccea40e19beb29da8f9798ad0e2d24346a9c59209f4` |
| Qualified/production owner | `e0f5164e395c6ccb5ba63cc5a2ff64cbfdc23021855d75c46139b5bcc87f78f1` |
| Predecessor linked ELF | `041585296b54ae734496f333432259d1f9841251d94f070ef805f3965b9a3846` |
| Qualified/production linked ELF | `ff7b3420a82c34f7403ef495d3adfa3293349711905403bde9b5e54f8234b23e` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `1f973e977a2fa5f0cc277b34384fe09b70683a7f7a6b2c64650a7051e9d0a9fb` |

The natural payload hash masks relocation immediates, while the retail body
hash is taken from the linked ROM, so those hashes are intentionally unequal.

## Semantic and production qualification

The big-endian guest oracle executes **96 cases** across inactive, stale,
unchanged and changed routes; all three changed axes; two stack phases; two
actor-ID boundaries; and two signed angle patterns. It runs the real connected
origin, direction, trigonometric and fractional-point helpers and compares
complete public state and traces. It covers 62 of 63 words; only the
compiler's unreachable load at `+0x4C` has no control-flow edge.

Native 32-bit O0/O2/O3 profiles pass **12,288** bounded defined-domain cases
under UBSan. Eight compiled negative controls independently reject the wrong
link field, actor identity, yaw field, point field, missing changed-byte clear,
endpoint, and either fractional output. The permanent four-test suite also
verifies the exact raw payload and bindings, callback registry, 36 owner
neighbors, strict literal whole-image prediction, protected data, and
installed source/object/image coherence. The focused installed suite passed
in 123.137 seconds. The 19 shared progress, PC16, padder and protected-layout
tests passed in 32.059 seconds.

The protected Game-data audit remains exact at 189,088 bytes across 720
owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The actual `make all -j4` rebuilt the guarded owners, linked
`conker.us.elf`, and produced `conker.us.bin`; it stopped only at the expected
whole-ROM SHA mismatch because the overall decomp is incomplete. The actual
production ELF equals the independently predicted ELF byte for byte, and a
fresh recount credits exactly this function.

The candidate qualifier and permanent tests were committed first in the tools
submodule as `c17ade3`, followed by installed-manifest support in `e1a8404`
and the installed predecessor-manifest reconstruction in `853e408`. Retained
stage: `conker/build/game-linked-actor-point-update-15107924-match/`.

This is instruction-level and bounded semantic proof, not natural whole-game
or gameplay acceptance. The README changes only its aggregate byte-exact rows.
No Claude call was needed.

## Graph retention

The required Graphify update extracted 24,247 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim. Graphify
also reported the known local 0.9.20-skill/0.9.26-package warning and one
zero-node `devcontainer.json` source.

## Continuation

Continue the ordinary Game queue at `func_151606A8` (63 words, 59 current real
differences), then re-rank before committing to `func_151C61A0` or
`func_151CD3CC`. Keep `func_150A76F0`, `func_151F8870`, `func_150A613C`,
`func_150AE280`, `func_15115F68` and `func_151AE2BC` outside an ordinary
direct-C screen until their existing boundaries are resolved. Every candidate
still requires source, ABI/caller, owner, guest/native, actual Make,
complete-image, protected-data, production recount and documentation gates
before credit.
