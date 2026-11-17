# Strip renderer first-basis schedule and generic relation - 2026-11-17

Private `func_151AD92C` now has a checked first-basis instruction schedule.
Its relation covers **18 paths from entry** and **eight paths for an arbitrary
entered sample**, through all six first-basis coordinate stores and the second
norm branch. All **194,991 first-basis FP observations** agree across the
544-case matrix. The complete renderer remains private and uncredited.
This advances [Note 2519](2519-game-strip-renderer-float-lifetimes-and-symbolic-opening-20261117.md).

Accepted progress remains **4,533 / 5,514 (82.21%)**, Game
**3,860 / 4,841 (79.74%)**, Init 492/492 and Debugger 181/181, zero drift.
The active 85% goal needs **154 more matches**. Root README is unchanged.

## Checked transformation

Owner `conker/src/game/generated_1D92F0.c`, VA151AD92C..151AE06C,
ROM1DADDC..1DB51C. Selected source remains v49: **469 words / frame 0x130**,
against **464 retail words / frame 0x130**. Its raw SHA256 remains
`0418af51e8fc3f1b5c9632de208a59f57b41e57a8844f365c690a2e47ebbb6c1`.

The derivation first applies the six previously qualified scalar-home operand
edits. It then reschedules existing first-basis instructions to recover the
retail combined FP/store order. The second-norm addition explicitly changes
its operand order to the retail order; arbitrary FP commutativity is not assumed.
Two vacated NOP slots balance the moved tail instructions. Length stays 469,
and every original branch word and position is unchanged. A non-NOP instruction
inventory check permits only the declared home edits and addition operand order.
No retail instruction range is copied and no production guards are installed.
Corrupting any checked source anchor makes the derivation fail closed.

## Symbolic scope

The entry relation has eight second-zero paths, eight second-nonzero paths and
two empty paths. The generic relation assumes `0 <= sample < count <= 20`
and relates an arbitrary entered sample to the same second-norm boundary.
Both compare every **320 private/incoming-home bytes**, ordered public stores
interleaved with abstract FP operations and status changes, stable public-read
multisets, public bytes, FP condition/status and required live roles.

The generic invariant supplies the corresponding sample indices, byte cursors,
captured count/width, output/record pointers, bank/table addresses, saved zero
and four, and an arbitrary shared incoming FP status. Other incoming FP
temporaries are dead independently on each side. The completed-store address
role is decoded from the actual delay-slot store, allowing an independent
T6/T7 allocation to pass both relations.

Five effective controls reject reversed norm-add operands, a wrong point stride,
a narrowed viewport home, a branch-likely annulled coordinate store and an
independent X subtraction moved before the Z addition. The viewport control
applies at entry; the other four reject in both entry and generic relations.
No unsupported-instruction failure counts as a successful rejection.

This is a mapped, disjoint, stable-memory, nontrapping-FP relation. It does not
prove the second basis, row backedge, arbitrary aliases, literal fault state,
cycle timing or complete provider-frame equivalence.

## Qualification and preservation

All **five tests pass fresh in both tools configurations**, with zero failures,
errors or skips: **115.117s primary / 92.514s sibling-overlay**, including input
and imported-helper fingerprinting.

- Full owner compilation preserves all 32 neighboring functions and normalized
  pools, and pins the selected raw bytes and relocations.
- Retail, raw and derived streams each pass **544 complete finite cases** for
  public memory, eleven provider arguments, return cursor and saved registers.
  Coverage is 464/464 retail and 469/469 raw/derived. Every sampled first-basis
  FP sequence agrees with retail; second-basis order is not claimed.
- The complete original 348-word caller and 47-word selector pass **64 literal
  descriptor cases per stream**, including signed viewport forwarding and budget
  rollback. The derived stream has not added the earlier separately labeled
  synthetic alternate-layer cases.
- Seven unchanged native32 binaries execute fresh after checking binary, source
  and fixture hashes: selected C at O0/O2/O3 and four rejecting controls. Their
  compilation is explicitly reused from Note 2519, not reported as fresh. The
  selected C body and SDK inputs are unchanged; no native FP-status claim is made.

The **1,536-input** snapshot shares 1532 files with the preceding immutable
snapshot and copies the four newly banked lifetime-tool files. Every frozen
and live input hash agrees, with **zero live-worktree hardlinks**. Actual import
records contain 344 rows/342 unique tool files in primary; sibling-overlay has
346 rows/344 unique files: seven overlay, 301 sibling and 38 primary rows.
The sibling's 2434 dirty paths and 339 present scoped dependencies remain intact.
Production ELF SHA256 remains
`9a3fca4a18c45119a77ad987895ba93c8f600ab46acbad5513147499567074b3`.

Evidence is retained under
`conker/build/game-next-151ad92c-private/basis-qualified/`: both qualification
directories, import/suite receipts, immutable inputs and `qualified-checkpoint.json`.
The normal Graphify update refused a smaller replacement and retained the old
graph; the scoped AST refresh retains old IDs and records the target reference.
This is not full-corpus re-extraction. Tools are committed before consumer
notes/pin, locally only. No host-port or frozen Release changes are involved.

## Next work

Recover the second-basis FP/store schedule and private state, then prove the
generic sample backedge and complete provider boundary. Resolve the five-word
length excess before both padders, relocation rebases, actual Make, strict
whole-image comparison, production recount and adoption. The source placeholder
and accepted match totals remain unchanged until those gates pass.
