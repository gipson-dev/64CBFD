# Record Occupancy Query And Full-Word ABI Match - 2026-11-08

`func_150A29C8` replaces its zero-return placeholder with the complete
actor/record occupancy query. The recovered unsigned parameters emit the
original **73 instruction words and 32-byte frame** at retail addresses.
Two relocation guards preserve the original low-word alias and its signed
LO16 carry. No scheduling/register guards or compiler-profile changes.

Fresh production count: **4244/5513 = 76.98%**, Game **3571/4840 = 73.78%**,
Init 492/492, Debugger 181/181, zero drift. **167 more** exact functions reach
4411/5513 and 80%. Conversion counts and progress CSV stay unchanged.

## Source, interface and behavior

Entry 150A29C8..150A2AEC; ROM CFE78..CFF9C; 292 bytes. Owner
`conker/src/game/generated_CDE80.c`; original IDO 5.3 O2/g3, MIPS2/O32.
Interface: `s32 func_150A29C8(u32 actorIndex, u32 identity)`.

The function masks the identity to twelve bits and returns 1 only when the
unsigned D_800D3094 limit is strictly smaller. Equality is deliberately
accepted, including identity zero with limit zero. Enabled actors 0..15
use three u64 mask words per actor at D_800D30F0. A set bit returns 0;
a clear bit returns 1. Other actors call func_150A1DA0 with actor stride
0x32C, the live descriptor pointer plus identity*0x34, and mode 1, returning
that provider's complete signed result without Boolean conversion.

The original s32/u32 candidate had 73 words/frame32 but 25 differences.
Changing the actor parameter to u32 recovers every retail instruction word.
A signed identity, flat mask indexing, and nested condition forms retain
30/28/25 differences. Explicit high/low-mask expressions grow to 85/86 words
and remain rejected. Raw SHA-256:
`29c4ce4f891efd3b1fe016ddf35f85aeabf90bfd8b6c545a71e3b3feaded6e48`.

The shared `functions.h` declaration changes from u8/u16 to u32/u32.
The related name-hiding macro, undef and local signed-word declaration in
`game_16EE20.c` are removed, so this caller uses the shared interface.
The unrelated selector and descriptor-pointer workarounds remain intact.

## Alias relocation and independent links

Raw C binds both high/low mask words to D_800D30F0, with addend 4 for the
low word. The production padder's instruction-ordered explicit relocations
can pair both HI16 entries with the first LO16. An independent GNU link at
base 0x81337FFC exposes the defect: the lower load resolves to 0x81328000
instead of 0x81338000. The original assembly names D_800D30F4 separately.

Two expected-word/expected-relocation guards recover that binding at offsets
78 and 88: the lower HI16 targets D_800D30F4, and the lower load changes
its local addend from 4 to 0 while targeting the same alias. All operations,
registers, accesses, branches and scheduling stay intact. At the production
addresses, both raw and normalized bodies bind to all 73 retail words.
The corrected alias also passes the crossing rebase; the uncorrected padded
binding is retained as an effective negative. The complete old CSV byte
prefix is preserved, and raw SHA/all fourteen bindings fail closed.

## Shared-header dependency and complete-image gates

Predecessor consumer dac89d6d4eee8ba4427e2819d75907aabe66a4e8; tools
df1a1ddbe6dcde1df29fff47555241bec1ec9ad4. Qualification freezes 300
source/header/compiler/input files. The copied actual Make plan executes
643 commands for all 199 linked sources that include functions.h, using
their existing owner profiles and the corrected declaration/caller source.

194 complete objects are byte-identical. Five differ only in nonallocatable
.mdebug input sections, including private command paths and compile times.
All other section metadata, contents, symbols and relocations remain fixed.
Three initially flagged objects are actually identical; the generic pool
helper rejected their relocation kind. The closed section audit handles
these complete objects without weakening the shared pool helper.

The frozen production linker already discards .mdebug through its existing
DISCARD policy, and the baseline ELF has no .mdebug section. No linker or
exclusion rule is added. Original-path probes independently expose compile-
time strings; their temporary header/object writes are restored with hashes
and object timestamps checked. The final dependency gate audits every
retained section, including after the real production rebuild. A retained-
section corruption is rejected. No dependent owner is omitted.

The target preserves all 27 raw/padded neighbors, pools and register metadata.
Production and strict padders agree on 28 functions/pools, with all 31 original
case-label definitions accounted for. The actual five-command target Make
recipe reproduces the complete qualified object. Production freshly compiles
the target plus all 199 header consumers using existing profiles. Make also
rebuilds additional dependencies: 324 compiler invocations over 319 source
inputs. The complete-image gate covers their resulting linked contributions.
The target has no compiler diagnostics; dependent-owner/Make warnings
are recorded in the production log.

The independent complete-image predictor equals production after **258
changed bytes, zero exclusions**. It replaces only the target body/size and
accounts for one closed swap of D_800DBE64 / D_8009D2C0 symbol/string entries.
Complete named definitions otherwise stay fixed. Every other linked body
and all 6053 addresses stay fixed. All 189088 protected data bytes across
720 owners remain exact. Makefile/layout/absolute rules are unchanged. The
ordinary all target reaches the expected development-image checksum rejection.

## Focused qualification

Both mounted and sibling configurations pass six fresh tests before and
after installation. Four new modules are supplied through the ignored
sibling overlay. Its absent pool helper and original SDK-shift oracle use
explicit fingerprinted mounted fallbacks; its 2434 dirty paths are preserved.
The 199-owner audit is reused by exact input/object fingerprints and section
checks; it is not claimed as rerun for every unit-suite invocation. Both
shared smoke checks are fresh, with three unchanged shared regressions per
copy explicitly reused by their helper/test hashes.

| Check | Evidence |
| --- | --- |
| Ordered guest model | 1298 cases; all 73 query and all 11 original SDK-shift words reached; all 64 shift counts |
| Width and bounds | Full u32 actors/IDs, low12 masking, unsigned inclusive limit, zero-limit identity zero, mask rows and provider return bits |
| Calls and lifetime | One provider at most; live descriptor lookup; provider/global/incoming-home mutations; saved integer/floating roles |
| Callers | All 18 JAL sites and zero entry/interior pointers; original call/delay/consumer windows plus a complete 19-word caller; 76 connected cases |
| Branch consumers | Original branch-likely annulment and caller result overwrites, raw return stores and zero/nonzero consumption |
| Fault prefixes | 52 executed-access cuts, including original SDK accesses; literal low-word state agreement |
| Native32 | 447 cases at each of O0/O2/O3; typed u32/u32 callback; real SDK actor812/descriptor52/pointer32 layouts; trapping UBSan |
| Effective negatives | Stub, exclusive bound, wrong mask/bit/row, Boolean provider result; a separate guest byte-actor negative |
| Relocation/image | Four independent GNU links; signed carry crossing with an effective raw negative; closed two-symbol swap; six image corruptions rejected |
| Fail-closed inputs | All 73 word corruptions, all fourteen binding corruptions, guard-prefix and retained dependency-section corruptions rejected |

A byte-actor native control initially had no effect because native actors
stay within the valid fixture arrays. It is replaced by a discriminating
full-word guest control; the native suite retains six effective controls.
The oracle caches immutable SDK instructions per frozen ROM/root, avoiding
repeated ROM reads without changing executed words or reducing the corpus.

Guest sparse/wrapped addresses and mask-row overrun probes are not portable
C array claims. Native tests use valid actor/record/mask arrays. The original
SDK instructions execute in the bounded O32 decoder; full hardware upper-
register/FCSR state is not modeled. The collision provider remains a separate
production placeholder/bounded service. Most callers are qualified windows,
not complete scripts, geometry or gameplay. Routine task: zero Claude calls.

## Bank and next action

Production ELF SHA-256: `d5bf9694a34e0f53eeb2e4b90534de869351364dcff42fd046eaf97b254f1534`.
Binary: `ed59dfc2786fdf2b96ea4e138e6413bda667468318ff99c877ea8175fc3092f9`.
Owner: `12547fa9c85a37d599c5ccdd4669f86800b4e5125e63248e8080b847d2be52ad`.
Guard CSV: `9a0c7123b46c9a22927ff17a9aa46b3eba0f53256d31f0c2a1b461b5dd05d3d0`.

Reproduce in prepared WSL at the consumer root:
`python3 -m unittest tools.tests.test_game_record_occupancy_150a29c8_match -v`.
Canonical receipts: `conker/build/game-record-occupancy-150A29C8-match/`.
Tools first, then source/interface/guards/docs/README aggregate rows/pin are
committed locally. No push or host/frozen Release work. Graphify uses a scoped
refresh with explicit old-node retention, not full-corpus extraction.

Next inspect `func_150A3058`, the adjacent 79-word query/search placeholder.
Keep the full 80% goal active; func_1513FAB4 remains private and uncredited.
