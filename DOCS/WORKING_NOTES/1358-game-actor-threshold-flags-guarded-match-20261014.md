# Game Actor Threshold Flags Guarded Match

Verified locally: 2026-10-14. Continue from
[Note 1357](1357-game-actor-effect-packet-guarded-match-20261014.md).
This restores the complete routine, not a simplified sibling substitute.
Retail guest-code matching does not establish host gameplay or hardware parity.

## Target And Baseline

- `func_151A77C0`, owner `conker/src/game/generated_1D43B0.c`.
- VA `151A77C0..151A787C`, ROM `1D4C70..1D4D2C`.
- Complete 47-word / 188-byte leaf; no frame, calls or literal pool.
- Starting consumer `38ef91d1`, tools `fc195e3`; preserve all completed routines.
- Before ELF `4e8749bc86fc0700b3236924fcf7c087d3f741cd969d632a70482e34ab320df4`.
- Installed ELF `294eba92c9b31ea335a560d67f8536a30993fc1fa429796df1c486fb532f7ddd`.
- Installed owner `689989a2794328712335b2967cc76509312440e851e86a76b13dbf5f5fd85e7a`.
- Installed guards `59473e88b9a02be589d8c72465716753aa8802f1908cba79b771f2c8fbf952d0`.

Reuse the immutable before snapshots under
`conker/build/game-actor-threshold-flags-match-test/`. Replace only this
zero-return placeholder. Reuse the existing global declaration and raw actor
pointer pattern; add no type, declaration, inline assembly or compiler profile.

## Complete Semantics

The assembly observes A0 as the actor pointer. Its parameter block starts at
actor `50`; the state at `38` and all three thresholds are signed halfwords.
The surrounding related updater supplies the void callback source pattern;
the actual enclosing dispatcher has not been identified.

Preserve all three strict-less gates. Below parameter `54`, write the low byte
of state times signed factor `56` to alpha `3F`. Below parameter `58`, multiply
signed factor `5A` by the full clock word `D_800BE9E4`, cache both signed axes
`34/36`, add with 32-bit wrapping and store the low halfwords in that order.
Reload state `38` after both stores.

Below parameter `50`, read flags `44`, set byte `2F` to `15`, OR flags with
`201`, load signed factor `52`, and multiply by the reloaded state. Write word
`14` as `000C000F` while MULTU is pending. Store the low product byte to colors
`42`, `41`, then `40`. This conditional flag/word/color group differs from the
related `func_151A787C`; do not transplant its unconditional color tail.

Unsigned delta/intensity locals make modulo-32 multiplication and additions
explicit without changing the emitted operations. Native halfword narrowing
is tested on the actual compiler; universal C-platform alias/endian behavior
is not claimed.

## Source And Guard Boundary

Selected O2/g3 semantic C emits all47 words with no frame or warnings and26
raw differences. Nine initial source forms and eight lifetime forms explore
flags order, register locals, explicit additions and unsigned product syntax.
Some flags-first forms reduce the count but change source write order; retain
the retail byte-first shape. O2 also has26 differences; O1/g3 and O1 expand to
65 words/frame10 with65 differences. Keep the existing O2/g3 profile.

Append26 existing-format expected-word guards. They close the GPR allocation,
commutative MULTU operand order, and the six-site value reload/MFLO/axis-store
schedule. Raw C hoists the state reload; fault prefixes expose the difference.
Both actual padders reject stale words and relocations. No instruction is
inserted or omitted, and no relocation is moved or owned by these guards.
The clock HI16 at `00C` and LO16 at `044` remain unchanged.

Only the guarded linked result is byte-exact; the raw C remains26 words
different. These guards do not turn an empty source body into retail code.

## Qualification

The complete installed threshold/effect/contact/consumer match/recovery/
producer/protected-text regression passes **86 checks in259.248s**. Both tools
copies pass project smoke and Windows byte-compilation; repository setup
passes all three checks. Tools `166a171944b9577e33feeefbda27108beced89f3`
are committed first, before the consumer pin. No push.

The corrected pre-install suite passes9 checks in21.169s. Its first pass
identified two test-fixture defects: a flag control began with the changed
bit already set, and the native harness failed a formatting warning. Correct
the fixtures rather than weakening the checks.

- Both real padders match47 words/188 bytes at the retail entry and three
  independent rebased links. Independently assembled original code agrees,
  including the clock HI/LO carry cases and relocation ownership.
- 104 fired stale-word/relocation rejections cover all26 guards in both tools.
- 640 guest domains cover signed boundaries/equality, four threshold sets,
  five clock words, seeded signed factors and two SP phases. Raw C agrees with
  the independent final-memory reference; guarded complete states agree with
  retail, including HI/LO. All47 words execute; no callback or frame is added.
- 819 fired root-access prefix pairs preserve complete modeled state, actual
  instruction PC and modeled branch-delay owner. Forty public alias domains
  overlap the clock with actor word/axis/state/alpha/color/flag/parameter
  storage. Thirteen raw-C prefix mismatches witness the allocation/schedule
  boundary. No hardware EPC/BD or native mixed-width alias acceptance claim.
- Native32 O2 and O0 each pass524,288 cases: every signed state, four threshold
  sets and two high-bit clock words. Full128-byte records agree, including
  untouched bytes. A compiled unsigned-threshold control fails. Six guest
  semantic controls also fail: equality, signedness, alpha destination, flag
  mask, final gate and fixed word.
- Six owner neighbors retain all raw words, relative relocations, normalized
  pools and warning statements. Both complete-owner padders preserve the
  prior34 owner guards, including the consumer and effect allocations.
- Seven current image/source/guard corruptions and one malformed baseline
  size are rejected. Original historical snapshots stay pinned; extend older
  audits only by the exact new slot/size and guard suffix. No reset or broad
  metadata tolerance.
- Authentic `D_8008C9C8[20]`, VA `8008CA18` / ROM `2314D8`, points here and
  remains byte-exact. This is table provenance, not a connected dispatcher test.

## Closed Image And Fresh Progress

The complete ELF changes132 bytes:131 instruction bytes and one symbol-size
byte, 12 ->188. No symbol/string serialization change occurs; every other
ELF byte remains fixed after the shared manifest rebuild.

Preserve the entire prior raw guard prefix and append exactly3,926 bytes for
the26 rows. Existing mixed line endings are deliberately unchanged. Protected
data remains exact:189,088 bytes /720 owners, zero differences. The conversion
CSV stays `14d100143c0654609b3cd7d97798dbeccd52551a77ad6b4ff1f826acde91482b`.

Fresh Game **2,836/4,823 (58.80%)**, total **3,509/5,496 (63.85%)**,
different **1,987**, drift **0**. Init492/492 and Debugger181/181 remain exact;
converted counts do not change. Root README changes aggregate rows only.

## Banking And Next Task

Bank the tools before the source/guard/docs/consumer pin. The independently
dirty older tools mirror stays at `ddbdd16`: verify all466 starting path
fingerprints, copy only seven owned modules and preserve the461 unrelated
fingerprints. Five existing modules change, two are added, leaving468 dirty
paths. Do not reset or duplicate its history. No push or configuration work.

Read-only sibling check: `64CBFDOGL/recomp_out/.c:1240803` still defines this
routine as a zero-return placeholder. That selected generated source and
CMakeLists are independently dirty; leave them unchanged and track a separate
transfer/host-qualification task. No host build, launch or frozen Release work.

The user's next task, after this function and its commit, is a read-only
byte-match audit of `Another Source/CBFD-Recompiled/conker`. Treat it as another
source only; do not import or adopt anything before measuring the actual match.
The wider Game backlog is not complete.

The full graph update refuses an18,915-node replacement of the40,692-node
corpus. Preserve the existing graph and use the incremental commit hook;
do not force the smaller replacement. The root graph excludes the tools
submodule; direct tests establish their coverage.

```sh
python3 -m unittest tools.tests.test_game_actor_threshold_flags_match -v
make -C conker build/conker.us.elf NON_MATCHING=1 -j4
make -C conker match-progress NON_MATCHING=1
```

## Post-Bank Verification

Consumer `41dfe733` banks the complete function and tools166a171 pin. Eight
fresh post-bank image/padder/corruption checks pass32.538s. Both active trees
are clean at that bank. The incremental hook completes40,702 nodes /81,179
edges while preserving the excluded-but-present corpus; no worker remains.
The next requested audit is completed separately in
[Note 1359](1359-alternative-source-byte-match-audit-20261014.md), adopting no source.
