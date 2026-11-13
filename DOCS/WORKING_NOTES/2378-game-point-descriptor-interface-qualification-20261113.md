# Point descriptor and trail interface: private qualification

Date: 2026-11-13. This continues [Note 2369](2369-game-point-descriptor-frame-abi-screen-20261113.md).
`func_151382E0` is still an uninstalled placeholder and receives **no matching
credit**. The installed Game checkpoint is **3,763 / 4,843 (77.70%)**;
112 more exact Game functions are needed to reach 80%. Parent baseline was
`994e2247876b6338573477a92b677f3acb3e5fe4`, with tools at
`c18d742e318361b5faf5250a26be1c93af8f6af4`.

## Candidate and interfaces

The 81-word point routine prepares a 76-byte descriptor and calls
`func_15153F18` unless the table category is 2. Its known original caller,
`func_15138BC0`, obtains normal types 0 through 19 or sentinel 99, and passes
positions and surfaces in its own stack frame. Three descriptor bytes remain
unwritten. The screen fixes that caller's unused but inconsistent return
declaration to `void` and uses the tagged surface type consistently.

For the trail helper, the private experiment standardizes all three active
call sites and its definition to the same `void *, void *, s32, s32, s32`
interface, keeping typed local pointers inside the helper. The two existing
caller objects compile with unchanged functions and sections. The helper's
raw body changes only five frame/home instructions; updating the expected
preimages of five existing guards retains their previous replacement words.
Both helper padders then reproduce all 41 functions in the installed object.
The point routine uses four additional guarded frame/home words. Its padded
body and relocations match all 81 original words; its 64 other padded owner
functions are unchanged. The candidate must not be described as a direct C
match: before padding its stack frame is `0x78`, versus retail's `0x70`.

## Fresh private checks

- **Guest point model:** 640 bounded cases, covering all 81 retail instruction
  locations, categories 0/1/2/255, representative groups, both stack phases,
  and separately allocated or caller-owned-stack positions. The retail and
  padded streams have identical complete state and events. The raw candidate
  produces the same initialized descriptor bytes and public effects in those
  cases; untouched bytes 61–63 retain their respective original stack data.
- **Frame alias limit:** guest-only inputs into the callee's private frame at
  offsets `-0x64` through `-0x48` in steps of four exposed differences between
  the unpadded C stream and retail. The padded stream matches retail for those
  inputs. These artificial accesses are not a portable C alias guarantee.
- **Connected caller:** 512 cases execute the complete original `func_15138BC0`
  into the original point routine, with modeled surrounding providers. They
  check category gating, the caller's stack positions, and forwarded surface,
  group and context. This is not a gameplay or hardware acceptance test.
- **Native point C:** 20,480 cases per optimization at `-O0`, `-O2`, and
  `-O3`, using 32-bit code and trapping UBSan. Six deliberately incorrect
  gate, flag, position, group, context, and constant variants were rejected.
- **Trail helper:** 256 guest cases compare original, padded, and raw C code
  against the existing independent provider model. The existing independent
  native model also passes 256 cases each at `-O0`, `-O2`, and `-O3` with
  UBSan. The host harness uses repeated-byte channel inputs, so it does not
  independently establish host endianness of the byte extraction.
- **Padders and relocation:** all four new point guards and all 16 existing
  helper guards rejected corrupted expected words, including both helper
  padding implementations: 36 effective corruption checks. Fifteen GNU
  links exercise point and helper bodies at three low-half address layouts.
- **Actual Make and whole-image shadow:** 21 actual recipe commands build all
  four owners and the separate caller translation unit. The helper and its
  other two caller objects retain every section; the point owner changes
  `.text`, `.rel.text`, `.symtab`, and `.strtab`. A strict linked-image
  prediction has zero exclusions, accounts for the new target body/extent
  and symbol ordering, preserves all 6,051 function addresses and changes no
  other function body. All 189,088 protected bytes across 720 owners match.

The scripts and candidate files are transient under ignored
`conker/build/game-point-descriptor-151382e0-screen/`. The point candidate
SHA-256 is `0c870e882a43ec983007b9b3349580dbb12197333dd676ace5655845f9cd8eae`;
the helper candidate is
`9d58d3ce115914255670b190f3d79051b6fb9a855ad3853b30796cb7df093ea8`.
These receipts depend on the exact source, compiler, baseline, and inputs;
recheck fingerprints if any change. The private scripts are not committed
reproducible tests and the shadow CSV normalized mixed line endings, so it
must not be copied over the production guard manifest wholesale.

## Before promotion

1. Review the nested typed-subobject follow-up below and the pre-existing
   descriptor views of the helper's other callers. A common `void *`
   declaration alone does not prove typed-access compatibility. Do not infer
   that UBSan proves effective-type rules.
2. Make durable, fingerprinted qualification fixtures, including connected
   caller and helper checks, and verify affected historical tests and both
   tools checkouts. Update only the five intended guard preimages and append
   the four point guards without rewriting unrelated mixed line endings.
3. Revalidate full production Make, guards, image, protected sections, and
   actual ELF recount after installation; update status and Graphify, commit
   tools before the consumer, and retain the 80% Game goal.

## Follow-up: nested typed subobjects

The prior flat descriptor passes differently named aggregate views into the
helper, so its passing machine and native screens alone do not settle C
aliasing. A later private variant instead gives the point descriptor separate
`AngularTrailInput` and `LocalizedTrailInput` subobjects and passes their
addresses. The localized position is a three-float structure with matching
`x`, `y`, and `z` members in both translation units; the helper's position
member was changed from an array to that compatible structure. The other
localized fields and their layouts remain the same. This removes the newly
introduced flat-descriptor view mismatch for this point caller; existing
helper callers still require their own typed-view audit. The existing
`func_151DBAA8` preset previously had an array member compatible with the old
helper view; changing only its position to the corresponding three-field
structure and adjusting its three assignments preserves the compatibility
with the revised helper. A full raw compile confirms all 62 functions,
constant pools, and diagnostics in that owner remain unchanged. The other
existing `func_15142180` caller uses a flat descriptor that already had a
different aggregate view before this experiment; it is not evidence that
arbitrary differently typed descriptors are valid.

The nested point's complete raw function and relocations equal the previous
flat candidate byte for byte, and all 64 raw owner functions agree between
those candidates. All 41 helper raw functions and their relocations also
remain unchanged. The nested point and helper each pass their independent
native checks at `-O0`, `-O2`, and `-O3`; the point again rejects all six
negative controls. A fresh actual-Make shadow build and strict whole-image
audit of the nested sources reproduce the results above: 6,051 fixed function
addresses, no other function body changes, and 189,088 protected bytes exact.
Guest and relocation results above apply to the nested candidate's identical
compiled payloads; they were not repeated against different instructions.

The nested point candidate SHA-256 is
`16f9e141e7c8c958d6a4a2a0daa6fcbb2511bb524bbffe86b5501dd79f1c8bd1`;
the nested helper candidate is
`53780bab36a07c1a33fb7b05e343e9b627257eae9567ae46eb516ebad338858f`.
The actual-Make rerun also included the compatible nested trail-preset
candidate, with its 62-function padded object unchanged section by section.
All candidates remain private and uncounted. Preserve the existing historical guard
rows and finish durable tests and production qualification before adoption.
