# View Point Projection Direct Match

Date: 2026-10-16. Consumer predecessor **7da31b87**, tools predecessor
**e72f87b**. Complete the adjacent recovery queued in
[Note 1455](1455-view-scissor-setup-direct-match-20261016.md).

## Direct C Recovery

Restore func_1501A764 in conker/src/game_476D0.c: **87 words / 348 bytes**, VA
**0x1501A764..0x1501A8C0**, ROM **0x47C14..0x47D70**. The normal **O2/g3**
profile emits every retail word directly, with the original **0x38 frame**,
RA home at **SP+0x24**, four pointed float locals at **SP+0x34 / +0x30 / +0x2C /
+0x28**, arithmetic order and live global reloads. **No new guards, padding,
private pools or compiler-profile/Makefile changes.**

```c
void func_1501A764(s16 view, f32 x, f32 y, f32 z,
                  f32 *outX, f32 *outY, f32 *outZ);
```

The old zero-return stub already counted as C; its incorrect ten-argument
transform declaration and commented-out draft are removed. Preserve the actual
seven-word wrapper interface, signed low-halfword view and three pointed
results. The view's 64-byte matrix transforms XYZ into four local components.
Compute the reciprocal W once, then emit X, inverted Y and scaled depth in
retail order. Reload D_800BE628 after each output store, and load the unsigned
D_800BE9C0 page only after the first two stores. Output pointers can alias
dimensions, origins, viewport halfwords, the base word or the page byte.

Name proven fields in the existing 0x180-byte ViewProjection476D0 without
changing its size or other offsets: originX **+0x34**, originY **+0x38**, and
the two real SDK Vp entries starting **+0x40**. Their signed depth vscale[2]
and vtrans[2] are **+0x44 / +0x4C**, plus the 0x10-byte page stride. Do not use
the old struct140 draft's misleading 32-bit depth members.

The alternate-source owner still has GLOBAL_ASM for this routine, followed by
the same unfinished draft. No external C body is claimed imported or verified.
Its pinned reference fingerprint remains unchanged.

## Real Transform Tail

The corrected owner-local helper declaration has **eight word arguments**:
matrix A0, XYZ words A1/A2/A3, then four stack output pointers. IDO also emits
the retail F12/F14 mirrors before the call; tests inspect them explicitly.
The actual handwritten helper consumes the word arguments, not the old
draft's imagined two leading floating parameters.

Connect all **58 original words**, independently GNU-assembled and compared
with both ROM and the frozen consumer ELF:

- func_150A7A00: **5 words**, saves the wrapper return address in T9 and
  redirects RA to the continuation before jumping to the matrix leaf.
- func_150A7960: **40 words**, computes the first three components while
  leaving A0 and F0/F2/F4 live for the continuation.
- func_150A7A14: **13 words**, computes W and returns through T9.

No opaque helper callback substitutes for this chain in guest tests. The
native adapter is separately compiled semantic C, not a claim that the
register-specific handwritten chain has been converted.

## Source Fitting

The initial typed body is **88 words / frame 0x40 / 29 differences**. Keeping
named record/viewport pointer temporaries inflates the frame; register hints
do not fix it. Inline all record accesses to recover **87 / 0x38**, initially
with 13 FPR/operand differences. The recovered X origin-first expression
reduces these to five, and the depth product-before-translation expression
recovers every remaining word directly. Reassociation or reversed depth
operands are not equivalent matching evidence.

Preserve the initial screens under conker/build/game-view-point-projection/.
Canonical immutable inputs and qualification are under
conker/build/game-view-point-projection-match/. All ten other normal-profile
owner functions retain their raw words and bindings. Revalidate the previous
func_1501A39C no-unroll override fingerprint and keep its selection unchanged.
All target compiler diagnostics are empty.

## Fresh Qualification

The final pre-install suite passes **eight tests in 22.300s**. After the normal
build, **all 11 final tests pass in 66.018s**:

```sh
python3 -m tools.experiments.game_view_point_projection --prelink
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_view_point_projection \
    tools.tests.test_game_view_point_projection_installed -v
make -C conker match-progress NON_MATCHING=1
```

- **1,488 three-way guest cases** compare retail, raw C and padded C against
  an independently grouped float32 reference at two stack phases. Compare
  complete public/private memory, registers, ordered accesses, real helper
  pointers and mirrors. Visit all **87 root and 58 helper words** dynamically.
- Include signed/full-word view encodings, unsigned pages through 255, signed
  depth halfwords, rounding-sensitive matrices, zero/negative-zero W,
  nonfinite reciprocals and live output/base/page aliases. These bounded
  float32 models do not emulate hardware FCSR, NaN payload policy or exceptions.
- **348 native32 cases each at O2 and O0**, UBSan enabled, no -fwrapv. Use the
  real SDK Vp type and recovered owner type/body, a typed seven-word caller
  and separate eight-word semantic matrix adapter. Check proven offsets and
  all **784 record/output words plus canaries**, base and page. Compare NaN
  class only for changed native floating outputs; other words remain literal.
  Base/page and halfword-output alias cases are guest-only, not portable
  little-endian native-C claims.
- Six compiled native negatives exit **21** for actual output differences:
  wrong matrix stride, wrong view record, missing reciprocal, unsigned depth,
  wrong depth scale and swapped helper outputs. Cached-base/page guest
  controls produce **two / one** measured output mismatches. Compile failure,
  signal, unmapped access or sanitizer trap never counts as an effective control.
- Independently assemble complete original callers **func_1516CC58 (285
  words)**, **func_1512AD54 (235)** and **func_151742EC (193)** against ROM.
  **72 actual three-way cut cases** qualify XYZ word arguments, stack outputs,
  real delay-slot setup, third-caller sign extension and output consumption
  by two real post-call load sequences. Full caller/gameplay execution is not
  claimed.
- **672 three-way connected memory-fault prefixes** cover all executed root,
  matrix, tail and continuation accesses in six fixtures/two phases. Literal
  private state is compared before the declared access, not an emulated
  hardware exception.
- Reject all **87** raw-word corruptions, all **seven** bindings plus an extra,
  private pools and stale source. Three original GNU and three independent C
  rebase links compare all 87 words with HI/LO carry and call relocation.

Two fixture issues were corrected before final qualification: a halfword alias
needed four bytes of mapped store backing, and the second base-alias control
needed distinct alternate-bank depth values to make its stale read observable.
Neither required a production fix or a weakened matching gate.

## Whole Image And Counts

Before installation, independently reproduce the frozen predecessor ELF and
predict exactly **274 changed code bytes plus two symbol-size bytes**. Extent
changes **12 -> 348**; all **3,257,636 ELF bytes** must match the prediction,
with **zero metadata serialization permutations or exclusions**. The normal
build exits zero and reproduces this complete first-predicted SHA-256:
**23d5ee08fc033c461872a1e3382969e6cd5587791ff3b4108c1350c08c9962cf**.

Installed owner SHA-256:
**6caa0dcc8c1ceaac1b96be30cbbc3d3f50dbc7ae61445c24641a81f036a0a61b**.
All **128** live inputs are checked; **126** remain unchanged. Every guard byte
and the Makefile remain unchanged. Protected data is still **189,088 bytes /
720 owners / zero different bytes**. Installed source/image/helper/caller/
metadata corruptions and both fixture-stage corruptions are rejected.

Fresh official totals: Game **2,934/4,828 (60.77%)**, overall
**3,607/5,501 (65.57%)**, still different **1,894**, zero address drift. Init
remains 492/492 and Debugger 181/181 exact among C functions. Conversion remains
5,501/6,044 functions, 86.04% bytes; the previous stub already counted as C.
The root README changes only the two matching aggregate rows.

## Bank And Next Work

Tools **fed3fa9e43b59958db0c8a9d2ccd365d02d54cbd** banks the six new tools
before the consumer pin. Both copies pass Windows AST checks and eleven shared
padder tests: active **0.033s + 0.020s**, older mirror **0.032s + 0.018s**.
make tools-check passes. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **905** initial dirty-file
hashes and **911** final dirty paths. Six added task-file pairs are identical;
do not commit/reset that mirror. Zero Claude calls, no push, host-port change
or frozen Release action.

Continue adjacent **func_1501A8C0**, still a zero-return stub: **373 words /
1,492 bytes / frame 0x48**, VA **0x1501A8C0..0x1501AE94**, ROM
**0x47D70..0x48344**. Recover its view dimensions, clipping bounds, viewport
pages and projection setup; audit the fourth argument's signed-halfword
contract, table widths, repeated live base reads and float-to-halfword stores.
Qualify its real func_1501AE94, func_1501AF44 and func_1510B32C chain before
installation. Keep timing's **141 differences**, other view providers, the
wider Game/additional-source queue and full gameplay acceptance separately open.

Follow-up in progress in [Note 1457](1457-viewport-initializer-recovery-and-matching-boundary-20261016.md):
func_1501A8C0 now has a complete 373-word/frame-0x48 research candidate and
seven passing recovery tests, but still 49 differences. It is not installed;
continue this same function and its outstanding installation gates.
