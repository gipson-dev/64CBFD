# Interpolated callback dispatcher and return contract

Date: 2026-11-12. This updates [Note 2309](2309-game-three-interpolated-callbacks-private-screen-20261112.md). No candidate is installed or counted.

The retail indirect caller is `func_1500BEC0`, whose original instructions are
in the ignored `asm/nonmatchings/game_36680/func_1500BEC0.s`. The window at
`1500C020..1500C0A4` computes a `D_8008CF00` pair index from a row and an
encoded field, uses the signed first halfword as the index into the
12-byte records starting at `D_8008CEB8`, loads the first function pointer,
and dispatches with `jalr` at `1500C074`. It passes the second halfword as
argument 0, the encoded field as argument 1, a slot as argument 2, an inverted
two-bit field as argument 3, the current `D_800DDD20` as stack argument 4,
and a record pointer as stack argument 5. After the call, `1500C090` stores
`v0` back to `D_800DDD20`; it also increments the per-slot halfword counter.
This is one observed caller window, not proof that no other callers exist.
The caller itself remains a C placeholder in the current checkout.

The 40 pairs in the five rows of retail `D_8008CF00` select table entries 2,
3, and 5 respectively for `func_1500B8F4`, `func_1500BAB8`, and
`func_1500BC7C`. Entry 2 occurs seven times with counts 1..7, entry 3 seven
times with counts 1..7, and entry 5 six times with counts 1..6. This is a
bounded census of those five rows; it does not prove arbitrary indices or
other caller paths are safe.

The caller **uses the callback return value**. For nonzero counts the retail
code leaves the last `func_1500AF08` return in `v0`. For zero, retail takes a
branch before loading the cursor and returns with the incoming `v0` unchanged.
The earlier `void` private candidate and its native tests did not check the
return value and cannot justify a complete C interface. A corrected private
`s32` candidate returns the cursor, but at count zero that differs from
retail's incoming `v0`; 16 deliberately distinct zero-count guest inputs per
function expose the difference, while 16 each at counts 1, 2, and 3 agree
with the modeled helper. The zero-count case is not selected by the five
retail table rows for these entries, but remains part of the standalone retail
instruction contract. Never assume it is impossible for every call path.

The corrected candidate compiles in the owner under target-only O2/g0 to
114 words and 56 identical word positions per function, versus retail's 113;
79 normal-profile neighbors are unchanged. Alternative fallthrough and
return-placement shapes produced 116 or 117 words. A 32-bit native finite
screen including the returned value passes 96 cases per function at O0/O2/O3;
incorrect weights and mode controls fail. A guest screen executes the original
instruction window with a modeled callback and helper on all 20 qualifying
retail table entries and four seeds, 80 cases total. Retail and corrected
candidate agree on the consumed return, counter, bounded external state, and
helper calls in that window. Deliberately changing the candidate return by one
fails the window check. This is a bounded instruction-window model, not full
parent execution or hardware/gameplay evidence.

Private reproducibility artifacts are in the ignored
`conker/build/game-three-interpolated-callbacks-screen/`: `return_screen.py`,
`dispatch_window_return.py`, `dispatch_window_bad_return.py`,
`native_return10_screen.py`, `return_shapes.py`, and
`owner_mixed_return10.py`. The scratch directory can be cleaned; the source in
Note 2309 remains historical, not the corrected interface.

Next, seek a correct return-bearing source shape and investigate how to retain
the retail zero-count return behavior without claiming defined C behavior that
is not established. Re-run the complete finite, caller, access, stack,
relocation, native, both-tools, actual Make, and independent whole-image
checks on any proposed final candidate. The shared helper
`func_1500AF08` remains a stub. The verified Game checkpoint remains
**3,704 / 4,840 (76.53%)**; 168 matches are needed for 80%.
