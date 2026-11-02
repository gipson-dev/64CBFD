# 1994 - Directional-effect factory recovered as guarded C

Verified 2026-11-02. Production **4,061/5,507 (73.74%)**; Game
**3,388/4,834 (70.09%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,446 different; one new installed match and unchanged C inventory.
The active 80% target remains **4,406/5,507**, requiring **345 more**. This is
progress toward that goal, not completion.

## Interface and recovered behavior

`void func_15154684(DirectionEffectInput *input, s32 channel, s32 owner)`
replaces the zero-return placeholder in `conker/src/game/generated_17CAF0.c`.
Original `17CAF0.s`: VA15154684..15154884, ROM181B34, 512 bytes, 128 words,
144-byte frame and eleven relocation bindings. The recovered input is one
natural 60-byte descriptor. Fifty-four bytes are semantically required; root
offsets 0x08, 0x09, 0x0C, 0x0D, 0x2A and 0x2B remain private. The sole caller
initializes 58 bytes, leaving only 0x2A and 0x2B unwritten. All twelve bytes of
the local direction vector are observable.

The factory draws a randomized request count. For each request it draws two
integer angles and a floating radius, calls `func_15143794` to construct the
direction vector, then draws scale, selector, duration and time values. The
eleven-argument provider `func_151C5F44` receives the provider type, complete
direction, randomized scale, mode, selector, duration and time, opacity
comparison, configured request value, low byte of `channel` and `owner`.
The return contract is `void`.

The complete linked-image census finds exactly one aligned JAL: ROM1F3728,
VA151C6278 in `func_151C61A0` (VA151C61A0..151C6290). Its words at VA151C6250,
151C6254 and 151C6258 establish the SP+0x1C descriptor, logical low-byte
channel and forwarded owner arguments. The call delay slot at VA151C627C
stores the final request value. All 54 required descriptor bytes have pre-call
store evidence; conservative return-value taint reaches no post-call read. No
aligned jump or literal function pointer exists. Complete parent gameplay
execution is not claimed.

## Closed compiler words

The semantic C emits the retail 128-word extent, random sequence, loop shape
and provider interface. Its natural compiler frame is 152 bytes; 31 checked
expected-word normalizations close the remaining independent layout choices:

- three frame and scratch-placement words;
- eighteen opening count, argument-home and initialization-schedule words;
- eight words in a closed random-value register-allocation cycle;
- two commutative floating-multiply operand orders.

The two opening relocation-aware schedule rows preserve their symbol bindings;
no helper target is replaced. Three independently shifted GNU layouts agree
after those 31 closed words. Raw semantic payload SHA256:
`65f8717db56dd0fe17874adab0d163cd4834e2ce5a0313ad2ee664e2e875a621`.
Normalized payload SHA256:
`3e1ea91a5ac5d8dbab21726da74374f5b34d7d5699677b7304993664d88a1b8a`.

## Fresh qualification

- Guest execution covers 256 cases at each of three independent links and
  three images, for 2,304 executions. All 124 reachable retail words execute;
  four unsigned-divisor trap words remain unreachable under the qualified
  ranges. Zero/one/two-request paths and all 256 channel bytes execute.
- Original, normalized and raw C agree in public memory, register, FP, call and
  complete provider-payload state. The comparison records 1,008 payloads,
  every one of the eleven provider arguments, complete 60-byte input snapshots
  and complete 12-byte scratch snapshots. Live mutations after count RNG,
  direction generation and provider calls prove the recovered read timing.
- Native O0/O2/O3 runs 256 cases per profile, 768 total, with warnings treated
  as errors and UBSan stopping at the first error. All profiles pass without a
  warning or sanitizer finding; complete input fences remain intact. The
  post-count-RNG live-read check stays with the guest oracle because host C may
  legally preload one count field while evaluating the expression.
- The caller census proves the sole original JAL, its C parent, all three
  arguments, all 54 required bytes and the two naturally unwritten padding
  bytes. Alternate-source code is not used for ABI proof.

The permanent five-method suite reproduces raw/binding, guest, caller, native
and complete-image gates from retained receipts. It passes after installation
against the actual production object and ELF. The bounded Graphify refresh is
structural AST only, retains every prior node and every still-valid prior edge
occurrence, archives the obsolete `s32` placeholder return edge and uses zero
LLM tokens. No full-corpus extraction, global reclustering or gameplay
acceptance is claimed.

## Owner, image and production result

All 40 raw and padded `generated_17CAF0` neighbors and normalized pools remain
identical; owner compilation has zero diagnostics. The real owner recipe uses
five commands and produces the qualified object. Protected Game data remains
exactly 189,088 bytes across 720 owners, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The strict complete-image predictor replaces only the 512-byte target. It has
zero exclusions: all 6,052 function addresses, 6,051 other bodies and the
complete named-definition multiset remain fixed. The installed production
object equals the qualified five-command Make object, and the production ELF
equals the independent strict whole-image prediction exactly.

Installed object SHA256:
`486b0599b1480bcbe15d9fa114c62a563916857a4660d1bf07d53d9dff2b8a80`.
Linked ELF SHA256:
`752feb861f0a37a4ce3ee397f1a52952a048048aff9c3521ad2b3ff3d9b122da`.
Production linker-map SHA256:
`ebb679dbafe5095950abc7ea997853701ce7cf975c8529cf54230dc13f2f0b51`.
The retained private-link map SHA256 is
`2227710ade48c6d2780d32fb7eadd52f190061357c6c4d8590994d18dffaa7a7`.

The public qualification tools were committed first at `0da6eac`. The retained
stage is `conker/build/game-direction-effect-factory-15154684-match/`; it
contains the layout, guest, native, caller, owner, whole-image and installed
receipts. The root README changes only aggregate rows; detailed recovery stays
here and in the five concise indexes. No Claude call was needed.

## Next step

Privately audit `func_15154884`, the next assembly placeholder in this owner.
Keep it uncredited until ABI/caller, semantic runtime, owner/actual-Make,
strict-image, installed recount, documentation and bounded Graphify-retention
gates pass.
