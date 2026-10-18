# Enabled Record Tag Query Byte Match

Date: 2026-10-18. Consumer predecessor **6fc71976**, tools predecessor
**3cc55c3**. Restore **func_15022B08**, owner `generated_49D30`, VA
**0x15022B08..0x15022BA4**, ROM **0x4FFB8..0x50054**. The wider Game matching
goal remains active; this is one completed function.

## Semantic Recovery

Replace the zero-return stub with typed **s32(s32 recordIndex,s32 category) C**.
The source checks the category's count, walks enabled u16 entries and compares
descriptor byte +2 (8-byte stride) with selected record byte +0x72 (0xA0-byte
stride). Any enabled match returns exactly one; empty/no-match returns zero.
The record-array pointer view recovers the natural stride without an invented
machine-word body or assembly fallback.

The existing **O2/g3/MIPS2/o32/-Wo,-loopunroll,0** profile hoists the repeated
count expression into one entry snapshot and captures the enabled-array
pointer once. Descriptor-table and record-base pointers reload on each enabled
iteration. Ordinary C emits the complete **39-word/no-frame** routine,
including the otherwise unreachable increment at **0x15022B88**. All 38
reachable words execute across the corpus; the dead word is checked by bytes,
not described as executed. Do not trim it as padding.

## Closed Normalization

Bounded loop/initialization/table/pointer forms recover the original control
flow. The selected complete C body retains **nine real word differences**.
They are only a closed **A0/A2 register-allocation cycle** and a three-word
independent setup schedule. From words5..35 exchange A0/A2 roles; rotate raw
words11..13 to raw12/raw13/raw11. The moved LW crosses only two independent
address ADDIUs, not another memory operation. RecordIndex is already retained
in A3 before the window; A0/A2 are caller-saved and dead argument roles at exit.

**Nine expected-word/relocation guards** perform precisely that transformation.
All eight data bindings are pinned, including three moved LO16 bindings.
No branch structure, return value, data operation, literal, instruction count
or compiler profile is substituted. No words are inserted/omitted. The linked
156-byte slot is fully retail-exact. These are guarded matches, not a claim
that all 39 raw C words already match without normalization.

The original guard bytes remain an identical prefix, with nine appended rows.
The existing CRLF-to-LF Git notice is formatting, not an instruction change;
the task diff contains only those nine new rows, without bulk normalization.

## Fresh Qualification

New tools: `experiments/game_enabled_record_tag_query.py` and
`tests/test_game_enabled_record_tag_query.py`. Ignored artifacts:
`conker/build/game-enabled-record-tag-query/`. Sixteen explicit inputs pin
owner/caller source and original assembly, whole ELF, guards, actual caller
object, build/symbol/header inputs and all four prepared compiler components.

All **seven strengthened pre-install tests pass in 52.385s**; all **seven
installed tests pass in 51.460s**:

```sh
python3 -m unittest tools.tests.test_game_enabled_record_tag_query -v
```

**2,688 three-way raw/normalized/retail cases** check counts through255,
disabled/nonzero/high-halfword enables, first/middle/last/no matches, unsigned
tag boundaries, record/category selection and two stack phases. Exact read
traces and boolean results match an independent reference; memory remains
unchanged, no calls occur and saved ABI state is preserved.

Native32 **O2/O0 with UBSan** each pass **16,384 cases**, covering all count/tag
byte values and four valid record/category indices. Descriptors occupy one
flat byte buffer, records occupy actual 0xA0-byte rows, and the complete input
image is checked for writes. Seven enable-one/ignore-enables/descriptor-stride/
descriptor-field/record-stride/record-field/false-positive controls return
explicit wrong-result status23. Compiled guest controls also change the live
boolean result, not merely an unused scratch register.

**20 scripted-read cases** separately perturb count/table slots at declared
guest read boundaries, demonstrating the emitted count/enabled snapshots and
descriptor/base reloads. These qualify emitted access lifetimes, not native
volatile, interrupt or data-race semantics. Native inputs remain stable.

Nine independent original/raw-C/actual-padded links at three code/data placements
pass **144 three-way rebased cases**. The normalized result equals independently
assembled retail at every placement; raw C follows the same read/result model.
All eight bindings and three LO16 moves are exercised. **472 access-fault
prefixes across 72 states** preserve raw/normalized memory/read prefixes and
saved/live counter roles. Normalized/retail complete state agrees. Raw dead
scratch registers and the independently scheduled LW's PC are not falsely
claimed identical; this is not a portable C fault or hardware MMU proof.

All **39 raw words / eight bindings / nine guard expectations / 32 live-and-
frozen input mutations** are corruption-gated. Nested historical views fail
closed. Unchanged broad neighbor suites are prior receipts, not fresh reruns.

## Three Caller Boundaries

Retail callers in asm/142560.s are **func_151189AC at 0x15118DF0**,
**func_1511A738 at 0x1511A778**, and **func_1511B07C at 0x1511B0D4**. They
derive recordIndex from signed pointer-distance division by0xA0, pass category
zero, and consume V0 in return branches. The local C declaration becomes
**s32(s32,s32)**. All **84 raw caller-owner functions**, pools/bindings and
the complete production caller object stay identical; neither compilation
introduces diagnostics. No shared header is edited.

The full **34-word func_1511A738** is already production/retail-exact. **162
full restored-C caller cases** execute it with raw and normalized query bodies,
checking gate bypass, boolean-dependent +0x7C/+0x18 clears, field/argument
lifetimes and saved state. Only its two downstream calls are scripted ABI
boundaries, not claimed complete subsystem behavior.

The other two containing production parents remain stubs. **48 bounded actual
retail windows** execute their index calculation, query call/delay and consumer
branches: saved T0/float selection in the first, taken/not-taken continuation
in the third. This does not claim either large parent or gameplay restored.

## First Prediction And Build

Before production edits, substitute the qualified padded owner in a copied
current linker script and freeze the entire **3,257,636-byte ELF** successor,
two source successors and guard successor. The independently qualified caller
has an identical complete object, so its typed declaration does not alter the
first ELF prediction. Original fixtures and the first successors are immutable.

```sh
make -C conker -o Makefile -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_49D30.c.o build/src/game/generated_142560.c.o \
    build/conker.us.elf progress.csv
make -C conker -o Makefile -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

The installed ELF equals that first prediction: **118 changed bytes = 117
target-code bytes + one target symbol-size byte**, at file offset2999035.
Target st_size changes **12 -> 156**, with zero metadata exclusions. All
**6,057 bodies/addresses** and canonical symbol definitions are audited;
only this body and extent change. All **56 raw owner neighbors**, pools and
bindings remain fixed; actual padded owner and caller objects match qualification.
The Makefile/profile stays fixed and Game data remains **189,088 bytes /
720 owners / zero differences**.

| Prepared Artifact | SHA-256 |
| --- | --- |
| Complete installed ELF | `23478930a3dea7a22178648e4c9330cb4b09d9271474b01fd9ddd2240826b85a` |
| Complete owner source | `350c4b08699ee583e4c5dd58b6fd403ab49dba62bf4aab53211d146850dc81de` |
| Typed caller source | `8a6596d3f961e0b7e1b8ab66bb07ba96664537b10feadeab5113396146ecfff2` |
| Unchanged caller object | `898b6213f95d4d0d24b05ce98261514521f8413a02ee366f09a73edd74a77fcf` |
| Raw target | `2725b2c7822030ee1dc09c12d45c63687e199d3c7c7aaf636bf34b713602348f` |
| Linked target | `c3a596ae3d2505be36e85f45740c2eec98eb9eaab70271cff4dfc02fa5705069` |
| Guard successor | `8f709f6c1cb03108c0f1e6f7b460e624d76f29734c97ed5fe9739f411f2046a1` |
| Unchanged guard prefix | `625033dd1c2150ce2edb45badf13c05d09aa95b83a0c2b1231e092105d3fc2b3` |

The four-member historical view rejects unknown/mixed or nested states and
retains physical raw reads for audit. Older fixtures/helpers/hashes are not
weakened; future work should freeze the new physical baseline directly.

## Bank And Next Action

Tools **5abdd73** is committed before consumer source/guards/docs/pin. Both
local copies pass eleven shared padder tests and project-tools smoke checks,
four Windows ASCII/AST parses and two exact task-file comparisons. Preserve
older mirror **ddbdd16**, all **1,200** initial dirty hashes and its history;
add only two absent paths for **1,202** dirty paths. No mirror commit/reset,
push, Claude call or host/frozen Release edit/build/launch occurs.

Fresh official totals: **Game 2,975/4,828 (61.62%)**, total **3,648/5,501
(66.32%)**, **1,853 different**, zero address drift. Conversion counts/bytes
remain unchanged. Root README changes only two aggregate rows.

Scoped Graphify refresh: **42,451 nodes / 82,523 links / 4,068 communities**.
All **19,398 nodes from 2,972 excluded-but-existing files** are retained.
Only three line-disambiguated UPDATE_LOG heading IDs change; all three labels
persist and all other old IDs remain. The new note contributes eight nodes.
Target/caller definition locations resolve to **L828/L327**. The original
graph is preserved under the ignored task build directory; graph outputs
remain ignored. No full-scan purge or graph-history rewrite is performed.

Next recover **func_15087E54**, owner `generated_B3020`, VA
**0x15087E54..0x15087EF0**, ROM **0xB5304..0xB53A0**, **39 words/frame0x18**.
Audit callers/helper ABI first. If D_800872A0 is nonnull, index 0x84-byte rows,
pass floats at +0x10/+0x0C and A2=0 to func_1505A630, then clamp actor u16 +0x76
against the wrapped helper result +0x4000. Preserve the negative-side exact
**delta<0xDBFF** and positive-side **delta>=0x2401** limits, storing target+0x2400
or target-0x2400 respectively. Do not replace their asymmetry with a symmetric
signed abs test. This slice's existing no-unroll CFLAGS must coexist with
ordinary O2/g3 GLOBAL_ASM processing. Callback/parent stubs, handwritten
func_150A76F0, both fade gaps and the other open queues remain separate work.
