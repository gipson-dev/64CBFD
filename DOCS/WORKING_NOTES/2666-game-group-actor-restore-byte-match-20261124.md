# Group actor restoration byte match - 2026-11-24

`func_15022398` replaces its zero-return placeholder with the complete group
actor-restoration routine. Semantic C emits **100 words / frame 64**, with
**96 words already exact**. An independently checked permutation of one private
pointer home changes four memory offsets. All **100 retail words** and bindings
then match. The CSV protects all 100 source words: 96 identity rows, four actual
changes, no insertions or omissions. This is a guarded C match.

Production rises from **4,645 to 4,646 / 5,528 (84.04%)**, Game **3,973 / 4,855
(81.83%)**. Init stays 492/492 and Debugger 181/181. Address drift remains zero;
882 functions differ, with **53 more matches needed for 85%**.

## Complete routine and recovered interface

The original is `conker/asm/49D30.s:6298..6404`, VA `15022398..15022528`, ROM
`4F848..4F9D8`. The recovered interface is `void(s32 index, s32 group)`. The
original does not establish a meaningful return value on every path, and its
caller ignores V0. The former untyped s32 placeholder was 12 bytes; its new
function extent is 400 bytes. Shared headers and provider bodies remain fixed.

1. Read `D_800C35C8[group][index]` as an unsigned halfword; zero bypasses. Capture
   the address `&D_800C35F0[group]`, read its row pointer and 8-byte record[index],
   and require unsigned-halfword kind 2. Capture byte 2 identity before helpers.
2. Call `func_15083E0C(identity)` and reject exactly -1. Preserve the resulting
   key, captured identity and table-entry address across the actor lookup
   `func_1505EEF4(key)`.
3. For an existing actor, live byte 5 equal to 3 becomes 0 for the base table
   entry, or 4 for another entry. Compare the entry addresses, not the row
   pointers: two groups can share a row. If captured identity is 1, read the
   live actor word+0xF4 after the byte store and clear bits 0x2A with FFFFFFD5.
4. If no actor exists, compare the signed captured key with live unsigned byte
   `D_800D2100`. On key<count, load the live descriptor pointer `D_800D20FC`,
   select its 0x30-byte record[key], and call
   `func_15082A44(descriptor, key, 0, group, 0)`. Look up the same captured key
   again. If creation produced an actor, call
   `func_1505E650(actor,0,0.0f,0.0f,0.0f,0.0f,1)`, then
   `func_1502225C((s32)((u32)actor-(u32)D_800CC2D0)/0x32C,group)`.
   Preserve the actor pointer across the physics call, using original modular
   subtraction and signed division. Do not repeat the existing-actor branch.

Actual provider interfaces are checked against generated_AEB40.c:428
(`15083E0C(u8)`), game_83300.c:1218 (`1505EEF4(s32)` returning struct127*),
the constructor ABI examples in generated_C4DC0.c:26 and game_83300.c:1775/1805,
the seven-argument physics declaration in functions.h:1079, and the existing
`1502225C(s32,s32)` body in this owner. The identity lookup returns -1 or a
descriptor index; the actual actor lookup excludes reserved actor slot 25.
Opaque-provider tests include that allocated slot as a stronger interface probe;
they do not claim that the actual lookup selects it.

The old shared variables.h declaration for `D_800D20FC` uses a 0x10-byte
struct258. The actual identity lookup's local record and C4DC0 ABI example
establish the retail 0x30 stride. This recovery uses a locally named exact
0x30-byte opaque descriptor. It does not propagate the stale shared type or
change unrelated declarations. The original constructor placeholder and retained
physics ASM remain unchanged, with no helper matching credit.

The complete original direct caller `func_15022848` is **39 words / frame 40**,
VA `15022848..150228E4`, ROM `4FCF8..4FD94`. Enabled byte
`D_800C35EA[group]==1` selects its loop. It clears D_800C3638, calls the recovered
target and then 150222E0 for each index, reloads D_800C363A[group] after each pair,
and finally sets 3638=1. Its original complete instructions execute with the
target connected; the remaining helpers stay opaque.

## Source fit, actual profile and independent relation

The first draft emitted 100 words/frame72 with ten differences. Seven local/
control/inline forms, 23 declaration permutations, six pointer forms and six
record/type forms were screened. Removing the named record cursor and ordering
actor/key/identity/records recovers frame64 and leaves four offsets different.

Exploratory screens used ordinary O2/g3. The actual owner has its existing
`-Wo,-loopunroll,0` setting at Makefile:184. Final qualification reuses the
existing 49D30 compile helper with O2/g3/no-unroll/MIPS2/o32 for both selected
and frozen-before C. Target instructions agree with the screen, while the
corrected complete before-owner reproduces the frozen production object
literally. All **56 other raw and padded definitions**, bindings, pools and
diagnostic rows remain fixed. No compiler-profile or volatile change is made.

The four instructions at words 24/30/34/37 save/reload A2 at SP+0x28 in raw C,
versus SP+0x2C in retail. The normalizer pins every raw instruction and binding,
then changes only those four offsets. It does not read retail instructions as
an output template.

An independent instruction-isomorphism proof imports no projection. It checks
all 100 words/bindings, the exact 64-byte frame, every branch/delay word, absence
of any SP-derived pointer escape, and disjointness from every other stack access.
The complete literal CFG visits **84 states** and proves stores dominate both
reloads. Every provider's argument homes end below offset 28, leaving both
private words protected. Identical instructions therefore preserve equal
registers/public memory under this private-word permutation across arbitrary
compatible provider effects. An independent home move to offset 48 is accepted;
three structural corruptions are rejected. These structural checks are separate
from the effective semantic source controls below.

This relation concerns mapped public objects disjoint from the private frame
and compatible returning o32 providers. It does not claim raw physical private/
fault-state identity, provider private-frame/code-address reflection, transitive
provider implementation matching or gameplay acceptance. The target is void;
native/semantic checks do not assign meaning to its unspecified V0.

## Fresh qualification and production evidence

| Paired run | Elapsed | Gates |
| --- | ---: | --- |
| preinstall-primary | 159.932s | 5 fresh / 0 reused |
| preinstall-sibling | 127.692s | 5 fresh / 0 reused |
| installed-primary | 119.234s | 5 fresh / 0 reused |
| installed-sibling | 125.096s | 5 fresh / 0 reused |

- **764 cases per instruction stream** execute raw C, both padders and retail.
  All 100 original instructions are reached. Gates, signed key/count boundaries,
  every identity byte, group-entry identity, flags, existing/created actors,
  actor-slot arithmetic, public aliases and provider mutations are checked.
  Padded/retail executions agree in complete memory/register/access state.
- **86 fault-prefix triples** qualify emitted instruction order, without a
  portable-C fault claim. **12 complete original caller cases per stream**
  exercise empty/disabled paths and count shrink/growth, producing 25 target and
  25 post calls. All four streams agree, including the caller's saved roles.
- **648 SDK32 native cases at O0/O2/O3** pass with strict aliasing and UBSan,
  typed actor/record/descriptor backing, shared rows, pointer/endian codecs,
  public/guard byte comparisons and provider observations. The remaining 116
  mixed-type aliases or modular negative-descriptor-key cases stay guest-only.
  **14 semantic source controls** reach known comparison exits 10..13; no crash,
  signal, sanitizer trap or compiler failure is counted as a semantic rejection.
  A proposed divisor change 812->808 preserved all tested integral actor-slot
  quotients and was not counted. The final 748 control changes a real slot result
  and reaches the public-state comparison failure.
- **236 strict word/binding controls** cover all 100 source words and 18 binding
  sites through both target padders. **12 GNU links / 96 guest rebase runs** cover
  four independent code/callee/global layouts, preserving table/byte-count
  cohorts and exercising split HI/LO carry.
- Both complete owner padders produce identical text/definitions/bindings/pools
  and metadata. Actual Make replays **three production commands** and reproduces
  the complete padded owner. Frozen old C plus only original target ASM builds
  an independent reference; named definitions and string values are reconstructed,
  including target extent and 0 reordered
  symbol records. Prediction, actual C link and production Make agree literally:
  **311 changed ELF bytes / zero exclusions**. All **189,088
  protected Game bytes / 720 owners**, other bodies/addresses/extents, conversion
  rows, original ASM, layouts, headers and prior guards remain fixed.

```text
before ELF: d0df9542f35f293a85c5561fe2a946cfc039c8ad911224fabeb5f0fa8ba3de1b
after ELF:  a226cf8d22779b1474ff96d7b1d1969608496b24f2755623db11df6eb9effd30
owner:      e63c677a77e70bf2ee88ba06cf4012e37a85173d712c1080445e2aab28b613c9
```

The 100 guard rows append to the exact prior CSV bytes. Production Make holds only
the inherited guard-dependency timestamp old; the changed owner rebuilds and
reads the new guards. Unchanged prior receipts remain fingerprinted and are not
described as fresh tests. Shared tools checks pass.

Tools qualification commit `e452130c40e80803ff22c5014dea63b96010250a` and header-only commit
`02509097e50a38702e028ab7e8b955370ed09565` precede the consumer
source/guards/pin/docs commit. An isolated tools overlay preserves the dirty
real sibling. Host configurations are reverified as binary consumers without a
direct reference to this C owner; no host or Release build/change occurs.
Codex resolved the task locally with zero Claude model calls. Graph receipts
separate normal refresh, observed commit-hook completion and scoped AST merge
with all old IDs retained; this is not full-corpus re-extraction.

README changes only two aggregate rows. Five DOCS indexes receive one short
entry with all previous bytes retained. Continue the active 85% goal from this
banked checkpoint; renderer15197148 remains private on its older baseline.

The header-only commit corrects a copied matcher module docstring. Every later
source byte and the AST with that docstring removed are identical to the code
used by all four fresh runs. Those original receipts remain intact, with exact
qualified/current hashes and Git blobs recorded in comment-only-tool-repair.json.
All matching C, object, guard, image and semantic artifacts remain unchanged.
