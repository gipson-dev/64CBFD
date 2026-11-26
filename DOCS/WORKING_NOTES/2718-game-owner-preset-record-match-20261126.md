# Owner preset record direct match - 2026-11-26

`func_1519021C` replaces the zero-return placeholder in
`conker/src/game/generated_1BA1D0.c`. **All 109 words / 436 bytes and all 12
binding positions emit directly from semantic C**, with the original 144-byte
frame and zero guards. VA `0x1519021C..0x151903D0`, ROM
`0x1BD6CC..0x1BD880`; the function fills its complete slot. No insertion,
omission, alignment tail, compiler-profile or Makefile change. All 60 raw and
padded neighboring functions, pools and the entire guard CSV remain fixed.

Production: **4,697 / 5,528 (84.97%) total**, **4,024 / 4,855 (82.88%) Game**,
Init 492/492, Debugger 181/181, zero address drift, 831 still different.
**Two more accepted matches reach 85%.** One matching credit; conversion rows
and denominators are unchanged. No caller/helper/host matching credit.

The recovered six-word interface is
`struct225 *(u8 *parentRecord, struct127 *actor, u8 preset, s16 lifetime,
u8 channel, s32 context)`. It uses the existing SDK `struct127`, `Header`,
`Header2` and factory `struct225` types. Descriptive local names are inferred
from the measured fields and caller use, not original symbols. Presets 24..255
return NULL before actor or table reads. For presets 0..23, the routine captures
three float table entries, constants 1/0/5/0 and `D_800A8004`, the actor pointer,
actor ID byte 0x3B, and truncated XYZ at actor offsets 0x14/0x18/0x1C.

The six-byte header holds flags 2 for lifetime -1, otherwise 3, type 18,
signed 16 lifetime 300 for -1 or the supplied lifetime, and subtype 37. Its byte 5
is originally unwritten. The eight-byte owner pair initializes a four-byte
pointer and one ID byte, leaving three original padding bytes unwritten.
No new initialization is introduced. The three integer coordinates form the
existing 12-byte `Header2`. The typed factory receives
`(&header,&position,0,255,209,0,255,0,0x30,channel,context)`.
A successful record receives the eight-byte owner pair at 0x18, eight floats
at 0x20 and parent pointer at 0x40. The allocation request remains48 bytes,
while these copies initialize44 payload bytes; the last four allocated bytes
stay untouched. The captured record pointer is returned even if memcpy's
return register differs. NULL allocation skips all three attachment copies.

The initial body had107 words/frame136. Recovering the conditional expression
`2 | (lifetime == -1 ? 0 : 1)` restored109 words/frame144 and all bindings,
leaving24 stack-offset differences. Declaring the created-record local before
the header recovered the exact original local layout naturally. No dummy
locals, physical register bindings, stack normalization or word guards are
used. Frame offsets: savedS0/RA0x38/0x3C, position0x4C, parent0x58,
values0x5C, owner pair0x7C, header0x84. The fifth channel argument is reloaded
as the low unsigned byte of its word home; context retains all 32bits.

The sole named direct original caller is `func_1518F5D0`,125 words with a
**200-byte frame**. Its original ASM equals the ROM. Its production C remains
an unchanged zero-return placeholder, so original caller execution is a
qualification fixture, not production caller restoration or gameplay proof.
On successful main allocation it forwards the main record, actor, a signed
byte selector narrowed to u8, signed 16 lifetime, channel and context. Selector-1
skips the child; otherwise the returned child pointer, including NULL, is
stored at main-record+0x84. It returns the main record. The aligned whole-ROM
census finds one direct JAL pattern at `0x1BCBC4` and no aligned pointer words.

Validation:

- Both complete production padders agree with the actual three-command owner
  Make recipe. Four preexisting compiler Warning712 diagnostics remain at the
  two `func_1518E4A0(arg0)` and two `func_15190454(arg0)` calls. Their normalized
  diagnostic signatures are checked before/after, allowing path/line changes
  only. **Zero new compiler diagnostics.** No suppression or unrelated repair.
- Guest:856 cases per each of five identical streams, all 109 target words,
  258 access-fault quintuples. Raw/original/both padded/normalized full private
  memory, GPR/FPR, HI/LO, FP-operation/FCSR, trace and fault states agree.
  The independent reference compares public memory, calls, all copied bytes,
  header/position observations and the returned pointer. All 24 valid presets,
  every invalid byte preset with NULL actor, signed lifetime boundaries, high
  incoming word bits, null/success, mutating providers, output aliasing the
  actor and four rounding modes are covered. Seeded guest padding remains
  observable. Original11-word memcpy executes on nonmutating-provider paths.
  Factory/wrapper services remain opaque; finite software FP and instruction
  fault models do not establish hardware acceptance.
- Native: actual selected C in three separate typed units,4096 cases each at
  O0/O2/O3, strict aliasing/FP, UBSan traps and LTO type checks. The provider
  observes only five defined header bytes and five defined owner-pair bytes,
  all 32 value bytes and the parent word. Only the three unwritten destination
  pair bytes are canonicalized in capture; when a later mutating provider
  overwrites those actor-alias bytes, their now-defined values are compared.
  Source and runtime behavior are unchanged. Typed arenas, canaries, metadata,
  copy order, return and MXCSR agree. All four rounding modes, finite signed 32
  coordinate conversions, invalid-preset NULL actor and mutating/alias paths
  pass. Eight semantic controls complete with comparison exit42; no compiler
  failure, trap or signal is counted as a control rejection.
- Complete original caller:192 cases per original/raw stream,80 connected
  children each, all 125 parent instructions. Literal private states agree;
  the independent semantic leaf-provider counterpart agrees publicly. Main
  allocation failure, selector-1, invalid child presets and child NULL are
  included. Three poisoned child V0 values change the actual parent store,
  proving result consumption. Provider private-stack identity is not claimed;
  other parent services remain opaque. Production parent slot stays unchanged.
- Both scoped padders expose218 word and24 binding corruptions. Twenty GNU links
  and100 guest rebases independently move services, tables and scalar across
  jump regions and signed-low carry seams. Oversize remains visible to the
  generic padder and rejected by the generated padder.
- The existing47 word factory,32 word wrapper,11 word copy, three 24-float tables
  and scalar are pinned to original ROM/frozen ELF. Static helper pins grant
  no new helper credit and are separate from actual copy execution.
- Independent frozen old-C plus original-ASM prediction equals the complete
  private and production ELF: **330 changed bytes, zero exclusions**. All
  189,088 protected Game-data bytes across 720 owners remain fixed. ELF SHA256:
  `a38b534c0e45458bc68c969b339b24adcafce94acf95298b0cbae65e4e92c24a`. Unwritten native bytes are a defined-value comparison
  boundary, not exclusions from complete image comparison.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 135.832 s | 5 fresh / 0 reused |
| preinstall-sibling | 110.816 s | 5 fresh / 0 reused |
| installed-primary | 109.06 s | 5 fresh / 0 reused |
| installed-sibling | 111.267 s | 5 fresh / 0 reused |

All 20 packaged target tests are fresh with identical primary/isolated-sibling
task, source, import and data fingerprints. Shared tools-check passes;
unchanged broad-suite receipts are reused explicitly, not called fresh.
Frozen inputs: 3973; snapshot copies: 2906.
The separately dirty real tools sibling is preserved. Tools commit:
`99bf715cf1ed5118e0a1a6ec622edf11c9757fe7`. Baseline consumer:
`82d006528c881d315db1fa0262c1bf6bfc81695b`. Receipts:
`conker/build/game-owner-preset-record-1519021c-private`.

Zero routine Claude calls and no subagents. Historical generated host target
checked separately; active host implementation remains unqualified. No host
transfer/build/launch, Release change, push, gameplay or hardware acceptance.
Scoped Graphify refresh audits all 61 owner definitions and retains old IDs and
qualification metadata, with actual hook termination observed. It is not full
corpus re-extraction. Root README receives aggregate/date rows only. Goal 85%
remains active.
