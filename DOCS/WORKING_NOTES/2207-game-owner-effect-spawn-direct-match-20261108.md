# Owner Effect Spawner Direct C Match - 2026-11-08

**Follow-up:** [Note 2373](2373-game-two-vector-effect-provider-direct-match-20261113.md) restores the provider; references to its placeholder below describe this earlier checkpoint.

`func_1514DE94` replaces a false zero-return placeholder with the complete
owner effect-spawn sequence. All **79 words / 316 bytes** and the original
**0x48-byte frame** emit directly from semantic C under the existing O2/g3
profile. There are **no guards, profile changes or assembly insertions**.

Production: Total **4,276 / 5,513 (77.56%)**, Game **3,603 / 4,840 (74.44%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift. There are
**1,237** converted functions still different and **135** more exact functions
needed for 4,411 / 5,513 and the active 80% goal. Conversion rows are unchanged.

## Recovered behavior and interface

Owner `conker/src/game/generated_179F30.c`, original `conker/asm/179F30.s`.
VA **1514DE94..1514DFD0**, ROM **17B344..17B480**. Public interface:

```c
void func_1514DE94(u8 *owner);
```

The owner argument is homed at incoming SP+0 and reloaded after helper calls.
The function submits an effect through `func_15160CDC` using type 12, vector
presets `D_800A58AC` and `D_800A58B8`, the exact `D_800A5E04` float word
`0x3C088723`, and the recovered twelve stack arguments. It next calls
`func_15083568(owner, 60, 1.0f, 0)`. That function returns an object pointer;
the owner-local declaration is corrected from void to `u8 *`, matching its
existing implementation and other typed declarations. The float is passed
as `0x3F800000` in A2 under O32, not in F12.

Only after the second call does the function read live byte `D_800BE9B4`.
When zero it stores **2400** at returned object+0x38. Retail has no null check;
a null returned object with a zero mode reaches that invalid store. A null
result with nonzero mode is ignored. The recovered C preserves that boundary.

The third call is `func_15160A58`, with the live owner, vector `D_800A58C4`,
kind 2, duration 300, subtype 11, full recovered color/flag/priority/context
packet, including signed byte -1. Its return, including NULL, is passed with
the reloaded owner and key **0x19** to `func_1514EC1C`. This function's result
is incidental: the real original caller ignores it and forces continuation 1.

The existing `GameEffectVector` and typed `func_15160CDC` interface used by
`func_1514F308` are moved before both users and reused. No duplicate vector
layout or conflicting factory prototype is introduced. Canonical declarations
for `func_15160A58` and `func_1514EC1C` are preserved. All 77 other owner
functions, their bindings, pools and padding remain unchanged.

## Qualification

- **111 frozen inputs** pin source, headers, compiler, ROM, guards, layout,
  link definitions, caller, effect presets and helper implementations.
- Both whole-owner padders agree across **78 functions**, with **74 original
  case labels** retained. The actual three-command Make recipe reproduces
  the qualified compact and padded owner. Four inherited pointer/integer
  warnings are unchanged; the new function and isolated compile are clean.
- The independent complete ELF prediction permits only the target body,
  size 12 to 316, and one closed two-entry/name exchange:
  `func_15150F90` / `D_8009D7A0`. The unequal names have reconstructed string
  offsets; values, types, extents and section indices are preserved by name.
  **290 changed bytes, zero exclusions**. All **6,052** function addresses,
  every other body and all **720 protected owners / 189,088 data bytes** are
  unchanged. Guard CSV, Makefile, progress CSV and retail data remain unchanged.
- The actual original four-word call window at **15099734..15099744** passes
  S1 in A0, calls the target, branches to 15099C00 and sets V0=1 in its delay.
  The complete large parent `func_15097A8C` remains unqualified. Whole-ROM
  aligned census finds one direct call and no entry/interior data pointers.
- Three baseline helpers are already byte-exact: `func_15083568` (89 words),
  `func_15160A58` (71) and `func_1514EC1C` (49). They are bounded providers in
  the target suite. `func_15160CDC` is still an unmatched C placeholder; its
  original 85-word body is independently executed against the existing
  typed payload reference with bounded `func_151602C0` and memcpy. That is
  original ABI evidence, with no production-integration or matching credit
  claimed for the factory.

Fresh checks in each tools environment, before and after adoption:

- **2,560 guest cases per body** visit all 79 words: every mode byte, complete factory packets, mutated globals, returned pointers, owner/effect/record aliases and guest-only incoming-home mutations. Raw C, padded C and retail agree in complete private state; saved GPR/FPR and frame lifetimes are checked.
- **800 fired fault-prefix triples**, including 48 delay-slot cuts, preserve exact private state and call order. The null effect/zero-mode path reaches its original invalid store after two calls; nonzero mode skips that access.
- **64 actual caller-window cases per body** preserve S1-to-A0, the ignored return and forced continuation 1. **64 independent original factory cases** visit all 85 words, including null owner and allocation outcomes.
- **Six independent GNU links**, with 72 cases per body, rebase code, four callees and all data references across adjusted HI/LO boundaries. Stale raw bytes/bindings and whole-image corruptions are rejected.

All 26 incorrect implementations are actually compiled and rejected by public counterexamples in the guest model and by native32 O2 execution. Native O0/O2/O3 each pass 14784 aligned-storage cases with SDK types and trap UBSan. Native fixtures copy float bits without a float-return initializer; such an initializer can quiet a signaling NaN under the x86 ABI. Guest home mutations remain outside portable C claims. These are bounded models and native ABI checks, not N64 FCSR or gameplay acceptance.

The existing whole-ROM checksum mismatch still makes `make all` exit 2. Target compile/link/progress and linked recount pass. Shared smoke checks are fresh in both tools copies; three unchanged regressions per copy are reused only by exact helper/test fingerprints.

Receipts: `conker/build/game-owner-effect-spawn-1514DE94-match/`. Sibling tools retain all 2,434 inherited dirty paths; host Release stays frozen. Tools are committed before the consumer pin. Scoped Graphify refresh retains existing unscanned nodes with evidence and makes no full-corpus extraction claim.

Next: `func_15188810`, owner `generated_1B5CC0`, a measured 79-word unmatched list registration/allocation routine. Audit its real caller ABI, signed timer comparison, allocation failures and typed list helpers before adoption or credit. The 80% goal remains active.

Production ELF SHA-256: `a6511cc41325dc75a85ed2ffdf213eb3e40f8ae86e864819a6bd2603a5d49dab`.

Guard SHA-256 (unchanged): `b6321a2e129ea7f0550984349d4cdab102ff203b44de7fb0ee9bea04ddd89be0`.
