# Four-Head Lookup Guarded C Match

2026-10-24. `func_151AE590`, owner `generated_1D92F0`.

## Result And Scope

**Installed, production-qualified and adopted.** Fresh actual native-ELF
recount: **3,786/5,505 exact (68.77%)**, Game 3,113/4,832 (64.42%), zero
address drift, 1,719 still different. The 75% threshold remains 4,129, requiring
**343 more matches**. Only this function leaves the unmatched queue.

The complete semantic C lookup matches all **44 retail words / 176 bytes**,
frame zero, with two HI/LO pairs. IDO5.3 emits 43 body words and one alignment
zero. Thirty-seven checked, derived guard rows recover retail's allocation,
address setup and branch-likely peeling; the final C return-delay NOP is
moved, not invented as alignment filler. This is **guarded semantic C, not a
compiler-only match or an assembly-body replacement**.

The C uses an explicit node-pointer return and unsigned byte key. The private
node type recovers only next+8 and key+0x10. Its row storage view permits typed
indexing but does not claim that every unused table cell is a pointer.
`variables.h`'s partial byte-table declaration stays unchanged.

Tools `f2a63f56cbb871aef3fd9084a3c8100e235f208d` are committed first.
Consumer changes are the one C body/declarations, 37 appended guard rows,
tools pin, aggregate README rows and focused documentation. No shared
header, compiler profile, dependency/provider configuration, host or Release
artifact changes. No push.

## Inputs And Recovered Behavior

- Source `conker/src/game/generated_1D92F0.c`; original
  `conker/asm/1D92F0.s`.
- VA `151AE590..151AE640`; ROM `1DBA40..1DBAF0`.
- Retail SHA-256:
  `98adf57f48b176f134989f22e64f57e0c91bb98ab109b282a7a9373e980d564a`.
- Complete raw 172-byte body SHA-256:
  `71952928fbaef3df6feb05e20f6da60a8c974c6467a7840c9260b4183f204e55`.

The mapping at `D_800A9270` selects columns 47 and 78. For each column,
scan row zero then row one in `D_800DCE50`, stride `0x1A0` bytes.
Priority is **47.row0, 47.row1, 78.row0, 78.row1**, not row-major columns.
Traverse next+8, compare the unsigned key at +0x10, and return the first
matching node or NULL. Retail loads the tag then captures next before the
match branch, including on a hit. Keep the unreachable node-advance word at
index 31. Store the entire incoming A0 word at SP+0 before masking the key.

The insert/remove helpers in `conker/src/game_1944C0.c` and related
`func_15155FD4` establish the partial table/link view; preserve their
definitions. A full aligned scan of the prepared matching reference covers
616,822 words: one direct JAL at ROM `1DB5A8`, no literal entry pointers.
This is not a scan of every compressed original-ROM medium or computed call.

Original caller `func_151AE0E4` passes LBU SP+0x3F at VA 151AE0F8.
NULL spins at 151AE108. Success uses the returned pointer and signed short
node+0x52, then owner enable/busy bytes. Its current C body remains a stub.
Qualification covers the original call interface, three early-return edges
with five return-value cases, one NULL-loop iteration and the continuation
boundary at 151AE134. The remaining math/helper path is not restored or
credited, and this does not claim gameplay acceptance.

## Derived Guards And Actual Build

The tools pin the whole raw body and all four relocation records before
normalizing. The recipe folds the mapping ADDIU into indexed LW, moves
independent address/counter setup, exchanges closed row/node lifetimes,
renames temporary roles and peels the existing tag load into a likely delay.
Copy existing node-advance instructions, including the dead word; recompute
all relative targets. Move the existing final return delay to the expanded
body. No source stub or literal retail-body injection.

Raw table HI/LO are at 8/24 and mapping HI/LO at 12/20. Fitted table HI/LO are
at 8/12 and mapping HI/LO at 24/32. Preserve the complete previous guard prefix.
The actual ordinary mixed-owner Make recipe runs five commands under normal
O2/g3. All 33 compact functions and the complete padded object agree with the
independent qualification. All 32 neighbors/pools, including six handwritten
routines, retain their bodies, addresses and extents. No new GLOBAL_ASM.

The complete independent ELF prediction changes **151 bytes: 140 target-code
bytes and 11 metadata bytes**, with **zero exclusions**. Metadata is the
target extent 12->176 and one closed symbol/string ordering swap:
D_80095BCC and D_8009EFCC. Validate their old definitions, spellings and
contiguous spans, then reconstruct the complete record/string permutation.
It accounts for six symtab and four strtab bytes; do not mask them.

Expected/predicted ELF SHA-256:
`edba3f330f4c4e2cc2606b9152a3643dacce779ea73647c7c18de2a2c890a0e9`.

Production Make exits0 and reproduces that exact prediction. All 6,054 other
linked bodies and every address remain unchanged. Both tools copies pass all
eight fresh installed checks, no skips or reused checks. Native adoption
verifies all 16,006 files before/after and permits exactly four overrides:
source,guards,targetobject,ELF. Fresh native ELF bytes are captured and
streamed back for an independent progress recount, not inferred from an
isolated candidate. Init 492/492 and Debugger 181/181 remain unchanged.

Native target-object SHA-256:
`0798327c021a7371a18699b9a162418de6da12c285ab9d5ed6cde40aff8c7895`.

## Focused Qualification

Permanent tools: `tools/experiments/game_four_head_lookup_match.py` and
`tools/tests/test_game_four_head_lookup_match.py`.

- Eight fresh checks in each tools checkout before and after installation,
  no skips, with zero reused checks.
- 6,336 guest cases: every key byte, byte-corner hits, high incoming homes,
  shared heads/tails and six alias layouts, including deliberate SP/node,
  mapping and selected-head collisions. Fitted complete private state agrees
  with retail. Raw C guest execution is checked for public effects, not
  asserted to have retail's private allocation or portable C fault order.
- All 43 reachable retail words visited. The unreachable index 31 is preserved
  by complete word/binding equality, not falsely counted as executed.
- 1,792 original-caller cases, all key bytes, signed short values 1/8000/FFFF,
  enable/busy early exits, NULL spin and explicit continuation boundary.
- Native32 O0/O2/O3 with trap UBSan: 9,216 positive cases per profile and
  eleven effective semantic controls. Typed pointer/byte interface and
  read-only table/node contents checked. Guest home aliases are not claimed
  as portable native stack behavior.
- 89 emitted-guest access-fault prefix pairs, mandatory next load on hit,
  effective skipped-load negative, and invalid-next miss fault.
- Six independent GNU links across three code/data layouts, including HI/LO
  carry boundaries. Effective compiled-MIPS row-major-priority negative.
- 43 raw-word, eight binding, two extent, two real-padder and one guard-history
  controls. Six strict-image corruptions include both symbol and string
  metadata, not only code.
- Shared project checks pass independently in both tools checkouts.

Development fixture fixes were not production changes: GDB located native
O2 MOVAPS failure at a misaligned freestanding harness stack; use the existing
`-mstackrealign` pattern without weakening UBSan/warnings. Separate the
normal node pool from the oracle's default stack. Initialize the shared oracle
with legal phase 0/8, then explicitly set both live and saved SP for deliberate
aliases. Rerun all eight checks after those fixes.

## Closure And Continuation

Capture 36 focused inputs and all 1,454 linker objects within the 16,002-file
baseline. Adding only the two task files to both tools copies gives 16,006
sealed native/cache files. Preserve every one of the older mirror's 1,630
pre-existing dirty paths/statuses/hashes and HEAD; its only additions are the
two owned task files. Never commit/reset/revert that independent dirty tree.

Keep source/guards/object/ELF adoption restricted to four audited overrides.
Protected Game data must remain 720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The preliminary, explicitly uncredited source/profile work is banked in
[Note 1709](1709-four-head-lookup-private-normalization-20261024.md).
The installed predecessor is [Note 1708](1708-linked-record-event-match-20261024.md).
Ignored receipts and checked stdin bridges live under
`conker/build/game-four-head-lookup-match/`; use the verified PSBBN
cache, not DrvFS project reads. The actual native-ELF recount is complete. The ELF-pinned queue retains
1,590 placeholders, 120 semantic/other definitions and nine parser-unlocated
entries; these are source-shape screens, not qualification. Next audit
`func_1517CFC4`; `func_1510D8C0` already has semantic C despite the parser miss,
and `func_15014094` remains a separate existing-C matching task. Keep the
wider 75% goal active.
