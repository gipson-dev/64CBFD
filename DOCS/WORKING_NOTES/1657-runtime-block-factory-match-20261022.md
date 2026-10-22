# Source Runtime-Block Factory Guarded C Match

Date: 2026-10-22

## Result

Restore `func_15189FF0` in `conker/src/game/generated_1B74A0.c` as
complete, purpose-commented C with the recovered pointer return and seven
arguments. All **41 linked words/frame56/two bindings** match retail.
The normal O2/g3 compiler emits **40 words**. Two expected-word guard rows
restore the redundant null-return branch and its success-path join. This is
**guarded semantic C, not a compiler-only 41-word match**.

VA15189FF0..1518A094 / ROM1B74A0..1B7544, ends exclusive.
Raw unlinked C body SHA-256:
`66d5f697d6fd3e6b0bdcb92d03c8c49b47905c5369cba1056c0898f26a853998`.
Keep the reference `conker/asm/1B74A0.s`, existing build profile, shared
headers and all five neighboring functions unchanged.

## Recovered Contract

Use `u8 *func_15189FF0(u8 *descriptor, u8 *source, const void *runtime,
u8 kind, u8 mode, u8 first, u8 variant)`.

Set source-record byte +0x58 to 0x0B unconditionally, before allocation.
This argument is a source record, not an actor pointer; the prior static
screen's actor label is corrected in Note 1656.

Call `func_151407D0(source, 0x80, descriptor, kind, mode, first, variant,
-1, 0xFF, 1)`. The first size is 128 source bytes, not a resource ID.
On success, copy all 32 runtime bytes to object+0x170 and return the
allocated object base. Do not return memcpy's destination, skip reserved
bytes, initialize them independently, or copy on allocation failure.

Preserve the full incoming homes for the first four arguments before
narrowing kind. The other three inputs are low-byte reads from their
incoming stack words. Retain the runtime pointer across the factory call
and the allocated pointer across memcpy at current SP+0x34. The original
null path preserves incidental V1; complete machine comparisons include it.

Use an owner-local ten-argument factory declaration matching its actual C
definition, and `size_t` for memcpy's size on both N64 and native32.
No current C parent calls this target, so no unrelated caller prototype edit
is needed. Existing neighboring C bodies, bindings, pools and diagnostics
remain identical; diagnostics are empty before and after.

Bindings relative to the target body:

| Offset | Kind | Symbol |
| --- | --- | --- |
| 0x60 | R_MIPS_26 | `func_151407D0` |
| 0x78 | R_MIPS_26 | `memcpy` |

## Closed Return Join

Preserve every raw compiler word in order except one branch displacement:

| Raw Offset | Expected | Replacement | Insert After |
| --- | --- | --- | --- |
| 0x84 | 0x10000002 | 0x10000003 | None |
| 0x88 | 0x00601025 | 0x00601025 | 0x10000001 |

The inserted word is a pure unconditional branch on the null path.
The existing conditional displacement lands on it; the following zero
return moves into its delay slot. The success branch advances by one word
to the same epilogue. No calls, argument values, payload accesses, register
assignments, relocations or other instructions are replaced. No words are
omitted, and there is no alignment filler or overflow trampoline.
Independently assembled original GNU code equals the normalized unlinked
body and bindings, not merely a sampled output.

Ordinary explicit-return, phi/conditional-return and local-layout probes
do not close the return join. The no-unroll profile emits the same tail.
Keep normal O2/g3 and use explicit return labels in the complete C body;
do not introduce dummy locals or a profile change to obtain a word count.
The original C spelling remains unknown.

Append exactly two structured CSV rows, retaining the entire prior manifest
byte prefix. Existing guards, including those of the helper, are unchanged.

## Caller And Helper Bounds

Execute original call windows at all six direct sites in `asm/179F30.s`:
1514D794, 1514D8E0, 1514E150, 1514E2D8, 1514E464 and 1514F0F8.
The first five forward the allocated result to `func_1514EC1C` with tags
9, 10, 6, 6 and 7; stop at that declared provider boundary.
The sixth preserves the result through its actual epilogue.

There are 24 caller-window phases across success/failure and SP phases 0/8.
Seed live inputs at each selected window boundary explicitly, including
the sixth window's descriptor/source/runtime addresses and temporary cursor.
These tests are not full-parent executions. Current parent C remains stubbed.

Connect the actual, already-exact 53-word `func_151407D0` and 11-word
`memcpy` for 32 phases. Execute all 64 helper words across the corpus.
The helper marks descriptor byte +1 as 3, ORs +0x40 with 0x40400000,
calls `func_1513D524`, copies 128 source bytes to object+0x110,
clears object+0x154, writes selector 0xFF at +0x169, and conditionally
increments `D_800DC9F0` with unsigned wrap.

The target's final 32-byte copy overwrites object+0x170..+0x190 within that
first copied range. Test sequential forward-byte overlap, descriptor/source
aliases and counter wrap. The nine-argument lower allocator remains a bounded
provider; no complete constructor, registration, hardware or gameplay
acceptance is claimed. Guest overlap/stack-alias fixtures are not portable
native memcpy or C-fault guarantees.

## Qualification

Tools: `experiments/game_runtime_block_factory.py` and
`tests/test_game_runtime_block_factory.py`, identical in both copies.

| Final Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 27.821s | 8 tests, 26.214s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 2.868s | 2 tests, 2.973s | 0 / 0 / 0 |

Explicitly reuse the other six checks per copy only under strict source,
raw/padded object, helper, input and full-image identity. They are not fresh
installed executions. Shared project-tool checks pass in both copies.

- 4,096 guest phases sweep every value of each of the four byte arguments,
  with poisoned upper bits, allocation outcomes, helper effects and SP phases.
  Another 96 phases cover guest input, forward-overlap and stack aliases.
- All 41 target words execute across the corpus. Verify full volatile GPR,
  FPR, HI/LO and argument-home clobbers, saved-register lifetime and V0/V1.
- 6,144 native32 cases per optimization at O0/O2/O3 use trap UBSan, real
  nonoverlapping source/destination objects and complete destination fences.
  All seven compiled wrong-C controls fail effectively.
- Six independent GNU links / 48 phases exercise both call relocations.
  Check 888 fired root-access fault prefixes, eight strict-image corruption
  controls and four raw-body/binding/guard rejection controls.
- Pin 28 historical/current inputs and the predecessor object. Preserve five
  owner neighbors, pools, diagnostics and addresses. The Make shadow uses
  its actual three productive commands and unchanged normal O2/g3 profile.

Initial failures were fixture defects, not accepted evidence: isolated input
was incomplete for the whole-owner padder; a mutation destroyed its own
runtime pointer in one intended alias; caller windows lacked live t8/t1
boundary values. Use the full owner, valid mapped aliases and explicit
window inputs, then rerun both complete suites. Final successful runs are
the table above; failed attempts are not counted as passing receipts.

## Production And Preservation

The old Linux cache was missing after the environment restart. Rebuild it
from 15,794 verified baseline files and reproduce the baseline ELF through
an independent cold GNU link. Add four new task-file copies and verify all
15,798 files, including all 1,454 linker objects, before qualification.
No dependency/provider installation or host-port changes are needed.

Actual production Make exits zero in 0.742s and exactly reproduces the
independent full-image prediction: **123 changed bytes = 122 instruction
bytes + one symbol-size byte**, zero exclusions or metadata permutations.
The inherited duplicate generated_12D630 Make recipe warning remains.
The CSV CRLF-to-LF Git advisory is not a compiler or matching failure;
the complete local prior-byte prefix is verified before adoption.

Installed ELF SHA-256:
`8ccd597559500389b092ed638e6e2b2e5f3c0ee996e4c792a35a5d7cec80d119`.
Installed owner object SHA-256:
`4c0f0f51514183db88a044bd7d3e9b7be5866e2d640d7e3bf873d4f65f8e0bd0`.

All other 6,055 bodies and all 6,056 addresses stay fixed.
Protected Game data remains exact: 189,088 bytes / 720 owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Recheck all sealed live inputs before/after adopting only the owner object,
ELF, generated linker script and progress CSV.

Tools commit `741c3259c3e55d3039af9aa86184894612c4df69` precedes the
consumer source/guard/docs/pin commit. Preserve all 1,526 pre-existing older
mirror dirty statuses/hashes; add only two task files, totaling 1,528 paths.
Do not commit/reset/clean/stash that mirror. No push or Claude call.
Host Release remains frozen. Root README changes only its snapshot date
and two aggregate rows. Refresh Graphify and explicitly audit retention
of old nodes and excluded-existing files at the committed checkpoint.

## Measured Progress And Resume

The literal standard matcher exits zero against the adopted live ELF:

| Section | Byte-Exact Converted C | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3,725 / 5,505 (67.67%) | 0 | 1,780 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,052 / 4,832 (63.16%) | 0 | 1,780 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The threshold remains 4,129; **404 more exact functions** are required.
The 75% goal remains unfinished. The refreshed ELF-pinned queue has 1,647
placeholders, 124 semantic/other definitions and nine unlocated entries.

Next: `func_1515D088`, 42 body words/frame64, already semantic but
37 words different. Source `conker/src/game_1897A0.c`, original
`conker/asm/nonmatchings/game_1897A0/func_1515D088.s`.
VA1515D088..1515D130 / ROM18A538..18A5E0, ends exclusive.
Screen its unsigned low-byte gate, original redundant signed-negative test,
12-byte payload with three untouched reserved bytes, eight-argument factory
and returned object across memcpy. Establish caller ABI and actual live
local/home layout before fitting. Screen only: no source change or matching
credit. Keep the 862-word `func_1508CAD8` owner stub queued separately.

Private snapshots, probes, fixtures, images, queues and audits live under
`conker/build/game-runtime-block-factory/qualified/`. Do not commit them.
