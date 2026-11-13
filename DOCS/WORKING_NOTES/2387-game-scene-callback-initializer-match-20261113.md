# Game scene callback initializer match

Date: 2026-11-13. `func_15010880` replaces the zero-return placeholder in
`conker/src/game_3DC30.c`. The 84-word retail body occupies
`0x15010880..0x150109D0`, ROM `0x3DD30..0x3DE80`.

The routine submits the scene setup arguments, installs `func_150DE32C` as
a callback, constructs a 12-byte record containing two offsets from the live
resource-table pointer, and copies it to an allocated record if allocation
succeeds. A flag on the live state controls a second allocation. The copied
record's two padding bytes retain their incoming stack contents. The local
declarations use the resource table's pointer representation and the allocator's
integer payload-size argument without changing the shared headers.

The complete 84-word routine comes from C. Eleven relocation-aware guards
reorder a closed group of existing instructions to place the callback store
before the independent resource-pointer load, matching retail; no instruction
is inserted or omitted. The two affected global words are distinct at their
retail addresses. An aligned ROM scan found no direct JAL to this function and
one literal pointer at `0x2278A0`, index 20 in `D_80082D90`. This does not rule
out dynamically constructed calls.

Tools commit `0948ceb` supplies the reproducible checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_intro_init_15010880_match -v
```

The checks cover 256 cases per retail, raw-C and padded guest stream against
an independent state/call model, including null allocation, wrapping address
arithmetic, live helper mutations and copied stack padding. They also cover 57
retail/padded fault prefixes, 128 cases through the original
`func_1500E470` indirect-dispatch window up to its next helper, and 64 native
32-bit cases each at O0/O2/O3 with trapping UBSan. Seven compiled incorrect
variants are rejected. Eight GNU links cover four address layouts, and 44
stale word/relocation guards reject across both padders; the generated-padder
layout for that check is synthesized from the retail slot boundaries. The
allocator, scene setup and copy providers are modeled, and the caller check is
a bounded window, not complete runtime or gameplay validation.

The focused suite passed in the mounted tools and an isolated sibling overlay
before and after installation; the overlay uses mounted fallback modules. The
sibling's 2,434 pre-existing dirty paths were preserved. Project-tool checks
also passed. The actual Make build and independent whole-image audit account
for 276 changed bytes with zero exclusions. Only this body changes among 6,051
functions; all addresses and all 189,088 protected Game-data bytes remain
fixed. Only `game_3DC30.c.o` changed among 698 fingerprinted linked objects.
The conversion CSV and prior guard rows are unchanged. The scoped Graphify
refresh retained all 60,058 prior node IDs and was not a full-corpus extraction.

Fresh production recount: Game **3,773 / 4,843 (77.91%)**, total
**4,446 / 5,516 (80.60%)**, zero address drift. **102** more Game matches are
required for 80% at the current denominator.

Next private screen: `func_1512DD50` builds an inline normalized line record.
Its old commented draft incorrectly treats the two inline structures at owner
offsets `0x6FC` and `0x870` as pointers. A corrected initial owner screen
preserves its sole neighbor and pools but emits 86 words versus 85 retail, with
81 same-position differences. It remains unqualified and uncredited; the
retail floating-point order and the helper's ability to modify the owner must
be preserved in subsequent work.
