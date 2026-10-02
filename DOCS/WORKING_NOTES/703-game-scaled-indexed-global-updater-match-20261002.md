# Game scaled indexed-global updater match

Date: 2026-10-02

Game `func_1509DF20` occupies the 37-word slot at
`0x1509DF20..0x1509DFB4`. It returns without changes unless event word `0x4`
equals one and `D_800D3840` equals three. When both gates pass, the routine
converts the signed event word at `0xC` to float, multiplies it by
`0.0000152587890625f` (`1/65536`), and writes the result to both
`D_800D2FC0[index]` and `D_800D2FD8[index]`, where the index is event word
`0x8`. It then writes one to `D_800D2FEC[index]`.

The recovered `void func(s32, s32 *)` contract explains the unused first
argument spill at stack offset zero. Expressing the two float assignments and
status assignment with their own event expressions preserves retail's repeated
loads of words `0x8` and `0xC`, while IDO keeps the scale constant in `f0`
across both conversions.

All 37 words emit directly from C without expected-word guards or a compiler
profile override. Both gate branches, global relocations, integer-to-float
conversions, shared scale lifetime, indexed address calculations, stores,
leaf return, and delay slots match in the focused object and final linked
image.

The incremental generated-object build, full link, and linked matcher complete
with zero address drift. Game advances to `2,542 / 4,788 (53.09%)`, with
2,246 different C rows; overall byte-exact C progress is
`3,210 / 5,456 (58.83%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
focused-object comparison, full-link, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 37-word `func_150FCF1C`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
