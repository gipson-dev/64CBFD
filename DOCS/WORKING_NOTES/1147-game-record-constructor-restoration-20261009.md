# Game Record Constructor Restoration

Date: 2026-10-09

## Result

Continue [Note 1146](1146-game-record-actor-position-conversion-20261008.md)
using the [focused workflow](../AGENT_WORKFLOW.md), one Codex writer and zero
Claude calls. Replace the false zero-return C body of `func_151D71B0` in
[generated_204660.c](../../conker/src/game/generated_204660.c):
VA 0x151D71B0..0x151D7264, ROM 0x204660..0x204714,
**45 words / 180 bytes / frame 0x50**. The complete routine emits directly
from semantic C under the existing O2/g3 profile. **No guards or normalizer.**
Retain original assembly, compiler profile, Makefile and retail inputs.

The complete 34-word/frame0x38 caller `func_151D74B0` now uses a pointer
return and `12.0f` instead of an integer bit literal. Its compiled instructions
and relative relocations are byte-identical. All **23 functions in this owner
now match retail**. This does not imply guard-free emission for its other
functions or complete gameplay acceptance.

Fresh full linked audit checks all 6,058 instruction slots and the entire
ELF. Only the constructor's original 180-byte slot and its own `st_size`
field (12 -> 180) change. Every other ELF byte, all slot addresses/extents,
protected data and all 11,475 guards remain unchanged. New ELF SHA-256:
`c921336917d3f64f5c162f479da6a04b0ca67289e3e3467e0f010dff9f1626f1`.
The old placeholder already counted as C, so **converted counts and bytes
do not increase**; progress CSV records remain identical.

| Section | Converted | Converted bytes | Byte-exact | Drift | Different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,484 / 6,042 (90.76%) | 1,938,336 / 2,256,728 (85.89%) | 3,396 / 5,484 (61.93%) | 0 | 2,088 |
| Init | 492 / 539 (91.28%) | 151,796 / 164,048 (92.53%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,811 / 5,321 (90.42%) | 1,766,900 / 2,072,880 (85.24%) | 2,723 / 4,811 (56.60%) | 0 | 2,088 |
| Debugger | 181 / 182 (99.45%) | 19,640 / 19,800 (99.19%) | 181 / 181 (100.00%) | 0 | 0 |

Root README changes only the snapshot date and its two affected exact rows.
The 6,042 main slots exclude 16 overflow symbols; raw progress has 6,044
records because two section headers repeat.

## Recovered Contract And Fit

Arguments are s16 duration, u8 active, u8 selector, f32 threshold, s32 extra
bytes, u8 slot and s32 context. Construct the existing 24-byte
CallbackRecord151D7264: null attachment, selector, zero flags, three positive
zero coordinates and bit-preserved threshold. Do not initialize its two
padding bytes. Preserve those exact emitted private bytes in retail/model
comparison; their values are not a portable C contract.

Call `func_15149130(duration, -1, 0x42, -1, active, 0x36,
extraBytes + sizeof(record), slot, context)`. On success copy 24 bytes to
created+0x28 and return the original created pointer, not memcpy's destination
return. Null allocation returns null without any payload copy. Size addition
uses the recovered unsigned sizeof expression and wraps at 32 bits.

Declaring the created pointer before the local record fits the retail layout:
RA+0x2C, record+0x34 and created save+0x4C; record padding at SP+0x3A/0x3B.
The record-first form has the same 45 words/frame but ten differences. The
selected form has zero differences and two R_MIPS_26 relocations at +0x78
(creator) and +0x94 (memcpy), no constant pools. Four profile measurements:
O2/g3 45 words/0 differences, O2 45/28, O1/g3 47/45 and O1 47/44.

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_constructor_candidates.py)
tests 24 complete forms. Eight wide-byte forms fail exact physical argument
qualification: e.g. active 0x12345680 is forwarded rather than retail's 0x80.
Record concrete witnesses; do not classify these as matching merely because
a narrowing callee might observe the same low byte. Alternate local padding
is excluded only for exploratory semantic comparisons, never selected/retail
comparison. Five compiled negatives are effective: wrong kind, zero active,
zero threshold, short copy and replacement of the result with memcpy's return.

## Qualification

The [eight-test suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_constructor_match.py)
reuses the existing Shaping/Triangle oracle, native32 harness and owner/padder
helpers. It adds an independent constructor reference, not another emulator.

- **4,224 cases / 8,448 executions** compare selected and retail against
  independent allocation/copy arguments, public bytes/events and return value.
  Cover signed duration boundaries, all active/selector/slot bytes, high input
  bits, 12 float bit patterns including signed zero and NaNs, wrapped size,
  full s32 context, allocation failure, caller-home clobber, public allocation
  mutation and both stack phases. All 45 words execute; GP/FP saves survive.
- **152 real missing-byte pairs** check public write fault prefixes. Trimmed
  failure fixtures require no destination/payload mapping. These qualify
  emitted instructions, not portable invalid C access or hardware traps.
- **69,120 actual native32 C cases** cover all 65,536 duration values,
  all byte values with 12 float patterns and 512 typed-caller cases. Check
  full 512-byte canaries, call widths, payload bits and original pointer return.
  Skip the two unspecified record padding bytes and caller's one trailing
  extension padding byte. Allocation and memcpy are bounded native stubs.
- **96 connected cases / 192 executions** use all 49 linked creator words,
  all 11 linked memcpy words and all 34 typed-caller words. All connected
  words execute. Independently check allocator flags 0x23/0x5F, requested
  size/context/slot, duration/header writes, zero area, payload, caller actor
  identity/joint/signed secondary byte and failure paths. Generic allocator
  `func_15167A68` and 16-byte bzero remain bounded. This creator is a real
  allocator wrapper, not a connection to the separate 115-word descriptor core.
- Preserve **22 copied-owner neighbors**, pools, relative relocations and
  the four existing diagnostics. Actual padder emits exactly 180 bytes with
  no `.space` or guards. Four independently linked GNU symbol sets qualify
  **64 cases**, including J26 regions and both SP phases. This is not a
  separately rebased original-assembly pair.

Pre-install eight-test run passes in **34.870s**, no skips. An earlier form
test incorrectly accepted wide physical arguments; correct its classification
using observed call words. The initial post-install audit failed because it
expected symbol size 12 to remain unchanged. Structured ELF parsing identifies
only the named function's size field, requires 12 -> 180, and permits exactly
that field plus the restored instruction slot. Do not call those failed runs
passing. Fresh complete post-install run passes in **33.365s**, no skips.
Fresh **24 shared tests pass in 0.310s**; both tools checks pass. Production
build succeeds with the existing duplicate generated_12D630 recipe warning
and four unchanged C diagnostics. Prior unchanged neighbor suites are
historical receipts, not newly rerun wholesale.
Twelve tool files parse and match the older mirror exactly; scoped link
validation checks **133 documents / 4,142 relative links / zero broken**.

## Receipts And Banking

Ignored receipts: `conker/build/game-record-constructor-test/` contains
baseline.json, before.elf, before-manifest.csv, before-progress.csv, slot.json,
guest.json, faults.json, forms.json, owner.json, native.json, connected.json,
linked.json and after.json. Do not commit binaries, progress CSV or receipts.

```sh
python3 -m unittest tools.tests.test_game_record_constructor_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Per "Keep commited", bank mounted tools
**ce159a51355b1594b9ed1fac3d71ef4b557ccc5f** first, then exact parent source/
docs/gitlink. Mirror only the two absent new files after exact-byte checks.
Preserve older standalone HEAD ddbdd16, independently dirty shared helper/
effect test and all unrelated paths; do not reset, duplicate history or push.

Manual Graphify refresh refuses 16,900 nodes over retained 38,689 and keeps
19,398 nodes from 2,972 excluded files still on disk. Do not force a reduced
corpus overwrite. Graph repair remains open. No OGL/Release, runtime/save/
editor, bridge or account changes. The wider Game goal stays active.

## Next Work

The current owner no longer contains a false-zero function. The next nearby
linked mismatch is **func_151D9EB0** in
[game_2062D0.c](../../conker/src/game_2062D0.c):
VA 0x151D9EB0..0x151D9FC0, ROM 0x207360..0x207470,
**68 words / 272 bytes / frame 0x60**, currently 65 differing linked words.
It remains a zero-return C placeholder. Recover signed halfword timer wrap
and early exit, random float/integer call order, the 16-argument effect call
and second random timer reset. It is referenced by the callback pool at
0x8008A610; that reference is not gameplay qualification. Capture its actual
owner/ABI/linked baseline before fitting and keep hardware acceptance open.
