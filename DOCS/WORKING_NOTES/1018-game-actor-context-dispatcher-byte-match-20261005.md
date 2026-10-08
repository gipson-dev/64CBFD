# Game Actor Context Dispatcher Byte Match

Date: 2026-10-05. Starting checkpoint: `e72210db`.

Complete the matching work from
[Note 785](785-game-actor-context-dispatcher-semantic-recovery-20261003.md).
`func_15044380` now matches all **107 words / 428 bytes**, interval
0x15044380..0x1504452C, ROM 0x71830..0x719DC. The next symbol is unchanged.

## Source And Compiler Closure

[generated_71820.c](../../conker/src/game/generated_71820.c) adds one typed
enable-byte pointer, assigned from the valid indexed element at each visit.
No explicit one-before-array C pointer arithmetic is introduced. Its local
declaration restores the **0x68 frame** and saved context at **SP+0x5C**;
mode/second-pass inputs are at SP+0x78/+0x7C. All floating and saved-register
homes, helper arguments, branch targets and delay slots match directly.

The unchanged default IDO O2/g3/mips2/o32 body has 107 words and **15 raw
differences**, down from the previous 107 / frame 0x60 / 20. The linked
match uses 15 expected-word guards, two preserving the exact HI16/LO16
relocations for D_800DBE62. No inserted/omitted words, padding, assembly
changes, compiler override or file-wide helper-prototype changes.

The remaining changes are exhaustively closed, not an unexplained batch:

| Lifetime | Raw Register | Retail Register |
| --- | --- | --- |
| Accumulated result | s7 | s6 |
| Eligibility pointer | s6 | s5 |
| Context limit 3 | s5 | s4 |
| Enabled constant 1 | s4 | s3 |
| First-pass mode | s3 | s7 |

Renaming every use within the active lifetimes leaves only the independent
three-instruction reorder at +0x94/+0x98/+0x9C (mode load and constants),
and the commutative unsigned addition at +0xF4. Saves/restores remain
individual and unchanged. All 107 normalized instructions then equal retail.
No call, branch target, memory address, frame offset or delay-slot behavior
is changed by the normalization.

## Qualification

[Pointer driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_actor_context_pointer_candidates.py)
freezes the old body independently of the live source. Nineteen controls
measure enable/eligibility pointer declarations and sum operand order.
Enable-pointer-before/middle forms recover frame 0x68 / 15 differences;
after forms retain 0x60 / 20. Explicit eligibility-pointer forms canonicalize
to 105 words / 99-100 differences and are not installed. Swapping the C sum
operands does not change compiler output. All controls have empty diagnostics.

[Matching tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_actor_context_dispatch_match.py)
pass **nine tests in 14.461 seconds**, no skips. They bind source identity,
the 19-form inventory, frozen baseline, frame/homes, complete allocation
cycle, actual object words/relocations, and production slot equality.
The actual guard emitter rejects missing or changed relocation symbols;
every stale expected word fails and every omitted cycle word has a bounded
behavioral counterexample.

Three-way retail/raw-C/old-C comparisons cover **6144 static cases plus
40 helper-mutation cases**, with all **107/107 retail instructions** visited.
They compare ordered external reads/writes, helper calls/arguments and the
32-bit result, with caller-saved registers/FPRs deliberately clobbered.
Saved registers/FPRs must survive at both stack phases 0 and 8.

Cases include enable bytes 0/1/2/255 in all four positions, zero/positive/
negative second-pass flags, context-3-only actor exclusion, any nonzero
post-switch eligibility, by-value XYZ, mode/zero secondary argument,
modular result overflow, post-preparation context capture, future-enable
mutation, and preparation changes to flags/extents. Final switch-to-zero
precedes the saved context restoration, including after secondary mutation.

The existing 14 source-extracted native tests and the other shared-slice
regressions pass in a fresh **320-test / 28-module run in 57.212 seconds**,
no skips. It includes all nine new matching tests and all 311 shared-slice
tests. An earlier standalone shared run passed 311 in 61.319 seconds.
The historical 367-test triangle/resource corpus is not rerun wholesale;
this run covers the full affected generated-slice regression surface.
Helpers here are opaque mocks:
this is dispatcher and instruction matching, not full actor-chain, FCSR,
hardware execution or PC gameplay acceptance. In particular the older
dimension/context-helper interface caveats in Note 785 are not resolved by
this dispatcher match.

## Linked Audit

The fresh DECOMP build and progress targets succeed. Across **6060 slots**,
only func_15044380 changes; all addresses and slot lengths remain intact.
Its linked SHA-256 is
`9442aaf3ed05edc7a8215c0d19d67b7613fc24130edbf399f9cfaa60ad54bb4c`.
Three-vertex transform, original preparation assembly, matrix/height
wrappers, triangle remap and every other linked slot are unchanged.

Complete Init **164048 bytes**, Init data/rodata **17376 bytes**, Debugger
**19800 bytes**, and Game data **189088 bytes / 720 owners** remain
retail-exact. The patch CSV adds exactly 15 rows to 10622; all previous
rows are unchanged. No relocation guard is relaxed.

Exact totals become **3305/5462 (60.51%)**, Game **2632/4789 (54.96%)**,
Init **492/492**, Debugger **181/181**, zero address drift, **2157 different**.
Conversion counts and the retained Init assembly inventory are unchanged.
README changes only these aggregate tables; detailed progress stays in DOCS.

`make tools-check`, whitespace and **2982 relative links** across nine
current/working documents pass; zero broken links. All 19 compiler controls
were rerun against the final unchanged preamble and reproduced their scores.

## Reproduction And Next

```powershell
wsl python3 -m tools.experiments.game_actor_context_pointer_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_actor_context_dispatch_match tools.tests.test_game_actor_context_dispatch tools.tests.test_game_actor_preparation_assembly tools.tests.test_game_three_vertex_transform tools.tests.test_game_entity_scan_assembly -q -f
wsl make tools-check
git diff --check
```

The affected-slice suite selects every `tools/tests/test_*.py` containing
`generated_71820.c`, `func_15044660` or `func_1504452C`, then adds
`tools.tests.test_game_actor_context_dispatch_match`. Load these 28 modules
with `unittest.defaultTestLoader.loadTestsFromNames` and run fail-fast; the
current selection contains 320 tests. This avoids importing unrelated heavy
triangle/reference suites just to exercise the shared slice.

Continue Game matching. The triangle transform remains 302 words / frame
0x140 / 242 differences with unresolved early read/SDK lifetimes; the
[cached audit](1017-game-actor-triangle-cached-iterator-audit-20261005.md)
records the rejected frame regressions. The nearby low-difference
`func_150E6FAC` still needs retail's duplicated return-address load explained;
its already-measured return/goto/profile controls do not close that gap.
Keep handwritten `func_150A76F0` in its separate register-contract/assembly
lane instead of interpreting its placeholder score as a C scheduling fix.

No sibling source/build/save/frozen Release change, host transplant or push.
The full Game goal remains active.
