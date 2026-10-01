# Init handwritten bcopy restoration

Date: 2026-10-01

`bcopy` occupies 196 words and 784 bytes at
`0x10023A10..0x10023D20`. ROM extraction already produced the authoritative
handwritten assembly in the intentionally ignored generated path
`conker/asm/libultra/libc/bcopy.s`, but the split configuration classified the
slot as C and linked a simplified byte-loop substitute from
`conker/src/libultra/libc/bcopy.c`.

The restored assembly implements the original overlap-safe copy routine. It
chooses forward or backward traversal from the source and destination ranges,
peels bytes to the required alignment, performs unrolled 32-byte and 16-byte
copies, handles 4-byte words, and finishes with byte tails. Three trailing
`nop` words retain the complete retail slot boundary. This is original
handwritten code, so preserving it as assembly is the correct ownership model;
attempting to represent its register-level implementation as compiler output
would misstate the source provenance.

`conker/conker.us.yaml` now classifies the slot as `asm`, and the simplified C
file has been removed. A fresh split regeneration, full serial rebuild, and
final ELF link complete successfully. `make tools-check` and all 11 focused
repository tool unit tests also pass. Direct comparison of the linked
`0x10023A10..0x10023D20` span against the pristine ROM reports zero different
words. Both 784-byte spans share SHA-256
`9de2251afa4dd169a3c55e33d2be4c540174550516f075ec6a6f0f9855fb6e6d`.

Because `progress.csv` and `match_progress.py` measure C conversion, this
ownership correction moves one function and 784 bytes from the C totals to raw
assembly. The byte-exact C numerator remains unchanged. The refreshed matcher
therefore reports `3,150 / 5,456 (57.73%)` overall and
`467 / 487 (95.89%)` in Init, with zero address drift and 20 genuinely
different Init C rows.
