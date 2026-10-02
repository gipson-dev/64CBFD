# Game clamped height-byte match

Date: 2026-10-02

Game `func_1518B1D8` occupies 35 words at
`0x1518B1D8..0x1518B264`. Its recovered C subtracts the object's reference
height at offset `0x170` from its current height at offset `0x3C` and rejects
a negative delta. It forms one candidate by multiplying signed field `0x64`
by four and another by truncating the delta and halving it. Each candidate's
upper bound is clamped to `0xFF`, the smaller candidate is selected, and a
nonnegative result is stored as the byte at offset `0x70` before returning
success.

The recovered arithmetic, comparisons, clamps, and store reproduce retail's
behavior. The first 21 words and final no-op already emit directly from the
semantic body. Ten stale-checked expected-word rows in the suffix normalize
only IDO's compiler phi register and an equivalent branch/delay-slot schedule.
All 35 retail words now match without a compiler-profile override.

The full non-matching link and matcher complete with zero address drift. Game
advances to `2,522 / 4,788 (52.67%)`, with 2,266 different C rows; overall
byte-exact C progress is `3,190 / 5,456 (58.47%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is compiler, full-link,
stale-guard, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 34-word `func_1519C4E4`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.

## Superseded resume point

`func_1519C4E4` was subsequently recovered and byte-matched in
[Working Note 685](685-game-tick-compensated-damping-callback-match-20261002.md).
Resume the ordinary queue with 35-word `func_151A787C`; the two parked special
cases above remain unchanged.
