# Actor Record Table Index Direct C Match

Date: 2026-10-22

## Result

Match existing semantic `func_1505E7CC` in `conker/src/game_83300.c`
directly from complete C: **42 static words, frame0, two bindings and no
guards** under the existing normal O2/g3 profile. Keep the original
`conker/asm/nonmatchings/game_83300/func_1505E7CC.s`.

VA1505E7CC..1505E874 / ROM8BC7C..8BD24, ends exclusive.
Unlinked C/GNU-original body SHA-256:
`adf9aef8c2e9454921e55ec1086031234310a3f158bb4ffc36b2c47e824b6442`.

The old semantic C produced a 71-word unrolled loop in a 42-word retail
slot, reached through a trampoline. It was not a zero-return placeholder.
This match adds no converted-C function and changes no denominator, shared
header, compiler profile, Make recipe or guard row. Use descriptive locals
and a short purpose comment; retain the address-based public symbol.

## Recovered Contract

Keep `u32 func_1505E7CC(s32 key, struct127 *actor)` and the existing
`extern s32 D_800D1588[187]` declaration. The words in this table represent
descriptor pointers in the 32-bit guest ABI; do not broaden the native
declaration to a fictional 256-pointer array.

Read actor ID at +4 as a byte. ID0xFF returns zero before any table access.
For other IDs, read the descriptor pointer; NULL returns zero. Read the
unsigned byte length at descriptor-4; zero returns before reading the entry
pointer. Divide by 0x18, then read the entry pointer at descriptor-8 even
when a nonzero length yields zero records. NULL entries returns zero.

Search only the resulting count, stepping 0x18 bytes per record. Compare
the full signed32 key against the zero-extended first byte, without narrowing
the key. Return the first matching zero-based unsigned index, otherwise zero.
A match at index zero is intentionally indistinguishable from not found.
There are no helper calls or memory writes.

Keep a separate entries pointer and initialize the cursor inside the
nonempty-count guard. A guarded do/while reproduces the original unrolled-free
loop, allocation and schedule under normal O2. Initializing the cursor outside
the guard gives 41 words/16 differences; an unsigned for-loop unrolls to73.
The selected unsigned index avoids an unnecessary signed local. No dummy
locals, instruction emitters, artificial padding or normalization are used.

All 42 static words match. Public paths visit40; the duplicate length load
at1505E804 and duplicate increment at1505E858 are statically unreachable,
not omitted or claimed dynamically exercised. Preserve both branch-likely
updates and the final cursor advance in its branch delay slot.

| Body Offset | Binding | Symbol |
| --- | --- | --- |
| 0x0C | R_MIPS_HI16 | `D_800D1588` |
| 0x24 | R_MIPS_LO16 | `D_800D1588` |

## Caller Boundary

Scan the retail US Init/Game/Debugger functions, not just remaining assembly
files: there are seven direct JAL sites in six parents.

| Parent | JAL VA |
| --- | --- |
| `func_150562FC` | 15056538 |
| `func_150562FC` | 15056768 |
| `func_1505959C` | 15059710 |
| `func_1505B5F8` | 1505B67C |
| `func_1505B9C4` | 1505C01C |
| `func_1505D2B8` | 1505D318 |
| `func_1506EA98` | 1506EB68 |

The last parent is already-converted C in `conker/src/game_981E0.c`, pinned
and unchanged. Preserve the existing shared prototype; no caller edits.
Run the literal two-word JAL/delay window for every site, three boundary-key
patterns and two SP phases:42 phases. Seed the declared boundary inputs and
stop at the actual return PC+8. Do not invent an executable stop instruction.
This qualifies the call/delay boundary, not complete parent execution or
natural gameplay. Graph adjacency alone is not evidence of a direct call.

## Qualification

Tools: `experiments/game_actor_table_index.py` and
`tests/test_game_actor_table_index.py`, identical in both local copies.

| Final Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 79.759s | 8 tests, 72.304s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 3.843s | 2 tests, 4.573s | 0 / 0 / 0 |

Explicitly reuse the other six pre-install checks per copy only under strict
source, raw/padded object, helper, input and complete-image identity. They are
not fresh installed executions. Shared project-tool checks pass in both copies.

- 2,776 guest phases cover every ID byte, full-word key poisons, unsigned
  length boundaries, null/empty gates and two SP phases;48 more cover aliases.
  Compare returns, exact read traces, final modeled GPR/FPR/HI/LO/events and
  unchanged memory. The union visits all40 reachable words.
- 1,888 native32 cases per O0/O2/O3 use trap UBSan and the canonical struct127.
  Exercise actual valid table indices0..186 and disabled0xFF. Sparse guest
  ID tests187..254 do not authorize native out-of-bounds array accesses.
  Test indices255,256,65535,65536 using fully backed records. Huge declared
  lengths use NULL or guaranteed early-match prefixes, not unbacked scans.
- All eight defined wrong-C controls fail: disabled ID, truncated key,
  stride, count divisor, byte field, one-based result, always-zero result
  and signed division. Finite controls use bounded1856-case vectors; the
  signed-length control uses the full1888 bounded/early-match vectors.
- Six independent GNU links /72 phases cover both bindings and signed-low
  carries at three table anchors. Verify424 fired root-read fault prefixes;
  these qualify emitted instruction state/order, not portable C fault or
  hardware MMU behavior. Nine strict-image corruption controls are rejected.
- Pin27 historical/current inputs and the old padded object. Preserve all88
  raw/padded owner neighbors and normalized pools. The eight inherited
  pointer/integer warnings remain identical after path/line normalization;
  isolated target diagnostics are empty. Actual Make shadow runs five
  productive commands under normal O2/g3 and reproduces all89 raw functions.

The final table excludes failed fixture runs. Fix the stale neighbor count,
coverage union, pre-existing SDK Header type collision, stop-boundary
membership, unused wide fixture and defined negative-control domains before
rerunning both complete suites. No production warning suppression or semantic
change was introduced to make those fixtures pass.

## Production And Overflow Accounting

Verify all15,806 live/cache files and the complete1,454-object link closure,
reusing the prior sealed Linux cache. Qualify the complete image before
installing the body. Actual production Make exits zero in3.161s and exactly
reproduces the independently linked prediction, with **zero byte or metadata
exclusions**. The duplicate generated_12D630 recipe warning remains.

Remove only the284-byte `__retail_overflow_func_1505E7CC` body at15F00420.
Owner overflow shrinks504->220; global Game overflow shrinks2912->2628.
The entire overflow stream is the old stream with just that range deleted.
Seven later overflow bodies move down284 bytes, with instructions unchanged:
1506EE60,150768DC,15076D3C,150781F4,150A7B80,150A7D00,15125490.
Update four ordinary jump destinations at150768DC,15076D3C,150781F4,
150A7D00. All retail function entry addresses stay fixed; do not claim all
overflow addresses or all other raw linked function bytes are unchanged.

Account for the removed local symbol, suffix-shared string table, relocated
symbol definitions, program/section/ELF headers and alignments. The two ROM-end
definitions move272 bytes because of16-byte alignment, not284. Full ELF size
shrinks320 bytes:3,257,444->3,257,124. No blanket metadata normalization.
The retired overflow symbol also reduces the linked function count by one.

Installed ELF SHA-256:
`2e6c870c43314ed068cbf2d51ddb8731b30a1ac0cf38b7fb4275885d99be35e8`.
Installed owner object SHA-256:
`82cb364a8131ef7031a43597269e9aea08cbdc8134aaa872f56a06ea1e55931f`.

Protected Game data remains exact:189,088 bytes /720 owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Preserve the entire guard manifest. Recheck live static files before/after
adopting only the target object, ELF, generated linker script and progress CSV.

Tools commit `d38ac24de8184754407383c4f302240747ea68f7` precedes consumer
source/docs/pin. Preserve all1,530 pre-existing older-mirror dirty statuses
and hashes; add only the two task files, totaling1,532 paths. Do not commit,
reset, clean or stash that mirror. No push, Claude call or host change;
Release stays frozen. Root README changes only two aggregate rows. Refresh
Graphify and audit old-node retention after the consumer commit.

## Measured Progress And Resume

The literal standard matcher exits zero against the adopted live ELF:

| Section | Byte-Exact Converted C | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3,727 / 5,505 (67.70%) | 0 | 1,778 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,054 / 4,832 (63.20%) | 0 | 1,778 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The75% threshold remains4,129; **402 more exact functions** are required.
The goal remains unfinished. The refreshed ELF-pinned queue contains1,647
placeholders,122 semantic/other definitions and nine unlocated entries.

Next screen: `func_150F07E4` in `conker/src/game/generated_11C2B0.c`,
original `conker/asm/11C2B0.s`,42 words/frame24/39 differences.
VA150F07E4..150F088C / ROM11DC94..11DD3C, ends exclusive. Establish
the true caller ABI, byte command capture, owner+0x60 descriptor, mode-zero
short-circuit/helper path and command0x2D word/byte swaps. Preserve full
incoming homes and alias-sensitive read order before fitting. This is only
a source/assembly screen: no edit, compilation, adoption or matching credit.
Keep the862-word `func_1508CAD8` owner stub queued separately.

Private snapshots, probes, native fixtures, images, queues and audits remain
under `conker/build/game-actor-table-index/qualified/`; do not commit them.
