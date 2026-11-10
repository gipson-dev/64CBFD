# Game actor water/stun update guarded match - 2026-11-10

`func_150585F0` matches its complete **170-word / 680-byte** retail slot,
VA **150585F0..15058898**, ROM **85AA0..85D48**, with the natural **0x28
frame**. Its two-argument semantic C emits 171 words. **11 checked guard
rows** normalize two float-register operands, independent gravity-constant
scheduling and one unused incoming-argument home-store omission. No insertion,
frame change, compiler-profile change, shared declaration or Makefile change.

Production recount: **4,309 / 5,513 (78.16%)** total; Game **3,636 / 4,840
(75.12%)**; Init 492/492 and Debugger 181/181. Zero address drift, 1,204 still
different; **102** more matches reach 4,411/5,513 and the active 80% goal.
Conversion CSV/counts stay fixed. README changes only aggregate rows.

## Recovered source and calling interface

Owner `conker/src/game_83300.c`; object `conker/build/src/game_83300.c.o`.
Original assembly `asm/nonmatchings/game_83300/func_150585F0.s` is retained.
The interface is `void func_150585F0(struct127 *actor, f32 unused_argument)`.
All seven original call sites pass a second word containing a float. The
existing byte-exact C movement caller also declares and passes it as f32.
The retail body never reads that incoming argument. Keep the parameter and
mark it explicitly unused, preserving the reconstructed caller interface.

The first motion call is:

`func_1505A3A8(0.0f, actor, 1.0f, motion_scale, 0)`

where `motion_scale = (f32)(u32)actor->unk109 * D_80099478`. The predecessor
incorrectly supplied that scale as the **first** float as well. Retail sets
F12 to zero, passes the actor in A1, 1.0f bits in A2, the scale bits in A3,
and zero in the fifth stack slot. The unsigned conversion retains the original
correction sequence even though its byte input cannot take the negative edge.
The original motion helper uses F12, so preserving the zero is meaningful.

Precomputing the scale in a local recovers retail's opening schedule and most
float-register lifetimes. Rename the heading local to `recovery_heading` and
remove the unused temporary. Local gravity declarations/register hints did
not improve the final shape and remain private. No source padding or profile
override is introduced.

## Water and stun behavior

All subsequent actor/global reads observe motion-provider effects. If field
0x1CC is below D_8009947C, capture the actor's Y. Water values 1..9 clear gravity,
multiply Y velocity by D_80099480 only below 60.0f, and compare Y against the
float32-ordered expression `(field118 - 60.0f) + 40.0f`. Exiting that surface
clears bytes 0x81/0x83/water and field 0xB8, then restores gravity to 4. Exact boundaries,
NaNs and infinities retain the retail comparison behavior.

Clear field 0x21C when D_800BE616 is zero or actor state is not 1. Stun 0xFF skips
the remaining stun routine; 0xFE skips only the decrement. Other values decrement
unless health is zero in state 1. Subtract signed D_800CC264 from signed field 0x10C,
then narrow back to s16 before testing it. A low field 0x28 and flag 0xF4 bit 0x100 also
force the timer to zero. Signed overflow through the halfword store is preserved.

At expiration, clear the child's matrix-physics byte at child+0x7D when the
pointer is nonnull, clear the timer and call `func_1505E874` with the live resource
byte D_800C3E78 and actor pointer. Reload stun after that callback. Recovery
clears XZ velocity and byte 0x81, restores headings 0x78/0x76 from saved 0x7A, handles
water/state-specific Y velocity or gravity/flag 0x8000 changes, and copies the
live byte 0x238 to 0x23A after the optional `func_1506B078` callback. A still-stunned actor
without flag 0x10B bit 2 submits command 12 through `func_150599C8`, optionally flipping
heading bit 0x8000 when flag 0x10B bit 4 is set, after writing byte 0x80 = 10.

All physical field offsets use the canonical SDK32 structure. Tests include
child-byte aliases into stun, water and the resource global. These guest-only
extensions qualify instruction ordering; native tests use typed separate child
objects and exclude those physical aliases. Helper algorithms and hardware/
visual gameplay are separate from this target's contract. In particular,
`func_1505A3A8` still has a zero-return C placeholder; its algorithm remains uncredited.

## Closed normalization and argument-home profile

Raw SHA256:
`89674eebf3caeef22a8bbe064f7a6c8d9a57f0833fb2df59d99e89c9ae774456`.
Pin all 684 source bytes, 18 binding sites and owner/function. Preserve every
instruction except source word 5, **AFA5002C**, the compiler's unused-A1 store
at SP+0x2C. With the 0x28 frame this is the second argument's incoming ABI home
at entrySP+4. No source-level address of that unused parameter escapes.

Raw guest execution must write the exact supplied argument word there and
preserve every other caller byte. Normalized/retail execution must preserve
the complete caller home region. This is an explicit private-ABI profile,
not a claim that raw and retail stack bytes are identical. The omission guard
checks the original word before removal, and stale-row controls exercise it.

The two operand edits redirect the computed scale from F0 to F14 and read that
same result into A3. F0/F14 are volatile at this call boundary; the original
motion helper overwrites F0 from its global timestep and F14 from A3 before
using them. The later source origins 144/138/139/145/140/141/142/143 reproduce
retail's eight-word gravity-constant schedule, with its branch displacement
recomputed. Public flag/gravity stores retain their order. No private-home
remapping, inserted word or saved-register-lifetime change.

Both independent target padders, full owner padding and original assembled
retail routine agree on all 170 words and relocation identities. Strict literal
whole-ELF prediction changes **265 bytes, all within the target's 680-byte slot**.
No metadata, symbol size, function address, other body or data change; no
excluded ranges. All 6,050 function addresses stay fixed.

## Focused checks and actual production

The owner contains 89 functions: 71 C definitions and 18 retained ASM functions.
All **88 non-target neighbors**, empty pools and register usage stay identical
in raw and padded comparisons. The **8 inherited diagnostics** stay at 8. Actual
five-command asm-processor/IDO O2-g3/postprocess/generic-padder/assembler output
equals the independent object and ELF. All **189,088 protected bytes / 720 owners**
remain exact, SHA256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Conversion CSV and prior guard history stay fixed. Existing duplicate `generated_12D630` Make
warnings and expected `make all` checksum exit 2 remain.

- Guest: **428 cases per body / 1,284 executions**, plus 12 rebases. Coverage is
  167/171 raw and 166/170 normalized/retail words. Three unsigned-conversion
  correction words and one dead duplicate load are unreachable. All 256 scale
  bytes, water/velocity/surface edges, signed timer/delta wrapping, health/state
  gates, FE/FF, heading masks, live resource/carry reloads and eight unused-float
  patterns pass. Public bytes, helper snapshots, saved ABI and home profiles agree.
- Native SDK32: **425 cases at O0/O2/O3**, UBSan and **19 effective controls**
  per profile. Retained actor/child/global bytes use explicit endian/pointer
  normalization. Mixed float/integer/fifth-stack arguments and the unused
  second float have their real prototypes. A fixture initially omitted field 0xF8
  initialization; a byte dump located and corrected it before qualification.
- Compiler controls: **21 effective IDO controls**, including stale resource
  and carried-byte captures. All 171 word and 18 binding corruptions are rejected;
  all 11 stale guards, including the omission, are rejected. Seven full-image
  corruptions and four independent GNU links / 12 executions pass. Only public,
  ABI, snapshot or call-count differences count as semantic witnesses; compiler,
  interpreter, private-home and fixture failures do not.
- Caller census: seven ROM JAL sites, no J or aligned pointer entries, across
  six parents. Original **48-word caller windows** pass **324 executions / 294
  target invocations / 30 branch rejections**, including branch-likely delay
  behavior, caller field setup, stack+0x48 argument save/reload and post-call
  heading loads. The second float words include 0.05f/0.1f/0.25f. Five parents
  remain 12-byte C placeholders; their original windows are qualified, not full
  parent reconstructions. The complete **3,836-byte C parent `func_150F34F4`** and its
  current call window are unchanged and byte-exact. Whole parent algorithms
  and hardware acceptance are not claimed.

Six fresh tests pass before and after installation in each tools environment.
Shared smokes are fresh; three unchanged regressions per copy are explicit
fingerprinted reuses. All 748 frozen inputs include caller sources, objects and assembly.
Sibling validation uses a read-only overlay and preserves its native Git
inventory of 2,434 dirty paths. Tools commit precedes consumer source/guards/
docs/pin. No push or host-port change.

Graphify receives a scoped AST refresh for the owner and six modules. All 71
active C definitions, 18 retained ASM functions and nodes outside changed files
are audited. New-module node coverage is recorded as observed; no full-corpus
extraction is claimed. Evidence lives in
`conker/build/game-water-stun-150585F0-match/`.

Next: recover the **137-word motion helper `func_1505A3A8`** in the same owner from
its zero-return placeholder. Recheck its complete assembly, fields, globals
and all callers before qualification. Keep the 80% goal active; unresolved
texture-command candidates remain private/uncredited.
