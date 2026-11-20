# Note 2588: Map-trail update direct byte match

Date: 2026-11-20. Consumer baseline `e2501e721e09c4c029dcb574dbafca905007e64a`;
tools baseline `a446347798ad2f0a8a5a2803b22afa010fccba9b`.
Qualified tools commit: `a9380e4a4e9c800ab6c310bd73f909d2c894cdad`.

`func_1510608C` is restored from GLOBAL_ASM to complete semantic C. Its
**85 words / 340 bytes emit directly**, including the **48-byte frame**, saved
registers, branch delays, calls and callback byte at **SP+0x2B**. Raw object
words **and relocation bindings** equal the original assembly. No new guard,
inserted instruction, omitted instruction or compiler profile is needed.

Fresh production recount: **4,574 / 5,525 (82.79%)** total, **3,901 / 4,852 (80.40%)** Game, zero drift and 951 different. Converted C: **5,525 / 6,048 (91.35%)**, 86.49% of bytes; Game **4,852 / 5,327 (91.08%)**, 85.89% of bytes. Init 492/492 and Debugger 181/181 remain exact. **123 more matches** are needed for 85% at the current denominator, which ASM conversions can increase.

## Recovered interface and behavior

Owner: `conker/src/game/generated_133190.c`; VA 0x1510608C..0x151061E0,
ROM 0x13353C..0x133690. Original assembly remains unchanged. The registered
signature is `void(struct102 *)`; trail-specific fields use the existing
`MapTrailRecord133190` view, and endpoint objects expose their position at +0x40.
Keeping that interface avoids an incompatible callback declaration.

The only aligned literal target pointer in the ROM is at 0x230C68, in the
kind-64 descriptor at 0x8008C1A8: base 0x8008B4A8 + 64*52. No direct JAL literal
targets this function. The original `func_151670C0` window at 0x15167168 passes
the node in A0, preserves node+8 across JALR and ignores incidental V0. This is
an inspected eight-word call/continuation window, not full-parent execution
or proof that arbitrary computed callers cannot exist.

Signed packet.flag selects D_80088C10 unless it is -1. Its two entries are
`func_15107924` and `func_15107E48`, each `s32(u8 *, u8 *)`. A nonnull callback
receives the record and changed-byte address. A zero return calls the removal
service and **continues**. Enabled bit 0 controls the signed halfword duration
decrement. A negative stored result calls removal again and continues; zero
survives. The changed byte is read afterward, including any later edits through
its retained address, to decide whether to rebuild the curve.

The independent signed sample timer always subtracts a fresh tick value, narrows
to a halfword and tests negativity. On expiry it rebuilds samples, calls the
integer random provider, then reads both signed bounds. Unsigned remainder plus
the minimum is stored as a halfword. Both decrements explicitly use modulo
32-bit subtraction. Valid execution requires a nonzero random divisor.

Each nonnull child receives point 0 or point 3 through its position field.
The compiler emits interleaved integer loads/stores, retaining arbitrary vector
bit patterns without floating arithmetic.

## C sequencing and owner audit

An initial single-expression random update matched IDO but failed an independent
native provider-mutation case: GCC could read the maximum before the random
call. The selected body assigns the random result in a separate statement,
sequencing that call before both bound reads. Its natural declaration layout
still recovers all 85 words, the original frame and the exact passed home.
No production candidate with the unsequenced expression was installed.

The real removal prototype is `void func_1516972C(struct102 *)`. Three older
implicit calls in this owner now cast their existing arguments to that type.
All **36 other raw functions**, relocation bindings and constant pools remain
unchanged. Both independent padders reproduce the entire preceding owner
object byte-for-byte. The actual five-command Make route retains O2/g3 and
its existing diagnostics. Broad headers and the existing guard CSV are fixed.

## Fresh validation and limits

Five tests pass before and after installation in each tools configuration.
All **334 imported Python fingerprints** match between configurations; the
second uses an isolated overlay of 341 unchanged sibling files, 675 primary
fallbacks, four task files and an empty bootstrap. The real dirty sibling
checkout retains its HEAD, complete status and 345 dependency hashes.

The independent MIPS contract passes **1,536 cases**, covers all **84 reachable
words** and observes 26 call traces. The excluded instruction is the original
zero-divisor BREAK. Cases include signed timer wraparound, zero boundaries,
callback sentinel/null/return paths, child presence, arbitrary vector bits,
both stack phases and mutations of ticks, bounds, endpoints and the retained
changed byte. Six instruction mutations are effectively rejected.

Native SDK32 passes **768 cases each at O0, O2 and O3**, with strict aliasing
and UBSan. Complete record and both child objects, callback traces and ticks
are checked against independently generated expectations. Five compiled source
mutations execute and fail: zero expiry, changed inversion, enabled mask,
callback result and wrong endpoint. Provider bodies are bounded models; these
checks do not claim full callback/parent execution, fault semantics, hardware
or gameplay acceptance. Existing unchanged neighbor receipts are reused by
their source/object/binding identity, not reported as fresh neighbor suites.

Production Make, fresh ELF recount and `make tools-check` pass. All **6,051**
named function slots and **189,088 protected data bytes** remain fixed. The
**entire ELF** equals the frozen independent prediction with zero exclusions:
`d428a774da73a7a019242548481f707cc7e7c6d670c233af41189771495dfb04`.
The progress CSV changes exactly this function from ASM to C.

Graphify's native update remains fail-closed on the smaller extraction. A scoped
AST merge plus explicit note/original-ASM references retains old IDs. The commit
hook is observed to completion and old references are retained before sealing
the checkpoint. This is not a full-corpus semantic re-extraction claim.

Codex owns all changes; zero Claude calls. Local commits only; no push or host,
save or Release work. Continue with `func_15106214`, the 168-word trail curve
builder in the same owner (original frame 128), then its sample updater
`func_15106610`. Keep the 85% total goal active.
