# Attached-strip position update guarded byte match - 2026-11-17

`void func_151AE3A8(u8 *input)` now replaces its false zero-return placeholder
with the complete attached actor/strip position update. Its **122-word /
488-byte slot and 0x78-byte frame are byte-exact in production**. Semantic C
emits 120 words; **107 relocation-aware checked guards and two insertions**
recover the original allocation and ordered FP schedule. No word is omitted
and no original instruction range is embedded in C.

The actual-ELF recount is **4,536 / 5,514 (82.26%)**, Game **3,863 / 4,841
(79.80%)**, Init 492/492 and Debugger 181/181, zero address drift and 978
still different. **151 further matches** are needed for the active 85% goal.
Conversion counts/bytes are unchanged. The root README gets two aggregate
matching-row updates; this note contains the function narrative.

## Source and interface recovery

Owner `conker/src/game/generated_1D92F0.c`, VA151AE3A8..151AE590,
ROM1DB858..1DBA40. The original has one incoming pointer and a void interface.
Its sole direct caller, the complete 13-word `func_151ACB60`, checks the child
record pointer before calling. That caller and its existing checked incoming
pointer store in the call delay slot remain unchanged.

The routine captures actor and strip record before its heading provider. It
narrows heading-minus-0x80 to a byte, calls the trig provider with angle-minus-
0x40 and then angle, and preserves the first result across the second call.
The local snapshot structure expresses the measured private layout: adjacent
point snapshots, captured actor/record, angle, first trig result, interpolated
Y and old Y/Z, with unused bytes left untouched. Initial scalar candidates
used smaller frames; the selected form recovers the complete 0x78-byte frame.

After all providers, the actor child, coordinates, input scale and progress
are read again. The saved record stays captured even if providers replace the
child's record pointer. The index uses truncation of 140/spacing, the count-
minus-quotient-minus-one span, and the progress product; its low byte is stored
at child+0xAE. The repeated count read/product, adjacent 24-byte point reads,
interpolation, heading-relative offsets and `(new-old)+old` coordinate updates
are retained, including their FP rounding behavior.

The private derivation explicitly exchanges three interpolation-add operands
and two independent FP scheduling pairs, then inserts two neutral schedule
slots. It does not assume floating-point commutativity. Independent instruction
execution and the complete symbolic relation compare the derived stream with
retail; the final guards and both padders emit the original bound body.

The separate donor has incorrect field widths and float/int loads, so it is
used only as a reference skeleton. It is not accepted as byte-exact source.

## Qualification and its limits

All **five final target checks pass in both tools configurations**, without
failures, errors or skips: **340.087s primary /
344.963s sibling overlay**. The complete owner compiles under its
unchanged O2/g3 profile, retaining all 32 neighbors and normalized pools.

- The instruction-driven relation covers the complete straight-line path,
  all **136 private/incoming-home bytes**, all three provider arguments and
  boundaries, ordered public writes/FP/status events, stable-read multisets,
  final public bytes and required GPR/FPR/stack/RA preservation. Providers
  can mutate public state, all four outgoing homes, caller-saved registers
  and abstract FP status. Captured locals retain their real lifetimes.
- An independent scratch-register allocation passes. Eight effective controls
  reject missing incoming storage, wrong actor/result/coordinate homes,
  wrong next-Z load and an incorrect restored frame.
- Retail/raw/derived each execute **2,560 guest cases**. Derived complete RAM,
  private/provider frames and all **71,680 ordered FP observations** agree
  with retail. Coverage is 122/122 retail and derived, 120/120 raw. Fixtures
  include all 256 angle bytes, high-word heading noise, counts 0..255,
  negative/high mapped indices, provider mutations, signed zero, NaNs and
  infinities. The interrupted earlier run is retained as partial evidence;
  the reported complete runs are fresh and finish normally.
- The complete original caller passes **256 cases per stream**, including
  attached and null-record paths, with all 13 caller words visited. Derived
  full RAM/private stack and FP events agree; a wrong callback pointer rejects.
- Native32 C is compiled freshly at **O0/O2/O3**, each passing **1,180 finite
  or signed-zero cases**. Four new controls reject wrong angle bias, next-Z
  stride, reloading a provider-mutated record, and using the wrong forward
  offset. All public regions and all three one-argument provider calls are
  compared. Native NaN/Inf payload propagation, private stack and FP status
  are outside this native claim; guest and symbolic checks cover FP ordering.

The symbolic domain is ordinary mapped, disjoint objects/private stack,
stable memory between calls/stores, valid index/conversion inputs and
nontrapping FP. This does not prove arbitrary aliases, literal fault-register
state, cycle timing, an entire gameplay path or host-port runtime acceptance.

## Padders, actual build and production image

Both real padders emit the independent original body and all three bindings.
Twelve independent GNU links use four code/data layouts and check the explicit
binding values, including owner-defined symbols when present. All old CSV
bytes remain intact; 107 new rows are appended with no retired guard.

Object controls reject **123 raw/binding
corruptions, 428 stale-CSV changes and
111 replacement/insertion changes**.
All 120 source-word corruptions reject before schedule derivation.

Five real Make commands build the independent complete-owner shadow. Production
Make then rebuilds source/object/ELF/progress; no prebuilt object is installed.
The strict whole-image prediction accounts for **394
changed bytes with zero exclusions**, with no metadata reorder groups.
Named definitions and four effective symbol/name/data/code
corruptions are checked independently.

All other **6,050 function bodies and every function address** are unchanged.
Exactly one of 698 frozen objects changes, retaining all 32 owner neighbors.
All **189,088 protected data bytes / 720 owners** remain exact. The production
ELF equals the independent prediction:
`acfda9b326af44f83b8a7d31c3a927bbf7111b9e2ae5b3b5ae26e6020183f731`.

Fresh post-install source compilation agrees on all 33 compact owner functions;
actual production instructions pass 2,560 guest and 256 original-caller cases,
visiting all 122 target words. Earlier source/padder/symbolic/native checks
are reused at this final stage only with exact input/task/fixture hashes.
Production match-progress, tools-check and an independent actual-ELF recount
pass. The existing duplicate generated_12D630 Makefile recipe warning remains.

## Preserved state and next work

The 1,563-input baseline copies changed production inputs and the ten prior
tools additions, linking only earlier immutable files. It has zero live-worktree
hardlinks. Exactly four frozen inputs change: source, guard CSV, owner object
and ELF. Conversion classification, retail data and all prior guards remain
unchanged. New task files and actual imports are separately fingerprinted.
The primary suite records 356 import rows. The sibling suite records ten task
overlay rows, 301 sibling rows and 47 primary fallback rows. The sibling's
2,434 dirty paths and 339 present scoped dependencies remain untouched.
Claude calls are 0; existing local ABI and
instruction-driven tools settle this routine.

The host sibling still has only `.codex` and `recomp_scene`, with no source/Git
checkout available. It is untouched, including Release and saves.

Evidence is in `conker/build/game-next-151ae3a8-private/adoption/`: paired
sealed suites/imports, original/padded GNU links, relation and negative controls,
guest/native/caller receipts, Make prediction, metadata controls, production
audit/focus and actual recount. Native Graphify refresh fails closed on the
reduced corpus; scoped AST merging retains all 64950 old IDs
and the explicit target reference. This is not full-corpus re-extraction.
Commit tools before source/guards/notes/aggregate rows/pin, locally only.

Next inspect **func_151AEAB4**, the 123-word randomized effect emitter with
frame 0x98, three incoming words and an 18-argument emission call. Preserve its
recovered constructor/caller interfaces. The 85% goal remains active beyond
this checkpoint.
