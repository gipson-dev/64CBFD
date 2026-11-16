# Linked ring emitter full recovery and guarded byte match - 2026-11-16

`s32 func_151A37C0(u8 *owner)` replaces its zero-return placeholder with the
complete linked-owner movement sampler and ring emitter. Semantic C emits
266 words / frame 0x120. **48 relocation-aware guard rows**, including one
omitted duplicate return assignment and **no insertions**, restore the complete
**265-word** original slot. VA 151A37C0..151A3BE4, ROM 1D0C70..1D1094.
This is a guarded C match, with the raw semantic transfer independently checked.

Production total **4,523 / 5,514 (82.03%)**, Game **3,850 / 4,841 (79.53%)**,
Init 492/492, Debugger 181/181; zero drift, 991 different, **164** further matches
to the active 85% goal. Conversion stays 5,514/6,048 (91.17%), 86.19% of bytes.
The earlier [setup screen](2500-game-linked-ring-emitter-recovery-and-ordered-setup-screen-20261116.md)
remains historical bounded evidence, with its old draft and freeze untouched.

## Source and provider ordering

The routine caches the payload pointer at owner+0x98 and record storage
pointer at owner+0x94. The local payload type
names its linked owner, identity, attachment, scale, lifetime/delay, value/rate,
phase bytes, position, pending progress and elapsed time. The 24-byte sample
names position, value, lifetime, delay, mark and phase. Unknown bytes retain
reserved offset names. The snapshot uses the existing 48-byte descriptor.
There are no shared header, Makefile or compiler-profile changes.

An absent live linked owner or identity mismatch returns 0. Initialization
queries its position and sets owner flag 4. Later query failure calls cleanup,
copies all 48 payload bytes into private storage, calls
`func_151491F4(300,-1,10,0,5,48, owner[0xC],0)`, and copies the snapshot to
a successful factory result+0x28. Factory mutations cannot change that snapshot.
The function returns 1 even if allocation fails.

Movement above the protected epsilon accumulates scaled distance. Pending
progress above 1 emits records, interpolates position/value/time and maintains
signed-byte head/tail/count with wrapping byte stores. The entry pointer is
latched before RNG, while phase/base/range are read after it. The RNG result
is assigned in a separate statement, then reduced modulo(range + 1), proven
1..256. The inline expression was rejected: GCC can read its divisor before
the call, and a provider-mutation case produced phase 0 where 248 was required.
The explicit order passes both IDO instruction and native C checks.

`D_800A8D58` is protected 0x38D1B717/0.0001f. `D_800BE9A4` is an absolute
runtime timestep symbol without an invented static value. The callback is
`D_8008A23C[6]`, VA 8008A254 / ROM 22ED14. Original 100-word parent `func_15147740`
calls its second table at 15147820; zero releases and one retains.

## Fresh qualification and limits

Five maintained tests pass in primary tools, isolated sibling overlay and
installed production at identical eight-file fingerprints. Raw SHA256:
`b8ae6eb6f52c8c383c4023df49bdf4880ac214f723d09655f13ef740c1266852`.

- Symbolic transfer checks entry 6 paths, retirement 2, setup 8, emission 6, tail 2,
  finish 1, epilogue 1. It compares ordered FP operands/operations/FCSR, public
  writes/calls, reads between writes, all 48 snapshot bytes, saved GPR/FPR lifetime,
  private frame state and loop live values across opaque o32 provider clobbers
  and public mutations. Seventeen semantic corruptions reject; independent
  temporary-register renaming passes.
- Independent guest model: **1,828 cases per retail/raw/guarded stream**, plus
  **103** cases executing the actual 26-word query, 12-word cleanup and 11-word
  memcpy. Cases cover gates, boundaries, all count/range/phase bytes, provider
  mutations, two guest alias families, NaNs and signed zero. Reachable target
  coverage is 262 retail / 263 raw / 262 guarded instructions.
- Actual native32 C: **768 cases each at O0/O2**, UB traps, complete initialized
  public objects and 48-byte snapshots. Twelve semantic controls exit 3, including
  the inline-RNG ordering regression. The first position-Y negative failed to
  compile because its deliberate error left an unused variable; this failed
  receipt is retained with no rejection credit. The replacement consumes that
  value, compiles cleanly and fails on incorrect output as intended.
- **618 original-parent cases per stream** include expiry without invocation,
  zero/release and one/retain, with opaque and connected providers. Raw agrees
  on public state, ABI and ordered FP; guarded/retail agree on complete machine
  state. Unrelated callbacks are disabled. Release, factory, RNG and the deeper
  position service remain bounded opaque providers; this is not full gameplay.
- Both actual whole-owner padders retain 22 neighbors and pools. All 266 raw-word
  and 11 binding corruptions reject, as do two stale actual CSV controls. Three
  independent GNU links verify rebased bindings and HI/LO carries. Existing guard
  bytes remain an exact prefix; only the 48 target rows append.

The symbolic domain is ordinary mapped/aligned public memory, immutable epsilon
and private disjoint stack. Reads commute only between public writes. FP traps
are not assumed disabled. Native cases use finite inputs and valid disjoint
typed objects. Raw C is not claimed equivalent for arbitrary fault prefixes or
all C aliasing. Guarded literal identity separately restores the retail machine.

## Actual production and evidence

The **1,301-input** immutable baseline starts consumer `d6b2336d` / tools `281455e0`;
all 1,293 earlier screen inputs were unchanged before its creation. Exactly source,
guard CSV, owner object and ELF change; **1,297 inputs stay unchanged**.
Actual Make shadow matches all 23 raw owner functions and both padding paths.
Production rebuilds source through Make; no prebuilt object is installed.

The whole ELF equals its independent prediction: **794
changed bytes / zero exclusions**, with one accounted symbol/string
permutation. All 20,289 named definitions agree except target size 12 -> 1060.
Effective symbol-value/name, protected-byte and target-word controls reject.
All other 6,050 bodies and every address stay unchanged. One of 698 objects
changes, retaining 22 neighbors/pools. Conversion/progress CSV is unchanged.
All **189,088 protected bytes / 720 owners** remain exact, SHA256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`. Production ELF SHA256:
`c6c92624f3d0097acadffae64a6d2e40114a33a25b5ba5dc209811ba2dc73e79`.

Reproduce prepared qualification:
`python3 -m unittest tools.tests.test_game_ring_emitter_151a37c0_recovery -v`.
Receipts: `conker/build/game-next-151a37c0-private/adoption/`.
The sibling's 2,434 dirty paths and 301 scoped dependency files stay unchanged
through an isolated overlay; actual import origins are recorded. Scoped graph
refresh retains old IDs; it is not full-corpus extraction. Zero Claude calls.
No host build, Release/save change, dependency upgrade or push. Commit tools before
consumer source/guard/pin/docs. Next inspect `func_151A3BE4`; keep 85% active.
