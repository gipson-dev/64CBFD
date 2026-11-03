# Working Note 2048: Game uniform matrix submit direct match

Date: 2026-11-03

## Result

`func_1515858C`, owner `conker/src/game/generated_185560.c`, retail VA
`0x1515858C..0x15158684`, ROM `0x185A3C..0x185B34`, is restored from its
zero-return placeholder as semantic C. The retail `-O2 -g3` owner profile now
emits all 62 words directly with the original `0x68` frame and no word guards.

The recovered callback:

1. takes a fixed-matrix output pointer and state pointer;
2. passes state rotations `+0xF8/+0xFC/+0x100` to `func_150A8050`;
3. inserts state translation `+0x48/+0x4C/+0x50` into matrix row three;
4. multiplies all nine basis components by the uniform scale at `+0x104`;
5. converts the floating matrix through `guMtxF2L`; and
6. returns active status `1`.

Declaring the recovered `rotation` pointer before the local matrix is material:
it preserves retail's single `state + 0xF8` temporary, places the matrix at
`SP+0x24`, and reproduces the complete frame and schedule naturally. The
adjacent donor source was useful for semantic orientation, but its scalar
decompiler types were not adopted; the installed state view uses named `f32`
fields and the callback's real `Mtx *` output ABI.

## ABI and ownership

The routine has no direct `jal` caller and one aligned function-pointer literal
at ROM `0x22F8CC`, `D_8008AE0C[0]`. The indirect call in
`func_151582C8` supplies the selected fixed-matrix output at state page
`+0x58`, passes the state as argument two, and tests the callback's return.
The two function relocations are:

- `+0x020`: `R_MIPS_26:func_150A8050`
- `+0x0D8`: `R_MIPS_26:guMtxF2L`

The selected owner comparison retains all 36 neighboring bodies. The strict
linked-image comparison contains 6,051 functions, changes only
`func_1515858C`, keeps every function address fixed, and uses zero exclusions.
Protected Game data remains exact across 189,088 bytes and 720 owners with
SHA-256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Permanent qualification

The tools were banked before source installation:

- `952c456` (`test(game): qualify uniform matrix submit`)
- `34df5f5` (`test(game): accept installed uniform matrix source`)

`tools/tests/test_game_uniform_matrix_submit_match.py` proves:

- 512 guest executions over 32 seeds, eight helper-mutation modes, and two
  initial timing phases;
- all 62 retail words visited;
- the three rotation arguments are captured before the rotation helper while
  translation and uniform scale remain live after that helper;
- the exact nine basis products, unscaled translation row, fixed output
  destination, and return value;
- native O0/O2/O3 execution; and
- eleven effective semantic controls covering each rotation, each translation,
  scale source, omitted basis scaling, incorrectly scaled translation, output
  destination, and return value.

The installed three-test suite passes. The shared match-progress, generated
word-patch, and protected-data regression suite also passes all 14 tests.

## Frozen evidence

| Artifact | SHA-256 |
| --- | --- |
| Compact object payload with relocation fields normalized | `a2b2aed67410b24442f948dad6945ead9f2c3f17e78f61b8e58df9fa1b8624e3` |
| Retail linked body | `d4ac8544f180d34ce45b665bf4541a61563a031139e4b2c71a311151975e759d` |
| Installed source | `ed7908ad40c86b66927e5bd5c5fc74c4192396680779b97e190f7c5fbde919ab` |
| Qualified/production owner object | `eda469151745d170a86ea119a3f4e618a18edcdf00f1a04924c299e460daeaf5` |
| Predecessor linked ELF | `0a3565d7fcb4108f007aa41435d322b74c6a53cc2a513a4388e4832bdfc12a51` |
| Qualified/production linked ELF | `24e0ca960552ee92f5b2ef0b3584f910bee36f23cc9ac07b8f00f8aec839be36` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Unchanged guard table | `40181c499def3c079e9cb3ed9a0f8eaf1476bb5750e5fe29670430ffb45b606d` |

The actual production Make rebuilt `generated_185560`, padded the complete
generated-slice owner, linked `conker.us.elf`, and generated `conker.us.bin`.
It stopped only at the expected final whole-ROM SHA mismatch while the decomp
remains incomplete; there were no compile, assembly, padding, or link errors.

## Recount

The fresh production ELF reports:

- Total: **4,118 / 5,511 (74.72%)**, zero address drift, 1,393 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,445 / 4,838 (71.21%)**, zero drift, 1,393 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **291 more** are needed.

## Graph retention

The required bounded Graphify update retained 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. It rebuilt a 58,209-node
graph with 112,170 edges and 4,987 communities; visualization was skipped at
the configured 5,000-node limit. The retained/refreshed
`graphify-out/graph.json` is 75,483,218 bytes with SHA-256
`96f22e26ed341fb643f15ee1fc63fc1a83020750fc126b0089e468bee3a89a46`.
The successful update used Graphify's incremental changed-path mechanism and
no force flag. This is bounded old-node retention evidence, not a full-corpus
extraction claim.

## Continuation

The seven documented handwritten/custom-ABI boundary cases remain outside the
ordinary queue. The fresh production ranking starts the ordinary queue at
`func_1515BAE0` (68 words, 61 real differences), followed by the remaining
61-difference tie. Every next candidate still requires source, ABI/caller,
owner, guest/native, actual Make, complete-image, protected-data, production
recount, documentation, and graph-retention gates before credit. This static
and bounded qualification does not claim full gameplay or hardware acceptance.
