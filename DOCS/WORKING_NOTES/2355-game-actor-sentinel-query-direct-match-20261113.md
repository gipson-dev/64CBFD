# Game actor sentinel query direct match

Date: 2026-11-13. `func_15037880` in `generated_64120.c` replaces a
zero-return placeholder with its complete actor override query. The 87-word
retail body at VA `0x15037880..0x150379DC` / ROM `0x64D30..0x64E8C` emits
directly from C with the original bindings and no new guards. Both object
padders reproduce the complete body and relocations.

The routine indexes the `0x32C`-byte actor table and selects the low three
bits of its `+0x2F8` halfword. Mode 1 writes three floats from the current
view, reloading the view pointer before each store. Mode 2 normally writes
three signed-halfword reference coordinates as floats. For actor type 4, it
first compares the squared horizontal distance against `D_8009862C`; if the
threshold is exceeded, it returns success without writing. Mode 3 likewise
returns success without writing; other modes return zero. The actor index is
not validated by this routine. The output and global fields can overlap, so
access and reload order matter. Existing callers at `0x15037B08` and
`0x1503B750` use the return value to decide whether to run a fallback query.

Tools commit `6f094f6` supplies the reproducible qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_actor_sentinel_query_15037880_match -v
```

An independent model passed 17,280 guest cases across retail, raw C and both
padded streams, including signed reference coordinates, threshold boundaries,
quiet-NaN threshold, negative and positive indices, and output overlaps with
the view pointer, view data, reference coordinates, actor data and stack.
Fifty-one access cuts agreed in complete modeled state, and nine null-output
paths covered both no-write success and write faults. Connected tests exercised
288 cases through the original sentinel fallback caller and 864 cases through
the second caller window, with the remaining fallback provider modeled.
Native 32-bit execution passed 1,440 cases at each of `-O0`, `-O2` and `-O3`
with UBSan and nine effective negative controls. Twelve GNU links used three
address layouts. These tests do not establish floating-point exception-state,
portable C fault behavior, full fallback-provider behavior, hardware or live
gameplay acceptance.

The pre-install suite passed in mounted tools and with staged sibling
dependencies. Three existing sibling helper files differ from mounted tools,
so both sets were exercised separately. The shared project-tool check passed.
The installed production owner and ELF match the independently audited shadow
byte-for-byte, and the other 1,453 linked objects are unchanged. The strict
image audit accounts for 270 changed bytes with zero exclusions, including a
closed `D_8009862C` / `D_8009DA5C` symbol metadata reorder. Only the target
body changes; all 6,050 function addresses and all 189,088 protected Game-data
bytes remain fixed. The other 18 owner functions, constant pools, existing
guard manifest and compiler diagnostics are unchanged. The existing duplicate
`generated_12D630` Make recipe warning remains.

A fresh recount reports Game **3,744 / 4,842 (77.32%)**, total **4,417 /
5,515 (80.09%)**, zero address drift, and **130** more Game matches required
for 80%. Continue the broader Game matching goal. Routine work used zero
Claude calls.
