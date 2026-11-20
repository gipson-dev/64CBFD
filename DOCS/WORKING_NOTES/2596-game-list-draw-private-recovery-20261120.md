# Note 2596: Private flare draw recovery

Date: 2026-11-20. Consumer baseline `9b9a40a499b85a01701e16600d1c64141f9dfb4d`;
tools baseline `15f923aae01392450f9e2c8a393e741e364d44c1`.
Qualified recovery tools commit: `960493de889983dc907fafcea04ae69725df3e66`.

`func_1517E4A8` now has a complete **private, uncredited** semantic C recovery.
The candidate naturally emits **361 words / frame 184**, matching retail's
length and frame, but retains **162 positional linked word differences**.
It is not installed. The production function remains its existing placeholder;
no guard rows, compiler profile, production source or matching counts change.

The verified production checkpoint remains **4,580 / 5,528 (82.85%)** total,
**3,907 / 4,855 (80.47%)** Game, zero address drift and 948 still different.
Init 492/492 and Debugger 181/181 remain exact. **119 more** are needed for
85% at this denominator. The goal stays active. Root README stays byte-identical;
this detailed recovery belongs in this note and the concise current indexes.

## Complete routine and interface

Owner `conker/src/game/generated_1AB530.c`, VA `0x1517E4A8..0x1517EA4C`, ROM
`0x1AB958..0x1ABEFC`, 361 words/1,444 bytes. The sole aligned-ROM direct JAL
is `0x1AB8F8`, from the restored list renderer; no aligned literal pointer is
found. Computed callers remain unexcluded. The private declaration is
`Gfx *(Gfx *, ListRecord1AB530 *, s32 group, s32 count, s32 falloff,
s32 strength, u8 *intensity)`. Its typed seven-argument caller preserves the
raw code, bindings and pools of **all seven neighboring owner functions**.

The routine captures centered screen coordinates, optionally smooths an
intensity byte toward a distance-based target in steps of five frame ticks,
and smooths the signed record brightness at +0x28 in steps of ten ticks.
It retains the distance, strength, viewport and absolute-coordinate gates.
Eligible records set RGB to 255 and initialize the packet's descriptor and
animation/flip bytes. Even nonpositive sprite counts retain this setup path.

If D_800DDD60 is clear, the routine calls `func_1517EA4C`, then the ten-argument
texture setup `func_150950D4`, then sets the flag. It captures alpha from the
post-setup record fields and iterates the selected seven-byte palette row.
Each iteration recomputes sprite coordinates and scaled extents, submits the
packet through `func_15095A48`, and appends an SDK pipe-sync command.
The original 16-byte palette is checked directly against ROM.

The complete compatible packet is **20 bytes**, with signed extents at +6/+8,
alpha/animation/flip bytes at +0xA..+0xD, and a descriptor pointer at +0x10.
Its coordinate prefix and padding are not initialized by retail and are not
read by the exercised provider contract. Mutable initialized fields persist
between calls. No speculative memset or zero initialization was added.

## Typed return repair and code-generation screens

The existing `func_15095A48` C wrapper is declared void while retail returns
its nested draw cursor in V0. The private repair declares
`Gfx *(Gfx *, ProjectedPacket95B08 *, f32, f32)` and explicitly returns the
address from `func_15095A90`, preserving the original 4096.0f and four zero
arguments. **All 19 raw helper-owner functions/bindings/pools and its entire
padded object remain identical**. Both compilations emit no diagnostics.
The repair is also private until the draw routine's full adoption gates pass.

The first complete draft emitted 365 words/frame 200. Moving loop locals and
recovering the original operation order obtained 361 words/frame 200. Removing
redundant scalar lifetimes recovered 361 words/frame 184. A 361-word/frame-192
screen has fewer positional differences (76) but retains the wrong frame.
The selected candidate uses the existing O2/g3 profile and the SDK's documented
local `fabsf` intrinsic declaration; no Makefile or profile change is proposed.

Selected raw SHA-256:
`2353a48952e6704d107ac718cd215cb7c5d88b7fa70ff864249ef962434a0a15`.
The exact binding map is frozen with the full semantic body and private helper
repair in the version-controlled recovery manifest. No word-normalization
table is generated from these measurements.

## Fresh focused evidence and limits

Five tests pass in both tools configurations. All **311 imported
Python fingerprints** agree. The isolated overlay has **1067 files**:
347 matching sibling files,
714 primary fallbacks, five task files and
one bootstrap. This is a hybrid overlay. The actual dirty sibling retains its
HEAD, exact status and **351 dependency hashes**.

- Guest/reference: **1,104 cases**, **953 logical helper calls**, with the
  complete **24-word retail initialization routine and 18-word draw wrapper
  connected**. The texture setup and nested draw core use bounded providers.
  Public memory, helper observations/arguments and returned cursors agree.
  Intensity can be null, separate, or alias either state byte or the enable byte.
  Providers mutate coordinates, dimensions, frame step, scales, brightness,
  colors, descriptor and animation fields; cursor changes are also covered.
- Both streams cover **347 of 361 words**. The remaining 14 are unvisited in
  this finite corpus, not established unreachable. Both use the same passed
  packet address at incoming SP-60. At all **953 call boundaries**, all 212
  private/incoming bytes agree except the two unpassed counter homes. Complete
  final guest memory agrees in 921 cases; the other 183 differ only in those
  same eight bytes. Saved GPR/FPR/SP/RA restoration is checked by the oracle.
- The selected raw counter spills/reloads at source words **302/338**, private
  **SP+0xA0**; retail uses **SP+0xB0** at the same words. Neither opposite home
  is otherwise accessed. The only non-frame SP-derived address is the packet
  at SP+0x7C. This identifies a potential closed home rename; it is not yet a
  complete normalization or unbounded proof.
- Three effective instruction controls reject a wrong distance cutoff, alpha
  home and strength gate. Native SDK32 O0/O2/O3 each pass **1,104 cases** with
  compatible objects, strict aliasing and UBSan, including the typed wrapper.
  Three source controls reject a wrong cutoff, alpha assignment and brightness
  numerator. No provider reads the packet's uninitialized coordinate prefix.
- Both padders agree for both proposed owners. Actual Make executes **three
  commands per owner** using its natural existing C recipe and reproduces the
  expected complete objects. Shared tools checks pass. The prior installed
  14-test checkpoint is reused through unchanged source/profile/input hashes;
  those neighbor suites are not described as fresh runs here.

The finite normal-execution domain uses valid disjoint objects, finite bounded
coordinates, widths 320/640/1280, heights 240/480/720, frame steps 0/1/2/30,
palette groups 0/1, counts -1/0/1/3/7, falloffs 1/30 and strengths -1/0/1/255/256.
Signed state extremes, enable values 0/1/2/255 and varied intensity bytes are
included. This is not
an unbounded integer/FCSR/fault-prefix proof, full downstream renderer test or
hardware/gameplay acceptance.

All **2156 frozen inputs** are audited against the explicit task
plan. The live production ELF, conversion CSV, both source owners and root
README remain byte-identical. There is no candidate whole-image prediction,
production build or new matching credit. Graphify records a private recovery
with matching credit zero and retains old IDs and qualification metadata.

Reproduce from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_list_draw_1517e4a8_recovery -v
```

## Continue toward matching

1. Derive the closed source-origin/register/schedule relation for the selected
   361-word stream. The measured opcode inventory includes one extra LBU and
   truncation, one fewer SLT and NOP, and branch/likely changes. Account for
   every operation and the counter home rename rather than replacing a body.
2. Prove the prefix and loop relation, including private packet/counter lifetime,
   calls, floating behavior and effective semantic controls. Retain explicit
   domain/observability limits and resolve all unvisited paths.
3. Qualify expected-word/binding guards, independent rebases, full object and
   image prediction, then production, installed tests and a fresh recount.
   Extend older fixture compatibility only for exact qualified owner/guard
   snapshots; preserve their immutable historical archives.
