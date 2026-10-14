# Game Actor Effect Packet Guarded Match

Verified locally: 2026-10-14. Continue Game matching from
[Note 1356](1356-game-actor-burst-contact-direct-match-20261014.md).
This installs the complete routine, not a simplified effect substitute.
Retail guest-code matching is not complete host gameplay or hardware acceptance.

## Target And Inputs

- `func_151A7610`, owner `conker/src/game/generated_1D43B0.c`.
- VA `151A7610..151A77C0`, ROM `1D4AC0..1D4C70`.
- Complete 108-word / 432-byte slot, frame `0x98`, existing O2/g3/MIPS2 profile.
- Starting consumer `f2c25ff9`, tools `bb793d8`; both active trees clean.
- Tools `fc195e3fb3271f486462a67941fb6fb87e90d8e0` committed first.
- Before ELF `205c023e2ffa29a90d7204bb8eb260989590a4ea30f268e916cd252f88d21708`.
- Installed ELF `4e8749bc86fc0700b3236924fcf7c087d3f741cd969d632a70482e34ab320df4`.
- Installed owner `5f432d87c5f118ce25394052b3b93691a6a1498874d882113f919a191b2483d7`.
- Installed guards `b306d18dd3d933fac33a2575a20c704f928c1c00e079bb445c54e62a0c22c6ff`.

Reuse the verified before snapshots in
`conker/build/game-actor-effect-packet-match-test/`. Preserve the original
assembly, factory, table data, layout, Makefile and complete conversion CSV.
Reuse the owner-local vector type and existing RNG declarations. Add only four
float globals and the narrow effect-factory declaration; replace this one
zero-return placeholder with its complete void routine.

## Complete Semantic Body

The incoming ABI is six float words followed by an actor pointer: X/Y in
F12/F14, Z and direction X in A2/A3, the other directions and pointer on the
stack. Retain actor field `40` before any RNG callback. Preserve the initial
position snapshot and all three private vectors.

Make three float RNG calls followed by two unsigned integer RNG calls. After
the first float sample, read the live world multiplier and coefficient:
`speed = (sample * 166 + 160) * D_800A8DC8`. Each velocity component is the
negated incoming direction times the world multiplier, then speed. Keep both
rounded multiplies, their operand order, and NEG.S before multiplication.

Use the second/third float samples for strength and lifetime. Strength is
`(sample * D_800A8DCC + -600) * D_800A8DD0`; lifetime is
`(sample * 500 + 400) * retained`. Counts use unsigned `%21 +15` and `%101 +100`.
Late actor bytes `C` and `1` remain live after the integer callbacks.

Submit all 17 factory arguments: position/zero/velocity vector pointers,
scale 1, strength, lifetime, both counts, then 15/20/0/-1/56/27/0 and the two
actor bytes. The `56/27` shorthand means hexadecimal `0x56/0x27`; the other
listed integers are decimal. No extra narrowing or return assignment is added.

## Source And Guard Boundary

The initial body emits 108 words/frame `0x90`, 40 differences. Distinguish the
initial float sample from the later one and order real, used declarations to
recover frame `0x98` and hexadecimal private homes: position `8C`, zero `74`, velocity `80`,
retained scalar `6C`, later floats `58/5C`, first integer `60`.

Write the negative literal as addition, preserving retail ADD.S rather than a
positive constant and SUB.S. The selected complete source then differs only in
one closed F2/F12 allocation cycle. Eight natural product forms retain that
same eight-word difference. Other profiles are worse: O2 16 differences,
O1/g3 121 words/116 differences, O1 121 words/118 differences.

Eight existing-format expected-word guards exchange only those two floating
registers at offsets `034/070/078/080/088/094/09C/0A4`. The `034` LWC1 guard
retains `R_MIPS_LO16:D_800BE9A8` on both sides. Its HI16 and every other
relocation remain fixed. There is no inserted/omitted instruction, profile
change, invented volatile access, inline assembly, dummy local or new core
normalizer. The raw C remains eight words different; only the guarded linked
result is byte-exact across all 108 words.

## Verified Gates

Pre-install qualification passes **10 checks in9.655s**. The combined installed
effect/contact/consumer match/recovery/producer/protected-text run passes
**77 checks in232.619s**. Complete bounded signed-DIV HI handling in the new
local oracle, making the signed control effective in guest as well as native;
the final ten effect checks pass **11.706s** after that test-only refinement.
Both tools copies pass project smoke and Windows byte-compilation.

- Both actual padders match all108 words and the432-byte extent. Independently
  assembled retail and both objects agree at four entries, including three
  independent rebased links with all four data symbols crossing HI/LO carries.
- **32 fired stale-word/relocation rejections** cover every guard in both
  padders. All relocation ownership and all original guard bytes are preserved.
- **128 guest domains** cover float tapes, high-bit integer words, callback
  mutations and two SP phases. Raw C matches the independent 23-value packet
  and six-call reference; guarded complete modeled states match retail.
  Every108 word executes. Saved F20..F31 and SP survive all callbacks.
- **376 fired root-access pairs** preserve all modeled prefix state, PC and
  branch-delay state. **32 fired alias prefixes** cover public input and three
  private actor aliases. A fired raw-C prefix exposes the F2/F12 mismatch;
  return/call agreement alone would not justify direct matching.
- **96 native32 cases per O2/O0 profile** check all23 packet values and callback
  order, including signed-zero directions. A signed-remainder source control
  fails both guest observation and native packet checks for high-bit input.
  Five other complete semantic controls are also effective.
- Six owner neighbors, complete raw words, relative relocations, normalized
  pools and warning statements stay fixed. Both full-owner padders retain the
  completed315-word consumer, direct117-word contact and ten prior guards.
- **16 connected cases** execute the unchanged original157-word
  `func_151A26EC` and real11-word memcpy across allocation failure/success.
  Retain three float/four integer calls, one allocation and zero/two copies.
  Both payload copies and complete modeled states agree; allocator/RNG remain
  bounded hooks.
- Authentic `D_80089AFC[1]` at VA `80089B00` / ROM `22E5C0` points to this
  routine. Its table data remains exact. An enclosing retail dispatcher has not
  been identified/qualified, so do not call this a connected dispatcher test.
- Seven current image/source/raw-guard corruptions and one malformed baseline
  symbol-size control fail, with no metadata exclusions or reset snapshots.

Native private-home aliases, full RNG/allocator implementations, all NaN or
extreme FP arithmetic, hardware FCSR/rounding/EPC/BD and gameplay are not claimed.

## Closed Image And History

The completed3,261,160-byte ELF changes exactly **353 bytes**: **351 instruction
bytes** and **two symbol-size bytes**, 12 ->432. No symbol-record/string
permutation occurs. Every undeclared ELF byte stays fixed, despite the shared
guard manifest causing many other objects to rebuild.

The CSV retains every prior byte and appends exactly **1,090 bytes** for these
eight rows. The existing mixed line endings and Git CRLF warning are not
changed here. Parsed guard logic is unchanged; raw-prefix checks remain enabled.
The older audit suites retain their original pinned snapshots and apply only
the asserted effect slot/size and exact guard suffix, following the prior
consumer/contact changes. No broad tolerance, pin reset or disabled control.

Protected data remains exact:189,088 bytes /720 owners, zero different bytes or
owners. The conversion CSV retains
`14d100143c0654609b3cd7d97798dbeccd52551a77ad6b4ff1f826acde91482b`.
Fresh Game **2,835/4,823 (58.78%)**, total **3,508/5,496 (63.83%)**,
different **1,988**, drift **0**. Init492/492 and Debugger181/181 remain exact;
converted counts do not change. Root README changes only aggregate rows.

## Banking And Next Work

The independently dirty older tools mirror stays at `ddbdd16`. Verify all464
starting fingerprints, copy only six owned modules, and preserve all460 other
fingerprints. Four prior modules change and two are added, leaving466 dirty
paths without resetting or duplicating its history. Bank tools before the
consumer pin. No push, dependency installation or REA configuration work.

Read-only sibling audit: `64CBFDOGL/recomp_out/.c:1240581` still has this routine
as a zero-return placeholder. That selected generated source and CMakeLists
are independently dirty. Leave them unchanged and track a separate PC-port
transfer/host-qualification task. No host build/launch or frozen Release work
occurs; this checkpoint does not claim a PC effect/gameplay fix.

Next recover `func_151A77C0` in the same owner: VA `151A77C0..151A787C`, ROM
`1D4C70..1D4D2C`, 47-word leaf. It remains a zero-return placeholder beside the
related recovered `func_151A787C`. Keep all completed routines exact. The wider
Game matching goal remains active.

```sh
python3 -m unittest tools.tests.test_game_actor_effect_packet_match -v
python3 -m unittest tools.tests.test_game_actor_burst_contact_match -v
python3 -m unittest tools.tests.test_game_actor_burst_consumer_match -v
```

## Post-Bank Verification

Consumer `1b0135da` banks the restoration and tools pin. Eight fresh post-bank
checks pass **14.301s**: actual emitter padders/carry links, emitter image and
corruptions, contact image, consumer image/serialization, producer image and
protected-text corruptions. Both active trees are clean after that commit.

The full graph update refuses an18,914-node replacement of the40,681-node
corpus. Keep the existing graph; do not force it. The restoration commit's
incremental hook finishes **40,691 nodes /81,169 edges**, preserving19,398 nodes
from2,972 excluded but present files. No worker remains. The root graph does
not prove coverage of the submodule's new tools; their direct tests do.
