# Linked-effect update direct byte match - 2026-11-23

`func_151D1138` now replaces its zero-return placeholder with the complete
actor-linked effect update. All **124 words / frame 56** and all **six relocation
sites** emit directly from semantic C. There are **zero guards, insertions or
omissions**. Total rises from **4,639 to 4,640 / 5,528 (83.94%)**; Game becomes
**3,967 / 4,855 (81.71%)**, Init remains 492/492 and Debugger 181/181. There is
zero address drift, 888 different functions and **59 more matches to 85%**.

## Behavior and interfaces

The complete original is `conker/asm/1FA770.s:4270`, VA
`151D1138..151D1328`, ROM `1FE5E8..1FE7D8`. It is update-table slot 95 at
`D_8008A4E8+0x17C` (`8008A664`), documented by the original rodata word in
`conker/asm/data/22EF80.rodata.s:116`. Its `void(struct260 *)` interface agrees
with the actual production dispatch table in `variables.h` and its caller.

- Capture the actor from owner+0x28. A zero actor first word or identity mismatch
  between owner+0x2C and actor+0x3B retires the owner's s16 lifetime at+0x0E to -1.
- Copy current position to previous, then invoke the position callback selected
  by owner+0x5C through `D_8008FC30`. It receives the captured actor and the
  public current-position pointer. On failure, restore current from the live
  previous vector and set the detach gate, while still running the later helpers.
- Compute the three coordinate differences into a real `f32 delta[3]`, call
  `func_15143E64` and store its returned distance. Then call the classifier on
  the captured actor's current word+0x184. Its actual source in
  `generated_13BB20.c` defines `u32 func_1510F8CC(u32)`, returning `value & 0x1F`;
  the new declaration preserves that interface.
- Reload the distance and actor state after the calls. Callback failure,
  distance>300 or<=0, nonzero actor float+0x28, nonzero byte+0xAD, or classifier
  result 5, 6, 9, 13 or 14 detaches through `func_151D13E0`. Otherwise construct through
  the already recovered `func_151D1448` only when the child pointer is null.
  NaN distance fails both ordered distance comparisons; NaN actor vertical state
  is nonzero. Pointer captures, call order and late public reloads are retained.

The first complete C draft had 124 words but a 64-byte frame. Explicit link-state
fields reduced scheduling differences, and assigning its two vector fields
directly removed redundant pointer locals and recovered the exact 56-byte frame.
The selected body uses the table-compatible owner parameter and real delta array,
without compiler hints or word normalization. All 51 owner neighbors, literal
pools, relocation bindings and diagnostics remain fixed. Both full-owner padders
produce an identical object, including metadata; actual Make replay reproduces it.

## Focused qualification

- **884 cases per raw/padded/padded/retail stream** agree with an independent
  public-memory, ordered-call and floating-gate model. Complete guest private
  memory, register and access traces agree across the identical instruction
  streams. Original word 115 is an unreachable duplicate load retained literally.
- **224 fired access-prefix quadruples** compare complete guest state and the
  dispatched word. These are binary observations, not portable C trap claims.
- The actual production `func_15149264` dispatcher in
  `src/game/done/game_1765E0.c` already matches all 45 original words. The complete routine runs with the new
  callback in **81 connected cases per stream**, including
  four ticking values, 10 pre-callback lifetime-underflow cases and 15 final
  retirement cases. The secondary cleanup index is -1; the final retirement
  helper is an opaque compatible provider. This gives no additional match credit.
- Actual SDK32 scalar types and typed native backing pass **776 cases each at
  O0/O2/O3** with strict aliasing and UBSan. All represented backing and guard
  bytes feed comparison fingerprints after explicit pointer/endian normalization.
  Nine deliberate
  callback/copy/delta/boundary/classifier/capture/reload errors fail by result
  comparison. The native adapter uses the correct void owner-table interface;
  it does not execute the complete original C dispatcher. Thirty-one owner/actor
  alias cases and 77 signalling-NaN float-return cases remain guest-only. No
  cross-ABI signalling-NaN return-bit identity is claimed.
- **260 instruction/binding controls** preserve detectable corruption across
  all 124 words and six sites through both direct padders. These are mismatch
  controls, not guard rejections. Generic overflow remains unmatched and generated
  padding rejects an oversized body. Twelve independent GNU links across four
  code/callee/global arrangements agree; 96 guest rebase executions pass. A
  separately compiled stale-distance control fails the independent call model.

A separate audit pins the retained native control sources and binaries and
confirms all nine exits are known comparison codes (10, 11 or 12). No signal
or UBSan trap is counted as a successful comparison control.

Opaque providers conservatively mutate public state to test capture/reload
lifetimes. The position callback, distance helper, classifier, constructor and
detach implementations are not all executed by those models. In particular,
the classifier mutation scenarios are stronger than its actual pure low-bit
body. Neighbor fingerprints retain earlier qualification without claiming fresh
neighbor-suite runs or hardware/gameplay acceptance.

| Run | Time | Checks |
| --- | --- | --- |
| preinstall-primary | 213.630s | 5 fresh / 0 reused |
| preinstall-sibling | 174.187s | 5 fresh / 0 reused |
| installed-primary | 163.035s | 5 fresh / 0 reused |
| installed-sibling | 227.619s | 5 fresh / 0 reused |

## Production and preservation

The independent predictor recompiles frozen old C and replaces only the target
with original ASM. It reconstructs every ELF byte and named definition without
the recovered C or guards. Production equals this prediction: **361 changed
bytes, zero exclusions**. All 189,088 protected Game bytes / 720 owners remain
exact. Actual production Make, production recount and shared tools-check pass.

```text
before ELF: 589d33abd291d98651f557223c00d9a1071c02adf8691dc87975f3d5a255d846
after ELF:  d22581018f435e71dde2322d1de70655c4ab0ce4193227f0912da30b285ee5db
owner:      503f7209d2a2821cdc3dc95ef056d311095dd5613a4064e1824049a0c76e8593
```

The guard CSV is byte-identical to the frozen baseline; its inherited newer
timestamp is held old with `-o retail_word_patches.us.csv` during actual Make.
All other frozen objects, conversion rows, layouts, headers and the complete
Debugger object are audited unchanged. The real dirty tools sibling is preserved
through a separately pinned overlay. Both host scene configurations were
rechecked: they consume binary inputs, the selected scene lists this target as a
stub, and no direct C consumer or complete host build root exists there. No host
build, Release change or gameplay acceptance is claimed.

Tools commit `3573a342cbba65ad39f65ed87c852a79ceeafb7f` precedes
the consumer source/pin/docs commit. Nothing is pushed. README changes only its
two aggregate status rows; five documentation indexes receive a short note entry
with every prior byte retained. Graphify's scoped AST qualification retains all
old IDs after observed hook completion; this is not full-corpus extraction.

The 85% goal remains active. Resume ordinary unmatched Game entries from this
committed checkpoint. The larger `func_15197148` renderer remains private and
uncredited on its own older frozen baseline.
