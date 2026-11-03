# 2016 - Owner identity event pair matched as guarded C

Verified 2026-11-02. Production **4,086/5,511 (74.14%)**; Game
**3,413/4,838 (70.55%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,425 different; two zero-return placeholders are replaced by qualified
semantic C and are newly byte-exact. The active 80% target is **4,409/5,511**,
requiring **323 more**. This is progress toward that goal, not completion.

## Recovery and interface

`func_15163FEC` and `func_15164134` are the paired 53-word, frame-`0x18`
owner-identity event handlers in `conker/src/game_18D770.c`. Their retail
addresses are `0x15163FEC` and `0x15164134`; their ROM offsets are `0x19149C`
and `0x1915E4`.

Both handlers narrow the third O32 argument to an unsigned byte and use the
identity state at owner offset `0x18`. Command zero compares the event's
32-bit key and byte tag to the current identity. Either match releases the
owner through `func_1516972C`. Command `0x2D` treats the event as two key/tag
pairs: matching the current first key installs the second pair, while matching
the current second key installs the first pair.

Every other command delegates through the owner's subtype callback. The first
routine indexes `D_8008B374` with owner byte `0x2D`; the second indexes
`D_8008B37C` with owner byte `0x3D`. A non-null callback receives the original
owner, event and narrowed command byte. The callback declarations are now
typed as three-argument void functions rather than the former one-argument
placeholder declaration.

The original parent dispatcher `func_151604A0` is an 88-word routine at
`0x151604A0`/ROM `0x18D950`. It narrows the command byte and forwards the
original owner and event through registry slots 16 and 17 in `D_8008B150`.
Those slots, at ROM `0x22FC50` and `0x22FC54`, are the only literal references
to the pair. There are no direct JALs to either child.

## Guarded compiler closure

IDO emits 52 words for each semantic body. Retail has 53 because its final
identity-replacement schedule contains one additional unconditional branch.
Seven checked rows per function close the independent branch-distance,
commutative equality-branch and store/return scheduling differences. The row
at target offset `0x094` replaces the candidate store and inserts the missing
branch; the row at `0x098` restores the delayed store as the retail saved-RA
reload follows it. No row changes a relocation because these routines contain
none.

The pair therefore uses 14 fail-closed rows and two insertions. Two independent
rebases reproduce every linked retail word. Mutating each expected guard word
produces 14 stale-row failures. Both functions match all 53 retail words while
retaining their original extents, frames, registry slots and neighboring owner
bytes.

| Artifact | SHA-256 |
| --- | --- |
| First raw candidate object | `1d5af4c41b78972d199cadfa590b70bae0ced15b1b6f5a5364104907795040ce` |
| Second raw candidate object | `f842e9254aa02a5345679dfb405b0560366101f6a52a39ea63af9c4892c331ca` |
| First isolated guarded object | `cec314e5db8050e41aadd83c0d3fee8ba988231dcb59bdc90512ff46de123bf7` |
| Second isolated guarded object | `2a51da8839df98f8226b2a7718c042b5d163d2ee2378b9590796f5cd3670f0a9` |
| Qualified/production owner | `63cc7f731e7afc843d2a83c34b8f7894c6d6fb43aeba9fad1479b270faf6eef2` |
| Qualified/production linked ELF | `eba8c0724344020251b40f67f7b48d9a4bb51d4999518ac66fca24ccb2919207` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `a9562abb9176e08fc7bfb6d3a21e24d37e3eb39a4cea342104c55cc85d3883e7` |

## Semantic, owner and image qualification

Five permanent tests pass in 56.340 seconds. A 5,208-case guest corpus runs
retail, raw and guarded programs for 15,624 executions across all 256 command
bytes, both callback tables, five alias layouts, both replacement directions,
null and non-null callbacks, callback clobbers, incoming-stack phases and
upper-bit narrowing. Another 336 executions validate two independent rebases.
The original parent and connected children run for 1,680 more executions,
proving the registry positions and forwarded three-argument ABI.

Native 32-bit O0/O2/O3 builds run 48,384 correct-handler cases and reject six
effective semantic controls in every profile. The owner comparison covers at
least 70 functions plus normalized pools. The qualified image has the same
function inventory, addresses and symbol inventory as production; after
installation it differs in no function. Static scanning confirms that the two
registry entries are the only references.

The actual `make all -j4` rebuilt the full generated, converted and libultra
corpus, linked `conker.us.elf` and produced `conker.us.bin`. It stopped only at
the expected retail-ROM checksum target because the overall decomp image is
not yet fully matching. The fresh independent recount credits exactly these
two functions. Protected Game data remains exactly 189,088 bytes across 720
owners with zero different bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The permanent experiment and tests were committed first in the tools
submodule as `a7a57ab`. The retained qualification stage is
`conker/build/game-owner-peer-event-pair-guard-match/`. This is
instruction-level and bounded semantic proof, not natural whole-game or
gameplay acceptance. The root README changes only its aggregate byte-exact
rows. No Claude call was needed.

## Graph retention and next step

The required Graphify update extracted 24,161 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep every
new candidate private until source, ABI/callers, owner, guest/native, actual
Make, complete image, protected-data, production recount and documentation
gates pass.
