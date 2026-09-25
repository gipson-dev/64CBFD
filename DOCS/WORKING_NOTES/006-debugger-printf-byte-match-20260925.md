# Debugger `_Printf` Byte Match - 2026-09-25

## Scope

Complete `func_16001BB4` without replacing its restored SDK `_Printf` C body
with another `GLOBAL_ASM` fallback. Preserve unrelated work and verify the
result against the linked US retail bytes.

## Measured boundary

The maintained macro-shaped C in `src/debugger_257350.c` compiles to 401 words
(`0x644` bytes). Retail is 402 words (`0x648` bytes). The bodies agreed through
the final `_PAD` loop except for IDO's interlocked tail scheduling choice:

- retail converts the first width guard to `beqzl`;
- its likely delay slot computes `fmt_ptr + 1`;
- a shared increment block precedes the loop back edge;
- the back-edge delay slot preloads the next format byte;
- inserting that preload moves the epilogue and changes ten forward exits.

Source variants using `while`, `for` increments, direct macro conditions, and
an explicit outer flag guard all compiled to the same 401-word schedule. This
confirmed a compiler scheduling boundary rather than missing formatter logic.

## Implementation

`tools/pad_c_object.py` now accepts an optional `insert_after` word on a
guarded patch row. The tool verifies the compiled input word, counts the
insertion inside the function, and rejects an insertion that would exceed the
retail slot. Existing replacement and relocation checks are unchanged.

`conker/retail_word_patches.us.csv` records the `_Printf` tail transformation:
four scheduling replacements, one inserted `lbu s0, 0(a3)`, and ten guarded
forward-branch displacement updates. The back edge targets `+0x64`, bypassing
the old loop-top load because the inserted delay slot already performed it.

An assembler-backed unit fixture verifies that an inserted scheduling word
increases the patched function size and leaves the following symbol at its
retail address. The debugger object explicitly depends on the patch table so a
patch change cannot leave a stale object.

## Verification

Passed from the `64CBFD` checkout:

```sh
python3 -m unittest tools.tests.test_pad_c_object_word_patches
make -C conker replace NON_MATCHING=1 -j4
make tools-check
make NON_MATCHING=1 -j4
make -C conker match-progress NON_MATCHING=1
```

Direct linked comparison at debugger offset `0x1BB4` reports 402 compared
words and zero differences. The linked matcher reports:

- total: `2523 / 5497 (45.90%)`, one address-drift blocker, 2,973 different;
- debugger: `177 / 181 (97.79%)`, no blockers, four different.

The remaining debugger order is `func_16000590` (52 real differences),
`func_16001044` (151), `func_1600078C` (180), and `func_16000B14` (277).

## Sibling audit

`64CBFDOGL` contains generated recomp translations of `func_16001BB4`, not the
decomp C object-padding pipeline. The scheduling normalization is therefore
not applicable to its host source. Its dirty worktree was left untouched, and
the frozen Release configuration was neither built nor launched.

## Resume boundary

Continue with `func_16000590`. Its 79-word body has the intended logic and loop
shape; focus first on the original context-pointer lifetime and saved-register
allocation represented by its 52 linked differences.
