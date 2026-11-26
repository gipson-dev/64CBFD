# Optional emitter direct match - 2026-11-26

`func_150D728C` replaces its zero-return placeholder in
`conker/src/game/generated_1045D0.c`. All **98 body words emit directly from
semantic C**, with the original **264-byte frame**, all seven call bindings,
and **zero word guards**. The complete retail slot is **101 words**: the body
plus three literal zero alignment words. VA `0x150D728C..0x150D7414` body,
slot through `0x150D7420`; ROM `0x10473C..0x1048C4`, alignment through
`0x1048D0`. No instruction insertion/omission, frame patch, compiler-profile
change, Makefile change or guard-manifest change. Both complete padders agree,
and the owner's other routine `func_150D7120` and all pools remain unchanged.

Production: **4,704 / 5,528 (85.09%) total**, **4,031 / 4,855 (83.03%) Game**,
Init 492/492, Debugger 181/181, zero drift, 824 still different. One matching
credit, no conversion-row or denominator change, no caller/helper credit.
The active **90% goal requires 4,976 matches: 272 more**.

The recovered entry is `void func_150D728C(Rotation150D728C *rotation,
Position150D7120 *position, Position150D7120 *direction, u8 slot, s32 context)`.
It reuses the existing position view. The optional basis is nine signed
halfwords, size 18 and alignment 2. The measured packet views are a 100-byte
point packet, a 120-byte oriented packet, and their common 84-byte setup body.
Type and field names describe inferred roles; the original effect names
remain unknown. The source header now describes the recovered emitter
construction routines instead of labeling both definitions as placeholders.

Three precursor calls always occur in order. Position, direction and slot
are captured in S1/S0/S2; after callbacks, the optional pointer and fifth
context word are reloaded from incoming homes. If the optional basis exists,
the routine negates XYZ into the oriented packet, copies its 18-byte basis,
copies the position, calls setup, then submits `func_1514FBFC`. Otherwise it
negates XYZ into the point packet, calls setup, copies the position afterward,
then submits `func_1514FB98`. That position-copy order is observable when the
setup provider changes the input. The first full semantic screen was already
raw-exact; no scheduling or register guards were needed.

The point packet occupies SP+0x2C..0x8F and the oriented packet occupies
SP+0x90..0x107. S0/S1/S2/RA homes are SP+0x18/0x1C/0x20/0x24. Point radius
and body are SP+0x38/0x3C; oriented radius and body are SP+0xB0/0xB4. The
oriented basis copy uses four LWL/LWR and SWL/SWR pairs, then LHU/SH. Neither
packet is enlarged to fit the frame. The setup helper writes body offsets
0..7 and 0x14..0x50, plus the radius, preserving the 12-byte position at
0x08..0x13. The small packet retains three unwritten tail bytes. The large
packet retains those three plus two internal alignment bytes. Native tests
never read those three/five indeterminate bytes.

Validation:

- Raw C, normalized assembly and both complete original-ASM owner padders
  match every body word/binding. All three retail alignment words remain
  zero. The actual three-command Make recipe agrees under normal
  O2/g3/mips2/o32, with zero target diagnostics. The existing full-build
  duplicate-recipe warnings for generated_12D630, generated_F44D0 and
  generated_F5800 are preserved, with no warning suppression.
- Guest: 288 cases across five literal streams have equal complete private
  state and 156 fault-prefix quintuples. **97 of 98 body words execute**;
  `0x150D73A0` is the original unreachable duplicate LWC1 after an
  unconditional branch. It remains literal exact without an execution claim.
  Full seeded 100/120-byte packets, memory access order, calls, finite NEG.S
  operations and FCSR agree with an independent reference. Zero, signed zero,
  subnormal and finite extreme inputs, matrix alignments 0/2, mutable fields
  and guest-only incoming-home changes are included. Unaligned instructions
  reuse the existing DirectionOracle behavior. The original helper exposed
  an unsupported SRAV in the inherited fixture; a local implementation was
  added before passing. A later rebase exposed a Python entry default bound
  to the old address; resolving the entry at construction fixed the fixture.
  Neither correction changed the production C or a shared interpreter.
- The original **88-word `func_151BFC40`** is connected and pinned against
  ROM and frozen ELF. Its complete measured body/radius write footprint,
  signed player/mode conditions and live defaults agree with the independent
  helper model. Other precursors and factories remain opaque contracts.
  This does not establish hardware, gameplay or full backend acceptance.
- Two aligned plain JALs are identified: ROM `0x81D38` / VA `0x15054888`
  in `func_150538CC`, and ROM `0xAF3F0` / VA `0x15081F40` in
  `func_15081E78`. Both pass slot 255 and fifth argument 1. The first passes
  a null basis; the second passes record+0x44, +0x08 and +0x38. No aligned
  plain pointers were found; script/compressed/derived references are not
  excluded. The first caller has static ABI context only.
- The complete original **466-word/frame-944** second parent and its 68-byte
  jump table are pinned. Disabled-record and event-13 paths run from real
  entry to return in 128 cases per original/raw stream, with 64 connected
  children and 52 parent words. An independent complete reference on those
  paths checks signed counter-halfword increment, saved result reload and
  final return. Three child-result poisons preserve public effects through
  parent return. The parent is already byte-exact and receives no new credit.
  Other parent events/states and full first-caller execution are unqualified.
- Native: actual selected C in three translation units, 4,096 cases at each
  O0/O2/O3, strict aliasing, trapping UBSan and LTO type checks. Typed views
  assert all sizes and offsets. Providers observe **97/115 defined bytes**
  and exclude all three/five unwritten bytes. Whole initialized input arenas,
  canaries, calls and MXCSR agree, with both basis alignments, typed
  position/direction aliasing, live setup mutations and all four rounding
  modes for finite inputs. Native providers are noipa counterparts rather
  than original guest backends. Guest home experiments are not portable C
  claims. Nine semantic source negatives complete with comparison exit 42;
  no compile failure, signal or trap counts. The initial slot negative made
  its parameter unused; narrowing that negative to one call removed the
  compile warning before it counted.
- Both scoped padders expose **196 body-word and 14 binding corruptions**.
  Oversize input is marked as explicit overflow by the generic padder and
  rejected by the generated padder; it is never silently accepted as exact.
  Twenty GNU links and 100 guest runs cover independent jump regions. This
  target has only call relocations, so no HI16/LO16 carry-seam claim. Rebase
  runs use opaque providers; the connected original helper is checked only
  at retail addresses. All zero alignment tails are checked separately.
- Independent frozen old-C plus original-ASM prediction equals the complete
  private and production ELF: **306 changed bytes, zero exclusions**. All
  189,088 protected data bytes across 720 owners remain fixed. ELF SHA256:
  `e63798912f30b70a380a271c88f0e6e676ae8e630c7eb0e3fe6fe0e2805e9234`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 113.686 s | 5 fresh / 0 reused |
| preinstall-sibling | 98.066 s | 5 fresh / 0 reused |
| installed-primary | 72.593 s | 5 fresh / 0 reused |
| installed-sibling | 91.022 s | 5 fresh / 0 reused |

All 20 target tests are fresh, with matching primary/isolated-sibling source,
task, import, data and artifact fingerprints. Shared tools-check passes.
Unchanged broad suites are reused explicitly, not reported fresh. Frozen
inputs: 4077; copies: 3018. The separately
dirty real tools sibling is preserved. Tools commit:
`8c3c906153c5f29da322aa64ce33926997e5c90c`. Baseline consumer:
`60bee1e6c5620c98b0e7b4152ee662e102434da8`. Receipts:
`conker/build/game-optional-emitter-150d728c-private`.

Zero Claude calls and no subagents. The historical generated host target is
still a stub, with active host implementation unqualified. No host transfer,
build, launch, Release change or push. Scoped Graphify refresh audits both
owner definitions, preserves old IDs and qualification metadata, and observes
actual hook termination; no full-corpus extraction claim. README receives
aggregate rows/date only. Continue from the sealed N70 checkpoint toward 90%.
