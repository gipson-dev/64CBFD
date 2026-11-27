# Oriented two-quad constructor guarded match - 2026-11-26

`func_15165F80` replaces its zero-return placeholder in
`conker/src/game/generated_193430.c`. The semantic C emits **102 words**,
with the original **56-byte frame** and all **six relocation positions**.
**Fifteen expected-word guards** recover the original body using two closed
GPR swaps. Eighty-seven raw words need no replacement. There is no alignment
tail, insertion, omission, stack remapping, instruction scheduling or FP
operand/arithmetic rewrite. This is guarded C, not a raw compiler byte match.
VA `0x15165F80..0x15166118`; ROM `0x193430..0x1935C8`.

Production: **4,706 / 5,528 (85.13%) total**, **4,033 / 4,855 (83.07%) Game**,
Init492/492, Debugger181/181, zero drift,822 still different. One matching
credit; no conversion-row, denominator, caller or helper credit. The active
**90% goal currently requires4,976 matches:270 more**.

Recovered entry: `void func_15165F80(s32 angle, s32 x, s32 y, s32 z,
s32 step, s32 lifetime, s32 mode, u8 selector, s32 category)`. Parameter and
field roles are inferred; original effect names remain unknown. Allocate
0xA8 bytes through `func_15167A68(4, category, 0xA8, 1, selector, 1)`. Failure
skips all constructor writes and origin publication. Angle-1 sets the eight
vertex Y halfwords from captured Y and zeros eight vertex Z halfwords, then
sets byte95=0. Other angles use signed integer-to-float conversion times the
pinned coefficient, then sine*127 truncated to byte91 and negative cosine*127
truncated to byte90, with byte95=1. Both paths fill two UV blocks, store the
narrowed lifetime/position/step/mode fields and flag9E=1, and call the origin
writer with full captured/live coordinate words as in retail.

The coefficient D800A6C94 is ROM24B754, float bits3C8EFA35
(0.01745329238474369). Source uses its external value, not a substituted
literal. The original FP order is signed CVT, coefficient multiply, sine,
multiply127, TRUNC, cosine, NEG, multiply127, TRUNC. Byte95 is stored before
the final TRUNC in emitted code. Guest FP observers include the complete
output, alternate record, marker, coefficient and origin bytes at every FP
operation, preserving that interleaving and its FCSR effects.

Source fitting retained the complete semantic body. The first screen had
102 words/frame56 with21 differences. Eight loop/declaration spellings reduced
this to18; a finite24-permutation screen of four real locals reduced it to15.
Selected local order is quad, created, radians, vertices; UV initialization
sets quad=0 before vertices=created. No volatile qualifiers or dummy operands.
The owner header now describes recovered routines and its remaining
func_15166268 placeholder without claiming the whole owner is complete.

Normalization is derived mechanically: raw GPR4<->5 at offsets54..88 and
GPR2<->3 at108..140 (hex). Both are closed loop-role swaps. FP instructions,
stack accesses and instruction order are literal. S0/RA homes are20/24,
radians2C and saved output30. The raw stream has equal complete memory, FP,
FCSR, HILO, calls, observations, access traces and consumed instruction inputs
under those role relations, including pending store data. Preserved GPRs
agree. **Full raw fault-register identity is not claimed**: dead caller-saved
loop roles can differ after overwrite. Four literal streams retain complete
private-state/fault identity without dropping any access boundaries.

Validation:

- All four raw neighbors and pools remain fixed. Both complete padders
  reconstruct the frozen BEFORE object and emit identical AFTER objects.
  The actual normal O2/g3/mips2/o32 three-command Make recipe agrees, without
  new diagnostics or profile/Makefile changes. Existing unrelated duplicate
  recipe warnings remain visible in the full build.
- Guest:768 cases per five streams, all102 retail words executed, and187
  literal fault-prefix quadruples with raw consumed-input/access relations.
  Allocation failure/success, signed conversion edges, four rounding modes,
  signed zero, subnormal/finite trig results, helper clobbers, global changes,
  guest-only incoming homes, saved pointer and radians mutations are included.
  An independent reference compares all public memory, calls, snapshots and
  ordered FP/FCSR. Seven instruction negatives cause comparison mismatches.
- The original origin helper is connected in four cases per stream and
  fault checks:7 body words,9-word slot. Its three halfword global writes
  agree with the reference. Allocator28, sine104, cosine88 and origin9 slots
  are ROM/frozen-ELF pinned; allocator and trig remain opaque dynamically.
  This does not claim full allocator/trig/backend or hardware acceptance.
- All seven aligned plain JAL sites receive static result-lifetime analysis:
  explicit overwrite, later ABI call, or the known recovered void parent
  return discards V0. No aligned plain pointers were found; derived/script/
  compressed references are not excluded. Only the small parent is fully
  connected, not the other six callers.
- The complete original func_150D8A34 executes all54 body words (55-word slot,
  frame64), with144 cases/stream and72 connected children. Original origin
  code is connected too. Independent full-parent memory/call/FP reference,
  entry gates, live owner/vector changes, callback selector and unused third
  word, four rounding modes and three child-result poisons pass. Its reference
  initially omitted the five outgoing stack arguments; adding those actual
  argument stores corrected the fixture before acceptance.
- The three C caller declarations in generated_105760, generated_E7970 and
  generated_E8090 now return void, matching the recovered entry. Their9/6/6
  functions, raw words/bindings/pools, both before/after complete padders and
  actual three-command Make recipes are audited. **All three full padded
  objects remain byte-identical to the frozen baseline**. These dependent
  owners are included in production and graph audits without exclusions.
- Native32 actual C:4,096 cases at each O0/O2/O3; three translation units,
  typed84-halfword allocation with legal character accesses, asserted168-byte
  extent, strict aliasing, trapping UBSan and LTO type checks. Complete
  initialized storage/canaries, calls/packets, coefficient, origin and MXCSR
  are compared. Twelve semantic negatives finish with comparison exit42;
  no signal, compiler failure or trap counts. Providers are opaque counterparts.
  Guest private-home experiments are not portable-C alias claims.
- Both padders reject30 guarded-word corruptions, expose174 unguarded-word
  changes and all12 binding changes, and reject oversized input. Twenty GNU
  links and100 guest rebase runs cover four independent jump regions and
  signed HI16/LO16 carry seams. Rebased providers remain opaque.
- Independent frozen old-C/original-ASM prediction equals the entire private
  and production ELF: **326 changed bytes, zero exclusions**. All189,088
  protected data bytes across720 owners remain fixed. ELF SHA256:
  `dbf6329c2046220bbc54de207d17a3c8ebb1a689d4f210b25faa2da2f6bb7e40`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 177.956 s | 5 fresh / 0 reused |
| preinstall-sibling | 158.156 s | 5 fresh / 0 reused |
| installed-primary | 120.133 s | 5 fresh / 0 reused |
| installed-sibling | 115.519 s | 5 fresh / 0 reused |

All20 target tests are fresh, with equal primary/isolated-sibling task,
dependency, data and artifact fingerprints. Shared tools-check passes.
Unchanged broad suites are not reported fresh. Frozen inputs:4108;
copies:3059. The separately dirty real tools sibling is
preserved. Tools commit:`47505e701e28e59d71dd1eb4c1cfa5c4f6fe574d`.
Baseline consumer:`a21f634b9fb7d84a7067cb46bc9740c335545411`. Receipts:
`conker/build/game-oriented-quad-constructor-15165f80-private`.

Zero Claude calls, no subagents. The historical host target remains a stub;
no host transfer/build/launch or Release change. Scoped Graphify refresh
audits26 current definitions across all four source owners and retains old
IDs/qualification metadata after observing actual hook termination. No full
corpus re-extraction claim. README receives aggregate rows/date only.
Continue from sealed N72 toward90% with another unmatched Game routine.
