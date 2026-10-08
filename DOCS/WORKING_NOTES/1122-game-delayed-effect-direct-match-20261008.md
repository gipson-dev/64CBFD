# Game Delayed Effect Direct Match

Date: 2026-10-08

## Result

Continue the adjacent placeholder from
[Note 1121](1121-game-effect-registration-direct-match-20261008.md).
Install complete semantic `func_15033AD8` in
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c).
All **65 words /260 bytes** emit directly under existing IDO5.3 O2/g3,
with the original **0x40 frame**, zero raw or linked differences.
The old zero-return placeholder differs at all 65 words.

VA `0x15033AD8..0x15033BDC`, ROM `0x60F88..0x6108C`.
Retail: [5D2C0.s](../../conker/asm/5D2C0.s).
No guards, filler, generated data, compiler-profile, Makefile or shared-header
changes. Add owner-local unsigned D_800BE616 and typed four-float proximity
declarations, consistent with the existing shared headers. Reuse the recovered
Init allocator interface and existing D_800BE9E4/callback declarations.
Two calls and three HI16/LO16 pairs remain symbolic relocations.

## Recovered Contract

1. Retain original node/actor pointers in S1/S0. Read unsigned D_800BE616
   before the node state. If nonzero, submit the actor's three binary32
   coordinates and radius **900.0f** to `func_1508B20C`; ignore its return.
2. Read full node +0x38 **after** that callback, so its mutations are visible.
   Any nonzero state returns zero without reading timer, step or allocation
   coordinates. With flag zero, actor storage is unnecessary on this path.
3. With state zero, read signed32 timer +0x3C. Below **30**, read D_800BE9E4
   and add it once, without clamping or allocating on the same call even if
   the new timer crosses 30. The IDO/retail `addu` wraps at 32 bits.
4. At timer >=30, do not read the step. Read coordinates +0x14/+0x18/+0x1C
   in that order; truncate to signed32 then sign-extend the low halfword for
   the recovered signed16 allocator arguments. The optional first callback
   can change these later coordinate reads.
5. Submit the complete twelve-word call:
   `func_1000FA64(0x513, x, y, z, 32000, 1000, 500, callback, node, actor, 0, 0)`.
   The callback is symbolic `func_15033BDC`; its integer callback/actor words
   follow the existing Init declaration, not a guessed variadic interface.
6. Store the legal zero-extended u16 result to node +0x3C, then **0x513** to
   +0x38. Both stores occur even on zero result and overwrite callback
   mutations. There is **no high handle bit** here. Return zero on all paths.

Frame: outgoing arguments +0x10..+0x2C; S0 +0x34, S1 +0x38, RA +0x3C.
Callback changes to incoming parameter homes do not replace retained pointers.
Signed C overflow is not a portable-language claim: modular overflow evidence
comes from executing selected IDO and retail instructions. Native GCC checks
stay within non-overflow arithmetic and defined float-to-s16 ranges.

## Source Fit

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_node_delayed_effect_candidates.py)
finds the direct match on the first complete positive state guard/if-else form.

| Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Selected /register-both /implicit parameter narrowing | 65 | 0x40 | 0 |
| Explicit unsigned wrapping update | 66 | 0x40 | 48 |
| O2 without g3 | 64 | 0x40 | 65 |
| O1/g3 | 63 | 0x38 | 65 |
| O1 | 62 | 0x38 | 57 |

The unsigned update is semantically consistent but not raw exact. Coordinate
cast controls still narrow through the typed allocator, so are not negatives.
Seventeen source/profile forms and ten effective compiled semantic negatives
check proximity polarity, full state width, signed timer, exclusive threshold,
step source, absent high bit, effect/state identities, radius and coordinate
bit interpretation. Ordinary alternate-profile executions compare public
effects and legal ABI, not private frames or full register schedules.

## Qualification

[Seven tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_node_delayed_effect_match.py):

- **10,360 guest cases**: 3,072 global-axis, 1,680 lifecycle, 1,512 callback
  and 4,096 coordinate-grid cases. Cover all 256 flag bytes, six full state
  patterns, ten signed timer patterns, seven increments, six legal u16 results,
  seven callback mutation modes and two SP phases. All **65/65 words execute**.
  Compare independent reference public read/write order, complete call ABI,
  callback state/timer observations, return and memory. C/retail also compare
  complete GP/FP state, trace, memory and saved registers.
- Four lazy gates, twelve required-storage fault prefixes and two aliases
  qualify flag/state/timer/step/coordinate read lifetime, node=actor and an
  increment source aliasing the timer. No arbitrary private-frame alias claim.
- **524,288 actual native32 executions** qualify complete C with asserted
  4-byte pointers/int/float and 2-byte s16. Coverage arrays prove all **65,536
  allocator results** and all **65,536 signed16 X coordinates** reach creation.
  Check complete callback ABI and every byte of input canaries, including
  callback-mutated coordinates and post-allocation overwrite. Axes are
  correlated in this native sweep; the guest coordinate grid is independent.
- Actual copied owner retains **39 unchanged neighbors**, relative relocations
  and normalized pools, with strict zero diagnostics. Real padder emits exactly
  260 bytes without filler or new data. Seven independent links rebase entry
  and all five symbols, including three signed-LO carry cases.

The first seven-test run takes **60.273s**: five pass; native fixture compilation
rejects misleading indentation, and the baseline assertion expects a delay-slot
zero return rather than the actual opening zero instruction. Split the native
checks onto separate lines and assert the actual three-word placeholder prefix.
No production candidate or comparison relaxation. All **seven pre-install
tests pass in64.312s**, zero skips/errors/failures.

The earlier effect-registration stub-owner fixture now retains the allocator
prototype shared by this new caller, with an exact absence assertion before
restoration. All strict neighbor/relocation/pool/padder checks remain intact.

All **47 post-install focused tests pass in544.431s**, zero skips/errors/
failures: seven new, eight previous effect, seven latch, eight matrix caller/
helper, seven cleanup, four binding and six scheduling checks. Ten shared
padder/word-patch tests pass in0.046s. Both tools checkouts pass project-tool
checks; Python syntax, driver source/profile/CLI and whitespace checks pass.
Documentation validation: **105 documents /3,844 relative links /zero broken**.
Verify all three changed tools files are byte-identical in both local copies.
Graphify's required AST-only update completes; its existing skill-version,
empty devcontainer and large-HTML visualization warnings are not build failures.

Proximity, allocator and effect callback remain controlled hooks, not actual
connected callee bodies. Invalid FP conversions, NaN/infinity, FCSR exceptions,
full hardware/gameplay and PC-port acceptance remain unqualified. No Claude
model call or workflow setup was required; no sibling Release/save/runtime change.

```sh
python3 -m tools.experiments.game_node_delayed_effect_candidates
python3 -m tools.experiments.game_node_delayed_effect_candidates --profiles
python3 -m unittest tools.tests.test_game_node_delayed_effect_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

Run from the decomp root with the pinned tools mounted. New tools/test changes
are mirrored in the sibling `64CBFD Tools` working copy, but are **uncommitted**
at this handoff. GitHub links describe intended published paths and are not
publication evidence; the committed tools pin remains unchanged. See
[tools repository setup](../TOOLS_REPOSITORY.md) for ownership.

## Linked Audit

First verify the live pre-install ELF equals
`game-node-effect-registration-test/after.json`: all 6,058 symbols unchanged.
After installation, the full audit retains **6,058 symbols /6,042 retail slots /
16 overflow symbols**. Only `func_15033AD8` changes; **6,057 other bodies** and
every address/extent are unchanged. Verify the old placeholder hash and all
65 previous differences. `.init`, `.init_data`, `.debugger` and `.game_data`
are unchanged; all 720 Game-data owners /189,088 bytes remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
All **11,144 guard rows** and conversion CSV hash are unchanged.

Fresh exact totals: **3,377/5,467 (61.77%)**, Game **2,704/4,794 (56.40%)**,
**2,090 different /zero drift**. Init 492/492 and Debugger 181/181 stay exact.
The placeholder already counted as C, so converted counts/bytes do not change.
README changes only the two matching aggregate rows. New ignored baseline:
`conker/build/game-node-delayed-effect-test/after.json`. ELF/progress rebuild
succeeds with the existing duplicate generated_12D630 recipe warnings.

## Next Work

Next local placeholder **`func_15033BDC`**, **137 words /548 bytes**, frame
**0x40**, VA `0x15033BDC..0x15033E00`, ROM `0x6108C..0x612B0`.
Static inventory only, not an installed candidate:

- Effect packet +0x18/+0x1C supply node/actor. Null node, actor or actor +0
  returns 1. Copy truncated actor coordinates to packet signed16 +2/+4/+6.
- Active input word/action0x37 selects optional audio from cached actor type,
  including type0x15F's random low-two-bit 0x444..0x447 selection, then updates
  node +0x38 from the live actor type and returns zero.
- Other active actions gate on actor attachment +0x31C, counter +0x19C <120
  and node state0x513. Store state0x3A1 before twelve-word effect allocation;
  reload callback-mutated node home before storing its handle. Return 1 only
  on this creation route; other active routes return zero.
- Inactive action0x37 optionally stops packet audio handle +0x24, reloads the
  packet home, clears its handle and clears the output halfword supplied by
  the seventh argument. Preserve branch-likely and private home lifetime.

Recover the typed callback ABI from actual callers before installation.
Continue wider Game matching, open `func_15031070` resolver and full callee/
runtime work. This checkpoint does not close that goal.
