# Game piece update/fade guarded match

Date: 2026-11-14. `func_1517A1EC` is recovered in
`conker/src/game/generated_1A7260.c`. Its complete **106-word / 424-byte**
body occupies `0x1517A1EC..0x1517A394`, ROM `0x1A769C..0x1A7844`, with
the original **0x18-byte frame**. **91 words emit directly from C; fifteen
expected-word guards restore retail scheduling and private register roles.**

All ten other owner functions and normalized pools remain unchanged,
including the matched burst caller, piece factory and settle/fade callback.
The shared record view now names the two unsigned halfwords at `0xAC/0xAE`
as `motionMode` and `dampingRange`, and the byte at `0xB2` as
`retireNibbles`. These names describe measured uses, not a complete
interpretation of the effect system.

## Recovered state transitions

The callback adds X/Z velocity, subtracts Y velocity, and advances each
angle by its signed-byte spin. Motion mode 5 increments Y velocity. When
the unsigned timer is below the mode value, two random draws damp X and Z
independently: each current velocity receives the negative of its sign
times the unsigned random remainder. Zero velocity uses the nonnegative
sign; the routine does not clamp a step that crosses zero.

The timer then subtracts `D_800BE9E4` with 32-bit wraparound. If the signed
result is negative, timer becomes zero and opacity loses four times that
same tick value, with signed-negative opacity clamped to zero before byte
narrowing. Timer equality does not start the fade. The record retires when
opacity is zero, or when a nonzero `retireNibbles` byte has equal low and
high nibbles. The zero packed byte does not itself retire the record.

The two random results are explicitly sequenced into `randomWord` before
reading `dampingRange`. Native helper-mutation testing exposed that the
single C remainder expression allowed a compiler to read the field before
the helper changed it. Explicit sequencing preserves the measured retail
order while leaving the IDO output unchanged. Unsigned intermediates make
the timer, fade and damping arithmetic's wrapping behavior explicit.

## Guard scope

Four guards move the ordinary-RAM timer load from before the final
Z-speed calculation/store to immediately after it. The timer and speed
occupy disjoint halfwords at `0xA6` and `0xA4`. Eleven more guards coalesce
the dead timer register with the opacity value, restore temporary roles,
and reuse a dead register for the retirement byte. Frame size, field
offsets, branch structure, helper calls and all five named bindings stay
fixed. There are no inserted or omitted operations or compiler/header
changes.

The complete raw body SHA-256 is pinned:
`b95469be23c121cedc8691b358a7142df8998f2011425d1f285bee24989c7688`.
All 106 individual raw-word corruption controls and one binding corruption
control reject altered input. Guarded code matches all retail words and
bindings. Raw C's reordered private register state and reordered memory
accesses are not described as instruction-by-instruction fault equivalence.

## ABI and focused qualification

A full retail census finds **no direct JAL callers** and exactly three
aligned callback pointers at ROM `0x230108`, `0x2301D8` and `0x23117C`.
They are descriptor entries **8, 12 and 89** in `D_8008B4A8`, stride `0x34`.
The callback takes one record pointer in A0 and has a void interface.

The integrated check is:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_piece_update_1517a1ec_match -v
```

- **2,477 guest cases** cover signed motion/spin, timer/mode boundaries,
  damping directions, helper mutations, all 256 retirement-byte values,
  all 256 opacity values, extreme tick words and two stack phases. Five
  additional global-alias layouts qualify guest behavior without claiming
  portable C aliasing semantics.
- **22 prefixes stop immediately before a zero-divisor DIVU**, after the
  preceding motion and helper effects. All three streams agree through
  that boundary. The check does not invent hardware HI/LO values or claim
  execution beyond division by zero.
- **144 cases through the authentic dispatcher window**
  `0x15167164..0x15167178` load each real descriptor callback, preserve the
  saved next-record link, execute the callback through JALR and return to
  the continuation. Retirement overwrites the modeled record, checking
  that the callback performs no subsequent record access.
- **92 fired memory boundaries** preserve complete modeled state between
  retail and guarded code. Raw C passes the independent public memory,
  helper-call and helper-observation model; its access reordering remains
  explicit.
- **1,376 native 32-bit cases per O0/O2/O3 profile** pass with UBSan,
  checking all 184 record bytes in N64 byte order and helper observations.
  Six effective source controls reject wrong Y direction, unsigned spin,
  gravity mode, damping direction, fade rate or zero-byte retirement.
  Four guest instruction controls also reject changed behavior.
- Both **complete-owner padders** pass. Twelve GNU links across four code
  layouts preserve the target's complete body and five named bindings.

**104 / 106 instructions execute** in the valid corpus; the two original
break-7 words remain static byte matches. Full divide-by-zero hardware
execution, handwritten 64-bit RNG execution, complete dispatcher/provider
lifecycle and gameplay acceptance are not claimed. RNG and retirement
implementations are modeled boundaries.

Fresh pre-install suite: **21.093 seconds**. Fresh installed suite:
**23.567 seconds**, no skips. A fresh installed suite using sibling tools
dependencies passes in **30.052 seconds**. Its overlay writes only to the
consumer's ignored build directory. Sibling HEAD stays
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with all **2,439** pre-existing
dirty paths preserved. Before/after status SHA-256 is
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`.
`make tools-check` and scoped whitespace checks pass.

## Production audit and progress

The independent shadow executes the three actual Make object commands.
Production ELF equals that prediction exactly, SHA-256:
`1247787b09209f1d5ec0d046c1fa9d40d5ba76d59187ec205f754937d0462f2e`.

Strict whole-image delta is **297 bytes**, with zero exclusions and no
metadata groups. Only this callback body and symbol extent change. All
**6,051 function addresses** stay fixed. Only `generated_1A7260.c.o`
changes among **698 objects**, in text/relocation/symbol/string sections.
All **189,088 protected data bytes**, **82 headers**, existing guard rows
and conversion CSV rows are preserved. Exactly fifteen guard rows are
appended, and **791 immutable input fingerprints** pass.

Actual recount: total **4,481 / 5,515 (81.25%)**, Game
**3,808 / 4,842 (78.65%)**, Init **492 / 492**, Debugger **181 / 181**;
zero drift and **1,034** different C functions. This is **one new exact C
function**. Converted function/byte totals remain unchanged. **207** more
matches reach 85% at the current denominator.

Scoped Graphify refresh covers the owner and five tools files, retaining
all **60,339** previous node IDs: **60,377 nodes / 113,714 links**, with
zero lost nodes. This is not a full-corpus extraction. Private evidence and
frozen inputs remain under `conker/build/game-piece-update-1517a1ec-screen/`.

## Resume boundary

Next: **`func_15179FE0`**, the same-owner **131-word constructor** with the
original **0x38-byte frame**. It initializes the motion-mode and damping
fields consumed here; recover its allocation path, parameter widths and
random-draw lifetimes before claiming another match.

Commit tools before the consumer source, fifteen guards, README aggregate
rows, note and concise indexes. Keep the 85% goal active; do not push.
`64CBFDOGL` has no host source checkout at the available path, so no host
build/runtime adoption is claimed. Frozen Release artifacts are untouched.
