# Game contact-effect update match

Date: 2026-11-13. `func_1516A3F4` in `generated_197120.c` replaces its
zero-return placeholder with a recovered height and contact-effect update.
Its 81-word body occupies VA `0x1516A3F4..0x1516A538` and ROM
`0x1978A4..0x1979E8`. Seventeen relocation-aware expected-word guards
normalize compiler register allocation and an independent store/move schedule.
Both supported padders reproduce the complete retail instruction body and
relocations. The recovered C preserves the original 80-byte frame, the
threshold spill, and the location of the partially initialized descriptor.

The routine captures a threshold from two signed record halfwords. When the
current height reaches that threshold it selects the query context and updates
height through `func_1510F8D8`. Depending on the resulting height it clears
the record timer and can submit a 24-byte effect descriptor, or scales two
signed motion halfwords. `func_15167AD8` copies all 24 descriptor bytes,
including the padding and untouched tail; the checks retain those bytes.
The modeled helpers can mutate the record between the original accesses.

The target is entry 7 of `D_8008C9C8`. The original caller windows in
`func_15167E0C` and `func_15168870` select that entry via signed bytes at
record offsets `0x2F` and `0xB2`, then pass the record in A0. Their bounded
windows passed 144 cases per stream. They do not qualify complete parents or
establish every source of the selector bytes. The initial investigation and
its descriptor-array distinction are preserved in [Note 2360](2360-game-contact-effect-private-screen-20261113.md).

Tools commits `42b87d1`, `1a473f6`, and `666d599` provide the reproducible checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_contact_effect_1516a3f4_match -v
```

An independent guest model passed 640 cases per stream across retail, raw C,
and both padded bodies, including all descriptor bytes and helper mutations.
Retail and both padded streams agree at 94 selected access-boundary prefixes.
Native 32-bit checks passed 160 cases at each of `-O0`, `-O2` and `-O3`,
with UBSan and seven effective negative controls. Twelve GNU links across
three symbol layouts verify the guarded outputs against rebased retail. The
suite passed both before and after installation with mounted tools and staged
sibling dependencies; project tool checks passed. These tests use modeled
helpers and do not establish arbitrary aliases, floating-point exception flags,
the complete caller/helper behavior, or live gameplay.

The actual production object and ELF match the audited Make-planned shadow;
the other 1,453 input objects remain unchanged. The independent strict-image
prediction accounts for 244 changed bytes with zero exclusions. Only this
body changes among 6,051 functions; every function address and all 189,088
protected Game-data bytes remain fixed. All three neighboring owner functions,
constant pools and compiler diagnostics remain unchanged.

A fresh production recount reports Game **3,750 / 4,843 (77.43%)**, total
**4,423 / 5,516 (80.18%)**, zero address drift, and **125** further Game
matches required for 80%.
