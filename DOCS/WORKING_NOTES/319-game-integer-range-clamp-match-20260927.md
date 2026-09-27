# Game integer range clamp match - 2026-09-27

## Result

`func_15143DA8` is byte-exact across all 24 words and 96 bytes at
`0x15143DA8..0x15143E08`. Fresh totals are 2,823 / 5,469 (51.62%) overall and
2,251 / 4,791 (46.98%) in Game.

## Recovery

The previous C implemented the correct clamp behavior but used an ordinary
pointer, a conventional temporary swap, and repeated memory reads. Retail
homes the pointer parameter at `0(sp)`, captures it before the swap, caches the
input value for both comparisons, and performs the bound exchange through two
XOR temporaries. Expressing the parameter as a volatile pointer slot and those
lifetimes explicitly restores the complete 24-word control-flow shape.

Nine guarded words preserve retail's independent local-register allocation:
the captured pointer uses `t6`, the XOR temporaries use `v1` and `a3`, and the
upper-clamp store reload uses `t7`. No relocation or address is patched.

## Evidence

The rebuilt span at `build/conker.us.bin+0x171228` and pristine retail span at
`conker.us.bin+0x171258` compare equal for all 96 bytes. Both have SHA-256
`48fe80871bb5898a546f9cc24607c2e7623247fd8d33110039c6467297c2425a`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,823 / 5,469 (51.62%) | 1 | 2,645 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,251 / 4,791 (46.98%) | 0 | 2,540 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused build/disassembly, required full guard-table rebuild, linked
matcher, direct comparison, replacement build, outer ROM build, tool checks,
all seven relocation tests, guard-table validation, and whitespace check pass.
The guard table now has 1,424 rows with zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` retains its 1,659 pre-existing status entries. Frozen
Release was not built, modified, or launched; `conker_pc.exe` remains
13,712,896 bytes with timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 29-word Game `func_151640C0`, the next ordinary unparked C row at
23 real differences. Keep the documented smaller special-case rows parked.
