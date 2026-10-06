# Game Piecewise Envelope Investigation

Date: 2026-10-06
Banked baseline: `adbeca4e` ([Note 1054](1054-game-timed-interpolation-match-20261006.md)).

## Current Boundary

Next `func_151415D4` in [`game_16DC80.c`](../../conker/src/game_16DC80.c):
**69 words / 276 bytes**, VA **0x151415D4..0x151416E8**, ROM
**0x16EA84..0x16EB98**, no frame. Its production zero-return placeholder is
**still unchanged**. No new guard, profile, shared-header or linked-image edit.
The preceding interpolation recovery is banked, post-commit audit passes,
and exact counts remain total3332/5464, Game2659/4791,2132 different/zero drift.

Recovered envelope inputs at actor+0x170: target+0, baseline+4, amplitude+8,
elapsed+0xC, rise start+0x10, rise end+0x14, fall start+0x18, period+0x1C,
inverse duration+0x20. Output at actor+0x158. Strict comparisons choose:

1. Before rise start: baseline.
2. Before rise end: baseline + amplitude * ((elapsed-riseStart)*inverse).
3. Before fall start: target.
4. Otherwise: baseline + amplitude * (1-(elapsed-fallStart)*inverse).

Float operation order matters. After writing output, load the **live** timestep,
capture period before the elapsed store, advance elapsed, then repeatedly
subtract period while period < elapsed. Return1 only after the loop. No clamp,
positive-period guard or replacement with modulo. Output/timestep and elapsed/
timestep aliases affect the live update and are included in guest fixtures.

## Evidence And Remaining Gap

Ignored artifacts under `conker/build/game-timed-interpolation-test/`:

- `next.py`, `next.log`, `next-piecewise/measurements.json`: **16 initial
  controls**, four expression/pointer forms across four profiles.
- `next-shapes.py/log`, `next-piecewise/shape-measurements.json`: **16 further
  controls**. Volatile rise/all-output stores, explicit goto, payload pointer,
  explicit do-loop, product-first sum, separate delta and declaration ordering,
  each under O2/g3 and O2. All32 controls have empty compiler diagnostics.
- Selected `next-piecewise/selected-o2g3.c/.o/.elf`: **68 words/no frame/52
  differences**. Product-first rise gives68/no frame/49 differences, not a
  complete match. O2 gives67 words; O1 initial variants85..88 with frames.
- `next-behavior.py/log/json`: **720 finite cases / two bodies**, selected raw
  and retail. Complete external storage, ordered external accesses, V0=1,
  saved GPR/FPR/SP/RA, two SP phases, strict envelope boundaries, positive
  periods and live timestep aliases agree with an independent rounded pass.
  **65/68 raw and66/69 retail words reached**. The three unreachable duplicate
  preludes are not artificially executed: raw0x15141600/15141644/15141664;
  retail0x15141600/15141648/15141668.
- **Eight guest-only bounded nonterminating runs**: both bodies for zero,
  negative and negative-infinite periods, and positive period with infinite
  elapsed. Each reaches the50000-step budget with9995 elapsed stores and no
  callback. This is bounded loop evidence, not termination or hardware proof.

Disassembly isolates the extra retail word in the rise branch: retail stores
output at0x1514163C, branches at0x15141640, and has nop at0x15141644. The raw
68-word candidate branches at0x1514163C and stores in its delay at0x15141640.
Subsequent retail addresses are four bytes later. Earlier branch targets and
several FPR allocations/commutative operands also differ. Do not insert a nop,
rewrite those branches or copy retail words merely to satisfy the slot length.

Next recover the original69-word source/compiler shape, derive any remaining
closed allocation changes, promote the bounded driver/oracle into maintained
tools, qualify actual native C, special-FP and negative controls, bind the real
padder/full production slot, and perform a one-slot audit before installation.
Current finite guest evidence does not establish those pending gates.
Large `func_151408A4` and other owner placeholders remain unrecovered.

No sibling source/build/save/frozen Release, runtime, push or host-adoption
change. No full N64 FCSR, hardware, dispatcher or gameplay acceptance claim.
Documentation verification: **37 documents / 3408 relative links / zero
broken**; diff checks pass. This checkpoint changes documentation only.
