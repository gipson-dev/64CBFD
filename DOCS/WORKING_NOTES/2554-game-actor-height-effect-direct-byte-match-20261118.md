# Actor height effect direct byte match - 2026-11-18

`func_150BAA14` is restored and **directly byte-exact from C across all 114 body
words / 456 bytes**, with its original **120-byte frame** and all **13 bindings**.
One unchanged zero alignment word completes the original **115-word / 460-byte
slot**. **No guards, normalizer, inserted instructions or omitted instructions**
are needed. The complete source body replaces its false zero-return placeholder.

Fresh production recount: **4,554 / 5,514 (82.59%)** total and
**3,881 / 4,841 (80.17%)** Game. Init remains 492/492, Debugger 181/181,
zero address drift and 960 different. Conversion stays 5,514/6,048 (91.17%),
86.19% bytes. **133 further matches** reach 85%. Root README changes only the
two aggregate matching rows; detailed progress stays here and in concise indexes.

Starting consumer `dc4e9ef670ba3ba6be49d27c8f920084df940b99`, tools
`1b117d554d14e2ac0c85fbf4cb0c78251931e783`, from
[Note 2553](2553-game-attached-actor-accumulator-guarded-byte-match-20261118.md).
The 1,814 committed inputs are verified, with two existing call-site source
owners and two original helper assemblies additionally frozen: **1,818 inputs**.
The six task artifacts are sealed separately. Byte copies and immutable
predecessor references are in `conker/build/game-next-150baa14-private/`; no live
hardlinks. The previous goal turn installed and committed the229-word accumulator.

## Restored source and original interface

Owner `conker/src/game/generated_E7970.c`, original `conker/asm/E7970.s`;
VA150BAA14..150BABE0 / ROM E7EC4..E8090. The recovered signature is
`void func_150BAA14(u8 *actor, s32 selector, s32 unused)`. The third word is part
of both real caller interfaces even though the body never uses it. The file's
obsolete placeholder header now accurately identifies the recovered C slice.
Five other owner functions and normalized pools remain unchanged.

The body preserves the actor+0x1D4 readiness gate; a 12-byte position and opaque
36-byte height output; the selector's low byte; cached low-byte query status
across two subsequent helpers; fixed preparation/command arguments; the conditional
record lookup; ordered float-to-signed32 truncations; event arguments; REAL then
unsigned RNG; and the final twelve effect arguments. Position and surface
buffers may remain exposed and change at later providers. The scale-derived
angle is cached before the event, while final position loads occur after RNG.
Unsigned arithmetic preserves the machine's wrap before signed16 narrowing of
angle+60/angle-60. Finite, representable signed32 conversions remain the native
C domain; no arbitrary truncation, FP-status or gameplay acceptance is inferred.

A typed record view expresses the measured **0x9A0 stride / field0x380**, with
unknown bytes left explicitly reserved. The height result's nine words are an
opaque storage shape, not invented semantic field names. Meaningful local
declaration order recovers the original status/angle/sample homes. Four layout
screens distinguish raw-address versus record-view indexing and original versus
recovered scalar order: 21, 15, six and **zero word differences**, respectively.
Every screen keeps 114 words/frame120 and all five neighbors/pools. No guessed
volatility, dummy local, shared header or compiler-profile change.

Selected raw unbound SHA:
`aaf8f739a501ecdcdc46b89b3e951580f361b1d837bfcaceb0377936dbcf5e3b`.
Source bytes and binding map equal independently assembled original before any
padding or link. Both actual owner padders retain the same 456-byte function
symbol plus its four-byte slot tail. The linked ELF's expected symbol-size
change from 12 to 456 is explicitly modeled, while every alignment byte remains
under the strict full-image comparison. No metadata or padding is excluded.

## Caller and callee evidence

The aligned retail census finds one direct JAL at15028A54 in the large original
50D80 dispatcher, and one literal pointer at ROM22EBBC / VA8008A0FC:
**D_8008A0B4 entry9**, with adjacent count **-1**. This is a scoped aligned
pointer/JAL census, not an exclusion of every possible address construction.

The genuine six-word direct window15028A4C..15028A64 passes actor, selector9
and unused wordFFFFFFFF, ignores the callback return and establishes V0=1 before
its continuation. **That direct window is not literal in current production**;
the large parent remains unqualified and unchanged. Its original window is
executed as reference evidence, not credited as a recovered parent.

The two real indirect dispatcher windows15141B4C/15141BAC are literal production
and reload this table callback. They pass actor/context with zero or a signed16
record amount as the third word. All five/eight window words are visited, and
the table pointer/count are independently checked against frozen ELF/ROM. Full
parent behavior beyond the windows is not claimed.

The first 26 actual instructions of `func_1514C678`, including both branch
outcomes, confirm the four o32 float arguments and signed16 stack arguments4/5/6.
These original/production prefix bytes match. Tests distinguish physical stack
words from the callee's meaningful signed16 values, including arbitrary upper
bits. The entire deep effect helper and gameplay remain outside this task.

## Fresh paired checks and production audit

Both final configurations pass **five tests**, zero failures/errors/skips:
**79.086s primary / 87.776s private sibling overlay**,
with **316 imported tool fingerprints each**. The 847-file overlay uses339
matching sibling copies,501 primary fallbacks,six task files and one empty
package bootstrap. The real sibling's dirty HEAD/status and343 dependency
hashes remain unchanged. Conflicting sibling edits were not overwritten or
represented as freshly tested.

1. Complete copied-owner before/after compilation; literal114-word/13-binding
 equality; independent original assembly/ROM; both real full-owner padders and
 all460 slot bytes; **12 independent GNU rebases** and **127 rejected source/
 binding corruptions**. The full existing guard CSV is reused byte-for-byte.
2. **1,024 guest cases**, visiting all114 body words, independently modeled
 readiness/status-byte gates, mutable retained buffers, late public globals,
 unsigned RNG, valid signed32 truncations and complete public memory/saved ABI.
 Source and original instructions are literally identical, including private
 accesses, branch delays and floating operands; no private-layout abstraction
 or commutative-operand relaxation is used for matching.
3. **128 direct caller cases**, **576 cases across both indirect windows**, and
 **128 actual callee-prefix cases**. All selector/unused-word conventions and
 signed16/byte boundary meanings are explicit. Parent and deep-provider limits
 are retained rather than inferred from a passing window.
4. **512 SDK32 native cases each at O0/O2/O3**, strict aliasing, no fast math and
 UBSan, compared with independent retail-executed transcripts. **11 effective
 negatives** reject readiness, status width, preparation/command arguments, record
 index/scale, event Y, final scale, angle offset, duration and signed RNG errors.
 Only initialized buffer bytes are observed, within their live provider calls.
5. Actual Make plus independent strict full-image prediction and four effective
 image corruptions, **zero exclusions**. Both configurations predict the same
 ELF, and production compiles the real source; no prebuilt object is copied.

Actual production recompiles only this owner, relinks and recounts. All **698
objects** are audited; only this owner changes. All **6,050 other function
bodies, addresses and extents**, five owner neighbors and normalized pools stay
unchanged. All **189,088 protected bytes /720 owners** remain exact. Only source,
owner object and ELF among1,818 frozen inputs change. The guard CSV, original
assembly, Makefile and conversion rows are byte-identical. The full ELF has
**368 explained changed bytes**, no alias-order metadata groups and zero
exclusions. Production SHA:
`d21cc93f91a8b810bcd3086728fe8b994fafeafdfb8d93a3905314d4c064a516`.

The gated-command declaration matches its frozen provider's byte return; the
caller deliberately ignores that return. The final source formatting also removes
one extra EOF blank line. A complete-owner
comparison proves all six functions/pools unchanged; both complete final suites
were rerun with the declared installed-input transaction and fresh output roots.
Earlier receipts remain archived and do not define the final task fingerprints.

Fresh installed checks independently compile all six owner functions/pools and
execute1,024 guest,128 direct and576 indirect caller cases against actual
production. Unchanged padder/rebase/native/callee-prefix/image receipts are
explicitly reused, not called fresh installed reruns. Production match-progress
and tools-check pass; the existing duplicate generated_12D630 recipe warning
remains. Root README only changes its aggregate rows. Graphify scoped refresh,
target reference and old-ID retention are recorded separately from the native
CLI's shrinking-update refusal; no forced overwrite or full-corpus claim.

Next inspect **func_150BABE0**, the zero-return placeholder at the start of
`generated_E8090.c` / `asm/E8090.s`: retail slot150BABE0..150BAFEC,
**259 words**, original **208-byte frame**. Freeze that owner C/assembly and
new caller/provider evidence from this committed baseline before drafting.
Routine work uses zero Claude calls and no REA/WSL reconfiguration. Frozen
Release, host captures, real saves and real sibling dirty work remain preserved.
Tools are committed first; no automatic pause or push. The85% goal remains active.
