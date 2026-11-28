# Actor type parameter defaults guarded byte match - 2026-11-28

`func_151216F8` in `conker/src/game/generated_14D110.c` replaces its three-word
zero-return placeholder with **115 words / 460 bytes** of semantic C, VA
`0x151216F8..0x151218C4`, ROM `0x14EBA8..0x14ED74`. There is no frame or
alignment tail. The restored original interface is `void func_151216F8(u8 *actor)`.

Actual production: **4,723 / 5,528 (85.44%) total**, **4,050 / 4,855 (83.42%)
Game**, Init 492/492, Debugger 181/181. Zero address drift; 805 still different.
Conversion rows and denominators are unchanged. **253 more matches** reach the
active 90% target of 4,976/5,528. This adds exactly one guarded C match.
Previous consumer `66b62799`; tools packet `5af610d1daf9283981f6c60789b3b5f8808a5c34` was committed first.

## Recovered behavior

The routine reads actor type byte +0x23E into a widened signed word. It writes
type-dependent binary32 constants to parameter fields +0x190/+0x784/+0x99C:

| Type / global condition | +0x190 | +0x784 | +0x99C | Additional effect |
| --- | ---: | ---: | ---: | --- |
| 0 | 25 | 90 | 0 | None |
| 0x34 | 80 | 350 | Preserved | None |
| 0x3B and `D_800BE9F0` equals 0x41 or 0x3C | -12 | 106 | -28 | None |
| 2, 0xA, 0x13 | 10 | 135 | 0 | OR word +0x84 with 0x80 |
| 0x12 and `D_800BE9F0` equals 0x3C | 10 | 180 | 0 | None |
| 0xF | 10 | 480 | 0 | None |
| 0x38 | 5 | 110 | 0 | None |
| 0x15 | 25 | 110 | 0 | None |
| Other cases | 5 | 75 | 0 | None |

The original branch order, conditional global reads and store order are retained.
There is no floating-point arithmetic or conversion: the code moves constant
bits and stores them. Type 0x34 deliberately preserves +0x99C. The one-pointer,
ignored-return interface is qualified from both original direct call sites;
there are no shared-header or Makefile changes.

## Two scheduling guards and complete owner

**113 bound words match directly**. Two expected-word guards at offsets
**0x98/0x9C** exchange `lw T6,0x84(A0)` and `mtc1 AT,F18`, restoring retail's
constant-move-before-load order. The instructions have disjoint destinations
and no dependency on each other's result, so their normal mapped-memory
completion states agree. This is an instruction schedule correction, with no
insertion, omission, floating-point algebra rewrite or register allocation cycle.

Raw fault-time full-state parity is explicitly **not claimed**. At a cut before
the flag load, retail has updated F18 while raw C has not. The guest check
observes that counterexample and proves complete fault-prefix state agreement
for retail and both normalized streams. Both guards are effective: four guard
removals produce visible differences and four stale expected words reject,
across the generic and generated padders.

All four original HI16/LO16 bindings to `D_800BE9F0` remain fixed. Both complete
padders reproduce the frozen before object and agree on the selected object.
All **four raw/padded neighbors**, compiler pools and the one original
`GLOBAL_ASM` body remain unchanged. The matched reset neighbor `func_151218C4`
retains its complete source body and raw/padded bytes. The existing O2/g3/
mips2/o32 profile and five-command mixed-owner Make recipe suffice.

## Focused qualification and linked acceptance

- Actual SDK/native32 C: **9,216 cases each at O0/O2/O3**, all 256 type bytes,
  nine signed/global boundaries and four flag patterns. Separate translation
  units, strict aliasing, trapping UBSan and LTO type checks pass. All **2,464
  actor bytes** and the unchanged native global are checked. Six semantic
  mutations fail with exit 42.
- Guest: **2,508 cases x four streams / 10,032 executions**, all **114 reachable
  instruction words** executed. Original unreachable word **106** is retained
  exactly. Literal normal-completion machine state and public access order
  match for retail, raw C and both normalized streams. **66 normalized memory-fault
  triples** preserve full states/prefixes. Three sparse pointer domains,
  both stack phases, nine global boundaries and 60 guest-only global/actor
  alias cases are included. Three guest semantic controls reject.
- Original direct JALs are at ROM **0x14D3A4/0x14D81C**, VA **0x1511FEF4/
  0x1512036C**, in `func_1511FC60` and `func_15120158`. Both complete original
  parents are pinned (318/1,230 words), but only **31 original window words**
  are qualified. All 31 execute in **2,304 connected executions**, 144 fixtures,
  four streams and four V0 poisons. A2/S0 are forwarded to A0, and no child V0
  use occurs before the next calls. A deliberate V0-dependent argument mutation
  demonstrates sensitivity. Subsequent calls to `func_15048758`/`func_1506160C`
  are **opaque boundaries**, not qualified providers or complete-parent proof.
- **16 actual GNU links** cover four independent entry/global address rebases,
  including signed HI16/LO16 carry seams. All normalized 115 words/bindings
  match at each rebase; the raw body differs only by the certified pair.
- An independent frozen-before-C plus original-target-ASM full-image prediction
  matches private and actual production Make output exactly: **394 changed
  bytes, zero exclusions**, no metadata permutation. All **720 protected data
  owners / 189,088 bytes**, other bodies, addresses and conversion rows remain
  fixed. Guard history changes only by the two appended target rows. Eight
  strict-image mutations reject, including both original caller JALs, the
  unreachable word, a neighbor, data, named extent and ELF header.
- Five complete packaged tests pass in both closed tools roots before and
  after installation: **20 fresh checks**, equal reports and verified import/
  data dependencies. Shared `make tools-check` passes. Six existing unrelated
  duplicate-recipe warnings remain; there are no new compile/assembly diagnostics.

ELF SHA256: `03ed647eb4a0e94ad1dd37066a2ae84126685490cf8ca2d27af9a5264c71f5c3`.
Mapped/aligned typed objects define the native C scope; guest-only aliases and
fault prefixes are additional machine evidence. The oracle does not emulate
hardware floating-point exception flags. No new visible gameplay acceptance
is claimed.

README changes are its two aggregate rows only. Graph refresh uses scoped AST
extraction with old-ID and qualification retention, not full-corpus extraction.
Final graph/hook/immutable-bank receipts live in
`conker/build/game-type-parameter-defaults-151216f8-private/`. The real dirty
tools sibling is preserved. Host applicability is assessed read-only, with no
host edits, builds or launches; Release stays frozen. N82 `func_1514EECC` remains
parked. No push or subagent is used.

Next: continue ordinary unmatched Game matching from the sealed N90 bank.
