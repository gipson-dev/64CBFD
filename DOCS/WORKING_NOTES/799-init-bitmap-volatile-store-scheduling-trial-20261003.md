# Init Bitmap Volatile Store Scheduling Trial

Date: 2026-10-03. Baseline: `8bf34ba`.

## Result

Three new ordered-store source forms for `func_10005BE0`, compiled under two
IDO profiles, still do not reproduce its nineteen-word slot. The experiment
tests a concrete new scheduling hypothesis after the ordinary-store forms
in [Note 751](751-init-bitmap-loop-mask-profile-trials-20261002.md): whether
volatile pointed-byte stores and an explicit saved comparison prevent the
extra comparison/back-edge operations.

All three actual host candidates pass 79 cases. No production Init owner,
compiler setting, header declaration, or instruction guard is changed.
Init remains 492 C / 47 assembly rows. The failed matching hypothesis is
banked as reproducible tooling, not an achieved conversion.

## Source And Reproduction

`tools/experiments/init_bitmap_ordered.c` snapshots both endpoint pointers,
writes through volatile byte pointers, reloads the signed count after filling,
and uses an explicit decrement followed by `(2u << bits) - 1` for the tail.

- Shape 1: inclusive postincrement comparison after each store.
- Shape 2: save `cursor != end`, increment the cursor, then test that value.
- Shape 3: unconditional store, break on endpoint equality, otherwise increment.

Run from the repository root in WSL:

```sh
python3 tools/experiments/compile_init_bitmap_ordered.py
```

The driver compiles warning-clean host executables, runs their cases, then
compiles IDO `-O2 -g3` and `-O1` objects. Each object is independently linked
at `0x10005BE0` with the three retail global addresses. GNU objcopy extracts
the text section; binary words through the final return delay slot are compared
with pristine ROM `0x5BE0..0x5C2C`. Output objects, logs, disassembly, and JSON
remain under ignored `conker/build/init-bitmap-ordered`.

## Measurements

Each cell is body words / differing aligned positions. Retail is 19 words.

| Shape | `-O2 -g3` | `-O1` |
| --- | ---: | ---: |
| Volatile postincrement | 20 / 19 | 31 / 31 |
| Volatile saved comparison | 20 / 19 | 34 / 34 |
| Volatile break loop | 20 / 19 | 32 / 32 |

The first two optimized forms retain the XOR comparison temporary. The break
form instead emits an equality branch with the store in its delay slot and an
additional unconditional back edge with the increment in its delay slot.
Its explicit mask decrement does emit `-1` rather than the earlier equivalent
shift-count `+31`, but the whole function still exceeds the slot and differs
in opening loads, control flow, and register allocation. This is not an
independent scheduling-only repair; no broad guards are added.

## Behavior Evidence And Limits

The actual host C tests 77 bounded endpoint/count cases twice: counts 1..64,
zero with an explicit single-byte endpoint, four negative signed-halfword
values, seven characterized retail counts, and 32,767. Every buffer byte,
including surrounding sentinels, is checked after both calls.

Two additional alias cases verify that filling both count bytes causes the
post-fill read to use low-three-bit value seven, and that filling the endpoint
pointer's storage still uses the original captured endpoint for the tail.
These tests use the native host data representation; they are not MIPS guest
execution or a general invalid-pointer/overflow proof. Reversed endpoints
and arbitrary pointer wraparound are not run as native C fixtures.

The runner compiles with host `-O2 -std=c99 -Wall -Wextra -Werror`.
All 237 shape/case combinations pass; all six guest compiles/links complete.
Python syntax and project tool checks pass. No matching conversion or README
aggregate increase is claimed.

## Next

Keep this leaf's original assembly and its characterized contract. Another
attempt needs a distinct compiler/dataflow explanation, not this same matrix.
Continue the connected Game dispatcher `func_1507C22C` instead of treating a
twenty-word approximate Init body as a completed nineteen-word conversion.
