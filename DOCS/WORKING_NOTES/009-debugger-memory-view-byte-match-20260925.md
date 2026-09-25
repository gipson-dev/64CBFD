# Debugger Memory Viewer Byte Match

`func_1600078C` now matches retail across all 180 words. The maintained C
caches each displayed memory word once, keeps the validated address as the
walking loop address, and uses an unsigned counter. Those source changes
restore retail's 48-byte frame and saved-register roles: `s0` context base,
`s1` screen row, `s2` memory address, `s3` loaded word, `s4` iteration count,
and `s5` color-range base.

IDO still chose 25 independent scheduling/register words differently. The
guarded normalization restores the likely invalid-address exit, the duplicated
`D_8002D4B0` relocation schedule, and volatile temporary coloring. Every entry
checks the compiled input word; relocation moves are explicit.

Direct comparison of linked `func_1600078C` with pristine
`conker.us.bin+0x25600C` passes for all 720 bytes. Linked progress is
`2526 / 5497 (45.95%)` overall and `180 / 181 (99.45%)` debugger. The final
debugger target is `func_16000B14`, currently 277 differences across 286 words.

The sibling contains this routine only in generated recomp output and symbol
metadata. No host-source change applies. Its unrelated dirty tree and frozen
Release configuration were inspected but not modified, built, or launched.
