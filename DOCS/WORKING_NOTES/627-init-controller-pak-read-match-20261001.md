# Init controller pak read match

Date: 2026-10-01

`__osContRamRead` occupies 145 words and 580 bytes at
`0x10025C20..0x10025E64`. The existing C already represented the controller-pak
read transaction, CRC check, status fallback, bounded retry, and 32-byte output
copy, but it omitted part of retail's retry preparation and retained a
redundant no-pak assignment.

After the initial write DMA and message receipt, each read attempt resets the
16 words of `__osPfsPifRam` to `0x000000FF` and clears `pifstatus`. Retail then
starts the read DMA, waits for completion, advances to the selected channel,
and copies the packed response into a local format record. A valid response is
CRC-checked; failure queries controller status and either returns that error or
retries with `PFS_ERR_CONTRFAIL`. A valid CRC copies all 32 payload bytes to the
caller buffer.

The recovered PIF reset loop reproduces retail's complete loop and global
stores. `CHNL_ERR` already computes `PFS_ERR_NOPACK` for the nonzero channel
error case, so removing the former explicit `else` assignment preserves that
result and recovers retail's direct fallthrough into the retry test. Those two
source corrections produce the complete 145-word routine directly from C. No
expected-word guards are used.

The complete ELF link passed. The authoritative matcher no longer lists
`__osContRamRead`; a direct comparison of all 580 bytes reports zero
differences, and the linked and retail spans share SHA-256
`bf8aa2ecac0083d38e003575c990c79882ead67450e9d1d777462ba2dea9b4be`.
Project tool checks pass. The focused unit suite passes all 10 tests, with 8
expected skips.

The matcher advances to `3,126 / 5,457 (57.28%)` overall and
`443 / 488 (90.78%)` in Init, with zero address drift and 45 genuinely
different Init C rows.

The duplicate Game routine `__osContRamRead2` remains a separate 145-word row
and is not claimed by this Init match.
