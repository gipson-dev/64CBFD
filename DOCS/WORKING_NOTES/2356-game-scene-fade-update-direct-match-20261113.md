# Game scene fade update direct match

Date: 2026-11-13. `func_151E4EE8` in `generated_20AE20.c` replaces a
zero-return placeholder with the scene fade and completion-callback update.
The 83-word body at VA `0x151E4EE8..0x151E5034` / ROM
`0x212398..0x2124E4` emits directly from C with the retail relocations and
no new guards. Both object padders reproduce the same body and bindings.

The routine derives a float fade value from byte `D_800E0B96`. Rate
`D_8008FD74 == 255` uses the first `D_800DDDC8` channel as a threshold
gate, advances the byte with wraparound and updates `D_800DDDD8` using
the `0x55` split. It dispatches the completion callback only after the
level and `0x6E` byte conditions are met. Other rates add the low 32 bits of
the tick/rate product, clamp signed results at 255, and dispatch when the
initial byte is already 255. Completion writes alpha 255, rate 8 and fade
1.0 before calling the pointer in `D_800E0A88`. These stores precede the
callback and can be changed by it. The floating comparison behavior for NaN
is retained.

The retail table `D_8008FDEC` stores this routine at index 7
(`0x8008FE08`, ROM `0x2348C8`). The original
`func_151E51EC` dispatch window at `0x151E5294..0x151E52B4` indexes
that table and calls through it. The callback setup and use are also
documented in Notes 1797 and 1804. This qualification exercises the dispatch
window and models the callback; it does not qualify complete parent or callback
implementations.

Tools commit `c173153` supplies the reproducible qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_fade_update_151e4ee8_match -v
```

The independent guest model passed 3,840 cases for retail, raw C and both
padded instruction streams, including wraparound, signed product boundaries,
thresholds, NaNs and callback mutations. The original table-dispatch window
passed 162 cases per stream, and 60 access-cut prefixes agreed in complete
modeled state. Native 32-bit execution passed 3,840 cases at each of `-O0`,
`-O2` and `-O3`, with UBSan and six effective negative controls. Twelve
GNU links used three symbol layouts. These checks do not establish FPU
exception flags, portable C fault behavior, complete callback behavior,
hardware behavior or live gameplay.

The suite passed before and after installation in mounted tools and with
staged sibling dependencies, without changing the sibling checkout. The
project-tool check passed. The production owner and ELF equal the audited
shadow, and the other 1,453 linked objects remain unchanged. The strict
whole-image audit accounts for 357 changed bytes, including closed symbol
metadata reorderings, with zero exclusions. Only this body changes among
6,050 functions; every function address and all 189,088 protected Game-data
bytes remain fixed. The other 59 owner functions, constant pools, compiler
diagnostics and existing guards are unchanged.

A fresh production recount reports Game **3,745 / 4,842 (77.34%)**, total
**4,418 / 5,515 (80.11%)**, zero address drift, and **129** further Game
matches required for 80%. Continue the Game matching goal.
