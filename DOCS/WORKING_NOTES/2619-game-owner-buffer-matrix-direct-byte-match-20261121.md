# 2619 - Owner matrix buffer direct byte match

Date: 2026-11-21. The total 85% matching goal remains active.

`func_151BEB20` now reconstructs the owner's selected matrix buffer directly
from semantic C. A fresh production recount measures **4,602 / 5,528 (83.25%)
total** and **3,929 / 4,855 (80.93%) Game**, with zero address drift and 926
different converted functions. Init remains 492/492 and Debugger 181/181.
The existing denominator requires **97 additional matches** to reach 85%.

## Recovered source and layout

The owner is `conker/src/game/generated_1E73B0.c`. The preserved original body
starts at `conker/asm/1E73B0.s:5219`, VA `0x151BEB20..0x151BEC94`, ROM
`0x1EBFD0..0x1EC144`. Its complete slot is 93 words / 372 bytes, with a
32-byte frame, S0 at SP+0x18 and RA at SP+0x1C. Seven relocations comprise
three HI16/LO16 pairs and the call to `func_150A8050`.

The local `BufferedMatrixOwner1E73B0` view exposes XYZ at 0x54/0x58/0x5C,
two 64-byte matrices at 0x7C/0xBC and the rotation angle at 0x120. The function
calls the existing SDK-compatible matrix helper with the selected buffer and
angles `(0.0f, owner->angle, 0.0f)`. After the call it snapshots
`D_800AA8E0`, copies translation into matrix row 3 and scales the nine upper
3x3 entries. Every destination independently reloads the byte `D_800BE9C0`.
It returns 1. Helper mutations therefore affect the selected destination,
the snapshotted scale and the copied owner fields at their original points.

The first complete draft matched all 93 retail words under the existing O2/g3
profile. Raw instruction SHA256 is
`9d50563ea66572abcc19eb3276a56cd92d1882987e27cf2a7bc17a0d8ecfcb61`.
There are zero guards, inserted words or omitted words. All 56 neighboring
functions, their relocations, constant pools and compiler diagnostics are
preserved. The existing mixed C/GLOBAL_ASM membership is retained.

## Qualification

The focused entry point is
`python3 -m unittest tools.tests.test_game_owner_buffer_matrix_151beb20_match -v`.
All five checks passed before and after installation in both the primary tools
checkout and the isolated sibling overlay. Imports and non-Python inputs are
fingerprinted. The actual dirty sibling checkout and its dependency bytes are
preserved. `make tools-check` also passed.

1. Raw C and padded target payloads equal the complete original body and
   relocation map. The natural mixed Make recipe runs five commands. The
   independently predicted whole ELF equals the actual link with **297 changed
   bytes and zero exclusions**. Besides the target slot and symbol size
   12->372, the prediction includes one closed symbol/name permutation between
   `D_800AA8E0` and `D_800A1040`. Both definitions and attributes are retained,
   accounting for two symbol records and 22 string bytes. GameData remains
   exact across 189,088 bytes and 720 owners. Conversion rows are unchanged.
2. Guest execution checks 1,248 cases for each retail/raw/padded stream, all
   93 instructions, complete memory and private stack, registers, return value,
   helper arguments and ordered accesses. The corpus includes all 256 selector
   bytes, scale boundaries, selector/scale/owner mutations and aliases that
   modify globals during destination writes. All 172 access-fault prefixes
   agree. Three instruction controls are effective.
3. Native SDK32 runs 768 cases at each of O0/O2/O3 with strict aliasing and
   UBSan. Owner extent and field offsets are asserted. Valid buffer indices
   0 and 1 exercise helper changes and all nine products. Six source controls
   detect incorrect translation, product, missing product, return value,
   stale scale and stale page. Byte-index and alias probes beyond these valid
   C objects belong to the guest instruction checks.
4. The complete 17-word `func_150C52CC` caller and 19-word
   `func_150C5280` predicate are byte-exact in the current ELF. The wrapper
   dispatches through the immutable GameData pointer at `D_8008ADA8`, executing
   its real JALR at 0x150C52F8 with the owner in A0. All 992 cases per stream
   check the skip/call gate, signed result and preserved registers. All 17
   caller words and 18 reachable predicate words execute. The remaining
   predicate word is the unreachable duplicate zero assignment. Three caller
   controls are effective. The aligned-reference census finds this one loaded
   function pointer and no direct ROM JAL/J references to the target.
5. Six GNU links test retail/raw/padded code at two independent code/data
   bases. All call and HI16/LO16 relocations agree with independent binding,
   including signed-low carry at the alternate data base.

The matrix helper uses a bounded 16-word output contract with selector,
scale and owner-field mutations and ABI clobbers. Its current 84-word slot
is retail-exact and preserves the existing handwritten kernel. Complete trig,
FCSR and hardware behavior is outside these target tests. Prior unchanged
neighbor-suite receipts are retained separately from the fresh target checks.
The existing duplicate generated_12D630 recipe warning and existing unrelated
owner diagnostics remain recorded in the build logs.

## Production and repository state

Actual production Make and the fresh recount pass. Production ELF SHA256 is
`57f5e0e496438c886b0195112c86a33975ee4717b2baa0d9434d6dced49cdde1`. The prior consumer commit was
`028b8958320b338863a1f56d2f1b50b77919afc8` and the tools baseline was `07d57b6430282cf3c367f444cc2ce27f21247493`.
Codex performed the work with zero advisory/model calls. The previous Claude
authentication failure was not retried. Tools are committed before the consumer.
The root README receives only its Total and Game aggregate row updates.

The available sibling host directory contains scene-recompile inputs and
configuration. Its saved input does not contain this target retail window,
and its configured symbols file is absent. The configuration consumes binary
words and symbols. This C recovery provides no direct source import into that
configuration. Host applicability was checked read-only and the Release
checkpoint remains frozen.

## Resume boundary

Inspect the preceding `func_151BE850` next, beginning with its complete retail
body, callers and owner profile. Camera event `func_15096A68`, keyed history
`func_15188F84`, sequence query `func_15022024` and camera transition
`func_15128030` retain their existing private handoffs and receive no new credit.

Graph maintenance: the native update exited 1 with all
70,112 prior IDs retained. The subsequent serial scoped extraction
covers 6 C/Python files with no missing AST sources, producing
70,154 nodes / 161,394 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
