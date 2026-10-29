# 1819 - Actor descriptor effect - 2026-10-29

`func_150F9950` now implements its complete semantic body in
`conker/src/game/generated_124920.c`, with interface
`void (u8 *actor, u8 selector, s32 parameter)`. The original name is retained
and the comment describes descriptor geometry and paired effect submission.

## Behavior and recovered interfaces

Look up the actor's key-0x82 descriptor with `func_150FF288`. If it exists,
`func_150FF6E0` fills a six-vector array plus four vectors. On success submit
`func_151D3F14` using the origin, then `func_151D4408` using direction,
velocity, the current matrix base plus descriptor byte 2 times 64, actor,
scale 1.0, selector and parameter. Finally call `func_150FF474` with the
possibly updated origin and six-vector array. A missing descriptor or failed
geometry skips the remaining effect calls. The descriptor is captured across
providers; matrix base and descriptor index are loaded after the first effect.

The existing lookup wrapper incorrectly declared a void result. It now returns
`u8 *` explicitly from the existing canonical
`s32 func_1503195C(u8 *, s32, u32)` provider, with key 0x82 and ordinal zero.
Its actor argument is typed `u8 *`. All 16 compact functions and the entire
padded `generated_12C1E0.c.o` remain byte-identical. The wrapper was already
instruction-exact, so this ABI correction adds no matching credit.

The sole aligned JAL to the target is ROM 0x55DD4 / VA 0x15028924 in
`func_150265CC`. Its original actor-type dispatch selects slot 36 of the
37-entry table at 0x80096CEC for actor type 152. The bounded 20-word route
loads actor from parent frame+0x764, selector from +0x773, passes literal 1,
and replaces the ignored result with 1. This is a caller-window qualification,
not execution or recovery of the entire parent function.

## Compilation and checked normalization

The compiler emits 49 words /196 bytes with the original 168-byte frame and
five call bindings at offsets 20, 68, 88, 152 and 172. Three original alignment
NOPs complete its 52-word /208-byte slot. The six-vector array occupies frame
+0x60..+0xA7; the four vectors start at +0x54, +0x48, +0x3C and +0x30.
The captured descriptor is at frame+0x2C.

Five expected-word guards normalize one closed register-allocation cycle in
the descriptor-index/matrix-address calculation, at offsets 0x60, 0x6C, 0x70,
0x80 and 0x8C. They add or omit no instructions and change no relocations.
This is a guarded C match. Sixteen initial natural type/layout/flow candidates
retain the same five differences or produce worse allocation; none is credited
as direct emission. Retail bodies and all call bindings remain authoritative.

## Qualification and production

Both tools copies pass eight fresh canonical methods and shared tools checks.
Production passes two fresh installed checks per copy; six semantic methods
are reused only under identical module/input/artifact fingerprints.

- 1,024 guest cases cover every body word, all selector/index bytes, incoming
  selector high bits, missing-descriptor/geometry gates and provider mutations.
  Raw C agrees on public memory, calls and vector packets. Original versus
  normalized code agrees in complete state/access order.
- 113 original/normalized fault-prefix comparisons include 23 delay-slot cuts.
  Raw private-register/fault-schedule equivalence and portable C fault behavior
  are not claimed.
- Native32 O0/O2/O3 each pass 65,536 cases with trapping UBSan, typed vectors,
  fresh untyped actor storage and eight effective negative controls. The actual
  corrected wrapper C is included with its provider arguments checked.
- 768 original caller-window cases cover all 20 scoped words and the null gate.
  200 connected original lookup/provider cases cover all nine wrapper words
  and 25 provider words. The route always supplies ordinal zero; this coverage
  is not presented as complete nonzero-ordinal provider execution.
- Five real guards fire; ten stale-word/relocation mutations are rejected by
  the production padder. Three GNU layouts/18 cases preserve original versus
  normalized complete state. Eight IDO-compiled semantic mutations and six
  full-image corruptions are rejected.
- Actual target Make uses five commands with no compiler diagnostics; all
  16 target-owner neighbors are preserved. Production also recompiles the
  corrected wrapper owner and confirms its complete object is unchanged.
- The entire ELF changes by exactly 154 predicted bytes: 153 code bytes and
  one target-extent byte, zero other metadata or exclusions. All 6,056 function
  addresses, 6,055 other bodies and 189,088 protected Game bytes/720 owners
  remain fixed. The inherited guard CSV prefix is byte-identical; five rows
  are appended. Shared headers, layout map and conversion inventory are fixed.

16,631 sealed and 642 focused inputs are audited. The older tools mirror keeps
1,898 inherited dirty paths plus three new qualification modules. Tools commit
`16eddda` precedes the consumer commit. No push is performed.

ELF SHA-256: `062730d9aef5dc979918e8c471770f0df2da59c8fc2558b8bdc9492dfe211c11`.
Target object: `083fe8a4465c5248c1f85723642ff328250d6824c40a65939d6df834e70840f8`.

## Progress and continuation

Actual live-ELF recount: **3,897/5,506 (70.78%)** total and
**3,224/4,833 (66.71%)** Game. Init 492/492 and Debugger 181/181 remain exact;
zero address drift; **233** more exact C functions reach 75%.
`func_1514E920` and `func_151D7000` remain parked and uncredited.

Graphify is refreshed over the two changed C owners, tools and Markdown, with
old-node and still-valid relationship retention. Obsolete target return-type
and lookup-wrapper parameter-type relationships are retired against source.
Missing assembly helper nodes are separately validated from literal definitions
and GLOBAL_ASM ownership; no assembly AST extraction is claimed. Historical
global analytics remain historical; this is not full-corpus re-extraction.

Local receipts and handoff: `conker/build/game-actor-descriptor-effect-match/`.
No host, hardware or gameplay acceptance is inferred from these static checks.
