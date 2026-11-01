# Actor matrix-position transform restored directly from C

`func_151644F4` now emits all **52 retail words and both call bindings directly
from semantic C**, with the original 120-byte frame and zero new word guards.
Its empty C body is replaced by the complete rotation/translation and coordinate
publication operation. The obsolete commented draft is removed.

Fresh production and live Windows-checkout recounts confirm **4,015/5,506
(72.92%)** total, Game **3,342/4,833 (69.15%)**, Init 492/492 and Debugger
181/181, zero drift and 1,491 different. The active 75% threshold remains
4,130/5,506: **115 more matches**. Tools were committed first at `696b894`.

## Source and ABI

Owner `game_18D770`; VA **151644F4..151645C4**; ROM **1919A4..191A74**.
The routine builds an Euler-rotation matrix from angleX, zero and angleZ using
`func_150A8050`, fills its translation row from the input point, and passes
`(0, height, 0)` to `func_150A7960`. It truncates the three resulting coordinates
and writes the attached actor's halfwords at +0xE, +0x10 and +0x12. The actor
pointer is reloaded before each store, preserving the original alias behavior.

The first screen exposes an incorrect inherited type description: height was
declared as an integer, while the caller's old shared structure described its
bits as a pointer. A file-local `ActorMatrixPositionState` view recovers actor
at +0x14, float height at +0x18, angleScale at +0x1C, angleFactors pointer at
+0x20 and inline translation at +0x24. Its size is 0x30. Native layout assertions
and the executed original parent check those offsets and the float argument
bits. Shared headers are unchanged.

Parent `func_151644A8` receives the same local view and descriptive locals. Its
raw compiled body and bindings remain unchanged. All **77 other raw and padded
owner functions**, including that parent, and the owner's pools are preserved.
Three existing parent type warnings disappear; the other 45 owner warnings
remain the same by warning code/message/source statement. No new warning is
accepted. Individual selected-function compilation is warning-free.

The ROM contains one aligned direct JAL to the target, at ROM **191988** /
PC **151644D8**, in `func_151644A8`, and no aligned target-pointer literal.
The complete original 19-word parent is exercised with both target inputs and
its result of one. Height and angle arguments use the recovered o32 float ABI.

## Runtime qualification

Four code forms agree: original retail, raw selected C, padded owner and actual
Make object. **870 guest cases / 3,480 executions** cover three independent
root addresses, two stack phases, both matrix patterns, signed zero and other
finite heights, translated input aliases and live mutations. All 52 body words
are reached. Complete machine state and ordered memory traces agree between
the four forms; public bytes, canaries and saved registers match the independent
rounded binary32 reference.

The point helper executes its **40 original instructions**, including the
retail floating-add association. Rotation is an explicit opaque provider which
records its arguments, writes a controlled matrix and clobbers caller-saved
registers/homes. Provider mutations change translation and actor pointers to
prove that the root reloads the intended live values. This does not claim new
trigonometric-kernel, hardware FCSR, NaN, rendering or gameplay acceptance.

**80 original-parent cases / 320 executions** connect that caller to all four
target forms and the original point helper. A guest-only alias changes the
actor-pointer high half through the first coordinate store; subsequent stores
follow the reloaded pointer. These byte aliases are kept separate from native
C's ordinary object domain.

Native32 O0/O2/O3 each pass **48 cases under UBSan**, with six effective compiled
controls: missing height, wrong Y translation, wrong Z output, missing Y store,
wrong X output and capturing the actor pointer before helper mutations. All
six controls fail in each profile. Native inputs keep coordinate conversions
finite and representable.

Six focused tests pass fresh in each tools copy before installation and again
after production installation; both shared tools checks pass. The independently
dirty older tools mirror receives the three owned modules without a commit or
changes to its unrelated work.

## Build and production audit

The actual five-command Make recipe reproduces the independently padded object
byte for byte under normal O2/g3. There are no guards, insertions, omissions or
compiler-profile changes. An independent prediction changes only the target's
208-byte code slot and its existing symbol-size field, from 24 to 208 bytes.
The first link and production Make reproduce that complete predicted ELF with
**145 changed bytes, zero metadata exclusions and no symbol-order adjustment**.

All **6,056 function addresses and 6,055 other linked bodies** remain fixed.
All **189,088 protected Game-data bytes across 720 owners** remain exact.
The map, guard manifest, conversion inventory and every unrelated sealed
production input are unchanged. The live Windows checkout receives only the
qualified source, object and predicted ELF; its independent recount agrees.

Raw C SHA-256:
`c5ebd93469dedf571311583e8c89177f6eea82cfafdff20083d261e60a2f2a21`.
Production ELF SHA-256:
`9623b373b626ff6207c2b5daea4449bec9dfa74a6c7a74762d864a3a487c8e16`.
Reproduce the focused gates with:

```sh
python3 -m unittest tools.tests.test_game_actor_matrix_position_match -v
```

Evidence: `conker/build/game-actor-matrix-position-151644F4-match/`, including
the 1,001-input frozen snapshot, canonical artifact fingerprints, original
assembly, raw/padded owners, actual Make commands, literal first-linked ELF,
runtime/native receipts, caller census and installed audits. Initial fixture
failures are retained separately: the parent has a 32-byte frame, and public
actor fixtures must sit outside the private-stack filter. No failed run is
counted as qualification.

Root README changes only its two aggregate matching rows. The scoped graph
refresh retains all prior nodes and valid relationship occurrences, archiving
the obsolete parameter-type references instead of retaining them as current.
No Claude calls, host/editor/Release changes or push are made.

Next adjacent screen: `func_151645C4`, currently a 111-word placeholder in the
same owner. Keep the scalar smoother and the earlier reference-event pair
private and uncredited; their distinct compiler gaps remain unresolved. The
wider 75% goal remains active.
