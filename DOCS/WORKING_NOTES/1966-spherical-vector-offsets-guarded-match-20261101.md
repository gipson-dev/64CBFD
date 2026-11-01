# Spherical-vector X/Z/Y offsets recovered as byte-exact guarded C

Verified 2026-11-01. `func_1505A184` in `game_83300` now matches all **51 words**
with its natural **48-byte frame** and two derived guards. Production total is
**4,035/5,507 (73.27%)**, Game **3,362/4,834 (69.55%)**, zero canonical drift
and 1,472 different. The 75% threshold is 4,131: **96 matches remain**. This
adds one exact C function; the C inventory and converted-byte totals are unchanged.
The wider Game goal remains active. No push was requested or performed.

## Recovered behavior and existing interface

The original span is VA `0x1505A184..0x1505A250`, ROM `0x87634..0x87700`.
The existing public six-argument interface was already correct:
`void(u16 yaw, f32 distance, f32 pitch, f32 *x, f32 *z, f32 *y)`.

The previous C body reversed its final X/Z stores and performed one horizontal
store before the last trig call. Retail halves distance, scales pitch through
`D_800994B8`, stores the vertical sine result, captures the pitch cosine scale,
then scales unsigned yaw through `D_800994BC`. It captures both yaw trig results
before storing X and then Z. The new body uses descriptive parameter/local
names and a short behavior comment, preserving the original `func_` symbol.
No caller declarations or shared headers changed. Original assembly is retained.

The pitch and yaw lifetimes remain separate. In-place distance/pitch updates
and declaration order recover the natural 51-word/frame48 shape. Both final
trig values survive helper calls; coefficient/output aliases and signed zero
are handled in the original order.

## Two closed private-spill guards

Raw semantic C differs only at offsets `0x8C/0x90`: its yaw-angle SWC1/LWC1
pair uses private SP+0x24, while retail uses SP+0x20. Expected-word guards move
both ends of the pair:

| Offset | Expected compiler word | Retail word |
| --- | --- | --- |
| `0x8C` | `0xE7AC0024` | `0xE7AC0020` |
| `0x90` | `0xC7AC0024` | `0xC7AC0020` |

Opcode, FP register, relocation bindings, body length and frame stay fixed.
The destination is disjoint from saved F20, RA and captured cosine. Nothing
is inserted or omitted. Two runtime negative controls move only the store
or only the load; both are detected. The normalized payload and all eight
bindings equal the complete original assembled routine.

Raw-C public equivalence is qualified for outputs outside the callee private
frame. Deliberately pointing outputs into that private spill storage is outside
this contract. Incoming formal-home mutation cases below qualify emitted guest
behavior and are not portable-C alias claims.

## Fresh runtime and caller evidence

- **3,456 guest cases / 13,824 executions**, three independent address layouts
  and nine output/alias layouts. Original ASM, padded owner and actual-Make
  programs agree in complete machine state and trace. Raw C agrees in public
  state and calls; final memory differs only in the two private spill slots.
  Saved GPRs/FPRs and SP are preserved. All 48 reachable root words execute;
  three unsigned-correction words are unreachable because LHU is nonnegative.
- **84 access-prefix cuts / 252 executions** compare the three normalized
  programs' complete states and traces. These are guest access-order tests,
  not hardware exception/EPC or portable-C fault equivalence claims.
- **2,304 connected-trig cases / 9,216 executions** use the original contiguous
  76-word cosine/sine span and all 12 coefficient words, pinned to retail.
  Cosine falls through to sine; it is not a wrapper provider. The corpus
  executes 73 of those words and includes tiny/huge finite pitch inputs.
  The independent float32 polynomial/reduction reference agrees. Full FCSR,
  NaN payload propagation and physical hardware execution are not modeled.
- Native32 **O0/O2/O3**, UBSan and canaries each pass **1,280 valid cases**
  across five portable alias layouts. Nine incorrect variants are all detected:
  distance scale, vertical sign, signed yaw, yaw coefficient, swapped X/Z,
  Z sign, early X store, reloaded yaw coefficient and rescaled pitch.
  Guest-only formal-home aliases are excluded through an explicit pointer map.
- The complete ROM scan finds **29 direct JAL sites**, no aligned direct jumps
  and no aligned literal pointers. **3,712 cases / 14,848 executions** cover
  every original JAL/delay pair, its six-argument boundary, real delay word,
  bounded output-pointer provenance, saved registers and return PC. All output
  pointers are outside the callee private frame. These windows do not emulate
  all paths through their large parent functions.
- The complete original **32-word `func_150593C4` wrapper** separately passes
  **512 cases / 2,048 executions**. All wrapper words execute. Its local X/Z/Y
  argument order, actor smoothing, float32 order and saved state are checked.

The initial native fixture accidentally mapped a guest stack-home alias to a
coefficient. The separate diagnostic identified row8; an explicit address map
now rejects such cases, and a genuinely portable fifth layout replaces it.
The corrected positive corpus passes all three profiles and all nine controls.

## Owner, Make, literal ELF/map and overflow closure

All **88 raw/padded owner neighbors** and normalized pools remain unchanged.
Diagnostics stay **8 -> 8**. The actual five-command Make object equals the
independently qualified padded object. Six focused tests and the shared tools
check pass in both tools checkouts before and after installation. Reused runtime
receipts are bound to the complete oracle bytes, selected C, source input index,
raw hash, qualified/raw objects and first linked ELF. A 36-artifact canonical
preparation manifest covers the retained qualification and prediction evidence.

Removing the obsolete 220-byte private implementation moves five later private
bodies down220 bytes. Their instruction bytes and local relative targets remain
unchanged. Only `func_150768DC` and `func_150A7D00` trampolines retarget; dynamic
checks preserve all registers/memory across both destinations and return poisons.
All **6,045 canonical addresses** and **6,050 other bodies** remain fixed.
The executable inventory is 6,054 -> 6,053, solely from obsolete-body removal.

The independent prediction also removes the unused `game_83300.c.o` FILE symbol,
reconstructs symbol/string tables and headers, and accounts for the224-byte ROM
cursor alignment delta. The complete ELF shrinks284 bytes to3,256,332. Its SHA-256:

`cded33da308db122019a82f17a72c6f77a3cda2274826ce9b593850acf7315d6`.

The complete production linker map also matches its independent prediction:
28 changed/deleted lines, with no path remapping or exclusions at the production
comparison. Protected Game data remains **189,088 bytes / 720 owners**, exact.
Only the source, its object, appended two-row guard CSV, ELF and map change in
the pre-documentation sealed-input review. No unrelated dependent object changes.
An independent recount reads the adopted Windows-checkout ELF and confirms the
new totals. Production source/header/compiler profiles and older guards are
preserved except for the scoped target body and appended guard pair.

Evidence lives in `conker/build/game-spherical-vector-1505A184-match/`, including
`runtime-qualification.json`, `caller-runtime.json`, `wrapper-runtime.json`,
`overflow-control-flow.json`, `retargeted-trampoline.json`, `public-preinstall.json`,
`production.json`, `installed-audit.json` and `native-install.json`.

## Next work

Continue the 75% push from the remaining Game queue. `func_1507E1D0` and
`func_150174C0` remain private at their documented compiler gaps in [Note1965](1965-private-codegen-audit-and-spherical-vector-preparation-20261101.md).
Do not credit either until its remaining compiler/ABI/runtime gates pass.
The owner-enable gate and other parked candidates are likewise uncredited.
All private work, original ASM, older tools mirror edits, prior archives and
the host-port Release checkpoint remain preserved.
