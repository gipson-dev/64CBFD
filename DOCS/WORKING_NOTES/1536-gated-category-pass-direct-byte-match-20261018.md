# Gated Category Pass Direct Byte Match

Date: 2026-10-18. Consumer predecessor **3c13e5aa**, tools predecessor
**0f19fe7**. Restore **func_15022848**, owner `generated_49D30`, VA
**0x15022848..0x150228E4**, ROM **0x4FCF8..0x4FD94**. The wider Game matching
goal remains active; this is one completed function.

## Recovery And Existing Profile

Replace the false no-argument s32 stub with commented **void(s32 index) C**.
Only an indexed D_800C35EA byte exactly equal to one enters the pass. Clear
D_800C3638, capture the address of D_800C363A[index], and iterate from zero.
Each entry calls **func_15022398 then func_150222E0**, with (ordinal,index).
Reload the unsigned count byte only after both calls. Set D_800C3638 to one
after the pass, including an initially empty count. Inactive gates leave it
untouched. The flag is not a saved/restored prior value.

The first complete source form emits **all 39 words / frame0x28**, preserving
S0/S1/S2/RA lifetimes and branch-delay argument setup. The local forward
declaration becomes void(s32), matching the observed caller's ignored result.
All **56 raw owner neighbors**, including that caller, relative bindings and
compact pools remain unchanged. Neither owner compilation emits diagnostics.

The slice already uses **O2/g3/MIPS2/o32 with -Wo,-loopunroll,0**. The first
default-profile exploration matches this target but cannot pad an unrelated
unrolled neighbor. Complete-owner qualification therefore uses the existing
profile through the existing compiler wrapper, before forming the first full
prediction. This is not a new override: **no Makefile/profile/padder changes,
no guards, no inserted/omitted words**. Production build receipts confirm the
same established no-unroll flag.

## Focused Qualification

New tools: `experiments/game_gated_category_pass.py` and
`tests/test_game_gated_category_pass.py`. Ignored artifacts:
`conker/build/game-gated-category-pass/`. Thirteen inputs pin the source,
whole ELF, guards/ROM/assembly, build/symbol/header inputs and all four
prepared compiler components.

All **seven pre-install tests pass in 18.169s**; all **seven installed tests
pass in 24.477s**:

```sh
python3 -m unittest tools.tests.test_game_gated_category_pass -v
```

**4,902 paired guest cases** cover all 256 gate bytes, empty and unsigned
count boundaries through 255, indices 0/3/256, two stack phases and seven
callback modes. The first callback may clear the count without suppressing
the second. A transient zero restored by the second helper does not end the
pass early. Other modes shrink/grow the live bound, change the gate after entry
or alter the context flag. All 39 target words execute across the corpus.
Public memory/call traces match the independent loop reference; complete
candidate/retail memory, registers and FPRs agree. Saved ABI state is checked.

**126 extra word-address probes** include a count/context alias at index -2,
gate/context alias at index78 and full-width index65537. These are explicitly
bounded guest address-model tests, not portable native negative-array indexing
or global-object alias guarantees. Initialization order and the flag write
before the first count load are included in the reference.

Native32 **O2/O0 with UBSan** each pass **14,336 cases**, exhausting all gate
and count byte values with callback mutations and valid array indices
0/3/255/256. Both entire 512-byte arrays, context and observable callback
count/hash are checked. Seven truthy-gate/cached-count/mid-pair-recheck/
reversed-callback/no-clear/no-final-set/narrowed-index controls exit explicitly
with wrong-result status23. Their compiled guest forms also change memory,
not merely dead registers; callbacks use an observation sink to expose order
and context changes.

Six independently assembled original/C links at three placements pass
**126 paired sequences**. All ten data/call relocation bindings are exercised,
including independent HI16/LO16 signed lows and a count/context binding alias.
**760 target-access fault prefixes across 72 states** compare complete memory,
register/FPR/call/PC/delay state. Opaque callback internals are excluded; this
does not claim hardware MMU policy or portable C fault semantics.

All **39 raw words / ten bindings / 26 live-and-frozen input mutations** are
corruption-gated. Nested historical views are rejected. Initial harness
corrections separate the pass-specific symbol tuple from the base oracle's
own fields and stop the caller window after the following call's delay slot;
neither required a production C change.

## Caller And Open Helper Boundary

The observed direct caller **func_1501D348** passes its full s32 slot in S5 at
**0x1501DA54**, with **move A0,S5 at 0x1501DA58**. It ignores the scalar result
and immediately proceeds to func_15022754. Correcting the target's local
forward declaration preserves its raw body, along with every other neighbor.

**126 bounded actual caller windows** execute the retail/production call and
delay slot, target body, return, and following call setup. The four-word
window is checked against current production bytes and stops before entering
the following helper. It verifies wide index delivery and memory/call effects,
not the complete large parent function or gameplay.

**Both func_15022398 and func_150222E0 remain production C stubs.** Their
two-argument ABI is evident in retail and their original bodies remain in
asm/49D30.s, but this checkpoint does not restore them. The focused pass uses
explicit scripted ABI/effect boundaries for both. Do not describe this as a
fully restored category-processing subsystem.

## First Prediction And Actual Build

Before editing production, replace only the qualified owner input in a copy
of the current full linker script. Freeze that first **3,257,636-byte ELF**
and source successor. The original source/ELF fixtures are not rewritten.

```sh
make -C conker -o Makefile -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_49D30.c.o build/conker.us.elf progress.csv
make -C conker -o Makefile -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

The installed ELF equals that prediction exactly: **131 changed bytes =
130 target-code bytes + one target symbol-size byte**, at file offset2859339.
Target st_size changes **12 -> 156**, with zero metadata exclusions. All
**6,057 bodies/addresses** and canonical symbol definitions are audited;
only the target body and extent change. Actual padded owner bytes and all
relative bindings equal qualification. Guards and Makefile remain fixed.
Game data stays **189,088 bytes / 720 owners / zero differences**.

| Prepared Artifact | SHA-256 |
| --- | --- |
| Complete installed ELF | `6f9f3636ee46917e8815196a03dfa8a3755e7cfd4763f64dc2b074d21013c3a6` |
| Complete owner source | `e0376d1609bcde42ce5b340453f9fbfcce6022a230b9016a0944f4044f23e187` |
| Raw target object | `644f3b919ab4d6d5b1b29aee2da07514107c6b385cd49511a7cf434d020e2243` |
| Linked target bytes | `037b9636a9a15df4dc0b1f0e20bf3619522a24be099b3935e3008223efe8c022` |
| Unchanged Makefile | `840897f11d9fea8109c4e67c57e927efa6e1686de2b399fec2c9025828b92d49` |
| Unchanged guard manifest | `625033dd1c2150ce2edb45badf13c05d09aa95b83a0c2b1231e092105d3fc2b3` |

The source/ELF historical view rejects mixed/unknown or nested states, retains
physical raw reads for audit and leaves older fixtures/helpers/hashes fixed.
Future work should freeze this new live baseline and retain the slice's
existing profile, rather than nesting old checkpoint views.

## Bank And Next Action

Tools **3cc55c3** is committed before the consumer source/docs/pin. Both local
copies pass eleven shared padder tests and project-tools smoke checks, four
Windows ASCII/AST parses and two exact task-file comparisons. Preserve older
mirror **ddbdd16**, all **1,198** initial dirty hashes and its history; add only
two absent paths for **1,200** dirty paths. No mirror commit/reset, push,
Claude call or host/frozen Release edit/build/launch occurs. Unchanged broad
neighbor suites remain prior receipts, not freshly rerun tests.

Fresh official totals: **Game 2,974/4,828 (61.60%)**, total
**3,647/5,501 (66.30%)**, **1,854 different**, zero address drift. Conversion
counts/bytes remain unchanged. Root README changes only two aggregate rows.

Scoped graph refresh completes at **42,441 nodes / 82,513 links / 3,935
communities**, preserving the **19,398 excluded nodes / 2,972 existing files**.
All old IDs survive except three shifted UPDATE_LOG heading IDs, whose labels
remain represented. The target resolves to source line792 and the next target
to line827; this note has seven graph nodes. Graph outputs remain ignored
local research artifacts, not production inputs.

Next recover **func_15022B08**, same owner, VA **0x15022B08..0x15022BA4**,
ROM **0x4FFB8..0x50054**, **39 words/no frame**. It snapshots the count byte,
walks enabled u16 entries, and compares descriptor byte +2 (8-byte stride) to
the selected 0xA0-byte record's byte +0x72, returning one on any match and zero
otherwise. Audit its observed caller in generated_142560.c and preserve the
complete slot, including the apparently unreachable increment at 0x15022B88.
Do not trim it as padding or invent an assembly substitute. The two callback
stubs, handwritten func_150A76F0, both fade gaps, other gate, additional-source,
caller and inherited-stack work remain separate and open.
