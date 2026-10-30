# 1850: Accelerated motion update match

Date: 2026-10-29. Target `func_150CCCB4`, owner `generated_F9430`.
Body VA `0x150CCCB4..0x150CCD88`, ROM `0xFA164..0xFA238`: **212 bytes /53 words**.
The complete classifier slot extends through ROM `0xFA240`; two existing zero
alignment words remain outside the function body.

The zero-return placeholder becomes
`s32 func_150CCCB4(GeneratedF9430KinematicObject *object)`. The local96-byte
view names rotation at+0x20/+0x24/+0x28, position at+0x38/+0x3C/+0x40,
velocity at+0x44/+0x48/+0x4C, angular velocity at+0x50/+0x54/+0x58 and
vertical acceleration at+0x5C. It always returns1.

Position X/Z advance by velocity times timestep `D_800BE9A4`. Position Y adds
`velocityY*dt + ((acceleration*dt)*dt)*0.5f` using the original single-precision
association. Vertical velocity then adds acceleration*dt; each rotation adds
its angular velocity times dt. The timestep is read again after stores.
Acceleration and the original vertical velocity retain their original cached
values. The source uses complete semantic C and a typed object view; all53
words and both relocations emit directly with the existing O2/g3 profile.

The routine is a leaf: no stack frame, stack accesses, saved registers,
incoming homes, outgoing homes or helper calls. No guards, insertions,
omissions, frame adjustments, shared-header or compiler-profile edits.
The guard manifest, conversion CSV and all pre-existing neighbor guards
remain unchanged, including the earlier motion-threshold recovery.

- Eight fresh canonical methods pass independently in both tools copies,
  plus shared checks. Production reruns two installed methods per copy;
  six unchanged semantic checks are reused only by complete fingerprints.
  The older mirror retains1,988 inherited dirty paths with exactly three
  new qualification files, without a mirror commit.
- An ordered symbolic expression/store graph equals the original for raw,
  padded and retail objects. It keeps operand order, all single-precision
  operations, saved inputs, timestep reloads and possible global/record
  alias effects. Changing the half-acceleration factor rejects both the
  exact payload and the symbolic graph.
- Guest: **2,016 cases /6,048 original/raw/padded executions**, literal
  full-state agreement and all53 words covered. Timestep aliases each of
  all13 float fields in guest and native tests, including the output cells
  whose stores change later timestep reads. Inputs cover positive/negative
  zero, fractions, finite extremes, subnormals, infinities and quiet NaNs.
  There are81 access-prefix comparisons, nine sparse executions using only
  the required fields/global, and three layouts /108 rebased cases.
- Native32 O0/O2/O3 each pass **1,008 cases with UBSan**, strict alias
  assumptions disabled and FP contraction disabled. Native output NaNs are
  compared by class, while other bits and untouched memory must agree;
  native NaN payload identity is not claimed. Eight controls reject: wrong
  half factor, cached timestep, omitted velocity update, wrong angular rate,
  wrong acceleration field, wrong return, missing timestep factor and
  swapped X/Y position-store order.
- Full-ROM scan finds no direct JALs and one aligned pointer at ROM
  `0x22E37C` / VA `0x800898BC`: **`D_800898B0[3]`**. Original dispatcher
  `func_151321D0` is in `conker/asm/15F680.s`; its C body remains a separate
  stub. Owner byte+0x71 selects the movement callback. The13-word window at
  VA `0x15132244` / ROM `0x15F6F4` executes96 cases, including48 zero-index
  skips. It passes owner in A0, saves/restores the caller flag at SP+0x23,
  and uses the target's nonzero result to retain that flag. Earlier gates
  and later callbacks remain preconditions; no complete parent/gameplay
  execution or new parent matching credit is claimed.
- Complete-owner compile/padding preserves five neighbors and pools. Three
  actual Make commands reproduce the exact object with zero C diagnostics;
  the inherited duplicate-recipe Make warning remains. All214 raw-byte/
  binding controls and240 whole-image corruption controls reject.
- Independent prediction equals production: **158 changed bytes =157
  target-code bytes +one symbol-extent byte**, zero metadata changes or
  exclusions. Symbol size becomes212; the eight alignment bytes remain.
  All6,055 other linked bodies and all function addresses remain fixed.
  Protected Game data stays exact across189,088 bytes /720 owners.

Fresh adopted-ELF count: **3,927/5,506 (71.32%)**, Game **3,254/4,833 (67.33%)**,
Init492/492 and Debugger181/181, zero drift. **203** more to4,130.
Tools committed first: `0984a15a03ff80d4ab7e0a1d97fabe402e567ee1`. No push. Root README gets aggregate rows only.

The scoped eleven-file AST refresh retains or uniquely relocates all50,110
prior nodes and preserves all103,891 old directed relationships. The s32
return interface remains; no old edge retires. Actual dispatcher/table,
leaf ABI, typed fields and ordered floating operations are annotated.
Outside manifest rows and analytics remain historical; no full-corpus claim.

Artifacts: `conker/build/game-accelerated-motion-update-match/`. Next screen
`func_151A084C` still needs full qualification. Other private candidates remain
uncredited. Hardware FCSR, exception modes and hardware NaN payload behavior
are outside the bounded arithmetic model. No host-port, frozen Release,
save/editor, private-input or memory changes. Zero Claude calls. The75%
matching goal remains active.
