# Keyed Resource Record Lookup Match - 2026-11-08

`func_150234A4` now matches all **78 words /312 bytes**, frame **0x28**,
using recovered semantic C and **13 checked register/scheduling guards**.
All private homes, saved RA, memory operations, branch destinations and delay
slots retain their retail roles. No instruction is inserted or omitted.

Production: Total **4,265 /5,513 (77.36%)**, Game **3,592 /4,840 (74.21%)**,
Init **492 /492**, Debugger **181 /181**, zero address drift. There are
**1,248** different converted functions and **146** more exact functions
needed for4,411 /5,513 and the active80% goal. The conversion CSV/denominators
are unchanged.

## Interface and record selection

Owner `conker/src/game/generated_49D30.c`, original `asm/49D30.s`.
VA **0x150234A4..0x150235DC**, ROM **0x50954..0x50A8C**.

```c
struct163 *func_150234A4(u32 key, s32 reset);
```

Reuse the existing56-byte `struct163`: signed16 key+0, flag byte+0x0C,
backing pointer+0x34. Three entries run from D_800C3CA0 to D_800C3D48.
Increment the input as a wrapping32-bit key, then compare against each
sign-extended16-bit stored key. The explicit `(u32)(s32)` comparison preserves
the LH/word equality boundary without signed C increment overflow.

- A matching key returns that entry unless reset is nonzero and its flag
  byte is nonzero. That busy-match path deliberately resets and selects the
  FIRST entry, even if the match occurred later in the table.
- An empty entry selects the current entry. A nonzero reset and flag invoke
  `func_15023440(current, 1)` before claiming it.
- A completely occupied nonmatching table unconditionally resets/selects the
  first entry, independently of the reset argument.
- Existing matches return without changing the key. Newly selected entries
  receive the captured low16 key after reset. Helper mutations are observed
  at their original read/reload boundaries.

The reset helper is the existing direct25-word recovery from [Note329](329-game-resource-entry-reset-match-20260927.md).
It releases backing through func_1516D2E0, clears its pointer and clears the
leading halfword for this mode. Shared structure definitions and callers
are unchanged; the old zero-return placeholder becomes the pointer routine.

## Compiler recovery and closed normalization

The first structured source has80 words and the correct frame. Naming the
loop-end pointer removes the two extra end-address reloads. Ordering local
declarations recovers cursor homeSP+0x18, selectedSP+0x1C, existingSP+0x20;
the adjusted key remains in the incoming homeSP+0x28. Initializing the cursor
after the wrapping increment gives the accepted78-word body. Explicit sign
extension emits identical words. All bounded source screens remain ignored
diagnostics; the best accepted source has13 word differences.

Normalization derives only three closed GPR regions and an independent
opening permutation. Four changed opening positions require **six adjacent
independent swaps**; every crossing is checked for register dependencies.
The short matching-address, empty-flag and final-bound/fallback-address
regions preserve all live inputs/outputs and conditional branch values.
There is no stack-home, frame, memory-order, branch-target or opcode repair.
Effective controls reject a live-register collision and a dependent crossing.
Raw scratch/fault-state identity is not claimed; normalized/original identity
is checked literally. The initial suite expected four swaps incorrectly;
the certificate derives six, and the corrected final suite passes unchanged
candidate/normalization bytes.

The existing Make profile stays **O2/g3/MIPS2/O32 with -Wo,-loopunroll,0**.
Reuse the existing no-unroll compiler helper, filtering that option from the
assembly prepass while passing it to IDO. Actual Make's three commands compile,
pad and assemble the identical owner. Both padders preserve all **57 functions
/56 neighbors**, pools and the exact register-mask union. No exported interior
labels move. Complete-owner and isolated bytes/bindings agree; diagnostics0.

## Execution, callers and effective controls

Six focused checks pass before/after installation in both tools copies,
sequentially with exact source/dependency fingerprints:

- **3,986 guest cases** cover occupied/empty/matching slots, all256 flag-byte
  values, wrapping32-bit inputs, signed16 comparisons, zero/high-bit reset,
  helper mutations and three code/data/helper layouts.
- **24 private-frame alias cases** and **41 interrupted-access cuts** qualify
  emitted memory/register behavior. Incoming-key or selected-home mutation is
  a guest-only synthetic probe, not portable C behavior. All77 reachable words
  execute; the unreachable duplicate increment at+0xCC remains preserved.
- **88,000 native32 cases per O0/O2/O3 profile**, trapping UBSan, use typed
  records, exact field offsets, backed end-marker adjacency and complete table
  canaries. All **12 semantic controls** are effective, including wrong key
  width/sign, reset target/mode, empty test, missing reset/store and return.
- Three independent GNU links and12 rebased executions qualify all13 binding
  sites, including low-half carry layouts. The table-end relation remains
  base+168 under rebasing. All78 word,13 binding,72 register-metadata and four
  entire-image corruption controls reject changes.

The original25-word reset helper runs connected in **72 cases**, with a
bounded release provider. Independent public effects agree; normalized and
original helper-private states also agree literally.

The pristine aligned census finds one direct call at ROM **0x51BEC /VA0x1502473C**
in **func_1502460C**, no aligned pointers and no interior entries. Its original
13-word window **0x15024720..0x15024754** derives reset from the descriptor's
signed byte+4, passes the saved word key in the JAL delay slot, copies V0 to
S0 and tests the pointer for null. **180 connected caller cases** cover both
reset outcomes and the pointer/null branch (synthetic selected-home mutation
can produce null). The full8128-byte caller and resource-release implementation
are not newly qualified. No hardware/gameplay acceptance is claimed.

## Literal image, production and preservation

The independent predictor replaces only the312-byte target body and its
12-to312-byte symbol extent: **227 changed bytes, zero exclusions, no metadata
permutations**. All **6,052** disassembled entries keep their addresses; all
other bodies/extents/metadata remain fixed. Protected data is exact across
**720 owners /189,088 bytes**, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production compiles only this owner and equals the entire predicted image.
The manifest preserves every old byte and appends exactly13 checked rows.
Makefile, data bindings and progress CSV stay unchanged. The pre-existing
full-ROM checksum mismatch (make all exit2) and duplicate generated_12D630
recipe warning remain separate from the successful compile/link/recount.

Shared smoke checks are fresh in both tools copies; three unchanged helper
regression checks per copy are reused by exact fingerprints. The sibling's
**2,434** dirty paths remain preserved. **104 frozen inputs** include the
original owner, caller, headers, layout, manifest, ROM and compiler inputs.
Baseline consumer `86a40af7b4464efe4352690de603173ec1a0e779`, tools
`d82bf06091141e53831199c179365184ed45ef36`. Claude calls: **0**; local source,
compiler, ABI, execution and literal-image evidence resolve this routine.

ELF SHA256: `a99eedc59042baca0a73176c212d7aad922006f61c75623822dedea46b1eef6a`.
Binary SHA256: `642c7b84ddad5431c23fe96c8c732853e12f2fe521f54b1014187b11a7c30826`.
Owner SHA256: `595930db56a17660e992f2d81e61fc379b983c3604acff7ddd83221ead0fd112`.
Guards SHA256: `9140ca7fb99506fc43c7be4e910d58eeee9f8bcc21f8743f314b59d7dd3875f8`.

## Resume boundary

Next: **func_150E41C0**, an uncredited78-word trigonometric three-coordinate
output builder in `conker/src/game/generated_111670.c`, original `asm/111670.s`.
VA150E41C0..150E42F8 /ROM111670..1117A8, frame0x40, savedF20 and RA.
Audit all callers and the actual owner profile before choosing its interface.

Snapshot/truncate actor float fields+0x2F8/+0x2FC/+0x300 through D_800DBFF0
before calls. Cache angle+0x398 in F20, call sinf then cosf, save500*sin and
-500*cos. Reload the actor global after those calls, cache angle+0x3A0, and
call sinf/cosf again. Preserve each original float operation and explicit0.0
addition/subtraction, then truncate and write three halfwords at D_800D99F0
offsets0,4,2. Do not merge arithmetic or hoist live actor/angle reloads. Qualify
finite native conversions separately from MIPS exceptional FP inputs/FCSR.
Complete normal ABI/owner/guest/native/image/production gates before credit.

Receipts: `conker/build/game-keyed-record-reuse-150234A4-match/`.
Tools are committed before the consumer pin. Graphify's scoped refresh retains
existing unscanned nodes with audit evidence; it is not full-corpus extraction.
Host Release stays frozen. The80% goal remains active.
