# 2656 - Actor effect ring update guarded byte match

Date: 2026-11-23. The total 85% matching goal remains active.

`func_15196748` now has its complete semantic C body in
`conker/src/game/generated_1C2C60.c`. Its **257 words / 1,028 bytes / frame 56**
match retail after a qualified source-derived transform. This is a guarded C
match. Raw compiler output is **256 words / frame 56** and is not byte-exact.
Original: `conker/asm/1C2C60.s:1157`, VA `15196748..15196B4C`, ROM
`1C3BF8..1C3FFC`. The default O2/g3/mips2/o32 owner profile is unchanged.

Fresh production recount: **4,636 / 5,528 (83.86%) total**, Game
**3,963 / 4,855 (81.63%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift, **892 different**. **63 more matches** reach 85% with
this denominator. Conversion rows are unchanged because this routine already
counted as C while it was a zero-return placeholder. One new match is credited.

## Recovered behavior and actual caller

```c
s32 func_15196748(u8 *owner);
```

The routine captures the owner's record and payload pointers once, then:

1. Rejects an almost-empty ring when payload kind bit 0 requests expiration.
2. Walks active records backward from the tail toward the live head, wrapping
   by the unsigned byte capacity. It integrates velocity and position, resets
   the mark byte, decrements signed delay or lifetime, conditionally calls the
   spawn helper, and advances size. Negative lifetime clears kind bit 1 and
   retires entries by advancing the live head and decrementing the byte count.
3. Applies the forward and reverse mark ramps selected by kind bits 1 and 2.
   Both use the original do-at-least-once behavior, signed16 remaining counts,
   and wrapping unsigned8 ramp arithmetic. The reverse loop tests its next
   cursor against the tail after decrementing, preserving the retail boundary.
4. Invokes optional sound, auxiliary and boolean tick callbacks through their
   signed selectors. A false tick callback returns zero immediately.
5. Reloads the live count/head and copies the head position through the captured
   record pointer, or writes positive floating zero when the ring is empty.
   It returns one on continuation.

The payload uses the existing recovered 0x90-byte type. Records use a 0x24-byte
type with genuine three-float arrays and offset-named unknown fields. The C
loads the existing `u8 *` owner fields before casting. Callback mutations may
replace public pointers, records, live cursor/count fields, selectors and time
globals: captured pointers remain captured, while actual retail reloads remain
live. Unknown field semantics are not invented.

The complete original **100-word `func_15147740`** dispatches this update through
`D_8008A200[2]`, passing one pointer word. A zero result leads to the release
path through `func_1516972C`. The frozen compiled caller also matches all 100
original words. Seventy-six guest cases execute that complete original caller
per stream; the release provider is bounded, not claimed reconstructed.

## Callback signatures repaired without extra matching credit

Four existing no-argument placeholders could not correctly express these calls.
They now have the original argument interfaces, but remain unrecovered stubs:

| Function | Interface | Raw words before/after | New matches |
| --- | --- | --- | --- |
| `func_15198110` | `void(u8 *owner, s32 index)` | 3 / 4 | 0 |
| `func_15198570` | `s32(u8 *owner)` | 3 / 4 | 0 |
| `func_151987CC` | `s32(u8 *owner)` | 3 / 4 | 0 |
| `func_1519897C` | `s32(u8 *owner)` | 3 / 4 | 0 |

The spawn placeholder is now void; the three boolean placeholders still return
zero. These edits do not recover their retail bodies. The existing point-sound
owner typedef gains its struct tag so the recovered sound table callback has
the same C type; its machine code is unchanged. Actual callback entry-argument
liveness is audited through branches and first-call frontiers. Unpassed live
registers are not silently treated as extra arguments or call-clobbered values.

An independent ABI-only C variant keeps the old parent stub and changes only
these interfaces/tag. Its 65 non-helper functions match the frozen owner; all
68 candidate non-parent functions match that independent variant. The other
64 neighbors, relocations, literal pools and diagnostics stay fixed. The four
new four-word placeholder bodies and zero-filled retail slots are explicitly
included in the full-image prediction; they are not excluded or credited.

## Instruction, semantic and ABI qualification

The normalizer consumes every pinned source operation, all 15 relocation sites
and 256 expected-word guards. It performs **31 mapped word replacements** and
clones one existing flag-test ANDI into a retail branch delay slot. There are
**one insertion and zero omissions**. It derives branch destinations from the
index mapping and retains binding identities; retail words are a separate
comparison, not the generator. The complete old guard CSV remains its prefix.

Four inductive symbolic regions cover entry, forward ramp, ramp gate and reverse
ramp with 2/6/3/6 paths. Two hundred outside words are literal/control-address
identities or proved commutative forms. The proof admits arbitrary mapped public
aliases through fresh reads and ordered writes, handles branch-likely annulment,
and compares register roles, HI/LO and public effects without a loop iteration
bound. All unchanged floating operations and FCSR behavior stay outside the
rewritten regions. Each stream has 128 dead-role checks extending beyond opaque
calls until definition/return; the proof does not assume unpassed values die at
a call. Its domain is ordinary mapped public memory with a disjoint valid o32
private frame, not arbitrary machine faults or recovered provider internals.

- Three independent alternative-allocation/eager-test positive controls pass;
  39 well-formed semantic mutations fail for meaningful transfer differences.
- Guest checks run **604 cases per raw/normalized/padded/retail stream**, including
  84 real-preset cases and eight large-capacity cases. The independent memory,
  return and ordered-call oracle agrees; raw private bytes also agree.
  Normalized/padded complete state, dispatched words and events equal retail.
  Only two statically unreachable duplicate words are unexecuted.
- Four additional guest-only alias probes cover exact/partial coordinate-output
  overlap and incoming argument-home mutation. These are not native alias claims.
- **312 fired own-access fault prefix sets** compare normalized/padded with
  retail complete state. This qualifies emitted access order, not C exception
  semantics or hardware behavior.
- Native SDK32 checks run all 604 ordinary cases at **O0/O2/O3**, strict aliasing
  and UBSan, using actual owner/payload/record layouts and initialized array
  guards. They check 12 owner, 14 payload and 11 record fields. All ten effective
  semantic mutations fail by comparison, including replaced-pointer reloads,
  ring boundaries, callback results and zero signs.
- Both complete owner padders reject all 256 changed words and all 15 changed
  bindings: **542 effective rejections**. Both reject oversized bodies.
- Twelve GNU links over four independent code/global arrangements validate
  HI16/LO16 carries and JAL-region constraints against original ASM.

Fresh paired suites run all five focused gates before and after installation:

| Run | Time | Checks |
| --- | --- | --- |
| preinstall-primary | 93.715s | 5 fresh / 0 reused |
| preinstall-sibling | 105.532s | 5 fresh / 0 reused |
| installed-primary | 96.845s | 5 fresh / 0 reused |
| installed-sibling | 101.567s | 5 fresh / 0 reused |


The first assembled suite caught a Python indentation error in the new arity
wrapper. It was corrected before installation and all four accepted suites run
fresh against the corrected files. Earlier isolated semantic checks do not
substitute for those accepted paired receipts.

## Production and checkpoint

Actual Make replay reproduces the entire independently padded owner. The strict
predictor first recompiles frozen old C with old guards, then uses the independent
ABI-only variant plus only the original parent ASM. It reconstructs five code
windows and five function sizes, all named definitions, metadata ordering and
every string-pool byte. Every byte of the production ELF equals the prediction:
**832 changed bytes, zero exclusions**. All 189,088 protected Game
data bytes and 720 owners remain exact. No shared header changes; the complete
debugger object remains frozen. All baseline inputs are audited against the
explicit source/guard/object/ELF/documentation adoption plan. Shared
`make tools-check` passes.

```text
before ELF: e5b2950028dd7a2e711e0500074abbe5790be86c2d390b0ba7eddee9cce9e47d
after ELF:  6909177ec67e462c17df17efb3c902e377fa85c7e8decfff9ad5d39a8fd0be2c
owner:      dfa75f8b8eae67cc0937a693f33b92b8458bf911f33bbd2e15d1d1dd8325313f
```

The disposable paired overlay records 1727 files with explicit sibling,
primary-fallback and task origins. The real dirty tools sibling's HEAD, status
and dependency hashes remain intact. Both host scene configurations consume
binary artifacts and do not reference this C owner directly; no applicable
direct C edit or complete host build root was found at the inspected path.
No host build or frozen Release artifact was used or changed.

Tools are committed before consumer source/guards/pin/docs; nothing is pushed.
Graphify refresh retains all prior IDs/qualification metadata after observed
hook producers terminate. The current definition receives one match; the four
ABI-only stubs explicitly receive zero. Scoped AST retention is not full-corpus
re-extraction. README changes only its aggregate status rows; this note owns the
recovery narrative. Codex is the only writer; Claude calls: zero.

Next audit `func_15196B4C`, the following unfinished effect ring emitter, with fresh
caller/source/ABI qualification. The 85% goal remains open.
