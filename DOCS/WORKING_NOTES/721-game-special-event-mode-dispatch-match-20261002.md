# Game special-event mode dispatch match

Date: 2026-10-02

`func_15015F40` replaces its zero-return placeholder with the 31-word retail
routine at `0x15015F40..0x15015FBC`. The function accepts a signed 16-bit
index and an event value. Events `0x1A`, `0x24`, `0x2B`, `0x2D`, `0x30`,
`0x33`, `0x34`, and `0x3F` set `D_800BE616` to one and publish
`func_151E5FAC() - 1` in `D_800BE9E8`. Every other event clears the mode byte
and publishes the signed input index minus one.

The previously unresolved 38-entry dispatch membership is now authoritative.
The retained retail asset `conker/assets/23B040.bin` contains the table at
relative offset `0x140`, corresponding to retail file offset `0x23B180` and
symbol `jtbl_800966C0_game`. Its entries cover events `0x1A..0x3F` and point
only to the special path at `0x15015F78` or default path at `0x15015F98`.
The complete 152-byte table has SHA-256:

```text
8dde52cf61dbed5487b81132f0f6b129d4f670e10b9182c3d99b58452e69de1e
```

The recovered C switch makes IDO reproduce all 31 retail instructions,
including the narrow-argument home and sign extension, range gate, indirect
jump, special-path call schedule, default stores, and epilogue. The owner
object now uses the established `RETAIL_RODATA_SYMBOL` mechanism to retarget
the compiler's local `.rodata` relocations to `jtbl_800966C0_game`. No
expected-word guards, checked insertions or omissions, or compiler-profile
override are required. This resolves the function's table ownership; it does
not claim that the repository's broader interleaved Game data-section layout
is complete.

The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with zero
address drift. The linked span at file offset `0x433C0` and retail span at
`0x433F0` are identical across all 124 bytes, with SHA-256:

```text
e8aa67cb66e0a2e31c0fe77b49c77a9f6da523dca2c82f69c3e663b89a75dfa7
```

The patch audit remains at 10,358 total rows, with zero rows for
`func_15015F40` and no duplicate patch keys. Game advances to
`2,561 / 4,788 (53.49%)`, with 2,227 different C rows; overall byte-exact C
progress is `3,229 / 5,456 (59.18%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Continue with
[Working Note 722](722-game-selector-vector-output-initializer-match-20261002.md),
which completes 41-word `func_150B060C` directly from semantic C. Keep
32-word `func_150A76F0` in its documented raw-assembly workstream and resume
the ordinary queue with 40-word `func_150DF820`.
