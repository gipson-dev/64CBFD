# Dual-point weighted motion match and private weight lifetime

Date: 2026-11-06. Continue the 80% goal from consumer
`ac28118b90f93cd603eeaa5eaaa878e40a053b0c` and mounted tools
`8db1a6cbb4814a949df823f4d675fe0125b81e59`.
This completes the private next target in
[Note 2118](2118-game-text-buffer-fade-guarded-match-and-compiler-lifetime-recovery-20261106.md).

## Installed result

`func_1514A594`, owner `generated_176A00`, now matches its complete67-word /
268-byte slot: VA0x1514A594..0x1514A6A0, ROM0x177A44..0x177B50.
The raw C has the original frame0x18, SP+4 weight store/reloads, return1 at
offset0x58 and return-delay stack restore. Seven expected-word guards restore
late FPR roles and three commutative addition operand orders. There are no
frame guards, inserted/omitted words or emitted model-adapter instructions.

The callback damps shared X/Z velocity at0x130/0x138 with factor0x140,
adds acceleration0x13C times the live timestep to velocityY0x134, then uses
a second live timestep read to advance both points at0x34..0x3C and0x40..0x48.
It blends the second point toward the first using weight0x54. Each single
operation rounds independently. The source retains typed float accesses,
descriptive component/anchor names and the one-pointer/signed-return ABI.
No decompiler integer-to-float misloads are imported from the adjacent source.

## The private alias that rejected the first fit

The first source emitted72 words. Reusing the finished Y/Z step variables
as first-point anchors removed four anonymous SP+0 store/reload words and
gave68/frame0x18. Byte-offset damping accesses recovered V0 as the time
address and delayed return1 to its original position, removing the extra NOP.
That first67-word candidate still had12 differences and was rejected.

With `owner = entrySP - 20 - 0x34`, firstPointX overlaps the real SP+4 weight
home. Retail reads firstPointX before writing the weight there; the first
candidate reads it afterward. The symbolic model rejects that layout, and an
independent guest execution produces a different endpointX. This is a real
memory-value failure, not a dead-register or scheduling-only difference.
The original rejected object and its failing alias are retained as a control.

An explicit early `firstX` snapshot fixes the lifetime while retaining67
words/frame0x18. The final seven differences are at0xBC,0xC4,0xD0,0xD4,
0xE8,0xEC,0xFC. Late firstY/firstZ use F14/F16 in raw C and F0/F2 in retail;
the preceding velocity/timestep roles are already dead. Three ADD operands
are exchanged. Every real instruction remains at its original position;
all memory instruction addresses/order, GPR roles, frame and return match.

The existing linear FP model receives a logical SP initializer and a checked
presentation of the return-delay restore. These three additional model words
are never emitted. Its complete70-entry instruction permutation must be the
identity. It verifies all163 ordinary/timestep/private-weight layouts without
reassociation. The actual raw and padded bodies remain67 words. This raw
expression proof does not establish NaN payloads, FCSR or fault timing.

## Compiler observations and rejected controls

The owned, fingerprint-locked normal O2/g3 CFE/UOPT/UGEN capture is reproducible:

```sh
python3 -m tools.experiments.game_dual_point_weighted_motion_frontend_trace
```

The isolated target and complete owner emit identical words/bindings. Captures
require actual intermediate paths, fired probes, producer/consumer/driver
completion, exact cc/cfe/uopt/ugen hashes and unchanged emitted objects/pools.
The final stream has622 CFE and549 optimized records. CFE SHA-256
`3a47029ccd4565f40a1219c688b81cbdc3da8fb950c39bc0b898cb0cf4a25ba3`;
UOPT SHA-256
`b2520ee03e2cf5b92b089305117a75b7f617a9c1a451ed4d05a23c1d0dfb2e8d`.
The preceding68-word control and focused field/lifetime screens are retained.

Naming the return value, caching the timestep and naming its address did not
repair the68-word form. Caching every anchor removes the real frame; a local
weight array restores a frame but still overflows. The mixed byte/array field
views and explicit named X lifetime, not an alternate profile, recover the fit.
The asm processor rejects O2/-g; direct IDO reports that -g disables optimization.
That profile is not qualified or installed. The generic constructor helper's
leading-word frame assumption is corrected locally in this trace wrapper by
finding the actual SP adjustment after the two opening address words.

No Claude call was made for this function. No compiler, dependency, REA setup
or host-port configuration was changed.

## Fresh qualification

Run from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_dual_point_weighted_motion_match -v
```

All nine installed checks pass in the mounted tools and through an ignored
overlay using the dirty sibling's actual compiler, parser, timing/FP engine
and native32 command builder. Helper paths/hashes and any mounted fallback
are recorded; the sibling is not edited. Both tools smoke checks are fresh.
The prior progress/word-guard/PC16 regressions are explicitly reused after
verifying unchanged helper hashes, not represented as newly executed suites.

- **10,080 cases per guest body**, retail/raw/normalized, check an independent
  rounded reference, all67 words, signed zero, subnormals, infinities, NaN
  classes, preserved GPR/FPR ABI and return1. Raw NaN payloads are not equated.
  Normalized complete RAM/register/event/PC state agrees literally with retail.
- **974 alias cases per body** cover all81 aligned timestep field positions,
  all81 owner offsets relative to the private weight home, both stack phases
  and rebinding the timestep itself to SP+4. The reference models the early
  X snapshot, actual private store and each subsequent live weight reload.
- The rejected late-X object fires its concrete mismatch again. **195 fired
  fault prefixes** require literal normalized private-state equality. Portable
  C private-stack aliases, raw fault timing and physical FCSR are not claimed.
- The complete **195-word original parent** executes32 success/skip scenarios
  per normalized body and covers49 parent words in these paths. Table slot6
  is `D_80089CB8[6]`, sole aligned literal ROM0x22E790. A controlled false return
  reaches the original cleanup call; return1 prevents it. Cleanup remains
  opaque in that negative control; unrelated parent branches are not covered.
- **Nine independent GNU links** at three addresses exercise both HI/LO
  bindings and carry boundaries, with240 sampled cases per body. The symbolic
  private-alias proof also runs at stack phase8 for each rebase.
- **12,288 native executions**, SDK widths, real float-array storage and12
  timestep field aliases run at O0/O2/O3 with UBSan and FP contraction disabled.
  Both direct and compatible callback calls are checked. Nine negative controls
  fail in native code and actual IDO output, including an effective early-time
  cache witness at field0x130. Native output NaNs are compared by class only.
- **268 raw-byte corruptions**, two binding corruptions, seven actual padder
  expected-word controls and five whole-image corruptions fail closed.

The first caller test expected a list where the oracle emits a tuple; that
representation-only fixture error is corrected. The focused caller check
passes before installation, and both complete installed suites pass afterward.
No candidate behavior or acceptance condition is weakened for that correction.

## Production proof and progress

There are99 frozen inputs. All35 compact/padded neighbors and allocated data
pools are preserved. The complete compact register-use metadata change is
pinned: `e3fffffe00000000ffff5ff7000000000000000000007ff0` to
`e3fffffe00000000fffffff7000000000000000000007ff0`; padded pools are identical.
Warning712 at the unchanged `func_1514BF50(arg0)` call is pre-existing. Only
source filenames and line locations are normalized when comparing diagnostics.

The strict whole-image prediction changes227 bytes: the target slot and its
12-to268-byte symbol extent only. It has zero exclusions or metadata
permutations; all6,052 function addresses and189,088 protected bytes /720 owners
stay fixed. The guard CSV preserves its entire predecessor prefix and appends
only the seven checked rows. Actual Make's object and ELF equal the prediction;
the conversion CSV is unchanged. The unfinished full-ROM checksum still exits2.

ELF SHA-256 `31b27f58de11cc97b8bbec75317b499a9319b5b8a6e6748ef3564f12dacd845a`;
guard CSV SHA-256 `b53721d727660eca66ed2771ba8fd8597642b08a123168033628a26ff92fd46b`.
Complete receipts are in `conker/build/game-dual-point-motion-1514A594-match/`.

Fresh production is **4,188/5,512 (75.98%)**, Game **3,515/4,839 (72.64%)**,
Init492/492 and Debugger181/181, zero drift. **222 more** at the current
inventory are needed for the4,410-function80% threshold. README changes are
aggregate rows only. The80% goal remains active.

Next audit nearby `func_1514A380`, a70-word Game slot in the fresh linked
list. Preserve the historical screens and reuse unchanged helper contracts.
The smaller handwritten `func_150A76F0` remains in its separate assembly
workstream, consistent with Notes1952/2003; no C credit or source change is
claimed for it.
Graphify receives a scoped refresh with old-node retention, not a claim of
fresh full-corpus extraction. Unrelated sibling edits, private inputs, real
saves, the eight earlier boundaries and frozen host Release remain preserved.
No push or host/hardware/gameplay acceptance is added.
