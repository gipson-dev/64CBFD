# Record opacity envelope - direct C match

Verified 2026-10-28. Restore func_150F55C8 in generated_1228D0:
VA 0x150F55C8..0x150F568C, ROM 0x122A78..0x122B3C, 49 words / 196 bytes.
Normal O2/g3 emits every original word directly. No frame, relocations,
new compiler profile, instruction guards or new translation unit are needed.

## Recovered behavior and interface

The interface is void func_150F55C8(u8 *record). Update both its forward
prototype and definition; callers ignore the previous placeholder result.

| Field | Meaning |
| --- | --- |
| +0x18 high signed half | Fade-in duration |
| +0x18 low unsigned half | Hold duration |
| +0x1C high signed half | Fade-out duration |
| +0x1C low unsigned half | Overall duration |
| +0x24 signed half | Remaining lifetime |
| +0x45 byte | Output opacity |

Let boundary = duration - fadeIn. If remaining exceeds boundary, opacity is
(duration - remaining) * 255 / fadeIn. Otherwise, while remaining exceeds
boundary - hold it is 255; afterward it is remaining * 255 / fadeOut.
Integer division truncates toward zero and the store narrows to a byte.
Signed packed high halves and signed remaining values are retained, including
negative values. Their ranges keep intermediate arithmetic within int32.

Direct field initializers let IDO reuse the two packed loads and recover the
original scheduling. The first draft cached the packed words in separate
locals and emitted 50 words; it was rejected. The selected 49-word body has
no compiler diagnostics. The owner retains ten pre-existing Warning 712
pointer/integer diagnostics; the full Make invocation retains its known
unrelated duplicate generated_12D630 recipe warning.

A selected zero divisor is outside valid native C execution. Literal guest
checks retain both original break7 sites and the preceding opacity store.
A fixed HI/LO sentinel is used only to reach the break; it is not a claim
about real hardware division-by-zero results. Both overflow break6 words
remain in the complete byte match, but INT_MIN / -1 is unreachable from
these field ranges. Native checks use nonzero selected divisors.

## Original callers and table routes

The full ROM census finds one direct JAL at VA 0x150F55B0 / ROM 0x122A60
inside func_150F5590. Its 14-word current body is byte-exact. It writes
4096 - remaining * 4, narrowed to halfwords at +0x38/+0x3A, then calls the
opacity updater. Seven original-wrapper cases qualify entry through return.

The sole target-address literal is at ROM 0x231508 / VA 0x8008CA48, slot 10
of the eleven-word D_8008CA20 table. Slot 9 points to func_150F5590.
The table is unchanged and equals the original ROM. Four original dispatchers
execute both callback routes and their disabled route, 48 cases each:

| Dispatcher | Original words | Visited words | Current body exact |
| --- | ---: | ---: | --- |
| func_15168BAC | 14 | 14 | Yes |
| func_15169988 | 48 | 47 | Yes |
| func_15167B44 | 69 | 59 | No |
| func_15167E0C | 195 | 45 | No |

The first dispatcher selects +0xE4; the phase/lifetime updater selects signed
+0x40; the animation updater selects +0x24; the expiry dispatcher selects
signed +0x48. The last test enters at the full parent entry and follows its
lifetime-expiry route through callback, release and return. It does not
qualify the parent's other animation paths. Release is a bounded provider.
Unmatched parents receive no recovery credit. This is instruction and ABI
evidence, not full-game or hardware acceptance.

## Qualification and strict integration

Both active and older tools copies pass eight fresh canonical test methods
and the shared tools checks. After production, each passes two fresh installed
checks; six unchanged semantic checks are reused only with exact source,
module, fixture and qualified-artifact fingerprints.

- 1,609 guest cases, including 217 zero-divisor guard cases, cover 47 of the
  49 words. Only the two unreachable overflow break6 words are unvisited.
  Raw compiler, padded object and retail execution agree in complete state,
  memory, access sequence, PC and delay-slot behavior.
- 96 fired access-prefix comparisons verify literal load/store ordering.
  A zero inactive denominator on the plateau remains safe.
- Native32 O0/O2/O3 each pass 262,144 cases: all 65,536 remaining-lifetime
  encodings under four packed-phase patterns. Typed record fields, the actual
  one-pointer void ABI, whole-object fences and trapping UBSan are checked.
  Seven native semantic mutations fail; eight separately compiled IDO
  mutations fail, including a guest-only zero-divisor boundary mutation.
- Three GNU layouts run 21 guest cases with original, raw and actual-Make
  objects. Three raw/binding corruptions and six full-image corruptions fail.
- The three-command owner Make recipe reproduces the qualified object.
  All 23 other owner functions, bindings and constant pools remain fixed.

The immutable seal covers 16,358 files and 369 focused frozen inputs.
An independent whole-image prediction permits exactly 131 changed bytes:
130 code bytes and one symbol-size byte (12 -> 196). There are zero exclusions.
All 6,056 function addresses, the other 6,055 bodies and 720 protected Game
owners / 189,088 data bytes are unchanged. Progress CSV, callers, shared
headers, Makefile and complete guard manifest remain unchanged.

Raw/original/linked body SHA-256:
1d37e31a89ff6e2172e13d21829c4b58919b1540c7231c779bf815230023aa9a

Adopted ELF SHA-256:
77b67000ba81892c36c0960e2ac4761e31eaf0cb6c3c7774edaf2a915e56690f

Unchanged guard manifest SHA-256:
4d5db7992914b7209e0976f4569be48fd6b3b36a850fc0b35140fc097209b840

## Bank and measured progress

Predecessor consumer: cb58f11e21ccddcd6747aa4612d6e354a46d13a6.
Tools committed first: 1ba1f38716b44d2a17c5804164df56801c00b181.
Preserve all 1,781 inherited dirty paths in the older tools mirror; add only
these three qualification modules there. No push performed. Routine Claude
calls: zero. Graph refresh is scoped AST work with old-node and relationship
retention; it does not claim full-corpus extraction or global reclustering.
Raw receipts: conker/build/game-record-opacity-envelope-match/.

| Section | Byte-exact C | Different | Address drift |
| --- | ---: | ---: | ---: |
| Total | 3,858 / 5,506 (70.07%) | 1,648 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,185 / 4,833 (65.90%) | 1,648 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The adopted native ELF recount leaves 272 more exact C functions to reach
4,130 / 75%. func_151918BC is the next placeholder to inspect; the queue is
only a screen. func_1514E920 remains parked and uncredited.
