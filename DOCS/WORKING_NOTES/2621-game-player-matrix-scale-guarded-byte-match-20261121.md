# 2621 - Player matrix scale guarded byte match

Date: 2026-11-21. The total 85% matching goal remains active.

`func_1503A678` now has a complete semantic C implementation. The fresh
production recount is **4,604 / 5,528 (83.29%) total** and **3,931 / 4,855
(80.97%) Game**, zero address drift and 924 different converted functions.
Init remains 492/492 and Debugger 181/181. **95 further matches** are needed
at the current denominator.

## Recovered source, layout and guards

Source: `conker/src/game/generated_64120.c`. Preserved original:
`conker/asm/64120.s:4067`, VA `0x1503A678..0x1503A7F0`, ROM
`0x67B28..0x67CA0`. The function is 94 words / 376 bytes with a 216-byte
frame, S0 at SP+0x18, RA at SP+0x1C and 14 relocation sites. All 18 neighboring
functions, pools and compiler diagnostic rows are preserved under the
existing O2/g3 profile. This owner's natural recipe is pure C.

The byte `D_800C3E78` selects an 812-byte actor from `D_800CC2D0`. Only kind
0x22 enters the body. Actor byte 0x20A produces planar scale
`(u32)byte * 0.015625f + 1.0f`. Phase zero uses that value; other phases use
its reciprocal. Y stays 1.0f. The matrix comes from the actor pointer at 0x1D4
and selector byte `D_80084404[D_800C3FFA]`, at a 64-byte stride.

The function sets the homogeneous column to 0/0/0/1, retains translation XYZ,
initializes a scaling matrix, multiplies into a temporary, copies all 64 bytes
back, restores translation and freshly reloads/increments the phase byte.
Semantic scalar temporaries and declaration order recover the actual homes:
translation SP+0x30/34/38, result SP+0x3C, scaling SP+0x7C and scale components
SP+0xC4/C8/CC. No invented padding, volatile qualifiers or profile changes
are used. Unsigned conversion is split from the floating expression to recover
the retail register lifetimes.

**This is a guarded match, not raw byte-exact C.** Sixteen expected-word guards
change register operand fields only: an eight-word V0/V1 exchange for the actor
and phase, plus eight words across short F0/F2/F10 lifetimes. Every opcode,
immediate, branch target, stack offset, instruction position and relocation
binding is unchanged. No insertion or omission is used. The entire previous
CSV remains a byte-identical prefix. Explicit bitfield proofs and stale-word,
stale-relocation, wrong-function, wrong-owner and duplicate-offset controls
pass. Raw instruction SHA256 is
`e1f281f36dbfc4f2350e899fb3b0d9112244e65e23166d47f338c5062430de0a`.

The local floating call view of `func_150A7CB0` places the three float bit
patterns into o32 A1/A2/A3. The existing provider exposes those words as u32.
Execution of the actual original provider verifies the bit transport and
diagonal stores. This is measured guest ABI agreement, not a claim that the
existing differing C prototypes are formally compatible across translation
units. Provider source and shared headers are preserved.

## Real callback and return contract

The literal census identifies JAL 0x1503A818 in the complete 16-word parent
`func_1503A7F0`, and the GameData pointer at 0x8008859C. That pointer belongs
to `asm/data/22D040.rodata.s`, the function/flag table based at 0x8008857C.
Offset 0x20 selects this function and flag 1; offset 0x28 selects its parent
with flag 1. The parent caches phase, runs its initializer with phase zero,
restores the cached phase and calls this routine.

The actual handwritten dispatcher window is 139 words at
`0x150A9750..0x150A997C`, inside `func_150A94DC`. Its real JALR is at
0x150A986C. Flag 1 saves/restores GPRs and all 32 FPRs, then continues at
0x150A96DC. V0 is restored rather than interpreted as a result. This establishes
the void callback contract and protects the different raw V0/V1 clobbers when
the actor-kind gate skips the body. Those standalone raw volatile registers
are not falsely described as retail-identical.

## Fresh qualification

Run `python3 -m unittest tools.tests.test_game_player_matrix_scale_1503a678_match -v`.
Five focused checks pass before and after installation in primary tools and
the isolated sibling overlay. Imported modules and non-Python inputs are
fingerprinted. Shared `make tools-check` passes. The actual dirty sibling and
its inspected dependency bytes are preserved. Prior unchanged neighbor checks
are retained as reused receipts rather than called fresh tests.

1. The natural three-command Make recipe and actual padder produce all 94
   original words and bindings. The independently predicted full ELF equals
   the link with **296 changed bytes and zero exclusions**, solely the target
   slot and symbol size 12->376. No metadata permutation is needed. GameData
   stays exact across 189,088 bytes / 720 owners. Production rebuilds every
   dependency affected by the guard CSV; its full ELF equals the same prediction.
   Conversion rows are unchanged.
2. Guest checks run 1,792 cases per retail/raw/normalized stream, all 91
   reachable instructions. Words 29/30/31 are the unreachable negative arm of
   an unsigned-byte float conversion. All byte scales, actor indices, phase
   boundaries, both matrix pages, helper mutations and stack phases are covered.
   Public matrix bytes, retained translation, helper inputs and ordered accesses
   agree. Normalized private states and all 74 sampled access-fault prefixes
   equal retail. Raw active states agree under helper ABI clobbers; skipped
   volatile V0/V1 differences are verified through the real callback.
3. The original callback window and parent execute together with each target
   stream for 432 cases. All 139 window words and all 16 parent words execute.
   Complete memory, private stack, restored GPR/FPR state, calls and accesses
   agree at the actual continuation. Three controls detect lost V0 restoration,
   lost F0 restoration and wrong table indexing. A separate 512-case group per
   stream executes the original identity, scale and multiply helpers. Their
   19/19/76 executable words are covered; the remaining 1/1/2 words are verified
   unreachable zero alignment tails. Only the parent initializer and bcopy use
   bounded contracts in these connected groups.
4. Native SDK32 tests run 2,496 cases at each of O0/O2/O3 with strict aliasing
   and UBSan. Owner/matrix extents and field offsets are asserted. Six source
   controls detect an incorrect kind gate, factor, reciprocal, Y axis, retained
   translation and stale phase. Matrix services are bounded native fixtures;
   the original MIPS helper execution is separate evidence.
5. Six GNU links at two independent code/data bases agree with independent
   relocation binding, including signed-low carry. The guarded padded stream
   equals retail; raw is compared against its own register allocation.

An initial private fixture placed matrix storage at the oracle stack address.
The full callback test exposed that overlap. Matrix storage was moved to
0x50000, separation was asserted, and the accepted target/caller suites were
rerun. The accepted comparisons include final matrix bytes as public memory.
No provisional result from the overlapping fixture supplies matching credit.

## Production and continuation

Production ELF SHA256: `3ad7323e8c7c9891a714929c3e063c081476c5cdb6e11c38f2e9992edf5ba722`. Prior consumer
`c58d36739ff8240059486f56b2cde6f403bbdf70`, prior tools `ddee43eb791c35907e828ffbdaf77a214e29c48c`. Tools are committed first.
Codex performs implementation and validation with zero advisory/model calls;
the earlier Claude authentication failure is not retried. Existing unrelated
owner warning 712 and duplicate generated_12D630 Make warnings remain recorded.
The README receives only its Total and Game aggregate row changes.

Sibling host applicability was inspected read-only. Its available saved
scene-recompile configuration consumes binary words/symbols rather than this
decomp C source. No host build, Release change or gameplay acceptance is claimed.

Continue the remaining Game census toward the full 85% goal. Position effect
`func_151BE850` remains private at 181 words / frame 200 / 147 differences,
with an unresolved fallback-neighbor ABI change. Earlier camera/history/query
candidates retain their private handoffs and receive no credit from this work.

Graph maintenance: the native update exited 1 with all
70,212 prior IDs retained. The subsequent serial scoped extraction
covers 6 C/Python files with no missing AST sources, producing
70,254 nodes / 162,392 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
