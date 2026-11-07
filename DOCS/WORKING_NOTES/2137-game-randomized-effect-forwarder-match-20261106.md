# Randomized effect forwarder matched with closed RNG capture homes

Date: 2026-11-06. Continues [Note 2136](2136-game-texture-tile-scanner-match-20261106.md)
from consumer `82c56ed1007a84d9f747c56b07f4309967faaf47` and tools
`720a669bd5a5a15429d70c0aaccc7a5474575b48` toward the active 80% goal.

## Recovered source and interface

`func_151C5588` in `conker/src/game/generated_1F2730.c` now has a complete
semantic C body. All **71 words / 284 bytes match after three guarded local
home adjustments**. Raw C remains three words different. VA
`0x151C5588..0x151C56A4`, ROM `0x1F2A38..0x1F2B54`, no alignment tail;
frame **0x58**, saved RA at SP+0x3C. The default O2/g3/MIPS2/O32 profile is
unchanged. No inline ASM or dummy frame-padding declarations are added.

The five incoming values are an owner pointer, **position pointer**, signed16
duration, unsigned8 selector/priority byte, and a full-word final parameter.
The position pointer refines the initial private draft's generic integer name.
Both original callers ignore the returned value, while the original body
forwards the submission helper's allocated pointer or null. One caller passes
an existing position buffer; the other passes its own three-float SP+0xD4
buffer. The helper's original followup entry loads the forwarded angle with
LWC1 and position with LW before copying its coordinates.

The first float draw is multiplied by D_800AAABC, increased by 604.0f,
multiplied by D_800AAAC0, and retained as the second scale word. The second
float draw is multiplied by 59.0f, increased by 141.0f, multiplied by
D_800AAAC4, and retained as the first scale word. **Two integer RNG calls
remain**, including the second state-advancing call whose result is not part
of the public submission. A third float draw supplies the final angle-like
parameter: draw*270.0f+D_800AAAC8. Float32 rounding follows each operation;
live global coefficients are read after the corresponding providers return.

func_15102B38 receives fourteen words: owner,0,D_800AAA90,D_800AAA9C,
pointer to the two scale floats,(first integer draw&3)+6,255,float value,
position pointer,255,0,signed duration,unsigned byte,full-word parameter.
Original helpers and handwritten RNG assembly are preserved. This target
does not convert or claim new C credit for those routines.

## Three home guards and frame provenance

The two-element integer array retains both observed stores. Scalar and
two-field-struct alternatives remove the second store and fail the literal
body; changing declaration order also displaces the float pair. These rejected
screens remain ignored. No unused third array element or fake local was added.

Read-only CFE/UOPT/UGEN observation runs in newly owned compiler children with
fingerprint checks, completed producers/consumer/driver, four fired frame
events, and identical isolated/full-owner output. CFE M20 remains UOPT M20;
the local area rounds to24 bytes, plus56 outgoing argument bytes and8 saved
bytes: **24+56+8=88**. The two-float pair already occupies retail SP+0x50/54;
the original frame, argument homes, RA and every other word already match.

The normalizer accepts the complete raw body and all 18 bindings, then derives
only three stack-immediate changes: stores at offsets0x7C/0x84 and the reload
at0x9C. Raw homes SP+0x48/4C move to retail SP+0x44/48. Both are private
integer capture words; the only escaped local address remains the disjoint
float pair SP+0x50. All operations, registers, calls, scheduling, bindings,
frame, extents and other 68 words stay fixed. The CSV appends three explicit
expected-word guards with no insertions, omissions or relocation changes.
Retail words are an independent acceptance oracle, not derivation inputs.
This is a guarded match, not a direct/raw compiler-output match claim.

## Fresh qualification

Eight target methods pass before and after installation in both tools
configurations. The sibling uses an ignored five-module overlay with its
actual existing helpers; its six tracked edits and 2,428 untracked paths are
preserved. Both tools smokes are fresh; three unchanged shared suites per
copy are explicit fingerprinted reuses from Note 2124. No Claude call was used.

- **371 guest cases per body**, retail/raw C/normalized, including all 256
  byte inputs, signed16/full-word boundaries, live coefficient/template/position
  mutation, nullable result and owner. **48 cases per body connect the original
  18-word integer and 25-word floating RNGs**, covering the twelve retained
  64-bit seed patterns and final state. All 71 root words and both RNG bodies
  are visited. Raw C agrees on public memory, calls, payload and result;
  normalized complete machine state matches retail literally.
- **32 private-home alias cases per body** and **133 fired access prefixes**
  check normalized full state, including writes to both capture homes and
  incoming argument homes. Raw private-home/fault equivalence and portable
  access-fault semantics are not claimed.
- **96 cases per body** connect the complete original 134-word submission
  helper, with all words reached. Independent checks cover all fourteen
  incoming words, copied owner/template payload, factory/followup arguments,
  null/allocated result and RNG state after its sixth draw. A separate actual
  **24-word followup entry** verifies the angle's floating load and the
  position-pointer load. Allocator and followup remainder remain explicit
  opaque boundaries; this is not full engine acceptance.
- **96 cases per body** execute both original caller windows (seven/six
  words), proving all five arguments and both real position-buffer routes,
  with saved integer registers and GP/SP/FP preserved. Whole parents
  func_150265CC and func_151C5280 remain unqualified.
- **Six independent GNU links**, three entry/global layouts, all 18 bindings,
  signed low16 carry and JAL rebase, with 36 cases per body and zero standalone
  tails. The actual retail slot has no tail.
- **SDK native32 O0/O2/O3 with UBSan** compares independently generated,
  separately rounded Python payload rows: **319 positive cases per profile**,
  **957 positive executions**, **8,613 total source calls** including eight
  wrong-source controls. All controls fail checked state/result comparisons
  (mask255), not sanitizer traps. Types, five RNG calls, pointer identity,
  pair order, live globals and mixed-width provider arguments are checked.
  FCSR, hardware exceptions and nonfinite native payload identity are outside
  this acceptance claim.
- All 284 raw byte corruptions, all 18 binding corruptions, a production
  expected-word corruption, six full-image corruptions and the old stub are
  rejected. All 7 raw/padded neighbors, data pools and register metadata stay
  fixed. All **122 frozen production/compiler inputs** are audited.

## Actual production and literal image accounting

```sh
make -C conker -o retail_word_patches.us.csv -o Makefile --output-sync=target -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

Only generated_1F2730.c recompiles, exactly once, with zero C diagnostics.
Actual padded owner and ELF equal independent predictions. The whole ELF
changes by **411 bytes**, with **zero exclusions**: the target body, its
symbol size 12 to 284, and six closed GNU symbol/name pair permutations are
reconstructed from the frozen predecessor. All named definition attributes
remain identical, apart from the declared target size. The original strict
target-only gate caught the permutations; the final predictor accounts for
every serialized byte rather than excluding metadata sections.

All **6,052 function addresses**, conversion rows, progress.csv, Make rules
and **189,088 protected Game data bytes in 720 owners** stay fixed. The existing
duplicate generated_12D630 recipe warning and expected unfinished-image
checksum failure remain.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,206 / 5,512 (76.31%) | 0 | 1,306 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,533 / 4,839 (73.01%) | 0 | 1,306 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**204 more** matches reach the current 4,410 threshold for 80%.

- ELF: `a6b0d2c2d2a6067ef4b698a9388277e06ac46071e382d05446afb0c98b17b516`.
- Owner: `ba1c87ba8f5a0fbe4be738794dbad54bdfb2c741ed3897b486f3663e4596bd0d`.
- Code binary: `4a43ad886a2918ed370fbdbd0b499f37c0ab57024cfe7b36333f965e04ee26b7`.
- Guard CSV: `28d7a491d60ac432579e06040e28e21cd7e074d6a47e5c665d1d466ef42670ee`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence: `conker/build/game-random-effect-forwarder-151C5588-match/`.
Tools are committed before source, guards, docs and consumer pin. Scoped
Graphify retention is checked; no full-corpus extraction is claimed. Root
README gets aggregate rows only. The host port needs no source transfer from
this retail-only C recovery; its source and frozen Release remain untouched.

## Resume boundary

Next: **func_15080228**, generated_AD6B0,72 words/frame0x138,
VA0x15080228..0x15080348, ROM0xAD6D8..0xAD7F8. It polls a 256-byte command
buffer, recognizes byte0x4C, combines four 7-bit bytes, divides by 367 with
zero mapped to 20, then dispatches through the current actor index. Recover
the reader and dispatcher ABI, signed division, live global timing, original
caller and genuine buffer frame before qualification. It is uninstalled and
uncredited. Preserve unrelated work, private inputs/saves, handwritten
func_150A76F0 and frozen host Release. Keep the full 80% goal active.
