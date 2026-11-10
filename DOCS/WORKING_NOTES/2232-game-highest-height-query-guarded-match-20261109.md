# Game highest-height query guarded match - 2026-11-09

`func_150450CC` now matches all **144 words / 576 bytes** with the original
**0x28 frame**. Complete semantic C emits144 words;30 expected-word/relocation
guards close register roles and scheduling. No insertion, omission, source
padding, compiler-profile change or shared declaration change.

Fresh production-ELF counts: **4,300 / 5,513 (78.00%)**, Game **3,627 / 4,840
(74.94%)**, Init492/492, Debugger181/181, zero drift and **1,213** different.
The active80% goal needs **111** more matches to4,411/5,513.
README changes only the two aggregate rows.

## Source and retail behavior

Owner `conker/src/game/generated_71820.c`; VA150450CC..1504530C,
ROM7257C..727BC. Original reference: `conker/asm/71820.s`.
This completes the matching work left open by [Note759](759-game-highest-height-query-semantic-recovery-20261002.md).
The collector/context restoration in [Note760](760-game-collector-context-assembly-restoration-20261003.md)
and the direct C caller match in [Note777](777-game-entity-terrain-highest-combiner-direct-match-20261003.md)
remain intact. The earlier declaration boundary is preserved; no slice-wide
prototype or shared table-type cleanup is introduced.
The mixed argument ABI is `(f32 *position, f32 threshold, HeightResult71820 *result)`;
the float threshold travels in the second o32 argument word.

If queryY < threshold, clear result flag2 and return0. Otherwise initialize
the result height from the byte-verified retail default **-10000.0f** at
D_80098D44, select context0, publish queryXYZ/threshold globals, then submit
the truncated signed X/Z coordinates to `func_150A3A70`.

Scan its signed count of16-byte candidate records. Convert each signed fixed
height to single precision and multiply by1/256. Keep the first strictly
highest candidate at or below the live queryY. Equal heights do not replace
the current selection. Reload result height and queryY through their live
pointers while scanning; helper mutations and output aliases matter.

For a selected candidate, copy three vertex XYZ triples, preserving the
16-byte source-vertex stride, signed index and three short loads/stores per
iteration. Optional metadata uses signed pointer difference /12 to index a
parallel word table. Publish state1, OR flags with7 and clear the value word.
Return1 iff threshold <= final height. **The flags remain ORed with7 when
that final threshold test fails**; a corrective-looking clear would be wrong.
With no selection, clear only flag2 and return0.

The accepted source moves selection initialization past the early return and
names the flags byte explicitly in both metadata arms. The latter preserves
the full144-word branch/publication shape. A focused comment describes the
query; existing parameter/layout names already identify their roles.

## Natural shape and bounded normalization

The predecessor C emitted143 words. Four initialization probes, seven local/
coordinate/flag layout probes and six register/cursor probes were measured.
The selected source emits144 words with its natural0x28 frame, correct saved
S0/RA lifetime, threshold/result argument homes and selected-index homeSP+0x20.
**114/144 words emit directly**. Its raw SHA-256 is
`8b23f1b0ccbcb6398d869c1f99eebb54ca5c9cebaf6d59777bb94c911c531a19`.

The30 guards divide into:

- Seven words close the count/index v1/a0 register swap before the output
  cursor reuses v1.
- Six words move the coordinate cursor increment into the ordinary loop-branch
  delay. Store offsets change from -2/0/2 after the increment to4/6/8 before it;
  all effective addresses, short widths and memory read/write order stay fixed.
- Seventeen words close metadata/quotient/flag register lifetimes and move the
  independent flag load after the metadata store into the jump delay. Metadata
  word0x18 and flag byte0x1C are disjoint. Two guarded words retain their exact
  D_800DBE5C HI16/LO16 bindings.

The normalizer pins the complete raw payload, function/owner and all20
relocation sites. It derives the loop reschedule and register changes from
the checked source instructions. Original assembly, both independent target
padders, the production owner padder and actual Make agree exactly.

All42 raw/padded neighboring functions, pools and register-use metadata remain
fixed. The owner has43 functions:41 C definitions and two retained assembly
functions, `func_15044660` and `func_15044ED0`. Compiler diagnostics are **0->0**.
Actual Make executes its five-command asm-processor/IDO/postprocess/pad/assemble
route. The strict whole-ELF predictor accounts for **197 changed bytes**, all
within this slot and its size metadata572->576, with **zero exclusions or
unexplained bytes**. All6051 linked function addresses and all189088 protected
data bytes across720 owners stay fixed. Guard history is an unchanged prefix
plus30 rows; conversion CSV and Makefile are unchanged.

## Fresh semantic and caller qualification

Six focused checks pass before and after installation in the mounted tools
checkout and a read-only overlay using sibling helpers. The sibling's2439
dirty paths are preserved. Shared smoke checks are fresh in both copies;
three unchanged regressions per copy are explicitly reused with exact helper/
test fingerprints. Claude calls:0; routine source/compiler/model evidence suffices.

- Guest: **3914 cases/body**, **11742 executions**,24 independent rebases.
  All flag bytes, negative/empty counts, equal heights, signed fixed-point
  extremes, negative vertex/metadata indices, NaNs, threshold equality,
  aliases, helper mutations and private-home changes are covered.
- Original context wrapper `func_1510F800` (8 words) and selector entry
  `func_150A49F4` (40 words) are byte-verified and executed for context0.
  The selector is an untyped assembly label, not an additional C match.
  The spatial scan is a bounded provider; its complete algorithm is not claimed
  executed. Scripted mutations and negative return counts are extensions.
- The target reaches143/144 words on normal entry. Word116 is an unreachable
  duplicate zero-metadata store, preserved statically in all three bodies.
- Native SDK32: **3866 cases/profile** atO0/O2/O3 with UBSan traps. Result fields,
  retained padding and canaries, signed indices, metadata and all12 semantic
  controls pass. Read-only triangle/vertex/metadata storage stays unchanged.
  The original C context wrapper is included. Guest frame/physical aliases
  are excluded from portable C claims.
- Twelve independently compiled IDO controls produce actual public-memory,
  call-observation or return-value differences. Private spill differences,
  compiler errors and interpreter/sanitizer failures are not witnesses.
  Both padders reject32 stale word/relocation guards each. All144 payload
  corruptions and six image corruptions are rejected; four actual GNU rebases
  execute16 cases.
- The sole retail direct call is ROM73EF0 in the already exact C combiner
  `func_1504697C`. Fresh ROM/linked census finds no aligned target pointers or
  direct tail jumps. The **entire161-word caller** remains retail exact and
  passes1296 executions across all three target bodies, with864 actual target
  invocations. All comparison/copy outcomes, saved o32 roles, the mixed float
  ABI and low-byte first-result narrowing are checked. Words76/140 are dead
  duplicate moves after unconditional branch delays; no incoming branch targets
  them. The other159 caller words execute. Its first spatial query remains a
  bounded provider, not a full query-algorithm acceptance claim.

The initial generated native fixture had duplicate NULL and flattened nested
initializers; the failed owned compiler was stopped after a focused syntax
check confirmed the error. Declarations were fixed and diagnostics bounded
before qualification. All-negative height cases were added to make the
signedness control effective. No failed run was counted as acceptance.

## Banking and continuation

The ordinary `make all` checksum exit2 and duplicate generated_12D630 recipe
warnings are inherited. Target production, data, image and recount gates pass.
Retail guest/native qualification does not establish hardware or host gameplay
acceptance. The separate host port and frozen Release remain untouched.

Requested Graphify refresh paths include this owner and six new tools modules.
All41 C source locations and both retained assembly functions are audited.
The current parent graph contains no nodes from the six new tools modules;
those modules are qualified through both tools environments above. Existing
nodes outside changed paths and excluded existing corpus nodes are retained,
with no full-corpus semantic extraction claim. Tools are committed first,
then the consumer source/guards/docs/pin. Local commits only; no push.

Ignored evidence: `conker/build/game-highest-height-150450CC-match/` holds717
frozen inputs, all probe variants, normalization/strict image receipts, guest/
native/control/caller reports, both tools environments before/after installation,
production hashes/recount, graph retention, review diffs and final handoff.

Next: `func_15045D48`,145 retail words /72 real differences, in this same owner.
Its sibling `func_15045F8C` has the same screened size/difference count. Inspect
each complete retail routine and interface before reusing the family model;
do not infer equivalence from similar source. The hard private `func_1510D404`
candidate stays uncredited. Keep the full80% matching goal active.
