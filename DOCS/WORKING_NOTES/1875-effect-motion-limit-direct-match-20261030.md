# Note 1875: effect motion limit direct C match

2026-10-30. `func_150B36AC`, owner `generated_DFBF0`, replaces its zero-return
placeholder with a semantic six-argument callback. VA `0x150B36AC..0x150B378C`,
ROM `0xE0B5C..0xE0C3C`: all **56 words / 224 bytes** match directly from C.
There is no frame, alignment tail, relocation, insertion, omission or new guard.
The existing O2/g3 profile, shared headers and entire guard CSV stay unchanged.
Tools commit: `b98276e9e4c7a0a151724735d885f8a2c7fcc1d6`.

## Source and ABI

The callback stores record `+0x3C = +0x10 + offset`. It captures vertical motion
at `+0x48` and compares the limit at `+0x170`. When the limit is lower, it clears
flags through four separate read-mask-write assignments, with masks `~7`,
`~8`, `~0x40` and `~0x20`. Bit `0x10` remains set if previously set. It zeros
`+0x44/+0x48/+0x4C` and clamps signed halfword `+0x64` to32 only above32.
Otherwise it scales six components using the captured `+0x14` scale; vertical
is negated before multiplication. Both routes return integer1. Unordered
floating comparison follows the scaling route.

The recovered interface is
`s32 func_150B36AC(u8 *, s32, s32, s32, f32, void *)`.
The unused register arguments retain their ordinary 32-bit ABI cells without
inventing original meanings. Their incoming stack homes `+4/+8/+12` are written.
The fifth argument is a float at `SP+16`; the sixth pointer at `SP+20` is unused.
The byte-offset accesses keep uncertain field names local to this recovery.

Raw C and retail SHA-256:
`dd3bc82f1321192dc45e6bb4ca5c54eb8a5e669890fd42c3935d612765e1738f`.
Padded object SHA-256:
`763e5bdc370f2f5e2195238761208bd431f422590640f73998e28ba64ab59faf`.

## Qualification and limits

Ignored receipts: `conker/build/game-effect-motion-limit-150B36AC-match/`.
`semantic_v13.py`, `private_checks_v17.py`, eight fresh canonical checks in
each tools copy, shared tool checks and installed checks all pass.

- Guest: **6,472 cases / 19,416 executions**, complete modeled state and access
  trace equality across original, raw C and padded C. All56 words execute.
  Signed clamps, all low flag bytes, NaNs, infinities, signed zero and subnormals
  are covered within the bounded IEEE-single model. Hardware FCSR, exception
  behavior and platform NaN payload rules are not claimed.
- Incoming-home aliases:48 guest-only cases across12 record fields and two
  stack phases, plus95 access-prefix checks including three branch-delay cuts.
  These measure emitted instruction order, not portable C faults or invalid
  pointer semantics. Native tests observe final state, not intermediate stores.
- GNU relocation independence:90 cases over three independently linked entry
  layouts. This leaf has no symbol bindings; full state and access order agree.
- Callers: no aligned direct JALs, one literal pointer at ROM `0x22E408`,
  selector5 of the actual14-word `D_80089934` table. Twelve original window
  cases cover the two indirect routes at `0x1513300C` and `0x151339B0`, the
  disabled first selector route, fifth-float delay-slot store and signed-byte
  return handling. The second window begins after its selector-nonzero gate.
  Earlier helper behavior is bounded. No complete-parent coverage is claimed.
- Current `func_15133894` is retained assembly and all320 bytes match retail.
  `func_15132DDC` remains an uncredited C placeholder. Neither parent gains
  matching credit from this callback recovery.
- Native32:6,472 cases per O0/O2/O3 profile with trapping UBSan and complete
  seeded record/canary checks. Fourteen semantic defect controls are effective.
  NaN results are compared by class rather than payload. Fifteen separately
  IDO-compiled controls include14 rejected semantic defects and one equivalent
  clamp-boundary shape control. Combining the flag masks is another rejected
  equivalent instruction-shape control.
- Fingerprints reject224 single-byte corruptions and five size/binding/scope
  controls. Strict image checks reject corruption in the target slot, symbol
  row and unrelated ELF locations, without exclusions.
- Full owner:all five neighboring functions and pools remain fixed. The actual
  three-command Make recipe reproduces the complete padded object and six
  compact functions. Target compiler/owner/Make diagnostics are empty.

Failed fixture attempts are retained. The second caller window initially
included selector0 even though its earlier gate excludes it. Its signed-byte
return required adding the already-supported LB semantics to this local oracle.
The native harness needed the existing freestanding `-mstackrealign` flag.
The first package also inherited an obsolete guard hash/store index and an
ineffective compound-assignment shape control. Corrected tests pass without
production source or compiler-profile changes. Zero Claude/REA calls or installs.

## Image, progress and banking

Production reproduces the independent literal image prediction:
**178 changed bytes = 177 target-code bytes + one target-extent byte**,
metadata0, exclusions0. All6,055 other bodies, all6,056 function addresses and
189,088 Game-data bytes across720 owners remain unchanged. The conversion
inventory CSV, linker script, map and inherited guard CSV remain fixed.
All17,017 sealed current inputs are verified with only declared target outputs
and source overrides; the older tools mirror retains its2,063 inherited paths.

Adopted ELF SHA-256:
`94bceedb6ee2665484ad0a9d70c1d9db2d2542c29dcf1856e5608319e8fbaacc`.
Actual Native ELF recount: **3,952/5,506 (71.78%)**, Game
**3,279/4,833 (67.85%)**, Init492/492 and Debugger181/181, zero drift.
The75% threshold is4,130/5,506, requiring **178** more exact functions.

Tools are committed before the consumer source/docs/pin commit, which parents
the user's `4a282c6b` wiki-cleanup commit. No push. README changes only two
aggregate rows. Graphify receives a scoped source refresh with historical node
and relationship retention evidence; deleted historical wiki references remain
historical and do not imply a new extraction of those removed files.

Next private screen: `func_150CEF60`. Parked candidates remain uncredited. The wider
75% matching goal remains active. No host-port, editor, save or Release changes.
