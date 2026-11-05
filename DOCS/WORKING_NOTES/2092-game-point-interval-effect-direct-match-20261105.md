# Point-interval effect callback directly byte-exact

Date: 2026-11-05. Target `func_150EB090`, owner `generated_118400`.
Source `conker/src/game/generated_118400.c`; retail `conker/asm/118400.s`.

## Outcome and scope

The callback replaces its zero-return placeholder with semantic C. All 73
body words emit directly under the existing O2/g3 profile; its 88-byte frame,
six bindings and three alignment words match without guards, inserted/omitted
instructions, profile changes or shared-header edits. The matcher covers the
complete 76-word slot. The other two owner routines remain byte-exact and
unchanged in raw and padded objects, including pools and bindings.

Production is **4,163/5,512 (75.53%)** total, **3,490/4,839 (72.12%)** Game,
zero address drift and 1,349 still different. Init remains 492/492 and Debugger
181/181. Conversion inventory remains 5,512/6,046. The active 80% threshold is
4,410 exact functions: **247 more** are required at this denominator.

## Retail contract and source shape

Body VA `0x150EB090..0x150EB1B4`, ROM `0x118540..0x118664`; the aligned
slot ends at VA `0x150EB1C0`, ROM `0x118670`. The recovered callback signature
is `void(u8 *actor, s32 mode, s32 amount)`. Both integer inputs arrive as full
words. It returns immediately when actor+`0x1D4` is zero. Otherwise it queries
`func_150EAF50(position, actor, &result, (u8)mode)`. A zero answer suppresses
the final effect submission.

The successful path calls:

```c
func_15141F78(10, (u8 *)&result, (f32)amount * D_800A1470,
              (u8)(u32)(*(f32 *)(actor + 0x40) * D_800A1474), position, mode);
```

The constants are float words `0x3C40C0C1` and `0x3F360B61` at
`0x800A1470/0x800A1474`. Their decimal renderings are approximately
0.01176470611 and 0.7111111283. The explicit unsigned-word then byte cast
exposes retail's two-stage conversion, including byte wrap. It emits the same
instructions as the original implicit byte-cast screen, while native tests
can cover the finite unsigned-word domain above 255.

The existing named `HeightResult71820` is completed locally using the actual
36-byte definition from `generated_71820.c`: height, nine signed vertex
halves, padding half, metadata word, flags/state bytes, padding half, value
word. No shared declaration is changed. Position is at SP+`0x4C`, result at
SP+`0x28`, the copied low mode at SP+`0x24`, RA at SP+`0x1C`; incoming homes
are SP+`0x58/0x5C/0x60` after frame allocation.

The full-width mode formal recovers the retained local copy and frame. A
byte formal instead emits frame80 and 17 differences. Full-width mode with
nested gates has only two opening-load differences. The early matrix-pointer
return recovers the exact duplicated actor-home load and subsequent mode
load. Typed actor, flat-gate and assignment screens remain private; no
volatile qualifier, dummy local or instruction guard is used.

The actor and amount homes are read again after the point query, so guest
home mutations can change the tag source and scale. The incoming mode home
can change without changing its earlier low-byte copy. If an alias overwrites
the copied local itself, the reloaded word changes and is forwarded; the
effect callee's mode type is u8. Actor-tag aliases with the vector, result,
mode copy and saved RA are explicitly checked.

The conversion saves its pre-conversion FCSR, requests truncation, handles
the unsigned high half using the `2^31` subtraction path and restores the
saved control before the effect call. Qualification uses the existing bounded,
nontrapping control model. It does not claim hardware exception flags,
enabled traps, denormal treatment or NaN payload fidelity. Native C tests
restrict the converted tag product to the finite unsigned-word domain.

## Registration and caller boundaries

The aligned retail census finds no direct JAL and exactly one target-pointer
word: ROM `0x22EBDC`, VA `0x8008A11C`. It is callback/count pair 13 in
`D_8008A0B4`, with count **85**. The source assembly block contains 43 words
including its terminal/padding words; that is not a 43-entry callback claim.

Both original `func_15141A7C` call interfaces are checked. The five-word
window at `0x15141B4C` forwards actor, context and zero. Its earlier classifier
gate reaches this direct-call branch only for a nonpositive count. This
callback's real positive count instead calls `func_15141E38(actor,13)` to
create/refresh a timed record; that actual earlier route is executed and
asserted separately. The first window is an interface boundary test, not a
claim that the retail count85 naturally takes it.

The eight-word window at `0x15141BAC` reloads table[index].callback and
forwards actor, context and the signed half at record+`0xE`. This is the
timed-record callback route. Earlier iteration/registration services and the
complete dispatcher are outside these bounded windows; no parent credit or
gameplay acceptance is added.

## Focused qualification

New modules: `game_point_interval_effect_candidates.py`,
`game_point_interval_effect_match.py`, and
`tests/test_game_point_interval_effect_match.py`. Existing compiler/padder,
MIPS/native32, FP-control and image helpers are reused without edits.

```sh
python3 -m unittest tools.tests.test_game_point_interval_effect_match -v
python3 -m unittest tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
```

Nine pre-install checks pass in 40.423 seconds. Shared 19 checks pass in
8.297 seconds; `make tools-check` passes. The installed suite is rerun fresh.

- 3,328 guest cases per original/compiler body cover every low mode byte,
  upper input bits, matrix/return gates, signed scale boundaries, finite and
  special float words, unsigned conversion paths and preserved control.
  All 72 reachable body words execute. The duplicate MFC1 at `0x150EB178`
  is unreachable after an unconditional branch; it remains byte-exact and
  is included in raw-corruption controls and the full slot comparison.
- 144 private-home/alias cases compare original and compiler complete state,
  independent public effects, call packets and result/vector bytes. Two cases
  overwrite saved RA and compare the actual redirected return state rather
  than calling them normal returns. The reference was corrected to reload
  the mutable local mode copy instead of treating it as immutable.
- 48 cases execute the original 56-word `func_150EAF50` helper, including
  modes zero/one/two/255, matrix gates and positive/negative/zero query results.
  Its resolver, initializer and lower query remain bounded providers. The
  original helper does not gain another matching-function credit here.
- Both dispatcher windows pass 96 cases per body, with signed halfword
  values -32768/0/85/32767, full context words, matrix/answer gates and stack
  phases. The real positive-count registration route is also checked.
- 92 fired access prefixes compare complete private state. A disabled matrix
  path succeeds with tag and constant bytes unmapped. Fault-order evidence is
  guest instruction evidence, not portable C fault behavior.
- Six independent GNU links compare original and compiler bodies across
  three layouts, both constant HI/LO carry edges and relocated call targets;
  48 rebased cases per body pass.
- Native32 O0/O2/O3 each execute 480 direct and 480 typed indirect calls,
  totaling 2,880 positive executions. Eight independently compiled wrong-C
  controls fail with trap UBSan and float-cast-overflow instrumentation.
  Eight actual IDO controls also have guest counterexamples. Actual result
  size and metadata/value offsets are asserted; actor backing is a fresh
  typeless allocation. Private guest home aliases are not native C claims.
- All 292 raw-byte flips and six binding corruptions fail closed. Whole-ELF
  corruptions outside the body and in alignment, plus four named metadata
  corruptions, are rejected. Both raw/padded neighbors and pools remain exact.

The first registry fixture incorrectly counted the assembly block as 42 words
instead of 43. Initial alias reference assumptions missed the mutable local
copy and redirected-RA cases. These fixture corrections precede the accepted
full run; product C, bytes and shared helpers were not changed to bypass them.

## Full image, production and recount

The production owner and ELF equal the independent compiler/padder/linker
artifacts byte for byte. Actual Make exits zero for the ELF and progress CSV.
All 6,052 function addresses and every other body remain fixed. Protected
Game data remains 189,088 bytes across 720 owners, with zero differences.
Guard CSV, layout, linker, conversion CSV, Makefile, complete retail input,
three shared headers and original text/registry assembly bytes are unchanged.

The entire **224-byte** ELF delta is independently predicted: 208 target-code
bytes, two bytes for symbol size 12 -> 292, and 14 bytes of named symbol
serialization. Referencing `D_800A1470` changes one linker hash-bucket collision
order with `D_8009CF70`: complete records at file `0x2D892C/0x2D893C` and
their two name strings swap positions. The predictor reconstructs both records
and strings solely from the pinned predecessor, preserving each symbol's
value, size, binding and section. Nothing is excluded or accepted from the
candidate image as a metadata template. This bookkeeping is not a code guard.

`make -C conker all` generates the code binary, then returns 2 at the expected
overall retail SHA mismatch for the incomplete decomp. The existing duplicate
`generated_12D630` recipe warning remains; no new owner warning is introduced.

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,163 / 5,512 | 75.53% | 0 | 1,349 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,490 / 4,839 | 72.12% | 0 | 1,349 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

The README updates only aggregate matching rows. This note and concise
current indexes hold the recovery and continuation details.

## Fingerprints and preserved scope

| Artifact | SHA-256 |
| --- | --- |
| Raw compiler target | `5a25e25740153faa7b6bb8bc60578768f6c5b63c6d94927bc0bf86f3df1b582e` |
| Linked retail body | `56dfa682164737f2cddb643c198a161d15896bdcb09ff6b0a2629a12103042fb` |
| Frozen predecessor ELF | `0547aedf1ed72a2ee2dc86c0b28a5f40d33f098984f9b078c5d11ce4f53afcde` |
| Qualified/production owner | `09d275dfc8dc90704458badf4b7db0f5bf312415603b9bd98b7db9b56ab28e1d` |
| Qualified/production ELF | `4a421a1bed2aab994b0ed564b673113dddcba2262cafd4aa4480e58fea16397f` |
| Production code binary | `8787922afd9f4f27f8d30a731f2f07cc433c40fe55ae998826152d5913d83ab4` |
| Guard CSV, unchanged working bytes | `1bb99ac99a4ee64a166ac72314f7af2b3d44d88cbfe954522f88242233415466` |

Ignored artifacts are retained under
`conker/build/game-point-interval-effect-150EB090-match/`, including frozen
inputs, independent owners/images, native fixtures, JSON receipts, Make logs
and live recount. Private source-shape screens stay in the adjacent candidate
directory and receive no credit. Unchanged neighbor-suite evidence is reused
through complete raw/padded byte, binding and pool equality, not called fresh.

Main baseline is `c4a4c473a184d19d6536f70c7f5c256a6632e7f9`; mounted tools
baseline is `f66a70a74094586c7b8ea88295f7f14c4e26b120`. Both were clean on
entry. Freeze-time Git counts include the newly created candidate file.
The sibling tools checkout at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`
retains its six existing tracked changes and 2,428 untracked files untouched.
Fresh checks use the mounted checkout only; no sibling qualification is claimed.

## Continuation and graph retention

The actual production rerank selects `func_1510ADD8`, 66 words with 65 real
differences. Keep the seven documented boundary cases separate:
`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC` and `func_150A6760`.

The fresh installed nine-test suite passes in **50.575 seconds**. Mounted
tools are committed first as `0ec84a9a3c2a84ed2def1f9274f14dcf9ebc2b8c`
(`test(game): qualify direct point-interval effect callback`). The consumer
includes that pointer, the recovered C and docs; the guard CSV is untouched.

The standard Graphify update refused a reduced 24,865-node extraction and
retained the existing graph. Scoped maintenance of seven changed paths
produces 58,667 nodes, 112,424 links and 5,169 communities. It retains
58,655 old nodes, relocates three update-log headings by the same label/source,
and adds nine nodes from this note. No node outside the changed paths is
removed. The graph SHA-256 is
`8e8d4c4cc89a0de6b907a043e412cf94b3713ee8d8e3f3616c08eeb747ea7534`.
Existing exclusions retain 31,816 nodes from 3,754 still-existing files.
This is scoped structural maintenance with retention, not full-corpus
re-extraction or fresh extraction of excluded source files. The ignored
`graph-retention.json` records the exact comparison.
