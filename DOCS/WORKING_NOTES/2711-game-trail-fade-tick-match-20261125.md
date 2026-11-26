# Trail fade tick match - 2026-11-25

`func_151B6420` replaces the zero-return placeholder in
`conker/src/game/generated_1E37D0.c`. Its complete **109 words / 436 bytes**
match retail after **five expected-word FP-register guards**; 104 words emit
directly from C. The leaf has no stack frame. All four relocation positions
match, with one guarded LO16 coefficient binding. There are no insertions,
omissions, alignment additions or compiler-profile changes.
VA `0x151B6420..0x151B65D4`; ROM `0x1E38D0..0x1E3A84`.

Production: **4,690 / 5,528 (84.84%) total**, **4,017 / 4,855 (82.74%) Game**,
Init 492/492, Debugger 181/181, zero address drift and 838 still different.
One new match; no additional caller, producer or neighbor credit.
**Nine more verified matches reach 85%.** Conversion rows and denominators
are unchanged.

The signed 32-bit status routine takes one owner pointer. Its observed
partial owner is 152 bytes, with flags at 0x1E, unsigned capacity at 0x25,
signed count/tail/head at 0x2C/0x2D/0x2E, reference position at 0x54 and
captured record pointer at 0x94. The 28-byte record contains a position,
float lifetime at 0xC, opacity byte at 0x10 and accumulated distance at 0x18.
Names describe these observed fields; retained bytes remain opaque.

When count is below two and owner flag bit 3 is set, it returns zero.
Otherwise it walks backwards from signed head to the current signed tail,
wrapping negative indices through capacity. Each visited lifetime subtracts
the repeatedly read float delta time. A negative result can drain tail toward
that index, narrowing tail/count through signed bytes and wrapping tail at
capacity. With positive count, it captures the oldest point's distance and
the external fade coefficient, then walks forward from tail to head. It
computes the ordered distance subtraction and multiply, truncates to signed
32 bits, caps only values above 155 and narrows the result to the opacity
byte. There is no lower clamp. Finally it copies the tail position or writes
three positive zero floats; ordinary completion returns one.

The complete aligned ROM census finds one literal at ROM `0x22ECEC`, with
no direct J/JAL patterns. This is index 11 of the 15-entry `D_8008A200`
table. The complete original 100-word / frame-32 dispatcher `func_15147740`
passes the owner in A0 at JALR `0x151477C4`; its zero-result consumer marks
expiration. Its original bytes also match the frozen linked ELF. Connected
execution covers selectors 0/11/15/255, lifetime narrowing, signed count,
flag combinations, skip/invalid-selector paths, and the later dispatch skips.
The expiration provider is opaque; other table entries and arbitrary computed
callers are not qualified by this work.

The coefficient at `D_800AA470` is ROM `0x24EF30`, bits `0x3EFCED92`
(about 0.494000018). Its original data owner is separately frozen. Preserve
its external binding and captured lifetime; it is not folded into a new pool.
The float delta retains its distinct mutable binding `D_800BE9A4`.

The first semantic source had 110 words. The typed owner argument removed
an unnecessary pointer copy. Capturing the real coefficient once recovered
109 words; inlining the distance expression reduced the residual allocation
differences to five words. The decoder proves the complete stream is retail
under one bijection restricted to the second fade phase (offsets E4..120):
raw F2->retail F14, F4->F18, F6->F4, F14->F6, F18->F2. Every word outside
that phase is unchanged. No opcode, integer operand, immediate, FP operand
order, control edge or relocation identity changes. Five guards normalize
only the coefficient load, difference/product/truncation roles and MFC1.
They validate expected words and the guarded LO16 binding before replacement.

Raw and normalized streams have equal complete memory, GPRs, HI/LO, saved
ABI state, return, ordered FP operands, FCSR and memory-access/fault order
in the qualified cases. Raw dead volatile FPR contents are intentionally
not claimed literally identical: they retain the compiler's allocation.
Original versus normalized/both padded streams do compare every FPR and
private state at all supported fault cuts. This distinction also applies to
the connected caller and rebase checks. IEEE checks are bounded software
models with traps disabled, not hardware or gameplay acceptance.

The initial private fitting generator accidentally inserted a factor field
into the record declaration in four probes. Those 32-byte-stride candidates
are rejected. The corrected screen asserts the record prefix is unchanged;
all credited tests enforce the original 28-byte layout. An ineffective clamp
control was replaced with a finite case that reaches the clamp. Rebase probes
also retain valid ring termination and use bindings consistent with their
linked global symbols. No failed probe or trapped control receives credit.

Validation:

- Complete owner before/after compilation and both production padders agree;
  all 16 neighboring bodies/bindings and raw/padded pools are unchanged.
  The actual three-command Make recipe emits the identical owner without
  diagnostics. The previous guard bytes are an unchanged prefix.
- Guest: 1652 cases across five streams, all four rounding
  modes, finite signed/count/clamp/truncation boundaries, owner/record/global
  aliases and 105 fault-cut quintuples. All 106
  reachable words execute; the three original duplicate load/store words
  remain byte-qualified. Five complete supported wrong variants are rejected.
- Native: 8,192 typed capacity-1..8 cases at O0/O2/O3, two translation units,
  strict aliasing/FP, UBSan traps and LTO type checks. Full owner/record arenas,
  canaries, globals, return and MXCSR agree. Seven controls complete with
  comparison exit 42; no trap or signal is counted. Native conversions stay
  finite and in signed-32 range. Invalid conversions and arbitrary guest
  aliasing do not become portable C claims.
- Caller: 4,608 cases and 960 connected child executions per stream, plus
  three effective return-consumer controls. Its source and linked bytes are
  unchanged, and it receives no new matching credit.
- Guards reject ten word corruptions and two guarded binding corruptions;
  208 unguarded word corruptions and six other binding corruptions stay
  visible. Twenty GNU links and 100 guest rebases cover independent symbol
  movement and HI16 carry boundaries. Both oversized padders reject.
- The independent image reconstructs the target from original ASM plus the
  frozen old C owner. Exactly 365 ELF bytes change; there are zero exclusions.
  All 189,088 protected Game-data bytes across 720 owners remain unchanged.
  Production ELF SHA-256: `87c0acb29f15b732177e1fe895797a10a03d7252d0b239ce6767105ce12d6d92`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 130.625 s | 5 fresh / 0 reused |
| preinstall-sibling | 93.66 s | 5 fresh / 0 reused |
| installed-primary | 98.362 s | 5 fresh / 0 reused |
| installed-sibling | 95.186 s | 5 fresh / 0 reused |

All 20 target tests above are fresh, with matching tools-copy fingerprints.
Shared tools-check passes. Unchanged broad neighbor suites are not rerun or
reported as fresh. The isolated sibling overlay preserves the independently
dirty real tools sibling. Frozen inputs: 3886; independent
snapshot entries: 2811. Its overlay uses
2211 immutable dependency links and nine
independent task copies. No additional Claude calls or subagents were used.

Baseline consumer `41c14f70f9918aaa03b3f310e1d601f0c93f2836`.
Tools commit `b2cb31508c04caa71be7d5e4d7831a6849a0223d`.
Receipts: `conker/build/game-trail-fade-tick-151b6420-private`.
The historical generated host target is an empty stub; no host transfer,
build, launch or Release change is made. No push or gameplay acceptance.
The graph refresh audits all 17 owner definitions, retains prior qualification
and old IDs, and waits for actual commit-hook writers before publication.
The root README receives aggregate/date rows only. The 85% goal remains active.
