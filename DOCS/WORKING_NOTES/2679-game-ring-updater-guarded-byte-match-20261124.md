# Ring updater guarded byte match - 2026-11-24

`func_150C8A68` is recovered as semantic C in `conker/src/game/generated_F5800.c`.
Its complete 212-word / 848-byte slot matches retail after 32 expected-word
and relocation guards. The compiler emits the retail 152-byte frame, saved
register lifetimes, expired byte at SP+0x93, previous radius at SP+0x8C and point
at SP+0x74. There are 183 raw matching instruction words; 29 instruction words
and three further relocation-only rows require normalization. This is a
guarded match, not an unmodified compiler byte match.

Production recount: **4,659 / 5,528 (84.28%)** total, Game **3,986 / 4,855
(82.10%)**, Init **492 / 492** and Debugger **181 / 181**, zero drift and 869 different.
**40 more functions are required for 85%**. Only this target earns one match.

Retail VA 150C8A68..150C8DB8, ROM F5F18..F6268. The function takes one record
pointer and returns void; the original dispatcher ignores its incidental V0.
The recovered body retains byte flags, signed byte callback selectors, signed
short lifetime/fade fields and the narrowed signed-short fade-in difference.
The RNG and byte-angle trig declarations match the existing SDK declarations.
The release helper uses its existing `struct102 *` declaration and an explicit
record-view cast. That declaration correction changes no raw words or bindings.

The routine optionally ages the record, updates its radius and fade amplitude,
accumulates a perimeter emission budget, and emits while that budget is strictly
greater than one. Each iteration snapshots the selected player's heading before
the RNG, combines it with an unsigned remainder modulo 81, wraps the angle to a
byte, performs two trig lookups and constructs a three-float point. The retained
XZ distance limit gates the emission callback. The update callback receives the
previous radius; the finish callback can request retirement. Callback-mutated
record fields and globals remain live at their original read boundaries.

The 32 guards normalize opening branch/address scheduling and bind three audited
float literals to their original data words. They are not claimed to be only
an instruction permutation. No instructions are inserted or omitted. The full
112-word suffix from word 100 through word 211, including the emission callback
loop and epilogue, emits directly with its original words and bindings. All old
guard bytes remain an exact prefix, followed only by the 32 new target rows.

The compact literal section is exactly 16 bytes: words 40C90FDB, 4B263BD7, 3F360B61
and zero padding. A new `check_ring_updater_150c8a68_pool.py` runs before padding
in the actual four-command Make recipe. It rejects wrong values/order/size,
writable or malformed pool sections, changed target code/relocations and another
function borrowing this pool. Thus relocation guards cannot silently preserve
retail output after a changed C constant. All 16 pool-byte corruptions, a writable
section and a wrong-endian object are rejected. The padded pool/data stay fixed.

All 18 raw and padded owner neighbors remain unchanged. Both padders agree with
independently assembled original assembly. The independent full-image reference
uses frozen old C plus original target assembly, accounting for 743 changed bytes
and four symbol-record permutations, with zero exclusions. Actual shadow Make
and production Make reproduce the complete predicted ELF. The 189,088-byte
protected Game data section and all 720 data owners remain exact; conversion
rows and every other frozen input are audited.

Guest qualification covers 472 cases per stream across four instruction streams,
all four rounding modes, mutable providers, signed timer extremes, fade paths,
culling and retirement. It executes 211 of 212 words; the retained divide-safety
BREAK at word 119 is unreachable because its divisor is 81. There are 261 complete
access-fault quads with equal state. Boundary controls reject 64 corrupted guard
words, expose 360 unguarded corruptions, pin 26 relocation bindings, reject both
oversized slots, and run 16 GNU links / 32 guest rebases across address regions,
HI16 carry and LO16 sign boundaries.

A complete aligned pristine-ROM census finds no direct JALs and exactly one
entry pointer at ROM 23095C / VA 8008BE9C. It is word 0 of descriptor 49 with a 52-byte
stride from D_8008B4A8. The original `func_151670C0` update-dispatch window executes
128 cases across four streams and two nesting levels. It prefetches/stores the
next link before entering the target and ignores V0 on return. Wrong A0 is an
effective fail-closed control. This is bounded dispatch-window qualification,
not complete parent execution or a proof about arbitrary runtime pointer writes.
RNG, trig, callback and release internals remain contracted and gain no credit.

SDK32 native C passes 562 legal backed, nonoverlapping cases at each of O0/O2/O3
with strict aliasing and UBSan. Ordered calls, point arguments and canonical
dual32 record/global memory digests agree with the independent reference.
All 256 emission angles and all four rounding modes are covered. Eleven effective
source controls exit 42 from comparison; no signal or UBSan trap is counted.
Signed 32-bit subtraction-overflow cases are guest-only; native tests keep defined
arithmetic. These finite tests do not claim all-input equivalence or gameplay.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 92.751s | 5 fresh / 0 reused |
| preinstall-sibling | 90.52s | 5 fresh / 0 reused |
| installed-primary | 84.132s | 5 fresh / 0 reused |
| installed-sibling | 94.832s | 5 fresh / 0 reused |

The earlier pre-pool suites are archived separately and are not the final
qualification receipts. Final suites use the typed release declaration and
four-command Make route with the pool checker. Shared `make tools-check` passes.
The second-copy run uses an isolated, dependency-verified overlay; the separately
dirty tools checkout remains untouched. Prior neighbor semantic receipts are
reused only with unchanged body/ABI/relocation/guard inputs, not called fresh.

Consumer baseline: `f4d0aea13934df1c7e7b02ed41a5a18840d7716a`.
Tools qualification commit: `006e56888b4391c32431cd36bb440c8825af395f`.
Production ELF SHA256: `c3b18d9448aac258cc76d44ee51209038819968edc7647c71f663afa5b92831d`.
Padded owner SHA256: `366eb27d1090767888cdee56bdb9bb0e07438c86e6ec5bb3f77c976faa35de85`.
The initial freeze contains 3507 inputs and 2099 file copies, including the original
dispatcher. Private receipts: `conker/build/game-ring-updater-150c8a68-private`.

Graphify was queried first. Native update and a scoped AST merge retain prior
IDs and qualification; actual hook producers must terminate before the final
merge and committed baseline bank. No full-corpus extraction, host/Release
change or push is claimed. This routine uses zero Claude calls. Next: screen
the 138-word `func_150C99B4` ring emission callback. The 85% goal remains active.
