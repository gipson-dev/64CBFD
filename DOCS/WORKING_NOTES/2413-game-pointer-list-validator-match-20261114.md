# Game pointer-list validator match

Date: 2026-11-14. `func_15114F44` now matches all 89 retail instructions at
`0x15114F44..0x151150A8` (ROM `0x1423F4..0x142558`), followed by two padding
words in its allocated slot. Its `void` C body replaces a zero-return
placeholder in `conker/src/game/generated_13D350.c`.

In modes `0x12`, `0x36` and `0x13`, it visits two lists, each with a signed
count and 12-byte entries containing three words. A word is accepted when its
high nibble is `8` and it is four-byte aligned. If any of the three fails,
the function writes `0x0C00005A` to `D_8003C8E0` and calls `func_150AD770`.
If execution returns, it reloads the current list count before continuing.
After both lists, it publishes its three incoming words to `D_800DBF9C`,
`D_800DBFA0` and `D_800DBFA4`. Other modes return without visiting the lists or
publishing those values.

The called `func_150AD770` is handwritten and begins with a syscall, not an
ordinary C return. Tests that stop at the actual syscall entry and tests that
hypothetically resume from the handler are reported separately below. An
aligned scan of the extracted retail code image found neither a direct JAL to
this function nor a literal pointer to its entry. The three-argument interface
is observed from the function itself; computed callers are not ruled out.

The compiler emits 82 of the 89 instructions directly in their retail
positions, with the retail frame and loop shape. Seven relocation-aware
expected-word guards restore setup scheduling and the empty-list branch; they
insert and omit no instructions. Both padding paths and 12 GNU links across
four symbol layouts produce the retail stream. All 33 neighboring functions
and normalized constant pools remain unchanged.

Retail, raw C and guarded streams agreed with an independent model in 4,400
cases each, including 240 that reached the original syscall entry. The corpus
also models hypothetical returns with changes to counts and incoming argument
homes. Sixty additional cases overlap list storage with globals or argument
storage; 12 gate cases use unmapped globals or entries. Retail and guarded
streams agree at 171 modeled access-fault prefixes. Forty synthetic caller
cases check the observed three-argument interface and preserved registers;
they do not establish a real caller or complete exception-handler behavior.

The C passed 1,760 native 32-bit cases in each of six O0/O2/O3 and
strict/no-strict-aliasing configurations with trapping UBSan. Native tests use
a returning helper stub; four altered source controls were rejected in both
aliasing modes. These bounded models do not establish actual syscall handling,
complete caller behavior, renderer output or gameplay.

The production Make rebuild is byte-identical to the independently predicted
shadow ELF. Its strict whole-image audit accounts for all 284 changed bytes
with zero exclusions, including the explicitly checked two-symbol metadata
reordering of `D_800DBFA4` and `D_8008A2A4`. All 6,051 function addresses and
189,088 protected Game-data bytes remain fixed. Only `generated_13D350.c.o`
changed among the 698 frozen linked objects; seven guard rows were appended,
and existing guard rows and the conversion CSV remain unchanged. A scoped,
fail-closed Graphify refresh retained all 60,113 existing node IDs; it was not
a full-corpus re-extraction.

Tools commit `31c9b60` retains the fingerprinted pre-install screen and
installed regression tests. The pre-install screen is bound to its original
inputs and is not a test of the installed checkout. For the installed checkout:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_pointer_list_15114f44_installed -v
```

Both installed tests passed in the mounted tools checkout and an isolated
sibling overlay, with no skips; `make tools-check` passed. The sibling tools
checkout's prior dirty paths were preserved.

Fresh production recount: Game **3,790 / 4,843 (78.26%)**, total
**4,463 / 5,516 (80.91%)**, zero drift. **85** more Game matches are needed
for 80% at the current denominator.
