# Height Curve Progress Query Match - 2026-11-08

`func_151AE2BC` is byte-exact across all **59 words / 236 bytes**, with no
stack frame. Total **4,251 / 5,513 (77.11%)**, Game **3,578 / 4,840 (73.93%)**,
Init **492 / 492**, Debugger **181 / 181**. Address drift remains zero;
1,262 converted functions remain different. Another **160** exact functions
reach 4,411 / 5,513 and the active 80% goal. Conversion totals are unchanged.

## Source and five-argument interface

Owner: `conker/src/game/generated_1D92F0.c`. VA 0x151AE2BC..0x151AE3A8;
ROM 0x1DB76C..0x1DB858. The recovered entry is:

```c
void func_151AE2BC(f32 *output, CurveProgress1D92F0 *curve,
                  f32 x, f32 height, f32 z)
```

The routine uses the middle coordinate, while preserving the original five-word
call packet. Its sole aligned direct JAL is at ROM 0x1DB5FC / VA 0x151AE14C,
inside `func_151AE0E4`. The complete aligned image census finds no entry or
interior pointer literals and no other direct entries. The original caller
loads the actor's float X/Y/Z fields at 14/18/1C: X bits enter A2, Y bits A3,
and Z is stored at caller SP+10 in the call delay slot. A0 is the actor's +31C
owner pointer plus 0xA0; A1 is the resource pointer saved at caller SP+34.

The callee begins by transferring A3 to F12, retaining the output pointer in
A3, and storing the complete incoming A0 and A2 words into SP+0/SP+8. It
never reads the fifth argument. The unchanged SDK actor declaration names
these coordinate offsets, supporting float types for all three coordinates.
No C caller source or shared SDK declaration is changed.

Sixty connected cases execute all seventeen original caller-window words,
including the actual X/Y loads, Z delay store, call and resource reload.
After return, the original code explicitly reloads the produced scalar from
the owner. Poisoning both V0 and F0 leaves its behavior unchanged. The larger
parent routine is not fully emulated. Its later F0 use follows an explicit
overwrite from the coordinate difference.

## Recovered data and behavior

The local knot type is 24 bytes, with its height value at +4. The local curve
type exposes the knot pointer at +38 and unsigned count byte at +42. Other
fields retain reserved names. Native32 asserts the pointer width, knot size
and exact count offset; no broad shared structure replacement is introduced.

Read the count once and start index at zero. When `count - 1` is positive,
load the knot table and scan heights with a 24-byte cursor. Stop at the first
`height <= knot->value`, or after `count - 1` entries. The ordered comparison
preserves the original behavior for NaNs and unsorted/repeated values.

- Index at least `count - 2`: write 1.0f. Counts 0, 1 and 2 follow the
  original early-result rules; an empty scan does not load the table pointer.
- Otherwise, index zero: write positive zero.
- Otherwise, reload the live knot pointer. Read previous/current heights,
  subtract them, and compute `(height - previous) / difference` when the
  difference is nonzero. A zero span selects positive zero.
- Write `(float)(index - 1) / (float)(count - 3)` plus
  `fraction / (float)(count - 1)`, preserving the original separately
  rounded divisions and addition. X and Z do not affect this result.

The two incoming-home stores happen before count/table loads. Guest-only
fixtures qualify their overlap with the resource count and first knot, as
well as six output-alias layouts. Ordinary stable tables cannot reach the
interior zero-span fallback through this ordered scan. Controlled live-table
reload mutations exercise that defensive branch and distinguish a fresh
pointer read from a cached cursor; this is identified as controlled evidence,
not ordinary native execution of a changing table.

## Derived instruction schedule

Semantic C emits all **59 words**, with no external relocations and the
original register roles. A closed permutation produces retail's schedule;
**23 expected-word guards** implement it. The complete non-branch instruction
multiset remains identical. No new operation, literal, memory access or call
is supplied by the guards. The common zero and index/count conversions move
into the original live ranges; the independent index ratio moves after the
fraction branch. Branch destinations follow their complete blocks, including
the moved setup before the interior table load.

Raw C SHA256:
`330fd2dfd39cea3a99cd893965421887d0f72b23a97335ccd90997b7cafe4c83`.
Normalized and retail body SHA256:
`92605b2d63cb44c6ebeb2b311cf4b4f48c2d6aff3e69e3a6d6620b88bdd36ec3`.
All 59 individual raw-word corruptions, an unexpected binding, 23 stale guard
words and 23 unexpected guard relocations are rejected. Every inherited CSV
byte is unchanged. Raw C is checked for public memory effects; literal raw
register/fault scheduling is not claimed.

## Register metadata and complete owner

Restoring this floating routine changes the compact owner's CPR1 mask by
exactly **0x280**. A fresh isolated compile of the same semantic function
emits identical words and register mask `(A300C1FE,0,F5FF7,0,0,7FF0)`.
The predecessor owner's mask is `(A31FFFFE,0,3F5D77,0,0,7FF0)`; its exact
union with the isolated declaration is the new mask
`(A31FFFFE,0,3F5FF7,0,0,7FF0)`. All six fields are audited. Seventy-two
individual metadata-byte mutations across predecessor, new and isolated
objects are rejected. This accounts for the changed section explicitly.
An optional IDO assembly-listing probe failed in ugen with signal 11; no
listing evidence is credited. The normal compiler path succeeds.

The frozen baseline contains **107 inputs**, including all referenced
GLOBAL_ASM files, SDK headers, assembler includes and exact compiler/linker
inputs. All **32** other raw and padded functions and all owner pools remain
fixed. Strict and production padders agree across the complete 33-function
owner and its register metadata. This owner has no retained jump-table labels.

The actual five-command Make recipe reproduces the qualified complete owner.
Three independent GNU links and nine guest executions qualify rebased entry
addresses. The body has no external bindings or absolute service calls.
The literal full-ELF predictor permits exactly **183 changed bytes**, comprising
this function body and its symbol size from 12 to 236 bytes, with **zero
exclusions**. There are no symbol/string permutations or linked register-mask
changes. All 6,053 function addresses, other bodies, 720 protected data owners
and 189,088 protected data bytes remain fixed. Four corruption controls reject
code, header, symbol-size and protected-data changes.

## Execution and production evidence

Both tools configurations pass six focused checks before and after
installation in four sequential, fingerprinted runs. The sibling uses a
scratch overlay for the new modules and explicitly records read-only helper
fallbacks if any. Its HEAD and 2,434 inherited dirty paths are preserved.
Both configurations pass a fresh shared smoke check; three unchanged shared
synthetic regressions per configuration are explicitly reused by exact hashes.

- **1,808 guest cases** cover every count byte, ascending/descending/repeated
  and unordered knots, small counts, boundaries, signed zeros, infinities,
  bounded NaNs, six output aliases, three home layouts and both stack phases.
- All **58 reachable words** execute, including the zero-span branch under
  controlled live-table reload. Fifty cases actually exercise a table change.
  The duplicate MOV.S at 0x151AE380 follows an unconditional branch with no
  incoming branch target; it remains preserved and is not counted as executed.
- **84 executed memory-fault cuts** compare complete literal retail and
  normalized states. Raw C has matching public effects under the bounded
  model, without a claim of identical fault scheduling or FCSR behavior.
- **1,525 native cases per executable** pass at O0/O2/O3 with trapping UBSan.
  Every resource and table byte and both output canaries are checked. Ten
  effective controls reject a stub, signed count, strict comparison, wrong
  stride, last/first rules, previous knot, both divisors and wrong axis.

Numerical checks use a bounded nontrapping IEEE-single round-to-nearest model,
without emulating hardware FCSR flags/traps or legacy N64 NaN payloads. The
normalized body is literally retail. Native comparisons exclude NaN results;
controlled guest mutation and home aliases remain separate from native cases.

Production compiles exactly one C owner with no C diagnostics. The installed
ELF equals the complete prediction. `make all` retains the expected checksum
exit 2 while other functions remain unmatched, separately from successful
compile/link and the fresh matching recount. `progress.csv`, compiler profile
and Makefile remain unchanged. README changes contain aggregate rows only.

Production ELF: `4f1c6cffa47cdb0b298956cc3a058e44cf0d61a6d2e0f01bd9e73ec269920a4f`.
Binary: `c855208e68cb52de56920e615fccbefdd37e75b0bae18c327647885c59ba8ae5`.
Owner: `f759c8f6cf8e618db6af7d672384839280994efaa016eef3691b3e465cea4daf`.
Guard CSV: `5ec2bcc421e929efbf856ce3b03e3e8e30e06d56a3d8716492eafadb409bc166`.

## Resume boundary

Next ordinary C candidate: `func_150229E4`, a 73-word, frame-free actor/list
query in `generated_49D30.c`, pending complete caller/data qualification.
It remains uncredited. The smaller handwritten/nonstandard-register routines
listed in Note 2180 remain separate work without false C-match credit.

Scratch receipts: `conker/build/game-curve-progress-151AE2BC-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
retains unscanned existing nodes and audits changed-path relocations; it is
not a full-corpus extraction. Frozen host Release artifacts are untouched.
