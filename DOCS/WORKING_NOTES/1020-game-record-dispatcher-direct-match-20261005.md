# Game Record Dispatcher Direct Match

Date: 2026-10-05. Starting checkpoint: `35a42809`.

Complete [Note 752](752-game-record-dispatcher-semantic-recovery-20261002.md)'s
semantic-but-overflowing `func_15040CC8`. All **38 words / 152 bytes** now
emit directly from C, in interval 0x15040CC8..0x15040D60, ROM
0x6E178..0x6E210. No guards, assembly edits, header changes or compiler
override. The previous 39-word overflow body and its trampoline are removed.

## Source And Compiler Boundary

[game_6D800.c](../../conker/src/game_6D800.c) retains the original recovered
contract: an empty sixteen-count delay, thirty direct eight-byte records
at indices -20 through 9, unsigned selector lookup through D_800844B0,
then one post-dispatch load of D_800848B0 and conditional cleanup.
Future selector, callback-table and cleanup-global mutations remain visible.

Two independent source changes are necessary under the unchanged default
IDO O2/g3/mips2/o32 profile:

- Keep the record address in an `s32`, matching the existing guest callback
  argument ABI, and use an unsigned-byte dereference for its selector.
- Update the signed index with `(i + 1) / 1`. This inhibits pointer strength
  reduction without emitting any divide instruction.

The second change alone retains the signed index/base/table in retail's
three saved registers and recovers the opening delay's S0 lifetime. But a
pointer-typed record still produces an extra V0-to-A0 move, for 39 words /
24 raw differences. The integer record alone remains strength-reduced,
39 words / 30 raw differences. Together they emit exactly 38 / zero.

Observed output establishes the retained index, folded divide and matching
instructions. The explanation that divide folding occurs after induction
analysis is a compiler-phase inference, not an instrumented IDO pass trace.
The index remains safely in -20..10; no signed overflow, division-by-zero,
pointer before the containing allocation or new volatile operation is used.
The record argument still points twenty records into a real allocation.

The complete **0x28 frame**, S2/S1/S0 saves at +0x20/+0x1C/+0x18, opening
base retention, sixteen-count delay, SLL/address computation, indirect
callback load/JALR, signed loop bound, branch-likely shift delay and duplicated
RA restoration all match retail. No insertion/omission normalization.

## Compiler Controls

[Induction driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_dispatch_induction_candidates.py)
freezes the old body independently of production. **45 controls** complete
with empty diagnostics. This is a new bounded index-canonicalization screen,
not a repetition of the historical 52 profile/for/do/goto trials.

| Control | Words | Saved Registers | Raw Differences |
| --- | --- | --- | --- |
| Frozen pointer-record baseline | 39 | 4 | 30 |
| Integer record only | 39 | 4 | 30 |
| Divide-by-one update only | 39 | 3 | 24 |
| Divide-by-one plus integer record | 38 | 3 | 0 |
| Inline/dereferenced address with divide update | 39 | 3 | 24 |
| Halfword/byte-narrowed index update | 41 | 3 | 25 |
| Negated-complement update | 40 | 3 | 25 |
| Unsigned biased bound | 38 | 3 | 25 |
| Post-increment loop header | 37 | 3 | 37 |

Other controls measure masked/split/unsigned/complement offsets, narrowed
index/condition/local types, biased/two-sided bounds and address increments.
Simply fitting a slot or reducing saved registers is not a match.
`division-unsequenced-negative-control` deliberately assigns/reads the same
local in separate call arguments; it is compiler-only and never installed or
semantically approved. All other compiler receipts likewise do not substitute
for qualification of the installed form.

The old **30 raw compiler differences** refer to its isolated 39-word body.
Note 752's **36 retail-slot differences** refer to the trampoline/padded slot;
these are different measurements and are not interchangeable.

## Qualification

[Matching tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_dispatch_match.py) pass
all eight tests. A fresh installed-source run, together with the existing
eight native semantic tests, passes **16 tests in 54.978 seconds**, no skips.
An earlier pre-install run passes seven qualification tests in 54.013 seconds.

- **12288 three-way guest cases** compare retail, isolated selected C and
  the independently frozen old semantic body. Every unsigned selector byte,
  zero/negative/high-bit cleanup state, eight callback-mutation modes and
  stack phases 0/8 are covered. All **38/38 retail words** are visited.
- Each case verifies thirty direct record addresses and callback identities
  independently, ordered non-stack reads/writes/calls, the complete non-stack
  image, exactly thirty table loads and exactly one post-dispatch cleanup
  load. Caller-saved registers/FPRs are clobbered at each helper boundary;
  all saved registers/FPRs survive.
- Mutations cover clearing or publishing cleanup, changing future selectors,
  replacing callback entries, combined selector/table mutation, repeated
  cleanup replacement and rewriting every remaining record/table entry.
- **Six high-address/repeat configurations**, for each of three instruction
  forms, preserve the guest s32 pointer ABI and restart at the first record.
  A second dispatch observes the first cleanup's cleared global.
- Signed-selector, wrong-stride, missed-final-record and missing-cleanup
  negative controls fail the retail contract. The signed-selector control
  may fail on its out-of-table address rather than a completed call trace.
- The selected body passes all eight existing source-extracted 32-bit native
  cases from [test_game_record_dispatch.py](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_dispatch.py),
  including sentinel preservation and future callback/selector mutations.
- Production source/slot identity, no target overflow symbol, unchanged next
  symbol/prototype, frame/saves, no divide and no guards are asserted.

The existing shared [TriangleOracle](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_actor_triangle_transform_match.py)
adds JALR dispatch to its existing call path. Target capture precedes the
encoded link-register write; zero-register writes remain discarded. A focused
same-register target/link test binds this ordering. Existing J/JAL handling
is otherwise unchanged. All three existing modules using TriangleOracle,
plus native record dispatch, pass **39 regression tests in 71.932 seconds**,
no skips. The unrelated historical full corpus is not rerun wholesale.

Callbacks and cleanup are bounded opaque helpers here, not their full bodies.
No null callback entry, invalid allocation, hardware cycle timing, FCSR,
complete caller chain or PC gameplay acceptance is claimed.

## Linked Image And Overflow Audit

Fresh DECOMP build/progress/match-progress targets succeed. The prior
position/radius checkpoint receipt contains **6060 linked symbols/slots**;
the new image contains **6059**. The only removed symbol is
`__retail_overflow_func_15040CC8`, whose 39-word SHA matches the independently
compiled frozen baseline. No symbol is added; all surviving lengths are
unchanged. All non-overflow addresses remain fixed.

Removing 156 bytes moves **16 later overflow symbols by -156 bytes**.
Every moved body's complete SHA remains unchanged. **13 retail trampoline
slots** change only their first jump word to the corresponding shifted body.
For every such slot, replacing that one target with its old address reproduces
the complete previous slot SHA. Apart from these proven retargets and the new
target body, every surviving slot is byte-for-byte unchanged. This is not an
"only target changes" audit; overflow compaction is explicitly accounted for.

The restored target SHA is
`6806b699ec97564c47babee61664cc680d3c94a42bad66a49e45e387e8a5b922`.
Local before/after slot and audit receipts are under
`conker/build/game-record-dispatch-match-test/`; full compiler inventory is
`conker/build/game-record-dispatch-induction/screen.json`.

Complete Init **164048 bytes**, Init data/rodata **17376 bytes**, Debugger
**19800 bytes**, and Game data **189088 bytes / 720 owners** remain retail-exact.
All **10637 existing guard rows** remain unchanged; none applies to this target.
No helper interface, data ownership, padding tool or guard is relaxed.

Exact totals become **3307/5462 (60.55%)**, Game **2634/4789 (55.00%)**,
Init **492/492**, Debugger **181/181**, zero retail address drift and
**2155 different Game C**. Conversion counts and retained Init assembly
inventory remain unchanged. README updates only aggregate tables.

`make tools-check`, whitespace and **2990 relative links** across nine
current/working documents pass; zero broken links.

## Reproduction And Next

```powershell
wsl python3 -m tools.experiments.game_record_dispatch_induction_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_record_dispatch_match tools.tests.test_game_record_dispatch -q -f
wsl python3 -m unittest tools.tests.test_game_actor_triangle_transform_match tools.tests.test_game_actor_context_dispatch_match tools.tests.test_game_position_radius_append_match tools.tests.test_game_record_dispatch -q -f
wsl make tools-check
git diff --check
```

Continue Game matching. Nearby `func_1508B2A8` remains a false zero-return
placeholder in generated_B3020.c; its retail 84-word recursive record-neighbor
visitor is a next recovery candidate, not a completed caller qualification.
The triangle read/frame boundary in
[Note 1017](1017-game-actor-triangle-cached-iterator-audit-20261005.md),
func_150E6FAC's duplicated RA load and handwritten func_150A76F0's separate
register-contract lane remain open. Note 1019's proposed 15040CC8 follow-up
is now complete.

No sibling source/build/save/frozen Release change, host transplant or push.
The full Game matching goal remains active.
