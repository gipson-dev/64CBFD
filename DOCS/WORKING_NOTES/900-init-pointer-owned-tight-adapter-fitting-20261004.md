# Init Pointer Owned Tight Adapter Fitting

Date: 2026-10-04. Starting HEAD: `69fca7fd`.

## Combined Hypothesis

Note 876's direct input/workspace sourcing saved two adapter stores but lost
the saving to input-section padding. Combining it with Note 899's tight
adapter may cross the aligned-rodata boundary rather than just reduce text.

The compiler option `--core-pointer-arguments` requires frame backing. In guest
builds, the header is read from the numeric input argument, and the core writes
the advanced input pointer before the stream reads it. Workspace address is
derived from the initialized workspace pointer in state, not a fifth argument.
Native builds keep their separate pointer/numeric-address semantics unchanged.

Pair this with assembler `INIT_DECODE_CORE_POINTER_ARGUMENTS=1`. It omits only
the input-state store at SP+0x20 and fifth-argument store at SP+0x10. Retain the
workspace pointer, output pointer, frame pointer, physical callee saves and
Note 899's RA/SP schedule. Compiler and assembler selections must be paired;
neither is a standalone production replacement.

## Sizes And Actual Link Layout

Packed core text stays 4,384 O2 / 5,792 O1. Adapter body/executable section
falls 184 -> 176, yielding packed executable text 4,560 / 5,968. Stack
allocation and packed call bounds stay unchanged at 392 / 352.

Isolated O2 layout:

| Candidate | Executable text end | rodata start | rodata end |
| --- | --- | --- | --- |
| Default 192-byte adapter | `0x104011E0` | `0x104011E0` | `0x104012B0` |
| Tight 184-byte adapter | `0x104011D8` | `0x104011E0` | `0x104012B0` |
| Pointer-owned tight 176-byte adapter | `0x104011D0` | `0x104011D0` | `0x104012A0` |

Unlike the intermediate tight adapter, the combined form reduces the measured
text-plus-rodata span sixteen bytes from the default. New tests require the
next read-only section to start at code end for both packed profiles. This is
isolated linker evidence, not production ROM placement. Executable text still
exceeds the retail 3,984-byte group by 576 bytes in O2.

Ignored receipts: `init-tight-pointer-ownership-trial-20261004/`,
`init-pointer-owned-adapter-trial-20261004.o`, and
`init-pointer-owned-adapter-o2-trial-20261004.elf`, all under `conker/build/`.

## Ownership Guards

The fixture adds input field zero to the existing read-before-initialization
guard. It poisons the omitted fifth-argument slot and rejects reads until a
full write initializes that slot. The slot may legally become a compiler spill.
Both omissions are checked in executed adapter words. Injected early LW reads
at the compiled core entry must fail with the specific input/fifth-slot guards.

An initial assertion incorrectly required the fifth slot to remain untouched;
frame O1 legitimately spilled into it. That run stopped at 18 tests in 94.842
seconds and receives no qualification credit. The corrected fence checks
consumption of uninitialized data, not irrelevant final-slot preservation.

## Default Preservation

Fresh packed builds with the new compiler option omitted match the old
scan-deficit objects' extracted `.text` exactly: 4,384 O2 / 5,792 O1 bytes.
Current default adapter `.text` matches the prior revision exactly, 192 bytes.
No existing default, native header behavior or production owner changes.

## Qualification

Corrected whole bounded run: 45 tests in 268.937 seconds, 44 passes and one
deliberate full-corpus skip. The suite retains live-SP, callee-return, ordered
FPR publication and six-shape semantic/error/storage checks, plus both executed
stale-read controls. Source/flags stayed fixed during this corrected run.

| Shape/profile | Linked executable text | Static / observed descent |
| --- | ---: | ---: |
| Frame O2/g3 | 5,536 | 3,256 / 3,256 |
| Frame O1 | 5,984 | 3,176 / 3,176 |
| Aligned end O2/g3 | 4,576 | 3,232 / 3,232 |
| Aligned end O1 | 5,968 | 3,192 / 3,192 |
| Packed remaining O2/g3 | 4,560 | 3,240 / 3,240 |
| Packed remaining O1 | 5,968 | 3,200 / 3,200 |

Other-shape reductions may include core allocation changes; the packed core
sizes above remain unchanged. Packed O2 minimum SP stays `0x80031D68`, margin
88 above the known neighbor. This does not establish full stack reservation.
Previous full corpora do not qualify this new combination. Tool/whitespace
checks pass; no full corpus, native suite or production rebuild is claimed.

## Next

- [x] Combine the two store omissions with the tight adapter and measure rodata placement.
- [x] Preserve omitted-option core/adapter text exactly.
- [x] Pass corrected whole bounded suite with executed input/fifth-slot controls.
- [ ] Full combined-candidate guarded corpora across masked CU1 modes.
- [ ] Continue fitting and prove full reservation, entry/frame ownership and hardware/context.

Production sources, README totals, word guards, sibling-port artifacts and
unrelated Game edits are unchanged. No production ROM or hardware run claimed.
