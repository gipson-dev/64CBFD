ï»¿# 1887 - Resource query bitmap match - 2026-10-30

`func_15016588` replaces its zero-return placeholder in `conker/src/game_439B0.c`.
Its **55-word / 220-byte body** matches retail after **two checked scheduling
guards**; all three alignment words in its 58-word slot remain fixed. The raw C
is not byte-exact. The existing O2/g3 profile, 80-byte frame, six bindings and all
saved-register lifetimes are preserved. No words are inserted or omitted.

Tools commit: `942ec394dc2a4e6f2692b22ec26aa5fce85d5d1a`. Ignored evidence:
`conker/build/game-resource-bitmap-15016588-match/`.

## Recovered bitmap and query contract

The routine clears exactly eight bytes at `D_800BE580`, then submits **67 queries**
with depth 3 and path `(0x1A, D_800BEAAB, index)`. The selector is reloaded before
every query. A nonzero output size sets the corresponding bitmap bit; the query
return address is ignored. Byte index starts at -1 and advances at each multiple
of eight, where the mask resets to 1. Other iterations shift the mask left once.

Indices 64..66 update bits 0..2 of **byte 8**, which the initial eight-byte clear
does not touch. Existing bits there are preserved unless the query sets a bit.
The recovery keeps the unsized external array declaration used by the existing
consumer. It does not invent eight-byte storage or change the clear length to
nine. `func_15080738` and its index helper read the resulting 67 bits correctly.

The recovered provider already uses `u32 func_1502B020(u32 *size, u32 depth, ...)`.
Its source and original 60-word body consume all three variadic path components,
mask the descriptor to 28 bits, and always write the nonnull output-size word,
including zero on a missing path. The bitmap caller preserves that signature.
The startup entrypoint already declares the routine `void func_15016588(void)`;
this owner now uses the same signature and removes its obsolete local prototype
and placeholder comments. No shared header or provider body changes.

The frame saves S0..S6 at offsets 32..56 and RA at 60. Output size is at 64 and
the mask home is at 68. S0 is the index, S1 byte index, S2 mask, S3 bitmap pointer,
S4 output pointer, S5 selector pointer and S6 limit 67. Local declaration order
recovers the retail homes; placing `index++` before the size test recovers its
independent post-call instruction order.

The mask has no C initializer, but every C path initializes it before use:
`index = 0` reaches the reset arm on the first iteration. IDO emits an unnecessary
load of its incoming stack home, then overwrites S2 with 1 before using it. Guest
fixtures vary that home. GCC reports a false-positive `maybe-uninitialized`
warning for this loop; the native harness suppresses that warning only around
the target definition, keeps the source body unchanged, and retains trapping
UBSan and all other warning checks. No control changes the first index to an
undefined mask path.

## Two-word scheduling boundary

Only words 16/17, bytes `[64,72)`, differ: initializing S0 to zero and completing
the S5 selector address occur in the opposite order. The selector LO16 relocation
moves from byte 68 to byte 64. The closed window contains no memory access,
branch, call or trapping arithmetic. Four independent GNU layouts, including
HI/LO carry boundaries, verify the instruction multiset and symbolic equality
of all 32 GPRs. Four actual padder controls independently corrupt each word or
binding and must fail. The inherited guard CSV remains an identical prefix.

## Qualification evidence

- **688 guest cases / 2,064 executions** compare original, raw and normalized
  code, all RAM/registers, calls, access traces and fault context. Every body word
  executes. Every run makes 67 queries. All 256 selector bytes, size patterns,
  missing-path stages, two stack phases, live selector/bitmap mutations and
  selector aliases at bitmap offsets 4/8 are covered.
- The original **40-word bzero** is connected on selected runs; its eight-byte
  route executes 11 words. All **60 original query-provider words** execute with
  the lower catalog lookup bounded independently. Descriptor flags, early path
  failure, variadic argument consumption and the size store are checked.
- **138 access cuts**, including 27 delay-slot cuts, cover all first 35 and last
  20 accesses plus every 17th intervening access in two full executions. Nine
  root/callee rebase cases use three independent layouts. These are sampled
  prefix tests with complete state comparisons, alongside the closed-window proof.
- The aligned ROM census finds one JAL at **`0x34D74`**, and no aligned literal
  function pointer. **96 cases** execute the original four-word startup window
  at `0x150078C4..0x150078D4`, including the following bounded service. The current
  C entrypoint's complete 124 words already match retail; full entrypoint execution
  is not claimed here.
- **804 consumer cases** execute all 19 words of the original bitmap reader and
  all eight words of its index helper across every valid index 0..66, including
  byte 8. These already matched functions receive no additional matching credit.
- Native SDK32 **O0/O2/O3 each pass 18,432 cases** with the real variadic query C
  and a bounded catalog lookup. All 256 selectors and initial ninth-byte values,
  six size patterns, four mutation modes, three path-failure modes and all 48
  bitmap/canary bytes are checked. A wrapper deliberately decouples the ignored
  return value from output size after invoking the retained provider.
- **15 effective controls** compile and fail semantically through IDO/guest and
  native execution: clear lengths 7/9, first byte index, mask reset, byte boundary,
  mask shift, depth, tag, selector, query index, return-vs-size, byte replacement,
  inverted size test, byte-sized size test and limit 64. Compiler/interpreter
  failures and UBSan traps do not count as effective semantic controls.
- Both tools copies pass eight fresh canonical checks and shared checks.
  Production repeats two installed checks per copy and reuses six prior checks
  only after exact input/module/artifact fingerprint equality.

These are bounded guest/native checks. No portable private-stack/linked-global
alias behavior, full catalog lookup, complete startup execution or hardware/gameplay
acceptance claim is made.

## Complete owner, image and progress

The ordinary C padder and actual three-command Make recipe reproduce the qualified
object. The complete `func_15016500` neighbor, bindings and pools remain identical;
selected, complete-owner and executed-command diagnostics are empty.

The first link exchanges adjacent `D_800BE950`/`D_800BE580` symbol records and their
names. The independent prediction explicitly serializes only this named two-entry
permutation, after checking its frozen offsets, names and definitions. It equals
the first link and adopted ELF with **178 changed bytes = 169 code bytes + one
symbol-size byte + eight metadata bytes**, with zero exclusions. All **6,055 other
bodies**, all **6,056 function addresses**, named definitions, C inventory CSV and
protected Game data (**189,088 bytes / 720 owners**) remain fixed.

Raw C SHA-256: `1a6b8c45f0b189e4d87c0c80d44d1ec9a2b01c538463d6e2c33954c3edfe5cf2`.
Owner source SHA-256: `0a4033e8d71f81b36bf3abd0a36ba1b2dffa1ce92d72c2cba45ce23748d3339f`.
Padded owner SHA-256: `e16546af90c6785c195dcdfee35bbdd709a92e5280cd9e2724c2953faf4ff9c8`.
Adopted ELF SHA-256: `37015d725a53decd1dd3d5d0d04a96d76ee6811bc507d393161fcdcc3946b052`.

Fresh recount: **3,964 / 5,506 (71.99%)** total exact C;
**3,291 / 4,833 (68.09%)** Game; zero drift. Init remains 492/492 and Debugger
181/181. The 75% goal remains active with **166 more** matches needed for 4,130.
Next private screen: `func_151668B8`. Root README changes are its two aggregate rows only.

All 2,099 inherited mirror dirty paths and its HEAD are preserved; three new
qualification modules are added there. Tools are committed before the consumer;
nothing is pushed. The scoped eleven-file Graphify refresh retains old nodes
and valid relationships and retires the obsolete signed placeholder return.
Historical communities remain historical; no full-corpus re-extraction or global
clustering is claimed. Routine work used zero Claude calls or dependency changes.
