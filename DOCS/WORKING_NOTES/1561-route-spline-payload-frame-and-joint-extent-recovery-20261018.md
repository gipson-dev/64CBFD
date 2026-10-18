# Route Spline Payload Frame And Joint Extent Recovery

Date: 2026-10-18. Consumer predecessor: `ccaddf88`. Tools committed first as
`6067024`. Continues [Note1560](1560-route-spline-payload-semantic-recovery-and-array-homes-20261018.md).

## Current Boundary

The same `func_150896EC`, owner `generated_B3020`, VA150896EC..15089BB0,
ROMB6B9C..B7060, now has a complete experimental C point with the original
**305 words, 248-byte frame, three saved FP pairs and six literal array homes**.
It still differs at **140 linked words**. The production zero-return stub is
unchanged; no installation or matching credit is claimed.

| Qualified Point | Words | Frame | Linked Word Differences | Complete Memories Equal |
| --- | ---: | ---: | ---: | ---: |
| Previous front-declaration point, retained | 302 | 288 | 289 | 0 / 1,069 |
| New frame-correct point | 302 | 248 | 287 | 1,069 / 1,069 |
| New joint extent/frame point | 305 | 248 | 140 | 1,069 / 1,069 |

New unlinked body SHA-256 pins:

- Frame point: `f1c17b8f044c3d950100bf4b530cf11a41e1bbb8630f85219914d3dde0711ded`.
- Joint point: `a048f871640fe3d03e7fb09e74f72a91817cd83cc7e8030cf16d91d50499c2e7`.

Both new points pin all 33 bindings and retain all 72 other primary-owner
bodies/bindings. The joint point is the next extent-fitting basis, while the
302-word point remains a useful opening/private-state control.

## Compiler Evidence

One newly owned, read-only GDB compiler trace completed, including all children
and the driver. The isolated qualified front-declaration body has identical
normal/traced text, function definitions, bindings and pools. Compiler hashes
remain locked; no compiler installation, modification or game attachment.

The fired UGEN frame watch records **0 -> 72 -> 88 -> 288**. Its final event
contains 200 local bytes, 72 saved bytes and 16 outgoing bytes, with temporary
size/base 0 and an empty temporary pool. The CFE stream reserves M=189 bytes
and contains a one-byte anonymous M/-189 VREG; UOPT reserves M=196, rounded by
UGEN to 200. Frontend/optimizer streams contain 1,285/1,193 decoded records.
This identifies upstream local reservation in this trace, not a universal
absence of temporary allocation or a numeric compiler-cost measurement.

The inherited observer prints benign unresolved temporary-probe breakpoint
messages when switching to the assembler child. The actual frame gate fired,
all required exit markers exist and output identity passed; zero temporary
events alone would not establish the conclusion. Relative compiler output
paths preserve spaces. The user confirmed the earlier overwritten scratch
file was disposable; no recovery or unrelated deletion was performed.

## Source And Literal Layout

The double heading factor is read-only literal data. Writing `0.01745` instead
of an explicitly named double local retains all three saved FP pairs and
removes eight reserved bytes. Inlining the six previous-coordinate expressions
removes another 24 local bytes. Reusing the first channel's byte cursor for
the earlier captured-object lifetime recovers the 248-byte frame without a
float-pointer alignment assumption during object capture. The pointer is
rebound to its aligned float array before any float access.

Move the seven existing phase/cursor declarations before the arrays. Their
entry-SP-relative homes remain exactly -44, -60, -76, -92, -108 and -124.
For the joint point, use the existing node capture and two nonoverlapping
integer lifetimes during the single phase advance. No physical-register
bindings, dummy padding locals, frame guards or new build profile are added.

The new compact owner adds exactly one literal double and eight alignment
bytes: `3f91de69ad42c3ca0000000000000000`; the old owner had no .rodata pool.
Other pools remain identical. The first eight bytes independently equal the
installed protected retail data at 0x8009DA18. Private qualification links
.rodata at that address using SUBALIGN(4), with strict pool/address checks.
An initial --section-start experiment was rejected because input alignment
inserted eight leading bytes. It is not used by qualification.

Thirty-three fresh complete-owner screens span 302..309 words and frames
248..280; shape alone gives no semantic acceptance. `screens.json` explicitly
labels generic-link difference counts, whose orphan literal addresses are
not the final comparison. Only qualified points use the correctly placed
literal: the joint screen's generic count141 becomes **140**, not zero.

## Fresh Qualification

**Seven focused tests pass in 80.456s, no skips.** Each new qualified point
passes 1,069 paired cases with identical complete memory, ordered public R/W
traces and literal helper arguments. The frame point also independently agrees
with the retained public reference. Its full-memory breakdown is null28/28,
stop18/18 and spline1,023/1,023. All 96 array bytes and private call addresses
are equal, not merely normalized. Extra stop-queue aliases remain effective.

The four actual installed helpers independently equal retail and execute all
216 words: position35, neighbor91, enqueue41 and cubic49. Sin/cos remain the
explicit deterministic rounded Python providers from Note1560, not retail
trigonometric instructions. Native32, real trigonometric accuracy, undefined
leading history, hardware traps/FCSR and unknown indirect callers remain open.

Five newly compiled source negatives fail through ordinary semantic/call
differences: stop command, signed channel, wrong decrement, float rather than
double heading scale, and fresh rather than captured channel object. The
float control's own literal bytes are seeded before comparing both machines;
missing literal memory or a linker rejection is not counted as a witness.
Strict corruption checks cover 335 frame-point words/bindings, 338 joint-point
words/bindings and all 16 literal-pool bytes. Five trace corruption/fingerprint
controls reject missing fired gates, incomplete producer exits, altered input
streams and changed compiler identity. Tests do not restart the compiler trace.

The frame point retains the first 17 retail instructions and equal complete
register/memory states at 16 fired early access cuts. The joint point does
**not** retain that opening: its first save is S6 rather than retail S7, and
the fired cut1 witness has different private memory. Its record is in S6,
captured node in S0 and first array cursor in S7, not retail's S7/V0/S1 roles.
Thus whole-run memory agreement does not establish full fault-prefix state
equivalence. Register allocation, stop payload-base addressing, load grouping
and scheduling still require actual recovery/proof.

Three repository-setup tests and the tool smoke checks pass in both tools
copies; consumer `make tools-check` passes. The standalone mirror receives
only three previously absent, byte-identical task files. All 1,256 prior dirty
leaf hashes and its older HEAD are preserved; it is not reset or committed.

Reproduction from the consumer root under WSL:

```sh
python3 -m tools.experiments.game_route_spline_payload_frame --trace
python3 -m tools.experiments.game_route_spline_payload_fitting --qualify
python3 -m tools.experiments.game_route_spline_payload_fitting --joint
python3 -m unittest tools.tests.test_game_route_spline_payload_fitting -v
```

The trace command owns a new compiler run; inspect its existing handle/log on
failure rather than automatically retrying. Artifacts remain ignored under
`conker/build/game-route-spline-payload-frame/` and `game-route-spline-payload-fitting/`.
The earlier Note1560 source points, captures and unchanged qualification receipts
are retained, not replaced or described as freshly rerun.

## Production And Next Work

All 22 production/compiler/reference fingerprints remain unchanged, including:

- ELF: `dfa6424d042a037e643108a051757e78515e4b89ac9772a95b8b9845938742e2`.
- Owner: `4fee3adb19dd5ee7f6d9e62994c948472365705afd6867d46fc7634aa260e1fe`.
- Guards: `07994470d0e3d22e880a7bbd18188badd28eb5fde11ced8ec40bfa3176ff6647`.
- Makefile: `5d18b2170461785d270be99353e9bacdf4717ff2fd5d85231b702132740cb99d`.

No production build/recount or README change. Latest fresh totals remain
Note1559's Game2,988/4,828 and total3,661/5,501, with 1,840 different/zero drift;
they are not a fresh recount here. No host or frozen Release actions, pushes
or Claude calls. Codex independently settles these bounded compiler/source
questions without an advisory call.

Continue this same 305-word routine from `joint_selected()` while preserving
the frame point as an opening-state control. Recover literal saved-register
lifetimes, stop payload-base operations and grouped extrapolation/scheduling.
Then complete native32, independent rebases, caller/private/fault, actual
padder/Make prediction, installation, whole-ELF/data audit and fresh recount
before any matching credit. Vector15088F30 and the wider Game goal remain open.
