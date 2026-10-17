# Overlay Mode Defaults Direct Match

Date: 2026-10-17

Continue consumer **819f51b4**, tools **b44bad7**, after the uninstalled
renderer investigation in [Note 1479](1479-mirrored-texture-float-color-saturation-20261017.md).
Install the independent **func_15181E18** reset from the same owner.
All **50 words emit directly from C**, with no instruction guards, compiler
profile, Makefile or literal-pool change. The renderer remains open.

## Complete Recovered Routine

- Owner: `conker/src/game/generated_1AC2F0.c`.
- Original: `conker/asm/1AC2F0.s`.
- VA **0x15181E18..0x15181EE0**, ROM **0x1AF2C8..0x1AF390**.
- **50 words / 200 bytes**, no frame, no JAL; interface **void(s32 channel)**.
- Retain the address-based symbol and add a succinct mode-dependent reset
  comment. No unsupported gameplay name or return value is invented.

When the unsigned byte D_800BE616 is nonzero, clear exactly three RGB bytes,
set duration to 25, and clear progress, kind and active bytes. Otherwise enable
the channel, set its scale to 1.0f, zero both projected components, then read
D_800A72B4 and publish its float bits to D_800DDDD8. Keep that constant read
late: it follows the projected stores and changes under qualified aliases.
Its retail bits are **0xBB83126F**.

The other source's apparent s32 stores at byte offsets 0/1/2 are not adopted.
The original uses SB. D_800BE616/D_800DDE3C use byte declarations;
D_800A72B4 is a named float, not a baked approximation. The only original
caller is a dispatcher case at **0x1509DFF8** whose JAL delay explicitly sets
A0=0. The caller later sets V0=0; that is not a callee return-value contract.

All **22 HI16/LO16 bindings / 11 anchors** are pinned. Raw target SHA-256:
`9b171dacb65c9703a0b2b640833a752be493b5383d5f6e4b08a7bf08426a82e0`.
All **27 raw/padded owner neighbors** and the inherited 16-byte pool are
unchanged. The normal padder preserves the complete direct 50-word match.

## Qualification

All **nine final tests pass in 97.507s**:

- **320 three-way guest cases**, original/raw-C/padded-C, both stack phases,
  full-word indices, nonzero flag variants, exact memory/read-store order,
  all registers/private state and natural coverage of every original word.
- **640 native32 cases per O2/O0 profile**, full body and separately compiled
  typed caller, UBSan, complete 1,024-byte canaries, signed-zero/NaN/infinity
  constant bits, aligned live-constant and mixed-bank aliases. All eight
  effective controls exit 22, not a trap/signal. No LTO or fwrapv.
- Three independent original/C rebase pairs, all 11 anchors including signed
  low carries, all 50 words equal, **36 packet/state cases**. A constant alias
  to the projected output proves the late read observes the new zero.
- **30 three-way positively fired access-fault prefixes** across both branches
  and stack phases, retaining full modeled state. This is 90 fired instances,
  not portable-C or hardware CP0/FCSR acceptance.
- **32 original caller cases**, executing the actual four packet words and
  complete 50-word callee, preserving the channel-zero delay and caller's
  later zero return. Not the complete unrecovered dispatcher or gameplay.
- All 50 word corruptions, 23 binding controls, 16 pool-byte controls and all
  **158 protected input entries / 149 paths** fail closed.
- First complete linked image/source prediction, exact symbol permutation,
  all protected data and 30 effective successor/metadata corruption controls.

Native scope is valid channels 0..3 and the existing GNU32 union-storage/
fno-strict-aliasing convention for aligned aliases, not universal ISO C
effective-type proof. Invalid indices and overflow remain guest-only.
An initial native harness used unavailable stdint.h/libc under the project's
freestanding flags. The harness was corrected to existing SDK types and the
existing raw exit convention before qualification; production C did not change.

## First Whole Image

Before production edits, freeze the baseline owner/link script, reproduce
the entire baseline ELF and prelink the qualified candidate. The first coarse
prediction caught a four-symbol/string serialization change caused by newly
referencing the proper named constant. Reuse the existing exact-permutation
validator; do not exclude metadata or use canonical-symbol equality alone.

The group is D_800A72B4, D_80099014, D_80090128, D_8009E974, reordered
**[1,2,3,0]**. Every original definition field, contiguous symbol row and
contiguous string is checked. All names, values, bindings and sections remain
identical. The independently specified complete prediction is frozen before
installation and covers every byte, including this serialization.

The normal rebuilt ELF equals that prediction exactly:

- **170 target instruction bytes**, one function-size byte (12 to 200),
  **30 exact symbol/string bytes**, **201 total changed ELF bytes**.
- No other function body/address/extent change; no excluded metadata or data.
- Game data remains **189,088 bytes / 720 owners / zero differences**.
- Mirrored-texture slot, projection/clipping neighbors and literal pool are
  literally unchanged. Makefile, guard manifest, original assembly and caller
  source remain unchanged.

ELF SHA-256:
`1d600586b847f1c38aaf0c7a8f62bc8c3465542601c754447be48f6ecac41519`.
Owner SHA-256:
`f2bd090d216aa39c0a553b3cab3e1d8d18eb26263dc2620a4daf6ade8c045e14`.
Only those two exact successors are recognized by the predecessor adapter;
unknown current bytes and corrupted before/after fixtures remain rejected.

Seven affected mirrored-candidate/compiler checks also pass freshly in
**109.690s**, using the explicitly recognized predecessor context. This
does not claim the whole live owner/ELF is unchanged. Other old guest/native/
caller suites are prior unchanged evidence, not newly rerun broad suites.

## Progress And Bank

Fresh official matching: Game **2,948/4,828 (61.06%)**, total
**3,621/5,501 (65.82%)**, still different **1,880**, zero address drift.
Init **492/492** and Debugger **181/181** remain exact. Nominal conversion
rows are unchanged. Root README receives only its two changed aggregate rows.

Tools **e3da0c4** banks six new helpers/tests plus three exact-successor fixture
updates first. Nine exact task pairs / **18 ASCII/AST checks** pass across
both copies. Eleven shared padder tests pass per copy: active **0.029s +
0.021s**, mirror **0.029s + 0.019s**. Consumer tools-check passes. Full target
tests run in the consumer, not as a separately claimed standalone toolchain.

Mirror HEAD **ddbdd16b** is unchanged: preserve **1,028 unrelated initial
dirty-file hashes**, update only three verified exact-predecessor task files,
and add six files, for **1,037 dirty paths**. No mirror commit/reset or push.
No dependency/provider changes, extra agent, host build/launch or frozen
Release action. Existing duplicate Makefile recipe warnings remain.

Prepared-checkout checks, sequentially:

```sh
python3 -m tools.experiments.game_overlay_defaults
python3 -m unittest tools.tests.test_game_overlay_defaults -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Install the complete 50-word semantic reset directly from C.
- [x] Qualify widths, late constant/aliases, original caller and whole image.
- [x] Preserve all neighbors/data/guards and bank measured progress.
- [ ] Resume func_1517FB9C's still-open 633-word coordinate/rate lifetimes.
- [ ] Continue the wider Game/additional-source queue; retain deferred pulse,
  query/sequence, timing and natural gameplay boundaries without false credit.
