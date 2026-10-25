# Setup-Byte Defaults Direct C Match

Date: 2026-10-25

`func_1518E524` now replaces its zero-return placeholder with a complete
seven-pointer `void` initializer. All **45 words / 180 bytes**, frame 24 and
both `R_MIPS_26` bindings emit directly from C, with **zero new guards** and
no alignment tail. Only this function receives matching credit.

## Source And Interface

Owner: `generated_1BA1D0`, source `conker/src/game/generated_1BA1D0.c`, original
assembly `conker/asm/1BA1D0.s`. Retail VA `0x1518E524..0x1518E5D8`, VROM
`0x1BB9D4..0x1BBA88`. Keep the existing typed `s32 func_150ADA20(void)` provider.
The recovered arguments are kind, flags, red, green, blue, alpha and signed
halfword mode outputs. The adjacent palette initializer supports the RGBA names.

Reset flags to two before the first random draw, then OR bit zero from that
draw. A second independent draw chooses kind `0x13` or `0x14`. Finally write
black RGB, alpha `0xFF` and mode `0x301`, preserving the original output and
pointer-reload order under aliases and helper mutations. Collapsing the two
draws changes the RNG state and behavior. The two-case switch preserves all
45 words; an equivalent simple if screened at 41 words and 28 differences.
Two switch-default words at offsets 92/96 are unreachable after the one-bit
mask but remain exact. All 43 reachable target words are covered.

Both call bindings, offsets 28/60, refer to the same retained 18-word RNG
`func_150ADA20`, seed `D_800885B0`. No headers, neighboring interfaces,
optimization profiles or guard CSV change. All 60 raw/padded owner neighbors
and pools stay fixed. The ordinary owner uses the existing O2/g3 profile and
actual three-command Make recipe. Four inherited Warning 712 diagnostics and
the duplicate `generated_12D630` Make warning remain; this is not a warning-free
build.

## Actual Indirect Caller

The aligned complete ROM scan finds no direct JAL and one literal pointer to
the target, at VROM `0x2320E0`. Arbitrary computed calls are not excluded.
`D_8008D620` is a two-entry table: this function, then existing exact
`func_1518E5D8`. `D_8008D628` begins a separate table.

Original `func_1518D6E0` is 750 words. Its complete original image is assembled
and locked to retail; tests execute the actual bounded window
`0x1518DEA4..0x1518DF54`, stopping before the last address. The window performs
unsigned division/list selection, reads the owner's unsigned selector byte
at `+0x3F`, constructs all seven pointers and calls slot zero through the real
JALR at `0x1518DF14`. The continuation ignores the initializer's return value.

Output offsets from caller SP are `10C, AE, 11C, 11D, 11E, 11F, 10E`.
Reserved descriptor byte `10D` and bytes `110..11B` stay unchanged. The actual
factory submission to typed `func_1513D524` is observed with all nine ABI
arguments. The allocator/factory is a bounded provider. The caller's current
C stub and all its original raw/padded words remain unchanged and uncredited.
Executing this window does not establish full 750-word entry/return parity.

## Qualification

Both tools copies pass six fresh pre-install checks, zero errors/failures/
skips/reuses: primary **82.720 seconds**, older mirror **82.564 seconds**.
Both shared project-tools checks pass, 0.504 and 0.586 seconds respectively.

- 4,096 opaque-helper guest phases and 8,576 actual-RNG phases compare complete
  modeled GPR/FPR/HI/LO/RAM/events/calls for original and selected images. Cover
  independent low bits, signed/high returns, seed edges and seeds 0..4095,
  sixteen output/seed/table aliases, two stack phases and helper mutations.
  All reachable root words and all 18 actual RNG words execute.
- Native32 O0/O2/O3 each pass 6,336 cases, comparing all 256 backing bytes and
  both callback snapshots. The canonical union exposes declared byte, halfword
  and seed views; no cast-based seed/halfword storage is used. Trap UBSan
  profiles and six effective wrong-bit/flags/kind/missing-flag/tail-order/
  one-draw controls pass, with expected negative exit 23. Native harnesses
  alone use `-mstackrealign`; IDO and production flags remain unchanged.
- 288 original caller-window phases cover prior RNG returns 0/1/3/FFFFFFFF,
  list counts 1/2/4, unsigned modulo, actual indirect argument construction and
  factory continuation. This is bounded window evidence, not full caller proof.
- Nine independent GNU links verify both bindings and rebases; 54 rebased
  phases agree. Eight guest argument-home alias phases and 258 fired target
  access-fault prefixes agree in complete modeled state and delay context.
- All 45 raw-word corruptions, two binding corruptions, seven strict-image
  controls, six frozen-input mutations and the stale stub are rejected.

Guest instruction-order evidence is separate from portable C fault behavior,
native guest-alias/endian equivalence, FCSR/MMU/hardware or gameplay acceptance.

## Image, Production And Progress

The independent full-image prediction changes exactly **125 bytes**: 124 code
bytes and one target symbol-size byte, from 12 to 180. There are no serialization
permutations or metadata exclusions. Actual production Make exits zero and
reproduces that complete image. All 6,055 function addresses and the other
6,054 bodies stay fixed. All 720 protected Game-data owners / 189,088 bytes
remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Tools commit `6a4959782f8e077d9124bc3c603791a312bd0194` precedes the consumer
pin/source/docs. Each copy passes two fresh installed owner/image checks;
four unchanged semantic checks are explicitly reused only after the complete
input, module and qualified-artifact fingerprints match. Those four are not
reported as fresh. Native adoption verifies all **16,062 sealed inputs** before
and after copying outputs. Only target source, target object and linked ELF
differ from the sealed baseline. The guard CSV is byte-identical.

The recount uses the actual adopted Native ELF, streamed to the verified cache.
Total **3,800 / 5,505 (69.03%)**; Game **3,127 / 4,832 (64.71%)**;
Init **492 / 492**; Debugger **181 / 181**. Zero address drift, **1,705** still
different. The 75% threshold is 4,129 matches, **329 more**. Only
`func_1518E524` leaves the preceding mismatch queue. Adopted ELF SHA-256:
`7b702d9c46302addb442515e315637dc6ad9fee9d31331e24a7dafefaea1ba0d`.

## Corrections And Handoff

Two initial capture attempts rejected an owned new tools module and the root's
uppercase `M tools` status respectively. Neither created a snapshot or changed
production artifacts. The successful capture verified all 16,058 prior inputs,
normalized the preceding three adoption overrides and added four owned tools
files across the primary/mirror copies. The older mirror's **1,658** existing
dirty paths, status/content and HEAD remain preserved, plus two owned modules.
No mirror commit/reset/stash is performed.

The first focused run passed six primary checks but failed mirror setup before
running any tests because the loader used the wrong ROOT. Its carried primary
detail is not mirror evidence. The corrected standard loader imports each
actual copy with its own ROOT and fingerprints before/after. Both complete
suites were rerun fresh. A later declared-native-storage improvement changed
only the test fixture; the final six-check results above were rerun in both
copies. Earlier failing loader/native-private receipts remain separate from
accepted results. No recovered C/owner/image change was needed for these fixes.

Next ordinary placeholder: `func_1518F51C`, same owner, 45-word retail slot.
Its queue entry is not qualification. Keep existing-C `func_15014094` and
parser-missed `Gfx *func_1510D8C0` separate. No private screen receives credit.
Baseline consumer `d537b2840198bb56d2df29b09c9e40ebbe271153`, tools
`0fa6f1aec51450b411589c361acf9df1855a4640`. Local receipts:
`conker/build/game-setup-byte-defaults-match/`.

Use an owned incremental Graphify refresh for the eight changed C/Markdown
files, with its manifest explicitly directed into quarantine and subset pruning
disabled. Retain historical outside-scope rows without freshness/full-corpus
claims, audit every old node or unique relocation, then adopt the graph.
Extract the two new tools modules separately because the parent ignores tools.
The automatic commit hook is skipped only for this explicit owned refresh.

Claude calls: zero. No dependency/global configuration, host/editor/Release or
gameplay changes. Nothing is pushed. The wider 75% goal remains active.
