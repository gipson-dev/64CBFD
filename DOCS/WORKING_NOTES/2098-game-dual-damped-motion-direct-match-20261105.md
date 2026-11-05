# Dual damped motion callback directly recovered

Date: 2026-11-05. Target `func_15197AB4`, owner `generated_1C2C60`.
Source `conker/src/game/generated_1C2C60.c`; original `conker/asm/1C2C60.s`.

## Outcome and recovered record

All eight pre-install checks pass in **42.277 seconds**. The eight fresh
installed checks pass in **39.246 seconds**. Actual Make and independent
complete-image prediction agree byte for byte.

The first complete semantic candidate emits all **66 words / 264 bytes
directly**, with no frame, alignment tail or guards. Both compact and padded
owners preserve all **68 neighbors**, their bindings and normalized pools.
VA is `0x15197AB4..0x15197BBC`; ROM is `0x1C4F64..0x1C506C`.

The recovered interface is `s32(DualDampedMotion15197AB4 *motion)`, returning
one. The local 0x164-byte type names position/endPoint at `+0x34/+0x40`,
velocity/endVelocity at `+0x140/+0x14C`, verticalAcceleration at `+0x158`,
damping at `+0x15C` and endDamping at `+0x160`. All other bytes remain reserved.
The file gets a local `extern f32 D_800BE9A4`; no shared header or compiler
profile changes. Native compile-time checks verify the size and field offsets.

## Motion arithmetic and live timestep

The routine snapshots both damping factors and the shared acceleration.
For each velocity triple, X/Z are multiplied by that triple's damping and Y
adds acceleration times the live timestep. The first point then advances
by the first velocity triple, and the endpoint advances by the second.
There is no endpoint blend or forced retirement. Every path returns one.

The global timestep `D_800BE9A4` is read **eight times**: once for each Y
acceleration and separately for all six coordinate advances. A timestep
alias to a damped velocity or an already updated coordinate must observe
the intervening store. C keeps these repeated expressions rather than a
cached timestep. Both factors and acceleration remain snapshotted as retail
requires. Each single-precision multiply/add rounds independently; the source
does not fuse operations or change their association.

## Registration and original caller

A complete aligned retail-word census finds no direct JAL or tail jump and
one address literal, ROM `0x22E7A0`, VA `0x80089CE0`. The 42-entry table
`D_80089CB8` contains the target at **slot10**. Its original data owner is
`conker/asm/data/22E730.rodata.s` and remains byte-identical.

The actual caller is `func_1513CFE4`. Its original 16-word window
`0x1513D034..0x1513D074` gates on state byte `+0x70`, loads the corresponding
table function, saves the state pointer and expiration byte, and calls through
T9 at `0x1513D058`. The return at `0x1513D060` reloads the state pointer and
expiration; V0 zero forces expiration to one. The target's nonzero return
preserves the signed saved byte. The tests connect both retail and C bodies
and deliberately substitute a zero return to prove this control is effective.
This window is bounded evidence, not qualification of the complete parent.

## Focused semantic, alias and fault evidence

All eight checks cover distinct contracts:

* **3,304 guest cases per body** cover both independent dampings, acceleration,
  positive/negative timesteps, signed zero, subnormals, rounding, cancellation,
  large values, infinities and NaNs. All 66 words are visited. Independent
  reference comparisons classify NaN outputs and compare all other bytes
  exactly; retail/C complete emitted states remain literally equal.
* **1,432 alias/private cases per body** cover every one of the 89 aligned
  timestep locations in the 0x164-byte record, both stack phases, four value
  patterns, both point sets and eight additional private-stack overlaps.
* **96 actual caller-window cases per body** cover zero/slot10 selection,
  signed expiration bytes, both stack phases and the effective zero-return
  control. No unsupported callback provider is substituted for the target.
* **246 fired access-prefix cuts** across six disjoint/overlapping layouts
  compare complete private state and ordered events at the same boundary.
* **Nine independent GNU links** compare original assembly, compact C and
  padded C at three layouts, including both HI/LO carry edges. All two
  bindings and **84 rebased cases per body** pass.
* Native32 O0/O2/O3 pass **12,288 positive executions** through direct and
  typed calls, with disjoint timestep storage and all 15 typed float-field
  aliases. The fixture binds the timestep expression to valid float storage;
  padding/global-address overlaps remain guest tests. All reserved/guard
  bytes are checked. UBSan is enabled and FP contraction is disabled.
* Ten negative native controls and ten actual IDO-compiled controls reject
  a false return, omitted/misassigned damping, changed acceleration, wrong
  point/velocity axis, cached timestep and reversed coordinate order.
* Every changed raw target byte, three malformed binding maps and four
  independent full-file corruptions are rejected. No target guard row exists.

NaN value classification in the semantic reference does not claim portable
NaN payload selection or FCSR/hardware parity. Literal matching and full
guest state equality separately preserve the emitted payload and access order.
No shared oracle is modified and no fixture repair is required for this target.

The shared nineteen padder, relocation, matcher and protected-layout checks
pass in **6.573 seconds**, and `make tools-check` passes. Unchanged neighbor
suites are reused through verified byte/binding/pool identity rather than
claimed freshly executed. Routine work uses zero Claude calls.

## Immutable inputs and complete-image proof

The private snapshot freezes **94 files**, including all headers, source,
object, ELF, code binary, retail input, original target/caller/registry,
guard history, layout, Makefile, linker, progress and graph. Artifacts are in
`conker/build/game-dual-damped-motion-15197AB4-match/`, with adjacent source
screening output. The generated-owner padder is used without overrides.

All **6,052 function addresses** remain fixed, and only the target body
changes. All **189,088 protected Game bytes across 720 owners** remain exact.
The literal complete-file prediction changes only the target slot and symbol
extent: **227 bytes**, zero exclusions, no symbol/string serialization
correction and no metadata substitution. The production owner and complete
ELF equal their independently qualified artifacts.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `19c57bdc96df0444fbf19c2b1310f68711211f9745dc1375d4689860bce65c5f` |
| Retail target | `6aafd82dc077210e6759995c00a872115d3ab6d0ebc368e2e4c5f4e97bca6053` |
| Frozen predecessor ELF | `62e5bfea14b052e47e4928f670c6895794b3b9c001a74d59f80906ff45419aae` |
| Qualified padded owner | `d8fdfceff9c875e6aeeb2d02e510423ee3faf2e2aa6ff6f2909c4dff59c80330` |
| Production complete ELF | `de83c495f3f7ba430fe8d252ad09111059fc6969d4c41f28cebc652169bba20f` |
| Production code binary | `77f8ca771caecc5154b11f63e82af5003915450b7c40fbb4863b764015f702a0` |
| Unchanged guard CSV working bytes | `87a70532340ab80357051ae8b6e0b77d09b65d08c2af717f3b1cf32b35e8b3ce` |

The guard manifest's bytes and modification time are unchanged. Frozen
headers, retail assembly/input, layout, Makefile and linker are unchanged.
The predecessor and candidate owner produce no compiler diagnostics. Actual
Make retains its inherited duplicate `generated_12D630` recipe warning.
`make -C conker all` creates the code binary and returns2 solely at the
expected overall retail SHA mismatch for this incomplete decompilation.

## Baselines, progress and continuation

Main baseline: `df599c92222caec29eb24357244810ae2af4edc5`. Mounted tools
baseline: `3aa6c5ac8e11994af4ab8b7d859b29bb4c3b639b`. Both start clean.
The separate sibling tools checkout is freshly checked at
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with six tracked changes and
2,428 untracked files. It is untouched, and no fresh sibling qualification
is claimed. No host-port or frozen Release changes are made. Existing
IDO/GNU tools are used under the documented Windows REA MIPS-adapter limit.

The fresh actual-ELF recount reports:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,169 / 5,512 | 75.63% | 0 | 1,343 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,496 / 4,839 | 72.25% | 0 | 1,343 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory stays 5,512/6,046. Root README edits are aggregate rows
only. The 80% threshold is 4,410/5,512, leaving **241 more** exact functions.
Fresh ranking selects `func_151A0AF8`, 69 words and 65 real differences, as
the next ordinary target. Keep `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC` and
`func_150A6760` as the separate documented boundary cases. Keep the wider
80% goal open. The tools-first commit and graph retention receipts follow.

Mounted tools are committed first as
`ec88172bbd701baff707b2be613531ad87a230f6`
(`test(game): qualify direct dual damped motion`). The consumer includes
that pointer, the typed C and documentation.

The standard Graphify update refused a reduced 24,921-node extraction
against the existing 58,714-node graph, preserving the larger graph. The
seven-path scoped refresh retains 58,711 old nodes, relocates three existing
`DOCS/UPDATE_LOG.md` headings and adds eight headings from this note plus
one type reference: 58,723 nodes, 112,481 links and 5,169 communities.
No node outside the changed paths is removed. The retention receipt records
SHA-256 `968a6f1a806199a74cb89e5a1f37b8ca043aaa64f19340f4e4f6e2b5d2c7cee9`.
The 31,816 retained nodes from 3,754 still-existing files outside the current
scan corpus are preservation evidence, not a fresh full-corpus extraction
claim. This AST-only refresh makes no LLM calls. The ignored
`graph-retention.json` receipt is retained in the qualification directory.
