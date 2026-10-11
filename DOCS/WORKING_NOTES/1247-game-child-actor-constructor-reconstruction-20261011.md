# Child Actor Constructor Reconstruction

Verified 2026-10-11. Consumer baseline
1e724fc8bf714b24f54ea82dd1a3eb8f4a1560a8; mounted tools baseline
672c03d84c6a2d45abb7f8a2b33dca0ed94e2d50. New tools
03d8ec2b8febcaab87d10cdcfec59f687e1c2d01 committed first. No push.
Single Codex writer, zero Claude calls; follow DOCS/AGENT_WORKFLOW.md.
This is complete semantic recovery, not a byte match or gameplay acceptance.

## Complete Recovery

Replace func_15083AC8's typed nine-argument zero-return placeholder in
conker/src/game/generated_AEB40.c. Original VA 0x15083AC8..0x15083DA0,
ROM 0xB0F78..0xB1250, 182 words / 728 bytes, frame 0x38. Full semantic
C fits the 182-word slot, emits frame 0x50 under existing IDO O2/g3 and
still has 125 linked word differences. No new word guards, profile changes,
source padding, handwritten replacement or extra matching/converted credit.

- Recover identity preparations, unconditional actor acquisition, signed
  wrapping actor/parent slot division by 0x32C, kind/value/attachment fields,
  one-based parent slot and ordered status initialization.
- Preserve all three flag-byte writes and clear only bit 0x10. Preserve the
  repeated parent+0x1DE read and six ordered byte copies. Volatile destination
  accesses retain retail's status-store fault prefixes; this does not assert
  portable C behavior for arbitrary invalid addresses.
- Recover the four independent inherited-scale/default-1.0 fields. Preserve
  the live incoming identity/value/flags/inherit homes, cached flags after
  their final reload, optional word+0xF8 bit 0x4000 and unsigned resource
  magnitude times scale at +0x270. Read the magnitude before destination scale.
- Recover the inclusive, callback-mutable signed D_80082FA0 allocation limit,
  +0x304 four-byte output cursor, preceding-slot +0x300+i*4 test, conditional
  +0x301 set without clearing, and unconditional +0x314 allocation result.
  Do not clamp counts or invent an allocation NULL gate.
- Preserve cached D_800C35EA==1, temporary D_800C3638 clear, final restore to
  exactly 1 rather than its previous value, three final helper calls and
  returned actor pointer. Late state/scale incoming homes remain live.
- Keep both adjacent helper placeholders byte-identical. func_150838EC's
  float is forwarded as its raw fourth O32 word rather than default-promoted
  double; the explicit comment documents why that still-unrecovered helper
  retains its old declaration. A future typed helper body must preserve this
  ABI. Native tests use the existing decomp no-strict-aliasing convention.

Initial complete candidate emitted 180 words / frame 0x48 with 167 differences,
but reordered public stores/scale reads. Ordered-access recovery initially
exposed 183/185-word forms; separate masked-bit lifetime and raw scale-word
forwarding produce the qualified full 182-word form. It is not installed as
a byte match merely because its length fits.

## Qualification

Nine final tests pass after installation and the linked rebuild. Immutable
baseline snapshots and generated receipts live in
conker/build/game-child-actor-constructor-test/; experiments in
conker/build/game-child-actor-constructor/. Historical neighbor checkpoints
are preserved rather than rewritten for this new ELF.

- 2,224 cases / 4,448 complete retail/raw guest executions against an
  independent ordered public reference: all flag/identity/inherit byte values,
  full-width signed inputs, zero/one/negative allocation limits, mode bytes,
  resource magnitudes, both stack phases, overlapping/self parent and child,
  and callback mutations of all live incoming words and globals. Reach 179
  retail words; three unsigned-LHU negative-conversion-path words cannot be
  reached through these inputs. All 182 words are statically inspected.
- 390 fired public-access fault pairs / 780 failed runs agree in public
  partial memory, ordered accesses and calls. Two explicit NULL-return runs
  both fault at the first actor write after exactly three callbacks. Private
  frame/fault equivalence is not claimed for the different 0x50 C frame.
- Six independently assembled links at three independently rebased entry,
  five-global and nine-helper symbol sets; 21 cases / 42 full runs qualify
  all ten static JAL sites, HI16 carry cases and no fixed-address assumptions.
- Seven effective newly compiled IDO negative controls distinguish parent
  index, flag mask, duplicate byte source, scale gate, inclusive limit,
  toggle restore and float-word forwarding. One native negative also fails.
- Native32 O2/O0 each pass 18,432 independent-reference cases, 36,864 total:
  all flag bytes, scale inheritance, negative/zero/two limits, callback-driven
  limit changes, self/offset aliases and exact late float bits, including a
  signaling-NaN bit pattern forwarded without arithmetic. Scale arithmetic
  uses finite fixtures. Guest FP-model coverage does not prove hardware FCSR.
- 32 cases / 64 runs execute the actual complete byte-exact 89-word descriptor
  caller and 70-word resource-transition helper around retail/raw constructors.
  Eight linked descriptors (2,15,17,46,54,79,85,5) exercise 28 real type-zero
  calls per form. An initial eight-descriptor selection exercised only the
  alternative constructor; its zero-hit assertion correctly failed before
  replacing the fixture with type-zero descriptors. Remaining deep allocators,
  initializers and the alternative constructor are bounded callbacks, not
  fully recovered resource behavior.
- Actual copied-owner compile, preprocessing and production padding preserve
  all 30 neighbors' bytes, extents and relocations, compiler pools and both
  adjacent placeholders; zero target/copy diagnostics. Existing caller/helper
  bodies are independently checked byte-exact before connection. Broader
  unchanged historical neighbor suites are not reported as fresh runs.
- Consumer make tools-check and mounted standalone python3
  check_project_tools.py both pass. Incremental linked rebuild succeeds with
  the existing duplicate generated_12D630 recipe warning; not warning-free.

## Linked Audit

Only the target slot and ST_SIZE 28 -> 728 change: 581 ELF bytes, all other
ELF bytes identical. ELF 3,261,160 bytes, SHA-256
8e89e21d747efa1f4db8944d48457583c529bd6b9c1172aec9c3dfa66b916ac9.
Protected data 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Owner 9,769 bytes, SHA-256
5cf9c0bc7ddb18b7d5e09538b53761e56d8df54c820f83642ebb1321a46c97f9.

Guard manifest remains 1,912,590 bytes, SHA-256
2e564bf3b7c1985023c66211fda8079b8605f0bb1a1bb7c82f505dd93c4a5237.
Conversion CSV remains 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.
Rodata, symbols and ignored undefined assignments remain byte-identical.
Fresh matching stays Game 2,779/4,821 (57.64%), total 3,452/5,494 (62.83%),
zero drift / 2,042 different. Converted total stays 5,494/6,043 (90.92%).
Root README aggregate rows remain current and unchanged; narrative belongs here.

```sh
python3 -m tools.experiments.game_child_actor_constructor_candidates
python3 -m unittest tools.tests.test_game_child_actor_constructor -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Older standalone tools HEAD ddbdd16 remains untouched: 263 prior dirty entries
plus two absent-only byte-identical new mirrors = 265. Protected helper hashes
and older submit copies are untouched; no older commit/reset/overwrite.
Native Graphify update refuses unsafe shrink 39,634 -> 17,852 nodes, exit 1;
retains 19,398 nodes from 2,972 existing excluded files. Preserve skill
0.9.20/package 0.9.26 and devcontainer.json zero-node warnings; no force,
purge or install. Require fresh consumer post-commit hook completion and
zero actual workers before reporting clean. No host/OGL source, Release,
saves, editor state or private inputs changed. Wider Game goal remains open.

## Next

Finish this full routine's original 0x38 frame and 125 remaining compiler
register/scheduling words before another broad conversion. Trace the cached
actor-base spill versus retail's rematerialized address, S2/S3 lifetimes,
private mode home, independent integer/FP schedules and delay slots. Preserve
the qualified ordered public accesses and live incoming homes. Only publish
any closed normalization after independently qualifying original private
frame/fault order and stale compiler/relocation rejection. Timeline matching,
actual deeper resource/allocator bodies, hardware and gameplay remain separate.
