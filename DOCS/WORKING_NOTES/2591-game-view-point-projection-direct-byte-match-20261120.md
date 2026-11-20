# Note 2591: Active-view point projection direct byte match

Date: 2026-11-20. Consumer baseline `cf68fe6a4fb05ffa5b16c35872741e52a61592dd`;
tools baseline `0c8f6368ae986e106c72b2128d55aeb3791edb52`.
Qualified tools commit: `4234c627e309eac0326b1b242bf08c6573013fe2`.

`func_1517EAAC` replaces its zero-return C placeholder with a complete world-point
projection. It **directly matches all 92 words / 368 bytes**, with the original
**152-byte frame** and **no normalization guards**. Both helper interfaces and
all exposed private addresses match retail directly from the existing O2/g3
profile. Source names describe the recovered behavior; they are not debug names.

Fresh production recount: **4,577 / 5,527 (82.81%)** total, **3,904 / 4,854 (80.43%)** Game, zero address drift and 950 still different. Converted totals stay **5,527 / 6,048 (91.39%)**, 86.54% of bytes. Init492/492 and Debugger181/181 remain exact. **121 more** matches are needed for 85% at the current denominator.

## Interface and recovered behavior

Owner `conker/src/game/generated_1AB530.c`; VA `0x1517EAAC..0x1517EC1C`, ROM
`0x1ABF5C..0x1AC0CC`. The interface is
`s32(f32 x, f32 y, f32 z, f32 *screenX, f32 *screenY)`. The original assembly
remains unchanged. A complete aligned ROM census finds one direct JAL, at
`0x1AB838` in `func_1517E28C`, and no literal target pointer. Arbitrary computed
callers remain outside that census.

The routine captures the active camera's negated X and Y rotations and its Z
rotation, and passes them to `func_15110360` with a 4-by-4 matrix. After that
helper it reloads the active view, captures its two scale values, then calls
the existing eight-argument homogeneous projection helper `func_150A7A00`.
For W greater than 10, it computes the reciprocal once, retains the original
ordered multiplications, and writes `scaleX + projectedX` and
`scaleY - projectedY`. Otherwise it writes positive zero to both outputs and
returns zero. It returns one on the accepted-depth path. Output pointers may
alias one another or public camera/view fields; scales remain the earlier
captured values even when the projection helper changes those public fields.

The private camera view has stride 0x9A0, with floats at +0x380, +0x388 and
+0x5EC. The private screen view has stride 0x180 and scales at +0xC/+0x10.
Native SDK32 checks qualify these sizes and offsets. No shared structure,
caller source, compiler profile, data layout or word-patch history is changed.

## Source shape and exact exposed storage

The first complete source emitted 92 words/frame144, but had 64 positional
differences. Naming the three rotation temporaries recovered their in-place
FP lifetimes. Placing the reciprocal local before the four projection outputs
then recovered the remaining private layout. The selected source emits every
retail word directly, including the unreachable zero-load word at index83.
No padding-only local or expected-word substitution is used.

The matrix is exactly at SP+0x38, with four projected-output homes at
SP+0x84, +0x80, +0x7C and +0x78. Both helpers see the same matrix pointer.
The scale spills are SP+0x34/+0x30, and the complete private frame and incoming
argument bytes agree between raw C and retail in the guest checks.

## Fresh qualification and boundaries

Six tests pass before and after installation in each tools configuration.
All **335 imported Python fingerprints** agree. The isolated second bundle has **1042 files**, comprising 347 matching sibling files, 690 primary fallbacks, four task files and one bootstrap. The real dirty sibling preserves its HEAD, complete status and **351 dependency hashes**.

The independent big-endian MIPS contract passes **896 cases per stream**:
all four view indexes, both stack phases, seven depth patterns including the
exact 10 threshold, the next binary32 value above it and a quiet NaN,
effectful helper view/scale changes, and four output-alias arrangements.
All **91 reachable words** execute; unreachable word83 is independently pinned
by the complete byte match. Public buffers, ordered helper arguments, return,
saved registers and complete private memory agree. Four effective instruction
controls reject an inclusive depth test, wrong Y sign, wrong scale home and
wrong camera rotation.

Native SDK32 passes **448 cases each at O0/O2/O3**, with strict aliasing,
UBSan, opaque providers and complete public-buffer hashes. Three compiled
source controls execute and fail. The original seven-word caller window also
executes **160 cases per stream**, loading F12/F14/A2, passing the fifth
argument in its real delay slot, executing the recovered routine and taking
the actual result branch. Helpers remain bounded models. Complete parent,
raw hardware/FCSR exceptions and natural gameplay acceptance are unclaimed.

All **seven other raw owner functions and bindings**, constant pools and
diagnostics stay fixed. Both independent padders agree on the complete object.
The actual five-command Make route retains O2/g3. Independent full linking
predicts **287 changed bytes**, limited to this function's 368-byte code slot
and its ELF symbol size changing from 12 to 368. All 6,051 named function
slots and addresses stay fixed; the **189,088-byte protected data audit** is
exact. Production reproduces the complete predicted ELF with zero exclusions:
`24e5239571eec2c8a0c683c61b692a6fa424479522326c1a3ad1ad3136403827`.
The progress CSV is byte-identical because this was already counted as C.
Unchanged neighbor receipts are reused by source/object identity, not called fresh.

## Graph and continuation

The native Graphify update remains fail-closed on its reduced corpus. A scoped
five-file AST merge plus explicit note/original-assembly references preserves
all existing IDs and previous qualification metadata. Commit-hook producers
are observed to completion before the retained graph is sealed. This is not
a full-corpus semantic re-extraction claim.

Codex owns the changes; zero Claude calls. Local commits only, no push, no host,
save or frozen Release changes. Continue the active 85% goal from the new
committed fingerprint baseline. Next audit `func_1517EC1C`, an existing C
placeholder in the same owner; it is not yet recovered or credited.
