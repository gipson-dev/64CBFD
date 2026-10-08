# Game Source Effect Constructor Direct Match

Date: 2026-10-06. Starting checkpoint: `6ba5a58b`.

Recover **`func_1513D2F0`, 114 words / 456 bytes**, VA
0x1513D2F0..0x1513D4B8, ROM 0x16A7A0..0x16A968, frame 0x38, in
[game_169510.c](../../conker/src/game_169510.c).
All instructions emit directly from semantic C under existing O2/g3.
Replace the seven-instruction false zero-return stub and its slot padding.
No new guards, compiler profile, shared header, symbols, data or metadata.

## Recovered Contract

Keep the existing twelve-argument ABI: descriptor pointer, table address in a
signed word, five unsigned bytes (kind/mode/first/setup/variant), signed
resource/extra/payload words, unsigned channel byte and signed context.
Working field names describe observed storage, not recovered original types.

- Read flags at descriptor+0x40 **before allocation**. Bit 23 selects category
  0x56 with priority over bit 25's 0x49; neither selects 0x1C. Bit 31 selects
  allocation mode two instead of one. Call `func_15167A68(category, context,
  payload+0x110, 1, channel, allocationMode)`. Null stops without later calls
  or result stores. Tests use safe signed payload additions, not overflow UB.
- On success, copy **88 live descriptor bytes** to result+0x18, including
  unspecified alignment bytes. An allocator mutation changes the copy, not
  the already-captured allocation flags. Do not invent padding initialization.
- Store bytes kind/mode/first/setup/zero at +0x70..+0x74. Zero 16 bytes at
  +0x100. Call `func_1513FFF4(result+0xC0, result[0x18], variant)` using the
  live post-copy/post-zero byte, then `func_151400D0(result+0xC0, table)`.
  Existing helper signatures use explicit 32-bit pointer casts; no shared
  prototype churn or portable 64-bit pointer claim. Ignore helper returns.
- Set +0x10 to one, +0x14/+0x98/+0x90 words and +0x95/+0x94/+0xA0 bytes to
  zero; store resource at +0x9C and extra at +0xB8. Copy the raw default float
  from `D_800A5184` to +0x78 **after helper callbacks, before view callbacks**.
  Its retail value is **0xC61C4000 / -10000.0f**, not positive scale one.
- Clear four pointer slots +0xA4..+0xB0 and owner +0xB4. For nonzero resource,
  run views for inclusive indices zero through live signed `D_80082FA0`;
  reload the bound after each callback. Store each `func_1515D480(resource)`
  return, then always store `func_1515D440()` at +0xB4, even for negative
  initial bound. Resource argument stays captured despite actor-field mutation.
  Return the actor pointer.

No invented four-view clamp. Bound four writes a fifth pointer into +0xB4,
then the owner return overwrites it. That case is a bounded ordinary-memory
diagnostic, not evidence that a fifth retail view is valid. Callback helper
indices outside real table domains are likewise ABI diagnostics only.

The actual 96-word `func_1519ED84` wrapper has flags **0x045C0081**: bits
23/25/31 are all clear, so its allocator category is **0x1C**, mode one.
On success it publishes the saved source pointer to actor+0x110. The retained
27-word `func_1519EF04` later uses that pointer for eight output stores.
All three routines remain directly exact; backend bodies are not adopted by
these controlled callback tests.

## Compiler Evidence

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_source_effect_constructor_candidates.py):
**16 forms x four profiles + six schedule forms x four profiles + nine
default-order forms = 97 controls**. Baseline has 113 words/frame 0x38 and
81 differences. Explicit sign-bit test produces 114 words with 23 differences;
byte-order correction reduces this to 20, captured-default scheduling to
eight, combined scheduling to five. Default-before-+0x98 gives four; later
+0xA0 clear gives two. Combine the direct early default assignment and later
+0xA0 clear: **114 words, frame 0x38, zero differences**. No assembly injection
or expected-word guards. Plain O2 gives 33 differences; O1/g3 and O1 give
152 words and 151 differences. All isolated diagnostics empty. Tests bind
every candidate length/frame/difference count, including overflowing tails.

## Qualification

[Nine constructor tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_source_effect_constructor_match.py)
use unchanged shared guest/native runners and an independent byte reference:

- **6912 guest cases / two bodies**, selected C and retail: eight flag
  combinations, null/success, context widths, two stack phases, six live-bound
  plans, zero/positive/negative resource, callback mutations and three padding
  patterns. Compare full external memory, twelve argument widths, ordered
  read/write/call traces, scratch stores and return. Clobber volatile GPR/FPR
  across callbacks; saved lifetimes hold. Cover **all 114 words**.
- **2048 selected guest cases**: every byte value in all six byte arguments,
  high incoming bits, four safe payload boundaries and both stack phases.
- **18 guest cases / two bodies**: nine raw default patterns with zero/nonzero
  resource, including signed zeros/subnormal/infinities/quiet/signaling NaNs.
  Helpers change the default before capture, views after it. This is raw
  transport, not arithmetic or hardware FCSR/exception-mode qualification.
- **576 actual wrapper/constructor guest cases**: mode/lifetime/channel/context,
  null/success and six bounds. Complete descriptor/callback/memory comparison
  and source-pointer publication. Exactly **204 reachable instruction words**:
  96 wrapper and 108 constructor. The wrapper's fixed flags cannot reach six
  alternative category/mode branch words; standalone tests cover those.
- **131072 native actual-constructor cases**: all kind/mode byte pairs with
  success/failure, all other byte widths, flag priority, signed resource,
  callback descriptor/helper/default mutation and inclusive live-bound plans.
  Typed callbacks, 32-bit pointer/layout checks and complete descriptor/output/
  global footprint. Snapshot the copy at call time; no expired local reads.
- **576 connected native cases** run actual wrapper and constructor C. On
  successful publication, mutate the source and run actual retained updater
  C, checking eight output stores and whole storage. Backend helpers remain
  controlled callbacks. Unspecified wrapper padding is compared to its copy
  snapshot, not assigned invented values.
- Six compiled negatives detect stub, wrong category, short descriptor copy,
  wrong default, invented four-slot clamp and captured instead of live bound.

The previous packet test now connects the actual recovered constructor rather
than asserting its former placeholder. Historical Note 1045 remains an
accurate checkpoint record. Fixture-only corrections: pass phase to runner
initialization before argument placement; use 204 reachable connected words
instead of all 210 because fixed flags skip six constructor branch words.
Initial native compiler indentation warnings were corrected in the fixture.
Production required no changes for these test expectation corrections.
All **43 focused post-link tests pass in 487.777 seconds**, no skips: nine
constructor, nine source effect packet, eight actor packet, six configuration
packet, six address-record allocator and five core guard-relocation tests.
The standalone constructor driver also completes all 97 controls.

## Linked Audit

`make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress`
passes. All 114 linked words equal retail; target SHA-256:
`ce796cc8d6438738fb4298586cadbd86b52d48fd1709455f1e3d5f57217a622b`.
Only `func_1513D2F0` changes across **6059 slots**; all addresses/sizes fixed.
Protected `.init`, `.init_data`, `.debugger`, `.game_data` unchanged. All
**720 Game-data owners / 189088 bytes** retail-exact. All **10660 guards**
identical and in order. The owner's **48 preexisting warnings** remain equal
after normalizing shifted line locations; **zero new warnings**, none in the
new body. Do not describe this broad owner as diagnostics-empty. Existing
Makefile duplicate generated_12D630 recipe warnings remain unrelated.

Measured totals **3324 / 5462 (60.86%)**, Game **2651 / 4789 (55.36%)**
exact; **2138 different**, zero drift. Init492/492 and Debugger181/181 stay
exact. Converted totals unchanged because the false stub was already C.
README receives aggregate measurements only. Ignored receipts under
`conker/build/game-source-effect-constructor[-test]/`; baseline snapshot
`conker/build/game-source-effect-packet/after.json`.
Tools-check, compileall and diff-check pass; **3303 relative links across
28 documents**, zero broken. No sibling source/build/save/frozen
Release change, runtime launch, full gameplay/backend/host claim or push.

## Next Work

Inspect **`func_1513FFF4`, 55 words / 220 bytes**, VA 0x1513FFF4..0x151400D0,
ROM 0x16D4A4..0x16D580, frame eight, retained as raw assembly in this owner.
The [retail body](../../conker/asm/nonmatchings/game_169510/func_1513FFF4.s)
narrows index/variant to bytes, skips index 255, reads unsigned dimensions
from 12-byte `D_80090B60` records, subtracts one modulo 65536 and writes
eight halfword corner coordinates according to the variant's low two bits.
Recover types, modulo truncation and store/branch ordering before installation;
do not replace the retained body with an unqualified approximation. The
constructor table helper `func_151400D0` and backend providers remain separate
follow-up boundaries. Other pending work: 228-word `func_15152190` placeholder
and semantic/non-matching 255-body/256-slot `func_1513264C` constructor.

Preliminary isolated screen completed **40 controls** (ten forms/four profiles)
without installing this helper. Explicit table-record pointer, unsigned
halfword dimensions and shared signed-word coordinate temporary emit all
55 words/frame eight directly under O2/g3. Repeated expressions emit 71
words; a shared halfword temporary emits 63; a shared word without explicit
record pointer emits 55 with 25 allocation differences. Typed pointer ABI is
material: keeping a signed-address parameter emits 50 words/frame zero and
55 differences. Before installation, recover the owner-local void/pointer/
byte prototype and caller casts, qualify modulo dimension boundaries and
connected constructor use, then audit the whole owner again. Receipts/source
are retained under ignored `conker/build/game-source-effect-constructor/next-helper/`
and `screen-next.py`. This is compiler evidence, not installed C or behavioral
acceptance; retained raw assembly stays untouched in this commit.
