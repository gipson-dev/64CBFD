# Microcode Loader Installed Guarded Match

Date: 2026-10-16. Consumer predecessor **d03359a8**, tools predecessor
**27dc235**. Complete the installation gates from
[Note 1461](1461-microcode-loader-guarded-match-qualification-20261016.md).

## Installed Contract

func_1501CC3C in conker/src/game/generated_49D30.c now replaces its zero-return
stub with the complete semantic microcode loader. The linked routine matches
all **97 words / 388 bytes**, VA **0x1501CC3C..0x1501CDC0**, ROM
**0x4A0EC..0x4A270**. The C emits 96 words, normalized by exactly **23 guards**:
this is a **guarded match, not a direct compiler match**.

Retain the original **frame 0x30**, S0/RA saves, range SP+0x20, paired offset
SP+0x28, variant SP+0x2C and existing O2/g3/no-unroll profile. No frame/home/
saved-lifetime repair. All **56 raw owner neighbors**, including the direct
239-word task parent, remain unchanged. Note 1461 owns the three exact guard
groups and raw-object/binding proof; do not duplicate or broaden those rows.

The proper interface is **void func_1501CC3C(void)**. Comments identify the
four ROM-relative words per row. Preserve the unsigned selector promoted to
a word, signed cache bytes, full-word flag equal to one, four blocking DMA
packets, live table reloads and ordered cache/data-pointer publication. The
existing Init provider's s32(s32, void *, u32, s32) definition is unchanged.

## Remaining Caller Verified

GNU-assemble all **426 original words** of func_15007B3C and compare them with
ROM **0x34FEC..0x35694**. **192 three-way cuts** execute the actual JAL/NOP at
**0x15008138**, loader, then the real LUI/ADDIU/LW post-call window through
0x15008148. A0 becomes 0x800CC2D0 and T9 loads its first word; SP and RA are
correct. Two unrelated four-word incoming argument patterns have no semantic
effect, and the caller does not interpret a return value.

This validates an original caller artifact and call/post-call cut, not the
complete startup loop or a natural startup run. The synthetic high-byte table
domain and bounded DMA provider remain explicit.

## First Whole Image Prediction

Reproduce the predecessor independently, then predict every **3,257,636 ELF
bytes before installation**. Exactly **361 bytes** change:

- **321 code bytes**, entirely inside this routine's 388-byte slot.
- **Two size bytes**, changing the function extent from **12 to 388**.
- **38 metadata bytes** from exactly one symbol/string ordering swap:
  func_1518FC04 and D_80089324. Their named definitions remain respectively
  (0x1518FC04, 64, STT_FUNC) and (0x80089324, 0, absolute symbol).

All other bytes and canonical definitions remain identical. No metadata
exclusions, address-drift allowances or post-build-derived prediction.

First predicted and normally rebuilt ELF SHA-256:
**d32f3bfa87f40838eccd6a087afbaf0e199c438932cf5cd56703b6bf22315a89**.
Installed source owner:
**04b1a7d3944b4bc2874524b9f9e1833a28fad5356dd926aca64688c7db031431**.
Installed guard manifest:
**a66f4a4c85152fb6c8629c16b44fc8ee9272d0a39324c6e8c1373cbba8df50b5**.

Install only the predicted owner and append exactly 23 guard rows. Preserve
every previous guard byte and the existing **298 CRLF lines**. The Makefile
and all other source inputs stay unchanged. Git's line-ending conversion
warning is not suppressed or treated as a compilation failure.

## Fresh Validation

All **15 pre-install tests pass in 65.595s**. After installation and the normal
dependency rebuild, all **18 final tests pass in 101.175s**, no skips:

```sh
python3 -m tools.experiments.game_microcode_loader_installation
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_microcode_loader_lifetimes \
  tools.tests.test_game_microcode_loader_native \
  tools.tests.test_game_microcode_loader_startup_caller \
  tools.tests.test_game_microcode_loader \
  tools.tests.test_game_microcode_loader_installed -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- Finish **695 compiler / 687 padder invocations**. The entire normal ELF
  equals the first prediction. Existing recipe/compiler warnings remain;
  this is not a warning-free build claim.
- Fresh target coverage retains **770 three-way guest cases**, 80 positive
  callback cases, 24 real-table cases, three independent original/C rebases,
  and **449 native32 O2/O0/UBSan cases each** with four effective controls.
- Execute **192 real task-parent/setup/loader cases** plus the **192 startup
  caller cuts** above. Retain **346 fired original/guarded fault prefixes**:
  105 isolated and 241 across the real 239-word parent/61-word setup chain.
- Check all **136 live inputs**, all **133 unchanged inputs**, the complete
  code/image/metadata prediction and unknown-successor corruptions. Protect
  **189,088 data bytes / 720 owners / zero differences**.
- Recognize only the three first-predicted successor hashes. Validate both
  before/after fixture stages and preserve the older seven-test research
  suite against its exact predecessor, rather than weakening its input gate
  to accept arbitrary current files. Those research tests are included in
  the 18, not counted as extra production coverage.

Raw C is qualified for public state and call semantics; literal private/
instruction/fault equality applies to original versus guarded emission.
PI/cache/queue hardware leaves are bounded, payloads use deterministic test
bytes, and extended high selectors use an explicit synthetic table. No full
startup, natural gameplay, RCP or host-port acceptance is inferred.
Zero new Claude calls; the prior advisory disposition stays in Note 1461.

## Progress And Bank

Fresh official matching: Game **2,937/4,828 (60.83%)**, total **3,610/5,501
(65.62%)**, still different **1,891**, zero drift. Init stays **492/492** and
Debugger **181/181**. Conversion remains **5,501/6,044 functions / 86.04%
bytes**, because the previous stub already counted as C. The regenerated
conversion CSV is literally unchanged. Root README changes only its two
matching aggregate rows; narratives remain here and in concise indexes.

Tools **fb26ff8** banks seven files before the consumer pin. Across both copies,
**14 Windows AST checks** pass, plus all eleven WSL padder tests per copy: active
**0.032s + 0.023s**, mirror **0.031s + 0.019s**. Consumer tools-check passes.
Preserve mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **932
other initial dirty-file hashes**, and synchronize only three existing task
files plus four new files, giving **939** final dirty paths. All seven pairs
match; no mirror commit/reset, push, host-port or frozen Release action.

- [x] Verify both actual callers, retaining the real 426-word startup caller artifact and its call/post-call window.
- [x] Reproduce the predecessor and freeze the complete independent first image/source/guard prediction before installation.
- [x] Install only the qualified semantic owner and 23 target guard rows, preserving original guard bytes and compiler profile.
- [x] Complete normal rebuild, all 18 final tests, exact successor/fixture corruption gates and protected-data audit.
- [x] Measure fresh official progress, update README aggregate rows only, and bank tools first then consumer source/pin/docs.

Next: **func_1501CE54**, still a zero-return stub in the same owner:
**105 words / 420 bytes / no stack frame**, VA **0x1501CE54..0x1501CFF8**,
ROM **0x4A304..0x4A4A8**. Recover the table/record scan, its -9999 sentinel
path and signed-halfword maximum while preserving the newly installed loader
and other owner functions. Timing's **141 differences**, wider Game recovery
and full gameplay acceptance remain separately open.
