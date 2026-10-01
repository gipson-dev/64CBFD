# Init audio-runtime bootstrap match

Date: 2026-10-01

`func_10008F90` occupies 271 words and 1,084 bytes at
`0x10008F90..0x100093CC`. Its previous compiled body returned zero while a
large incomplete recovery remained commented out below it.

The recovered body installs the audio DMA and resource callbacks, selects the
AI output frequency, derives and rounds the per-frame sample counts, copies
the two synthesis parameter areas, and initializes the n_audio globals. It
then constructs the streaming and command record pools, allocates the command
buffers and two audio frame records from the configured heap, creates four
message queues, and starts the audio thread at the requested priority.

Compiling the recovered body in the original owner perturbs IDO's retained
translation-unit state and changes already matched functions that follow it.
The Makefile therefore uses the established scoped `--function-object`
mechanism: the normal owner compile retains its original placeholder for
neighbor stability, while a macro-enabled compile supplies only
`func_10008F90`. That isolated body preserves retail's `0x270` frame and six
saved-register lifetimes, and emits 263 semantic words. One hundred
thirty-nine function-scoped, stale-checked rows normalize the remaining
allocation and layout differences, including eight checked insertions and 45
rows with explicit relocation data. One hundred twenty-four source words emit
without a guard.

The targeted object rebuild accepts every expected word and relocation, the
complete repository rebuild succeeds, and the full linked ELF completes
successfully. Direct comparison of `0x10008F90..0x100093CC` reports zero
different bytes. Both 1,084-byte spans share SHA-256
`7d897607c391e61d966f2a5e6f8cff10d99527081e8193fb3d7b01c73dee38c3`.

The refreshed matcher reports `3,155 / 5,456 (57.83%)` byte-exact C functions
overall and `472 / 487 (96.92%)` in Init, with zero address drift and 15
different Init C rows. The next smallest measured Init candidate is the
275-word `func_1000CEAC`, currently different in 273 words.
