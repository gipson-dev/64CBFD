# Rectangle Private Clipping Homes Byte Match

Date: 2026-10-18. Consumer predecessor **63fc92b6**, tools predecessor
**d8111ab6**. Previous goal turn made progress by recovering twelve flip
words directly from C. This turn completes the installed guarded match for
**func_15095D34**, owner `generated_C1D70`, VA **0x15095D34..0x1509629C**,
ROM **0xC31E4..0xC374C**. The wider Game objective remains active.

## Result

All **346 words / frame0x88** now match retail after **six** qualified
private-stack-layout guards. Raw semantic C remains at **six** differences;
do not describe it as a direct/raw compiler match. Source, types, comments,
SDK macros and compiler flags are unchanged from Note1528.

The only new rows change X's SP+4 home to SP+0xC and Y's SP+0 home to SP+8,
including its signed-halfword SP+2 to SP+0xA access. Word indices are
205/210/211/224/242/254. Opcodes, base/value registers, branch instructions,
instruction count and all 28 target relocation sites stay fixed.

## Fresh Compiler Evidence

`tools/experiments/game_packet_rectangle_clip_homes.py` pins **20 actual
current inputs**, separate from the older 18-difference fixtures. Fresh
captures live under `conker/build/game-packet-rectangle-clip-homes/`:

```text
compiler-selected-gates
allocation-selected-5
```

The owned compiler driver and CFE/UOPT/UGEN children terminate successfully.
Normal/traced objects, pools, bindings and the complete-owner/isolated target
are identical. The current isolated source SHA is
`7fd708773e4d996ecf3530d95b0976f2ff4e7f84bb0ec7dcbbae645f6b2c9e91`;
raw target SHA remains Note1528's `e2e13c50...`. Current streams contain
**1,366 frontend / 1,212 optimizer records**; these are not the old capture's
1,362/1,208 records. Compiler fingerprints and descriptor tables stay pinned.

All **24 events / 20 selected temporary expressions** are bound to the actual
owned UOPT child, probe PCs, producer/consumer paths and cleanup order. Native
forbidden vectors and allocation-graph blockers agree:

| Macro Range | Blockers By Earlier Home | Forbidden Temp IDs | Selected M Home | Retail SP Home |
| --- | --- | --- | --- | --- |
| X 347 | `[73,235]`, `[107]` | 0,1 | -132 / SP+4 | SP+0xC |
| Y 354 | `[235]`, `[107,349]`, `[347]` | 0,1,2 | -136 / SP+0 | SP+8 |

The provisional pool reaches 144 bytes, but final optimizer storage and the
observed emitted frame remain **136 bytes**. Later gettemp actually reuses
M-124 without growing the pool. Suppressed real-number diagnostics are not
valid numerical timing/cost evidence.

Nine complete source screens, including the baseline, test real coordinate
phase changes before/after the flip blocks. All eight alternatives regress:
345..354 words, frames0x88/0x90 and 175..332 differences. All 18 neighbors
and owner pools stay fixed. No phase variant is installed, and the macro's
full-width Y sign predicate is preserved.

## Closed Home Lifetimes

`tools/experiments/game_packet_rectangle_home_match.py` proves the complete
emitted CFG, including normal/likely branch delay slots, return and BREAK
paths. Its **384 states / five terminal states** establish:

- The complete 0x88-byte frame is callee-owned and mapped. No call or stack
  address escape occurs; frame setup/teardown are fixed.
- Exactly seven instructions touch private slots: the earlier dead SP+0
  spill and the six rewritten accesses. SP+8/+0xC have no competing use.
- Every X/Y read is dominated by the corresponding complete store. The old
  SP+0 spill has no reader before its reuse. All other stack accesses are
  caller argument homes at SP+0x88 or above and remain literal.
- Only the six expected displacement fields change. Every other emitted
  word is unchanged, with no insertion/omission or relocation movement.

This is a compiler-private-home equivalence, **not equality of dead raw
private stack bytes**. Guest comparisons retain every other memory byte,
including caller stack state, all registers/FP/condition state, access order,
and each live logical temporary's value. External objects that alias the
callee-owned frame are explicitly rejected, not silently projected away.
The ABI ownership/mapped-frame contract is necessary and is not a claim
about malformed pointers or arbitrary hardware fault mappings.

## Qualification

The final nine-target-test suite passes in **99.093s**, including a twelve-test
source-regression sub-suite in **59.242s**. Strengthened owned-child identity
checks and the all-zero-PID control additionally pass their focused rerun
in **3.238s**. Earlier eight-test pre/post passes are 32.449s / 33.888s.

```sh
python3 -m tools.tests.test_game_packet_rectangle_home_match -v
```

Fresh layout checks cover **5,760 complete paired executions**, plus all
**2,912 memory-access fault prefixes / 64 states**. Effective controls catch
wrong private stored values even with identical public output, incorrect
displacements, stack-address escape, malformed native vectors/identities,
removed interference, every pinned live/frozen input and attempted repeated
compiler captures. Actual compiler traces are retained, not regenerated.

The unchanged source suite freshly covers native32 O2/O0 with UBSan and
1,048,576 animation cases per selected profile, eight effective native/guest
controls, aliases, traps, animation, independent symbol rebases and the real
connected caller. It runs in an explicit exact predecessor view. Its old
installed-image test is superseded by the new actual-image audit, not faked.
The view redirects the old source padder to the archived guard CSV because
that parser uses open(), outside the Path reader view. No historical helper,
hash or disk input is weakened/rewritten. Real image audit uses raw reads.

## Installed Image And Bank

The actual guest owner, ELF and progress builds pass. The entire ELF equals
its first emitted-slot prediction: **six changed bytes**, only in the target,
no metadata edits/exclusions. All **6,057** bodies/addresses and symbol
metadata are audited; the actual padded owner/relocations equal the qualified
one. Game data remains **189,088 bytes / 720 owners / zero differences**.
The complete guard prefix, including 299 legacy CRLF endings, is preserved
byte-for-byte; only the six generated LF rows are appended.

Installed ELF SHA is
`9a3f5eeca3804bde42fd9ee5b2dbd2d49c34ae58b7c5a1c47003f6e391a5441b`.
Installed guard SHA is
`6fbe433672dd2e72c09417034b7127feeba4ea827403c9ccbb55af83c3dd4a5e`.
The exact two-member successor view admits only these predicted artifacts
and restores readers/padder callbacks on exceptions; nested use is rejected.

Fresh official totals: **Game 2,967/4,828 (61.45%)**, total
**3,640/5,501 (66.17%)**, **1,861 different**, zero drift. Converted counts
and bytes are unchanged. Root README changes only its two matching rows.

Tools **bcedfb7** is committed before the consumer guards/docs/pin. All eleven
shared padder tests and smoke checks pass in both copies; six Windows ASCII
AST parses and three byte-identical mirrored pairs pass. Preserve mirror
HEAD **ddbdd16** and all **1,183** initial dirty hashes; only three absent
task paths are added, for **1,186** dirty paths. No mirror commit/reset,
Claude call, push or host-port/frozen Release action occurs.

## Next Action

The first raw-ranked `func_150A76F0` remains a handwritten live-register
fragment returning through V0, not an ordinary C target. Keep that separate.
Next ordinary C candidate: **func_15101148**, owner `generated_12DAB0`,
VA **0x15101148..0x151011E8**, ROM **0x12E5F8..0x12E698**, 40 words /
37 differences from its current placeholder. Retail conditionally releases
members in order +0x138/+0x13C/+0x134/+0x140/+0x144 through func_1516979C,
then calls func_1513CAA0 on the original owner. Read its caller/provider ABI
before recovering a typed, commented body. Preserve the original fade,
gate, additional-source, caller and inherited-stack queues and keep the full
Game objective open.
