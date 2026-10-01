# Init VI manager creation match

Date: 2026-09-30

`osCreateViManager` occupies 94 words and 376 bytes at
`0x100034E0..0x10003658`. The empty placeholder is replaced with the recovered
libultra VI manager creation routine.

The routine rejects duplicate initialization, starts timer services, creates
the five-entry VI event queue, and configures the retrace and counter messages.
It temporarily raises the caller's thread priority when needed, disables
interrupts while publishing the manager state, creates the VI manager thread,
initializes VI state, starts the thread, and restores both interrupts and the
caller's prior priority.

The canonical source is retained locally in `tools/ultralib/src/io/vimgr.c`.
In retail, the manager thread's stack top and the event queue occupy the same
boundary address but remain distinct source symbols. Expressing the stack top
as the adjacent message-buffer base minus `sizeof(OSMesgQueue)` preserves that
separate IDO materialization without introducing an artificial alias symbol.
The result emits the exact 94-word extent, 48-byte frame, and complete retail
schedule directly from C. No word guards are required.

The focused object build, full ELF link, authoritative matcher, project tool
checks, and direct 376-byte section-span comparison pass. The linked and
retail spans share SHA-256
`a2bae43e3aad95cb561f2ee54b5d0a09c7a71b1dd254f71dce0c90b0e0dbbabd`.

The matcher advances to `3,115 / 5,457 (57.08%)` overall and
`432 / 488 (88.52%)` in Init, with zero address drift and 56 genuinely
different Init C rows.

Resume with adjacent `viMgrMain`, whose canonical SDK body is in the same local
reference file. Its retail span is 102 words at `0x10003658..0x100037F0`.
