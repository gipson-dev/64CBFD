# Owner setup dispatcher direct recovery and byte match - 2026-11-16

`void func_151A3390(u8 *owner, u8 channel)` replaces its zero-return stub
with the complete descriptor/preset/sound/vector-effect routine. All **93
words / frame 0x98** emit directly from C: **zero guards, insertions or
omissions**. VA `0x151A3390..0x151A3504`, ROM `0x1D0840..0x1D09B4`.

Production: **4,521 / 5,514 (81.99%)** exact C functions; Game **3,848 /
4,841 (79.49%)**, Init **492 / 492**, Debugger **181 / 181**. Zero address
drift, 993 different; **166** more to the active 85% goal. Conversion stays
5,514 / 6,048 (91.17%), 86.19% of bytes.

## Recovered interface and behavior

The routine builds the original partial **48-byte descriptor** at incoming
SP-48, passing it to `u8 *func_151A3504(void *, u8)`. It captures owner+0x3B,
sets the owner link and attachment, zero vector, original scalar/short/byte
presets and the two `D_800A8D50/54` values. Unknown meanings retain offset
names. Five reserved bytes at 0x06/0x07, 0x1E/0x1F and 0x2F stay untouched.

It submits `func_151A4590` and `func_151A499C` for the same owner/channel,
calls `func_10010154(0x1AA, owner, 0x55F0, 1000, 4000)`, then submits the
zero vector at incoming SP-60 through the original 16-argument
`func_15160A58(owner, 1, vector, 2, 300, 80, 255, 255, 117, 255, 0, -1,
0, 0, channel, 1)`. Signed tag, narrow flags/priority and unused arguments
follow the existing provider definition in `game_18D770.c`; the audio ABI
follows its definition and `functions.h`. All five providers are already
converted and byte-exact in the current ELF and are frozen as ABI inputs.

The owner is an ordinary mapped input; no new null guard is added. Three
original direct callers ignore V0. The generic caller at `0x150272C8` has
a null-owner gate and loads A1 from a byte; the two bounded nonnull paths
at `0x1506D314` and `0x1507435C` supply 0xFF. The source uses `void` and a
byte channel. A separate return-use audit proves V0 is overwritten before
any read on all three original continuations, including both paths of the
second caller's forward branch. IDO requires the exact existing `u8 * volatile` qualifier in
the forward declaration for `func_151A4590`; no shared declaration changes.

## Fresh qualification

Raw object SHA256:
`120d894aa5167c19938303605bd695cb012345da3d6e4d826561fc226b11b2db`.
All 93 words and nine bindings equal an independently assembled original
reference. Literal transition identity at equal PCs proves identical machine
steps, FP/FCSR and fault prefixes for the compiled streams. This does not
claim portable C fault or indeterminate-padding semantics.

All five maintained tests pass freshly in primary, isolated sibling-tools
and installed production at identical task-file hashes:

- Both complete owner padders retain all 22 neighbors/pools and the direct
  target. All 93 raw-word and nine binding corruptions fail; two stale CSV
  cases fail. Three independent GNU links verify symbol rebases and HI/LO
  carries. The production guard CSV remains byte-for-byte unchanged.
- An independent ordered model checks **1,536 cases per retail/raw/padded
  stream**, all 93 instructions, all descriptor bytes, five call order,
  every final argument, public effects and complete frame/register equality.
  Seeded F20/F21 survive all providers. Guest-only owner/descriptor aliases
  and incoming channel-home mutations exercise the actual repeated reloads.
- Actual native32 C passes **1,024 cases each at O0/O2 with UB traps**,
  observing 43 defined descriptor bytes. Six errors exit 3: wrong identity,
  descriptor byte, audio distance, vector, provider order and final priority.
  Retained-packet mutation skips padding; native inputs include signed zero,
  infinities, quiet and signaling NaN bit patterns without arithmetic.
- The identity fixture accepts independent T0/T1 allocation and rejects
  wrong identity, priority slot, saved F20 pair, audio distance and provider
  order through semantic observations, without relying on the source hash.
- **384 cases per stream** connect the full target to all three actual
  original caller windows (9/5/5 words), including the null branch. Windows
  outside these bounds are not qualified. The first caller window is still
  unmatched in production; the other two equal retail. All three current
  production windows are independently verified unchanged from the freeze.

Pre-freeze fixture failures remain in `fixture-screen*` and receive no credit.
The saved-FPR cache was synchronized with explicit F20/F21 seeds, and caller
scope was corrected to distinguish retail windows from an unmatched parent.
A diagnostic located a native fixture failure before invocation: returning
a signaling NaN through the helper's x87 ABI quieted it. Character-access
seeding now preserves all source bit patterns; fresh frozen suites use this
corrected fixture, without changing or weakening any historical snapshot.

## Production and retained evidence

The **1,281-input** baseline begins at consumer `d4c78eb0` / tools `4a376df`.
Exactly source, owner object and ELF change; **1,278 inputs stay unchanged**.
Actual five-command Make shadow agrees with all 23 raw owner functions.
Production rebuilds through Make, without copying a prebuilt object.

The complete ELF equals the independent prediction: **315
changed bytes / zero exclusions**, with 1 explicit symbol/string
permutations. All 20,289 named definitions agree except target size 12->372.
Symbol-value/name, protected-byte and target-word corruptions fail. Every
other 6,050 linked body and address remains unchanged; one of 698 objects
changes, preserving 22 owner neighbors and pools. All **189,088 protected
bytes / 720 owners** remain exact, SHA256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production ELF SHA256: `76ffca2b60eb75b88e844689efd0bf86ab4cb6f1928ef2889b8c4a38695bc7fb`.

Reproduce prepared target gates with
`python3 -m unittest tools.tests.test_game_owner_setup_151a3390_recovery -v`.
Receipts: `conker/build/game-next-151a3390-private/adoption/`.
Sibling dirty state and scoped dependency hashes are preserved; no sibling
source is overwritten. Required progress/project-tool checks pass. No Claude
call, host build, Release/save change or push. Root README gets aggregate
rows only. Graphify uses retained-ID scoped updates rather than claiming a
full-corpus rebuild. Commit tools before consumer source/pin/docs. Next:
`func_151A361C`; the wider 85% goal remains active.
