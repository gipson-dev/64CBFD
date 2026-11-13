# Game trajectory callback and separate no-op restoration

Date: 2026-11-13. `func_15072F10` in `game_981E0.c` replaces a zero-return
placeholder with semantic C. The 81-word recorded retail slot at VA
`0x15072F10..0x15073054` / ROM `0xA03C0..0xA0504` now matches retail.
The first **79 words** are the main callback. The last two are a separate
`jr`/`nop` callback at `0x1507304C`, independently referenced by the callback
table; they are restored by checked insertions, not represented as another C
function. The generated ELF does not yet provide a separate symbol for that
entry. The combined slot uses 19 checked relocation-aware guards, including
the two insertions. Both independent padders reproduce the complete slot.

The main callback reads the active actor's signed pitch, decrements a nested
16-bit timer, calculates a direction using `func_1505A184`, then reloads the
active actor and submits the scaled world position through `func_150E1570`.
It forwards the latter's return value. The table at `D_8008630C` selects the
main callback at index 177 and the independent no-op at index 180; the original
lookup window and both entry addresses were checked. The linked production
image now contains `jr`/`nop` at `0x1507304C`, where the placeholder build
had zero-filled padding.

**Remaining dependency:** `func_150E1570` is still a zero-return C placeholder
in `generated_10EA20.c`. The target instruction match and bounded helper
models do not establish its gameplay behavior. The deeper trigonometric calls
and final submission helper are modeled in these tests, and no hardware or
gameplay acceptance is claimed.

Tools commit `d86cb2e` provides the qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_state_trajectory_15072f10_match -v
```

All eight checks passed before and after installation using mounted tools and
staged sibling dependencies. They include 4,800 independent-model cases,
392 deliberate stack-overlap cases (eight stopped with matching modeled
exceptions), 274 actor/state overlaps, a timer/global-pointer overlap,
160 cases through the original vector helper with its trig calls modeled,
and 576 modeled memory-access cuts. The native 32-bit candidate passed 2,400
cases at each of `-O0`, `-O2`, and `-O3` with UBSan and ten effective negative
controls. Twelve GNU links exercise three symbol bases. The isolated no-op was
executed with eight initial register/stack combinations; the original callback
lookup window selected both table entries. These models do not establish
portable C fault behavior or hardware floating-point exception behavior.

The actual Make build matches the independently audited shadow ELF, binary
and owner object. The strict image audit accounts for **261** changed bytes
with zero exclusions; only the recorded target slot changed, all **6,050**
function addresses stayed fixed, and all **189,088** protected Game-data bytes
were unchanged. All 327 other owner functions, the other 1,453 linked objects,
constant pools, 36 existing compiler warnings and conversion rows were
preserved. A fresh linked recount reports Game **3,741 / 4,842 (77.26%)**,
total **4,414 / 5,515 (80.04%)**, zero drift, and **133** more Game matches
needed to reach 80%.

Next inspect the called `func_150E1570` in `generated_10EA20.c`, including
its caller-visible return, original allocator/geometry contracts and full
retail body. It remains unmatched and uncredited.

The scoped Graphify refresh retained or relocated all 59,965 previous nodes,
with 59,967 afterward and no out-of-scope changes. It retained 31,816 nodes
fail-closed; it was not a full-corpus extraction.
