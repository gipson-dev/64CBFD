# Game Resource Buffer Retail-Length Improvement

Date: 2026-10-11. Continue the complete recovery in
[Note 1255](1255-game-resource-buffer-preparation-recovery-20261011.md),
under [the agent workflow](../AGENT_WORKFLOW.md). Single Codex writer,
zero Claude calls. Keep the wider Game matching goal active and commit
authorized checkpoints tools-first without pushing.

## Target And Baseline

- Function: func_15084044, VA 0x15084044..0x1508434C.
- Retail ROM: 0xB14F4..0xB17FC, 194 words / 776 bytes.
- Owner: conker/src/game/generated_AEB40.c; retail conker/asm/AEB40.s.
- Consumer baseline: 76ae0a11175fa623c4ff62a468f9909cba7084a7.
- Mounted tools baseline: 7f64ce9950cadca48c980cf3b4276f3f1192af78.
- Both active checkouts clean at entry. Older standalone tools remains at
  ddbdd16b53ce60b054fb6e11bf0649a41f48375a with 281 dirty entries.
- Banked recovery: complete semantic C, 192 words, frame 0x60,
  130 raw word differences, no guards; ELF SHA-256
  e8a9504c87c628ce552d6f752fe26c27f4fcaaf1651612a37f998c80ba8bf690.

Reread the complete routine and sole direct retail caller func_1503DA9C.
Its 104-word assembly is available; current C caller remains a placeholder.
Full resource loading, hardware heap and gameplay acceptance are not implied.

## Measured Source Improvement

The installed C changes only three related source shapes:

1. Place the first-buffer reload separately at each mode-one allocation/
   sharing branch join, rather than after their common join. The successful
   copy path still reloads the live slot after callbacks; no cached-value
   shortcut or fallback removal.
2. Spell the mode-two cursor as actor + (channel << 3), retaining the
   original actor/channel domain. IDO now recomputes it rather than reusing
   the early pair pointer.
3. Initialize offset before that cursor assignment, then use the original
   exclusive-eight loop bound and four-byte update.

| Complete Candidate | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Committed recovery | 192 | 0x60 | 130 |
| Split mode-one join, original cursor | 193 | 0x60 | 119 |
| Split join, shifted cursor | 194 | 0x60 | 40 |
| Earlier offset initialization, installed | 194 | 0x60 | 39 |
| Cached eligible pointer, earlier initialization | 194 | 0x60 | 42 |
| Separate initial shared-source local | 194 | 0x68 | 53 |
| Inline initial global access | 195 | 0x68 | 187 |

The new experiment module preserves complete banked and candidate bodies,
join/source/type/cursor variants and bounded lifetime/register experiments.
Register storage-class hints do not improve the 40-difference variant.
The separate-source generator's two overly broad replacements were caught
and narrowed before qualification or installation: never replace allocation
publication or the nested allocation NULL gate with the cached source.
Discard earlier malformed separate-source results; only corrected forms
are valid evidence. No shared compiler/oracle/padder edits or broad guards.

## Fresh Qualification

Reuse tools/tests/test_game_resource_buffers.py with the actual new body.
Keep the immutable original-stub baseline and its hash checks. Recompile
the historical 192-word body separately; the pre-install linked audit verifies
that actual known historical installation, not an unchecked skip. Add a
second immutable committed-recovery baseline and a twelfth exact-delta gate.
Do not overwrite either baseline.json or matching-baseline.json.

- Eleven pre-install tests pass in 28.067s; added delta gate passes separately.
- All twelve post-install tests pass in 29.240s.
- 7,424 mode/identity/count/slot/failure cases, 14,848 original/C executions;
  172 original words reached, full memory and access order equality.
- 896 parent/channel/size/live-helper mutation cases, 1,792 executions.
- 3,632 all-access fault pairs; every gate fires and complete partial memory,
  access/call receipts agree. This is emitted guest order, not portable C
  fault behavior.
- 27 fresh original/candidate/padded links, three normal symbol sets and
  resource/count aliases, 43 cases; complete-pair short circuit avoids globals.
- Eight freshly compiled IDO semantic negative controls, all effective.
- Actual complete native32 C: 12,288 cases each at O2/O0, 24,576 total,
  plus an effective wrong-count negative; widths/stride/canaries checked.
- All 30 copied-owner neighbors retain bytes, extents, relocations and pools;
  zero owner diagnostics, both real padding routes preserve non-target bytes.
- Actual linked Init allocation wrapper and SDK bcopy: 144 cases/288 runs,
  207 connected words, 72 reached. Only genuine saved continuation PCs are
  normalized; allocation core/free remain bounded callbacks.
- Complete original 104-word caller: 576 cases/1,152 runs, 60 words reached,
  576 actual helper invocations per original form. Actor/channel/failure
  forwarding agrees; loader callback and extras-zero-count scope remain bounded.

Commands from 64CBFD:

```sh
wsl --exec python3 -m tools.experiments.game_resource_buffers_matching --lifetimes
wsl --exec python3 -m unittest tools.tests.test_game_resource_buffers -v
wsl --exec make -C conker -j4 build/conker.us.elf progress.csv
wsl --exec make -C conker match-progress NON_MATCHING=1
wsl --exec make tools-check
```

Mounted standalone WSL python3 check_project_tools.py also passes. Older
standalone WSL check and native py_compile of the new experiment pass.
Its native python check_project_tools.py fails with WinError 193 at a
subprocess executable; record this separately, do not modify older work.
Known duplicate generated_12D630 recipe warning remains unchanged.

## Complete Linked Delta

Compare the actual production ELF with both immutable baselines. From the
committed Note 1255 recovery, exactly 317 bytes change: 316 in this 776-byte
slot, one in its symbol-size field (768 -> 776). Every other ELF byte is
literally identical, including raw symbol/string tables except that size.
All other functions, addresses, extents, pools and protected inputs stay exact.
Relative to the older stub baseline, 622 bytes change: 584 target-slot bytes
and 38 metadata bytes including extent/existing symbol ordering; the original
structured symbol/name/section equality gate still passes.

- New ELF SHA-256: d543a0960902f688cb569ca95d96e563b105f2ff37ff1a8dc7a73f62d1987056.
- Owner SHA-256: 51c99470e8b1454913539860ace42ccd5a81f3927d7ca88e96d3c916c0c40941.
- All 189,088 protected data bytes / 720 owners exact; SHA-256
  0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
- Guards unchanged: 5e50f8952c0e5d4ba39b7e9054b7ac5727517d021ba8e92d3b10c8a2f07b2f19.
- Conversion CSV unchanged: 32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.
- Rodata source, layout, tracked symbols and ignored auto assignments unchanged.

Fresh matcher: Game 2,786 / 4,822 (57.78%), total 3,459 / 5,495 (62.95%);
Init 492 / 492, Debugger 181 / 181. Zero drift, 2,036 different.
No matching or converted credit. Root README aggregate rows are correct and
unchanged; function narratives stay in documentation, not the root README.

## Ownership And Graph

Mounted tools commit 2a4183d396f054401de85c2647d78c4805eaae78 banks only
the new experiment and focused test evolution before the consumer gitlink.
Copy only the absent new experiment into the older standalone checkout,
hash D4C8C553AD1B8BC7EE14040A1D8C2902694166160B5EEAD77599D8F0B1FC72B8.
Do not overwrite its existing recovery test or candidate module. Older HEAD
and all four protected existing hashes remain unchanged; dirty count 281 -> 282.
No older commit/reset or push. No OGL, Release, save, editor or private-input
changes. Release remains frozen.

Native graphify query func_15084044 --budget 650 succeeds. Native update .
extracts two uncached files but refuses unsafe shrink 39,708 -> 17,926 nodes,
retaining 19,398 nodes from 2,972 excluded-but-existing files. Preserve its
version/zero-node warnings and protective refusal; no force/purge/install.
After consumer commit, separately require fresh rebuild-log bytes/UTC,
a fresh Rebuilt tail and zero actual Graphify/Python workers before ending.

## Next Matching Work

The complete body, length, frame, joins and cursor schedule are now banked.
Do not replace the semantic body with broad expected-word patches or skip
to an easier target for a matching count. The 39 differences are measured
raw words, not 39 independent scheduling operations.

1. Recover the opening allocation: retail retains actor in A2 (candidate
   channel), config in V0 (candidate A1), mode in V1 (candidate V0), initial
   global resource in A0 (candidate A1). Most mismatches are this region's
   consistent register choices; preserving the frame and private slots matters.
2. Preserve the now-exact branch joins and cursor instruction positions.
   Offset zero occupies the retail branch delay; recomputation matches length.
3. At offsets 0x290/0x298/0x29C, retail reloads the loop destination in V0,
   uses ordinary beq, and moves V0 to A1 in its delay slot. Current C reloads
   directly into A1, uses beql and loads the shared source in the delay slot.
   Test a distinct short-lived copy-destination lifetime without removing the
   live reload/fallback or enlarging the frame. This remains a hypothesis.
4. Reuse all twelve gates and both immutable baselines; extend exact-delta
   evidence if the next qualified body changes. Fresh matcher before credit.
   Full C caller/resource loader/heap/hardware/renderer/gameplay remains open.
