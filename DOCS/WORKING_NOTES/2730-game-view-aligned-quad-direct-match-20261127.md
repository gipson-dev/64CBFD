# View-aligned quad direct C match - 2026-11-27

`func_15149D18` replaces its zero-return placeholder in
`conker/src/game/generated_176A00.c`. All **107 words /428 bytes**, all **seven
relocation positions** and the original **72-byte frame** emit directly from
semantic C. **Zero guards**, inserted/omitted instructions, alignment tail,
compiler-profile or Makefile changes. The entire guard CSV stays unchanged.
VA `0x15149D18..0x15149EC4`; ROM `0x1771C8..0x177374`.

Production: **4,709 /5,528 (85.18%) total**, **4,036 /4,855 (83.13%) Game**,
Init492/492, Debugger181/181, zero address drift,819 still different. One
matching credit; conversion rows and denominators stay unchanged. The active
**90% goal requires4,976 matches:267 more**. No parent/helper/host credit.

Recovered entry: `Vtx *func_15149D18(u8 *actor,s16 view)`. Names describe
inferred roles, not original identifiers. Existing16-byte `Vtx` supplies
coordinate, flag, UV and color fields. Owner width2C, height30, XYZ34/38/3C,
64-byte templateC0 and four cache pointers100 describe a272-byte prefix;
these offsets are hexadecimal. The production entry keeps its opaque byte
view rather than introducing a shared actor layout. Native fixtures allocate
the full typed prefix with real float/template/pointer subobjects.

Call `func_151D5D60(actor+100,view,64,&cursor,&fresh)` and separately capture
the returned output pointer for the final return. Null returns immediately.
Fresh buffers copy the64-byte template into both pages, reloading the cache
pointer after the first copy. Preserve the two calls even when their source
is the same. The full cache allocation is128 bytes, not merely one vertex page.
After copies, cache width once and calculate forward from D800DD1D8[view]
and side from D800DD1E8[view]. Retain the original emitted multiply operands.

Coordinate truncation/narrowing and stores occur in this order:

| First / second stores | Value before signed32 truncation and signed16 narrowing |
| --- | --- |
| vertex3.x / vertex0.x | x + side |
| vertex1.y / vertex0.y | y |
| vertex3.z / vertex0.z | z - forward |
| vertex2.x / vertex1.x | x - side |
| vertex3.y / vertex2.y | y + height |
| vertex2.z / vertex1.z | z + forward |

Flags, UV and color bytes remain from the retained template or prior buffer.
The originally captured pointer is returned even when an opaque copy provider
redirects the live cursor. The frame saves S0/RA at20/24; freshness37,
captured first40, cursor44 and signed view home4C are literal. No dummy local,
gratuitous volatile, padding object, physical-register binding or added address
escape is used. All35 other raw/padded functions and pools stay fixed in this
36-definition owner:35 C definitions and one retained GLOBAL_ASM.

The initial complete semantic source already emitted107/frame72 with seven
aligned bindings and four word differences. Reversing three source expressions
(both coefficient products and the upper-Y addition) recovers IDO's original
FP operand and load placement. The final compiler output has every original
COP1, load/store, branch and private-stack word literally identical; no binary
FP commutative rewrite or scheduling normalizer is installed.
Complete selected source SHA256:`7fcb3f961bfb1ff0979e06ccd823eb7e0e222e96938fb050c13e72d51dcc81d2`.
Complete padded owner SHA256:`f965280c7dd0ad338300008228ea752bb6ce5e6fd70e3eaaec24606b7abe182f`.

The aligned retail census finds one pointer atROM22E904/VA80089E44, row10
of the39-entry D80089E1C table (156 bytes, baseROM22E8DC). It finds no aligned
plain J/JAL pattern naming the leaf; derived/script/compressed references are
not thereby excluded. The complete table matches retail and the frozen ELF.
Original dispatcher1513DB00 passes owner and narrowed signed view through
JALR1513DC24, then consumes the pointer at1513DC30 to free or skip on null.
**Production dispatcher1513DB00 remains its12-byte zero-return stub**;
its exact opening is00001025,03E00008,00000000. Its original295-word body is
qualified separately; this change gives no dispatcher restoration credit.
Original52-word cache helper and11-word memcpy match retail/frozen ELF.

Validation:

- Both complete padders reconstruct frozen BEFORE and emit identical AFTER.
  All35 neighbors/addresses/extents and raw/padded pools remain fixed. Actual
  Make replays five commands, including real GLOBAL_ASM preprocessing and
  postprocessing. One pre-existing Warning712 at `func_1514BF50(arg0)` remains;
  its line moves, but code/text/statement agree. Zero new diagnostics.
- Guest:1,008 cases per five literal streams;all107 words execute and494
  full memory/GPR/FPR/FCSR/HI-LO/access/PC fault quintuples agree. Independent
  ordered-FP/public-memory/calls/pointer-return reference agrees under four
  rounding modes, fresh/null, template/pointer/width/cursor/return-home changes
  and bounded aliases. Six effective instruction controls are rejected.
  Actual52-word cache helper and11-word memcpy run together and separately;
  allocation stays opaque. Private-home redirects, sparse signed views and
  aliases are guest-only evidence, not portable C or N64 hardware acceptance.
- Native32:actual recovered C in three TUs,8,192 cases at each O0/O2/O3.
  Typed272-byte prefix/16-byte Vtx/all offsets, two320-byte buffer arenas,
  canaries, coefficient arrays, provider metadata, returned pointer and MXCSR
  agree. Four rounding modes, strict aliasing/FP, undefined/float-cast UBSan
  traps and LTO type checks pass. All float-to-s32 conversions stay in range;
  negative signed views use only null native paths. Nine defined controls
  exit42 through comparison, including live-cursor return and retained flags;
  no compiler error, trap or signal is counted as a successful control.
- Complete original parent:306 cases/stream,144 connected children/stream,
  all293 reachable words out of295;duplicate defaults115/146 are unreachable.
  Both literal leaf streams agree on full private state. An independent leaf
  provider counterpart agrees on public state, calls, ordered FP/FCSR and
  return; its private stack is not equated. Two return poisons change complete
  parent behavior. Render services and free remain opaque, and the production
  parent remains its pinned stub.
- Both scoped padders expose214 word and14 binding corruptions. Twenty GNU
  links and100 guest rebases independently move both helper and coefficient
  symbols through four jump regions and aligned signed HI16/LO16 carries.
  Generic oversize remains visibly overflowing; generated oversize rejects.
- Independent frozen-before-C plus original-ASM prediction equals actual
  private recipe link and production ELF byte-for-byte:308 changed bytes,
  zero exclusions or metadata permutations. Protected189,088 data bytes
  across720 owners and all other functions stay fixed. Fresh recount agrees.

| Phase | Seconds | Coverage |
| --- | ---: | --- |
| preinstall-primary | 114.626 s | 5 fresh / 0 reused |
| preinstall-sibling | 143.717 s | 5 fresh / 0 reused |
| installed-primary | 179.919 s | 5 fresh / 0 reused |
| installed-sibling | 190.807 s | 5 fresh / 0 reused |

All20 passing target tests are fresh. Primary/isolated sibling task/import/
data/artifact fingerprints agree; asm processing uses each copy's own tools.
The first packaged attempt exposed two missing report returns and a mistaken
stub instruction-order assertion; its failed receipts/task bytes are retained
under `failed-package-1`. Revision2 changes only those three harness adapters;
the recovered source/object never changes. Shared tools-check passes; unchanged
broad suites are not reported fresh. Frozen inputs:4145;
copies:3097. The separately dirty real tools sibling is
preserved. Tools commit:`3325c59ad3b2824b3dbde11044bd4986975a9fc4`.
Baseline consumer:`2fbef9fda93c41a53c7a81ef1bf61b7a9c8860fa`.
Production ELF SHA256:`3a9ab6167ec702bfccc7135fd09924ed156c1fcdf537c706acb0ff3ad8db9363`.
Receipts:`conker/build/game-view-quad-15149d18-private`.

Zero Claude calls and no subagents; local evidence resolves this routine.
The host's generated target is an empty stub; active host applicability stays
unqualified, with no host transfer/build/launch or Release change. Scoped
Graphify refresh audits35 current C definitions, retains all old IDs and
qualification metadata, and observes actual commit-hook termination before
publication. No full-corpus re-extraction claim. README receives aggregate
rows/date only. Continue from sealed N75 toward the active90% goal.
