# Record Flag Refresh Direct Byte Match

Date: 2026-10-18. Consumer predecessor **853bea63**, tools predecessor
**236d562d**. Restore **func_15113180**, owner `generated_13D350`, VA
**0x15113180..0x15113218**, ROM **0x140630..0x1406C8**. The wider Game
matching goal remains active; this is one completed function.

## Recovery And ABI

The false return-zero stub becomes a typed, commented **void record-flag
refresh procedure**. All **38 words / 152 bytes / no frame** emit directly
under unchanged **O2/g3/MIPS2/o32**: zero raw differences, zero guards,
no compiler override or inserted/omitted word.

For each 0xA0-byte record, clear +0x6F bit0x40. Reload the table base and
record flags, then restore that bit when the low nibble is nonzero OR +0x70
bit0x04 is set, AND the +0x38 object word is nonzero. Reload the signed count
after writes. Nonpositive counts do not touch the table. The byte cursor is
unsigned, matching retail's wrapping word arithmetic; ordinary native fixtures
remain within their supplied arenas.

The original hypothesis retained s32 because the stub and caller declared it,
and retail leaves the loop index in V0. Full static source/assembly/header
search finds one direct caller: **func_15019130**, call **0x15019180**. Its next
instruction **0x15019188** overwrites V0 before reading it. No named data/table
reference is found. This supports a void procedure, not a C count-return API;
the selected source still preserves the exact retail V0 index lifetime.

Correct only the caller's local declaration in `game_45B80.c` from s32 to void.
All **16 caller-owner functions**, relative relocations and pools are unchanged.
Its four pre-existing Warning712 diagnostics are unchanged after normalizing
only the before/after scratch filenames. The newly recovered owner has no
diagnostics. Most importantly, the **actual rebuilt caller object is byte-for-
byte identical**, including metadata. No shared header or caller body changes.

Sixteen normal-profile source forms were measured. The first explicit-return
form reached 38 words but 36 differences. Reusing the local pointer, comparing
the masked flag explicitly to 4, and promoting the loaded byte to u32 recover
retail's dataflow. Explicit-return wide-flag forms remain 39 words/10 differences;
the source-level register-hint control gives no gain and is not installed.
The selected void form reaches 38/zero without any physical register binding.
Source spelling is a recovery, not proof of the original authored text.

## Fresh Qualification

New tools: `experiments/game_record_flag_refresh.py` and
`tests/test_game_record_flag_refresh.py`. Ignored receipts live at
`conker/build/game-record-flag-refresh/`. Sixteen inputs pin source, ELF,
guards/ROM/assembly, helper ownership sources, compiler/build/symbol inputs,
the caller source and its complete original production object.

All **seven pre-install tests pass in 29.090s**. The installed suite passes
in **28.651s**; strengthening guest controls to require a memory mismatch,
not merely a scratch-register difference, passes all seven again in
**28.680s**:

```sh
python3 -m unittest tools.tests.test_game_record_flag_refresh -v
```

Coverage includes **14,336 guest flag cases** plus signed-count boundaries,
all 256 primary flag bytes, seven secondary flag patterns, null/low/high object
words and low/high record addresses. Whole memory, V0's actual index and saved
state are checked. V0 agreement is machine-state evidence, not a nonvoid C API.

Native32 **O2/O0 with UBSan** each pass **131,077 cases**: every 256x256 flag-
byte pair with null/non-null object words (131,072), two global-alias arenas
and three nonpositive/null-table cases. Native flat ABI arenas use
`-fno-strict-aliasing` and freestanding `-mstackrealign`; this is not a general
ISO-C effective-type or endian-independent pointer-representation proof.

All six cached-count/cached-base/low-nibble-only/missing-object/wrong-stride/
missing-clear controls produce **observable wrong memory** in both native and
compiled guest execution. No crash or merely dead-register mismatch is accepted.
Three independently linked symbol/entry placements exercise HI16/LO16 carry,
count aliases and pointer aliases across **15 sequences**. One placement makes
the initial clear alter the table pointer before its immediate reload; another
alters the next iteration's base after the conditional set.

All **462 target-memory fault prefixes / 52 states** preserve complete memory,
events, access counts and the loop index. Eight connected actual caller slices
verify the return boundary and subsequent V0 discard in both stack phases.
All **38 raw-word**, **four relocation-binding**, **32 live/frozen input**
corruptions and nested historical views are rejected. Hardware faults and
complete gameplay are not newly qualified. Prior unchanged neighbor-suite
receipts are reused rather than called fresh broad regressions.

## First Prediction And Actual Build

A copied current linker script substitutes the qualified owner before
production edits, predicting the complete **3,257,636-byte ELF**. The caller
declaration's independently verified identical code requires no byte replacement.
The actual two-owner/ELF/progress build reproduces the complete first prediction:
**112 changed bytes = 111 target-code bytes + one target symbol-size byte**.
Target st_size changes **12 -> 152**; there are no metadata exclusions.

```sh
make -C conker -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_13D350.c.o build/src/game_45B80.c.o \
    build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

All **6,057** bodies/addresses are compared; only the target body changes.
Canonical symbols differ only in its expected extent. All **33** raw owner
neighbors/pools/relocations are fixed, including the newly exact matrix
constructor. Actual padded-owner bytes/relative bindings equal the qualified
object. The actual caller object remains identical. Guards are unchanged;
Game data stays **189,088 bytes / 720 owners / zero differences**.

| Prepared Artifact | SHA-256 |
| --- | --- |
| Complete installed ELF | `c20a95cd43bb3ea44e97fdd57f7691f530144cabe398370943f4aa04d074b5ec` |
| Complete owner source | `5c781613db2a007870cf4e0c83a54324f7789fa5a0ed65364e996941eaa3195b` |
| Caller source | `63ff5cd1051b8ed117581dcc5321b4e4dd5370f8cffaf62bc5091087e968b210` |
| Unchanged caller object | `6f93d458b6a4991ee00a8d815534c58451aad5b9864fff79c9ceaf0c9533fafc` |
| Unchanged guard manifest | `625033dd1c2150ce2edb45badf13c05d09aa95b83a0c2b1231e092105d3fc2b3` |
| Raw target object | `0ebf63ce1434334e558ab0614cf8fc5ef50dea3c6c2b601cb6dccb3782a36235` |

The three-member source/caller-source/ELF historical view retains immutable
before/after fixtures, maps only Path readers for research and rejects mixed,
unknown or nested states. Physical audit keeps raw reads. Older helpers and
fixture hashes are unchanged; future experiments should freeze the new live
baseline directly instead of weakening or blindly nesting older views.

## Bank And Next Action

Tools **d13c136** is committed before the consumer source/docs/pin. Both tools
copies pass eleven shared padder tests and project-tools smoke checks, four
Windows ASCII/AST parses and two exact task-file comparisons. Preserve older
mirror **ddbdd16**, all **1,192** initial dirty hashes and its history; add only
two absent paths for **1,194** dirty paths. No mirror commit/reset, push,
Claude call or host/frozen Release edit/build/launch occurs.

Scoped graph refresh completes at **42,414 nodes / 82,518 links / 3,946
communities**, retaining **19,398 excluded nodes / 2,972 files**. Every old
node ID remains except three shifted Update Log heading IDs whose labels
remain represented. The recovered procedure resolves to source line82 and
this note has six graph nodes. No purge or full extraction is performed.

Fresh official totals: **Game 2,971/4,828 (61.54%)**, total
**3,644/5,501 (66.24%)**, **1,857 different**, zero address drift. Conversion
counts/bytes remain unchanged. Root README changes only two matching rows.

Next recover **func_15107AE0**, owner `generated_133190`, VA
**0x15107AE0..0x15107B78**, ROM **0x134F90..0x135028**, **38 words / no frame**.
It computes the original three deltas between A0/A1 input vectors, then writes
A2/A3 outputs with **D_800A2420 = 0.333f (0x3EAA7EFA)** and
**D_800A2424 = 0.6667f (0x3F2AACDA)**. Do not replace these by exact thirds.
Source coordinates are reloaded between output stores while the original
deltas remain live, making overlap behavior significant. Audit the four-pointer
ABI at call sites 0x15107894, 0x15107A00, 0x15107DF8 and 0x15107F34 before
replacing the false no-argument s32 stub. Handwritten func_150A76F0, both fade
gaps, other gate, additional-source, caller and inherited-stack work remain open.
