# Game event-0x3E owner dispatcher match

Date: 2026-09-30

`func_150F7310` occupies 35 words and 140 bytes at
`0x150F7310..0x150F739C`. For event `0x3E`, it compares the object owner word
and identity byte at offset `0x28` against the incoming owner record; either
match destroys the object through `func_1516972C`. Other event codes forward
the incoming owner record, event code, object fields at `0x28/0x2C`, and
object pointer to `func_15149514`.

Declaring the event byte and incoming owner pointer volatile recovers retail's
incoming argument homes and deliberate repeated loads. Writing the word
comparison in target-first order recovers the retail value ordering.
Twenty-three words emit directly from semantic C. Twelve stale-checked guards
normalize the remaining closed identity-register cycle and independent owner
load schedule; branches, arguments, calls, and both relocations remain
compiler-owned.

The focused object, exhaustive guard-dependent rebuild, complete relink,
authoritative matcher, and direct span comparison pass. The linked ELF and
retail spans share SHA-256
`48c08c6129179c91ef5a8cfcfc843012e4ec73ee2fa9353bc1442508c71b4969`.
The matcher advances to `3,081 / 5,461 (56.42%)` overall and
`2,502 / 4,788 (52.26%)` in Game, with zero address drift.

Resume in Init, which has 94 genuinely different C rows remaining.
