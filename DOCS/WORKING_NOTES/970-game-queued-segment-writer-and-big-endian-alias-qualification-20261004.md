# Game Queued Segment Writer And Big-Endian Alias Qualification

Date: 2026-10-04. Starting HEAD: `eb906080`.

Subsequent [Note 972](972-game-palette-color-emitter-byte-match-and-segment-connection-20261004.md)
recovers color emitter `func_1510CDB8` with all 42 words raw-exact and qualifies
its actual writer connection. The next upstream source is palette updater
`func_1510CB10`; this note's writer measurements and rendering boundaries stand.

## Decision

Continue [Note 969](969-game-immediate-texture-cache-release-recovery-20261004.md)
by replacing `func_1510D8C0`'s zero-return placeholder with its actual
`Gfx *` queue writer. Use the existing SDK `gSPSegment`, not hand-encoded
commands. It fits 40 body words in the 44-word retail slot, without a frame,
new guards, compiler profiles, ownership changes or drift. It remains
non-matching at **38 raw word positions**; no byte-exact claim.

Existing queue reset `func_1510D864` and append `func_1510D874` stay unchanged
and raw-exact across their complete four- and nineteen-word slots. README
aggregates stay unchanged because the writer was already counted as C.

## Queue And Command Contract

`D_800D9ED0` is the unsigned count byte. `D_800D9ED8` contains eight
sixteen-byte entries: key at zero, first address at four, optional second
address at eight, unsigned segment bytes at twelve/thirteen, and two untouched
bytes. The eight-entry table ends at `0x800D9F58`, the existing dirty-minimum
global; do not treat it as a 255-entry production allocation.

The writer takes a Gfx cursor and signed 32-bit key. Capture the initial
unsigned count and return the unchanged cursor for zero. Scan in order, using
the cached count on mismatches. On a matching key, emit the first segment
command even when its address is zero. Refresh count only after matching
command stores. Queue contents/count are not otherwise cleared or consumed.
Return the cursor advanced by eight bytes for each emitted command.

The SDK F3DEX2 macro emits `0xDB060000 | ((segment * 4) & 0xFFFF)` followed
by the full unmasked address word. Segment inputs remain unsigned bytes,
including 128..255; no four-bit segment normalization or physical-address mask
is invented. Store the command header before reading/storing its address.
Test the second address only after first-command stores. If nonzero, read the
second segment byte, store its command header, then **reread the second address**
for that command's data. Output aliases can therefore change the gate, segment,
data and subsequent keys. Do not cache these reads ahead of stores.

No output-capacity check, count clamp, NULL guard or validation is invented.
Complete ordinary queue workflow is qualified for counts 0..8 and mapped
output storage. Corrupt counts above eight and count/output overlaps are tested
only against deliberately extended mapped fixtures. They prove the original
unclamped behavior, not safety of indexing beyond the real queue.

## Verification

Ten new checks in
[`test_game_queued_segment_writer.py`](../../tools/tests/test_game_queued_segment_writer.py)
extract the actual reset/append/writer C and SDK macros from project headers.
Strict 32-bit native fixtures connect reset -> append -> writer, verify command
words and return cursor, and exercise all 256 append-count values: counts at
least eight reject without modifying entries, smaller counts append exactly one
entry and truncate segment arguments to bytes. Reset changes only count.

For byte aliases, native little-endian execution is not substituted for N64
behavior. A bounded big-endian low-word instruction oracle reuses the project's
`TimelineOracle` operations, adding these leaves' signed comparisons and branch/
branch-likely delay handling. It runs both checksum-verified retail words and
the current production C words and compares complete mapped memory, ordered
data reads, ordered stores/values, return cursor and callee-saved registers.
It is not a full MIPS emulator or physical guest execution.

**898 paired instruction traces** cover:

- Actual reset/append/writer connection, including rejecting the ninth append
  and the append helper's count-store-before-final-segment-store ordering.
- Empty queues with zero, ordinary and high-address cursors, without entry reads.
- All 256 segment bytes, zero/nonzero second addresses, signed/high-bit keys,
  sparse matches, full address words and matching-only count reloads.
- All 256 writer counts on an explicitly extended nonmatching-entry fixture.
- Aligned queue/output overlaps that modify current/later input words and bytes.
- A count/output overlap where big-endian `0xDB060008` changes count from one
  to 219, extending the scan only within additional fixture storage.

Representative alias results are independently asserted, not only paired:
with output at the current entry, the second header replaces its source address
and the fresh data load returns that header. With output eight bytes into the
entry, the first command data `0x12AB5678` changes the second segment to `0xAB`,
giving second header `0xDB0602AC`. These would not be equivalent native-byte
observations on a little-endian host.

Coverage includes every non-padding instruction address in both the forty-word
C body and forty-one-word retail body, including actually executed delay slots.
Independent fresh IDO O2/g3 compilation and MIPS linking reproduce complete
production slots without instruction normalization. Assembly annotations are
independently compared to the checksum-verified ROM, including padding. No
expected-word guards are present for this writer.

| Complete Slot | SHA-256 |
| --- | --- |
| `func_1510D8C0` C, 44 words | `f3a227545fc8d35dd017430e12f6fd1da0512c5746e400423358eee3a9566feb` |
| Exact reset, four words | `e81b7668246b58e182518ea12697cbf47014a01b764ea1a2dc2f1e8ce2d55a31` |
| Exact append, nineteen words | `5ca5af947408d6055c1fdf4ce2c517d915c75c052975430b17056b22969beffb` |

Bounded compiler-shape trials do not improve matching: a separate first/last
cursor local produces 41 words with 39 differences; volatile count and reversed
entry/count declaration order retain their respective 40/38 or 41/39 results.
Keep the SDK-based forty-word body; do not add an override or guards.

**All 237 combined checks pass in 57.937 seconds, no skips.** This is the
previous 227-check command plus the new ten-check module. Fresh production
compile/padding/link/progress/matcher succeeds. Existing duplicate
`generated_12D630` recipe warnings remain; no new source warning.
Complete Init code/data, Debugger code and Game data remain raw retail-exact;
prior recovery identities, including the immediate-release body, stay intact.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_queued_segment_writer -q -f
make tools-check
git diff --check
```

Fresh totals stay 3282 / 5463 exact C functions, zero drift, 2181 different:
Init 492 / 492, Game 2609 / 4790, Debugger 181 / 181. No production Init
conversion or README aggregate change. Recovery narration remains in docs.
No hardware/RSP/RDP, natural rendering, ROM promotion or PC acceptance claim.

## Sibling And Next

Read-only audit finds active sibling `recomp_out/.c` line 822945 already has
the complete original recompiled writer, including both address loads and late
count reload. The scoped host `src`/CMake search finds no named override.
Its presence is not fresh runtime proof. This differs from Note 969's immediate
release helper, which remains a separate PC stub synchronization task. No host
source/build/save or frozen Release changes are made.

Retail `func_151137D4` calls color emitter `func_1510CDB8` at `0x15113AC8`,
passes its returned cursor to this writer at `0x15113AD4`, and uses the returned
cursor afterward. The caller is not newly source-recovered or behavior-qualified.
This direct connection sets the next source target to **`func_1510CDB8`**, its
42-word primitive/environment palette-color emitter. The neighboring object
constructor remains a separate recovery task. Preserve unsigned RGB reads,
low-byte alpha truncation, three-byte palette stride, full store/read ordering
and the two-command cursor advance.

- [x] Recover the writer with the actual SDK macro and correct pointer result.
- [x] Connect actual queue reset/append/write and retain both exact helper slots.
- [x] Qualify big-endian aliases and every body instruction in bounded fixtures.
- [x] Preserve complete Init/Debugger/data and previous recoveries.
- [x] Recover color emitter `func_1510CDB8`, then qualify its writer connection (Note 972).
- [ ] Recover/qualify the full render caller and real RSP/RDP/natural effects.
- [ ] Pursue raw matching separately; 38 word differences remain.
- [ ] Identify and qualify the staged texture producer separately.
- [ ] Synchronize the PC immediate-release stub as its own qualified host change.
