# Working Note 1913: Owner matrix scale callback

Date: 2026-10-31. `func_15108D24`, generated owner `generated_135D00`.
ROM `0x1361D4..0x1362C0`; VA `0x15108D24..0x15108E10`.
Tools: `81c550dd8971f3c83b04350ccde632c77302c3c5`.

## Recovered behavior and callback interface

The zero-return placeholder becomes
`s32 func_15108D24(u8 *owner, s32 view)`. The original dispatcher passes a
sign-extended 16-bit view as the second argument. This callback preserves its
incoming home slot but does not use that argument. It always returns one,
allowing the dispatcher to emit the owner's matrix/segment/display-list commands.

The callback captures `owner + *(s32 *)(owner + 0x50) + 0xF8`, then asks
`func_150A8050` to build a local rotation matrix from that state's first and
second floats, with a zero middle angle. After the helper returns, it copies
the captured state's float at `+0x10` into matrix element `[3][1]`.
It multiplies exactly the nine upper-left 3x3 basis elements by `D_800A2490`.
The remaining matrix elements, including the height translation, are unscaled.

The scale and page globals are read after the rotation helper. The state pointer
remains the one captured before that call, even if a callback changes the owner's
offset field. `guMtxF2L` publishes the matrix to
`owner + 0x78 + ((u32)D_800BE9C0 << 6)`, then the callback returns one.
No shared headers, dispatcher source, table bytes or SDK implementation change.

## Compiler and normalization evidence

Ordinary O2/g3 emits the complete 59-word slot with its original 96-byte frame
and all six relocation bindings. RA is at SP+20, the captured state pointer at
SP+28, the 64-byte matrix at SP+32, and the two argument homes at SP+96/+100.
All 59 words are reachable; there is no alignment padding.

Seven expected-word guards normalize closed state-offset, page and owner
temporary-register cycles, at word indices 7, 8, 42, 44, 45, 47 and 48.
The global-page HI16/LO16 bindings are checked by name and retained. No floating
operation, call order or access order is changed. There are zero insertions or
omissions. All fourteen actual padder stale-word/binding controls reject.
This is a guarded C recovery. Raw C public memory, calls, observed matrix,
return, preserved registers and access traces agree; temporary GPRs differ.

All ten owner neighbors and pools remain identical, with no compiler diagnostics.
Actual Make's compiler, padder and assembler reproduce the qualified object.

## Behavioral qualification

Guest checks pass **2,376 cases**, 9,504 normalized and 2,376 raw executions,
across three independent code/global rebases. They cover every body word,
all nine products, unscaled height, signed offsets, pages including 255,
callback mutation of scale/page/height/owner offset, signed zero, subnormals,
and nonfinite inputs. Ninety-nine access-prefix cuts include three delay-slot
cuts. All normalized architectural state and traces agree across original,
normalized C, padded and actual Make objects.

An additional **576 cases**, 2,304 normalized and 576 raw runs, execute the
original 116-word `guMtxF2L` across all four rounding modes. This connection
uses finite values within signed-conversion range. The rotation provider stays
opaque; no complete FCSR exception or invalid-conversion behavior is claimed.

Native32 O0/O2/O3 each pass **14,080 cases** with trapping UBSan and ten wrong
semantic controls that exit 1. Finite, signed-zero and subnormal observations
are compared bit-for-bit; NaNs are compared by classification without promising
a particular payload. Mutation cases distinguish a captured state pointer
from a recomputed pointer and live post-helper scale/page from stale values.

The aligned frozen-input census finds no direct JAL and one literal pointer,
at ROM `0x22E6EC`, slot one of the original seven-entry `D_80089C28` table.
**360 cases**, 1,440 normalized and 360 raw runs, execute the original 75-word
`func_1513B83C`: table fetch, JALR delay slot, signed view forwarding, callback
result test, visibility/skip gates and the three emitted graphics commands.
The callback's rotation/converter providers are opaque in this caller suite;
the separate converter connection establishes the bounded original conversion.
This does not establish whole-renderer or gameplay acceptance.

Both tools copies pass eight fresh canonical methods and shared tool checks.
After installation each passes two fresh installed checks, reusing six semantic
checks only after full input, module and qualified-artifact fingerprint equality.

## Strict production image and progress

The independent complete prediction agrees with the production link on
**200 changed bytes: 181 code bytes, one target extent byte and 18 metadata bytes**.
The metadata is one closed permutation of the named symbol/string-table pair
`D_800A2490`, `D_80090A00` at symbol-table offset `0x2D4474`.
The predictor verifies the original names, addresses, attributes and contiguous
string block before reordering that pair. There are zero excluded ranges.

All other 6,055 linked bodies and all 6,056 function addresses remain unchanged.
All 189,088 bytes across 720 Game data owners remain exact. Existing guard rows
and conversion CSV bytes are preserved. The complete pre-adoption seal checks
17,283 files; the final banked seal includes the new note as file 17,284.

Production ELF SHA-256:
`9d0ddf117f5941f532908ea7e4c6bef546a5fecda308844ba2345ba73b948277`.
Map SHA-256:
`19139e6eb3cb32838dba4e8909f0275dc9bc2b9ce99a8efd030e800380070e85`.

Captured installed-ELF recount: Total **3,990/5,506 (72.47%)**;
Game **3,317/4,833 (68.63%)**; Init 492/492; Debugger 181/181; zero drift.
The 75% threshold remains 4,130, with **140** further exact functions needed.
Tools are committed first. The README changes only its two aggregate rows;
detailed progress stays in DOCS. The eleven-file scoped AST update retains all
old nodes and valid relationships, including the still-correct s32 return edge.
No full-corpus extraction or new global clustering/centrality is claimed.

Next screen: `func_15109410`, uncredited until the complete gates pass.
Evidence is under `conker/build/game-owner-matrix-scale-15108D24-match/`.
Private candidates, older tools mirror changes and sibling host/Release outputs
are preserved. No push is performed.
