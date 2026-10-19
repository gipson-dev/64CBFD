# Mode Context Initializer Complete Match

Date: 2026-10-19

## Scope And Predecessor

Recover `func_15089BC0`, owner `generated_B3020`, after
[Note1603](1603-barrier-crossing-complete-match-20261019.md).
Retail is247 words/988 bytes, frame40, VA15089BC0..15089F9C,
ROM B7070..B744C. The previous production body was a12-byte zero-return stub.
Keep the original address-based name and add a concise behavioral comment;
the exact higher-level subsystem name is not established here.

Consumer predecessor2bec3691, tools predecessor3923525. Neither primary
checkout had pre-existing changes. Tools **23cce29** is committed before
the consumer pin. No push, sibling host, frozen Release,
save, dependency, REA setup or Claude operation is involved. Zero advisory
calls suffice because source, compiler, literal instruction and link evidence
settle the recovery directly.

## Recovered Contract

Capture the full-word `D_800D2E48` before the asset-payload lookup. A NULL
lookup returns0 without clearing context, retaining any lookup effects.
A non-NULL unsupported key clears `D_800D23B0` and returns0. Supported keys
are B7,B8,B9,BA,BB,BD,BE; BC is deliberately default. Preserve the seven
separate switch assignment blocks and their physical source order.

Publish the selected payload and call void `func_1508BC20` first. Preserve
fresh context loads after every store and fresh signed-byte `D_800E0BD0`
reads at each table use. Zero flags1700,1701,1703,1702,1704 in that precise
order; store the original cached key at16BC, the selected threshold at16B8,
and zero1745. For sixteen four-byte rows, clear16C0, seed1868 from the live
float table, then clear17A8,17E8,1828. Finish with the sign-extended byte-table
parameter at context+C. Return0 on every path.

The semantic key/data/offset declarations initially emitted247 words/frame32.
Declaring data, offset, key before their real assignments recovers frame40,
RA at SP14 and the cached key at SP1C without dummy storage, volatile,
register bindings, instruction-layout guards or frame repair. The selected
normal O2/g3 owner body has only two local switch-table address differences.
The primary no-unroll profile emits133 words/frame40 and is not selected.

## Switch Binding And Owner Isolation

Select this function alone as the third normal-object override beside
`func_150891E8` and `func_1508BC20`. Keep every other function's primary flags.
The actual seven-command Make shadow reproduces raw payloads, all73 primary
functions, padded code and metadata. All72 padded neighbors and their
extents, plus all73 addresses, remain fixed. Both raw profiles preserve70 neighbors
literally; the other two change only their local-rodata LO addends.

The compiler adds one32-byte switch table at owner-rodata+8, expanding496
to528 bytes. Removing just that interval recovers every previous pool byte
and relocation owner. All eight table targets match the original retained
`jtbl_8009DA24_game` at ROM2424E4. Two appended binding rows at+38/+40
select that retained table; **zero instruction-layout guards** are needed.

The manifest is not an unchanged historical prefix: exactly two old
`expected` cells are requalified for the added32-byte pool interval:
`func_1508E6D0+18`:8C2E0008->8C2E0028 and
`func_1508E780+2C`:8C380104->8C380124. Their replacement instructions,
binding identities and every other historical cell/byte remain unchanged.
Fresh newly padded neighbor regression pairs cover1,805 and16,245 cases.

```text
Isolated raw: 75900d393e6234dc3f400483d56b7b91df70214d6d1ab8d83ce58887efca14b4
Owner raw:    e05a7607e0fd3662ccca72fdd1296e1ac7704764c9ccffa23f09243b7db6a8ff
```

## Qualification Boundary

The pre-install nine-test run passed in20.134s:

- 312 fixtures/624 literal retail/source pairs across two stack phases,
  all256 signed selector patterns, five complete live-mode aliases and
  all247 retail words visited. Compare complete public buffers, ordered
  stores, calls, private RAM/register state and saved ABI lifetime.
- 1,362 fired private access-cut pairs agree literally. A flag-order negative
  has identical final public state but differs at fired cut14.
- Native32 O0/O2/O3 with UBSan and nine effective semantic negatives cover
  missing lookup, BC rejection, cached key, live/signed selectors, signed
  byte output, full loop, row seeds and helper order.
- 24 connected runs execute the actual15-word lookup wrapper and189-word
  cyclic-weight body, with counts0/2 and an opaque RNG returning0.25.
  This is not full lookup/RNG/gameplay acceptance. The prior count16/
  inclusive-one scratch caveat from Note1601 is not newly qualified here.
- 16 returning-caller runs use the genuine JAL/NOP/branch/RA-load prefix at
  1509E084..1509E090 and shared return tail1509E3CC..1509E3D8. This is not a
  complete command-dispatcher claim.
- Three independent GNU link maps/27 rebased pairs compare original assembly
  and raw C, all247 code words and all eight table entries, including HI/LO
  carries. No literal normalized-code substitute supplies the retail side.
- 279 raw/binding stale controls, two actual-padder stale-manifest controls
  and four strict whole-image corruption controls reject changes.

Signed out-of-range selector probes use explicit guest/native backing,
not claims about actual retail C-array bounds. Native table views preserve
big-endian ROM values on the little-endian host; overlapping float/byte
table cross-view aliases are not claimed. The live selector/byte-buffer
alias is real and separately covered. No target floating arithmetic is
invented; table-bit loads/stores remain unchanged.

## Production Audit

The production rebuild passes and reproduces the independent first link
byte-for-byte: **769 changed bytes,767 target-code bytes and two target
symbol-size bytes**. Only this function's st_size advances12->988. No
symbol-order, string-table or other metadata changes, section exclusions
or wholesale literal-code transplant are accepted. All6,056 other bodies
and their extents, and all6,057 addresses, remain fixed. Protected Game
data remains189,088 exact bytes/720 owners, zero differences. The broad
shared-manifest rebuild retains inherited unrelated generated-code warnings
and the duplicate generated_12D630 Make recipe warning; the qualified
target/owner compiler diagnostics are empty.

All **ten installed tests pass in30.605s**, no skips, including the final
strict installed-image/data audit and complete988-byte target comparison.
Shared `make tools-check`, whitespace and syntax checks in both tools
copies pass. Only the five absent task files were copied to the standalone
mirror. Its HEAD ddbdd16 and all1,399 pre-existing dirty leaf hashes remain
fixed; no mirror commit/reset/stash/clean. Old unchanged owner tests are
not called fresh runs; the two affected switch neighbors are freshly
executed from their newly padded objects as described above.

```text
Source: 630d6cbaa567addbb094dce43b81277ece9b1dfb2865196038af637a691b7845
Make:   cf6de057267055cf5ad789e72426b7433c0bfe37d04ae56c241332cf2f2febf4
Guards: 9aefde5eabf696da27221d6daa912245766d5e9781563b9abadf39d7560733a1
ELF:    e8b1afc1b2bfd45d1bd516e86fd61c4480b673c8a6cde72bae792962ba3dacf4
CSV:    16798cbd1f7d69f7ecdd8b7e0071ba9ea975a50652bd8797673d1ec2b500c9be
```

Fresh matching: **Game3013/4832 (62.36%)**, **total3686/5505 (66.96%)**,
**1,819 different/zero address drift**. Init492/492 and Debugger181/181 stay
exact. Owner **65/73 exact, eight remaining**. Conversion stays5505/6044
(91.08%) and86.08% bytes; its CSV is byte-identical. Root README changes
only the two matching aggregate rows; function narratives remain in docs.

The unchanged nonmatching `func_1508B3F8` has282 raw word differences but281
classified instruction differences, in both predecessor and installed ELFs.
The older inventory used the raw count; the fresh inventory uses the shared
classifier. This diagnostic distinction is not additional matching progress.

## Resume

Next: **func_1508C1A4**,261 words/1,044 bytes, retail frame168,
VA1508C1A4..1508C5B8, ROM B9654..B9A68, currently a12-byte C stub with252
differing words. Freeze this installed baseline, then inspect its complete
retail routine and direct callers before another qualified conversion.
The tied261-word `func_1508C5B8` follows separately; keep the wider Game
goal active. The complete eight-entry owner inventory is retained in
`integration/remaining-owner.json` below the ignored evidence directory.

## Reproduction

```sh
python3 -m unittest tools.tests.test_game_mode_context_init_match -v
python3 -m tools.experiments.game_mode_context_init_integration --audit
python3 -m tools.match_progress conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
make tools-check
```

Ignored candidates, frozen inputs, literal/native/helper/caller/GNU receipts,
Make shadow, independent first link, build/audit and graph evidence belong
under `conker/build/game-mode-context-init/`.
