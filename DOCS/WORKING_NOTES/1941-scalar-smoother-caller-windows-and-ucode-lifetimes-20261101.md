# Scalar smoother caller windows and compiler lifetime evidence

`func_150495B0` now has reproducible qualification of three original caller
windows covering five JAL sites. This resolves representative six-argument
placement and caller-stack-local questions. It remains private and uncredited:
the best C is still 55 words / frame 16 / 38 word differences, against retail
54 words / frame 24. Production remains **4,014/5,506 (72.90%)**, Game
**3,341/4,833 (69.13%)**, zero drift, 1,492 different; **116 more** are needed
for the active 4,130/5,506 target. Experimental tools commit: `5d8ddc3`.

## Original caller windows

Every copied instruction is checked against its assembly ROM offset and the
original ROM word before execution. The callee executes as connected guest
instructions, using either retail words or the actual compiled private object;
it is never replaced by a modeled helper result.

| Window | Original PC interval, end exclusive | Call sites | Cases per program |
| --- | --- | ---: | ---: |
| Global XYZ smoothing, FDD70.s | 150D0A3C..150D0AD4 | 3 | 536 |
| Fixed coefficients, caller stack position, 15B5F0.s | 1512E3C8..1512E43C | 1 | 536 |
| Dynamic coefficients, caller stack position, 15B5F0.s | 1512E3F8..1512E43C | 1 | 536 |

Together these pass **3,216 window executions / 5,360 connected callee calls**.
Each window uses 268 finite input rows and two stack phases. The first executes
all three global component calls. The latter two update position at callerSP+72
and velocity at owner+0x25C, then execute the original consumption of that local
into owner+0x2FC and owner+0x344. The stack local is position, not velocity.

All six call arguments agree with independently constructed expectations.
Fifth/sixth arguments occupy callerSP+16/+20, including the actual sixth-argument
delay-slot store. Both root pointers are explicitly checked outside the outgoing
home area and the callee frame. Public bytes, caller locals, outgoing homes,
canaries and saved state agree with the rounded binary32 reference. Only the
callee's private 24-byte frame is excluded from byte comparison.

Six effective guest controls remove the sixth-argument delay-slot store or move
the fifth-argument home in each window. Each causes a wrong position or velocity
output; a changed call log alone does not count as killing a control.

These are bounded windows with explicit live-in fixtures. The dynamic window's
A0 is seeded from the preceding branch delay slot. Whole-caller reachability,
all 67 census sites, hardware FCSR behavior and a global return ABI are not
qualified by these tests. The provisional void interface remains provisional.

## CFE and UOPT captures

The fingerprint-locked frontend diagnostic captured two source/object pairs
without changing their emitted code, functions, relocations or pools. Driver
and owned compiler children completed successfully, with probe/order/cleanup
checks. No compiler executable or shared trace helper changed.

The best in-place source has 488 CFE and 493 UOPT records. In its first function,
UOPT emits `rlod R P`, offset 20, register offset 50: deltaTime is promoted to
F18, consistent with the emitted code. Next position stays at memory offset
-12, with a store and two loads; the local memory extent is 12, rounded to the
observed 16-byte frame. Retail instead reloads deltaTime after the velocity
write and uses one next-position reload from SP+4 after its comparison.

The named-acceleration source has 492 CFE and 499 UOPT records. Its 24-byte
memory extent is caused by a different lifetime: old velocity spills at -24,
while strength uses its parameter home. It matches retail length/frame but
still has 51 word differences. Descriptor-defined fields and emitted code
support these observations; a VREG marker alone is not register-allocation
evidence.

A further bounded six-value experiment moves the used next-position declaration
to the fifth/sixth local home under three rotations. All six variants emit the
same 55-word / frame-32 / 53-difference payload. Declaration position does not
resolve this allocation. No filler locals, IR edits, guards or source adoption
are introduced.

## Reproduction and retained evidence

```sh
python3 -m tools.experiments.game_scalar_velocity_smoothing_candidates --qualify-semantics
python3 -m unittest tools.tests.test_game_scalar_velocity_smoothing_private -v
```

The public experimental command now includes caller qualification. Four tests
pass in each tools copy; both shared tools checks pass. Existing native O0/O2/O3
and standalone guest qualification are rerun by those tests. The independently
dirty older tools mirror remains uncommitted and its unrelated work is retained.

Target stage: `conker/build/game-scalar-velocity-smoothing-150495B0-match`.
Receipts: `caller-windows-v30.json`, `caller-publication-v31.json`,
`next-homes-v32.json`, `lifetime-captures-v29.json`, and each capture's
`frontend.json`, `trace.json` and compiler output. No new Claude call was made.
The one-call advisory budget for this target remains spent.

Next: diagnose the value graph which promotes deltaTime while spilling next,
rather than repeating declaration permutations. Any new candidate must first
improve the measured code and then pass the existing semantic/caller tests.
Adoption still requires exact code/bindings or justified bounded guards,
owner/padder qualification, actual Make, independent full-image prediction,
production audit, recount and a separate adoption note. The wider 75% goal
remains active; this checkpoint awards zero matching credit.
