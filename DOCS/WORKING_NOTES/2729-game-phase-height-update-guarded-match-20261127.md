# Phase-height update guarded match - 2026-11-27

`func_1511F788` replaces its zero-return placeholder in
`conker/src/game/generated_142560.c`. Complete semantic C emits **105 words**
and the retail **48-byte frame**. **52 derived expected-word guards** recover
all **105 retail body/slot words**, with no inserted or omitted instructions
and no alignment tail. Fifty-three raw words are already literal. This is a
guarded C match, not a raw compiler byte match.
VA `0x1511F788..0x1511F92C`; ROM `0x14CC38..0x14CDDC`.

Production: **4,708 / 5,528 (85.17%) total**, **4,035 / 4,855 (83.11%) Game**,
Init492/492, Debugger181/181, zero address drift,820 still different. One
matching credit; conversion rows and denominators do not change. The active
**90% goal requires4,976 matches:268 more**. No parent or helper credit.

Recovered entry: `void func_1511F788(HeightPhaseState1511F788 *record)`.
Names describe inferred roles rather than recovered original identifiers.
The private136-byte record view names height12,offset18,duration3C,delta5C,
finished6E,phase7C,mode80,timer84 (offsets hexadecimal). It does not replace
the owner's separate, shorter cosine-height record or change shared headers.
The existing signed RNG prototype is retained without a duplicate declaration.

The function captures the narrowed signed16 integral height plus offset,
derives a threshold from duration times60, conditionally resets phase from
the RNG's low16 bits under cached byte D800BE9B4, calculates
cosf(signedphase *0.0054931640625f)*25, then advances phase by live ticks*10.
Mode1 adds live ticks to the wrapped timer and switches to2 when the signed
threshold is exceeded. Mode2 lowers narrowed height by ticks and marks
finished below-10000. The final signed16 delta subtracts the captured integral
height from the new height plus offset. Field reloads, helper mutation points,
floating arithmetic operands/order and truncation/narrowing are preserved.

**Integer dialect qualification:** the recovered signed compound multiply
emits the pinned N64 compiler's MULTU/MFLO low32-bit result followed by signed
DIV60. The source comment calls out that target behavior. Actual native C
tests explicitly use **-fwrapv**, with an independent **unsigned32 product**
reference and all32-bit duration edge domains retained. This is not a claim
that unflagged generic ISO C defines signed multiplication overflow. No MIPS
compiler flags or shared Make profile are changed.

Source fitting tested complete semantic bodies, real captures, local order,
scopes and divisor forms under normal O2/g3/mips2/o32. The selected declaration
order recovers105 words/frame48 with all six bindings aligned. No gratuitous
volatile, dummy/padding local, address escape or compiler-profile change is
used. Earlier94/frame32 and104-word screens are private rejected experiments.
The final complete-source SHA256 is `5829f0f56594128c68a672cc9d1c2497047b7ab74649cb5926750abdf947dbe2`.

Normalization is derived from two closed GPR cycles and a split product live
range. Through78(hex), raw5->2,2->8,8->5; the rawV1 product at40..70 moves to
retailT9 while the quotient retainsV1. At7C..194 the ten transient registers
8,9,10,11,12,13,14,15,24,25 rotate by two. MFLO moves from74 to50 and the
division-check block shifts right four bytes. The divisor is literal60 at8,
with a static no-write proof through this block; divide-by-zero and MIN/-1
BREAK routes are unreachable. Original unreachable words5C,6C,70,74 remain
present;101 reachable words execute. All six relocation positions are pinned:
14/1C D800BE9B4 HI/LO,84 RNG JAL,BC cosf JAL,D8/DC D800BE9E4 HI/LO.

Stack byte addresses, access widths and order remain literal, with the final
LH destination GPR participating in the cycle. The previous signed16 home1E,
threshold24, incoming-owner home30 and frame48 are unchanged. Every FPR index,
floating arithmetic operation and operand order is literal; MTC1/MFC1 GPR
fields follow their derived roles. No floating commutative rewrite is used.

Four literal streams agree on full private/register/memory/FP/FCSR/access/PC
fault states. Raw qualification separately compares full memory, preserved
GPRs, FP/FCSR/HILO, accesses and consumed operand values under the explicit
roles and scheduling relation. **Raw full dead-GPR fault identity is not
claimed.** The moved quotient/check block cannot be treated as the same raw
branch-PC frontier merely by replacing one PC. No data access occurs inside
that moved block. Opaque RNG/cosine providers and disabled FP traps are bounded
fixture contracts, not a claim of complete game/hardware behavior.

Validation:

- All83 raw neighbors/pools stay fixed in the84-definition owner (83 C
  definitions and one retained GLOBAL_ASM). Both complete padders reconstruct
  frozen BEFORE and agree AFTER. Actual five-command Make includes real
  asm-processor pre/postprocessing, IDO compile, padding and GNU assembly;
  normal profile and object agree with no new compiler diagnostics.
- Guest:771 cases per five streams, four literal;101 reachable retail words,
  106 full literal fault quadruples and106 raw memory/FP/access/consumed-input
  fault relations. Four rounding modes, overflow/wrap boundaries, helper
  public mutations and guest-only incoming/local-home changes are covered.
  Public FP snapshots include two contiguous full records and an alternate
  record. Six effective instruction negatives are rejected; the phase-mask
  control uses RNGFFFFFFFF so the high low-word bit is actually exercised.
  The architectural model additionally exercises a quiet-NaN case.
- Native32 actual C:4,096 cases at each O0/O2/O3, three translation units,
  asserted canonical136-byte record/offsets within192-byte canary storage,
  fully initialized state, globals, calls, snapshots and MXCSR compared.
  Strict aliasing, explicit-fwrapv, UBSan undefined/float-cast traps, strict
  SSE/fenv and LTO type checks pass. Twelve effective controls exit42 through
  comparison; signals/traps are not counted as successful controls. Private
  stack-home mutations and the guest architectural NaN case are not portable
  native fixtures; native cosine inputs obey the finite provider contract.
- Original callback dispatcher func15113E54:all127 words execute, frame64,
  144 cases/stream and147 connected children/stream across linear/grouped
  pools, flag/finished gates, copied state and the complete epilogue. Four
  return poisons prove the callback return is ignored. The original22-word
  script installer1509EBBC..1509EC14->1509ED5C executes completely. Its
  D80088C90 callback table row65 atVA80088F9C/ROM22DA5C contains
  (1511F788,1511F768,0);all1,072 table bytes are pinned to retail/frozenELF.
  The8-word activation slot runs four mode cases. RNG18-word/cosf88-word
  slots are pinned but remain opaque providers dynamically. **Production
  dispatcher func15113E54 is still its12-byte zero-return stub.** These are
  original-retail caller tests and give no parent restoration credit. The
  aligned census finds no direct JAL to the leaf and one plain pointer;
  derived, script and compressed references are not thereby excluded.
- Both padders reject104 guarded-word and4 guarded-binding corruptions,
  expose106 unguarded-word and8 unguarded-binding corruptions, and reject
  oversizes. Twenty actual GNU links cover four jump regions and signed
  HI16/LO16 carry boundaries, with100 rebased guest runs.
- Independent full-image prediction uses frozen before-C plus original ASM
  and equals both actual recipe-linked and production ELF byte-for-byte:
  310 changed bytes, zero exclusions, no metadata permutation allowance.
  All83 neighbors/addresses/extents and protected189,088 data bytes across720
  owners remain fixed. Prior guard CSV bytes are an unchanged prefix; only
  the52 derived target rows are appended. Fresh production recount agrees.

| Phase | Seconds | Coverage |
| --- | ---: | --- |
| preinstall-primary | 119.354 s | 5 fresh / 0 reused |
| preinstall-sibling | 86.442 s | 5 fresh / 0 reused |
| installed-primary | 97.525 s | 5 fresh / 0 reused |
| installed-sibling | 117.461 s | 5 fresh / 0 reused |

All20 target tests are fresh. Primary and isolated-sibling task/import/data/
artifact fingerprints agree; actual asm processing uses each copy's own tools.
Shared tools-check passes; unchanged broad suites are not reported fresh.
Frozen inputs:4135;copies:3087. The
separately dirty real tools sibling is preserved.
Tools commit:`591428501ac8da61a92426d3efb8ea0e0882edce`.
Baseline consumer:`4775876cfd98383bcab859858716ab4a9714ef1e`.
Production ELF SHA256:`c396640122a332212068baa5930689ad1ddf8dba8a2a5fdd9fd61842f8df4e7e`.
Receipts:`conker/build/game-phase-height-update-1511f788-private`.

Zero Claude calls for this routine; local evidence settled the remaining
questions. No subagents. The host's generated callback is an empty stub;
no host transfer/build/launch or Release change. Scoped Graphify refresh
audits83 current C definitions and retains all old IDs/qualification metadata
after observing actual hook termination; no full-corpus re-extraction claim.
README receives aggregate rows/date only. Continue from sealed N74 toward90%
with another unmatched Game routine and the same complete acceptance gates.
