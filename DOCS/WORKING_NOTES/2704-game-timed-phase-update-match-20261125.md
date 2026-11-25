# Timed phase callback match - 2026-11-25

`func_15108658` replaces its zero-return placeholder with a typed timed phase
callback in `conker/src/game/generated_135780.c`. Its complete slot is
**105 words / 420 bytes, 40-byte frame, no alignment tail**, VA
`0x15108658..0x151087FC`, ROM `0x135B08..0x135CAC`.
**59 words and bindings emit directly; 46 checked guard rows, including
10 relocation-bearing rows, normalize zero rematerialization, FP allocation,
comparison scheduling and the common exit layout. Raw C is not byte-exact.**
Arithmetic operators and their operands remain ordered. Comparisons can move
relative to independent arithmetic; the raw observer proof explicitly covers
that difference with FP traps disabled. There is no private frame mapping,
insertion, omission or IDO/Make profile change.

Production recount: **4,683 / 5,528 (84.71%)** total; **4,010 / 4,855
(82.60%)** Game; Init492/492 and Debugger181/181; zero address drift,
845 still different. **16 more verified matches reach85%.** One new match;
zero parent/provider credit. Conversion rows and denominators are unchanged.

The recovered interface returns signed32 status0/1, accepts a record pointer
in A0 and an unused scratch pointer in A1, and retains retail's incoming A1
home atSP+0x2C. The target saves RA only; it does not save S0. Its record+0xA8
phase pointer lives across the no-argument float RNG150ADA68 atSP+0x18.
The original unused parameter's C type is unobservable in this routine; the
pointer declaration follows the actual callback producer.

The measured188-byte typed prefix has flags at0x1C, signed display byte0x74,
and five floats at0xA8/0xAC/0xB0/0xB4/0xB8: remaining, total, transition width,
edge width and cooldown. Field names describe observed use. This does not
recover the full original object extent or C effective type. Native tests use
an actual typed prefix and separate16-byte scratch buffer with canaries.

The target computes total-minus-remaining, chooses flags0/0x10000/0x20000
from the two edge distances, and advances either cooldown or remaining time
by D800BE9A4. The cooldown path sets display byte-1/3 from D800A2460 and
11-minus-cooldown, clamps a negative updated cooldown to zero, and returns1.
The other path returns0 if remaining becomes negative. If still active with
flags0x20000, it calls150ADA68 and resets cooldown to11 when the returned
float is less than D800A2464. Actual repeated field reads, signed byte stores,
provider mutations and the post-RNG threshold read are retained.

An ordinary local phase pointer recovers the authentic frame without dummy
uses of A1 or storage tricks. The transition comparison needs its retail
remaining-field reload. A105-word/frame40 source with only36 differences
was rejected: it short-circuits the11-minus-cooldown subtraction. At cooldown
2^-30 and delta0, public memory and the integer return agree while retail
retains inexact sticky4 and that candidate retains0. The expanded2592-case
screen rejects144 cases. The selected source computes the edge distance
unconditionally and uses the genuine cooldown return1. Register hints,
declaration permutations, array views and additional volatile fields did not
recover the needed behavior. None of those experimental qualifiers is installed.

All160 bytes/40 entries of D80089760 agree across ASM, ROM, frozen and live
ELF. The target is entry24 at800897C0/ROM22E280. An aligned whole-ROM scan
finds that one literal pointer and no direct J/JAL target pattern; this is not
a universal indirect-call census. The complete428-word/frame88 original
parent151303EC agrees with ROM. Its linked C remains a placeholder.

Connected qualification covers the actual17-word callback window
15130A0C..15130A50 and JALR15130A38, its real two-word prologue, and a
**separately executed** four-word epilogue. **576 cases per stream,
144 children per stream, 23 actual parent instructions** verify signed
selector byte72/-1 and A3 skip gates, A0 record, A1 parentSP+0x48 scratch,
saved A0/A3, and the original zero-return consumer. Public memory, private
frame, saved registers, RNG observations and modeled FP status agree. Two
supported controls finish and fail comparison. The parent cleanup, other
dispatch cases and complete parent runtime are not qualified. Raw scratch
GPR/FPR equality is not claimed.

The abstract observer proof enumerates **1024 assignments of10 independent
FP predicates across13 paths**, with arbitrary initial float bits and provider
public-byte epochs. It compares ordered arithmetic operands, public RAM and
writes, complete private frame, saved ABI state, integer return, and FP state
at provider/return boundaries. FP operators, predicates and exception outputs
are opaque; sticky exception bits combine by OR and Cause/condition follow
their last defining operation. This permits the measured independent
comparison/subtract scheduling while preserving observers. It assumes
disabled FP traps and the stated operation/exception model; it is not an IEEE
emulator, SMT solver, enabled-trap or raw fault-prefix proof. Four complete
controls reject, including the lost subtraction in256/1024 assignments.

The finite scalar guest reference passes **2592 cases per stream across five
streams**: four literal-retail versions plus raw C. It checks public/private
memory, status return, RNG observations, four rounding modes, FP flags and
ordered arithmetic operands. **101 distinct retail instructions execute**;
offsets0x54/0x88/0x11C/0x14C are unreachable duplicate instructions, not
padding or omitted bytes. All105 words remain byte-compared. **140 access
fault quads** compare exact state across the four literal-retail streams.
Raw comparison interleaving, scratch registers and raw fault-prefix identity
are explicitly outside that comparison.

Native32 compiles the actual selected body and independent reference/provider
harness in two translation units: **2608 calls per profile atO0/O2/O3**,
188-byte prefixes,268-byte arenas, all retained bytes/scratch/canaries,
four rounding modes and seeded sticky flags. Full RNG arena/global/MXCSR
snapshots, provider mutations and quietNaN/infinity arguments agree. Strict
aliasing, UBSan traps, LTO type checks and strict FP flags remain enabled.
Seven wrong C variants complete and return comparison42; signals/traps
never count as effective controls. The unused scratch warning alone is suppressed.

The full native FENV gate uses **native-only -fno-tree-sink**. With the same
body and other strict flags, default GCC O2 sinks the used-on-one-edge
subtraction and loses native inexact: row64 gives MXCSR8080 versus8112.
-fnon-call-exceptions alone does not resolve it; disabling tree sinking does.
The explicit short-circuit control still fails42 under that setting. FP status
checks were not masked, and no IDO/Make profile was changed. This does not
claim default optimized GCC FENV parity, MIPS hardware FP validation or host
gameplay acceptance. The initial native layout probe's libc-header dependency
was corrected to the existing freestanding32 route without installing anything.

Both complete owner padders agree, preserving both neighboring functions and
all literal/data pools; this owner has zero exported retail jump labels.
Actual Make uses **three commands**: IDO, padder and assembler, with no
GLOBAL_ASM processing. The independent reference uses frozen old C plus the
original420-byte target ASM, without recovered C or new guards. Reference,
Make link, literal prediction and production ELF agree: **400 changed bytes,
zero exclusions**. All189088 protected Game data bytes/720 owners, unrelated
code/address/extents, the old guard prefix and conversion rows are fixed.
Named symbol/string metadata uses closed byte accounting.

Boundary tests reject92 guarded corruptions, expose118 unguarded corruptions,
pin9 raw relocation positions, reject12 guarded binding corruptions and both
oversized probes, and run20 GNU links/100 guest rebases at four entry/address
carry patterns including lows0x7FF8/0x8000/0xFFF8.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 86.942 s | 5 fresh / 0 reused |
| preinstall-sibling | 87.538 s | 5 fresh / 0 reused |
| installed-primary | 76.785 s | 5 fresh / 0 reused |
| installed-sibling | 102.249 s | 5 fresh / 0 reused |

The final20 tests are fresh. The first packaged primary run is preserved as
a failed integration attempt: five wrappers omitted result returns, and one
boundary wrapper shadowed its module alias with a subprocess result. Those
wrappers were corrected and both copies resealed before the final fresh pair;
the selected body, guard rows and profiles did not change. The first tools
packager also stalled in a WSL Git status read; only its owned read child was
terminated, its parent was observed terminal, and nativegit.exe replaced
that status route before any task files were written.

The isolated second tools copy has2145
immutable dependency links and10 independent task copies. Freeze:
3785 inputs/2703 copies. Task/import/data/
profile/artifact fingerprints agree across copies, including the second Make
route's own tools. Shared tools-check passes. The independently dirty real
tools sibling is preserved. One packet-only Claude review completed with
tools and MCP disabled and zero tool uses; its repeated source suggestions
were not adopted as proof, and its scheduling-only conclusion was narrowed
by the independently measured FP status counterexample. No subagents ran.

Baseline consumer `ac29aaaab566537018d9bc06f83634b1d3dc60c5`.
Tools commit `f7c77687edbe24e4ab5938a251fe4c0c80f69270`.
Production ELF SHA256 `4c5c283a22fc8ddd96a2ef69605104bd075f011de45cc9db51fcc032ee571079`.
Padded owner SHA256 `d79e8d71b11e89ca7451a63e91f3fbe223b0a4b9be623799206d8a56d3c61740`.
Receipts: `conker/build/game-timed-phase-update-15108658-private`.

Root README receives aggregate/date rows only. Scoped Graphify retention and
actual hook-writer termination are audited before banking. No host transfer,
build, launch, Release change, runtime/gameplay acceptance or push is claimed.
The85% matching goal remains active after this checkpoint.
