ï»¿# 1885 - Actor point-pair transform match - 2026-10-30

`func_151D5714` replaces its zero-return placeholder in
`conker/src/game/generated_200930.c`. Its complete **57 words / 228 bytes** match
retail after **eight checked scheduling guards**. The raw compiler body is not
byte-exact. The existing O2/g3 profile, two call bindings and 88-byte frame are
preserved; there are no inserted or omitted instructions.

Tools commit: `5f18d9dd767e9426c50b72cfd0feb25140af6970`. Ignored evidence:
`conker/build/game-actor-pair-transform-151D5714-match/`.

## Recovered behavior and interfaces

The seven arguments are an actor, two point pointers, a joint word, a float scale,
a kind word and a mode word. The shared public declaration remains unchanged.
The actor is required: the original routine dereferences it without a null gate.
A null actor matrix or low tag nibble equal to 15 skips both helper calls.

The selected matrix is `actor->unk1D4 + (u8)joint * 64`. Two input point pointers
and two distinct local output pointers are submitted to `func_15145EA4` with
count 2. The first transformed point is the origin; the second becomes the
componentwise endpoint-minus-origin displacement. The cached selected matrix,
actor, scale representation, zero-extended low kind byte and full mode word are
then submitted to `func_151D4408`. The routine returns void, as both callers expect.

The local declaration of the final provider describes its assembler argument
word boundary: `f32, s32, s32`, with the explicit `(u8)kind` conversion at this
call. This provider is still opaque assembly, not a recovered C definition.
Its original incoming kind read is `lbu` at its `SP+0xE7`. A narrow local kind
prototype let IDO assume the consumer would truncate the value and emit a full
word load at the caller. The selected declaration and explicit cast instead
reproduce the original outgoing byte load without changing the public header.
This does not settle the provider's eventual C signature.

The frame saves RA at `SP+36`, output pointers at 44/48, input pointers at 52/56,
cached matrix at 60, displacement at 64..75 and origin at 76..87. Scale, kind,
mode and actor homes are reread after the first helper. Guest provider mutations
check the cached matrix against changes to the actor and check those late home
reads. Such private stack mutations are guest instruction tests, not portable
C alias guarantees.

## Closed scheduling proof and guard boundary

All differences lie within words 39..47, bytes `[156,192)`. Word 40 is the same
`sub.s f8,f4,f6` at the same PC. The other eight words reschedule disjoint stack
loads/stores and argument-address setup. Both versions contain the identical
nine-instruction multiset with no calls, branches or relocations in the window.

A symbolic evaluator compares all 32 GPRs, all 32 FPRs and final memory. Reads
at `SP+60..63`, `+104..107`, `+111` and `+112..115` are disjoint from stores at
`+68..71` and `+72..75`. The arithmetic operands and schedule point remain fixed.
An altered subtraction is rejected by an independent DAG control.

Each guard checks its literal expected word and empty binding preimage. Sixteen
actual padder controls corrupt each expected word or binding separately and must
be rejected. The inherited CSV remains an identical prefix. No guard changes
control flow, arithmetic, inserted/omitted words, compiler profile or another
function. Raw and retail final guest states agree; their private access orders
differ. Full access and fault-prefix equality is claimed only for retail versus
the normalized code, whose complete instruction stream is byte-exact.

## Qualification

- **2,816 guest cases / 8,448 executions** compare original, raw and normalized
  bodies. All 57 target words execute. Joint/kind bytes and all actor tag bytes,
  matrix-null and tag exits, signed zeros, finite cancellation, subnormals, two
  stack phases, source null/all-zero gates and post-provider mutations are covered.
- The original **117-word primary helper** is connected on selected cases;
  **113 words** execute through fixed/float-matrix and transform/translation routes.
  Its conversion, point-transform and translation endpoints are bounded services
  with independent argument/list/output checks. Full matrix math is not newly
  requalified here; the final effect provider remains opaque.
- **86 access cuts**, including five delay-slot cuts, compare retail/normalized
  complete state, access prefix and fault context. Twelve rebase cases exercise
  three independent entry/callee layouts across address boundaries.
- The aligned ROM census finds only JALs at **`0x9E9DC` and `0x9ED7C`**, with no
  aligned literal function-pointer words. Complete 23-word callers
  `func_150714E8` and `func_15071888` already match retail in the current linked C.
  **512 cases** exercise all 46 caller words, their 40-byte frames and the nested
  root/primary protocol. Their source and shared header are unchanged.
- Native SDK32 **O0/O2/O3 each pass 196,608 cases** with trapping UBSan, the real
  recovered primary C, both matrix routes, null/zero/finite points, all joint/kind
  and tag bytes, four finite output-pair patterns and 12 scale representations.
  Every actor byte is checked. Scale bits are injected via a union to avoid a
  host float-return ABI quieting a signaling NaN in the harness.
- **15 effective controls** compile and fail semantically through both IDO/guest
  and native execution: extra actor gate, tag mask, joint width, stride, count,
  input/output pair ordering, reversed subtraction, addition, scale, kind width,
  kind zero, mode zero, late matrix reload and omitted final call. Compiler or
  interpreter failures are not counted as successful controls.
- Both tools copies pass eight fresh canonical checks and shared checks. The
  adopted production repeats two installed checks per copy, reusing six prior
  checks only after full module/input/artifact fingerprint equality.

These are bounded guest/native validations, not full effect execution, general
FCSR equivalence, portable C fault behavior or hardware/gameplay acceptance.

## Complete owner, image and status

The actual five-command GLOBAL_ASM Make recipe reproduces the qualified object.
Selected, complete-owner and executed-command diagnostics are empty. All **27
other owner functions** and pools remain identical. The full-image prediction,
first link and adopted ELF agree: **176 changed bytes = 175 code bytes + one
symbol-size byte**, metadata 0, exclusions 0. All **6,055 other function bodies**,
all **6,056 function addresses**, the C inventory CSV and protected Game data
(**189,088 bytes / 720 owners**) remain fixed.

Raw C SHA-256: `ed1e22dea969b7b4540e08a91986f1f0ab292c91cfb909de661f3332b7dc8085`.
Owner source SHA-256: `40d4acca044b8dc8f9a550005f020cc865a41fa35b3d3ae6a405a940e86a5fd9`.
Padded owner SHA-256: `f7d60d33cdeae0b14adc35ba439cc100f6a0a835fd7c46944e3ce0a46adaf128`.
Adopted ELF SHA-256: `3b36f423f4d83be4236dca0c6a4496441460fe07a199c8b3448fcd16920ec5f6`.

Fresh recount: **3,962 / 5,506 (71.96%)** total exact C;
**3,289 / 4,833 (68.05%)** Game; zero drift. Init remains 492/492 and Debugger
181/181. The 75% goal remains active with **168 more** matches needed for 4,130.
Next private screen: `func_1512C068`. Root README changes are its two aggregate rows only.

All 2,093 inherited mirror dirty paths and its HEAD are preserved; three new
qualification modules are added there. Tools are committed before the consumer;
nothing is pushed. The scoped eleven-file Graphify refresh retains prior nodes
and valid relationships and retires the obsolete signed placeholder return.
Historical communities remain historical; no full-corpus re-extraction or global
clustering is claimed. Routine work used zero Claude calls or dependency changes.
