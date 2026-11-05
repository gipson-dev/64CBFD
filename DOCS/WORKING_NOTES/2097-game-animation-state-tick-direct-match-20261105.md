# Animation state tick directly recovered

Date: 2026-11-05. Target `func_15167B44`, owner `game_1944C0`.
Source `conker/src/game_1944C0.c`; original
`conker/asm/nonmatchings/game_1944C0/func_15167B44.s`.

## Outcome and source shape

All nine pre-install checks pass in **83.446 seconds**. The nine fresh installed
checks pass in **79.842 seconds**. Actual Make and the independent complete-image
prediction agree byte for byte.

The routine emits all **69 words / 276 bytes directly**, with frame24, three
bindings, no alignment tail and no guards. Both compact and ordinary padded
C owners preserve all **41 neighbors**, their bindings and normalized pools.
VA is `0x15167B44..0x15167C58`; ROM is `0x194FF4..0x195108`.

The recovered interface is `void func_15167B44(u8 *state)`. Its local forward
declaration is corrected from the false untyped `s32` declaration. Existing
callback-table and release-helper declarations remain unchanged. The first
semantic candidate already has the correct length/frame but eight register
differences in the negative-rate path. Giving the signed negated rate its own
local assignment before the threshold test recovers the complete retail
schedule. No compiler profile, padder, external translation unit or guard
manifest change is needed.

## Signed phase, countdown and live reads

The optional unsigned callback index is `state[0x24]`. Zero skips the callback
table entirely. A nonzero index calls `D_8008CA20[index](state)`, after which
the state pointer is reloaded from its incoming home and all working fields
are read live. The signed byte at `+0x22` is the rate; `+0x23` is the unsigned
countdown. The descriptor pointer is at `+0x10`, its unsigned count at `+4`,
the signed phase at `+0x14` and signed step at `+0x16`.

For a positive rate, strictly greater remaining time is decremented; a tie
or exhausted countdown instead sets phase to the descriptor count shifted
by eight. For a negative rate, phase/256 must have reached count-1 and the
countdown must be strictly greater than the negated rate. That holding path
decrements the countdown and subtracts step before the common phase advance.
Both halfword stores remain observable, including wrapped signed results.

Signed division by256 truncates toward zero. Arithmetic shift is different
for negative nonmultiples and is rejected by an effective compiled control.
Phase stores retain the existing signed-halfword wrapping behavior.
The final descriptor pointer is loaded before the common phase store, while
its count byte is read after that store; descriptor counts may alias phase,
step, rate or countdown. The final wrapped phase quotient reaching count
calls `func_1516972C`, with no later state-field read.

## Registration, actual caller and lifecycle boundary

A complete aligned retail-word census finds no direct JAL or tail jump to
the target and exactly one address literal, ROM `0x230004`, VA `0x8008B544`.
It is row3, field0 of `D_8008B4A8`, with a 52-byte `struct115` stride. The
catalog begins at ROM `0x22FF68` and spans the original `22FF40`/`22FF90`
data owners. Both original owners are frozen and preserved.

The actual update caller is `func_151670C0`. Its original 33-word window
`0x15167118..0x1516719C` is connected to both target bodies. The field0 JALR
is at `0x15167170`, returns at `0x15167178`, and passes the current list node
in A0. The window increments signed update depth, saves the next node in the
depth-indexed slot before calling, reloads that slot afterward, and restores
depth on exit. Both banks, empty/single/two-node lists and callback changes
to the saved next pointer are covered. `func_151671E8` uses field4, which is
zero for this row; it is not counted as a second caller of this target.

The original 28-word release routine `func_1516972C`, 20-word unlink routine
`func_151696DC` and eight-word fallback `func_15169804` are also connected.
Unlink updates every matching saved slot below signed current depth. Kinds0/1
return after unlink; kind3 with a null destructor follows the original
fallback to bounded `func_15168B10(state, 1)`. This proves the tested saved-slot
and null-destructor routes, not non-null destructor behavior, full heap
reclamation, the complete outer dispatcher, gameplay or hardware acceptance.

## Focused qualification and effective controls

The nine-test suite checks these distinct contracts:

* 11,520 guest cases per body cover all rate/countdown/count byte values,
  threshold/tie cases, negative quotients, signed-step extremes and wrapped
  halfwords. Their union visits every one of the 69 target words.
* 760 provider/private/descriptor-alias cases per body include callback
  mutations of fields, descriptor, table entry, saved-next slot and incoming
  state home. Of these, 758 return or reach the deliberately redirected
  return boundary; two have an explicitly required identical guest fault.
* 288 connected lifecycle cases per body and 48 actual caller-window cases
  per body exercise the original routines and both list banks.
* All 44 fired access-prefix cuts compare complete register/RAM state and
  ordered traces. Separate zero-index/zero-rate cases leave the callback
  table/countdown unmapped and still complete without reading them.
* Nine independent GNU links compare original assembly, compact C and padded
  C across three layouts, including both HI/LO carry edges. All three
  bindings and 120 rebased cases per body pass.
* Native32 O0/O2/O3 pass **24,816 positive executions** through direct and
  typed calls, three descriptor aliases and UBSan. Nine negative native
  controls and nine independently compiled IDO controls are effective.
* Every one of 276 changed raw bytes, each bad binding and four independent
  full-file corruptions is rejected. No target guard row exists.

The controls reject unsigned rate/phase, floor division, either countdown
tie change, cached pre-callback rate, wrong callback index, omitted holding
backstep and the wrong release equality boundary. The native reference uses
native byte order; guest alias expectations use big-endian byte order.

Fixture corrections did not change production C. The reference now models
callback writes to all four outgoing homes and the actual caller's temporary
depth increment. An added negative-phase/count3 witness makes unsigned-phase
controls effective. One deliberately overlapping private input has saved RA
at its callback-index byte: the save replaces zero with `0xDE`; that callback
overwrites the descriptor with `0xB5000000`, producing an unmapped byte read
at `0xB5000004`. Both rates test the identical fault, complete state and trace
instead of incorrectly requiring a successful return.

The shared nineteen padder, relocation, matcher and protected-layout checks
pass in **7.102 seconds**, and `make tools-check` passes. No shared oracle is
changed. Unchanged neighbor suites are reused through measured byte/binding/
pool identity, not claimed freshly executed.

## Immutable inputs and complete production image

The private snapshot freezes **96 files**, including all headers, source,
object, ELF, code binary, retail input, original target/callers/registry,
guard manifest, layout, Makefile, linker, progress and graph. Artifacts are in
`conker/build/game-animation-state-tick-15167B44-match/`, with adjacent source
screens. The accepted ordinary C-owner padder output is `qualified-owner.o`.

All 6,052 function addresses remain fixed; only the target body changes.
All 189,088 protected Game bytes across 720 owners remain exact. Literal
complete-file prediction changes only the target's 276-byte slot and its
symbol extent: **204 bytes**, with zero exclusions, no symbol/string
serialization correction and no metadata substitution. Actual Make's owner
and complete ELF equal their independent qualified artifacts.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `b3ee4d4860755a3629384d55d5c8febd44a8509d0ec6bf9215e01892a52e5123` |
| Retail target | `92b6457e9e90d582e1779373bc4080ed6ed747f3cd32fe35b52ab6732efe100f` |
| Frozen predecessor ELF | `6f1eb8121a4c21b123b88b0dc068ae30fd930ba3a03d112117fdf40a7510f71b` |
| Qualified padded owner | `5e1878fbb498dd27ab7d7b46e740ef138113a0db2e5794c1b11ebc2e4779759f` |
| Production complete ELF | `62e5bfea14b052e47e4928f670c6895794b3b9c001a74d59f80906ff45419aae` |
| Production code binary | `cc31fe74216bf757bdd9f2bac8c7be7f4508bc424f23ca3627490461e1830817` |
| Unchanged guard CSV working bytes | `87a70532340ab80357051ae8b6e0b77d09b65d08c2af717f3b1cf32b35e8b3ce` |

The guard manifest's bytes and modification time are unchanged. Frozen
headers, retail assembly/input, layout, linker and Makefile are unchanged.
The inherited owner diagnostics remain six warning712 and one warning709;
normalized predecessor/candidate diagnostics agree. Actual Make retains its
pre-existing duplicate `generated_12D630` recipe warning. `make -C conker all`
creates the code binary and returns2 solely at the expected overall retail
SHA mismatch for this incomplete decompilation.

## Baselines, measured progress and continuation

Main baseline: `fe4a84b0a737dfcf4cb82b88ed091bc11cb9783a`. Mounted tools
baseline: `ef757f6e3632b6f08a26e1df8f67b3c7f280ff53`. Both start clean.
The separate sibling tools checkout remains at
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with six tracked changes and
2,428 untracked files. It is untouched; no fresh sibling qualification is
claimed. No host-port or frozen Release changes are made. Routine work uses
zero Claude calls. Existing IDO/GNU tooling is used under the documented
Windows REA MIPS-adapter limitation, without repeating configuration setup.

The fresh actual-ELF recount reports:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,168 / 5,512 | 75.62% | 0 | 1,344 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,495 / 4,839 | 72.23% | 0 | 1,344 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory stays 5,512/6,046. Root README edits are aggregate rows
only. The 80% threshold is 4,410/5,512, leaving **242 more** exact functions.
Fresh ranking selects `func_15197AB4`, 66 words and 65 real differences, as
the next ordinary target. Keep `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC` and
`func_150A6760` as the separate documented boundary cases. Keep the wider
80% goal open. Graph retention and the tools-first commit receipt follow.

Mounted tools are committed first as
`3aa6c5ac8e11994af4ab8b7d859b29bb4c3b639b`
(`test(game): qualify animation state tick and lifecycle`). The consumer
includes that pointer, the direct C and documentation.

The standard Graphify update refused a reduced 24,912-node extraction
against the existing 58,706-node graph, preserving the larger graph. The
seven-path scoped refresh retains 58,703 old nodes, relocates three existing
`DOCS/UPDATE_LOG.md` headings and adds eight headings from this note:
58,714 nodes, 112,473 links and 5,158 communities. No node outside the
changed paths is removed. The retention receipt records SHA-256
`9a33dd54b12fb3c183237decdd6bec49810c5c14ed6061d65df1c4001d931a7e`.
The 31,816 retained nodes from 3,754 still-existing files outside the current
scan corpus are preservation evidence, not a fresh full-corpus extraction
claim. This AST-only refresh makes no LLM calls. The ignored
`graph-retention.json` receipt is retained in the qualification directory.
