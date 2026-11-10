# Script action dispatcher restored as direct C

Date: 2026-11-10. `func_1509D780` replaces its zero-return placeholder with
the complete action switch: **95 words / 380 bytes**, original **0x18 frame**,
**zero word guards** and an exact **40-entry / 160-byte switch pool**. Preserve
the existing O2/g3/no-unroll owner profile and bind its compact pool to the
retail `jtbl_8009F1AC_game` using one scoped Makefile variable. No arithmetic
substitution, insertion, omission, opaque assembly or shared-header change.

Fresh actual-ELF recount: **4,317 / 5,513 (78.31%)** total; Game **3,644 /
4,840 (75.29%)**; Init **492/492**; Debugger **181/181**. Zero address drift,
**1,196** different. **94 more** accepted matches reach 4,411/5,513 and the
active 80% goal. Conversion CSV and converted-function/byte totals remain fixed.

Baseline consumer `bf3b9107130c5036ee61a51eea103e77900ca962`; tools
`ece935d4b5061ecc64ef88ea36777dde0f3a7c8e`, from
[Note 2247](2247-game-actor-slot-allocation-direct-match-20261110.md).
Bank the eight proof files first in tools commit `877567d5791e6676f83df5e184dd603fff52a345`. Local commits only.

## Source, actions and return boundary

Owner `conker/src/game/generated_C9EC0.c`; retained original assembly
`asm/C9EC0.s`. Retail span VA **0x1509D780..0x1509D8FC**, ROM
**0xCAC30..0xCADAC**. The old 12-byte stub differed at 88 retail-slot words.
Retain its integer-return interface and recover the two actual input registers:

```c
s32 func_1509D780(s32 command, u8 *record);
```

The original C return type is not independently proven. Only command 9's
null-actor branch explicitly returns a C value, zero. Other branches fall
through after their side effects. The retail machine may leave incoming V0,
propagate helper V0 or return the lookup's null pointer. Preserve those exact
instructions and check every resulting register value through the original
interpreter. Do not replace them with a deterministic default return.

This is a retail-compiler matching source with a deliberate return boundary:
**portable C fall-through results are unqualified**. Native tests discard all
such results and only consume the explicitly defined command-9/null result.
They disable GCC's return-type warning for that deliberate source shape;
UBSan remains enabled. The IDO owner itself emits zero diagnostics. A host
port that consumes other C return values needs a separate explicit policy.

The switch range is selectors 2..41. The full action groups are:

| Selector | Recovered operation |
| --- | --- |
| 2 | clear byte `D_800D9920` |
| 4, 5, 6 | call `func_150E35DC(command >> 6)` |
| 8 | call `func_150B3DD0()` |
| 9 | masked 12-bit actor-key lookup, explicit null return, then `func_150C5C9C` |
| 10 | call `func_150C522C()` |
| 18 | signed word at record+4 to `func_151CD394` |
| 19 | signed halfword at record+6 to `func_151D2718` |
| 21 | submit `(0x20, 0x18, 0)` to `func_151616D0` |
| 22 | submit `(0x23, 0x28, 0)`, then `(0x24, 0x28, 0)` |
| 26 | submit `(0x26, 0x18, 0)` |
| 36 | masked actor-key lookup; call `func_150F6DB0` only when non-null |
| 38 | submit `(0x29, 0x18, 0)` |
| 39 | unsigned byte at record+7 to `func_150F9720` |
| 41 | call `func_150EB8C4()` |

Other selectors use the shared epilogue without reading the packet. Packet
field views retain signedness and the original load timing. A forward-declared
`struct struct127` keeps the recovered lookup's pointer return compatible
with its actual definition. The old-style `func_151D2718` halfword parameter
is declared with its promoted s32 argument at this call boundary. Other helper
declarations follow their current definitions; shared SDK headers stay fixed.
The no-argument `func_150EB8C4` entry overwrites argument registers before its
first nested call. Its larger algorithm remains outside this qualification.

## Direct code, pool and whole image

The first complete switch emits all 95 retail words after binding, with no
source fitting hints. Raw target SHA256:
`0bbcf5457f7ff0d71971b08734cf0eba9bb02ceeb96271d66c3e12a16ee43f98`.
Its twenty bindings include the compact `.rodata` table, one global flag and
the real helper addresses. Only the table symbol is rebound by the existing
padder's `--rodata-symbol` mechanism; no instruction word is normalized.

The owner previously had no compact rodata pool. Prove all forty new R_MIPS_32
entries belong to this function and equal the preserved retail destinations.
All **18 other functions**, raw/padded bindings and register information remain
equal. There are no other changed pools or IDO diagnostics. The full historical
word-guard manifest remains byte-for-byte unchanged.

Three actual Make commands under the proposed Makefile agree with independent
complete-owner compilation using the existing **O2/g3/no-unroll** flags.
The Makefile changes exactly one target-specific retail pool binding. No other
owner profile, recipe, header, layout or conversion row changes.

Freeze **2,241 input fingerprints** and exact mutable baseline files. The strict
predicted ELF changes exactly **271 bytes**: target body and its symbol size
**12 -> 380** only. No metadata permutations; **zero exclusions**. All **6,050
function addresses** remain fixed. All **189,088 protected bytes / 720 data
owners** remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
This includes the original switch pool and callback table.

## Focused validation and original interpreter

- **704 guest cases / 1,408 executions** compare complete memory, GPRs, FP
  registers, traces and calls in 704 pairs. Cover all forty table slots and
  **all 95 instructions**, out-of-range/negative/upper-flag selectors, null
  lookups, signed field edges, packet/flag/stack aliases and clobbering opaque
  helpers. Every actual MIPS V0 value is checked against the independent model.
- **680 native SDK32 cases/profile at O0/O2/O3**, **2,040 total runs**, reproduce
  **80,364 serialized public/call bytes/profile**, with UBSan and
  `-fno-strict-aliasing` for the raw mixed-width packet views. Native data is
  serialized canonically; packet aliases remain guest-only. Fall-through
  returns are discarded, with only explicit null returns consumed.
- **17 effective compiled controls** complete normally and change observed
  behavior. Cover wrong flags/masks, byte/halfword signs and offsets, helper
  ABI sign extensions, missing/reordered submissions, wrong selectors,
  omitted calls, lookup gates and explicit null results. Ineffective cast-only
  trials were rejected; two sign controls also alter the declaration contract.
  No execution errors count as counterexamples.
- Both independent padders pass; reject **115 word/binding corruptions** and
  **all 40 individual pool-entry corruptions**. **80 guest executions** across
  four symbol sets and **16 actual GNU linker comparisons** cover low halves
  0, 0x7FFC, 0x8000 and 0xFFFC. **25 exact target-access cut pairs** and eight
  full-image corruptions pass their expected checks. Isolated reference
  assembly localizes exported jump labels only for branch resolution; the
  production image retains the actual exported labels and addresses.

The aligned census finds zero direct J/JAL sites and one literal pointer,
ROM **0x22CF50**, loaded at **0x80088490**: entry 13 of callback table
`D_8008845C`. The original handwritten interpreter's internal entry
**0x150AE108** selects this table, passes the original record in A1 and clears
dispatch bits 12..15 from its word into A0. The encoded callback nibble is E.
An outer dispatch selects builtin slot 4 and reserves its original argument
homes before reaching the callback.

**368 original VM pairs / 736 executions**, covering **42 window words**, check
both indirect dispatch levels, callback arguments and publication of actual
V0 to **D_800D3848**, followed by the result pointer at D_800D384C. Preserve
the handwritten S7/RA convention and SP restoration rather than asserting a
generic O32 contract for the whole interpreter. Additional **624 pairs /
1,248 executions** connect the original 55-word actor lookup across all 26
slot positions, signed states and key limits, covering 52 helper words. Its
entire current linked body still equals retail. The interpreter's existing C
stub remains untouched/uncredited. Complete VM, effect-helper, hardware and
live-gameplay behavior are not claimed; computed indirect calls remain
unexcluded beyond the qualified path.

## Production, banking and continuation

Production completes in **190.33 seconds**, matching the predicted
owner, ELF and binary. Existing duplicate `generated_12D630` recipe warnings
and expected whole-ROM checksum exit 2 remain. Actual-ELF recount passes.

| Artifact | SHA256 |
| --- | --- |
| Production ELF | `850efdf299b1811a970e342af134f4399c742c99aab1a7bfd715119703473890` |
| Built binary | `b6d8a528c3a1bda4be7a4583254eaacfd4ead23f1706699264335411a484cf9e` |
| Padded owner | `cfc6059f9e3ce63dbdb3ede6811a94169c05fabe99c85223a382c1ce8ffb28c8` |
| Makefile | `91eacf1733f0554dec7fa2ab6f1d2658f4bf3b180bc2b54693389216f2e97f5c` |

Eight fresh preinstall checks pass/environment: mounted
**118.07 s**, sibling **73.51 s**.
Two fresh installed checks requalify Make/image and guest behavior: mounted
**33.80 s**, sibling **38.51 s**. The
other six methods are explicit preinstall reuses with all tool/imported
dependencies rehashed. Shared smokes are fresh, while three unchanged pure
helper regression receipts per environment are reused separately.

The sibling uses an exact eight-file private overlay, including the new local
compiler wrapper. Missing diagnostic/binding helpers use explicit mounted
fallbacks; Make uses the mounted CLI and independent in-process padders use
sibling helpers. All **2,434 pre-existing sibling dirty paths** are preserved.
Codex is sole writer; zero Claude calls. Host source, saves and frozen Release
are untouched.

Scoped graph: **59,698 nodes / 113,087 links**. All
59,698 old nodes are retained or relocated; outside-scope
definitions stay fixed apart from community metadata. Verify all nineteen C
positions. New tools have 0 indexed nodes under
existing submodule filters. Historical excluded nodes are retained; this is
not a full-corpus extraction. Post-commit receipts audit heading relocations
and actual graph-worker completion separately.

```sh
python3 -m unittest tools.tests.test_game_event_dispatch_1509d780_match -v
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Reproduction needs the prepared WSL PSBBN consumer and retained pre-adoption
mutable inputs under `conker/build/game-event-dispatch-1509D780-match/frozen/`.
No ROM/ELF binary is committed; an unprepared clone is not claimed to reproduce
the workspace image.

Next: investigate **`func_150C4D20`**, 95 words/frame0x48,
in `generated_F21D0.c`. Its 12-byte placeholder still
differs at 91 retail words and remains untouched/uncredited.
The complete original updates float angle/velocity, accumulates ticks, submits
a periodic helper call and performs a trigonometric/damped wrap update.
Qualify record layout, helper effects, callers, return ABI and float conversion
domains before implementation. Keep the wider 80% goal active.
