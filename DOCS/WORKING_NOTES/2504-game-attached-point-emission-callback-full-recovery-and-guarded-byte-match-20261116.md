# Attached-point emission callback recovery and guarded byte match - 2026-11-16

`void func_151A4A38(u8 *owner)` replaces the false zero-return placeholder with
the complete attached-actor update callback. **168 of 170 words emit directly
from C**; two expected-word guards preserve an independent angle-load / floating
constant schedule. The complete **170-word slot / frame 0xA8** is byte-exact.
There are **no insertions, omissions, dummy locals or register bindings**.
VA 151A4A38..151A4CE0, ROM 1D1EE8..1D2190. This is a guarded C match.

Production total **4,526 / 5,514 (82.08%)**, Game **3,853 / 4,841 (79.59%)**,
Init 492/492, Debugger 181/181; zero drift, 988 different, **161** more matches
to the active 85% goal. Conversion stays 5,514/6,048 (91.17%), 86.19% of bytes.

## Original interface and recovered behavior

The sole aligned pointer is `D_8008A4E8[5]`, VA 8008A4FC / ROM 22EFBC.
The complete original **45-word / frame 0x18** dispatcher `func_15149264`
passes owner in A0 and ignores the result. Its signed callback selector is +0x11;
the existing setup `func_151A499C` selects callback 5. The parent, both selected
table words, 98-word transform and 224-word emitter are literal retail bytes
in production. No caller, shared header, profile or Makefile change is needed.

The owner+0x28 payload stores actor, identity, rate, accumulator, matrix index
and local point. An actor type word of 0 or 8, or changed identity, retires the owner by
setting its signed lifetime to -1 and flag bit 0. Missing actor matrices and
low-nibble actor state 15 skip the update. Otherwise accumulator advances by
`rate * D_800BE9A4`; emission occurs only when it is greater than one.

Before transforming the point, the callback snapshots the actor's high angle
byte minus 64. It calls `func_15143134` with payload+0x14, the private output
point and `actor->matrix + (matrixIndex << 6)`. The post-helper accumulator is
reloaded, truncated through signed16 and subtracted as that narrowed value.
The saved angle remains the pre-helper angle even if the provider changes the
actor or owner link. Owner channel and context bytes are freshly read after
the two random calls.

The **108-byte descriptor** starts at incoming SP-124; transformed position is
at incoming SP-16 and the signed angle is at SP-126. Header/state constants,
the narrowed count, transformed position, angle bias -25, signed -44/50/50,
300/400 scalar fields, 1/15/0/-0.5 values and sentinels are recovered. Initial
flags 7 acquire independent 0x40 and 0x80 random bits. The final call is
`func_15153634(&packet,255,owner[0xC],owner[1])`.

**100 descriptor bytes are defined; eight stay indeterminate in C** (byte 5
and 0x65..0x6B). The actual consumer also reads the untouched word at +0x68.
The C object owns the complete extent; no field is invented or zero-filled.
Unknown field meanings retain offset-based names. Native checks never observe
or mutate the eight indeterminate bytes; guest and connected checks retain
their seeded retail stack values.

## Fitting and fresh semantic evidence

The first candidate emits 170 words but has a frame eight bytes too large.
Seven declaration-order screens retain that wrong frame. Removing an
unnecessary actor local and using the existing payload pointer recovers the
retail homes/frame and leaves six words. Typed semantic payload names preserve
the emitted object. Reordering two constant assignments reduces six to two.
Selected raw SHA256:
`7c48d7c5cb95e62daa343033f7c361dec6bd0c9bf9c374c52fe7d8a6ed607bbc`.

Only raw +0x1D0/+0x1D4 differ: `lh t9,0x2A(sp)` and `mtc1 at,f16` are in the
opposite independent order. The guards preserve retail's ordering; all other
words and relocations emit directly. Earlier candidates and failures remain
in the ignored private study; prepared v9 was not counted as a compiled screen.

All **six maintained tests** pass in primary tools, the isolated sibling overlay
and installed production at the same ten-file fingerprints:

- Whole-function symbolic relation across **10 paths**: ordered FP operands
  and FCSR, all **184 private/incoming-home bytes** at every call and return,
  complete return registers, all 108 descriptor bytes, arbitrary public
  provider mutations and retained transform-output mutations. All **169
  reachable words** are covered; raw/retail +0x60 is the same unreachable
  redundant load after the unconditional epilogue branch. It is recorded
  separately rather than claimed as executed. Ten semantic instruction errors
  reject independently of fingerprints; a hot-region T0/T1 rename passes.
- Independent guest model: **1,248 cases per retail/raw/guarded stream**, all
  public bytes, provider arguments, private descriptor/position homes and
  physical return value. Invalid links, actor gates, threshold and signed16
  count boundaries, all channel bytes, both stack phases, random flags,
  owner/actor aliases, pre-helper angle snapshots, post-helper accumulator
  reloads and late owner changes agree. There are no FP-order disagreements.
- Native32: **1,216 cases at O0 and O2**, strict aliasing and UB traps, all
  three 512-byte public objects, the 100 defined descriptor bytes and provider
  call counts. Eight broken semantic bodies compile and exit 3. Binary fixture
  inclusion avoids millions of C initializer tokens. The 32 BE byte/word alias
  cases remain guest-only; native typed fixtures do not claim endian aliases.
- Full original **45-word dispatcher**, **384 cases per stream**: signed
  callback disable, lifetime subtraction/wrap, actual update and cleanup tables,
  ignored result, cleanup callback and subsequent lifetime recheck. Cleanup and
  release remain bounded provider hooks; every dispatcher word is visited.
- Actual **224-word emitter + 61-word mode-zero base factory + 11-word memcpy**,
  **480 cases per stream**, **267 helper words visited**: zero through three
  allocations, exact six-argument forwarding/allocation tuples, allocation
  failure, 112-byte descriptor and four-byte parameter copies and output/owner
  aliasing. Complete public/private RAM and registers agree across streams.
  Other factory modes are outside this caller's domain; transform, trig,
  random and allocator providers remain bounded hooks. The 98-word transform
  is verified unchanged but is not itself executed by this connected test.
- Both real whole-owner padders, all **170 raw-word + six binding corruptions**,
  two actual stale-CSV controls and three independent GNU rebases pass. All
  22 neighboring functions and pools remain unchanged; old guard bytes remain
  an exact prefix.

The symbolic scope is normal mapped/aligned public RAM, a private disjoint stack
and bounded o32 providers. Arbitrary fault prefixes, general portable C aliasing
and live gameplay are not claimed. Native fixtures do not emulate hardware FCSR.
The guarded production stream separately has literal retail instruction identity.

## Production and retained evidence

Accepted predecessor: consumer `0fe610cf` / tools `b4b9531`.
All previous 1,335 inputs were verified before a **1,337-input** initial freeze.
The maintained **1,347-input** freeze changes exactly source, guard CSV, owner
object and ELF; **1,343 inputs remain unchanged**. An interrupted freeze was
completed only after the original process was authoritatively absent: 1,198
retained files were verified byte-for-byte and 149 missing copies were added.
No retained snapshot was overwritten or bypassed.

The initial compile stopped on a real file I/O error before compiling; Windows
subsequently reported paging-file error 1455. Memory availability recovered
without a restart, and all immutable inputs were reverified before compilation.
A deliberate missing-store control exposed a trace-prefix diagnostic bug, which
was fixed without changing the candidate. A whole-function register-rename
positive correctly failed cold-return temporary-register equality; the accepted
positive is restricted to the hot region and retains the full return-state gate.

Actual Make shadow and production rebuild from C without installing prebuilt
objects. Only one of 698 objects changes, preserving all other 6,050 bodies,
every address, 22 owner neighbors and pools. The complete ELF equals its
independent prediction: **522 changed bytes / zero
exclusions**. All 20,289 named definitions agree except target size; there are
zero metadata permutations. Symbol-value/name, protected-byte and
target-word corruptions reject. Conversion CSV remains unchanged. All
**189,088 protected bytes / 720 owners** remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production ELF SHA256: `982f0f31f23210afe687e32313befc8d64462b477eb5d1498c511a4a238b0338`.

Reproduce prepared qualification:
`python3 -m unittest tools.tests.test_game_attached_emission_151a4a38_recovery -v`.
Receipts: `conker/build/game-next-151a4a38-private/adoption/`.
The sibling's 2,434 dirty paths and scoped dependencies remain unchanged; actual
overlay/sibling/primary import origins are sealed. Root README changes only
Total/Game aggregate rows. Graphify retains historical IDs through a scoped AST
refresh; no full-corpus extraction is claimed. Zero Claude calls, no push,
dependency upgrade or host Release/save change. Commit tools before consumer.
Next inspect `func_151A5660` from the actual unmatched list; the 85% goal stays active.
