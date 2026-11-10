# Game entity-height query pair guarded match - 2026-11-09

`func_15045D48` (lowest) and `func_15045F8C` (highest) now match their complete
**145-word / 580-byte** retail slots, each with its natural **0x28 frame**.
Semantic C emits all 145 words. Expected-word/relocation guards close 52 words
in the lower query and 54 in the upper query. No insertion, omission, source
padding, compiler-profile or shared declaration changes.

Fresh production-ELF counts are **4,302 / 5,513 (78.03%)**, Game **3,629 / 4,840
(74.98%)**, Init 492/492 and Debugger 181/181. Address drift 0; 1,211 still differ.
The active 80% goal requires **109** further matches to 4,411/5,513.
The README changes only aggregate rows; function detail stays in this note.

## Scope and recovered behavior

Owner `conker/src/game/generated_71820.c`; object `conker/build/src/game/generated_71820.c.o`.
Retail reference `conker/asm/71820.s`:

| Function | VA span | ROM span | Raw words | Guards |
| --- | --- | --- | --- | --- |
| func_15045D48 | 15045D48..15045F8C | 731F8..7343C | 145 | 52 |
| func_15045F8C | 15045F8C..150461D0 | 7343C..73680 | 145 | 54 |

This completes the matching left open by [Note773](773-game-context3-entity-lowest-height-query-recovery-20261003.md)
and [Note765](765-game-entity-height-query-semantic-recovery-20261003.md).
The [Note766](766-game-entity-scan-producer-assembly-restoration-20261003.md)
producer/wrapper assembly remains intact. Direct C combiners from
[Note774](774-game-lowest-height-combiner-direct-match-20261003.md) and
[Note775](775-game-highest-height-combiner-direct-match-20261003.md) stay exact.

Both interfaces are `(f32 *position, f32 threshold, s32 *input,
HeightResult71820 *result)`. The float occupies the second o32 argument word.
Neither query has an early threshold gate. Initialize the lower default
from D_80098D58 (47C34FF3,99999.8984375f) or upper D_80098D5C
(C61C4000,-10000.0f). Call150A44F0 with input[0], the inline D_800D3830
buffer and0. Reload input and signed-truncated X/Z for150A43E0.
Those two helpers remain bounded providers in these target tests.

The inline D_800D3300 table contains16-byte candidate rows. Convert signed
fixed heights to f32 and multiply by1/256. Lower keeps the first strictly
lowest candidate >=live queryY; upper keeps the first strictly highest
candidate <=live queryY. Ties retain the first candidate. Reload live queryY
and result height, including provider changes. A nonpositive count selects none.

Cache the selected triangle and signed vertex BYTE OFFSET before copying
three XYZ short triples. This offset is not multiplied by16. Reload the
candidate entity index after those copies, then form an entity pointer from
the pointer global D_800DBEF4 with stride0xA0. Cache that pointer and publish
it in result.value before loading entity.metadataTable. If a table exists,
use signed `(triangle-D_800DBE3C)/12` minus unsigned16 firstTriangle to index
it; otherwise use entity.metadata. Publish flags|6, optional flag1 from
entity flag0x80, and state3 in both queries. Lower accepts height<=threshold;
upper accepts threshold<=height. Selected threshold failure retains the
published flags. No selection clears only flag2 and returns0.

## Source shape and closed normalization

The predecessor bodies emitted144 words. Flags, state placement, duplicate
state arms, carrier widths, local ordering and block shapes were screened.
The accepted flags local is loaded in both metadata arms; state3 is written
before the entity flag test. This recovers145 words/frame0x28 naturally.
Focused comments identify the lower/upper entity triangle query. Existing
layout and parameter names are preserved; no speculative global rename.

Raw SHA-256:

- Lower206182f7c82eebb71158948570ec1a9b46e94dd40c5a0e2f8df9ed936e4827e4.
- Upperf847b13b39994e2e166ba681906fb77a7994acc853a64e2554f4dc905069876a.

The normalizer pins each full payload, length, owner/function and16 binding
sites. It derives a closed selected-index/count/index register cycle,
cached candidate/triangle/offset roles, and entity-stride/base roles.
The copy cursor moves into the ordinary loop branch delay; adjusted short
store offsets preserve every effective address and memory-event order.
The triangle cursor increment moves only after its load has completed.
Metadata flags loads move past disjoint result metadata stores.

The publication tail exchanges two exclusive duplicate f32 loads plus one
common state store for one common f32 load plus two exclusive state stores.
Every runtime path executes one of each; branches, masks and values agree.
For aligned result/entity pointers, result.state offset1D cannot alias the
entity flag byte offset6F. Result flags/state are separate bytes. Upper also
exchanges two independent opening tail loads. Full raw/original/normalized
guest agreement includes cases that overwrite the candidate or entity table.
All 106 guards are replacements; four guarded HI/LO words retain their exact
entity-base relocations. Guard history remains an identical byte prefix.

## Qualification and evidence limits

The 43-function owner has 41 C bodies and two retained ASM routines,
15044660/15044ED0. All **41 non-target neighbors** remain identical before
and after both raw compilation and production padding. Pools and reginfo
stay fixed. CFE diagnostics remain0. The normal five-command Make recipe,
independent original assembly, isolated generated/generic padders and full
production owner agree. All 6051 function addresses stay fixed.

Strict independent whole-ELF prediction accounts for **341 changed bytes**,
only the two580-byte function slots and their st_size updates576->580.
No exclusions or unexplained bytes. Protected 189,088 data bytes across 720
owners remain exact, SHA2560bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
The conversion CSV and Makefile are unchanged. The inherited whole-ROM
checksum mismatch (`make all` exit2) and duplicate12D630 Make warnings persist.

Six fresh focused tests run before and after installation in each tools
environment. An attempted installed native/control receipt reuse was rejected
when the complete raw object hash changed. A repeat compile measured only
.mdebug changes with all 43 function bodies identical. Fresh installed native/
control checks replace that rejected reuse; no weaker hash gate is substituted.
The sibling environment uses a read-only overlay for new modules;
helper origins, transitive dependencies and hashes are recorded. Its 2,439
preexisting dirty paths remain unchanged. Both shared tool smokes are fresh;
three unchanged regression checks per copy are explicitly fingerprinted reuses.

- Guest: 904 cases per body across six bodies =5,424 executions, plus 48
  independent rebases. All result/entity/candidate state, helper observations,
  o32 saved registers, frame/home mutations and aliases are checked. Each body
  visits 144/145 words; unreachable fallback load 109 is preserved statically.
- Native SDK32: 1,728 defined cases at O0/O2/O3, UBSan, 24 effective per-function
  controls per profile. Full result, padding/canaries, entity/candidate fields,
  retained bytes and readonly data are checked. Physical aliases/private guest
  homes are guest-only. Vertex padding uses equivalent numeric halfwords
  across endianness; the initial fixture mismatch was corrected and uncredited.
- IDO: 24 effective controls, twelve for each routine. Signed-height witness
  includes negative queryY so the lower unsigned mutation cannot escape.
  No compiler/interpreter/sanitizer error counts as a semantic witness.
- Both padders reject 110 stale expected-word/binding cases each. All 290
  single-word payload corruptions and seven whole-image corruptions are rejected.
  Eight independent GNU links and32 executions cover HI/LO carry boundaries.
- Caller census:one lower JAL in150461D0, two upper JALs in15045780/15046460;
  no aligned entry pointers or direct tail jumps. Whole164/166-word C combiners
  and32-word retained ASM wrapper execute 1,350 cases/900 target invocations
  against all three target versions. Every combiner word is visited; wrapper
  word19 is the dead duplicate store following an unconditional branch/delay.
  Float ABI, real stack buffers, first-return byte narrowing, packet copies,
  comparisons and early paths agree. Preparation and the other spatial query
  are bounded providers; this does not qualify their algorithms or gameplay.

Requested Graphify refresh includes the owner and six tools modules. All41
owner C source locations and both retained ASM functions are audited, with
old nodes outside changed paths retained. The parent corpus does not index
the new tools modules; actual zero-node coverage is reported honestly.
Excluded existing corpus is retained fail-closed, not fully re-extracted.
Local tools-first and consumer commits bank the source/guards/docs/pin.
No push, sibling edits, host-port build or frozen Release changes.

Ignored evidence lives in `conker/build/game-entity-height-pair-match/`:
717 frozen inputs, source probes, qualification/normalization, guest/native/
controls/caller receipts, tools replays, production recount/hashes, graph
retention, review diffs and accepted continuation handoff.

Next: inspect the context2 pair 15045880/15045AE4 in this owner, 153 retail words
and 88 screened differences each. Reuse family infrastructure only after full
retail/caller qualification; their context/result rules can differ. The hard
private 1510D404 candidate remains uncredited. Keep the 80% total goal active.
