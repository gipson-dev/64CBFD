# Pickup Update Private Homes And Selector Cursor

Date: 2026-10-19. Consumer predecessor: `76df4404`; tools predecessor:
`e707d3e`. Tools checkpoint **9c3c005** is committed first. No push.
This continues the complete `func_1508DC24` reconstruction from
[Note 1626](1626-player-item-and-pickup-update-reconstruction-20261019.md).
The wider Game goal remains active; the previous and current turns make progress.

## Result And Boundary

The complete semantic C now emits **all 17 targeted private homes directly**,
preserves the cached selector base separately from its live cursor, and caches
the incremented signed selector without a second public read. All **468 final
public/private memories and final FPR vectors** agree literally with retail.
This is **not** whole-machine equivalence or an installed match: final GPR
vectors still differ in every one of those 468 phases.

Selected output remains **680 words/frame 280**, one word short of the original
**681 words/frame 280**, VA **1508DC24..1508E6C8**, ROM **BB0D4..BBB78**.
Counted differences improve **665 to 636**, comprising **635 overlapped words
and one missing word**. The original name, no-argument void interface and
complete purpose-commented C are preserved. Production still contains its
12-byte placeholder. No installation, word guards, padding or match credit.

## Direct C Homes

The [lifetime experiment](../../tools/experiments/game_pickup_state_update_lifetimes.py)
reorders only existing real scalar declarations. It adds no dummy storage or
new locals. One real scalar precedes `player`, seven precede coordinates,
three precede the owner pointer and the real mode local precedes `kinds`.

| Value | Original And Recovered SP Offset |
| --- | --- |
| Player counter | 110 |
| Coordinate outputs x/y/z | F0 / EC / E8 |
| Owners / selectors / held / overrides / timers | D8 / D4 / D0 / CC / C8 |
| Kinds / flags / fixed targets / grace | C0 / BC / B8 / B4 |
| Saved x/y/z | B0 / AC / A8 |
| Attached-effect list | 80 |

The intermediate `DIRECT_HOMES` body has 680 words/652 differences. Its only
changes from the prior byte-cursor object are **60 SP-relative displacement
fields**, covering exactly these 17 slots. Opcodes, register fields, branch
fields and all **77 original C-object bindings** are unchanged at this step.
This intermediate is retained as a control, not mistaken for final `SELECTED`.

**34 fired guest home aliases**, both stack phases, validate every named home.
Each finishes and produces different observations with the old layout. These
are physical guest probes, not portable-C stack alias semantics.

## Cursor And Selector Captures

With homes fixed, a complete-memory diagnostic found **208 of 468** final
memories still differed at the cached selector slot. C advanced `selectors`
and wrote that cursor back to SP+D4. Retail loads the base once for its second
pass and advances a register, leaving the home unchanged.

Reuse the existing `scan` local as the actual advancing byte cursor. The
cached `selectors` value remains independent. **Two fired OBJECT-call aliases**
redirect SP+D4 and alter an alternate record: retail and selected C retain
the live cursor; the direct-home-only predecessor reads the modified home and
processes the wrong second record. Both old controls finish and differ.

The literal B9 skip/else shape is restored without advancing a skipped player's
cached count. The cursor/skip form briefly caused an extra ordinary read of
`D_80087340` in every fixture. Explicitly capture `(s8)(D_80087340 + 1)` in
an existing real scalar, store it, then compare that same signed value.
The extra read disappears; an effective uncached control still performs two
selector reads instead of one. Equal length/difference counts alone did not
distinguish these two sources, so retain their fingerprints and read gate.

## Fresh Qualification

[Eighteen tests](../../tools/tests/test_game_pickup_state_update_lifetimes.py)
pass in each copy, zero skips/errors/failures. Final elapsed harness times:
**40.130s primary**, **40.756s standalone mirror**.

- The complete 234-case corpus passes both compiled profiles and stack phases:
  **936 candidate fixture/profile/phases**, all **681 retail words visited**.
  Ordered public reads/writes, canonical helper calls and complete public
  state agree. Ordered-read equality is now a hard test assertion, not merely
  a diagnostic count. Both profiles emit identical selected target bytes.
- Across **468 additional phases**, complete final memory and all 32 modeled
  FPR words match literally. The GPR result is explicitly **0/468 equal**;
  do not claim full register, intermediate or instruction-fault parity.
- Retain the 34 home aliases and two live-cursor aliases with effective old
  controls, plus the signed-selector extra-read control.
- **Eight bounded connected phases** execute the actual original 35-word
  `func_15086CBC`, not a provider replacement: node 0 versus word 255, fixed
  versus random placement, both stack phases. Valid coordinates and the
  rejected-node seeded-RAM results agree. Four old-home negatives differ.
  Both old and new coordinate homes are seeded with finite values so the
  control stays inside the existing conversion model; no FCSR behavior is
  invented to interpret uninitialized arbitrary floats.
- Retain **234 native32 fixtures at O0/O2/O3 with trap UBSan**, six effective
  compiled semantic negatives and the installed placeholder negative. The
  rejected-node seeded-stack cases are guest-only, not native C assertions.
- Both full raw owner profiles keep all **72 other function bodies and pools**.
  Both project-tools checks pass; two new task files agree byte-for-byte
  between copies and all four Python copies parse. All seven production
  fingerprints remain unchanged.

The original assembly is also assembled independently with GNU and linked:
its complete **2,724-byte slot matches the ROM**. Its **77 relocation entries**
are not identical to the selected C object's **73 entries**. Exact multisets:

| Present More Often In | Symbol | Extra HI16 / LO16 |
| --- | --- | --- |
| Original | D_800D23B0 | 1 / 1 |
| Original | D_80087340 | 2 / 2 |
| Original | D_800BE9E4 | 1 / 1 |
| Selected C | D_800CC2D0 | 2 / 2 |

The four-entry net difference is **eight original-extra and four C-extra
entries**, not simply four missing relocations. Independent rebases of the
eventual complete layout remain open; one normal-address original assembly
link is not that broader gate.

## Preservation And Receipts

```text
Selected semantic C: 92dae131dcb3342086aa66da7dfd07391fd350e29ca2dddbdcc31fbb47187fae
Selected raw target: aa2d148b4b51b725d32722cd832571aad2822a9bc68f16a97116b93a3a411f82
Direct-home control: 209ecb6dd904bcbfae6d743f96dc4bf2cbc2d9260451986d63cfa88547468e31
Uncached selector:   3a20dead90c81a5e0f02632008af84b15f8e3b5ee5f9279f74dc8ecfd758a9bd
Installed ELF:      40623350a4c531d2ef27a110ca30ea329b22e11c1dba97d8554907a674a20132
```

Ignored artifact root: `conker/build/game-pickup-state-update/lifetimes/`.
Keep final primary/mirror logs/run JSON, both `test-receipt.json` files,
direct displacement proof, home/cursor aliases, literal final states,
connected coordinate phases, independent original object/link and binding
boundary, native/negative fixtures, selected fingerprints and production,
mirror and graph audits. Earlier failed/diagnostic receipts are historical,
not substitutes for these final successful runs.

Thirteen prefix partitions plus the selected declaration partition, eight
logical-role screens, nine skip forms, six constant/hint forms and eleven
cursor forms were measured. Unselected constant/hint forms folded to the same
code; do not claim recovered original register hints. These screens are not
additional qualified matches or permission to pad a nearly sized function.

All **1,464 existing dirty mirror leaf hashes/statuses** and HEAD `ddbdd16b`
are preserved. Only the two absent task files were added: **1,466 dirty paths**.
No mirror commit/reset/clean/stash, host/frozen Release, save/configuration,
compiler/dependency change, push or advisory call. Root README and installed
totals remain unchanged because the seven production inputs, including the
ELF, are identical; no fresh production build/recount is claimed.

## Continue Here

Continue this same `SELECTED`, not another function. Recover the remaining
one-word extent difference, lifetime-scoped GPR allocation, original address-
materialization/relocation multiplicities, instruction/branch-delay schedule
and own-access intermediate state. Preserve the 17 direct homes, cached/live
selector distinction, all ordered public reads and 468 complete final memories.
Any normalization needs explicit semantic C origins, stale-input controls,
independent GNU code/data rebases, actual Make/padding selection and a strict
first linked-image audit before installation and fresh recount. Hardware
FCSR/MMU, unrestricted provider/capacity behavior and gameplay remain separate.
