# Actor Input Movement Recovery And Fitting Boundary

Verified 2026-10-17. Consumer predecessor `53557216`; tools predecessor
`971eddb`. Both active trees began clean. The previous turn banked the owner
burst restoration in [Note1511](1511-owner-burst-emitter-restoration-and-match-20261017.md).
The user resumed the wider Game goal; it remains active on the next complete
routine, not a reduced replacement.

Target: **`func_150F34F4`**, owner `generated_11FF10`, VA
`150F34F4..150F43F0`, ROM `1209A4..1218A0`, **959 words / 3,836 bytes**,
retail frame `0x80`. Its dispatch slot is `0x80086068`, ROM `0x22AB28`.
Production still contains the old zero-return placeholder. **No new C body is
installed, no guards are added, and matching credit is zero.**

## Complete Recovery

`tools/experiments/game_actor_input_movement_recovery.py` contains the complete
typed C candidate and the existing-profile compiler/linker qualification.
`MovementActor34F4` describes the actual `0x32C` record layout;
`MovementInput34F4` describes the four-byte button/signed-stick packet. Thirty-four
native field offsets, both sizes and the 32-bit pointer ABI are checked.
Descriptive field labels are working interpretations, not recovered original
names. Uncertain values retain offset-based names. The function name remains
stable, with a short purpose comment.

All three state paths are recovered:

1. Disabled movement, facing update and linked-record release.
2. Initial controller/heading/speed setup, entry transitions and link acquisition.
3. Active input smoothing and turning, record selection, vertical/acceleration
   limits, linked-record acquire/release, bounded spawn scan, contact transitions,
   provider requests and final animation selection.

The sibling reference draft at
`../Another Source/CBFD-Recompiled/conker/conker/src/game/game_11FF10.c`
was read only as a navigation aid. Its full-file SHA256 is
`ae5183d1c3338523229f12ff81c30ae1a9fc4ff13b6ed200cc4cf9fe380030b9`.
It contains incorrect access widths, float/integer reinterpretations and call
arguments; it is not imported or credited as byte-exact. The retail assembly,
actual linked anchors and direct callee interfaces govern this recovery.

Important corrections independently exercised by the tests include:

- Signed byte stick inputs, unsigned byte states/cooldown, signed facing
  halfword, unsigned heading arithmetic, byte flags and genuine float accesses.
- `func_1505A630(f32, f32, s32)` receives zero as its third argument, not the
  actor pointer. Its first two floats use F12/F14.
- `func_150599C8(actor, u8, u16)` uses integer-register arguments; residual
  F12 content is not another formal parameter.
- `func_1505A3A8(f32, actor, f32, f32, u8)` has five arguments. The adjacent
  live F14 value is not a sixth parameter. Its ignored float return is retained
  in the prototype.
- `func_15059140(actor)` takes one argument. The global-request providers do
  not acquire bogus arguments from residual registers in the draft.
- The 25-record nearest scan keeps every eligibility gate and strict tie
  comparison. The separate 24-record spawn scan preserves its original
  endpoints and count-less-than-five boundary.

Caller-packet evidence is not proof of every original provider formal. For
example, the retail caller explicitly supplies `0.25f` to `func_150585F0`,
although that callee overwrites incoming A1 before reading it. The candidate
preserves that measured packet; it does not claim the ignored slot was an
original source parameter. Unused return values and opaque provider behavior
are not treated as complete callee type/semantic recovery.

The normal owner profile is unchanged. `#pragma intrinsic (fabsf)` follows
existing repository/SDK practice and emits ABS.S; an unresolved library call
is rejected, not assigned a synthetic address. All target bindings use real
production anchors. All eleven raw owner neighbors and owner pools are intact.

## Measured Fit

| Property | Retail | Complete Candidate |
| --- | ---: | ---: |
| Executable words | 959 | 962 |
| Frame | `0x80` | `0x70` |
| Overlapping unequal words | 0 | 811 |
| Extent gap | 0 | +3 words |
| First contact-height store | SP+`0x58` | SP+`0x60` |

The S0 and RA save words already agree exactly at SP+`0x28` / SP+`0x2C`.
That does not establish their entire private lifetime. The contact-height home
is caller-relative -40 in retail and -16 in the candidate, so adjusting only
the frame would not restore the real storage layout.

The real owner padder rejects the candidate's `0xF08` bytes against its
`0xEFC` slot. No executable tail is trimmed and no overflow or frame guards
are proposed. At memory-fault cut zero the complete private states already
differ by the 16-byte SP/frame gap. Public agreement does not remove that
rejection.

```text
Candidate raw SHA256:
704bac447c0f4f30022a305d7f24ec2c315766bfff235294704c1148da1fff3f
Unchanged production ELF SHA256:
245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60
```

## Fresh Qualification

The final **11-test suite passes in 72.175s**:

- 683 complete three-path/boundary cases, 1,283 width/cooldown/table-alias
  cases and 530 record/filter/provider/targeted cases: **2,496 cases** compare
  actual retail, complete candidate and an independently ordered float32 model.
  Complete public bytes, semantic call packets and call-boundary actor/global
  snapshots agree. All 256 stick-byte values and cooldown values are covered.
- Nine effective provider-mutation modes exercise repeated loads and call
  ordering. Fourteen provider interfaces are observed. The actual 21-word
  `func_150F34A0` retail helper executes as connected MIPS, rather than an
  opaque return stub; remaining providers use explicit bounded contracts.
- Two independent text rebases pass twelve additional complete cases with
  real external bindings. These are text rebases, not data-carry qualification.
- Twenty additional FP-edge cases cover signed zero, infinities, NaNs and
  large values in the nontrapping model. Native invalid signed conversions,
  general FCSR behavior and hardware acceptance remain unqualified.
- Eight complete compiled guest negative controls catch signed stick/yaw,
  angle/acceleration ABI, nearest tail/tie, spawn limit and contact equality
  errors. Eight native controls fail semantic gates 42/44, not crashes.
- Native32 O2/O0, UBSan, **130 complete cases per profile**, full actor/table/
  controller bytes, scalar globals, semantic call packets, and provider
  command/gate snapshots all pass. Guest table aliases are not presented as
  native alias or private-stack qualification.

The full-run retail coverage is **947 executed words**. The other twelve
original words each follow an unconditional branch and its delay slot, have
no direct incoming target or call-return site, and there is no internal indirect
jump. A separate static check proves this scoped unreachability. They are not
deleted or excluded from later literal byte matching.

The first native harness run faulted at a newly owned executable's unaligned
SSE MOVAPS in its final-call recorder. GDB established that exact instruction;
the existing native-test `-mstackrealign` setting fixes the freestanding entry
alignment. This was a harness issue, not a production failure. The final suite
above includes both corrected native profiles. Four final EOF-only cleanups
preserve the exact Python ASTs and embedded C strings; AST/pair checks pass.

Receipts and complete generated C/objects remain ignored under
`conker/build/game-actor-input-movement/`: `candidate-audit.json`, `core.json`,
`widths.json`, `records-mutations.json`, `negative-controls.json`, `rebases.json`,
`private-gap.json`, `native.json`, `FP-edges.json`, `static-dead.json` and
`production.json`.

```sh
python3 -m tools.experiments.game_actor_input_movement_recovery
python3 -m unittest tools.tests.test_game_actor_input_movement_recovery -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Preserved Production And Banking

All **284 protected entries / 261 paths** remain byte-identical, including the
entire ELF, source, guards/profile/conversion manifests and older immutable
checkpoints. All 6,057 bodies and all 189,088 Game-data bytes / 720 owners are
audited. The dispatch-table word remains unchanged. No normal production
rebuild is needed or claimed for this uninstalled work.

Fresh totals remain Game **2,965 / 4,828 (61.41%)**, total
**3,638 / 5,501 (66.13%)**, 1,863 still different and zero drift. Init 492/492
and Debugger 181/181 remain exact among converted functions. Root README is
unchanged; this narrative belongs in the working docs.

Tools **6f22514** is committed before the consumer docs/pin. Both local tools
copies pass twelve shared tests and smoke checks, eight ASCII/AST parses and
four byte-identical task pairs. All four mirror destinations were absent;
all 1,146 prior hashes and mirror HEAD `ddbdd16b` are preserved, with 1,150
dirty paths afterward. No mirror commit/reset, push, dependency installation,
Claude call, host-port change or frozen Release action. Earlier unchanged
burst/neighbor suites are reused prior receipts, not freshly rerun suites.

The existing incremental graph rebuild succeeds without a force override:
42,239 nodes / 82,373 edges / 3,950 communities. Retained nodes from still-existing
excluded files are preserved; HTML is skipped at the existing graph-size limit.
The previously diagnosed full-scan shrink rejection is not retried or bypassed.

## Continue The Same Function

- [x] Recover the whole state machine and actual width/sign/call contracts.
- [x] Qualify complete public behavior, actual curve execution, mutations,
  native32, effective controls and the full production-preservation boundary.
- [x] Expose the literal extent/frame/private rejection without granting credit.
- [ ] Trace the CFE/UOPT/UGEN local area and contact-height/scalar homes; recover
  retail frame `0x80` and real caller-relative storage without fake parameters,
  inert padding or frame/address word rewriting.
- [ ] Resolve the three executable excess words, then actual register roles
  and scheduling. Require all 959 literal words, private/fault-prefix behavior,
  appropriate data/call rebases and the complete first-image audit before
  installation. Preserve the twelve original unreachable words.
- [ ] Keep the 139-word gate, both fade lifetime gaps, full opaque caller/
  provider/runtime acceptance and wider Game goal open. Do not switch to
  `func_150F43F0` while this routine's fitting work is pending.
