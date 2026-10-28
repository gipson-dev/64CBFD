# 1755 - Ordered record classifier direct C match

Verified: 2026-10-27. Target `func_15159370`, owner `generated_185560`.
VA `15159370..1515942C`; retail ROM `186820..1868DC`.

## Result and recovered interface

Replace the zero-return placeholder with the complete semantic classifier.
All 47 words /188 bytes emit directly under normal O2/g3: no frame, two
HI16/LO16 bindings for `D_800BE616`, zero guards and no target diagnostics.
Preserve all 36 neighbors, pools and all 37 compact functions, including the
existing GLOBAL_ASM routine. The actual five-command asm-processor/IDO/
postprocess/generated-padder/assembler Make route reproduces the object.
The owner's four existing pointer/integer warnings remain unchanged; the
inherited duplicate generated_12D630 recipe warning also remains.

The interface is `s32 func_15159370(u8 *record, u8 *classification)`.
The result indicates whether any rule applied; it is independent of whether
the resulting classification byte is zero. A no-match call leaves the output
unchanged and returns zero. Apply these rules in order:

| Condition | Written classification |
| --- | ---: |
| nonzero unsigned `D_800BE616` byte | 0 |
| record byte +0x3B equals 1 | 0 |
| record byte +5 equals 5 or 2 | 1 |
| record byte +4 equals 8 | 2 |
| record byte +4 equals 10 | 3 |
| record byte +4 equals 0x29 or 0x2A | 4 |

The first three tests are independent; the final type switch can override
any earlier output. Each applied rule sets the return flag to one. Preserve
later record reads after preceding output writes. The output can legally alias
record bytes, so pre-caching all fields or returning after the first match
changes behavior. The initial straightforward ordered C already matches all
47 words; no source-order search or compiler profile override is needed.

## Complete original caller

The aligned whole-ROM census finds one JAL at ROM 186148, VA 15158C98, inside
`func_15158BD0`, with no pointer literal or tail J. The original caller
allocates a record, initializes its header and coordinate fields, and passes
its source record plus the allocated record's byte +0x1D to this classifier.
A zero result releases the allocated record and returns null. A nonzero result
clears its byte +0x50 and returns the record, including when classification
zero is valid.

256 cases connect the rebuilt/retail classifier to the complete 65-word
original caller. They cover null source, allocation failure, acceptance,
rejection/release, initial flag values and each class of rule. Verify the
public header/coordinate writes, classification byte, helper arguments,
release decision and returned pointer against an independent reference;
compare complete private state between retail and rebuilt paths. Allocator
and release are bounded providers. The caller's C placeholder stays unchanged
and uncredited; this is not full allocator, release or gameplay acceptance.

## Fresh qualification and effective controls

Both tools copies pass eight fresh canonical methods and shared project-tool
checks. Each later runs two fresh installed owner/image checks and reuses six
semantic methods only after exact module/input/artifact identity.

- 15,008 guest cases cover every global gate, record type and subtype byte,
  all rule priorities, unmatched output preservation, two stack phases,
  seven output layouts and four global layouts. Actual GNU-linked aliases
  cover output over type/subtype/tag bytes, the global byte, a stack byte,
  and a record byte that no rule reads. Global labels can overlap record
  fields. All 47 words are dynamically exercised; full RAM/GPR/FPR/events/
  visits and ordered access traces agree.
- Native32 O0/O2/O3 with trapping UBSan pass 1,572,864 positive cases per
  profile. All 65,536 type/subtype pairs run with two global states, two tag
  states and six valid output layouts. Compare the whole record, separate
  output byte and global byte. Eight deliberate variants fail by result:
  exact-one global gate, wrong tag/subtype/type codes, pre-cached fields and
  an early return. The native contract uses valid byte objects and aliases.
- 56 fired read/write prefix pairs preserve private state, trace and PC/delay
  ownership. A no-match sparse mapping needs no output mapping or store.
- Three dedicated GNU layouts pass 18 rebase cases, including signed-low
  carries for both bindings; alias links are additional. Three raw-word/
  binding corruptions and six full-image corruptions fail closed.
- An actually compiled early-return mutant is rejected: a global rule writing
  zero must still permit a later type-8 rule to write two. No fixture failures
  or production adjustments were needed for the passing qualification.

Routine Claude calls: zero.

## Production, recount and banking

Actual production Make reproduces the independently predicted entire ELF:
129 changed code bytes plus one function-size byte, 130 total, zero exclusions.
Only the target extent changes 12->188. All other named definitions, all 6,056
function addresses and 6,055 other bodies remain fixed. Protected Game data
remains exact across 720 owners /189,088 bytes. No metadata cycle is introduced.
Inventory, guard CSV and shared headers remain byte-identical.

ELF SHA-256:
`62095f23df6993e6bdd474197951164e05d56cc37b827318dc414c1b5975e664`.
Unchanged Native CRLF guard SHA-256:
`f867c3817abab6b6ef822343afa48a4b188e7067ce1d4c69a078b54a6f4b4c40`.
The Native/cache seal covers 16,202 inputs and 184 focused inputs. Recount the
captured adopted Native ELF with the unchanged C inventory:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,833 /5,506 (69.61%) | 1,673 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,160 /4,833 (65.38%) | 1,673 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only `func_15159370` becomes exact. Converted totals remain fixed. Threshold
4,130 leaves 297 more matches to 75%. The remaining source screen contains
1,544 placeholders, 120 semantic/other definitions and nine unlocated entries.

Predecessor consumer `94c18635780f95de8421398f62c0b4c5206d5f11` and tools
`9c51017daf06d0cd156a4f1556dbd2dd2566d231`. Bank tools first at
`5f661001c850cfffa0351221addb73f3b20c4128`, then source, consumer pin and
measured documentation. Preserve the older mirror's 1,720 inherited dirty
paths plus two new tools files without committing its independent history.
No push. The root README changes only its two aggregate matching rows.

Refresh ten changed C/Markdown/tool sources with Graphify, preserving all old
nodes and still-valid relationships/contexts. The target retains its s32
return and gains byte-pointer parameters; it remains a leaf. Keep outside
freshness and communities historical, with no full-corpus extraction or global
clustering/centrality claim. Receipts and independent final audit remain in
`conker/build/game-record-priority-classifier-match/`.

Next inspect `func_15171F04` in `generated_19F150` using a new frozen
predecessor and caller/ABI audit. Keep `func_1514E920` private and uncredited.
The 75% goal remains active.
