# Complete Node Alternate Resource Loader Byte Match

Verified 2026-10-11. Consumer baseline cf5aa7e8d6216710561af3c750d8426925d6677b;
mounted tools baseline daabcf7a9866a7606c5b4f0ecdec3438e58eda26. New tools
030412c0b57b8bf54374f5e2d27620db5120eb85 committed first. No push.
Single Codex writer, zero Claude calls; follow DOCS/AGENT_WORKFLOW.md.

## Recovery

Replace func_1503F62C's false zero-return body in generated_6C960.c. Complete
99 words / 396 bytes, VA 0x1503F62C..0x1503F7B8, ROM 0x6CADC..0x6CC68,
original 0x40 frame. Seven O32 word arguments: resource kind, selector,
records/count/source/transform outputs and required attachment output.

Allocate 0x3F8 bytes, publish the returned attachment even when NULL, and
clear only its first 0x40 bytes. Set bytes 0x215/0x45. Call the actual default
loader with the extra pointer output at attachment+0x3F0 and private count
at frame+0x3C. Preserve byte-truncated count/selector metadata, two wrapping
count<<6 allocations at 0x3E8/0x3EC, and the typed action packet
(node,1,0,1.0f,0.0f,0). Normalize the outer result to 0/1.

Preserve retail's ignored nested status and inverted NULL-free gates:
free NULL buffer values, reloading the attachment after each such callback;
skip non-NULL partial buffers, then free the captured/reloaded attachment.
This is original behavior, not a corrected ownership policy. Required NULL
attachment output still faults even when the first allocation returns NULL.

IDO O2/g3 emits all 99 semantic words and the original frame, with zero
diagnostics/pools. Reuse the incoming kind word at all three attachment
captures to retain the original saved-register lifetime. Raw has 24 word
differences, one closed S0/S1 allocation swap. Whole-body fingerprint and nine
JAL relocation checks guard 24 substitutions; no inserts, omissions, call
changes, control-flow changes, or compiler profile changes. Fitted linked
body matches all 99 retail words. Raw saves S1/RA/S0 while retail saves
S0/RA/S1; do not claim raw private fault-order equivalence.

## Qualification

Ten final target tests pass after the full rebuild. Ignored reproducible
receipts are under conker/build/game-node-alternate-loader-test/.

- 1,560 boundary cases / 4,680 retail/raw/fitted executions: all kind and
  selector bytes, full-word count/status boundaries, both stack phases,
  allocation NULL gates, caller GP/FPR clobbers and all 99 words reached.
- 73 alias/mutation cases; 3,651 fired retail/fitted fault pairs / 7,302
  failed executions with exact partial memory/events/calls/FPR agreement.
  Live attachment home, selector/count, post-call reloads, cached node and
  destructive aliases qualify. Raw complete runs normalize only the private
  save-order prefix; no raw private fault-order claim.
- Nine independently rebased links / 324 cases / 972 executions cover all
  nine JAL sites and five callback symbols. Reject all 99 stale-word and nine
  stale-relocation controls, stale manifest and duplicate publication.
- Actual copied-owner postprocess/padder proves all three neighboring
  function bytes/extents/relocations and normalized pools unchanged;
  zero compiler diagnostics before and after.
- Seven effective fresh IDO semantic negative controls, one effective
  native negative, and 4,096 native32 O2/O0 runs. Native mock loader always
  writes a valid count even with nonzero status. Native assignment-destination
  callback mutations are excluded: C evaluation order is unspecified; guest
  tests qualify IDO's post-call attachment reload instead.
- 192 connected cases / 384 executions run actual 114-word default loader
  and 29-word action helper; independent ordered nested-default reference,
  exact 12-word integer/float dispatch packet and 331 fired fault pairs.
- 1,536 initializer cases / 3,072 executions run actual 96/99/114/29-word
  chain. Real records/count/source/transform/attachment outputs, copied
  parent buffers, signed selector bytes, reference rollover and both levels
  of buffer failure qualify.
- Seventeen current loader/initializer behavior regressions pass freshly.
  An initial unfiltered 20-test run had two historical checkpoint failures:
  the old loader expects its unchanged guard manifest, and the old initializer
  expects source before the already-banked default-loader restoration. Their
  saved snapshots are retained, not rewritten. The passing scoped rerun
  excludes these two old whole-ELF audits and the historical zero-stub probe;
  this target's new full-ELF audit is authoritative for this checkpoint.

Actual default-loader allocation failure returns 1 without writing the private
count. Alternate ignores it and reads the unwritten stack word. The connected
guest fixture seeds that residue as 0x80000001, verifies resulting metadata,
allocation packets and status, and never initializes the production local.
Do not run or claim this case as portable native C. Allocators, free, bzero,
deeper resource/record helpers and final SDK dispatcher are bounded callback
receipts, not actual allocation lifetimes, complete resources or gameplay.

## Linked Audit

Only target slot and its ST_SIZE 12 -> 396 change: 288 different ELF bytes,
all other bytes exact. ELF 3,261,160 bytes, SHA-256
485c256877f212283f9ec97a8676002d037da29cee741ae359fe516f4e8c6334.
Protected data 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Rodata, tracked symbols and ignored undefined assignments byte-identical.
Installed source 2,316 bytes, SHA-256
7c903d825702e774c560511f0a6a0d640354afc032ebd007239a764608d51229.

Guard manifest 1,884,235 bytes, SHA-256
e091fe4166d771ea50cf1031ea2712f7eb4176846b3d47dd017227799c640c49:
only 24 new rows; complete old byte prefix including 298 CRLF lines retained.
Conversion CSV remains 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.
No additional conversion credit for replacing an already-counted C stub.

Fresh match-progress: Game 2,777/4,821 (57.60%), total 3,450/5,494 (62.80%),
zero drift / 2,044 different. Delta +1 matching / -1 different only.
Converted counts/bytes unchanged: total 5,494/6,043 (90.92%),
1,941,060/2,256,728 bytes (86.01%); Game 4,821/5,322 (90.59%),
1,769,624/2,072,880 bytes (85.37%). Init 492/492 and Debugger 181/181
already-converted routines remain exact; unconverted routines stay open.

```sh
python3 -m tools.experiments.game_node_alternate_loader_candidates
python3 -m unittest tools.tests.test_game_node_alternate_loader_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Manifest change triggers full padded-object rebuild; existing duplicate
generated_12D630 recipes and SDK/generated compiler warnings remain. Zero
target diagnostics is not a warning-free full-build claim. Both tools checks
pass. Older standalone tools HEAD ddbdd16 remains untouched: 251 prior dirty
entries plus three absent-only, byte-identical new mirrors = 254 entries;
protected helper hashes unchanged, no older-checkout commit/reset/overwrite.

Native Graphify update refuses unsafe shrink 39,593 -> 17,811 nodes, exit 1,
retaining 19,398 nodes from 2,972 existing excluded files. Keep the existing
skill 0.9.20/package 0.9.26 and devcontainer.json zero-node warnings; no
force/purge/install. Require fresh post-commit hook log growth/completion and
zero actual workers before reporting a clean checkpoint. No OGL/Release,
saves, active editor or private inputs changed; wider Game goal remains open.

## Next

Recover full 66-word func_1503F4B0, the remaining zero placeholder in this
same owner: VA 0x1503F4B0..0x1503F5B8, ROM 0x6C960..0x6CA68, original
0x48 frame. Audit the live global selector, gated temporary 0x320 allocation,
transform packet, effect submissions, unconditional final actor update and
conditional temporary free before determining its C return contract. Preserve
all three now-real neighbors and bank that checkpoint before a broad batch.
Full 182-word func_15083AC8 and actual resource/allocator/hardware/gameplay
acceptance remain open.
