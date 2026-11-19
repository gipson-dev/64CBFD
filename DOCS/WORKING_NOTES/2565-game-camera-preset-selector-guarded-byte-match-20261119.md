# Note 2565: Camera preset selector guarded byte match

Date: 2026-11-19. Consumer baseline `9808919ddb10f5617a247c2fdf4580dd471010a3`,
tools baseline `e11586b3ef2e2762f2eecee838f1ae391abe6e82`.
Matching tools are committed as `5cadd5afc6696360c90ea7efbd004204818fb5ae`.

`func_15123568` is installed as semantic C and matches all **90 words / 360
bytes / frame 0x18**, after **seven derived expected-word guards**. The
production zero-return placeholder is removed. The original assembly stays
unchanged. Actual production Make, the complete image prediction, installed
tests and the fresh recount pass.

Total is **4,559 / 5,514 (82.68%)**, Game **3,886 / 4,841 (80.27%)**,
Init **492 / 492**, Debugger **181 / 181**, with zero address drift and
955 different C functions. **128 additional matches** are needed for 85%.
Conversion remains **5,514 / 6,048 (91.17%)**, **86.19%** of bytes.

## Recovered behavior and ABI

Owner: `conker/src/game_14FF90.c`. VA `0x15123568..0x151236D0`, ROM
`0x150A18..0x150B80`. The interface is `void(struct108 *camera)`, with a
nonnull camera and the retail actor-pointer preconditions.

The attached actor's type 4, camera state and disable byte select a forced
preset 1 setup. Otherwise the routine decrements a positive integer cooldown,
clamping the wrapped 32-bit result at zero. Eligible input cycles backwards
through enabled presets, calls `func_15124B18` and `func_15125608`, and
starts a 20-tick cooldown. Preset1 has the original early return behavior.

Offset 0x7B8 is an integer cooldown here, although the shared incomplete
struct declares a float. A local typed alias view covers the cooldown,
reserved word and float distance at 0x7C0. Its GCC alias annotation preserves
native strict-aliasing behavior without changing the shared struct or other
functions. The unsigned subtraction preserves target wrap before the signed
clamp. Native builds explicitly mask variable-shift counts to reproduce
MIPS SLLV behavior; the IDO form already emits that single instruction.
Names are descriptive and are not claimed as recovered debug identifiers.

The first global float read precedes the preset store in the emitted body.
The final source assigns distance first; the compiler schedules the two
disjoint camera stores into retail order. The unsigned state comparison at
0x6FC also recovers retail's separately materialized constant 4.

## Guard derivation and owner boundary

Raw C has 90 words, frame24 and seven original relocation bindings. **83
words emit directly**. The seven guarded words contain two constant-one
register lifetimes (`v1` to `a1`), their halfword/branch uses, and the
loop-entry LI/BEQ schedule. The latter keeps the absolute branch target at
body+0x158 and executes the existing dead `t3` decrement in the retail delay
slot on the exit path. This changes no public memory, calls or preserved ABI
state. The complete raw fingerprint and each original word are checked.

No instructions are inserted or omitted. No floating operation, frame,
address binding, table or data changes are normalized. All seven original relocation bindings
remain unchanged. Six independent GNU rebases link both the compiled C and
freshly assembled, hash-pinned original assembly, with complete target-byte
equality after the same seven non-relocation guards.

All **44 other owner functions** match before/after in raw and padded form.
Constant pools, inherited five diagnostics and the register-mask union are
unchanged. The copied actual Make recipe reproduces the exact padded object.

The independent full-image prediction changes only this body, its symbol
size16 to360, and one adjacent GNU symbol/string-table pair
(`D_800A34D8`, `D_800991D8`). Named definitions are identical across that
bounded metadata permutation. The entire **3,254,384-byte ELF** matches the
prediction with **313 changed bytes and zero exclusions**. All 6,051 function
entries retain their addresses; only the target body changes. Protected data
is exact across **189,088 bytes / 720 owners**.

## Fresh qualification and production evidence

Tools: `experiments/game_camera_preset_15123568_match.py`, its manifest,
the guest/native helpers and `tests/test_game_camera_preset_15123568_match.py`.
Run from the prepared consumer root:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_camera_preset_15123568_match -v
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin --version us
make tools-check
```

- **268 guest cases per stream**, comparing literal retail, natural C and
  guarded C against an independent state/call model. They visit all 88
  reachable retail positions; the two compiler-left loads at words 27/37 are
  unreachable and remain byte-exact. Tests include gates, signed cooldown
  boundaries and wrap, preset masks, helper clobbers/mutations, byte/halfword
  widths, raw float bits, guest-only wrapped addresses and sparse aliases.
- **141 exact fault-prefix pairs** compare retail and guarded streams at
  actual memory accesses. Four effective instruction controls are rejected.
- Both original two-word direct call windows at `0x15122F40` and
  `0x1512819C` execute four cases each with the literal target connected.
  The complete ROM census finds those two JALs and no literal target pointers.
- **174 actual native SDK32 C cases each at O0/O2/O3**, with UBSan and
  strict aliasing, plus five executed semantic negatives per profile.
- **Twelve independent GNU links** cover six relocation rebases and all
  target bytes/bindings. All 360 raw byte corruptions and three whole-image
  corruptions are rejected by the focused fail-closed tests.
- Four-test suites pass in the primary checkout and isolated sibling overlay,
  both before and after installation. The paired installed runs record 313
  and 314 imported tool files; the extra overlay file is its empty bootstrap.
  Identical imported bytes are qualified. The real sibling's dirty status,
  HEAD and 343 dependency hashes are preserved; it is not edited or committed.
- Production Make rebuilds the guard-dependent objects and exits 0. All
  **1881 frozen inputs** are checked: only the declared source, guard table,
  target object and ELF change. Progress CSV stays byte-identical. Actual
  object/ELF equal the independent predictions. `make tools-check` passes.

Helpers remain bounded opaque providers; the two connected call windows are
not full-parent or hardware/gameplay acceptance. Native cases exclude sparse
guest aliases and incoming argument-home redirection. Degenerate enabled
masks are tested only on paths that bypass the potentially infinite retail
selection loop. Fault-prefix equality applies to emitted guarded instructions,
not portable C faults. Other unchanged function suites are not claimed fresh.

Private receipts: `conker/build/game-camera-preset-15123568-private/`,
including `production-audit.json`, installed suite reports, `qualified/`
contracts, whole-image receipts and `installed-recount.md`.

## Continuation and review

Zero Claude calls; this is a bounded reconstruction using existing local
compiler, guest, native and linking helpers. The actor-burst 591-word private
candidate and its prior handoff remain preserved and uncredited. Next inspect
the 93-word `func_15103AA0` timer/sound callback in `game_130CB0.c`.

Root README changes only its aggregate matching rows; recovery detail stays
here and in the concise DOCS indexes. This is decomp work; no host build,
Release artifact or real save changes.

Graphify's native update refuses a shrink and retains its old graph. A
scoped five-file AST merge and literal manifest target reference preserve
all 67,254 preceding IDs. This is not full-corpus re-extraction. The consumer
commit hook must finish before historical heading retention and the final
graph SHA are sealed in the private checkpoint.
