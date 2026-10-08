# Game Effect Callback Scheduling Match

Date: 2026-10-08

## Result

Continue the callback identified in
[Note 1122](1122-game-delayed-effect-direct-match-20261008.md).
Install complete semantic `func_15033BDC` in
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c).
The linked routine is byte-exact across **137 words / 548 bytes**, retaining
the original **0x40 frame**. Raw IDO 5.3 O2/g3 C matches **135/137 words**;
two expected-word guards swap independent type-store/zero-return scheduling.
This is a **guard-normalized match**, not a direct compiler-only match.
The old zero-return placeholder has 127 real word differences.

VA `0x15033BDC..0x15033E00`, ROM `0x6108C..0x612B0`.
Retail: [5D2C0.s](../../conker/asm/5D2C0.s).
No filler, inserted or omitted instructions, generated data, profile, Makefile
or shared-header changes. Three owner-local sound/RNG declarations agree with
the existing shared interfaces. Four calls and the self-callback HI16/LO16
pair retain symbolic relocations.

## Callback ABI

Verify the Init allocator and dispatcher, rather than inferring the pointer
arguments from this routine alone:
[init_EB00.c](../../conker/src/init_EB00.c) contains `func_1000FA64`,
`func_10011624` and the seven-argument callback invocation. Its `struct15`
record is 0x30 bytes; allocation arguments eight/nine populate +0x18/+0x1C.

Recovered signature: packet, value, volume, pan, cents, fx, sound-ID output.
The active gate reads the **third argument**, a full signed32 volume word.
The second/fourth/fifth/sixth pointees are unused; the seventh is `u16 *`.
The local `u8 *packet` represents the same guest record without a shared
structure refactor. Native tests assert the complete 32-bit pointer ABI.

## Recovered Contract

1. Load both packet +0x18 node and +0x1C actor before pointer gates. Null
   node/actor or zero actor fullword +0 returns 1. Otherwise copy coordinates
   +0x14/+0x18/+0x1C to packet signed16 +2/+4/+6, interleaving each load,
   truncation and store before reading volume. Earlier stores survive a later
   required-storage fault.
2. With nonzero volume and action byte node +1 ==0x37, load the full node
   cache +0x38 but compare only its low16 against unsigned actor type +0x84.
   Changed type 0x15F selects `(func_150ADA20() & 3) + 0x444`; other changes
   do not draw RNG or play audio. Submit `(0, soundId, 24000, 0, 0, actor)`
   to `func_10010FFC`. Reload actor/node private homes after RNG and play;
   then store the live actor type to full node +0x38 and return 0.
3. With nonzero volume and other actions, read actor attachment +0x31C.
   Creation requires nonnull attachment, unsigned16 counter +0x19C **<120**,
   and full node state +0x38 ==0x513. Otherwise return 0.
4. On creation, write state **0x3A1 before allocation**. Read coordinates
   in emitted X/Z/Y order, passing signed16 X/Y/Z in the twelve-word call:
   `func_1000FA64(0x3A1, x, y, z, 32000, 1000, 500, self, node, actor, 0, 0)`.
   The callback can overwrite state; do not restore it. Reload the node home,
   store the legal zero-extended u16 result to +0x3C even if zero, without a
   high handle bit, and return 1.
5. With zero volume and action 0x37, optionally stop nonzero unsigned16
   packet handle +0x24 using `func_100111C8`. Reload the packet home after
   stop before clearing the handle, and reload the incoming seventh-argument
   pointer before its halfword clear. Return 0. Other inactive actions
   return 1 without reading attachment/cache/handle/output.

Frame: RA +0x34, actor +0x38, node +0x3C; incoming packet +0x40, unused
value +0x44 and pan +0x4C, final pointer +0x58. Controlled hooks can redirect
the actor/node/packet homes or incoming sound-output pointer where retail
actually reloads them. Unused pointer arguments need no pointee storage.

## Source Fit

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_node_effect_callback_candidates.py):
the initial complete inline-cache body has 35 differences at the correct
137-word length/frame. Giving the cached node word an explicit local recovers
33 words without changing the public contract. Twenty-one targeted
source probes retain two differences; no production volatile annotation.

| Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Inline cache, O2/g3 | 137 | 0x40 | 35 |
| Selected explicit cache, O2/g3 | 137 | 0x40 | 2 |
| O2 without g3 | 136 | 0x40 | 135 |
| O1/g3 | 148 | 0x50 | 147 |
| O1 | 148 | 0x50 | 146 |

The two appended rows in
[retail_word_patches.us.csv](../../conker/retail_word_patches.us.csv) are:

| Offset | Expected | Replacement |
| --- | --- | --- |
| 0x108 | 0x00001025: zero return | 0xAD0F0038: node type store |
| 0x110 | 0xAD0F0038: node type store | 0x00001025: zero return |

The intervening unconditional branch word67 (`0x10000041`) is unchanged.
The store's T0/T7 operands are independent of V0. Both instructions execute
on the same routes, each original instruction occurs once, and no branch
destination or relocation changes. The real padder rejects stale expected
words and relocations. Raw fault-time GP state at this scheduling pair is
not claimed identical; fault checks qualify public prefixes and stores.

## Qualification

[Seven tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_node_effect_callback_match.py):

- **12,352 guest cases**: 3,072 selector, 2,304 gate, 2,880 callback and
  4,096 independent coordinate-grid cases. Cover all 256 action bytes,
  full32 volume, unsigned types/counters, low16 cache comparison, eight
  mutation modes, six RNG/results and two SP phases. Independent reference
  checks public read/write order, calls, preallocation observations, return
  and memory. Raw C/normalized C/retail also compare complete GP/FP state,
  trace, memory and saved-register ABI on ordinary executions.
- **135/137 words execute**. Missing indices 69/118 are duplicated pointer/
  action loads bypassed by branch-likely routes; both still emit and match.
  Four lazy gates, twenty fault prefixes and three aliases (packet=node,
  packet=actor, sound-output=packet+0x24) qualify storage requirements,
  partial coordinate writes, live type and private-home reload lifetime.
- Nineteen source/profile forms, 48 ordinary control executions and eleven
  effective compiled semantic negatives cover wrong volume argument, cache
  width, inclusive counter, counter byte width, effect ID, state-after-call,
  RNG mask, sound amount, clear-before-stop, word output and inactive return.
  Alternate-profile checks compare public behavior and ABI, not private frames.
- **524,288 complete native32 C executions** assert 4-byte pointer/int/float
  and 2-byte s16. All 65,536 unsigned types/counters are exercised; explicit
  allocator coverage proves every u16 result and signed16 X reaches creation.
  Check complete calls and every input/output canary byte, state-before-call,
  type-after-play, inactive handles and null unused pointer arguments. Native
  axes are correlated; guest coordinate-grid axes are independent.
- Actual copied owner retains **39 unchanged neighbors**, normalized pools
  and relative relocations, with zero diagnostics. Real padder emits exactly
  548 bytes, no filler or new data. Seven independent links rebase entry and
  all five symbols, including one signed-LO self-callback carry case.

The first six-test run takes **57.549s**, with three fixture failures:
volume/output buffers at 0x40000 overlap oracle stack storage, defeating a lazy
case and the wrong-volume negative; native GCC rejects attachment +0x19C in
a 64-byte fixture. Move buffers to 0x50000 with an explicit stack-disjoint
assertion, give attachment 0x1C0 bytes and complete canaries, and add the real
copied-owner/padder check. No production-body or comparison relaxation.
The corrected **seven pre-install tests pass in 96.442s**, zero skips/errors/
failures. Only the corrected runs qualify these cases.

All **54 post-install focused tests pass in 439.695s**, zero skips/errors/
failures: seven callback, seven delayed effect, eight registration, seven
latch, eight matrix, seven cleanup, four binding and six scheduling checks.
Ten shared padder/word-patch tests pass in 0.046s. Both tools checkouts pass
project checks; Python syntax, driver source/profile/CLI, whitespace and
required Graphify AST update pass. Graphify's existing version/devcontainer/
large-HTML warnings do not invalidate its graph. Documentation validation:
**106 documents /3,856 relative links /zero broken**. All six changed tools
files are byte-identical in both local copies. The post-regression linked
audit retains the same one-target change and exact slot.

RNG/play/stop/allocation and the original Init dispatcher are controlled
interfaces, **not connected complete callee bodies**. Guest finite int32-trunc/
low16 behavior beyond s16 is instruction evidence, not portable C conversion;
native/alternate-profile checks remain in defined conversion ranges. Invalid
FP, NaN/infinity, FCSR, arbitrary private aliases, full hardware/gameplay and
PC-port acceptance remain open. No Claude call or workflow setup was needed;
no OGL Release, save, configuration or runtime change.

## Linked Audit

`make -C conker -j4 build/conker.us.elf progress.csv` succeeds. Changing the
guard CSV rebuilds other guarded objects; existing compiler and duplicate
generated_12D630 recipe warnings remain, so this is not a warning-free build.
The isolated candidate/copied owner are diagnostic-free.

Compare against `game-node-delayed-effect-test/after.json`: **6,058 symbols /
6,042 retail slots /16 overflow symbols**. Only `func_15033BDC` changes;
**6,057 other bodies** and all addresses/extents are unchanged. `.init`,
`.init_data`, `.debugger` and `.game_data` stay unchanged. All 720 Game-data
owners /189,088 bytes retain SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
All prior **11,144 guard rows** and conversion CSV hash are unchanged; append
exactly two scheduling rows, total **11,146**. The shared history helper checks
the exact prior slices and exact new pair, not a relaxed tail comparison.

Fresh exact totals: **3,378/5,467 (61.79%)**, Game **2,705/4,794 (56.42%)**,
**2,089 different /zero drift**. Init 492/492 and Debugger 181/181 remain exact.
Converted counts/bytes do not change: the former placeholder already counted
as C. Root README changes only its two matching aggregate rows.
New ignored baseline: `conker/build/game-node-effect-callback-test/after.json`.

```sh
python3 -m tools.experiments.game_node_effect_callback_candidates
python3 -m tools.experiments.game_node_effect_callback_candidates --profiles
python3 -m unittest tools.tests.test_game_node_effect_callback_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

Tools changes are mirrored in mounted `tools/` and sibling `64CBFD Tools`,
but are **uncommitted/unpublished**, along with the previous delayed-effect
checkpoint. GitHub tool links describe intended paths, not publication proof.
Committed tools pin stays `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`.
See [tools repository setup](../TOOLS_REPOSITORY.md). No commit/push this turn.

## Next Work

Next local **`func_15033E28`** remains compiler-generated assembly, not a
zero-return placeholder: **23 words /92 bytes**, frame **0**, VA
`0x15033E28..0x15033E84`, ROM `0x612D8..0x61334`.
Static inventory only; no C candidate installed:

- Walk the list headed by D_800C3EE0, returning zero without actor/output
  reads for an empty head. Preserve the redundant opening null gate.
- Compare actor byte +0x3B against each node byte +0. Reload actor group each
  iteration, allowing aliased output stores to change a later comparison.
- Snapshot next pointer +0x54 **before** any matching-node output store.
  Append matching node pointers to the supplied output array and return count.
- Do not invent capacity/cycle limits or a terminator store absent from retail.

Resume from the new baseline. Continue wider Game matching, the open
`func_15031070` resolver and complete callee/runtime work; this checkpoint
does not complete the wider goal.
