# Four-Head Lookup: Private Normalization Checkpoint

2026-10-24. `func_151AE590`, `generated_1D92F0`.

## Status And Acceptance Boundary

**Private, unqualified and uncredited. Nothing installed.** Complete semantic
C emits 43 body words plus one zero alignment word. A mechanically derived
normalization reproduces all 44 retail body words, including the unreachable
duplicate assignment. This is not a compiler-only match, and no production
guard rows have been appended. The source still contains its old placeholder.

The last installed checkpoint remains consumer `b1ac99c9`, tools `c7501612`,
[Note 1708](1708-linked-record-event-match-20261024.md): 3,785/5,505 exact
(68.76%), Game 3,112/4,832 (64.40%), zero address drift and 1,720 different.
The 75% threshold remains 4,129, requiring **344 more installed matches**.
No fresh production build/recount is claimed for this private experiment.

## Original Routine And Interface

- Source: `conker/src/game/generated_1D92F0.c`.
- Original: `conker/asm/1D92F0.s`.
- VA `151AE590..151AE640`; ROM `1DBA40..1DBAF0`.
- Retail extent: 176 bytes / 44 body words, frame zero, no alignment tail.
- Retail SHA-256:
  `98adf57f48b176f134989f22e64f57e0c91bb98ab109b282a7a9373e980d564a`.
- The byte-key argument is masked to eight bits, while its full incoming
  A0 word is stored in the caller's argument home at SP+0.
- The return is a node address or zero, with no helper calls. Existing code
  uses both pointer and signed address-word interfaces; the proposed C uses
  an explicit node-pointer return, not an undefined fallthrough.

The two mapping words at `D_800A9270` / `800A9274` are 47 and 78, retained in
`conker/asm/data/24DD30.rodata.s`. For each selected column, scan row zero
then row one in `D_800DCE50`, with row stride `0x1A0` and four-byte cells.
Priority is **column47.row0, column47.row1, column78.row0, column78.row1**.
It is not row-major across the columns.

Each selected cell is a head pointer. Follow node+8 links and compare the
unsigned byte at node+0x10. Retail loads the tag, then captures the next
pointer before the match branch, even on a successful return. Other node
fields and unused table cells are not recovered here. Existing insertion
and removal code in `conker/src/game_1944C0.c` confirms the byte-view row
stride and link offsets; related lookup `func_15155FD4` confirms this node
prefix. Do not replace `variables.h`'s partial byte view with a claimed
complete table structure.

A full aligned scan of the prepared matching `conker.us.bin` covers 616,822
words and finds exactly one direct JAL, ROM `1DB5A8`, and no literal pointer
words equal to the entry address. The call is VA `151AE0F8` inside original
`func_151AE0E4`. This is a prepared matching-reference scan, not a claim
about all original compressed-ROM media or dynamically computed calls.

That caller passes the byte at SP+0x3F, consumes V0 as a pointer, spins
forever on NULL, then reads signed short node+0x52 on success. The larger
caller remains a C stub. Its complete behavior has not been qualified.

## Source Fitting

The best normal-profile source uses a private 104-cell row storage view,
only dereferencing the four selected cells. Its loops are equivalent to:

```c
LookupNode1D92F0 *func_151AE590(u8 key) {
    LookupNode1D92F0 *node, *next;
    u8 outer, row;
    s32 column;

    outer = 0;
    do {
        column = D_800A9270[outer];
        row = 0;
        do {
            node = ((LookupRow1D92F0 *)D_800DCE50)[row].cells[column];
            while (node != NULL) {
                next = node->next;
                if (key == node->key) return node;
                node = next;
            }
            row++;
        } while (row < 2);
        outer++;
    } while (outer < 2);
    return NULL;
}
```

This emits 43 body words plus an alignment zero under existing IDO5.3
`-O2 -g3`, with no diagnostics. The complete raw body hash is:
`71952928fbaef3df6feb05e20f6da60a8c974c6467a7840c9260b4183f204e55`.
The raw word/length difference score against retail is 38, not one: equal
slot size does not imply matching code. Typed pointer-row indexing recovers
retail's shift/add row calculation and avoids changing HI/LO. Ordinary byte
offset expressions instead emit a hardware multiply and are not equivalent
to retail's complete private state merely because the returned node agrees.

Additional byte-offset, signed-address, counter, post-increment, mapping
address and inner-loop forms did not produce a direct match. Direct compiler
profile checks, with an exact normal-wrapper positive control, measured:

| Profile | Body Words | Word/Length Differences | Diagnostics |
| --- | ---: | ---: | --- |
| O2/g3 | 43 | 38 | None |
| O2 | 43 | 40 | None |
| O2/g2 | 60 | 60 | Optimization disabled warning |
| O1 and O1/g3 | 54 | 53 | None |
| O3/g3 | 43 | 38 | `uld` unsupported `-Xfullwarn` warning |
| O2/g3 with `-Wo,-loopunroll,0` | 43 | 38 | None |
| O2 with `-Wo,-loopunroll,0` | 43 | 40 | None |

The same results hold for scalar-address and defined-constant mapping
diagnostics. Earlier attempts to pass unsupported extra flags through the
asm-processor wrapper were interface failures, not measured compiler
outputs. The subsequent direct checks above resolve that ambiguity.
No compiler or Make profile was changed.

## Derived Private Recipe

The recipe validates the complete raw-body hash and all four bindings.
It derives the fitted body from those C-generated instructions, not from a
retail-body replacement:

1. Fold the map base's existing low ADDIU relocation into its indexed LW,
   and move map address setup into the outer loop.
2. Reorder independent base/counter setup and exchange closed V1/A0
   lifetimes for row and node roles. Rename the head-cell, tag and mask
   temporaries consistently.
3. Retain the column shift using the now-free address temporary and derive
   its result copy from an existing MOVE instruction.
4. Convert the mismatch and next-node branches to likely branches. Copy the
   existing node-advance instruction into their required positions, including
   the unreachable duplicate after the successful return.
5. Peel the existing tag load into the next-node likely delay slot, remove
   the old redundant NOP and derive every changed relative branch target.

The table HI/LO bindings remain at offsets 8/12; mapping HI/LO move to
offsets 24/32. The original four raw bindings are at 8/24 and 12/20.
Standard HI/LO carry relocation at the original symbol addresses produces
all 176 retail bytes and the retail hash above. Independent GNU assembly,
carry-boundary rebases and real production padding remain **open**; this
check is not a substitute for them.

The ignored private validator rejects a perturbation to each of the 43 raw
words. Retail and raw C were executed with the existing MIPS oracle over
2,048 valid-list cases: all 256 byte keys across eight empty/nonempty and
duplicate-key layouts. Each agrees with a column-first reference on return,
preserves callee-saved registers, writes the complete incoming home word,
and otherwise leaves fixture memory unchanged. These are separated-stack,
valid-list public-semantic checks, not native32, adversarial alias, arbitrary
pointer, fault-prefix, private-register or full-caller acceptance.

## Reproduction And Next Work

Native scratch: `conker/build/game-four-head-lookup/`.
Checked PSBBN cache:
`/tmp/cbfd-ray-stream-a38bdeb53163/64CBFD`.
Use the checked stdin bridge, not DrvFS project reads. The 36 focused inputs
and all 1,454 linker objects were captured within the 16,002-file seal before
screening. The independent older tools mirror's 1,630 dirty paths must remain
untouched.

`index_screen.py` produces the selected `index-0-0-0.c/.o` under `qualified/`.
`private_recipe.py` derives and tests the fitted words and writes
`qualified/private-recipe-proof.json`. `direct_profile_screen.py` and its
`--nounroll` mode produce the measured profile receipts. Other screen runners
are `screen.py`, `address_screen.py`, `counter_screen.py`,
`signed_address_screen.py` and `byte_row_screen.py`. Their outputs are private
experiments, not production qualifications.

Next: bank the recipe in focused tools/tests, then close native32 and effective
controls, aliases and access faults, actual caller ABI/window bounds,
independent relocation rebases, complete owner/neighbors/pools, real padder,
actual Make and strict full-image prediction. Preserve all six handwritten
owner functions. Only after those gates pass should the C and derived guard
rows be installed, rebuilt, independently audited, adopted, freshly recounted
and committed tools-first. Until then the source, guards, object, ELF and
README matching counts stay unchanged. The wider 75% goal remains active.
