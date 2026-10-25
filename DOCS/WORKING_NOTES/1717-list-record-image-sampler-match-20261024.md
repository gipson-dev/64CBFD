# List Record Image Sampler Direct C Match

2026-10-24. Production-qualified direct C recovery, adopted and freshly recounted.

## Recovered Routine

`func_1517E1AC` now has its complete semantic C body in
`conker/src/game/generated_1AB530.c`, replacing the zero-return placeholder.
All 56 words / 224 bytes emit directly under the existing O2/g3 compiler
profile, with frame zero, no alignment tail and **zero guards**.

- VA: `0x1517E1AC..0x1517E28C`; VROM: `0x1AB65C..0x1AB73C`.
- Original assembly: `conker/asm/1AB530.s`; canonical interface:
  `void func_1517E1AC(void)`.
- Eight original HI16/LO16 bindings remain: `D_800DDD64` at +0/+4,
  `D_800BE9C4` at +8/+12, `D_800BE624` at +20/+36, and
  `D_800BE620` at +24/+32 (byte offsets).
- Keep the shared buffer declaration as `s32 D_800BE9C4`, with an explicit
  `u16 *` cast inside the routine. Do not replace it with an incompatible
  pointer declaration. Width and height are signed words. The renderer's
  RGBA16 color-image and scissor commands support these roles.
- Refine only the private 0x34-byte `ListRecord1AB530` view: expose `u16
  sample2A` and keep the remaining two opaque bytes at +0x2C. The shared
  incomplete `struct162` view and shared headers remain untouched.
- Traverse next at +0x24. Reject coordinates outside the signed dimensions
  or below zero using the original floating comparisons; only then truncate
  each coordinate, index the current RGBA16 image and store its unsigned
  halfword at +0x2A. Skipped records and all other bytes remain unchanged.
- Preserve lazy reads, the current node's captured width, live per-node
  global refreshes and the branch-likely next preload. Do not cache the image
  or dimensions across records, zero skipped samples or invent a cycle cap.

The prior constructor `func_1517E080` body remains literally unchanged and
emits identical words under the refined private layout. Adjacent handwritten
`func_1517E134` and the larger `func_1517E28C` remain unchanged and uncredited.

## Actual Caller

The original scheduler `func_1501878C` lives in `conker/src/game_45B80.c`
(not `game/done/`). Its full 412-word / 1,648-byte body has frame 0x68,
saving RA and S0..S4. The message-two path calls the sampler at VA
`0x15018808` / VROM `0x45CB8`, encoded word `0x0D45F86B`, with a nop delay,
no arguments and no consumed return value. Its entry is VA `0x1501878C` /
VROM `0x45C3C`.

The local prototype now returns `void` instead of `s32`. All 16 compact
caller functions, pools and diagnostics remain unchanged, and the **complete
production caller object is byte-identical**. The whole-ROM aligned scan of
2,467,288 bytes finds this one encoded JAL and no literal target pointer;
that does not exclude arbitrary computed calls.

## Focused Qualification

Both tools copies pass **six fresh pre-install checks**, with zero errors,
failures, skips or reused checks: primary 44.156 seconds, older mirror
48.015 seconds. Both existing shared tool checks also pass (1.121 / 0.310
seconds). The focused snapshot covers 70 inputs; the final sealed manifest
covers 16,034 Native/cache inputs.

- 2,222 guest executions visit all 56 reachable words. Cover signed bounds,
  NaN/infinity, signed zero and subnormals, low-word index wrap and aliases
  involving head, width, height, buffer, sample-record and pending state.
- 108 paired fault prefixes match full guest state; six lazy-unmapped skip
  fixtures preserve the original non-accesses. These establish emitted guest
  order, not portable C fault semantics.
- Two effective compiled guest controls reject cached bounds and a cached
  image. Eighty connected scheduler cases cover 72 message-two paths and
  eight skip paths using actual original/retained caller instructions.
- Native32 O0/O2/O3 with trap UBSan pass 981 sampler fixtures per profile.
  Seven effective controls detect an inclusive upper bound, wrong stride,
  wrong offset, missing store, clearing skipped records, rounded coordinates
  and first-record-only traversal. Native fixtures use defined storage and
  arithmetic; global alias and overflowing-index probes remain guest-only.
- Fresh native constructor regression under the new private layout passes
  5,120 cases per O0/O2/O3 profile, retaining all five earlier effective
  constructor controls. This is new layout coverage, not a second match.
- Reject all 56 raw-word corruptions, one extent change and eight binding
  controls. Six GNU links in three layouts cross HI/LO carry boundaries;
  six rebased executions exercise all four global pairs. Six strict-image
  corruption controls remain effective.

Whole-owner compilation preserves seven neighbors, one GLOBAL_ASM routine,
extents, diagnostics and normalized pools. The real five-command generated
owner Make route reproduces all eight compact functions and the qualified
padded object; the caller's three-command route reproduces all 16 functions
and its unchanged complete object. Original assembly, shared headers,
compiler profiles and the entire retail guard CSV remain unchanged.

Two failed scratch gates are retained, not counted as passes. An independent
link command initially omitted established auto-symbol scripts; the corrected
command uses the existing production linker flags, without build-config edits.
A native setup parser could not recognize `struct162 *` return syntax; the
fixture now verifies the complete frozen constructor-definition literal once
in both sources. No shared parser or source/ABI/image assertion was weakened.
The corrected qualification and all six fresh checks in both copies pass.

## Production Image

Normal `make -C conker -j4 build/conker.us.elf progress.csv` passes in
13.297 seconds in the verified Linux cache using stdin/tar transport, with
no project data reads through DrvFS. It reproduces the independent **152-byte
exact image prediction**: 151 code bytes and one symbol-size byte, zero
exclusions. All 6,054 other linked bodies and all addresses remain fixed.

Protected Game data remains exact across 720 owners / 189,088 bytes:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Each tools copy passes **two fresh installed checks plus four fingerprinted
semantic reuses**, not six fresh installed checks. The fresh installed checks
take 0.834 / 0.696 seconds. Reuse requires literal equality of installed source,
caller, target/caller objects and ELF, complete sealed inputs, both modules and
all qualified artifact fingerprints.

The tools were committed first as
`138a5802a2c3dc435aa024082ce307c8d91b52d5`
(`Qualify direct RGBA16 list sampling and scheduler caller`). Preserve the
older mirror's 1,644 pre-existing dirty paths and HEAD; only two owned modules
are added there, without a mirror commit, reset or stash. Nothing is pushed.

## Measured Progress

Native adoption verifies all 16,034 sealed inputs with four explicit
source/caller/target-object/ELF overrides. The unchanged caller object is
verified independently. The actual adopted Native ELF is streamed to the
GNU recount without DrvFS and equals the independent/production image:

`f44275f52b5cf0625f28b9e08b0ba1335263a88d8a6fb2a3b3c0d6fc2b4b1cb4`.

| Section | Byte-exact C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 3,793 / 5,505 (68.90%) | 0 | 1,712 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,120 / 4,832 (64.57%) | 0 | 1,712 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Only `func_1517E1AC` leaves the predecessor queue. The 75% threshold remains
4,129 / 5,505, requiring **336 more matches**; the wider goal remains active.
Source-shape triage contains 1,583 placeholders, 120 semantic/other definitions
and nine parser-unlocated entries, not additional qualifications. Root README
changes only its two aggregate match rows; the existing verification date is
already 2026-10-24.

## Fingerprints And Handoff

| Artifact | SHA-256 |
| --- | --- |
| Focused input snapshot | `790b42a17519b9383a17eeba46d756ba4d3a89a0c255f363b70731b294857cef` |
| Final sealed manifest | `6ff7a242778eccfbb8b0f567010b3bec8f35d9fffa27c300a2ca01b57215b022` |
| Recovered owner source | `a6b84618865f2257b301edacda715fbc19b8d4ed79d6ffc807e5064e552aa34d` |
| Typed caller source | `7836725eafedce2e7103e6ce28e31dabdcd9164cebbe11683e04aff44713fb39` |
| Raw 56-word body | `418fb0289a421f4680957a0003d80c9e2dc29c746dbb6712b83e349dffd259c4` |
| Retail 224-byte slot | `e2ff360d01ee671976751fa8d514b1f0b033b1c0dd75fb7d64128a8c6a46a821` |
| Qualified padded target object | `1ca0c4d4ceec4c08763f49047e5d7a52df4d1c57e9221819d4ec43ec5748beba` |
| Unchanged complete caller object | `6f93d458b6a4991ee00a8d815534c58451aad5b9864fff79c9ceaf0c9533fafc` |
| Experiment module | `fdc04d116dd94b5be321b398ed343d9f6b1fe03fd3b56a1d368d7a062c435bad` |
| Test module | `287e1f18595763ba6f53d6e52ab6f4b27ee5325de0e09e49319bd4cf430f1d1d` |

Detailed local receipts remain in ignored
`conker/build/game-list-record-sample-match/`. Private ROMs, ELFs, compiler
outputs and packets are not published. The older private sampler screen is
superseded by this adopted checkpoint and provides no separate credit.

Next ordinary target remains `func_1519E818`, still private/non-exact at
44/45 words. Keep existing-C `func_15014094` and parser-missed
`Gfx *func_1510D8C0` separate. No candidate is credited before its complete
ABI, owner/Make, guest/native, strict-image and actual adoption gates close.

The IEEE value model is bounded, not complete FCSR/exception emulation.
OS queues and follow-up providers are bounded, not a complete scheduler,
hardware/gameplay or host acceptance claim. No host/Release, provider,
package, global configuration, save or memory files are changed.
