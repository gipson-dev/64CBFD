# Complete Node Resource Initializer Byte Match

Verified locally: 2026-10-11. One banked function checkpoint in the active
Game matching goal; not complete resource loading, cleanup or live gameplay.

## Result And Baseline

Recover complete func_1502FFD8 in
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c): VA
0x1502FFD8..0x15030158, ROM 0x5D488..0x5D608, 96 words / 384 bytes,
original 0x40 frame. The semantic body replaces a false zero-return C
placeholder; every final linked word matches retail. Keep original assembly
in conker/asm/5D2C0.s and existing O2/g3 profile. No pools, body insertion,
omission, layout or symbol-assignment changes.

Baseline consumer 4d93a45857090b8fc13fa60c779fe3beb8705c51; mounted tools
d2ad015add2fd9914aacbfcd05aed2410837d942. Baseline source SHA-256
01abbb5db432fbdbfe965a558ee83b37a413cbc86fee8ea9d38db8c7ea11707a;
baseline ELF cd907778bb225f56d0ab100345238ee72e9537a89e69bd2817407e6bf8210b8b.
Use [Note 1238](1238-game-complete-animation-node-constructor-byte-match-20261010.md)
for the already banked 152-word factory.

Tools 8ec84847451503994e2dde7121892568c99d799b are committed first, then
consumer source/guards/docs/tools pin, no push. Single Codex writer; zero
Claude calls because compiler experiments, independent references and fresh
negative controls settle the assembly/ABI questions locally. No bridge,
dependency/account changes or token-cost claim. Preserve OGL, frozen Release,
saves/editor state and private inputs.

Older standalone tools HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a remains
unchanged. Only three absent authored paths are mirrored: dirty entries
243 -> 246. Protected game_owner_pool.py and node-effect-registration test
fingerprints remain unchanged; all three mirrors byte-equal, all six AST
parses and both tools checks pass. No old-checkout reset or duplicate commit.

## Complete Contract

1. A non-NULL node resource pointer at 0x24 returns zero without reading the
   selector, actor flags or loader output. Otherwise read the signed selector
   at 0x17 and the unsigned resource kind at byte 1.
2. Selector -1 calls func_1502FE10(kind, node+0x24, node+0x14, &source,
   node+0x30, 0, 0). All other signed selectors call func_1503F62C(kind,
   selector, node+0x24, node+0x14, &source, node+0x30, node+0x48). Preserve
   all seven O32 arguments and callback partial writes. Any nonzero status,
   including the sign bit alone, returns normalized 1 before actor access.
3. Success requires the loader to write the private source-pointer output
   before it is consumed. Compute the 32-bit end-minus-source span once. Read
   actor byte 0x66 even when node flag 0x10 bypasses copying. Copying requires
   node bit 0x10 clear, actor mask 0xC equal to 8, and node+0x30 non-NULL.
4. Allocate two buffers with (size,1,2,2), storing each result at node+0x28
   and node+0x2C even on failure. First NULL returns 1. Second NULL frees the
   live first pointer through func_10004074, then clears node+0x28 and returns
   1. Preserve free-before-clear, partial state and callback mutations.
5. On paired success, bcopy the live source to each live destination using
   the captured size. Reload the escaped source output after the first copy;
   callbacks may change it or the second destination. Set node byte 8 to 1.
   The noncopy path aliases the source into both destinations instead and
   does not set byte 8. Successful completion sets byte 9 to 1 and returns 0.

The source local is intentionally not initialized to zero. Both deeper
loaders, func_1502FE10 and func_1503F62C, still have three-word zero-return
stubs and do not write the required success outputs. A zero status from those
stubs does not satisfy the recovered loader contract. Eight separate guest
cases connect their actual bodies and expose the unwritten private word with
seeded stack residue; they are not valid-output/native-C acceptance. Do not
execute that unwritten-local case as portable C or claim resource restoration.
func_15030158 likewise remains the original incomplete cleanup zero stub.

## Source Fit And Guard Boundary

The early-return form emits 98 words. An outer cached-resource gate recovers
96 words / frame 0x40; local declaration order recovers the correct size home
at frame+0x34, leaving 12 differences. Additional flag widths, register hints
and evaluation-order alternatives do not improve that fit.

Twelve expected-word guards normalize only the checked post-loader read
schedule, closed temporary allocation, branch displacement and branch-delay
flag mask. All seven JAL relocations stay at their original offsets with
their original symbols. No instructions are inserted or omitted. Require the
complete 96-word raw fingerprint and exact relocation map before generation;
all 96 independent stale-word mutations and all seven stale-symbol mutations
reject. Duplicate/stale publication rejects; preserve the historical prefix.

Raw compiler private read order is not claimed to equal retail. Raw C is
qualified separately for public behavior under the valid loader-output and
fresh allocation contract. Retail and fitted forms agree on full ordered
memory/events/calls, private aliases and fired fault prefixes. Guest fault
timing and wrapping extreme noncopy spans are not portable C fault semantics.
Word 38, VA 0x15030070, is an unreachable duplicated actor-home load. Preserve
it byte-exact without claiming execution coverage; the other 95 words fire.

## Fresh Qualification

[Target suite](../../tools/tests/test_game_node_resource_initializer_match.py)
passes all ten tests before installation (32.946s) and after the full rebuild
(42.914s). Reuse existing compiler, MIPS oracle, native32, production padder,
owner-pool and protected-data APIs; no shared helper changes.

- 10,112 cases / 30,336 runs: all signed selector, unsigned kind, node/actor
  flag bytes; cached-resource and nullable transform gates; full nonzero
  statuses; first/second NULL allocations; zero/variable lengths and rollback.
  Each case compares an independent complete ordered reference with retail
  and fitted forms, plus raw public behavior. Caller GP/FPRs are clobbered.
- 107 live-mutation/alias/NULL/boundary cases, 1,240 fired fault pairs / 2,480
  failed runs. Qualify loader/home mutations, source-output escape, live
  destinations, free-before-clear, private/node/actor aliases and wrapping
  guest-only noncopy spans. Required NULL actor access fails at byte 0x66,
  including node-flag bypass; cached/error paths do not require that read.
- Nine independently linked forms at three placements, 96 cases / 288 runs:
  all five callbacks/seven JAL sites and both seven-argument loader packets.
- Complete copied owner compile/post-process/real padding: zero diagnostics,
  pools unchanged, all 39 other functions' bytes/extents/relocations exact,
  deeper loader and cleanup stubs unchanged.
- Ten effective fresh IDO negatives: unsigned selector, narrowed status,
  wrong actor mask, wrong allocation mode/size, missing free/clear, wrong
  copy destination, cached escaped source and false early success. Both
  native wrong-mask and missing-clear controls also fail.
- Native32 -O2/-O0: 12,802 cases each / 25,604 runs; typed seven-argument
  packets, cached/error NULL actor gates, nullable transform, valid success
  outputs, whole node/gaps, buffers and actor compared, rollback ordering and
  escaped-source second-copy mutation. Fresh disjoint buffers only.
- Eight descriptor/record samples independently equal the ROM. Sixty-four
  cases / 128 runs connect actual 89-word caller, 152-word factory, full
  initializer and 113-word action dispatcher with its owned jump tables.
  Fresh bounded allocations handle the two-record sample separately; compare
  independent initializer and action public effects. 1,925 fired connected
  fault pairs / 3,850 failed runs. Actual cleanup zero stub remains connected;
  resource loaders/allocator/free/SDK copy/external action calls are bounded.
- Eight cases / sixteen runs separately connect actual deeper zero loaders
  to expose their unwritten success output. This is a guest boundary receipt,
  not complete resource loading or native-C validity.

Historical factory, request/lookup/classifier and action suites are not rerun
as standalone suites here. Their unchanged linked bodies are covered by the
entire ELF audit; relevant real callers/consumer are executed in the new suite.
Do not label unchanged prior receipts fresh or claim hardware/gameplay parity.

## Linked Audit And Progress

Permit only the target's 384-byte slot and ST_SIZE 12 -> 384. Exactly 284 ELF
bytes change; every other ELF byte is exact. ELF 3,261,160 bytes, SHA-256
9c8e1b09667b0fd9ee9aad0cd36bc44e98048c2388bc430d604093a4fdc46ebc.
Protected data: 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Protected rodata, tracked symbols and ignored undefined assignments are exact.
Conversion CSV byte-identical: 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.
Installed source 53,860 bytes, SHA-256
0ab470e18a81ccdb3dd435a55831a3e19cce4dac72fcaaa7a6f3b5aaf0943b85.

Guard history retains the entire 1,878,484-byte mixed-newline prefix and its
298 CRLF lines; append only twelve LF rows. Working manifest 1,880,308 bytes,
SHA-256 e655f2414198b4e530e3fb953d0ee72899d104716f01ed21b298f9497da0c14f.
Git's existing LF-checkout warning remains; no unrelated normalization.

Fresh match-progress: Game 2,774/4,821 (57.54%), total 3,447/5,494 (62.74%),
zero drift / 2,047 different. Delta +1 matching / -1 different only. Converted
counts/bytes unchanged: total 5,494/6,043 (90.92%),
1,941,060/2,256,728 bytes (86.01%); Game 4,821/5,322 (90.59%),
1,769,624/2,072,880 bytes (85.37%). This was already a C placeholder.

```sh
python3 -m unittest tools.tests.test_game_node_resource_initializer_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

The manifest dependency triggered a broad successful rebuild. Retain existing
generated_12D630 duplicate-recipe and legacy pointer/type/MIPS3 warnings; not
a warning-free full build. Both tools checks pass. Native Graphify refresh
after final code changes refuses unsafe shrink 39,564 -> 17,782 nodes,
exit 1, retaining 19,398 nodes from 2,972 excluded-but-existing files. Preserve
skill 0.9.20/package 0.9.26 and devcontainer.json zero-node warnings. No
force/purge/install. Consumer commit hook requires fresh log growth/completion
and zero actual workers before reporting a clean checkpoint.

## Next

Recover complete 102-word func_15030158, VA 0x15030158..0x150302F0,
ROM 0x5D608..0x5D7A0, original 0x20 frame. Qualify immediate versus delayed
release, initialized/copy ownership gates, attachment/resource release,
nullable auxiliary pointers, live callback reloads, list unlink and final node
free, including the actual factory failure path. Bank that checkpoint before
a broad batch. Deeper func_1502FE10/func_1503F62C resource loaders and full
182-word func_15083AC8 remain open, as do hardware/live gameplay acceptance.
