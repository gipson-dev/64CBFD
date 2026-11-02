# 2011 - Motion-target clamp matched as guarded C

Verified 2026-11-02. Production **4,078/5,511 (74.00%)**; Game
**3,405/4,838 (70.38%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,433 different; one zero-return placeholder is replaced by qualified
semantic C and is newly byte-exact. The active 80% target is **4,409/5,511**,
requiring **331 more**. This is progress toward that goal, not completion.

## Recovery and callback contract

`func_150DFCA8` is the 63-word, frame-zero motion integrator and target-velocity
clamp at VA `0x150DFCA8` and ROM `0x10D158` in
`conker/src/game/generated_10CD70.c`. Its recovered interface is:

```c
void func_150DFCA8(MotionTargetState150DFCA8 *state);
```

The routine converts signed global tick count `D_800BE9E4` to float and
integrates `position += velocity * ticks`. Positions below `11.0f` select
`D_800A0FA0`; positions above `55.0f` select `-D_800A0FA4`; the middle region
retains the record's current target. Velocity approaches that target using the
upward step `D_800A0FA8` or downward step `D_800A0FAC` and clamps after any
overshoot. The recovered local type documents the observed fields at offsets
`0x04`, `0x64`, and `0x7C`; reserved spans remain opaque rather than receiving
speculative names.

Retail installs this routine as an object-update callback through the table at
`D_80088C90 + 0x21C` (ROM `0x22D96C`). The complete parent window at
`0x15113E54` calls the object callback stored at `+0x38` with the state pointer
in `a0` and ignores its return value. Three permanent callback-window cases
verify that ABI. No direct JAL, jump, or function-pointer literal targets this
routine elsewhere.

## Guarded compiler closure

The recovered C naturally emits the complete 63-word control flow, all branch
and delay-slot positions, every memory access, and all ten relocations. Fresh
IDO differs only in 24 floating-register allocation and independent scheduling
words at offsets `0x00C`, `0x010`, `0x018`, `0x01C`, `0x024`, `0x028`,
`0x02C`, `0x030`, `0x034`, `0x040`, `0x058`, `0x060`, `0x070`, `0x078`,
`0x098`, `0x09C`, `0x0A0`, `0x0A4`, `0x0A8`, `0x0D0`, `0x0D4`, `0x0D8`,
`0x0DC`, and `0x0E0`.

Exactly 24 checked expected-word replacements close that allocation cycle.
Three rows retain their unchanged `R_MIPS_LO16` bindings for `D_800A0FA4`,
`D_800A0FA8`, and `D_800A0FAC`. The original link and three independent
layouts reproduce their expected linked words. Independent mutation of every
expected word and every row's expected relocation field produces 48
fail-closed cases. There are no insertions, omissions, or semantic instruction
substitutions.

The source remains behind `RETAIL_FUNC_150DFCA8`. The owner recipe compiles a
base object and a macro-enabled object, selects only `func_150DFCA8` from the
latter, and preserves the already-matched neighbors from the base compile.
This prevents IDO's changed floating-register state from perturbing the later
matched `func_150E05F8`.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor linked ELF | `e27a83e2af6dd164bcf80349f04257422c2fca30e10454f317937aae92b08870` |
| Raw candidate owner | `427f3c8064349712283bbf7404c5eef0dec59bad8c08e4df4e51d14f42fc173b` |
| Retail/guarded 63-word slot | `212e88c887ae947c0eece5a0938e64908781393b8b7dcb778625302fe0a9d343` |
| Guard manifest | `84bf2328b52e7467008dabef11a32529aeb25c2fe8cdd5e9a1af26ccff888377` |
| Qualified/production owner | `900d01d8ae2028c82395d2da314aabdf1382431207f0095e91ce79e2dbbd5866` |
| Qualified/production linked ELF | `313b438cbb051b6f8b22f4fbb9b6b4e218248585b831594f77786a24dfb71d06` |
| Production map | `0f9af6c3578cff80ed406b8510f09e8dd211b6d07abb0e1c6614b4640522165d` |

## Semantic, owner and image qualification

Six permanent tests pass (latest run: 16.639 seconds). The guest corpus covers **1,167
cases / 3,501 executions**, all 60 reachable words, every low/middle/high
region and both approach directions. Its path counts are 400 low, 434 middle,
and 333 high. Fifteen alias layouts preserve retail's read/write ordering.
Native O0/O2/O3 each pass **1,152 cases / 11,520 executions**, for 34,560
executions total, with nine effective controls rejecting plausible wrong
implementations.

Every non-target function and relocation in `generated_10CD70` remains
byte-for-byte unchanged. Strict whole-image prediction changes only the
252-byte target slot and its symbol extent, keeps every address fixed, and uses
zero exclusions. Actual Make reproduces the qualified owner and predicted
linked ELF byte-for-byte. The dependency corpus rebuild compiles and links the
complete Game, Init, Debugger, generated, converted, and libultra inputs; the
full `make -C conker all -j2` pipeline stops only at the expected final retail
SHA-1 mismatch because the wider decomp image is not yet byte-identical.

Protected Game data remains exactly 189,088 bytes across 720 owners with zero
different bytes, SHA256
`0bbc00e1adfac5ffe611f5be9c941575f87b341a77d808004603ac1cb87c670`.
The permanent experiment and qualification suites were committed first in the
tools submodule as `c6166e9`. The retained qualification stage is
`conker/build/game-motion-target-clamp-150DFCA8-guard-match/`. This is
instruction-level and bounded semantic proof, not natural whole-game motion or
visual gameplay acceptance. The root README changes only its aggregate
byte-exact rows. No Claude call was needed.

## Graph retention and next step

The required Graphify update extracted 24,128 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep
handwritten/custom-ABI work on its separate track, and keep every new candidate
private until source, ABI/callers, owner, guest/native, actual Make, complete
image, protected-data, production recount and documentation gates pass.
