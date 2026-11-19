# Note 2573: Nearest-height guarded byte match

Date: 2026-11-19. Consumer baseline `f74e7f3e51f8d8b21ba751a1f94f0cf3d75e4733`;
tools baseline `bca6f289d08c095fb7918442308b92d4106ac70d`.

`func_15104634` is installed as semantic C and **byte-exact across272 body
words and its complete275-word retail slot**, using121 relocation-aware
register-field guards. It replaces the former zero-return C stub. The existing
O2/g3 profile,224-byte frame, saved F20/F22 lifetime, incoming argument homes
and three private array bases remain. Four exact owner neighbors are unchanged.

Fresh production recount is **4,565 / 5,516 (82.76%)**, Game **3,892 / 4,843
(80.36%)**, zero address drift and951 still different. Init492/492 and
Debugger181/181 remain exact. **124 further matches** are needed for85% at the
current denominator. Conversion totals/bytes remain5516/6048 (91.20%),86.24%:
this function was already classified C. The full85% goal remains active.

## Recovered source and qualified guards

The original body is VA0x15104634..0x15104A74, with three alignment NOPs through
0x15104A80, ROM0x131AE4..0x131F30. The recovered interface is
`s32(f32 x, f32 z, f32 targetHeight, f32 *heightOut)` through F12/F14/A2/A3.
Collision context0 and the signed X/Z query feed an upward-orientation filter.
Accepted signed fixed-point heights are scaled by1/256; the nearest absolute
distance wins, with first-hit/NaN and earlier-tie behavior preserved. Empty
queries or no accepted triangles return0 without an output store; success
stores the selected height and returns1. The direct16-byte result-table type
is local to this owner; the unsuitable shared pointer declaration is unchanged.

The source and all137-to121-difference recovery work are banked in Notes2571/2572.
The installed source uses that exact selected text. The closed per-PC role
relation from Note2572 is freshly rechecked: all272 words,241 CFG nodes,
269 edges and839 fixed-point worklist steps, with identical ordered memory/FP
effects and no FP commutation or private-cell permutation. The candidate's121
changed words are solely register fields. Guard rows contain the exact expected
unbound word and unchanged relocation binding, then restore the corresponding
original register field. Complete original assembly independently supplies the
replacement words. No new profile, raw assembly body or branch/constant/offset
replacement is used.

The normalized source body and12 relocation sites equal the separately assembled
original. Both complete-owner padders agree on all five functions and constant
pools. The actual generated-C Make recipe executes compiler, padder and assembler
with the existing flags and produces the identical padded object. Six independent
GNU rebases link the normalized C body and original separately, including changed
high/low address halves. Altered expected guard words and relocation bindings
are rejected; all1088 raw bytes and12 bindings retain effective corruption gates.

## Linked-image and production proof

An independent predictor starts from the frozen ELF, replaces only the1100-byte
target slot with retail and updates the target's declared symbol size12->1088.
The complete linked image equals that prediction with **786 changed bytes and
zero exclusions**. All6051 function keys/addresses are fixed; this target is the
only changed instruction vector. Protected game data remains189088 bytes across
720 owners, with zero differing bytes or owners. Existing guard history is an
exact prefix of the121 appended rows. The conversion CSV and Makefile are
unchanged. Metadata outside the declared target extent is included in the full
byte comparison, rather than excluded from the audit.

Actual production Make rebuilds the dependent objects after the shared guard
manifest changes. Every resulting frozen input is compared against the declared
four-file source/guard/object/ELF plan. The production object and entire ELF
equal the pre-install prediction. ELF SHA-256:
`d3eeddd84c1cd3c6c0877467dfdf37015677dc0a81885ea7f5ed6d528b2f352d`.
Four effective image negatives reject changed header, unrelated tail, target
instruction and target alignment-tail bytes.

## Fresh tests and retained limits

Primary tools and isolated sibling overlay each pass **nine tests before and
after installation**. Each run includes494 guest cases per original/raw stream,
419 actual SDK32 cases each at O0/O2/O3 with strict aliasing/UBSan/float-cast
checks and eight effective source controls/profile, the complete role relation,
15 paired overflow probes, the original21-word caller window across32 scenarios,
both padders/actual Make, six GNU rebases and guard/image negatives.

The query harness has40 records and exercises query counts through39 with at
most24 accepted indices. The selected unchecked24-index local reproduces the
observed frame. Its original declared debug array length and asset-level hit
guarantees are unknown. Separate emitted-code probes retain retail's overflow
behavior:30 all-upward hits overwrite the output home with index29 and attempt
an unaligned output store. No overflowing portable C fixture is executed and no
new runtime bounds check changes retail. Raw unguarded temporary-register dumps
are related by role; installed guarded instruction words are literally retail.
No hardware FCSR, interrupt, full-parent gameplay or host acceptance is claimed.

Primary316 imported tool files and overlay317 have equal bytes except the empty
bootstrap. The934-file overlay uses339 unchanged sibling files,585 explicit
primary fallbacks,9 target files and1 bootstrap; only three target files are new
in this change. The real dirty `64CBFD Tools` sibling retains HEAD/status and343
dependency hashes. `make tools-check` passes. Older private actor-burst work and
the host/frozen Release are untouched. This restores the existing retail N64
routine and introduces no host-specific behavior requiring transfer.

Graphify's native update refuses a shrinking corpus. A scoped AST merge covers
the two new Python files and installed C owner while retaining prior node IDs.
The matching manifest has an explicit target edge. This is not full-corpus
extraction. Commit-hook producers are observed terminal before heading aliases
and the final graph fingerprint are sealed. Routine work used zero Claude calls.

## Next function

Inspect `func_15104A80` at VA0x15104A80..0x15104C44, ROM0x131F30,113 words,
currently GLOBAL_ASM in `conker/src/game_131F30.c`. Its opening frame is0x68.
Qualify its complete original body, caller interface, owner profile and neighbors
before conversion. No private candidate for that function is credited here.

Reproduce this match under prepared WSL: `python3 -m unittest
tools.tests.test_game_nearest_height_15104634_match -v`. Ignored evidence:
`conker/build/game-nearest-height-15104634-match-private/`.
