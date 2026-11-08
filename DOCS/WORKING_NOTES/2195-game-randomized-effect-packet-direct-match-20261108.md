# Randomized Effect Packet Direct Match - 2026-11-08

`func_15014F6C` now emits all **78 words /312 bytes directly from semantic C**,
with its original **0x98 frame** and **zero new guards**. Its complete owner,
both padders and actual Make output agree. The literal full-ELF prediction
changes **229 bytes**, with zero exclusions or metadata permutations.

Production: Total **4,264 /5,513 (77.34%)**, Game **3,591 /4,840 (74.19%)**,
Init **492 /492**, Debugger **181 /181**, zero address drift. There are
**1,249** different converted functions and **147** more exact functions
needed for4,411 /5,513 and the active80% goal. Conversion denominators and
the progress CSV remain unchanged.

## Recovered interface and ordered packet construction

Owner `conker/src/game_40490.c`; original
`asm/nonmatchings/game_40490/func_15014F6C.s`. This root owner has no aggregate
`asm/40490.s`. VA **0x15014F6C..0x150150A4**, ROM **0x4241C..0x42554**.

```c
s32 func_15014F6C(DispatchRecord40490 *record);
```

The existing callback record/type is retained; its local forward declaration
now carries the recovered pointer argument. Clear the obsolete placeholder
comment and replace the zero-return stub with the complete routine.

Set source byte+0x16 bit2, capture the low byte of source word+0x20 and
source word+0x1C bit0, then capture the low/high16 halves of source word+0x18.
The84-byte packet starts at frameSP+0x44:

| Offset | Field |
| --- | --- |
| 0x00 | Source pointer |
| 0x04 /0x08 | Minimum and extra inclusive range |
| 0x0C | Unsigned random selection |
| 0x10..0x4F | Complete64-byte float matrix |
| 0x50 /0x51 | Boolean mode and low-byte variant |
| 0x52..0x53 | Two untouched C padding bytes |

Call `func_150ADA20` and interpret its signed API result as an unsigned32-bit
word. Compute `random % (extraRange + 1) + minimum` using the saved halves.
The divisor is1..65536. The original unreachable BREAK7 at relative+0x90
remains in place; no valid captured range can reach it. RNG mutations cannot
change the captured range, mode or variant, but subsequent angle reads remain
live. Read source float words+0x0C/+0x10 after RNG and call
`func_150A8050(packet.matrix, angle0, angle1, 0.0f)`.

The matrix helper writes all16 words. Its unchanged original84-word slot
(83-word routine plus alignment) is pristine, SHA256
`727ecfda0b752639a309fedd7e97297a5df2acf2d817b92a76e528e0f51c70f2`.
Its final JR delay store writes matrix[3][3]=1.0f. After the helper, reload
the three signed16 source coordinates at+0/+2/+4, convert to float and replace
matrix[3][0..2]. Packet+0x4C is initialized matrix data, not padding. Tests
provide all64 matrix bytes, preserving arbitrary non-arithmetic FP payloads,
and exercise coordinate mutation after the matrix call.

Submit the nine factory words
`(300, -1, 0x31, -1, 0, 0x2A, 0x54, 0xFF, 0)`. A nonnull result receives
`memcpy(result + 0x28, &packet, sizeof(packet))`; both paths return1.
The existing shared factory declaration carries its size word in a
`struct37 *` parameter. Its original body performs numeric+0x28 size
arithmetic rather than dereferencing that parameter. Keep the explicit
`(struct37 *)sizeof(packet)` cast and document this measured legacy ABI;
do not repair unrelated shared callers as part of this conversion.

## Source screens and complete owner

A direct byte-field if/else emits77 words; a direct byte-field ternary emits
78 words with33 differences. An explicit local signed32-bit ternary followed
by the byte store recovers the exact78-word compiler shape and every word.
The local variable needs no initializer. `sizeof(packet)` also emits the
same raw bytes as the literal84-byte size. The isolated and complete-owner
function bytes and all four JAL bindings agree exactly, raw SHA256
`c358b30bab8ba993f7ffdff8a5de6af47160f6cf167c110115ef7d3e675a2c47`.

Keep the existing O2/g3/MIPS2/O32 profile. Actual Make uses five commands:
assembly prepass, IDO compile, assembly postpass, production padder and GNU as.
Both padders preserve all **32 owner functions /31 neighbors**, unchanged
pools and the exact register-mask union. The independent padder uses a
layout-only manifest generated from frozen retail annotations; candidate
instructions always come from the compiled object. There are no moved
exported interior labels. All compiler diagnostics are empty.

## Execution qualification

Six focused checks pass before and after installation in both tools copies,
with sequential runs and exact source/dependency fingerprints:

- **4,338 guest cases** cover zero/full16-bit ranges, high-bit RNG results,
  modes, variants, allocation outcomes, stack phases, helper mutations and
  three code/helper layouts. Independent complete memory, calls and packet
  observations agree with original assembly. All77 reachable words execute;
  the unreachable BREAK remains preserved.
- **24 synthetic alias cases** cover source/private-frame overlap and an
  output payload aliasing the input. These are guest address-model probes.
  All84 packet bytes, including the seeded private padding, are compared.
- **124 interrupted-access cuts** compare literal original/direct-C state.
  They qualify emitted instruction order, not portable C fault behavior.
- **2,880 native32 cases per O0/O2/O3 profile**, with trapping UBSan, use
  typed source/packet objects, measured field offsets and full object canaries.
  All **15 semantic controls** are effective, including signed RNG remainder,
  wrong mode/range/variant, unsigned coordinate conversion, matrix overwrite,
  factory/copy sizes and return value. Native padding bytes are observed and
  copied without assigning a portable value to them.
- Three independent GNU links and **12 rebased executions** qualify all
  four helper bindings. All78 word corruptions, four binding corruptions,
  72 register-metadata corruptions and four entire-image corruptions fail.

The original49-word factory and11-word copy routine run connected in
**72 cases**. Allocation and zeroing are bounded providers. The real factory
requests124 bytes with `(35, 0, 124, 1, 255, 1)`, initializes the measured
prefix and zeroes16 bytes; the actual byte-copy loop transfers84 bytes.
Private helper state is checked by literal original/direct-C execution;
an independent model checks public effects and ordered packet observations.

The pristine aligned census has no direct J/JAL entries or interior pointers.
Its sole aligned pointer is ROM **0x22794C /VA0x80082E8C**, slot23 in
**D_80082E30**. The existing recovered dispatcher is **func_15013000**.
Its original16-word window **0x15013050..0x15013090** decodes kind bytes
0x5C..0x5F, fetches slot23, passes the correct record in the JALR delay slot,
then reloads the live count. **96 caller cases** cover both0/0x34 offsets,
all four kind bytes, both allocation outcomes and helper mutations. Parent
S0 is restored and the count/iteration update agrees. The caller ignores V0;
the target still returns1. The complete dispatcher loop, RNG implementation,
trigonometric leaves, hardware and gameplay are not newly qualified here.

## Literal image and production

The independent predictor replaces only the312-byte target body and its
12-to312-byte symbol extent. All **6,052** disassembled entries retain their
addresses; every other body, extent and metadata byte remains fixed.
Protected data is exact across **720 owners /189,088 bytes**, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production compiles only this owner and equals the complete229-byte prediction.
Makefile, table bindings, guard manifest and progress CSV are unchanged.
The known full-ROM checksum mismatch (make all exit2) and duplicate
generated_12D630 recipe warning remain. They are recorded separately from the
successful target compile, ELF link, production recount and exact-image audit.

Both shared tools smoke checks are fresh. Three unchanged helper regression
checks per copy are reused with exact fingerprints. The sibling tools'
**2,434** dirty paths remain fingerprinted and preserved. There are **107
frozen inputs**. Baseline consumer `83b156ff9a672a37e29ae646aafbea4b677e271e`,
tools `c832531aaf5e4202f3a830b5be0854fde741ed92`. Claude calls: **0**;
local source/compiler, ABI, execution and literal-image evidence resolve this
routine without an advisory review.

ELF SHA256: `9999cfb70f41038cf49d477311db03fcc79859e7b2499290b378ede0a3b79615`.
Binary SHA256: `7e7c0069e04ff8116a90076511e4967788bf1b83eeefad33f5ced24cfb71282c`.
Owner SHA256: `61ab93b1495c8fc3d52bfeb50568c7beeb6db85e8885efaa5e720a41e316db77`.
Guard CSV SHA256: `937a368e14e175c75d7577633990f4a3bba0a0f50040900924b9c948bc4d1850`.

## Resume boundary

Next: **func_150234A4**, an uncredited three-record lookup/reuse routine in
`conker/src/game/generated_49D30.c`, original `asm/49D30.s`.
VA150234A4..150235DC /ROM50954..50A8C;78words /312bytes, frame0x28.
Audit its two-argument pointer-return interface, all callers, globals and
actual owner compiler profile before attempting source recovery.

Scan three0x38-byte records from D_800C3CA0 to D_800C3D48 for signed16
key arg0+1 or an empty key. Matching-record reuse and empty selection have
different paths. If reuse is requested and byte+0x0C is set, call the existing
reset helper func_15023440 with the first-record base on a match, or the
selected record on an empty slot. The full-table path falls back to the
first record and resets it regardless of that request flag. Preserve saved
key/pointer lifetimes, helper mutations, repeated lookups and the final key
write only on the selected fallback. Keep all matching credit private until
the normal owner/ABI/execution/literal-image/production gates pass.

Receipts: `conker/build/game-randomized-effect-packet-15014F6C-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
retains existing unscanned nodes with audit evidence; it is not a fresh
full-corpus extraction. Host Release stays frozen. The80% goal remains active.
