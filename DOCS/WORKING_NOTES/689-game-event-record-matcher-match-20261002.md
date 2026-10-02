# Game event-record matcher match

Date: 2026-10-02

Game `func_151D7538` occupies the 35-word slot at
`0x151D7538..0x151D75C4`. For selector `0x3D`, it compares the object's word
at offset `0x40` and tag byte at offset `0x44` against the incoming five-byte
record. A match in either field calls `func_1516972C` to destroy the object.
Every other selector forwards the incoming record, low selector byte, both
embedded-field addresses, and object through `func_15149514`.

The recovered semantic body makes the selector, object record, comparison
pointers, and true-branch object lifetime explicit. Its compact form emits 34
instructions. Retail also retains the advanced record pointer as an
independent instruction, so fourteen stale-checked patch rows normalize the
closed compiler allocation: thirteen guarded word substitutions and one
checked insertion. The insertion also accounts for the retail branch distance
and consumes the generated slice's former final padding word. Neither
relocation-bearing call is modified.

The function-specific object disassembly matches all 35 retail words. A full
non-matching rebuild and linked matcher also complete with zero address drift.
Game advances to `2,527 / 4,788 (52.78%)`, with 2,261 different C rows;
overall byte-exact C progress is `3,195 / 5,456 (58.56%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
full-link, stale-guard, and linked-word comparison evidence.

The fresh linked-difference scan selected `func_151EDB58`, which is now
complete; see
[Working Note 690](690-game-counted-resource-owner-teardown-match-20261002.md).
Keep `func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
