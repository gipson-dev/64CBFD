# 2026 - Actor direction submission matched directly from C

Verified 2026-11-03. Production is **4,096/5,511 (74.32%)**; Game is
**3,423/4,838 (70.75%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,415 functions remain different. The active 80% target is
**4,409/5,511**, requiring **313 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_150E4010` replaces its zero-return placeholder in
`conker/src/game/generated_1104D0.c`. It is the actor direction-submission
callback at `0x150E4010`, ROM `0x1114C0..0x1115CC`, owned by
`generated_1104D0`. Its recovered interface is:

```c
void func_150E4010(u8 *actor);
```

The routine returns immediately when the actor word at `+0x1B4` is zero. For
an enabled actor it treats `actor + 0x110` as the private extension, submits
the extension's `+0x60/+0x64` pair to `func_150484A0`, scales the returned
angle by `D_800A1050`, converts it through the compiler's unsigned
float-to-`u32` sequence, keeps the low halfword, subtracts `0x4000`, and forces
the result odd. It then calls `func_1505D1C4` with the live `+0x30/+0x34/+0x38`
position, the extension `+0xA4` word ORed with `0x60000`, owner `-1`, the
derived direction, and two zero tail arguments. `extension + 0xA4` is the same
physical actor word as the opening `actor + 0x1B4` gate; the post-helper reload
is intentional and tested.

The callback has no direct `jal` caller. Its sole aligned literal pointer is
the second entry of `D_8008FBD0` at ROM `0x234694`, between `func_151C2F48`
and `func_150E411C`.

## Direct compiler and image closure

The retail `-O2 -g3` profile emits the complete **67 words/frame56** directly
from the semantic body. The natural candidate differs from the linked retail
bytes only in the four relocation immediates:

- `+0x20`: `R_MIPS_26:func_150484A0`
- `+0x44/+0x48`: `R_MIPS_HI16/LO16:D_800A1050`
- `+0xF4`: `R_MIPS_26:func_1505D1C4`

There are zero word guards, insertions, omissions, assembly blocks or profile
changes. The duplicate `mfc1` at `+0xCC` follows an unconditional branch and
has no reachable control-flow edge; the other 66 words are reached by the
guest corpus.

All 12 other functions in `generated_1104D0`, normalized owner pools, all
6,051 function addresses and the complete allocated image outside this
function remain fixed. Adding the previously unused owner reference to
`D_800A1050` changes one deterministic GNU-ld hash collision: `D_800A1050`
and `D_800A92A0` exchange adjacent `.symtab` and `.strtab` positions. The
qualifier predicts that complete closed cycle; strict full-ELF comparison uses
zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural relocation-normalized 67-word payload | `1a451ac2de909a57d9b65adf6f1fc2db813355f868b2c22d25711e62bcc72923` |
| Retail linked 67-word payload | `0878674bf8d4503184855b6069b8b0be89528b3dcf89988135db3be44d6a9a73` |
| Qualified/production owner | `f501e5f1dc018c54c2ad605b3b36b910ab84820bf334cf4a4fc6bf7152a012ba` |
| Predecessor linked ELF | `63b5a0307061c35391c6c43920c3aa57eb395868b27775c44f1d2a63efef4a2b` |
| Qualified/production linked ELF | `041585296b54ae734496f333432259d1f9841251d94f070ef805f3965b9a3846` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Unchanged production guard table | `cf2019b55b64b2c6a5f6408a41bbcd195cb431b13276d895e893fc84cd2668e1` |

The natural payload hash masks relocation immediates, while the retail body
hash is taken from the linked ROM, so those hashes are intentionally unequal.

## Semantic and production qualification

The big-endian guest oracle executes **384 cases** across the disabled/enabled
gate, eight angle classes, helper mutation on/off, two stack phases, three
incoming FCSR states and two field patterns. It checks the angle-helper inputs,
live post-helper actor reloads, all eight packet arguments, signed and unsigned
conversion routes, invalid/negative handling, caller-clobbered lifetimes and
FCSR restoration. All 66 reachable words are covered; only the compiler's
unreachable duplicate `mfc1` remains unexecuted.

Native 32-bit O0/O2/O3 profiles pass **12,288** bounded defined-domain cases
under UBSan. Eight compiled negative controls independently reject the wrong
enable field, position field, flags, owner, mask, angle bias, forced odd bit
and tail argument. The permanent four-test suite also verifies the exact raw
payload and bindings, callback registry, 12 owner neighbors, two-symbol cycle,
literal whole-image prediction, protected data, and installed
source/object/image coherence. Together with the 19 shared progress, PC16,
padder and protected-layout tests, all **23 tests pass**; the focused installed
suite took 75.365 seconds and the shared suite 33.695 seconds.

The protected Game-data audit remains exact at 189,088 bytes across 720
owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The actual `make all -j4` rebuilt both the generated owner and the dependent
guarded `game_EF410` owner, linked `conker.us.elf`, and produced
`conker.us.bin`; it stopped only at the expected whole-ROM SHA mismatch because
the overall decomp is incomplete. A fresh independent recount credits exactly
this function.

The candidate qualifier and permanent tests were committed first in the tools
submodule as `9f6fbbc`. Retained stage:
`conker/build/game-actor-direction-submission-150E4010-match/`.

This is instruction-level and bounded semantic proof, not natural whole-game
or gameplay acceptance. The README changes only its aggregate byte-exact rows.
No Claude call was needed.

## Graph retention

The required Graphify update extracted 24,234 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim. Graphify
also reported the known local 0.9.20-skill/0.9.26-package warning and one
zero-node `devcontainer.json` source.

## Continuation

Continue the ordinary Game queue at `func_15107924` (63 words, 59 current real
differences). Keep `func_150A76F0`, `func_151F8870`, `func_150A613C`,
`func_150AE280`, `func_15115F68` and `func_151AE2BC` outside an ordinary
direct-C screen until their existing boundaries are resolved. Every candidate
still requires source, ABI/caller, owner, guest/native, actual Make,
complete-image, protected-data, production recount and documentation gates
before credit.
