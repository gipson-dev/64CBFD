# Game clock hands and chime guarded match

Date: 2026-11-14. `void func_1510AA44(u8 *state)` replaces the last
zero-return placeholder in `generated_137ED0`. All **229 words** match retail
with **ten checked guards**, no insertions/omissions. Its original **0x40
frame**, RA at SP+0x1C, hour-angle home at SP+0x24, minute home at SP+0x38
and incoming state-pointer home at SP+0x40 are retained. The owner is now
**4 / 4 byte-exact**, following the projection recovery in
[Note 2453](2453-game-projection-bounds-guarded-match-20261114.md).

The production recount is **4,495 / 5,515 (81.50%)** total, **3,822 / 4,842
(78.93%)** Game, zero address drift and **1,020** different. Init remains
**492 / 492**, Debugger **181 / 181**. **193 more matches** reach the active
85% total goal. Converted counts/bytes remain **5,515 / 6,048 (91.19%) /
86.17%**. Root README receives aggregate rows only.

## Recovered behavior and source fit

Source `conker/src/game/generated_137ED0.c`, original assembly
`conker/asm/137ED0.s`. VA **0x1510AA44..0x1510ADD8**, ROM
**0x137EF4..0x138288**, **916 bytes**. Baseline consumer `e57a797f`, tools
`4992782c21befe37073c751fe7874c39af9a49ee`. Ignored artifacts are in
`conker/build/game-clock-update-1510aa44-screen/`.

The routine advances the signed tick accumulator at state+0x3C, initializes
it once from nonzero `D_800BE3E4`, handles its 2,592,000-tick cycle, and
updates the two clock hands and their fixed scale fields. It detects
quarter-hour transitions, sets the pending chime count, and submits at most
one pending chime when the computed second changes. It does not loop to
replay every skipped second. Hour-boundary zero maps to twelve chimes;
other quarter boundaries select one. The sound packet is
`func_15114D24(state, 0x4CC, 32767, 200, 1000, 12)`.

The initialization multiplication explicitly wraps in unsigned 32 bits
before remainder by **43,200**. The tick addition and pending-count decrement
also preserve 32-bit wrapping; signed division/remainders retain truncation
toward zero and the two negative-minute corrections. The final integer casts
use the prepared two's-complement o32/native32 implementation. No signed
overflow is needed in the tested C operations.

Reading the actual clock field, rather than carrying a redundant local clock
snapshot, restores retail's value lifetimes. Declaration order
`previousMinute, minute, second` recovers the original private homes without
dummy locals, volatile qualifiers or frame guards. The complete raw function
has **229 words / 0x40 frame / five binding sites**, SHA-256
`f826860b370a8b49ad9989c89cf76c646e34b7af6c716529066bc1ba92ff1e6c`.
All three neighboring raw functions and owner pools remain unchanged.

The ten real word differences are one commutative equality-operand swap at
+0x2B8 and nine words affected by a closed six-register caller-FPR cycle
in the tail starting at +0x300. The guard derivation changes no operation,
literal, branch edge/mode, memory offset, stack home, binding or call packet.
Its independent proof verifies every other instruction bit and all **three
tail paths**, including opaque caller-FPR clobbers. Each renamed value is
defined before use; no incoming renamed FPR value is read. Two proof controls
reject a changed store offset and branch mode. **234 corruption controls**
reject 229 changed raw words and five changed bindings. Normalization reads
no retail ROM bytes.

## Qualification and caller evidence

- [x] **2,563 guest cases / three streams**, using an independent signed
  arithmetic/state model, compare complete public memory, six-word chime
  packets and all **272 record bytes at each helper entry**. Negative and
  extreme signed accumulators, unsigned initialization wrap, minute/quarter/
  cycle boundaries, stalled seconds and full-word pending counts are covered.
- [x] **128 guest-only cases** include record/global overlap and all sixteen
  combinations of provider mutations. The provider can change record/global
  values, redirect the saved incoming state pointer, or overwrite the actual
  private angle/minute homes. Final stores must use the correct restored
  pointer and homes. These are emitted guest storage tests, not a portable
  native private-memory contract.
- [x] **193 / 229 words** are visited; fixed-divisor error paths remain
  original and unexecuted. Four effective emitted controls reject the
  initialized marker, hour divisor, chime ID and minute scale. **119 memory
  access prefixes** compare complete retail/normalized memory, registers,
  condition, PC, trace and branch-delay ownership. Precise raw scheduling
  fault order and hardware/FCSR behavior are not claimed.
- [x] **2,435 native32 cases at each O0/O2/O3**, with undefined-behavior
  traps, compare all 272 record bytes, both globals, call count, complete
  sound arguments and the full record snapshot before helper effects. Seven
  effective C controls cover initialization remainder/multiplier, cycle
  comparison, quarter calculation, sound ID, decrement direction and scale.
  Native provider effects modify ordinary record/globals only.
- [x] Original registry **D_80088C90 row 46**, stride twelve, contains
  `(func_1510AA44, 0, 0)` at ROM **0x22D978** / VA **0x80088EB8**.
  All **22 original installer words** execute and transport the actual
  callback into state+0x38. Aligned input scans find no direct J/JAL and
  exactly this one literal pointer; computed/external calls remain possible.
- [x] Both original bounded parent windows, **13 words at 0x15113ED4** and
  **30 at 0x15113F94**, pass **144 cases / three streams**, with gate and
  second-iteration behavior. Four return-register poison values give the
  same complete continuation state within each stream, proving those callers
  ignore the callback result. The recovered void interface follows that
  observed use; original source declarations/full parent gameplay are not
  recovered by these windows.
- [x] Both complete-owner padders, four code/data rebases and **12 GNU links**
  preserve all four owner functions and their binding behavior.
- [x] Mounted pre-install suite passes in **45.567 s**, isolated sibling
  suite in **64.444 s**. The final comment clarification is separately
  recompiled in the mounted and sibling overlay copies: identical raw hash,
  bindings and guards. All seven final overlay task files are byte-identical
  to the mounted files. The installed mounted suite passes in **26.431 s**; fresh
  `make tools-check` passes.

The early fixture's generic `mode` attribute was overwritten by its inherited
machine constructor, so the clock uses its own `clock_mode`. Negative-control
offsets now assert the exact original word before mutation. Bounded parent
windows intentionally advance saved loop registers, so their checks preserve
SP/callee-saved FPRs and compare complete outcomes across return poisons;
they do not assert unchanged parent loop counters. These fixture corrections
precede the successful receipts above.

Reproduce on the prepared consumer:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_clock_update_1510aa44_match -v
make tools-check
```

## Production audit and next target

All **810 frozen inputs** pass the pre-install gate. Independent actual-Make
owner commands and the production Make agree. The complete ELF is exactly
the prediction: **642 changed bytes**, covering the target body/size and one
closed metadata permutation of `D_800BE3E4`, `D_80099640`, `D_80099290`.
All named definitions retain their values and extents apart from the declared
target size; no metadata sections or other bytes are excluded.

All **6,051 function addresses**, **189,088 protected bytes / 720 owners**,
conversion rows, **82 headers** and three neighbors are fixed. Only the
intended object changes among **698**; its changed sections are `.text`,
`.rel.text`, `.strtab`, `.symtab`. **806 immutable inputs** remain exact.
The CSV preserves its entire prior byte prefix and adds only ten target
rows, with no insertions/omissions. The existing duplicate `generated_12D630`
Make recipe warning remains unrelated.

Production ELF SHA-256:
`0619dc2bfb3ed16c4fb1e520115f9742323fcd2f16460caf5fcde396ca96d7ad`.
Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Sibling HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, its **2,439 dirty
paths** and status SHA-256
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`
are preserved. No sibling files are overwritten.

Scoped Graphify AST merge covers eight files, retaining all **61,058 old
IDs**, zero lost nodes: **61,097 nodes / 114,813 links**, zero LLM tokens.
This is not full-corpus re-extraction. Routine Claude calls: zero. Tools
commit `ad71ba49ede0c0a8f11085b8ba37b743cf620cb9` precedes the consumer pin/source/documentation
commit. No push; the host Release checkpoint remains frozen.

Next: **84-word `func_15016850`**, owner `generated_43D00`, a record resource
cache builder. Preserve its handle initialized once at SP+0x50: an ID at or
above 0xBB skips the loader and can reuse that live handle. Qualify helper
changes to the live count/table and deduplication before matching. The shorter
53-word `func_150A613C` has an implicit T4/F20..F31 input contract and S2
output; the nominal 55-word `func_150AE280` branches into an earlier routine.
Neither is an ordinary standalone C target based on word count alone.
The common particle updater remains private and uncredited at
[Note 2452](2452-game-common-particle-frame-native-and-callers-20261114.md);
retain its old frozen baseline when preparing any future adoption.
