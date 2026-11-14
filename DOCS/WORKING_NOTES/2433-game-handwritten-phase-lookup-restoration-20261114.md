# Game handwritten phase-lookup restoration

Date: 2026-11-14. `func_150A76F0` is restored from its false zero-return C
placeholder to the original handwritten assembly in
`conker/asm/nonmatchings/generated_D4450/func_150A76F0.s`, included by
`conker/src/game/generated_D4450.c`. Its 29 instructions / 116 bytes occupy
`0x150A76F0..0x150A7764`, ROM `0xD4BA0..0xD4C14`; three original zero
alignment words complete the 32-word slot ending at `0x150A7770`.

This is **assembly restoration with zero new C-match credit**. Its original
register protocol takes the phase in T4, a 65-word table in S6, and the
folding constants 128/256 in S7/T9. It returns the table-derived value in
F8 by jumping through V0, rather than the C return register RA. Six retail
computed-return windows use this interface. There are no JAL callers or
literal function pointers in the inspected retail code image. Exposing
this helper as a normal C function would misrepresent that interface.

## Original instruction and object evidence

The restored file is an exact fragment of `conker/asm/D4450.s`; no
instructions, relocations, guards, compiler flags or shared headers change.
All 29 raw, postprocessed and padded words match retail. All 18 other owner
entries and normalized pools are unchanged. GNU links pass at four code
regions (`0x15000000`, `0x25000000`, `0x65000000`, `0x95000000`), with
12 links comparing the complete 32-word slot across the retail fixture
and two padder outputs.

The production full-owner `pad_generated_object` path passes. The strict
`pad_c_object` full-owner inventory rejects the same six pre-existing
global jump labels in both the old placeholder owner and proposal:
`D_150A75BC`, `D_150A75F0`, `D_150A760C`, `D_150A7624`, `D_150A763C`,
and `D_150A7654`. Its checks remain intact. Both padders additionally pass
for an isolated fixture containing this helper's identical compiled words
and its existing layout row. This is not a strict full-owner padder pass.

## Register-protocol qualification

The focused suite compares independently modeled finite table lookup
against original assembly, compiled GLOBAL_ASM and padded streams:

- 5,136 cases cover every byte phase, five table patterns, poisoned upper
  phase bits, stack phases and alternate table bases including wraparound.
- 3,072 cases execute the six authentic computed-return windows through
  their continuation boundaries. Complete parent-routine execution is open.
- Seven cases qualify signed arithmetic traps and table misalignment.
  The T9 subtraction in a branch delay executes even when quadrant three
  later overwrites its result; the oracle preserves this behavior.
- All 29 instructions execute. All 256 fired table-read boundaries agree
  in modeled lower-32-bit GPR, FPR, memory and trace state. There are no
  memory writes, and unrelated register state is preserved.
- Five effective instruction controls reject a changed phase mask,
  quadrant boundary, sign reversal, return register or index stride.

The real table is independently checked between protected retail input
and linked `.game_data`. Native C qualification does not apply to this
non-C protocol. Nonfinite/FCSR behavior, full 64-bit hardware state,
complete parent lifecycle and gameplay acceptance are not claimed.

Fresh installed tests pass in the mounted tools checkout (12.129 seconds)
and an ignored overlay using the sibling tools dependencies (15.478 seconds).
The sibling `64CBFD Tools` checkout retains HEAD
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a` and all 2,439 pre-existing dirty
paths; before/after status SHA-256 is
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`.
`make tools-check` passes.

## Production audit and recount

The independent five-command shadow uses the existing GLOBAL_ASM Make
recipe. Production selects that same recipe automatically after the pragma
is installed. Actual linked ELF equals the independently predicted image:

- Strict full-image delta: 84 bytes, zero exclusions, no metadata groups.
- All 6,051 linked function addresses are fixed; only this helper's body
  and expected 116-byte extent change.
- Only `generated_D4450.c.o` changes among 698 production objects; its
  18 neighbors and pools are preserved.
- All 189,088 protected data bytes, 82 headers and guard rows are unchanged;
  787 immutable input fingerprints pass.
- Conversion CSV changes exactly one field: this helper's language from
  `c` to `asm`. No other function row changes.

ELF SHA-256:
`fcbfcef9989d1268ae859d7346584cb36f175479c6ed31b6fbcd6beb97549f13`.
Original helper body SHA-256:
`8094bf0973b11f720425b9a80440e605c6d5c1605a4fbee7440c4662ec6cb112`.

Actual recount: **4,478 / 5,515 total C functions exact (81.20%)**;
Game **3,805 / 4,842 (78.58%)**; Init **492 / 492**, Debugger **181 / 181**;
zero address drift and 1,037 different C functions. Converted totals become
5,515 / 6,048 (91.19%), 86.17% of bytes; Game 4,842 / 5,327 (90.90%),
85.54% of bytes. The ratio changes because the former false C placeholder
is now classified correctly, not because another C function matched.
At the current denominator, **210** additional exact C matches reach 85%.

Scoped Graphify refresh covers the owner, five tools files and explicit
glabel/pragma extraction for the assembly fragment. All 60,213 previous
node IDs are retained, with the helper concept moved from C to assembly;
60,245 nodes / 113,512 links result. This is not a full-corpus extraction.

## Resume boundary

Next genuine C candidate: **`func_1517AA20`**, 87 words in
`generated_1A7260`, with a normal compiler-generated entry, 0x50-byte frame
and standard float/integer argument handling. Recover and qualify it before
claiming any new C match.

The remaining `generated_D4450` placeholders need an explicit handwritten
root/internal-label audit: five other roots and thirteen internal global
entries remain. Other small mismatch rows such as `func_151F8870` and the
`func_150A613C` / `func_150AE280` groups likewise require ABI/ownership
classification before treating them as C candidates.

`64CBFDOGL` has no available host source checkout at this path, so no host
source/build/runtime adoption is claimed. Its frozen Release is untouched.
Evidence is retained in the ignored
`conker/build/game-phase-lookup-150a76f0-restoration/` directory. Commit
the five qualification tools first, then the source, assembly and consumer
documentation/pin; keep the wider 85% matching goal open.
