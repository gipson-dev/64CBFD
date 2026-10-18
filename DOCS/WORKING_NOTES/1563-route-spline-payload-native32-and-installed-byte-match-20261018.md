# Route Spline Payload Native32 And Installed Byte Match

Date: 2026-10-18. Consumer predecessor: `7c2e5d12`. Tools committed first as
`5f0358c`. Completes the same function from
[Note1562](1562-route-spline-payload-isolated-layout-match-and-private-padder-20261018.md).

## Installed Result

Replace `func_150896EC`'s zero-return placeholder with complete typed
`void func_150896EC(u8 *record,u8 *actor,s32 stop)` in generated_B3020.
The linked **305-word/frame248** routine is byte-exact throughout
VA150896EC..15089BB0 / ROMB6B9C..B7060. Its caller's local prototype is corrected
to void with three explicit arguments; the caller still emits identical code.

This is a normalized C match, not a direct compiler match: retain the qualified
305-word/frame248 raw C with140 differences and the closed Note1562 layout.
Append305 expected-word/binding rows, preserving the previous2,430,646 guard
bytes exactly. All305 C instruction origins remain present once, with no
insertions/omissions or frame change. No Makefile change or broad conversion.

Fresh `make -C conker match-progress NON_MATCHING=1` reports:

| Section | Byte-Exact | Different | Address Drift |
| --- | ---: | ---: | ---: |
| Total | 3,662 / 5,501 (66.57%) | 1,839 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,989 / 4,828 (61.91%) | 1,839 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversion counts stay fixed because the old placeholder already counted as
C. The root README changes only these verified aggregate rows, not function
narratives. All original assembly and previous experimental points remain.

## Native32 Qualification

The complete raw C passes **6,270 cases per O0/O2/O2+UBSan build** with four
real recovered C helper bodies: position, neighbor, enqueue and cubic. Their
source-span hashes are pinned, and the corresponding216 installed MIPS words
independently equal retail. Compare the full aligned80-KiB native arena and
complete helper call logs against a separate reference. Native position/cubic
logs compare values, not literal x86 private stack addresses.

The corpus retains the1,069 guest-reference cases, adds all256 channels times
20 queue cursors,80 effectful cases and the .625 heading witness. Five required
fired mutation gates exercise fresh enqueue objects, captured spline fraction,
live cached-position/heading fields, a changed original object's channel and
the post-initialization frame count. Candidate-side fired flags must agree
with the reference, and all five modes must actually execute.

Nine separately compiled negative C bodies fail through ordinary arena/call
differences, not compiler errors, traps or timeouts: wrong stop command, signed
channel, narrowed stop flag, wrong fraction decrement, float rather than double
scale, fresh channel object, prematurely cached channel, prematurely cached
frame count and reloaded spline fraction. Eight return23, narrowed stop22.

Use the existing native32/SSE/no-contract flags and explicit float32 reference
rounding. Memory is aligned, host-endian and pointer32; `-fno-strict-aliasing`
matches the raw-address source style. Only the unused extern declaration for
D_8009DA18 is removed from the GCC translation, not an executable operation.
Sin/cos are explicit finite-input lookup providers; positive runs require no
lookup misses. They are not claimed to be the retail trigonometric bodies.

## Installed Tests And Callers

**Twelve installed tests pass in82.642s, no skips.** They freshly cover:

- All305 linked words and33 independent retail assembly bindings; the pure
  layout still works with file reads disabled and retains305 unique origins.
- 1,069 compared guest states plus four stop-queue aliases, using four actual
  helpers and literal guest array/call addresses.
- 1,644 instruction-gated synthetic memory-prefix cuts, including1,084 in
  helper code, with equal compared registers/memory/events. These are not
  hardware traps, and no hardware FP status acceptance is claimed.
- Two independent complete data/call rebases,338 raw word/binding controls,
  87 recipe controls,12 invalid call rebases and the extrapolation dependency
  checks under their explicitly commutative finite-FP term policy.
- 100 connected executions through the real67-word dispatcher,305-word
  payload and216 helper words, across signed actor slots, both stack phases,
  initialized states and both modes.
- Actual mixed-profile padding and all seven expanded Make commands, correct
  primary/override flags,72 unchanged neighbors in both profiles, four retained
  GLOBAL_ASM bodies and the existing projection override.
- First prediction/installed audit, metadata-order negatives and three mixed
  source/guard/image stage rejections. The113-difference alternative still
  fails its private-memory witness and is not substituted.

A whole-Game retail-layout scan finds exactly two direct calls, both in
func_15087CC0:15087D6C and15087D8C. Their delay slots pass0 and1, and V0 is
overwritten immediately after each return. Unknown indirect interfaces,
undefined leading history, unmapped/misaligned native aliases, strict NaN
payload/FP exception equivalence and full hardware/gameplay behavior remain
outside the bounded C/native tests. The installed instruction identity is a
separate complete binary fact, not a claim of a universal symbolic C proof.

## Whole-ELF Prediction

The first actual link exposed three symbol/string ordering groups, not code
or data changes outside the target. Reconstruct only these named permutations:

- `(func_1500B3B0,D_8008D680,D_80088910)` becomes
  `(D_80088910,func_1500B3B0,D_8008D680)`.
- `(D_8009979C,D_800888E0)` exchanges order.
- `(func_150A7A14,D_8008891C)` exchanges order.

Structured ELF parsing verifies the original contiguous records and strings,
rebuilds their name offsets/records, and proves canonical named definitions
unchanged. No whole-section metadata exemption or copying is used. The first
predicted image is fingerprint-locked before installation. The production
build reproduces it exactly: **1,050 changed ELF bytes**, only target code/
extent plus these closed ordering changes.

Audit all **6,057 function addresses** and6,056 other function bodies as fixed;
preserve **189,088 protected Game-data bytes across720 owners**, with zero
different bytes/owners. Source/guard/image successor pins are:

- ELF: `15138e12aba5c25923d3438ff1db199d550accd18ad4596918a4b2ecd71ec8fd`.
- Owner: `a98ad9f3b781a4f93f39e45cbbe9646054c60c7b1d329bb5b2d21fb1499f7573`.
- Guards: `d9a994d78370af27db71af35f5639096bb0afc56e63b197b7bc6b19bffb7f902`.

The other19 members of the22-input capsule retain their predecessor hashes. A guarded
historical view preserves the earlier raw-source qualifications without
weakening their pins. Use the installed integration suite rather than invoking
an old predecessor-only fixture directly against the new production image.

The production build succeeds. Updating the shared manifest triggers dependent
recompilation and prints warnings in untouched C sources, as well as the
existing duplicate generated_12D630 recipe warnings. No warning-free build is
claimed; the target shadow compile has no new diagnostics. No host port or
frozen Release build/launch/modification, emulator session or Claude call.

## Repository And Next Work

Three repository-setup tests and smoke checks pass in both tools copies;
consumer `make tools-check` passes. Mirror only three absent, identical task
files, preserving all1,262 old dirty leaf hashes and the older standalone HEAD.
It now has1,265 dirty leaf paths and is not reset or committed. Commit primary
tools before the consumer pin, and do not push.

Reproduce from the prepared consumer root under WSL:

```sh
python3 -m unittest tools.tests.test_game_route_spline_payload_integration -v
python3 -m tools.experiments.game_route_spline_payload_integration --audit
make -C conker match-progress NON_MATCHING=1
```

Ignored `conker/build/game-route-spline-payload-integration/` retains the native
sources/binaries/receipts, first successor snapshots, private Make plan/objects,
prediction and installed audit. Earlier unchanged neighbor receipts are reused,
not described as fresh broad regression runs.

Next recover **func_15088F30**, the remaining83-word route XYZ output helper
still represented by a zero-return placeholder. Its existing walker caller
passes a record and three four-float output arrays. Keep this installed payload
fixed while recovering that helper; the wider Game matching goal stays open.
