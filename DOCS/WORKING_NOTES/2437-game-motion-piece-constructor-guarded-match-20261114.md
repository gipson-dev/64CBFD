# Game moving-piece constructor guarded match

Date: 2026-11-14. `func_15179FE0` is recovered in
`conker/src/game/generated_1A7260.c`. Its complete **131-word / 524-byte**
body occupies `0x15179FE0..0x1517A1EC`, ROM `0x1A7490..0x1A769C`, with
the original **0x38-byte frame**. **115 words emit directly from C;
sixteen expected-word guards restore cached scalar homes and the final
initialization schedule.** All ten other owner functions and normalized
pools remain unchanged, including the motion/fade callback and burst pieces.

## Recovered interface and behavior

The constructor has a void interface with eleven integer O32 argument words:
unsigned-byte variant; signed-halfword X/Y/Z; signed-byte vertical speed;
unsigned-halfword lifetime and mode; unsigned-byte movement, spin and damping
ranges; and a full signed-word category. Its only direct caller ignores the
return register. The complete retail census finds that JAL at ROM `0xF5124`
and no aligned literal pointers to this function.

Allocation is `func_15167A68(category, 0, 0xB8, 1, 255, 1)`. Failure performs
no record initialization or random calls. Success initializes position and
vertical speed, then draws centered horizontal X/Z velocities from the
unsigned random remainder minus half the movement range. Mode 5 applies an
initial four-step offset: add X/Z velocity and subtract Y velocity, with
signed-halfword position narrowing. The three angles start at zero.

Three further draws initialize signed-byte X/Y/Z spin around half the spin
range. A sixth draw initializes scale to `((random & 127) + 140) *
D_800A7220`. Finally the routine sets lifetime, variant, mode, a zero
retirement byte, opacity 255 and the damping range used by the existing
update callback. Other bytes of the 184-byte record remain intact.

The movement range and half-range are captured after the first RNG call and
survive the second. The spin pair is captured after the third draw and
survives the fourth and fifth. Using the formal parameters directly preserves
these IDO lifetimes and the retail frame; explicit range/half-range/random
locals inflated the frame or added moves. No shared header or compiler
profile changes are needed.

## Guard scope

Ten guards relocate the two successive, nonescaping range/half-range pairs
from raw SP+0x2C/+0x30 to retail SP+0x28/+0x2C. Saved S0/RA, the frame,
outgoing allocation arguments, incoming argument homes and all helper calls
stay fixed. Six more changed words exchange the opacity/damping temporary
roles and restore the final mode store, damping load, retirement clear and
opacity store order. The heap record and stack argument homes are disjoint.
Every operation remains present. All nine named relocation bindings remain
unchanged; none of the sixteen guarded offsets carries a relocation.

The entire raw body is pinned by SHA-256:
`fe39cd31d306fb8f88c08375ef6c8163e09348f9285aa571a841421a5adf0ee4`.
All 131 individual raw-word corruption controls and one binding corruption
control reject altered input. Guarded code matches the complete retail body
and bindings. Raw C has different private spill locations and final access
order; it is not described as instruction-by-instruction fault equivalence.

## Focused qualification

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_motion_piece_15179fe0_match -v
```

- **3,654 valid guest cases** cover all byte-range values, allocation failure,
  signed coordinates/vertical speed, 16-bit narrowing, mode/lifetime limits,
  full-word categories, three random patterns, two stack phases, provider
  register clobbers, outgoing-home clobbers and record/global mutations.
  Deliberate incoming-home mutations test cached range lifetimes only in the
  guest ABI; they are not portable C parameter mutation claims.
- **38 zero-divisor prefixes** stop before DIVU after checking preceding
  effects. There is no claim about hardware HI/LO values or break behavior
  after division by zero. **126 / 131 words execute**; five original break-7
  words remain static matches.
- **96 cases** execute the authentic 28-word caller window
  `0x150C7C0C..0x150C7C7C` in `func_150C79BC`, including its float-to-variant
  conversion, all eleven arguments, JAL and saved-register continuation.
  This qualifies the call boundary, not the entire unrecovered caller.
- **72 fired memory boundaries** preserve complete modeled state between
  retail and guarded streams. Raw C passes independent final-record and
  helper-call/observation checks. Five effective instruction controls reject
  wrong allocation size, mode, initial step, scale mask or spin field.
- **1,534 native 32-bit cases at each of O0/O2/O3** pass with UBSan,
  comparing all 184 record bytes in N64 byte order and helper observations.
  Six effective source controls also reject an incorrect velocity center.
  Native cases exclude zero ranges and guest incoming-home mutation.
- **144 constructor-to-callback scenarios** execute 168 subsequent retail
  update steps and 24 retirements, including three-step sequences. The
  callback's complete 106 words are reverified from the newly padded owner.
  Retirement overwrites the record and prevents another callback dispatch.
  Allocation, handwritten RNG and retirement providers remain modeled.
- Both **complete-owner padders** agree across all eleven functions and
  pools. Twelve GNU links across four code layouts preserve the target and
  all nine named bindings.

Fresh pre-install suite: **24.980 seconds**. Fresh installed suite:
**29.316 seconds**, no skips. The installed sibling-dependency overlay suite
passes in **31.054 seconds**; before/after status reports are retained in
the private target evidence. It writes only to the consumer's ignored build
directory, with fallback to
mounted dependencies when a sibling module is absent. Sibling HEAD stays
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, preserving all **2,439** dirty paths;
before/after status SHA-256 is `a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`.
`make tools-check` and scoped whitespace checks pass. Full provider/hardware
execution and gameplay acceptance are not claimed.

## Production audit and progress

The independent shadow executes the three actual Make object commands.
Production ELF equals that prediction exactly, SHA-256:
`4e1379b2896b8859e11c070c71bf2aa8c1c33168c40aaeec5c1fd12cc7a49b49`.

Strict image delta is **369 bytes**, with zero exclusions and no metadata
groups. Only this constructor's body and symbol extent change; all **6,051
function addresses** stay fixed. Only `generated_1A7260.c.o` changes among
**698 objects**, in text/relocation/symbol/string sections. All **189,088
protected data bytes**, **82 headers**, prior guard rows and conversion CSV
rows remain unchanged. Exactly sixteen guard rows are appended, and **792
immutable input fingerprints** pass.

Actual recount: total **4,482 / 5,515 (81.27%)**, Game
**3,809 / 4,842 (78.67%)**, Init **492 / 492**, Debugger **181 / 181**;
zero drift and **1,033** different C functions. This is one new exact C
function. Converted function/byte totals remain unchanged. **206** more
matches reach 85% at the current denominator.

Scoped Graphify AST refresh covers the owner and six tools files, retaining
all **60,384** old node IDs: **60,426 nodes / 113,793 links**,
with zero lost nodes. This is not a full-corpus extraction. Private evidence
and frozen inputs remain under
`conker/build/game-motion-piece-15179fe0-screen/`.

## Resume boundary

Next: **`func_1517A3A0`**, the same-owner **169-word** routine with the
original **0x58-byte frame**, spanning `0x1517A3A0..0x1517A644`. Recover
its two pointer arguments, remaining argument width and category-dependent
branches before credit. `func_15179DB0` is the other remaining owner stub.

Tools commit `ec0a0a3` banks the six qualification files before the consumer
source, sixteen guards, README aggregate rows, this note and concise indexes.
Keep the 85% goal
active; do not push. `64CBFDOGL` has no host source checkout at the available
path, so there is no host adoption or runtime claim. Release stays frozen.
