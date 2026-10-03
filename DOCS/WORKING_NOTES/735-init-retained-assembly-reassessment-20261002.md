# Init Retained Assembly Reassessment

Date: 2026-10-02

Follow-up: [Note 736](736-init-memory-clear-leaf-conversion-20261002.md)
completes the `func_10001420` experiment as semantic C with a byte-exact
linked result. Current Init is 492 C / 47 assembly rows. The inventory and
read-only evidence below record the preceding assessment, not current totals.

## Result

The supported compiler-generated Init recovery queue is complete. No additional
routine is currently established as an ordinary compiler-generated C recovery.
That does not mean every remaining routine is impossible to express in C.
Three small custom leaves are plausible behavioral rewrite experiments, but
none has a demonstrated byte-exact C replacement or recovered original C.
Keep the verified assembly baseline intact until an experiment proves both
the complete function match and its caller contract.

This resumes the user's Init assessment, not the pending Game conversion.
No guest source, layout, word patches, README aggregates, or host-port artifacts
were changed during this audit.

## Live Baseline

The checkout started clean at `7f0a76f`, two local commits ahead of origin.
`conker/progress.csv` contains 539 Init rows: 491 C and 48 assembly.
Their lengths total 151,760 C bytes and 12,288 assembly bytes.

A fresh read-only linked matcher reports Init 491 / 491 exact, zero drift,
and zero different C rows. Direct ELF section extraction independently matches
all 164,048 Init code bytes and all 17,376 initialized-data bytes against
`conker/conker.us.bin`. This includes the retained assembly, not just C rows.

```text
.init SHA-256
34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf
.init_data SHA-256
a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239
```

These are existing linked-artifact checks. No rebuild, compiler experiment,
gameplay test, or compressed-ROM build was performed for this assessment.

## Remaining Inventory

| Group | Rows | Bytes | Disposition |
| --- | ---: | ---: | --- |
| SDK assembly outside `init_5AB0` | 19 | 2,288 | Retain original SDK assembly |
| Boot entry `func_10001000` | 1 | 80 | Retain clear-and-jump entry contract |
| Custom leaves `func_10001420`, `func_100038E0` | 2 | 80 | Possible C experiments, not proven matches |
| `init_5AB0` hardware/context routines | 8 | 4,376 | Retain privileged/context assembly |
| `init_5AB0` decompressor entry/helpers | 10 | 3,984 | Retain shared register/frame contract |
| `init_5AB0` bitmap leaf `func_10005BE0` | 1 | 76 | Possible C experiment, not a proven match |
| `init_5AB0` SDK thread queue leaves | 2 | 96 | Retain proven SDK assembly provenance |
| `init_5AB0` cleanup/debug/glyph machinery | 5 | 1,308 | Retain nonstandard entry/return and live registers |
| Total | 48 | 12,288 | No production conversion in this audit |

The 19 separated SDK routines are `osMapTLBRdb`, `bzero`, `bcopy`, `sqrtf`,
`__osSetSR`, `__osGetSR`, `__osSetFpcCsr`, `osGetCount`, `__osSetCompare`,
`__osDisableInt`, `__osRestoreInt`, `osSetIntMask`, `osInvalICache`,
`osInvalDCache`, `osWritebackDCache`, `osWritebackDCacheAll`, `osUnmapTLB`,
`osMapTLB`, and `__osProbeTLB`. Local SDK assembly references are under
`tools/ultralib/src/{os,libc,gu}`. The live inventory names the count accessor
`osGetCount`, not `__osGetCount` as the older triage list did.

The eight hardware/context rows are `func_10005AB0`, `func_10005B04`,
`func_10005C2C`, `func_100061F8`, `func_100071D0`, `func_100077B8`,
`func_10007A38`, and `func_10007DA0`. The bodies include CP0/TLB operations,
exception/context handling, or `syscall`; an ordinary C rewrite cannot
replace those instructions without assembly/intrinsic support.

The ten decompressor rows are `func_10006240`, `func_1000625C`,
`func_1000632C`, `func_10006380`, `func_10006424`, `func_10006828`,
`func_1000692C`, `func_1000696C`, `func_10006E00`, and `func_1000709C`.
For example, `func_10006380` saves `$ra` at `0xA68($sp)` without allocating
a frame and consumes live `$s7`, `$gp`, and `$fp`. `func_1000692C` uses the
caller's `0xA44`/`0xA74` stack slots. These are not independently convertible
ordinary-ABI functions. A semantic decompressor rewrite would be a separate
whole-contract project, not another small matching conversion batch.

`func_100079D8` and `func_10007A24` directly reproduce the local SDK
`__osEnqueueThread` and `__osPopThread` assembly in
`tools/ultralib/src/os/exceptasm.s`. Their simple algorithms are C-expressible,
but simplicity does not make them missing compiler-generated C recoveries.

The five cleanup/debug/glyph rows are `__osCleanupThread`, `func_10007C74`,
`func_10007CC4`, `func_10007D28`, and `func_10007DAC`. The glyph helper
consumes `$t1..$t4` and updates `$t1`; its callers use `$t3` as a link register
for an interior cleanup/debug entry and return through `$a1`. Converting only
the glyph leaf would discard its actual interface. The cleanup inventory row
also contains an interior debug entry, so its SDK-looking symbol is not proof
that the entire row is a stock C-callable routine.

## Optional C Experiments

| Routine | Bytes | Recovered behavior | Remaining proof obligation |
| --- | ---: | --- | --- |
| `func_10001420` | 36 | Clear `0xFE0` bytes at `D_80043B40` in four-byte stores | Exact nine-word loop, symbol ownership, caller contract |
| `func_100038E0` | 44 | Publish address `0xBC000C02`, publish `0x4040`, and write the halfword to that MMIO address | Volatile access width/order, complete eleven-word match |
| `func_10005BE0` | 76 | Fill the inclusive bitmap range with `0xFF`, mask the final byte for a partial group | Inclusive end and low-three-bit edge cases, full nineteen-word match, extraction from the assembly owner |

The generated `Handwritten function` comment alone is not proof of original
authorship for the first two leaves. Their current source owners explicitly
retain them as assembly, and no matching C experiment was run here. The
assessment is therefore deliberately conditional rather than an impossibility
claim. `func_10005BE0` has no such generated comment and uses ordinary argument/
temporary registers; it is the other reasonable small experiment.

If all three experiments succeeded, Init would reach 494 / 539 C rows and
151,916 / 164,048 C bytes, leaving 45 assembly rows / 12,132 bytes. Those are
conditional arithmetic, not reported project progress. They would not justify
forcing the rest of the original assembly into C to reach 100%.

## Next Steps

1. For another Init-only experiment, start with `func_10001420`. Isolate the
   candidate from the production source and try the existing IDO profiles.
   Require all nine words to match before replacing the assembly owner.
2. For MMIO `func_100038E0`, establish explicit volatile halfword semantics
   and verify the guest stores and neighboring addresses. Do not infer host
   portability from a C rewrite of a privileged guest address.
3. For `func_10005BE0`, test byte-count multiples of eight, partial final-byte
   masks, and the inclusive endpoint, then preserve the surrounding assembly
   symbols when changing source ownership.
4. After any successful experiment, run the full code link, regenerate the
   inventories, compare the entire Init code/data sections, and document actual
   measured results. Keep README limited to aggregate status tables.
5. The normal decomp queue remains Game `func_15157FE8`; this Init audit does
   not change or complete that pending recovery.
