# Init Stream Masked Dispatch And Buffered Byte Rewind Fitting

Date: 2026-10-03. Baseline: `222c871`.

## Result

Two opt-in stream changes together reduce the best packed O2 core to 4,512
bytes, or 4,832 with the unchanged 320-byte adapter. The retail group is
3,984 bytes, leaving 848 bytes to remove, down from Note 848's 864.
All qualified profiles retain their existing stack bounds.

`--stream-masked-dispatch` selects block types from `header & 6`, with cases
0/2/4 corresponding to stored/fixed/dynamic. This replaces the shift/mask
and cases 0/1/2, preserving final-bit handling and invalid-block status 2.
In particular, the fixed block still ignores the compressed decoder's status,
restores workspace/address and reports status zero, as characterized earlier.

`--stream-byte-rewind` retains the signed `bits >= 8` guard but computes the
unread byte count with `(uint32_t)bits >> 3`, stores `bits & 7` and subtracts
the count from the input pointer. For the guarded nonnegative bit count,
these final values equal the old repeated subtraction/decrement loop. Original
dispatch and rewind remain the defaults. Store timing/count inside this C
state changes; asynchronous intermediate-state equivalence is not claimed.

## Trials

Packed trials extend the qualified histogram plus fixed-literal-cursor flags:

| Trial | O2 core text | O1 core text |
| --- | ---: | ---: |
| Note 848 baseline | 4,528 | 5,968 |
| Distance cursor plus literal cursor, rejected | 4,528 | 5,984 |
| Distance cursor plus literal/arithmetic operation, size-only | 4,528 | 5,952 |
| Early stream error returns, rejected | 4,528 | 5,984 |
| Early errors plus arithmetic operation, size-only | 4,528 | 5,952 |
| Masked dispatch alone | 4,528 | 5,952 |
| Byte rewind alone | 4,528 | 5,952 |
| Masked dispatch plus byte rewind, qualified | 4,512 | 5,952 |
| Both plus arithmetic operation, size-only | 4,512 | 5,920 |

Distance cursor without the literal cursor also measured 4,544/5,936 versus
histogram-only 4,544/5,920. Rejected distance/early-error flags and source
branches are removed. No semantic qualification is assigned to those trials
or the new arithmetic-operation combinations.

Ignored receipts remain under `conker/build/init-distance-cursor-*`,
`init-stream-early-errors-*`, `init-stream-masked-dispatch-*` and
`init-stream-rewind-*`, all suffixed `-20261003`.

Packed O2 stream body shrinks from 83 to 79 words with the combined flags;
core body/slot remain 60/60. Separately, masked dispatch saves one body word
but adds one final padding word; rewind saves three but adds three padding
words. Together all four words survive into linked text. O1 stream body
shrinks 98 to 93, with core slot growing 91 to 92: net four words saved.

## Qualified Costs

All final builds retain 116-byte state and a 320-byte adapter:

| Shape/profile | Linked text | Static total bound | Observed descent |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 6,080 | 3,280 | 3,280 |
| Frame O1 | 6,464 | 3,200 | 3,200 |
| Aligned/end O2/g3 | 4,864 | 3,240 | 3,240 |
| Aligned/end O1 | 6,256 | 3,176 | 3,176 |
| Packed/remaining O2/g3 | 4,832 | 3,256 | 3,256 |
| Packed/remaining O1 | 6,272 | 3,192 | 3,192 |

All six linked images shrink 16 bytes relative to Note 848, with unchanged
stack bounds. Packed core-only bounds remain 408/O2 and 344/O1; O2 retains
minimum SP `0x80031D58`, 72 bytes above the known protected neighbor.
Neither that fence nor these tests prove complete reservation ownership.

## Verification And Active Rewind Gate

The inherited tests pass 420 bounded stream/context comparisons, 114 direct
builder comparisons and six exact fixed-initializer comparisons. The latter
retain the 318-store sequence, all 2,632 table bytes, roots/allocation and
frame/workspace guards. Nested lookup still records 3,212 calls / 3,383
iterations on page 169.

The initial rewind probe used retail pages 0/169/506 and 1..8, but none entered
the compiled rewind store. Its execution-gate assertion failed; that was
missing path coverage, not a decoder mismatch. It was replaced with a valid
constructed dynamic stream: 256 literal codes of width nine, end code of
width one, a complete code-length tree and one distance code of width one.
The stream emits `A` followed by end-of-block and explicit lookahead bytes.
Zlib independently verifies the output.

Twelve additional paired context comparisons pass for this stream across all
six builds and both masked CU1 modes. Total bounded stream/context comparisons
are now 432 for this variant. A separate packed O2 instruction gate proves
the actual rewind store executes once: 11 buffered bits, one byte unread,
three bits remaining. It identifies the stream's count shift, branch guard,
pointer subtraction and input store; a delay-slot shift visit alone is not
accepted as proof. Snapshots verify the count, pointer subtraction and final
bit state. This is constructed coverage, not natural retail-page coverage.

Terminal commands:

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_stream_fitting
wsl python3 -m unittest tools.tests.test_init_decompressor_stream_fitting.InitDecompressorStreamFittingTests.test_byte_rewind_path_is_exercised
```

The first run loaded the module before the new gate was added: 17 tests in
202.434 seconds, 16 pass and one intentional corpus skip. The final gate
passes separately in 6.353 seconds. Combined: 17 pass, one skip. Fresh compile
and link logs are empty. Root `make tools-check` and `git diff --check` pass.

No production build, ordinary full-suite, changed full corpus, hardware replay
or sibling-port test is claimed. Earlier full-corpus receipts are not
reassigned to these changed opt-in images.

## Next

- [x] Measure and remove unsuccessful distance-cursor/early-error branches.
- [x] Retain a real linked reduction from combined dispatch/rewind fitting.
- [x] Qualify bounded contexts, exact initializer and an active rewind path.
- [ ] Continue fitting; 848 linked bytes still exceed retail capacity.
- [ ] Changed full corpus in both masked CU1 modes before promotion.
- [ ] Other-profile corpus and remaining ownership/hardware/resume gates.

The opt-in full-corpus class is `InitDecompressorStreamFittingCorpusTests` in
`tools.tests.test_init_decompressor_stream_fitting`, with the same environment
selectors documented in Note 848. It was not run here. Production Init,
adapter assembly, default flags and README totals remain unchanged.
Unrelated Game edits are preserved and excluded from this checkpoint.
