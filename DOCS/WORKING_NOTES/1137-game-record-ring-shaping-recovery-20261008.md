# Game Record Ring Shaping Recovery

Date: 2026-10-08

## Result And Banking

Continue [Note 1136](1136-game-record-ring-sampling-conversion-20261008.md)
under the [focused workflow](../AGENT_WORKFLOW.md). Recover the complete
retained `func_151D7CD0` as an **uninstalled candidate**, not a conversion or
byte match. Retail is **253 words / 1,012 bytes / frame 0xB8**, at VA
0x151D7CD0..0x151D80C4, ROM 0x205180..0x205574. The natural O2/g3 body is
**256 words / frame 0x98 / 253 raw differences**. The real padder rejects its
0x400-byte body in the 0x3F4-byte slot. Keep the original directive in
[generated_204660.c](../../conker/src/game/generated_204660.c), the complete
[slice](../../conker/asm/204660.s) and
[function assembly](../../conker/asm/nonmatchings/generated_204660/func_151D7CD0.s).

Per "Keep commited", bank the two new tools files in mounted tools commit
**856ba006efda6d15766e0071ebebfffcd162e1e7**, then commit this handoff and the
exact consumer gitlink. Parent entry baseline is c08defd9; tools entry
baseline is 9fb0eb2. Mirror only the two new reviewed files to the older
standalone tools checkout, preserving its ddbdd16 HEAD and all independent
dirty work. No duplicate standalone commit, reset, stash or push.

No production source, data, compiler-profile, layout, guard or progress edits.
README aggregate tables remain correct and unchanged. Converted **5,480 /
6,042**, Game **4,807 / 5,321**; exact **3,391 / 5,480**, Game **2,718 /
4,807**; zero address drift and 2,089 still different. All 11,205 existing
guards remain unchanged; no target guards added.

## Recovered Contract

Read signed state at owner+0x2C, unconditionally capture payload+0x98 and
buffer+0x94, and skip working-field accesses/calls when state is below 2.
Retail's inactive branch still performs an unused private stack load; this
does not establish portable uninitialized C arithmetic.

The first do-at-least-once pass traverses 28-byte records backwards from the
signed current byte+0x2E, wrapping negative indices using unsigned count+0x25.
Flag mask 0x0002 selects owner XYZ+0x10 as the first previous position; otherwise
step backwards once to select a previous record before traversing.
Construct a private three-float difference vector and call the magnitude
helper. Store each returned length at record+0x10 and accumulate a float total.

For total strictly above 80.0f, reload the stored length. If nonzero, trim XYZ
and length using **(total - 80.0f) * (1.0f / length)**, with separate float
rounding. Retail reads the next axis before storing the preceding axis;
the independent retail trace model preserves that pipeline. Set total to 80,
then increment/wrap the live signed goal byte+0x2D and decrement live signed
state until goal reaches the traversed index. Test the live goal after every
iteration and reload state after the complete pass.

When freshly reloaded state is at least 2, update captured payload phase+0x18
by -41.0f * live D_800BE9A4, then wrap it between -16384.0f and the live
upper constant. Traverse again using a fresh current byte. Accumulate stored
lengths, scale by live D_800AB2E0, add the live captured payload phase, call
the wrapper and store each point's phase at +0x18. Preserve mixed ABI
F12/F14/A2 argument bits and F0 return. Reload goal after each call and state
after the complete pass.

When fresh state remains at least 2, derive fade start and width from the
saved total and live D_800AB2E8. Traverse once more from fresh current. Store
byte +0x14 as 60 before fade start; otherwise clamp the distance difference
to width and convert the float fade through the retail **unsigned 32-bit**
conversion sequence before taking its low byte. Advance distance using the
stored point length. Always return 1.

Payload and buffer pointers remain captured even when callees mutate owner
pointers. State, goal, current, count, phase, scale and delta retain their
individual live/captured lifetimes. Signed-byte cursor arithmetic is not
interchangeable with unsigned count or unsigned fade conversion.

## Proven Caller And Helpers

The target is **third-table callback index 4**: D_8008A284+0x10 at 0x8008A294,
ROM 0x22ED54. The earlier test setup incorrectly treated it as second-table
index 22; the complete original dispatcher rejects second indices >=18.
Correct the fixture rather than changing the original dispatcher or table.

Execute all 100 original words of `func_15147740` in the bounded connection:
timer gate off, first and second kinds zero, player gate flag 0x10 on,
signed player byte+0x24 equal to 4. The dispatcher invokes this target,
consumes its true return and avoids the release hook. Its linked C routine
is still a placeholder; this does not restore that dispatcher or qualify
other branches, release behavior or gameplay.

`func_15143E64` is the complete 12-word rounded XYZ magnitude routine,
VA 0x15143E64 / ROM 0x171314, using direct sqrt.s. `func_15144528` is the
complete 28-word/frame0x10 wrap routine, VA 0x15144528 / ROM 0x1719D8.
Both current linked bodies match their full original words and execute in
the connection test, rather than being replaced there by numeric hooks.

## Fitting And Qualification

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_ring_shaping_candidates.py)
screens 28 complete forms and four profiles, with no isolated compiler
diagnostics or data pools. Meaningful variants use byte stride, a vector
structure, phase-local lifetimes and declaration placement. No dead locals,
padding, filler, assembly substitution or proposed guards.

| Natural Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 256 | 0x98 | 253 |
| O2 | 255 | 0x98 | 208 |
| O1/g3 | 341 | 0x50 | 329 |
| O1 | 341 | 0x50 | 329 |

The valid byte-stride form emits 252 words/frame0x90/215 differences;
byte-stride with phase locals emits 252/frame0xA0/213 differences. The
253-word live-buffer form is an **effective negative**, not a fitting success.
Reassociated division is also an effective negative: returned length
91.99920654296875 yields trimmed length 80.00000762939453 with the recovered
reciprocal product, versus 80.0f with direct division.

[Seven focused tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_ring_shaping_recovery.py)
pass in **71.119s** after correcting the fixture import, retail trim access
pipeline, callback table and copied-owner asm postprocessing:

- 1,861 bounded guest cases compare raw C and retail public memory, call
  arguments and result with an independent model. Cover all 256 state,
  current and count bytes, inactive goal bytes, two SP phases, ten callee
  mutations, three buffer layouts, phase endpoints, trimming and clamp cases.
- The full guest bodies reach 248/253 words. An additional 84 fragment cases
  reach all 32 unsigned-conversion words, including signed fallback, sentinel
  and FCSR save/restore. The combined coverage leaves only +0x128 unexecuted;
  no full-body reach or hardware FCSR flags/traps/RM/NaN-payload claim.
- 66 required retail fault-prefix cases and three lazy layouts compare
  independent partial public state/trace. Raw-C fault-prefix, private GP/FP
  and raw access-trace identity are explicitly not claimed.
- 17 ordinary forms pass 425 executions; all eleven deliberate wrong forms
  discriminate. An extra actual ABI call is a witness for invalid loop
  controls, not an instruction-budget timeout or unsupported-opcode result.
- 48 connected cases / 96 executions run real helpers and the complete
  original dispatcher across raw C and retail, consuming callback 4's result.
- Copied, asm-postprocessed owners preserve all 22 other routines, relative
  relocations, normalized pools and four existing diagnostics. Isolated and
  copied target bytes/relocations agree. The real padder accepts the baseline
  and rejects the oversized candidate without truncating or installing it.

Zero-length controlled returns keep byte-boundary fixtures out of unreachable
pruning domains. Count zero and signed negative indices use explicitly mapped
guest storage. Negative length controls exercise the clamp/invalid-conversion
model, not a claim about the real magnitude helper. Nonterminating active
goal/current/count combinations are not repaired. Native32 qualification and
independent symbol rebases remain pending; no ISO C or live-gameplay claim.

Fresh checks: nine shared matcher/padder/repository-setup tests, mounted and
standalone project checks, CLI help and Python syntax. Fresh baseline audit
preserves all 6,058 linked bodies/addresses/extents, protected sections,
game data, progress rows and all guards. Source/assembly/Makefile/progress/CSV
fingerprints equal entry. The older sampling and neighbor suites were not
rerun; their unchanged receipts remain historical, not fresh tests here.

Scoped documentation validation passes: 123 documents, 4,047 relative links,
zero broken links and 35 relevant mounted/standalone tools files identical.
The older standalone status differs only by the two new mirrored files.

Ignored evidence is under `conker/build/game-record-ring-shaping-test/`:
slot.json, guest.json, faults.json, conversion.json, controls.json,
connected.json, owner.json and baseline.json. Screens remain under
`conker/build/game-record-ring-shaping/`; installed baseline remains
`conker/build/game-record-ring-sampling-test/after.json`.

Graphify query ran before investigation. Fresh `graphify update .` refuses
16,800 new nodes versus 38,589 existing nodes and retains 19,398 nodes from
2,972 files outside the new corpus. Preserve the refusal; no force, install
or ignore-rule change. No host/runtime/save/editor changes; OGL Release frozen.

## Resume Steps

1. Keep this complete target active; start from the valid byte-stride and
   phase-local forms. Recover retail frame0xB8, vector SP+0x98 and total
   SP+0xAC through meaningful used-variable lifetimes. Natural C saves F26
   for zero, while retail saves only F20/F22/F24; investigate that lifetime.
2. Add bounded native32 finite-domain qualification. Preserve float grouping,
   signed-byte updates, captured pointers and effective negative controls.
3. Fit the complete 253-word extent and saved-register lifetimes before
   proposing closed guards. Qualify actual padding and independent symbol
   rebases, then exact private state/access behavior for any normalized body.
4. Only then install the target, rebuild, audit against the unchanged sampling
   baseline and refresh measured progress. Bank tools first, source/docs/pin
   second. Keep linked dispatcher restoration, hardware/gameplay and the
   reduced-corpus graph repair separate.
