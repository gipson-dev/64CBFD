# Game Natural-Logarithm Approximation Guarded Match (2026-11-03)

## Outcome

`func_1504A620` now matches its complete 68-word / 272-byte retail slot with
no stack frame. The semantic natural-logarithm approximation already restored
from the ects source is unchanged; its stale non-matching marker is replaced
with an accurate matching note. Forty-one expected-word guards plus three
checked scheduling-word insertions normalize the 65-word natural IDO body to
the retail 68-word layout. There are no omissions, and the linked function is
byte-exact.

This is a source/ABI review, raw and padded owner, caller, guest/native
execution, strict whole-image, protected-data, production-build, recount, and
graph-retention result. It is not live gameplay, renderer, mathematical-library,
or hardware acceptance.

## Preserved semantic contract

The function preserves its binary32 approximation contract. Negative and zero
inputs return zero. Positive inputs are normalized into `[1, 2)` while the
accumulator is adjusted by the two stored logarithm constants. The normalized
mantissa is transformed to `(x - 1) / (x + 1)`, and the odd-term series is
accumulated until the binary32 result stops changing.

No source-body fitting rewrite was installed. The selected body remains the
existing seven-local implementation in `conker/src/game_77AD0.c`; only its
status comment changed. The natural compiler output already has the correct
frame, branch structure, normalization loops, arithmetic order, termination
test, and return behavior.

## Guards, insertions, and bindings

The natural compiler body is 65 words; retail is 68. The 41 fail-closed rows
form closed register-allocation and instruction-scheduling cycles, while three
rows insert the retail scheduling words at natural compiler offsets `+0x014`,
`+0x02C`, and `+0x0A4`. No compiler word is discarded.

The two constant bindings also move as part of those closed schedules:

- `D_800990B0` moves from natural `+0x048/+0x054` to final
  `+0x048/+0x05C`;
- `D_800990B4` moves from natural `+0x084/+0x098` to final
  `+0x084/+0x088`.

The relocation-bearing replacement words at compiler offsets `+0x040`,
`+0x054`, `+0x07C`, and `+0x080` use zero addends. This is required because the
linker applies the HI16/LO16 symbol value after padding; embedding the resolved
address in the replacement word would add the symbol twice. Both constant
pairs are checked symbolically by the permanent qualifier.

## Caller boundary

The retail assembly has one raw direct caller: `func_1504A400` in
`asm/778B0.s`, with the JAL at ROM offset `0x77994`. It supplies the input in
`f12`, consumes the return in `f0`, and multiplies it by its saved `f14` value.
The current linked C version of that caller remains a zero-return placeholder,
so this result does not claim a live linked semantic caller path. That boundary
is retained explicitly instead of treating a raw-ROM call pattern as linked-C
acceptance.

## Qualification and execution

The permanent tools were committed first as tools commit `8bd9d4f`
(`test(game): qualify logarithm approximation match`). They add the source
shape screener, strict match qualifier, independent binary32/guest/native
oracle, and five-test permanent suite. The shared dual-phase qualifier was
also generalized so natural and final relocation offsets can differ without
weakening either binding check.

The installed five-test suite passes in 84.281 seconds:

- the complete 68-word slot, all 65 compiler words, 41 guards, three
  insertions, and four final relocations are checked;
- 1,040 finite guest inputs produce 2,080 natural-and-retail executions;
- 63 / 65 natural words and 66 / 68 retail words are dynamically reachable;
  the two words on each side that are not reached are duplicate
  branch-likely shadow operations and are unreachable by construction;
- native 32-bit O0, O2, and O3 builds each pass all 1,040 cases with UBSan;
- fifteen independent semantic controls are rejected;
- 264 raw-byte and binding controls plus every one of the 41 guard-preimage
  mutations fail closed; and
- 57 owner neighbors, the strict 6,051-function image, and all target/caller
  boundaries remain closed.

The shared match-progress, guarded-object, generated-PC16, and protected-data
suite passes all 19 tests in 11.354 seconds. Protected Game data remains exact
at `0x80082760`: 189,088 bytes across 720 owners, zero different bytes or
owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Production closure and frozen evidence

Because the shared guard manifest changed, the actual
`make -C conker all -j2` rebuilt every padded C owner. It completed compilation,
assembly, padding, linking, and binary generation, then stopped only at the
expected final retail-ROM SHA mismatch. There was no compile, assembly,
padding, relocation, owner-preimage, or link failure. The production ELF and
owner exactly reproduce the independent pre-install predictions.

| Artifact | SHA-256 |
| --- | --- |
| Natural 65-word compiler body | `6773ad789c97dbd36e75e2748d30735eccb25871d945cd3797a6edc7d16e0cbb` |
| Complete linked retail target body | `5ea84c1d30ac4dba44ae3ef6b79c082ebd45000ace9a0c7a4d369a2c708bb40c` |
| Unchanged semantic owner source with corrected marker | `0622cf1158c1af3325f045239e1046f7f393ef516b0095cae21653a46a659f9a` |
| Qualified/production owner object | `7ea3ce9cb8ec49968ac4523317748783deeff6504a84aa45169ba174116b9875` |
| Predecessor linked ELF | `0abc440198d59385cea1558814510a4c592e87efa616c3a9ef342ed3945dc751` |
| Qualified/production linked ELF | `b455dfc321bb762f5ea37cbc347cf03cd5af38c70aa1a45d1bf8ba54d1700da7` |
| Production rebuilt ROM image | `6c232aabf1b530a3f64dec52f2b9fd1bebbaf69e7f539b6cc7d5e86305ac4845` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Installed guard table | `eb461fd4d6e7ffeb4d3e627829d600f7feb30cf1bb85735452f23a4e1afb6b4b` |
| Aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

## Recount

The fresh production ELF reports:

- Total: **4,127 / 5,511 (74.89%)**, zero address drift, 1,384 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,454 / 4,838 (71.39%)**, zero drift, 1,384 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **282 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted nine uncached inputs but
proposed only 24,508 nodes against the retained 58,302-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. No forced refresh was used.

An explicit nine-path incremental rebuild with `force=False` then produced
58,312 nodes, 112,210 links, and 5,059 communities. Against the saved
pre-change snapshot, 58,299 / 58,302 old node IDs were retained. The three
replaced IDs are line-number-derived `DOCS/UPDATE_LOG.md` headings, and each
has one uniquely relocated replacement; 13 IDs were added, including the
Note 2057 file, title, and section headings. A final one-path refresh after
recording this section produced **58,313 nodes, 112,211 links, and 5,162
communities**.

## Continuation

Continue the ordinary Game queue at `func_15172D80`, followed by
`func_1519E1F4` and `func_151DE6D4` in the same prior 62-difference tier. The
seven documented handwritten/custom-ABI boundary cases remain in their
separate lane. Every next candidate still requires source, ABI/caller, owner,
guest/native, actual Make, complete-image, protected-data, production recount,
documentation, and graph-retention gates before credit.
