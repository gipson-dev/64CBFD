# Region emitter recovery and guarded byte match - 2026-11-16

`void func_151A5660(u8 *owner)` replaces the false zero-return placeholder with
the complete region-sampling emission callback. **356 of 403 words emit directly
from C**; 47 expected-word guards restore compiler scheduling, register choices
and two commutative multiply operand orders. The complete **403-word / 1,612-byte
slot and frame 0x108** are byte-exact. There are no insertions, omissions, dummy
locals or explicit register bindings. VA 151A5660..151A5CAC, ROM 1D2B10..1D315C.
This is a guarded C match; the final 100 words already emit literally from C.

Accepted production total **4,527 / 5,514 (82.10%)**, Game **3,854 / 4,841
(79.61%)**, Init 492/492, Debugger 181/181; zero drift, **987** still different.
**160 further matches** are required for the active 85% goal. Conversion remains
5,514/6,048 (91.17%), 86.19% of bytes. Root README changes only aggregate rows.

## Recovered interface and behavior

Owner+0x28 contains a 112-byte payload with source pointer, rate/scale,
accumulator, coordinate ranges, signed lifetime bounds, byte-value bounds,
height-query result and optional view mask. A null source retires the owner by
setting its signed halfword at +0xE to -1. Source disabled byte equal to one,
a rejecting optional view mask or accumulator at most one skips emission.
The callback preserves `(scale * rate) * D_800BE9A4` and the strict greater-than
one loop. It reloads the accumulator after each provider call before decrement.

Four modes recover rotated rectangular sampling, two radial variants and direct
coordinates. Signed halfword extents, unsigned angle conversion and byte
wrapping, original trig lookup, optional height result and fresh source reads
after mutable providers are retained. Lifetime and byte remainders use complete
unsigned random words. The C explicitly sequences each integer RNG call before
reading the mutable bounds; reusing the completed mode selector preserves the
exact IDO output while avoiding an unspecified C operand-evaluation assumption.

The 72-byte packet has **69 initialized bytes** and indeterminate padding at
+0x35..0x37. Constants are initialized once outside the loop; provider mutations
of retained packet/query memory remain possible. The position query is 12 bytes;
its cached result is an actual typed 36-byte object, not a float cast over a byte
array. The six-argument call is
`func_15149550(&packet,10,0,0,owner[0xC],owner[1])`; its result is ignored.
Unknown meanings retain names based on their offsets.

The original 45-word dispatcher `func_15149264` selects `D_8008A4E8[6]` via
owner byte +0x11. Actual update/cleanup table words and the whole dispatcher are
literal retail bytes in production. The producer is **func_150139AC**, whose
complete 163-word body calls `func_151491F4(300,-1,6,0,10,112,255,0)` and copies
112 bytes from its SP+0x50 to returned-record+0x28. Both the 49-word factory and
28-word wrapper already match retail in production.

Correction to the private Note 2505: the target's **24-byte source view is
partial**, not the source object's full size or array stride. The producer reads
flags/index through +0x1B, requiring at least 28 bytes, and indexes coefficient
table `0x80095FA0 + source.index * 56`. Typed declarations/comments preserve this
distinction. The producer and downstream `func_15149550` remain production
stubs; this static interface audit does not claim their execution or recovery.

## Fresh qualification and its limits

All seven maintained tests pass in primary tools, the separate tools checkout
through an isolated task overlay, and installed production, with the same eleven
task-file hashes and recorded actual import origins.

- Seven symbolic opening paths and 42 inductive iteration paths compare private
  frame state at providers/exit, arbitrary public aliases, retained packet/query
  mutations and saved-register restoration. Five effective iteration controls
  reject, and a T8/T9 rename positive passes all 42 paths. Forty-five differing
  words are proved by the actual transfer relation; two floating multiply
  operand orders at +0x264/+0x298 are explicit projections, not an ordered-FP
  equivalence claim. Exact signed16 sum/difference conversions are compared by
  epoch; remaining effectful FP operations retain their order.
- Conservative range analysis of complete original and literal production
  `func_1504697C` (161 words), `func_15047004` (43) and `func_15046C80` (32)
  proves the normal wrapper return is 0/1. Changing a secondary return to 256
  propagates through the wrapper and rejects the byte-narrowing contract.
- Guest oracle: **793 cases per retail/raw/guarded stream**, 764 native-eligible
  and 29 guest-only. Coverage is **398/399/398 target words** and all 27 trig
  words, including valid/invalid unsigned-conversion fallback routes. Five
  semantic instruction defects reject. Remaining normal-path holes are dead
  copies and the two zero-divisor BREAK words outside valid input; complete
  guarded bytes are nevertheless checked literally.
- Native32: **764 cases each at O0/O2/O3**, strict aliasing and UB traps,
  568 public bytes/seven globals, provider arguments and 69 defined packet bytes.
  Eight broken C bodies compile and exit 3; eleven runs pass their expected
  outcomes. Packet padding and guest-only endian/invalid-conversion cases are
  not credited as portable native behavior. Earlier native failures exposed the
  real RNG/bound sequencing issue; corrected v39 retains identical raw MIPS.
- Complete original dispatcher: **384 cases per stream**, every one of its 45
  words, actual tables, signed selector/lifetime wrap, ignored callback result
  and post-cleanup lifetime recheck. Cleanup/release remain bounded providers.
- Both real full-owner padders, **439 raw-word/binding corruptions**, **94 stale
  CSV controls**, all 36 original bindings and **12 independent GNU links**
  over four code/data layouts, including HI16 carry. All 14 neighbors and pools
  remain unchanged; no carrier insertions or omissions are accepted.
- Complete producer/factory static interface audit verifies the 112-byte payload
  and partial source view. It does not execute or restore the producer.

Scope is normal mapped/aligned public RAM, a private disjoint stack and bounded
o32 providers. Physical FCSR/trap/fault-prefix parity and gameplay are not
claimed by symbolic or native models. The guarded production stream separately
has complete literal retail instruction identity.

## Production audit and retained evidence

Predecessor consumer `8c129a37`, tools `13598c5`. Original target SHA256:
`d899dd1968e9cfb89b1c45972a413f119da2d41f03c06eb0ad10a63cc021205a`.
Canonical raw SHA256:
`02fc65e9c06e740bd1e5dc1bce5dad2062dfbcab08e0a7c2ce546bdd38f597dc`.

The initial 1,360-input snapshot and intermediate failed migration snapshots
remain immutable. The final 1,415-input snapshot reuses only verified immutable
snapshot files (1,414 hardlinks and one copied correction), with **no live
worktree hardlinks**. Bootstrap defects involved premature imports and a string
passed to `write_bytes`; fixes changed maintained wrappers, not proof gates.
Suite completion includes its final fingerprint scan before receipts are sealed.

Actual Make shadow and production rebuild from C; no prebuilt object is installed.
Exactly source, guard CSV, owner object and ELF change; **1,411 frozen inputs
remain unchanged**. Only one of 698 objects changes, preserving all other 6,050
bodies, all 6,051 addresses, 14 owner neighbors, pools and register metadata.
The complete production ELF equals its independent prediction:
**1,366 changed bytes, zero exclusions**. All
**20,289 named definitions** agree except target extent;
metadata accounting is complete. Symbol-value/name, protected-data and target
corruptions reject. Old guards remain an exact byte prefix, 47 rows append and
conversion CSV remains unchanged. All **189,088 protected bytes** remain exact.
Production ELF SHA256: `ec37c2d7281c9b7b9b95266aa7184ffb6b25494fd7403dbc98ac30212ee2577b`.

Prepared qualification requires the retained immutable snapshot and a fresh
owned output directory, for example under `conker/build/`, supplied through
`CBFD_REGION_EMITTER_WORK`. Run
`python3 -m unittest tools.tests.test_game_region_emitter_151a5660_recovery -v`.
Receipts: `conker/build/game-next-151a5660-private/adoption/`, including sealed
primary/sibling/installed suite reports, actual-Make/image/production audits
and the actual ELF recount. The sibling's 2,434 dirty paths and 337 dependency
files remain unchanged; the overlay imports are recorded separately.

One earlier packet-only Claude attempt produced no usable retained answer after
an encoding failure; it supplied no acceptance evidence and was not repeated.
The native Graphify update refused a smaller replacement and preserved all
63,823 prior IDs. A scoped AST merge refreshed the eleven changed code files,
retained every prior ID and added an explicit manifest-to-function reference;
no full-corpus re-extraction is claimed. At the current sibling `64CBFDOGL` path only `.codex`
and `recomp_scene` remain, with no Git checkout or source tree available for
synchronization/build validation. No host, Release or save files are changed;
this decomp result does not establish host or gameplay acceptance.
Commit tools before consumer; no push or dependency upgrade.

Next inspect `func_151A6C90` from the actual unmatched list. The producer
`func_150139AC` and packet consumer `func_15149550` are separate open recoveries.
The total 85% goal remains active.
