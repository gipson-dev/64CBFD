# Game attached-direction callback guarded match

Date: 2026-11-14. `func_151A87F8` replaces the zero-return placeholder in
`conker/src/game/generated_1D4E00.c`. Its 138-word retail slot is
`0x151A87F8..0x151A8A20` (ROM `0x1D5CA8..0x1D5ED0`). The semantic C
retains the original 0x90-byte frame and saved-register contract. Of the
138 words, 120 emit directly; 18 expected-word guards restore three local
homes, three return-constant schedules and one commutative address operand
order. No instruction is inserted or omitted. All floating arithmetic emits unchanged.

The eight stack-reference guards move the collision token from SP+0x5C to
SP+0x78, the three-component delta from SP+0x78 to SP+0x7C, and the
orientation temporary from SP+0x6C to SP+0x60. All passed pointers and
stores move together. Nine words rotate three closed mask/store/return
constant schedules; branch destinations stay unchanged. The remaining
word swaps the operands of the matrix-address addition. Both padding
outputs match all 138 retail words and relocations.

The callback snapshots the owner cache and its target pointer, rejects an
inactive target, identity mismatch or type 0xFF, and returns zero for those
invalid attachments. With a matrix, it transforms the cached local point
through the selected 64-byte target matrix. Unless the cache is already
latched, it submits a collision query and checks the returned hit token.
A rejected query clears direction-valid bit 2 and still returns one for the
valid attachment. An accepted hit latches cache bit 1.

The remaining path computes the endpoint delta and stores the helper's
length. Nonzero lengths update the reciprocal and orientation, then set
bit 2. Positive and negative zero clear bit 2 without replacing the prior
reciprocal. A NULL matrix also clears bit 2 and returns one. Cache and target
pointer snapshots survive helper-visible link changes; flags, coordinates,
parameters and length fields are read or written at their original stages.

The retail table `D_8008F940[1]` points to this callback. Sixteen original
caller windows at `0x151A7AF0..0x151A7B1C` execute its indirect lookup and
call, then the zero-test consumer of the return value. The complete caller
`func_151A7A90` remains a production placeholder and is not qualified by that
window. Continue with that caller next to restore this part of the chain.

Guest validation compares an independent bounded model with retail, raw C
and padded streams in 2,048 ordinary cases and 6,224 full executions.
This includes the 16 caller windows and 16 additional guest-only alias cases:
the cache overlaps the orientation temporary, or the target aliases the
owner. Those alias cases compare retail and padded streams. Raw C uses its
own three local homes in the disjoint cases; it is not credited with the
retail temporary-address or intermediate private-state contract.

Cases cover target rejection, unsigned identities and matrix indices,
NULL matrices, cached and queried endpoints, query/hit outcomes, zero and
negative-zero lengths, negative and positive modeled lengths, reciprocal
updates and helper-visible mutations. All 136 reachable instructions are
exercised. The original duplicate loads at `0x151A8844` and `0x151A89FC`
are unreachable from normal entry and remain intact. Retail and padded
modeled machine states agree at 168 fired memory-access prefixes, including
the return-register timing restored by the schedule guards.

Native 32-bit C passes 259 cases in each of six O0/O2/O3 and
strict/no-strict-aliasing configurations with trapping UBSan. All seven
source controls are detected: incorrect live gate, identity comparison,
matrix stride, collision delta, latch bit, reciprocal and cache reload.
Fixtures use typed, aligned, disjoint objects, initialized helper outputs,
finite floats and a complete matrix buffer. Numeric words and pointers
are checked separately from unchanged byte ranges to account for native
endianness. These checks model the transform, collision, hit, length and
orientation providers. Their complete bodies, the full caller lifecycle,
unrestricted C aliases, nonfinite/FCSR behavior, hardware and gameplay are
not qualified. Prior unchanged neighbor receipts remain prior evidence.

Both padders pass 12 GNU links over four independently rebased layouts.
The other 22 owner functions and normalized pools remain unchanged, and the
target compile has no diagnostics. Production Make uses normal compiler,
padding and link rules for the changed owner. Since all 18 appended guards
belong to this target and every prior row is preserved, the scoped build
marks the guard manifest old and reuses the 697 frozen neighboring objects:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The resulting ELF equals the independent shadow prediction. The strict
whole-image audit accounts for all 413 changed bytes with zero exclusions
and no metadata cycles. All 6,051 function addresses and 189,088 protected
Game-data bytes remain fixed. Only the target owner changes in the
698-object census. The conversion manifest, Makefile and earlier guard
rows remain unchanged.

Tools commit `03c4cf6` retains the installed suite. It passes in the mounted tools
checkout and an isolated sibling-tools overlay; the sibling's 2,434 existing
dirty paths are preserved. `make tools-check` also passes:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_attached_direction_151a87f8_installed -v
```

A scoped fail-closed Graphify refresh retains all 60,141 prior node IDs and
produces 60,141 nodes. This is not a full-corpus re-extraction. No host files
were modified. The prior `64CBFDOGL` path currently contains diagnostic/
capture directories rather than the former host source checkout, so no
host source, build or runtime comparison was attempted. This adoption is
qualified against the retail decomp inputs and does not alter a host release.

Fresh production recount: Game **3,800 / 4,843 (78.46%)**, total
**4,473 / 5,516 (81.09%)**, zero drift. At the current denominator,
**216** additional exact matches are needed to reach 85% total.
