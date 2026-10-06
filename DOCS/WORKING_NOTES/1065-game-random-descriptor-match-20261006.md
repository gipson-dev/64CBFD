# Game Random Descriptor Match

Date:2026-10-06. Baseline:`512f5c88`
([Note1064](1064-game-effect-record-updater-match-20261006.md)).
Continue original Game decomp matching, not host-port adoption or full gameplay
acceptance. Production source:[game_16EE20.c](../../conker/src/game_16EE20.c).

## Retail Contract

**func_15141F78**:96 words /384 bytes, frame0x78,
VA15141F78..151420F8, ROM16F428..16F5A8. Recover six inputs:
`void func_15141F78(u8 slot,u8 *source,f32 scale,u8 tag,f32 *position,u8 mode)`.
The eight original call sites do not consume a result. The return register
left by the submit helper is incidental, not a recovered scalar-return ABI.

Build the40-byte descriptor at SP+50. Every field's offset/store width is
retained: flags6F701; unsigned slot byte6 and zero byte7; integer RNG1 as
**unsigned%61+100**, halfword4; zero words8/C; integer RNG2 masked7F+128
to byte10; bytes11..15 all255, byte16 zero, byte17 seven, word18=3B0002,
byte20=255, halfwords22=40/24=6. Capture the live word source+18 into word1C
**after both integer draws and before the float draw**.

Descriptor byte21 and final bytes26/27 are unspecified padding, not implicit
zeros or fields. No expanded payload or memset is installed.

Float RNG sample follows both integer draws. Retain three separate binary32
operations: multiply5, add10, multiplyscale. After this provider, load live
source/position values and low-byte tag/mode. The complete submit ABI is:

```c
func_1513C650((s32)&descriptor, 0, 0, (s32)(source + 4),
    position[0], *(f32 *)source, position[2], range, range,
    tag, mode == 2, 3, 1, 0, 255, 1);
```

The A3 value is **the address source+4**, not the word stored there. The old
commented draft used `arg1->unk4` and cannot be transplanted as-is. Descriptor
sourceWord must not move past the float provider; source/position float reads
must not move before providers. Recovered native byte inputs truncate through
their types; full32-bit guest input aliases verify original byte homes.

## Direct Compiler Recovery

[Maintained driver](../../tools/experiments/game_random_descriptor_candidates.py)
screens16 shapes times four actual-SDK profiles:64 controls. Controls cover
the existing signed SDK descriptor versus a local unsigned-byte descriptor,
s32/u8 boolean local, explicit if versus equality expression, and local
declaration order. Empty standalone diagnostics for all controls.

The corrected signed SDK shape already emitted96 words/frame0x78, but six
byte255 constants became `addiu -1`, followed by identical byte stores.
Recovering local unsigned-byte fields produces **all96 words directly** under
the existing O2/g3 profile. Both s32/u8 branch-shaped boolean controls match;
choose s32 as the retail unmasked stored argument. No profile/frame rewrite,
word guards, insertion/omission or shared SDK/header changes. Old partial
commented draft removed; typed local declaration installed.

The layout has the same40-byte extent and field offsets as SDK struct157.
Only the byte signedness is corrected locally; names do not establish a full
effect-system taxonomy or downstream helper restoration.

## Qualification

[Eleven maintained tests](../../tools/tests/test_game_random_descriptor_match.py):

- **6912 paired guest cases**:six first random words/four second words, three
  float samples/two scales, three modes, disjoint/overlapping source-position,
  four provider mutation masks and two stack phases. Compare every ordered
  trace and all storage, including copied padding. Reach all96 words in both
  compiled and original bodies; saved registers/SP/FPRs survive poisoned calls.
- **944 edge cases**:512 every-byte/full-width guest slot/tag/mode aliases and
  432 float pattern pairs across three aliases. Signed zeros, subnormals,
  overflow, infinities and NaNs retained as binary32 values. No hardware FCSR,
  exception flag/rounding-mode or native NaN-payload parity claim.
- **48 guest-only parameter-home probes**:float provider redirects source,
  scale, tag, position and mode homes. Final submit reloads these; descriptor
  sourceWord still retains its earlier capture. Native C is not asserted to
  allow external access to private parameter homes.
- **57856 actual32-bit native cases**:57600 integer/float/scale/mode/alias/
  provider-mutation combinations plus256 every-byte cases. Verify complete
  known descriptor fields, all16 submit arguments, external storage and output
  sentinels. Three unspecified descriptor padding bytes are not prescribed;
  arithmetic NaNs are classification-compared. Submit models return a nonzero
  pointer without turning the source into a result-producing function.
- **144 connected cases** execute the eight original jal/delay pairs, including
  the sixth-argument store. Connect each to compiled/original descriptor code
  under three aliases, two SP phases and three mode words. Caller continuation
  is a bounded synthetic epilogue; this is **not complete original caller
  execution**, float-to-tag conversion/FCSR acceptance or gameplay validation.
- Actual padder preserves all384 bytes and all four R_MIPS_26 relocations;
  alternate targets exercise call retargeting. No guards are emitted.
- Twelve compiled negatives must change known external storage/call sequence
  on valid mapped inputs:placeholder, missing submit, source-address dereference,
  signed remainder, wrong random mask/mode/position/slot/lifetime/descriptor
  flag/float order, and cached sourceWord. A fault, compiler difference or
  unspecified padding difference alone does not satisfy the negative gate.
- Unmapped sourceWord/position/submit output fails strict guest memory gates.
  No hardware fault or legal native out-of-bounds behavior is claimed.
- Copied actual-SDK owner contains93 functions:target raw bytes/relocations
  equal the standalone direct body;92 other function bytes/relocations, existing
  pool and two warnings unchanged. Maintained tests reconstruct only this
  target's baseline in a copy, not through a historical Git or ignored fixture.
- Production binds the typed source, complete96-word linked slot, five exact
  neighbors and the entire unchanged10809-row guard file.

RNG providers and func_1513C650 remain bounded models in behavior fixtures.
Original instruction identity proves this function's retail code, not original
helper execution, allocator acceptance, real effect output or full gameplay.

Harness corrections:the initial native expected sourceWord marker occupied
an output sentinel byte, causing a real sentinel assertion failure. Move the
marker into its own scalar. The signed-modulo negative exposed missing signed
DIV/HI support in the local oracle; implement quotient-toward-zero/remainder
before counting its semantic difference. Avoid importing a unittest class by
name, which initially caused its unrelated five tests to be discovered too.
Corrected ten-test pre-install bundle passes in72.952 seconds, no skips/errors/
failures; independent three-gate rerun also passes. No production body changes
were needed for those harness fixes.

## Production Verification

Explicit `make -j4 VERSION=us build/conker.us.elf` passes. Compared against
512f5c88, **only func_15141F78 changes across6059 slots**; addresses/extents
stay fixed. Target SHA-256:
`073ecdb14ebceb0141e2c3c75f39b638fc611f8e7a5caaf2269a46f32e3a2df9`.
Dispatcher100, actor45, context57, checked caller37 and updater80 words remain
exact. Protected `.init`, `.init_data`, `.debugger` and `.game_data` addresses/
hashes unchanged; all720 Game-data owners /189088 bytes match, zero differing
owners/bytes. Owner warnings2->2 with identical code/statement/caret evidence,
no new warnings. The full build is not warning-free.

All10809 guard rows remain unchanged, canonical SHA-256:
`e021c108eef6c84112743955be809d3bdf4ce4e1de0cba474897ed3b0bcabb8a`.
Conversion counts remain5464/6042 total and4791/5321 Game; byte coverage stays
85.57% total/84.89% Game. Exact total **3340/5464 (61.13%)**, Game
**2667/4791 (55.67%)**, **2124 different**, zero drift. Init492/492 and
Debugger181/181 remain exact. Complete-ROM checksum not claimed.

All54 focused post-link tests pass in528.932 seconds, no skips/errors/failures:
11 descriptor,11 updater, eight actor classifier, eight context classifier,
11 dispatcher and five actual-padder tests. Documentation:47 documents/3521
relative links/zero broken. Project tool, scoped Python syntax and
`git diff --check` gates pass. Ignored receipts:
`conker/build/game-random-descriptor-test/`.

## Next Function

Continue **func_15142180**,80 words /320 bytes, frame0x70,
VA15142180..151422C0, ROM16F630..16F770. The intervening func_151420F8 already
has semantic C; do not count it again. Next routine is still a placeholder.

1. Recover five input types from seven original call sites. First input is
   consumed as low-byte slot; the second supplies a three-word position copy;
   third is stored as an opaque word, while fourth/fifth feed float products.
2. Recover the76-byte descriptor at SP+24, including three-word copy at SP+2C,
   halfword constants, unsigned identity byte at SP+60 and private padding.
3. Preserve separately rounded2.5/2 times the fourth input and3/3.5 times the
   fifth input. Read live D_800A5470/5474; keep their original data owners.
4. Bind func_15153F18's five arguments:descriptor pointer, copied-position
   subrecord pointer,0,255,1. Recover its local prototype without changing a
   shared header or adopting an unrelated host implementation.
5. Qualify aliases, float patterns, constructor/argument ordering, actual SDK
   frame/padding, negatives, retained neighbors and all-slot/data audit before
   installing another function.

The two live constants have retail words3DDD2F1B/3E51EB86 at ROM249F30/249F34,
inside the existing640-byte Game-data owner at800A5200..800A5480. Preserve
that owner rather than duplicate its floats in compiler rodata. The commented
`struct218XXX` in game_2062D0.c is not the actual small SDK struct218; check
the full76-byte layout before choosing a type. Retail func_15153F18 spans168
words in asm/17CAF0.s (VA15153F18..151541B8); the production version in
src/game/generated_17CAF0.c is still a zero-return placeholder. Keep that
helper's restoration separate from qualifying its five-argument call site.

Root README aggregate rows only. No sibling source/build/save, frozen Release,
runtime launch, host adoption, hardware/gameplay acceptance or push.
