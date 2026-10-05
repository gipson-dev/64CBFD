# Game Caller-Buffer Resource Loader And Syscall Boundary

Date: 2026-10-05. Starting HEAD: `81255fe4`.

## Result And Scope

`func_1502B224`'s false zero-return placeholder is replaced with its semantic
raw/compressed resource loader into a caller-supplied buffer. All **75 words /
300 bytes and the original 0x30 frame emit directly from default IDO O2/g3**.
No expected-word guards, profile overrides, insertion/omission, extra padding
or data-layout change is introduced. Its declaration now describes four real
arguments and a 32-bit returned count rather than the empty-argument stub.

Source: `conker/src/game_57FA0.c`; entry/end `0x1502B224..0x1502B350`;
ROM `conker/conker.us.bin+0x586D4..0x58800`.
Complete raw/linked/retail SHA-256:
`a19404b10321ccddb4e281f6712c201be4aa66052e2021d3e48082b8740257d1`.

The shared patch table is untouched: 10595 rows, no new loader rows. Init,
Debugger, other Game source and the sibling PC port are not edited.

## Recovered Contract

The low 28 descriptor bits are rounded up to an even count. A nonzero cap
replaces that count only when smaller, using an unsigned comparison. An odd
cap remains odd; only DMA length is subsequently rounded up to 16 bytes.
The source address is passed through unchanged, without a new alignment fix.

Compression is selected exactly when `(descriptor & 0x70000000) == 0x10000000`;
bit 31 does not affect that test. Other flag combinations DMA directly into
the supplied buffer and return the capped/even count, not the DMA status or
16-byte-rounded transfer length. Zero count still submits zero-length DMA.

Compressed mode allocates that count with `(1, 2, 2)`. Allocation failure
returns zero without DMA, destination reads, decoding, error submission or
freeing. There is no second output allocation: destination belongs to the
caller. The DMA status is ignored here as in retail.

After loading, the first temporary-buffer word is masked to 31 bits and
captured before the decoder can mutate it. D_8003809C is read live after DMA
and passed to `func_10006240`. The returned low 32-bit count is retained for
comparison and eventual return, including zero/negative signed decoder
results. There is no synthesized output-size limit or fallback.

A mismatch stores `0x0C000036` to D_8003C8E0 in the error-call delay slot, then
calls `func_150AD770`. The following instructions free the temporary buffer
and return the retained decoded count **if that handler returns**. Equal-size
decodes reach cleanup directly. Callback modifications of scratch/header/error
state must not replace the captured header or retained decoded count.

## Compiler Screen

The [22-form source screen](../../tools/experiments/game_buffer_resource_loader_candidates.py)
uses fixed retail relocations and the ordinary O2/g3 profile. All candidates
compile without isolated diagnostics. The original three-word/no-frame
placeholder differs across all 75 slot words. Initial semantic C has 75 words
but a 0x28 frame and ten differences.

Declaration order `amount, compressed, expanded` puts the captured header at
sp+0x24 and recovers the complete 0x30 frame and all words. The alternate
`compressed, amount, expanded` order is also direct-exact. Other declaration
orders, register hints, nested/reversed/ternary cap forms and allocation-in-
condition controls remain nonmatching; the raw-first branch layout has 52
differences. The selected routine needs no register hint.

All ten unlinked relocations are retained: allocation at 0x68, DMA at 0x98
and 0x10C, scratch HI16/LO16 at 0xAC/0xB8, decode at 0xC0, error-word
HI16/LO16 at 0xDC/0xE4, error call at 0xE0 and free at 0xE8. No patch-table
entry exists for this function.

## Qualification

The [eleven-check module](../../tools/tests/test_game_buffer_resource_loader.py)
pins complete direct/linked identity and hash, original frame, source-shape
controls, all relocations, absence of guards and native/connected behavior.

- 5120 native actual-C boundary cases cover all 16 high-flag combinations,
  ten low lengths including 28-bit maxima, eight caps including unsigned
  extremes, allocation failure and equal/zero/negative decoder results.
  Call arguments/counts/order are checked independently. Raw bounded DMA
  effects and unchanged surrounding destination words are also checked.
- 112 native captured-header cases cover zero/high-bit/31-bit/large headers,
  seven decoder results and ordinary/temporary-alias destinations. Decoder,
  error and cleanup hooks mutate live state while the captured header and
  returned count stay intact. No real decoder alias-support claim is made.
- A native failed-allocation control passes a NULL destination and requires
  allocation-only behavior with the destination storage untouched.
- 6912 two-way retail/raw instruction cases cover flag/length/cap boundaries,
  both valid N64 stack phases, allocation failure, success and mismatch. All
  75 words are visited in both forms. Complete mapped memory including
  private frames, ordered reads/stores/events, call arguments, return and
  saved-register lifetime agree exactly; no event commutation is allowed.
- 120 two-way destination-alias/live-scratch cases cover ordinary buffers,
  caller stack, temporary header, scratch and error-word outputs with varied
  captured headers and decoder results. These qualify the caller body under
  explicit opaque decoder effects, not allocator ownership or real decoding.
- 600 connected retail `func_1502B8E0` caller cases execute the actual freshly
  compiled loader and checked lookup/cache bodies. Depths 1..5, every missing
  descriptor position, raw/compressed/bit-31 flags, five caps and both stack
  phases preserve lookup counts, resolved base, full descriptor and returned
  count. All 53 retail caller words are visited. Its source is not yet recovered.
- Ten zero-depth caller cases seed the incoming descriptor word at caller
  entry SP-0x14. No lookup runs; the actual retail caller still passes that
  seed to the loader. Seeds select different raw/compressed lengths and
  results. This is bounded incoming-frame evidence, not a defined C local.

Large DMA/allocation lengths in the boundary matrices qualify arguments and
control only. DMA hooks write complete synthetic payloads only for lengths
up to 64 bytes; larger transfers are not performed or extent-qualified.
Zero-length compressed cases have explicitly initialized, mapped temporary
storage supplied by the fixture, not proof of actual zero-byte allocation
or valid asset layout. Native GCC is 32-bit with warnings as errors and the
existing `-fno-strict-aliasing` byte-buffer convention.

## Real Error Boundary

Retail `func_150AD770` is the handwritten `syscall 0` at ROM 0xDAC20, not an
ordinary returning cleanup callback. Forty separate two-way mismatch-prefix
cases stop before entering that helper. They require the exact error word,
retained decoded count, return address and complete memory/event prefix,
with no free yet executed. The original syscall word is pinned from the ROM.
Read-only inspection of the current linked helper also confirms the original
`0x0000000C` syscall and three trailing zero words at 0x150AD770.

Returning error hooks in the other corpora exercise only the conditional
continuation instructions. They do not qualify exception handling, syscall
recovery, actual post-trap cleanup or return in the game. No handwritten
error-handler conversion, allocator, DMA or decoder implementation is added.
Hardware, real assets, arbitrary buffer extents/alignment, PC runtime and
rendering remain separate acceptance boundaries.

## Measured Progress

The rebuilt owner and final ELF report:

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3296 / 5463 (60.33%) | 0 | 2167 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2623 / 4790 (54.76%) | 0 | 2167 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversion counts remain unchanged because the placeholder was already C.
The 47 retained Init ASM functions are untouched. README changes contain
aggregate counts only; recovery narration stays in dedicated docs. Existing
duplicate generated-slice recipe warnings remain; the changed owner and
isolated candidates compile without diagnostics. `make tools-check` passes.
The final combined suite passes **221 tests in 161.605 seconds, no skips**,
against the rebuilt ELF. Protected Init code (164048 bytes), Init data
(17376 bytes), Debugger code and Game data (189088 bytes / 720 owners) remain
byte-exact. Earlier connected resource, alias and source-shape gates pass.

## Reproduction

Run from the `64CBFD` root in PowerShell:

```powershell
wsl python3 -m tools.experiments.game_buffer_resource_loader_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_buffer_resource_loader tools.tests.test_game_variadic_table_address_match tools.tests.test_game_variadic_table_range_match tools.tests.test_game_table_range_loader tools.tests.test_game_cached_lookup_match tools.tests.test_game_cache_installer_match tools.tests.test_game_cache_installer_candidates tools.tests.test_game_block_loader_direct_match tools.tests.test_game_offset_relocator_match tools.tests.test_game_attachment_cursor_match tools.tests.test_game_resource_helper_schedule tools.tests.test_game_extended_child_constructor tools.tests.test_game_variadic_resource_loader tools.tests.test_game_asset_table_lookup_and_block_load tools.tests.test_game_texture_resource_setup tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
wsl make tools-check
git diff --check
```

## Host Boundary And Next

Read-only sibling inspection finds translated retail `func_1502B224` at
`64CBFDOGL/recomp_out/.c:203175`, with its original frame/cap compare, captured
header, live scratch read, error-store delay slot and cleanup sequence already
present. No maintained `src/pc` override/reference is found. No host
synchronization is needed for this matching change. No sibling source, build,
save or frozen Release artifact is modified.

Next connected source target: `func_1502B8E0`, still a zero-return placeholder,
53 retail words / frame 0x48. Its zero-depth path forwards an incoming private-
frame descriptor without writing it. Preserve that verified seed dependency;
do not replace it with a convenient zero/one initialization or discard the
zero-depth cases to obtain a nominally matching C recovery.
