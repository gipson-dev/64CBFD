# Timed billboard targets direct C match - 2026-11-27

`func_1514A19C` replaces its zero-return placeholder in
`conker/src/game/generated_176A00.c`. All **121 words / 484 bytes**, all
**20 relocation positions** and the original **32-byte frame** emit directly
from semantic C. Zero guards, inserted/omitted words, alignment tail, compiler
profile or Makefile changes. The entire guard CSV remains unchanged.
VA `0x1514A19C..0x1514A380`; ROM `0x17764C..0x177830`.

Fresh production recount: **4,711 / 5,528 (85.22%) total**, **4,038 / 4,855
(83.17%) Game**, Init 492/492, Debugger 181/181, zero address drift and 817
different. One target matching credit; converted totals and denominators stay
fixed. The active **90% goal requires 4,976 accepted matches: 265 more**.
No caller, RNG-helper or host credit is added.

The entry is `s32 func_1514A19C(u8 *actor)` and returns one. The local
72-byte `BillboardTargets1514A19C` describes only observed fields embedded at
actor+0x110. Its names are inferred roles, not recovered original identifiers.
The three independent signed16 timers are at actor+0x12E, +0x12C and +0x154.
Each subtracts a fresh signed32 D_800BE9E4 value using unsigned low-word
arithmetic, narrows and then tests the reloaded signed16 result. Retain all
three live global reads and their wrapping behavior.

When expired, the height timer resets through unsigned integer RNG %6.
Another draw &3 selects the lower/middle or middle/upper interval, and a float
RNG draw interpolates heightTarget. The width and animation-rate timers reset
through unsigned RNG %17 and %15 and sample their own intervals. All endpoint
loads follow the float RNG call. Current height+0x30 and width+0x2C approach
their targets using D_800A5794 and D_800A5798; signed32 animation rate+0x24
advances by the truncated difference scaled by D_800A579C, using a wrapping
unsigned low-word sum. Keep separate single-precision operations and ordered
operands. Do not cache clocks or pre-call endpoints, use signed remainders,
or replace the narrow-and-reload timer tests with wide arithmetic.

The existing `func_1513CFE4` consumes actor+0x24 as an animation rate, so the
candidate's previously generic value fields are named accordingly. That
current dispatcher and all 195 original words are already retail-exact in
the frozen predecessor. Note 1759's historical twelve-byte stub description
no longer describes production; the first stale expectation failed and was
corrected before caller qualification. The parent is unchanged by this work.

The entry keeps its opaque byte interface. The native fixture allocates an
actual typed 344-byte prefix with the 72-byte target subobject, signed rate,
floats and timers at every observed offset. It asserts size, 32-bit pointer
ABI and all accessed field offsets. The old struct171 prefix is too short for
the +0x154 timer and is not used as a whole fixture allocation.

The source fit recovered the real pointer lifetime with one params initializer.
That reduced an initial 123-word form to 121/frame32/five word differences.
Unsigned sum operand order resolved the integer ADDU. Reversing source ADD
operands and named sample captures did not change the four remaining FP words;
product captures also reversed semantic multiplication operands and were
rejected. Twelve declaration/order forms, pre-call snapshots and block-local
captures did not match. Typed params fields resolved all four FP additions
literally; both source expression orders emitted the same exact body. A typed
whole owner still had one word different. The selected params-only form uses
no dummy storage, register binding, gratuitous volatile or FP word rewrites.
All 35 other raw/padded functions and pools remain fixed in this mixed owner:
35 C definitions and one retained GLOBAL_ASM routine.

One packet-only Claude advisory completed with tools and MCP disabled. Its
proposed product-first reversal had already failed independent source screens;
its register-coloring and NaN-payload explanations were not accepted as proof.
Codex's typed-field experiment and complete raw equality resolved the issue.
No further advisory or subagent was used. No commutative floating-point guards
were installed. Retained private screens and review receipts are in the N77
build directory; they are not extra matching credit.

Complete selected source SHA256: `ec9f27c0e70a7533314590776a11fa6d308c30f61b53ff641fb58f421337bbbc`.
Complete padded owner SHA256: `4c927dfa457cb55d8f7d45b90c9b8d0ae03cc59290a2b5831e8e700f34a45c85`.

The aligned retail census finds one pointer at ROM22E830 / VA80089D70,
row4 of the complete 44-entry D_80089D60 table (ROM22E820..22E8D0). The whole
176-byte table matches retail and the frozen ELF. There is no aligned direct
J/JAL pattern naming this target; that does not exclude other reference forms.
The original/current 195-word dispatcher passes actor through JALR1513D090
and consumes V0 as a boolean at1513D09C. Independent bounded public-state/call
reference and both literal target streams pass 1,024 cases, including 256
connected target invocations per stream. Active/lifetime gates, pre-callback
failure, target selection, fade flags, post-callback rescue and release are
covered; 115 parent words execute. Animation rate is deliberately zero for
this bounded integration; complete animation-service/gameplay acceptance is
not claimed. Pre/post/release services are bounded opaque providers.

Fresh qualification:

- 1,096 guest cases across five literal streams compare full private memory,
  GPR/FPR, HI/LO, FCSR, calls, trace and return. An independent rounded reference
  checks public memory and ordered FP operations. All 121 target words execute.
  Include all four rounding modes, existing flags, unsigned draws, signed16
  boundaries, large/negative deltas, bounded invalid guest conversions, opaque
  public mutations and actual writable delta aliases. Six wrong instruction
  variants fail by comparison.
- 144 fired access-prefix quintuples preserve full literal private/fault state,
  instruction PC and branch-delay ownership. These are guest-order probes,
  separate from portable C fault semantics or exception-hardware acceptance.
- Both retained RNG helpers (18 and25 words) match ASM, ROM and frozen ELF.
  Connect all43 original instructions in 384 cases per stream, all four modes
  and twelve 64-bit seeds. Mathematical seed progression, original scale,
  public data, calls, ordered FP/FCSR and full private states agree. All43 helper
  words execute and their only store is to the eight-byte seed. Opaque mutation
  stress remains a separate, deliberately stronger provider experiment.
- Native32 actual C in three TUs passes 8,192 cases at each O0/O2/O3, strict
  aliasing/FP, trapping undefined/float-cast UBSan and LTO type checks. Full
  records, canaries, globals, RNG-call sequence, returned value and MXCSR agree
  with a separately rounded reference. Nine wrong C controls exit42 through
  comparison, including cached live clock; no compiler error, trap or signal
  counts as a valid negative control. Native conversions stay in range.
- Both scoped padders expose242 word and40 binding corruptions. Twenty GNU
  links and100 guest rebase runs independently move both RNG symbols and all
  four global bases through four jump regions and signed HI16/LO16 carries.
  Generic oversize remains visibly overflowing; generated oversize rejects.
- The actual five-command mixed-owner Make route reproduces the complete
  qualified object. One existing pointer/integer Warning712 remains unchanged
  after normalizing only source label/line; no new warning is introduced.
- An independent frozen-before-C plus original-ASM full-image prediction equals
  private recipe link and production ELF byte-for-byte:509 changed bytes,
  zero exclusions. Thirteen symbol records change order, with complete named
  definition equality and closed metadata accounting; no symbol-table blanket
  exclusion is used. All other function bodies/addresses, guard history and
  inventory rows stay fixed. Protected189,088 data bytes across720 owners
  remain exact.

| Phase | Seconds | Coverage |
| --- | ---: | --- |
| preinstall-primary | 187.007 s | 5 fresh / 0 reused |
| preinstall-sibling | 180.493 s | 5 fresh / 0 reused |
| installed-primary | 150.59 s | 5 fresh / 0 reused |
| installed-sibling | 169.46 s | 5 fresh / 0 reused |

All20 passing target test methods are fresh. Both tools copies have identical
closed task/import/data/artifact fingerprints; asm processing uses each copy's
own tools. Shared tools-check passes. Unchanged broad suites are not described
as fresh. Frozen inputs:4165; copies:3117.
The separately dirty real tools sibling is preserved. Tools commit:
`ee816e16920757e63545857422556c8735ff8255`.
Baseline consumer: `f0fa4b181282e5475a5b3bcc803b33770581b236`.
Production ELF SHA256: `59d24b31874f04e40f339114775a2120be513531088f8dda433e638d1ae1dbb5`.
Receipts: `conker/build/game-billboard-target-update-1514a19c-private`.

The host generated target is an empty stub; active host applicability remains
unqualified. No host transfer/build/launch or Release change. Scoped Graphify
refresh audits35 current C definitions, retains all old IDs and qualification
metadata and waits for actual commit-hook producers to terminate before final
publication. No full-corpus re-extraction claim. Root README receives aggregate
rows/date only. Keep the 90% matching goal active and continue from sealed N77.
