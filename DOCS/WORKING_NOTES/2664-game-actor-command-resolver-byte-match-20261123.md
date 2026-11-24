# Actor command resolver byte match - 2026-11-23

`func_1506E46C` replaces its zero-return placeholder with the complete actor
command resolver. Semantic C emits **95 words / frame 48**; independently
proved index-home lifetime and register/control scheduling reproduce all
**100 retail words** using **95 expected-word guards, eight insertions and
three omissions**. This is a guarded C match, not direct raw C identity.

Total rises from **4,643 to 4,644 / 5,528 (84.01%)**; Game becomes
**3,971 / 4,855 (81.79%)**. Init stays 492/492 and Debugger 181/181.
There is **zero address drift**, 884 different functions and **55 more to 85%**.

## Original routine, providers and actual callers

The complete original is
`conker/asm/nonmatchings/game_981E0/func_1506E46C.s:1..114`, VA
`1506E46C..1506E5FC`, ROM `9B91C..9BAAC`. The existing SDK32 interface remains
`s32(s32 actorWord,s32 commandWord,s32 mode)`, with explicit actor/command pointer
casts inside the recovered body. Shared headers and caller declarations remain
fixed. The former typed stub emitted 24 bytes including incoming argument-home
stores; its symbol extent becomes 400 bytes.

1. Capture the full command and its low15-bit index before providers. If bit
   0x200000 is set, mode0 calls `func_100107F8(actor)`, mode1 calls
   `func_10010894(actor)`, and mode2 calls `func_151F2CDC()`. Any nonzero result
   rejects the first two; exactly 1 rejects the last. Other modes bypass gating.
2. If the captured index is at least 2000, read the live actor byte+0x288 and
   its live pointer entry in `D_800BE5A8`, then word[index-2000]. Zero rejects.
   Preserve command&0xFF200000. Nonzero preserved flags combine with the low24
   replacement bits; zero flags retain the complete replacement word.
3. If the resulting command's high16 bits are nonzero, call `func_150ADA20`.
   Its low byte may not exceed the captured command high byte. On acceptance,
   keep the low15 bits and, if the high-word low5 bits are nonzero, replace them
   with `func_1000F568(low15,choiceCount)`'s full word. Do not mask its result.
4. Only success performs the final command store and returns 1. Failure returns 0
   while retaining arbitrary provider effects. Command/index snapshots stay
   captured; the actor selector and replacement pointers stay live until read.

The actor gates have actual `s32(struct127 *)` definitions in init_EB00.c:850/870;
the choice provider is `s32(s32,u32)` at init_EB00.c:357. `func_151F2CDC(void)`
is defined in libultra/audio/game_21FC90.c:148. The random provider's existing
`s32(void)` declaration is used. The table initializer in generated_43D00.c
and the actual source/object/header/ROM inputs are frozen. Provider bodies are
not replaced by their stubs or credited as new transitive matches.

Original callers `func_1506E5FC`, `func_1506E898` and `func_1506E8D8` are each
complete 16-word routines. They load the actor pointer from D_800D154C, pass
the command address D_800D1580, supply modes0/2/1 in the JAL delay slot, and
consume the Boolean result. Success calls1506BA4C/1506BB64/1506BAD8 respectively
with (300,1800); failure bypasses that call. Their complete original routines
are executed with the target connected, keeping all other providers opaque.
Other C/ASM callers and all unrelated linked bodies remain unchanged; no extra
caller matching credit or gameplay/audio acceptance is claimed.

## Source recovery and independently proved normalization

The initial semantic draft emitted 90 words/frame48. Seven switch/index-sharing/
positive-threshold forms and eight index lifetime forms were measured. Sharing
the index and options variable incorrectly shrank the frame to 32; it was not
selected. Seven additional explicit control/flag forms did not improve the fit.
The selected ordinary switch/positive-threshold form keeps independent command
and index snapshots and emits 95 words/frame48. All 327 other raw definitions,
pools and diagnostics remain fixed. No volatile qualifier or compiler-profile
change is introduced; existing O2/g3/MIPS2 remains in force.

The normalizer derives words and bindings from fingerprinted raw C output. It
keeps the index in the retail V1 lifetime, establishes its SP+24 home around
the three gate calls, moves the captured command home from SP+44 toSP+40, and
reuses SP+24 for the later options lifetime. It closes temporary-register roles,
clones the necessary home loads/stores and argument move, removes redundant
copies, restores likely/non-likely delay-slot schedules, and retargets branches.
No retail payload is imported by the normalizer. All 95 source words and seven
binding sites are guarded; the output has100 words in the same 48-byte frame.

A separate instruction interpreter imports neither this normalizer nor its
word map. It checks 68 symbolic paths with arbitrary 32-bit command/mode/provider
results. Modular affine address terms reconcile indexed pointer arithmetic;
public-memory terms preserve actor/command/table aliases. Ordered reads, calls,
writes, full public memory, return words, incoming argument homes and o32 saved
roles agree. Dead registers and provider outgoing-home clobbers may differ
independently. Twenty behavior mutations reject by predicate/public/ABI
observation; a complete T0/T1 rename and index/options private-home swap pass.

Scope is ordinary mapped nontrapping RAM and compatible returning o32 providers.
Private-frame/incoming-home exposure and code/return-address reflection are
excluded. Raw complete private/fault identity and transitive helper semantics
are not claimed. Padded/retail complete state and fault prefixes are checked
separately by literal instruction execution.

## Fresh validation and whole-image evidence

| Run | Elapsed | Gates |
| --- | ---: | --- |
| preinstall-primary | 121.053s | 5 fresh / 0 reused |
| preinstall-sibling | 103.674s | 5 fresh / 0 reused |
| installed-primary | 97.136s | 5 fresh / 0 reused |
| installed-sibling | 96.886s | 5 fresh / 0 reused |

- **2,124 guest cases per stream** across raw, both padded targets and retail:
  low15 index boundaries, all four meaningful mode classes, gate result 0/1/2/-1,
  all 256 random-byte values against boundary thresholds, replacement/choice word
  widths, live selector/table mutations and command aliases with actor words,
  table-pointer words, row entries and the provider marker. All reachable retail
  words execute; word 35 is an unreachable duplicate home store, retained literally.
- **89 complete dispatched/access fault-prefix triples** for both padded streams
  and retail. **24 connected cases per stream** execute three complete original
  callers: 10 post-action calls and 14 bypasses. Delay-slot arguments, Boolean
  consumption, public effects and restored caller state agree.
- **2,096 SDK32 native cases at O0/O2/O3**, strict aliasing and UBSan, typed
  actor/command/table/row backing, offset assertions, endian/pointer codecs,
  complete public/guard comparison and all row canaries outside the active
  windows. Actor-word, row-word and marker aliases are included. The 28 pointer-
  object word aliases stay guest-only. Twelve source controls reach known
  comparison exits; no signal, compile failure or sanitizer trap counts.
- Both isolated strict target padders reject **204** changed-word/binding
  controls. **12 GNU links /96 guest runs** cover four independent code, callee
  and table arrangements, including signed HI16/LO16 carry.
- Actual Make reproduces the complete production owner. All **327 neighbors**,
  bindings and pools remain fixed. Its existing `func_1506EE60` is 80 bytes for
  a 76-byte slot; the production generic padder preserves its original 80-byte
  .game_overflow section and trampoline. No whole generated-owner strict-pad
  claim is made; both target padders are strict, and the complete generic owner
  plus every linked section is audited without excluding the old overflow.
- Frozen old C plus only original target ASM reconstructs an independent full
  reference. Prediction, actual C link and production Make agree byte-for-byte:
  **299 changed bytes / zero exclusions**. Named definitions
  and string values are reconstructed, including the target extent change and
  0 predicted reordered symbol records.
  All 189,088 protected Game bytes /720 owners, other function addresses/extents,
  conversion rows, layouts, headers and prior guards remain fixed.

```text
before ELF: 8b6184f9c38df6e054d3cf0dc91552c7bc83baabd9dc9f724f679802a6e75cfd
after ELF:  5352a14473b8a21c274371d6e8ecc9a72d3483d6a3fb4bd8922cc3aa34e21dc6
owner:      1fe0e79ac5aaf3794c75593ff3af85e5abb24750ee2019db0e42f439ef1ca3e5
```

Two fixture issues were diagnosed before the final fresh suite runs. The
independent reference's temporary basename changed a local FILE symbol and grew
the string table by 3 bytes; using the production `game_981E0.c.o` basename restores
the exact original ELF geometry, with no metadata exclusion or relaxed check.
A native provider's write to a byte guard used host word byte order; its explicit
big-endian guard codec was corrected while typed row writes retain host word
order. The source body, normalized instructions and production remain unchanged
through both fixture corrections.

The 95 rows append to the prior CSV bytes. Production Make holds only the inherited
guard dependency timestamp old with `-o retail_word_patches.us.csv`; the changed
source rebuilds and reads the new guards. Prior unchanged receipts are retained
by fingerprint, not described as fresh tests. Shared tools checks pass.

Tools commit `339d7ad6095859049a9091668a2bcc45b426515a` precedes the consumer
source/guards/pin/docs commit. The dirty real tools sibling is preserved through
an isolated pinned overlay. Host configurations consume binary artifacts and
do not directly reference this C owner; no host build or Release change occurs.

Codex resolved the work locally with zero Claude model calls. Graph receipts
separate normal refresh, observed hook completion and scoped AST extraction with
old-ID retention; this is not full-corpus re-extraction. README changes only its
aggregate rows. Five DOCS indexes receive a short entry while every prior byte
is preserved. Continue the active 85% goal from this banked checkpoint; the larger
renderer15197148 remains private on its older baseline.
