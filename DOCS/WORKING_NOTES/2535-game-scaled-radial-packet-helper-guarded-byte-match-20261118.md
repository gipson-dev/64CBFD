# Scaled radial packet helper guarded byte match - 2026-11-18

`func_150B85C0` now replaces its zero-return placeholder with the full scaled
radial particle descriptor submission. Semantic C emits **119 words / 476
bytes**, retaining the **0x98-byte frame**. **19 checked guards** normalize
independent integer setup scheduling and a closed caller-saved GPR role cycle.
No words are inserted or omitted. Both original floating-point multiplies,
all four RNG calls, descriptor bytes and the factory return are preserved.

Actual production recount: **4,545 / 5,514 total exact (82.43%)**, Game
**3,872 / 4,841 (79.98%)**, Init **492/492**, Debugger **181/181**.
Address drift is zero and **969** converted functions remain different.
Conversion inventory and byte percentages are unchanged. **142 more matches**
reach the active85% goal. Root README changes only two aggregate rows.

## Scope, interface and complete source

Owner `conker/src/game/generated_E4070.c`, original `conker/asm/E4070.s:1804`.
VA `0x150B85C0..0x150B879C`, ROM `0xE5A70..0xE5C4C`.
Baseline consumer `c48b70ad12173185f7aac7cff13a58ba8f22d083`, tools
`09bd28576883a8dcabd174e7feac5be6bd6e2341`.
Recovered interface:
`void *func_150B85C0(MenuBurstPointE4070 *, f32 *, f32 *, u8, s32)`.
It returns the allocation result of `func_15130374`, including NULL. The
original parent ignores this return; the emitted helper still preserves it.

The new local `MenuRadialPacketE4070` is **112 bytes**; its Vec3 position is
three32-bit words at0x30. **98 bytes are defined**, while0x5C..0x5F and
0x66..0x6F remain unwritten. The descriptor home is SP+0x28 through the incoming
SP; the first flag's preserved spill is SP+0x20. Declaring the two flag locals
in reverse order recovers that retail home without stack remapping. All172
private/incoming bytes are compared at every call and return. No shared header
changes; all20 neighboring owner functions and pools remain fixed. Offset
field names describe the recovered layout rather than original debug names.

1. Initialize type41, mode0xE03, resource0x200005 and zero word4 before RNG0.
2. Store duration `(u32)RNG0 % 11 + 35`, zero words0x0C/10, fixed RGB and
   effect bytes. Store randomized byte0x1B as `(u32)RNG1 % 51 + 100`, plus
   alpha255 and bytes0x60/61=3.
3. Compute radius*20 into0x28, then height*20 into0x2C. Copy the current
   three-word position; zero all seven floats0x3C..0x54. Input pointers can
   alias one another; the public reads happen after RNG1.
4. Consume RNG2/RNG3 to choose flag bits0x40/0x80 and combine them with0xCE01.
   Set signed bytes0x62/63/64=-1, byte0x65=0, shorts25/10/40, and load the
   then-current `D_8009FD88` into float0x24.
5. Submit `func_15130374(&packet, 1, 0, slot, context)` and return its pointer.

The factory's existing wrapper forwards the descriptor through
`func_15130280`; its source/ABI remain frozen. Providers can mutate public
inputs/literals between RNG calls and all112 exposed descriptor bytes in the
factory. Tests preserve that access order and compare all112 seeded guest
bytes. Native C credits only98 defined bytes and never reads the14 unwritten
bytes for comparison. Allocator/gameplay/hardware behavior remains separate.

## Derived scheduling and independent proof

Raw target SHA-256:
`275be11d043aa292d47ae1ec39ec7c535f9a7c9731f8f30f5849fa8eaf3069f7`.
The normalizer permutes source words89..92 as `[92,89,90,91]`, moving the
independent OR before a literal-address setup, literal load and context load.
Those two loads keep their order; neither FP operation moves. The boundary OR
consumes the old t2 role and defines the new output role. Subsequent words use
the closed temporary mapping
`9->10->11->12->24->15->13->14->25->8->9` through the final call delay.
Each live role is defined before use; the final ABI call closes all temporary
lifetimes. Argument, saved-register, SP and RA roles remain fixed.

Replacement words derive from compiler instructions and relocation identities,
not embedded retail ranges. Independently assembled original code is the
comparison. Three changed rows carry moved HI16/LO16 identities. All119
normalized words equal retail. The complete instruction-driven relation covers
**four paths**, all119 words per side, all172 private/incoming bytes, all112
descriptor bytes, ordered FP/FCSR effects, public read epochs, saved ABI and
returned pointer. Eight effective transfer negatives reject altered kind,
divisors, scale operand, literal address, tail byte, context and return home.
Ordinary mapped/aligned memory and private-stack separation are assumed;
raw fault-register identity, interrupts and hardware FP exceptions are unclaimed.

## Original parent and current production boundary

The parent **`func_150B7B40` remains a zero-return C stub in production**.
Its reconstruction is not installed or credited by this change. The caller
fixture independently GNU-assembles and binds all **484 original parent
words**, matches them to ROM and verifies the real call at **0x150B7D94**.
It records the frozen production parent's different stub/padding bytes and
verifies those stay unchanged in the final ELF.

Retail/raw/normalized helper streams each pass **129 complete original-parent
cases**, with128 helper invocations and one null-actor return. Cases cover
model/no-model positions, zero/nonzero dimensions, floor hit/miss, all flag
branches, clamped dimensions, factory success/failure and mutable providers.
All119 helper words and **483 reachable parent words** execute. The remaining
word at0x150B7D60 is a preserved unreachable duplicate LUI: the preceding
conditional branch jumps past it, and the other path branches around it.
All final memory/GPR/FPR state and provider observations agree across streams.
The other parent's providers, including `func_150B82D0`, remain modeled;
this proves a bounded original-caller connection, not restored live gameplay.

## Fresh production qualification

Eight maintained files use the `game_scaled_radial_150b85c0` stem. Both final
tools configurations pass **six fresh tests**, no errors/skips:
**104.498s primary / 109.153s private sibling overlay**.
Each fingerprints **334 imported tool files**.

- The complete owner uses its existing O2/g3/no-unroll profile and
  `jtbl_8009FD00_game` binding. All20 compact/padded neighbors and pools stay fixed.
- Both real padders match retail. **12 GNU rebases**, **126 raw/binding
  corruption controls** and **126 real CSV corruption controls** pass/reject
  as intended. There are19 guard rows, three with relocation identities.
- Original/raw/normalized code each passes **384 guest cases** covering all119
  words, four input-alias arrangements, mutable RNG services, unsigned RNG
  boundaries, slot widths, allocation failure and the full descriptor/return.
- Native32 O0/O2/O3 each passes384 cases with strict aliasing, no-fast-math
  and UBSan. Eight controlled source negatives reject kind, duration, color,
  radius source, position, flag, context and returned-pointer errors.
- Both configurations build/link the same predicted ELF through three actual
  Make-derived commands and reject four whole-image corruptions.
- Actual production Make compiles only this owner, relinks and regenerates
  progress. No prebuilt object is copied; the ELF equals the independent
  prediction. The pre-existing duplicate generated_12D630 recipe warning remains.
- Strict audit accounts for **358 changed bytes**,
  including the target's size metadata, with **zero exclusions** and no
  symbol/string permutation groups.
  All **6,050 other linked bodies**, all addresses and **189,088 protected
  data bytes** stay fixed. Only one of698 frozen objects changes. Conversion
  rows and the complete previous guard prefix remain unchanged.
- Fresh installed-source compilation reproduces all21 compact functions.
  Production/fresh-raw/fresh-normalized guest and original-parent checks pass;
  unchanged native/proof/padder/rebase receipts are explicitly reused by exact
  hashes. Required tools checks and actual-ELF recount pass.

Production ELF SHA-256:
`e7b6381b18c7ce77f0632bfeaf5de587f69786d2444ef85ad10a6ebe6a1c4e18`.
The freeze contains **1680 inputs**; exactly source, guards,
owner object and ELF change. The actual sibling's2,434 dirty paths and343
dependency hashes remain fixed. Its private overlay uses339 exact sibling
files,382 pinned primary fallbacks and eight task files. The host sibling
currently contains only `.codex` and `recomp_scene`, with no Git/source/build
checkout available for applying this change. Host Release and saves are
untouched; host applicability/runtime parity remains unverified. No Claude
call or push is needed.

One early proof control targeted an unused MTC1 bit and was corrected to the
actual divisor instruction before acceptance. Initial paired imports also
exposed caller assembly running before OUT creation; assembly now runs in
the caller test. Both failed producers were terminal before the scoped fix;
their receipts/fingerprints are retained and final paired tests are fresh.

## Continuation

Graphify has separate native/scoped-merge receipts, retains old IDs and links
the qualified manifest to the installed helper. This is not full-corpus
re-extraction. Commit tools before source, guards, aggregate rows and notes.

Next recover **`func_150B82D0`** (188 words/frame0xE0), the other particle
helper called by `func_150B7B40`, then reconstruct the484-word parent. Its
position/dimension/clamp/ground/spawn behavior is mapped, and the complete
retail-parent fixture now provides a concrete caller harness. The private
drafts in Notes2531/2532 remain uninstalled and uncredited. The85% goal stays
active; this adoption adds one match and leaves142 required.
