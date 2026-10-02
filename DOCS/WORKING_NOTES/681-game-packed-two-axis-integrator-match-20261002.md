# Game packed two-axis integrator match

Date: 2026-10-02

Game `func_1516F864` occupies 34 words at
`0x1516F864..0x1516F8EC`. Its recovered C reconstructs signed packed X and Y
velocities from high bytes at object offsets `0x26` and `0x28` plus unsigned
low bytes at `0x27` and `0x29`. Each velocity is multiplied by the global
time scale `D_800BE9E4` and accumulated into a packed position: signed
halfwords at `0x0E` and `0x12`, with low bytes at `0x2A` and `0x2B`.

The compiler emits the retail arithmetic, load/store order, multiply lifetime,
and return sequence, but chooses a different closed register allocation.
Thirty-two stale-checked expected-word rows normalize that allocation. Two of
those rows are relocation-aware `HI16`/`LO16` references to `D_800BE9E4`; the
remaining 30 preserve register-only instruction encodings. The final `jr` and
delay-slot `nop` emit directly. The linked function matches all 34 retail
words.

The full non-matching build and linked matcher complete with zero address
drift. Game advances to `2,519 / 4,788 (52.61%)`, with 2,269 different C rows;
overall byte-exact C progress is `3,187 / 5,456 (58.41%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is compiler, full-link,
stale-guard, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 34-word `func_15170EC4`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
