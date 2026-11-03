# 2025 - Dual effect-band emitter matched as guarded C

Verified 2026-11-02. Production is **4,095/5,511 (74.31%)**; Game is
**3,422/4,838 (70.73%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,416 functions remain different. The active 80% target is
**4,409/5,511**, requiring **314 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_150C2424` replaces its zero-return placeholder in
`conker/src/game_EF410.c`. It is the dual randomized effect-band emitter at
`0x150C2424`, ROM `0xEF8D4..0xEF9CC`, owned by `game_EF410`. Its recovered
interface is:

```c
void func_150C2424(u8 channel);
```

The routine samples `func_150ADA68` twice and submits two complete twelve-
argument packets to `func_1514C470`. The first packet uses the shared
`D_800A0268` coordinate, constants -490, -328 and 328, a randomized
`sample * 8 + 8` value and mode one. The second uses `D_800A026C`, constants
-560, -580 and 8117, a randomized `sample * 3 + 4` value and mode three. Both
forward the caller's narrowed channel after the preceding callbacks.

The sole retail caller is event `0x2E` in the large dispatcher at ROM
`0x56A9C`. Its `andi a0,s0,0xFF` delay slot remains unchanged, as do the
preceding `func_150C2290` call and its own narrowed argument. There are no
aligned literal pointers equal to this function's entry.

## Guarded compiler and image closure

Retail-profile IDO naturally emits the complete **62 words/frame56** with all
eight original relocations. Only four first-packet scheduling words differ:
the compiler materializes -490 before loading `D_800A0268`, while retail loads
the global first. Four checked rows rotate those independent words and move
the HI16/LO16 relocation pair symbolically from natural `+0x28/+0x2C` to
retail `+0x1C/+0x20`. There are no insertions, omissions, assembly blocks or
compiler-profile changes. The two random calls, two packet submissions and
second-global relocation pair remain naturally fixed.

All 17 other functions in `game_EF410`, normalized owner pools, all 6,051
function addresses and the complete allocated image outside this function
remain fixed. Adding the previously unused `D_800A026C` reference also causes
one deterministic GNU-ld hash collision: `D_800A026C` and `D_80096A6C` swap
adjacent `.symtab` and `.strtab` positions. The qualifier predicts that closed
ten-byte metadata cycle exactly; strict full-ELF prediction uses zero
exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural 62-word object payload | `dfd09087fa42d34720069460ea30cdfee5e2ec4f65f7c58db07f4fead4f751dc` |
| Retail linked 62-word payload | `a14cc47b15a7b2dd207f0d7c6b4b5df4bf90c12357475dbff7d8a0c091ee9ae9` |
| Qualified/production owner | `d164f895c4ceca4381431147dbecce201045387235795f836f13992389c967d5` |
| Predecessor linked ELF | `4f1a7767805854fe649a52f78c8b6ae4788586cb2f48ed4ec2410ff85651f2af` |
| Qualified/production linked ELF | `63b5a0307061c35391c6c43920c3aa57eb395868b27775c44f1d2a63efef4a2b` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `cf2019b55b64b2c6a5f6408a41bbcd195cb431b13276d895e893fc84cd2668e1` |

The natural object hash masks relocation immediates, while the retail body
hash is taken from the linked ROM, so those hashes are intentionally not
equal.

## Semantic and production qualification

The raw big-endian guest oracle executes **320 cases** across five incoming
channel words, four samples per band, two independent global-coordinate pairs
and both stack phases. It checks both random calls, all 24 submitted packet
words, binary32 multiply/add rounding, channel narrowing and channel lifetime
after the first packet helper clobbers caller-saved integer and floating
registers. Every retail body word is reached.

Native 32-bit O0/O2/O3 profiles pass 384 bounded packet submissions. Ten
effective controls cover both global origins, packet coordinates, random
scales/biases, modes, second-band ordering and channel forwarding. The
permanent four-test suite additionally verifies all four stale-guard
mutations, the sole caller, all 17 owner neighbors, the complete symbol/string
cycle, literal full-image prediction, protected data and installed
source/object/image coherence. Together with the 19 shared progress, PC16,
padder and protected-layout tests, all **23 tests pass in 110.631 seconds**.

The protected Game-data audit remains exact at 189,088 bytes across 720
owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The actual `make all -j4` rebuilt the complete guard-table dependency set,
linked `conker.us.elf` and produced `conker.us.bin`; it stopped only at the
expected whole-ROM SHA mismatch because the overall decomp is incomplete. A
fresh independent recount credits exactly this function.

The candidate qualifier and permanent tests were committed first in the tools
submodule as `4882d30`. Retained stage:
`conker/build/game-dual-effect-band-emitter-150C2424-guard-match/`.

This is instruction-level and bounded semantic proof, not natural whole-game
or gameplay acceptance. The README changes only its aggregate byte-exact
rows. No Claude call was needed.

## Graph retention

The required Graphify update extracted 24,234 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

Continue from a fresh ordinary Game ranking after this banked match. Keep
`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68` and `func_151AE2BC` outside an ordinary direct-C screen until
their existing boundaries are resolved. Every candidate still requires
source, ABI/caller, owner, guest/native, actual Make, complete-image,
protected-data, production recount and documentation gates before credit.
