# Resource record query and vector forwarding match - 2026-11-25

`func_150EB484` replaces its zero-return placeholder in
`conker/src/game/generated_1188E0.c`. The complete original routine is
**100 words / 400 bytes**, VA `0x150EB484..0x150EB614`, ROM
`0x118934..0x118AC4`. There is no alignment tail or interior global entry.
**77 words and bindings emit directly; 23 expected-word guards normalize
private frame size, independent address scheduling and priority-loop layout.**
Raw C uses a 72-byte frame; retail uses 80. This is guarded semantic C,
with no insertion, omission, dummy source work or production profile change.

Fresh production recount: **4,684 / 5,528 (84.73%)** total and
**4,011 / 4,855 (82.62%)** Game. Init 492/492, Debugger 181/181,
zero address drift, 844 different. **15 more verified matches reach85%.**
The denominator and conversion rows remain fixed. Only this routine earns a
new match; the wrappers, unfinished children and original parent earn none.

The actual three-pointer interface is `(f32 *start, f32 *end, f32 *output)`
with signed32 status0/1. Full original346-word `func_150A3504` reads both
input vectors and writes three floats through A3 on success. This establishes
the third parameter as an output vector rather than an integer flag.
The geometry body itself remains unreconstructed.

The query looks up context9 using the actual `u8 *func_15083E90(u8)` ABI.
With a context, it checks four priority record indices1/2/4/3. A hit calls
`func_150A2864(index,1)`, stores the one-based priority position at context+0x2E8,
reloads the resource base and calls `func_150EBC80(record,255,1)`, returning1.
After four misses it checks eight secondary indices45..52 and returns1 on
any hit. With no context, it tests record76 and may set its field18 to1,
but **always returns0**, including a successful test. Callback-visible
global reloads, saved index lifetime and all output-vector forwarding remain.

The 52-byte record type repeats the complete compatible CDE80 member layout;
its field18 is at24. The context store uses an aligned signed32 field at744.
Native qualification uses actual typed records/context and float arrays, with
legal start/end/output aliases. Full original object effective types and
unrestricted malformed pointers are not recovered by these tests.

All52 bytes of both index tables plus their following float agree across
ASM, ROM, frozen ELF and production ELF. D_80088AD0 is a **float scalar** at
D_80088AB0+32; the C cursor compares with its converted address without
dereferencing it. The table adjacency and eight-word extent are pinned.
The aligned ROM JAL census finds only the sum wrapper and15081E78 calling
this query; no aligned literal pointers to the five affected ABI entries
are found. This is not a universal indirect-call proof.

`func_150EB430` now explicitly accepts and forwards the output pointer while
computing its three-float sum. Its complete21 words/frame40 emit directly,
retiring its four old register guards. `func_150A34B0` explicitly forwards
record/start/end/output to the geometry child and still emits its complete
21 words/frame24 directly. Both wrappers were already counted, so add zero.
The typed `func_150A3504` and `func_150EBC80` placeholders gain four and three
argument-home stores respectively:7 and6 words. They remain zero-return
stubs, unmatching and uncredited. Their changed code and symbol sizes are
explicitly included in the full-image prediction and both-owner audit.

The changed-region proof compares opaque provider effects, callback arguments
and selected-field writes for all8 hit/miss x priority-index cases. It proves
the induction0..4, two commuting address-materialization pairs, and a bijection
between the routine's saved-slot offsets24..68; canonical outgoing homes0..15
map relative to SP as well. Raw frame72 and retail frame80
keep the same active offsets relative to their own SP; the retail extra8-byte
tail is unused. No pointer into this private frame is passed to a provider.
This proof excludes stack introspection, asynchronous observers, hardware and
raw fault identity. It is not a claim of identical scratch registers/stack.

The bounded guest oracle passes **1120 cases per stream across five streams**,
covering all100 original words, four priority/eight secondary/miss/null paths,
nonzero signed return classes, changing global bases, context/output mutations,
all three vector aliases and vectors in the caller's stack. Raw C agrees on
public memory, return, provider arguments/observations and saved ABI state.
Four literal-retail streams additionally agree on complete machine state and
**225 access-fault-prefix quads**. Raw private-frame/fault identity is excluded.

Full forwarding tests cover2048 gate cases per stream, including every flag
byte and disabled bytes0/1/2/255, and ten complete sum-wrapper cases. The
original466-word/frame944 parent15081E78 is pinned to ROM.160 cases per stream
execute its real six-word prologue, window15081F60..15081FFC and separate
five-word epilogue. The actual arguments are parent SP+0x374/+0x368/+0x380; the
parent overwrites V0 with-1 after the call. Parent memory outside the child's
explicit80-byte frame, vector results, provider observations and saved state
agree. Other parent paths and complete parent runtime remain unqualified.

Native32 uses the actual query and actual forwarding gate in three translation
units, with4480 cases per O0/O2/O3 profile. The independent scalar reference
compares the full9136-byte typed arena, base pointer and complete provider
events including arena digests. Strict aliasing, UBSan traps and LTO type
errors remain enabled. All **eight** controls finish and fail comparison42:
fallback result, selection index, status argument, effect byte, wrong output,
short priority/secondary scans, and cached base across providers. Signals and
traps are not accepted controls. Geometry/effect bodies remain contracted.

Both complete owner padders agree. They retain all28 untouched raw functions
and both sets of pools; after padding both existing wrappers also remain fixed.
Actual Make replays three commands for1188E0 and **five** for CDE80, including
its two existing GLOBAL_ASM bodies, with zero command diagnostics. No recipe or
profile changes are installed. The first Make adapter wrongly assumed the
three-command route; explicit stdout redirection and the actual five-command
route corrected that fixture. A native arena-copy probe was also changed to
the existing freestanding byte-copy route without installing libc headers.

Independent frozen-before-C plus original target ASM and literal typed-stub
homes reconstructs the full linked ELF: **349 changed bytes, zero exclusions**.
Every other function body/address/extent and all189088 protected Game data
bytes across720 owners stay fixed. Named symbol/string metadata is accounted
for without borrowing candidate bytes. The four retired guards and23 added
guards leave every unrelated row fixed. Guard tests reject46 guarded word
corruptions, expose154 unguarded corruptions, pin16 relocation positions,
reject12 guarded binding corruptions and both overflows.20 GNU links and
100 rebased guest runs cover four entry/address carry patterns.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 131.528 s | 6 fresh / 0 reused |
| preinstall-sibling | 138.003 s | 6 fresh / 0 reused |
| installed-primary | 121.015 s | 6 fresh / 0 reused |
| installed-sibling | 131.881 s | 6 fresh / 0 reused |

All24 final tests are fresh. Two packaged primary failures are retained:
missing result returns and packet-module name collisions, then a missing
subprocess import in the image wrapper, were corrected before both task copies
were resealed. Candidate source, guards and
production profile did not change. The isolated tools snapshot has
2155 immutable dependency links and10 independent
task files; freeze 3800 inputs/2719 copies.
Task/import/data/binding/artifact hashes agree, shared tools-check passes and
the independently dirty real tools sibling is preserved. No Claude call or
subagent was used for this routine.

Baseline consumer `6b48dddc2806ff006ba12afb8f1e011639bbb257`.
Tools commit `605b884f2121884faf1d93bf6a4f86c940c346ba`.
Production ELF SHA256 `717c83d3c64a2b1d0f259b39fbd5805c0bd4e416d74fee8e9f439e9ef4bfd017`.
Receipts: `conker/build/game-resource-record-query-150eb484-private`.

Read-only sibling applicability is recorded in `host-applicability.json`.
The historical64CBFDOGL path currently has no root Git/build files or monolithic
recomp_out.c; its checked cd64_out reference is an empty generated stub. An
active host implementation is not qualified from that reference. No source
transfer, host build/launch or Release change was performed.

The root README receives aggregate/date rows only. Scoped Graphify old-ID and
qualification retention, actual hook-writer termination, coherent consumer
commit and frozen bank follow these accepted checks. No host transfer/build/
launch, Release change, gameplay acceptance or push is claimed. The85% goal
remains active.
