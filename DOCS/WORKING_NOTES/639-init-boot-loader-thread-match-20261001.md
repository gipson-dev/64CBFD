# Init boot-loader thread match

Date: 2026-10-01

`func_10001194` occupies 163 words and 652 bytes at
`0x10001194..0x1000141C`. The former C implementation was empty; an older
commented draft captured the broad boot sequence but treated ROM offsets as
globals and decoded one fewer relocation-table entry than retail.

The recovered thread initializes the loading subsystem, clears the available
RAM range selected by `osResetType`, and invalidates both caches over the main
boot allocation region. It initializes the low-level managers, allocates two
`0x1ECC0`-byte framebuffers, and creates the VI manager.

The routine reads the compressed Game-image header from ROM offset `0x42450`,
allocates the required transfer span through `0x19EA88`, loads and decompresses
that image, and performs the post-load setup call. It derives the Game overlay
page count from `func_15000000..D_151FA130`, aligns the destination and offset
table, reads `(blockCount + 2)` entries, then decodes exactly
`blockCount + 1` offsets using retail key `0x8039CCCA` and the ROM base.

The final sequence clears `D_8003BE74`, selects asset `0xEB`, and enters the
remaining initialization and Game startup calls. A linker-address alias for
`D_151FA130` preserves retail's data-style relocation to the end of the Game
section rather than misrepresenting that boundary as a callable function.

The semantic source restores the retail 80-byte frame, saved `s0` lifetime,
stack-slot reuse, loop count, branch topology, and exact 163-word extent.
Eighty-seven words emit directly from C. Seventy-six stale-checked rows
normalize IDO's remaining allocation and scheduling cycles; relocation-aware
rows preserve calls, globals, and the two Game-section boundary addresses.

A repository-wide stale-check rebuild and authoritative linked matcher pass
classify the function byte-exact. The linked and retail 652-byte spans share
SHA-256
`681ac3de3b09479dfe0890da9d095fded0097f673189325a1b87e771a0ee983e`.
Project tool checks and all 10 tool unit tests pass.

The paused checkpoint is `3,138 / 5,457 (57.50%)` overall and
`455 / 488 (93.24%)` in Init, with zero address drift and 33 genuinely
different Init C rows. The smallest three rows remain parked; the next
unparked candidate by size is `func_10010BE8` at 164 words.
