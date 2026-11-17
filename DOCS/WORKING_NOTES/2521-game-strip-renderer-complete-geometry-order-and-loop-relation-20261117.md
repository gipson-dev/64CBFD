# Strip renderer complete geometry order and loop relation - 2026-11-17

Private `func_151AD92C` now agrees with retail on **all 306,846 ordered FP
observations across 544 cases**. Both coordinate bases and all twelve coordinate
stores participate in a **complete generic geometry-sample relation**. Four
entry paths establish the loop invariant; eight generic paths advance it or
reach display-list setup. This advances
[Note 2520](2520-game-strip-renderer-first-basis-schedule-and-generic-relation-20261117.md).

The complete function remains private and uncredited. Accepted progress stays
**4,533 / 5,514 (82.21%)**, Game **3,860 / 4,841 (79.74%)**, Init 492/492 and
Debugger 181/181, zero drift. The active 85% goal needs **154 more matches**.
Root README, production source/guards and production ELF are unchanged.

## Second-basis recovery

Owner `conker/src/game/generated_1D92F0.c`, VA151AD92C..151AE06C,
ROM1DADDC..1DB51C. The selected C remains v49: **469 words / frame 0x130**,
against **464 retail words / frame 0x130**. Raw SHA256 remains
`0418af51e8fc3f1b5c9632de208a59f57b41e57a8844f365c690a2e47ebbb6c1`.

The derivation retains Note 2520's first-basis transformation. For the second
basis it closes the F12/F14/F16/F18 allocation cycle, then caches current Y
and Z in the now-dead reciprocal/norm registers. Explicit operand edits assign
each plus/minus result and truncated coordinate its corresponding temporary.
Existing source instructions are rescheduled into the original combined
FP/store order. The source-order list is a checked partition: only two redundant
private Y/Z reloads and two existing NOPs leave the scheduled body. Four vacant
NOP slots are temporarily retained before the loop branch, preserving 469 words
and every branch word/position while this private transformation is qualified.
No retail instruction range is copied and no production normalization is added.

A pinned SHA256 checks the entire second-basis source region before any edit.
Bit corruption at every checked first-basis anchor and every word of that
second-basis region makes derivation fail closed. The C body, compiler profile,
callback ABI, eleven provider arguments and SDK graphics macros are unchanged.

## Complete geometry relation

The **four entry paths** cover both texture shifts and empty/nonempty geometry.
They compare all 320 private/incoming-home bytes, public state/read multisets,
ordered effects and FP condition/status, and establish the required geometry
roles, zero index/byte cursor, saved zero/four and captured count/width.

The **eight generic sample paths** cover terminal/nonterminal tangents and both
norm fallbacks. Four reach the next sample and four reach display-list setup.
For `0 <= sample < count <= 20`, they compare:

- Every one of the **320 private/incoming-home bytes** and all public bytes.
- The **combined ordered public-store/FP trace**, including abstract status and
  condition changes; store ordering is not separated or weakened.
- Stable public-read multisets and required live scalar/pointer/FP roles.
- At the backedge, index advancement, the 24-byte point cursor, and retail's
  separately maintained next index, establishing the next iteration's invariant.

Other FP temporaries are independently dead at the row entry. The relation uses
mapped, disjoint, stable objects and nontrapping FP; it does not establish
arbitrary aliases, literal faults, cycle timing or the provider/suffix boundary.

An independent T6/T7 allocation passes entry and generic relations. Four
effective controls reject a wrong cached-Z home, wrong point stride, incorrect
index in the branch delay slot, and inverted loop backedge. Unsupported or
unbounded execution does not count as a successful control rejection.

## Fresh qualification and preserved state

All **five tests pass in both tools configurations**, with zero failures, errors
or skips: **206.941s primary / 115.484s sibling-overlay**, including fingerprint
and actual-import recording. The shared engine bindings are restored afterward.

- Full owner compilation preserves all **32 neighbors** and normalized pools,
  with the selected raw bytes and relocations pinned.
- Retail/raw/derived each pass **544 complete finite executions** for public
  memory, all eleven provider arguments, return cursor and saved GPR/FPR values.
  Coverage is 464/464 retail and 469/469 raw/derived. The derived stream agrees
  on the full ordered FP trace in all 544 cases, replacing the previous
  first-basis-only result.
- Complete original caller/selector execution passes **64 literal descriptor
  cases per stream**. Caller coverage is 282/348 words; the selector remains 47
  words. Signed viewport forwarding and budget rollback are checked. No new
  synthetic alternate-layer coverage is claimed.
- Seven unchanged native32 binaries execute fresh after source/binary/fixture
  hash checks: selected C at O0/O2/O3 and four rejecting controls. Compilation
  remains explicitly reused from Note 2519; there is no native FP-status claim.

The **1,542-input** snapshot links 1536 preceding immutable files and copies the
six newly banked first-basis tool files. All frozen/live hashes agree, with zero
live-worktree hardlinks. Primary imports have 347 rows/345 unique tool files;
sibling-overlay has 349 rows/347 unique files: six overlay, 301 sibling and 42
primary rows. The sibling's 2434 dirty paths and 339 present scoped dependencies
remain intact. Production ELF SHA256 remains
`9a3fca4a18c45119a77ad987895ba93c8f600ab46acbad5513147499567074b3`.

## Remaining private-state and adoption work

Complete RAM and provider-frame agreement still hold in **0/544 cases**. A
separate four-case diagnostic at counts 0/1/3/20 identifies exactly three
provider words: raw saves captured count at SP94; retail leaves that slot intact,
saves count at SP124 and the zeroed segment index at SP128. The later UV loop also
needs its private homes and live roles qualified. Four source-only cursor/UV
variants preserve neighbors/pools but do not improve the selected match: they
remain private, with no credit or adoption.

Continue with those provider homes, the opaque-call boundary and the generic UV
backedge/return relation. Resolve the five-word excess, including the four
temporarily retained vacant slots, before both padders, relocation rebases,
actual Make, strict whole-image comparison and production recount/adoption.

Evidence is retained under
`conker/build/game-next-151ad92c-private/geometry-qualified/`; private geometry
and provider diagnostics are in `second-basis-v49/`. The normal Graphify update
refused a smaller graph; a scoped four-file AST merge retains old IDs and records
the target reference. This is not full-corpus re-extraction. Commit tools before
consumer notes/pin, locally only. No host-port or frozen Release changes occur.
