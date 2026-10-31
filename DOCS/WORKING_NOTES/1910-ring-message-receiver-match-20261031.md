# Working Note 1910: Ring message receiver

Date: 2026-10-31. `func_15043CA4`, ordinary owner `game_70200`.
ROM `0x71154..0x71240`; VA `0x15043CA4..0x15043D90`.
Tools: `e66a15d8b49ea89b779a2e01fe28e8fe6c1dc37b`.

## Recovered behavior and interface

The zero-return placeholder is replaced by
`s32 func_15043CA4(struct105 *queue, u8 *output, s32 capacity)`.
The existing four-word structure holds the ring address, capacity, read cursor
and write cursor. No shared header or structure declaration changes.

An empty queue returns zero without touching the output or calling a helper.
Otherwise the original ring reader consumes a four-byte signed length header.
If the signed output capacity is less than that length, the receiver copies
capacity minus one bytes, appends a zero byte and skips the remaining payload.
If the full message fits, it copies exactly the message length without adding
a terminator. A zero-length message still consumes its header and publishes
the advanced read cursor. The return value is the original message length,
including when the output is truncated. Ring and capacity fields are reloaded
between helper calls, preserving callback mutations and output aliases.

Explicit unsigned subtraction preserves the retail 32-bit wrap in capacity
decrement and skip arithmetic. Invalid nonempty capacities and negative length
headers retain retail's potentially invalid large-copy behavior; bounded guest
prefixes cover those cases. Native positive-domain tests do not claim portable
execution of invalid copies. There is no added clamp or changed wire format.

The aligned census of the complete frozen decompressed input finds one JAL,
at ROM `0x12700`, inside `func_100126E8`, and no literal target pointers.
The original 12-word Init wrapper uses fixed queue `D_800427A0`, forwards its
two arguments and executes the original call delay slot without redirection.
Its existing void C declaration is unchanged; the machine wrapper leaves the
receiver's V0 result intact. This census is not a complete indirect-call claim.

## Match and qualification

The semantic C emits 58 body words under the existing O2/g3 profile. The
retail slot adds one alignment NOP. The frame is 56 bytes; S0/S1/RA are saved
at 28/32/36, initial cursor at 44, header length at 48 and output home at 60.
There are 57 reachable body words. The duplicate load at offset `0x48` is
unreachable and is preserved. All four R_MIPS_26 helper bindings match.

Two expected-word guards close the empty-queue temporary allocation and
commutative branch comparison: offset `0x30`, `8E2F000C` to `8E38000C`, and
offset `0x38`, `55EE0004` to `55D80004`. There are no insertions or omissions.
This is a guarded C recovery, not an unmodified compiler byte match. All four
actual padder stale-word/binding controls reject. Raw C public state, return,
preserved registers and access trace agree; its caller-saved T7/T8 differ.

Guest qualification passes 2,880 cases: 11,520 normalized and 2,880 raw
executions, three independent rebases, 24 aliases, 83 access-prefix cuts,
10 branch-delay cuts and 22 bounded signed-payload prefixes. All reachable
words are covered. Call stubs clobber volatile registers, FPU, HI/LO and
outgoing argument homes and exercise queue-field reloads.

An additional 480 connected cases execute the original 42-word ring reader,
18-word skipper and 11-word memcpy, for 1,920 normalized and 480 raw runs.
The original Init wrapper passes 36 cases, 144 normalized and 36 raw runs.
These checks do not establish producer, gameplay or hardware acceptance.

Native32 O0/O2/O3 each pass 129,256 cases with trapping UBSan, including
512 empty/unbacked full-word cases, real existing reader/skipper C, wrap,
truncation, queue mutation and output aliasing the write cursor. Eight wrong
semantic controls exit 1. Native headers use host byte order; the guest suite
establishes guest header behavior. The private O2 fixture initially faulted on
an SSE aligned stack store; aligning its freestanding entry point corrected
the harness, with no production change.

Both tools copies pass all eight fresh canonical methods without skips.
After installation each passes two fresh installed checks and reuses six
unchanged semantic checks only after full module/artifact fingerprint equality.
Shared tool checks pass. All 15 owner neighbors and pools are preserved;
actual Make executes three owner commands with no inherited diagnostics.

## Production, accounting and handoff

The independent full-image prediction and actual production link agree on
175 changed bytes: 174 target code bytes and one target extent byte. There
are zero metadata changes or excluded ranges. All other 6,055 function bodies
and all 6,056 function addresses are unchanged. All 189,088 bytes across
720 Game data owners remain exact. Existing guard rows and conversion CSV
bytes are preserved. The complete 17,262-file seal is verified before adoption.

Production ELF SHA-256:
`f3f2bcd185eea3d186342924109c3599b0cd83704b48aef6c1ae749c613c6b8c`.
Map SHA-256:
`19139e6eb3cb32838dba4e8909f0275dc9bc2b9ce99a8efd030e800380070e85`.

Recount of the captured installed ELF: Total **3,987/5,506 (72.41%)**;
Game **3,314/4,833 (68.57%)**; Init 492/492; Debugger 181/181; zero drift.
The 75% goal remains open at 4,130 exact functions, with **143** more needed.
The root README changes only its two aggregate status rows. Detailed updates
stay in DOCS. Tools are committed before the consumer; nothing is pushed.
The scoped eleven-file AST graph refresh retains all previous nodes and valid
directed relationships, including the still-valid s32 return edge, without
claiming full-corpus extraction or new global clustering.

Next screen: `func_1509B810`. It remains uncredited until the complete gates pass.
Private candidates, old tools mirror edits and sibling host/Release outputs
are preserved. Evidence is under
`conker/build/game-ring-message-receive-15043CA4-match/`: canonical receipts,
caller census, installed audits, strict image proof, captured-ELF recount,
function views, graph retention proof and final sealed audit.
