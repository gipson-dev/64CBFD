# Init controller-pak read packet builder match

Date: 2026-09-30

`__osPackRamReadData` occupies 91 words and 364 bytes at
`0x10025E64..0x10025FD0`. The existing SDK packet builder was semantically
complete except for Conker's opening PIF RAM initialization.

The recovered loop clears all 16 words of the 64-byte `__osPfsPifRam` before
the routine constructs the controller-pak read request. The remaining SDK
logic sets the PIF execute flag, fills the read-command header and address
CRC, initializes the 32-byte data area, skips preceding controller channels,
copies the packet into PIF RAM, and writes the command terminator.

Establishing the PIF pointer before a signed literal-16 loop reproduces the
retail `-O1` address lifetime, signed `slti`, and register schedule. The
complete 91-word slot emits directly from C and retained padding. No
expected-word guards, insertions, or omissions are used.

The non-matching build compiles and links the updated object. The expected
whole-ROM checksum remains different because the project contains unrelated
non-matching functions. The authoritative matcher and direct 364-byte
section-span comparison pass. The linked and retail spans share SHA-256
`9cb0dfb5ca12bc56ef6b89440bad89924d74a4cf6b4957f1236eb3cd03c40400`.

The matcher advances to `3,110 / 5,457 (56.99%)` overall and
`427 / 488 (87.50%)` in Init, with zero address drift and 61 genuinely
different Init C rows.

Resume the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
