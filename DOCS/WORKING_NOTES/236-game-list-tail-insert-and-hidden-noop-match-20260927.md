# Game list-tail insertion and hidden no-op match - 2026-09-27

## Result

`func_151957B0` is byte-exact across 29 words and 116 bytes at
`0x151957B0..0x15195824`. Newly tracked `func_15195824` is byte-exact across
two words and eight bytes at `0x15195824..0x1519582C`. Fresh totals are
2,739 / 5,469 (50.08%) exact C functions overall and 2,168 / 4,791 (45.25%)
in Game.

## Recovery

`func_151957B0` allocates an eight-byte doubly linked-list node, clears its
forward link, and inserts it at the tail represented by `arg2`. For a nonempty
list, the new node points back to the old tail, the old tail points forward to
the new node, and `*arg2` advances. For an empty list, both `*arg1` and `*arg2`
receive the new node. Allocation failure leaves both list endpoints unchanged.

The old C expressed the empty-list arm first and reused its cached old-tail
value. Retail lays out the nonempty arm first and reloads `*arg2` before
writing the old tail's forward link. Reversing the condition and preserving
that repeated load makes IDO reproduce all 29 words directly, including the
`a0` tail pointer, retained `a1` result, branch-likely empty path, and store
delay slot. No guarded retail-word entries are required.

The old tracked extent also absorbed a complete second `jr ra; nop` body at
`0x15195824`. Splitting that pair in the retail assembly, layout, and symbol
metadata identifies independent no-op `func_15195824`; an empty `void` C body
emits its two words exactly.

## Evidence

Linked ELF offset `0x1D57B0` and decompressed retail offset `0x1C2C60`
compare equal across the combined 124-byte span. Both have SHA-256
`22c5d40b78c2f3bccdc1e6f6d0d4265b35303c4ef299109fd6b688c92acee6fd`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,739 / 5,469 (50.08%) | 1 | 2,729 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,168 / 4,791 (45.25%) | 0 | 2,623 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
combined-span hashes and `cmp`, replacement build, project tool checks, all
padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with 22-word `func_151A8A20`, the next unparked Game C row in the
fresh queue, with 20 real differences. Keep the previously documented
lower-difference rows parked.
