# Palette-state initializer guarded byte match

Date: 2026-11-10. `func_15000940` replaces its zero-return placeholder with
semantic C for the selected palette-state initializer. The **95-word / 380-byte**
body and **0x28 frame** match retail after **73 relocation-aware word guards**.
This is a guarded match: the compiler does not emit the retail body directly.
The following one-word zero alignment pad is preserved independently.

The production ELF recount is **4,321 / 5,513 (78.38%)** total and
**3,648 / 4,840 (75.37%)** Game; Init **492/492**, Debugger **181/181**.
There are **1,192** different functions, zero address drift and **90** more
matches needed to reach 4,411/5,513 and 80% total. Conversion progress is fixed.

Baseline consumer `eb2b4a4007c04e79371df2ce5f731ea4387c0b57`, tools
`783ba489c1032f4fedd79f890a11d56e304415f5`. The eight target proof files were
banked first in tools commit `41b961316923b2371684a52e19d30658d029f3ad`; the
formatting-only fixture update followed in `a43eab262c74bbfd41805435331e17cc763d08fb`.
Local commits only.

## Behavior and interface

Owner `conker/src/game_2DDF0.c`; original retained at
`conker/asm/nonmatchings/game_2DDF0/func_15000940.s`. Body VA
**0x15000940..0x15000ABC**, ROM **0x2DDF0..0x2DF6C**; zero pad ends at
VA **0x15000AC0**, ROM **0x2DF70**. Its old 12-byte stub differed in 95 slot
words. The retained source interface is `void func_15000940(s32 unused)`: retail
saves the incoming A0 word but never reads it. This records the observed o32
word home without claiming the original source type. Retail's residual V0 is
not a proven return value.

The context byte at `D_800B0DF0->unk29` selects a three-byte entry in
`D_800A2CD0`. Its values select three RGB triples in `D_800A2CE8`,
`D_800A2CEC`, and `D_800A2D04`. Across four rows of three channels, clear
12 halfwords at `D_800D9E70`, repeat the three selected triples into
`D_800D9E88`, `D_800D9E98`, and `D_800D9EA8`, and clear 12 bytes at
`D_800D9EB8`. `D_800D9EB4` is a three-byte destination reset on each row;
it ends with the third selected RGB triple. No new selector bounds check is
invented. The eight actual preset entries have first index zero and second and
third indices 0..6. Tests outside that actual table domain are guest-only.

The sole direct JAL is VA **0x1500076C**, ROM **0x2DC1C**, in
`func_150006E0`; there are no aligned literal target pointers. The original
ten-word caller window includes the delay-slot float store and continuation;
the continuation overwrites V0 before reading it. The full parent remains a
placeholder and is not qualified as a whole.

## Compiler and closed guard recipe

The source uses the target-specific **O2/g3, no-unroll and no-constant-in-register**
profile, scoped to `game_2DDF0.c.o`. It emits 95 body words and the correct
frame and saved-register set, but 73 encoded words differ from retail. The
guard recipe pins the complete raw body and every relocation binding. It uses
every emitted instruction exactly once, maps the cursor and temporary register
roles, moves two invariant end-address pairs into setup, adjusts five equivalent
post-increment store offsets, and recomputes the two branch displacements.
No instruction is added or removed. The 73 expected-word guards carry moved
HI16/LO16 bindings and append to the existing manifest without altering its
prefix. Original assembly and the layout remain unchanged.

An affine modulo-32-bit instruction model compares 130 ordered memory accesses
and 16 loop decisions for symbolic input registers, loads and addresses. Both
forms preserve S0..S7, SP and RA for the normal disjoint stack/global domain;
raw V0 is caller-scratch. The proof treats HI/LO address pairs as address atoms;
16 independent GNU links separately test actual split relocations and carry
edges. It does not claim portable C fault behavior or arbitrary raw temporary
register equivalence.

## Qualification and production

* **304 cases / 912 executions** compare original, raw and normalized guest
  bodies, cover all 95 instructions, and include all eight retail preset entries,
  unused A0 patterns and 256 guest-only byte-index cases. Full machine equality
  is checked for normalized versus original; raw ordered memory traces agree.
* Native SDK32 tests execute **2,168 defined-domain cases per profile** at
  O0/O2/O3 with UBSan and strict aliasing, checking all destination objects,
  canaries, palette inputs and context selector. Ten incorrect C variants
  complete normally and are detected. End labels use corresponding valid
  one-past pointers in the native fixture.
* Both independent padders and separately assembled original agree; **432**
  raw byte/binding corruptions are rejected. Four symbol layouts exercise
  **16** GNU links and **64** executions. **390** guest access-cut triples,
  **15** guest alias triples and **48** actual caller-window triples pass.
* Actual Make runs three commands for the complete plain-C owner. The compiled
  owner has no other functions; its GPR mask changes from `80000004` to
  `a3fffffc`. Both independent and actual compact objects agree. The independent
  strict complete-ELF prediction accounts for **406 changed bytes**, including
  the target body, symbol size **12->380**, and three closed symbol/string-table
  permutations; there are zero exclusions. All **6,050** function addresses and
  **189,088** protected bytes across **720** data owners remain fixed.

Both tools environments passed eight fresh pre-install methods, then eight fresh
installed requalification methods after a whitespace-only formatting correction.
Two more installed methods run freshly in each environment; six other methods
are reused from the exact-fingerprinted installed requalification receipts.
Each shared smoke is fresh; three unchanged shared regression receipts are
fingerprinted reuses. The sibling uses a private overlay with documented
fallbacks; its 2,434 existing dirty paths are preserved. Actual Make uses the
mounted CLI. This does not establish a clean sibling checkout.

Production Make agrees with the independent ELF and binary predictions. The
existing whole-ROM checksum failure and duplicate generated_12D630 warnings
remain expected. ELF SHA256 `13a164bde40e8decb342d06479b6cb6d48ff80f0678050d34604f5ca41cb739b`; binary SHA256
`aa168306f288539fca9e85a476db0591e8f5136b0a69f3befb7b3ff514926e85`. Runtime gameplay and full parent behavior are outside
these checks.

Graphify's scoped refresh retains or relocates all 59723 old
nodes and produces 59723 nodes / 113108 links;
outside-scope definitions remain fixed apart from community metadata. This is
not full-corpus extraction. Post-commit graph-worker completion is checked
separately.

```sh
python3 -m unittest tools.tests.test_game_palette_state_15000940_match -v
make -C conker match-progress NON_MATCHING=1
```

Reproduction requires the prepared PSBBN consumer and retained mutable inputs
under `conker/build/game-next-15000940-match/frozen/`; no private ROM or ELF is
committed. Next investigate `func_1501FE68` in `conker/src/game/generated_49D30.c`: its
12-byte stub differs in 88
retail-slot words and remains uncredited. Keep the 80% goal active.
