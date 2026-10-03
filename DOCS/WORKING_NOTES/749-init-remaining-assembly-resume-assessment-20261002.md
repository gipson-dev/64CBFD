# Remaining Init Assembly: Resume Assessment

Date: 2026-10-02

## Conclusion

Two remaining small Init leaves are reasonable C rewrite candidates, but neither
has a proven matching replacement: `func_100038E0` and `func_10005BE0`.
The other 45 assembly rows are not an established ordinary C recovery queue.
Keep their original implementations unless a separate whole-contract project
proves a replacement. C-expressible behavior is not proof of original C or of
a byte-exact conversion.

This assessment resumes the user's Init request. The paused Game target
`func_15040CC8` is untouched. No source conversion, compiler experiment, build,
new behavior test, or gameplay qualification was performed for this audit.

## Fresh Evidence

The checkout began clean at `f59a641`, on `master`, ten commits ahead of origin.
A fresh inventory of `conker/progress.csv` has 539 Init rows: 492 C rows /
151,796 bytes and 47 assembly rows / 12,252 bytes. Init C coverage remains
91.28% of rows and 92.53% of bytes.

A fresh linked matcher reports all 492 Init C rows exact, with zero drift and
zero differing Init C rows. Independently extracted ELF sections match retail:

| Section | Bytes | SHA-256 |
| --- | ---: | --- |
| `.init` | 164,048 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| `.init_data` | 17,376 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |

These checks validate the existing linked artifact, including retained assembly;
they do not establish that it was rebuilt during this assessment.

## Remaining Groups

| Group | Rows | Bytes | Next action |
| --- | ---: | ---: | --- |
| Separated SDK assembly | 19 | 2,288 | Retain SDK assembly provenance |
| Boot clear-and-jump entry | 1 | 80 | Retain non-C entry contract |
| MMIO leaf `func_100038E0` | 1 | 44 | Deferred isolated C matching experiment |
| Hardware/context routines in `init_5AB0` | 8 | 4,376 | Retain privileged/context assembly |
| Decompressor entry/helpers | 10 | 3,984 | Whole-contract rewrite only |
| Bitmap leaf `func_10005BE0` | 1 | 76 | Deferred matching and ownership extraction |
| SDK thread queue leaves | 2 | 96 | Retain original SDK assembly |
| Cleanup/debug/glyph machinery | 5 | 1,308 | Recover nonstandard interfaces as a group |
| Total | 47 | 12,252 | Two bounded candidates; no new conversion |

The detailed routine lists and interface evidence are in
[Note 735](735-init-retained-assembly-reassessment-20261002.md).
Its historical 48-row table predates the completed clear-loop conversion in
[Note 736](736-init-memory-clear-leaf-conversion-20261002.md).
Live inspection of `conker/asm/init_5AB0.s` reconfirms CP0/TLB operations,
interior entry labels, and the syscall leaf. Ordinary ABI C functions cannot
simply replace those interfaces.

## Init Work Order

1. Resume `func_100038E0` in an isolated fixture first. It owns a separate
   source slice and needs no extraction from the shared assembly owner.
   Preserve the address publication, halfword publication, and volatile MMIO
   halfword write, in that order. Do not invent a return value or hardware
   identity. [Note 737](737-init-mmio-leaf-bounded-compiler-experiment-20261002.md)
   records five prior trials; repeating those unchanged is not new evidence.
2. Compare new source shapes against all eleven retail words. The unresolved
   differences include retained address reuse, constant rematerialization,
   and return-delay scheduling, not just register names. Any normalization
   must have a specific equivalent instruction/dataflow justification and
   strict expected-word checks; matching length alone is insufficient.
3. Then resume `func_10005BE0`. Preserve its inclusive fill endpoint, initial
   unconditional store, signed-halfword count, and low-three-bit final mask.
   [Note 738](738-init-bitmap-leaf-contract-and-compiler-experiment-20261002.md)
   records three compiler trials and 65 passing candidate behavior cases,
   but no matching production conversion. Resolve its nineteen-word loop
   and mask shape before changing assembly ownership.
4. For the bitmap leaf, reconcile the pointer declarations with all consumers
   and extract only its span from `init_5AB0`, preserving neighboring symbols,
   interior labels, and layout. Keep tests for all eight remainder classes,
   inclusive bounds, repeated calls, and surrounding-byte preservation.
5. Before banking either conversion, run the full code build and tool checks,
   regenerate progress, compare the complete function and following address,
   and independently compare both entire Init sections. Update README only
   when aggregate progress actually changes.

If both candidates succeed, Init would reach 494 / 539 C rows and 151,916 /
164,048 C bytes, leaving 45 assembly rows / 12,132 bytes. This is conditional
arithmetic, not current progress. There is no demonstrated path to converting
all remaining Init assembly into ordinary matching C.

The sibling host port and its frozen Release artifacts were not touched.
