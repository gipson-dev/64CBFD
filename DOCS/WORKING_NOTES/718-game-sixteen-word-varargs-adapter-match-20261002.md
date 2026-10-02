# Game sixteen-word varargs adapter match

Date: 2026-10-02

`func_15042E3C` now matches all 36 retail words at
`0x15042E3C..0x15042ECC`. The former fixed 17-parameter C body assigned each
incoming word separately. IDO emitted a 39-word body, so retail padding moved
it to the overflow section and left a trampoline in the original slot.

The retail entry homes all four argument registers, initializes a `va_list`
after the first named argument, and copies sixteen `s32` values into a local
array. IDO unrolls the loop four ways, including the repeated four-byte
alignment operations from the SDK `va_arg` macro. The completed array and the
first named argument are then forwarded to `func_15042ECC`.

Recovering the true varargs signature removes the overflow trampoline and
reproduces the complete retail loop. Declaring the `va_list` before the local
array gives the array its retail `sp+0x24` location. The frame, register homes,
unrolled loads and stores, branch delay, call, and epilogue all emit directly
from C. No expected-word guards, checked insertions or omissions,
relocation-aware rows, or compiler-profile override are required.

The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with zero
address drift. The linked span at file offset `0x702BC` and retail span at
`0x702EC` are identical across all 144 bytes, with SHA-256:

```text
960b46d7d58ab64501ae1b5c769920c38ce12c5d9833b30f0abfee63db919a0a
```

The patch audit reports 10,343 total rows, zero rows for `func_15042E3C`, and
no duplicate patch keys. Game advances to `2,558 / 4,788 (53.43%)`, with
2,230 different C rows; overall byte-exact C progress is
`3,226 / 5,456 (59.13%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`. `make tools-check` also passes. No fresh
gameplay run was performed.

Resume the ordinary small-Game queue with 35-word `func_150634E4`, currently
at 35 real differences. Keep `func_15015F40` parked behind unresolved
indirect-table ownership and `func_150A76F0` in the handwritten
register-contract workstream.
