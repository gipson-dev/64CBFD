# Game Actor Source Packet Byte Match

Date: 2026-10-06. Starting checkpoint: `73c87133`.

Recover **`func_1519EB8C`, 102 words / 408 bytes**, VA
0x1519EB8C..0x1519ED24, ROM 0x1CC03C..0x1CC1D4, frame 0xB8, in
[generated_1CBE20.c](../../conker/src/game/generated_1CBE20.c). Existing O2/g3
emits the complete semantic routine, correct length/frame and saved-S0/RA
lifetime; **14 relocation-aware expected-word guards** normalize only the
closed independent opening schedule. No profile/shared header/symbol/metadata/
data edits. This is a guarded byte match, not a direct compiler match.

## Recovered Contract

Five incoming arguments: 32-byte source prefix, unsigned resource halfword,
signed lifetime halfword, unsigned channel byte and signed context word.
The source has a three-float position at +0, three-float vector at +0xC,
width at +0x18 and height at +0x1C. Save the **source pointer value** in a
separate local, not a copy of its first four bytes.

Construct the established 124-byte extended actor descriptor:

| Offset | Value |
| --- | --- |
| +0 / +4 / +0x1C / +0x20 / +0x24 | float 1.0 |
| +8 / +0xC | source width/height multiplied separately by D_800A8CD4 |
| +0x10..+0x18 | three source vector words |
| +0x28..+0x30 | three source position words |
| +0x34..+0x3C and +0x40..+0x48 | two complete copies of D_800A5480's three words |
| +0x4C / +0x50 | float positive zero / flags word 0x980 |
| +0x54 / +0x56 | lifetime / resource halfword |
| +0x58 / +0x5C | byte zero / word zero |
| +0x60 / +0x61 / +0x62..+0x67 | bytes 255 / 21 / six zeroes |
| +0x68 / +0x6A / +0x6C / +0x70 | byte 2 / byte zero / word zero / byte zero |
| +0x72 / +0x74 / +0x78 | halfwords 1 / 255 / word zero |

Exactly **eight alignment bytes remain untouched**: +0x59..+0x5B, +0x69,
+0x6B, +0x71, +0x76..+0x77. No memset or invented padding initialization.
The local view follows the existing extended-emission descriptor's offsets,
splitting its six-byte reserved tail to expose the retail word at +0x78.
Field names are working descriptions, not recovered original declarations.

Call retained `func_1513264C((u8 *)&packet, 3, 255, NULL, 4, channel, context)`.
On null, perform no payload copy. On success, copy exactly four bytes from the
saved source-pointer local to returned actor+0x170. The source pointer is
captured before callbacks; changes to its pointee do not change that pointer.
The [retail caller](../../conker/asm/50D80.s), ROM 0x54D54..0x54DA4, validates
resource below 0xE9, selects a 0x44-byte-stride source record, passes signed
lifetime/channel/context one, and ignores V0. The recovered C wrapper is void;
tests distinguish machine V0 transport from any promised C return API.

The constructor declaration preserves its actual byte-pointer input and
`struct ExtendedState15F680 *` state type via an owner-local forward tag.
Do not change the retained constructor to accommodate the wrapper. Its
existing [C body](../../conker/src/game/generated_15F680.c) is semantic but
**still non-matching**: 255-word body / 256-word slot, frame 0x50 versus retail
0x48, 184 word differences. Its helper `func_151336A8` and wrapper
`func_15132A4C` retain their previously verified matches. Constructor/backend
qualification here does not make those dependencies hardware-complete.

## Compiler and Guard Evidence

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_actor_source_packet_candidates.py)
screens **14 forms / four profiles = 56 controls**, isolated diagnostics empty.
Plain field order, delayed field4C, factor capture/assignment, chained unit
fields and unit-from-first-field all retain 102 words/frame 0xB8/14 differences
under O2/g3. Wider resource/lifetime add one argument-home instruction
difference. Vector/position struct copies emit 103 words; extra named unit/
factor/address captures grow frames to 0xC0. Dimensions-first has 29 differences.
Plain O2 has 101 words/frame 0xB8/95 differences; O1 variants produce up to
113 words and different frames. Tests bind every exact measurement, including
overflowing tails. No available control is a direct match.

Selected raw code and retail are identical from byte +0x40 onward. Their
opening 16 words are the **same instruction multiset**. All 14 changed offsets
are +8..+0x3C: two independent address pairs, unit-float setup, saves, argument
homes and private local stores move without changing operations. Four
relocation sites move with their HI16/LO16 symbol identities. Guards bind each
expected instruction and relocation; no inserts/omissions/register rewriting.
Tests bind the complete instruction/relocation multiset and reject a changed
input word rather than silently patching it.

The global factor load moves earlier relative only to private stack stores;
no external read/write/call order changes. This excludes arbitrary private
stack aliases, MMIO, concurrency and invalid memory. It is not a claim that
this reorder is valid under those excluded conditions.

## Qualification

[Eight tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_actor_source_packet_match.py) use
an independent byte-packet reference, the existing guest runner and actual C:

- **3456 guest cases / three bodies**: raw compiler, guarded and retail. Eight
  argument bundles, high incoming bits, four contexts, two stack phases,
  three padding patterns, constructor mutation, three outcomes including
  output aliasing source, and three source patterns. Check all 124 packet
  bytes, constructor/copy arguments, external read/write/call traces and full
  external storage. Saved GPR/FPR/SP/RA lifetimes and all **102 words** execute.
- **65536 additional guarded guest cases** cover every resource/lifetime
  halfword on success and all channel bytes, with unrelated high bits and
  both stack phases. Constructor is opaque; high resource IDs are transport
  diagnostics, not valid indexing into the actual 234-entry resource tables.
- **384 guest cases / three bodies** cover signed zero, smallest subnormals,
  normal boundary, near-one and largest finite dimension inputs, three factor
  bit patterns and both stack phases. Coordinate/default copies include raw
  quiet/signaling NaNs and infinities, without arithmetic on those values.
  The runner models ordinary single-precision values, not hardware FCSR or
  exception modes; subnormal/native signaling-NaN behavior is not claimed.
- **131072 opaque native cases**: every halfword twice, successful/failed
  constructor outcomes, every channel byte, high context bits and mutations.
  Actual selected C; check 32/124-byte layouts, four-byte pointers, field
  offsets, all initialized packet fields and entire source/global/output
  storage. Native callback does not assert unspecified padding values.
- **192 connected native cases** reuse the established constructor fixture
  with the actual wrapper, actual constructor and actual resource helper.
  IDs 0/7/232, four signed lifetimes and four slots traverse success, record
  allocation failure, node allocation failure and load failure. Check ordered
  allocation/load/setup/attachment/copy/view calls, resource-list references,
  copied descriptor/default-state bytes, full actor storage and source-pointer
  publication. Backend allocators/loaders/view providers remain callbacks.
  The fixture adds only a four-byte wrapper-copy hook, not production changes.
  Snapshot the descriptor while the wrapper's local is still alive; the final
  actor comparison does not dereference an expired stack-local address.
- Six compiled negative controls detect stub, wrong flags, payload size,
  copying pointee bytes instead of pointer value, wrong channel and zeroed
  alignment byte. Shared guest/native runners are unchanged.

Pre-link controls/width/boundary tests pass (three tests, 79.399 seconds).
The connected native test passed after correcting the local declaration's
pointer types; emitted code stayed unchanged. All **56 focused post-link tests
pass in 281.571 seconds**, no skips: eight new wrapper tests, six configuration
packet, six address-record allocator, 15 retained constructor, 13 extended
emission, three resource-helper schedule and five core guard-relocation tests.

## Linked Audit

The shared guard-table edit triggered a complete padded-object rebuild.
`make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress`
passes. All **102 linked words** match retail; target SHA-256 is
`1ecd9b2811d9839ccff1e288b898398c3c8edb6c30f279ed7b300ef7c56c8604`.
Across **6059 linked slots**, only `func_1519EB8C` changes; every address and
size stays fixed. `.init`, `.init_data`, `.debugger` and `.game_data` are
unchanged. All **720 Game-data owners / 189088 bytes** remain retail-exact.
The previous **10646 guard rows** remain identical and in order; exactly
14 target rows bring the total to **10660**. Baseline/current owner diagnostics
are empty. The usual SDK -mips3/o32 warnings remain outside this owner.
ROM D_800A5480's three default words are all zero; D_800A8CD4 is 0x3DCCCCCD.

Measured aggregate: total **3322 / 5462 (60.82%)**, Game **2649 / 4789
(55.31%)** exact; **2140 different**, zero address drift. Init **492 / 492**
and Debugger **181 / 181** remain exact. Converted counts do not change;
the replaced stub was already counted as C. README changes only these totals.
Keep the baseline snapshot under
`conker/build/game-effect-configuration-packet-test/after.json`; new ignored
receipts are under `conker/build/game-actor-source-packet[-test]/`.
Tools-check, compileall and diff-check pass; **3272 relative links across 27
documents**, zero broken. No sibling source/build/save/frozen Release
edit, runtime launch or push. Broad Game matching goal remains active.

## Next Work

Inspect the same owner's `func_1519ED84`, still a stub: 96 words / 384 bytes,
ROM 0x1CC234, frame 0xA0. It constructs a different source-backed packet,
calls `func_1513D2F0` with a resource table and twelve arguments, and conditionally
copies the source pointer to result+0x110. Recover the full packet, initialized
versus untouched bytes, argument widths and helper contract before installation.
This is static inspection, not a recovered or qualified routine. The effect
consumer `func_15152190` and projection/pair-clamp frame work remain open.
