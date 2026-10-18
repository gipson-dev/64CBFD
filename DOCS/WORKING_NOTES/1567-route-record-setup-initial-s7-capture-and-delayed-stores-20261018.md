# Route Record Setup Initial S7 Capture And Delayed Stores

Date: 2026-10-18. **Progress, not an installed byte match.**

## Baseline And Result

Continue `func_150870D0`, `generated_B3020`, VA `150870D0..15087350`,
ROM `B4580..B4800`, 160 words / frame 0x60, from
[Note 1566](1566-route-record-setup-semantic-recovery-and-private-order-boundary-20261018.md).
Consumer baseline `f4c1e431`; tools predecessor `483ddb2`.
Tools **b12e663** is committed before the consumer pin.

The complete experimental body now has **39 raw differences**, down from 43.
It retains the proper three-argument interface, original extent/frame,
S0/S1 walk roles, all 26 relative bindings and all 72 primary-owner neighbors
and normalized pools. Raw text SHA-256:
`823565227dec4d2fc1f6875ea3c50c42cb476ff1fa8bc7e7766455c34f6decc0`.

**All nine words at `150871C4..150871E8` now match literally**, including both
initial selector calls, the first result's byte mask into S7, its live lifetime
across the second call, and the two subsequent seed stores. The old private
cut-43 rejection is closed. An explicit `& 0xFF` on the selected class limit
also recovers the two original ANDI operations, without adding words.

Production remains the three-word placeholder. No new guards, Makefile edits,
production build, matching credit or README changes. The previously installed
vector/spline/projection/dispatcher baseline remains unchanged.

## Source Evidence

**34 additional bounded source forms** were measured, all without new compiler
diagnostics and with all 72 owner neighbors / normalized pools fixed. A guarded
comma-assignment validity gate removes the earlier extra transfer, keeping
160 words instead of 161. Reusing the two neighbor temporaries across the
initial captures and subsequent seed reloads restores the initial S7 lifetime.
Neutral `neighbor0` / `neighbor1` names and a short lifetime comment avoid
claiming that either temporary has one fixed directional role throughout.

Early declarations and the `register` hint do not improve allocation.
Separate temporaries alter incoming-count roles; narrower/unsigned and nested
forms regress the shape or saved roles. Unconditional scratch-byte views are
diagnostic only: 162/163 words, rejected, and not portable proof for reading
indeterminate bytes. The selected source still short-circuits those reads on
the selected-FF path. No arbitrary padding or physical-register binding is added.

The prior experiment and its 43-difference pin are unchanged. The new module
reuses its compiler, frozen-input and owner-measurement APIs. The new test
class runs the existing semantic/native/caller/corruption cases with the new
model scoped into their module, not by weakening the earlier fixture.

## Fresh Qualification

**Eight tests pass in 44.157 seconds, no skips.**

- **1,259 paired ordinary guest cases**: 530 route/count/provider cases plus
  729 five-slot/class cases. Compare complete ordinary memory, ordered public
  accesses/calls, both stack phases and saved ABI. Include long 128/254/255-node
  routes and the existing guest-only alias providers.
- Execute the real linked 19/88/33-word lookup/selector/constructor helpers,
  freshly checked against retail; only allocation is opaque and caller-clobbering.
- **1,286 native32 cases per O0/O2 build**, both with UBSan and all three actual
  C helpers. Complete banks, route bytes, globals and ordered calls agree.
  Five semantic negatives exit ordinary wrong-result 23, not a crash.
- **41 retail-only caller windows** preserve the full-width key/player/extra
  arguments, real A2 delay-slot load and caller zero-result branch. The one
  whole-Game direct site remains func_1509DFC4 at `1509E1B8`.
- **186 raw-word/binding** and **46 live/snapshot corruption controls** fail
  closed. All 23 real production inputs remain byte-identical.
- **472 paired call-lifetime observations** require the independently expected
  first result in S7 before the second selector, with both seed bytes still
  unwritten. The freshly recompiled prior 160/43 body is an effective negative:
  it fails this observation and the nine-word literal window.
- A four-node witness separately checks the later saved roles, so the initial
  capture result is not mistaken for lifetime equivalence through construction.

These are finite guest/native tests, not full caller execution, unknown indirect
interfaces, universal portable-C proof, physical hardware traps or gameplay.
Native tests retain the documented exclusions for incompatible guest aliases,
positive null allocations and malformed/nonterminating routes. No unchanged
broad neighbor suite is described as freshly rerun.

## Next Concrete Boundary

**465 fired paired memory cuts: 174 exact memory/access prefixes, 291 rejected**,
versus 140/325 before. The original cut 43 is explicitly required to agree.
The per-fixture raw/retail access counts remain 243/243, 158/158, 28/28 and
36/37; the unpaired final early-failure access is not called a fired raw fault.

The first remaining rejection is **cut 60**, both recorded PCs `150871F0`.
The previous completed access reads parent `SP+0x48` in the candidate and
`SP+0x49` in retail. RAM bytes happen to agree in that three-node fixture;
the **access order** does not. This is not a new output mismatch.

In the four-node witness, both bodies initially capture the same first result
in S7 and have identical complete ordinary memory/public traces/calls. At each
of the three constructor calls, however:

| Model | S7 | FP/S8 |
| --- | ---: | ---: |
| Candidate | 3, before index | 2, after index |
| Retail | 2, after index | 3, before index |

**Continue this same function**: recover the post-call seed reload order and
preserve the after/before values in S7/FP respectively. Do not lose the now-
literal initial capture block, 160-word/frame-0x60 shape, S0/S1 walk roles,
full-width argument/count sum or signed-limit access order. Full private
ordering, source-derived all-word/binding fit, actual padding/Make, independent
rebases, first whole-ELF prediction, installation, linked audit and fresh
recount remain open. No complete normalizer is claimed.

## Banking And Reproduction

Tools **b12e663** first. Copy only the two absent task files into the standalone
mirror, byte-identically, preserving its older ddbdd16 HEAD and all **1,272**
previous dirty hashes. The mirror now has **1,274** dirty leaf paths; it is not
committed or reset. Both task pairs are ASCII and AST-valid. Three repository-
setup tests and smoke checks pass in each tools copy; consumer `make tools-check`
passes. No push, Claude call, debugger/emulator work or host/Release actions.

Production hashes remain the Note 1566 baseline, including whole ELF
`e55a6d218b40d9216dbe690c058132eacbae0e57d009c0f2670501ff46aa65b3`.
The last installed Note 1565 counts are reused, not freshly recounted:
Game **2,990/4,828 (61.93%)**, total **3,663/5,501 (66.59%)**,
**1,838 different / zero drift**. Root README remains aggregates-only and
unchanged; this experimental improvement earns zero new matching credit.

From the prepared consumer root under WSL:

```sh
python3 -m unittest tools.tests.test_game_route_record_capture -v
python3 -m tools.experiments.game_route_record_capture --qualify
python3 -m tools.experiments.game_route_record_capture --widths
make tools-check
```

Ignored `conker/build/game-route-record-capture/` holds frozen inputs, all
34 source-screen objects/commands/receipts, selected owner/native artifacts,
the old-model control, capture/later-role observations and private-prefix
rejection. The wider Game matching goal remains active.
