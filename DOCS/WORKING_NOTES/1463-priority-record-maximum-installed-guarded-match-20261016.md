# Priority Record Maximum Installed Guarded Match

Date: 2026-10-16. Consumer predecessor **4e56c53e**, tools predecessor
**fb26ff8**. Continue the same-owner handoff from
[Note 1462](1462-microcode-loader-installed-guarded-match-20261016.md).

## Installed Contract

func_1501CE54 in conker/src/game/generated_49D30.c replaces its false
zero-return stub with **void func_1501CE54(s32 slot)**. The complete linked
routine matches **105 words / 420 bytes**, VA **0x1501CE54..0x1501CFF8**, ROM
**0x4A304..0x4A4A8**. The C emits 105 words; exactly **48 relocation-aware
guards** produce retail emission. This is a **guarded match, not a direct
compiler match**. No frame, stack access, FPU work or outgoing call is added.
Retain the existing O2/g3/no-unroll profile and all **56 raw owner neighbors**,
including the newly restored 97-word loader and 239-word graphics-task parent.

- Clear the output word before reading the unsigned byte count. Zero count
  must not dereference any pointer table.
- Cache the primary-count pointer. If its first unsigned halfword is at
  least four, return the first preferred record's signed +0x12 override
  unless it is exactly **-9999**. Explicit zero and negative overrides are
  valid and must not be treated as missing values.
- Scan enabled records with nonzero primary counts for the largest signed
  +0xA value above the initial zero. An actual preferred output update, not
  merely an eligible record, suppresses the entire fallback pass.
- Otherwise reload the enable cursor and scan fallback tails. Reload the
  fallback-count pointer inside each enabled iteration, use the complete
  unsigned halfword count and load the signed value at **entries * 8 - 2**.
- Preserve cached byte count, pointer reloads, signed comparisons, the
  branch-likely index updates and both signed loop tests.

The local RecordMaximum49D30 definition names only the consumed prefix:
signed halfwords at **0xA** and **0x12**, with explicit padding. Its 20-byte
prefix is not a claim about the complete retail record size. Pointer rows
retain the observed **30 entries / 0x78-byte stride**. Comments explain the
preferred-before-fallback contract and the phase-dependent local value's
preferred-update flag lifetime. Original symbols remain address-named.

## Bounded Matching

Natural source/profile screens retain the existing no-unroll profile:
ordinary O2 unrolls the initial form to 255 words. Separate signed field
loads, full-word loop comparisons and the override/update/fallback local's
retail lifetime recover the original 105-word control-flow shape.

Pin all raw words, all **18 relocation bindings**, empty private pools and
the independently assembled original words/bindings. The only non-identity
instruction routing is the independent four-word fallback setup:
target/source offsets **0x11C/0x124**, **0x120/0x128**, **0x124/0x11C**,
**0x128/0x120**. After routing, every opcode, immediate, shift and special
function is identical. Only AT/temporary GPR operand fields may differ;
argument, output, zero, saved-register, SP and RA role repairs are rejected.
The remaining **44 guards** normalize temporary allocation only. There are
**no inserted or omitted words**, and no new compiler profile.

Raw C SHA-256:
**f5207f069387e6276e47b620614f3a25075067a0af2230ec741e0c613aa93b6f**.
Original unlinked text:
**1ca9ff9805fb6c8f36cbb37565483d4e6017fc09904ded36abcae1d08a0cd843**.

## Fresh Qualification

All **28 final tests pass in 158.460s**, no skips. This includes ten new
target/native/installed tests and all eighteen previous loader tests, freshly
rerun against exact predecessor fixtures through the new successor gate.

- **436 three-way guest cases** compare original, raw C and guarded emission
  with an independent ordered reference. Every one of the 105 words is
  visited in each form. Preserve SP, saved GPRs, all FPRs, input bytes and
  surrounding output canaries.
- **218 native32 cases each at O2 and O0 with UBSan**, separate actual body
  and SDK-typed caller units, no fwrapv. Verify the prefix offsets, all input
  object/pointer/padding bytes, other output cells and surrounding canaries.
  Include unsigned enable high bits, count bytes 128/255 with disabled
  records and full tail counts **32768/65535** in explicitly bounded arenas.
- **Eight effective native controls** all exit 21 for functional mismatches:
  rejecting negative overrides, unsigned preferred fields, marking an update
  on presence alone, unconditional fallback, byte-only enable flags, unsigned
  tails, byte-truncated tail counts and wrong tail stride. All compile and
  run; no compiler failure, signal or sanitizer trap counts as a control.
- **Six guest alias cases**, including output-overlapping primary, enable,
  tail-count and value lanes, plus a synthetic negative slot whose initial
  output clear zeroes its count byte. Zero-count, disabled-record and empty-
  tail cases use missing pointer entries to prove their dereference gates.
- **156 fired original/guarded memory-fault prefixes** preserve literal
  memory, GPR/FPR, PC, branch-delay, access and event state. Raw C is qualified
  for public behavior, not identical private registers or fault prefixes.
- **Three independent original/guarded rebases** compare all 105 words,
  including HI16/LO16 carry boundaries. All raw/original word, binding, pool
  and **528 guard-field corruptions** fail closed.
- Verify all **473 original caller words** of func_1501D348 against ROM
  **0x4A7F8..0x4AF5C**. **216 three-way real call cuts** execute its JAL at
  **0x1501D9C4**, passing S5 to A0 in the delay slot, then the real next JAL
  to func_15022BA4 and its same S5 argument delay slot. Preserve S5/SP and
  the correct RA. The next provider is opaque and clobbers caller-saved
  registers; no return value from the maximum scan is interpreted.

Guest mixed-width aliases are not native mixed-endian C alias claims.
High byte counts, large tails and the negative alias slot are explicit
synthetic domains, not natural gameplay acceptance. The full caller flow,
next provider's semantics, host port and full gameplay remain unvalidated.
Zero new Claude calls and no dependency/configuration changes.

## First Whole Image Prediction

Reproduce the predecessor independently, then predict every **3,257,636 ELF
bytes before installation**. The normal rebuild equals that first prediction.
Exactly **371 bytes** change:

- **318 code bytes**, entirely inside this routine's 420-byte slot.
- **Two size bytes**, changing its function extent from **12 to 420**.
- **51 metadata bytes** in one exact symbol/string ordering group:
  D_800C35D0, .L15099274_game_data and D_800A8D98 change order to the second,
  third, first entries. All three named definitions remain identical.

All other image bytes and canonical definitions are unchanged. No metadata
exclusions or address-drift allowances. Preserve the entire previous guard
prefix, append exactly 48 target rows and retain its CRLF bytes. All **136
live inputs** pass, including all **133 unchanged inputs**. Protect
**189,088 data bytes / 720 owners / zero differences**.

First predicted and normally rebuilt ELF SHA-256:
**15a46ab59454790f0c2685d986f38d7ee5193ebc4d4dc7b9b987c439a15e6245**.
Installed source owner:
**acf2dfaa4a818c738e557f33015211331bfc9b7a497a7771ec8c443b63e5e9c0**.
Installed guard manifest:
**9c2663db21c4bc173b12fe41b5d6d17346d7d5edd785531232fbb2c8babb8572**.

Unknown successors and corrupt before/after fixtures are rejected. The prior
loader's research and installed checks retain their original exact inputs;
the new checkpoint does not accept arbitrary live successors. Existing
Makefile/compiler warnings remain; this is not a warning-free build claim.

## Progress And Bank

Fresh official matching: Game **2,938/4,828 (60.85%)**, total **3,611/5,501
(65.64%)**, still different **1,890**, zero drift. Init stays **492/492** and
Debugger **181/181** exact among converted functions. Conversion remains
**5,501/6,044 functions / 86.04% bytes**; the old stub already counted as C,
and the regenerated conversion CSV is literally unchanged. Root README
changes only its two aggregate matching rows.

Tools **199b23f** banks eleven files before the consumer pin. Synchronize
only the nine new target files and two exact prior-loader checkpoint/test
updates to the older tools mirror. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **937 other initial dirty-file
hashes**, and its independently dirty history; **948** final dirty paths.
All eleven file pairs are identical. Across both copies, **22 Windows
ASCII/AST checks** and all eleven WSL padder tests per copy pass: active
**0.033s + 0.022s**, mirror **0.028s + 0.018s**. Consumer tools-check passes.
No mirror commit/reset, push, host-port or frozen Release action.

Reproduction in the prepared checkout:

```sh
python3 -m tools.experiments.game_record_maximum_installation
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_record_maximum_match \
  tools.tests.test_game_record_maximum_native \
  tools.tests.test_game_record_maximum_installed \
  tools.tests.test_game_microcode_loader_lifetimes \
  tools.tests.test_game_microcode_loader_native \
  tools.tests.test_game_microcode_loader_startup_caller \
  tools.tests.test_game_microcode_loader \
  tools.tests.test_game_microcode_loader_installed -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Recover signed override/preferred/fallback semantics and the actual void(s32) interface.
- [x] Qualify only temporary/schedule guards, original emission, native/guest behavior, caller cuts, rebases and fault prefixes.
- [x] Freeze the entire independent first image/source/guard prediction before installation.
- [x] Complete normal rebuild, all 28 final tests, exact successor/fixture corruption gates and protected-data audit.
- [x] Measure official progress, update README aggregate rows only, preserve both tools copies and bank tools first.

Next: **func_1501D044**, still a zero-return stub in the same owner:
**100 words / 400 bytes**, frame **0x18**, VA **0x1501D044..0x1501D1D4**,
ROM **0x4A4F4..0x4A684**. Recover its per-slot/global state reset and
func_150233BC call, including signed sentinels, floating constants and
post-call stores, while preserving the newly installed scan and loader.
Timing's **141 differences**, wider Game/additional-source recovery and
full gameplay acceptance remain separately open.
