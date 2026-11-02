# 1989 - Oriented-effect factory recovered as guarded C

Verified 2026-11-02. Production **4,056/5,507 (73.65%)**; Game
**3,383/4,834 (69.98%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,451 different; one new installed match and unchanged C inventory.
The active 80% target remains **4,406/5,507**, requiring **350 more**. This is
progress toward that goal, not completion.

## Interface and recovered behavior

`void func_15152F70(OrientedEffectInput *input, u8 mode)` replaces the
zero-return placeholder in `conker/src/game/generated_17CAF0.c`. Original
`17CAF0.s`: VA15152F70..15153298, ROM180420..180748, 202 words, 264-byte
frame and thirteen relocation bindings. The recovered input record is 88
bytes. Its position, scalar bases/ranges, angular bases/ranges, randomized
byte and short ranges, six full-width submission arguments, four fixed motion
bytes and mode are all preserved explicitly.

The routine builds a constant descriptor, caches the input position and fixed
motion bytes, and draws a randomized count. Each iteration draws two angles,
queries `func_151423D8` at each angle and its quarter-turn offset, draws speed,
header byte/short and two motion scalars, constructs the three oriented motion
components, and submits all fifteen arguments through `func_15147DA0`. The
input remains live across every provider and submission call. Mode is an
unsigned byte and the return contract is `void`.

The draft in `Another Source/CBFD-Recompiled` was used only as a recovery lead.
All credited types, control flow, private extents, callers and byte behavior
were independently qualified against this repository's retail image and build.

## Complete private extents and closed compiler words

The descriptor has a **36-byte** private extent with 30 visible bytes. The
motion packet has a **32-byte** private extent with writes through byte 28, and
the header has a **24-byte** private extent with writes through byte 22. Their
complete scratch footprint is **92 bytes**. Guest payload captures prove that
the descriptor's six tail bytes, motion's two four-byte private regions and
the header's three private bytes stay untouched.

The semantic C emits exactly **202 words** and all thirteen relocation
bindings, but IDO chooses a 272-byte frame. Thirty-seven checked expected-word
normalizations close only the retail 264-byte scratch placement and one saved
register/scheduling cycle. After normalization, every word equals retail at
three independently shifted GNU code/provider layouts. No relocation word is
guarded.

Raw semantic payload SHA256:
`07baa8548bb2a5b67b717eaa44d704390c5f4b52507d446c4d16afb099aaf7c9`.
Normalized payload SHA256:
`25c67ac4d7109f3bc77eef9078d6893f57d0ecb108bd2b38aed2bf7691bebd16`.

## Fresh qualification

- Guest execution covers 256 cases at each of three independent links, for
  2,304 original/normalized/raw-C executions. All 197 reachable words execute;
  the five unsigned-divisor trap words remain unreachable under the qualified
  nonzero ranges. All 256 mode bytes and zero/one/two-particle paths execute.
- Original and normalized code agree in full memory, register, FP, call,
  payload, event and access-trace state. Raw C agrees in complete register/FP
  state, public memory, canonical calls, complete 36/32/24-byte payloads and
  role-normalized input/scratch traces. The corpus compares 41,472 role-trace
  events and 150 equal normalized access-prefix pairs.
- Live input mutation after the first RNG call and after every submission
  proves that count, angular ranges, scalar ranges, fixed fields and all six
  full-width arguments are read at their recovered times rather than cached
  speculatively.
- Native O0/O2/O3 runs 256 cases per profile, 768 total, with UBSan configured
  to stop on the first error. The independent control compares the full
  88-byte input, call order, initialized descriptor/motion/header bytes and all
  submission arguments. All three profiles are warning-free and UBSan-clean.
- The complete ROM census finds exactly five aligned JALs in four unique C
  parents, with no aligned jump or literal target pointer. All 84 input bytes
  read by the callee have pre-call store evidence. Every mode is a byte,
  byte-mask or constant. Conservative V0 taint reaches no read after any call,
  proving the recovered `void` contract. Complete parent execution is not
  claimed.

Both tools copies contain byte-identical five-module qualification suites. The
shared installed suite passes all five methods after validating those hashes.
No gameplay acceptance or portable reading of uninitialized private bytes is
inferred.

## Owner, image and production result

All 40 raw and padded `generated_17CAF0` neighbors and normalized pools remain
identical; owner compilation has zero diagnostics. The real owner recipe uses
five commands and produces the qualified 29,576-byte object. Protected Game
data remains exactly 189,088 bytes across 720 owners.

The strict complete-image predictor replaces the 12-byte placeholder slot and
symbol extent with the 808-byte target. It has zero exclusions and needs no
metadata reorder closure. All 6,052 addresses, 6,051 other bodies and the
complete named-definition multiset remain fixed. The installed production
object and directly linked ELF equal the qualified object and independent
whole-image prediction exactly.

The live default Make invocation was interrupted after its WSL/OneDrive
recursive source scan remained blocked in `p9_client_rpc`; bypassing that scan
was rejected because it selected incorrect padding rules. This does not weaken
the credited owner gate: the genuine five-command Make owner recipe passed,
and the production linker consumed that exact object and the unchanged full
object graph. No claim is made that the live default aggregate target completed
in that invocation.

Installed object SHA256:
`13171ae4c94be7c6e966fbdd0f353e05dfdfe220af3f0c0cd703ce9cadf67b39`.
Linked ELF SHA256:
`e62447ad4dc113aa5633ac7639ccc34eba9ef21104d56fe48b48c8027e790c31`.

The public qualification tools were committed first at
`b77fdedaa51a1ee1314ceac1dfc6853246536a11`. The retained stage is
`conker/build/game-oriented-effect-factory-15152F70-match/`; it contains the
layout, guest, native, caller, owner, whole-image, installed and mirror
receipts. The root README changes only aggregate rows; detailed recovery stays
here and in the five concise indexes. No Claude call was needed.

## Next step

Privately audit adjacent `func_15153298`, still a zero-return placeholder in
the same owner. Qualify its real ABI, caller census, complete private extents
and provider ordering before source fitting. Keep it uncredited until its
guest/native/caller, owner/actual-Make, strict-image, installed recount,
documentation and Graphify gates pass.
