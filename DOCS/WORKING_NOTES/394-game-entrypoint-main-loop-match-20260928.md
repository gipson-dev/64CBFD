# Game entrypoint main-loop byte match

Date: 2026-09-28

## Scope

This pass replaced the false zero-return placeholder for `func_15007830` in
`conker/src/game/entrypoint.c` with the complete semantic Game entrypoint. The
retail slot spans `0x15007830..0x15007A20`, or 124 words and 496 bytes.

The object now retains its five-entry switch table as
`jtbl_80095A30_game`. `entrypoint.c` was removed from the C-padding exclusion
list and assigned that retained rodata symbol in `conker/Makefile`.

## Recovered behavior

The routine performs the Game-side startup sequence: it creates the main
message queue, initializes the entry state and global mode bytes, calls the
subsystem setup routines, and initializes the two global state words.

Its permanent loop dispatches `D_800BE615` states through the retail jump
table. States 1 and 5 begin with `func_151E50C8`; state 2 runs
`func_15017498`, conditionally submits event `0x81280783`, and forwards the
three signed halfword parameters at byte offset 2; state 3 runs
`func_15007B3C` and clears the mode. Every path reaches the shared
`func_100051E8` / `func_150186D0` cleanup before dispatching again.

The prior commented sketch had shifted switch cases and used 32-bit array
indexing for values that retail reads as signed halfwords. Those details are
now represented directly. `D_800BEA68` was also corrected from a pointer
declaration to the inline `struct195` object that retail addresses.

## Compiler normalization

IDO emits the complete calls, branches, jump-table control flow, delay slots,
and data accesses from the recovered C. It does not retain the shared constant
2 in `s7`; that choice shifts the six later saved-register lifetimes and
materializes one extra loop constant.

Sixty-six function- and offset-scoped expected-word guards normalize that
closed allocation cycle. The set includes relocation-aware movement of the
jump-table and call words. Two guarded insertions restore the unreachable
retail epilogue words omitted by the semantic compile. The guard manifest has
no duplicate `(filename, function, offset)` keys.

## Verification

- The focused `entrypoint.c.o` build passed with all expected words and
  relocations validated by `pad_c_object.py`.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_15007830` as byte-exact.
- The linked and retail 496-byte spans share SHA-256
  `35409e3b55dd3cc62229f6fe0dbb7d58cfa76db9b03e30b1dec4c8c621b22e90`.
- `make tools-check` passed, and all nine tests under `tools/tests` passed.
- Fresh matcher totals are `2,896 / 5,466 (52.98%)` overall and
  `2,322 / 4,790 (48.48%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 30-word `func_1518CCA8`, currently at
25 real differences. Keep `func_151F3D78` parked behind the pre-existing
audio-object layout drift, keep the tied Init SDK cache routines in their
ownership lane, and keep address-drift row `func_10012588` parked.
