# Context Node Search Guarded C Match

Date: 2026-10-20. Consumer predecessor: `d4d30f47`; tools predecessor:
`8061257`. Tools **d106360** are committed first. No push.
This goal turn makes verified progress. The wider **75% total C-matching
objective remains active**, not complete.

## Installed Recovery

Replace the false zero-return `func_151CE634` placeholder in
[generated_1FA770.c](../../conker/src/game/generated_1FA770.c) with the complete,
purpose-commented, read-only search, retaining its original name and pointer
return. VA **151CE634..151CE6D0**, ROM **1FBAE4..1FBB80**.

This is **guarded semantic C, not compiler-only output**:
normal **IDO O2/g3 emits 41 words**; **41 expected-word/relocation rows**
normalize the complete **39-word / 156-byte / frame-zero retail slot**.
No compiler profile, Makefile, shared header or original assembly is changed.

For phase 0 then phase 1, load the selected column, scan row 0 then row 1,
and traverse each list through node +0x08. Require the complete signed word at
node +0x20 to equal **11** before following its payload pointer at +0x98.
Compare the payload's context word at +0x48 with the opaque input context.
Return the **first matching node pointer**, otherwise NULL. There are no
helper calls or memory writes in the target.

The original global column values are **77 and 34**. The fixed table has two
416-byte rows, 104 four-byte heads per row, from **800DCE50 to 800DD190**.
Qualification also exercises legal columns 0/103, reversed/duplicate columns,
shared heads and payloads, NULL contexts, nonmatching full-width type words,
and empty/longer lists. Payloads must be valid when the type equals 11;
non-type-11 nodes may have NULL payloads and must be skipped.

## Closed Normalization

The ordinary loop, declaration, pointer-view and no-unroll screens did not
close the two-word difference. Corrected alternate-source hints also remained
non-matching; do not adopt its incorrectly scaled pointer expressions.
The optional advisory client was signed out: **zero model calls**, no account,
configuration or dependency changes.

[The integration helper](../../tools/experiments/game_context_node_search.py)
pins the full 41-word input SHA-256 and all six data bindings. Its explicit
semantic origin ledger maps every retail word to a compiled C operation:

```text
Retail Word -> Compiled C Word
 0.. 9:  0, 1, 6, 7, 8, 9, 2,10,11, 3
10..19:  4,14,15,16,18,17,20,21,22,23
20..29: 24,25,26,27,28,29,30,31,17,32
30..38: 33,12,34,35,36,37,38,39,40
```

All **38 unique retained origins** are accounted for. The remaining three
source words are closed folds, not discarded semantics:

- **Word 5:** fold the table-base LO16 add into the indexed load's displacement.
  Preserve both symbolic bindings and signed HI16/LO16 carry behavior.
- **Word 13:** coalesce the hoisted base-to-row copy. Rematerialize the immutable
  row base at each phase; preserve the same row/head addresses.
- **Word 19:** remove the head-test delay NOP. Split **word 17**'s row advance
  onto the empty-head delay edge and the continuing nonempty-list edge.
  The head BEQ becomes BEQL so only the proper edge executes its advance.
- Move the early local phase increment to the retail latch. During a row scan,
  the raw compiler's phase temporary is one ahead; it is used only at the next
  phase/latch, or overwritten with the returned node on success.
- Map the scoped context/node/row/column/payload/type/end register lifetimes.
  On early return, unused cursor values may differ in raw C; returned pointer
  and ordered reads remain identical. Normalized code is literally retail.

CSV rows are physical emission slots; the origin ledger is the separate
semantic provenance map. Three omitted input slots plus one inserted output
slot give **41 - 3 + 1 = 39**. Every input word, including the unused NOP and
unreachable next-link load, has an expected-word and relocation check.

Append only these 41 rows to
[the existing manifest](../../conker/retail_word_patches.us.csv). Preserve its
entire previous working-tree prefix, SHA-256 **7ca8a25f...**, byte-for-byte.
The resulting working-tree SHA-256 is
`7ccd028cda1fdbe5f212c315aa649188f3b88f72b7003cf5573eb5c01d048115`.
The existing Git CRLF-to-LF advisory remains; no line-ending rewrite was
performed, and the staged manifest diff adds exactly 41 rows.

## Final Address Form

The final unused column advance is expressed as
`(void **)((u32)column + 0x1A0)`, rather than pointer arithmetic beyond the
head table. This is an explicitly qualified **flat 32-bit address operation**,
not a portable arbitrary-host pointer conversion. The row end remains the
actual one-past table address; no out-of-range column is dereferenced.

Before the final source update, recompile and compare **all 52 raw owner
functions and their bindings/pools**: every instruction remains identical.
Re-run the full seven-test candidate suite in both copies with the installed
prior image independently audited. The final source form then receives its
own production rebuild and installed tests. Historical input pins are not
advanced to accept the change.

## Qualification

[Seven focused tests](../../tools/tests/test_game_context_node_search.py)
pass in both tools copies, with no errors, failures or skips:

| Stage | Primary | Standalone Mirror |
| --- | ---: | ---: |
| Initial candidate qualification | 12.421s | 12.232s |
| Final address form, before source update | 14.405s | 34.680s |
| Final installed source | 29.233s | 34.887s |

- **391 cases / 782 three-way phases** compare original, raw C and guarded
  execution with an independent first-match/read-order reference.
  There are **646 successful-return phases**. Raw C agrees on all reads,
  unchanged memory and returns; guarded code agrees on full modeled state.
- Execute all **38 reachable retail words** and **40 reachable raw words**.
  Retail word **25** and raw word **29** are the preserved unreachable
  next-link loads after the early return; do not claim all words executed.
- **389 native32 cases**, O0/O2/O3 with trap UBSan, check typed head/node/payload
  layouts, legal column domains, NULL contexts, sharing, first-match priority
  and read-only byte fences. The two NULL non-type payload probes are guest-only.
  Native end-marker aliases qualify the fixed table-size contract, not
  arbitrary placement of distinct host globals.
  The source remains a low-level flat-address view; native tests use the
  prepared -m32/-fno-strict-aliasing ABI, not a portable ISO-C layout claim.
- **Eight compiled semantic controls** reject wrong type, context sense/offset,
  next link, phase ordering/count, row count and discarded result.
- **41 word mutants and six binding mutants** trigger the actual guard
  checks for this target, not an earlier setup error.
- Three independent global rebases, preserving the required base/end distance,
  pass **51 phases** with raw, original and guarded code. Include signed LO16
  carry cases and all six data bindings.
- Full pristine function scan finds one direct JAL:
  **func_151CE51C at 151CE528**. The actual delay slot forwards +0x18 from A1.
  **42 caller-window phases / 126 executions** check context forwarding,
  pointer return and its SP+0x38 save. **96 positive boundaries actually fire**
  at the later position helper; NULL results complete the caller's zero path.
  The positive remainder of the 70-word caller is **not** executed or claimed.
- Seven strict image controls reject unrelated header/code/data, symbol-size,
  truncation and appended-byte changes.
- Both shared tools checks pass; all four Python copies parse and agree.
  Preserve all 1,486 older mirror dirty paths/statuses/hashes and its ddbdd16
  HEAD; only the two absent task files are added, leaving 1,488 dirty paths.

Raw private-GPR/fault-state identity, hardware MMU/FCSR, malformed memory,
unbounded corrupted-list termination, full positive caller behavior,
gameplay and host-port acceptance are separate. This recovery does not add
defensive behavior absent from retail.

## Production And Progress

Preserve all **51 other raw/padded owner functions**, pools and inherited
diagnostics. The actual plain-C owner uses **three productive Make commands**.
The guard-triggered wider build passes in **269.689s**; the final address-form
rebuild passes in **87.715s**. Both produce the same strict predicted ELF:

- **126 changed bytes**: **125 instruction bytes** plus **one size byte**,
  target extent 12 to 156. **Zero metadata exclusions**, no new overflow.
- All **6,055 other linked bodies**, **6,056 addresses**, and all
  **189,088 protected Game-data bytes / 720 owners** remain fixed.
- ROM, original assembly, variables header, Makefile and progress CSV remain
  byte-identical. The guard manifest changes only by the certified suffix.
- ELF SHA-256:
  `b0d56898304dc5a82310a458eaf388663b05b86e4b14d5f6f8c5ab3d9ecd8dda`.
- The known duplicate generated_12D630 Make recipe warning remains.
  Unchanged broad neighbor-suite receipts are reused through the complete
  image proof, not described as fresh reruns.

Fresh full matcher: **3,702/5,505 exact (67.25%)**, Game **3,029/4,832 (62.69%)**,
**1,803 different / zero drift**. Init remains 492/492; Debugger 181/181.
The current 75% threshold is 4,129: **427 more matches** remain.
The refreshed ELF-pinned queue has **1,669 zero-return placeholders,
125 semantic/other definitions and nine unlocated entries**. It is triage,
not permission to install unqualified code.

Next **func_150CA930**, VA 150CA930..150CA9D0, ROM F7DE0..F7E80:
a **40-word/frame-64** wrapper submits a point after integer/float RNG calls.
Qualify unsigned modulo-21 plus 10, signed-short storage, float32 scale
59*random+170, point reload timing, twelve-argument floating ABI, actual
func_1514C678 return/interface, callers, full owner and image.
It remains **queued, uninstalled and uncounted**.

Keep root README updates aggregate-only; detailed progress belongs here and
in concise indexes. Commit tools before the consumer pin; no push. Verify
the existing post-commit Graphify hook's terminal processes and node retention
in the ignored final checkpoint. No host source, save, configuration or
frozen Release artifact is changed.
