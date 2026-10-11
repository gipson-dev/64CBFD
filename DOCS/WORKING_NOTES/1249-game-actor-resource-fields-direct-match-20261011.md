# Actor Resource Fields Direct Match

Verified 2026-10-11. Consumer baseline
4d05f02f69457fa18693ea3d5c2e57d83f0acc97; mounted tools baseline
a9694bd84dbfcb35be65ffe696e48ebb319a3fc3. New tools
83ade717bd246c6a2087055d73d8064c3a485399 committed first. No push.
Single Codex writer, zero Claude calls; follow DOCS/AGENT_WORKFLOW.md.
Previous goal turn made progress by banking the complete constructor match.
This checkpoint finishes the next complete routine, not the wider Game goal.

## Complete Recovery And Direct Match

Recover func_150839B8, VA 0x150839B8..0x15083AC8,
ROM 0xB0E68..0xB0F78. All 68 words / 272 bytes emit directly from semantic
C with the original 0x18 frame, seven relocations and no new guards or pools.
The original leaf zero-return placeholder had a 12-byte ELF symbol extent.
Its recovered signature is void (u8 *actor, s32 identity, u8 *configuration).
Both complete retail call sites, in func_15082A44 and func_15083AC8, ignore
the return value. Remove the obsolete local s32 declaration; no other callers,
adjacent helper bodies, compiler profiles or guard rows change.

- Compare the complete identity word with 255 before any actor/resource/
  configuration/world access. Non-sentinel resource indexing retains the
  original low-word pointer arithmetic and cached resource pointer.
- With configuration, read its unsigned halfword at +0x2C: zero copies the
  resource halfword +0x2A, one clears actor +0x10, otherwise copy the value.
  Only this branch subsequently reads world; world 0x1D overrides +0x10
  with 1000. Without configuration, clear the field without reading world.
- Preserve ordered byte/word/halfword copies to +0x13B, +0x2CB, +0x2CC,
  +5, +0x68, +0x69 and +0x160, including retail's signed LB/LH producers.
  Field names remain offsets because this work does not establish their
  broader resource-schema meaning.
- Nonzero resource byte +4 selects D_80086CAC[resource[5]] for actor +0x2C4.
  Reload resource +4 after that store, write actor +0x2C8, then reload the
  actor byte before resource +0x38 and truncate their sum into actor +0x2C9.
  Zero resource count leaves the existing +0x2C4/+0x2C8 fields untouched.
- Nonzero resource +0x29 calls the existing void func_15036C70(actor) after
  all fields. Do not invent a synthetic NULL resource guard or return value.

The initial complete candidate already had all 68 words and the right frame;
only three LBU schedule words differed. Reversing the commutative final
addition's source operands makes IDO emit the retail actor-first load order,
including the likely-branch delay load. No scheduling patches are required.

## Fresh Qualification

Nine final tests pass after installation (17.097 seconds). Receipts and
immutable source/ELF/guard/progress/rodata/symbol/undefined snapshots are in
conker/build/game-actor-resource-fields-test/. Both shared tools checks pass.

- 7,962 independent-reference cases / 15,924 complete retail/C guest runs:
  all identity/count bytes, NULL configuration, halfword boundaries, world
  gate boundaries, high/full-word identities and two stack phases. Reach 67
  retail words; the duplicate SH at offset 0x54 is unreachable through the
  routine's branches. All 68 words are verified statically. Sentinel 255
  accepts unmapped actor/resource/configuration/world without accessing them.
- 43 alias cases and 1,265 fired complete-access fault pairs / 2,530 failed
  runs compare full partial memory, ordered reads/writes and calls. Qualify
  resource/configuration aliases into the actor and private stack, callback
  writes, world alias read after the halfword store, resource-table caching,
  pointer-table aliasing and count reload after an overlapping pointer store.
  Each fault gate is confirmed to fire. Guest instruction fault order is not
  a claim about portable C fault semantics.
- Nine independent original/C/padded links at three symbol sets, 15 cases /
  45 runs. All three global HI16/LO16 pairs and the helper call are independently
  rebased across signed low-half carry boundaries. Original assembly, raw C
  and actual production padding agree at each entry and symbol set.
- Actual production preprocessing, compilation, post-processing and padding
  of before/after copied owners preserves all 30 neighbors' bytes, extents,
  relocations and normalized pools. No diagnostics. The full matched
  constructor compiler fingerprint and every existing guard remain valid.
- Nine freshly compiled effective IDO negatives distinguish full-word
  sentinel, default halfword, value-one gate, world override, source field,
  live count, sum, helper gate and reversed commutative load order. The last
  negative changes access order even when ordinary final bytes agree.
- 32 cases / 64 executions connect the complete actual matched 182-word
  constructor to original/C initializers. Confirm 32 real initializer calls
  per form with full memory, events, calls, GP and FPR equality. Deep resource
  transition, allocation/initialization and final animation callbacks remain
  bounded models; this is not full allocator/gameplay acceptance.
- Native32 O2/O0 each pass 8,192 independently modeled cases, 16,384 total,
  including resource self/offset aliases and configuration aliases. Width
  assertions verify 32-bit pointers/integers and 16-bit halfwords. One native
  semantic negative fails. Wrapped guest addresses and fault order are not
  inferred from native tests; strict aliasing remains disabled as in the
  existing decomp harness.
- Whole linked audit below passes with unchanged guards/conversion rows.

Fixture corrections before the final run: use no guards for the isolated
one-function padder, and the full historical manifest for copied owners;
reuse the existing CopyOracle signed-LB instruction handler locally rather
than modifying the shared interpreter; map the constructor's high-identity
resource entry explicitly; correct the baseline leaf symbol extent to its
measured 12 bytes. These were harness issues, not source regressions.
Historical unchanged-neighbor and constructor-private qualification receipts
are reused on the freshly proved byte/fingerprint basis, not called new tests.

## Installation Audit

Only 217 ELF bytes change, confined to this 272-byte slot and its 12 -> 272
ST_SIZE update. Every other ELF byte and metadata entry remains exact.
ELF 3,261,160 bytes, SHA-256
cc415433f08ef935143e9f04bab77402be7b66009b7712b0d909a4e3318115c5.
Protected data 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
New owner 11,050 bytes, SHA-256
686fd368af31cecf307728edd37377ce6ec34f35285b4deb9f011beeb9b2239a.

Guard manifest stays byte-identical at 1,940,850 bytes, SHA-256
5e50f8952c0e5d4ba39b7e9054b7ac5727517d021ba8e92d3b10c8a2f07b2f19.
Conversion CSV stays 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.
Rodata, symbols and ignored undefined assignments remain byte-identical.
Fresh linked rebuild succeeds; duplicate generated_12D630 recipe warnings
remain. Root README gets two aggregate matching rows only.

Fresh Game matching 2,781/4,821 (57.69%), total 3,454/5,494 (62.87%),
zero drift / 2,040 different: +1 matching, no new converted credit. Total
converted remains 5,494/6,043 (90.92%); Init 492/492 and Debugger 181/181
already-converted functions remain exact.

```sh
python3 -m unittest tools.tests.test_game_actor_resource_fields -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Older standalone tools HEAD ddbdd16 stays unchanged: 267 existing dirty
entries plus two absent-only byte-identical new mirrors = 269. No existing
older paths overwritten or committed; protected helper hashes remain exact.
Native Graphify query found 33 nodes, showed 22 and explicitly truncated 11.
Native update exits 1, refusing unsafe shrink 39,650 -> 17,868 nodes and
retaining 19,398 nodes from 2,972 excluded-but-existing files. Preserve
skill 0.9.20/package 0.9.26 and devcontainer.json zero-node warnings; no
force, purge or install. Require fresh post-commit log growth/Rebuilt tail
and zero actual workers before reporting clean. No OGL/Release, saves,
editor state, private inputs or broad conversion batch changed.

## Next

Recover complete 51-word func_150838EC in the same owner,
VA 0x150838EC..0x150839B8, ROM 0xB0D9C..0xB0E68, original frame 0x28.
Its current body still returns zero. Inspect the resource-presence and
unsigned-count table gates, all four incoming argument homes, actor +0x2D0
store before the allocation NULL check, failure return one, 0x40-byte clear
and func_1505E650 delegation with three zero float arguments. Derive the
fourth incoming float/raw O32 word contract before changing its declaration
or the constructor call; do not numerically convert its forwarded bits.
Preserve this direct initializer and the constructor's complete guard
fingerprint. Timeline matching and actual deeper resource/allocator/hardware/
renderer/gameplay acceptance remain separate open work.
