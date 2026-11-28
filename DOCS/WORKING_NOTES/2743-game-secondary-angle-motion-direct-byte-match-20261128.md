# Secondary effect angle/motion callback direct byte match - 2026-11-28

`func_150EA944` in `conker/src/game/generated_117490.c` replaces a three-word
zero-return placeholder with **115 words / 460 bytes** of semantic C. The
complete slot, VA `0x150EA944..0x150EAB10`, ROM `0x117DF4..0x117FC0`, matches
retail directly. There is no frame, alignment tail, added guard, insertion or
omission. The recovered interface is `void func_150EA944(u8 *effect)`.

Actual production: **4,722 / 5,528 (85.42%) total**, **4,049 / 4,855 (83.40%)
Game**, Init 492/492 and Debugger 181/181. Zero address drift; 806 still
different. Conversion rows and denominators are unchanged. **254 more matches**
reach the active 90% target of 4,976/5,528. This adds exactly one direct C match.
Previous consumer `3925224b`; tools packet `ce58ae321befef187aa2b5192b2ebef77233b7e2` was committed first.

## Recovered behavior

The callback runs only when both low bits of effect byte +0x73 are set. It
converts signed `D_800BE9E4` to binary32 once for the angle updates at +0/+4/+8,
using angular rates at +0x60/+0x64/+0x68. Each angle is adjusted by 360 at most
once: add when below zero, otherwise subtract when at least 360. The original
multiply/add and compare ordering is retained; this is not a modulo loop.

The routine captures the life byte at +0x8A, subtracts acceleration (+0x3C)
times the freshly read integer tick from signed halfword Y velocity (+0x5C),
then integrates halfword X/Z positions (+0x10/+0x14) from velocities +0x5A/+0x5E.
The updated Y velocity advances the 32-bit accumulator at +0x7C; its signed
value shifted right three supplies the Y position halfword at +0x12. Integer
products and sums use unsigned 32-bit arithmetic before the original signed
halfword truncations, preserving wrap without C signed-overflow undefined behavior.
Integer tick loads remain repeated, including under the tested guest aliases.

The signed remainder of captured life minus four times the integer tick is
stored back as a byte when positive. Otherwise byte +0x6E becomes one and the
old life byte is retained. The function has no meaningful return value: the
original callback windows discard V0. The definition restores that original ABI
without shared-header edits.

## Direct code, complete owner and image

All **115 raw words and two HI16/LO16 bindings** match the original assembly
under the existing O2/g3/mips2/o32 profile. Both complete padders reproduce the
frozen before object and agree on the selected object. All **ten neighboring
functions**, compiler pools and **five original GLOBAL_ASM bodies** remain fixed.
The existing five-command mixed-owner Make recipe is replayed unchanged.
There are six pre-existing unrelated duplicate-recipe warnings and no new
compiler or assembler diagnostics. No Makefile, guard CSV or header changes.

An independent full-image prediction inserts the original target assembly into
the frozen before-C owner and changes only the named target size from 12 to
460 bytes. Actual private and production Make images match that prediction
byte for byte: **326 changed bytes, zero exclusions**, no metadata permutation.
All **720 protected data owners / 189,088 bytes**, other bodies, addresses,
guard history and conversion rows are unchanged. ELF SHA256:
`a96cb7b71c3194e6ee393008c5cdc433f0f797dadbc62bb3ceaca6037877c198`.

## Focused qualification

- Actual SDK/native32 C runs **1,400 finite binary32 cases each at O0/O2/O3**,
  with separate translation units, strict aliasing, trapping UBSan and LTO type
  checking. Every one of the 160 effect bytes and the global tick are checked.
  Signed zero, one-step angle wrapping, extreme signed/unsigned tick products
  and halfword boundaries are included. Seven semantic mutations fail with exit 42.
- Guest checks run **1,254 cases x four direct streams / 5,016 executions**:
  retail, raw C, generic padder and generated padder. All **111 CFG-reachable
  words** execute. Four original unreachable words (indices **27,48,67,112**)
  are retained exactly. Literal full machine states, access order and **146
  memory-access fault quadruples** agree. Fixtures cover all flag/life bytes,
  three sparse pointer domains, both stack phases, 18 quiet-NaN/infinity cases
  and 24 guest-only tick/object alias cases. Three guest semantic mutations reject.
- The only registration is row **60** of the original 1,072-byte `D_80088C90`
  table, pointer ROM **0x22DA20**, row `(func_150EA944,0,0)`. All 22 original
  installer words execute. Two original dispatch/result-discard windows in
  `func_15113E54` total **43 words** and supply **384 connected executions**
  across 48 fixtures and four V0 poisons. They establish the one-pointer,
  ignored-return ABI. The complete 127-word parent is pinned but its unrelated
  paths/providers are not qualified by these windows.
- **16 actual GNU links** cover four independent entry/global address rebases
  including signed HI16/LO16 carry seams. Eight strict-image mutations reject:
  each unreachable target word, a neighbor, the callback row, named extent and
  ELF header. The image comparison has no excluded ranges.
- Five complete packaged tests pass independently in both closed tools roots
  before installation and again after installation: **20 fresh checks**, equal
  reports and verified import/data dependencies. Shared `make tools-check` passes.

Native C claims require mapped/aligned typed objects and finite binary32 input
arithmetic in the tested domain. Guest quiet NaNs/infinities and tick aliases
are additional machine evidence, not portable C alias/trap guarantees. The
guest oracle does not emulate hardware floating-point exception flags. This
is matching/build/behavior evidence; no new visible gameplay acceptance is claimed.

README receives only its two aggregate matching rows. The graph refresh uses
scoped AST extraction, old-ID retention and preservation of existing qualification
metadata; it is not full-corpus re-extraction. Local hook, graph and immutable
bank receipts live in `conker/build/game-secondary-angle-motion-150ea944-private/`.
The real dirty tools sibling is preserved. The host sibling is assessed read-only;
there are no host builds, launches or edits, and Release remains frozen.
N82 `func_1514EECC` remains parked. No push or subagent is used.

Next: continue ordinary unmatched Game matching from the sealed N89 bank.
