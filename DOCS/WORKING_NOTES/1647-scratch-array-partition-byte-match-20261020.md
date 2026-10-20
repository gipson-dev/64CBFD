# Scratch Array Partition Byte Match

Date: 2026-10-20. Consumer predecessor `72a8a146`; tools predecessor
`f81540b`. The 75% total C-matching goal remains active.

## Recovered Routine

`func_15002754` in [game_2DF70.c](../../conker/src/game_2DF70.c):
VA **15002754..150027F8**, ROM **2FC04..2FCA8**, **41 words/frame24**.
This is an existing semantic routine, not a zero-return stub. Its old
compiled extent is **152 bytes**, with **38 retail word differences**.
Do not replace genuine semantics to raise the percentage.

Align the 32-bit scratch cursor upward to four bytes and publish it before
loading the count and context index. Publish the three selected bases at
`800DBDD8`, `800DBDE8`, and `800DBDF8`, advancing the cursor by count
times **12, 8 and 4 bytes**. Keep all four cursor stores, call
`func_1510F800(index)`, and clear the count only after its return.
Preserve the existing `void(void)` ABI and add a purpose comment plus the
correct owner-local `void func_1510F800(s32)` declaration. Shared headers
and all other owner functions must remain unchanged.

Use unsigned 32-bit additions/multiplications to retain the retail wrapping
words without assuming defined signed overflow. Conversion back into the
existing signed globals preserves the word on the pinned two's-complement
32-bit toolchains. Numeric address arithmetic here is not an allocation or
heap-capacity guarantee.

## Compiler Fit

A local-cursor probe collapses three required cursor publications and emits
38 words. Direct cursor updates restore all 41 words, the complete schedule,
the 24-byte frame and all 15 bindings. The direct, natural pointer,
signed-count, declaration-order, implicit-conversion, unsigned-index and
byte-offset probes all retain the same ten-word allocation difference.

The selected C uses direct updates. Ten expected-word, relocation-aware
guards normalize one closed **a1/a2 count/index-scale allocation cycle**.
There are no omitted/inserted instructions, artificial locals, register
bindings, volatile annotations or compiler-profile changes. Raw C is not
claimed compiler-only or byte-exact. Preserve the entire prior guard prefix.

## Actual Caller And Helpers

The pristine complete-function JAL scan finds exactly three sites, all in
the **142-word func_15003668**: **150036BC**, **150036E4**, **15003768**.
There is no aligned literal target pointer in ROM. Qualify all three sites
inside the complete original caller, with initialization, scan, rendering,
end-of-context and packing providers explicitly bounded.

Execute the unchanged **eight-word func_1510F800** wrapper at **1510F800**,
ROM **13CCB0**, and the public returning **40-word** handwritten selector
entry at **150A49F4**, ROM **D1EA4..D1F44**. Its five indexed word loads and
six publications remain assembly. The apparent 66-word extraction also
contains the following handwritten continuation beginning at **150A4A94**;
do not execute, convert or claim that continuation as part of this entry.

## Qualification Gates

[The experiment](../../tools/experiments/game_scratch_partition.py) freezes
27 live source/header/assembly/layout/image/build inputs and separately pins the old padded owner object. Preserve
**25 other owner functions**, raw/padded pools, metadata, all other linked
bodies/addresses and all protected Game data. Use the actual five-command
legacy Make path, not the generated-slice padder.

[The focused tests](../../tools/tests/test_game_scratch_partition.py) cover
wrapping words and alignment residues, context
captures, all four cursor stores, post-call mutations and count clear,
typed/fenced native32 arrays with UBSan, effective compiled negatives,
the actual selector/wrapper and caller, signed-low relocation carries,
guest-only symbol aliases and target fault prefixes. Do not claim portable
out-of-bounds/global alias behavior, arbitrary heap validity, full parser/
renderer implementations, hardware or gameplay acceptance.

## Installed Checkpoint

Each copy passes all eight tests before installation, with zero errors,
failures or skips. After installation, each copy freshly passes the two
install-sensitive tests (01 and 08), including a fresh isolated compile,
full installed audit and all frozen inputs. The six unchanged model/native/
caller/guard/rebase tests per copy reuse their pre-install receipts only
after source, raw/padded object, helper, tools and whole-image identity is
proved. These six are not claimed as fresh installed reruns. Copies run
sequentially because scratch outputs are shared:

| Run | Fresh Tests | Seconds |
| --- | ---: | ---: |
| Primary, pre-install | 8 | 834.816 |
| Older mirror, pre-install | 8 | 822.584 |
| Primary, installed | 2 | 41.140 |
| Older mirror, installed | 2 | 165.775 |

Each complete pre-install suite covers **868 cases / 1,736 modeled phases**, including **80
guest-only phases**, and **828 native32 cases** at O0/O2/O3 with trap
UBSan. Eleven compiled semantic negatives are effective. The actual old
signed-arithmetic body is rejected on numeric-word wrap inputs, not
invalid native array access. All 41 target instruction words execute.

The real eight-word wrapper plus 40-word selector pass **96 phases**,
visiting all 48 helper words. The full 142-word caller passes **48 phases**
across all three real sites; other providers remain explicitly bounded.
When the actual leaf preserves them, raw C's private a1/a2 values are
compared under the proved allocation swap; normalized C has identical
physical state. Raw C is not claimed byte-exact.

Eighteen independent GNU links pass **96 rebase phases**, with all 15
bindings, signed-low carries and three symbol-alias layouts. All **78
target fault prefixes**, **30 guard controls**, ten raw-word corruption
checks and seven strict-image negatives pass. Symbol aliases/out-of-range
indices are guest-only stress tests, not portable C object-layout claims.

Both shared tools checks pass. The inherited owner compiler diagnostics
are unchanged after normalizing filenames/line numbers; isolated C has
no diagnostics. The duplicate generated_12D630 Make recipe warning is
inherited. Do not claim a globally warning-free build.

The independently qualified owner and proposed guard manifest are installed
byte-for-byte. Production passes in **1411.270s**:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The `-o` flag reuses unaffected objects: the complete old manifest prefix
is unchanged, and the only ten appended rows name this rebuilt routine.
The changed owner and full link still run. No Makefile/profile, shared
header, original assembly, ROM or conversion-row changes.

The complete **16,228-byte production owner object** is binary-identical
to the qualified padded object (SHA-256
`ae0da9529b4b8179c6ca7b8ffabda0d053235dccec849cbcd281efbc0bcf1ad5`).
This closes object identity for the explicitly reused pre-install tests.

The independent first link and production image agree exactly:
**128 changed bytes = 127 instruction bytes + one symbol-size byte**,
extent **152 -> 164 bytes**, **zero metadata exclusions**. ELF SHA-256:
`9c49b22ea18204941236929c1b2b692fde1a23003166cb685ea767423482d44b`.
Raw unrelocated C SHA-256:
`ad79c62ccd743c79b7fab7852569707b8c00b923591889e705ad64f67c58051b`.

Preserve all **6,055 other linked bodies**, all **6,056 addresses** and
**189,088 protected Game-data bytes / 720 owners**. Protected data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

After production/audit, run the literal standard Make matcher recipe from
`conker/`, avoiding a redundant dependency scan:

```sh
python3 ../tools/match_progress.py progress.csv build/conker.us.elf conker.us.bin --version us --objdump mips-linux-gnu-objdump
```

Fresh results: **3,712/5,505 total (67.43%)**, **3,039/4,832 Game (62.89%)**,
**492/492 Init**, **181/181 Debugger**, **zero drift / 1,793 different**.
The current 75% threshold is **4,129**, leaving **417**. The strict-ELF-pinned
queue has **1,660 placeholders, 124 semantic/other bodies and nine unlocated
entries**; these source-shape screens are not qualification. README changes
are only its two aggregate rows; the roadmap checks off this function.

The older mirror remains at `ddbdd16`. All **1,506 pre-existing dirty
statuses/hashes** are preserved; only two absent task files are added,
bringing it to **1,508**. Both copies are byte-identical and all four files
are AST-valid. Never commit/reset/stash/clean that mirror. Active tools
are committed first as `ff22329`; the consumer source/guards/docs/pin
checkpoint follows. No push. Host source, real saves/configuration and
frozen Release stay untouched. Routine task: zero Claude calls.

## Next Function

Next is `func_150B6C90` in `generated_E4070.c`:
VA **150B6C90..150B6D34**, ROM **E4140..E41E4**,
**41 words/frame40**. It is currently a zero-return placeholder.
Recover the conditional old-pointer release, eight-argument color factory,
saved result/state byte and exact zeroed table slots. Preserve exact store widths and table
bounds and inspect the actual caller ABI before choosing a return type.
The pristine ROM scan finds exactly one direct JAL, **150B6BF8**
(ROM **E40A8**), in the **52-word/frame24 func_150B6BC0** dispatcher,
and no aligned literal pointer. Its local epilogue does not consume v0;
the upstream return ABI still needs qualification. These are read-only
screen results, not a draft, installation or matching credit.
Keep `func_1508CAD8` queued.

Receipts: ignored `conker/build/game-scratch-partition/qualified/`.
Before the consumer commit, retain the old graph and rebuild-log offset;
afterward, wait for both owned workers and audit the commit stamp and
retention of old/excluded nodes. The 75% goal remains active.
