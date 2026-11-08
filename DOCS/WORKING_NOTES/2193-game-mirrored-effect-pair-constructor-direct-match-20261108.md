# Mirrored Effect Pair Constructor Direct Match - 2026-11-08

`func_151BD2F8` now emits all **77 words / 308 bytes directly from C**,
including the original **0x60-byte frame**, three full-word incoming homes,
sparse 60-byte packet and the two-byte scratch at SP+0x20. There are
**zero new instruction guards, compiler-profile changes or table bindings**.
No metadata permutation is required. The literal full-image delta is
**243 bytes**, with zero exclusions and all other code/data preserved.

Production: Total **4,262 / 5,513 (77.31%)**, Game **3,589 / 4,840 (74.15%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift. There are
**1,251** different converted functions and **149** additional exact functions
needed to reach 4,411 / 5,513 and the active 80% goal. Conversion rows and
denominators remain unchanged.

## Interface, packet and original behavior

Owner `conker/src/game/generated_1E73B0.c`, original `asm/1E73B0.s`;
VA **0x151BD2F8..0x151BD42C**, ROM **0x1EA7A8..0x1EA8DC**.

```c
void func_151BD2F8(u8 *owner, s32 unused1, s32 unused2);
```

The original spills A2 at incoming SP+8 and A0/A1 at incoming SP/SP+4.
Only the owner argument contributes semantic values. A null owner skips
the packet, global load and all helper calls. The recovered local packet
type has the measured 60-byte layout; it does not alter shared headers or
invent names for fields whose broader meaning is not established.

For a nonnull owner, capture owner[0x3B], retain the owner pointer, and
construct the following packet at frame SP+0x24. Explicit padding fields
stay untouched, matching seeded original guest bytes.

| Packet offset | Width | Initial value |
| --- | --- | --- |
| 0x00 | byte | captured owner[0x3B] |
| 0x04 | pointer word | owner |
| 0x08 | byte | 1 |
| 0x0C..0x20 | six f32 | 31, -34, -117, 35, -24, -182 |
| 0x24 | byte | 0 |
| 0x26 / 0x28 / 0x2A | three s16 | 50 / 100 / 300 |
| 0x2E / 0x2F / 0x30 | bytes | 4 / 4 / 3 |
| 0x34 | f32 payload | D_800AA850, copied exactly |
| 0x38 / 0x39 | bytes | 5 / 0xFF |

Submit this same packet to `func_15134DAC(&packet, 2)` twice. Each independent
nonnull result receives `memcpy(result + 0x80, zero, 2)`. The second submission
must still happen if the first allocation fails, and its result must be
tested independently. After the first factory and optional copy, reload and
negate packet floats at offsets 0x0C and 0x18 (SP+0x30 and SP+0x3C).
Provider mutations to those live fields must affect the second packet.
Changes to the owner tag/global after initial construction do not trigger
new owner/global reads. The zero scratch can also be changed by a bounded
copy provider and remains live for the second copy.

## Direct compiler shape and owner qualification

Actual Make uses this owner's inherited O2/g3/MIPS2/O32 profile without
the previous target's no-unroll flag. The first semantic compile already
matched the 77-word length, frame and all 56 owner neighbors. Three words
differed because scalar `u16 zero` was allocated at SP+0x22.

`u16 zero[1]` recovers SP+0x20 and both original copy-source arguments
directly. Only two bytes are initialized; adjacent bytes remain untouched.
The rejected scalar and accepted one-element-array screens are retained.
All 77 words and all **six** bindings agree in isolated and complete-owner
compiles. No raw words or relocations are normalized.

Both padders preserve the complete **57-function** owner and all **56**
neighbors/pools. The register mask is the exact union of the frozen owner
and isolated target. There are no exported interior labels to move. The
actual five-command Make recipe reproduces the exact padded object and all
57 compact bodies. Six existing pointer/integer diagnostics remain identical;
the target has no isolated diagnostic and introduces no new warning.

## Execution, helpers and caller evidence

Six focused checks pass before and after installation in both tools copies,
with sequential runs and exact source/dependency fingerprints:

- **1,632 guest cases** across three code/global/helper layouts execute all
  77 words. Independent full memory, sparse packet padding, argument homes,
  helper calls and observations agree. Original and C literal register,
  FP, private-memory, access-trace and branch-delay states are identical.
- **195 guest alias cases** cover shared output, copy destinations within
  the mirrored fields, scratch, packet padding and owner byte, plus owner
  byte aliases with scratch, a packet field and the A2 incoming home.
  Synthetic private-frame aliases are guest address-model checks only.
- **129 exact fault-prefix cuts** fire and preserve identical original/C
  states. These qualify emitted order, not portable C fault behavior.
- **8,448 native32 cases at each of O0/O2/O3** pass trapping UBSan, packet
  offset/width checks, live provider mutations, exact coefficient bits,
  independent allocation outcomes, shared backed output and full output
  canaries. All **16 semantic controls** are effective. Native fixtures
  inspect initialized fields; guest fixtures qualify untouched padding.
- Three independent GNU links and **12 rebased executions** qualify all
  six bindings, including global low-half carries and rebased helper JALs.
  Word/binding/register-metadata controls reject 77, six and72 corruptions.

The original **39-word `func_15134DAC`** and **11-word memcpy** run connected
in **64 cases**, with a bounded six-argument allocation provider. The real
factory forwards `(0x29, 0, 0x82, 1, 0xFF, 1)`, copies all 60 packet bytes,
and performs its original result initialization. The independent reference
checks all non-stack effects; literal helper scratch also agrees between
original and C executions. This is not full allocator qualification.

The complete aligned pristine census finds one direct JAL at ROM
**0x17C6A4 / VA0x1514F1F4** in `func_1514F194`, with no aligned entry/interior
pointer literal or direct interior entry. The original seven-word window
**0x1514F1F0..0x1514F20C** sets A1=0xFF and puts A2=1 in the JAL delay slot.
Its following call to `func_151B9F00` rewrites A0/A1/A2 before entry and does
not consume this target's V0. **64 connected caller cases** preserve complete
memory, calls, packet observations and literal original/C state. The larger
parent and following service body are not qualified by this bounded window.

Fixture corrections were completed before the accepted final suites: the
independent -24.0f constant was corrected to 0xC1C00000, and native test
functions use `-mstackrealign` after GDB identified a misaligned SSE stack
store at the freestanding x86 entry. No IDO or production profile changed.
FP negation tests cover exact payload/sign behavior; FCSR exception
equivalence is not claimed.

## Whole-image and production audit

The predictor starts from the complete frozen ELF, replaces only this
308-byte body, and updates its symbol extent from12 to308. All **243 changed
bytes** are in that body/extent. No symbol/string table or other region is
excluded, reordered or copied from the result. Four corruption controls
reject changes in the header, target body, extent and protected data.

All **6,052** disassembled entries retain their addresses and every other
function body/extent is fixed. Protected data remains exact across **720
owners /189,088 bytes**, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production Make compiles only this owner and reproduces the predicted ELF
and padded object. The progress CSV, Makefile and guard manifest remain
byte-for-byte unchanged. A fresh actual-ELF recount gives the totals above.
The existing full-ROM checksum failure (make all exit2) and duplicate
generated_12D630 recipe warning remain.

Both shared tools smoke checks are fresh. Three prior helper regression
checks per copy are reused with identical fingerprints. The sibling tools
checkout's **2,434** existing dirty paths are fingerprinted and preserved;
the sibling overlay is read-only outside the ignored target stage.
Baseline consumer `bb0b3043f3b3b7cf993f1e4de6077d9e1446f823`, tools
`ffa9d51123bf7dcd8b4d7780a6d2a4ae3e9222a6`; **115 frozen inputs**.
Claude calls: **0**. Source, compiler, original helper/caller and literal
image evidence resolve this routine without an advisory call.

Accepted raw SHA256: `ead9eded03bfe0fb2c7c7bdbefcf4bcf8bf374171835a17e7cd1012cf8de69ff`.
ELF SHA256: `63cfd155ada437ef55436f4718a7100ce7182d070bb750934786b8d71f046bf3`.
Binary SHA256: `a7d6c56ac3c1de3396250adaa72987951cf9f5af8a74b9ef508e77964ad19421`.
Owner SHA256: `898f3f5494ec19fe431c543fbbe55ec9e512cfcba4d9b7676b4996220477d7d7`.
Guard CSV SHA256: `f67f8d18908dc6db9ba58dfa2db4b4204a7202104e67173c35213711333f4dd9`.

## Resume boundary

Next: **`func_150EFA4C`**, an uncredited attachment-position-delta callback
in `conker/src/game/generated_11C2B0.c`. Body77words /308bytes; frame0x18,
VA0x150EFA4C..0x150EFB80 /ROM0x11CEFC..0x11D030. Graphify currently shows
placeholder/owner relationships, with no accepted recovery for this target.

Follow actor+0x60 to its link+8 source, and source+0x110 to the attachment
block. Gate on source byte0x128 bit0 and attachment owner's word+0x1D4.
On success, preserve six ordered source-word copies to actor+0x30..0x44,
two exact FP loads to actor+0x54/+0x58 and byte-indexed D_800A1638 /
12-byte D_800A1620 selection. Call func_15143134 with the selected vector,
actor+0x48 output and the live matrix base plus the selected byte<<6.
Reload actor fields after the helper, subtract position components from
the new actor+0x48 vector, and set actor byte0x1C bit1. Both failure paths
clear that bit; every path returns1. Preserve original duplicate/unreachable
loads and branch-delay behavior. Audit actual callers and byte-index
domain before declaring table bounds or shared structures.

Complete the usual qualification and production gates before matching
credit. Current receipts: `conker/build/game-mirrored-effect-pair-151BD2F8-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
preserves existing unscanned nodes, with retention evidence; it is not a
fresh full-corpus extraction. Host Release remains frozen. The 80% goal
remains active.
