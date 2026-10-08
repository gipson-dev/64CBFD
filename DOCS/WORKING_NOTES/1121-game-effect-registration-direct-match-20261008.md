# Game Effect Registration Direct Match

Date: 2026-10-08

## Result

Continue the adjacent placeholder from
[Note 1120](1120-game-attachment-state-latch-direct-match-20261008.md).
Install complete semantic `func_150339C8` in
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c).
All **68 words /272 bytes** emit directly under existing IDO5.3 O2/g3,
with the original **0x40 frame** and **zero raw or linked differences**.
The previous zero-return placeholder differs at all 68 words.

VA `0x150339C8..0x15033AD8`, ROM `0x60E78..0x60F88`.
Retail: [5D2C0.s](../../conker/asm/5D2C0.s).
No guards, filler, generated data, compiler-profile, Makefile or shared-header
changes. Add owner-local declarations for D_800BEA0C and the allocator, using
the existing recovered allocator interface in
[functions.h](../../conker/include/functions.h) and
[init_EB00.c](../../conker/src/init_EB00.c).
The three calls and four HI16/LO16 address pairs remain symbolic relocations.

## Recovered Contract

1. Preserve node/actor in S1/S0. Always call the matched tile-scroll routine
   `func_150334B8(node, actor)` **before** reading either global gate. Ignore
   its return. Its actual body can mutate the fourth tile-size command even
   when this routine subsequently exits at the mode/freeze gate.
2. Read unsigned mode byte D_800C35EA. Only value 1 returns immediately;
   values 0 and 2..255 proceed. Read unsigned freeze byte D_800BEA0C next.
3. With freeze nonzero, read the full node +0x3C handle. If nonzero, call
   `func_1000FD38(func_15033BDC, node, actor)`, then clear the handle to zero.
   The callback observes the old handle; any callback handle mutation is
   overwritten. Clear also occurs when the initial handle is zero.
4. With freeze zero, preserve any nonzero handle without reading coordinates
   or making another allocation. Otherwise read actor binary32 coordinates
   +0x14, +0x18 and +0x1C in that order. Retail truncates each toward signed
   int32, then sign-extends its low halfword for the signed-16 interface.
5. Submit the complete twelve-word call:
   `func_1000FA64(0x448, x, y, z, 32000, 1000, 500, callback, node, actor, 0, 0)`.
   The callback pointer and actor's pointer-sized word use the existing Init
   declaration's integer fields, not a guessed variadic interface.
6. Store returned handle OR 0x80000000 at the original node +0x3C, including
   when the legal u16 result is zero. Do not add an allocation-failure gate or
   reread globals after the callback. Return zero on all paths. Incoming-home
   mutations do not replace the pointers retained in the saved registers.

Private frame: outgoing arguments +0x10..+0x2C, saved S0 +0x34, S1 +0x38,
RA +0x3C. The global mode gate is not permission to skip the first helper's
required storage or faults.

## Source Fit And Controls

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_node_effect_registration_candidates.py)
recovers the direct match on its first complete source form. The positive
mode guard/if-else lifecycle and the allocator's recovered signed-16 argument
types fit the retail calls and coordinate schedule naturally.

| Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Selected /register-argument controls | 68 | 0x40 | 0 |
| Implicit parameter narrowing after s32 coordinate cast | 68 | 0x40 | 0 |
| Early mode return | 70 | 0x40 | 57 |
| O2 without g3 | 66 | 0x40 | 67 |
| O1/g3 or O1 | 66 | 0x38 | 66 |

The s32-coordinate cast is a source control, not an effective negative: the
allocator parameters still narrow to signed16. **Eighteen measured forms**,
**27 ordinary executions** and **nine effective compiled negatives** cover
skipped scrolling, wrong mode gate, missing high handle bit, byte-sized handles,
clear-before-unregister order, integer coordinate-bit interpretation, reversed
coordinates, wrong effect identity and swapped rate/limit.

Ordinary alternate-profile executions stay within the defined float-to-s16
conversion domain; their private frames and raw upper argument bits are not
claimed identical. Separate selected/retail instruction tests qualify finite
signed-int32 truncation followed by low-half narrowing beyond the s16 range.
NaN/infinity, invalid conversion, FCSR exception behavior and abstract C behavior
outside the defined conversion domain are not inferred from the bounded oracle.

## Qualification

[Eight tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_node_effect_registration_match.py):

- **14,208 guest cases**: 2,048 global-axis, 8,064 lifecycle and 4,096
  coordinate-grid cases. Each global covers all 256 bytes. Eight handle
  patterns, six legal u16 allocator results, seven callback mutation modes,
  two SP phases and sixteen finite binary32 coordinate patterns qualify.
  Compare an independent reference's public read/write order, calls, callback
  handle observations, return and memory; compare full GP/FP state, complete
  trace/memory and saved registers for C versus retail.
- **67/68 words execute**. Word 27, the duplicated node-handle load at
  VA 0x15033A34, is bypassed by both retail branch-likely routes, but still
  compiler-emitted and checked byte-exact.
- **576 connected guest cases** execute actual C/retail tile-scroll bodies,
  both selectors, global/freeze/handle gates, two allocation results, all six
  command layouts and two SP phases. A null-command lazy case and **six
  connected fault prefixes** prove malformed helper storage faults before
  either global gate is read, including mode 1. No helper-return shortcut.
- Three other lazy cases, **eight standalone fault prefixes** and three
  aliases cover required global/node/coordinate storage, node=actor and a
  handle destination overlapping a global. The first helper is a controlled
  hook in these standalone cases, not an inferred full helper execution.
- **1,572,864 actual native32 executions** qualify the complete C body,
  with 4-byte pointers/2-byte s16/4-byte binary32 asserted. Explicit coverage
  arrays prove all **65,536 u16 results** and all **65,536 signed16 X
  coordinates** actually reach creation, not merely get seeded behind a gate.
  Check every input byte, complete callback ABI, pre-unregister handle and
  post-callback clear/high-bit store. Axes are correlated in the native sweep;
  the guest coordinate grid is independent.
- Actual copied owner has **39 unchanged neighbors**, unchanged relative
  relocations and normalized pool identities, with strict zero diagnostics.
  The real padder emits exactly 272 bytes without filler/data. **Eight
  independent links** rebase entry and each of six symbols, including three
  signed-LO carry cases for globals/callback pointers.

The initial eight-test run takes **33.320s**: seven pass, one alternate-profile
control fails because its out-of-s16-domain input has different raw upper
coordinate argument bits under O1. Bound ordinary controls to the defined
conversion domain; retain the selected/retail wider instruction checks.
Strengthen native mutation routing and coverage arrays so every result and
signed16 coordinate is observed at creation. The next **eight tests pass in
96.321s**, zero skips/errors/failures. Production candidate is unchanged by
these fixture-only corrections. The final post-install run also includes the
six added connected fault prefixes.

The first 37-test post-install run takes **202.786s**: 36 pass, the earlier
[cleanup owner fixture](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_node_cleanup_match.py)
fails compilation because stripping its declaration block also removes the
callback/unregister prototypes now shared with this effect caller. Retain
exactly those two declarations in the stub baseline, with count assertions;
keep every strict neighbor/relocation/pool/padder check. No production change
or comparison relaxation. The targeted fixture passes in **3.426s**.

All **37 post-install focused tests pass in221.412s**, zero skips/errors/
failures: eight new, seven latch, eight matrix caller/helper, four earlier
owner/padder, four selection-binding and six selection-scheduling checks.
Ten shared padder/word-patch tests pass in0.040s. Tools, Python syntax,
driver source/profile/CLI and whitespace checks pass. Documentation validation:
**103 documents /4,200 relative links /zero broken**.

Allocator, unregistration and the effect callback remain controlled test hooks.
Their complete implementations, full hardware/gameplay and PC-port acceptance
are separate. No sibling Release build, save or runtime is modified.

```sh
python3 -m tools.experiments.game_node_effect_registration_candidates
python3 -m tools.experiments.game_node_effect_registration_candidates --profiles
python3 -m unittest tools.tests.test_game_node_effect_registration_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

## Linked Audit

Against `conker/build/game-node-attachment-latch-test/after.json`, retain all
**6,058 symbols /6,042 retail slots /16 overflow symbols**. Only
`func_150339C8` changes; **6,057 other bodies** and every address/extent
are unchanged. Verify the old placeholder hash and 68 previous differences.
`.init`, `.init_data`, `.debugger` and `.game_data` are unchanged. All
720 Game-data owners /189,088 bytes remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
All **11,144 guard rows** and the conversion CSV hash are unchanged.

Fresh exact totals: **3,376/5,467 (61.75%)**, Game **2,703/4,794 (56.38%)**,
**2,091 different /zero drift**. Init 492/492 and Debugger 181/181 stay exact.
The placeholder already counted as C, so converted function/byte counts stay
unchanged. Root README changes only the two aggregate rows. New ignored
receipts/audit/baseline: `conker/build/game-node-effect-registration-test/after.json`.
ELF/progress rebuild succeeds with existing duplicate generated_12D630 recipe
warnings; no repository-wide warning-free claim.

## Next Work

Next local placeholder **`func_15033AD8`**, **65 words /260 bytes**, frame
**0x40**, VA `0x15033AD8..0x15033BDC`, ROM `0x60F88..0x6108C`.
Static inventory only, not a recovered candidate:

- Optional D_800BE616 gate calls `func_1508B20C` with actor coordinates and
  binary32 radius 900 before the node-state gate.
- Nonzero node +0x38 returns zero. Otherwise a signed timer at +0x3C below
  30 adds D_800BE9E4 once without clamping, then returns zero.
- At the timer threshold, allocate effect 0x513 with the same coordinate/
  callback contract. Store the returned handle and state 0x513, even on zero
  allocation result. Preserve pointer relocations and callback/read lifetime.

Continue wider Game matching, the open `func_15031070` resolver and complete
callee/runtime work. This checkpoint does not close that goal.
