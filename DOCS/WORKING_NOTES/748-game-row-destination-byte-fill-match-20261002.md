# Game Row Destination Byte Fill

Date: 2026-10-02

## Retail Contract

Recovered `func_1501CDC0` in `conker/src/game/generated_49D30.c` from its
zero-return placeholder. Retail occupies `0x1501CDC0..0x1501CE54`, 37 words /
148 bytes, at ROM `0x4A270..0x4A304`.

The signed argument selects a count byte in `D_800C363A` and a destination
pointer-table row in `D_800C3960`. Retail computes a 120-byte row offset.
The local declaration `u8 *D_800C3960[][30]` represents this guest row stride
using four-byte pointers; it does not establish a runtime count bound or a
new capacity check.

Zero count skips destination accesses. Otherwise the routine fills the first
sixteen bytes of each active destination with `0xFF`. The inner loop has four
explicit stores per pass and runs four passes. The destination pointer is
loaded anew before every store; it is not a cached pointer or a `memset` call.
Between destinations the count byte is read again, then the index advances
and the slot pointer moves by one guest word.

The inspected call site at `0x1501D9BC` in `conker/asm/49D30.s`
immediately calls another routine and does not consume this routine's result.
The recovered function is `void`; the retail count accumulator's incidental
final value in `$v0` is not claimed as a return contract.

## Compiler Recovery

The first return-count trial emitted 38 words, adding a return move and
exceeding the fixed slot by one word. Recovering a void contract emits 37
words with the retail register allocation. Moving counter initialization
inside the nonzero-count arm changes register allocation and is not retained.

The existing slice profile already disables compiler loop unrolling.
The final source explicitly spells out the four stores, while keeping the
inner offset and outer destination loops intact. No profile override is added.

Two strict expected-word guards normalize only the independent opening
schedule at offsets `0x14` and `0x1C`: row-offset subtraction and counter
initialization exchange positions around the count gate, recovering the
retail branch-delay initialization. Both operations execute on either path;
they touch different registers and no memory. No instruction, branch,
relocation, or semantic operation is inserted or omitted.

## Behavior Verification

`tools/tests/test_game_row_destination_fill.py` extracts and compiles the
actual source in a freestanding 32-bit host fixture. Six tests cover:

- Zero count with a null destination slot that must not be dereferenced.
- One destination with four sentinel bytes on either side of the exact fill.
- Row selection, real four-byte pointers, and a 120-byte row stride.
- All thirty slots in a fixture row, preserving neighboring rows and counts.
- Duplicate destination pointers and repeated fills.
- A self-aliasing pointer slot: the first store changes that slot's low
  pointer byte, and subsequent stores must use the newly loaded pointer.

The fixture uses aligned storage and `-fno-strict-aliasing`. Its self-aliasing
case is intentionally a little-endian native pointer test, not a big-endian
guest replay or realistic gameplay buffer. It stays within the allocated
table storage and active count one. The target instruction check, rather
than the host fixture, proves retail's count reload and all pointer loads.

The ordinary cases compare every buffer byte and check pointer preservation.
No negative/out-of-range row, count beyond a fixture row, null active pointer,
concurrent mutation, or gameplay qualification is claimed. Capability checks
explicitly skip without freestanding 32-bit compiler/execution support.

All six new tests execute and pass. All 91 repository tool tests and
`make tools-check` pass.

## Linked Verification

The full `make -C conker NON_MATCHING=1 all match-progress -j4` rebuild passes.
Independent linked-byte comparison confirms all 148 bytes match the pristine
ROM. SHA-256:
`29e3e1c94d09fae0b194b19f01e357352734eb83325fc5b1260df8a5c2f0e5ab`.
The following `func_1501CE54` remains at `0x1501CE54`.

Both entire Init sections remain byte-exact after rebuilding: `.init` is
164,048 bytes and `.init_data` is 17,376 bytes. Their SHA-256 values remain:

- Code: `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf`.
- Data: `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239`.

This is linked code/data evidence, not BSS, gameplay, or a full-ROM match.

## Progress and Resume

Conversion totals remain 5,461 / 6,042 C rows. Exact C now totals
3,251 / 5,461 (59.53%); Game is 2,578 / 4,788 (53.84%). There are 2,210
different C functions and zero address drifts. Init retains 47 assembly rows;
the supported compiler-generated Init queue remains complete.

Next ordinary Game target: `func_15040CC8`, 38 words / 36 real differences.
Keep `func_150A76F0` in the handwritten/register-contract workstream and
`func_150F631C` in its separate near-match cleanup queue. No sibling host-port
source, build, or runtime artifact was changed.
