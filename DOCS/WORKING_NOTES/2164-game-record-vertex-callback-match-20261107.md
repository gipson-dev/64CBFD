# Scaled record vertex callback recovered and byte matched

Date: 2026-11-07. Continues [Note 2163](2163-game-record-motion-update-match-20261107.md)
from consumer `ca6bf494501f046f6fe509f89480289e1cfddaa4` and tools
`dfa24a4a9fa1495ae796abf69f05c1ba603407c2`. One qualified Game recovery
advances the active 80% total goal. Host code and frozen Release are untouched.

## Recovered interface, scratch and output

`Vtx *func_1513E83C(u8 *actor, s16 view)` replaces the false s32 zero-return
placeholder in `conker/src/game_169510.c`. All **167 words / 668 bytes** match
at VA 0x1513E83C..0x1513EAD8, ROM 0x16BCEC..0x16BF88. The existing O2/g3,
MIPS2/O32 profile emits the original **216-byte frame**, saved S0..S4 and
F20/F21 pair, original homes, signed view handling and four-iteration loop.
Five R_MIPS_26 call bindings remain literal.

1. Query func_151D5D60 with `(actor+0x100, view, 0x40, &cursor, &fresh)`.
   Capture the returned cursor and return NULL immediately if it is absent.
2. For a fresh buffer, copy the 64-byte template at actor+0xC0 into both
   halves of the selected view buffer. Reload the buffer pointer between
   copies; keep the captured return pointer independent of the live cursor.
3. Construct four XY corners from width/height at +0x2C/+0x30. Orientation
   receives actor angles +0x40/+0x44/+0x48. Set matrix translation from
   +0x34/+0x38/+0x3C and scale its first three rows with +0x4C/+0x50/+0x54.
4. Transform each corner with literal Z=0. Truncate XYZ to the SDK Vtx
   coordinate fields, clear Vtx.flag, reload and advance the escaped cursor.
   Return the initial captured pointer after all four vertices.

The local scratch view gives fresh at SP+0x5B, points at SP+0x5C, first at
SP+0x8C, cursor at SP+0x90, matrix at SP+0x98, and incoming view at SP+0xDC.
Its three leading bytes and four alignment bytes stay untouched. Source
comments identify these original private homes rather than claiming that
the scratch aggregate recovers the original author's exact type spelling.

The point address explicitly uses 32-bit arithmetic over the local points
array with stride 12. This is the N64 O32 contract; native checks assert
pointer32 and the scratch member relationships. Signed view input, signed16
loop index, 16-byte vertex stride and separate float32 operations remain.

## Source screens and eight closed guards

The related adopted func_15140190 supplied the semantic quad-building shape.
Adding the nine row scales, removing unused Z initializations and recovering
the signed counter reached 167 words but an incorrect 208-byte frame and
48 differences. Reordering separate declarations did not change that result.
Grouping the original private homes recovered frame 216 but gave 168 words.
The explicit 32-bit point address recovered **167 words / frame 216 / eight
differences**. Other screens remain private and uncredited.

Raw target SHA-256:
`cfe9e5532a20a1b649af001042a8cae0f8898cce37920869a18427d47d2c71dd`.
Exactly eight expected-word guards normalize these bounded differences:

* On either successful copy/fresh edge, compute the matrix address before
  the single common width load. There is no intervening call or store. Null
  output skips both forms. The same actor word is read once on either path.
* Rename the closed matrix lifetime from S3 to S2 and the points lifetime
  from S2 to S3 after their earlier view/copy roles are dead. Both original
  saved registers restore before return. Matrix and point addresses passed
  to helpers stay identical.
* Commute the independent point-base and stride definitions before MULTU
  consumes them. No instruction insertion, deletion, branch retarget, frame
  alteration or relocation rewrite is involved.

The guarded words are 40, 43, 44, 45, 78, 79, 117 and 119. Complete raw-body
and binding fingerprints pin their scope. Removing one role update is an
effective control that produces wrong public output. An explicit raw-versus-
retail access-cut counterexample also demonstrates the private-state limit.

**Raw emitted code is qualified for public output, calls and return within
the ordinary mapped-memory/provider contract. Raw private/fault-prefix
identity is not claimed.** Separately, normalized code matches the full
retail machine and memory-access prefixes. Overlapping-copy and exceptional
floating-point fixtures exercise guest words, not portable C memcpy/cast
semantics. Native cases use valid disjoint objects and finite cast inputs.

## Actual table, helpers and original dispatcher

The complete aligned retained-ROM scan finds no direct JAL, exactly one
entry pointer at ROM 0x22E8DC, and no interior pointers. This is real slot 0
of D_80089E1C. Its first **39 words** are renderer pointers; the following
graphics words at ROM 0x22E978 are excluded from that callback prefix.
The related func_15140190 occupies slot 30 of the same prefix.

The complete original **295-word func_1513DB00** selects byte +0x73 and
calls this routine at 0x1513DC24 with actor A0 and signed16 view A1. It
consumes the pointer result for rendering/release behavior. **That dispatcher
is still an unrestored production stub.** Its retained execution qualifies
this interface without claiming a dispatcher restoration or live gameplay.

Seven focused checks pass before and after installation in both tools
configurations:

* **919 guest cases per body** compare retail, normalized and raw code with
  an independent ordered copy/float32/vertex/return model. Cover signed and
  upper-bit view inputs, widths/scales, null/fresh paths, live slot and
  cursor changes, first/incoming-home mutations, aliases and cast boundaries.
  All 167 target words execute; the scratch gaps and saved lifetimes agree.
* Connect the original **11-word memcpy, 40-word matrix transform and
  52-word buffer backend**, each checked against ROM and the frozen ELF.
  All 103 words compare and 102 execute. The one unexecuted backend word
  supplies a fallback fresh pointer; this caller always supplies a nonzero
  byte address. Allocation remains a bounded provider. Orientation is an
  explicit matrix provider, separate from these original helper connections.
* **290 complete-dispatcher cases per body** compare the actual connected
  callback against a counterpart using the independent leaf provider. Cover
  visibility/attached gates, null/success, color/geometry/animation branches,
  copy mutations and cursor redirects. Execute 293 of 295 caller words.
  Words 115/146 are duplicate defaults skipped by both explicit predecessor
  branches; all 295 remain compared. Other rendering services stay bounded.
* **805 fired access cuts**, including **152 delay cuts**, compare normalized/
  retail full private memory, GPR/FPR/HI/LO, PC and memory prefixes, including
  original-helper execution and saved F20/F21/S-register lifetimes.
* Native32 O0/O2/O3 each pass **432 cases** using SDK Vtx, typed services,
  pointer32, live escaped cursor/copy-slot mutations, scratch-address checks,
  trapping UBSan and round-to-nearest with FTZ/DAZ clear. Ten compiled
  negatives reject with exit 1: stub, missing flags, three vertices, wrong
  query size, translation, scale, axis, Z input, copy offset and return.
* Two independent GNU links preserve all five calls. Every altered raw
  word, binding/history/pool corruption and six whole-image corruptions reject.

Floating-point modeling is bounded IEEE-single arithmetic, not hardware FCSR,
exception or NaN-payload emulation. Native private-home and overlap exclusions
are explicit. No Claude call was required for this qualified reconstruction.

## Production and progress

All **181 frozen inputs**, **58 raw/padded neighboring functions**, pools,
register masks/options and **43 inherited compiler warnings** remain fixed.
The padder preserves its existing `jtbl_800A5188_game` anchor. Actual Make
recompiles only game_169510.c and equals the independent full-image predictor:
**502 changed bytes, zero exclusions**: 500 Game-body bytes and two target-
extent bytes. No symbol/string ordering change occurs. Only this function's
extent grows from 12 to 668 bytes.

All **6,052 function addresses** and **189,088 protected Game bytes across
720 owners** remain exact. Eight guard rows append; historical guards,
Makefile and progress CSV remain unchanged. Compilation/linking pass. The
remaining whole-ROM checksum retains expected exit 2 and the inherited
duplicate generated_12D630 recipe warning.

Both tools copies pass fresh shared smoke checks. Three unchanged shared
regressions per copy are explicitly reused after exact fingerprints. A
disposable overlay and hashed read-only missing-helper fallback preserve
all 2,434 inherited dirty sibling paths.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,234 / 5,512 | 76.81% | 0 | 1278 |
| Game | 3,561 / 4,839 | 73.59% | 0 | 1278 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**176 more exact functions** remain to 4,410 / 80%. Root README gets only
aggregate rows. Four concise index leads preserve all historical text.
Refresh Graphify on changed paths with fail-closed legacy-node retention,
without a fresh full-corpus claim; commit tools before consumer source/docs/
pin, then verify the fresh hook terminal and stable production artifacts.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `dcbf32c646a456f9018e2f426b44409d324ff50182ef2c3f0ea89a425aaf3876` |
| Production binary | `388af889052301bb5c8be2fc46b3847a3d6960f13e4e41972208916ff091c549` |
| Padded owner | `35d3bae46aec04b21d70027769c0cc039b0f33947a07963d01af5985c3bb5195` |
| Guard manifest | `89060a24e81fd2df17749fc4379c55c983002fd7b4485ec97da47cd5a5ed5e47` |

Ignored receipts: `conker/build/game-record-vertex-callback-1513E83C-match/`;
initial/layout source screens remain in its adjacent private directory.

Next: **func_1513F728**, the related damping/motion callback at
VA 0x1513F728..0x1513FA2C, ROM 0x16CBD8..0x16CEDC, 193 words / frame 48.
Inspect its tick-count damping loop, old-vector snapshot, midpoint position
update and angular-rate updates; recover its actual update-table interface
and qualify independently. Keep other candidates private and uncredited,
the 80% goal active, and all frozen/private-input/save/host Release boundaries.
