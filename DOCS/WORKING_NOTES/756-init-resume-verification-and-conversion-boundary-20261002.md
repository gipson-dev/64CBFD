# Init Resume: Verification and Conversion Boundary

Date: 2026-10-02

## Decision

The supported ordinary compiler-generated Init C recovery queue is complete.
Two small retained leaves can be expressed behaviorally in C, but neither has
a proven byte-exact replacement. The other 45 rows require retained original
assembly or a separately scoped whole-contract rewrite. This is not a claim
that their algorithms are impossible to express in C.

| Remaining group | Rows | Bytes | Disposition |
| --- | ---: | ---: | --- |
| Separated SDK assembly | 19 | 2,288 | Retain original SDK implementations |
| Boot clear-and-jump entry | 1 | 80 | Retain non-C entry contract |
| MMIO leaf `func_100038E0` | 1 | 44 | Deferred matching C experiment |
| Hardware/context routines | 8 | 4,376 | Retain privileged/context assembly |
| Shared-frame decompressor entry/helpers | 10 | 3,984 | Whole-contract rewrite only |
| Bitmap leaf `func_10005BE0` | 1 | 76 | Deferred matching and ownership extraction |
| SDK thread queue leaves | 2 | 96 | Retain SDK assembly provenance |
| Cleanup/debug/glyph machinery | 5 | 1,308 | Recover nonstandard interfaces together |
| Total | 47 | 12,252 | No conversion in this audit |

The full routine lists are in
[Note 735](735-init-retained-assembly-reassessment-20261002.md); its historical
48-row inventory predates the completed clear-loop conversion in Note 736.

## Small Candidates

1. `func_100038E0`: eleven words publishing the address `0xBC000C02`, publishing
   halfword `0x4040`, then writing that halfword to MMIO. Five earlier trials
   and twenty follow-up shape/profile trials did not establish a matching
   replacement. Revisit only with a new explanation for retail's address
   lifetime, repeated constant materialization, and return-delay scheduling.
   Do not invent a return value or hardware identity. See
   [Note 750](750-init-mmio-pointer-lifetime-profile-trials-20261002.md).
2. `func_10005BE0`: nineteen words filling an inclusive bitmap range and
   masking the last byte. The final 55-combination matrix had no exact body;
   its eleven source shapes passed 65 positive-count cases twice each.
   These are historical behavior results, not tests rerun in this audit.
   A new candidate must preserve the initial unconditional store, signed
   count, inclusive endpoint, and all eight remainder classes. Prove the
   complete match before extracting its span from `init_5AB0`. See
   [Note 751](751-init-bitmap-loop-mask-profile-trials-20261002.md).

If both eventually succeed, Init would reach 494 / 539 C rows and
151,916 / 164,048 C bytes, leaving 45 assembly rows / 12,132 bytes.
Those are conditional totals, not current progress.

## Fresh Verification

The checkout began at `d3774f4`, sixteen commits ahead of origin, with three
modified files from an interrupted Game overlap recovery. A fresh CSV
inventory reconfirms 492 C rows / 151,796 bytes and 47 assembly rows /
12,252 bytes. C coverage is 91.28% of routines and 92.53% of bytes.

After preserving the Game draft as described below, the full code build and
progress regeneration completed successfully:

```sh
make -C conker NON_MATCHING=1 all match-progress -j4
```

The rebuilt matcher reports Init 492 / 492 exact, zero address drift, and
zero different C rows. Independent ELF extraction matches retail for both
complete sections, including retained assembly:

| Section | Bytes | SHA-256 |
| --- | ---: | --- |
| `.init` | 164,048 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| `.init_data` | 17,376 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |

All 131 tool tests pass (`python3 -m unittest discover -s tools/tests`).
`make tools-check` and `git diff --check` also pass. No new tests were added
for this inventory/verification-only audit.

Live assembly inspection also reconfirms CP0/TLB instructions, shared caller
stack slots at `0xA44`, `0xA68`, and `0xA74`, the `$t3` link-register call
interface, and the syscall leaf. These are concrete reasons not to convert
individual rows as ordinary ABI C functions.

No new compiler experiment, production Init conversion, guest execution,
compressed-ROM qualification, or gameplay validation was performed. README
aggregates remain unchanged. The sibling host port and frozen Release
artifacts were not touched.

## Preserved Game Draft

The interrupted `func_15044B78` recovery produced a 92-word compact body for
a 91-word retail slot. The generated-slice padding tool rejects that body,
so it is not a buildable production conversion. Its float-return correction
for `func_15048A40` is part of the same unfinished draft.

All three modified paths were saved together in a named Git stash, without
discarding the work:

```text
5b554b70ce671454878a1025fec26b93ad457153
WIP func_15044B78 overlap recovery - 92 words exceeds 91-word slot; deferred for Init audit
conker/include/functions.h
conker/src/game/generated_71820.c
conker/src/game_75E60.c
```

To resume that work on a suitable clean checkout, apply the saved object
without dropping it:

```sh
git stash apply 5b554b70ce671454878a1025fec26b93ad457153
```

Resolve the extra word, verify the helper's float-return contract and bytes,
add actual-source behavior tests, and compare the complete linked spans before
banking the recovery. The current production target remains its earlier
placeholder; the stash is not included in a normal commit or push.

## Next Work

For more Init-only work, choose a new, justified small-leaf compiler experiment
or explicitly scope an entire decompressor/nonstandard-interface rewrite.
Repeating the completed matrices is not new evidence. For ordinary matching
decomp progress, the preserved Game overlap draft is the next pending recovery.
