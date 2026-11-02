# 1990 - Short-packet factory recovered as guarded C

Verified 2026-11-02. Production **4,057/5,507 (73.67%)**; Game
**3,384/4,834 (70.00%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,450 different; one new installed match and unchanged C inventory.
The active 80% target remains **4,406/5,507**, requiring **349 more**. This is
progress toward that goal, not completion.

## Interface and recovered behavior

`void func_15153298(ShortPacketInput *input, u8 mode, s32 owner)` replaces the
zero-return placeholder in `conker/src/game/generated_17CAF0.c`. Original
`17CAF0.s`: VA15153298..15153634, ROM180748..180AE4, 231 words, 192-byte
frame and fourteen relocation bindings. The recovered input record has 62
live bytes; a two-byte private tail preserves its natural 64-byte C size.

The routine converts three floating positions to signed shorts and scaled
bytes, copies the fixed packet owner, colors, alpha and control fields, and
draws a randomized packet count. Each iteration draws two angles, queries
`func_151423D8` at both angles and their quarter-turn offsets, draws speed and
five integer fields, builds three truncated direction components, and submits
the complete packet through `func_15167D84`. Mode is an unsigned byte, owner
is a full-width signed argument and the return contract is `void`.

The draft in `Another Source/CBFD-Recompiled` was used only as a recovery lead.
Its decompiler casts were not adopted. All credited types, field widths,
caller evidence, packet extent and byte behavior were independently qualified
against this repository's retail image and build.

## Complete packet extent and closed compiler words

The submitted packet has a complete **56-byte** private extent. Forty-two
bytes are initialized by the factory. Fourteen bytes remain untouched: the
eight-byte region at offsets 4..11, two bytes at 26..27, bytes 43 and 51, and
the two-byte tail at 54..55. The downstream provider copies all 56 bytes, so
the guest gate explicitly verifies that the factory preserves every private
byte rather than treating the visible writes as the complete object.

The semantic C emits exactly **231 words**, the retail 192-byte frame, all
fourteen relocation bindings and all retail stack offsets. IDO chooses a
different closed integer temporary-register cycle and one independent
initialization schedule. One hundred three checked expected-word
normalizations close only those compiler choices. No relocation word is
guarded. After normalization, every word equals retail at three independently
shifted GNU code/provider layouts.

Raw semantic payload SHA256:
`5b93e16561cb70b6553e717752618e7fc83d2d03bbb9fc041670b7320ab4fa69`.
Normalized payload SHA256:
`b2ac88679486f7a4480a273566bac6d278e652762bd9c936d3f200c50a7f9a10`.

## Fresh qualification

- Guest execution covers 256 cases at each of three independent links, for
  2,304 original/normalized/raw-C executions. All 223 reachable words execute;
  the eight unsigned-divisor trap words remain unreachable under qualified
  nonzero ranges. All 256 mode bytes and zero/one/two-packet paths execute.
- Original and normalized code agree in full memory, register, FP, call,
  payload, event and access-trace state. Raw C agrees in public memory,
  callee-preserved integer/FP state, canonical calls, all 42 initialized packet
  bytes and the complete packet payload. The role-trace multiset compares
  42,240 events; 122 normalized access-prefix pairs also agree.
- Live input mutation after the first RNG call and after every submission
  proves that count, angular ranges, speed, randomized fields and later-loop
  inputs are read at their recovered times rather than cached speculatively.
- Native O0/O2/O3 runs 256 cases per profile, 768 total, with UBSan configured
  to stop on the first error. The independent control compares the 62-byte
  input, call order, all initialized packet bytes and all six submission
  arguments. All three profiles are warning-free and UBSan-clean.
- The complete ROM census finds exactly one aligned JAL in one C parent, with
  no aligned jump or literal target pointer. Static pre-call provenance covers
  all 62 input bytes. The caller and callee both establish byte mode, preserve
  the full third argument, and conservative V0 taint reaches no post-call read.
  Complete parent execution is not claimed.

Both tools copies contain byte-identical five-module qualification suites. The
shared installed suite passes all five methods after validating those hashes.
No gameplay acceptance is inferred from the byte and semantic controls.

## Owner, image and production result

All 40 raw and padded `generated_17CAF0` neighbors and normalized pools remain
identical; owner compilation has zero diagnostics. The real owner recipe uses
five commands and produces the qualified 29,852-byte object. Protected Game
data remains exactly 189,088 bytes across 720 owners.

The strict complete-image predictor replaces the 12-byte placeholder slot and
symbol extent with the 924-byte target. It has zero exclusions and needs no
metadata reorder closure. All 6,052 addresses, 6,051 other bodies and the
complete named-definition multiset remain fixed. The installed production
object equals the qualified five-command Make object, and the installed ELF
equals the independent whole-image prediction exactly.

The direct production link against the OneDrive checkout stalled while the
WSL filesystem bridge held a zero-length output. That invocation was stopped
without accepting an artifact. Production then installed the already-qualified
strict private ELF and a byte-for-byte path-normalized copy of its linker map;
both came from the same complete object graph used by the zero-exclusion proof.
No claim is made that the stalled direct invocation completed.

Installed object SHA256:
`5058f0a965555a37c79ba1a58709388492acb3bda6395a120cc766d13d1f2376`.
Linked ELF SHA256:
`c96781392ff30f96aea42f93ef2ec8c5aa9c19964aa3688694ce7a0aa4f495e2`.
Linker-map SHA256:
`ebb679dbafe5095950abc7ea997853701ce7cf975c8529cf54230dc13f2f0b51`.

The public qualification tools were committed first at
`be6548f`. The retained stage is
`conker/build/game-short-packet-factory-15153298-match/`; it contains the
layout, guest, native, caller, owner, whole-image and installed receipts. The
root README changes only aggregate rows; detailed recovery stays here and in
the five concise indexes. No Claude call was needed.

## Next step

Privately audit `func_151539B4`, the next C placeholder after the retained
assembly routine `func_15153634`. Qualify its ABI, callers, full private object
extents and provider ordering before source fitting. Keep it uncredited until
guest/native/caller, owner/actual-Make, strict-image, installed recount,
documentation and Graphify gates pass.
