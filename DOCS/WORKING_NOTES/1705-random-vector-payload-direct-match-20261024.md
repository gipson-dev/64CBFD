# Randomized Vector Payload Direct C Match

Verified 2026-10-24. Recover `func_150B1EE0` in
[generated_DF260.c](../../conker/src/game/generated_DF260.c), replacing its
zero-return placeholder with complete semantic C. All 44 words match
directly; no new guards, profile changes or alignment tail.

## Scope And ABI

- VA `150B1EE0..150B1F90`, ROM `DF390..DF440`, 176 bytes.
- Normal mixed-owner O2/g3 profile; frame 72, RA at SP+0x2C.
- Four arguments: owner bytes, three-float vector, two unused full words.
  Retail homes A0/A2/A3, not A1; recover a void callback, not a zero return.
- Preserve the owner's four other functions and normalized pools, including
  handwritten `func_150B1DB0`. Do not convert the handwritten RNG.

The function copies the three vector words into SP+0x38 and writes positive
zero at SP+0x44 before invoking `func_150ADA20`. Treat the RNG's low word
as unsigned for modulo 133, then add 69, giving lifetime 69 through 201.
Only afterward read owner+0xC and owner+1 for the factory's routing fields.
Keep the explicit separate lifetime statement: a single argument expression
allowed native GCC to read owner bytes before the RNG. The native mutation
fixture exposed that counterexample; explicit sequencing keeps exactly the
same IDO instructions and bindings.

Use the actual `func_15149130` prototype:
`(s16, s8, s8, s8, u8, u8, struct37 *, u8, s32)`.
The fourth argument is signed -1, not unsigned 255. The pointer-shaped
seventh argument carries the numeric payload extent 16 in this existing ABI;
the original factory computes a 56-byte allocation request. Preserve the
shared declaration/helper rather than changing its historical pointer
arithmetic. Native tests observe that token without dereferencing it.

The factory receives `(lifetime,-1,0x49,-1,1,0,16,slot,route)`.
On non-NULL result, forward-copy all 16 vector/scalar bytes to result+0x28.
On NULL, do not copy. No owner/position NULL checks or new return contract
are invented.

## Caller And Helpers

`D_8008F970` contains four callbacks; target is slot 3 at ROM `23443C`.
The aligned retail scan finds that sole literal and no direct JAL to this
target. Execute the original ten-word `func_151A8CEC` window
`151A8E9C..151A8EC4` (ROM `1D634C`) with selectors -1 and 0 through 3.
It passes owner, the parent's stack vector, a full A2 word and masked A3
byte. Only -1 is excluded; no invented range checks. The larger parent C
placeholder remains untouched and uncredited.

Connect the original 18-word 64-bit RNG, 49-word factory and eleven-word
memcpy, verified against the predecessor ELF. In 48 seed/failure/stack
phases, visit every RNG/copy word and all 47 factory words reachable with
flags=1. The two flag-2 allocator-kind instructions are outside this
caller's domain. Bound the generic allocator and bzero; allow caller-saved
GPR/FPR and legal argument-home clobbers. Preserve low-word DIVU semantics
after a sign-extended RNG result. This is not full-parent, native factory
pointer-arithmetic, hardware or gameplay acceptance.

## Qualification

[Experiment](../../tools/experiments/game_random_vector_payload.py) and
[focused tests](../../tools/tests/test_game_random_vector_payload.py)
reuse the existing compiler, padder, linker, owner/pool, MIPS and native32
helpers. Both tools copies pass eight fresh pre-install and eight fresh
installed checks, with no failures, errors, skips or reused checks.
Both shared project checks pass.

- 1,920 semantic guest cases: unsigned random boundaries, all routing-byte
  values, six vector layouts including private argument/payload aliases,
  four destination layouts, allocation failure and provider mutations.
  Original and direct-C complete modeled states agree.
- Actual table/call-window execution in ten phases; parent C remains a stub.
- Native O0/O2/O3 trap UBSan, 12,288 cases per profile, full output canaries
  and ten effective defined wrong-C controls. The freestanding SSE fixture
  explicitly realigns its stack; it does not run the factory's pointer arithmetic.
- 80 fired root-access prefix pairs, emitted guest order only; six
  independent GNU links over three layouts; four strict-image corruptions.
- Independently assembled original, isolated/whole-owner C and padded
  objects agree. Three original symbolic bindings at offsets 52, 132, 152.
  Actual five-command Make preserves all five compact functions and the
  complete padded object. Isolated diagnostics empty; owner diagnostics
  unchanged. Existing duplicate generated_12D630 Make warnings remain.

Raw body SHA256:
`1b74f8ca1ba73c024b2693fcfafe9e3deea1895adb683f87a3b8204a33d30623`.
Retail body SHA256:
`f8c328cb145f493f52ceafa6f869dfc31c459b7468b111ecce1c2b356274d266`.

## Production And Progress

Tools `7971484f3da4cd31a61521b2c312dbf65663e5c4` committed first.
The older mirror retains all 1,622 pre-existing dirty paths/statuses/hashes
and its HEAD; only the two owned modules are added, now 1,624 dirty paths.
No push or host-port changes.

Seal 15,990 files, 39 focused inputs and all 1,454 linker objects in native
and Linux cache copies using checked stdin/tar transfer, no DrvFS project
reads. Production Make passes. Adopt only source, target object and ELF
as three qualified seal overrides; generated linker/progress files are
identical. Whole-image delta is precisely 130 bytes: 129 target-code bytes
plus one target-size byte (12 to 176), zero metadata exclusions or symbol
cycles. All other 6,054 bodies and all 6,055 addresses remain fixed.
The entire guard CSV is unchanged.

All 720 protected Game-data owners / 189,088 bytes remain exact:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Adopted ELF SHA256:
`f5f5c17a2ccd35e3c59fe76fe161bfc6241e271c49ed9744e38c7facceff6710`.

Freshly recount actual adopted native ELF bytes: total **3,782/5,505
(68.70%)**, Game **3,109/4,832 (64.34%)**, Init 492/492, Debugger 181/181,
zero drift and 1,723 different. The 75% threshold stays 4,129, requiring
**347 more** exact functions. Goal remains open.

Queue: 1,594 placeholders, 120 semantic/other definitions and nine parser
misses. These are screens, not qualification. `func_1510D8C0` already has
semantic `Gfx *` C; `func_15014094` is separate existing-C work.
Next audit `func_150CE150` (44 words/frame 0x918), especially its partially
initialized 0x8F0-byte copied payload, callers and return contract before
installing C. Larger `func_1509E730`, `func_1508CAD8` and `func_15169070`
stay separate. Refresh the normal incremental graph after the consumer
commit and audit old-node retention; do not equate it to full-corpus extraction.
