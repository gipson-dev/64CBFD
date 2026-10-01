# Init controller-pak write packet builder match

Date: 2026-09-30

`__osPackRamWriteData` occupies 96 words and 384 bytes at
`0x10025AA0..0x10025C20`. The existing SDK packet builder was semantically
complete except for Conker's opening PIF RAM initialization.

The recovered loop clears all 16 words of the 64-byte `__osPfsPifRam` before
the routine constructs the controller-pak write request. The remaining SDK
logic sets the PIF execute flag, fills the write-command header and address
CRC, copies the 32-byte payload, skips preceding controller channels, copies
the packet into PIF RAM, and writes the command terminator.

Establishing the PIF pointer before a signed literal-16 loop reproduces the
retail `-O1` address lifetime and opening schedule. The initial channel loop
used equivalent `ptr++, i++` updates in its `for` clause, but IDO placed the
pointer store before the loop branch and the index store in the delay slot.
Restoring the canonical `for (...; i++) { *ptr++ = 0; }` shape swaps those two
independent stores into retail order.

The complete 96-word slot emits directly from C and retained padding. No
expected-word guards, relocation rewrites, insertions, or omissions are used.
The focused object build, complete ELF link, authoritative matcher, project
tool tests, and direct 384-byte section-span comparison pass. The linked and
retail spans share SHA-256
`cdf63a7878b35bab75e7439410fc7835571158ed2351f8ed0f75196b8b429087`.

The matcher advances to `3,117 / 5,457 (57.12%)` overall and
`434 / 488 (88.93%)` in Init, with zero address drift and 54 genuinely
different Init C rows.

Continue the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
