# Random sprite scatter direct match - 2026-11-26

`func_15179B14` replaces the zero-return placeholder in
`conker/src/game/generated_1A6360.c`. **All 103 words / 412 bytes and nine
binding positions emit directly from C**, with the original **272-byte frame
and zero guards**. VA `0x15179B14..0x15179CB0`, ROM
`0x1A6FC4..0x1A7160`; no alignment tail, insertions, omissions, compiler-profile,
Makefile or guard-CSV change. All eight raw/padded owner neighbors and pools
stay fixed, including five exported retail jump labels.

Production: **4,701 / 5,528 (85.04%) total**, **4,028 / 4,855 (82.97%) Game**,
Init 492/492, Debugger 181/181, zero drift, 827 still different. One matching
credit, no conversion-row or denominator change, and no caller/helper credit.
The active **90% goal requires 4,976 matches: 275 more**.

The recovered interface is `void func_15179B14(s32 count)`. It captures the
signed 16-bit origin coordinates from `D_800DD438[0]` and `[2]` before testing the
count. For a positive count it captures the mutable no-ground sentinel once,
then draws two signed random values per iteration, takes their signed
remainders modulo 500, and adds the captured origins. It calls the height
query as `(x, 10000, z, 0)`, converts its signed 32-bit result to float under the
current rounding mode, and compares that value to the captured sentinel.
The original scalar at VA 0x800A7208 / ROM 0x24BCC8 is -10000.0f, bits C61C4000;
ROM and the frozen ELF agree. Alternate finite sentinels are test controls,
not a claim that the production scalar has another value.

On an accepted height, the routine fills the measured fields of the existing
168-byte selected-vertex sprite layout: value80=0, value8A=128, truncated
16-bit coordinates, lifetime/remaining=25, initialHeight=0, tag=14,
textureIndex=18, flags=0x9804, mode=0. It initializes the palette with four
255 bytes, then calls the sprite factory with channel 255 and context 0. The helper receives the
same descriptor pointer across iterations. Local type/field names describe
measured roles; original game names and the effect's visual identity remain
unknown. No additional initialization of retained descriptor bytes is added.

The first fitting source already had 103 words, but its frame was 264 instead
of 272. Keeping the captured signed 16-bit global values in signed 32-bit working locals
`originX` and `originZ` restores the complete retail frame naturally. Either
single promoted working local also matches; both promoted locals are selected
for consistent coordinate arithmetic. Values remain sign-extended from the
same global halfwords. No synthetic local, volatile access, alignment trick,
physical register binding, frame patch or compiler-profile change is used.
The saved F20 pair is at SP+0x18, saved S0..S7/RA at SP+0x24..0x44, and the
descriptor occupies SP+0x48..0xEF in the original 0x110 frame.

The aligned ROM census finds one plain JAL at ROM 0x1A6958 / VA 0x151794A8,
inside `func_15179008`, and no aligned plain pointer. That census does not
exclude compressed, script-driven or derived references. The complete
original parent is 304 words/frame 64. Its frozen production ELF slot is still
different from retail; this recovery does not install or credit the parent.
Its idle state 0 and default modes 5/255 are privately qualified from normal
entry to return. The origin-update helper remains opaque and may change the
signed count before the parent reloads it and divides by 30. The child resumes
at 0x151794B0, and its return register is ignored. Other parent FSM states,
reset/RNG branches and the origin-update implementation are unqualified.

Validation:

- Both complete owner padders use the full original `1A6360.s` boundaries
  and produce identical whole objects. This generated owner needs no
  layout-only shim. All eight neighbors/pools and five exported jump labels
  stay fixed. The actual three-command Make recipe matches that complete
  object under the unchanged O2/g3/mips2/o32 profile, with zero diagnostics.
  The full build retains its existing duplicate-recipe Make warnings for
  generated_12D630, generated_F44D0 and generated_F5800; the Makefile is unchanged.
- Guest: 608 cases per five literal streams, all 103 words preserved and 95
  exercised. A separate instruction proof pins S3=500, its preservation
  through calls, and both nonzero/non-minus-one guard branches. The eight
  unreachable compiler divide-break words at offsets 74,84,88,8C,AC,BC,C0,C4
  (hex) remain present; no execution coverage is claimed for those words.
  Full private memory, GPR/FPR, HI/LO, FCSR, PC/delay state, ordered trace and
  81 fault-prefix quintuples agree. An independent semantic reference compares
  public memory, call order and every one of the 168 descriptor bytes.
  Signed random extremes, short-origin limits, nonpositive/positive counts,
  all four rounding modes, signed 32-bit conversion boundaries, existing and
  provider FP flags, sentinel/origin mutations, allocation failure and
  descriptor mutations are included. Finite conversion/compare modeling
  does not qualify NaNs, enabled hardware FP traps or hardware exception
  delivery. Incoming frame/fault experiments are guest-only evidence.
- Connected guest checks run the original 105-word palette and the
  original 28-word factory with opaque allocator/copy contracts. Palette UV
  dimensions include 0,47/31,65535. The copy contract compares all 168 bytes;
  it does not claim execution of the original bcopy/allocator. The random
  provider remains opaque. The 215-word height-query slot remains different
  from retail and its implementation is not qualified by this routine.
- Complete original parent execution on the bounded idle/default paths:
  432 cases per original/raw stream, 288 connected children each; 52 of 304
  parent instructions exercised. Original ASM/ROM and the parent jump-table
  bytes are pinned. An independent bounded-parent reference and complete
  private literal states agree. Origin/count mutation verifies the late
  count reload and signed division by 30. Three child return poisons
  (0,FFFFFFFF,13579BDF) leave public effects unchanged through parent return,
  confirming the void interface. This is not all-state parent coverage.
- Native: actual selected C in three translation units, 4,096 cases at
  O0/O2/O3, strict aliasing, UBSan traps, LTO type checks and strict SSE FP
  options. Typed Vtx/descriptor views assert the measured layout. The
  provider observes 109 initially defined descriptor bytes; the other 59
  bytes are never read before definition. A palette mutation defines four
  retained84 bytes, which are then compared as well. Native factory output
  copies only defined fields into initialized arenas; it does not claim
  portable copying or observation of unknown source bytes. Full initialized
  output arenas, canaries, metadata, calls, globals and MXCSR agree. Guest
  tests separately preserve and compare the full 168-byte packet. Ten
  semantic controls finish with comparison exit 42, with no compile failure,
  signal or trap counted as rejection. Native noipa providers are contracts,
  not execution of original backend implementations.
- Both scoped padders expose 206 word and 18 binding corruptions. Twenty
  independent GNU links and 100 guest rebases cover jump regions and signed
  HI/LO carry seams. Rebase tests use opaque helper contracts; connected
  original helpers are tested at their retail addresses. Generic oversize
  remains visibly marked and the generated padder rejects it. Zero guards
  mask instruction or binding changes.
- Independent frozen old-C plus original-ASM prediction equals the complete
  private and production ELF: **300 changed bytes, zero exclusions**. All
  189,088 protected data bytes across 720 owners stay fixed. ELF SHA256:
  `d65997092cd8ca58566b5bd0a6c13344926af276362413bad38004141908c82b`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 190.268 s | 5 fresh / 0 reused |
| preinstall-sibling | 169.937 s | 5 fresh / 0 reused |
| installed-primary | 182.981 s | 5 fresh / 0 reused |
| installed-sibling | 206.112 s | 5 fresh / 0 reused |

All 20 packaged target tests are fresh, with matching primary/isolated-sibling
task, source, import and data fingerprints. Shared tools-check passes. Prior
unchanged broad suites are reused explicitly, not reported as fresh. Frozen
inputs: 4040; copies: 2980. The separately
dirty real tools sibling remains intact. Tools commit:
`4669c2af71fe451c5a800514ae603d65b261d53e`. Baseline consumer:
`a772645a07a665f94df7386f09b745bcc66dc854`. Receipts:
`conker/build/game-random-sprite-scatter-15179b14-private`.

Zero Claude calls or subagents: the origin-width screen settled the frame
locally. The historical generated host target is an empty stub; its active
implementation remains unqualified. No host transfer, build, launch, Release
change, push, gameplay or hardware acceptance. Scoped Graphify refresh audits
all nine owner definitions, retains old IDs/qualification metadata and
observes actual hook termination; no full-corpus extraction claim. README
receives aggregate rows/date only. Continue toward 90% from this sealed
checkpoint with another qualified unmatched Game routine.
