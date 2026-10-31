# Dependency activation guarded match - 2026-10-31

`func_1509CCF4` is restored from its zero-return placeholder to semantic C.
The complete 58-word / 232-byte slot matches the US retail image after two
checked branch-operand normalizations. The compiler body alone differs at
those two words; this is a guarded C match, not a raw compiler match.

The actual adopted ELF recount is **3,977 / 5,506 (72.23%)** exact C functions,
with Game **3,304 / 4,833 (68.36%)**, Init 492/492 and debugger 181/181.
There are 1,529 different C functions and zero address drift. The 75% threshold
is 4,130, leaving **153** further exact matches. The goal remains active.

## Source and retail contract

Owner `conker/src/game/generated_C9EC0.c`; original `conker/asm/C9EC0.s`.
VA `0x1509CCF4..0x1509CDDC`; ROM `0xCA1A4..0xCA28C`.
Signature `s32 func_1509CCF4(s32 index)`; no shared header change.
A 20-byte row supplies a sentinel-terminated list of unsigned 16-bit IDs.
Every listed ID sets its bit through the current `D_800D2E4C` pointer, even
when already active. The routine rereads the current list word to look up
`D_800D2E70`, stores state 3 when needed, rereads it for `func_1509CCB4`, and
counts callbacks. The bitset pointer and next list word reload after callbacks.
An empty list does not read the bitset pointer, bitset bytes or state array.
No bounds checks or portable alias guarantees have been invented.

The 56-byte frame saves S0..S6 at SP+24..48 and RA at SP+52. S0 retains the
list cursor; S1 the callback count; S2 the bitset-pointer address; S4 the state
base. S6 is the FFFF sentinel, with separate S3/S5 constants for state 3.
The existing owner profile is `-O2 -g3 -Wo,-loopunroll,0`; the existing
`game_active_record_lookup_match.compile_owner` adapter is fingerprinted in
both tools copies. No Makefile/profile change was needed.

## Exact normalization and object evidence

Only two commutative equality-branch operands differ:

| Offset | Compiler | Retail | Operation |
| --- | --- | --- | --- |
| 0x054 | 0x10760019 | 0x12C30019 | BEQ v1,s6 becomes BEQ s6,v1 |
| 0x0B4 | 0x5476FFEC | 0x56C3FFEC | BNEL v1,s6 becomes BNEL s6,v1 |

Opcodes, branch immediates/targets and branch-likely annul behavior are
unchanged. There are seven relocation bindings, no inserted/omitted words
and no memory-access scheduling changes. All prior guard rows are retained.
The suite rejects 237 payload/scope/binding corruptions, eight modified guard
fields, and both actual padder preimage corruptions.

All 18 raw/padded owner neighbors and normalized pools remain unchanged.
The actual three-command Make recipe reproduces the qualified padded object;
selected, before/after owner and Make diagnostics are empty.
A first generic-profile experiment incorrectly enabled loop unrolling and
overgrew a neighbor. That rejected experiment is retained privately; the
existing no-unroll adapter fixes the experiment without changing production.

Strict independent whole-image prediction has **zero exclusions**:
182 changed bytes = 181 root-code bytes + one symbol-extent byte, with no
metadata changes. All 6,055 other linked bodies and all function addresses
remain fixed. All 189,088 protected Game data bytes across 720 owners match.

- Raw target SHA-256: `97aba6f36d0a65865b41f7f598b96293f2908ce509a63d0cd74da5c8f2a69a5d`.
- Normalized unlinked target: `c384d76ab11f195a41004bccd2d01c156f84f83b0b6689fc9dea949a1603c4dd`.
- Qualified ELF: `78034ee06d159dcf43d73cf66557aa70528a104d580e3632e95665df4fbbdf38`.

## Behavioral qualification

Guest tests run 4,092 ordinary cases / 16,368 executions through original,
raw compiler, guarded padded and actual-Make code across three GNU relocation
layouts, including HI/LO carry. All 58 root words are visited. Eight additional
alias fixtures exercise list/bitset/state/pointer overlap; 222 access-prefix
cuts include 25 branch-delay cuts. Full raw/guarded register, memory, call and
access traces agree. Callback mutations cover current/next list words,
sentinel insertion, state, bitset base and row-pointer changes.

Native SDK32 C passes 262,268 cases at each of O0/O2/O3 with trapping UBSan.
It covers all 65,535 non-sentinel IDs and all 128 callback-mutation modes,
using valid disjoint typed storage. Fifteen compiled semantic controls each
return the designated mismatch result; compiler failures or traps do not
count as controls. Synthetic full-ID tests do not establish retail allocation
bounds or portable alias semantics.

The aligned full-ROM census finds exactly two direct JAL words, at ROM
`0xCA2A8` and `0xCA2D4`, and no aligned literal root pointers. The original
34-word `func_1509CDDC` caller runs its complete 204-record fixed-point scan
in 18 cases / 72 executions. Original `func_1509CCB4` (16 words) and
`func_1509CE64` (49 words) run connected in 72 cases / 288 executions, with
all helper words visited. Fixtures are finite acyclic dependency graphs;
there is no claim about arbitrary cycles or complete gameplay/hardware.

## Adoption and continuation

Both tools copies pass all eight fresh canonical tests and their shared
checks. Installed validation reruns the two source/image gates and reuses
six unchanged semantic gates only through complete artifact, module,
compiler-adapter and input-seal identity. Tools are committed first at
`9532066458126ea83e9039ec91a3bb43c8b42608`, then the consumer source, two guards, tools pin and seven docs.
Root README changes only its two aggregate rows.

Evidence lives in `conker/build/game-dependency-activation-1509CCF4-match/`:
`preparation.json`, `private-semantics-v13.json`, preinstall/installed receipts,
`sealed-production-proof.json`, `75-percent-queue.json`, full function views,
`graph-final-proof.json` and `BANKED_STATUS.json`.
The scoped graph refresh preserves all prior nodes and valid relationships;
the existing s32 return relationship is still valid and is retained.
Historical archived checkpoints can be restored from the sibling Build Archive.

Next screen: `func_150DE6D8`. A queue row is a source-size screen, not ABI or matching
credit. Keep private candidates uncredited until their complete gates pass.
