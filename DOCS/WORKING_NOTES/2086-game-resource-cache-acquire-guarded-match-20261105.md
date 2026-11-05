# Working Note 2086: Game resource-cache acquire guarded match

Date: 2026-11-05

## Recovered resource-cache contract

`func_1518C900` occupies `0x1518C900..0x1518CA04`, ROM
`0x1B9DB0..0x1B9EB4`, in `generated_1B9DB0.c`: **65 words / 260 bytes**.
The zero-return placeholder is replaced by `s32 func_1518C900(s32 kind)`.
The three indexed tables are byte reference counts at `D_800DF7D0`, retained
texture-list pointers at `D_800DF9B8`, and resource-header pointers at
`D_800E0148`.

A zero reference count invokes `func_1502B6BC(NULL, 0, NULL, 2, 9, kind)`.
Allocation failure returns zero immediately, preserving any provider mutations
without incrementing the count or publishing a cache entry. Success passes
the header's first word to `func_1510CE60` with `(0, 1, 0x3E)` and the selected
texture-list output cell. It reloads that first word for `func_15168E54`,
passes the header as the second argument, and only then publishes the header
in the resource cache. The texture helper's return does not determine success.

A nonzero count reuses the cached header. Both successful routes reload the
live byte count and increment it unless it is already 255, then return the
header's live first word. Provider mutations to counts, header data, output
cells, and cache entries must retain this order; early publication and cached
data/count snapshots are observably different.

The aligned retail reference census finds exactly six direct JALs and no
function-pointer literals:

| JAL address | Argument form in the original call window |
| --- | --- |
| `0x1509013C` | Immediate kind `0xB8` in the delay slot |
| `0x15093880` | Immediate kind `0xBA` in the delay slot |
| `0x151557E0` | Immediate kind `0xA6` in the delay slot; return discarded |
| `0x15170CF8` | Kind from S0 in the delay slot |
| `0x15171098` | Unsigned halfword kind from the record in the delay slot |
| `0x15171384` | Kind already in A0; float store in the delay slot |

The discarded-return caller in `generated_182C30.c` had a false `void`
prototype. Its declaration is corrected to `s32`. Independent before/after
compiles preserve all **nine functions**, relocations and normalized pools;
both complete padded objects equal the production object byte for byte,
SHA-256 `856f27e9cc343d03fb1fda9123cc960b8acf2e791a3c8f082853292b6e1c48fa`.

## Natural C and private spill normalization

The normal `-O2 -g3` body has all **65 words**, the original **64-byte frame**,
saved-register lifetime, control flow, and eleven relocations. **59 words**
emit directly. Six fail-closed, non-relocating rows move two private spill
homes upward by four bytes within the same frame:

| Offset | Natural | Retail |
| --- | --- | --- |
| `+0x054` | `AFA80034` | `AFA80038` |
| `+0x058` | `8FA80034` | `8FA80038` |
| `+0x08C` | `AFB90028` | `AFB9002C` |
| `+0x090` | `AFA80034` | `AFA80038` |
| `+0x0B0` | `8FAB0028` | `8FAB002C` |
| `+0x0B4` | `8FA80034` | `8FA80038` |

These preserve each opcode, source/destination register and SP base. The
count pointer moves `SP+0x34 -> SP+0x38`; the scaled table index moves
`SP+0x28 -> SP+0x2C`. No instructions, relocations or profiles are added or
removed, and the incoming kind home remains `SP+0x40`.

Swapping local declaration order leaves the same six differences. An explicit
count temporary changes the body to 63 words; a named result local keeps 65
words but allocates a 72-byte frame; a late byte-count local emits 64 words.
Those variants remain private controls, not adopted source.

The natural target hash is
`1b1a539482abf273805508bba68d5ca94be9bd18c3e23cdc03be24296c81d1f6`.
The normalized target equals retail, hash
`7fc963b128273618962ba087ac5acb5ae9181126b3b34aedf08c44d9385ed053`.

## Qualification evidence

The pre-install suite passes all five tests in **38.013 seconds**. The installed
suite, including the explicit kind-484 alias case, passes in **35.977 seconds**.
Its main
guest corpus executes **4,080 cases per body**, covers every word, and includes
all 256 byte counts, allocation success/failure, seven public provider plans,
and both stack phases. Native32 O0/O2/O3 pass 12,288 executions, and sixteen
compiled semantic controls are rejected. Six corrupted guard preimages and
inside/outside-target ELF corruption are rejected.

Another **59 cases per body** cover the sparse/layout edge and private roles.
Five guest-only private plans qualify the existing incoming kind home and
the two spill roles, including provider changes to the saved pointer/index.
Sparse signed word indices are guest ABI probes. Kind `0x1E4` has a specific
layout edge: `D_800DF9B8[484]` aliases `D_800E0148[0]`. Guest tests explicitly
check that output write and the separate publication at cache index 484.
Native fixtures use ordinary table indices through 483; they do not claim
portable C behavior for the linked layout edge or out-of-range indices.

The caller suite executes **288 original two-word JAL/delay-slot windows**
across all six call sites. **210 fault observations / 34 unique active
boundaries** qualify emitted accesses. These are bounded caller and provider
tests, not qualification of complete callers, the three provider bodies,
hardware execution, or gameplay. Guest private/fault probes are not portable
C fault semantics. Routine work uses zero Claude calls.

Shared match-progress, PC16, guarded-object and protected-data checks pass
**19 tests in 5.699 seconds**; `make tools-check` passes. The standalone tools
checkout's pre-existing dirty work is preserved; fresh receipts use mounted
tools.

## Independent image prediction

The qualified owner preserves its one neighbor and normalized pools. Across
**6,052 linked functions**, only the target body changes, with all addresses
fixed. Replacing its instruction span and updating the named symbol extent
from 12 to 260 bytes predicts the entire ELF: **197 changed bytes**, with
**zero exclusions**. All **189,088 protected Game-data bytes / 720 owners**
remain exact, hash
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Frozen predecessor ELF | `b3eecf1336289ea865dfd089d311aa3730cecb90a44e50721ac74a4a3d28cfc4` |
| Qualified / production owner | `7abaf7b23f94de7b3d8ff2c6a8fbf006235af2276b041f3810bac20fb750cdd5` |
| Qualified / production ELF | `29005e48a1f51044750259749b5f066abcc3f85ba0c05cd3d58147a281df94de` |
| Production code image | `c5001fd3ea837eba370f4f4d8831921d6b00ab06c537aa9ff14767e959e2a913` |
| Production map, unchanged | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Guard registry after six rows | `ec315f15b1521a131671d9cd6e030ae69a252da2a0cf6d6f51c3feada04d9116` |

The six new registry rows trigger a full four-job production rebuild. All
applied preimages pass and linking succeeds. The actual target object and
ELF equal the independently qualified files; the corrected caller object
retains its exact frozen bytes. `make all` creates the binary and stops only
at the expected retail SHA-1 mismatch. The inherited duplicate
`generated_12D630` recipe and unrelated owner declaration/SDK warnings remain;
neither changed owner introduces a diagnostic difference.

The guard registry retains its exact frozen byte prefix plus the six derived
rows. Conversion CSV and Makefile remain byte-identical to their predecessors.

## Authoritative recount and continuation

| Section | Exact C functions | Address drift | Different |
| --- | ---: | ---: | ---: |
| Total | **4,157 / 5,512 (75.42%)** | 0 | 1,355 |
| Init | **492 / 492 (100.00%)** | 0 | 0 |
| Game | **3,484 / 4,839 (72.00%)** | 0 | 1,355 |
| Debugger | **181 / 181 (100.00%)** | 0 | 0 |

Converted inventory remains 5,512 / 6,046. The active 80% target requires
4,410 exact functions, **253 more**. Continue at ordinary candidate
`func_1518EF54`; preserve the seven previously documented compiler/custom-ABI
boundaries. This checkpoint advances the active goal and does not complete it.

Reproduce under prepared WSL from the consumer root:

```sh
python3 -m tools.experiments.game_resource_cache_acquire_match
python3 -m unittest tools.tests.test_game_resource_cache_acquire_match -v
make -C conker -j4 build/conker.us.elf
make -C conker all
```

## Graph retention

The frozen graph has **58,605 nodes / 112,373 links / 5,082 communities**,
SHA-256 `d2350bca8ecd995abb39fdba03735d371eacae2e188dacda900fa8137859b47b`.
The standard reduced update extracts nine uncached paths but proposes only
24,811 nodes and correctly refuses to overwrite the retained graph. Its
corpus warning retains 31,816 nodes from 3,754 still-present files outside
the reduced scan. An explicit nine-path refresh with `force=False` produces
**58,613 nodes / 112,376 links / 5,119 communities**, retaining **58,602 /
58,605** prior IDs with **zero removals outside changed paths**. Three
line-derived Update Log IDs relocate; eleven IDs are added, including eight
Note 2086 nodes.

Qualified graph SHA-256:
`a724cc8ed4f9a06ff49ba68b6cd484164659a77d76b4a85e0c609571e4152f43`.
This is a scoped AST refresh with zero semantic LLM calls, not a fresh
full-corpus extraction. A final one-path note refresh checks stabilization.
