# Game View Corner Initializer Direct C Conversion

Date: 2026-10-06. Starting checkpoint: `1b85d8cd`.

Convert **`func_1513FFF4`, 55 words / 220 bytes**, VA
0x1513FFF4..0x151400D0, ROM 0x16D4A4..0x16D580, frame eight, in
[game_169510.c](../../conker/src/game_169510.c). The retained raw assembly was
already retail-exact; semantic C now emits the same entire slot directly under
existing O2/g3. No guards/profile/shared header/data/symbol/metadata changes.
Keep the [retail assembly](../../conker/asm/nonmatchings/game_169510/func_1513FFF4.s)
as the unchanged reference.

## Recovered Contract

Void return, output pointer, unsigned index byte and unsigned variant byte.
Index **255** returns without table/output access; it needs neither pointer
to be valid. Other values address a **12-byte** `D_80090B60` record and capture
unsigned halfwords at **+6/+8**. Subtract one with truncation modulo 65536,
then shift each promoted value left six for the corner coordinates. Values
remain nonnegative and fit signed 32-bit before final halfword stores. Width/
height are working interpretations, not recovered original struct names.

| Output Offsets | Stored Value |
| --- | --- |
| +0x38 / +8 | variant bit 0 set: shifted width; otherwise zero |
| +0x28 / +0x18 | variant bit 0 set: zero; otherwise shifted width |
| +0x1A / +0xA | variant bit 1 set: shifted height; otherwise zero |
| +0x3A / +0x2A | variant bit 1 set: zero; otherwise shifted height |

Exactly eight halfword stores, in that order. Variant higher bits are ignored.
All other bytes remain untouched. Both dimensions are captured before any
output store, including when output overlaps table storage. The local table
type describes only observed stride/fields and owns no new data.

Correct the **owner-local** placeholder declaration from signed-word return/
arguments to `void func_1513FFF4(u8 *, u8, u8)`. Its only live C caller,
`func_1513D2F0`, now passes result+0xC0 directly instead of a signed-address
cast. Caller never consumed the helper return. No shared header change.
All **114 constructor words remain identical**; no invented return value.
The constructor experiment declaration/body and typed native callback were
updated consistently; its 97 control measurements and source binding rerun.
Historical Note 1046 describes its earlier signed-word helper boundary.

## Compiler Evidence

[Driver](../../tools/experiments/game_view_corner_initializer_candidates.py)
screens **ten forms x four profiles = 40 controls**, isolated diagnostics
empty. Repeated conditional stores emit 71 words/frame eight and 49
differences. Shared halfword coordinate emits 63 words/42 differences;
shared word without explicit record pointer emits 55 words/25 differences.
Use the explicit record pointer and shared signed-word coordinate: **55
direct words, frame eight, zero differences** under O2/g3.

Plain O2 emits 53 words and 53 differences. O1/g3 emits 65 words/frame 16,
65 differences; O1 emits 64 words/frame 16, 64 differences. Keeping the
signed-address ABI loses the saved-register frame: 50 words/frame zero,
55 differences. Coordinate declaration order, unsigned word and file-scope
table declaration alternatives also match under O2/g3. Register-coordinate
O1 controls shrink to 57/56 words but still differ at 56 words. Tests bind
all lengths/frames/differences including overflowing tails. The function's
local declaration remains the narrowest production data/type scope.

## Qualification

[Nine tests](../../tools/tests/test_game_view_corner_initializer_match.py)
use unchanged shared runners and an independent byte-store reference:

- **8192 guest cases / two bodies**: every index, eight variant bundles,
  four unsigned dimension pairs and both stack phases. Selected C versus
  retail, complete external memory, ordered reads/writes, no calls, saved
  GPR/FPR/SP/RA lifetimes and **all 55 words** covered.
- **65536 selected guest cases** cover every index/variant byte pair with
  high incoming bits and alternating stack phases.
- **15 no-access cases / two bodies** use index-255 aliases/high bits with
  invalid output and absent table memory. No external accesses. **256 alias
  cases / two bodies** overlap output/table around the chosen row; dimensions
  must be captured before the first store. No real retail allocation/table
  domain is inferred from these bounded ordinary-memory diagnostics.
- **589824 native helper cases**: all 65536 unsigned dimension values through
  eight variants (524288), then all 65536 index/variant pairs. Check 12-byte
  row layout, field offsets, four-byte pointers and entire 96-byte output
  storage; index 255 also accepts null. Native storage uses the **byte-exact
  equivalent file-scope declaration control** so the table can be defined in
  the fixture. Function statements remain unchanged, with no invented padding
  writes. This is ordinary-memory arithmetic, not hardware acceptance.
- **1536 connected guest cases / two bodies** execute the actual constructor
  and actual corner helper. Flags, failures, index/variant, allocator/zero
  mutations, negative/full/dynamic bounds and zero/nonzero resource. Complete
  actor/external memory, typed calls and ordered trace comparison. Cover all
  **169 instruction words** (114 constructor + 55 helper). The post-zero
  descriptor byte selects the helper row; copied/allocated mutations stay live.
- **131072 connected native cases** run actual constructor C with entry
  instrumentation forwarding to actual helper C, not an opaque corner
  callback. Every index/variant pair through both allocation outcomes; all
  actor bytes compared independently, including untouched helper fields,
  corner halfwords and later table callback stores. Other table/backend
  providers remain controlled callbacks, not full gameplay/host adoption.
- Six compiled negatives detect stub, wrong sentinel gate, wrong dimension
  adjustment, wrong variant bit, wrong shift and displaced halfword store.

Initial connected-case count expectation was corrected to **1536**, the actual
product of the matrix factors, from an erroneous 3072. Every case already
passed its memory/call/trace assertions. Production did not change for that
fixture correction. The initial driver format-expression error was corrected
before its 40 controls completed. All **52 focused post-link tests pass in
713.368 seconds**, no skips: nine corner initializer, nine constructor, nine
source effect packet, eight actor packet, six configuration packet, six
address-record allocator and five core guard-relocation tests. The standalone
corner driver also completes all 40 controls; all 97 updated constructor
controls retain their original measurements.

## Linked Audit

Build/link/progress pass. Target SHA-256:
`ea3b793b5d2967c382db64bca3a80439e340313a0309dffacb2194a563cec6a8`.
**All 6059 linked function slots are identical** to the assembly checkpoint;
all addresses/sizes unchanged. This conversion does not change executable
instructions. Protected `.init`, `.init_data`, `.debugger`, `.game_data`
unchanged. All **720 Game-data owners / 189088 bytes** remain retail-exact;
all **10660 guard rows** identical and in order. Owner diagnostics retain
**48 identical preexisting warnings**, zero new after normalizing shifted
line locations. None belong to the converted helper. Existing generated_12D630
Makefile duplicate-recipe warnings remain unrelated.

Converted counts increase because this routine genuinely changes from raw
assembly to C: **5463/6042 (90.42%)**, Game **4790/5321 (90.02%)**.
Converted bytes: **85.57% total / 84.88% Game**. Byte-exact totals:
**3325/5463 (60.86%)**, Game **2652/4790 (55.37%)**, **2138 different**,
zero address drift. Init492/492 and Debugger181/181 stay exact. README only
receives aggregate measurements. Ignored receipts under
`conker/build/game-view-corner-initializer[-test]/`; baseline snapshot
`conker/build/game-source-effect-constructor/after.json`.
Tools-check, compileall and diff-check pass; **3316 relative links across
29 documents**, zero broken. No sibling source/build/save/frozen Release
change, runtime launch, push or complete caller/backend/gameplay/host claim.

## Next Work

Inspect **`func_151400D0`, 48 words / 192 bytes**, VA
0x151400D0..0x15140190, ROM 0x16D580..0x16D640, frame zero, retained raw
assembly in this owner. The
[retail body](../../conker/asm/nonmatchings/game_169510/func_151400D0.s)
transfers four 10-byte input records into four 16-byte output vertices:
halfword at input+8 to vertex+6, signed halfwords at +0/+2/+4/+6 to color
bytes +0xC..+0xF, and vertex+6 cleared again before the last byte store.
Preserve intermediate halfword stores and exact alias-sensitive read order,
not just final colors/zero flags. Recover the pointer/void ABI locally and
qualify actual constructor/first-helper/second-helper chaining before converting.
`func_15152190`'s 228-word C placeholder and `func_1513264C`'s semantic but
non-matching extended constructor remain separate pending work.

Preliminary isolated **24 controls** (six forms/four profiles) completed without
installing the next helper. The four-record byte-pointer loop with direct
color stores followed by the flag clear emits all **48 words/frame zero
directly under O2/g3**. Plain O2 emits 47 words and two differences; O1/g3
and O1 retain a 22-word loop/frame eight and 47 differences. Naming an alpha
temporary forces V0 and creates 32 differences despite the correct 48-word
length; the SDK Vtx-pointer direct form has four scheduling differences.
IDO's direct byte form schedules each flag clear after the last color load
but before its byte store, exactly as retail. Preserve and qualify complete
intermediate read/write traces under table/output aliases before installation.
Ignored candidate sources/measurements live under
`conker/build/game-view-corner-initializer/next-attributes/`, generated by
`screen-next.py`; retained `func_151400D0` assembly stays untouched here.

Additional bounded candidate qualification passes **456 two-body guest cases**
over 19 table/output relationships, twelve signed/raw halfword patterns and
both stack phases. Independent ordered reference reproduces every intermediate
read/write, including the transient flags; all 48 words execute. **131072
native candidate cases** sweep every halfword bit pattern through overlapping
and disjoint source/output, checking the whole 320-byte storage. Receipts under
`next-attributes/qualification.json`, generated by `qualify-next.py`. Still
not installed: owner-local void/pointer ABI, actual constructor/two-helper
chain and full linked/diagnostic audit remain the integration gates.
