# Game model vertex wave guarded match

Date: 2026-11-14. `func_1517725C` is recovered in
`conker/src/game/generated_1A20A0.c`. All **106 words / 424 bytes** match
retail after **33 checked guard rows**, including **two inserted instructions**
for the original F20/F21 save and restore. Raw semantic C emits **104 words**;
this is a guarded match, not a direct C match. The **0x30-byte frame** already
matches. The three alignment NOPs through 0x15177410 remain unchanged.
Owner now **6 / 9 C-exact**.

VA **0x1517725C..0x15177404**, ROM **0x1A470C..0x1A48B4**.
Derivation: `tools/experiments/game_model_vertex_wave_1517725c_match.py`.
Raw text SHA-256:
`bba1d95ae2a05651dd5840ce6723b40eb55bf7875584b936c0d8d219c772c576`.
Baseline consumer `29b09561b8b2994b40cb5469f09b29f85ffc2eed`, mounted tools
`a69d646b556d082ef8dc307fe87d57789a92e978`.

## Contract and recovered geometry

The existing caller already declares `void func_1517725C(u8 index)` and calls
it with slot **7**. The definition now agrees. The byte transport is homed as
an O32 word before masking; packed high bits do not alter the selected slot.
The return value is unused. No neighboring body or shared header changes.

The function selects a **56-byte** state at `D_8008D0B0[slot]` and snapshots
the model pointer from the **five-word** row at `D_800DDE88[slot]`. That model
pointer stays cached across all six providers. The data owner contains eleven
state rows; native tests use only those valid indices. Sparse byte indices
and packed arguments are guest-only probes.

Two wave paths build signed vertex coordinates. The first stores a wave
computed from the live phase and amplitude, converts that wave to an angle,
and calls the two trigonometric entrypoints with the same captured angle.
The radius is read after both providers. Vertices 10/11 receive negative X,
17/18 positive X; the four Y stores retain their original order. The second
path uses phase minus **30.0f**, its own two named conversion factors and
the second radius, then updates vertices 14/19. Float products round to
single precision before signed truncation and halfword stores.

Phase and speed are reread after all vertex stores and providers. The function
adds speed, rereads the stored phase, and subtracts **360.0f once** when the
result is at least 360. It does not repeatedly reduce large angles or wrap
negative angles. Providers can mutate the live state, coefficients and model
table; the cached model and the two captured pair angles keep their lifetimes.

## Restricted normalization

The normalizer pins **104 raw words** and **18 named binding sites** and
rejects all **122 altered-word/binding controls**. It reads no retail words
to transform a candidate. Its explicit substitutions restore two identical
call-save windows:

```text
raw:    angle in F12 -> sine JAL / save angle at SP+0x24
        reload angle -> cosine JAL / save sine at SP+0x20
retail: angle in F20 -> sine JAL / move F20 to F12
        save sine at SP+0x28 -> cosine JAL / move F20 to F12
```

Both providers receive the same F12 bits. The sine save completes before
the cosine provider executes in both streams. These substitutions involve
private homes and register transport, with no intervening public memory access.
The inserted double save at SP+0x10 and restore preserve F20/F21 across the
whole function. GPR saves move to SP+0x1C/0x20/0x24, and the sine home to
SP+0x28. Those private objects are disjoint within the existing frame.
Sixteen instruction words restore the closed integer X/Y/negative-X temporary
lifetimes. Source arithmetic, vertex offsets, provider identities and constants
remain intact.

The final branch retains its displacement and enters the inserted restore at
normalized **0x194** on the unclamped path. The clamped path passes through
the same restore. Exactly **33 rows** are appended, with **two insertions**,
**no omissions**, and all previous guard bytes unchanged.

Raw C private-stack/fault-register order is not claimed. Private sine overwrites
run against retail and guarded code only; finite public semantics are checked
across all three streams. Declaration-order, register-hint and scoped-pair
screens did not recover the original floating allocation directly and remain
ignored diagnostics, without match credit.

## Completed qualification

- [x] **267 independent guest cases** compare full public memory and all six
  provider packets across retail, raw C and guarded code. They cover packed
  byte slots, phase boundaries and large/negative steps, signed fractional
  radii, provider mutation combinations, cached model-pointer replacement,
  coefficient changes, state/vertex aliases and two stack phases.
- [x] **32 private-sine cases** write the original SP+0x28 home during each
  cosine provider. Retail and guarded code observe the overwritten value.
  Providers clobber caller GPRs/FPRs, outgoing homes and HI/LO; all callee-saved
  registers and the complete F20/F21 pair are preserved.
- [x] **171 target-memory prefixes** compare complete memory, GPRs, FPRs,
  condition, HI/LO, calls, traces and delay-slot state for retail versus guarded
  code. The corpus visits **all 106 retail instructions**.
- [x] **284 native32 cases per O0/O2/O3 profile**, with undefined-behavior
  traps, compare **616 state bytes**, **1,024 vertex-buffer bytes**, six
  float-argument packets, coefficient words and the selected model pointer.
  Five effective controls reject the wrong radius, 30-degree offset, vertex
  component, wrap threshold and trigonometric provider. Native indices are
  0..10, vertices are distinct storage, and signed conversions/negation stay
  inside their defined bounded domain.
- [x] **128 executions through the authentic six-word caller window** at
  **0x15183F28..0x15183F40**, including the flag load/branch and actual JAL
  at ROM **0x1B13E8**, verify rejection or the delay-slot argument **7**.
  Return checking uses the JAL's actual return address. This is a connected
  caller window, not a complete-parent execution claim. No registry pointers
  name the target. Three effective emitted controls reject the wrong phase
  source, outer radius and sine home.
- [x] Both complete-owner padders pass **four independent GNU layouts /
  twelve links**, including code/data rebases and low-half carry boundaries.
  All nine functions and owner pools agree; the alignment tail is retained.
- [x] Actual Make's three recipe commands reproduce the independent owner.
  Strict image prediction, production installation/build/audit and fresh
  actual-ELF recount pass. Post-install mounted and isolated sibling suites
  pass; shared `make tools-check` passes.

The first caller fixture incorrectly compared RA with the pre-JAL window
state; it now records the actual callee-entry RA. A wrong-home negative
control initially exceeded the emulator's qualified conversion range; the
replacement reads a bounded incoming word and fails on semantic output.
Neither fixture correction changed production behavior or broadened the
conversion domain.

Providers remain bounded models. Sparse indices, aliases, incoming-home
writes and private-sine writes do not expand the portable native contract.
No full trigonometric implementation, FCSR exception behavior, hardware,
emulator gameplay or host-port acceptance is claimed. Routine Claude calls:
zero. Reproduce with the retained ignored baseline:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_model_vertex_wave_1517725c_match -v
make tools-check
```

Six byte-identical task files replay in the isolated sibling overlay, with
sibling dependencies and mounted fallback. `64CBFD Tools` remains at
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`; all **2,439 dirty paths** and
before/after status SHA-256
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`
are unchanged.

## Image and measured progress

The **807-input** baseline includes 698 objects and 82 headers. All **803
immutable inputs** remain fixed. Only the source, guarded owner, guard CSV
and linked ELF change. The owner changes only `.text`, `.rel.text`, `.symtab`
and `.strtab`; all eight neighboring raw/padded bodies, bindings and pools
remain unchanged. Conversion rows are byte-identical.

All **6,051 function addresses** remain fixed. Only this function's body and
12-to-424-byte symbol extent change. The production ELF equals the independent
prediction, with **454 changed bytes** and **zero exclusions**. Four closed
metadata permutations are fully accounted:

```text
D_800A71AC, D_8009E47C -> D_8009E47C, D_800A71AC
D_800A71B0, D_8009E480, func_150F34A0 -> D_8009E480, func_150F34A0, D_800A71B0
D_800A71B4, D_8009E484 -> D_8009E484, D_800A71B4
D_800A71B8, D_800A7988, D_8009E488 -> D_800A7988, D_8009E488, D_800A71B8
```

All **189,088 protected bytes across 720 owners** remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production ELF SHA-256:
`6d09d1d30d71f7b2ac2328ef74310e276bb6afce5b15997b8fa27694f47eb651`.

| Section | Byte-exact C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | **4,491 / 5,515 (81.43%)** | 0 | 1,024 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | **3,818 / 4,842 (78.85%)** | 0 | 1,024 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Converted functions remain **5,515 / 6,048 (91.19%)**, converted bytes
**86.17%**. One new C match is credited; **197 more matches** reach 85%
at this denominator. The wider goal stays active.

The scoped Graphify AST merge covers six tools files and the owner, retaining
all **60,853 old IDs**, with zero lost nodes: **60,891 nodes / 114,512 links**.
This is not full-corpus re-extraction. Tools commit `e65d090dfc65ae6d2656ab31735319f5cf07b26b` precedes the
consumer commit. Root README contains aggregate changes only; no push.
`64CBFDOGL` has no source checkout here, and Release remains frozen.

Next focused target: **155-word `func_15176B84`**, VA
**0x15176B84..0x15176DF0**, ROM **0x1A4034..0x1A42A0**, frame **0x20**.
Its complete primary routine is inspected: qualify model/control gates,
visibility and alpha transitions, state dispatch, distance/random paths and
the existing delegated update boundary. Preserve the remaining unrecovered
961-word `func_15175958` and 202-word `func_1517685C` until separately qualified.
