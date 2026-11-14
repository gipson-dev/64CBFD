# Game direction-record update guarded match

Date: 2026-11-14. `func_151A7A90` replaces its zero-return placeholder in
`conker/src/game/generated_1D4E00.c`. The complete 183-word slot is
`0x151A7A90..0x151A7D6C` (ROM `0x1D4F40..0x1D521C`). Semantic C retains
the original 0x68-byte frame, saved S0/RA contract and two live owner roles.
Of the 183 words, 147 emit at their retail positions directly; 36 checked
guards restore local stack references and one closed instruction schedule.
No instruction is inserted or omitted, and all arithmetic emits unchanged.

The local delta, side, cross, death flag and loop-owner homes move together
from raw SP+0x38/0x44/0x50/0x5F/0x60 to retail
SP+0x3C/0x48/0x54/0x63/0x64 within the same frame. Outside the eight-word
schedule at offsets 0x1C4..0x1E0, all 28 guards change only an SP-relative
offset by four bytes. That schedule permutes the same eight operations,
after translating the homes, in order 3,6,0,1,2,7,4,5. It restores the
owner/death reloads and loop-index initialization around the first cross
scaling operation. There are no changed branch targets or guarded symbol
bindings. Raw C uses its own private homes; it is not credited with the
retail temporary-address or intermediate machine-state contract.

The updater conditionally decrements the signed 16-bit lifetime with
defined unsigned subtraction and retail halfword narrowing. It calls two
optional signed-byte-selected callbacks in sequence, treating their full
32-bit results as truth values. It reads the second selector after the
first callback. A dead record is released; a live record advances its timer.
On timer expiry it submits the signed-16-bit last-vertex index, context and
limit 100 to `func_151A8340`, then draws the new interval. The source
sequences the sample before re-reading helper-mutable range and minimum.
IDO removes the intermediate timer store without adding another local home.

With direction-valid bit 2, the routine builds endpoint delta and side
vectors, takes their cross product, scales it by the live reciprocal and
transforms each 24-byte vertex's three output coordinates. It reloads the
count through the retained original owner after the output writes. Typed
state and vertex declarations document the recovered offsets. The public
signature is `void func_151A7A90(struct102 *record)`, matching the registered
update interface in `func_151670C0`.

The retail registry `D_8008B4A8[0x2D].unk0` at `0x8008BDCC` points to this
routine. Sixteen original caller windows execute all nine words at
`0x15167164..0x15167188`: indirect dispatch, delay-slot next-node retention,
and the subsequent depth-indexed next-node load. They cover live/dead
records, callbacks, helper mutations and both tested stack phases. This
qualifies the window rather than the complete registry traversal.

Guest checks compare an independent bounded model with retail, raw C and
padded streams in 657 ordinary cases and exercise all 183 instructions.
Sixty-four additional cases execute the complete original 138-word
`func_151A87F8` attachment callback in this updater. Half also execute the
actual 29-word `func_151450B4` cross product, independently checked against
the production object and ROM. Deeper attachment providers remain modeled.
Twelve guest-only alias cases put vertex outputs over the owner count or
local basis vectors, or place the owner in caller stack storage. Retail and
padded machine states agree at 191 fired memory-access prefixes. Guest
aliases and fault-prefix checks are not claims about unrestricted portable C.

Native 32-bit C passes 349 cases in each of six O0/O2/O3 and
strict/no-strict-aliasing profiles with trapping UBSan, SSE floating point,
disabled contraction and standard excess precision. All seven source
controls are detected: wrong lifetime mask, truncated callback return,
premature second-selector snapshot, missing signed count narrowing,
premature interval-range snapshot, wrong vertex basis and wrong release
predicate. Fixtures use typed, aligned, disjoint records and bounded vertex
arrays; numeric fields and pointers are checked separately from unchanged
byte ranges. Optional table entries are controlled providers, including
synthetic second-callback entries rather than executing the retail NULL slot.

`func_151A8340` remains a placeholder and uncredited. Its existing old-style
declaration is retained; this caller supplies only integral/pointer arguments,
with no floating default-promotion issue. The modeled event, random and free
providers and deeper attachment helpers are not qualified complete routines.
Nonfinite/FCSR, unrestricted aliases, hardware and gameplay remain outside
these checks. Continue with `func_151A8340` next to recover the remaining
event/geometry helper in this chain.

Both padders match all retail words and pass 12 GNU links across four
independent symbol layouts, including HI16 carry boundaries. All 22 owner
neighbors and pools remain unchanged. Production uses the normal compiler,
padding and link rules, reusing 697 frozen neighboring objects after checking
that every appended guard belongs solely to this target:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The resulting ELF equals the independent shadow prediction. The strict
whole-image audit accounts for 568 changed bytes with zero exclusions and
no metadata groups. All 6,051 function addresses and 189,088 protected
Game-data bytes stay fixed. Only the target owner changes among 698
objects. All 786 immutable input fingerprints pass, including 82 headers,
retail assembly/input, compiler, prior conversion rows and other objects.
The 36 new guards append without altering prior rows. Prior unchanged
neighbor receipts remain prior evidence.

Tools commit `f08338a` retains the installed suite. It passes in the mounted
checkout and isolated sibling-tools overlay, as does `make tools-check`:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_direction_update_151a7a90_installed -v
```

The sibling's live baseline is 2,439 dirty paths at `ddbdd16`; identical
before/after status digests confirm preservation. The scoped fail-closed
Graphify refresh retains all 60,143 prior node IDs and reports 113,351 links;
this is not a full-corpus re-extraction. No host files were modified. The
prior `64CBFDOGL` path contains diagnostic/capture directories rather than
the former source checkout, so no host source/build/runtime comparison was
attempted and no Release artifact was touched.

Fresh production recount: total **4,474 / 5,516 (81.11%)**, Game
**3,801 / 4,843 (78.48%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift and 1,042 still different. **215** further exact total
functions are needed for 85% at the current denominator. The wider goal
remains active. Root README contains aggregate figures only.
