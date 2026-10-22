# Six Ordered Byte Submissions Direct C Match

Date: 2026-10-21

## Result

Restore `func_150B3DD0` in `conker/src/game/generated_E1280.c` as
purpose-commented, complete C. Normal O2/g3 emits all **41 body words,
frame40 and seven R_MIPS_26 bindings** directly. There is no alignment
filler, guard, raw emitter, profile change or shared-header edit.
Keep the reference `conker/asm/E1280.s`.

VA 150B3DD0..150B3E74 / ROM E1280..E1324, ends exclusive.
Unlinked C/GNU-original body SHA-256:
`dfa8426fa9150a1b4cc5336888199f15b34a74b4dab22581f7e4c4561c5ec142`.

## Recovered Contract

Use `void func_150B3DD0(void)` with a local `u8 selection[4]`.
First call `func_15147D64(0, 5)`. Then set only byte zero to
**0, 2, 4, 1, 3, 5**, in that order, calling
`func_151494E0(selection, 0x18)` after every store.

The same pointer survives all six callbacks in saved S0. The selected
four-byte array recovers retail's SP+0x24, or entry-SP-4, address. A scalar
and an eight-byte array also have frame40 but miss seven address-related
words. This establishes an exact conservative storage view, not uniquely
proven historical type spelling. No dummy padding variable is introduced.

Leave the other three bytes uninitialized. Guest fixtures start with
controlled memory patterns and verify their preservation or callback
mutations. Native providers never read these bytes before initializing them
themselves. Later callbacks must see those writes retained while byte zero
is overwritten with the next selection. Do not add a memset or initialize
an invented payload tail.

No incoming argument is read. The routine does not materialize a return
word; both actual helper C definitions are void. Preserve incidental V0 in
the machine comparison and original caller, without inventing a semantic
zero return. Add only owner-local `void (void *, u8)` helper declarations;
the existing helper definitions use machine-compatible pointer words.

Bindings relative to the target: offset 0x10 calls `func_15147D64`;
0x24, 0x38, 0x4C, 0x60, 0x74 and 0x88 call `func_151494E0`.
Check all seven bindings independently, then link at retail and three
independent address sets.

## Caller And Helper Bounds

The original `func_1509D780` spans 95 words/frame24 at
VA1509D780..1509D8FC / ROM CAC30..CADAC. Command 8 selects table entry 6
at 8009F1C4, targeting 1509D854. Execute its original dispatch prefix,
target call and return path, plus unsigned out-of-range defaults. Preserve
the result word through its epilogue. This is selected-path qualification,
not all-95-word dynamic coverage. Its current C body in
`generated_C9EC0.c` remains a placeholder; no current-parent execution or
new matching credit is claimed.

Connect both original 13-word/frame24 wrappers:
`func_15147D64` at ROM175214 and `func_151494E0` at ROM176990.
Both are already exact in the current linked image. Each forwards a
registry pointer, count 2, payload pointer and zero-extended command byte
to `func_15169260`.

The initial registry `D_800A5760` supplies 0x4D/0x22; the six submissions
use `D_800A5770`, supplying 0x23/0x5F. Check the complete 26 wrapper
words, saved argument homes and payload across hostile volatile clobbers.
The lower dispatcher is a bounded packet provider in these tests. Its
current C body remains empty. Its original 123-word body and metadata were
inspected and pinned, but not dynamically qualified here. No natural
registration, handler implementation, rendering or gameplay claim follows.

## Qualification

Tools: `experiments/game_six_byte_dispatch.py` and
`tests/test_game_six_byte_dispatch.py`, identical in both local copies.

| Final Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 36.793s | 8 tests, 57.970s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 5.538s | 2 tests, 10.731s | 0 / 0 / 0 |

Explicitly reuse the other six checks per copy only under unchanged source,
raw/padded object, helper, pinned-input and whole-image identity. They are
not fresh installed executions. Shared project-tool checks pass twice.

- 1,024 guest phases vary all 256 seeds, two SP phases and callback mutation.
  All 41 target words execute; preserve six byte stores, the shared local
  address, saved registers, caller homes and incidental V0.
- 512 legal native32 cases per optimization at O0/O2/O3 run the actual C
  with trap UBSan. Eight compiled wrong-C controls are effective, including
  missing submission, wrong order/command and invented tail initialization.
- Six independent GNU links / 48 phases check all seven R26 bindings.
  Sixteen connected wrapper phases cover all 26 wrapper words. Thirty-two
  original caller phases cover command 8 and unsigned default selections.
- Eighty fired root-access fault prefixes compare full modeled state,
  memory trace and current/delay PCs. These are bounded software-model
  checks, not portable fault, hardware timing or MMU acceptance.
- Pin 32 historical/current inputs and the predecessor object. Preserve all
  nine owner neighbors, pools, diagnostics and the complete guard manifest.
  The actual Make shadow executes three productive commands with O2/g3.

The first commit whitespace check rejected extra EOF blank lines in the
new tool files. Normalize them and rerun both complete suites against the
final bytes; the table above records those final runs. The initial consumer
promotion gate also caught a blank-line-only source discrepancy before any
production copy/build; correct it to the exact qualified source first.

## Production And Preservation

Seal all 15,790 live/copy files, including the complete 1,454-object linker
closure. Rebase only the previously committed SDK source/caller/object/ELF
delta using its strict adoption proof, then add four new task-file copies.
The existing Linux cache remains valid; no new dependencies or provider
reconfiguration are needed.

Actual production Make exits zero in 2.353s. It reproduces the independent
full-image prediction exactly: **128 changed bytes = 127 instruction bytes
+ one symbol-size byte**, zero metadata exclusions/permutations.

Installed ELF SHA-256:
`54a5080e31880f9c13c5ba4f233a0a7204fdb09cf851eb82fd412591e0f5ac65`.
Installed owner object SHA-256:
`67f76057b026dd214b7353df37958974531fcd63df0e17e25034b7679cf2c09a`.

All other 6,055 function bodies and all 6,056 addresses remain fixed.
Protected Game data is exact: 189,088 bytes / 720 owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Recheck every sealed live file before and after adopting only the owner
object, ELF, generated linker script and progress CSV.

Tools commit `bda743c91ebd4389ad772c2cbc1500edbb54ae26` precedes the
consumer source/docs/pin commit. Preserve all 1,522 pre-existing dirty
statuses and hashes in the older tools mirror, adding only two task files
for 1,524 dirty paths. Do not commit/reset/stash/clean that mirror.
No push, host build/launch/change, shared-header/profile edit or Claude call.
Host Release remains frozen. Root README changes only two aggregate rows.
Refresh Graphify and audit old-node retention at the consumer checkpoint.

## Measured Progress And Resume

The standard matcher exits zero against the adopted live consumer ELF:

| Section | Byte-Exact Converted C | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3,723 / 5,505 (67.63%) | 0 | 1,782 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,050 / 4,832 (63.12%) | 0 | 1,782 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The 75% threshold remains 4,129; **406 more exact functions** are needed.
The broader goal is unfinished. The refreshed ELF-pinned queue has 1,649
placeholders, 124 semantic/other definitions and nine unlocated entries.

Next screen: `func_15188AD0`, 41 body words/frame48 in
`conker/src/game/generated_1B5CC0.c`, reference `conker/asm/1B5CC0.s`.
VA15188AD0..15188B74 / ROM1B5F80..1B6024, ends exclusive.
Statically it traverses `D_800DF7C8` through +0x0C links, compares +0x10
against the incoming key, rewires the head/previous link, and calls
`func_100043B4(node[2], 2)` then `func_10004074(node)` for a match.
Determine actual caller/return ABI, helper contracts, cached-successor and
previous-node lifetime, callback-visible effects and reachable-word coverage
before drafting/installing. No new credit or source change is claimed.

Private receipts, snapshots, probe shapes, guest/native fixtures, Make
shadows, linked images, queue and preservation audits are under
`conker/build/game-six-byte-dispatch/qualified/`. No ROM, generated
fixture or build artifact is committed.
