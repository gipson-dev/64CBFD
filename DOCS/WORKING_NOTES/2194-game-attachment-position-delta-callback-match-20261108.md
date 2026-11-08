# Attachment Position Delta Callback Match - 2026-11-08

`func_150EFA4C` now matches all **77 words /308 bytes**, frame **0x18**.
The recovered semantic C body uses **42 checked normalization rows** for
closed temporary-register lifetimes and independent instruction scheduling.
No instruction is inserted or omitted, and the existing compiler profile
and all table/data bindings remain unchanged. The literal full-ELF prediction
changes **271 bytes**, with zero exclusions and two closed metadata groups.

Production: Total **4,263 /5,513 (77.33%)**, Game **3,590 /4,840 (74.17%)**,
Init **492 /492**, Debugger **181 /181**, zero address drift. There are
**1,250** different converted functions and **148** additional exact functions
needed for4,411 /5,513 and the active80% goal. Conversion rows/denominators
are unchanged.

## Recovered interface and effects

Owner `conker/src/game/generated_11C2B0.c`; original `asm/11C2B0.s`.
VA **0x150EFA4C..0x150EFB80**, ROM **0x11CEFC..0x11D030**.

```c
s32 func_150EFA4C(u8 *effect);
```

Follow effect+0x60 to its link+8 source; the attachment block is source+0x110.
Gate on source byte0x128 bit0 and the attachment owner's matrix word+0x1D4.
If either gate fails, clear only bit1 of effect byte0x1C and return1.

On success, capture the unsigned attachment byte+0x0D, perform two ordered
three-float structure copies (six exact word payloads from source+0x34..0x48
to effect+0x30..0x44), and copy attachment float payloads+0x3C/+0x40 to
effect+0x54/+0x58. The private vector type has the measured12-byte layout;
no speculative shared structure/header is introduced.

The byte selects a12-byte vector in D_800A1620 and one byte of D_800A1638.
After the copies, reload the live owner matrix word and add the selected
byte<<6. Submit `(vector, effect+0x48, matrix)` to the existing qualified
three-argument point helper `func_15143134`. Reload the effect's incoming
home and position/output fields after that call, subtract position from
the returned vector, preserve all other flag bits while setting bit1, and
return1. Helper mutations to coordinates, flags, source links and the
guest incoming home are covered. Incoming-home retargeting and synthetic
overlapping objects are guest address-model cases, not portable C fixtures.

## Source screens and closed normalization

Initial six-float/common-return source emitted75 words. Two three-float
copies, named link/source/attachment carriers, explicit branch returns and
a vector-array declaration recover the77-word shape/frame, leaving42 word
differences. Sixty bounded isolated source-shape screens were retained;
the best alternative reduces this to41 but does not emit retail directly.
The selected source retains the measured early index capture and straightforward
field operations. Its isolated and complete-owner bytes/bindings agree.

Normalization is derived from the accepted raw words; it never copies a
retail word table into the function. It renames temporary roles before the
helper and in the flag-clear/success blocks, then applies three explicit
instruction permutations. The certificate proves:

- Four register-lifetime regions have unchanged live-in/live-out roles;
  the two temporaries sharing a normalized physical register have disjoint
  lifetimes. The taken branch-likely edges preload the exact clear-block roles.
- Three schedule blocks require24, four and two adjacent independent swaps.
  GPR/FP dependencies and overlapping memory cells forbid a swap; the fixed
  effect offsets used for movable flag/coordinate operations are disjoint.
- X/Y/Z subtraction order, frame, saved RA and incoming home are fixed.
  Outgoing branches are unconditional and retain their original destinations;
  the constant result moves into their always-executed delay slots.
- All77 instructions remain present, including the two unreachable duplicate
  flag loads at+0x100/+0x114. There are no insertion/omission rows.

Raw C scratch-register and fault-prefix identity is not claimed. The normalized
function is literal retail, including register/private/branch-delay states.
Two effective certificate controls reject a live-register collision and a
dependent instruction crossing. All77 changed-word controls, five binding
controls and72 register-metadata controls reject corruption.

The existing O2/g3/MIPS2/O32 profile has no new flags. Both padders preserve
all **44 owner functions**, all **43 neighbors**, pools and exact register-mask
union. No exported interior labels move. Actual Make's three-command recipe
produces the identical padded object and all44 compact function bodies.
Baseline, complete-owner and isolated compiler diagnostics are empty.

## Execution and registered caller

Six focused checks pass before and after installation in both tools copies,
with sequential runs and exact source/dependency fingerprints:

- **2,324 guest cases** include all256 index and flag bytes across three
  code/global/helper layouts. Independent full memory, calls and helper
  observations agree for raw C, normalized C and original assembly.
- **252 alias cases** cover in-place/overlapping snapshots, the live matrix
  cell overwritten by copied fields, selector-byte aliases, source/flag aliases,
  and helper retargeting. All75 reachable words execute; both unreachable
  original loads remain preserved.
- **133 fault-prefix cuts** fire and compare literal normalized/original
  states. They qualify emitted instruction order, not portable C faults.
- **32,768 native32 cases at each of O0/O2/O3**, trapping UBSan, use typed
  backing objects, exact offset/width checks, full object canaries, fresh
  post-helper fields and all flag bytes. All **14 semantic controls** are
  effective. Native table indices0/1 are backed objects; the broader byte
  index domain and synthetic aliases are guest checks.
- Three independent GNU links and **12 rebased executions** qualify the
  five bindings, global low-half carries and rebased helper JAL. Arithmetic
  cases use finite components; non-arithmetic copies preserve exact FP
  payloads, including signed zero, infinities and NaNs. Raw FCSR exception
  equivalence is not claimed.

The original98-word `func_15143134` runs connected in **96 cases**, including
zero/nonzero vectors and floating matrix selection, using its existing bounded
leaf-provider models. An independent scalar model checks all non-stack effects;
literal normalized/original execution also checks helper-private state. This
does not newly qualify all matrix-provider bodies or hardware behavior.

The aligned pristine census finds no direct J/JAL entry or interior entry.
Its sole aligned pointer is ROM **0x234400 /VA0x8008F940**, slot0 in
**D_8008F940**; the complete288-byte data owner remains exact. The registered
dispatcher is **func_151A7A90**. Its original11-word window
**0x151A7AF0..0x151A7B1C** loads this slot, passes the effect in A0, saves its
live T0 home, calls through T9, then consumes V0 with SLTIU/ANDI and restores
T0. **72 connected callback cases** prove return1 keeps the continuation flag
clear, while preserving memory and original/normalized literal state. The
whole larger dispatcher and unrestricted table-index domain are not claimed.

## Literal image and production

The predictor replaces only the308-byte body and its12-to308-byte extent.
New external references cause two GNU ld metadata reorderings, derived from
five unchanged frozen named definitions and their exact contiguous strings:

| Frozen order | Required order |
| --- | --- |
| D_800A1620, D_800A5920, D_800A1B70 | D_800A5920, D_800A1B70, D_800A1620 |
| D_800A1638, D_800A5E88 | D_800A5E88, D_800A1638 |

No symbol/string table is excluded or copied from the result. The complete
predicted ELF changes **271 bytes**:245 in body/extent and26 in those closed
metadata permutations. All **11 image corruption controls** reject header,
body, extent, protected data, each named definition and each string block.
All **6,052** disassembled entries retain their addresses; every other body
and extent is fixed. Protected data stays exact across **720 owners /189,088
bytes**, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production compiles only this owner, matches the complete prediction and
regenerates the identical progress CSV. The guard manifest preserves every
prior byte and appends exactly42 checked rows. Makefile/profile/table bindings
are unchanged. The existing full-ROM checksum failure (make all exit2) and
duplicate generated_12D630 recipe warning remain.

Both shared tools smoke checks are fresh; three unchanged helper regression
checks per copy are reused with exact fingerprints. The sibling tools'
**2,434** dirty paths remain fingerprinted and preserved. There are **106
frozen inputs**, including callback data, YAML and the existing point-helper
source. Baseline consumer `5de92a28e3caa7aa8a3d5b84a47bfe575e60e570`, tools
`31ece34ab052621e719f6205bb6c7de0f3d89b38`. Claude calls: **0**; local compiler,
dependency, execution and literal-image evidence resolve this target.

Accepted raw SHA256: `6ceed807820ea656282bf1ec64390e144efeb7b77b216d8a42829b0ce40a67a6`.
ELF SHA256: `b9fc7b73cedf6d81d9284e76cddb4cd136c9831049fde908734cacd125634c62`.
Binary SHA256: `385a727d5870ef7947b1fb2908842c787164a5ebc8877124666358d92f629c4a`.
Owner SHA256: `7ab9cd41d349ac5ba1152e4c067daa5e4eaf6cf186a513bafbe48fc85ead80aa`.
Guard CSV SHA256: `937a368e14e175c75d7577633990f4a3bba0a0f50040900924b9c948bc4d1850`.

## Resume boundary

Next: **func_15014F6C**, an uncredited randomized effect-packet initializer
in `conker/src/game_40490.c`. Original
`asm/nonmatchings/game_40490/func_15014F6C.s`;78words /312bytes, frame0x98,
VA15014F6C..150150A4 /ROM4241C..42554. Audit its existing prototype, callers
and actual Make profile before choosing the one-pointer/return1 interface.

Set source byte16hex bit2, snapshot the low byte of word20hex, source word1Chex
bit0, and the low/high halves of word18hex. Save the source in an84-byte
sparse packet at frameSP+44hex. Call func_150ADA20, then compute unsigned
remainder modulo(high+1) plus low, using the saved halves. Keep the original
DIVU/remainder and guarded break shape; high+1 is nonzero for a16-bit high.
Call func_150A8050(packet+10hex,source+0Chex word,source+10hex word,0) and
reload three signed16 position components after that helper for float conversion.

Submit func_15149130(300,-1,0x31,-1,0,0x2A,0x54,0xFF,0). A nonnull result gets
memcpy(result+28hex,packet,0x54). Return1 independently of allocation success.
Preserve the two tail bytes at packet50/51hex, untouched padding,48-byte
transform region, post-helper source rereads and saved S0/RA lifetime.
Complete all standard qualification, actual-Make, literal-image and production
gates before credit. Graphify currently gives placeholder/owner relationships.

Current receipts: `conker/build/game-attachment-position-delta-150EFA4C-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
preserves existing unscanned nodes with retention evidence; it is not a fresh
full-corpus extraction. Host Release remains frozen. The80% goal stays active.
