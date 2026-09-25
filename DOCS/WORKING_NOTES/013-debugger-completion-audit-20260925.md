# Debugger completion audit - 2026-09-25

## Completion result

The US debugger section is finished. Its complete `progress.csv` inventory is
182 tracked rows:

| Classification | Rows | Exactness evidence |
| --- | ---: | --- |
| C | 181 | `match_progress.py`: 181 / 181 byte-exact |
| Original handwritten assembly | 1 | direct 40-word linked-ELF/retail comparison: 40 / 40 exact |
| Total | 182 | 182 / 182 accounted for and exact |

The apparent 181 / 182 conversion figure does not identify unfinished
debugger work. It preserves the source-language distinction for
`func_16003650`, the original handwritten routine at
`0x16003650..0x160036EF`.

## Handwritten boundary

`func_16003650` iterates over all 32 TLB entries and records EntryLo0,
EntryLo1, EntryHi, and PageMask values. Its source contains the privileged
`mtc0`, `tlbr`, and `mfc0` instruction sequence and is explicitly marked
`/* Handwritten function */`. IDO C cannot emit these operations, so retaining
the assembly is the correct completed representation, not a deferred
conversion.

The linked function contains 40 words. A direct comparison mapped VRAM
`0x16003650` through the US debugger segment to `conker.us.bin` and compared
those words with `build/conker.us.elf`; every word matched. `progress.csv`
contains no other debugger assembly row.

## Validation snapshot

- Linked matcher: debugger `181 / 181 (100.00%)`, zero address-drift blockers,
  zero differing C-classified rows.
- Handwritten function: `40 / 40` linked words equal retail.
- Inventory: 181 C-classified rows plus one assembly row equals 182 total.
- Full linked build had already passed before this audit.

Debugger work should only be reopened for a newly demonstrated regression or
new scope. The active decomp matching boundary is now the two-difference game
queue recorded in Working Note 012.
