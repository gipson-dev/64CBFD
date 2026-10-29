# State byte publisher direct C match

Verified2026-10-29. `func_151738C4` replaces the zero-return placeholder in
`conker/src/game/generated_1A0790.c`. VA151738C4..15173994, ROM1A0D74..1A0E44:
52 words/208 bytes,32-byte frame,14 bindings. All instructions emit directly
from C with zero guards, alignment, insertion, omission or profile changes.

## Recovered contract

`void func_151738C4(s32 context)` acts only when `D_800B0DF0->value` (signed
byte+0x46) equals-1. If bit0 of the word at `D_800DBFF0+0x5F0` is set, it calls
`func_151733E4(6,6,context,0,-1)`, then publishes `D_800DD2E4[0..2]` into
`D_800DBEA8[0..2]`. The emitted code loads all three source bytes before stores.
Otherwise it calls the provider with0,0,context,0,-1, reloads `D_800B0DF0`,
and publishes bytes5/6/7 with interleaved loads/stores. No physical meaning
beyond the observed three-byte state is inferred.

Direct byte assignments recover the original temporary registers exactly.
Named local bytes produced21 register differences; a three-byte struct copy
produced48 words using LWR/SWR. The final source is exact in the full owner.
Raw/original SHA256 `840d3103fe77315fbd403eea1bc7c7e95ffdb78129391d210e3cb3b2a1584c69`.

The provider's current C body remains its unprototyped zero-return placeholder.
Its original entry establishes five32-bit arguments; the source comment states
that boundary. No provider C matching credit or complete provider execution is
claimed. Adding formal parameters to its stub would create unrelated argument-
home code, so the placeholder remains unchanged. The target result is unused.

The existing caller in `conker/src/game_45B80.c` now declares the target void.
All16 compact functions/pools and its entire actual-Make padded object remain
unchanged. Three inherited caller warnings remain; no new diagnostics.

## Qualification

- Eight fresh canonical checks and shared tools checks per tools copy; two
  fresh installed checks each and six unchanged semantic checks reused only
  with identical module/input/artifact fingerprints.
- 640 guest cases plus40 guest partial-alias cases cover all gate bytes,
  flags/context boundaries, provider mutations, pointer reloads and both copy
  orders. All51 reachable words are covered; the duplicate at15173944 is dead.
  Original/raw/padded complete state, calls, memory and access traces agree.
- Native32 SDK O0/O2/O3 each pass65,536 cases with trapping UBSan. Eight
  effective semantic controls are separately compiled by IDO and native GCC;
  each terminates and has a behavioral witness. Native buffers are disjoint;
  guest partial-global aliases are not claimed as portable C behavior.
- The sole aligned ROM JAL is467D4; no aligned pointer registrations. Original
  caller `func_15019130` uses the two-word window15019324..1501932C, with96
  cases and an LW argument load in the delay slot. Precondition S0 points to
  D_800BE9F0, established by original words at ROM46754/46758. Return ignored.
- Sixteen cases execute the original21-word provider prefix151733E4..15173438:
  fifth argument loaded from stack into S0, fourth preserved in S3, first
  three homes and the DD2F0 halfword side effect verified. No full caller or
  provider execution, hardware or gameplay claim.
- 31 fault-prefix pairs include3 delay-slot cuts. Another255 sparse gate-skip
  cases remove flag/source/destination memory without accessing it. Three GNU
  layouts pass24 cases with all14 relocations and all four object images equal.
  66 raw/binding and212 whole-image corruption controls reject.
- The actual owner Make recipe has four commands: primary O2/g3, non-debug O2,
  padder selecting only `func_151733D8` from the latter, and assembler. All four
  neighbors are fixed. The caller's separate three-command Make path is exact.

## Production audit and progress

Complete production ELF equals the independent prediction:165 changed bytes=
164 target instructions+1 target extent byte; metadata0, exclusions0.
All6,056 addresses,6,055 other bodies,189,088 protected Game bytes/720 owners,
all non-target objects, guard CSV, conversion inventory and map remain fixed.

Fresh live-ELF recount: **3,902 /5,506 (70.87%)**;
Game **3,229 /4,833 (66.81%)**; Init492/492; Debugger181/181; zero drift.
**228 more** exact C functions reach4,130 /5,506 (75%).
ELF SHA256 `ae49e847d3cda56030e290efc7838489dd4621ca19ad3a793322ec56c57e6b26`.
Object SHA256 `36b938f32a23584eddf905fc7bb18281421024117f60e499d1fcac81f19ca01d`.
Tools committed first as `7e97ee1`; consumer follows this note. No push.

## Resume

Evidence: `conker/build/game-state-byte-publisher-match/` holds655 frozen focused
inputs,16,666 sealed inputs, canonical/installed receipts, strict image, mixed
Make and caller checks, live recount, graph and final audits. The older tools
mirror retains1,913 inherited dirty paths plus3 new modules. README changes
only aggregate rows; graph refresh is scoped, without full-corpus/global
analytics claims. Goal active. Next screen `func_15187EC0`; next note1825.
`func_1514E920` and `func_151D7000` remain parked/uncredited.
