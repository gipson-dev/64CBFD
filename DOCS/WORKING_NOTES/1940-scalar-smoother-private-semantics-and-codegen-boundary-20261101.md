# Scalar smoother semantics qualified; byte matching remains private

`func_150495B0` remains an uninstalled, uncredited private candidate. Its finite
position/velocity behavior is now reproducibly qualified against original code,
but the best ordinary C screen still emits **55 words / frame 16 / 38 real word
differences**, against retail **54 words / frame 24**. This checkpoint adds
experimental tools and evidence, not a function conversion or a byte match.

Production remains **4,014/5,506 (72.90%)**, Game **3,341/4,833 (69.13%)**,
zero drift, 1,492 still different. Init 492/492 and Debugger 181/181 stay exact.
The active 75% target remains 4,130/5,506: **116 more matches** are needed.
Consumer matching baseline: `15be776e`; experimental tools: `9558afc`, committed
before this documentation pin. No production source/object/ELF, guard CSV,
conversion inventory or root README aggregate changes are made.

## Recovered operation and provisional ABI

VA 0x150495B0..0x15049688; ROM 0x76A60..0x76B38; owner generated_76A60.
The six proposed arguments are `(f32 *position, f32 target, f32 *velocity,
f32 strength, f32 damping, f32 deltaTime)`. A1 and A3 carry float bits moved
into F12/F14. Fifth/sixth arguments are at entrySP+16/+20, or retailSP+40/+44
after its 24-byte frame allocation. Return-value use still needs caller analysis.

The routine computes difference=target-position and its sign, scales difference
by strength, and updates velocity by `(difference-velocity)*damping*deltaTime`.
It then reloads the updated velocity and position, computes
next=velocity*deltaTime+position, and compares the old and new target-direction
signs. Agreeing signs retain next; disagreement stores target and then zeroes
velocity. That final store order matters when the two pointers alias.

The selected private C updates difference in place. This recovers retail's
opening argument moves and scaled-difference register lifetime. It still has
the wrong later allocation: retail reloads deltaTime after the velocity store,
compares the computed next value before storing it to SP+4, and reloads that
slot once for the final position store. The candidate caches deltaTime and
reloads its staged position twice. These are unresolved compiler lifetime and
stack-layout differences, not two independent scheduling words.

## Finite behavior qualification

An independently rounded binary32 reference and both original/candidate guest
programs agree across **1,072 cases / 2,144 executions**, including two stack
phases, separate pointers and exact position/velocity aliases. There are 244
snap cases and 828 accepted-position cases. The corpus includes both signed
zeros, equal targets, zero time/strength/damping, overshoot in both directions,
negative factors and finite cancellation cases. Every public word and canary
is checked, and saved GPR/FPR/SP state is preserved.

Retail reaches 52 of 54 static words. The two unreachable scheduling copies are
at offsets 0x3C and 0xC4. The candidate reaches 53 words. Full equality of private
stack traffic and caller-saved scratch registers is not claimed, because the
compiler layouts differ. Aliases with outgoing argument-stack slots are
excluded; actual caller argument placement still needs qualification. NaNs,
hardware FCSR and denormal traps are outside this finite model.

Native32 O0/O2/O3 each pass **536 cases** under UBSan, with eight effective
compiled controls: missing strength, missing damping, missing time in the
velocity update, wrong initial sign, wrong equality boundary, missing velocity
zero, reversed clamp stores and missing accepted-position update. All public
words and canaries are compared, including alias cases.

Three fresh private qualification tests pass in both tools copies, and both
shared tool checks pass. The tests verify the measured nonmatch explicitly,
finite behavior and negative controls, and unchanged production inputs. The
complete owner preserves its one other function and pools without diagnostics.
There is no production Make, padding or whole-image adoption claim for this
private body.

## Caller census and experiments retained

All **67 aligned JAL literals** map to original executable call instructions in
**22 containing routines across 18 assembly files**, checked against ROM words.
No aligned function-pointer literal exists. This establishes ownership of the
sites, not execution of all callers or return-value consumption. The original
six-argument setup is visible in representative source windows; complete
caller-window execution remains pending.

Initial ordinary C emits 52 words/ frame 0 with 42 differences. Updating difference
in place improves to 55/frame 16 with 38 differences. A named acceleration value
can produce 54/frame 24, but with 51 differences and the wrong spill target.
The other source's auto-decompiled body produces 54/ frame 32 with 52 differences,
so it was not adopted. Its provenance/hash is retained privately.

Bounded formal/local register annotations, declaration orders, expression/value
copies, pointer-access qualifiers, alternate return/storage forms, scratch
carriers and optimization profiles did not resolve the mismatch. O1 alone is
farther away; O1/g3 was rejected by the preprocessor before compiler invocation.
No-unroll is ineffective here. Exact failed shapes and object/disassembly
receipts remain in the target stage; no fabricated volatile storage or padding
has been installed.

One packet-only Claude advisory call completed through the existing configured
route with effective tools=[] and mcp_servers=[]. Its three suggestions were
independently compiled: splitting the final reset worsened the code, and
reversing the comparison or multiplication spelling was ineffective. All three
are rejected on measured evidence. No further advisory calls are authorized by
the current per-task budget. Packet, hash, response and dispositions are private.

## Reproduction and next boundary

```sh
python3 -m tools.experiments.game_scalar_velocity_smoothing_candidates --qualify-semantics
python3 -m unittest tools.tests.test_game_scalar_velocity_smoothing_private -v
make tools-check
```

These commands create private fixtures under conker/build and do not install
source or change matching counts. The original placeholder must still be
present; the command fails if that baseline changes. Selected C, retail words,
compiler/profile outcome, owner/pool checks and semantic receipts are emitted.

Stage: `conker/build/game-scalar-velocity-smoothing-150495B0-match`.
Key receipts: `private-semantics-v20.json`, `caller-census-v10.json`,
`register-lifetimes-v4.json`, `declaration-order-v12.json`,
`advisory-variants-v11.json`, `canonical-primary-v22.json`,
`canonical-mirror-v23.json`, and the fresh public-private-run subdirectories.
All 999 before-input copies and hashes are retained. The 17,482-file production
seal is preserved apart from intended documentation changes; new experimental
modules are added in both tools copies. The independently dirty mirror stays
uncommitted. Scoped nine-file AST refresh retains all prior graph nodes and
edge occurrences, with zero retired return-type edges because source is unchanged.

Next: inspect CFE/UOPT value/lifetime records for the excess next-position reload
and cached deltaTime, using the retained source/object pairs instead of repeating
surface spelling screens. Qualify representative real caller windows and the
argument-stack separation. Adoption still requires a credible 54-word/frame 24
compiler shape, owner/padder/actual Make, literal full-image prediction,
installed checks, recount and a separate adoption note. Goal remains active.
