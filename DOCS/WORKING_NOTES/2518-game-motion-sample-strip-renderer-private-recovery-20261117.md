# Motion-sample strip renderer private recovery - 2026-11-17

`func_151AD92C` has a complete private semantic C recovery and maintained
qualification. Selected v10 emits **458 words / frame 0x130**, against
**464 retail words / frame 0x130**. The renderer is **not installed or credited**:
ordered floating-point execution and private homes still differ. Production
retains its existing placeholder until the remaining matching gates pass.
The preceding update is [Note 2517](2517-game-motion-sample-strip-update-guarded-byte-match-20261117.md).

Accepted total remains **4,533 / 5,514 (82.21%)**, Game
**3,860 / 4,841 (79.74%)**, Init 492/492, Debugger 181/181, with zero drift.
The active 85% goal still needs **154 matches**. No aggregate README change is
needed for this private recovery; function details stay in this note.

## Retail behavior and recovered interface

Owner `conker/src/game/generated_1D92F0.c`, VA 151AD92C..151AE06C,
ROM 1DADDC..1DB51C, 1,856 bytes. Literal 52-byte descriptors for classes
0x2F and 0x4E register this callback at +8; both have layer byte +0x30 equal1.
The actual interface is `Gfx *func_151AD92C(Gfx *output, u8 *record, s32 viewport)`.
The caller sign-extends a viewport halfword into its third full argument word.
The callback preserves that complete incoming word at home+8, and returns the
advanced display-list pointer. It does not consume the viewport value.

The existing 88-byte strip record, 24-byte sample and 12-byte texture views
are reused without changing shared headers. Texture/count loads use unsigned
halfword/byte widths; texture width and height are unsigned halfwords.
The raw count and texture dimensions are captured before the texture provider.

For each bounded sample, the renderer computes two perpendicular bases from
the next-point tangent. The final tangent is (0,1,0). It writes four vertices'
XYZ halfwords, preserving flags, UVs and colors. Retail's first zero-length
fallback is deliberately **(100,0,0)** before scaling by4; the second is
**(1,0,1)**. Every vertex access reloads the current vertex pointer and bank.

SDK macros emit geometry mode, texture enable and pipe sync. The texture
submission is the actual **eleven-word** `func_15094FE8` interface, ending in
256,256,62; it contains no floating-point arguments. Its texture argument is
reloaded immediately before the call. Afterwards the renderer reloads render
mode, bank and vertex pointer while retaining count/dimensions. Segment output
loads eight vertices, emits the eight side triangles, updates two texture
coordinates and adds two cap triangles on the first segment. Width/UV packing
retains wrapped unsigned 32-bit shifts. Empty strips still submit setup state.

The alternate source at `Another Source/CBFD-Recompiled/conker/conker/src/game/game_1D92F0.c`
was inspected read-only. Wrong-width loads, pointer/float reinterpretations and
a malformed thirteen-argument helper call reject that draft as a ready donor.
The private reconstruction follows the complete retail routine and SDK macros.

## Fresh focused qualification

All **five maintained tests pass in both tools configurations**, with no skips:
88.372s primary and 92.601s sibling/overlay, including input/import recording.
The sibling's 2,434 dirty paths and all 339 present scoped dependencies remain
unchanged. Actual imports are retained: primary319 distinct files; overlay run
321 distinct files, with row origins seven overlay, 301 sibling and fifteen
primary fallbacks. The overlay's seven rows include its two package adapters.

- Full owner IDO5.3 O2/g3 compilation pins the selected raw hash and bindings.
  All **32 other functions and normalized pools** agree with the frozen owner.
  Sixteen bounded source experiments remain in the ignored packet; v10's
  removal of dead/redundant scalar live ranges recovers the 304-byte frame.
- **544 finite cases per retail/raw stream** compare every declared public
  byte, all eleven provider arguments, exact return and saved GPR/FPR state.
  They cover counts0/1/2/3/19/20, both banks/textures, tangent degeneracies,
  unsigned dimensions0/1/32/65535, complete incoming viewport words and mutable
  provider behavior. Coverage is **464/464 retail and 457/458 raw words**.
- The complete **348-word retail caller** and **47-word original selector**
  execute 64 literal-descriptor cases per stream, plus four separately labeled
  altered-layer fixtures. Caller coverage is323/348; selector coverage13/47
  covers the two actual class groups. The unvisited optional pre/post callbacks
  are null in both literal descriptors. Signed viewport forwarding, next-list
  retention, return consumption and display-list-budget rollback agree. A wrong
  callback record pointer is rejected.
- Exact selected C and SDK macros run natively at **O0/O2/O3**, using544 cases,
  strict aliasing and undefined-behavior traps. Full record/sample/vertex,
  texture-table and both display-list arenas are checked. Only actual pointer
  fields/commands are canonicalized; numeric graphics words retain all bits.
  Four additional native runs reject wrong zero-length fallback, texture shift,
  helper tail argument or reloaded post-provider count.
- Five retail-instruction controls reject wrong fallback, shift, helper tail,
  viewport-store width or signed texture height. The private oracle's missing
  XOR instruction is implemented and checked on four operand pairs, including
  writes to the architectural zero register.

The matrix uses mapped disjoint bounded objects and finite float inputs with
one conforming opaque texture provider. It is not a proof for arbitrary aliases,
all FP inputs/status, faults, hardware or host gameplay.

## Measured matching frontier

All finite public results agree, but only the **20 empty cases** have the same
ordered FP trace. The retail matrix contains **306,846 FP observations**; the
first nonempty mismatch is observation16, a retail truncation versus an early
independent C addition. Complete mapped RAM and provider-frame bytes agree in
**0/544 cases**. Equal frame size therefore does not establish private identity.

The next work stays on this renderer:

- [x] Recover the complete body, types, full helper ABI and actual caller.
- [x] Qualify owner neighbors, finite public guest behavior and native SDK C.
- [ ] Recover/relate ordered FP operations, private homes and loop-live roles.
- [ ] Prove any normalization, then qualify both real padders, independent
  symbol rebases, corruption controls and normalized guest/caller streams.
- [ ] Run actual Make and strict independent whole-image prediction before
  installation; audit all addresses/bodies/protected bytes, recount and commit.

No new retail guards, compiler profiles or production objects are installed.
All **1,525 frozen inputs** are unchanged. Production ELF SHA256 stays
`9a3fca4a18c45119a77ad987895ba93c8f600ab46acbad5513147499567074b3`.
Selected raw SHA256:
`50f6c44ae94b1ee17226e3e1c0666b518d1cb119641fd7fa70ae583daaae15eb`.

Run `python3 -m unittest tools.tests.test_game_strip_draw_151ad92c_private -v`
under prepared WSL with a fresh owned `CBFD_STRIP_DRAW_PRIVATE_WORK` path.
Immutable baseline, experiments, native vectors, full reports and actual imports
remain under ignored `conker/build/game-next-151ad92c-private/`; the paired
maintained-suite receipts are in `semantic-qualified/`.

Both sibling projects were considered: `64CBFD Tools` is qualified through an
overlay without modifying its dirty checkout. The local `64CBFDOGL` directory
has no source checkout to apply this private recovery to; its frozen Release
artifacts and saves remain untouched. No Claude invocation was needed.

The native Graphify update refuses a smaller replacement graph and retains
the current graph. A scoped AST merge covers the five new Python files,
preserves all 64,651 prior IDs and adds an explicit recovery-to-function
reference. This is a scoped refresh, not full-corpus extraction; commit-hook
process observations and final retention receipts stay with the packet.
