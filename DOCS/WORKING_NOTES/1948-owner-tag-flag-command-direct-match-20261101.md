# First owner/tag flag command restored directly from C

`func_1506D958` emits all **72 retail words directly from C**, with no frame,
guards, assembly inserts, omissions or compiler-profile change. Its full
288-byte slot matches under the existing O2/g3 owner profile.

Production Make and the live Windows-checkout recount agree on **4,021/5,506
(73.03%)**, Game **3,348/4,833 (69.27%)**, Init 492/492 and Debugger 181/181,
zero drift and 1,485 different. **109 more matches** are needed for the active
4,130/5,506 threshold. Tools were committed first at `37ecbcc`.

## Recovered operation and callback interface

Owner/source `game_981E0`, `conker/src/game_981E0.c`.
VA **1506D958..1506DA78**; ROM **9AE08..9AF28**.
The false integer-return placeholder becomes `void func_1506D958(void)`.
The sole aligned ROM pointer is D_800863FC[29], at VA80086470 / ROM22AF30.
There is no aligned direct JAL or second pointer literal. Original dispatch
ignores the callback result.

Capture D_800D1580's low byte as matchByte and bits 8..15 as flagBits. Scan
actor slots **0 through 24**, excluding the declared pool's slot 25. Select
only the first record satisfying all three conditions, in this order:

1. Its 32-bit interaction_state is nonzero; negative states qualify.
2. Its unsigned tag byte +0xAB equals matchByte.
3. Its unsigned link byte +0x65 equals D_800C3E78 + 1, evaluated as an integer.
   Owner byte 255 produces 256 and cannot match a byte; it must not wrap to zero.

For the selected record, clear flag-byte +0x101 bit zero, then OR the **entire
command high byte** into that byte. The high byte is neither a Boolean nor a
single-bit value. Return immediately; no later record is updated. No match
performs no write. Header types and the pool's 0x32C stride remain unchanged.

The source uses a simple indexed 25-record loop and two compound assignments.
The compiler peels slot zero and unrolls the remainder two ways. The peeled
slot-zero path combines the assignments into **one store**. Later-record paths
retain **two stores**, first the bit-clear result and then the OR result. Both
are original instruction behavior and remain present. Two word-sized masked
locals, with the low-byte assignment first in source, recover the original
register roles and first-record scheduling without normalization guards.

## Compiler, owner, Make and complete image

The isolated C is warning-free. Raw C body SHA-256:
`76c311ebb56531540a75eafa0c5511b91d37e6a685e7b17da579139aa233173e`.
Its 20 pinned relocation fields derive record aliases from D_800CC2D0.
The original assembly names aliases such as +0xAB, +0x65, +0x101, +0x32C and
+25*0x32C separately. Raw binding names are not claimed identical. Relocation
qualification preserves those relationships and proves all 72 linked words
identical at three independent code/pool address layouts, including HI/LO carries.

All **327 other raw/padded owner functions** and owner pools remain unchanged,
including the preceding four restorations in this owner. The 36 inherited owner
warnings are unchanged. The actual five-command Make recipe emits the qualified
padded object byte for byte. Makefile, shared headers, guards, layout and C
conversion inventory remain unchanged. Shadow linking retains the original
object basename for the synthesized FILE symbol of this owner with overflow code.

An independent literal whole-image prediction changes only this slot and its
symbol extent from 12 to 288 bytes: **251 changed bytes**, with no exclusions
or metadata reordering. All **6,056 function addresses**, **6,055 other linked
bodies**, and **189,088 protected Game data bytes / 720 owners** remain fixed.
Production ELF SHA-256:
`56dfb862d6a37ea40ec9e0bfdb47acc8a1d1faefbd4d69fdfa26afe27741e3d6`.
Native installation changes exactly source, padded owner object and ELF.
All other prior **17,534 sealed inputs** remain unchanged before the explicit
new tools/documentation refresh. **1,009 focused inputs** are frozen.

## Instruction, access-prefix and native qualification

- **2,455 guest cases / 9,820 executions** compare original assembly, isolated C,
  padded owner and actual Make output. The complete case corpus runs at retail
  addresses; two other relocation layouts run the scan-boundary corpus. This
  is not described as a full Cartesian corpus at every layout.
- All **70 reachable words** execute. The duplicate next-record load at +0xC8
  and pointer step at +0x10C follow unconditional returns and are unreachable;
  both remain in the complete body without being counted as executed.
- Cases cover all 256 mask, tag and owner bytes; every slot including excluded
  slot 25; no match; all three rejection gates; zero/negative active states;
  multiple candidates; and ignored upper command bits. All registers, memory,
  reads, writes, traces and saved state agree across the four programs.
- Every selected slot is checked for its exact flag effect and store count.
  **139 controlled access prefixes / 556 executions** compare state before
  every access for representative slots 0, 1, 2 and 24. For each later slot,
  stopping before the final store exposes the intermediate cleared byte.
  These are guest instruction-prefix checks, not portable C fault semantics.
- **80 cases / 1,280 executions** qualify the original 19-word indirect
  dispatch window at VA1506AEB0..1506AEFC, including table entry 29, four
  callback-return poisons and both post-call script-index paths. Callback
  return is ignored before v0 is replaced. Full dispatcher reachability and
  gameplay acceptance are not claimed.
- **2,175 native cases each at O0/O2/O3**, with UBSan, field/stride assertions,
  final background canary checks and seven effective controls: Boolean mask,
  wrong command byte, positive-only active states, wrapped owner increment,
  including slot 25, continuing after a match, and clearing the wrong bit.
- Both tools copies pass six fresh focused tests before and after installation,
  plus shared checks. Body/binding and literal-image corruptions are rejected.
  Neighbor suites are reused through exact body/pool identity, not claimed fresh.

The first public test receipt had incorrect hard-coded corpus totals; the
independent runtime receipt already recorded 2,455 guest and 2,175 native cases.
The expected totals were corrected and both full public suites rerun before
installation. Case generation, semantic checks and the selected C were unchanged.

## Artifacts and next boundary

`conker/build/game-owner-flag-command-1506D958-match/` holds frozen inputs,
source screens, original/selected/owner objects, Make commands, independent first
link, caller census, access-prefix/runtime qualification, installed recount,
Graphify proof, current seals and bank receipts. Public modules are
`game_owner_flag_command_match.py`, `game_owner_flag_command_oracle.py` and
`test_game_owner_flag_command_match.py`.

Graphify receives an eleven-file scoped AST refresh preserving prior nodes and
valid edge occurrences; the two false integer-return edges are archived.
No full-corpus extraction or reclustering is claimed.

Next ordinary C placeholder: **func_1506B3B8**, same owner, VA1506B3B8,
ROM98868, 77 words and 32-byte frame. Audit the complete position/actor update,
helper calls and caller contract before reconstruction. Scalar smoothing and
other private stages remain uncredited. No Claude calls, host/editor/Release
changes or network push.
