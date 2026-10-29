# Resource byte-list loader direct C match

Verified 2026-10-29. `func_15084488` replaces the zero-return placeholder in
`conker/src/game/generated_AEB40.c`. VA15084488..15084558,
ROMB1938..B1A08: 52 words/208 bytes, 40-byte frame, seven bindings.
Every word emits directly from semantic C: zero guards, alignment words,
instruction insertion/omission or compiler-profile changes.

## Recovered contract

`void func_15084488(u8 *record, s32 unused, s32 context)` reads record[4].
Identity255 exits without table access or helper calls. Otherwise it calls
`func_1503D774(identity,context)` and then reloads the resource pointer from
`D_800D1C90[identity]` using the captured original identity. The ignored second
argument retains its original incoming-home store.

The resource's byte4 selects the list/count. Zero becomes one and uses
record+4; nonzero uses the address in `D_80086CAC[resource[5]]`. Resource
byte38 is added to the count. Each iteration calls `func_1503D774`, reloads
the current byte, calls `func_1503D660`, then advances the cursor. A helper's
mutation can change the second call's identity. The count and selected cursor
stay captured across loop calls; table/descriptor changes do not redirect
the remaining iteration sequence. Helper statuses are ignored, as in retail.
The API expects the first helper to leave a usable resource pointer; no new
allocation-failure/null-pointer recovery behavior is added.

Separate list and loop-cursor variables recover the register lifetimes.
Initializing the index before moving the list into the cursor recovers the
last two independent setup words. A single-pointer first draft used53 words.
The chosen for-loop form emits the entire original body directly. Raw/original
SHA256: `719af73b8d23b868cd65ac4d4f3dee0191a213877fd0430ce3ddc72b046ceccb`.

The local declarations of both helpers now return s32, matching their existing
definitions in `generated_6A3D0.c`. Their results remain ignored. All30 compact
owner neighbors, pools and retained assembly bodies are unchanged. Actual
Make uses five commands and the existing `jtbl_8009CC40_game` rodata anchor;
the normal O2/g3 profile is unchanged. No compiler warnings are emitted.

## Caller evidence and qualification

The aligned full-ROM scan found one JAL, ROMB00B4, and no aligned full-address
registration words. This does not exclude computed/encoded indirect calls.
The original parent is `func_15082A44`, still a zero-return C placeholder.
Only its eight-word window VA15082BEC..15082C0C, ROMB009C..B00BC, is connected
to the target in32 cases. Its S0=actor precondition is explicit. A separate
six-word original prologue runs in four cases, proving the0x68-byte frame
and incoming argument-home stores. No complete parent C/runtime equivalence
or additional parent matching credit is claimed.

Eight fresh canonical methods and project tools checks pass independently
in both tools copies. The focused tests cover:

- 260 guest cases, including sentinel skip, both list routes, unsigned byte
  identities, raw context/unused words, two stack phases, root table changes,
  byte mutations between helper calls and captured descriptor/cursor state.
- Counts through510 entries, giving1,021 provider calls in the largest case.
- Native32 O0/O2/O3 with UBSan:672 cases per profile and six rejected mutants
  (wrong gate, omitted extra count, wrong default count, signed byte, lost
  context and a cached byte that misses the second load).
- 52 access-fault prefix pairs and two sparse-memory skip cases, including
  branch-likely annulment of an otherwise unmapped descriptor-byte read.
- Three independent GNU layouts/24 cases,215 raw-byte/binding mutation
  controls,212 whole-image mutation controls, fresh full-owner compilation
  and independent padding with the retained rodata symbol.

The tests visit50 of52 original words. The duplicate load at150844EC is
unreachable after an unconditional branch. The load at15084514 is in the
annulled delay slot of a count<=0 branch: the normalized unsigned-byte count
plus unsigned extra byte is always1..510. Both words remain byte-exact in
the restored slot. These are emitted-code/fault-prefix checks, not portable
C fault semantics or hardware/gameplay acceptance. Providers are bounded
hooks; their complete implementations receive no new matching credit.

The first private suite exposed a descriptor fixture overlapping the guest
stack and an out-of-range negative-control gate. The fixture now rejects
stack overlap explicitly, and the gate mutant safely rejects a valid
boundary identity. The corrected private v7 and both canonical copies pass;
the initial v5 failure is historical test evidence, not a production failure.

## Production and progress

Tools were committed first at `884c9ee1e97c84b3a85d1c8456cc952393f2ad8b`.
Production reproduces the private independent prediction exactly:165 code
bytes and one target symbol-size byte change, with zero other metadata bytes
or exclusions. All6,056 disassembled function addresses and6,055 other bodies
remain fixed. All189,088 protected Game bytes across720 owners stay exact;
guard CSV, linker map and C inventory CSV stay unchanged. Each tools copy
then passes two fresh installed checks, with six semantic checks reused only
through complete input/module/artifact fingerprints.

ELF SHA256: `22e028b94afa7a644fb598b180cc2ff698f0608def55ad2eadd9c883363fd510`.
Target object: `a9486bf70532f8f901a6956cb17f668a8b212c79c3b0e45b091d5a272040aa90`.
Source: `73004779dc6f9cead340c7082976b4f8bf14c45f7d352c8ba149506fa8a2e0e1`.

Actual ELF recount: **3,904/5,506 (70.91%)**, Game3,231/4,833 (66.85%),
Init492/492 and Debugger181/181, zero drift. **226 more** are needed for the
4,130-function75% threshold. The independent older tools mirror preserves
its1,919 inherited dirty paths and adds only the three qualified modules,
without a mirror commit. Detailed narratives stay in notes; the root README
changes only its two aggregate matching rows.

The local ignored stage is `conker/build/game-resource-byte-list-match/`.
The allocator `func_15187EC0` remains private and uncredited in Note1825.
Next screen: `func_150C308C`. Keep the wider75% goal active.
