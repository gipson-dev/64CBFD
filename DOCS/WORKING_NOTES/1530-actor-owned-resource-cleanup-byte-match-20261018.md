# Actor Owned Resource Cleanup Byte Match

Date: 2026-10-18. Consumer predecessor **62ed4a00**, tools predecessor
**bcedfb7b**. Previous goal turn completed the rectangle's guarded match.
This turn restores **func_15101148**, owner `generated_12DAB0`, VA
**0x15101148..0x151011E8**, ROM **0x12E5F8..0x12E698**. The full Game goal
remains active; this is one completed function, not overall completion.

## Installed Recovery

The false zero-return placeholder is replaced with a typed, commented
**void actor-destruction callback**. All **40 words / frame0x20** now match
retail after **three** expected-word register/setup guards. Raw C has three
differences; do not describe it as a direct/raw compiler match.

The callback releases non-null owned objects in order **+0x138, +0x13C,
+0x134, +0x140, +0x144** through `func_1516979C`, then calls
`func_1513CAA0` on the original actor. Each later field is read after the
preceding callback; callbacks can change future slots. The local
`ActorOwnedResources101148` view names the five pointer fields relative to
the observed actor+0x110 block without inventing gameplay roles.

A volatile owner parameter reproduces retail's argument-home reloads across
the callbacks. It is a recovered source form, not proof of the original
authored spelling. The normal **O2/g3/MIPS2/o32** profile remains unchanged.
The actual helper declarations confirm void cleanup operations. An existing
byte-pointer sibling wrapper requires the legacy unprototyped void declaration
of `func_1513CAA0`; adding its full global pointer prototype produced a new
warning, while a block-only declaration conflicted with the sibling's implicit
declaration. The selected form is warning-free and leaves all siblings intact.

## Caller And First Argument

Retail callback table **D_80089F2C[1]**, slot **0x80089F30**, selects this
routine. The original **func_1513CBA4** dispatcher retains the actor in A0
through its indirect call. The common struct210 view describes the base actor;
the local resource view covers its otherwise unnamed pointer region.
Shared legacy dispatcher/table C declarations are not rewritten. Connected
qualification uses the actual retail dispatcher bytes and its observed A0 ABI,
not a claim that the existing void(void) callback declaration is portable C.

Ten normal-profile source shapes were screened. The ordinary owner promoted
to S0 and frame0x28; the selected argument-home form reaches 40/frame0x20 with
only the first resource's register choice different. O1 and O1/g3 forms remain
41 words and are rejected. No profile override, unused padding, physical
register binding or broad conversion is installed.

The three guards are at **+0x10/+0x14/+0x20**, words **4/5/8**:

- The first resource loads into T7 instead of source A0.
- The likely branch tests the corresponding resource register.
- The call delay slot copies T7 to A0 instead of retaining the source NOP.

Both null/non-null branches preserve the actual helper argument. On the null
edge A0 is overwritten by word10 before its next use. The remainder of the
target never reads T7. T7 is ABI caller-saved; no equality of dead scratch
registers or undocumented provider inputs is claimed. All six R_MIPS_26
call bindings remain fixed, with no inserted/omitted word or relocation move.

## Fresh Qualification

New tools are `experiments/game_actor_owned_resource_cleanup.py` and
`tests/test_game_actor_owned_resource_cleanup.py`. Artifacts live under
`conker/build/game-actor-owned-resource-cleanup/`. Sixteen pinned inputs
include source, retail assembly/ROM, helper sources, shared type declarations,
the callback table, build/guard/symbol inputs and all four prepared compilers.

All **seven pre-install tests pass in 15.636s**. After installation and adding
the four compiler pins, all **seven final tests pass in 17.299s**:

```sh
python3 -m tools.tests.test_game_actor_owned_resource_cleanup -v
```

Fresh checks cover **1,024 guest cases** across every presence mask,
callback mutation mode, repeated-pointer alias, low/high pointer values and
both stack phases. Provider hooks poison caller-saved state so the recovered
body cannot rely on it. Native32 **O2/O0 with UBSan** each pass **256 cases**;
four wrong-order/omitted/null-release/wrong-owner controls are effective in
both native and compiled guest execution. Native flat views explicitly use
`-fno-strict-aliasing`; this is not universal ISO-C alias proof.

All **1,928 target memory-access fault prefixes / 128 states** preserve calls
and memory. Forty instruction/guard-window corruption controls and forty raw
object-word controls reject changes. All pinned live/frozen input corruptions
and nested predecessor views are rejected. **128 real dispatcher sequences**
cover both the base cleanup and specialized callback branches, with preserved
owner arguments. Hardware faults, real frees and full gameplay remain separate.

All **22 raw owner neighbors**, their relative relocations and owner pools
remain unchanged. Prior unrelated function-suite receipts are reused as
unchanged evidence, not represented as freshly rerun broad regressions.

## First Prediction And Actual Build

Before editing production, a disposable full link substitutes the qualified
padded owner in a copied current linker script. It predicts the complete
**3,257,636-byte** ELF, not just a retail-byte patch to a guessed image.
The real owner/ELF/progress builds then reproduce that first prediction exactly:
**123 changed bytes = 122 target-code bytes + one target symbol-size byte**.
The function's st_size changes 12 -> 160. No metadata exclusions are used.

All **6,057** bodies/addresses are compared; only this target body changes.
Canonical symbol definitions differ only in the expected target extent.
The actual padded owner and six call relocations equal the qualified object.
Protected Game data remains **189,088 bytes / 720 owners / zero differences**;
callback slot 0x80089F30 stays 0x15101148. The complete guard prefix, including
mixed legacy line endings, is retained byte-for-byte; only three rows append.

| Prepared Artifact | SHA-256 |
| --- | --- |
| Complete installed ELF | `d2cda82f7b4ae411706bad464b7680eebcd46efff7b50b6b77fa7e2a50e9be72` |
| Complete owner source | `8d42746275aa7e3a3523a6a6be4cda8441c1956d502ad788fbf195f272f406a5` |
| Guard manifest | `034e4adad354d74935a842725e1e2c3490a6c68bad6f875897e2ca6c4ee6282f` |
| Raw target object | `cbb47854ef6c04e0de22430c14521969a26cfd799a1a5b1f0eeb5851a4ea55cd` |

The exact three-member historical view verifies these physical successor
artifacts and their immutable predecessors, maps only their Path readers for
research, rejects unknown/mixed states and restores readers on exit. Actual
image audit uses raw reads and actual object/linker tools. Do not weaken old
rectangle/movement hashes or blindly nest independent historical views.

## Bank And Next Action

Fresh official totals: **Game 2,968/4,828 (61.47%)**, total
**3,641/5,501 (66.19%)**, **1,860 different**, zero address drift. Conversion
counts/bytes are unchanged. Root README updates only its two matching rows;
function narratives stay in working documents.

Tools **e371724** is committed before the consumer source/guards/docs/pin.
Both tools copies pass eleven shared padder tests, project-tools smoke checks,
four Windows ASCII/AST parses and two exact task-file comparisons. Preserve
mirror **ddbdd16** and all **1,186** initial dirty hashes; add only two absent
paths, for **1,188** dirty paths. No mirror commit/reset, push, Claude call or
host-port/frozen Release edit/build/launch occurs.

Next recover the paired callback **func_15101090**, same owner, VA
**0x15101090..0x15101148**, ROM **0x12E540..0x12E5F8**, **46 words/frame0x20**.
It first conditionally releases the unsigned-halfword handle at actor+0x1A0
through **func_100111C8**, then visits the five resource fields in the same
order through **func_1516972C**, and finishes with **func_1513CA6C** on the
original actor. Qualify its real helper/callback ABI and handle width before
reusing this pattern. Handwritten func_150A76F0, both fade gaps, other gate,
additional-source, caller and inherited-stack work remain open.
