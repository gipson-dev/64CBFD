# Working Note 2083: Game linked matrix point update guarded match

Date: 2026-11-04

## Recovery and callback contract

`func_15107E48` occupies `0x15107E48..0x15107F54`, ROM
`0x1352F8..0x135404`, in `generated_133190.c`: **67 words / 268 bytes**.
The zero-return placeholder is replaced with this semantic interface:

```c
s32 func_15107E48(u8 *owner, u8 *changed);
```

The callback resolves the link at `owner+0x60` and its actor pointer. It returns
false without modifying the changed byte when the actor is inactive, the
identity bytes at `link+4` and `actor+0x3B` differ, or the actor's matrix pointer
at `+0x1D4` is zero. A valid callback clears the byte, snapshots the owner's
three-float point at `+0x14`, and calls `func_15107F54` with the actor, unsigned
matrix index at `link+0x14`, input point at `link+8`, and owner point output.

If any coordinate differs after that helper, including unordered NaN
comparisons, it sets the changed byte and calls `func_15107AE0` to rebuild
fractional points at `owner+0x20/+0x2C` toward `owner+0x38`. Valid callbacks
return one whether or not the point moved. The index and matrix remain live
after clearing the changed byte; aliased writes must not be replaced with
pre-clear cached values.

The sole aligned retail pointer is ROM `0x22D6D4`, slot **D_80088C10[1]**.
There are no direct JAL references. The original `func_1510608C` dispatcher
loads this table using the owner's signed selector, invokes it at
`0x151060C8`, passes owner/A0 and its local changed byte/A1, then consumes the
callback return. Ten connected cases execute the actual caller window through
that JALR and return, preserving its stack and saved owner register.

## Natural C and checked frame normalization

Natural `-O2 -g3` C has the correct **67-word** extent and both original call
relocations. It allocates a 64-byte frame instead of retail's 56-byte frame.
Nine fail-closed rows normalize only that eight-byte frame difference and
the associated incoming changed-pointer and vector snapshot homes:

| Offset | Natural | Retail |
| --- | --- | --- |
| `+0x000` | `27BDFFC0` | `27BDFFC8` |
| `+0x014` | `AFA50044` | `AFA5003C` |
| `+0x048` | `8FA80044` | `8FA8003C` |
| `+0x068` | `27A9002C` | `27A90024` |
| `+0x094` | `C7A4002C` | `C7A40024` |
| `+0x09C` | `C7A80030` | `C7A80028` |
| `+0x0A8` | `8FAD0044` | `8FAD003C` |
| `+0x0C0` | `C7B00034` | `C7B0002C` |
| `+0x108` | `27BD0040` | `27BD0038` |

The other 58 words emit naturally. There are no insertions, omissions,
relocation changes or profile edits. The two bindings remain
`R_MIPS_26:func_15107F54` at `+0x8C` and
`R_MIPS_26:func_15107AE0` at `+0xEC`. The owner retains its existing
`RETAIL_RODATA_SYMBOL := D_800A2420` binding.

The natural target hash is
`de00ee337d85f828445303335f3f5e5ded1d1ce6319368537e9994f27ef63458`;
the qualified target equals retail with hash
`ef64e458318375bb187a475212933fb615d2177827550c56a14a5f23d7d49143`.

## Behavioral evidence

The focused suite executes **363 cases per body** with the original wrapper,
98-word point transformer, fixed-matrix converter, matrix/vector transform,
translation helper and fractional-point helper connected. An independent
binary32 reference checks both natural C and retail across inactive, stale,
missing-matrix, unchanged and changed routes, all three changed axes, unsigned
indices 0/128/255, floating/fixed matrices, zero input points, two stack phases,
identity boundaries and quiet NaNs. It reaches **65/67** callback words.
Duplicate shadow words at `+0x44` and `+0x60` are structurally unreachable;
both remain statically exact and are not claimed as covered.

Another **48 alias cases per body** check a separate changed byte, matrix-index
byte, first owner-point byte and matrix-base low byte. They retain the original
post-clear index/matrix reloads. **190 fault observations across 44 unique
active boundaries** qualify emitted accesses. These are guest instruction
tests, not portable C fault semantics or hardware/FCSR acceptance.

Native32 O0/O2/O3 pass **12,288 executions**, and **14 compiled semantic
controls** are rejected. They cover wrong link/identity/matrix gates, signed
or incorrect matrix index, incorrect input/output fields, missing changed-byte
clear, incorrect return routes and incorrect fractional destinations.

Two initial fixture issues were corrected: helper arguments must be captured
before a later aliased changed-byte store, and the caller-window code map must
contain its stop sentinel before the jump membership check. The C body was
unchanged. Pre-install components pass after those corrections. All **five
installed tests pass in 41.491 seconds**. Routine work used zero Claude calls.
Shared match-progress, PC16, guarded-object and
protected-data tests pass **19 tests in 15.445 seconds**; `make tools-check`
passes.

## Whole-image and production audit

The independently qualified owner preserves **36 neighbors** and normalized
pools. The full **6,052-function** image has only the target body changed and
every function address fixed. An exact **187-byte ELF delta** is reconstructed
from the target instruction span and its named symbol extent (12 -> 268), with
zero metadata exclusions or symbol-order allowances. The predecessor ELF is
pinned to the accepted Note 2082 checkpoint, so unrelated rebuild deltas fail.

All **189,088 protected Game-data bytes / 720 owners** remain exact, hash
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner | `b2ac99758cadc7adde6161f7dcb8754a5d393bce907700cf5003a85351329042` |
| Frozen predecessor ELF | `1bf15eaf5cd81203aac76f30c50e7bd0819b1c99c1e279807502036e280ca388` |
| Qualified / production ELF | `92b4ed1166612a791154a72a680449cbeafae6eb8ef320422f338c9e546e57db` |
| Production code image | `6293c9307dabe8c182a2b046334657e1a0d5e2f34d7aa81884583888bdbb4b76` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |

The fresh production owner and ELF equal the independently qualified files.
Changing the shared guard registry caused a full four-job production rebuild;
all existing preimages pass and linking succeeds. `make all` generates the
binary and stops only at the expected retail SHA-1 mismatch. The inherited
duplicate `generated_12D630` recipe warning and two unrelated owner declaration
warnings remain. No new target diagnostic is introduced. The guard CSV retains
the exact frozen byte prefix plus nine rows; the conversion CSV and Makefile
remain byte-identical to their frozen predecessors.

## Authoritative recount

| Section | Exact C functions | Address drift | Different |
| --- | ---: | ---: | ---: |
| Total | **4,154 / 5,512 (75.36%)** | 0 | 1,358 |
| Init | **492 / 492 (100.00%)** | 0 | 0 |
| Game | **3,481 / 4,839 (71.94%)** | 0 | 1,358 |
| Debugger | **181 / 181 (100.00%)** | 0 | 0 |

Converted inventory remains 5,512 / 6,046. The active 80% target is 4,410
exact functions, requiring **256 more**. This checkpoint advances that goal;
it does not complete it.

## Reproduction and continuation

Run under the prepared WSL toolchain from the consumer root:

```sh
python3 -m tools.experiments.game_linked_matrix_point_update_match
python3 -m unittest tools.tests.test_game_linked_matrix_point_update_match -v
make -C conker -j4 build/conker.us.elf
make -C conker all
```

Continue at ordinary candidate `func_1515BFA8` after the installed checkpoint,
then rerank. The seven previously documented custom-ABI/compiler boundary
cases remain separate.

## Graph retention

The frozen graph has **58,580 nodes / 112,350 links / 5,118 communities**,
SHA-256 `6f178743025e435310352bfda4366c8783239beacf3531afcba5e5ddab90d6cf`.
The standard reduced `graphify update .` extracted eight uncached paths but
proposed only 24,787 nodes, so it correctly refused to replace the retained
graph. Its corpus warning retains 31,816 nodes from 3,754 still-present files
outside that reduced scan.

An explicit eight-path incremental rebuild with `force=False` produces
**58,589 nodes / 112,363 links / 5,188 communities**. It retains **58,577 /
58,580** prior IDs, with **zero removals outside changed paths**. Three
line-derived Update Log IDs relocate; twelve IDs are added for their new
forms and the nine Note 2083 nodes. This is an AST refresh with no semantic
LLM calls, not a new full-corpus extraction.

Qualified graph SHA-256:
`089130a69286337eae36eae43a62fb4f161642926a217c5cbdabe3b1e716b215`.
The final note's one-path stabilization detects no topology change and leaves
every qualified node and link untouched.
