# 1890 - Linked actor cleanup scan and endpoint alias

Verified 2026-10-30. `func_150626EC` in `conker/src/game_83300.c` occupies
VA `0x150626EC..0x150627D4`, ROM `0x8FB9C..0x8FC84`: 58 words with no
alignment words. Detailed artifacts are retained under
`conker/build/game-linked-actor-request-150626EC-match/`.

## Recovered behavior and interface

The routine scans actor slots 0 through 24 in the 26-record pool. It invokes
`func_15060F28(record, request)` only when the record has a nonzero
`interaction_state`, its unsigned owner byte at offset 0x65 matches the
one-based owner slot, and its byte at 0x127 equals 255. The owner slot uses
signed truncating division of the SDK32 address difference by 812. Integer
address arithmetic preserves negative and unaligned inputs without undefined
subtraction between unrelated C array pointers. Each iteration reads its gates
from live memory, so a cleanup can change later records. Slot 25 is excluded.

The sole aligned direct call is at ROM `0x8E428`, inside the original cleanup
helper. It forwards owner and request and ignores the return value. The local
placeholder declaration and definition are corrected to
`void (struct127 *owner, s32 request)`. No shared header changes are required.
The helper can recursively invoke the scan for attached actors before clearing
the current record; finite chain and star ownership fixtures exercise that path.

## Matching source and relocation qualification

An indexed 25-record loop recovers all 58 words and the original saved-register
layout: frame 56, RA at SP+52, and s0 through s6 saved. The otherwise unused
v0 initialization is emitted by the compiler's indexed-loop lowering; no
artificial return contract or dead source initializer is introduced.

The compiler expresses the endpoint as `D_800CC2D0 + 0x4F4C`, while retail
uses the named alias `D_800D121C`. Their required relation is checked against
the complete frozen symbol table: `D_800D121C == D_800CC2D0 + 25 * 812`.
Two expected-word/relocation guards change the HI/LO binding names and one
LO instruction immediate. There are no inserted or omitted words. Four actual
padder controls reject wrong instruction or binding preimages; an invalid
endpoint relation is also rejected.

Independent GNU rebases exposed a real qualification limit: the raw object has
multiple pending HI relocations for the same base symbol but different low
addends. A carry-boundary layout can pair the endpoint HI with another base
use under literal GNU linking. That failure is retained as a negative control.
The raw instruction pair is separately checked with a per-register-pair symbol
bound to exactly the same base address; its instruction words are unchanged.
Original and normalized objects use their literal bindings in all three GNU
rebase layouts. The named endpoint normalization removes this ambiguity.
No general raw-GNU-link equivalence across arbitrary layouts is claimed.

## Validation evidence

- Guest: 1,136 cases / 3,408 executions cover all 54 reachable words. The four
  unreachable words belong to constant-divisor exception paths. Complete
  register, memory, trace and access-fault context agree between original,
  raw and normalized streams under the stated relocation treatment.
- 131 access-prefix cuts include 72 branch-delay cuts. Nine rebased cases and
  four additional arithmetic carry layouts pass.
- The connected original helper has 176 words; the selected resource-free
  fixtures visit 83. Remaining cleanup services are bounded explicitly.
  Chain and star recursion, later-record mutations, all owner slots, high
  owner-byte values, signed/unaligned/extreme address inputs and request bit
  patterns are covered. This does not recover the helper's empty C body or
  qualify all resource-release paths.
- Caller qualification executes the original four-word window in 512 cases,
  checking both arguments and ignored return use. Sixteen further cases enter
  the original helper itself with chain/star ownership. No additional function
  is credited from those fixtures.
- Native SDK32/UBSan tests pass 8,640 cases at each of O0, O2 and O3, comparing
  all 26 record buffers and ordered cleanup/finish logs against an independent
  bounded model. Twelve native and IDO semantic controls fail for their
  intended behavior differences. A signed-byte interpreter extension is
  independently checked against all 256 byte values; interpreter failures
  are not treated as effective semantic controls.
- All 88 other owner definitions and pools are preserved. The five actual
  Make commands, including asm-processor preprocessing and postprocessing,
  reproduce the qualified object. The isolated target has no diagnostics.
  The owner's eight pre-existing pointer/integer warnings remain identical
  after normalizing only the temporary source filename; unrelated warnings
  and code are not suppressed or changed.
- The independent full-image prediction equals the first real link with zero
  exclusions: 181 changed bytes, comprising 180 target-code bytes and one
  target-extent byte. No metadata bytes change. All 6,055 other linked bodies
  and every function address remain fixed. All 189,088 Game data bytes across
  720 owners remain exact. Inherited guard rows are unchanged.
- Eight fresh canonical methods and shared tools checks pass in both tools
  copies. Installed source/input/image checks are fresh; six unchanged semantic
  methods are reused only through complete immutable fingerprints.

## Banked checkpoint

Tools commit `4adfeebbf8c14bcabd742dbff21e7fa1e9c6449b` is banked before the consumer pin. The older dirty tools
mirror remains preserved. The adopted ELF recount gives Total **3,967/5,506
(72.05%)**, Game **3,294/4,833 (68.16%)**, Init 492/492 and Debugger 181/181,
with zero address drift. The inventory CSV is unchanged. The README receives
only its two aggregate rows; detailed progress stays in this document.

The scoped Graphify refresh retains prior nodes and valid relationships and
retires the obsolete placeholder return edge. It makes no full-corpus,
clustering, centrality or hardware claim. No push is performed.
The 75% goal remains active: **163** more exact functions to 4,130.
Next private screen: `func_15080348`. Existing private candidates remain uncredited.
