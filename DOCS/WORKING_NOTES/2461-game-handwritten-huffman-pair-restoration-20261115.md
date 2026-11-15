# Game handwritten Huffman pair decoder restoration

Date: 2026-11-15. `func_151F8870` is restored from its false zero-return C
placeholder to the original handwritten assembly, included from
`conker/src/game/generated_225D20.c`. Its 47 words / 188 bytes fill
`0x151F8870..0x151F892C`, ROM `0x225D20..0x225DDC`, with no alignment words.
The source comment documents the actual register interface.

This is **assembly restoration with zero new C-match credit**. The routine
takes the byte cursor in A0, bit cursor in T0, lookup-bank selector in A2,
fast-table base in S5 and fallback tree in S0. It returns the decoded pair
in V0/T1, advances A0/T0 and jumps through RA. An ordinary o32 C declaration
would omit important inputs and outputs. The restored fragment is identical
to the corresponding portion of `conker/asm/225D20.s`.

## Exact instruction and register-protocol evidence

Raw postprocessed and padded payloads all match the complete retail body.
There are no guards, relocations, compiler-profile changes or shared-header
edits. All five other owner entries and normalized pools are preserved.
Both `pad_generated_object` and `pad_c_object` pass their complete owner
inventory. Twelve GNU links across four code regions (`0x15000000`,
`0x25000000`, `0x65000000`, `0x95000000`) preserve the full 47-word slot.

The independent semantic model and instruction executor qualify:

- **7,466 cases through three streams**: retail assembly, postprocessed owner,
  and padded owner. Cases cover all 256 eight-bit lookaheads at all eight bit
  positions in three banks, all 255 positive consumed-length bytes, signed
  tree leaves, depths 1 through 25, mixed left/right paths, negative bit
  counters, and alternate table bases including address wraparound.
- **All 47 instructions execute**. The checks compare modeled outputs,
  preserved registers and FPRs, unchanged memory and expected caller stores.
- **62 fired memory-access prefixes** compare complete modeled lower-32-bit
  GPR/FPR, memory, read trace and instruction/delay context between streams.
- **Five signed-arithmetic trap cases** cover bit-count updates, cursor
  overflow, the table-base adjustment and bank-address addition.
- **32 authentic caller cases** cover both original JAL windows. The first
  consumes T1 in the branch-delay move to S6; the second extracts V0's four
  low bits into four halfword outputs. The continuations are bounded windows,
  not complete parent executions.
- **Five effective instruction controls** reject a wrong lookahead mask,
  cursor stride, low-nibble result, omitted slow bit increment and unsigned
  tree-leaf read. The aligned retail Game-code JAL census finds exactly ROM
  `0x225EC4` and `0x226084`; the aligned full-input literal-pointer census
  finds no copies of the helper's entry address.

The model initially needed explicit support for MIPS SRLV. An added cursor
overflow fixture initially consumed fewer than eight bits and did not move
the cursor; setting its initial bit position to seven made the intended
overflow effective. The final pre-install suite passes in 13.178 seconds;
the fresh installed suite passes in 12.250 seconds. These fixture corrections
do not change production instructions or acceptance requirements.

Native C qualification does not apply to this custom assembly protocol.
Complete parent lifecycles, full 64-bit hardware state, FCSR and gameplay
acceptance remain outside this bounded qualification.

## Independent Make and production audit

The independent five-command shadow uses the existing GLOBAL_ASM recipe.
The production build selects the same recipe after installation. Its ELF
equals the independently predicted image:

- **145 changed ELF bytes**, zero exclusions and no metadata permutations.
- All **6,051 function addresses** remain fixed; only this helper's body and
  expected extent change, from the old 12-byte placeholder to 188 bytes.
- Only `generated_225D20.c.o` changes among **698 objects**, in `.text` and
  `.symtab`. Its five neighbors and pools are unchanged.
- All **189,088 protected data bytes / 720 owners**, **80 headers / two
  include files**, original assembly inputs and guard rows remain fixed.
- **814 production input fingerprints** were frozen before restoration;
  the final audit verifies all **810 non-adoption inputs** unchanged.
- The conversion CSV changes exactly one field: this routine's language
  changes from `c` to `asm`. No other function row changes.

Production ELF SHA-256:
`0930a8afce47f722da1559a48e0c00c6f58fe559de1715ab5a1d9b7de9cdbcf7`.
Original helper body SHA-256:
`f38a8bb78d87a3fcb4bd760f2e88a317c35201067d8013f6e60f4b14cc1fd2cd`.

`make tools-check` passes. The existing duplicate `generated_12D630` Make
recipe warning remains. The installed suite also passes in **15.783 seconds**
through an ignored overlay using sibling tools dependencies. The overlay
contains five task files plus the unchanged arithmetic-helper dependency.
The actual sibling `64CBFD Tools` remains at
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`; all **2,434 Windows-Git dirty
paths** are preserved byte for byte. Its before/after status SHA-256 is
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.

Scoped Graphify extraction covers six source/tools files and the explicit
assembly glabel/pragma relationship. All **61,323 old node IDs** are retained;
the helper concept moves from C to assembly. The resulting graph has
**61,351 nodes / 115,207 links**. This is not full-corpus re-extraction.
The root README changes only its four affected aggregate rows.

## Actual recount and resume boundary

Fresh production recount: **4,498 / 5,514 total C functions exact (81.57%)**;
Game **3,825 / 4,841 (79.01%)**; Init **492 / 492**, Debugger **181 / 181**;
zero address drift and **1,016 different C functions**. Converted totals are
**5,514 / 6,048 (91.17%)**, **86.16%** of bytes; Game is
**4,841 / 5,327 (90.88%)**, **85.54%** of bytes. The exact-C numerator is
unchanged. The ratio improves solely because the false C placeholder is now
classified honestly. At this denominator, **189 additional C matches** reach
85%; the wider goal remains active.

Next genuine C candidate: **`func_15017640`**, the view/projection reset in
`conker/src/game_44A90.c`, with **82 body words plus two alignment words**.
It has a conventional 0x28-byte frame, bzero and guPerspective calls. Its old
commented draft clears only four of the six record-flag bytes cleared in
retail. Recover the full six-record reset and qualify the source, callers,
provider effects, object/image and native C before assigning match credit.

The other `generated_225D20` placeholders remain separate work:
`func_151F8994` and `func_151F8B4C` are handwritten decoder parents;
`func_151F8CF0` needs its own complete audit. No batch classification change
is inferred from this one helper.

The `64CBFDOGL` path still contains only scratch `.codex` and `recomp_scene`
directories, without a host Git/CMake checkout. No host adoption is claimed;
its frozen Release remains untouched. Evidence is retained under ignored
`conker/build/game-huffman-pair-151f8870-restoration/`.

Tools commit: `49c475ad263d0b1689716ae4d755be9bac3923b7`.
The consumer source, assembly, tracking rule, aggregate documentation and tools
pin are committed afterward as one coherent restoration. No push is performed.
