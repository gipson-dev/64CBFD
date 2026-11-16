# Alternate composite-burst constructor recovery and byte match - 2026-11-16

`void func_151A3150(u8 *record)` replaces the zero-return placeholder with
the complete alternate timed constructor: **142 body words / frame 0x90**,
VA `0x151A3150..0x151A3388`, ROM `0x1D0600..0x1D0838`. Two zero alignment
words complete its 144-word slot through `0x151A3390` / ROM `0x1D0840`.
The initial successor preflight incorrectly counted all 144 words as body;
the original endlabel and retail bytes establish the 142+2 split.

Production now has **4,520 / 5,514 (81.97%)** exact C functions; Game
**3,847 / 4,841 (79.47%)**, Init **492 / 492**, Debugger **181 / 181**.
Zero address drift, 994 different; **167 more** to the active 85% goal.
Conversion remains 5,514 / 6,048 (91.17%), 86.19% of bytes.

## Behavior and actual interface

The only aligned literal reference is `D_8008F8E0[1]`, VA `0x8008F8E4`,
ROM `0x2343A4`. Original 45-word/frame 0x20 `func_151A2960` selects this
callback at `0x151A29E4`, supplies A0=record and ignores the return value.
The signed selector, timer/fade, disable and trigger gates remain intact.

The recovered C uses the existing provider-qualified `CompositeEffectInput`
and `CompositeEffectPosition` declarations in the same owner. The complete
116-byte packet is at incoming SP-116, with four untouched padding bytes
at 0x59..0x5B and 0x6B. It calls `void func_15152B38(CompositeEffectInput *,
u8, s32)` with the mode from record+0xC and zero-extended record+1.
Provider recovery remains [Note 1988](1988-composite-effect-factory-direct-match-20261102.md);
the previous slot-0 constructor is [Note 2496](2496-game-timed-composite-burst-constructor-recovery-and-byte-match-20261116.md).

The alternate packet requests base count 10/range 15, copies the record
position and optionally adds record+0x4C..0x54 when flags contain 0x1000.
Its size expressions retain repeated loads and ordered float operations.
Retail constants are D_800A8D3C=`0x3CADAB9F`, D_800A8D40=`0x3D59E83E`,
D_800A8D44=`0xBF83F7CF`. Both radius values are 8.0. Header byte range is
2, short base/range 15/30, and fields 0x64/0x66 are 15/17. All remaining
byte/angle/flag fields and signed tail sentinels follow the actual assembly;
unknown provider meanings retain offset-based names.

## Complete compilation and focused qualification

Raw C emits all **142 words / frame 0x90**, SHA256
`51df0c3cef8b94d3689a99aa7880cd0a3ad21b0877c294e39101c93402762c02`.
Exactly **17 expected-word guards** normalize integer allocation and store
scheduling. A bijection conserves every source operation, literal, memory
offset and all seven bindings: **zero insertions and zero omissions**.
The ordinary conditional branch and ordered FP/FCSR behavior are preserved.

All five maintained tests pass freshly in the primary checkout, an isolated
sibling-tools overlay, and installed production at identical task hashes:

- Independent instruction execution covers both paths and all 142 words,
  full private frame at call/return, ordered FP/FCSR, complete return registers,
  public aliases in the normal-memory model, and opaque provider mutation.
  Independent T0/T1 allocation passes; flag, mode, FP order, tail destination
  and return-delay private-gap corruptions fail semantically.
- Guest execution checks 1,024 cases per retail/raw/padded stream, every mode
  and extra byte value, seeded whole 116-byte packet, provider and record effects.
- Actual native32 C checks 1,024 cases each at O0/O2 with UB traps. Only 112
  defined bytes are observed or mutated. Five source errors exit 3: forced or
  omitted offset, wrong scale, wrong tail sentinel, swapped mode/owner arguments.
- The actual parent checks 256 cases per stream and all 45 words, slot 1,
  unchanged slot 0 and skipped routes, signed timer boundaries, marker clearing
  after callback, provider record changes and preservation of its full A1.
  The unchanged sibling callback and common tail stay opaque in this fixture.
- Both whole-owner padders preserve 38 neighbors and pools. All 142 raw words
  and seven bindings reject corruption; ten stale CSV cases fail, and three
  independent symbol rebases across HI/LO carries preserve the relation.

These gates qualify nonfaulting compiled instructions and finite native
fixtures; they do not establish portable padding contents or gameplay/hardware
acceptance. No shared ABI or helper is changed, and no Claude call was needed.

## Production and evidence

Immutable baseline: **1,269 inputs**, consumer `1d6d525b`, tools `90654787`.
Exactly source, appended guard CSV, owner object and ELF change; **1,265 inputs
remain unchanged**. All predecessor snapshots and overlays are preserved.
Sibling Windows Git status and 301 dependency fingerprints remain unchanged;
its 2,434 pre-existing dirty paths are preserved.

The independent five-command Make shadow agrees with all 39 raw functions.
Production compiles through actual Make without copying a prebuilt object.
Its entire ELF equals the independent prediction: **481
changed bytes, zero exclusions**, with 2 explicitly checked
symbol/string-table permutations. All 20,289 named definitions agree except
the target size 12->568. Symbol value/name, protected data and target-word
corruptions fail the complete-image check. All other 6,050 linked bodies,
every address, 38 owner neighbors and pools remain exact; only one of 698
objects changes. Alignment zeros are included in whole-image accounting.

All **189,088 protected bytes / 720 owners** remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`. Production ELF SHA256:
`9c724d2fa6166eb1826b1783024a4d95efbb4e914bf9893602d13651e5d781ca`.

Reproduce prepared target gates with
`python3 -m unittest tools.tests.test_game_composite_burst_151a3150_recovery -v`.
Receipts: `conker/build/game-next-151a3150-private/adoption/`.
Actual recount and project tools checks pass. Older unchanged semantic evidence
stays historical alongside the fresh complete owner/image audit. Root README
changes only Total/Game aggregate rows. Graphify uses retained-ID scoped AST
updates; no full-corpus re-extraction claim. Tools are committed before consumer
source/pin/docs. No push or host Release/save change. Next: `func_151A3390`.
The wider 85% goal remains active.
