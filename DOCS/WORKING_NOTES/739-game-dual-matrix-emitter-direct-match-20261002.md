# Game Dual Matrix Emitter Direct Match

Date: 2026-10-02

Follow-up: [Note 740](740-game-secondary-timed-callback-record-match-20261002.md)
completes the next target `func_15158224`; ordinary Game work resumes at
`func_1515FFEC`.

## Recovery

`func_15157FE8` at `0x15157FE8..0x15158078` replaces its zero-return
placeholder with the complete 36-word / 144-byte display-list emitter in
`conker/src/game/generated_183640.c`.

The four-argument contract retains a display-list cursor, two unused argument
homes, and a signed record index. The first command loads a projection matrix
from `D_800BE628 + index * 0x180 + D_800BE9C0 * 0x40 + 0x100`. The second
multiplies the projection matrix from `D_800DC2A0[D_800BE9C0] + index * 0x40`.
Both append one eight-byte command and return the advanced cursor.

Local declarations establish `D_800BE628` as a pointer-owned record table and
`D_800DC2A0` as a pointer array. They do not churn unrelated shared headers.
The actual local F3DEX2 SDK `gSPMatrix` macro encodes the two command words
`DA380007` and `DA380005` using named projection/load/multiply/no-push flags.
No manual command opcode emitter replaces the SDK macro.

## Direct Compiler Match

The existing `-O2 -g3 -mips2 -o32` profile emits all 36 words directly from
C. The opening argument-home stores, repeated matrix-page loads, shifts,
record stride, table indirection, command stores, returned cursor, and nop
return delay slot match retail.

The pointer-arithmetic variant initially had five register-allocation
differences in the first record-address calculation. Expressing its loaded
base as a guest-width `u32` before address arithmetic restores the original
base-first calculation and removes all five differences. There are no new
word guards, insertions, omissions, or compiler overrides.

## Tests

Three new source-behavior tests extract the actual function body and the
actual `_SHIFTL`, `gDma2p`, `gSPMatrix`, and relevant F3DEX2 constants from
the repository SDK headers. Minimal host types retain four-byte command
words, eight-byte `Gfx`, and 64-byte `Mtx`; macros are not reimplemented.

Tests check both command words and low-32-bit matrix addresses, record/page
indexing, the returned cursor, preserved surrounding commands, and unused
argument independence. They cover page zero and one with record indices
zero, three, and seven. All 31 tool tests pass. These are source-level checks,
not a claim of fresh guest graphics rendering or host-port acceptance.

## Verification

`make -C conker NON_MATCHING=1 all match-progress -j4` passes. Independent
linked extraction matches all 144 bytes against pristine span
`0x185498..0x185528`. The following `func_15158078` stays at `0x15158078`.
The function SHA-256 is:

```text
dfa6f9cc4c06140ec1e89568380b5b83e09803167c3fc9cbe3cc9decffb5da95
```

The full Init code (164,048 bytes) and initialized data (17,376 bytes)
independently retain their exact baseline hashes. Project tool checks pass.
Existing pointer-type warnings elsewhere in the generated source remain
outside this change. No host-port source or frozen Release artifact changed.

The row was already counted as C because of its former placeholder, so C
conversion counts and bytes do not increase. Fresh matching results are:

- Total: 3,242 / 5,461 exact C (59.37%), zero drift, 2,219 different.
- Game: 2,569 / 4,788 exact C (53.65%), zero drift, 2,219 different.
- Init: 492 / 492 exact C; retained assembly 47 rows / 12,252 bytes.
- Debugger: 181 / 181 exact C; unchanged.

## Resume

The next ordinary Game target is `func_15158224`, 41 words with 35 real
differences in the fresh queue. Keep `func_150F631C` in its near-match cleanup
queue and `func_150A76F0` in its handwritten/register-contract workstream.
The custom Init MMIO/bitmap experiments remain deferred, not completed.
