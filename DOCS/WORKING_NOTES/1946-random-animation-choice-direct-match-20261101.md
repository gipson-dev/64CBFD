# Random animation choice restored directly from C

`func_1506B634` now emits all **67 retail words directly from C**, with its
original 24-byte frame, incoming byte reload and compiler-generated divide guard.
The full 268-byte slot is exact, without guards, assembly insertion, omission
or a compiler-profile change.

Production Make and the live Windows-checkout recount agree on **4,019/5,506
(72.99%)**, Game **3,346/4,833 (69.23%)**, Init 492/492 and Debugger 181/181,
zero drift and 1,487 different. **111 more matches** are needed for the active
4,130/5,506 threshold. Tools were committed first at `eeecc3d`.

## Recovered operation and byte interface

Owner/source `game_981E0`, `conker/src/game_981E0.c`.
VA **1506B634..1506B740**; ROM **98AE4..98BF0**.
The false `s32 func_1506B634(s32)` placeholder becomes
`void func_1506B634(u8 choiceCount)`. Both actual callers pass constant nonzero
bounds (8 and 2) and ignore the result. The superseded commented nonmatching
draft beside the placeholder is removed; original assembly is retained.

1. Call `func_150ADA20`, interpret its low word as unsigned, and take its
   unsigned remainder by choiceCount. The argument is stored in its incoming
   home, then reloaded as a byte after the random helper returns.
2. Load current actor/state after that helper. If state byte +0x16 is nonzero,
   use packed byte table D_80099ABC, remapping choice 7 to 0 only in category
   0x29. Otherwise use packed byte table D_80099AB4 with the original remainder.
   Both legacy shared declarations are s16 arrays; explicit local u8 views
   recover the actual lbu access without broad shared-header changes.
3. Store the selected byte into unsigned state halfword +0xE. Reload the
   current actor and state before testing that halfword against 0xA7.
4. For 0xA7, write packet word FF020144 to D_800D1580 before the second random
   call. Store unsigned random modulo 3 plus 2 to the current state's byte +0xC.
   Call `func_1506E8D8`, then reload current actor and live factor D_80099C38
   before multiplying its xz_velocity at +0x3C.

The existing random helper's s32 declaration remains unchanged; explicit u32
casts recover the unsigned division. No clamp, early zero return, cached actor
across helpers or stale state-pointer substitution is added. Zero bounds retain
the original compiler-generated break 7 path in the emitted guest instructions;
native C execution is restricted to nonzero bounds.

## Compiler, owner, Make and complete image

The isolated C is warning-free. Raw body SHA-256:
`9e0dc26802ab957becc320953a6acca8741e593e76b3f986e6728dec2ba520e4`.
All 19 raw relocation fields and body words match the original assembly
object. The indexed choice must be a byte; broader temporary types change
register allocation or add a word in the isolated screens.

All **327 other raw/padded owner functions** and owner pools are unchanged,
including both original callers. The 36 inherited owner warnings are unchanged.
The actual five-command Make recipe produces the qualified padded object byte
for byte. Makefile, shared headers, word guards, layout and conversion inventory
are unchanged. The original object basename is retained in the shadow link so
its synthesized FILE symbol for overflow code stays identical.

Independent whole-image prediction changes only this slot and its symbol extent
from 16 to 268 bytes: **214 changed bytes**, no exclusions or metadata reordering.
All **6,056 function addresses**, **6,055 other linked bodies**, and **189,088
protected Game data bytes / 720 owners** remain fixed.
Production ELF SHA-256:
`45f1a369228dc3084cb6c601826e914a631d2c64f875b1ea00089c3e4d9b3829`.
Native installation changes exactly source, padded owner object and ELF.
All other prior **17,520 sealed inputs** remain unchanged before the explicit
new tools/documentation refresh. **1,006 focused inputs** are frozen.

## Qualification and explicit limits

- **5,583 normal guest cases / 22,332 executions** across original, isolated C,
  padded owner and actual Make object. Three code/global address layouts retain
  the packed tables' eight-byte offset. All 66 nontrap words execute; registers,
  memory, ordered accesses, helper observations and saved state agree.
- All nonzero byte bounds, high-bit random values, every modulo-3 outcome,
  category remapping, table modes, signed zero/normal/subnormal float samples,
  helper retargeting and incoming-home changes are covered.
- **63 zero-divisor trap cases / 252 executions** verify the break-7 boundary
  and public access/effect prefix. Three explicit opaque HI/LO result patterns
  are used for DIVU by zero. This does not claim hardware DIVU-zero results,
  portable native C zero-division semantics or a hardware FCSR model.
- A guest-only halfword/current-pointer alias makes the selected-state store
  retarget the current pointer to a different aligned actor view. A separately
  compiled cached-state negative control fails this case. Its frozen object
  stays immutable; fresh controls compare function payload/bindings to it.
- ROM-wide aligned census finds exactly two JALs: ROM98C8C / PC1506B7DC and
  ROM98CC4 / PC1506B814, with no pointer literal. **128 caller cases / 2,048
  executions** qualify original argument/epilogue windows for both constant
  bounds and four injected return values. Parent writes, saved return address
  and stack restoration are checked. Full parent reachability is not claimed.
- **1,837 native cases each at O0/O2/O3**, with UBSan and six effective controls:
  signed random remainder, short instead of byte table reads, wrong category,
  wrong special value, wrong follow-up variant, and cached actor after helper.
  Guest-only aliases/home mutations and zero bounds are excluded from native C.
- Native fixtures use a typed union backing the overlapping table views and
  factor at +0x184. A larger backing also keeps the incorrect short-read control
  within mapped/defined storage. Numerical halfword/float normalization avoids
  host/guest endian differences in canary checks. No asset bytes are embedded
  in committed tools; private test inputs come from the frozen ELF.
- Both tools copies pass six fresh focused tests before and after installation,
  plus shared checks. Body/binding and literal-image corruptions are rejected.
  Neighbor suites are reused through exact body/pool identity, not claimed fresh.

Random and follow-up helpers are explicit adversarial providers. This work does
not newly execute the complete 64-bit random generator or downstream effect
implementations, and does not claim visual/gameplay acceptance.

## Artifacts and next boundary

`conker/build/game-random-animation-choice-1506B634-match/` holds frozen inputs,
source screens, original/selected/owner objects, Make commands, independent first
link, caller census, runtime qualification, immutable negative object, installed
recount, Graphify proof, seals and bank receipts. Public tools are
`game_random_animation_choice_match.py`, `game_random_animation_choice_oracle.py`
and `test_game_random_animation_choice_match.py`.

Graphify receives an eleven-file scoped AST refresh preserving prior nodes and
valid edge occurrences. The obsolete integer-return and word-parameter edges
are archived separately. No full-corpus extraction or reclustering is claimed.

Next ordinary C placeholder: **func_1506BCC8**, same owner, VA1506BCC8,
ROM99178, 72 words and 24-byte frame. Audit the full actor-state/float branches,
helper calls, inputs and return contract before reconstruction. Scalar smoothing
and other private candidates remain uncredited. No Claude calls, host/editor/
Release changes or network push.
