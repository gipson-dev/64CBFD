# Actor Target Timer Complete Match

Verified: 2026-10-19. **Installed complete C recovery: all115 words /460 bytes
match retail, including frame80 and the observable script result.** Finish
func_1508D850, generated_B3020, VA1508D850..1508DA1C, ROM BAD00..BAECC, after
[Note1592](1592-actor-target-timer-semantic-recovery-and-matching-boundary-20261019.md).
Consumer predecessor **b0375f4d**, tools predecessor **4211351**. Bank tools
**2728516** before the consumer source/guards/docs/pin. No push.

## Source And Script Result

Replace the zero-return placeholder with the complete target publication,
fresh full-word target read, float32 horizontal distance, signed selector/
threshold/timer views, timer clear, current-context notification mask and
callback-aware probability-flag update. Preserve the original actor/timer
pointers across helpers and reload the nested pointer and selector where
retail does. Restore the explicit signed32 slot prototype and meaningful
local names; do not invent original symbol names or a record structure.

The source keeps its partial return: negative target returns0; other paths
fall through. The new comment makes that boundary explicit. Do not replace it
with void, return0 everywhere, a returned distance class, or an int cast of
the float RNG. Native qualification discards the C result. Separately qualify
the emitted MIPS result against its real handwritten consumer.

The wider audit finds func_1509DFC4 in D_800884D4[14], reached through the
handwritten func_150ADAF0 dispatch helper at150AE12C. That helper is itself
selected through D_800886A4[6]. Its result is not simply dead: after the
dispatcher returns, **150AE00C stores V0 to D_800D3848**, and150AE024 publishes
that result-cell pointer to D_800D384C. Freeze DAFA0.s and the supplying
22BEF0/22D070/243DC0 rodata alongside the existing caller/owner inputs.

The emitted result is path-dependent: zero on negative targets, the class
on a no-helper path, the notification provider's residual when it changes the
old timer, or the RNG seed's low16 bits after a random update. The actual
25-word RNG returns the fraction in F0, not a corresponding integer in V0.
Seed89413 produces fraction1.0 and V0=65535, demonstrating why a float-to-int
cast would corrupt the interpreter result. This is a verified machine-code
ABI, not a new general portable-C numeric-result promise.

## Explicit Layout Recipe

Sixteen unique pointer/table/operand screens retain the old115/frame80/60
body as the qualified source. Shared offsets and table views do not improve
the complete fit. The bit-lifetime screen reaches58 differences but frame88;
reject it rather than treating the smaller difference count as progress.

The60 checked rows are generated from a specific instruction-origin recipe,
not copied retail words:

- Coalesce the two identical slot*4 shifts at source origins9/10. Omit only
  origin10; both uses refer to the remaining slot-offset lifetime.
- Hoist only the selector and threshold **LUI address definitions**, origins
  18/63, into their original early positions. Do not hoist the mutable loads.
  Their destination roles are dead before the new definitions and preserved
  through their later uses.
- Recover the explicit actor-table/actor/target-slot/timer-base/timer roles,
  then the selector/threshold/mask and later probability temporaries. The
  mapping is lifetime-specific, including separate roles for successive
  timer reads; it is not a whole-function register substitution.
- Schedule the independent class shift/timer address and mask shift/load
  work. Exchange operands only on one commutative nontrapping ADDU and AND.
  The earlier command-0x61 setup replaces its always-executed branch delay.
- Split origin86's timer load over mutually exclusive edges: one copy in
  the mask-zero likely-branch delay, the other after the notification call.
  Redirect that branch to the common timer test and adjust the earlier
  threshold branch's displacement. The predicate, number and order of
  executed memory accesses are unchanged; the non-taken likely delay is
  annulled. This is more than a pure GPR renaming and is tested accordingly.

The result remains115 words:114 unique source origins, one omitted duplicate
shift and one edge-duplicated timer load. Preserve all16 relocation bindings,
including both calls. Frame, constants, FP operations/register fields and
comparison condition fields remain unchanged. Raw/binding fingerprints,
structural preconditions and the normalized digest reject stale recipes.

```text
raw:        7a173d55e1f6d80293c18209802ce9ab0bb18cba06317baa1329024ca4adc601
normalized: ab81695a5e81d361f6b34284a44efdfb16e96b19189fd380922d29e237d967cb
```

## Fresh Qualification

Before installation, the ten matching tests and seven earlier recovery tests
pass together:17 tests in52.406 seconds. Repeated corpus checks are not new
input domains. The strengthened **11 installed tests pass in60.669 seconds**,
without skips, including the additional script-result control and guest targets.

- **316 full literal-state pairs** across158 fixtures/two stack phases match
  GP, FP, LO, condition, private/public memory and ordered events. Raw C also
  preserves the entire private memory/event trace and residual V0, despite
  its different temporary register allocation. The independent public
  reference separately checks complete public buffers and stores.
- **105 fired access-cut triples** compare retail, normalized and raw C on
  negative, unchanged-timer, mask-zero and callback-mutating paths. The raw
  private prefix and requested access agree too. These checks do not claim
  hardware fault/FCSR equivalence.
- Native32 O0, O2 and O2+UBSan each pass158 complete translated-buffer cases
  using the **actual partial-return body**, with its result discarded. Only
  the native return-type warning is disabled for that known shape. Five
  effective native negatives change threshold equality, probability equality,
  probability sign, timer-context caching or distance equality; each exits21
  or23, not a signal.
- **24 script-consumer triples** execute the real two indirect tables,
  dispatcher prologue, third table's selected switch arm, full-word slot
  load, target call, actual epilogues and result stores. The fired stop is
  after D_800D384C is written, not a full interpreter run. Include negative
  targets, no-helper and callback-result paths; two triples connect the real
  seeded RNG. A return-delay zeroing negative preserves function effects
  but demonstrably corrupts the stored65535 result.
- **50 real-RNG fixture pairs** and the **actual26-word notification wrapper**
  are rerun using the existing qualified tests. The script provider behind
  that wrapper is modeled, not the complete interpreter. The inherited
  wrapper/access-prefix and20 direct returning-caller runs also pass.
- Five completed backed guest triples cover full-word targets32/33/63/255/
  256, byte publication and MIPS low5 shift counts. The earlier publication
  alias also passes. These are emitted-binary checks, not native bounds or
  out-of-range C-shift validity claims.
- **Three independent GNU maps /45 executed rebased pairs** qualify all16
  bindings, including calls and HI/LO carry boundaries. Rebase code, globals,
  heaps and provider anchors; compare raw/normalized effects, private traces
  and residual results against the independent reference.
- Twenty-five raw/binding/recipe corruptions reject. Two stale manifests
  fail through the actual padder; five changed images fail the strict image
  check. Canonical symbol identities/values change only at the target size.
- Both complete-owner profiles have empty diagnostics and preserve72 other
  routines and pools. Actual padding preserves those neighbors and all73
  addresses. Seven expanded Make commands reproduce the qualified code,
  bindings and padded metadata without a production flag/profile change.

## Strict Image And Production

The initial code/size-only prediction rejected the first private link. New
references also reorder nine existing symbol rows/strings in four bounded
runs. Predict precisely these sequences, checking the old rows, contiguity,
literal strings and unchanged semantic fields:

```text
func_15109410, D_80090244 -> D_80090244, func_15109410
D_800E0BD0, D_800A36A0  -> D_800A36A0, D_800E0BD0
D_8009DA8C, D_8009865C, .L15041730_game_data
  -> D_8009865C, .L15041730_game_data, D_8009DA8C
D_800A6B80, D_80090230  -> D_80090230, D_800A6B80
```

Keep the failed initial receipt. Do not broadly ignore canonical-symbol or
string-table changes, or permute the actual output to make it pass.

The corrected private prediction and production Make agree over the entire
3,257,636-byte ELF: **461 changed bytes =341 target-code bytes +two target-size
bytes +118 serialization bytes** (46 symtab,72 strtab). Target size12 ->460;
all6,056 other bodies, every address and all189,088 protected Game-data bytes
/720 owners stay fixed. Production succeeds with inherited warnings from
untouched code; only the target owner profiles have empty diagnostics.

```text
owner SHA: faf1daec7d177ba36d35c8ee90c52ef5a253925f0e94cc6100ebbf56cfac52c8
guards:    bc019c19bbd9b3ae7078f19ed2833ace7895879f76a2ed9e237aeaca1a5a08b8
ELF:       3010db543bf9dd6844ebe7e8eb2b8a7587378d2d23060e5e3c5b9ff6b464fa62
```

Commands from64CBFD under WSL:

```sh
python3 -m unittest tools.tests.test_game_actor_target_timer_match -v
python3 -m tools.experiments.game_actor_target_timer_integration --audit
python3 -m tools.match_progress conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Receipts, commands, native fixtures, initial image diagnosis, complete rebuild
log and installed audit are ignored under
`conker/build/game-actor-target-timer/matching/`. Python syntax checks pass in
both tools copies; five new files are copied identically while preserving all
1,358 older mirror hashes and its old HEAD. No standalone mirror commit.

## Progress And Resume

Fresh **Game3006/4832 (62.21%)**, **total3679/5505 (66.83%)**, **1,826 different
/zero drift**. Init492/492 and Debugger181/181 remain exact. Conversion totals
stay5505/6044 and86.08% bytes; README changes only the two matching rows.
The independently refreshed owner audit is **58/73 exact,15 still different**.
Roadmap recovery/matching items are checked off, not left as open work.

Next audit **func_15089F9C**,136 words/frame112, VA15089F9C..1508A1BC, ROM
B744C..B766C. Current placeholder has131 real differences. Inspect its cached
count/active mask, state/mask exclusions, slot-specific distance range,
clamped sine score and first strict-best result. It preserves S0..S7/FP and
F20..F30 and calls sinf; qualify saved lifetimes and helper-visible reads.
The sole aligned direct site is VA1509E4B8 /ROM CB968 with full-word A0 from
A2+8 in the delay slot, inside func_1509E3DC. The supplying2424E0.rodata.s is
already frozen. Start from this new owner/guard/ELF baseline, not Note1592's.

No host-port or frozen Release changes, Claude/REA calls, dependency installs or push.
The broad Game decomp/matching goal remains active.
