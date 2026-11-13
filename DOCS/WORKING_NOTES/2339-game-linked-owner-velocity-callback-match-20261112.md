# Game linked-owner velocity callback match

Date: 2026-11-12. `func_150D6CC4`, owner `generated_1028F0`, VA
`0x150D6CC4..0x150D6E60`, ROM `0x104174..0x104310`, now has its semantic
C body and matches all **103 retail words**. The prior source was a
zero-return placeholder. The observed caller passes a pointer as the unused
second argument.

The callback dereferences the linked target at owner offset `0xA8`, then
returns zero if the target's first word is zero or its identity byte differs
from the owner's saved byte. A null target is not an early-return case. For a
valid link it copies the target position with `func_150D6C98`, snapshots the
three velocity components, advances the vertical velocity using the timestep,
then calls `func_15131958` with the current velocity and linked factor. It
integrates the three position components from the old and new velocities using
`D_800BE9A4` and `D_800BE9A8`, and returns one. The local vector snapshot and
the loads after each helper call preserve the observed mutation and alias
behavior.

The compiler emits 103 words with the retail stack frame; 96 words already
agree at the same positions. Seven relocation-aware expected-word guards
normalize the address and vector-copy schedule, including moving the timestep
symbol's HI16/LO16 relocations. The guarded body and relocation bindings match
independently assembled retail through both padders. The compact register
metadata changes, but the assembled padded metadata is unchanged. All 16 other
owner functions, normalized pools and diagnostic categories were preserved.

Tools commit `f19a566` adds the qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_owner_velocity_150d6cc4 -v
```

The seven checks pass before and after installation with both the mounted tools
and staged sibling dependencies. They cover 1,536 modeled guest cases across
raw, retail and padded bodies, including helper mutations and candidate-body public
read/write traces; 192 overlapping owner/target cases; 282 modeled access-fault
cuts; 288 cases connected to all 30 instructions of the two byte-exact retail
helpers; and 48 cases through `D_80089760[30]` and the original
`func_151303EC` callback window at `0x15130A38`. Native 32-bit checks pass 384
finite cases at each of `-O0`, `-O2` and `-O3`, with eight effective negative
controls and UBSan. Guest non-finite arithmetic uses the instruction model;
these tests do not prove hardware exception or gameplay behavior.

A concurrent regression run initially exposed a shared temporary output path
between this packet and the previously matched `func_150D6F0C` packet. Tools
commit `938f4e6` separates those output directories and adds assertions for
their names. After that fix, both linked-owner suites and the earlier effect
callback suite each passed simultaneously; the two linked-owner suites also
passed with staged sibling dependencies. The production source and image did
not change as part of the test-harness fix.

The actual Make production build equals the independently planned shadow
image. The strict linked-image audit found 288 changed bytes with **zero
exclusions**; only `func_150D6CC4` changed, all 6,050 function addresses are
unchanged, and all 189,088 protected Game-data bytes remain exact. A fresh
production recount reports **3,728 / 4,840 Game matches (77.02%)**, **4,401 /
5,513 total matches (79.83%)**, zero drift, and **144** more Game matches
needed for 80%.

The scoped Graphify refresh retained all out-of-scope nodes: 59,937 before,
59,939 after, and three relocated IDs matched by signature. Its fail-closed
path retained 31,816 existing nodes; this was not a full-corpus extraction.
