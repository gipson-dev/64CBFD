# Selected-point effect descriptor directly matched

Date: 2026-11-06. Continues [Note 2141](2141-game-linked-event-callback-match-20261106.md)
from consumer `dd955ba8ff48d176780d57ba032d84924193c998` and mounted tools
`a0993cedbabe6d9c1a3dd6f30f355da911582262`, toward the active 80% goal.

## Direct source recovery and callback ABI

`func_15146A98` in `conker/src/game/generated_173D40.c` emits all
**72 words / 288 bytes directly from semantic C**, with **zero new guards**.
VA `0x15146A98..0x15146BB8`, ROM `0x173F48..0x174068`, frame `0x68`, no
alignment tail. The O2/g3/MIPS2/O32 profile is unchanged. All12 compact/padded
neighbors and padded pools/register metadata remain fixed. Its14 relocation
bindings match retail. The inherited guard CSV is byte-identical.

The interface is `void (u8 *actor, s32 context, s32 unused)`. The full context
and third argument match the existing `GameEffectCallback` type. A zero actor
word at offset0x1D4 returns immediately. Otherwise, the routine calls
`func_15146890(&position.x, actor, NULL, (u8)context)`, copies the position into
a real descriptor, fills its scalar fields and calls
`func_15150F90(&descriptor, 0, 255, 1)`. The point helper's return value is
ignored. The third callback argument is retained in the ABI and is unused.

The original callback appears once, at ROM0x22EB84 / VA0x8008A0C4, entry2 of
`D_8008A0B4`, followed by its positive count85. There is no direct JAL or tail
entry. The two original dispatch windows in func_15141A7C pass a full-word
context and either zero or a signed16 record count. The positive retail count
uses registration before the queued route; the direct window is qualified as
a call boundary, not falsely reported as that entry's default first-stage path.

## Real descriptor and exit shape

`EffectPoint173D40` has three float words /12 bytes, at SP+0x5C.
`PointEffectDescriptor173D40` occupies68 bytes at SP+0x18. These two real
objects account for the original frame; no synthetic frame padding or unused
local was added. The descriptor's three padding bytes are left unwritten.
All offsets in the following table are hexadecimal relative to the descriptor.

| Offset | Recovered contents |
| --- | --- |
| 00 / 04 | Count base5 and range22 |
| 08 / 0C / 10 | Three copied position words |
| 14 / 18 | Float constants D_800A5708 / D_800A570C |
| 1C / 1E | Signed16 values0 /255 |
| 20 / 22 | Signed16 values-20 /14 |
| 24 / 28 | Float values6.0 /3.0 |
| 2C / 30 / 34 / 38 | Float constants D_800A5710 /5714 /5718 /571C |
| 3C | Byte3 |
| 3D / 42 / 43 | Unwritten padding |
| 3E / 40 | Signed16 values25 /25 |

The first complete body already had72 words/frame104 but six differences:
the opening actor reload/schedule and one closed T6/T7 allocation pair. An
ordinary **early return** recovers all six naturally. Flattening the following
block preserves the exact result. Declaration reversal displaces both objects;
old-style syntax, byte context and assignment-order experiments need not be
repeated. There are no postcompiler instruction changes for this routine.

The compact owner newly uses T4/T5. Its .reginfo and .options GPR mask changes
only A301CFFE to A301FFFE. Every other raw allocatable pool/metadata field and
all padded pools/register metadata remain fixed. Discarded raw debug geometry
is not claimed identical. No compiler diagnostics are introduced.

## Qualification boundaries and evidence

Eight methods pass before/after installation in both tools configurations.
The sibling's dirty2434 status paths remain unchanged. Its own compiler,
parser, guest oracle, native command and metadata serializer are used. The
sibling lacks game_player_status_accessor_match.py; its complete allocatable
pool auditor is an explicitly fingerprinted, read-only mounted fallback.
New target modules are loaded through a disposable overlay. The109 core/header
snapshots remain checked.

- **1,397 guest cases per body** cover all256 context bytes, upper context
  bits, full-width unused arguments, both helper results, post-helper constant
  mutations and raw float bits including signed zero, subnormals, infinities,
  quiet/signaling NaNs. Raw compact C, padded C and retail are byte-identical;
  the two executed bodies agree in full literal state. Every root word is visited.
- **240 alias cases per body** cover actor gate/position, rebased globals and
  incoming homes. **170 fired access cuts** compare complete states and fault
  PCs/delay markers. A disabled actor needs neither constants nor local buffers.
  Seeded private bytes and guest faults are not portable C claims.
- **1,036 connected point cases per body** run the original56-word helper.
  Modes1/2 select point indexes0x13/0x17 and receive a filled position through
  the bounded resolver. A literal NULL result bypasses the height-query branch.
  Other modes leave the seeded guest position untouched, which the caller still
  copies. Portable native tests use initialized provider outputs and do not
  claim defined uninitialized-position or padding semantics.
- **180 connected consumer cases per body** run the complete original155-word
  func_15150F90 alongside the point helper as applicable. The independent
  float32 reference checks5-to27 emissions, angles, scalar ranges, spread,
  flags and signed16 values. Initial count and doubled spread remain cached;
  later position/spread/mode/value mutations are reloaded where retail reloads.
  The consumer reads no padding bytes. RNG, direction construction and final
  emission remain bounded provider models; their hardware/gameplay behavior
  and additional C recovery are not credited.
- **64 cases per original caller window**, five and eight words, check table
  index2, unsigned-byte point selection, full context and signed16 third
  arguments. The original14-word positive-count branch is also checked and
  invokes func_15141E38(actor,2). Complete list-dispatch parents are not claimed.
- **Six independent GNU links**, three layouts and36 cases per body check
  all14 bindings: two JALs and six HI16/LO16 constant pairs, including signed
  low16 carries and standalone zero tails.
- SDK native32 with UBSan at **O0/O2/O3** runs **885 cases per profile**.
  Descriptor/point sizes, offsets and pointer width are asserted. A captured
  position pointer remains distinct from the copied descriptor position while
  both objects are alive. A promoted helper argument and typed callback test
  the full-word/byte boundary. All nine controls fire: gate, point mode, newly
  checked helper result, count, copied coordinate, signed range, float constant,
  consumer tag and the former stub. Native reads only initialized fields.
- **288 raw-byte corruptions,14 binding corruptions and11 image corruptions**
  fail closed. The former stub and initial six-difference source are rejected.
  Both tools copies pass fresh smoke checks. Three unchanged shared regression
  receipts are reused only with exact helper/test fingerprints.

## Production and resume boundary

Only generated_173D40.c recompiles once, with zero C warnings/errors and no
profile changes. Actual Make equals the **complete376-byte ELF prediction**,
with zero excluded ranges. The target body and symbol size12 to288 account for
230 changed bytes. Adding constant references causes six bounded GNU
symbol/string permutations involving13 existing definitions, accounting for
146 metadata bytes. The predictor serializes only frozen BEFORE records and
strings; every named definition is retained. Both code and metadata corruptions
are rejected. All6,052 function addresses, other bodies, progress.csv, Makefile,
and189,088 protected Game bytes across720 owners remain fixed.

The inherited duplicate12D630 recipe warning and expected unfinished-image
checksum exit2 remain. No live hardware or gameplay acceptance is claimed.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,211 / 5,512 (76.40%) | 0 | 1,301 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,538 / 4,839 (73.11%) | 0 | 1,301 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**199 more** matches reach the current4,410 threshold for80%.

- ELF: `37445089783b40e86d03888ca71642b0ff1e9ddc8499c57119049e707f6ebc27`.
- Owner: `ba91463c3e72a4e3379486996c50838da42097079d8e4f182de32a6a54ef5d8f`.
- Binary: `22e20933bfbf228a47d14ce33d0b00bee46e180b2ad3c8a383fe426eb6f01415`.
- Unchanged guard CSV: `9892912f5423eb5e518da147fb0bf7e358de56260cb3d59e6b2e6d1bcff0c4ab`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Reproduction: `python3 -m unittest tools.tests.test_game_selected_point_effect_match -v`.
Actual Make uses `-o retail_word_patches.us.csv -o Makefile`, followed by the
ELF/progress, expected unfinished-image `all`, and
`match-progress NON_MATCHING=1` targets. Receipts are retained in
`conker/build/game-owner-effect-descriptor-15146A98-match/`.

Tools commit precedes source/docs/pin. Root README gets aggregate rows only.
Graphify retains nodes outside changed paths and the legacy fail-closed corpus;
this scoped refresh is not full extraction. Claude calls:0. Next is
**func_1514F6E8**, generated_17CAF0,72 words; inspect its retail routine and
caller contract before recovery. It remains uncredited. Preserve handwritten
func_150A6FA0/func_150A76F0, unrelated work, private inputs/saves and frozen
host Release. Keep the full80% matching goal active.
