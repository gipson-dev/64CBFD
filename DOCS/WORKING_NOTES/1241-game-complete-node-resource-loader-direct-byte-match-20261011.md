# Complete Default Node Resource Loader Direct Byte Match

Verified locally: 2026-10-11. One banked function checkpoint in the active
Game matching goal, not complete alternate resource loading or live gameplay.

## Result And Baseline

Recover full func_1502FE10 in
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c): VA
0x1502FE10..0x1502FFD8, ROM 0x5D2C0..0x5D488, 114 words / 456 bytes,
original 0x50 frame. The complete semantic body replaces a false zero-return
placeholder and emits every retail word directly from C. No guards, pools,
instruction insertion/omission, compiler-profile or layout changes. Preserve
original conker/asm/5D2C0.s and existing O2/g3 profile.

Baseline consumer f863dedb8138261b22b5209193429127b834c318; mounted tools
088efd42a4e25aae38a5f73e9f9859a43e9fccb9. Baseline source SHA-256
86ccba6353f361ca2682c9c47641e3758e26f6576232eb5a646524cca9ad577d;
baseline ELF 21860452ad90029ea4130259bf0c92dad90765ba67dd4a9f71e68a40bdfb0a55.
See [Note 1240](1240-game-complete-node-release-byte-match-20261011.md) for
the already banked release/factory rollback boundary.

Tools daabcf7a9866a7606c5b4f0ecdec3438e58eda26 are committed first, then
consumer source/docs/tools pin, no push. Single Codex writer, zero Claude
calls: compiler experiments, independent references and fresh negatives settle
this routine locally. No bridge, account/dependency or shared-helper changes;
no token-cost claim. Preserve OGL, frozen Release, saves/editor and private inputs.

Older standalone tools HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a remains
unchanged. Mirror only two absent authored files: dirty entries 249 -> 251.
Both byte-equal, four AST parses and both tools checks pass. Protected
game_owner_pool.py and node-effect-registration test hashes are unchanged.
No overwrite, reset or duplicate old-checkout commit.

## Complete Contract

1. Recover seven O32 arguments: full-word kind, required record-array output,
   count-byte output and source-pointer output, then optional transform,
   extra-pointer and extra-count outputs. Do not narrow the kind argument.
   No new bounds checks: extreme wrapping index receipts are guest-only.
2. Read D_800DF7D0[kind]. Nonzero uses the retained header in
   D_800E0148[kind], publishing its word 0 and packed word 4 shifted right two
   into the record-array and byte-count outputs. Do not relocate cached records
   again. Zero calls variadic func_1502B6BC(0,0,0,2,9,kind).
3. NULL fresh header returns normalized 1 before dereferencing required
   outputs. Fresh success publishes the same two outputs, then rebases each
   live record word by the header's 32-bit address. Submit
   func_1510CE60(record,0,1,0x3E,&D_800DF9B8[kind]) followed by
   func_15168E54(live_record,header). Ignore both callback returns.
4. Reload record-array output after each callback and count byte after the
   second; callback mutations can shrink or grow the loop. On completion,
   publish the captured header into D_800E0148[kind]. Preserve captured
   reference-pointer lifetime and all callback/private-home alias behavior.
5. Increment the live reference byte modulo 256, including 255 -> 0. Store
   required source pointer header+0x18. Optional transform copies header word
   0x10. Optional extra copies header word 8; only inside that gate does a
   non-NULL extra-count receive unsigned header word 0xC shifted right four.
   Preserve the retail reads of optional argument homes even at NULL gates.
6. Return zero on cache/fresh success. The actual 96-word initializer's
   selector-minus-one path now receives written source/count/record/transform
   outputs and consumes real source bytes. It still propagates loader failure
   and its own first/second buffer allocation failures.

Alternate func_1503F62C remains a zero stub lacking required success outputs.
The lower variadic resource loader, record-retain/relocate helpers, allocator
and SDK copy callbacks are bounded fixtures here; no whole resource system,
actual allocator lifetime, emulator or host/gameplay acceptance is claimed.

## Source Fit And Fresh Qualification

Explicit reference, dependency and byte-offset locals initially emit 114 words
but frame 0x58 and eleven differences. Remove those locals, retain the record
index and use a positive byte-count gate: IDO recovers the original induction
register, saved-register lifetimes, reference-pointer home and 0x50 frame.
32-bit integer record rebasing is directly exact. Six repeatable candidates
include the 115-word for-loop mismatch; selected/register-header forms are
114/0x50/zero differences. All eleven JAL/HI16/LO16 sites remain correct.

[Target suite](../../tools/tests/test_game_node_resource_loader_match.py)
passes all ten tests before installation (39.211s) and after rebuild (39.997s).
Reuse existing compiler, MIPS oracle, native32, owner/padder and data-layout
helpers. No shared helpers changed; do not repeat unchanged broad suites.

- 3,072 cases / 9,216 runs: all kind/reference/count bytes, cache/miss/NULL
  loader result, eight optional-output masks and two stack phases. Independent
  reference compares complete memory, ordered reads/writes/calls and status
  with retail/raw/fitted forms. All 114 retail words fire; caller GP/FPRs clobber.
- 97 mutation/alias/NULL cases and 402 fired fault triples / 1,206 failed runs:
  live record/count/header/reference/cache changes, escaped output argument
  homes, public/private outputs and required NULL-output failure gates. Check
  each injected fault actually fired. Guest faults/private aliases are not
  portable C fault semantics or valid extreme pointer/index acceptance.
- Nine independent links at three placements, 219 cases / 657 runs: rebase
  all three globals and callbacks independently, including signed HI16/LO16
  carries and repeated cache-address sites. Three extreme kind cases separately
  qualify full-word wrapping guest addressing, not native out-of-array C.
- Copied-owner compile/post-process/production padder: zero diagnostics,
  pools unchanged and all 39 neighbors' bytes/extents/relocations exact. The
  existing seven-argument initializer caller emits unchanged instructions.
- Ten effective fresh IDO negatives: narrowed kind, wrong cache gate/load tag,
  count shift/rebase/retain mode, missing reference increment, wrong source/
  extra-count shift and a cached callback-mutated loop bound. Two native
  wrong-rebase/missing-reference controls also fail.
- Native32 -O2/-O0: 6,912 cases each / 13,824 runs, independent loop/cache
  reference compares complete header/record arrays, output/gap words, active
  cache/reference/dependency entries and all callback packets. Public callback
  mutations qualify; resource/record callbacks remain bounded.
- 576 cases execute actual 96-word initializer with this full loader. Verify
  written source output, copied/aliased buffers, cached reference rollover,
  loader NULL and both buffer-NULL paths. Independent ordered loader reference
  checks the complete nested body. All 181 injected connected access faults
  fire; this is not a separate full factory/alternate-loader acceptance suite.
- Five successive-call cases / fifteen runs prove cached records are not
  rebased twice and reference 255 -> 0 causes the next miss to load/publish a
  fresh header, source pointer and record array.

Historical initializer/factory/release suites are not rerun standalone. Their
unchanged linked bodies are covered by the complete ELF audit; the relevant
real initializer connection executes in this new suite. Prior receipts are
not labeled fresh; runtime acceptance remains separate.

## Linked Audit And Progress

Permit only target's 456-byte slot and ST_SIZE 12 -> 456. Exactly 334 ELF
bytes change; every other byte is exact. ELF 3,261,160 bytes, SHA-256
4e180029d6a23026000a55fc5c6d0614331312c8e33227e3f4571dd6f3a5aa13.
Protected data 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Protected rodata, tracked symbols and ignored undefined assignments are exact.
Installed source 56,994 bytes, SHA-256
860cd5809b49f19812bdcf73f049666e399437e5729eca30adeeda968194363c.

Guard manifest is byte-identical, including its 298 historical CRLF lines:
1,880,988 bytes, SHA-256
97d736eeb70d54ea162326bffdfdd94d30d5c41ddec3a40c1dcf684815db6a64.
Conversion CSV byte-identical: 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.
Do not infer new conversion credit from replacing an already counted C stub.

Fresh match-progress: Game 2,776/4,821 (57.58%), total 3,449/5,494 (62.78%),
zero drift / 2,045 different. Delta +1 matching / -1 different only.
Converted counts/bytes unchanged: total 5,494/6,043 (90.92%),
1,941,060/2,256,728 bytes (86.01%); Game 4,821/5,322 (90.59%),
1,769,624/2,072,880 bytes (85.37%). Init 492/492 and Debugger 181/181
already-converted routines stay exact; unconverted routines remain open.

```sh
python3 -m tools.experiments.game_node_resource_loader_candidates
python3 -m unittest tools.tests.test_game_node_resource_loader_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Only the target owner recompiles before relink/progress; no guard dependency
change or broad rebuild. Preserve existing generated_12D630 duplicate-recipe
warnings; zero target/compiler diagnostics is not a warning-free full-build
claim. Both tools checks pass. Native Graphify update refuses unsafe shrink
39,584 -> 17,802 nodes, exit 1, retaining 19,398 nodes from 2,972 existing
excluded files. Preserve skill 0.9.20/package 0.9.26 and devcontainer.json
zero-node warnings; no force/purge/install. Require fresh post-commit log
growth/completion and zero actual workers before reporting a clean checkpoint.

## Next

Recover complete 99-word func_1503F62C in generated_6C960.c: VA
0x1503F62C..0x1503F7B8, ROM 0x6CADC..0x6CC68, original 0x40 frame. Preserve
seven O32 arguments, output attachment allocation/clearing, actual default
loader connection, live outputs, two count-scaled allocations and typed
float action call. Retail ignores the nested loader status and subsequently
reads its private count output; qualify unwritten output on failure as a guest
boundary rather than silently initializing it. Preserve and explicitly test
the unusual allocation-failure NULL-free branches instead of correcting them
incidentally. Bank that checkpoint before a broad batch. Full 182-word
func_15083AC8 and actual resource/allocator/hardware/gameplay work stay open.
