# Owner single-packet callback guarded byte match - 2026-11-27

`func_1514E31C` replaces its zero-return placeholder with the complete
**123-word / 492-byte** callback in `conker/src/game/generated_179F30.c`.
VA `0x1514E31C..0x1514E508`; ROM `0x17B7CC..0x17B9B8`.
All seven relocation positions and the original **304-byte frame** match.
The raw C preserves every register role and packet offset. Thirty-two
expected-word guards reorder only independent initialization instructions.
No frame/register/FP/value rewrite, instruction insertion/omission, artificial
storage, assembly body or compiler-profile change is introduced.

Actual production recount: **4,715 / 5,528 (85.29%) total**,
**4,042 / 4,855 (83.25%) Game**, Init 492/492 and Debugger 181/181.
There is zero drift and 813 still different. This adds one accepted match;
conversion rows and denominators remain unchanged. The **90% goal stays
active: 261 more matches** reach the required 4,976 / 5,528.

## Recovered interface and behavior

The function receives one `u8 *owner`. Slot 3 of the complete 58-entry
retail `D_8008AA70` callback table contains its address, at ROM `0x22F53C`.
The table, original target and complete 109-word `func_1514D15C` dispatcher
are pinned against ELF and ROM. No aligned direct J/JAL pattern or interior
entry is found. The dispatcher ignores the callback return; the recovered
interface is `void (u8 *)`. Historical C return spelling remains unproven.
Original and normalized code leave the final spawn provider's value in V0.

The existing packet types are reused with their full extents:

| Object | Extent | SP offset | Recovered fields |
| --- | ---: | ---: | --- |
| Final vector | 12 bytes | `0x50` | Separate `(0, 0, 150)` storage |
| Runtime | 32 bytes | `0x5C` | `(0, 0, 100, 0, 0, 600)`, owner, kind 12, owner identity, mode 2 |
| Descriptor | 88 bytes | `0x7C` | Type 3, flags `0x401` / `0x2012`, color `(255, 230, 0, 255)`, zero vector |
| Source | 92 bytes | `0xD4` | Sizes `(45, 55, 25, 45)`, two half values, live coefficients, scale and tail |

Source `zero10`/`zero14` receive 0.5; these shared field names predate this
callback and do not imply a zero value. Coefficients are loaded from
`D_800A5E18` / `D_800A5E1C`, with retail bits `0x3F666666` / `0x358637BD`.
Uninitialized bytes are retained rather than cleared.

The call to `func_15189FF0` supplies `(desc, source, runtime, 2, 3, 0, 0)`.
That already restored 41-word wrapper writes source byte `0x58 = 11`,
calls its factory and copies the 32-byte runtime to result+`0x170` on
success through the original 11-word `memcpy`. The 92-byte source extent
is required. Both original helper bodies are pinned and executed here;
this does not add helper credit.

Attachment under key 7 occurs unconditionally, including NULL. The final
16-argument call is `(owner, 12, &finalVector, 2, 300, 40, 255, 181, 0,
255, 0, 2, 0, 0, 255, 1)`. Its vector is separate from the live runtime
storage, which opaque providers may retain or mutate.

The original prologue saves RA at SP+`0x44` and the incoming owner at
SP+`0x130`, the valid caller argument home above its frame. The owner is
reloaded after the wrapper and after attachment. Tests that deliberately
mutate that home are **guest ABI probes only**; portable native C tests
do not claim an external helper can mutate an unescaped parameter home.

## Closed compiler normalization

The selected source emits 123 words, the exact 304-byte frame, identical
RA/home lifetime, all local offsets and all seven bindings before guards.
All 77 raw neighbors, their pools and four existing diagnostics are unchanged.
Source declaration and assignment ordering recover the retail register roles.

| Schedule block | Instructions | Closed dependency proof |
| --- | ---: | --- |
| `0x06C..0x078` | 3 | Disjoint initialized fields |
| `0x078..0x088` | 4 | Disjoint color-byte stores; three positions differ |
| `0x0F4..0x104` | 4 | Disjoint runtime zero stores |
| `0x108..0x118` | 4 | Disjoint source tail bytes |
| `0x18C..0x1D4` | 18 | Separate final vector/outgoing arguments and fresh owner load |

Every pair within each permutation block is independent in both register
and memory read/write hazards. No call/branch or FP arithmetic, conversion,
comparison or FCSR operation is crossed. Only the 32 differing positions
receive guards, each checking the exact input word and absence of a binding.
All 123 normalized words and seven bindings equal the original.

Both complete padders produce the same owner, and both before objects
reproduce the frozen accepted baseline. All 77 normalized neighbors and pools,
the classifier tables, and prior neighbor guards remain unchanged.
Raw and normalized complete post-return guest states agree. Literal raw
fault-prefix parity is not claimed because independent instructions move;
the normalized streams have complete literal fault-state parity.

## Fresh qualification and actual production

- Native actual C: **28,672 cases each at O0/O2/O3**, all 256 identities,
  NULL/success, four provider-mutation masks and fourteen coefficient patterns.
  Separate translation units, opaque noipa providers, strict aliasing,
  UBSan traps and LTO type checks are enabled. MXCSR remains unchanged.
  Providers poison all packet bytes only after checking initialized fields;
  subsequent full-byte checks therefore avoid reading indeterminate native
  representations. The final vector must remain separate. Ten effective
  controls reject wrong flags/color/size/coefficient/mode/kind/key, skipped
  NULL attachment, aliased vector and wrong final Z. Signal/trap is not
  accepted as a successful negative control.
- Guest: **1,280 cases per stream**, four streams, two helper modes,
  **10,240 runs**. All 123 target, 41 wrapper and 11 memcpy words execute.
  Independent byte-offset packet/public-effect references, all owner-home
  mutation masks and complete raw/normalized post states agree.
  **392 fault-prefix triples** compare complete normalized states.
  Three controls reject stale attachment owner, stale final owner and
  aliased final vector.
- Complete original dispatcher: **11,632 connected runs**, 7,680 target
  entries, two parent streams, two child streams and both helper modes.
  All 109 parent and 123 child words execute. Three selected routes and
  three return-value poisons agree with the independent dispatcher reference.
  Table/route controls are effective. Selectors/classifier remain controlled
  interface fixtures; grandparent, hardware and gameplay acceptance are not
  inferred from this bounded caller test.
- Boundaries: all **246 word**, **14 binding**, **64 injected guard binding**
  and **64 missing-guard** cases are visible or rejected as appropriate.
  Both overflow controls reject. Twenty independent GNU links cover four
  symbol groups, HI16/LO16 carries and raw/manual/retail/both-padder routes.
- The actual three-command Make owner recipe reproduces the qualified
  object. An independent frozen-before-C plus original-ASM ELF prediction
  equals the complete linked image: **458 changed bytes, zero exclusions**.
  All 720 data owners / 189,088 protected bytes, all neighbors, guards outside
  the appended rows, addresses and conversion rows are unchanged.
  Actual production Make and the fresh matching recount agree.

The focused packet is checked in both the primary tools repository and an
isolated tools twin before and after installation. The real sibling tools
repository, its HEAD and all preexisting dirty work remain untouched.

| Phase | Elapsed | Tests |
| --- | ---: | ---: |
| pre-primary | 202.932 s | 5 fresh / 0 reused |
| pre-sibling | 204.139 s | 5 fresh / 0 reused |
| installed-primary | 176.889 s | 5 fresh / 0 reused |
| installed-sibling | 206.331 s | 5 fresh / 0 reused |

The paired reports agree, including 327 primary / 328 twin imports and 244 tool data inputs. All ten new task files are independently copied. Shared `make tools-check` passes. The frozen input set contains 4,210 hashes and 3,774 independent snapshot copies. Claude calls: **0**; no subagents or pushes.

Tools commit: `2cbb00dd6c8f92ad1b665d1847be0c632ae249b6`.
Production ELF SHA256: `1f39fa259bcbaf77f39a0668e5df81b58907273feda67b6a16e675835f588d98`.
Selected complete owner C SHA256: `4ee183d196a526053dacebb1f96b871dbd6ac5518f96f436817f7374dbab077e`.
Selected padded owner SHA256: `f0558e7813adc5ed7c223dde6d472e96dfdaa2b3b5e844fbbd5cfe2577ee91b3`.

## Host applicability, graph and next step

The read-only sibling audit found `64CBFDOGL/recomp_scene/cd64_out/func_1514E31C.c` as an unqualified generated stub (SHA256 `ea39cf98e7890d9c122117eb25ea12b1a0509f8da41740c47099ae956eac0e1b`). No host implementation transfer, edit, build or launch is made. Release stays frozen.

Graphify receives a scoped AST refresh and audits every current definition and retained prior ID/proof after observing the actual Git hook producers terminate. Full-corpus re-extraction is not claimed. The committed bank retains the graph, frozen inputs, both suite closures, actual build/image proofs and final commit receipts.

Continue with the next ordinary unmatched Game callback from sealed N81. `func_1514EECC` is the next candidate in this owner; inspect its complete body, ABI, caller and compiler output before selecting it. The adjacent `func_1514E508` is already matched and receives no new credit. One accepted callback does not complete the 90% goal.
