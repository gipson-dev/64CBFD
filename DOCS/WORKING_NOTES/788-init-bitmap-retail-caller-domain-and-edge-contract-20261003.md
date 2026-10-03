# Init Bitmap Retail Caller Domain And Edge Contract

Date: 2026-10-03.

## Result

The remaining bitmap leaf `func_10005BE0` is still retained assembly, not a
new C conversion. The new evidence narrows the caller-domain question from
[Note 782](782-init-pause-resume-conversion-assessment-20261003.md): the only
direct retail code JAL to resize wrapper `func_100014C4` is in
`func_15007B3C`, and its input-producing branches give positive counts.
An instruction-word-driven fixture now protects the leaf's edge contract.

## Direct Caller Evidence

Scan the aligned words of retail Init code `0x1000..0x290D0` and Game code
`0x2D4B0..0x2275E0` for JAL word `0x0C000531`. The only hit is ROM
`0x350D0`, VMA `0x15007C20`. This is a direct-JAL inventory, not proof that
indirect calls, tail jumps, or external/debug entries cannot reach the wrapper.
Setup JALs occur at ROM `0x13EC` (startup) and `0x1520` (resize wrapper).

The retail jump table at ROM `0x23A510`, VMA `0x80095A50`, has 45 entries
for categories `0x13..0x3F`. Its targets are:

- `0x15007B9C` for `0x1A`, `0x24`, `0x2B`, `0x2D`, `0x30`, `0x33`,
  `0x34`, and `0x3F`: base 259, except category `0x24` uses 243; category
  `0x33` or `0x3F` subtracts eight, and `0x34` adds eight.
- `0x15007BE0` for `0x13`: count 235 when a configuration flag is set;
  otherwise signed byte `D_800B0DF0->byte11 + 235`.
- `0x15007C10` for other entries and out-of-table categories: signed byte
  `D_800B0DF0->byte11 + 235`.

Therefore these input-producing paths have count range 107..362, all positive
and representable in the signed halfword used by setup. This is static input
arithmetic; pointer validity and actual runtime traversal are not demonstrated.
The fixture pins the full retail caller prefix through the resize call/delay
slot and checks the retail table plus input-producing words. It does not execute
the caller or establish that a corresponding recovered Game C body is correct.

Use retail bytes for this table audit. An initial absolute-address lookup in
the linked `.game_data` section did not yield this retail table; that lookup
was discarded and supplies no caller evidence. No Game-data parity is claimed.

## Leaf Contract Tests

`tools/tests/test_init_bitmap_assembly.py` decodes the actual nineteen words
from `conker/asm/init_5AB0.s`, checks their complete address interval and hash,
and models their integer operations, big-endian loads/stores, and branch delays.
It is a deliberately bounded instruction model, not an N64 emulator or guest
execution. Its reference SHA-256 is:

```text
fb041ca8620d0564873d0763acbed67a65f8b7ccfe4c5e175a7ef71631f12899
```

Eight tests cover:

- Complete slot `0x10005BE0..0x10005C2C`, including the nop return delay.
- Counts 1..64, direct-caller extrema/special counts, and 32767, covering all
  remainder classes, sentinels, repeated calls, ordered stores, and final cursor.
- Zero count with an explicitly configured single-byte endpoint: still stores
  `0xFF`, with the unconditional branch-delay decrement leaving `$a0 == -1`.
- Zero count with setup's `end = start - 1`: stores immediately and does not
  return within a 128-instruction budget. This is not an infinite-loop claim;
  the real address space/fault behavior is not modeled.
- Signed negative counts with a separately valid endpoint: final masking uses
  the low three bits, not a defensive early return.
- Count alias: filling its two bytes changes the subsequent signed load to
  `0xFFFF`, so the last-byte mask becomes `0x7F` even if the original count was 8.
- Endpoint-global alias: the loop and final store use the pre-fill endpoint
  snapshot, despite overwriting its global storage.
- Retail direct-call inventory and caller-domain evidence above.

Every modeled run also checks preservation of saved registers, gp, sp, fp, and
ra. The invalid-count and alias fixtures characterize the leaf in isolation;
they are not claims that ordinary gameplay reaches those configurations.

## Allocation Boundary

Setup uses signed-halfword `(count + 7) >> 3` for the requested bitmap size and
`start + size - 1` for the endpoint. Startup count 235 requests 30 bytes.
The allocator `func_10003C6C` clamps requests below eight to eight and rounds
to four bytes; a successful startup allocation therefore reserves at least
32 payload bytes, while the configured bitmap still spans 30 bytes.

That allocation rounding does not validate a zero-count endpoint. Nor does the
allocator alone prove its free-list payload cannot overlap configuration storage:
that requires initialization/free-list provenance. Its failure path can return
zero after the error callback. Allocation success and pointer validity are not
established by the static count proof.

## Verification And Next Work

All eight new tests, all fourteen focused Init tests, and all 439 tool tests
pass. Project tool checks pass. The preceding fresh build/matcher and
independent full Init
section comparisons are recorded in Note 782; no production source changes
occurred afterward. Init remains 492 C / 47 assembly rows, 492 / 492 exact C,
with both complete sections retail-exact. README aggregates are unchanged.

The next conversion experiment may use the positive direct-call domain as
evidence, but must retain the leaf's observed semantics unless a narrower
contract is explicitly justified. Establish allocator/free-list provenance and
a genuinely new compiler/dataflow hypothesis before another matrix. The prior
55 bitmap shape/profile trials are not rerun, and no large word-replacement
guard is added to manufacture a match. Keep MMIO `func_100038E0` secondary;
the other 45 Init assembly rows retain their SDK/hardware/shared-interface
boundaries. Pending Game dimension-helper recovery remains untouched.
