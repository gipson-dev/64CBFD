# Ring record updater direct recovery and byte match - 2026-11-16

`s32 func_151A361C(u8 *owner)` replaces its zero-return placeholder with
the complete ring-record update routine. All **105 words / frame 0** emit
directly from C: **zero guards, insertions or omissions**. VA
`0x151A361C..0x151A37C0`, ROM `0x1D0ACC..0x1D0C70`.

Production: **4,522 / 5,514 (82.01%)** exact C functions; Game **3,849 /
4,841 (79.51%)**, Init **492 / 492**, Debugger **181 / 181**. Zero address
drift, 992 different; **165** more to the active 85% goal. Conversion stays
5,514 / 6,048 (91.17%), 86.19% of bytes.

## Recovered interface and behavior

The owner holds an unsigned capacity byte at +0x25, signed count/head/tail
bytes at +0x2C/+0x2D/+0x2E, record storage at +0x94 and state at +0x98.
The local 24-byte record type names its three-component position, float
value, signed lifetime and delay, and mark byte. Reserved bytes retain
their offset names and stay untouched. State has a signed lifetime scale
at +0x1C, float rate at +0x24, signed byte phase step at +0x2A, flags at
+0x30 and wrapping byte phase at +0x4C. No shared header changes.

The count/flag gate returns zero before any mutation. Other paths advance
the phase, walk backward through live records, decrement either delay or
scaled lifetime, mark each record, and add the scaled float increment.
An expired lifetime clears state flag bit 1 and advances the ring head,
decrementing the signed count with byte-store wrapping. The final output
is the head record's position when the count is positive, otherwise zeros.
Successful updates return one. The C retains the original repeated reads
and uses unsigned 32-bit arithmetic for tick multiplication/subtraction so
extreme signed tick inputs do not introduce signed-overflow UB.

`D_800BE9E4` supplies signed ticks and `D_800BE9A4` the float timestep.
Both are existing absolute runtime symbols, without static ELF-backed
values. Their addresses and bindings are frozen; no invented constants.

The callback is the aligned pointer at `D_8008A200[6]`, VA `0x8008A218`,
ROM `0x22ECD8`. The original parent `func_15147740` selects it through
owner+0x2F and calls at `0x151477C4`. Zero requests release; one retains
the owner. The parent can instead expire its own signed timer before the
callback. The bounded fixture disables unrelated optional callbacks and
models `func_1516972C` as an opaque release marker and caller clobber.
It does not qualify allocator internals or complete gameplay behavior.

## Fresh qualification

Raw object SHA256:
`902f1550149825a4adc9b47c91cdabf07fb2382623b7bc76b4d83fb5792ebaa8`.
All 105 words and four bindings agree with the independently assembled
original reference. Literal transition identity at identical PCs covers
machine steps, FCSR and guest fault prefixes. The original unreachable
load at +0xAC and zero transfer at +0x188 remain present: 103 instructions
are reachable, while all 105 static words match. No stack frame or calls.

All five maintained tests pass freshly in the primary tools, isolated
sibling-tools overlay and installed production at identical task hashes:

- Both owner padders retain the direct target and all 22 neighbors/pools.
  All 105 word and four binding corruptions fail; two stale CSV controls
  fail. Three independent GNU links verify rebases and HI/LO carries.
  The production guard CSV remains byte-for-byte unchanged.
- An independent ordered model checks **2,752 cases per retail/raw/padded
  stream**, all 103 reachable instructions, complete memory and register
  state. Cases include all signed count bytes, flags, wrapping head/tail,
  delay/lifetime boundaries, extreme ticks and scales, and two intentional
  owner/state/record alias families. The full seeded guest stack survives.
- Actual native32 C passes **1,024 cases each at O0/O2 with UB traps**,
  comparing complete initialized owner, state and record storage. Native
  inputs use valid disjoint objects and finite float operands. All eight
  deliberate errors exit 3: count gate, flag gate, phase direction, delay
  boundary, expiry boundary, count decrement, float rate and output source.
- Whole-word identity includes the two unreachable words. Four independent
  semantic controls reject early count gating, wrong mark, wrong cleared
  flag bit and a growth-operation mutation against the separate model.
- **384 cases per stream** connect the full target to the actual original
  100-word parent and selected callback/release routes, including parent
  expiry without invocation. The callback pointer and current production
  parent bytes are checked against the immutable baseline. Bounded routes
  do not establish full-parent coverage or opaque release semantics.

Pre-freeze fixture receipts in `fixture-screen/` are smoke evidence only.
The first acceptance launch preceded completion of the baseline-copy
process and failed on the missing fingerprints file before any test ran.
After that process exited successfully, the complete frozen suites ran.
All original snapshots and losing source candidates remain retained.

## Production and retained evidence

The **1,289-input** baseline begins at consumer `c1b18e80` / tools
`465deca7`. Exactly source, owner object and ELF change; **1,286 inputs
stay unchanged**. Actual Make shadow agrees with all 23 raw owner
functions. Production rebuilds through Make, without copying a prebuilt
object. The conversion/progress CSV and guard CSV do not change.

The complete ELF equals the independent prediction: **302
changed bytes / zero exclusions**, with 0 explicitly accounted symbol/string
permutations. All 20,289 named definitions agree except target size
12->420. Symbol-value/name, protected-byte and target-word corruptions fail.
Every other 6,050 linked body and every address remain unchanged; one of
698 objects changes, retaining all 22 owner neighbors and pools. All
**189,088 protected bytes / 720 owners** remain exact, SHA256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production ELF SHA256: `1d1bea744d892598a879dec2589b1ee951eb14fb052dde39916b2067573a10dd`.

Reproduce the prepared target gates with
`python3 -m unittest tools.tests.test_game_ring_update_151a361c_recovery -v`.
Receipts: `conker/build/game-next-151a361c-private/adoption/`.
The sibling's 2,434 dirty paths and 299 scoped dependency files are preserved
through an isolated overlay. Actual import origins remain recorded: the
sibling run uses the new overlay modules, existing sibling helpers and
explicitly fingerprinted primary fallbacks. Required progress and
project-tools checks pass.
No Claude call, host build, Release/save change or push. Root README gets
aggregate rows only. The normal Graphify update fails closed on its smaller
scan corpus and retains the curated graph. An eight-file scoped AST update
retains all 63,356 previous IDs and adds the recovered function relationship;
this is not a full-corpus re-extraction claim. Commit tools before consumer
source/pin/docs. Next: `func_151A37C0`; the wider 85% goal remains active.
