# Embedded Owner Link Event Pair Guarded C Match

Date: 2026-10-22. Predecessor consumer `e588f42d`, tools `ee347ee`.
Qualification tools committed first as `41380d8`.

## Recovery

Recover both complete callbacks without changing their original assembly:

| Function | Source owner | VA range | ROM range | Words / frame |
| --- | --- | --- | --- | --- |
| `func_150CE694` | `generated_FB600.c` | `150CE694..150CE740` | `FBB44..FBBF0` | 43 / 24 |
| `func_150D6E60` | `generated_1028F0.c` | `150D6E60..150D6F0C` | `104310..1043BC` | 43 / 24 |

Each callback receives an owner pointer, word-sized event address and byte
command, with an unused void result. A private embedded link at owner +0x18
or +0xA8 holds a pointer and identity byte. Command 0x2D exchanges matching
before/after references, with the first match winning. Preserve pointer
capture before packet reads and late identity reads after the pointer store.
Command zero releases the owner if the first event pointer matches, or if
the embedded identity matches raw packet byte +4. That byte is deliberately
not the paired event's after-identity field: command zero uses an eight-byte
wire payload, while command 0x2D uses the twelve-byte pair view.

Use narrowly scoped `EmbeddedOwnerLink` and `OwnerLinkEvent` views, explicit
opaque bytes and purpose comments. Include `structs.h` for the existing
`func_1516972C(struct102 *)` helper contract, with an explicit owner cast.
Do not reinterpret the legacy global `struct102` fields for these subclasses.
No caller, shared-header, compiler-profile or original-assembly edits.

## Checked Normalization

These are guarded semantic C matches, not compiler-only matches. Derive four
expected-word rows per callback from a closed V1/A0 register-allocation cycle
within words 10 through 22 and commutative BNEL operands at words 12/20.
Word 12 maps back to the same bits, so it needs no row.

| Offset | Expected raw C | Retail |
| --- | --- | --- |
| `028` | `8C430000` | `8C440000` |
| `02C` | `8CA40000` | `8CA30000` |
| `050` | `54790013` | `57240013` |
| `058` | `AC440000` | `AC430000` |

Change only GPR fields. Keep opcodes, immediates, frame, extent and call
bindings unchanged; insert or remove no words. Both R_MIPS_26 bindings stay
at +0x94 to `func_1516972C`. Check complete raw hashes and bindings before
normalization, and retain the entire existing CSV byte prefix.

Raw text SHA-256, in table order:

- `57edf69ea16766717420246c52a6d1682e3562c8cbd61025b524f7e8f854545e`
- `5146553c4fe4c90b6eda4a36936cba8139b82cfe68d2e843972572bad852098e`

Qualified guard CSV SHA-256:
`efd301f9aecad2f3a36112f6f0c1a21040369cd60354fd34933ed5495a365f7e`.

## Actual Registration And Helpers

Retail scanning finds one literal pointer per target and no direct JALs.
Qualify the actual registered callers, not the unrelated `D_8008A390` table
or `func_15147D1C` dispatcher used during initial exploration:

- `func_15160090`, 18 words, uses `D_8008B0E4` at ROM `22FBA4`, three
  entries, target slot 2, selector byte owner +0x14. The target pointer is
  at ROM `22FBAC`; other entries are NULL and `func_151CB49C`.
- `func_15131C2C`, 22 words, uses `D_80089878` at ROM `22E338`, fourteen
  entries, target slot 8, selector byte owner +0x75 and enable bit 0x4000
  at owner +0x68. The target pointer is at ROM `22E358`.

Both original/current caller bodies remain exact and unchanged. Execute all
40 caller words, and compile the existing typed C callers in native checks.
Pin the actual data owners `22FB90.rodata.s` and `22E220.rodata.s`.
Other callback slots use bounded providers, not recovered implementations.
The larger `func_15169260` and `func_1516944C` broadcast dispatchers remain
unqualified production stubs and receive no matching credit.

Qualify all 56 original/current words of retained `func_1516972C` (28),
`func_151696DC` (20) and `func_15169804` (8). Preserve the signed count at
`D_800DD190`, cached positive count and matching owner-slot replacement in
`D_800DD198` with owner +8 successor. Preserve the owner type byte, 52-byte
`D_8008B4D0` entries, optional type callback and default
`func_15168B10(owner, 1)` release. Lower release/type callbacks remain bounded
providers; this does not recover the complete heap or gameplay workflow.

## Qualification

Each tools copy passes eight pre-install tests and two fresh installed
checks, without failures, errors or skips. Explicitly reuse six unchanged
behavioral checks only under exact source, raw/padded object, guard, helper
and complete linked-image identity. Shared tools checks pass in both copies.

- 10,840 guest phases cover commands, widths, ordered accesses and outcomes;
  480 additional alias phases cover guest-only overlapping data.
- 348,160 defined native32 cases per O0/O2/O3 build, with twelve effective
  wrong-C controls per target and optimization. Use typed disjoint objects;
  do not claim native64, private-home alias legality or invalid-input C.
- 1,240 actual registration/caller phases visit all 40 caller words;
  240 release/scan/default-chain phases visit all 56 helper words.
- Eighteen independent GNU links and 240 rebased phases verify original,
  raw and padded C at alternate entries/callee addresses.
- 1,732 fired root-access fault prefixes check complete guarded state,
  PC and delay identity. Forty-two reachable words per target execute;
  unreachable duplicate packet load word 19 is retained statically.
- Eighteen raw/binding negatives and nine strict-image controls reject
  corrupted or incorrectly normalized inputs. Old zero-return stubs fail
  effective behavioral cases.

Raw C public memory and traces pass; raw complete-GPR equality is not claimed.
Only guarded output claims literal full-state/fault equality with retail.
Sparse type-255, uncanonical argument homes, invalid addresses and overlapping
guest data qualify emitted guest behavior, not portable C object semantics.

The initial signed-byte helper test exposed a missing LB operation in the
test oracle. Add a test-local adapter using the existing search-oracle LB
implementation and instruction bookkeeping; rerun the complete suites,
including negative signed counts 128/255. Shared oracle code stays unchanged.
Native Graphify Python lacks generic build dependencies; run module-importing
qualification/install actions under the existing prepared WSL environment,
without modifying that Python environment. A failed cache precondition
promoted nothing; restore only the two owned disposable cached proposals to
their verified preimages before the successful build. Live sources stay
equal to the qualified proposals.

## Owner And Image

Preserve four FB600 neighbors and sixteen 1028F0 neighbors, raw/padded pools,
all addresses and extents. Actual five-command Make recipes per owner include
the normal assembly processor. Both actual outputs equal their separately
qualified padded objects byte for byte.

Independent linking and normal production Make agree on the complete image:
238 changed bytes, consisting of 236 code bytes and two symbol-size bytes.
No metadata exclusions. Each target size advances from 12 to 172 bytes in
its existing reserved slot. Preserve all other 6,053 bodies and all 6,055
addresses, including the two complete caller bodies and pinned tables.

ELF SHA-256:
`51782d54c37fc37e88620896f2ba218cd84bbed4d68837e20bb8cb9561a583e1`.
Owner object SHA-256, in table order:

- `c55cc38790f75ea10afa3fecf5db7e2d79d9e798ebfea3450ed6d4c0b1ac60f8`
- `be2e84078588aa4afcc1a7b34fe2e1c4b966b5698fd837a35843978b4b22f9f1`

All 720 protected Game-data owners / 189,088 bytes remain unchanged, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Seal and recheck 15,882 files and all 1,454 linker objects before and after
live adoption. Six manifest overrides cover only the two qualified sources,
two objects, guard CSV and ELF. Promote only generated objects, ELF, linker
script and progress CSV; the last two remain byte-identical. The guard
manifest changes only by its eight target rows. Treating its old prefix as
an old dependency during the bounded production Make is justified by that
explicit ownership proof, not by claiming the complete CSV unchanged.

Commit primary tools before the consumer. Preserve all 1,568 preexisting dirty
paths and the HEAD of the independent older tools mirror, adding only the
two identical target experiment/test files. No push.

## Handoff

Fresh standard matching against the adopted live ELF reports total
**3,748/5,505 (68.08%)**, Game **3,075/4,832 (63.64%)**, Init 492/492 and
Debugger 181/181 exact. Zero address drift; 1,757 different. The 75% target
is still 4,129 exact, requiring **381 more matches**. The refreshed queue has
1,626 placeholders, 122 semantic/other and nine unlocated definitions.
Next `func_150F088C` (43 words) is queued only, unmodified and uncredited;
retain the 862-word `func_1508CAD8` stub in the queue as well.

README changes only its Total/Game aggregate matching rows. Post-commit
Graphify worker completion and every-old-node retention checks remain private
receipts. Incremental retention is not a fresh full-corpus extraction; retain
the excluded-corpus and large-HTML caveats. Host Release, saves and
configuration remain untouched. The wider 75% goal remains active.
