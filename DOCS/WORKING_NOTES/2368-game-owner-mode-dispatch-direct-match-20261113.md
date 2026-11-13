# Owner-mode dispatch direct C match

Date: 2026-11-13. `func_1514EA1C` in `generated_179F30.c` now matches all
84 retail instruction words at VA `0x1514EA1C..0x1514EB6C`, ROM
`0x17BECC..0x17C01C`. Its code and helper calls emit directly from C with no
new guards. The callback dispatches modes 3 through 12 to
`func_1518E37C`, choosing values 2, 3, 5 or 6 and consulting owner byte
`0x22` for three modes. Other modes forward all three arguments and the
return value to `func_1514E89C`; handled modes return 1.

The compiler-generated ten-entry switch table has the same target offsets as
retail `jtbl_800A5E20`. The owner's Makefile setting binds its `.rodata`
relocation to that existing table; the generated padder restores the original
internal jump labels. No new table is linked into the image. Both padding
paths reproduce the target instructions and bindings, and all 77 other owner
functions remain unchanged. The original indirect dispatch window in
`func_1514D3B0` indexes callback table `D_8008AB64`, whose entry 4 points to
this function, and forwards the payload, mode and context.

Tools commit `68a349c` supplies the checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_owner_mode_1514ea1c_direct -v
```

An independent guest model passed 720 cases per instruction stream. The
original indirect-dispatch window passed 180 modeled cases per stream, and
210 cases per stream execute the original delegate and setter instructions;
the setter's nested cleanup remains modeled. Another 288 cases exercise
deliberate owner overlaps with stack and table storage, and 19 injected
access-boundary prefixes compare complete modeled states. Native 32-bit
checks passed 855 cases at each of `-O0`, `-O2` and `-O3`, with UBSan and
seven effective negative controls. Twelve GNU links across three layouts
verify the code and table bindings. The seven tests passed before and after
installation with mounted tools and staged sibling dependencies, and project
tool checks passed. These checks do not establish full caller behavior,
hardware faults, the nested cleanup implementation or live gameplay.

The production object and ELF match the independently audited Make-planned
shadow. The strict image prediction accounts for 271 changed bytes with zero
exclusions, including an explicitly checked linker symbol-order swap between
`jtbl_800A5E20` and `D_8009F890`. Only this function body changes among
6,051 functions; all addresses and all 189,088 protected Game-data bytes are
unchanged. The other 77 owner functions, pre-existing data, normalized
compiler diagnostics, existing guards and other 1,453 linked objects are
unchanged.

The actual recount is Game **3,756 / 4,843 (77.56%)**, total
**4,429 / 5,516 (80.29%)**, zero drift, with **119** more Game matches
required for 80%.
