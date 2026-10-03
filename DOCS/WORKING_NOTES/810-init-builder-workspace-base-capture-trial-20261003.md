# Init Builder Workspace Base Capture Trial

Date: 2026-10-03. Baseline: `d4af2e9`.

## Result

Capturing the workspace base does not improve the measured builder. The
frame-backed aligned/bounded O2 candidate grows from 5,200 to 5,232 text bytes
and from a 400 to 408-byte core direct-call frame bound. The packed/bounded
candidate grows from 5,184 to 5,200 bytes, with its bound unchanged at 408.
O1 also fails to improve. Do not promote this source shape as an optimization.

The experiment remains opt-in and reproducible. Exact production Init assembly,
default candidate instruction bytes and README aggregates stay unchanged.
Separately pending Game changes remain outside this checkpoint.

## Source Shape and Domain

`INIT_DECODE_CACHE_WORKSPACE` captures `s->workspace` after the zero-count
return and uses that local pointer for builder link, parent and leaf stores.
Allocation count updates, frame table metadata and output ordering remain in
their previous source positions. Other decoder functions retain their original
workspace access. No `restrict`, guest pointer reinterpretation or production
adapter is introduced.

The trial requires a stable workspace pointer throughout the call. Caller
outputs, scratch writes and workspace writes must not alias and mutate that
pointer cell. This is an explicit experimental assumption, not a newly proven
production ownership fact. The existing valid-array, sufficient-storage,
coherent-scratch and bounded-shift domains still apply where selected.

The driver adds `--cache-workspace` and a distinct `-cached-workspace` output
suffix; all other options/defaults remain unchanged. Combinations with earlier
array caching and flat bit helpers are not qualified here.

## Guest Measurements

All values are fresh IDO compiles; text and call-frame bounds are bytes. Bounds
exclude caller state/scratch, exception context and original-entry adapter.

| Representation / mode | Uncached O2 text / bound | Cached O2 text / bound | Uncached O1 text / bound | Cached O1 text / bound |
| --- | ---: | ---: | ---: | ---: |
| Embedded baseline | 4,928 / 456 | 4,928 / 464 | 5,328 / 344 | 5,344 / 352 |
| Embedded aligned + bounded | 4,800 / 440 | 4,800 / 448 | 5,152 / 312 | 5,152 / 312 |
| Embedded packed + bounded | 4,784 / 440 | 4,784 / 448 | 5,168 / 312 | 5,184 / 320 |
| Frame-backed baseline | 5,312 / 416 | 5,344 / 424 | 5,600 / 328 | 5,616 / 336 |
| Frame-backed aligned + bounded | 5,200 / 400 | 5,232 / 408 | 5,424 / 296 | 5,440 / 296 |
| Frame-backed packed + bounded | 5,184 / 408 | 5,200 / 408 | 5,440 / 296 | 5,456 / 304 |

Frame-backed cached builder O2/O1 body words and frames:

| Mode | O2 words / frame | O1 words / frame |
| --- | ---: | ---: |
| Baseline | 648 / 216 | 611 / 136 |
| Aligned + bounded | 619 / 200 | 567 / 96 |
| Packed + bounded | 613 / 200 | 572 / 104 |

Aligned/packed variants retain zero builder `swl`/`swr` opcode forms; baseline
retains one of each. Workspace capture is not an entry-alignment change.

## Instruction Evidence

In aligned/bounded frame-backed O2, both objects keep the state pointer in `s0`.
The uncached builder has four static `lw ...,8(s0)` instructions; cached has one.
However, builder `lw ...,offset(sp)` count grows from 35 to 45, and
`sw ...,offset(sp)` count grows from 21 to 23. Its frame grows from 192 to 200
bytes and body from 612 to 619 words. This confirms fewer state-field loads
without a net size/stack benefit. Static opcode counts do not prove dynamic
execution frequency or instruction-by-instruction spill causality.

Do not reuse the `s0` field-load count for O1: that profile uses a different
state access shape. O1's measured frame/text receipts remain independently valid.

## Qualification

Five native classes cover uncached-shift embedded/frame-backed workspace
capture, frame-backed aligned/bounded capture, frame-backed packed/bounded
capture, and sanitized frame-backed packed/bounded capture. All 78 focused
tests pass in 48.353 seconds, including 2,535 retail page calls and 145 generated
tree comparisons against the assembly interpreter. Physical-frame checks are
inherited for every frame-backed class.

The guest matrix additionally measures embedded aligned/packed combinations;
those two combinations have guest codegen receipts but no dedicated native
combination classes in this checkpoint. Do not imply that compiling them alone
qualifies their semantics. Neither native output tests nor guest compilation
prove MIPS scheduling, full exception behavior or original-entry hardware ABI.

Sixteen guest compiles pass: twelve cached variants plus four default
representation/profile controls. Every compiler log is independently checked
empty. The four freshly compiled default `.text` byte sequences equal the
pre-edit object text, not merely their lengths. Root `make tools-check` passes.

Final verification: all 905 project tool tests pass in 303.156 seconds. The
suite's twenty-five native retail corpus methods execute 12,675 page calls;
this remains native semantic evidence, not hardware execution. Both changed/new
Python modules pass syntax checks, and `git diff --check` passes. No production
build, original-entry adapter or gameplay run is claimed.

## Reproduction

From the repository root in WSL:

```sh
python3 -m unittest tools.tests.test_init_decompressor_cached_workspace -q
python3 tools/experiments/compile_init_decompressor.py --cache-workspace
python3 tools/experiments/compile_init_decompressor.py --frame-backed --cache-workspace
python3 tools/experiments/compile_init_decompressor.py --frame-backed --aligned-entry --bounded-builder-shifts --cache-workspace
python3 tools/experiments/compile_init_decompressor.py --frame-backed --packed-entry --bounded-builder-shifts --cache-workspace
```

## Next

Reject workspace caching as the current size/stack lead. Retain the uncached
aligned/bounded frame-backed reference for lower stack demand and uncached
packed/bounded for smaller O2 text. Next investigate builder address/index
translation or shorten overlapping scalar lifetimes using the retail register
ledger, rather than capturing another long-lived base without evidence.
Production replacement still requires storage ownership, original-entry ABI
and fitting code layout.
