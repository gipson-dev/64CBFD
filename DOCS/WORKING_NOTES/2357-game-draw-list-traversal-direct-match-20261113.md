# Game draw-list traversal direct match

Date: 2026-11-13. `func_15188D00` in `generated_1B5CC0.c` replaces a
zero-return placeholder with the selected-list renderer. The 82-word body at
VA `0x15188D00..0x15188E48` / ROM `0x1B61B0..0x1B62F8` emits directly
from C with the original relocations and no new guards. Both object padders
reproduce the entire body and its bindings.

The routine reads the indexed head from `D_800DF7C8`. An empty list returns
the incoming display-list cursor. A nonempty list emits the retail matrix,
geometry, pipeline, alpha-compare and conversion commands, then dispatches
each node through `D_8008D590[node->active]`, passing the cursor, node and
signed 16-bit view. The callback's return becomes the next cursor, and the
next pointer is read after the callback, so callback mutations can affect
traversal. Neither list index nor handler index is checked by the retail
routine. The original `func_150195A0` window at
`0x15019868..0x15019898` calls this routine for lists 0 and 1 in sequence,
passing the first return to the second. The handler table contains
`func_151895F4` and `func_151897A4`; the former is still a placeholder.
This work models the handlers rather than qualifying their full behavior.

Tools commit `7c0cb6b` contains the reproducible qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_draw_list_15188d00_match -v
```

An independent guest model passed 4,608 cases across retail, raw C and both
padded streams, including empty and multi-node lists, signed views, list-head
overlap and callback mutations. The original paired caller window passed 160
cases per stream, and 126 access-cut prefixes agreed in complete modeled
state. Native 32-bit execution passed 240 cases each at `-O0`, `-O2` and
`-O3`, with UBSan and six effective negative controls. Twelve GNU links
used three symbol layouts. These checks do not establish portable behavior for
invalid pointers, complete handler behavior, rendered output, hardware or
live gameplay.

The suite passed before and after installation in mounted tools and with
staged sibling dependencies, without changing that checkout. Project-tool
checks passed. The production owner and ELF match the independently audited
shadow, and the other 1,453 linked objects are unchanged. The strict image
audit accounts for 261 changed bytes with zero exclusions. Only this body
changes among 6,050 functions; all function addresses and 189,088 protected
Game-data bytes are unchanged. The other 14 owner functions, constant pools,
compiler diagnostics and existing guards are unchanged.

The screened view initializer `func_15017640` remains private: its retail
loop and scheduling still differ. The independent slot-notification candidate
`func_15156028` also remains private pending exact code generation and
qualification. Neither is credited in the recount.

A fresh production recount reports Game **3,746 / 4,842 (77.36%)**, total
**4,419 / 5,515 (80.13%)**, zero address drift, and **128** further Game
matches required for 80%. Continue the Game matching goal.
