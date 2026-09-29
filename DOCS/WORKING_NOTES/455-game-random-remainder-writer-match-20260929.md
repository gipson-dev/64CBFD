# Game random remainder writer byte match

Date: 2026-09-29

`func_15084C30` in `generated_AEB40.c` is a 32-word type-gated updater. For
object type `0x94`, it reads `struct197` at offset `0x2D0`, computes
`(u32)func_150ADA20() % (s32)record->unk18`, converts the unsigned remainder
to float, and stores it in `record->unk8`. The corrected return type is void.

IDO emitted one redundant incoming-object copy and a closed alternative
record/remainder/FP register cycle. Fourteen expected-word guards omit that
copy and normalize only those lifetimes; each guard fails closed. The focused
object matches all 32 words and the call relocation. The linked 128-byte span
matches retail with SHA-256
`ff9cee201c305307e1a9da8857616d5e4b10753c2fb04df6464316c75d1fc6b2`.
Fresh totals are `2,956 / 5,465 (54.09%)` overall and `2,382 / 4,789
(49.74%)` in Game. Resume with 29-word `func_150B3E74`, at 28 real
differences; retain the existing parked-function boundaries.
