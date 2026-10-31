# 1899 - Resource-pair payload: direct C match

Date: 2026-10-31. Function `func_151B5240` in
`conker/src/game/generated_1E26F0.c`. VA `0x151B5240..0x151B5328`,
ROM `0x1E26F0..0x1E27D8`: 58 words / 232 bytes, no alignment words.
Every word and all six relocation bindings emit directly from semantic C under
the existing O2/g3 profile. Zero guards, insertions, omissions, assembly
injection, compiler-profile changes or shared-header changes.

## Recovered behavior and layout

`void *func_151B5240(s16 effect, u8 variant, s32 flags)` resolves resource IDs
23 and 22 through `func_15083E90`, initializes the known fields of a 1,448-byte
local payload, and calls the constructor with
`(effect,-1,-1,1,1,21,1448,variant,flags)`. On success it copies the complete
payload to record+0x28 and returns the saved record pointer. Failure returns
NULL after both resource lookups. NULL resource results are retained in the
packet; they do not suppress allocation.

The 1,504-byte frame saves RA at SP+44. Payload starts at SP+48; the record
pointer spills at SP+1500 across memcpy. Incoming effect, variant and flags
homes are SP+1504, SP+1508, SP+1512. The halfword reload is at+1506 and byte
reload at+1511. There is no saved-S-register lifetime.

| Payload offset | Initialized field |
| --- | --- |
| 0x580 / 0x584 | First resource pointer / ID 23 |
| 0x588 / 0x58C | Second resource pointer / ID 22 |
| 0x590 | Float 18.0 |
| 0x594 | Float 0.0 |
| 0x598 | Float 250.0 |
| 0x59C | Runtime single-precision 1.0/250.0 |
| 0x5A0 | Captured `D_800AA418`, retail bits`0x3F666666` |

Thirty payload bytes are initialized. The opaque 0x580-byte prefix, six entry
padding bytes and final four bytes retain their original uninitialized state.
They are not zeroed. `u64 retained[0xB0]` expresses the opaque storage's N 64
8-byte alignment; no numeric interpretation of its contents is claimed.
This alignment recovers SP+48, while the rejected byte-array draft started
four bytes too high. The explicit first lookup literal 23 and zero-before-factor
assignment also recover retail materialization and floating register choices.

## Caller and provider interfaces

The complete aligned-ROM census finds one JAL at`0x5529C` and no aligned
literal function pointer.216 cases execute the complete original 14-word
command window at VA 0x15027DC4 plus its five-word parent epilogue. They cover
both the fixed 5000 and signed difference paths, narrowed variant, flags 0,
varied callee returns and stack phases. The window overwrites the result with 1.
The large parent itself is not claimed fully executed.

The actual resource lookup scans 26 records of stride 0x32C, ignoring inactive
records and selecting the first matching identity byte at+0x3B. Connected tests
cover all 26 positions, absent resources, inactive entries and active duplicates.

The original constructor treats its seventh incoming word as a size and adds
0x28, yielding an actual 1,488-byte heap request. Its original header stores,
allocator/list registration and 16-byte bzero are executed. The local prototype
models this observed o32 size-word contract. Historical untouched callee source
spells that word as a `struct37` pointer and forms an address-only+0x28 expression;
this work does not claim portability of that legacy source spelling. Its code
and shared headers remain unchanged. The guest path executes the original
instructions, rather than relying on that source spelling as an oracle.

## Fresh qualification

- Eight fresh focused methods plus project tools checks pass independently in
  both tools copies. After production, two installed methods rerun per copy;
  six unchanged methods are reused only through exact fingerprints.
- Guest: 1,984 cases /3,968 original/raw executions, all 58 root words visited and
  three independent GNU layouts. Original/raw/padded/actual-Make images are
  byte-identical. Seeded guest memory compares the complete 1,448-byte copy.
- Twenty-four additional guest alias cases include overlapping payload copies
  and overwrite of the saved result slot. The original pointer reload lifetime
  is preserved. An effective saved-RA overwrite control rejects the corrupted
  return in both streams. These are guest contracts, not portable C overlaps.
-100 fired access-prefix pairs include 10 branch-delay cuts. Resource mutations,
  global-factor capture before constructor mutation, allocation failure, narrow
  signed effect/variant arguments and saved state agree on complete modeled state.
-896 connected cases /1,792 executions retain 180 original helper words: lookup 72,
  constructor 49, allocator 28, registration 20, memcpy 11. Visited counts are
  respectively 66, 47, 28, 20, 11. Retained size is not equated to execution coverage.
  Header fields, zeroed state, list links, full seeded payload and output fences
  agree. Heap allocation and bzero remain bounded; no gameplay/hardware claim.
- Native SDK32 O0/O2/O3: 524,288 positive cases per profile with trapping UBSan,
  all 65,536 effect halfwords, all 256 variants, varied flags, allocation outcomes,
  resource results and provider mutations. Seventeen effective source controls
  compile and fail semantically. The native memcpy ABI probe observes/transfers
  the thirty initialized bytes only. It does not read or claim values for the
  uninitialized prefix/padding; the full original copy is checked in the guest.

No portable uninitialized-byte, guest overlap, FCSR or complete legacy-program
C-language portability claim is made. The reserved-keyword control-name compiler
failure is retained as a harness failure and never counted as an effective
control; both final canonical executions rerun every suite afresh.

## Owner, image and banking

The complete owner preserves both neighboring functions and normalized pools.
Its plain generated-source recipe uses three actual Make commands:compiler,
padder, assembler. The preceding slice's five-command assumption was rejected
without changing Make. Selected, owner and invoked-command diagnostics are empty.

The independent complete ELF prediction has zero exclusions and exactly 215
changed bytes: 202 root-code bytes, one root-extent byte and 12 metadata bytes.
The named symbol/string rows for`D_800AA418` and`D_800A3760` swap as a closed
serialization; all named values, bindings and sizes are retained apart from the
selected extent. All 6,055 other linked bodies, all addresses and 189,088 protected
Game bytes across 720 owners are unchanged. Guard and conversion CSVs are
byte-identical.

Tools commit `f5e137b15e9e515f7e5e60a2c662f6656d58d7c8` precedes the consumer commit. Production ELF SHA-256:
`f5e0295c5f8b0776043931231e065492bd3178795224a5815ccc64a633201b7a`.
Actual adopted-ELF recount: **3,976 / 5,506 (72.21%)**, Game
**3,303 / 4,833 (68.34%)**, Init 492/492 and Debugger 181/181. Zero drift;
1,530 C functions still differ. **154 more** are required for 4,130 exact (75%).
Next screen: `func_1509CCF4`.

Artifacts and immutable inputs remain under ignored
`conker/build/game-resource-pair-payload-151B5240-match/`. Root README changes
only two aggregate rows. Scoped graph refresh preserves prior nodes and valid
relationships and retires the obsolete placeholder return edge. No full-corpus
extraction, global clustering, hardware, gameplay acceptance or push is claimed.
