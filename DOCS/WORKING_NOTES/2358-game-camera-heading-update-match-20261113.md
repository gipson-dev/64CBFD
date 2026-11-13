# Game camera heading update match

Date: 2026-11-13. `func_15122980` in `generated_14F8F0.c` replaces a
zero-return placeholder with its recovered camera-heading update. Its
87-word body occupies VA `0x15122980..0x15122ADC` and ROM
`0x14FE30..0x14FF8C`. Twelve expected-word guards adjust the compiler's
stack frame and local offsets to the retail layout; all other words and all
relocation bindings emit directly from C. Both object padders reproduce the
complete retail body.

Unless camera state `+0xDC` is 4, the routine computes two direction
vectors relative to `+0x2F8`, obtains their headings, and sets smoothing
target `+0x8D4` to 0, 0.5 or 0.75 according to the halfword at `+0x298`,
flag `0x100000` and the open 180-to-270-degree interval at `+0x390`.
It advances the smoothing state at `+0x8DC/+0x8D8`, adds the wrapped
heading difference multiplied by the resulting value to `+0x37C`, and
updates `+0x39C` with the factor at `D_800A34A0`. The three trailing
camera helpers run in order even when the main update is skipped. Helper
effects are observable: the heading, smoothing value and factor are read at
their retail points, and NaN follows the original ordered comparisons.

The retail callers include `func_151220D0` and `func_15122170`; their
call windows at `0x15122158` and `0x15122198` are exercised. The
camera-mode dispatcher also reaches this target as recorded in Note 2018.
The helper implementations and complete parent functions are not newly
qualified by this bounded call-window test.

Tools commit `c08c34f` supplies the reproducible checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_camera_direction_15122980_match -v
```

The independent guest model passed 448 cases across retail, raw C and both
padded streams, including thresholds, NaNs and helper mutations. Modeled
helpers overwrite outgoing argument slots as well as caller-saved registers.
The two caller windows passed 192 cases per stream; 77 access-cut prefixes
matched for retail and the guarded streams. The unguarded C frame differs,
so it is checked against the independent semantic model instead of claiming
identical raw stack traces. Native 32-bit execution passed 224 cases each at
`-O0`, `-O2` and `-O3`, with UBSan and seven effective negative controls.
Twelve GNU links used three symbol layouts and verified both guarded streams
against rebased retail. These checks do not establish floating-point exception
flags, portable C fault behavior, complete helper behavior or live gameplay.

The focused suite passed in mounted tools and with staged sibling
dependencies, including after installation; the sibling checkout remains
untouched. Project-tool checks passed. The production object and ELF equal
the audited shadow, and the other 1,453 linked objects remain unchanged.
The strict full-image audit accounts for 316 changed bytes and closed symbol
metadata reorderings with zero exclusions. Only this body changes among
6,050 functions; all function addresses and all 189,088 protected Game-data
bytes remain fixed. The other owner function, constant pools and diagnostics
remain unchanged, and the 12 guarded rows are appended to the existing
manifest.

The randomized scatter candidate `func_1517AA20` remains private: a direct
typed call changes an unfinished neighbor and its compiler schedule still
differs. It has not been counted.

A fresh production recount reports Game **3,747 / 4,842 (77.39%)**, total
**4,420 / 5,515 (80.15%)**, zero address drift, and **127** further Game
matches required for 80%. Continue the Game matching goal.
