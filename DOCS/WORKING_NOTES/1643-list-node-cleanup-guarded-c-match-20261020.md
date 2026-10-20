# List Node Cleanup Guarded C Match

Date: 2026-10-20. Consumer predecessor: `aec7db94`; tools predecessor:
`7aa7932`. Tools **ac05ac7** are committed first. No push.
The **75% total C-matching objective remains active**, not complete.

## Recovered Routine

Replace `func_1514D310`'s false zero-return placeholder in
[generated_179F30.c](../../conker/src/game/generated_179F30.c) with the complete
list cleanup. Preserve the address-based name, add a purpose comment and
reuse the existing private `GameListNode` layout.
VA **1514D310..1514D3B0**, ROM **17A7C0..17A860**,
**40 words / 160 bytes**, **48-byte frame**, five bindings, normal **IDO O2/g3**.

Read the head at owner+0x2F4. Cache each successor **before** either call.
Use the node's signed halfword at +0x1C to select a descriptor through
`D_8008ABE8`, then read its signed callback halfword at +2. Skip **only -1**,
not every negative value. Otherwise call `D_8008AB58[callback]` with the
node's +0x10 payload word. Remove the node with `func_1516972C` and continue
through the cached successor. Return **exactly one**, including the empty list.
The routine itself does not explicitly clear the owner's head.

The empty path never reads either table. Payloads remain late per-node reads;
callbacks/removal can change a later payload or redirect the live list links.
Correct this owner's old unprototyped `s32 func_1516972C()` declaration to
the actual `void` return. Qualify all other owner functions after that change;
do not change shared headers or claim a universal cross-TU object layout.

## Five Closed Guards

The C already has the original length, frame, saved-register lifetime and
loop. Raw C has five differences: descriptor-base and -1 roles use S2/S3
opposite to retail, with a three-word pure setup rotation. Normalize only
the following expected words/bindings:

| Offset | Expected C Word | Retail Word | Binding Change |
| --- | --- | --- | --- |
| 0x2C | 2413FFFF | 3C130000 | none -> HI16 descriptor table |
| 0x30 | 3C120000 | 26730000 | HI16 -> LO16 descriptor table |
| 0x34 | 26520000 | 2412FFFF | LO16 -> none |
| 0x44 | 024FC021 | 026FC021 | none |
| 0x50 | 10530006 | 12420006 | none |

The **40 instruction origins are bijective**: retail setup indices 11/12/13
take raw origins **12/13/11**. Close the S2/S3 role cycle and commute the
equality operands. No instruction is omitted, inserted or duplicated.
The descriptor HI/LO pair moves coherently; preserve all five final bindings.
This is **guarded semantic C**, not compiler-only byte-exact output.

Comparison reversal, conditional do/while, wider callback, alternate read
order, named sentinel, declaration order, local table and descriptor-local
screens do not improve the accepted direct fit. No dummy locals, physical
register binding or compiler-profile change is installed.

Preserve the complete old working-tree manifest prefix, SHA-256
`36513f2bad7fd30dbf191f428a3e0d154726fa4e9bfb619d5f0a36bda28987ae`.
Append only the five certified rows; no line-ending normalization.

## Focused Qualification

[The module](../../tools/experiments/game_list_node_cleanup.py) freezes 15
source/header/assembly/table/image/build inputs.
[Eight tests](../../tools/tests/test_game_list_node_cleanup.py) pass in both
tools copies, before and after installation, with no errors/failures/skips:

| Stage | Primary | Older Standalone Mirror |
| --- | ---: | ---: |
| Before installation | 184.581s | 202.323s |
| Installed source | 221.602s | 230.494s |

- **307 cases / 614 three-way final-state phases** compare original, raw-C
  and guarded-C behavior. All 40 target words execute. Guarded call-time
  private roles agree with retail; raw C has different private S2/S3 roles
  in 598 phases while preserving public behavior and final modeled state.
- Verify all **28 non-NULL descriptor entries** and all **three callbacks**
  against pristine ROM. Include empty lists, poisoned/replaced links, head
  mutations, late payload/descriptor changes, stack alignments and clobbers.
  Three signed-negative index cases are **guest-only**, not native C bounds
  guarantees.
- **304 native32 cases**, O0/O2/O3 with trap UBSan, exercise actual node layout,
  typed callback dispatch, exact returns, traces and fences. **Nine compiled
  semantic negatives** reach rejection23. No native negative-table-index or
  broad pointer-object portability claim.
- **25 guard controls** fire all five sites, including actual padder rejection
  of wrong expected words and relocation identities. Omissions preserve real
  mismatches. Check the complete old manifest prefix byte-for-byte.
- Three independent GNU HI/LO/call rebases pass **48 phases**, including signed
  LO16 carry cases; both fitted and original relocation-bearing objects are
  linked independently.
- Scan all direct JAL sites and aligned ROM words: one direct call from
  `func_15060F28` at **15060F40**, no literal function pointer. Execute the
  original **eight-word opening window** through the child in **28 phases /
  84 fired join boundaries**, stopping at **15060F48**. Preserve parent
  frame32, saved S0/S1 and return. The complete **176-word parent is not run**.
- Execute all **27 original callback words** in four phases, then all
  **28 removal + 20 registry + eight release-wrapper words** in **96 phases**.
  Include kinds 0/1/2/255, signed-byte registry counts 0/3/128, duplicate
  registry slots and NULL/non-NULL destructors. Lower payload, allocator and
  destructor calls remain bounded providers.
- **Nine strict-image negatives** reject code/header/protected-data changes,
  wrong target extent, changed swapped-symbol value/string and image length.
  Both shared tools smoke checks pass. Hardware/FCSR/MMU, invalid-memory
  domains and full parent/gameplay/host acceptance remain separate.
  Routine task: **zero Claude calls**.

The preflight refined signed LB/SLT support only in the new oracle and isolated
the target for independent GNU rebases to avoid unrelated owner externals.
The final suite reads fitted instructions from the actual independent linked
ELF and asserts the actual padder's output, rather than synthesizing fitted
code from truth. These fixture refinements are not production fixes.

The older mirror stays at **ddbdd16**. Preserve all **1,498** pre-existing
dirty statuses/hashes; add only the two absent task files, verify both copies
byte-identical and all four Python files AST-valid. Final dirty count **1,500**.
Do not commit/reset/stash/clean that independently dirty checkout.

## Installation And Progress

Preserve **77 other raw/padded owner functions**, bindings, pools and inherited
diagnostics. The three productive actual Make commands use normal O2/g3,
and their raw/padded code and metadata equal the independently qualified
objects. After proving the single-owner guard suffix, reuse unaffected objects:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

The first command rebuilds the changed owner and performs the complete link.
The `-o` flag acknowledges proven unchanged manifest dependencies for other
owners; no compiler flags, Makefile or timestamps are changed. Unrelated
owners are not claimed freshly recompiled. A later ordinary Make may rebuild
more objects because the manifest is newer. Broader unchanged suite receipts
are reused through the strict source/prefix/whole-image proof, not fresh reruns.

Production succeeds in **1,248.271s**, delayed by mounted-filesystem I/O.
It reproduces the strict independent ELF prediction:
**168 changed bytes = 127 code + 41 metadata**, target extent **12 -> 160**,
**zero metadata exclusions**. Account for the exact two-entry GNU symbol/string
bucket permutation of `D_8008ABE8` and `func_1503DF48`, preserving their values,
binding fields and the complete bucket extent. No metadata region is masked.

All **6,055 other bodies**, **6,056 addresses**, and **189,088 protected
Game-data bytes / 720 owners** remain fixed. ROM, original assembly/tables,
shared headers, Makefile and progress CSV are byte-identical. The four inherited
pointer/integer compiler warnings in other owner functions, duplicate
generated_12D630 recipe warning and Git's manifest CRLF/LF notice remain.
Do not call this warning-free or normalize the existing manifest.

ELF SHA-256:
`c582f2895c58e25fc86f1f818f8d4692d50a4a5c3db73514dea09186b7619918`.

Both installed suites pass. A direct invocation of the literal standard
Make matcher recipe and the independently refreshed ELF-pinned queue agree:
**3,708/5,505 exact (67.36%)**, Game **3,035/4,832 (62.81%)**,
**1,797 different / zero address drift**. Init remains 492/492; Debugger
181/181. Converted counts/bytes are unchanged. Threshold 4,129 leaves
**421** more matches. Queue source shapes: 1,663 placeholders, 125
semantic/other and nine unlocated. These are screens, not qualification
or permission to replace actual semantics with matching placeholders.

The Make matcher also passes in **512.160s** without rebuilding any object;
its table agrees with the direct recipe's **4.896s** recount and refreshed
queue. Recheck the unchanged image and all pinned inputs before committing.

## Next Target

The fresh queue next lists `func_15195698`, `generated_1C1150.c`:
VA **15195698..15195738**, ROM **1C2B48..1C2BE8**, **40 words / frame48**.
The original second pointer's unsigned bytes at +0x1CA and +0x127 gate the
eight-argument `func_15136C3C` call and following `func_15145A50` /
`func_1507CD64(..., 6)` calls. Independently, the first pointer's type byte
at +4 equal to 0x47 clears its own +0x1CA byte. Preserve original incoming
argument homes, late first-pointer reload and the actual return contract.
Graphify query and full retail-body inspection are read-only screens, not
ABI/C qualification. No draft, installation or matching credit. Keep the
862-word `func_1508CAD8` owner stub separately queued.
