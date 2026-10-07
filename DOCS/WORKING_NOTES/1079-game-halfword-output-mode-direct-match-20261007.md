# Game Halfword Output Mode Direct Match

Date: 2026-10-07. Baseline: `a20021b7`,
[Note 1078](1078-game-cursor-updater-match-20261007.md).
Replace `func_151441A4`'s zero-return placeholder with its semantic leaf.
No shared headers, production-profile or padder-algorithm changes.

## Retail Contract

86 words /344 bytes, leaf, frame zero. VA `151441A4..151442FC`,
ROM `171654..1717AC`. Four signed-halfword output pointers and ten incoming
byte inputs occupy fourteen ABI argument positions. Inputs4..7 are the first
four-byte group; inputs8..11 are a direct group, input12 is scale, input13 is
mode. Argument7 is unused by this leaf but retains its ABI slot. Return type
is void; the original caller does not consume the transient v0 contents.

At entry, read the low bytes of the incoming mode word at SP0x37, scale word
at SP0x33 and first-group input0 at SP0x13, in that order. These reads happen
even in cases that do not use scale/input0. Mode is unsigned; modes>=5 select
the default without reading the jump table. Lower modes use the preserved
five-entry table at `jtbl_800A5648_game`:

| Mode | Destination | Behavior |
| --- | --- | --- |
| 0 | `151441F4` | Store fourth output0, reread it, then copy to outputs2/1/0 |
| 1 | `1514420C` | Store output2=0, reread it, copy to outputs1/0, then direct3 to output3 |
| 2 | `151441D0` | Read/store the four direct bytes in ascending output order |
| 3 | `15144228` | Reload scale/input0, scale the first three bytes, then output3=0 |
| 4 | `15144270` | Separate duplicate of the scaled-three/zero block |
| >=5 | `151442B8` | Scaled-three/zero using the cached entry scale/input0 |

Scaled output is `(input * scale) >> 8`, an integer product in0..65025,
result0..254. Preserve both repeated scaled cases and their extra stack reads.
For direct and scaled cases, later inputs are read after earlier output stores.
When guest output pointers overlap argument homes, those later input bytes can
change; scale remains cached after its initial/reloaded read. Keep byte narrowing,
four halfword stores, store ordering, zero-mode signed halfword rereads, and
the default's original final store/JR/NOP shape.

## Compiler Recovery

[Driver](../../tools/experiments/game_output_mode_candidates.py) retains96
case-order/chained-store/signed-product/shared-case controls over four profiles.
Exactly two forms match: selected case order2/0/1/3/4, chained zero propagation,
integer-promoted byte products and separate cases, under O2/g3 and O2.
The selected production profile remains O2/g3. Both O1 forms emit97 words,
frame0x8; they qualify bounded external-output behavior, not retail stack traces.

All86 instructions, branch destinations, registers, immediates, delay words and
five case offsets emit directly from C. Standalone linking initially placed
the input table eight bytes late because its ELF alignment overrode the requested
address; correcting the test script with SUBALIGN(4) yields the direct match.
The final96 measurements use the corrected link, not the one-word alignment
receipt. No production instruction normalization or frame patch is needed.

In the copied owner, the compiler appends this five-entry table at compact
pool offset624. The existing624-byte relocation-owned prefix is unchanged;
the new pool is656 bytes:20 table bytes and12 alignment bytes after the prefix.
The generated table matches all five original destinations. Two expected-word
and expected-relocation guards at offsets0x18/0x20 redirect its HI16/LO16 to
the preserved `jtbl_800A5648_game`, removing only the compact624-byte addend.
HI word stays `3C010000`; LO changes `8C2E0270` to `8C2E0000`, with the
original address supplied by relocation. No register/operation/control edit,
table rewrite, insertion or omission is involved.

## Qualification

[Eleven tests](../../tools/tests/test_game_output_mode_match.py):

- 65536 paired raw-C/retail guest cases cover all256 mode bytes,16 distinct
  input patterns, eight output-alias layouts and two stack phases. Complete
  memory, ordered reads/writes, register state and saved GPR/FPR state agree
  with an independent reference. All86 retail words are executed.
- 24576 guest argument-home overlap cases qualify live later bytes, cached scale,
  mode snapshots and ordered halfword stores. A separate256-mode unmapped-slot
  check proves argument7 is never read.
- 3584 additional cases exhaust all256 unused input7 bytes, poisoned high words,
  all switch/default paths and distinct/identical output pointers.
- Minimal mapped fixtures require only the selected input bytes. Mandatory entry
  reads, case-specific bytes, selected table entry and output writes fail closed
  when unmapped. Modes>=5 work with the entire table unmapped.
- 557056 actual freestanding32-bit native calls cover all mode bytes, eight
  output-alias layouts, fourteen-position typed calls and all65536 byte products
  across modes3/4/5/255 and distinct/identical outputs. Full16-halfword arrays
  retain their untouched guards. Native tests do not claim guest argument-home
  alias behavior: ordinary C parameters are passed by value.
- 2048 cases execute the original25-word setup/call/delay fragment from
  `func_1515BBF0`, starting at `1515BC10` (ROM `1890C0`). Four output halfwords
  at caller-stack0x70/0x6E/0x6C/0x6A and ten bytes from object0x20..0x29 are
  staged; the final SW argument13 occurs in the JAL delay slot at `1515BC70`.
  Calls, complete memory and ordered traces match both connected bodies.
  Earlier context and return scaffolding are seeded/synthetic, not a whole caller.
- Four profile controls cover2048 bounded mode/alias cases. Six compiled negatives
  detect full-word mode, wrong shift/direct/fourth input, nonzero scaled fourth,
  and removal of the original zero-mode reread. That last control is detected
  by the read trace, not by a claimed changed final output.
- Copied owners preserve89 symbols, all88 neighbors' bytes/relative relocations,
  prior normalized pool bytes/identities and the same two existing warnings.
  Only the appended table/padding is new. Raw target agrees with standalone
  after normalizing its table addend.
- Actual owner post-processing/padding/linking emits all86 retail words. Two
  alternate addresses exercise HI16 carries; stale expected words and relocation
  metadata fail closed. The linked retail table is not rewritten.
- Production source, complete slot, table owner and historical guard prefix are checked.

Ten pre-install tests pass in29.674 seconds, no skips/errors/failures. The native
fixture's loop formatting was corrected under warning-as-error, and the first
zero-elision negative was replaced because IDO retained the original reread.
The16 input patterns were made distinct and checked before final qualification.
These tests do not prove complete callers, hardware execution, gameplay or
host-port adoption.

## Neighboring Pool Checks

Extend the context/point checks for the measured656-byte pool and validate the
five appended targets and exact relocation offsets. The cursor receipt now
reports the actual measured pool length rather than a historical constant.

The resolver's copied baseline removes its own24-byte table, moving the later
output table from624 to600. Its test now explicitly checks just that LO addend
change in the otherwise-identical output neighbor, preserving both relocation
identities, all other bytes, the first600 pool bytes and the later table's
normalized owner/case identities. Exact new padding is checked. This is not
a generic relaxation for arbitrary neighbor or pool changes. Production binds
both tables to their original owners; the linked audit must still change only
the newly recovered output leaf.

## Production Audit

US ELF rebuild passes. Across all6059 linked slots, only `func_151441A4`
changes. Every address/extent and protected `.init`, `.init_data`, `.debugger`
and `.game_data` section is unchanged. All720 Game-data owners /189088 bytes
remain exact. Prior10912 guard rows are pinned unchanged; two new table
bindings total10914 guards. The original five-entry table remains byte-exact.

Matching: total3351/5465 exact (61.32%), Game2678/4792 (55.88%),
2114 different, zero address drift. Conversion stays total5465/6042 (90.45%),
Game4792/5321 (90.06%); the placeholder was already counted as C. README updates
aggregate matching rows only. All153 post-link regression tests pass in578.698
seconds, zero skips/errors/failures.61 documents/3690 relative links/zero broken;
project tool, Python syntax, whitespace and final post-regression linked audit
checks pass.

## Resume

Next forward placeholder `func_151442FC`:120-word leaf,
VA `151442FC..151444DC`, ROM `1717AC..17198C`, frame zero. Its fourteen-input
shape resembles this leaf, but argument7 is now live and the unsigned switch
has14 entries at `jtbl_800A565C_game`. Destinations for modes0..13 are
`15144368`, `15144380`, `15144324`, `15144324`, `151443D0`, `151443FC`,
`15144428`, `15144398`, `151443B4`, `15144494`, `1514444C`, `15144470`,
`15144398`, `15144348`. Preserve genuinely shared modes2/3 and7/12, separate
duplicated product cases4/5, and the default's cached scale, output2/1/0
stores, direct3/input3 read order and shifted fourth-output product.
At entry only mode at SP0x37 and scale at SP0x33 are read unconditionally.
This is original assembly/table inspection, not a semantic recovery or test.

Original `func_1515BBF0` stages its next four outputs and calls this leaf at
`1515BCD0` (ROM `189180`); inspect setup after the preceding output call.
Sampler `func_151432BC` still needs two path-local exits/circle-byte scheduling;
oriented `func_15142600` still has27 private-layout differences. Neither is
installed. No sibling/frozen Release/save/runtime or push work.

Ignored receipts:`conker/build/game-output-mode/` and
`conker/build/game-output-mode-test/`. The broader matching goal stays active.
