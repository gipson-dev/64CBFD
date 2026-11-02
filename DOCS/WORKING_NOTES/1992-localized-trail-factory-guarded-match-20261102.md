# 1992 - Localized-trail factory recovered as guarded C

Verified 2026-11-02. Production **4,059/5,507 (73.71%)**; Game
**3,386/4,834 (70.05%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,448 different; one new installed match and unchanged C inventory.
The active 80% target remains **4,406/5,507**, requiring **347 more**. This is
progress toward that goal, not completion.

## Interface and recovered behavior

`void func_15153CCC(void *transform, LocalizedTrailInput *input, s32 request,
s32 channel, s32 owner)` replaces the zero-return placeholder in
`conker/src/game/generated_17CAF0.c`. Original `17CAF0.s`:
VA15153CCC..15153F18, ROM18117C, 588 bytes, 147 words, 184-byte frame and
thirteen relocation bindings. Its recovered configuration is a natural
68-byte C object. Sixty-five bytes are required by the routine and caller
chain; padding bytes 0x35..0x37 remain private. The transform is a natural
44-byte object with 41 required bytes and private padding bytes 1..3. All
twelve bytes of the local velocity scratch are observable.

The factory first rejects inactive transforms. It then chooses a randomized
request count and, for each request, asks the recovered basis-position helper
for a randomized point. Four further integer/float random draws select scale,
duration, mode, time and request-selector values in their configured ranges.
The 18-argument provider receives those values, the configuration, the
request and owner identifiers, the low big-endian byte of `channel`, two fixed
global values and the recovered opacity comparison. The provider return is
ignored and the function's return contract is `void`.

The direct parent at VA150DA67C calls the factory at VA150DAC0C/ROM1080BC.
The typed wrapper `func_15153C84` calls it at VA15153CB4/ROM181164, and the
third direct parent at VA151D09A8 calls it at VA151D0CA0/ROM1FE150. The wrapper
has one caller at VA150DACD4. The complete ROM census finds no aligned jump or
literal target pointer, and all three returns are unconsumed.

## Closed compiler words

The semantic C emits the retail 147-word extent, frame, saved-register
lifetime, loop and all thirteen bindings. Eight checked expected-word
normalizations close the remaining independent compiler choices:

- six frame/home/scratch-placement words at offsets 0x000, 0x044, 0x088,
  0x090, 0x1D8 and 0x248;
- two commutative floating-multiply operand orders at offsets 0x12C and
  0x13C.

No relocation word is guarded. Three independently shifted GNU layouts agree
after those eight closed words. Raw semantic payload SHA256:
`113bc5680dce87ab01bb2fc6e61dd680c0145bf7207aa2277ca62bc1457755f5`.
Normalized payload SHA256:
`4010f34df3c4ee71e3737d1a9a82e5a30411d8ac815647534f69c3b69960c93d`.

## Fresh qualification

- Guest execution covers 256 cases at each of three independent links and
  three images, for 2,304 executions. All 143 reachable words execute; four
  positive-divisor trap words remain unreachable under the qualified ranges.
  Zero/one/two-request paths and all 256 target-channel bytes execute.
- Original, normalized and raw C agree in public memory, register, FP, call,
  provider-payload and access-prefix state. The comparison records 945 full
  provider payloads, every one of the 18 arguments and 152 normalized
  access-prefix pairs.
- Live configuration and transform mutations after the transform helper and
  provider calls prove that later-loop fields are consumed at their recovered
  times. The three private bytes in each input extent stay outside the required
  interface. Count-RNG mutation is retained as a guest control because host C
  operand evaluation order need not equal retail MIPS scheduling.
- Native O0/O2/O3 runs 256 cases per profile, 768 total, with warnings treated
  as errors and UBSan stopping at the first error. All profiles pass without a
  warning or sanitizer finding. Endian-neutral repeated-byte channel values
  exercise every channel while the guest proves retail big-endian byte
  selection.
- The complete caller census finds exactly three aligned JALs. Both direct
  parents establish all 65 required configuration bytes and 41 required
  transform bytes. The wrapper chain preserves the complete configuration,
  while byte-exact `func_1514F640` constructs every required transform field.
  Complete parent gameplay execution is not claimed.

The public five-method suite reproduces the raw/binding, guest, caller, native
and complete-image gates from the retained private receipts. It passes after
installation against the actual production object and ELF. The bounded
Graphify refresh is structural AST only, retains every prior node and every
still-valid prior edge occurrence, and uses zero LLM tokens. No full-corpus
extraction, global reclustering or gameplay acceptance is claimed.

## Owner, image and production result

All 40 raw and padded `generated_17CAF0` neighbors and normalized pools remain
identical; owner compilation has zero diagnostics. The real owner recipe uses
five commands and produces the qualified 30,148-byte object. Protected Game
data remains exactly 189,088 bytes across 720 owners, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The strict complete-image predictor replaces only the 588-byte target. It has
zero exclusions and closes one explicitly measured metadata ordering group,
`D_800A5FFC` with `D_800A1CFC`. All 6,052 function addresses, 6,051 other
bodies and the complete named-definition multiset remain fixed. The installed
production object equals the qualified five-command Make object, and the
production ELF equals the independent strict whole-image prediction exactly.

Installed object SHA256:
`2f7c430999f0b99e0665eb283ef71e25a12a6baf68f23342eaa4acfc580437f9`.
Linked ELF SHA256:
`6169616442e3370f715b255f6db33fdffba7eb9b2aa6ea8bea645282cbf70f5f`.
Production linker-map SHA256:
`ebb679dbafe5095950abc7ea997853701ce7cf975c8529cf54230dc13f2f0b51`.

The public qualification tools were committed first at `07d336d`. The
retained stage is
`conker/build/game-localized-trail-factory-15153CCC-match/`; it contains the
layout, guest, native, caller, owner, whole-image and installed receipts. The
root README changes only aggregate rows; detailed recovery stays here and in
the five concise indexes. No Claude call was needed.

## Next step

Privately audit `func_15153F18`, the next zero-return placeholder in the same
owner. Its current 168-word retail slot has 158 real differences. Qualify its
ABI, callers, object extents, provider ordering and owner neighbors before
source fitting. Keep it uncredited until guest/native/caller, owner/actual-Make,
strict-image, installed recount, documentation and bounded Graphify-retention
gates pass.
