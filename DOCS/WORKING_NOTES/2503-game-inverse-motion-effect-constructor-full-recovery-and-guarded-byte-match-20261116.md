# Inverse-motion effect constructor recovery and guarded byte match - 2026-11-16

`void func_151A4638(f32 x, f32 y, f32 z, f32 vx, f32 vy, f32 vz, u8 *owner)`
replaces the zero-return placeholder with the complete effect constructor.
Its **129-word retail slot / frame 0xA8** is restored by **37 expected-word
guards**, folding one generated private descriptor address into stack accesses.
Raw C emits 130 words; there are **no insertions and one address omission**.
VA 151A4638..151A483C, ROM 1D1AE8..1D1CEC. This is a guarded C match.

Production total **4,525 / 5,514 (82.06%)**, Game **3,852 / 4,841 (79.57%)**,
Init 492/492, Debugger 181/181; zero drift, 989 different, **162** more matches
to the active 85% goal. Conversion stays 5,514/6,048 (91.17%), 86.19% of bytes.

## Actual interface and complete descriptor

The sole aligned function-pointer literal is `D_80089A70[1]`,
VA 80089A74 / ROM 22E534. Original **261-word / frame 0xB8** parent
`func_151342BC` dispatches at 151345FC. It supplies F12/F14=x/y,
A2/A3=z/vx bits, SP+0x10/+0x14=vy/vz bits, and SP+0x18=owner. It ignores the
callback result and continues decrementing its pending-emission counter.
The entire original parent remains byte-identical in production.

The initial default `rg` search omitted ignored nonmatching assembly. A scan
of original Game instructions found the table address materialization at
15134530, leading to `asm/nonmatchings/game_161520/func_151342BC.s`.
The caller is present; a default text-search absence was not treated as proof.

The local descriptor owns **all 112 bytes** at incoming SP-112, including its
reserved 12-byte tail. The original `func_15130374` wrapper forwards to
`func_15130280`, which copies all 0x70 bytes. The first 100-byte draft had the
right instruction count but frame 0x98 and an undersized C object; it is
rejected. The corrected type uses explicit reserved ranges at 0x3C..0x47,
0x5C..0x5F and 0x64..0x6F. **84 bytes are defined, 28 stay indeterminate in C.**
The separate six-short parameter array is at incoming SP-128.

The constructor initializes its header/state bytes, derives an initial counter
15..19 using an unsigned RNG remainder, and initializes both scalar values
from `sample*50+500`. Position is copied from the first three arguments.
Velocity is `-inputComponent * (D_800A8D60 * D_800BE9A8)`;
the protected coefficient is 0x3DB22D0E. Two further RNG results independently
set flag bits 0x40 and 0x80. Unknown field meanings keep offset-based names.
The counter/scalar names agree with the existing effect-update record views.

The owner channel at +0xC is read after the RNG calls, immediately before
`func_15130374(&packet,0,12,channel,1)`. Allocation failure skips the copy.
Success copies all six signed parameters `[16,15,13,19,17,-24]` to result+0xA8.
No shared ABI/header, Makefile or compiler-profile change is introduced.

## Ordered semantics and fresh qualification

Two annotated volatile views constrain existing private descriptor stores to
the observed retail FP order. They express the qualified emitted ordering;
they do not establish the spelling of the unavailable original C. No physical
register bindings or dummy stack padding are used. Raw SHA256:
`4c78d618c868e0cd54c60e9a4c5d0b195685957387c6480938d8d5774972ed25`.

An earlier 129-word/frame-0xA8 draft agrees on sampled public output but changes
FP order in all 2,112 guest cases. It remains rejected. The selected source
passes the complete ordered relation rather than relying on shape/output alone.

All **six maintained tests** pass in primary tools, the isolated sibling overlay
and installed production at identical ten-file fingerprints:

- **Eight symbolic paths**, every 130 raw / 129 retail instruction, all nine
  ordered FP operations/operands/FCSR transitions, complete return registers,
  and all 196 private-frame/incoming-home bytes at each call and return.
  Both private argument ranges and arbitrary packet mutation are qualified.
  Ten semantic corruptions reject without fingerprint guards; independent
  T0/T1 allocation passes. The unsigned constant divisor is nonzero.
- Independent guest model: **2,112 cases per retail/raw/guarded stream**,
  full initialized public bytes, provider calls, all 112 descriptor bytes and
  12 parameter bytes, private homes, return word and ordered FP. Cases include
  channel-byte coverage, signed/high RNG results, both stack phases, allocation
  failure, output/owner aliasing and early/late provider mutations. No FP-order
  disagreements remain. A phase-16 fixture was rejected by the inherited
  machine's explicit 0/8 phase contract; the corrected fixture uses 0/8.
- Native32 C: **2,112 cases each at O0/O2**, UB traps and strict aliasing.
  Only the 84 defined descriptor bytes are observed/mutated; all 28
  indeterminate bytes are excluded from native observations. Both public
  192-byte objects remain completely checked. Only successful typed payload
  copies undergo endian conversion. Eight source errors compile and exit 3.
- **192 connected cases per stream** execute the actual 18-word wrapper,
  61-word factory and 11-word memcpy; 67 helper words are visited for the
  constructor's mode-zero/NULL-vector domain. Allocation arguments, failure,
  all 112 copied descriptor bytes, all 12 payload bytes, aliasing and late
  owner/global changes agree. Other factory modes and its optional-vector
  path are outside this call's contract; the deep allocator is opaque.
- **576 original-caller-window cases per stream**, all 64 words at
  15134528..15134628: computed seven-argument forwarding, repeated emissions,
  counter gates, no-op callback and ignored return, with opaque and connected
  factories. A synthetic NULL table fixture checks the lookup guard and is
  explicitly separate from retail data. The parent's upstream gates and
  transforms are outside this bounded window; full-parent gameplay is untested.
- Both real whole-owner padders retain 22 neighbors and pools. All **130 raw
  word + ten binding corruptions**, two stale actual CSV controls, and three
  independent GNU rebases across HI/LO carries are checked. The previous CSV
  bytes remain an exact prefix. The omitted word is solely
  `addiu v0,sp,0x38`; its two consumers become equivalent SP-relative stores.

The symbolic scope is normal mapped/aligned public RAM with a private disjoint
stack and bounded o32 providers. It preserves ordered FP without assuming traps
disabled; arbitrary memory fault prefixes and general portable C aliasing are
not claimed. Native fixtures are finite and do not emulate hardware FCSR.
The guarded instruction stream separately has literal retail identity.

## Actual production and evidence

The accepted predecessor is consumer `6df8f54c` / tools `b31cfa9d`.
All 1,321 predecessor inputs were verified through its four-entry adoption
plan before an immutable 1,324-input initial freeze and supplemental caller
snapshot. The maintained **1,335-input** freeze changes exactly source, guard
CSV, owner object and ELF; **1,331 inputs stay unchanged**. Earlier candidates,
rejected fixtures and snapshots remain preserved.

Actual Make shadow and production build source through the existing profile;
no prebuilt object is installed. Every address and all other 6,050 bodies are
unchanged. Only one of 698 objects changes, preserving 22 neighbors/pools.
The complete ELF equals its independent prediction: **415
changed bytes / zero exclusions**. All 20,289 named definitions agree except
target size; metadata permutations are accounted explicitly. Symbol value/name,
protected-byte and target-word corruptions reject. Conversion CSV is unchanged.
All **189,088 protected bytes / 720 owners** remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production ELF SHA256: `9b68ca2cd4136aae6c99e98c9a417b0fa14a51d34da44b5c310e9a0ab21b2abb`.

Reproduce prepared qualification:
`python3 -m unittest tools.tests.test_game_inverse_motion_151a4638_recovery -v`.
Receipts: `conker/build/game-next-151a4638-private/adoption/`.
The sibling's 2,434 dirty paths and scoped dependencies stay unchanged; actual
overlay/sibling/primary import origins are sealed. Root README changes only
Total/Game aggregate rows. Graphify uses a retained-ID scoped AST refresh,
with no full-corpus extraction claim. Zero Claude calls, no dependency upgrade,
host Release/save change or push. Commit tools before consumer source/guard/pin/docs.
Next inspect `func_151A4A38` from the actual unmatched list; the 85% goal stays active.
