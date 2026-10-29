# 1818 - Actor channel command - 2026-10-29

`func_15080430` is recovered as `void (u8 *actor, s32 channel, s32 duration)` in
`conker/src/game/generated_AD6B0.c`. Its 51-word / 204-byte body emits directly
from C, followed by the original alignment NOP in its 52-word retail slot.
The original name is retained; the comment explains the channel command and
optional duration clamp. No guards or custom compiler profile are used.

## Behavior and ABI

A null actor returns immediately. Otherwise query `func_1507E968(actor)`.
With a positive animation count, channel zero clears `D_800D1928`, stores 20
at actor+0x72, and calls `func_1507E500(actor, 0, 10)`. Nonzero channels store
0xFFFE at actor+0x72. Channel one sets global mode 2; other channels keep a
zero duration or clamp a nonzero signed duration to 1 through 20 before applying
it. With a nonpositive count, mode becomes `(channel != 0)` and channel zero
clears actor+0x1FF. The explicit nonzero-channel return preserves the retail
layout without caching the global address across its stores.

Frame size is 24 bytes. Nine bindings comprise three JAL sites to two helpers
and three HI16/LO16 global-address pairs. The body starts at VA 0x15080430 /
ROM 0xAD8E0, ends at 0x150804FC, and retains the alignment NOP at 0x150804FC.

The sole aligned direct call is VA 0x15080308 / ROM 0xAD7B8 in
`func_15080228`; no aligned pointer registrations are present. This original
72-word dispatcher converts the unsigned packet selector to signed channel by
subtracting one, decodes a 28-bit packed value, divides by 367, replaces zero
quotients with 20, and selects actor base 0x800CC2D0 plus index times 0x32C.
It ignores the result. The dispatcher remains a C placeholder and receives no
new matching credit from its original-assembly execution here.

## Qualification and production

Both tools copies pass eight fresh canonical methods and their shared tools
checks. Production passes two fresh installed methods per copy; the other six
are explicitly reused under identical module, input and artifact fingerprints.
Canonical v3 supersedes v2 only to remove an extra EOF blank line in the oracle.
The recovered C and compiled artifacts are unchanged by that formatting fix.

- 3,024 guest cases cover all 51 body instructions, signed argument boundaries,
  null actors and opaque provider effects. Full state and access traces agree.
- 78 fault-prefix comparisons include 29 delay-slot cuts; these qualify guest
  instructions, without a portable C fault-semantics claim.
- Native32 O0/O2/O3 each pass 40,192 cases with trapping UBSan and nine effective
  negative controls. The actor uses fresh aligned untyped storage. The fixture
  explicitly realigns its freestanding entry stack after an owned debugger
  proved an initial O2 SSE stack-alignment fault in the test entrypoint.
- 720 connected original-dispatcher cases cover 68 reachable words and its
  packet loop. Four division-exception words are unreachable with literal
  divisor 367. The packet reader is bounded at its interface.
- 2,400 connected helper cases cover the retained exact-C count helper's 31
  reachable words out of 32 and all 50 words of the original-assembly apply
  helper. Identity, definition, animation, submit and tick services are bounded.
  The apply helper remains assembly and receives no C credit here.
- Three GNU layouts / 192 cases exercise JAL and HI16/LO16 relocation carries;
  two actual relocated global-to-actor layouts add 768 overlap cases. Nine
  independently compiled semantic mutations and six full-image corruptions
  are rejected.
- Actual Make uses three commands for this direct-C owner: compiler, padder,
  assembler. There are no compiler diagnostics; inherited duplicate-recipe
  warnings in Make's plan remain unrelated. All three neighbors are preserved.
- The complete ELF changes by exactly 150 predicted bytes: 149 code bytes and
  one symbol-extent byte, zero other metadata or exclusions. All 6,056 function
  addresses, 6,055 other bodies and 189,088 protected Game bytes /720 owners
  remain fixed. Guards, headers, layout map and conversion inventory are fixed.

16,624 sealed inputs and 634 focused inputs are audited. The older tools mirror
retains all 1,895 inherited dirty paths plus the three new qualification modules.
Tools commit `8796721` precedes the consumer pin. No push is performed.

ELF SHA-256: `b7034c6528bf4fedc75fb8c77d66a040e98a9e7a85297e6bfd4718ce7ddb347b`.
Object SHA-256: `3475bc77e06349eeadbbbbf69394a3ff816750f47baebda90bd304ff4193f170`.

## Progress and continuation

Actual live-ELF recount: **3,896/5,506 (70.76%)** total,
**3,223/4,833 (66.69%)** Game; Init 492/492 and Debugger 181/181 remain exact.
Zero address drift; **234** more exact C functions reach 75%. The current queue
selects the next private screen; `func_1514E920` and `func_151D7000` remain
parked and uncredited. No host, hardware or gameplay acceptance is inferred.

Graphify is refreshed over changed C, tools and Markdown with old-node and
still-valid relationship retention. The obsolete placeholder s32 return edge
is retired. The missing apply-helper function node is separately validated
from its literal assembly definition and GLOBAL_ASM ownership; this is not an
assembly AST extraction. Historical global communities and centrality remain
historical; no full-corpus re-extraction is claimed.

Local preparation, canonical, production, recount and final-audit artifacts
remain in `conker/build/game-actor-channel-command-match/`.
