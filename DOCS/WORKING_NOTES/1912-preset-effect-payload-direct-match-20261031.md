# Working Note 1912: Preset effect payload direct C match

Date: 2026-10-31. `func_150E1060`, generated owner `generated_10E240`.
ROM `0x10E510..0x10E5FC`; VA `0x150E1060..0x150E114C`.
Tools: `3f5d2e8c05182ddbe19fcbf24633a1c1fe154cf3`.

## Behavior and recovered ABI

The zero-return placeholder is replaced by
`void *func_150E1060(u8 index, u8 variant, s32 flags)`. Both byte arguments
are required for the retail home slots and narrowing behavior. Adding a
separate index local produced an 80-byte frame; using the original byte
parameter directly reproduces the 72-byte frame and every instruction.

Indices other than zero or one return NULL before reading the table.
The retail lower-bound check is retained even though a byte index is never
negative. For a valid index, the routine looks up the unsigned table byte
at `D_800A0FE0[index]` through `func_151149AC`, returning NULL on failure.
It then calls `func_1510F800(0)` and reads signed halfwords at resource
offsets `0x10` and `0x14` for `func_1510FD20`. These fields are read after
the reset call; callback mutations are preserved.

The 16-byte local payload contains the index byte, three retained padding
bytes, the resource pointer, the opaque 32-bit helper result and positive
floating zero. The allocator receives `(300, -1, 31, -1, 0, 31, 16, variant,
flags)`. On success the function copies all sixteen bytes to the returned
record plus `0x28`, then returns that record pointer. Allocation failure
returns NULL without copying. No shared declarations change.

The three padding bytes retain their existing stack contents. They are
deliberately not initialized or zeroed. Guest tests check the entire copied
payload against independently seeded stack bytes. Portable C tests inspect
the initialized fields and output boundaries without promising a particular
initial padding value.

## Exact compiler and behavior evidence

Ordinary O2/g3 emits all **59 words and seven relocation bindings directly**,
with **zero guards, insertions or omissions**. No compiler profile or guard
manifest changes are needed. The body has 57 reachable words; offsets `0x20`
and `0x24` belong to the unreachable negative-index return path.

The frame is 72 bytes: RA at 44, payload at 52, record spill at 68, input
homes at 72/76/80 and the variant byte reloaded at 79. All two neighboring
function bodies and owner pools remain unchanged, with no C diagnostics.
Actual Make's compiler, padder and assembler produce the qualified object.

Guest tests pass **1,356 cases / 5,424 executions** across three independent
code/table rebases, covering every byte index, signed coordinate boundaries,
variant narrowing, flags, helper mutation, allocation/lookup failures and
output aliases. All architectural state and memory traces agree across
original, direct C, padded and actual Make objects. The suite covers all
57 reachable words and 77 access-prefix cuts, including 16 delay-slot cuts.

An additional **452 cases / 1,808 executions** use the original 11-word
memcpy. Its complete sixteen-byte copy includes the three retained bytes.
The other helper providers remain opaque.

Native32 O0/O2/O3 each pass **131,072 cases** with trapping UBSan. Nine wrong
semantic controls exit 1: range, table, signed coordinate, context, type,
variant, destination, zero and return errors. The native compiler suppresses
its type-limits warning for the deliberately retained redundant retail check.
No portable padding-initial-value or gameplay claim is made.

The complete frozen-input aligned census finds one JAL at ROM `0xCA974`
and no literal target pointers. **96 cases / 384 executions** run the six
original caller-window words: load the script byte, set variant `0xFF`, call
with flags 1 in the delay slot, then branch and reload the saved V0 in that
branch's delay slot. This proves the call interface and ignored pointer
result within the bounded window; it does not execute the full dispatcher.

Both tools copies pass eight fresh canonical methods and shared tool checks.
Post-installation each passes two fresh installed checks, reusing the other
six only after complete module/input/artifact fingerprint equality.

## Production and progress

Independent full-image prediction and actual production link agree on
**177 changed bytes: 176 target code bytes and one target extent byte**.
There are zero metadata changes and zero excluded ranges. All other 6,055
linked bodies and all 6,056 addresses remain unchanged. All 189,088 bytes
across 720 Game data owners remain exact. The entire existing guard manifest
and conversion CSV remain byte-identical. All 17,276 sealed inputs are checked.

Production ELF SHA-256:
`bb0d274014310d7968ee5100f2154b94a12554dba9dd34baaff5a54c6547ca5c`.
Map SHA-256:
`19139e6eb3cb32838dba4e8909f0275dc9bc2b9ce99a8efd030e800380070e85`.

Captured installed-ELF recount: Total **3,989/5,506 (72.45%)**;
Game **3,316/4,833 (68.61%)**; Init 492/492; Debugger 181/181; zero drift.
The 75% threshold remains 4,130, with **141** more exact functions needed.
Tools are committed first. The consumer commit includes source, tools pin
and seven documents; the root README changes only its two aggregate rows.
The scoped eleven-file AST refresh retains old nodes and valid relationships,
retiring the obsolete s32 placeholder return relationship. It does not claim
full-corpus extraction or fresh global clustering/centrality.

Next screen: `func_15108D24`, uncredited until the complete gates pass.
Evidence is under `conker/build/game-preset-effect-payload-150E1060-match/`.
Private candidates, old tools mirror work and sibling host/Release outputs
are preserved. No push is performed.
