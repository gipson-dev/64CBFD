# Recursive dependency readiness guarded C match

Verified 2026-10-28. `func_1509CBD4` is adopted after canonical qualification,
production reproduction and the actual native ELF recount. Its complete
48-word / 192-byte slot, 40-byte frame and five relocation bindings match
retail using semantic C and twelve checked normalizations.

## Recovered behavior and ABI

Owner: `conker/src/game/generated_C9EC0.c`. Retail VA
0x1509CBD4..0x1509CC94, ROM 0xCA084..0xCA144. The interface is
`s32 func_1509CBD4(s32 index)`.

The first pointer in each inline 20-byte descriptor at `D_8008743C` selects
a halfword dependency list terminated by 0xFFFF. Each dependency must itself
pass the recursive check and have its active bit set through `D_800D2E4C`.
An empty list returns 1; the first failed condition returns 0. Preserve the
original order: recurse first, reread the list value and bitmap pointer, then
test the bit and recursive result. Do not add an index, cycle or depth clamp.

The original frame saves S0..S3 at +0x14..+0x20 and RA at +0x24. Its self-call
uses A0 and a literal J26 binding at +76. The other four bindings are the
HI16/LO16 pairs for the descriptor and bitmap globals at +40/+48 and +52/+56.
The list sentinel limits list traversal; it does not impose a root-index bound.
Guest tests cover wrapped indices separately from valid allocated native C
storage. Native32 tests disable strict aliasing for the original flat pointer
storage and use trapping UBSan.

## Twelve checked normalizations

The semantic source emits the complete body. All guards require the exact
compiled word and relocation state before changing it. No words are inserted
or omitted, and no relocation site, frame or saved-register slot moves.

- At +60/+68/+72, normalize the closed opening value lifetime. Raw C loads the
  halfword into S0 and uses a likely equality branch whose delay slot sets the
  return value. Retail loads T7, assigns the identical S0 value in a nonannulled
  delay slot and reaches the existing return-one instruction before restoring
  the frame. All 65,536 possible halfwords are checked at both common joins.
- At +92..+120, normalize one closed bitmap-check scratch allocation, including
  two commutative operand orders. S0, the recursive result and saved pointers
  retain their meaning.
- At +152, normalize the symmetric sentinel-comparison operand order.

The second halfword load at +144 is unreachable after the preceding
unconditional failure branch. All 48 literal words are checked; dynamic
coverage correctly reports the other 47 reachable words.

## Actual owner profile and preservation

The existing owner Make rule uses `-O2 -g3 -Wo,-loopunroll,0`. The initial
generic screen omitted that option and enlarged the already matched
`func_1509CB68`; the full padder rejected it. The accepted qualification uses
the existing compiler-only no-unroll adapter and actual generated Make recipe.
All 18 other compact and padded functions and owner pools remain unchanged.
There is no profile change or excluded neighbor.

The actual three-command Make shadow and production build emit the same padded
owner. Compiler diagnostics are empty. The strict complete-image prediction
changes exactly 146 bytes: 145 target code bytes and one function-size byte
from 12 to 192. There are zero exclusions or metadata reorder allowances.
All 6,056 function addresses, 6,055 other disassembly bodies, named definitions,
720 protected Game data owners / 189,088 bytes and the map remain fixed.
The inventory CSV is unchanged. Twelve guard rows are appended after the exact
historical manifest bytes.

## Canonical qualification

The tools now separate the core, reusable execution oracle and eight tests.
Both tools copies pass all eight fresh canonical methods and their shared
tools checks. The final accepted run is `canonical_v4.py`; earlier packaging
scope/path attempts and the pre-whitespace execution receipts remain archived.
Explicit module paths ensure each copy executes its own three canonical files.

- 5,380 finite recursive graph cases compare raw C, normalized code and retail
  instructions against an independent result/call reference. Cover trees,
  shared dependencies, repeated edges, deep chains, high child values and
  wrapped empty roots. Complete memory and access traces agree.
- A deliberate physical stack alias makes a child frame overwrite the bitmap
  pointer with five. The actual recursive instructions and raw C both reload
  that new pointer value. No synthetic provider hook creates the mutation.
- 283 fired fault and cycle-prefix pairs compare full registers, memory, PC,
  branch-delay state, calls and access traces. Cycles retain the original
  unbounded recursion; a bounded prefix is not claimed as a terminating result.
- Native32 O0/O2/O3 each pass 268,284 cases and seven effective controls: all
  65,535 nonsentinel child values, all bitmap bytes at eight boundary nodes,
  and every mask of a twelve-edge chain. Verify input storage and buffer fences.
  The freestanding startup explicitly aligns its stack for optimized builds.
- 65,536 actual MIPS opening-join pairs prove the entry normalization for every
  halfword value, including the empty-list path.
- Three actual GNU layouts, including signed-low-half carries, pass eighteen
  recursive cases. The strict isolated padder consumes the exact twelve target
  rows; the complete owner separately consumes the full manifest.
- Two compiled IDO controls reject skipped recursion and a wrong result. Ten
  effective rejection controls cover raw words, bindings, guards, the inherited
  manifest and complete-image corruption; the final image method also checks
  six corruptions independently.

Each production-installed copy then passes two fresh owner/image methods and
reuses six semantic results only after the complete source/module/input/artifact
fingerprints agree. Freeze 16,274 current inputs and 273 focused inputs; all
25 unique preparation/Make artifact fingerprints remain valid.

## Complete return-consuming caller

The current `func_1509B4A0` already matches its complete original 208 bytes /
52 words and 48-byte frame. Its call at ROM 0xC89B4 / VA 0x1509B504 reads a
halfword ID, tests this routine's signed32 result and invokes `func_1509B5AC`
only on success, forwarding its saved second argument. It reloads the live
list pointer and count as execution proceeds.

All 52 caller words are visited across 576 connected cases with actual target
recursion and bounded outer-helper effects on the bitmap, list pointer and
count. Those four outer helpers remain bounded contracts; this work adds no
helper C credit, full pipeline, gameplay or hardware acceptance.

## Banking and measured progress

Tools commit `1387bd07289c0f0f946c5ef4e1f6c8eeb9cb8c07` precedes the consumer
source/guard/pin/documentation commit. Preserve the standalone mirror's 1,748
inherited dirty paths and its three new canonical modules; do not commit or
reset that separate mirror. No push is requested or performed.

The adopted native ELF recount is **3,847 / 5,506 exact C functions (69.87%)**;
Game **3,174 / 4,833 (65.67%)**, Init 492 / 492 and Debugger 181 / 181.
There are 1,659 different C functions and zero address drift. The 75% goal
remains open at 4,130 required matches, with **283 more** needed. Only this
function is removed from the predecessor queue: 1,530 placeholder source
shapes, 120 semantic/other and nine unlocated entries remain.

Next inspect `func_150D596C` in `generated_1028F0`. `func_1514E920` remains
parked and uncredited. Keep function details in notes and status documents;
the root README changes only its two aggregate match rows. Refresh eleven
changed code/document/tool sources in Graphify, retain all old nodes and valid
contexts, and validate the actual self-call and caller relationship. The CSV
appendix is audited independently; outside-scope graph freshness and global
analytics remain historical.

Private reproduction evidence is under
`conker/build/game-recursive-dependency-readiness-match/`, including
`preparation.json`, `tests-*-preinstall.json`, `tests-*-installed.json`,
`sealed-production-proof.json`, `sealed-live-adoption-audit.json`,
`75-percent-queue.json` and the independent native final audit.

| Artifact | SHA-256 |
| --- | --- |
| Raw C body | `a70bbbf44cf0f326dded327566a1e9d78ef896e1d38095047e898c7e4ab31613` |
| Normalized/original relocatable body | `1aa89546ea48a2aed2814cc77d4440fe10e33c207322144ee41d4f0de1efca8b` |
| Complete retail slot | `c5c69000b343e2f2c508a6a5186639631972bd019baae66b49b5d2bfeb34c4b0` |
| Qualified padded owner | `7c589c76f7ba69811ae9b502376ba821ef8c3234a451574c5fb1287f9b18f36b` |
| Adopted ELF | `e8a939f26b31041a250422843deea4be69cc97c004014e43e6fbfb89b522bf76` |
| Extended guard manifest | `70585f37f91bfac072fa8df784c94ef782fbdb6f2d4fe295f5aed132195433bb` |
