# Init audio-library bootstrap match

Date: 2026-10-01

`func_10008180` occupies 214 words and 856 bytes at
`0x10008180..0x100084D8`. Its previous C body was a zero-return placeholder,
despite the retail function being the main Init audio-library bootstrap.

The recovered semantic body initializes the `0x3E000`-byte audio heap and
synthesizer configuration, loads the bank file and its control/table data,
relocates the bank, and publishes its first bank. It then loads and fixes the
sequence-file metadata, rounds all 150 sequence lengths upward to even byte
counts, initializes the shared sequence-player configuration, allocates and
attaches three sequence players, and configures the sound player and its final
channel settings. The call site in `src/game/entrypoint.c` now uses the retail
routine's actual `void` return type.

IDO emits the complete behavior in 213 words, but chooses a `0x108` stack
frame instead of retail's `0xF0` frame and makes a different closed allocation
through the sequence loop and three-player setup. Sixty-four function-scoped,
stale-checked rows normalize that compiler residue. One row inserts the retail
sequence-pointer delay-slot update, and 10 rows explicitly move HI16/LO16
relocations among the equivalent sequence and player setup instructions. The
remaining rows preserve the recovered semantics while restoring stack offsets,
temporary registers, and the loop latch. No broad or unchecked binary patch is
used.

A targeted object rebuild accepts every expected word and relocation. The
full linked ELF completes successfully, and direct comparison of
`0x10008180..0x100084D8` reports zero different bytes. Both 856-byte spans
share SHA-256
`e5edcb6039f9b8e816dacd1dea8996ed458a81fa7a68f9f342ef13de781a5dbf`.
`make tools-check`, all 11 focused tool unit tests, and `git diff --check` pass.

The refreshed matcher reports `3,151 / 5,456 (57.75%)` byte-exact C functions
overall and `468 / 487 (96.10%)` in Init, with zero address drift and 19
different Init C rows. After this focused checkpoint is committed, the next
measured Init candidate is `func_100049E0`.
