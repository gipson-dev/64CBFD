# Phase-driven curve emitter recovery and byte match - 2026-11-16

`func_151A11E4` now has a complete typed C recovery and matches all **350
retail words / frame 0x110**, VA `0x151A11E4..0x151A175C`, ROM
`0x1CE694..0x1CEC0C`. The zero-return placeholder is replaced by the actual
phase-driven particle emitter, including its 17-short motion/intensity curve.

The fresh production count is **4,516 / 5,514 (81.90%)**, Game
**3,843 / 4,841 (79.38%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift, 998 different. This is **one new match**; the active 85%
goal needs **171** more at the current denominator. Conversion remains
5,514 / 6,048 (91.17%), covering 86.19% of function bytes.

## Recovered behavior and interface

The callback receives `struct260 *` through `D_8008A4E8[2]`, actual pointer
VA `0x8008A4F0` / ROM `0x22EFB0`, under `func_15149264`. It advances the
32-byte payload's phase by emission rate times `D_800BE9A4`, then emits while
the phase exceeds 1. Each emission preserves the original provider sequence:
two integer angle samples, four trigonometric samples, one real sample, four
further integer samples, packet submission and an optional curve copy.

The typed 56-byte packet preserves all ten unwritten byte positions. Its
random flags accumulate across emissions. The target coordinates are captured
before subsequent providers can change the record; the live coordinates,
short ranges/bases, mode and owner are reloaded at their original boundaries.
Two unsigned remainder operations and five signed divisions construct the
17-short curve. The nullable helper return controls the complete 34-byte copy
to `result+0x50`, then the live phase is reloaded and decremented.

The shared 32-byte record payload types are lifted before the callback without
changing the neighboring factory's meaning. The public signature is
`void func_151A11E4(struct260 *record)`, matching the real parent interface.
The preceding [Note 2492](2492-game-packet-allocator-nullable-return-and-direct-match-20261115.md)
restored the packet helper's pointer return needed by this routine.

## Source shape and normalization

Recovered C emits **344 words / frame 0x110**, raw SHA-256
`9add47659e4f249bfd0a9f084b1ae2ebed574e1466102bcd3896cb1b72293988`.
Using the real early half-lifetime curve cell recovers its store/reload.
Declaration order recovers both cached-coordinate homes, SP+0x8C and SP+0x90,
without memory-operand patches. Packet SP+0xD4 and curve SP+0xB0, their exposed
absolute addresses, and all 17 opening frame/save words agree with retail.
Comments explain the target capture and reuse of dead basis components for
velocity, keeping the source semantic rather than encoding assembly words.

The normalization retains every compiled operation exactly once and adds six
redundant operations: four GPR copies, one FP copy and a repeated literal LUI.
All **39 FP operations retain their value operands, order and FCSR evolution**.
The operation projection permits register allocation and branch scheduling,
preserves literal/memory offsets and relocation identities, distinguishes
zero/SP/RA roles, and is separate from the independent instruction proof.

The table adds **344 expected-word guards / six insertions / zero omissions**.
CSV rows are sequential output carriers for the proved permutation; two
carrier insertion locations differ from the six logical-copy locations. An
inserted carrier can therefore hold a retained source operation. The source
operation inventory and independent relation, not the CSV carrier position,
establish provenance. Both complete owner padders produce the exact slot and
preserve all 38 neighbors and pools.

## Independent qualification

Eight maintained task files use the `game_curve_emitter_151a11e4` prefix under
`tools/experiments` and `tools/tests`. From the prepared consumer root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tools.tests.test_game_curve_emitter_151a11e4_recovery -v
```

Five tests pass freshly before installation, through the isolated sibling
tools overlay, and after installation at identical eight-file fingerprints.
Actual imported helper paths and digests are retained for each configuration.
The final runs take 233.498s, 176.538s and 171.465s respectively.

- The independent symbolic relation covers two entry/exit paths and **512
  inductive loop paths**, arbitrary public aliases, fresh public memory epochs
  after writes/providers, opaque caller-saved/FCSR/HI/LO effects, mutations of
  previously exposed packet/curve ranges, saved roles and return custody.
  The complete private frame is compared at every provider and at loop/return
  boundaries, including incidental integer result registers on return.
- All **332 raw / 338 retail normal instructions** are covered. Only twelve
  BREAK words per stream lie outside the explicit nonzero/nonoverflow normal
  division domain. All 350 words, including those BREAKs, are present in the
  exact installed slot. No image bytes are excluded. This proof is not a
  portable-C undefined-input, raw fault-register, hardware or gameplay claim.
- A T0/T1 scratch-allocation positive passes. Valid corruptions of an unwritten
  private gap, mode offset, curve cell and FP operand order fail semantically;
  unsupported instructions or unbounded execution do not count as controls.
- The independent finite model checks **1,920 cases per stream** across retail,
  raw and padded code, with exact exposed homes, allocation failure/success,
  repeated emission, late field mutations and persistent escaped flags.
- Native32 C passes O0/O2, **1,920 cases per selected run**, with UB and
  float-cast traps. Persistent-flag reset, short curve copy and wrong-position
  controls fail effectively. Native checks compare defined packet fields and
  curves; uninitialized padding is qualified by the guest/frame checks.
- The actual **45-word parent** passes **256 cases per stream** across all
  three streams, visiting every parent word and all eight update/expiry/free
  combinations. Timer and slot reloads after the callback, signed timer wrap,
  expiry rescue and the second expiry/free decision are covered.
- Both owner padders, three independent symbol sets (including HI/LO carry
  boundaries and moved providers), **363 raw-word/binding controls** and eight
  real stale-CSV controls pass. The rebased instruction relations also pass.

Ordinary nonfaulting public reads can commute inside a quiet memory epoch;
FP/FCSR, writes and calls remain ordered. Providers cannot inspect implementation
PCs or unpassed private locals. These assumptions are explicit in the checker.
No unchanged broad neighbor semantic suite is called fresh: prior unchanged
body receipts are reused with fresh owner, padding and full-image audits.

## Production and frozen evidence

A new **1,235-input** baseline records consumer
`67b66157bebdf9177f3da6a7d43c74479813abfc` and tools
`8cf2fee0d3ccfe0f52fc88815e93046e0a563c7f`, including the imported transitive
helpers. The earlier 895-input baseline and return-ABI adoption overlay remain
immutable. Only four new baseline inputs change: source, guard table, the
single owner object and the ELF; **1,231 inputs remain unchanged**.

Five actual Make recipe commands in an independent shadow predict the complete
ELF. Production Make rebuilds from installed source/guards without copying a
prebuilt object. The shared guard file is treated as old for dependency
scheduling only; the affected recipe reads the new table, whose previous bytes
are preserved exactly. The existing duplicate recipe warnings for
`generated_12D630` are unchanged; this owner introduces no diagnostic.

Production equals the independent image prediction across **1,082 changed
bytes / zero exclusions**, including the target extent change from 12 to
1,400 bytes and one closed four-name GNU symbol/string permutation. All
**6,050 other bodies**, all addresses and **697 other objects** are fixed.
All 698 objects are audited. The 189,088 protected bytes stay exact with SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production ELF SHA-256:
`f132be7cecc593a2c546342fc3513186959f9b277284575c9a85ad1785a25d0c`.

Preparation, suite/import fingerprints, the literal image prediction,
production audit and fresh recount are retained under
`conker/build/game-next-151a11e4-private/emitter-recovery/`. Do not rerun its
freeze/install/bank scripts or weaken historical whole-owner fixtures.
`make tools-check` and diff checks pass. Root README changes only aggregate rows.

## Review, sibling and next work

One packet-only Claude Pro review used the verified claude.ai/firstParty route,
CLI 2.1.218, effective tools=[] / MCP servers=[] and zero tool uses. It found
no concrete soundness defect. Codex independently checked its byte/short,
induction and allocation-pin observations. Its path-count explanation is
corrected: 512 comprises two random-bit branches, five signed-minus-one guards,
the nullable result and the repeat decision. The advisory is not a test receipt;
the actual rename/negative controls and final suites provide fresh evidence.
No second review call was made.

Sibling `64CBFD Tools` remains at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`,
2,434 dirty paths, Windows status digest
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
Its files are not overwritten; eight task files are tested in a private overlay.
The OGL path has retained captures and no maintained source checkout to update.
No host build, frozen Release or save is touched.

Graph maintenance uses the native update attempt, scoped AST merge, old-ID
retention and any post-hook heading aliases; it is not full-corpus extraction.
Tools-first local commits are authorized; nothing is pushed.

Continue with adjacent placeholder `func_151A1998` after banking this function.
Read its entire retail window, factory/dispatch interface and new clean heads
before preparing the next baseline. Do not award its credit from this proof or
carry the current whole-owner fingerprints forward as though unchanged.
