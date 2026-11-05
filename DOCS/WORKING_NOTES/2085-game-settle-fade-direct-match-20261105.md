# Working Note 2085: Game settle/fade callback direct match

Date: 2026-11-05

## Recovered interface and state transitions

`func_1517A84C` occupies `0x1517A84C..0x1517A958`, ROM
`0x1A7CFC..0x1A7E08`, in `generated_1A7260.c`: **67 words / 268 bytes**.
Its zero-return placeholder is replaced with a void callback taking a typed,
writable record. The recovered fields are signed halfword XYZ at `+0x90`,
angles at `+0x96`, signed byte spin at `+0x9C`, signed halfword XYZ speeds at
`+0xA0`, unsigned halfword timer at `+0xA6`, signed floor height at `+0xB0`,
and opacity byte at `+0xB3`. The original factory allocates `0xB8` bytes;
the typed portion ends at `0xB4` and the remaining tail is preserved.

When the timer is zero, the callback adds all three speeds to the stored
positions, with signed halfword wrapping. A positive Y speed is decremented;
when that reaches zero it becomes -3. The callback compares the newly stored
Y coordinate to the floor. At or below the floor it sets X angle to 90,
clears Z angle, sets the timer to 60, and clamps Y. Above the floor it adds
the three signed spin bytes to the corresponding halfword angles.

When the timer is nonzero, it computes a wrapped 32-bit difference from
`D_800BE9E4`. A positive difference is stored back to the unsigned halfword
timer. Opacity is its wrapped 32-bit left shift by eight, reinterpreted as
signed and divided by 60 with truncation toward zero, then narrowed to a byte.
Nonpositive differences call `func_1516972C(record)` without first storing
the expired timer. Explicit unsigned intermediates define subtraction and
shift overflow while preserving the original signed division.

The sole aligned retail pointer is ROM `0x23013C`, VA `0x8008B67C`, the
callback in **D_8008B4A8[9].unk0**, descriptor stride `0x34`. There are no
direct JAL references. `func_1517A644` submits category 9 and allocation size
`0xB8` to `func_15167A68`. The original `func_151670C0` dispatcher passes the
record in A0 at JALR `0x15167170` and ignores the callback's return.

## Direct compilation and focused checks

The complete semantic C body emits **all 67 retail words directly**, with
the original **24-byte frame** and **zero guards**. The existing `-O2 -g3`
profile remains unchanged. One scalar carries both the initial timer and the
subsequent floor difference, recovering the original temporary lifetimes.
All three bindings emit naturally: `D_800BE9E4` HI16 at `+0x0C`, LO16 at
`+0xCC`, and the retirement call at `+0xF4`.

The focused suite passes before installation and after the actual build:

- **2,640 guest cases per body** check signed coordinate wrapping, all spin
  signs, zero/one/two/negative Y speeds, floor equality and wrapping, unsigned
  timer boundaries, signed tick extremes, and both stack phases. **480 cases
  per body** produce a negative shifted fade numerator before signed division.
- These routes reach **66/67 words**. The duplicate angle load at `+0x98`
  is structurally unreachable; it remains statically exact and is not counted
  as executed coverage.
- **128 alias cases per body** check four layouts including tick overlap with
  position, speed, and timer fields, comparing every byte of the full backing.
- Native32 O0/O2/O3 pass **12,288 executions** with undefined-behavior traps;
  **23 compiled semantic controls** are rejected, including unsigned timer,
  signed spin, landing gates and constants, wrong fields, missing retirement,
  wrong fade arithmetic, and unsigned division of the wrapped numerator.
- **150 fault observations / 42 unique active boundaries** check emitted
  accesses. **128 connected cases** execute the actual four-word dispatcher
  window, including its next-record store in the call delay slot, callback,
  call trace, return, and saved registers.

The original oracle lacked signed-byte load opcode `0x20`; the target-local
extension now implements its signed eight-bit load through the existing
tracked access helper. The selected C was unchanged. The extended installed
suite passes all **five tests in 31.573 seconds**. Shared matcher, PC16,
word-guard, and protected-data regressions pass **19 tests in 5.286 seconds**;
`make tools-check` passes. Routine work uses zero Claude calls.

The retirement helper remains a bounded clobbering provider. These checks do
not qualify its complete implementation, the complete dispatcher/factory,
hardware execution, or gameplay. Guest fault prefixes qualify instruction
access order, not portable C fault semantics. The standalone tools checkout's
pre-existing dirty work is preserved; fresh target receipts use mounted tools.

## Linked-image and production audit

Independent compilation, padding, and linking preserve **ten neighboring
functions** and normalized pools. Across **6,052 linked functions**, only the
target body changes, with all addresses fixed. The entire ELF is predicted by
replacing the 268-byte target instruction span and changing only its named
symbol extent from 12 to 268 bytes: **201 changed bytes**, **zero exclusions**.
Corruption inside or outside that span is rejected.

All **189,088 protected Game-data bytes / 720 owners** remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Natural target before relocation | `793790020a1a6eb1b48ee52a0d41593bc6d8d8996c9f751551e17c1a95f12420` |
| Linked target / retail | `de50604b8c75524b590f3806b3fa78c1889db3f1173778aa8171ff108524e722` |
| Qualified / production owner | `cd2f56e667ddafeef97c15fbf3b746c4d06124706fe395d299a909308cf969dd` |
| Frozen predecessor ELF | `b775949211d110993c2e819b0c15135c0e21f92b74bd8dac61f5996a4ff3fdbb` |
| Qualified / production ELF | `b3eecf1336289ea865dfd089d311aa3730cecb90a44e50721ac74a4a3d28cfc4` |
| Production code image | `4194d2cfa71a920cb0055de6863637912a249c1c3b1a192ab5b9e33cde1f84ad` |
| Production map, unchanged | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |

Actual Make recompiles only this owner and links successfully. `make all`
generates the binary and stops only at the expected retail SHA-1 mismatch.
The inherited duplicate `generated_12D630` recipe warning remains; no new
target diagnostics occur. Guards, conversion CSV, and Makefile remain
byte-identical to their frozen predecessors.

## Authoritative recount and continuation

| Section | Exact C functions | Address drift | Different |
| --- | ---: | ---: | ---: |
| Total | **4,156 / 5,512 (75.40%)** | 0 | 1,356 |
| Init | **492 / 492 (100.00%)** | 0 | 0 |
| Game | **3,483 / 4,839 (71.98%)** | 0 | 1,356 |
| Debugger | **181 / 181 (100.00%)** | 0 | 0 |

Converted inventory remains 5,512 / 6,046. The active 80% target requires
4,410 exact functions, **254 more**. Continue at ordinary candidate
`func_1518C900`; preserve the seven previously documented compiler/custom-ABI
boundaries. This is another checkpoint toward the goal, not its completion.

Reproduce under prepared WSL from the consumer root:

```sh
python3 -m tools.experiments.game_settle_fade_match
python3 -m unittest tools.tests.test_game_settle_fade_match -v
make -C conker -j4 build/conker.us.elf
make -C conker all
```

## Graph retention

The frozen graph has **58,597 nodes / 112,369 links / 5,137 communities**,
SHA-256 `5af8548a03f68d8c1dfadd75deea6324b067150244cd439c528568a940c5dacf`.
The standard reduced update extracts eight uncached paths but proposes only
24,803 nodes and correctly refuses to overwrite the retained graph. Its
corpus warning retains 31,816 nodes from 3,754 still-present files outside
the reduced scan. An explicit seven-path refresh with `force=False` produces
**58,605 nodes / 112,373 links / 5,082 communities** and retains **58,594 /
58,597** prior IDs, with **zero removals outside changed paths**. Three
line-derived Update Log IDs relocate; eleven IDs are added, including seven
Note 2085 nodes and an additional reference node.

Qualified graph SHA-256:
`d2350bca8ecd995abb39fdba03735d371eacae2e188dacda900fa8137859b47b`.
This is a scoped AST refresh with zero semantic LLM calls, not a fresh
full-corpus extraction. A final one-path note refresh checks stabilization.
