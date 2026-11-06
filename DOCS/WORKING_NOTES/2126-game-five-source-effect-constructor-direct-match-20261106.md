# Five-source effect constructor direct match

Date: 2026-11-06. Continue the 80% goal from consumer
`dbaa75c3ab2f1067ed1d5e6779652bf4ebaf49eb` and mounted tools
`6d3c134f135987dbbc489da0e29b085b49cf213f`, following
[Note 2125](2125-game-controller-axis-sampler-match-and-constant-allocation-profile-20261106.md).

## Restored C

`func_150DB518`, owner `generated_108320`, now emits its complete **70-word**
slot directly from semantic C: VA `0x150DB518..0x150DB630`, ROM
`0x1089C8..0x108AE0`, 280 bytes, frame `0x90`, RA saved at SP+`0x2C`.
It uses the existing O2/g3 profile, one R_MIPS_26 binding and **zero guards**.
All five raw and padded neighbors, including the established parameter
clamp `func_150DB630`, remain unchanged. No Make or guard CSV edit is used.

The supported interface is `void(void*,void*,void*,void*,void*,s16,u8,s32)`.
All five source pointers and the signed low half of the sixth argument must
be nonzero; negative values pass. The first four raw argument words occupy
their original incoming homes. The compiler naturally recovers the ordered
home reloads, including branch delays, without volatile parameter qualifiers.
The seventh argument is consumed as an unsigned byte and the eighth as a word.

The request is exactly **0x58 bytes** at SP+`0x38`. Only **23 bytes** are
defined here: kind at +0, mode at +2, signed duration at +4, zero word +8,
flags +0xC, four color bytes +0x10..13, allocation flags +0x40 and two
0xFF bytes at +0x44..45. Reserved bytes retain their stack contents. The
factory's actual contract copies all 0x58 bytes; it does not justify a
blanket zero initializer. SDK native fixtures assert every used offset and
both structure sizes, and compare only defined request fields.

The call is `func_1513D524(&request,0,10,0,8,0,20,channel,context)`.
The existing header and factory C agree on its nine-argument interface.
On a nonnull result, the routine rereads the live source homes and stores
them at result+0x110/114/118/11C/120 in argument order **0,1,2,4,3**.
The null-result branch delay still reloads the first home. Guest fixtures
retain factory mutations of incoming homes and ordered output/home aliases.

An ordinary typed request already emitted 70 words/frame0x90 but differed
at 18 initialization words. Recovering statement order reduced that to four
color stores. Keeping RGB as one assignment chain and alpha separate recovers
all remaining words directly. Volatile parameter probes emitted 75 words
and were rejected. No compiler profile change or instruction normalization
was needed, and no Claude advisory call was used for this routine.

## Qualification evidence

All eight pre-install checks pass in both tools configurations; all eight
pass again after installation against both actual helper copies. The sibling
overlay is confined to the ignored build directory, preserving its six
tracked edits and 2,428 untracked files. Both tools smokes are fresh. Three
unchanged shared suites per copy are explicitly reused from the fingerprinted
Note 2124 receipts: match-progress, word patches and PC16 padding. They are
not represented as fresh regression executions for this target.

- **2,537 cases per body**, original/raw/padded, cover all 70 words, all 32
  source-pointer masks, signed-halfword truncation, all 256 channel bytes,
  negative and zero duration, nullable factory returns, complete guest packet
  and memory, live homes, source/output aliases and saved GPR/FPR/SP/RA.
- **217 access-cut prefixes** compare complete machine states across all
  three bodies, including saved RA, incoming homes, partial request stores,
  reject-path delay reads and the post-factory first-home reload.
- **256 cases per body** connect the original 28-word factory wrapper and
  114-word core. An independent public-output reference checks allocation
  arguments, full 88-byte descriptor copy, header fields, zeros and five
  final source stores. Under this root's fixed 0x401 flags and zero resource,
  **117 of 142 helper words** execute. Full helper-path coverage is not
  claimed. Allocator, byte copy, zeroing and two initializers are bounded;
  the independent reference does not claim their private stack or hardware.
- **64 cases per body** execute the original 12-word caller window in
  `func_150265CC`, with explicit prior A0/record/duration preconditions. The
  stack argument setup and caller branch delay overwrite the incidental
  result with one. Full parent execution is not claimed. Aligned-ROM census
  independently finds its sole JAL at ROM0x5593C and no tails/literal pointers.
- **Nine independent GNU links** over three R26 targets run 36 cases per
  body. The standalone fixture requires SUBALIGN(4), verifies the exact
  0x150DB518 entry and 280-byte symbol, and separately pins its eight zero
  container-alignment bytes. Initial failures exposed fixture alignment and
  tail-accounting errors; correcting those produced a fresh full pass with
  no C change and no production-image exclusion.
- **540,672 native32 SDK/UBSan calls** at O0/O2/O3 cover all 65,536 duration
  patterns, all source masks, channel/context boundaries, both factory
  outcomes, valid backing, direct calls and compatible callbacks. All output
  bytes and guards are checked; indeterminate request bytes are not scored.
  Ten incorrect variants fail with checked return code42 and no diagnostics.
- All 280 raw-byte corruptions, a binding corruption and five whole-image
  corruptions are rejected. The former zero-return stub and a 70-word source
  with the wrong color assignment shape also fail the exact-word gate.

## Actual production

Actual Make compiled this owner once under its unchanged default profile,
then linked and recounted the real production ELF:

```sh
make -C conker -o retail_word_patches.us.csv -o Makefile -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

The old-dependency flags retain the scoped-build procedure from Note 2125;
neither shared dependency changes here, while the changed source forces its
real compile. Keep both flags until a deliberate broader rebuild, without
touching unaffected object mtimes.

The actual ELF equals the independent **215-byte** prediction, with **zero
exclusions or metadata permutations**. Only the target slot and symbol size
(12 to 280 bytes) change. All **6,052 function addresses**, conversion rows,
progress.csv and **189,088 protected data bytes in 720 owners** remain fixed.
Compact GPR metadata changes from `8300C116` to `A300FFF6`, independently
derived from the body; its other 20 bytes and all padded pools are fixed.
The unfinished wider image retains its expected checksum failure and the
existing duplicate generated_12D630 recipe warning.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,195 / 5,512 (76.11%) | 0 | 1,317 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,522 / 4,839 (72.78%) | 0 | 1,317 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**215 more** matches reach the current 4,410 threshold for80%. Fingerprints:

- ELF: `d05bc50428188e52c31da38789d7fb077727db3df75df1af9bfb3cfff352cbcd`.
- Owner: `a60dd7161e9250faf31dca24897d6bf05849adad3670e985b0c8d779f06fe43d`.
- Code binary: `eb535f80d34a4e340e70f318a967fb0abc6ae21df9eb3cad4f2f1fb64d106fb2`.
- Unchanged guard CSV: `7d469fee131d8adbc169fda991046c614fea90f2704bfcd612c41371e6efa1f0`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence lives under `conker/build/game-five-source-effect-constructor-150DB518-match/`.
Graphify receives a scoped refresh with old-node retention accounting, without
claiming a full-corpus extraction. Tools are committed before the consumer.

Next: `func_151A3504` in `generated_1D0840`, another 70-word request builder.
Inspect its first-word gate, 0x30-byte input snapshot, position-query output,
partial 0x50-byte payload, allocator result+0x98 copy destination and return
preservation before recovery. Keep handwritten `func_150A76F0`, unrelated
work, private inputs/saves and frozen host Release separate. The 80% goal
remains active; these function tests do not claim host/gameplay acceptance.
