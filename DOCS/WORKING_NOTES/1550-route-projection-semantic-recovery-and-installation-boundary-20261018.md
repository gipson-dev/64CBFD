# Route Projection Recovery And Installation Boundary

Date: 2026-10-18. Consumer predecessor **0116077**; tools predecessor
**2c94753**, new tools checkpoint **bc4a6e8** banked first. Target
**func_150891E8**, owner `generated_B3020`, VA **0x150891E8..0x150896EC**,
ROM **0xB6698..0xB6B9C**, retail **321 words /1284 bytes /frame0x78**.
Recover the complete C semantics, but **do not install or claim matching**:
the selected experimental body is307 words/frame120 with309 word differences,
including14 missing words, and has a demonstrably different private lifetime.
The wider Game matching goal remains active.

## Recovered Contract

Use `void func_150891E8(u8 *record, u8 *actor)`, not the alternate source's
float first argument. The retained caller passes pointers at JAL15087D4C
with a NOP delay slot in unfinished func_15087CC0. Capture actor+318 at entry;
return if null. Capture preferred class0/1 from unsigned-halfword
D_8008FDBC bit40. Record+30 is a signed-byte state, not a word.

For state2, scan signed-halfword D_80087290 over16-byte D_800D2350 nodes,
stopping after the first type5/class2 anchor. Store its low-byte ID to
record4A/4B; inspect all five neighbor bytes9..D, ignoring FF. Capture signed
D_800D23A8 for each valid candidate: mode0 accepts class3, nonzero accepts
other classes. The last accepted candidate becomes4B. Reload count after
the anchor, preserving the full-width scan index even above255.

Walk the closed cycle with real func_1508907C(current,FF,previous,preferred).
Capture the current node pointer before the call. Compare signed-node X/Z
against actor coordinates with separately rounded binary32 subtraction,
multiplication and addition. Start the minimum at D_8009DA08, whose original
rodata word is1e9. Keep the winning edge in4A/4B; stop when the returned ID
reaches the initial current ID. Retail has no artificial cycle fallback.
Queue command5 using a fresh actor+318, then write state3.

Common handling compares current/previous horizontal distances. If current
is nearer, update4A and call the selector again, then write4B. Retain the
captured current-node pointer across the call; refresh actor coordinates and
node coordinates afterward, but use the pre-call current distance. Read the
chosen nodeY and actorY, compute sqrtf(dy*dy+horizontal distance), normalize
all three components using the **unclamped** length, then cap length at1000.

Payload is record+4C. Preserve the zero stores, fresh actor XYZ copies and
projected XYZ writes, particularly capture projectedZ before zeroing payload4.
Write30f/30f/+0f at30/34/2C and projectedZ at1C. Queue command7 using fresh
actor+318 and the payload pointer. Finally write30f to entry-captured object
19C,1A4,1A0,1A8; do not reload the object for those final writes.

The guest executes both real helper bodies:91 selector words and41 original
enqueue words at1512D560. The enqueue helper rereads object channel+23D,
D_800DC2B0 and the selected B0-byte queue's cursorAC for each of four phases:
command store, payload store, increment and exact20 wrap. These reloads matter
when stores alias the object pointer or queue state. The helper's production
C is still a placeholder; running its ROM instructions is not qualification
of the production C chain or complete gameplay.

## Compiler And Private Boundary

The complete readable recovery and compact model live in
`tools/experiments/game_route_projection_setup.py`. Selected raw SHA-256:
`1825510015d392e2f819acaa88ea5372de3aa21771025fe060b0b8d2ae5af269`.
Strict gates bind all307 words,18 relocation sites and15 frozen inputs.

Normal O2/g3 emits307/frame120 with no diagnostics. All72 raw neighbors,
their relative bindings and normalized pools agree with a **normal-profile
baseline**. Production's existing owner uses the no-unroll profile; this is
not evidence permitting a whole-owner profile replacement. Compact no-unroll
instead emits250/frame72. Rejected word/byte mode variants range299..338
words; no declaration/shape result is installation evidence.

The normal model recovers the seven retail S5/S2/RA/S4/S3/S1/S0 save homes,
but that does not recover private locals. On the null-object path, raw C
unconditionally stores zero at **entry-SP-4**; retail leaves that word alone.
For nonnull objects, retail's captured object is SP+3C, versus model SP+74.
Other observed homes differ: preferred44/5A, best50/3C, distance5C/40
(retail/model, offsets from adjusted SP). The necessary extent/entry gate
accepts retail and rejects the model; it is not a sufficient match proof.
No guard generator, production replacement or matching-credit path is added.

## Fresh Qualification

```sh
python3 -m unittest tools.tests.test_game_route_projection_setup -v
```

Final six-test run passes in **25.668s**. Ignored sources, objects and JSON
receipts are under `conker/build/game-route-projection-setup/`.

- **575 paired raw/retail guest cases** compare public byte memory, including
  the record payload, and exact helper calls.480 base cases cover five states,
  eight finite coordinate patterns, three signed modes, both preference bits
  and queue cursors0/19.95 additional cases cover nine aliases, null objects,
  signed counts, no/later anchors and a qualifying anchor at index258/count300.
  Saved F20..F31 agree; both helpers execute actual instructions, not hooks.
- The independent retail-ordered reference agrees on all480 base traces.
  Raw ordered traces agree in only240/480, despite equal public results.
  Base cases visit281/307 raw root words and266/321 retail root words; helper
  visits bring connected totals to387/372. These are bounded finite fixtures,
  not complete branch, arbitrary float, fault-prefix or hardware coverage.
- **Nine compiled complete-C negative controls** produce real wrong public
  memory results: preference bit, root type, unsigned coordinates, premature
  clamp, cached payload inputs, refreshed entry object, refreshed selected
  table, omitted command5 and wrong command7. Crashes are not witnesses.
- Both stack phases expose the null-path private mismatch. A real raw word
  swap moving the payload zero ahead of the actorZ load changes aliased output;
  the correct ordering passes. Public tests deliberately exclude private stack
  memory, but explicitly reject a public fixture inside that exclusion window.
- Reject all307 raw-word flips,18 removed bindings and30 live/snapshot input
  corruptions. Locally added signed-LB support passes five signed values and
  five fired first-access fault controls; local sqrt.s support passes six
  +0/-0/finite/Inf/qNaN inputs. Shared runners are unchanged. This does not
  establish FCSR/signaling-NaN semantics or whole-function access-fault parity.

Earlier fixture mistakes are not retained as qualification: record80000 now
lies outside private stack40000; the original overlap accidentally excluded
record output checks. The effective negative controls exposed that mistake.
The reference's limit/previous-ID read order was corrected against retail;
480/480 trace equality now checks the corrected sequence. Count1/2 fixtures
use a closing FF route rather than a nonclosing cycle; no production bound
or fallback was invented. A truncated terminal output was checked against
actual process termination and fresh receipts before the final captured run.

Native32, independent parent rebases, complete caller execution, exhaustive
fault/private-state proof and linked installation are **not done**. An ignored
enqueue C probe emits41 words with30 register differences, but is unqualified
and uninstalled; do not confuse equal length with restored production behavior.
Routine recovery used **zero Claude calls**; no REA reinstall/setup was needed.

## Preserved Baseline

Production C, Makefile, guard manifest, linked ELF, progress files and root
README are unchanged. No build or recount is claimed. Verified fingerprints:

| Artifact | SHA-256 |
| --- | --- |
| Whole ELF | 4b8ab8ed1c080b5f392f60ddf05d2902229e3b4baa6cc880f006881538b7f9ea |
| B3020 C owner | f7db991ff588fad0fcfde4d10e0b234221abb82c829bea68c8ec5be954e1e17f |
| Guard manifest | c40fe51b50da9855fb73bc86bb2d0562e42365dc8afb1eb2c3603018040073a9 |
| Makefile | 840897f11d9fea8109c4e67c57e927efa6e1686de2b399fec2c9025828b92d49 |

Note1549's unchanged totals remain **Game2,985/4,828 (61.83%)**, **total
3,658/5,501 (66.50%)**, Init492/492, Debugger181/181, **1,843 different
/zero drift**. This checkpoint adds **zero matching credit**.

Shared padder/PC16 tests pass eleven per tools copy, both smoke checks and
consumer tools-check pass. Both task files pass ASCII/AST checks and are
byte-identical across copies. Standalone mirror HEADddbdd16 and all1,226
prior dirty hashes are preserved; only two absent files are added for1,228.
No mirror commit/reset, push, host or frozen Release action.

## Resume Here

1. Fit func_150891E8's full321-word extent and actual conditional object
   lifetime, including the retail null path, private homes and five-slot
   unrolling. Keep the existing no-unroll owner boundary explicit. Do not
   repeat the measured mode-width variants or normalize away missing words.
2. Qualify ordered/aliased accesses and original private/ABI behavior, then
   independent links, effective fault/semantic controls and any proposed
   closed normalization before prediction, installation and whole-ELF audit.
3. Recover production enqueue helper1512D560 separately. Its equal-length
   ignored C probe and the parent's execution of original ROM are not a match.

Keep vector15088F30's two-save fit, other parent150896EC and wider queues
open. The current production parent remains a false zero-return placeholder
at generated_B3020.c:887; this note banks a reproducible semantic recovery,
not a completed conversion or runtime acceptance.

Scoped Graphify refresh: **42,573 nodes /82,643 links /4,093 communities**.
All42,561 unaffected old IDs remain; the three duplicate UPDATE_LOG headings
relocate by eleven lines with the same labels/files. This note adds seven
nodes. Preserve19,398 nodes from2,972 excluded-but-existing files; tools remain
outside the configured graph corpus, not fresh Python AST-coverage evidence.
Original graph and ID audit remain ignored task artifacts. No full-scan purge,
committed graph output or history rewrite.
