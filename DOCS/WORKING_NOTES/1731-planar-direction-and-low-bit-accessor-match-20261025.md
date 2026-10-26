# 1731 - Planar Direction and Low-Bit Accessor Match - 2026-10-25

The adopted Native ELF measures **3,808/5,506 exact C functions (69.16%)**,
Game **3,135/4,833 (64.87%)**, zero address drift and 1,698 different.
Both `func_1510F820` and `func_1510F8CC` receive matching credit after production
qualification. The corrected 75% threshold is 4,130/5,506; 322 more matches remain.

## Recovered C and interfaces

Owner `generated_13BB20` contains the pair. `func_1510F820` occupies VA
`0x1510F820..0x1510F8CC`, ROM `0x13CCD0..0x13CD7C`: 43 words and a 40-byte
frame. Its seven-argument O32 interface forwards two optional vertex sources
opaquely to `func_1510E388`; the fifth argument is intentionally unused.
Four float outputs retain the helper components and their normalized values.
Names and comments describe the recovered roles without renaming the retail symbols.

The routine computes the planar magnitude, saves both original components,
and scales the magnitude by `D_800A2D9C`. That retail float is word `0x3CA3D70A`
(approximately 0.02), independently checked in ROM and the live ELF. A zero
scaled magnitude writes 1 and 0; otherwise each current component is divided
by the scaled magnitude. Preserve late component reloads and output aliases.
One unreachable duplicate divide at word 34 remains in the complete emitted body.

One expected-word guard at byte `0x64` (word 25) preserves the commutative
`c.eq.s` operands. All instructions emit from semantic C; the guard changes
only that comparison encoding. The body has three relocations: a helper call
and the HI/LO constant pair. The ordinary O2/g3/mips2/o32 profile is unchanged.

`func_1510F8CC`, VA `0x1510F8CC..0x1510F8D8`, ROM `0x13CD7C..0x13CD88`,
is the complete three-word unsigned accessor `return value & 0x1F;`.
It matches directly from C with no guards, frame, calls or memory access.

## Inventory boundary correction

The old layout merged both functions into one 46-word extent, while
`undefined_funcs_auto.txt` retained an absolute definition of the leaf.
That definition overrode the object symbol into SHN_ABS and placed it outside
the progress parser's ordinary Game entries. Remove only that stale fallback
and split only the verified boundary into 43-word and three-word rows.
Converted instruction-byte totals remain unchanged.

The generated fallback manifest is ignored by Git. Bank the durable extraction
rule in `conker/symbol_addrs.us.txt` instead: add only `func_1510F8CC`
with `type:func defined:true`. The actual Splat parser/writer excludes
that defined leaf while preserving an unresolved function canary. Removing the
annotation is an effective negative control that recreates its stale fallback.
No full extraction or broader alias conversion is performed.

An independent inventory-only full link changes exactly two ELF bytes:
the leaf's symbol section becomes Game instead of absolute. It changes no code
and earns no matching credit: 3,806 exact / 1,700 different on the corrected
5,506-C inventory. Production recovery of the pair then yields 3,808 / 1,698.
The total inventory becomes 6,045 functions; Game becomes 5,324 total / 4,833 C.

The broader absolute-symbol screen finds 150 STT_FUNC aliases inside existing
mapped extents. That is a review screen, not evidence of 150 missing functions.
All other aliases and extents remain unchanged and unqualified. Review their
actual boundaries before any later inventory or matching claim.

## Caller, helper and behavioral evidence

Five retail JAL sites in `game_77AD0` are audited, across parents
`func_1504B0FC`, `func_150511E8` and `func_15051558`: VA `0x1504B7C8`,
`0x15051298`, `0x150512E0`, `0x15051604`, `0x15051720`. No literal registration
is found. Their source and object remain unchanged; the C parent stubs receive
no new credit. The graph query is used for context and all real sites are
checked against the original assembly.

Both tools copies pass eight fresh private checks and shared tools checks.
The initial installation runs two fresh checks plus six identity-gated reuses;
those original receipts remain preserved. After adding the durable tracked
annotation, both copies run all nine final checks freshly, with zero reuse,
including the actual Splat writer and missing-defined negative. The final
module hashes, unchanged 61-input snapshot, tracked annotation and all 14
frozen runtime artifacts are pinned. Both shared tools checks pass again.
A second actual Make shadow and production relink preserve the complete
qualified object, ELF, map and progress bytes.

- 3,570 guest normalizer cases cover 14 alias layouts, two phases, signed zero,
  tiny/large values, scale aliases, late component reloads and an unused unmapped
  argument. Raw, fitted and original complete states agree.
- 320 leaf cases cover all 32 low values and high/sign words. Thirty-six cases
  execute the full original 171-word triangle helper with packed, indirect and
  NULL vertex sources; all helper words are visited.
- Forty original caller-window cases enter 48 calls across all five physical
  sites, verifying all seven arguments and local gates. This is bounded window
  evidence, not full parent reconstruction.
- SDK/native32 O0/O2/O3 each run 1,296 normalizer and 128 leaf cases with trap
  UBSan, layout assertions and a NULL unused argument. Nine compiled semantic
  negatives are effective. The native helper provider is bounded.
- 134 fired guest fault-prefix pairs preserve access order and complete state.
  Guest fault behavior is not claimed as portable C behavior.
- All 43 normalizer words and three leaf words have effective perturbation
  controls, plus binding/extent/history and actual padder controls. Six GNU
  links span three layouts, including HI/LO carry rebases. Seven strict-image
  corruptions are rejected.

Preserve all 12 neighboring raw/padded functions and their bindings, including
`GLOBAL_ASM` routine `func_1510E950`. The complete actual five-command Make
object equals the independently qualified padded object. No helper, parent,
hardware or full-gameplay acceptance is inferred.

## Production and sealed adoption

Actual Make exits zero in 5.239s and reproduces ELF `ae2868d7489238a6ed10b99e956ec9a8dd4d94a8f13008b26d2d8c7dc5045322`.
The complete image delta is 150 bytes: 127 code bytes and 23 metadata bytes,
zero exclusions. Metadata includes target size, the leaf section correction
and a closed serialization cycle among `D_800A2D9C`, `D_80090ADC` and
`D_8009059C`; named symbol values and types remain fixed.
The disassembly inventory changes from 6,055 to 6,056 functions only by
reindexing the verified leaf. All existing addresses and 6,054 other existing
function bodies remain fixed. The inherited duplicate generated_12D630 Make
warning remains unchanged. Production progress is regenerated from the actual
Make map and independently verified against the qualified inventory.

Source SHA: `e87e29c165a1f565fc119d019c7683af28b25e2f6286b361281f26fd9ef044fa`.
Guard CSV SHA: `8c374d6e04e30a01128238f044a404be119457734195fc61543fea76082c4013`.
Layout SHA: `1eb1e705545ec2e19f6b68ef5025d816f4d513684518968a6806008b6dc17612`.
Fallback manifest SHA: `d1e08c44df8e90d3094ee91f11ee700b5cc4f2c8cbfa7b41ab9cba3ff9d1a2f6`.
Padded object SHA: `5efef08c48e49890412fa82c9b7badc6e37df96061bfa04de5c7223804ba998a`.
Raw normalizer SHA: `cd91b91626b621e7c1f78abd35cf3019e4d7b58520a59a47335eca607d4de0e6`.
Raw leaf SHA: `17da24965109cb7e9ea29ece4ce439695121e840905cd692c52b34176d560024`.

Baseline consumer `5bf49ac9`, tools `bed7f692`, ELF `d657fc68`.
Initial qualification tools `8587d22ef25acbc631b43e56fa0b523367bf2d9b` are committed first.
The durability follow-up `7f41664382322dae40a4f0784e54a4b3399b454d` is committed before
the consumer pin; no old tool execution is credited to its changed modules. All 16,091 inherited/owned files and 61
focused inputs are sealed. Native adoption changes exactly nine qualified
source, manifest, object, ELF, map and progress outputs. The durable metadata
follow-up adds the tracked symbol annotation and updates four canonical tools
files across the two copies: 14 explicit final seal overrides in total. All
other sealed inputs remain identical; no runtime artifact changes in that follow-up. Preserve the older mirror's history and all 1,672
pre-existing dirty paths; add only this tools pair there.

The scoped graph closeout refreshes eight changed C/MD files while retaining
or uniquely relocating all 44,272 previous nodes. Historical manifest rows
outside the scope retain their original freshness. Tools AST extraction is
separate because the parent ignores `tools/`; this is not full-corpus extraction.
Use Graphify's existing isolated Python environment for owned workers.

## Continuation

The remaining ELF-pinned queue has 1,569 placeholders, 120 semantic/other
definitions and nine unlocated screens. Next screened placeholder: `func_151592B8`
(`generated_185560`); it is uncredited until its full qualification gates pass.
Keep the 75% goal active. Routine Claude calls: zero. No push or host-port work.

Prepared-checkout focused command:

```sh
python3 -m unittest tools.tests.test_game_planar_direction_match -v
```

Keep raw objects frozen between executions. Recompilation requires fresh
fingerprints; compiler debug metadata remains in the strict image audit.
