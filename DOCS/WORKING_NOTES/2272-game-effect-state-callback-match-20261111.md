# Effect-state callback byte match

Date: 2026-11-11. `func_150BF0F4` replaces the zero-return placeholder in
`conker/src/game/generated_EC420.c`; original assembly is in
`conker/asm/EC420.s`. Its 74-word retail body spans VA
`0x150BF0F4..0x150BF21C`, ROM `0xEC5A4..0xEC6CC`.

The C callback updates an effect's intensity toward a target or zero, advances
two signed halfword accumulators using the global tick, caps its phase byte,
and returns one when the effect should be removed. Unsigned intermediate
arithmetic preserves the retail low-word wrapping behavior. It reloads the
activity byte after the intensity store, as retail does.

The compiler emits 73 raw body words. Twenty-eight expected-word guards
normalize register allocation and instruction scheduling, and one guard also
inserts the additional retail branch. The resulting 74 words and relocation
bindings match retail. The raw semantic C and normalized instructions are
both tested; the guarded output must not be described as an unguarded match.

A bounded oracle compared retail, raw C and guarded output in 1,020 cases,
including signed and 32-bit wrapping boundaries, and visited all 74 retail
words. Native SDK32 O0/O2/O3 each passed the same 1,020 cases and 11 negative
controls with undefined-behavior sanitization. The original dispatcher window
uses `D_8008CBA0[8]` and branches on the callback return. An aligned ROM
scan found its address at `0x231680` and no direct JAL. In 2,040 cases the
complete original `func_1516D678` dispatcher ran with linked and null binding
records, visiting all 48 words; the final release helper was modeled. Inputs
use valid disjoint records and tick storage. Arbitrary aliasing, concurrent
mutation, hardware faults and complete release-helper behavior are not
qualified.

Both padders agree with independently assembled retail code and bindings;
12 rebased GNU links, 26 bounded access-cut triples and 108 corruption
rejections pass. Actual Make and strict independent image comparison account
for **210 changed bytes** with zero exclusions. All 6,050 function
addresses and 189,088 protected data bytes remain unchanged. Actual ELF
SHA-256: `ee0ff44a48872e1f2db4d1917cd8bf47de920136c6f5c6fb08113c9cc014c957`. The existing complete-ROM checksum mismatch
remains.

Fresh actual ELF recount: **4,340 / 5,513 (78.72%)** overall and **3,667 /
4,840 (75.76%)** Game, zero drift and 1,173 different. The 80% target needs
71 more exact functions. The tools commit `8c9ef5c9ef0bf971b9c4e49965032a6ddf6011c4`
precedes the consumer change.
