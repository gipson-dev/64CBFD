# Attached random emitter guarded match - 2026-11-26

`func_150E06D8` replaces its zero-return placeholder in
`conker/src/game/generated_10CD70.c`. The semantic C emits **100 raw words**;
**24 expected-word guards**, including one insertion, recover the original
**101 body words**, original **112-byte frame** and **17 bindings**. One
literal zero alignment word completes the 102-word slot. This is guarded C,
not a raw compiler byte match. Of the raw words, 77 need no word replacement.
VA `0x150E06D8..0x150E086C`, alignment through `0x150E0870`; ROM
`0x10DB88..0x10DD1C`, alignment through `0x10DD20`. No omission or new profile.

Production: **4,705 / 5,528 (85.11%) total**, **4,032 / 4,855 (83.05%) Game**,
Init 492/492, Debugger 181/181, zero drift, 823 still different. One matching
credit; no conversion-row, denominator, caller or helper credit. The active
**90% goal requires 4,976 matches: 271 more**.

The entry is `void func_150E06D8(struct127 *owner, u8 variant, u8 selector,
s32 context)`. It uses the canonical actor attachment field `struct255
*unk1D4` at offset 0x1D4, with no volatile qualifiers or dummy accesses.
Names describe inferred roles; original effect names remain unknown. If an
attachment exists, a selected preset is transformed through the current
player's matrix, then a 14-argument factory receives the transformed point,
two preset pointers, a two-float pair and randomized scalar parameters.

The float/int callback order is float, float, int, int, float. The pair is
`[28 + draw*14, 2 + draw*1]`; integer draws are captured as u32 before
remainders, yielding 4..6 and 100..255. The final float is `400 + draw*300`.
The range macro preserves the unit multiply and complete ordered COP1
sequence. A local variant capture retains the compiler's final live reload.
The factory's narrow formal types are inferred from observed loads and ABI;
they are not a claim to have recovered its original source prototype.

Normalization is mechanically derived from the raw object:

- The eight private words map raw to retail (hex offsets): 44->60, 48->4C,
  4C->48, 50->44, 54->50, 58->54, 5C->58, 60->5C. The outgoing pointer-valued
  SP+10 cell also has an explicit value relation after its defining store.
  RA at3C, point64..6C and incoming homes70..7C remain fixed.
- One closed GPR cycle 11->12->13->14->11 applies in normalized intervals
  40..70 and D4..168. All consumed instruction inputs are compared under
  the PC/frame relation. All COP1 register/arithmetic words and their order
  remain literal. Two SWC1 private-home addresses move with the bijection.
- An unchanged expected anchor at raw34 inserts `lw t3,0x70(sp)` at
  normalized38. It repeats the owner home saved by the prologue and read
  earlier, with no intervening store/call. The forward branch and all later
  PCs/bindings shift by four. There are no arbitrary arithmetic replacements.

The added read is qualified as an explicit stutter under an ordinary mapped
O32 stack-home assumption. **Full raw private-register/fault identity is
not claimed**. Every memory-access fault cut remains present in all four
literal streams; three extra-read cuts have separate raw stutter witnesses,
and 111 common cuts have frame/access/consumed-operand relations. No hardware
fault, timing, gameplay or portable-C incoming-home-alias guarantee is made.

Validation:

- Both full raw owner profiles (normal and RETAIL_FUNC_150DFCA8) preserve all
  12 neighbors and literal pools. Both complete padders reconstruct the
  frozen BEFORE object and emit identical AFTER objects. The unchanged
  mixed Make recipe retains the existing motion-clamp function object and
  D_800A0FD0 rodata anchor: four compile/pad/assemble commands plus one
  deliberately deferred transient cleanup. No compiler diagnostics were
  added. Existing unrelated duplicate-recipe warnings remain visible.
- Guest: 256 cases per five streams, all 101 retail words reached. Four
  literal streams have complete private-state identity and 114 fault-prefix
  quadruples. The fifth raw stream passes the explicit frame/PC/operand
  relation, including all four rounding modes, unsigned remainder edges,
  live globals, provider clobbers, pointed slot mutations and guest-only
  incoming-home experiments. An independent public-memory/call/packet/FP/
  FCSR reference agrees. Five changed instruction controls cause comparison
  mismatches. A fixture constructor originally reset the RNG cursor Counter;
  initializing the two cursors after its base constructor fixed that fixture.
- Tables A800A0F70 and B800A0F88 occupy 48 pinned contiguous bytes, stride12:
  A(+/-17,0,90), B(+/-17,0,150). SHA256
  `25684396db9786f0c69c58a9897401cc4e48a3d6777283f82f9cd3562745671a`.
  Matrix/RNG/factory original slots are pinned; these providers remain
  opaque in this target's dynamic checks.
- The original parent func_150265CC has 3,451 words/frame1,872. Its bounded
  dispatch window at15028810 through the complete return epilogue executes
  24 original parent words, with 96 cases and32 connected children per
  stream. It loads owner fromSP764, selector fromSP773 and variant from
  scriptS0+5, gates on owner type4A, and overwrites the child result with1.
  Null-owner likely-branch, rejected-type continuation, and three child-result
  poison controls pass. Original caller bytes are ROM-pinned; this does not
  credit or claim a full current-production match for that parent.
  **Variant is an unchecked script u8. Only indices0/1 have qualified table
  domains here; all script values and other parent paths remain unproved.**
- Native32 actual C runs4,096 cases at each O0/O2/O3, three translation units,
  canonical actor prefix copied from the frozen header with asserted offsets,
  strict aliasing, trapping UBSan and LTO type checks. It compares all
  initialized actors/banks/tables, all14 factory arguments and defined packet
  bytes, callback sequence and MXCSR. Eleven source negatives exit42 through
  comparison; no compile failure, signal or trap counts. Providers are typed
  noipa counterparts; only valid two-entry table inputs are used.
- Both padders reject48 guarded-word and4 guarded-binding corruptions;
  expose152 unguarded-word and30 unguarded-binding changes. Both reject
  oversized input. Twenty independent GNU links plus100 guest rebase runs
  cover four jump regions and signed HI16/LO16 carry seams.
- Independent prediction from frozen old C and original target assembly
  equals the complete private and production ELF: **390 changed bytes,
  zero exclusions**. All189,088 protected data bytes across720 owners remain
  fixed. ELF SHA256: `7ca6dee9d27cf3c72e85bba6721f7123051a92e3eae081694304d474a286542e`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 131.929 s | 5 fresh / 0 reused |
| preinstall-sibling | 104.152 s | 5 fresh / 0 reused |
| installed-primary | 121.159 s | 5 fresh / 0 reused |
| installed-sibling | 117.03 s | 5 fresh / 0 reused |

The pre-install source had one extra newline at EOF. Final diff checking
removed that newline only; C tokens and all preceding line numbers are
unchanged. `EOF-trivia-reconciliation.json` retains the original source/task
fingerprints and receipts. Production was rebuilt and both installed suites
rerun against the final source/manifest, followed by shared tools-check.
The complete padded object and predicted ELF remain identical. The original
pre-install receipts qualify the same tokens before this EOF-only correction.

All20 tabulated stage tests are fresh, with equal primary/isolated-sibling task,
import, data and artifact fingerprints. Shared tools-check passes. Unchanged
broad suites are not reported fresh. Frozen inputs:4090;
copies:3032. The separately dirty real tools sibling is
preserved. Tools commit:`f6c8cc6fce51fa7a96289153cc163967bfdba5bc`.
Baseline consumer:`ac9acee275af162c5d06af0dd1caa9242c32e376`. Receipts:
`conker/build/game-attached-random-emitter-150e06d8-private`.

One completed packet-only Claude advisory, no subagents. Host applicability
is recorded separately; no transfer/build/launch, Release change or push.
Scoped Graphify refresh retains all old IDs and qualification tags, audits
current owner definitions and observes actual hook termination. No full-corpus
extraction claim. README changes are aggregate rows/date only. Continue from
sealed N71 toward90%; choose another unmatched Game routine before new credit.
