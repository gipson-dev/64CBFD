# Game midpoint subdivision guarded match

Date: 2026-11-14. `func_151A8340` replaces the zero-return placeholder in
`conker/src/game/generated_1D4E00.c`. Its complete retail slot is
`0x151A8340..0x151A8560` (ROM `0x1D57F0..0x1D5A10`), 136 words with a
0x78-byte frame. Normal O2/g3 emits the complete semantic body in 135 words
with the original saved-register roles. Twenty-two expected-word guards
restore instruction scheduling, two commutative multiply operand orders,
three branch displacements and the original first-call delay-slot no-op.
No original operation is omitted. The one inserted word is a no-op.

The first two scheduling rows exchange the dz subtraction and first random
call, move that call's `R_MIPS_26` binding with it, and append the no-op.
Only the two forward exits and the back edge cross that inserted word.
The other schedule is a closed permutation of 18 operations at output
offsets `0x158..0x1A0`, in order
`2,0,1,6,4,5,9,7,10,11,12,13,14,15,16,17,3,8`; 15 words change position.
The recipe changes no arithmetic operation, memory offset, recursion
argument or saved-register home. Raw C is not credited with the retail
intermediate instruction schedule or fault-state contract.

The recovered signature is:

```c
void func_151A8340(u8 *record, s16 first, s16 last, f32 amplitude, s16 depth);
```

The fourth argument travels as float bits in A3 after the leading pointer
and integer arguments. The fifth argument is the signed 16-bit recursion
limit in the outgoing stack area. The caller's field at `record+0x20` is
therefore renamed from integer `context` to `f32 amplitude`, and its
old-style helper declaration is replaced with this precise prototype.
These corrections preserve every raw word and binding in `func_151A7A90`;
the linked audit also confirms the caller remains unchanged and byte-exact.
This supersedes the provisional field/interface interpretation in Note 2427.

Ranges shorter than two vertices and nonpositive depths return immediately.
Otherwise the helper computes the signed midpoint, snapshots the endpoint
deltas and retains the original left anchor. It draws separate random
displacements for midpoint x and y, each centered around zero using
`sample * (amplitude + amplitude) + -amplitude`. The z coordinate uses
ordinary midpoint interpolation. Anchor coordinates are read after their
corresponding providers, while the delta snapshots survive those calls.
Each output reloads the current vertex-array pointer. The left half is
subdivided recursively, followed by the right half; IDO converts the latter
call to the original loop. Both recursive calls receive `depth - 1` without
prematurely overwriting the parameter's incoming home.

Guest validation passes 1,086 independent-model cases against retail,
raw C and padded streams, exercising all 136/135/136 instructions. Cases
include reversed/empty ranges, negative first indices within allocated
storage, shallow and deeper subdivision, signed depth boundaries, poisoned
upper argument halves, positive/negative zero and signed amplitudes, and
providers that mutate anchors or replace the vertex-array pointer.
Eight additional guest-only alias cases place the owner in caller stack
storage or overlap vertices with the incoming depth home. Retail and padded
machine states agree at 354 fired memory-access prefixes. These physical
stack-alias and fault-prefix cases are not unrestricted portable-C claims.

Eighty coupled cases execute this helper through the complete original
183-word `func_151A7A90` updater, including its real five-argument call,
timer continuation and vertex-output loop. Half also execute the actual
29-word cross-product helper. Zero/one-vertex cutoffs, four amplitude bit
patterns, both tested stack phases and larger bounded ranges are covered.
The random provider and remaining outer helpers are controlled stand-ins;
their complete behavior is not newly qualified by these cases.

Native 32-bit C passes 546 cases in each of six O0/O2/O3 and
strict/no-strict-aliasing profiles with trapping UBSan, SSE floating point,
disabled contraction and standard excess precision. All seven source
controls are detected: wrong range/depth cutoffs, midpoint, noise bias,
cached output-array pointer, reloaded left anchor and wrong z delta.
Inputs are typed, aligned and disjoint with bounded allocated arrays.
Numeric float words, pointer identities and unchanged bytes are checked
separately to account for native endianness. Nonfinite/FCSR, unrestricted
aliases, hardware and gameplay remain outside this qualification.

The existing updater suite is rerun after the interface correction: 657
guest cases, its original caller/alias/fault checks, and 349 native cases
per six compiler profiles still pass. Its former missing-cast negative
control is replaced by an incorrect last-vertex index: the precise `s16`
prototype now enforces narrowing even if that source cast is removed.
All seven updated parent controls are effective.

Both padders pass 12 GNU links across four independently rebased code
layouts, including the self-recursive binding. All 22 owner neighbors and
normalized pools stay unchanged. Production uses the existing normal
compiler/padder/link rules, reusing the 697 frozen neighboring objects:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The production ELF equals the independent shadow prediction. The strict
whole-image audit accounts for all 422 changed bytes with zero exclusions
and no metadata groups. All 6,051 function addresses and 189,088 protected
Game-data bytes remain fixed. Only the target owner changes among 698
objects. All 786 immutable input fingerprints pass, including 82 headers,
the compiler, retail assembly/input and prior conversion rows. The 22 new
guard rows append without changing earlier rows or the Makefile.

Tools commit `64b6768` retains the new installed suite and parent test
correction. Both installed suites pass in the mounted checkout and isolated
sibling-tools overlay; `make tools-check` also passes:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_direction_subdivide_151a8340_installed tools.tests.test_game_direction_update_151a7a90_installed -v
```

The sibling retains its 2,439 dirty paths at `ddbdd16`, with identical
before/after status digests. One focused Claude advisory used effective
tools=[] and mcp_servers=[] through existing subscription auth. Its
overbroad byte-identity claim was rejected against literal comparison;
the accepted closed permutation and all qualification results are
independently measured. The packet, response and reconciliation remain
private build receipts.

The scoped fail-closed Graphify refresh retains all 60,145 prior node IDs
and reports 113,354 links; it is not a full-corpus re-extraction. No host
files or Release artifacts were changed. The prior `64CBFDOGL` path still
contains diagnostic/capture directories rather than its former source
checkout, so no host source/build/runtime comparison was attempted.

Fresh production recount: total **4,475 / 5,516 (81.13%)**, Game
**3,802 / 4,843 (78.51%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift and 1,041 still different. **214** further exact total
functions are needed for 85% at this denominator. The goal remains active.
Next screen: `func_151A8624`. Root README contains aggregate figures only.
