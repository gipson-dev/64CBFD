# 2480 - Side-effect constructor recovered with its pointer interface

`func_1519F1C8` replaces its zero-return placeholder with the complete semantic
constructor. It matches all **124 words / 496 bytes**, with the original
**0xB8 frame**, 51 checked setup-scheduling guards, no inserted words and no
omissions. Production and the independent linked-image prediction agree.

Fresh ELF recount: total **4,510 / 5,514 (81.79%)**, Game
**3,837 / 4,841 (79.26%)**, Init **492/492**, Debugger **181/181**,
zero address drift, **1,004** still different. Exactly one new C match is
credited. The 85% threshold remains 4,687 at this denominator: **177 more**
matches are required. The wider goal remains active.

## Scope and interface

Owner `generated_1CC440`, source `conker/src/game/generated_1CC440.c`,
VA `0x1519F1C8..0x1519F3B8`, code-image offsets `0x1CC678..0x1CC868`.
The verified baseline is consumer `81437a874b164fe0724ce39a5be2a3e64bcddc41`
and tools `74f04ea06485803a06c30dd5811fe330ee274a1b`.

Recover `u8 *func_1519F1C8(u8 *state, u8 mode)`. The allocation result is a
pointer, including the null outcome. Correct both local callers' result types
and the four resource-pointer members of `FourWord1CC440`; this matches the
existing teardown's four-pointer view. All **38 other owner functions**,
including the two callers and the clear/cleanup helpers, compile identically.
No shared header or compiler profile changes.

The constructor snapshots state +0x18's actor before the color selector call.
Public state may change during that call; the original actor is still used
for the packet's reference X/Z, read after the callback. The query itself reads
the live state actor. Literal and palette reads also retain their retail order.

## Two complete local records

The factory's first argument is a **28-byte request**, not just a 12-byte
position vector. Its copy in `func_15147A80` and the original assembly establish
the full layout. At the root's SP+0x98:

| Offset | Type | Value or source |
| --- | --- | --- |
| 0x00 | three floats | Query output; untouched when the query fails |
| 0x0C | s16 | Lifetime 300 |
| 0x0E | u16 | Flags 0x42; OR 4 after a successful query |
| 0x10 | s32 | Zero-extended incoming mode byte |
| 0x14 | byte | Untouched |
| 0x15 | byte | Count 10 |
| 0x16..0x1B | bytes | Untouched |

The separate **80-byte payload** starts at SP+0x48. It contains the owner
pointer, kind 6, the two literal floats `D_800A8CE8`/`D_800A8CEC`, a conditional
position copy, zero phase/elapsed fields, the captured actor's reference X/Z,
three bytes from `D_800AB414[color * 3]`, and the complete retail preset:
200, 255, 40, 25, floats 1 and 1.5, style bytes
0x03/0x55/0x03/0x55/0x88/0xC4, two zero halfwords, count 6 and command 0x325.
The local type names describe recovered use; they are not recovered original
debug names.

Reserved bytes and failed-query position fields are deliberately not zeroed.
The guest proof and model retain their exact original stack-byte provenance.
Native checks read only fields initialized by the selected path; copying
reserved bytes does not establish portable values for uninitialized fields.

Call the exact query recovered in [Note 2479](2479-game-perpendicular-offset-derived-parameter-home-match-20261115.md).
On success, copy all three position words and OR request flag 4. The factory
receives `(request, 0x50, 0x24, 5, 5, 5, 0, 0, state + 0x34, 255, 1)`.
On a nonnull result, copy the full payload to the pointer at object +0x98.
Return the allocation result in both branches; the memcpy return is ignored.

## Compiler and instruction proof

The selected semantic C emits **124 words** naturally with the **0xB8 frame**.
Declaration order restores the actor home at SP+0xB4 and both exposed records
at their retail addresses. No volatile/register bindings or artificial frame
padding are introduced. Eight argument/order screens and ten additional kind
placement screens are retained privately; alternatives are not installed or
credited.

Raw target SHA-256:
`1f9c4ce034b21320ffe0766270c3a0060da69d4e8693101302bc33be8a8a0f4f`.
Ten original relocation entries are pinned. Fifty-one expected-word guards
normalize independent setup scheduling and scratch-register roles, preserving
all 124 C-generated words. Every old manifest byte remains intact.

The instruction-driven symbolic proof covers all **four query/allocation
outcomes**. It compares ordered public reads, caller-visible results, saved
registers, FCSR propagation, all 80 passed packet bytes and all 28 request bytes.
Opaque helpers may alter public state and passed packet/output storage. Untouched
bytes are symbolic tokens for their actual initial stack addresses. Three
semantic negative controls fail; every changed raw instruction and binding is
also rejected by 134 fingerprint controls.

Proof preconditions are valid mapped/aligned storage and the normal o32 ABI.
Opaque providers cannot inspect implementation PCs/unpassed private storage or
retain private addresses after return. This is normal observation equivalence;
it does not equate private/scratch fault registers or portable undefined input.

## Fresh qualification

- **1,920 cases per stream**, retail/raw/guarded, cover query and allocation
  outcomes, mode narrowing, color 0/10/255, two stack phases, callback mutations
  and payload destinations overlapping public owner, actor or palette storage.
  All **124 root words** execute. Four effective semantic instruction controls.
- **512 cases per stream** execute the complete original 94-word query and its
  original 7-/27-word heading and phase helpers, checked against the current ELF.
- **80 cases per stream** additionally execute the complete original 115-word
  factory and 11-word memcpy. Verify allocation `(77, 1, 600, 1, 255, 1)`,
  request and optional-record copies, six flags, payload/end pointers, zeroed
  ranges, exact 80-byte payload and null outcome. These dependencies match the
  current ELF before connection. Allocation/bzero remain explicit opaque hooks.
- **795 fired access cuts** compare public effect prefixes across all three
  streams. Private scratch state and uninstrumented opaque helper internals are
  outside this claim.
- **240 native32 cases per profile**, six O0/O2/O3 strict/no-strict aliasing
  profiles, UBSan traps and actual typed request/state/actor/output objects;
  nine effective source controls. Reserved/failed-query fields are not read.
- Both complete original callers (`func_1519F3B8` and `func_151A084C`) plus the
  original cleanup helper: **160 cases per stream**. All three direct JAL sites
  are covered (`1519F3C4`, `1519F3E0`, `151A08BC`). The scanned code image is
  **2,467,288 bytes**, not the complete asset ROM; computed calls are not claimed.
- Both padders, two independent symbol rebases, real Make's five-command
  owner recipe, independent GNU ELF link, strict whole-image prediction,
  production adoption/recount and installed suite pass. Shared tools checks pass.

The full suite also passes against a seven-file ignored overlay on the separate
`64CBFD Tools` checkout. Its HEAD
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a` and all **2,434 dirty paths** remain
unchanged; no conflicting sibling file is overwritten. The primary tools
checkpoint is **`8159f5ebfeba1577c6ed180c98b373a0e74fd0e0`**, committed before the consumer pin.

## Production and next boundary

The **875-input** frozen baseline changes only the source, guard manifest,
owner object and ELF. Only one of **698 objects** changes; all 38 owner neighbors,
all **6,050 other linked functions**, all addresses and **189,088 protected data
bytes** remain unchanged. Conversion CSV/classifications stay fixed.

The predicted complete ELF delta is **421 bytes**, zero exclusions. It includes
one explicitly pinned symbol/string-order swap:
`[D_800A8CEC, func_1509C414] -> [func_1509C414, D_800A8CEC]`.
Names, bindings, addresses, extents and protected contents remain unchanged.
Production ELF SHA-256:
`6266954e3b007f64c072dda4628fbd885560eaad2f71d25692cbd1ea3c3647ae`.

Receipts and rejected probes are retained in
`conker/build/game-side-effect-constructor-1519f1c8-private/`. Reproduce with
`python3 -m unittest tools.tests.test_game_side_effect_constructor_1519f1c8_match -v`
under the prepared PSBBN environment. Historical frozen/private receipts remain
immutable. The seven-file scoped AST refresh preserves all **62,213 prior IDs**;
this is not full-corpus extraction. Five DOCS indexes get one concise entry;
the root README changes aggregate rows only. No Claude calls, push, host build,
Release changes, save changes or private-input changes.

Next: **`func_1519F4F0`**, the **192-word** remaining placeholder in this same
owner, VA `0x1519F4F0..0x1519F7F0`, offsets `0x1CC9A0..0x1CCCA0`, frame 0x78.
Its linked effect payload now has a recovered constructor. Read its complete
retail body and actual callback interface, then qualify the source and all
production gates independently before credit. No new candidate for it exists.
