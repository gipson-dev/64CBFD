# 1813 - Queued-entry retirement callback - 2026-10-29

`func_1518AA10` now emits its complete 51-word / 204-byte retail slot directly
from semantic C, with a 32-byte frame, five external bindings and no guards.
The zero-return placeholder becomes `void func_1518AA10(u8 *queue)` in
`conker/src/game/generated_1B7EC0.c`. Original symbols are retained; comments
explain the alias-sensitive link reload and the count reload after release.
The release declaration and cast use the existing `struct102 *` interface.

## Recovered behavior and ABI

- A zero count at queue+0x1C exits without reading the timer, entry or clock.
- A negative signed timer at queue+0x22 retires the entry at queue+0x14.
  A null next link clears both queue ends. Otherwise it clears next+0x14
  and then reloads entry+0x18 into the queue head. Those two fields may alias.
- A nonzero unsigned entry+0x1C indexes `D_8008D5C0` and passes entry+0x10
  to the selected callback. The entry survives at SP+0x18; the queue pointer
  survives in the incoming home at SP+0x20 across both helper calls.
- `func_1516972C` releases the entry, then the current queue count is reloaded
  and decremented. Unsigned arithmetic retains the original wrapping behavior.
- A nonnegative timer decreases by `D_800BE9E4` only when queue+0x24 bit 0 is
  enabled. The result is stored as a halfword, retaining the original truncation.

The only aligned original pointer is at ROM 0x23054C / VA 0x8008BA8C:
`D_8008B4A8 + 0x1D * 0x34`, descriptor offset zero. There are no aligned direct
JAL callers. The 12-word original `func_151670C0` window at 0x15167158 forwards
S0 in A0, saves the next owner before JALR, ignores the callback result and
reloads the next owner. Its current C parent remains an unchanged stub.
The separate descriptor fields at offsets 4, 8 and 0xC are not this route.

The optional table's only non-null retail entries are 1=`func_150BB408` and
2=`func_150CBF5C`; both take one owner pointer and return void. Their 18- and
7-word bodies, the 28-word release dispatcher, 20-word active-slot scan and
8-word unlink adapter are already byte-exact in the current ELF.

## Qualification

Eight target checks and shared project-tool checks passed independently in
both local tools copies. After adoption, two image/owner checks ran fresh in
each copy; six unchanged semantic checks were reused only after matching the
complete input, module, compiler-adapter and artifact fingerprints.

| Evidence | Result |
| --- | --- |
| Retail/compiled guest comparison | 1,424 cases, all 49 reachable instructions, complete state and access traces |
| Unreachable original instructions | Both duplicate instructions at offsets 0x44 and 0x9C retained in the exact 51-word slot |
| Original helper execution | 108 connected cases, all 81 helper words exercised |
| Original dispatcher window | 72 cases, 12 original words, owner forwarding and ignored result checked |
| Native SDK / 32-bit execution | 12,288 cases each at O0/O2/O3 with trapping UBSan and valid aligned storage |
| Effective bad-body controls | Nine independently compiled variants rejected by observable values or calls, in native and guest execution |
| Fault prefixes | 173 complete state/access prefixes, including 29 branch-delay cuts |
| GNU relocation layouts | Three layouts, 48 cases, original/Make/padded/raw objects equal |
| Raw body/binding corruption | 56 rejected mutations |
| Complete image corruption | 234 rejected mutations; no excluded bytes |
| Full owner / actual Make | Four compact functions, three unchanged neighbors, three actual Make commands, no new owner diagnostics |

Guest probes include all 256 unsigned selectors, six overlapping layouts,
helper effects and deliberate incoming-home changes. High selector probes use
synthetic mapped callbacks; they do not claim that arbitrary indices are valid
in the four-entry retail table. Native checks use a separate valid 512-cell
backing table and disable strict aliasing for the byte-based owner accesses.
They do not claim portable C semantics for guest faults or home overwrites.

The helper chain bounds `func_15168B10`, `func_1513F6C0`, and synthetic cleanup
providers. It does not establish complete list-service, parent-dispatcher,
hardware or live gameplay behavior. Routine work used zero Claude calls.

## Production audit and progress

The actual production Make build reproduces the independently predicted ELF.
All 6,056 function addresses and the other 6,055 bodies remain fixed, as do
189,088 protected Game bytes across 720 owners. The guard CSV, conversion
inventory and linker map are unchanged. The complete ELF changes by 182 bytes:
157 code bytes, one extent byte and 24 explicitly reconstructed symbol/string
metadata bytes. The two closed swaps are `D_80099804` / `D_8009EE54` and
`D_8008D5C0` / `D_80088820`; all named definitions are preserved.

- Before: total 3,890/5,506 (70.65%); Game 3,217/4,833 (66.56%).
- After: total **3,891/5,506 (70.67%)**; Game **3,218/4,833 (66.58%)**.
- Init 492/492 and Debugger 181/181 remain exact; address drift is zero.
- The 75% threshold is 4,130 exact C functions: **239 more** are needed.

Tools were committed first as `3eda82b3bf47908816e929287267d1b4af589b19`.
The consumer commit carries this note, its source, the tools pin and aggregate
README rows. Prior consumer/tools were `8930c62a` / `289df16`. The older tools
mirror retains its 1,880 inherited dirty paths plus the three new qualification
modules. No push or host-port/Release change is part of this recovery.

Evidence is retained in `conker/build/game-queued-entry-retire-match/`, including
immutable input snapshots, prior private evidence, canonical receipts, complete
ELF prediction, production proof, recount and scoped Graphify retention audit.
No full-corpus graph extraction or recomputed global analytics is claimed.

Next inspect `func_151A1EE8` in `generated_1CC440.c`, the next 51-word placeholder
in the refreshed queue. It has no matching credit yet. `func_1514E920` and
`func_151D7000` remain parked and uncredited.
