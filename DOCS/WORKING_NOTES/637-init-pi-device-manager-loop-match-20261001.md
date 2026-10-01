# Init PI device-manager loop match

Date: 2026-10-01

`func_10002E50`, also linked as `__osDevMgrMain`, occupies 148 words and 592
bytes at `0x10002E50..0x1000309C`. The former C implementation returned zero
and left the complete PI command-thread behavior in assembly.

The recovered routine receives `OSIoMesg` commands from the device manager's
command queue and dispatches the retail message types. DMA reads and writes use
the manager's `dma` callback; extended DMA reads and writes use `edma` with the
message's PI handle. Loopback messages are returned immediately, while unknown
types are rejected.

The DMA-read path also preserves Conker's direct-PI ownership handshake. If
`D_8003A572` reports direct PI activity, the routine raises `D_8003A575`, stops
the PI manager thread object at `D_80035910`, and clears the deferred-stop flag.
It marks `D_8003A573` while the queued transfer is active and clears it after
the matching completion event has been returned.

Successful transfers wait on the event queue, return the original message to
its response queue, and release the device-manager access queue. The switch
uses the canonical libultra case order, which is significant to IDO's block
layout, and owns retail jump table `jtbl_8002C080_init` through the source
object's build rule.

The recovered source emits the retail 96-byte frame, saved-register lifetime,
jump-table layout, branch-delay slots, and complete 148-word extent directly.
No expected-word guards or compiler-normalization patches are required.

A full stale-check build and authoritative linked matcher pass classify the
function byte-exact. The linked and retail 592-byte spans share SHA-256
`827b2c980c11c00f6ac52be3d05a66941f1d7a4d2850bd4a5a4d3263e5123ba2`.
Project tool checks and all 10 tool unit tests pass.

The matcher advances to `3,136 / 5,457 (57.47%)` overall and
`453 / 488 (92.83%)` in Init, with zero address drift and 35 genuinely
different Init C rows.
