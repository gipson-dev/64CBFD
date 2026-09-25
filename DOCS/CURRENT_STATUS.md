# Current Decomp Status

Last verified: 2026-09-24

This page is the short, current handoff for `64CBFD`. Historical experiments
remain in [WORKING_NOTES.md](WORKING_NOTES.md); detailed session handoffs live
under [WORKING_NOTES/](WORKING_NOTES/).

## Repository state

- Branch: `master`
- The restoration baseline is banked in coherent commits beginning after
  `2ed3523` (`tool updates`): generated-slice assembly support, restored guest
  routines, OGL reference tooling, RGBA5551 tooling, and documentation.
- Before checkpointing, `git status --short` reported 123 changed tracked paths
  and 37 untracked paths. The empty personal `DOCS/user notes.md` remains
  preserved locally and excluded through `.git/info/exclude`.
- The broad assembly restoration in the current tree is buildable, but it
  reduced the number of functions represented in C. It improves original-code
  coverage and port support; it is not C-decomp completion.

## Measured progress

Fresh `progress.csv` and linked retail comparison on 2026-09-24:

| Section | C functions | Raw assembly | C bytes |
| --- | ---: | ---: | ---: |
| Total | 5,497 / 6,038 (91.04%) | 541 | 1,933,296 / 2,256,728 (85.67%) |
| Init | 508 / 538 (94.42%) | 30 | 148,936 / 164,048 (90.79%) |
| Game | 4,808 / 5,318 (90.41%) | 510 | 1,764,720 / 2,072,880 (85.13%) |
| Debugger | 181 / 182 (99.45%) | 1 | 19,640 / 19,800 (99.19%) |

| Section | Byte-exact C | Address drift | Different C |
| --- | ---: | ---: | ---: |
| Total | 2,522 / 5,497 (45.88%) | 1 | 2,974 |
| Init | 387 / 508 (76.18%) | 1 | 120 |
| Game | 1,959 / 4,808 (40.74%) | 0 | 2,849 |
| Debugger | 176 / 181 (97.24%) | 0 | 5 |

The percentage increase from the old July matching snapshot remains primarily
denominator driven: the exact count is now 2,522, equal to July's count, while
481 functions moved from C back to assembly. The paired event-swap pass added
two byte-exact functions and the debugger rectangle-fill, float-formatter,
and glyph-blitter passes added one each after the restoration baseline.
`func_10012588` remains the sole address-drift blocker.

## Verified build state

These commands passed from the current checkout on 2026-09-25:

```sh
make -C conker replace NON_MATCHING=1 -j4
make tools-check
make NON_MATCHING=1 -j4
make -C conker match-progress NON_MATCHING=1
```

The successful non-matching build establishes that the current source links
and emits `conker.us.bin`. It does not establish a matching ROM hash or fresh
end-to-end gameplay acceptance.

## Resume boundary

1. The restoration baseline is banked. Do not fold a broad conversion batch
   into it; future work should start from a new focused commit.
2. Resume debugger `func_16001BB4`. The matcher reports 27 differences, but
   the restored SDK `_Printf` body is 401 words versus retail's 402; isolate
   the final `_PAD`/loop-back branch schedule before broader rewrites.
3. Keep `func_15135480` as a game follow-up candidate. It has the same
   branch-operand mismatch solved in the paired event-swap routines, plus one
   additional difference that still needs isolation.
4. Treat raw-assembly conversion as a separate queue. Start by reviewing the
   smallest game-owned rows in `progress.csv`; exclude SDK, CP0, handwritten,
   and mixed code/data routines before converting anything.
5. After every source change, relink and rerun `match-progress`. Update public
   percentages only from a fresh linked scan.

The baseline and candidate list are in [Working Note 001](WORKING_NOTES/001-decomp-status-and-resume-boundary-20260924.md).
The completed pair and compiler-shape evidence are in
[Working Note 002](WORKING_NOTES/002-paired-event-swap-byte-match-20260924.md).
The completed debugger rectangle fill and guarded scheduling normalization are
in [Working Note 003](WORKING_NOTES/003-debugger-rectangle-fill-byte-match-20260924.md).
