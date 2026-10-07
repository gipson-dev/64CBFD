# Game Secondary Halfword Output Direct Match

Date: 2026-10-07. Baseline: `e41fd0b2`,
[Note 1079](1079-game-halfword-output-mode-direct-match-20261007.md).
Recover `func_151442FC` from its zero-return placeholder. No shared headers,
production compiler profiles or padder algorithms are changed.

## Retail Contract

120 words / 480 bytes; leaf, frame zero.
VA `151442FC..151444DC`, ROM `1717AC..17198C`.
Four signed-halfword output pointers and ten incoming bytes occupy fourteen
ABI argument positions. The first and direct groups each contain four bytes,
followed by scale and mode. Unlike the preceding leaf, argument 7 is live.
Return type is void: the inspected original caller does not use the leaf's
transient v0 contents.

Entry always reads mode at SP0x37 and scale at SP0x33, in that order.
No first-group byte is unconditionally read. Unsigned modes >=14 take the
default without a table read. Lower modes use `jtbl_800A565C_game`:

| Modes | Destination | Outputs |
| --- | --- | --- |
| 0 | `15144368` | Fourth=0; reread it, then copy to outputs2/1/0 |
| 1 | `15144380` | Reload scale; fill outputs2/1/0, fourth=0 |
| 2, 3 | `15144324` | Four first-group bytes, read/store in output order |
| 4 | `151443D0` | Reload scale; fill outputs2/1/0, fourth=first3*direct3>>8 |
| 5 | `151443FC` | Separate duplicate of mode4 |
| 6 | `15144428` | First three first-group bytes, fourth=direct3 |
| 7, 12 | `15144398` | Third=0; reread/copy to outputs1/0, fourth=direct3 |
| 8 | `151443B4` | Third=0; reread/copy to outputs1/0, fourth=first3 |
| 9 | `15144494` | Reload scale; fill outputs2/1/0, fourth=direct3 |
| 10 | `1514444C` | Four direct bytes |
| 11 | `15144470` | First three direct bytes, fourth=first3 |
| 13 | `15144348` | First three first-group bytes, fourth=0 |
| >=14 | `151444B0` | Cached scale fill, fourth=first3*direct3>>8 |

Preserve the genuinely shared 2/3 and 7/12 cases and the separate 4/5 blocks.
Later input-byte reads occur after earlier output stores. Product paths read
direct3 before first3; scale stays cached through the stores. Products are
integer-promoted byte values in 0..65025, shifted results in 0..254.
The default stores its fourth result before JR/NOP; other paths retain their
retail return-delay stores. Zero paths retain the signed halfword reread.

## Compiler Recovery

[Driver](../../tools/experiments/game_secondary_output_candidates.py) retains
96 case-order/chaining/product-order/shared-product controls over four profiles.
The screen passes in 48.734 seconds. Only the selected form under O2/g3 and its
O2 control match all 120 words directly. O1 variants emit 140 words/frame0x8;
their bounded external-output behavior is tested, not their argument-home traces.

Standalone code and all fourteen table destinations are direct matches.
The production O2/g3 profile is unchanged. No instruction, register, schedule,
frame, branch, insertion or omission normalization is necessary.

The copied owner previously had 644 meaningful pool bytes and 12 alignment
bytes, total656. The compiler starts the new fourteen-entry table at offset644,
reusing the old trailing alignment area. The resulting704-byte pool contains
the preserved644-byte payload,56 table bytes and4 zero padding bytes.
All old relocation-owned identities remain unchanged.

Two expected-word/expected-relocation guards bind the original table owner:
offset0x14 HI16 keeps `3C010000`; offset0x1C LO16 changes `8C2E0284` to
`8C2E0000`. Both switch from compact .rodata to `jtbl_800A565C_game`;
only the compact644-byte addend is removed.

## Qualification

[Eleven tests](../../tools/tests/test_game_secondary_output_match.py):

- 65536 paired guest cases: all256 modes,16 distinct patterns,8 output-alias
  layouts and2 stack phases. Complete mapped memory, ordered reads/writes,
  registers and saved state match an independent reference. All120 words run.
- 24576 argument-home overlap cases preserve mode/scale snapshots, live future
  bytes, product read order and ordered halfword stores.
- 4096 live-argument7 cases exhaust its low byte with poisoned high words across
  every path that reads it and distinct/identical output pointers.
- Minimal mapped fixtures check unconditional mode/scale reads, selected live
  bytes and lazy first-group reads. Defaults work with the full table unmapped;
  required bytes, selected table entries and output writes fail closed.
- 557056 actual freestanding32-bit native calls cover all modes/output aliases,
  fourteen-position typed calls, independent scale patterns, and all65536
  first3/direct3 products across modes4/5/14/255 and two output-alias layouts.
  Complete16-halfword arrays retain untouched guards. Native C parameters are
  by value; native tests do not claim guest parameter-home alias semantics.
- 8192 connected cases execute the original50-word caller fragment beginning
  `1515BC10` / ROM `1890C0`. Both recovered leaves are connected. The first
  call uses object mode0x29 and output homes0x70/0x6E/0x6C/0x6A; the second uses
  mode0x2A and outputs0x68/0x66/0x64/0x62. Both final mode SWs are JAL delays.
  Full memory, both fourteen-argument vectors and all staging/leaf reads/writes
  match. Earlier context and return scaffolding are seeded/synthetic.
- Four profiles pass2048 bounded mode/alias cases. Six compiled negatives detect
  full-word mode, wrong shift/fourth/scale/direct input, and zero-reread removal.
  Final detections:90/24/32/48/16/8. Zero-reread removal is a trace-only failure.
- Copied owners preserve89 symbols,88 neighbors' bytes/relative relocations,
  two existing warnings, the meaningful prior pool and all its owner identities.
- Actual padder/link controls produce120 retail words and exercise two alternate
  HI16-carry addresses. Stale expected words and relocation metadata fail closed.
- Production source, complete linked slot/table and historical guards are checked.

Ten pre-install tests pass in30.566 seconds, zero skips/errors/failures.
Thirteen focused post-link tests pass in39.082 seconds, including all eleven
new tests and both affected earlier-table copied-owner checks, no skips/errors/failures.
The initial negative fixtures could not detect wrong shift or scale because
one product was zero and reused patterns correlated input0 with scale. The
fixture now separates scale and uses four negative-test patterns; all six
deliberately wrong compiled forms are detected. This corrects qualification
coverage, not production behavior.

No full-caller, hardware execution, gameplay or host-port adoption claim.

## Neighboring Pool Checks

The context-owner check pins all175 table targets, exact relocation offsets,
704 pool bytes and4 final padding bytes. Point/cursor checks preserve normalized
owner pools and raw neighbor metadata.

Copied baseline tests that remove earlier tables must move later compact
addends. Removing the resolver's24-byte table shifts the first output table
624->600 and secondary table644->620. Removing the first output's20-byte table
shifts the secondary table644->624. Tests pin each original/replacement LO word,
all other neighbor bytes and relative relocations, meaningful normalized pool
bytes, every moved owner/case identity and exact final padding.
No generic allowance for neighbor or linked-data drift is added.

## Production Audit

US ELF rebuild and linked audit pass. Only `func_151442FC` changes across all6059
slots. Every address/extent and protected .init/.init_data/.debugger/.game_data
section is unchanged. All720 Game-data owners/189088 bytes remain exact.
All10914 prior guards are pinned unchanged; two new table bindings total10916.
The original fourteen-entry table remains byte-exact.

Matching: total3352/5465 exact (61.34%), Game2679/4792 (55.91%),2113 different,
zero address drift. Conversion stays total5465/6042 (90.45%), Game4792/5321
(90.06%); the placeholder already counted as C. README updates aggregate rows
only. All164 post-link regression tests pass in736.713 seconds, zero skips/
errors/failures.62 documents/3701 relative links/zero broken; project tools,
Python syntax, whitespace and final post-regression linked audit checks pass.

## Resume

Next forward placeholder: `func_15144CEC`,101 words/frame0x48,
VA `15144CEC..15144E80`, ROM `17219C..172330`. Original assembly inspection
shows optional output pointers with three stack-local fallbacks, a call to
`func_150A7A00`, floating bound/zero gates, reciprocal depth, and a two-coordinate
update using live view data. Recover ABI, private locals, lazy paths, saved s0
lifetime and floating read/order behavior before installing it.
This is inspection only, not a C recovery or qualification.

Sampler `func_151432BC` exits/circle-byte scheduling and oriented
`func_15142600`'s27 private-layout differences remain open.
No sibling/frozen Release/save/runtime or push work. Broader matching goal active.

Ignored receipts: `conker/build/game-secondary-output/` and
`conker/build/game-secondary-output-test/`. The initial probe/screen wrappers
are under `conker/build/game-output-mode-test/secondary_*.py`.
