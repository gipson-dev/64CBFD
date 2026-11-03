# Working Note 2049: Game timed packet callback guarded match

Date: 2026-11-03

## Result

`func_1515BAE0`, owner `conker/src/game/generated_188F90.c`, retail VA
`0x1515BAE0..0x1515BBF0`, ROM `0x188F90..0x1890A0`, is restored from its
zero-return placeholder as semantic C. The retail `-O2 -g3` owner profile now
matches all 68 words and the original `0x28` frame. Two checked word guards
normalize only IDO's callback-result spill width:

- `+0x070`: natural `sw v1,0x24(sp)` becomes retail `sb v1,0x23(sp)`;
- `+0x080`: natural `lw v1,0x24(sp)` becomes retail `lbu v1,0x23(sp)`.

The two words are an isolated byte-versus-word completion-value home. They do
not replace a branch, helper call, global binding, record access, or callback
dispatch. The same compiler artifact is already represented in the related
timed-callback family at `func_15158224`.

The recovered update:

1. tests bit zero of the record flag byte at `+0x11`;
2. when enabled, subtracts signed frame step `D_800BE9E4` from the signed timer
   at `+0x14` and starts removal when the result becomes negative;
3. otherwise dispatches signed update selector `+0x38` through
   `D_8008B078`, treating a zero callback result as a removal request;
4. when packet pointer `+0x1C` is nonzero, calls `func_1514401C` with mode
   `+0x10`, packet address `+0x1C`, cursor address `+0x18`, and command
   `+0x12`; its low result byte becomes the final removal state, including the
   retail behavior that may clear an earlier update-callback request;
5. when removal remains active, dispatches signed final selector `+0x39`
   through `D_8008B07C`; and
6. releases the record with `func_1516972C` when that final callback returns
   nonzero, or directly when selector `+0x39` is `-1`.

The installed source uses named signed and unsigned fields for the recovered
record view and typed callback tables. In particular, both selector bytes are
signed, the timer is signed 16-bit, and the packet-helper result is narrowed
to the same low byte that retail spills and reloads.

## ABI and ownership

The routine has no direct `jal` caller. Its sole aligned function-pointer
literal is at ROM `0x23131C`, the callback field at `0x8008C85C` in the
anonymous descriptor beginning at `0x8008C858`. The callback takes one record
pointer and returns `void`.

The nine function/global relocations are:

- `+0x018/+0x02C`: `D_800BE9E4` HI16/LO16;
- `+0x058/+0x068`: `D_8008B078` HI16/LO16;
- `+0x0A0`: `R_MIPS_26:func_1514401C`;
- `+0x0BC/+0x0CC`: `D_8008B07C` HI16/LO16; and
- `+0x0E4/+0x0F4`: `R_MIPS_26:func_1516972C`.

The selected owner comparison retains all ten neighboring bodies. The strict
linked-image comparison contains 6,051 functions, changes only
`func_1515BAE0`, keeps every function address fixed, and uses zero exclusions.
Protected Game data remains exact across 189,088 bytes and 720 owners with
SHA-256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Permanent qualification

The tools were committed before source installation as `27e1a72`
(`test(game): qualify timed packet callback`). The permanent harness consists
of:

- `tools/experiments/game_timed_packet_callback_candidates.py`;
- `tools/experiments/game_timed_packet_callback_match.py`; and
- `tools/tests/test_game_timed_packet_callback_match.py`.

The installed three-test suite proves:

- 264 guest executions from 132 cases at entry phases zero and eight;
- all 68 retail words visited;
- signed timer behavior, subtraction wrap, both selector sentinels, update and
  final callback dispatch, packet-result overwrite, record mutations, and call
  clobbers;
- native O0/O2/O3 execution; and
- eight effective semantic controls: wrong flag bit, zero expiry, inverted
  update result, inverted packet presence, full-width instead of low-byte
  packet result, swapped packet/cursor pointers, inverted final-callback
  result, and missing sentinel release.

The installed suite passes all three tests in 27.773 seconds. The current
shared match-progress, generated-word-patch, PC16, and protected-data suite
passes all 19 tests in 36.144 seconds. The two guard rows are checked for stale
expected words by the complete owner/image gate.

## Frozen evidence

| Artifact | SHA-256 |
| --- | --- |
| Natural compact payload with relocation fields normalized | `7bc36c213ea35d0ff56e589c55e331778c866338bc64bd4dc0878f462250616d` |
| Mini-linked guarded candidate | `6e31f278cc58d333b162bcf63c22e9b2d242e54ce2b96cff24f00ec6c8a50e14` |
| Retail linked body | `25311acc5110ab6cab187ee93422a646099b3da0b0dcdd76378fed0b7b255da0` |
| Installed source | `4dce2233f947bd056c79b2ee4c83acf0a4594bc0a7cda657039fede4dd73865e` |
| Qualified/production owner object | `2fe3427a143d9725546afc9059c3c9345fef44780a9353d6ce4dc89ddf0efb9a` |
| Predecessor linked ELF | `24e0ca960552ee92f5b2ef0b3584f910bee36f23cc9ac07b8f00f8aec839be36` |
| Qualified/production linked ELF | `1d0569b59a52f3e64cf44276ce81919f7d9cdfaecc43c3b7daec7b061e99839f` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Installed guard table | `319c0f9fc120b65487e5a2c0455b279e5b312aae5cf11470d4804b61fc9ca5f5` |

The actual production Make rebuilt the complete Game and libultra object set,
padded every generated owner, linked `conker.us.elf`, and emitted
`conker.us.bin`. It stopped only at the expected final whole-ROM SHA mismatch
while the decomp remains incomplete; there were no compile, assembly, padding,
or link errors. The production owner and ELF reproduce the independently
predicted hashes above exactly.

## Recount

The fresh production ELF reports:

- Total: **4,119 / 5,511 (74.74%)**, zero address drift, 1,392 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,446 / 4,838 (71.23%)**, zero drift, 1,392 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **290 more** are needed.

## Graph retention

The required bounded Graphify update retained 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. It rebuilt a 58,227-node
graph with 112,180 edges and 4,983 communities; visualization was skipped at
the configured 5,000-node limit. An independent comparison against the
preserved pre-refresh graph retained 58,215 of 58,218 prior node IDs, removed
three changed-corpus IDs, and added twelve changed-corpus IDs.

The retained/refreshed `graphify-out/graph.json` is 75,496,764 bytes with
SHA-256 `d8d332276c41b1895e2a560ea9dd61914aefa87938a394ba9528d2c0536f8b1e`.
The update used Graphify's incremental ten-path mechanism, deterministic hash
seeding, one worker, and `force=False`. This is bounded old-node retention
evidence, not a full-corpus extraction claim.

## Continuation

The seven smaller entries remain in their documented handwritten/custom-ABI
lane: `func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC`, and `func_150A6760`. The fresh ordinary
queue starts at `func_151732E0` (62 words, 61 real differences), followed by
the remaining 61-difference tie. Every candidate still requires source,
ABI/caller, owner, guest/native, actual Make, complete-image, protected-data,
production recount, documentation, and graph-retention gates before credit.
This static qualification does not claim gameplay or hardware acceptance.
