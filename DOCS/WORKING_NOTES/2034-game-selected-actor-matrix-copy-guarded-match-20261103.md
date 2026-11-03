# 2034 - Selected actor matrix copy matched as guarded C

Verified 2026-11-03. Production is **4,104/5,511 (74.47%)**; Game is
**3,431/4,838 (70.92%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,407 functions remain different. The active 80% target is
**4,409/5,511**, requiring **305 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_15133A94` replaces its zero-return placeholder in
`conker/src/game/generated_15F680.c`. It is the selected attached-actor matrix
copy at VA `0x15133A94`, ROM `0x160F44`, owned by `generated_15F680`. Its
recovered interface is `s32 func_15133A94(Mtx *output, u8 *actor)` and its
complete slot is 65 words on a 104-byte stack frame.

The routine resolves the attached actor at `actor + 0x7C` and returns `-1`
when that pointer is null, its leading word is zero, its type byte at `+0x04`
is `0xFF`, or its identity byte at `+0x3B` differs from `actor[0x80]`. It then
resolves the matrix array at attached offset `0x1D4`; a null array or low
nibble `0xF` in attached byte `0x74` returns zero. The matrix selector is the
unsigned byte at actor offset `0x170`, with a 64-byte stride.

When `D_800C3E90` is nonzero, the selected 64-byte matrix is copied directly to
the output. Otherwise it is copied to a 72-byte local workspace, elements
`[0][3]`, `[1][3]` and `[2][3]` are normalized to `0.0f`, `[3][3]` is
normalized to `1.0f`, and `guMtxF2L` converts it to the fixed-point output.
Both successful routes return one.

There is no direct JAL to this callback. Its aligned pointer literal is at ROM
`0x22E460`, the sixth entry in the table rooted at `D_8008998C`.
`func_15132A88` invokes that table entry with output
`actor + D_800BE9C0 * 0x40 + 0x90` and the actor as its second argument.

## Compiler and image closure

The readable body naturally emits the complete frame, saved-register lifetime,
branches, delay slots and both copy/conversion routes. Only two independent
commutative integer-add operand orders differ from retail: offsets `0x0A4` and
`0x0C4`. Two checked expected-word rows normalize those compiler scheduling
choices from `0x006C2821` to `0x01832821` and from `0x006E2821` to
`0x01C32821`. There are no inserted or omitted words.

All five original relocations remain attached to their semantic operations:
HI16/LO16 for `D_800C3E90`, two J26 calls to `memcpy`, and one J26 call to
`guMtxF2L`. All thirty other owner functions and normalized pools remain
unchanged. Across the linked image, only `func_15133A94` changes, all 6,051
function addresses remain fixed, and strict comparison uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural relocation-masked 65-word payload | `da71c46b7c04743709d267e69ec7fe2aca6be435b6b0f479aea583f779c52591` |
| Retail linked 65-word payload | `7ddf1b2d34b59f5cf64b141c6f79c55aaa68da8a717ac423c9ce5ceaad1f0e87` |
| Qualified/production owner | `b365fc0596803fbdfc734950d492a37890f04996403ee050ac9a5789ae7f2f5c` |
| Predecessor linked ELF | `b51f10a96c977eaad1da4dab466420ece3e4bf3339f377a18d8c5a425cdf16f1` |
| Qualified/production linked ELF | `4c8c817a25b56fe734a8cfaec6bfdd74509dfed2658e7c9dac5352410d2e8512` |

## Semantic and production qualification

The big-endian guest oracle covers all 256 selector bytes, both copy modes,
both stack phases, every rejection gate, helper clobbers and source mutation.
More than 1,024 executions cover all 62 reachable retail words. The three
remaining slot words are compiler-emitted duplicates behind branch-likely
shadows at offsets `0x50`, `0x64` and `0xB0`; they are checked statically and
are not executable. Native 32-bit O0/O2/O3 builds exercise the actual C and six
effective controls reject altered gates, selector stride, matrix normalization,
copy route and return behavior.

The six focused permanent tests pass against the installed production source,
object and ELF. Seventeen shared progress, owner-pool and protected-layout tests
and eleven generated/guarded padder tests also pass. Stale expected words and a
wrong-source control fail closed. Protected Game data remains exact at 189,088
bytes across 720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The actual `make all -j4` rebuilt the full production corpus, linked the ELF and
generated the binary. It stopped only at the expected whole-ROM SHA mismatch
while the decomp remains incomplete. The installed qualifier then confirmed
the predicted owner and ELF byte for byte, fixed addresses for all 6,051
functions, zero strict exclusions, and exactly one changed body. A direct
production recount credits exactly this function.

The qualifier and permanent tests were committed first in the tools submodule
as `e6c28bf`. This is instruction-level and bounded semantic proof, not natural
whole-game or gameplay acceptance. The README changes only its aggregate
byte-exact rows. No Claude call was needed.

## Graph retention

The required bounded Graphify update extracted 24,298 nodes versus the retained
58,384. It failed closed without `force=True`, preserving 31,816 nodes from
3,754 still-existing files outside the reduced scan corpus. The retained graph
SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

The fresh ordinary Game ranking keeps the same seven documented boundary cases
outside the direct-C queue: `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. The next ordinary candidate is `func_15134070` (63 words,
60 current real differences), followed by the other 60-difference ties. Every
candidate still requires source, ABI/caller, owner, guest/native, actual Make,
complete-image, protected-data, production recount and documentation gates
before credit.
