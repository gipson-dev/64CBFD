# Init Memory-Clear Leaf Conversion

Date: 2026-10-02

Follow-up: [Note 737](737-init-mmio-leaf-bounded-compiler-experiment-20261002.md)
records five bounded MMIO-leaf trials without a direct match. That routine
remains assembly; the next Init experiment is `func_10005BE0`.

## Recovery

`func_10001420` clears `0xFE0` bytes beginning at the address of
`D_80043B40`. Its retail slot is `0x10001420..0x10001444`, nine words /
36 bytes. The source owner is `conker/src/init_1420.c`.

The old shared declaration types `D_80043B40` as a pointer, but the retail
routine uses the symbol's address, not a loaded pointer value. The recovered
body therefore takes `&D_80043B40` and leaves the shared declaration alone.
A guest-width integer base constructs the exclusive endpoint `base + 0xFE0`;
a do/while stores zero, advances four bytes, and compares against that end.
The function remains `void func_10001420(void)` without dummy arguments.

This is a semantic C replacement of a retained custom assembly leaf, not
proof that its original author wrote C. Note 735's conditional experiment
has now advanced to an actual implementation. The privileged/shared-register
remainder must still be treated separately.

## Compiler Evidence

The isolated fixture and actual translation unit use the existing IDO 5.3
`-O2 -g3 -mips2 -o32` profile. A simple pointer-plus-end expression emits
ten words because IDO materializes a second symbol address. `-O2` without
debug flags gives the same structure; `-O1` spills the locals and is larger.
Adding `register` qualifiers does not improve the ten-word candidate.

Constructing both pointers through the integer base emits exactly nine words
in the actual source owner. All arithmetic, loop direction, branch target,
delay-slot store, return, and instruction positions match retail. Six strict
expected-word guards normalize the closed register allocation:

| Offset | IDO word | Retail word |
| --- | --- | --- |
| `0x00` | `3C020000` | `3C0E0000` |
| `0x04` | `24430000` | `25C50000` |
| `0x08` | `24640FE0` | `24A40FE0` |
| `0x0C` | `24630004` | `24A50004` |
| `0x10` | `0064082B` | `00A4082B` |
| `0x18` | `AC60FFFC` | `ACA0FFFC` |

The first two retain their exact `R_MIPS_HI16` / `R_MIPS_LO16`
`D_80043B40` relocation contracts. The only register changes are symbol
temporary `$v0 -> $t6` and cursor `$v1 -> $a1`; the end stays `$a0`.
There are no insertions, omissions, compiler overrides, or opaque assembly
instructions in the C body. The branch and its store delay slot retain the
retail cursor-update semantics.

## Behavior Tests

`tools/tests/test_init_memory_clear.py` extracts the actual source definition
and compiles it as host C in a non-PIE executable. The fixture uses real low
addresses and four-byte `u32` values, checks address representability before
calling, and does not alter the extracted body. It places sentinels on both
sides of the 4,064-byte payload and checks every byte after two calls.

Three tests cover `0xA5`, all-one, and already-zero initialization. All 28
tool tests pass. These tests establish bounded source behavior, not a guest
gameplay run. The CSV has 10,388 rows and zero duplicate function/offset keys;
project tool checks pass.

## Verification

`make -C conker NON_MATCHING=1 all match-progress -j4` passes. The focused
object preserves both symbol relocations, and the linked function matches
all 36 bytes at `0x10001420`. `func_10001444` remains at `0x10001444`.
The function SHA-256 is:

```text
a4726841f3477fedc98f9ff44c74f6cb613b2950e7d1c9434a0f61dbda17bdbf
```

Direct extraction confirms the entire 164,048-byte Init code and 17,376-byte
initialized-data sections remain byte-exact with the baseline hashes in
Note 735. Fresh inventories report Init 492 / 539 C rows (91.28%), all
492 exact; C bytes are 151,796 / 164,048 (92.53%). The retained assembly
remainder is 47 rows / 12,252 bytes. Total C is 5,461 / 6,042 (90.38%),
with 3,241 exact (59.35%), zero address drift, and 2,220 different rows.
Game and Debugger results are unchanged.

Existing pointer/integer warnings and the formatter initializer warning in
`init_1420.c` predate this conversion and remain outside its scope. The
sibling host port and frozen Release artifacts are untouched.

## Resume

The next small Init-only experiment is the eleven-word MMIO setup leaf
`func_100038E0`. Preserve volatile store widths and order before evaluating
instruction matching. `func_10005BE0` remains the later bitmap experiment.
The ordinary Game target `func_15157FE8` remains pending.
