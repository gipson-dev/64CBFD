# Paired Record Event ABI And Candidate Rejection

Date: 2026-10-15

## Result

Recover and qualify the input/call contract of **func_1516F548**, not a new
production C match. Retail is **199 words / 796 bytes**, VA `0x1516F548`,
ROM `0x19C9F8`, frame `0xF8`, RA at SP+`0xCC`, in
[`generated_19A8B0.c`](../../conker/src/game/generated_19A8B0.c).
The zero-return placeholder remains unchanged. None of **33 diagnostic-free
source forms** passes the strict direct-match gate. **Zero functions credited,
zero new guards, zero profile or shared-header changes.**

This continues [Note 1405](1405-dual-factory-preset-direct-match-20261015.md),
whose 148-word direct match remains fixed. The complete additional-source /
Game goal remains active, including the
[failed-comment/binding/unanchored queues](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md)
and inherited-stack renderer deferral. The older 1,717-object and 801-file
audits are historical, not freshly rerun here.

## Recovered Interface

The additional source declares fourteen parameters named arg0..arg11,
arg15/arg16. That declaration places its final two arguments in the wrong
physical slots. Retail consumes **17 positions**, leaving **12..14 unused**.
Both original direct call sites supply those three unused words as well.

- Inputs 0/1/2: signed low-halfword coordinates.
- Input 3: captured unsigned halfword for the factories, but the final event
  reloads its **full word after both factory calls**.
- Inputs 4/6/9: captured unsigned bytes; input 5: captured signed halfword.
- Inputs 7/8: 32-bit left shift by 12, signed division by 4096, then signed
  low-halfword result. C shifts through `u32` to avoid signed-shift UB. Keep
  the actual retail branch/add/shift sequence as a separate matching demand;
  the independent packet reference uses the equivalent signed low 16 result.
- Input 10: first factory field 19, forwarded as a full physical word.
  Input 11: second factory field 19, read live after the first call.
- Input 15: low byte at incoming+`0x3F`, read before each factory call.
  Input 16: full word at incoming+`0x40`, read before each factory call.

The ten genuine saved words are x/y/z at SP+`0xF4/F0/EC`, byte4/byte6 at
`0xE8/E4`, width/height at `0xE0/DC`, half3 at `0xD8`, byte9 at `0xD4`, and
half5 at `0xD0`. The archive's `unkspF6/F2/EE` are **signed low-halfword
aliases of the initialized coordinate words**, not uninitialized variables.
Second-call coordinates use LH, other saved values use LW. Final-event
coordinates are reread through those signed aliases after the second call.

Both factory calls to **func_1516D99C** are unconditional and carry all
49 words. They use preset 13; field 19 selects input 10/11, and field 39
selects 0/6. All fixed fields, zeroes, signed sizes, saved parameters and live
tail words are tested, not merely sampled.

The final **func_1000FA64** packet has twelve words:
`7, x, y, z, 0x36B0, 1000, 100, func_1000EBC4, full_live_arg3, 0, 0, 0`.
Private declarations use the actual Init source types, including callback
`s32 (struct00 *, s32, s32, s32)` and the event's pointer-valued context.
The linked event and callback symbols bind to their proper addresses and
match all **109 / 24 words**. This is binding/static-byte evidence, not
execution of the Init queue, callback or game audio.

## Caller Boundary

Ignore-inclusive assembly/source/header search finds two direct calls, both
inside original **func_150265CC** in `conker/asm/50D80.s`:

| Setup Start | ROM | Words Through Actual JAL Delay | Call Site |
| --- | --- | --- | --- |
| `0x150270C8` | `0x54578` | 43 | `0x1502716C` |
| `0x15027174` | `0x54624` | 48 | `0x1502722C` |

Execute each original window with explicit prepared FP/stack dependencies at
two stack phases and stop only at the fired call boundary after the delay
instruction. All 17 words agree with the independently prepared expected
packet. Slots 12/13/14 are 190, slot 15 is 128, slot 16 is zero in these
fixtures. **Both current linked windows are still placeholders**, with no
matching words in the sampled windows. No full/current-caller or natural
gameplay execution is claimed.

## Compiler Screen

Use the existing IDO 5.3 retail owner profile and relative compiler paths.
The driver freezes **57 unique predecessor inputs** before compiling, adds
candidate-source SHA-256 to every result, and preserves all 29 other owner
functions' raw bytes, sizes, relative relocations and pools.

| Form | Words | Real Word Differences | Frame |
| --- | --- | --- | --- |
| Initial indexed homes | 211 | 205 | `0xF8` |
| Plain non-coordinate saved reads | 199 | 77 | `0x120` |
| Same, inline size computation | 199 | 77 | `0x118` |
| Same, short shift temporaries | 199 | 73 | `0x118` |
| Initial-input first packet / indexed saved reads | 199 | 162 | `0xF8` |
| Inline ten-word array | 211 | 205 | `0xF8` |

The ten-word array, aggregate/reverse-member layouts, narrower parameters,
indexed stores, ordinary/indexed coordinate reads and `register` declarations
do not close the gap. The tested full-size/full-frame form is
`candidates()['initial_inputs']`, SHA-256
`f438247d74e81f4e6c3f9088ee4f3b8ca4fc6e060d6394b4dddb0663464bf850`.
It preserves the normal packet contract but second-call width/height loads
use LH rather than retail's LW and the full schedule remains different.

**Measured:** plain saved reads retain a closer 199-word instruction shape
with an oversized frame; address-based reads can recover the frame but add
or move narrowing operations. **Hypothesis:** lexical debug homes and
across-call spill storage are not merging. No CFE/UOPT producer trace has
yet established that explanation for this function.

One bounded, read-only Claude advisory suggested an addressable aggregate
would merge the storage without extra narrowing. Fresh array/struct
compilations did **not** produce that proposed match. No advisory edits,
builds, tests or Git mutations occurred; Codex checked every suggestion.
No padding locals, volatility, incompatible function-pointer calls, frame
guards, broad factory-interface changes or profile adjustments were adopted.

## Verification

All **ten focused checks pass in 20.978 seconds**, exit 0:

- Assemble the original source independently and compare all 199 words to
  ROM. Keep all 57 current inputs byte-identical to their frozen captures,
  including the complete ELF, source owner, original assembly, archive input,
  guard CSV, progress rows, shared headers and build profiles.
- Verify all 49/49/12 packet words across **2,072 original guest cases**,
  both stack phases, full caller-saved clobbers, live incoming-home updates,
  saved-home writes and outgoing-home clobbers. Cover every original word.
- The C candidate agrees in **1,554 normal/live-input/outgoing-home cases**
  but rejects **all 518 forced private-home cases**. Physical provider writes
  to private locals are a guest qualification probe, not portable C behavior.
- Compare complete original-source/ROM private state at **1,152 fired memory
  fault prefixes**. Do not claim candidate fault-prefix equivalence.
- Run native 32-bit C at O2 and O0, **65,536 cases each**, plus **seven
  effective semantic negatives** with controlled exits. The 49-word capture
  provider checks source-expression forwarding, not the narrow production
  factory's complete native ABI or private guest stack mutations.
- Rebase original and candidate independently at three text locations,
  both call targets and callback signed-low carry boundaries. All original
  words match the independently rebased ROM prediction; normal candidate
  packets agree, but candidate instruction mismatch remains explicit.
- Connect freshly verified **125-word factory / 28-word allocator wrapper**
  bodies for **128 original/candidate pairs** covering independent null /
  success allocation results. Check both initialized records and the final
  event packet. Lower allocation/registration and the Init event are opaque.
- Qualify both original caller windows, unchanged 29 owner neighbors,
  all **57 before-capture corruptions** and a changed manifest. Reject wrong
  length/frame/word/diagnostic candidates before any adoption.

`make tools-check` and Windows syntax/standalone candidate checks pass in
active tools and the older mirror. The fresh official report remains:

| Section | Byte-Exact | Still Different | Address Drift |
| --- | --- | --- | --- |
| Total | 3,573 / 5,501 (64.95%) | 1,928 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,900 / 4,828 (60.07%) | 1,928 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversions remain unchanged. The root README is untouched, aggregate-only;
this investigation adds no decompilation credit.

## Banking And Next Work

Bank tools **07a68c3** first, then the consumer docs/pin. Preserve the
independent older mirror HEAD **ddbdd16** and every **680 initial dirty
fingerprint**. Copy only the two absent owned Python paths, giving **682
final dirty paths** with no overwrite, mirror commit/reset or history copy.
No push, installs, account changes, host build/launch or frozen Release action.
Eight scoped documentation files resolve **5,036 relative links, zero broken**.

Graphify's full update refuses **19,451 nodes against 41,230** and retains
19,398 nodes from 2,972 excluded-but-present files. Keep that fail-closed
result; do not force a smaller graph or install a different version. Await
the actual incremental commit workers separately.

Prepared WSL consumer-root reproduction:

```sh
python3 -m tools.experiments.game_paired_record_event --screen
python3 -m unittest tools.tests.test_game_paired_record_event -v
make tools-check
make -C conker match-progress NON_MATCHING=1
```

The driver without `--screen` intentionally fails qualification: the initial
211-word candidate is not an installable match.

1. Reuse the hash-gated compiler observation approach in
   `tools/experiments/game_table_fade_frame.py` and
   `game_actor_callback_frame_trace.py`, adapted to this exact owner/target.
   Observe CFE/UOPT/local reservation producers and actual exits, not just a
   hypothesized frame explanation. Preserve the baseline captures above.
2. Resolve genuine named-home/spill lifetimes and signed width/height reads
   without inventing storage or rewriting the frame through guards. Compare
   the correct-size/frame form against the closest ordinary-local form.
3. Repeat strict word/private/fault/native/rebase/chain qualification, verify
   production padding and independently close the complete linked-image
   change before replacing the stub. Update matching credit only afterward.

Do not start another broad conversion batch, silently accept private-state
differences, or treat any of the 33 source variants as another recovered
function. Continue the full additional-source/Game objective afterward.

## Post-Bank Verification

Consumer **7602b95b** banks the docs and tools **07a68c3** pin. All **ten
post-bank checks pass in 21.354 seconds**, exit 0. All 57 production inputs,
the complete ELF, the uninstalled stub, original guards/profiles and matching
counts remain unchanged. The normal ELF/progress targets are up to date.
Both active checkouts are clean before this receipt edit, and the root README
has no change relative to the preceding checkpoint.

Recheck older mirror **ddbdd16**: all **682 final fingerprints** remain fixed,
including every **680 initial dirty file** and both hash-equal owned copies.
The source commit's actual captured graph workers finish at **41,240 nodes /
81,337 edges / 3,964 communities**, without forcing the refused smaller scan.
Keep the compiler-home investigation and production-adoption gates above open.

## Resolution

[Note 1407](1407-paired-record-event-direct-match-and-compiler-spill-recovery-20261015.md)
resolves this handoff with actual compiler observations and a direct 199-word
C match. Repeated narrowed input expressions let UOPT create all ten real
spill homes without the duplicate CFE named-local reservation. The historical
33-form rejection results and captures above remain unchanged; the complete
private/fault and independent-image adoption gates are passed in Note 1407.
