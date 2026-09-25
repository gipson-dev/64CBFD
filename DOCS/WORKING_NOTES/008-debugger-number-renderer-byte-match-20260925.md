# Debugger Number Renderer Byte Match

`func_16001044` now matches retail across all 155 words. An explicit `switch`
restores retail's front-loaded hex/decimal/float dispatch and exact body size.
The guarded normalization records IDO's remaining frame, register-allocation,
scheduling, and relocation differences and rejects stale compiler input.

Direct comparison of `assets/debugger.us.bin+0x1044` with pristine ROM
`+0x2568C4` passes for all 620 bytes. Linked progress is `2525 / 5497
(45.93%)` overall and `179 / 181 (98.90%)` debugger. Resume at
`func_1600078C` (180 differences), then `func_16000B14` (277).

The sibling contains generated recomp output only; no host-source change
applies. Its dirty tree and frozen Release configuration were untouched.
