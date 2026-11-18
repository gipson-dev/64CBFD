# Snapshot trail emitter guarded byte match - 2026-11-17

`func_151B0050` replaces its zero-return placeholder with the complete
snapshot trail emitter. Semantic C emits **90 words / 360 bytes**, retaining
the original **0x80-byte frame**. **Eight checked guards** move four private
capture stores and their reloads down eight bytes; no instructions are
inserted or omitted and no retail instruction ranges are embedded in C.

The independent production-ELF recount is **4,540 / 5,514 (82.34%)**, Game
**3,867 / 4,841 (79.88%)**, Init 492/492 and Debugger 181/181. Address drift is
zero; 974 converted functions remain different. **147 further matches** are
needed for the active 85% goal. Conversion counts, converted bytes and the
classification CSV are unchanged. Root README receives two aggregate rows.

## Interface and recovery

Owner `conker/src/game/generated_1DD500.c`, VA151B0050..151B01B8,
ROM1DD500..1DD668. Original `D_8008AA00[21]`, retained at ROM22F514, binds
this callback. The 15 incoming argument slots remain explicit: X/Y/Z are
slots 2/3/4, signed pitch is slot 8, signed heading slot 9 and the channel byte
slot 14. The donor's compressed eight-argument prototype and inferred floating
arguments to the random providers are not adopted.

The routine snapshots all three position components before any provider.
It obtains a real speed sample, multiplies D_800AA28C and adds D_800AA290,
then calls the direction helper with heading, pitch, speed and a private
three-float destination. It captures, in order, a real extent sample, unsigned
integer duration sample, unsigned integer color sample and real time sample.
A final integer draw chooses `(sample & 1) + 3` for the submission request.
All eight calls remain ordered.

The 18-argument `func_151DA6F8` submission uses both private vector addresses,
the extent expression, duration `%20U+31`, color `%101U+155`, time scaled by
D_800AA298 plus D_800AA29C, the request and original fixed fields, channel
and final 1. The callback returns 1 regardless of the submission result.
The actual direction-helper interface and the actual submission body's
three-float reads confirm both12-byte exposed objects; private captures
are outside either exposed vector.

The original extent expression includes a zero multiply. IDO folds literal
`sample * 0.0f`, shortening the body to 85 words and removing original floating
operations. The explicit `(f32)(s32)0` form retains the original integer-zero
conversion, multiplication and addition. It also preserves signed-zero and
nonfinite operation behavior in the guest checks. Alternative union/local
forms either changed the frame/pools or emitted additional instructions and
were rejected. The normal O2/g3/mips2/o32 profile is unchanged.

Raw body SHA-256:
`ed0bc9a3b8520bd11d4217f34acafb085e0c2c058b66f7d60a2367d1fb5f4aff`.
All 18 call/data relocation records match. The full owner retains 15 neighbors,
including the existing `func_151B03B8` GLOBAL_ASM restoration, and unchanged
normalized pools. That neighbor remains classified as assembly.

## Private capture relation and focused validation

Raw words 26,28,30,32,35,42,43,49 access four captured words at SP58..64;
retail uses SP50..5C. The independent derivation changes only those eight
identified SP-relative store/load offsets by minus8. Position SP74, direction
SP68, saved RA SP4C, outgoing 18 homes and all incoming homes already match.
All 90 derived words equal retail.

The complete symbolic proof compares **188 private/incoming bytes**, ordered
public and FP/status effects, all 8 calls, all 18 outgoing arguments, both
exposed vectors, restored saved registers/SP/RA and return 1. Raw private
layout is related through a bijective rotation of SP50..67: raw50..57 maps
to canonical60..67, and raw58..67 maps to canonical50..5F. The canonical
entry-byte relation is explicit. Derived/retail has the literal relation.
An independent GPR allocation is a positive control; five effective negatives
reject wrong angle home, capture slot, position snapshot, vector pointer and
frame restoration. This is not literal physical raw-padding or fault equality.

All **six final checks pass fresh in both tools configurations** with zero
failures, errors or skips: **85.042s primary / 89.212s sibling overlay.

- Both full-owner padders preserve all 15 neighbors and all 90 target words.
  **12 GNU links** cover independent symbol/carry layouts. **108 controls**
  reject each raw-word or relocation-binding corruption.
- **48 guard controls** reject wrong expected words, replacements and missing
  rows in both padders. Exactly 8 rows are appended; prior CSV bytes remain
  intact and no guards are retired.
- Raw/original/derived streams each pass **2,432 guest cases**, visiting
  all 90 words and comparing **14,592 ordered FP observations**. Independent
  results check all 18 arguments, both vectors and provider call frames.
  The derived stream equals retail's complete compared RAM and frames.
  The additional 128 signed-zero cases include positive extent with a
  negative-zero global, making the folded-zero control effective.
- Native32 source compiles fresh at **O0/O2/O3**, each passing **640 defined
  finite/signed-zero cases** under UBSan. Seven effective negatives cover the
  folded-zero expression, snapshot X, signed duration remainder, swapped
  angles, wrong channel, final argument and callback return. There are 10
  builds/runs total; native checks cover defined fields and disjoint objects.
- The original **16-word radial-dispatch window** executes **80 cases per
  stream**, checking all 15 argument slots and continued dispatch. A zero-return
  control takes the original loop-stop branch. The complete parent and other
  three table-dispatch parents remain outside this qualification.

Initial private guest screening covered 2,304 cases; the final maintained
matrices include the additional 128 signed-zero cases. Preliminary screening
is retained separately and does not substitute for these final receipts.
Hardware FP traps, cycle timing, arbitrary native aliases/private padding,
opaque provider implementations and gameplay acceptance are not claimed.

## Actual Make and production audit

The independent shadow executes the actual **five-command GLOBAL_ASM owner
recipe**, including assembly processing, compilation and padding. Real
production Make builds only this owner, relinks and recounts; no prebuilt
object is copied. Production equals the independently predicted ELF:
`76f6337145e8d03ac4efe3dfefe031049c9b24da0c293e98ad3cee2fbd5f7a64`.

Strict complete-image accounting changes **369 bytes** with
**zero exclusions**. Six named symbol/string reorder groups are modeled
explicitly; definitions retain their values except the declared target size.
Four effective image controls reject symbol-value, name-byte, protected-data
and target-word corruption. All other **6,050 bodies and all 6,051 function
addresses** are unchanged. Exactly one of 698 objects changes, retaining
all 15 neighbors. All **189,088 protected bytes / 720 owners** remain exact.

Fresh installed-source compilation agrees on all 16 owner functions. Actual
production words pass another 2,432 guest and 80 caller-window cases per stream.
Padder/link, complete symbolic and native receipts are reused only with exact
task and input fingerprints. Production match-progress, tools-check and an
independent actual-ELF recount pass. The pre-existing duplicate
generated_12D630 recipe warning remains unchanged.

## Preservation and next target

The baseline freezes **1612 inputs** without links to live-tree files.
Exactly four change: source, guard CSV, owner object and ELF. Eight maintained
task files and actual imported dependencies are separately fingerprinted.
The sibling's 2,434 dirty paths and 343 scoped dependencies remain byte-identical;
testing uses an isolated overlay. Claude calls are 0. Host Release/saves are
untouched; the adjacent host directory has no source checkout to synchronize.

Evidence is retained under `conker/build/game-next-151b0050-private/adoption/`:
sealed paired suites/imports, independent proof, guest/native/caller receipts,
padders/links/controls, independent Make/image prediction, production audit,
installed focus and actual recount. Native Graphify update fails closed on
its reduced scan; scoped AST merging of seven code files retains all
65205 prior IDs and the explicit target reference.
This is a scoped refresh, not full-corpus extraction. Commit tools before
consumer source, guards, notes, aggregate README rows and pin, locally only.

Next inspect **func_151B01B8**, the **128-word** placeholder in the same owner.
The 85% matching goal remains active.
