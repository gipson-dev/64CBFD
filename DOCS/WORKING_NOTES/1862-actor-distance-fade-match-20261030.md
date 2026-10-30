# 1862: Actor distance fade restored from C

Verified 2026-10-30. `func_150E05F8` replaces its zero-return placeholder with a
semantic `void(u8 *record)` callback in
[`generated_10CD70.c`](../../conker/src/game/generated_10CD70.c).
The complete 56-word, 224-byte leaf is byte-exact after normal relocation.
No guards, inserted or omitted words, frame changes, shared header changes,
compiler-profile changes or guard-manifest edits are required.

The linked recount is **3,939 / 5,506 (71.54%)** total and
**3,266 / 4,833 (67.58%)** Game. Init remains 492/492, Debugger 181/181,
address drift zero. The 75% goal remains active: **191** more to 4,130/5,506.
The C inventory remains 5,506 and the conversion CSV is unchanged.

## Recovered behavior and compiler shape

The record holds signed halfword coordinates at offsets 0x10, 0x12 and 0x14.
The player pointer is `D_800DBFF0`; its float coordinates are at 0x2F8,
0x2FC and 0x300. Float32 operations preserve the retail order:
`sqrtf(z*z + (x*x + y*y))`. The callback writes record byte 0x8A:

- Distance at or below 2570 produces 255.
- Distance at or above 3850 produces zero.
- The intermediate range uses `255 - (distance-near) * (1/(far-near)) * 255.0f`,
  truncates to signed 32-bit and stores its low byte.

The mixed integer/float spelling of the two 255 operands recovers retail's
independent materializations; spelling both as float merged them and emitted
55 words. Named mutable or const threshold externs preserve semantics but
change scheduling. Numeric local literals recover retail's opening 32 words
and complete register schedule. The SDK intrinsic emits `SQRT.S`, with no call
or stack frame. The duplicate subtraction at offset 0x9C remains literally
present and unreachable; all other 55 words are exercised.

The two literals compile into a 16-byte pool, including eight padding bytes.
Every byte matches retail ROM 0x245A90..0x245AA0: 2570 (0x4520A000),
3850 (0x4570A000), then two zero words. The existing padder's
`RETAIL_RODATA_SYMBOL` mechanism binds this pool at `D_800A0FD0`.
The far load's +4 addend resolves to `D_800A0FD4`.
The Makefile adds this owner-specific anchor and Makefile prerequisite;
the original protected data owner retains all literal storage.

## Qualification

Evidence remains in ignored `conker/build/game-actor-distance-fade-match/`.
Three tools modules are banked first at **56cf597e585f2e4724d08f223b430925785a6da5**; the consumer commit then
pins that exact tools commit. No push is performed.

- Source/ABI: original callback triple `(func_150E05F8,0,0)` at ROM 0x22DB4C,
  VA 0x8008908C, table `D_80088C90`, index 85, stride 12. The five-word
  original indirect dispatch at 0x15113EE0, ROM 0x141390, forwards the actor
  in A0 and ignores V0. Its window passed 23 cases for each original/raw/padded
  program. Symbol references reveal no direct target calls.
- Compiler/owner: all 56 words and six HI/LO bindings are qualified under the
  existing O2/g3 profile, including pooled-symbol addends. All 12 raw and padded
  neighbors are fixed; compilation emits zero diagnostics. The actual three
  Make commands reproduce the qualified padded object exactly.
- Guest: 1,076 cases / 3,228 executions compare all integer/FP registers,
  memory, events and access traces among original assembly, raw C and padded C.
  Coverage includes signed halfword extremes, all axes, every alpha transition
  and adjacent float values, infinities and NaNs. There are 39 interrupted
  access prefixes, 63 cases across three independently relocated layouts,
  three record/player aliases, and a sparse near branch without far-threshold
  storage. The unreachable duplicate is preserved and no branch enters it.
- Native32: 896 finite cases per O0/O2/O3 profile pass UBSan, checking every
  record/player/global byte. Eight effective controls cover threshold, output,
  scale, branch result, coordinate offset and signedness mistakes. Single
  precision square root uses SSE `sqrtss`; FP contraction is disabled.
- Linked image: production ELF SHA-256
  `8de5d938cca687938e6dd1e12b28da5fb731d6219d800a676814dd79df34aa76`
  equals the independent full-file prediction. Exactly 175 bytes differ:
  174 target-code bytes and one symbol-extent byte. No metadata reorder or
  exclusion is needed. All 6,055 other disassembled bodies, every function
  address, and all 189,088 protected Game data bytes across 720 owners are fixed.
- Both tools copies pass eight fresh checks and their project-tools check.
  Each then passes two fresh installed checks; six unchanged semantic checks
  are explicitly reused through identical module/input/artifact fingerprints.
  The complete 16,926-file seal preserves all other source and generated
  objects. Production suppresses timestamp rebuilds of unrelated Makefile
  consumers; the full-file audit and seal verify their exact bytes.

These are bounded nontrapping software FP and native tests. They do not claim
hardware FCSR exception/NaN-payload behavior, complete parent execution, or
host-port/gameplay acceptance. The alternate source's float coordinate reads
contradict retail `LH` and were not adopted.

## Continuation

Next screen **func_15158FA4** from the fresh live queue. Keep private candidates
uncredited until the same ABI, guest/native, owner, Make, whole-image,
production, recount and documentation gates pass. The previous deferred
`func_1507E1D0` and allocator/scheduling candidates remain parked.

The root README changes only its two aggregate exactness rows. Detailed
function updates remain here and in the documentation indexes. Graphify is
refreshed structurally for the changed sources and notes, with explicit
old-node/relationship retention and the obsolete s32 return edge retired;
this is a scoped refresh, not full-corpus re-extraction.
