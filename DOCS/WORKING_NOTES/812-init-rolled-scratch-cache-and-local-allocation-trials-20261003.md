# Init Rolled Scratch Cache and Local Allocation Trials

Date: 2026-10-03. Baseline: `d1b4cc4`.

## Result

With the no-unroll profile, packed/bounded entries plus either scratch-cache
mode reduce frame-backed O2 text from 4,256 to 4,224 bytes. This is 240 bytes
over the 3,984-byte retail region. The core direct-call frame bound increases
from 392 to 400 bytes. Aligned/bounded with counts/offsets caching reaches
4,240 bytes with a 392-byte bound, compared with uncached 4,256/384.

The smallest text is now 4,224 bytes; uncached aligned/bounded remains the
lower-stack lead at 4,256/384. These are measured tradeoffs, not replacements
for the exact production assembly. Individual slot fitting and original-entry
ABI/storage ownership remain open; README aggregates do not change.

A new local allocation-cursor trial does not improve the rolled candidate.
It stays opt-in and is not the fitting lead. Separately pending Game changes
remain outside this checkpoint.

## Rolled Scratch Cache Matrix

All rows use physical frame scratch and `--no-unroll`. Text/frame bounds are
bytes. Bounds exclude caller state, `0xA88` scratch, exception context and any
entry adapter. Cache `all` holds counts, sorted and offsets bases; cache
`counts-offsets` leaves sorted accesses in their original form.

| Entry / cache | O2 text | O2 builder frame | O2 core bound | O1 text | O1 builder frame | O1 core bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aligned / none | 4,256 | 176 | 384 | 5,424 | 96 | 296 |
| Aligned / all | 4,256 | 192 | 400 | 5,424 | 104 | 304 |
| Aligned / counts-offsets | 4,240 | 184 | 392 | 5,424 | 104 | 304 |
| Packed / none | 4,256 | 184 | 392 | 5,440 | 96 | 296 |
| Packed / all | 4,224 | 192 | 400 | 5,456 | 112 | 312 |
| Packed / counts-offsets | 4,224 | 192 | 400 | 5,440 | 104 | 304 |

The two packed cached O2 builders both emit 413 words. Counts/offsets caching
is the preferable O1 comparison of the two, but it does not recover the
uncached O1 stack bound. Do not label either cache mode an across-profile win.

## Local Allocation Cursor

Retail keeps allocation count in low-word FPU state. The new
`INIT_DECODE_LOCAL_ALLOCATED` source trial captures the candidate's count just
before entry emission, after zero-count/all-zero returns and scratch setup.
It uses that local for link indexing and cursor advancement, and commits
`s->allocated` immediately at each table allocation at the previous update
position. It does not defer state updates until function return.

The trial requires the allocation-count field not to be mutated by aliased
workspace, frame or caller-output writes. That stable-field assumption is
explicit and is not a proven original-entry ownership fact. General valid-array,
sufficient-capacity and coherent-scratch boundaries still apply. No `restrict`,
FP-register ABI or new production entry adapter is introduced.

The driver adds `--local-allocated` with separate `-local-allocated` outputs.
No default source shape/profile/output is changed.

| Entry / profile shape, local cursor selected | O2 text | O2 builder frame | O2 core bound | O1 text | O1 builder frame | O1 core bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aligned / normal unrolling | 5,200 | 192 | 400 | 5,440 | 96 | 296 |
| Aligned / no unroll | 4,272 | 176 | 384 | 5,440 | 96 | 296 |
| Packed / normal unrolling | 5,168 | 200 | 408 | 5,456 | 104 | 304 |
| Packed / no unroll | 4,256 | 184 | 392 | 5,456 | 104 | 304 |

There is a sixteen-byte text saving in the unrolled packed O2 shape, but no
rolled benefit. The rolled aligned case grows sixteen bytes; O1 also grows.
Do not promote this trial as an optimization of the current fitting lead.

## Individual Slot Ledger

The smallest measured O2 object is packed/bounded, no-unroll, counts/offsets
cached, without a local cursor. Retail slot counts come from the actual
`init_5AB0.s` bodies and alignment; C counts come from the fresh object slot
receipt. Fixed setup has 75 instructions plus two alignment NOPs at
`0x100071C8`/`0x100071CC`, giving its 77-word available slot.

| Retail routine / region | Retail words | C slot words | C minus retail |
| --- | ---: | ---: | ---: |
| Core `func_1000625C` | 52 | 49 | -3 |
| Stream/dispatch `func_1000632C` + `func_10006380` | 62 | 78 | +16 |
| Compressed decoder `func_10006424` | 257 | 100 | -157 |
| Stored decoder `func_10006828` | 65 | 55 | -10 |
| Builder `func_1000696C` | 293 | 413 | +120 |
| Dynamic decoder `func_10006E00` | 167 | 224 | +57 |
| Fixed tables `func_1000709C` | 77 | 82 | +5 |
| Original entry wrapper `func_10006240` | 7 | Not emitted | -7 |
| Original builder wrapper `func_1000692C` | 16 | Not emitted | -16 |
| New leading C helper region | 0 | 55 | +55 |
| Total | 996 | 1,056 | +60 |

The core body is 48 words; its 49-word slot includes one trailing padding word.
The original wrappers are absent as distinct ABI implementations, not recovered
zero-length equivalents. Stream and dispatch are combined in the C routine;
this accounting is not a claim that each original entry address is preserved.

Sixty words exactly account for the 240-byte net excess. Builder/dynamic/fixed
and merged stream slots still overflow even though compressed/stored slots are
smaller. An aggregate fit alone would not establish exact-slot restoration,
preserved internal entries or space for the missing entry adapter.

## Semantic Qualification

Six new native classes cover aligned/bounded cached counts/offsets, packed
cached counts/offsets, packed cached all, aligned local allocation, packed local
allocation and sanitized packed local allocation. All 102 focused tests pass
in 63.334 seconds, including 3,042 native retail page calls and 174 generated
tree comparisons against the assembly interpreter. Physical scratch/layout
checks are inherited by every class.

Aligned cached-all has a guest codegen receipt but no new dedicated native
combination class. Local-cursor plus cache/byte-parent/flat-helper combinations
are not newly qualified. Native GCC tests do not execute IDO objects or prove
MIPS scheduling, exception hardware, DMA/cache ownership or original-entry ABI.

Twenty-four post-edit guest compiles pass: eight unchanged controls, eight
rolled scratch-cache combinations, and eight local-cursor combinations. All
compiler logs are independently checked empty. The eight controls retain their
pre-edit `.text` SHA-256 hashes, including both representations' default
profiles and the two rolled combined entry shapes. Initial pre-edit cache
measurements were repeated after the source change.

## Final Verification

- All 1,078 project tool tests pass in 418.406 seconds.
- All 102 focused combination/local-cursor tests pass in 63.334 seconds.
- Thirty-five native corpus methods execute 17,745 retail page calls.
- Twenty-four post-edit guest objects compile with empty logs; eight control
  text hashes are unchanged.
- The retail/C slot ledger is independently checked: 994 retail body words
  plus two alignment words versus 1,001 C named-slot words plus 55 helper words.
  Both retail alignment NOPs are also checked in the pristine linked image.
- Root `make tools-check`, two Python syntax checks and `git diff --check` pass.
- No production build, original-entry adapter or hardware/gameplay run is claimed.

## Reproduction

From the repository root in WSL:

```sh
python3 -m unittest tools.tests.test_init_decompressor_rolled_builder_state -q
python3 tools/experiments/compile_init_decompressor.py --frame-backed --packed-entry --bounded-builder-shifts --no-unroll --cache-builder counts-offsets
python3 tools/experiments/compile_init_decompressor.py --frame-backed --aligned-entry --bounded-builder-shifts --no-unroll --cache-builder counts-offsets
python3 tools/experiments/compile_init_decompressor.py --frame-backed --packed-entry --bounded-builder-shifts --no-unroll --local-allocated
```

## Next

Retain both size and stack leads. Use the per-routine ledger to investigate
the dynamic decoder's 57-word excess and rolled builder's 120-word excess,
without assuming that spare compressed-decoder space resolves entry layout.
Reject local allocation capture as the rolled fitting direction. Preserve the
exact production baseline until code layout, original-entry ABI and storage
ownership are independently qualified.
