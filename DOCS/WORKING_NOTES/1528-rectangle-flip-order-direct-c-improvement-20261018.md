# Rectangle Flip Order Direct C Improvement

Date: 2026-10-18. Consumer predecessor **aa4d27ac**, tools predecessor
**ddd9d88e**. Previous goal turn installed the movement state machine.
This turn makes **progress**, not another completed matching function:
`func_15095D34`, owner `conker/src/game/generated_C1D70.c`,
VA **0x15095D34..0x1509629C**, ROM **0xC31E4..0xC374C**.

## Installed Source Gain

Within each horizontal/vertical flip block, calculate the texture origin
before negating/narrowing the corresponding texture step. These are two
assignment-order changes to the existing typed, commented semantic C.
The SDK macro, signatures, field names, compiler profile and guards stay fixed.

| Measurement | Before | Installed |
| --- | ---: | ---: |
| Complete routine | 346 words | 346 words |
| Frame | 0x88 | 0x88 |
| Raw unequal words | 18 | **6** |
| Literal opening words | 148 | **205** |
| Literal final words | 91 | 91 |
| Previously exact words lost | 0 | **0** |
| New guards | 0 | **0** |

All twelve flip-block differences now emit directly from C. Fixed word
indices are 148/150/151/152/154/155 and 159/161/162/164/165/166.
The routine remains non-matching: do not award a completed-function credit.

The remaining six indices are **205, 210, 211, 224, 242, 254**, at
**0x15096068, 0x1509607C, 0x15096080, 0x150960B4, 0x150960FC,
0x1509612C**. They are the macro X SP+4 versus retail SP+0xC, macro Y SP+0
versus SP+8, and the corresponding signed-halfword access SP+2 versus SP+0xA.
No stack-displacement guards, artificial padding or unused locals are added.

## Current Baseline Screen

New tools: `experiments/game_packet_rectangle_clip_phases.py` and
`tests/test_game_packet_rectangle_clip_phases.py`, under the tools repository.
Artifacts are in `conker/build/game-packet-rectangle-clip-phases/`.

The older rectangle runner freezes a much earlier complete image. Its
rejection of today's movement-installed ELF is a fixture boundary, not a
compiler failure. Keep its hashes and artifacts immutable. The new runner
pins **17 actual current inputs** and calls the existing complete-owner
compiler/linker helpers directly with the normal retail O2/g3 profile.

All **19** unique source forms are compiled and checked against their actual
objects, relative bindings, pools and linked words. Results:

- One flip-order change gives 12 differences; both give **6**.
- Explicit descriptor-dimension locals give 346/347 words, frame0x90 and
  149..209 differences; reject them.
- Step casts at the macro call give 346..352 words and 94..172 differences;
  reject them. Narrowing the macro X argument alone is unchanged at 18.
- All 18 owner neighbors and their relative relocations remain unchanged.
  Owner data pools are unchanged in every form. Preserve the macro's
  full-width Y sign predicate; narrowing Y is an effective negative control.

## Fresh Qualification

The pre-installation twelve-test pass completed in **81.922s**. After adding
physical-object/slot corruption controls and installing the source, all
**13 final tests pass in 50.331s**, exit zero:

```sh
python3 -m tools.tests.test_game_packet_rectangle_clip_phases -v
```

Fresh coverage includes 2,880 geometry cases at both stack phases, native32
O2/O0 with real SDK macros and UBSan, **1,048,576 animation cases per native
selected profile**, eight effective native and compiled-guest controls,
80 guest alias pairs, 16 arithmetic cases/five special floats, 672 animation
pairs, three independent symbol-rebase sets/48 pairs, and 32 connected real
caller/visibility/renderer pairs. All 346 raw-word corruptions, 28 binding
corruptions, extra pools, 346 first-slot corruptions and all live/frozen
input corruptions are rejected.

The first **205** literal words reach **0x15096068** with identical complete
guest boundary state/FCSR in 32 cases; the private-state corruption control
fires. This does not establish complete later private-stack equivalence,
hardware FCSR/fault parity, portable flat-memory aliases or host gameplay.
Old compiler captures remain prior evidence, not fresh captures of this body.

## Real Linked Scope

The actual normal guest owner/ELF/progress builds pass. The whole ELF equals
the immutable prediction made from the **actual emitted C slot**: exactly
**21 changed bytes**, all in the target, no metadata edits/exclusions.
All **6,057** function bodies/addresses are compared; only this target body
changes. Named symbol metadata is fixed. The real padded owner matches the
qualified object including relative relocations. Protected Game data stays
**189,088 bytes / 720 owners / zero differences**. Guard history is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Installed raw object target | `e2e13c5089c8786bc9aeb729e6b90a26440af550d12cffaa93155b14c3514edb` |
| Installed linked target | `ff3d235b00bf542ffc18643e6c90e1d6475223eb188d9827aed631d5b8cb8e79` |
| Complete owner source | `27194aad3aa8465ab2fc1569ffdfa0672e4740efcbdd2c379652ca923eb6e32b` |
| Complete installed ELF | `42fd81f02acabbf952709ae45c24c310e48d68a658b8ed70fb4c4a5399ef475d` |

The new runner's explicit `installed=True` verifies this exact two-file
successor against its immutable predecessor and emitted slot, while compiling
the frozen source for repeatable tests. It does not rewrite disk inputs or
teach any historical rectangle/movement fixture to accept the new ELF.

Fresh official totals remain **Game 2,966/4,828 (61.43%)**, total
**3,639/5,501 (66.15%)**, **1,862 different**, zero address drift. Converted
counts/bytes are unchanged. Root README stays byte-identical; detailed
function updates belong here and in concise working-document indexes.

## Bank And Next Action

Tools **d8111ab** is committed before the consumer source/docs/pin. Both
tools copies have identical new files, pass four Windows ASCII/AST parses,
all eleven shared padder tests per copy and the project-tools smoke check.
Preserve the old mirror's **ddbdd16** HEAD and all **1,181** initial dirty
hashes; only the two new paths are added, giving **1,183** dirty paths.
Do not commit/reset that mirror. No push, Claude call, host-port edit or
frozen Release build/launch occurs.

Continue this rectangle at **0x15096068**, now the first differing word.
Re-establish the clipping-temporary lifetime map for the newly selected
six-difference body before another source decision. Note1440's native
forbidden-home evidence and Note1441's rejected step screens still matter,
but their captures belong to the old 18-word source, not this new body.
Do not force the two homes or narrow the full-width Y sign check. Keep the
wider Game, additional-source, caller and inherited-stack work open.
