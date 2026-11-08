# Class-6 Record/Actor Scan Byte Match - 2026-11-08

`func_150A0D8C` replaces its zero-return placeholder with the complete
class-6 record/actor effect scan. The installed **173-word** routine is
byte-exact with its original **128-byte frame** and saved GPR/FPR lifetimes.
There are **31 guards**, derived from closed register-role swaps, instruction
permutations and commutative additions; 142 words already match directly.

Production totals: **4247/5513 = 77.04%**, Game **3574/4840 = 73.84%**,
Init 492/492, Debugger 181/181, zero address drift and 1266 different.
**164 more** exact functions reach 4411/5513 and 80%. Conversion rows are fixed.

## Recovered source, data and call interface

Owner `conker/src/game/generated_CDE80.c`; VA 0x150A0D8C..0x150A1040,
ROM 0xCE23C..0xCE4F0; 692 bytes, normal IDO 5.3 O2/g3/MIPS2/O32.
Entry is `void func_150A0D8C(void)`. The original caller at ROM 0x467BC
uses no arguments and immediately proceeds to another call without using V0.

The local 52-byte record type now exposes signed `radius` at 0x06, float
`parameter10` at 0x10, and `disabled` at 0x14. The existing heightOffset at 0x08,
flags at 0x15 and subtype at 0x17 retain their positions. The parameter's name
deliberately preserves its offset; the large effect provider is not restored
here. No shared header changes. Both old and new complete owners preserve
every other raw body and binding after these local type refinements.

The routine tests the opening count for nonzero, then snapshots D_8009F5A8
once. It scans 0x34-byte records under the live unsigned D_800D3094 bound,
requiring disabled zero and flags>>2 equal to 6. Each eligible record scans
exactly 25 actors at 812-byte stride in D_800CC2D0; the declared 26th element
is excluded. Actors require nonzero interaction_state and byte 5 equal to 0 or 1.

Each collision call receives (actor,current live record address,1). Only a
zero result proceeds. The record pointer is reloaded after that provider.
The Y difference is truncated and narrowed to signed 16 before the subtype
branch. Subtype 0 calls the handwritten distance helper with signed 16 x/y/z
deltas. The record base is reloaded after that helper, and signed distance
must be strictly below the signed radius. The inner radius is radius times
the opening scale, clamped above at 100; NaN comparison remains unordered.
The type 2 effect packet has actor index, float origins, zero, parameter10,
radius-inner, radius and 255.f. Other subtypes submit type 1 with actor x,
secondaryY at 0x180, actor z, zero, zero, 100.f, 150.f, 255.f.

The outer count is reloaded after the eligible actor scan. Provider writes
to actor coordinates, records, table pointer and count remain visible at
their original boundaries; scale changes do not replace the entry snapshot.
Changes to the current record's class do not re-gate the ongoing actor scan.

## Source experiments and derived normalization

The first for-loop draft was 171 words/frame120 and reloaded the scale in the
accepted path. An extern const alone did not change that compiler behavior.
An explicit scale snapshot under the opening gate restores its lifetime and
frame 128, but a guarded for-loop emits two redundant count-test words.
A guarded do/while restores 173 words. Keeping radius conversion anonymous
recovers the original F2/F0 allocation and improves 35 differences to 31.
Equivalent pointer-addition and actor-loop initialization order controls
do not reduce the remaining count.

Raw SHA256: `b98f5bb57bab00777996a0bacb3429473526f923ca4ef834516d965558a9aaeb`.
The normalizer derives two closed body-role swaps, S3/S4 and S5/S6, while
leaving fixed save/restore slots alone. It permutes the scale/150 setup,
two independent integer constants, and the type 1 outgoing-argument setup.
Three ADDU instructions exchange commutative operands. Every scheduled
instruction already exists in the raw C output; bindings move with their
instructions. Arithmetic, call targets, branch targets and frame size remain
unchanged. All 14 bindings are retained; the scale HI16/LO16 pair moves two
words later with independent signed-low carry handling.

The inherited guard CSV is an exact byte prefix of the new manifest, which
appends 31 expected-word/relocation rows for this function only. All 173 raw
word corruptions, 14 binding corruptions and an altered inherited prefix
are rejected. The production padder separately rejects a stale word and
unexpected relocation at every one of the 31 guarded positions.

## Owner metadata, actual Make and complete image

Predecessor consumer 6963fab4c27c3891cb676efe96a79496645ffe55 and tools
3fc4af2569409ac57959925d4895d90d3a2a5c0b. Frozen inputs: 105 files, including
the original caller and provider assembly/source, SDK headers and compiler
stages. All 27 raw/padded neighbors and all 31 original case labels are fixed.
The production and strict padders agree on all 28 functions and pools.

The raw owner's CPR1 mask changes from 0x003FFDFF to0x3FFFFFFF, adding
exactly 0x3FC00200 for the F8/F9 arithmetic pair and saved F22..F29 pairs
relative to the inherited mask. GPR mask, other coprocessor masks, GP,
geometry, relocation data and all other pool bytes remain fixed. Every byte
of that 24-byte metadata record has an effective corruption check.
Both padded objects retain the existing all-zero register metadata;
padded pools are compared literally without exclusions.

The actual copied five-command Make recipe reproduces the qualified complete
object. Production compiles this owner once under O2/g3 with no C diagnostics.
The independent whole-ELF prediction equals production with **533 changed
bytes, zero exclusions**: 531 target-body bytes and 2 symbol-size bytes,
12->692. No metadata permutation. All other linked bodies, all 6053
addresses, other named definitions and all 189088 protected data bytes across
720 owners stay fixed. Makefile, shared headers, layouts, absolute rules and
progressCSV are unchanged. Existing duplicate generated_12D630 recipe
warnings and the normal development-image checksum rejection are recorded.

## Focused qualification

Both mounted and sibling configurations pass six fresh tests before and
after installation. New task modules run in an ignored consumer-side overlay
for the sibling, with exact helper origins/dependency fingerprints and
explicit missing-helper fallbacks recorded. Its 2434 pre-existing dirty paths
stay unchanged. Shared smoke checks are fresh in both copies; three unchanged
synthetic shared regressions per copy are explicitly reused by source hashes.
Final installed receipts are sequential replays; earlier overlapping attempts
are archived and uncredited.

| Check | Evidence |
| --- | --- |
| Ordered model | 311 cases; raw C and normalized public effects agree with an independent reference; all 173 words reached from the public entry |
| Lifetime and mutation | All saved GPRs/FPR pairs restored; scale snapshot, current record reloads, live count growth/shrink, actor/class/subtype changes |
| Numeric boundaries | Signed16 narrowing, radius limits, strict distance test, finite/negative/zero/NaN/infinite scale cases; invalid native casts remain guest-only |
| Explicit aliases | Record/outgoing argument frame, record/actor fields, count/pointer globals; modeled outgoing stack stores and service effects |
| Real connections | 24 cases; original six-word caller gate, all 32 handwritten distance words, 29 effect-provider early-return words |
| Native32 | 203 cases at each of O0/O2/O3, trapping UBSan, SDK actor 812/record 52/pointer 32; two-int/eight-float effect ABI and callback/state digests |
| Effective negatives | Stub, unsigned Z, wrong class, skipped last actor, wrong mode, inclusive radius, scale reload, stale collision/distance records, cached count, wrong secondaryY |
| Fault prefixes | 692 executed access cuts across root and connected provider code; literal normalized low-word states |
| Relocation/image | Two independent GNU links of all 14 bindings with signed LO16 carries; four complete-image corruption controls |

The caller fixture owns the authentic return destination and stops before
the following JAL. Whole-ROM aligned census finds one direct call, no entry/
interior pointers and no direct interior jumps. The connected effect path
uses its original control-byte-15 early exit; its complete large body and gameplay
are not claimed. Collision stays an opaque service. The distance reference
uses its sorted absolute-value integer approximation and is checked against
all 32 real helper words on signed-short inputs.

Native cases use valid arrays and defined finite coordinate casts. Sparse
aliases, nonfinite/out-of-range conversions and large shrinking counts are
bounded guest probes. Fault equivalence is for normalized instructions;
raw scheduling/private fault states and full hardware upper-GPR/FCSR behavior
are outside this proof. Routine task: zero Claude calls. Host and frozen
Release remain untouched.

## Bank and next action

Production ELF SHA256: `68d7dd3659d2d20b824ca85fd7772d9445db5bdb3d3f6a1a7ab3fb11b26f3435`.
Binary: `976d183829b17e1d8381103ec9e7a7c24dabc9ce030515a821b85e6195a498dd`.
Owner: `f0d8db3a727c4cfff22e60de9910535b73122e136be178e4d92c90dd8629b3d1`.
Guard CSV: `efa24cbf5b02ded109725d251bc83be27272659cf305dc84f8f2dfa710890f82`.

Prepared WSL reproduction from the decomp root:
`python3 -m unittest tools.tests.test_game_class6_actor_scan_150a0d8c_match -v`.
Canonical receipts: `conker/build/game-class6-actor-scan-150A0D8C-match/`.
Commit tools first, then source/guards/docs/README aggregate rows/pin locally.
No push. Refresh Graphify with explicit retention of existing nodes; this is
a scoped update, not a full-corpus extraction. Keep the full 80% goal active.

Next inspect `func_150A09D0`, the 209-word record-state/audio updater,
including its incoming argument, class dispatch, live tables and callbacks.
