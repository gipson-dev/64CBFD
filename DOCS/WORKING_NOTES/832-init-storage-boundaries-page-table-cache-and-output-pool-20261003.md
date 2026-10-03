# Init Storage Boundaries: Page Table, Cache And Output Pool

Date: 2026-10-03. Baseline: `4e760fe`.

## Result And Scope

New bounded instruction tests pin and execute retail startup/page arithmetic
and the cache-maintenance address loop. They establish concrete usage
boundaries, not a complete storage reservation/ownership manifest.

- Startup's rounded page-table transfer is 2,048 bytes and ends exactly at
  the input-buffer address 0x80033330.
- All 507 retail DMA spans remain at most 3,072 bytes, with 440 bytes before
  the workspace at 0x800340E8 (the earlier bound is freshly rechecked).
- The cache loop emits 257 operands, including 0x80034330. Its address sweep
  extends into the workspace region; it is not an input allocation-capacity
  proof or a software-store range.
- Output page selection uses the separately allocated pool base plus
  page_index * 0x1000. Four boundary cases execute the original arithmetic.

All ten focused tests pass in 4.150 seconds. No decoder/adapter, production
owner, default compiler shape or README aggregate changes. Complete ownership,
synchronous faults and the 896-byte fitting excess remain open.

## Executed Startup Arithmetic

The test pins all thirty original words at 0x10001318..0x1000138C to the local
US retail ROM (the page loader verifies its SHA-1). It executes only that
block, stopping before the DMA call at 0x10001390. Prior s0 is seeded with
the startup offset 0x42450; no allocator, OS initialization or DMA is replayed.

The block computes the page count from 0x151FA130 - 0x15000000, rounded up to
4 KiB: 507. It publishes aligned input/table pointers to D_800354F8/354FC,
computes the rounded transfer, and prepares the source address 0x42454:

| Boundary | Value |
| --- | ---: |
| Table start | 0x80032B30 |
| Page count | 507 |
| Offset entries subsequently rewritten | 508 |
| Rounded table DMA bytes | 2,048 |
| Table transfer end / input start | 0x80033330 |
| Bytes after the 508 required offset words | 16 |

The transfer expression requests count+2 words before rounding; the XOR loop
in `init_1050.c` rewrites count+1 entries. Thus the last sixteen transferred
bytes include the extra unrewritten word and alignment padding, not another
required page offset. The executed block writes only the two pointer globals
and two local stack cells. This pins the setup/data boundary, not all future
indirect users or writers of the backing memory.

## Cache Sweep Is Not Buffer Capacity

The seven-word block at 0x10005DEC..0x10005E04 loads the input pointer, forms
input+0x1000, emits CACHE operation 0x15, compares unsigned, and increments
the cursor by sixteen in the branch delay slot. It emits an operand at the
endpoint before exiting, leaving the cursor at input+0x1010:

```text
257 operands: 0x80033330, 0x80033340, ... , 0x80034330
final cursor: 0x80034340
workspace:    0x800340E8
```

The final cursor is 600 bytes above the workspace base. This is arithmetic
about the emitted sweep and stride, not a claim that six hundred workspace
bytes are overwritten. The test records CACHE operands only; it does not
model cache lines, tags, writeback/invalidation, PI transactions or cache/DMA
ordering. Software writes in this isolated loop are absent. Therefore its
0x1000 constant must not be used to infer a disjoint 4 KiB input allocation:
the input-to-workspace gap is only 0xDB8 / 3,512 bytes.

The real page DMA spans fit that gap, but arbitrary larger payloads and full
hardware cache correctness are not qualified by this test.

## Output Pool And Remaining Owner Audit

The eleven words at 0x10005CF4..0x10005D1C clear the chosen bitmap bit, derive
the page index from bitmap byte offset and bit index, and add its 4 KiB stride
to D_8003BE74. Tests execute pages 0, 7, 8 and 234 in a 235-page fixture pool,
pin the words to retail, and check both bitmap store and output address.
The fixture's physical pool base 0x00100000 and bitmap pointer 0x80200000 are
private examples, not observed retail allocations.

Scoped source inspection locates the actual allocation path:

- `init_1050.c` initially calls `func_10005B04(0xEB)`.
- `init_5AB0.s:func_10005B04` calls `func_10003C6C` for count<<12 bytes with
  arguments (size, 0xFF, 4, 1, 2), masks the returned pointer into D_8003BE74,
  and allocates the bitmap separately. Allocation failure retries using the
  previously saved count; this path is not executed by the new fixture.
- `init_3BD0.c` seeds the heap/free-list heads at D_800E9D10. The allocator
  uses free-list metadata and alignment tables, including a tail allocation
  path for arg3 != 0. That seed alone does not prove all later free-list
  mutations or fallback requests remain valid/non-aliasing.
- The BSS configuration in `conker.us.yaml` remains a broad segment, not an
  explicit per-object reservation manifest. Symbolic-use searches identify
  the table/input/workspace globals but do not exclude numeric or indirect aliases.

The next ownership work is the pool allocation/fallback and free-list writer
audit, plus a complete reservation/writer account for the exception stack and
workspace. These tests do not authorize consuming the apparent gaps as extra
stack/storage. The previous retail thread-end boundary and corpus stack margin
remain independent evidence.

## Verification

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_decompressor_retail_pages tools.tests.test_init_decompressor_context_layout -v -f
```

- Ten tests pass in 4.150 seconds: four new boundary/primitive tests, three
  existing retail-page tests, and three context-layout tests.
- The local address fixture adds SLTU and XORI support only for these bounded
  blocks. An initial run stopped on unsupported SLTU; the fixture extension
  and its primitive checks fix that test limitation, not production code.
- Both guest SDK layout profiles recheck the 0x230 retail thread storage end
  at 0x80031D10. Existing representative retained-core tests also pass.
- Root `make tools-check`, the new module's Python syntax check and
  `git diff --check` pass.
- No new compiled-shadow full corpus, production build, complete handler,
  hardware cache/DMA/pipeline or gameplay execution is claimed.
- Pending Game changes and sibling repositories are preserved and excluded.

[Note 831](831-init-explicit-corpus-cu1-modes-and-clear-full-pass-20261003.md)
still supplies the latest loop-lookup full-page CU1-clear receipt. This note
does not transfer that private-buffer pass into a complete ownership proof.
