# 1896 - Actor-height effect: direct C match

Date: 2026-10-31. Function `func_151A0A10` in
`conker/src/game/generated_1CC440.c`. VA `0x151A0A10..0x151A0AF8`,
ROM `0x1CDEC0..0x1CDFA8`: 58 words / 232 bytes with no alignment words.
The complete semantic body emits directly from C under the existing O2/g3
profile: all words and five relocation bindings match, with zero guards,
insertions, omissions, assembly injection or shared-header changes.

## Recovered behavior and interface

`void func_151A0A10(u8 *actor, s16 effect, u8 variant, s32 flags)` first
checks actor for NULL. For a non-NULL actor it captures X at+0x14 and Z at+0x1C.
The global byte `D_800C35EA == 1` then suppresses height capture, classification,
allocation and copying. Other gate values remain enabled. Gate1 still performs
the original X/Z reads; no actor reads occur for NULL.

The enabled path captures float height at actor+0x180 and zero into a 20-byte
local packet. `func_1510F8CC(actorWord184)` extracts the low five bits. Kind10
and default select0; kinds15/17 select1. Factory arguments are
`func_151491F4(effect,-1,1,1,0,20,variant,flags)`. On success,20 packet bytes
are copied to the returned record+0x28. Allocation failure skips the copy.
The routine copies float representations; it performs no floating arithmetic.

The 80-byte frame saves S0 at SP+40 and RA at SP+44. The packet is at SP+56. Incoming
effect, variant and flags homes are SP+84, SP+88, SP+92; the signed halfword reload is at SP+86
and byte reload at SP+91. No record-pointer spill is observed. Declaring the record
pointer before the packet recovers the original stack allocation; the rejected
initial order placed the packet 4 bytes too high. No compiler-profile change.

## Callers and retained providers

The two complete original 13-word void wrappers `func_1506FBE8` and
`func_1506FC1C` pass `D_800D154C`, IDs 0x46/0x28, variant0xFF and context 0.
Their current linked bodies are byte-exact and unchanged. The original 8-word
command window at VA 0x150291AC passes its captured actor, ID0x28, arbitrary
variant byte and context 1, then overwrites the callee result with1. Its original
five-word parent epilogue is also executed. The large parent is not claimed fully
executed. All three aligned ROM JALs are accounted for:0x5666C,0x9D0B4,0x9D0E8.
No aligned literal function pointer occurs.

Connected cases retain 139 original words: the 3-word classifier, 28-word factory,
49-word constructor slot, 28-word allocator, 20-word list registration and 11-word
memcpy. Live ELF bytes match those original provider bytes. The suites check
both empty and nonempty list insertion, complete initialized header fields,
header padding retention, zeroed state, complete packet bytes and allocation
failure. Connected allocation uses the observed caller rows 0/1. Arbitrary wide
context forwarding is checked separately with the bounded factory contract.
Heap allocation and bzero remain bounded; no gameplay/hardware claim is made.

## Fresh qualification

- Eight fresh focused methods plus project tools checks pass independently in
  both tools copies. After production, two installed methods rerun per copy;
  six unchanged semantic methods are reused only through exact fingerprints.
- Guest: 1,736 cases / 3,472 executions, all 58 root words visited, three independent
  GNU layouts and four identical original/raw/padded/actual-Make images. Float
  bit copies, low-five-bit classification, narrow arguments, saved registers,
  provider mutations and captured payload lifetime agree on full modeled state.
- 48 guest alias cases preserve the original forward-copy behavior. 139 fired
  root access-prefix pairs include 20 branch-delay cuts. NULL and gate1 cases
  explicitly unmap data that must not be read. One rejected synthetic layout is
  retained as an effective saved-RA overwrite control; both streams reject its
  corrupted zero return. Guest overlaps are not a portable C alias claim.
- Caller checks execute 32 complete-wrapper cases plus 2,048 original command
  windows. All four arguments and the command window's constant result are
  verified against varied callee returns and stack phases.
- 1,152 connected cases / 2,304 executions check the original provider chain,
  both actual context rows, empty/nonempty list heads, header fields, payload
  padding and byte-for-byte output fences. Per-helper visited-word counts are
  retained in receipts; retained slot size is not equated to execution coverage.
- Native SDK32 O0/O2/O3: 655,360 positive cases per profile with trapping UBSan,
  all 65,536 signed effect halfwords, all 256 variant bytes and gate values, NULL,
  captured float bits, provider changes, whole-actor/output fences and 14 effective
  semantic controls. Every selected/control source compiles successfully;
  compiler/interpreter failures do not count as effective controls.

Automatic packet padding at offsets 13..15 is compared only in seeded guest
memory. Native checks cover initialized fields and surrounding storage without
claiming portable padding values, guest-stack overlap semantics or FCSR behavior.

## Owner, image and banking

All 38 raw/padded owner neighbors and normalized pools are unchanged. Five actual
Make commands reproduce the qualified object. Selected, owner and Make builds
have zero diagnostics. Existing GLOBAL_ASM neighbors and prototypes are retained.

The independent complete ELF prediction has zero exclusions and exactly 177
changed bytes: 176 target-code bytes and one target-extent byte. No metadata
bytes change. All 6,055 other linked bodies, all addresses and 189,088 protected
Game data bytes across 720 owners are unchanged. Guard manifest and conversion
inventory CSV are byte-identical.

Tools commit `e369fd69daed1eec208e5af6a9e7f4b6c96e9f75` precedes the consumer commit. Production ELF SHA-256:
`c6bea0febe42193097b6be9bf54579bc5280f4b9bd18bba01869174c695c514b`.
Actual adopted-ELF recount: **3,973 / 5,506 (72.16%)**, Game
**3,300 / 4,833 (68.28%)**, Init 492/492 and Debugger 181/181. Zero drift;
1,533 C functions still differ. **157 more** are required for 4,130 exact (75%).
Next screen: `func_151A0E40`.

Artifacts and immutable before-inputs remain under ignored
`conker/build/game-actor-height-effect-151A0A10-match/`. The root README changes
only two aggregate rows. Scoped graph refresh retains prior nodes and valid
relationships and retires the stale placeholder return-type edge. No full-corpus
extraction, global clustering, hardware, gameplay acceptance or push is claimed.
