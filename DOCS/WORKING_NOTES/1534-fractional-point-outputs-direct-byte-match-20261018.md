# Fractional Point Outputs Direct Byte Match

Date: 2026-10-18. Consumer predecessor **087f494b**, tools predecessor
**d13c1360**. Restore **func_15107AE0**, owner `generated_133190`, VA
**0x15107AE0..0x15107B78**, ROM **0x134F90..0x135028**. The wider Game
matching goal remains active; this is one completed function.

## Recovery And Literal Ownership

The false no-argument s32 stub becomes typed, commented **void C with four
float-vector pointers**: start, end, first output and second output. Original
dx/dy/dz are captured before any store. Output coordinates then read the start
vector again in retail order, so exact/partial input/output aliases retain
their observed behavior. No restrict qualifier or whole-input caching is added.

The exact fractions are **0.333f (0x3EAA7EFA)** and **0.6667f (0x3F2AACDA)**,
not exact thirds. Twelve complete normal-profile source forms were measured.
Named mutable global captures produce 38 words/19 scheduling/register
differences; register/declaration controls give no gain. Float-return controls
produce 39 words and are rejected. There is no evidence of a C float-return
API merely because retail retains dx in F0.

The two literal-source forms reproduce **all 38 instructions / no frame**
under unchanged **O2/g3/MIPS2/o32**. Their isolated compact link initially has
four private pool-address differences, not four instruction/dataflow changes.
The existing `RETAIL_RODATA_SYMBOL` mechanism binds this owner's offset-zero
pool to **D_800A2420**, preserving the second literal's +4 addend. The actual
linked 152-byte function is fully retail-exact, with **zero instruction guards,
no compiler override, no inserted/omitted words**.

This is ordinary source literal relocation, not instruction normalization.
The compact pool is exactly **16 bytes: two original floats plus eight zero
alignment bytes**, with no pool relocations. All 36 other raw owner functions
and relative relocations are unchanged. The only new compact pool is checked
against the complete existing retail block; production padding emits text and
continues using the original `asm/data/246ED0.rodata.s` owner. No duplicate data
is linked and no retail constant/data source is edited. The owner's two existing
Warning712 diagnostics at lines125/130 are unchanged; no new warning is added.

## Fresh Qualification

New tools: `experiments/game_fractional_points.py` and
`tests/test_game_fractional_points.py`. Ignored artifacts:
`conker/build/game-fractional-points/`. Thirteen inputs pin the source, whole
ELF, guards/ROM/assembly, build/symbol inputs, retained neighboring assembly,
constant-data source and all four prepared compiler components.

All **seven pre-install tests pass in 24.847s**; all **seven installed tests
pass in 32.537s**:

```sh
python3 -m unittest tools.tests.test_game_fractional_points -v
```

The finite reference separately rounds each float32 subtraction, multiply and
addition. **10,240 guest cases** cover eight value patterns, five input
relationships, 64 output-overlap layouts, low/high addresses and both stack
phases. Values include signed zeros, subnormal boundaries, cancellation,
large finite values and rounding-sensitive neighbors. Whole memory, output
guard bytes and saved state are checked; all six output stores retain order.

Native32 **O2/O0 with UBSan** each pass **2,560 finite cases** with explicit
rounding, contraction disabled and freestanding stack realignment. Five
exact-thirds/cached-start/live-delta/reversed-store/reversed-delta controls
produce observable wrong memory in native and compiled guest execution. No
crash or merely dead-register mismatch is accepted.

Three independently linked code/pool placements pass **171 sequences**, including
both positive and negative-address HI16/LO16 carries where the second literal
crosses 0x7FFF. A wrong retail-anchor control fails observably. Exact pool bytes,
all 38 raw words and all four relocation bindings are corruption-gated.

**95 nonfinite guest pairs** compare candidate/retail instruction execution;
they are not a hardware NaN-payload/FCSR/exception policy proof. All **2,888
target-memory fault prefixes / 152 states** preserve complete memory, events,
registers and access counts. All **26 live/frozen input mutations** and nested
historical views are rejected. Unchanged neighboring suites are reused as prior
evidence, not called freshly rerun broad regressions.

## Caller Boundary

Four retail call sites at **0x15107894, 0x15107A00, 0x15107DF8 and 0x15107F34**
pass four vector pointers and consume output stores, not a scalar result.
**24 bounded retail caller windows** exercise the actual setup/call/delay/return
instructions with controlled live inputs. These windows qualify the pointer
delivery and stores, not complete parent-function or gameplay behavior.

All four containing production caller bodies remain stubs. In particular, the
retained assembly neighbor **func_15107B78 ends at 0x15107C1C**; it does not
contain the call at 0x15107DF8, which belongs to func_15107C1C. Do not reuse the
earlier handoff assumption that this neighbor supplied a restored full caller.
No caller restoration or runtime acceptance is claimed by this checkpoint.

## First Prediction And Actual Build

A copied current linker script substitutes the qualified owner before editing
production and predicts the entire **3,257,636-byte ELF**. The actual source,
per-owner mapping, object/ELF/progress build reproduces that first prediction:
**123 changed bytes = 122 target-code bytes + one target symbol-size byte**.
Target st_size changes **12 -> 152**, with zero metadata exclusions.

```sh
make -C conker -o Makefile -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_133190.c.o build/conker.us.elf progress.csv
make -C conker -o Makefile -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

The Makefile-old flag avoids recompiling unrelated generated owners after the
single-owner anchor addition; the new target variable is still read and the
affected source is explicitly rebuilt. The build receipt includes
`--rodata-symbol D_800A2420`. All compiler optimization/profile flags stay fixed.

All **6,057** bodies/addresses are compared; only the target body changes.
Canonical symbol definitions differ only in its expected extent. Actual padded
owner bytes and relative bindings equal the qualified object. Guards are
unchanged; the complete original 16-byte literal block and its source stay
fixed. Game data remains **189,088 bytes / 720 owners / zero differences**.

| Prepared Artifact | SHA-256 |
| --- | --- |
| Complete installed ELF | `d6f9ef39a264d51413b532ae5a4b587400864b346d0cbab1b9e066eaf09c327b` |
| Complete owner source | `07ef53eb53f67b749de94a6390cbc836dbcf99b7e1983c91efd27fc0730d4ed4` |
| Makefile with owner-only anchor | `840897f11d9fea8109c4e67c57e927efa6e1686de2b399fec2c9025828b92d49` |
| Unchanged guard manifest | `625033dd1c2150ce2edb45badf13c05d09aa95b83a0c2b1231e092105d3fc2b3` |
| Raw target object | `8be0c877fd146def90f9ec4194c677fe9bb75cb3f8a4133ed4c05ba062865bbf` |

The source/Makefile/ELF historical view retains immutable before/after fixtures,
maps only Path readers for research, rejects unknown/mixed or nested states
and restores readers on exit. Physical audit keeps raw reads. Older helpers
and hashes are not weakened; future work should freeze the new live baseline.

## Bank And Next Action

Tools **4d3a3d8** is committed before the consumer source/build/docs/pin. Both
copies pass eleven shared padder tests and project-tools smoke checks, four
Windows ASCII/AST parses and two exact task-file comparisons. Preserve older
mirror **ddbdd16**, all **1,194** initial dirty hashes and its history; add only
two absent paths for **1,196** dirty paths. No mirror commit/reset, push,
Claude call or host/frozen Release edit/build/launch occurs.

Fresh official totals: **Game 2,972/4,828 (61.56%)**, total
**3,645/5,501 (66.26%)**, **1,856 different**, zero address drift. Conversion
counts/bytes remain unchanged. Root README changes only two aggregate rows.

Scoped graph refresh completes at **42,423 nodes / 82,516 links / 4,065
communities**, preserving the **19,398 excluded nodes / 2,972 existing files**
instead of purging evidence. All old IDs survive except three shifted
UPDATE_LOG heading IDs, whose labels remain represented. The target resolves
to its current source line161; this note has seven graph nodes. Graph outputs
remain ignored local research artifacts, not production inputs.

Next recover **func_151AB930**, owner `generated_1D6E80`, VA
**0x151AB930..0x151AB9C8**, ROM **0x1D8DE0..0x1D8E78**, **38 words/frame0x48**.
It snapshots the actor pointer, u8 +0x3B and u16 +0x84 into a 0x1C-byte local
packet at SP+0x28. Further fields are 0.0f, D_800A9014, 3.0f and the low byte
returned by func_151D8E20. Then func_151491F4(0x3C,-1,0xE,1,9,0x1C,0xFF,0)
creates a destination; if nonnull, memcpy copies all 0x1C bytes to +0x28.
Audit the actual helper/caller contracts and snapshot lifetimes first. Six
bytes at SP+0x2D..0x2F and +0x41..0x43 are inherited padding, not proven zero
fields; do not initialize or claim them without the private-stack qualification.
Handwritten func_150A76F0, both fade gaps, other gate, additional-source, caller
and inherited-stack work remain separate and open.
