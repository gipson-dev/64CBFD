# Cosine phase motion and alternating sound callback recovered

Date: 2026-11-05. Target `func_1510ADD8`, owner `generated_137ED0`.
Source `conker/src/game/generated_137ED0.c`; original `conker/asm/137ED0.s`.

## Outcome and scope

The semantic C body is installed after all nine pre-install checks and nine
fresh installed checks pass. Actual Make and the complete-image predictor
agree byte for byte. Fresh production is **4,164/5,512 (75.54%)** total and
**3,491/4,839 (72.14%)** Game, zero address drift and 1,348 still different.
The 80% goal remains active: 246 more exact functions to 4,410/5,512.

The routine has 66 words / 264 bytes, frame32, eleven bindings and no alignment
tail inside the slot. Nine checked words derive from four closed FPR lifetimes
and swapping two adjacent reads. There are no inserted/omitted instructions,
frame changes, compiler-profile changes or shared-header edits. All three
raw/padded neighboring routines, their bindings and normalized pools stay fixed.

## Recovered behavior and live reads

Body/slot VA `0x1510ADD8..0x1510AEE0`, ROM `0x138288..0x138390`.
The callback interface is `void(u8 *state)`. It advances the float at `+0x80`
by `(D_800A26B0 * (f32)D_800BE9E4) / 60.0f`, preserving separate single
multiply/divide/add operations and the signed tick conversion. Retail constant
words are `0x40490FDB` for both the rate and half-period threshold, and
`0x40C90FDB` for the full period, at `0x800A26B0/B4/B8` respectively.

The updated phase is reloaded into F12 before `cosf`. The callback saves its
record pointer in the incoming home in the cosine call's delay slot and reloads
it afterward. The cosine provider may change fields, constants or that home;
the subsequent work must use the live reloaded record. It computes cosine
times 10, reads the current value at `+0`, calculates **previous minus new**,
stores the new value at `+0` and publishes the delta at `+0x60`.

Any nonzero word at `+0x7C` selects the full-period branch. A zero word tests
phase >= half-period, sets the word to one and sends sound event `0x4CA`.
The nonzero branch tests phase >= full-period, computes phase minus one full
period, clears the word and stores the captured phase before sound `0x4CB`.
Only one threshold branch and one period subtraction occur per invocation.
Large phases do not cause a loop or two sound calls in one callback. Both
events pass record, event, 12000, 200, 1000 and flags4 to `func_15114D24`.

Capturing the wrapped phase before clearing the flag is necessary: the
full-period constant can alias that flag word. A reread after clearing it
changes the subtraction and is rejected by an actual compiled control.
The source uses ordinary scalar temporaries and pointer views; no artificial
volatile qualifier, dummy local or imported assembly body is substituted.

The source sound prototype reflects the inspected retail access widths:
record pointer, full event word, full volume word, signed pan/duration halves
and full flag word. The callback ignores its result. Its original flags4 path
reads the record's handle at `+0x74` and signed coordinates at `+0x10/12/14`,
calls `func_10010E78` with eleven arguments, and clears the record handle.
The other sound flag paths are outside this callback's connected claim.

## Closed guard derivation and relocation

The selected natural C has all 66 instructions and the original 32-byte frame.
Earlier source screens had 69 words because a post-flag constant reread
preserved alias semantics that retail does not have. Capturing the subtraction
first recovers the retail single read. Typed record views and ordinary local
variants remain private, uncredited source screens.

The four FPR-role intervals are:

| Raw interval | Natural FPR | Retail FPR | Value |
| --- | --- | --- | --- |
| `+0x64..+0x70` | F12 | F16 | Published delta |
| `+0x78..+0x88` | F6 | F18 | Half-period constant |
| `+0x7C..+0x88` | F16 | F6 | Live phase for half-period compare |
| `+0xD8..+0xE8` | F12 | F4 | Captured wrapped phase |

The normalizer maps only FPR instruction operands within these closed
definition/use intervals. GPR bases, stack words, branch conditions and
unrelated FPRs are untouched. A complete natural-body hash and exact eleven
bindings gate the derivation; the complete fitted object body must equal
the masked retail bytes.

Natural `LWC1 F0,+0x80(A0)` at `+0xB8` and `LWC1 F2,LO(period)(AT)` at
`+0xBC` swap to retail order. Both are reads with distinct destination FPRs,
unchanged base GPRs and no intervening write; coincident addresses remain
valid. The LO16 binding moves from `+0xBC` to `+0xB8` while its HI16 remains
at `+0x54`. Expected/replacement relocation rows explicitly describe both
ends of the move. Natural/fitted fault-order equality is not claimed for
this read swap; literal original/fitted fault prefixes are checked instead.

Nine derived rows cover `+0x64/70/78/7C/88/B8/BC/D8/E8`. The old guard CSV
prefix stays byte-exact, including its mixed historical line endings; nine
new rows use its final-line style. The first append attempt refused a false
uniform-CRLF assumption before opening the output for writing. The corrected
append preserves every existing byte and is checked against the frozen prefix.

## Registration and original callers

The complete aligned retail census finds no JAL/tail J and one target-pointer
word, ROM `0x22D984`, VA `0x80088EC4`. It is row47 in the twelve-byte
`D_80088C90` registration table, with zero secondary callback and zero mode.
The original 22-word installer at `0x1509EBBC` transfers that triple into
record fields `+0x38/+0x78/+0x92`; every instruction in that window is used.

Both original callback dispatches are executed at `0x15113EE8/0x15113FC0`,
inside seven/nine-word windows starting `0x15113EE0/0x15113FB8`. The record
is forwarded and the result register is poisoned four ways on return, proving
these bounded continuations ignore the callback's return value. Loop counters,
pointer updates and alternate continuations remain part of the original
windows; complete parent dispatchers are not claimed.

## Focused qualification

New tools are `game_cosine_phase_sound_candidates.py`,
`game_cosine_phase_sound_match.py` and
`tests/test_game_cosine_phase_sound_match.py`. Existing compiler/padder,
MIPS/native32, cosine reference and image helpers are reused without edits.

```sh
python3 -m unittest tools.tests.test_game_cosine_phase_sound_match -v
python3 -m unittest tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
```

All nine pre-install tests pass in **80.609 seconds**. Shared 19 regressions
pass in **9.594 seconds**, and `make tools-check` passes.

- 1,800 guest cases per original/natural/fitted body cover all 66 body words,
  signed tick extremes, half/full-period boundaries, arbitrary nonzero flags,
  finite/special float words, cosine values and post-call mutations. Independent
  public memory, calls and sound observations agree for all three bodies;
  complete original/fitted private state and traces agree.
- 240 constant/home/record aliases exercise period/flag/phase overlap, the live
  record home and private output words. Outgoing duration/flag words can
  overwrite an aliased record field before the sound call, and the RA save
  can overwrite an aliased input before phase arithmetic. The reference models
  both. Redirected returns and missing-pointer reads compare actual partial
  states; missing reads must also fail at the same byte in the reference.
  They are not presented as ordinary returns or portable C alias behavior.
- 144 cases per body execute the original 120-word sound helper's flags4 path
  with a bounded eleven-argument audio provider. Another 144 connect both that
  helper and the original 88-word cosine slot, including its real constants
  and independent cosine reference. Complete sound flag paths and hardware
  audio behavior are not claimed; no helper gains another matching credit.
- The 22-word installer and both dispatcher windows pass; the two dispatch
  windows cover 96 cases per body, four return poisons and both loop routes.
- 86 fired access prefixes compare complete original/fitted private state.
  Guest fault evidence is distinct from portable C and hardware exception
  behavior. Natural read-order fault parity is explicitly not claimed.
- Nine GNU links compare original/natural/fitted bodies across three layouts,
  with 72 rebased cases per body, high/low carry edges and all eleven bindings,
  including the moved LO16.
- Native32 O0/O2/O3 each execute 6,480 direct and 6,480 typed indirect calls,
  totaling **38,880** positive executions under trap UBSan. Ten native wrong-C
  controls fail. Eleven actual IDO controls have guest counterexamples,
  including the period/flag alias case that is outside the native fixture.
  Native cosine is a bounded provider; actual retail cosine is checked in
  guest execution. Native arithmetic inputs are finite.
- All 264 raw-byte corruptions, eleven binding corruptions, four real-padder
  preimage corruptions and five inside/outside/named-metadata ELF corruptions
  fail closed. Three raw/padded neighbors and normalized pools remain fixed.

Fixture corrections before the accepted full run added the cosine NEG/TRUNC
instructions, actually linked symbols into the alias layouts, separated a
rebase cosine address from the callback entry, modeled aliased outgoing/RA
stores and corrected native aggregate braces. Compiler failure diagnostics
are retained privately and their UI preview is bounded. Product semantics,
closed guard proof and acceptance assertions were not weakened to bypass them.

## Independent full-image prediction

The predicted full ELF changes **248 bytes** with zero exclusions: 218 bytes
in target code/symbol extent and 30 bytes of named linker serialization.
Only this function body changes; all 6,052 function addresses, protected Game
data (189,088 bytes / 720 owners), neighbors, old overflow regions and pools
remain fixed in the independently linked image.

Referencing `D_800A26B0` rotates one five-name linker hash bucket. The complete
symbol records at file `0x2B450C..0x2B454C` and their names rotate from
`D_800A26B0,D_800A1128,D_800AAA78,D_800AA9A8,D_8009CC28` to the same list
with its first item moved last. The predictor reconstructs every byte from
the pinned predecessor while preserving each symbol's value, size, binding,
section and destination name index. No candidate metadata is accepted as
its own template. This serialization is bookkeeping, not a code guard.

## Fingerprints and preserved scope

| Artifact | SHA-256 |
| --- | --- |
| Natural compiler target | `c3e4ed0649d8b692013b56f80caf5c403fc132706cf962a98ebec3b1eb29da6a` |
| Linked retail body | `c2112e688fd2b7156e8d496c079d8c3dc2d536b3a45d7632174c8ea8553da526` |
| Frozen predecessor ELF | `4a421a1bed2aab994b0ed564b673113dddcba2262cafd4aa4480e58fea16397f` |
| Qualified padded owner | `764d9588bc7dc7d2236ca5ba811a55bf207f82da8bb90ee384ccdcd1e720406f` |
| Qualified complete ELF | `426d61d5a54e30dffc620cd594ba46e49d11042889663ef9fb24295bc0ada0fc` |
| Production code binary | `a310f250c00907d0135bb68f7dbae8baae9c04864308425093c86c1e47dd6c65` |
| Guard CSV working bytes after nine rows | `52e92c5bf75905247a3d33df7ae1ee14274f6517d19e8b15a35a5153568c5bff` |

Artifacts are retained under ignored
`conker/build/game-cosine-phase-sound-1510ADD8-match/`, with private source
screens in the adjacent candidate directory. Frozen input bytes are never
recaptured. Repeated current-target fixtures are regenerated independently;
old neighbor suites are reused through unchanged bytes/bindings/pools rather
than claimed fresh.

Main baseline is `4377e418bd75ebb2805665794378db09edc7ef47`; mounted tools
baseline is `0ec84a9a3c2a84ed2def1f9274f14dcf9ebc2b8c`. Both were clean on
entry; freeze-time Git counts include the new candidate file. The separate
sibling tools checkout remains at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`
with six pre-existing tracked edits and 2,428 untracked files untouched.
Fresh target qualification uses only the mounted checkout.

## Production closure and continuation

The full four-job Make rebuild completes with exit zero for the ELF and
progress CSV. Its actual target owner equals the independently qualified
padded owner; its complete ELF equals the literal 248-byte prediction.
The fresh installed nine-test suite passes in **85.691 seconds**.

The old guard bytes are an exact prefix plus nine rows. Frozen original text,
registry/constant/sound assembly, complete retail input, layout, linker,
conversion CSV, Makefile and three shared headers remain unchanged. All 6,052
function addresses, every other body, old overflow regions, neighbors, pools
and 189,088 protected Game bytes across 720 owners remain fixed. No function,
section, symbol or metadata is excluded. Inherited SDK/pointer and duplicate
`generated_12D630` recipe warnings remain; no new target warning is introduced.

`make -C conker all` generates the code binary and returns 2 only at the
existing overall retail SHA mismatch, expected for the incomplete decomp.
The fresh actual-ELF recount reports:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,164 / 5,512 | 75.54% | 0 | 1,348 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,491 / 4,839 | 72.14% | 0 | 1,348 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

The converted inventory remains 5,512/6,046. Root README edits are aggregate
matching rows only; detailed recovery stays in this note and concise indexes.
Actual production ranking selects `func_1513A48C`, 66 words and 65 real
differences, as the next ordinary target.

Retain the seven documented boundary cases separately:
`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC` and `func_150A6760`.

Mounted tools are committed first as
`07974169b42b61e52aff2faf03183752b424c663`
(`test(game): qualify cosine phase and alternating sound callback`). The
consumer includes that pointer, the recovered C, nine checked rows and docs.

Standard Graphify update refused a reduced 24,876-node extraction, preserving
the existing graph. The eight-path scoped refresh retains 58,664 old nodes,
relocates three existing `DOCS/UPDATE_LOG.md` headings and adds ten headings
from this note: 58,677 nodes, 112,432 links and 5,089 communities. No node
outside the changed paths is removed. The retention receipt records SHA-256
`9ca8e6b1eac68cf2c433f1915bc20427243d09d47bcd34c04c8e29ba3168928c`.
The 31,816 retained nodes from 3,754 still-existing files outside the current
scan corpus are preservation evidence, not a claim of fresh full-corpus
extraction. The ignored receipt is `graph-retention.json` in the qualification
directory.
