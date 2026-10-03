# Init Shadow Fitting Trials And Helper Attribution

Date: 2026-10-03. Baseline: `98026ef`.

## Decision

Five isolated source/profile hypotheses do not reduce the smallest shadow
decoder's O2 text. Reject the temporary leaf/snapshot cursor changes; retain
the existing source and six-profile qualification baseline. No production
conversion, new semantic qualification, or fitting improvement is claimed.

The useful next fitting target is the builder's actual control flow and the
separate shared helpers/adapter, not the misleading combined builder slot.
The current combined text remains 4,896 bytes, 912 over retail's 3,984 bytes.

## Fresh Size Receipts

All rows use the frame-backed packed/remaining shape with ABI FPR shadow:

```powershell
wsl python3 tools/experiments/compile_init_decompressor.py --output conker/build/init-shadow-fitting-20261003 --frame-backed --packed-entry --bounded-builder-shifts --no-unroll --bounded-length-scan --dynamic-cursor --cache-builder counts-offsets --builder-symbol-cursor remaining --abi-fpr-shadow
```

The following are core object text bytes, excluding the unchanged 320-byte
shadow adapter. The bound is the compiler receipt's direct-call frame sum
from `init_decode_core`, excluding the physical frame and adapter area. It is
not a newly observed runtime stack descent.

| Trial | O2/g3 text | O1 text | O2 builder ledger words | O2 core frame bound |
| --- | ---: | ---: | ---: | ---: |
| Existing baseline | 4,576 | 5,984 | 424 | 408 |
| Leaf pointer cursor | 4,656 | 6,016 | 442 | 424 |
| Cache workspace (`--cache-workspace`) | 4,592 | 5,984 | 428 | 416 |
| Local allocation (`--local-allocated`) | 4,624 | 5,984 | 434 | 408 |
| Snapshot capture pointer copy | 4,576 | 6,000 | 424 | 408 |
| Both snapshot copies pointer-bounded | 4,592 | 6,032 | 424 | 400 |

All fourteen compiler logs (six trial/baseline pairs plus restored-baseline
pair) are empty. Measurements are under ignored `conker/build/` directories:
`init-shadow-{fitting,leaf-cursor,cached-workspace,local-allocated,copy-cursor,copy-cursor-both,fitting-restored}-20261003`.
These are local disposable compiler receipts, not tracked release artifacts.

The rejected source hypotheses were:

- Leaf cursor: capture the leaf table/end and stride, then replace
  `leafTable[next]`/`next += stride` with a do/while pointer store/advance
  terminating at `leafCursor < leafEnd`. The temporary selector implied
  leaf-table caching. Both profiles grow; the flag and source branch are removed.
- Capture copy: replace the six-element indexed `abiSaved` to `abiFpr + 2`
  copy with source/destination pointers, stopping at `abiSaved + 6`.
  O2 text is flat, O1 grows. No reduction survives text alignment.
- Both copies: additionally use pointer bounds for the initial six saved
  registers copied from the physical frame into `abiSaved`. O2's static
  frame bound falls eight bytes, but both text profiles grow. Neither copy
  branch nor its temporary selector remains in the source.

These are compile/size experiments only. No execution equivalence is claimed
for rejected variants. In particular, pointer bounds would require their own
validity/aliasing qualification if reconsidered. Existing cache-workspace and
local-allocation options remain available, unchanged and not newly selected
by the default profiles.

## Correct Helper Attribution

The O2 receipt places two unnamed helpers between the builder and compressed
decoder, so the named builder ledger includes them:

| Unit | Words | Bytes |
| --- | ---: | ---: |
| Actual `init_decode_build` public unit | 346 | 1,384 |
| Capture helper at object offset 0x644 | 22 | 88 |
| Lookup helper at object offset 0x69C | 56 | 224 |
| Combined builder ledger | 424 | 1,696 |

The disassembly identifies the capture helper by its writes to ABI snapshot
state and the lookup helper by its bit-buffer/table traversal. These offsets
are relocatable object offsets, not production addresses. The retail builder
is 293 words, so the actual builder's excess is 53 words/212 bytes, not the
131 words/524 bytes obtained by attributing both helpers to that body.

An accounting reconciliation for the baseline is:

- Seven actual public C units: 1,011 words / 4,044 bytes.
- All unnamed helpers: 133 words / 532 bytes (including the 78 above).
- Core object text: 1,144 words / 4,576 bytes.
- Shadow adapter: 80 words / 320 bytes; combined 4,896 bytes.
- Retail group: 973 named-body words plus 23 wrapper words = 996 / 3,984 bytes.
- Combined excess: 152 public-body bytes + 532 helper bytes - 92 retail-wrapper
  bytes + 320 adapter bytes = 912 bytes.

This is size attribution, not instruction matching, a removable-helper proof,
or permission to omit ABI/context behavior. The helpers are shared; folding
them may duplicate code. Any fitting change must preserve recovered scratch
history and the retail wrapper contract.

## Restored Baseline And Next

The compiler script and semantic decoder have no Git diff after removing the
task's experimental edits. Fresh restored compilation produces the same
4,576/5,984 text sizes. O1 objects compare equal in full. O2 objects differ
outside the `.text` comparison; extracted `.text` compares equal byte-for-byte:

```text
O2 .text SHA-256: 146c91334708247c406d7882ec8c2f8b181bda36a7fc1cb6f15d53a25a7e4ebc
```

No fresh corpus, bounded shadow suite, production build, hardware or gameplay
test is claimed. [Note 827](827-init-full-masked-shadow-corpus-20261003.md)
remains the masked 507-page receipt for the unchanged selected profile.
README totals and pending Game work are untouched.
Root `make tools-check` and `git diff --check` pass after the documentation update.

Next inspect the actual builder's register spills/parent-table control flow
and shared bit/lookup helper costs with a new specific hypothesis. Do not
repeat these five trials as though they reduced text. Other full-corpus
profiles/CU1-clear, complete storage ownership, synchronous faults, and fitting
remain open before production conversion.
