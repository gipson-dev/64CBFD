# Game attached-direction constructor direct match

Date: 2026-11-14. `func_151A8624` replaces its zero-return placeholder in
`conker/src/game/generated_1D4E00.c`. Normal O2/g3 emits all 117 retail
words directly, with the original 0xA0-byte frame and no diagnostics.
The complete slot is `0x151A8624..0x151A87F8` (ROM
`0x1D5AD4..0x1D5CA8`). There are no new guards, inserted/omitted words,
compiler-profile changes or guard-manifest edits.

The constructor builds an 80-byte direction descriptor and a 40-byte
attachment cache. Typed vector members make their structure assignments
valid without casting float arrays to unrelated structure types. An
alignment-one four-byte structure preserves the packed input copy and
its original LWL/LWR and SWL/SWR instructions. Declaration ordering places
the cache at SP+0x24, descriptor at SP+0x4C and retained result at SP+0x9C.
The separate lifetime-flags value recovers the common store and register
roles; its unused home occupies the original low-frame gap.

The complete recovered interface has 15 arguments:

```c
s32 func_151A8624(u8 *owner, struct17 *position, u8 matrixIndex, s16 lifetime,
    f32 minimum, f32 range, DirectionPackedWord151A8624 *packed, f32 scale,
    struct17 *offset, u8 kind, u8 attachmentMode, s8 secondCallback,
    s32 extraBytes, u8 channel, s32 context);
```

A NULL owner returns zero. Otherwise the cache snapshots its owner,
identity byte, local position, matrix index, optional offset vector and
attachment byte, and clears its latch flags. A NULL offset supplies three
positive zero words. The descriptor uses nine vertices, the supplied
interval values, packed word, scale and second callback, the existing
global amplitude, zeroed vectors/length, reciprocal one and kind two.
Lifetime -1 selects a stored value of 300 with countdown disabled; other
lifetimes keep their signed halfword value with countdown enabled. Both
retail kind-selection paths choose first callback one; their original
clamp and branch shape remain intact.

The record factory receives the descriptor, `extraBytes + 40`, channel and
context. The addition uses unsigned wrapping before the signed ABI cast.
Allocation failure returns zero. Success loads the returned record's cache
pointer, copies all 40 snapshotted bytes there and returns the record,
retaining it across the copy helper's clobbered return value.

No aligned direct JAL or literal pointer to this constructor occurs in the
prepared US image, and source/assembly searches find no direct caller.
That inventory does not rule out computed or external use. No original
caller window is claimed. The complete callee's incoming argument reads,
width/sign conversions and the typed native harness qualify the interface.

Guest validation passes 1,033 independent-model cases against retail,
raw C and padded streams, exercising all 117 instructions. Cases cover
NULL ownership and allocation failure, lifetime boundaries, poisoned upper
argument bits, unsigned and signed byte arguments, kind normalization,
optional offsets, packed-word alignments, wrapping payload-size forwarding,
and helper-visible input/global/cache-pointer mutations. Sixteen additional
guest-only alias cases place inputs in the constructor's local cache or
descriptor, or place the owner in caller stack storage. Packet observations
check all descriptor/cache bytes, including original stack padding, under
the tested seed patterns and stack phases.

Sixteen coupled cases execute the actual 80-word `func_151A7950` factory
and original 11-word memcpy and 39-word bzero bodies. The factory's current
production words are independently checked against ROM before reuse.
The outer allocator remains modeled; these cases do not qualify general
heap behavior or every path through the SDK helpers. Four independent
big-endian merge probes check the unaligned load/store model at every
byte alignment. Retail/raw machine states agree at 185 fired modeled
memory-access prefixes. These checks do not establish hardware bus-fault
behavior or unrestricted portable-C stack aliases.

Native 32-bit C passes 521 cases in each of six O0/O2/O3 and
strict/no-strict-aliasing profiles with trapping UBSan, SSE floating point,
disabled contraction and standard excess precision. All seven defined
source controls are detected: wrong default lifetime, vertex count,
matrix index, identity byte, lifetime flags, payload size and cache-copy
length. Fixtures use typed, aligned, disjoint objects and an alignment-one
packed structure. Numeric fields/pointers and unchanged byte regions are
checked separately for native endianness. Native checks compare initialized
members rather than indeterminate structure padding. Nonfinite/FCSR,
unrestricted aliases, hardware and gameplay remain outside this scope.

Both padders pass 12 GNU links across four independent code/data layouts,
including the amplitude's HI16/LO16 binding and carry boundary. All 22
owner neighbors and normalized pools remain unchanged. Production uses
the existing compiler, padding and link rules with 697 frozen neighbors:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The production ELF equals the independent shadow prediction. The strict
whole-image audit accounts for all 338 changed bytes with zero exclusions
and no metadata groups. All 6,051 function addresses and 189,088 protected
Game-data bytes remain fixed. Only the target owner changes among 698
objects. All 787 immutable input fingerprints pass, including 82 headers,
the compiler, retail assembly/input, conversion rows and the unchanged
guard manifest. Prior unchanged neighbor receipts remain prior evidence.

Tools commit `a0c2aa0` retains the installed suite. It passes in the mounted
checkout and isolated sibling-tools overlay; `make tools-check` also passes:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_attached_direction_constructor_151a8624_installed -v
```

The sibling retains its 2,439 dirty paths at `ddbdd16`, with identical
before/after status digests. The scoped fail-closed Graphify refresh retains
all 60,147 prior node IDs and produces 60,148 nodes / 113,362 links. It is
not a full-corpus re-extraction. No host files or Release artifacts were
changed. The prior `64CBFDOGL` path contains diagnostic/capture directories,
so no host source/build/runtime comparison was attempted.

Fresh production recount: total **4,476 / 5,516 (81.15%)**, Game
**3,803 / 4,843 (78.53%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift and 1,040 still different. **213** further exact total
functions are needed for 85% at this denominator. The goal remains active.
Next screen: `func_151A9834`. Root README contains aggregate figures only.
