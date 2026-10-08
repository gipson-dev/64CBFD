# Game Record Ring Shaping Conversion

Date: 2026-10-08

## Result

Finish the complete target from [Note 1137](1137-game-record-ring-shaping-recovery-20261008.md)
under the [focused workflow](../AGENT_WORKFLOW.md). Replace only the retained
`func_151D7CD0` directive in [generated_204660.c](../../conker/src/game/generated_204660.c).
The linked routine is **253 words / 1,012 bytes / frame 0xB8**, byte-exact
through its complete return delay slot. VA 0x151D7CD0..0x151D80C4; ROM
0x205180..0x205574. Preserve the [slice](../../conker/asm/204660.s) and
[original function](../../conker/asm/nonmatchings/generated_204660/func_151D7CD0.s).

The complete semantic C emits the full retail extent with **183 direct words
and 70 strict closed normalization guards**. This is not a directly unguarded
compiler match. No inserted/omitted words, fallback body, dead-local padding,
assembly substitution, compiler-profile change or new data pool.

Fresh linked audit compares all **6,058 bodies, addresses and extents** against
`conker/build/game-record-ring-sampling-test/after.json`: all unchanged,
including this formerly retained-assembly target. Protected Init, Init data,
debugger and Game data remain unchanged; Game data layout is exact. Preserve
all **11,205 prior guard rows and their raw CSV prefix**, then append 70.
The only progress-row change is this **1,012-byte ASM-to-C conversion**.

| Section | Converted | Converted Bytes | Byte-exact |
| --- | ---: | ---: | ---: |
| Total | 5,481 / 6,042 (90.71%) | 85.79% | 3,392 / 5,481 (61.89%) |
| Game | 4,808 / 5,321 (90.36%) | 85.13% | 2,719 / 4,808 (56.55%) |

Zero address drift; 2,089 still different. Init remains 492/492 exact;
debugger remains 181/181 exact. Root README changes only its aggregate rows.
The wider Game goal stays open; this does not authorize host integration.

## Meaningful Fitting

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_ring_shaping_candidates.py)
retains the original complete recovery and screens **111 full source forms**.
Use byte addressing for the 28-byte stride, phase-local cursor/record
lifetimes, and meaningful used trim intermediates. A float truth test on the
reloaded length avoids hoisting a saved F26 zero. Split the fade distance
update between its two real branches to recover the complete 253-word loop.
The private vector remains three floats, not a padded buffer.

The fitted O2/g3 body has **frame 0xB8, vector SP+0x98, saved F20/F22/F24 and
S0..S5**. Its private total spill is SP+0xA8 before normalization; two paired
guards move the spill/reload to retail SP+0xAC. The earlier natural body was
256 words/frame0x98 and oversized. The behaviorally wrong 253-word live-buffer
form remains an effective negative, not a fit. Preserve the exact reciprocal
product grouping, not reassociated division; Note 1137 contains the witness.

| Fitted Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 253 | 0xB8 | 70 |
| O2 | 252 | 0xB8 | 251 |
| O1/g3 | 351 | 0x80 | 339 |
| O1 | 351 | 0x80 | 339 |

## Guard Review

[Seventy rows](../../conker/retail_word_patches.us.csv) encode only reviewed
closed allocation/scheduling cycles. Every row has an exact expected word,
explicit relocation ownership, and no insertion or omission:

- +0x10C/+0x1C0/+0x1C4 close the previous-point/goal-read schedule;
  +0x1A0 preserves commutative branch operand order.
- +0x110..+0x180 close trim FP allocation and independent XYZ/retained-length
  scheduling without changing arithmetic grouping or the public trim pipeline.
- +0x1D4/+0x1EC pair the private-total SP+0xA8 to SP+0xAC move.
- +0x1F4..+0x278 close phase FP allocation while preserving live field/global
  reloads, both helper interfaces and captured payload/buffer pointers.
- +0x29C..+0x3BC close the fade FP roles and cursor/point V0/V1 allocation,
  including the final output-byte/length-read/distance-add/delay-slot schedule.
  The raw compiler hoists a length load before its output store; normalized
  code restores retail fault/access order. Neither arithmetic nor array
  contents are synthesized from the ROM at runtime.

The three guarded global LO16 words at +0x1FC, +0x24C and +0x29C use **zero
object addends**, with matching expected/replacement symbol relocations.
The isolated linked normalizer checks their actual symbol low halves.
All 13 relocation sites retain their positions/types/symbols.

## Fresh Qualification

Eight pre-install tests pass in **177.089s**. All eight installed tests pass
in **163.182s**, with no skips. Eleven affected-neighbor checks pass in
**117.305s**; the complete loader/runner receipt takes 120.587s.
The [focused suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_ring_shaping_recovery.py)
qualifies:

- **1,861 guest cases** across raw C, normalized and retail code, compared
  with an independent reference. Normalized/retail complete memory, private
  GP/FP state and trace agree. All 256 state/current/count bytes, inactive
  goals, two SP phases, ten live mutations and three buffer layouts qualify.
- **155,964 native32 cases** execute the fitted C through a volatile typed
  call with independent scalar/offset reference, argument bits and 16,384-byte
  canaries. Cover all 65,536 current/count pairs, all 65,536 flag words,
  all state bytes, inactive goals and ten mutations across three layouts.
- **66 required fault prefixes and three lazy layouts** compare retail and
  normalized partial public state/trace with the independent reference.
  Raw C fault order and portable C fault behavior are not claimed.
- **84 bounded conversion fragment cases** reach all 32 unsigned-conversion
  words, including signed fallback, sentinel and FCSR save/restore. Full-body
  cases reach 248/253 words; fragment coverage leaves only +0x128 unreached.
  Sixteen XOR boundary checks qualify the local oracle operation required by
  a complete conditional-post source form, not a new production instruction.
- **111 complete forms / 2,500 ordinary executions / eleven effective
  negatives** pass. Extra ABI calls remain explicit rejection witnesses,
  never instruction timeouts or unsupported-opcode substitutes.
- **48 connected cases / 144 executions** run both complete actual helpers
  and the 100-word original dispatcher across all three bodies. Verify
  third-table callback 4, true-result consumption and no release on this gate.
- Copied owners preserve **22 neighbors**, normalized pools, relative
  relocations and four existing diagnostics; isolated/copied target bytes
  agree. The actual padder emits **1,012 bytes with no padding**, with all
  13 independently expected relocation sites in **six links / 240 executions**
  across carry, high-address and jump-region boundaries.
- Reject stale header/all 70 expected words, malformed guard history and four
  actual padder word/relocation mutations. Shared history checks preserve
  each earlier complete guard segment and the new exact 70-row tail.

One rebase fixture originally put a global inside the oracle's private stack
range; move only the fixture addresses while preserving their low-half carry
boundaries. A new complete source form emitted integer XOR; extend only this
local oracle and add discriminating boundary checks. Neither fixture issue
is a production-source fix or an effective negative result.

The original dispatcher remains a linked placeholder. Executing its complete
retail words in the connection test does not restore it, qualify alternate
dispatch/release branches or establish live gameplay. Native checks exclude
invalid float-to-unsigned casts; the guest conversion model is bounded, not
hardware FCSR flags/traps/rounding-mode/NaN-payload qualification. Preserve
retail nonterminating domains and explicitly mapped negative-index/count-zero
fixtures; do not change the algorithm to accommodate them.

Fresh affected checks cover sampling/ring/velocity copied-owner padding,
rebases, actual connections and installed guard history, plus cleanup and
allocation history/owner checks. Preserve the later 70-row segment when
retesting earlier sampling guards; update bounded history counts in older
fixtures without changing production neighbor code.

Fresh shared checks: **14 matcher/padder/repository-setup tests**, project
checks in mounted and standalone tools, CLI help, six-file syntax and mirror
byte equality. Older comprehensive neighbor-suite receipts remain historical,
not fresh complete-suite runs. Scoped documentation checks pass **124
documents / 4,060 relative links / zero broken links**, with **35 relevant
tools files byte-identical** in both checkouts.

## Baseline And Banking

Entry parent **bbbd885ac1a609403162b064ba9fbea4db2cc584**, mounted tools
**856ba006efda6d15766e0071ebebfffcd162e1e7**. Before installation:

```text
source: f130527184a98e66698e64e315a7666bf58af90587528e4ff98c93ae5a41c949
reference ASM: 14c690097e848287eb8f9e5f3f1031cfa7c3fd65ebdb31075cdafc30a732fa48
Makefile: d5e4c8459b9bf1ac7485b913f559fe9e0242ec284d76cddf0650c210e2a73466
progress: 8ca0455bc7d4ce937afba6083f482ab9d7744c0b34f3bb8e793f3ef12c9cefdd
guard CSV: b2bceb2ae2449511f5d07f9d36b43f10f62ce2a7f2cad8e06217705c28bc2c38
```

Per "Keep commited", mounted tools **5c9e50bfb3d84c9a2ac9c9435be2944b2134049e** banks the six
reviewed files first. The parent source/guard/docs checkpoint records that
exact consumer pin. Mirror only those six files after checking each
older copy against the mounted entry blob; preserve older **ddbdd16** HEAD,
its exact dirty status and independent edits. No duplicate standalone-history
commit, reset, stash, unrelated staging or push.

Ignored receipts are in `conker/build/game-record-ring-shaping-test/`:
slot, guest, native, faults, conversion, controls, connected, owner,
audit-baseline, audit-installed and after JSON; before-progress/manifest are
the pre-install witnesses. The new after.json is the next linked baseline.

Graph query precedes investigation. Fresh `graphify update .` exits 1,
refusing **16,810 new nodes versus 38,598 existing**, retaining 19,398 nodes
from 2,972 excluded-but-existing files. No force, installation or ignore-rule
change; a later incremental commit hook is not full-corpus repair.
Zero Claude calls. No host source, build or runtime changes, and no save,
editor, bridge or account changes;
OGL Release remains frozen.

## Next Target

Next retained **func_151D80C4**, **405 words / 1,620 bytes / frame 0xD0**:
VA 0x151D80C4..0x151D8718, ROM 0x205574..0x205BC8. Recover its complete
original routine and actual caller/callee interfaces before fitting; no
candidate or qualification is claimed here. The broader Game matching goal,
linked dispatcher restoration, hardware/gameplay and full graph repair stay open.
