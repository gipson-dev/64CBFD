# Game Fixed-Point Cursor Updater Match

Date: 2026-10-07. Baseline: `a0631401`,
[Note 1077](1077-game-actor-gated-packet-match-20261007.md).
Recover `func_1514401C` from its zero-return C placeholder. No shared-header,
production compiler-profile or padder-algorithm changes.

## Retail Contract

98 words / 392 bytes, leaf, frame zero, VA `1514401C..151441A4`,
ROM `1714CC..171654`. Low-u8 index and flags, two word pointers, word return
zero or one. The original prologue stores the complete incoming index/flags
words in caller argument homes before narrowing them; retain that behavior.

Read the live tick word `D_800BE9E4`, velocity, the single unsigned byte at
`D_80090B64 + index * 12`, and cursor in that order. The local 12-byte count
view overlaps the existing texture table's byte4; it is not a new data owner.
Compute `limit = (count << 16) - 1`; advance and store the cursor with the
low32 bits of `position + velocity * ticks`. Keep unsigned modular arithmetic
for multiplication, addition, wrapping and negation.

If the updated cursor exceeds the signed limit, choose the first mode:

| Flag | Upper Action |
| --- | --- |
| `1` | Return1, leaving the advanced cursor and velocity |
| `2` | Store velocity0, then cursor=limit |
| `4` | Store cursor=limit minus signed remainder, reread and negate velocity |
| None | Repeatedly subtract limit and store each cursor while cursor > limit |

Otherwise, if the advanced cursor is negative:

| Flag | Lower Action |
| --- | --- |
| `8` | Leave the negative cursor and velocity, return0 |
| `16` | Store velocity0, then cursor0 |
| `4` | Store cursor=wrapped negation modulo limit, reread and negate velocity |
| None | Repeatedly add limit and store each cursor while cursor < 0 |

Normal returns are0 for every mode except upper flag1. The upper limit comparison and
upper wrap continuation are strict. Preserve the separate lower branch,
mode priority, each intermediate wrap store, and the reflection velocity
reread after storing the cursor. Identical velocity/cursor pointers therefore
have materially different behavior from caching velocity at entry.

## Trap Boundary

All256 possible count bytes yield either -1 or a positive limit, never zero.
Both BREAK7 zero-divisor paths are unreachable. The upper BREAK6 overflow
path is also unreachable: count0 is needed for divisor-1, but the upper gate
excludes numerator INT_MIN. Lower reflection with count0 and updated INT_MIN
does reach BREAK6, unless lower flags8/16 bypass it. The original MFHI,
cursor store and velocity reread precede that trap.

The guest oracle uses remainder/HI0 for INT_MIN divided by -1 as a bounded
model convention, not a hardware HI claim. Native tests exclude invalid
division; the source's signed remainder overflow is not a portable defined-C
operation. IDO's generated original DIV/guard sequence is retained, not repaired.
Long count0 wrap paths are neither repaired nor generally executed here;
only short modular boundary cases are qualified.

## Compiler Recovery

[Driver](../../tools/experiments/game_cursor_updater_candidates.py) retains131
measurements across declaration/initialization controls, five selected profiles,
loop assignment forms, result/flow controls, table/wrap shapes, compound stores,
signedness/register qualifiers and explicit temporaries. No direct exact form
was found. O2/g3, including its no-unroll control, emits98 words/frame0 with46
differences. O2 without g3 emits100 words; both O1 controls emit122/frame0x10.
Alternate controls are bounded behavior screens, not installed candidates.

The initial recovery missed a lower-loop copy because its experiment generator
used the upper loop's indentation when replacing the lower loop. Correcting
and asserting the transformations recovered the full98-word shape. The final
131 measurements and qualification use the corrected generator, not the
obsolete97-word receipts.

Selected C stores then rereads the initial cursor and each loop cursor.
This recovers both retail loop copies and branch-delay updates directly.
52 words match directly;46 expected-word guards normalize only temporary
register operand fields and the commutative opening addition's operand order.
All instruction opcodes/functions, shifts, immediates, branch targets, frame,
load/store base registers and four HI16/LO16 identities/locations remain
unchanged. There are no inserted, omitted, reordered or frame-fixing words.

Register roles change by lifetime, so one global register renaming is not the
proof. Static field masks reject any non-register change. Paired instruction
operand traces compare actual arithmetic/division inputs, HI/LO results,
memory addresses/values, branch inputs and return targets at the same PCs.
Only truly commutative operands are sorted for comparison.

## Qualification

[Eleven maintained tests](../../tools/tests/test_game_cursor_updater_match.py):

- 18944 paired raw-C/retail guest cases exhaust mode bytes and index low bytes,
  limits, strict boundaries, distinct/identical pointers and two stack phases.
  Independent results, complete final mapped memory, ordered public reads/writes,
  full incoming argument homes and saved GPR/FPR state agree.
- 3500 modular-extreme cases cover INT_MIN/INT_MAX, product/add/sub/negation wrap,
  tick/velocity aliases and caller-stack pointer storage, with full memory/trace.
- 1024 count0 cases include64 natural modeled overflow traps, preserving the
  pre-trap store/read order. All95 reachable retail words are covered. Dead
  words are `151440D4`, `151440EC`, and `15144160`, justified by the valid count
  domain rather than claimed as executed.
- 11776 additional paired instruction traces check live operand equivalence
  across all95 reachable words, including loop and trap paths.
- Lazy table access requires only the selected byte. Missing required tick,
  pointer or table input fails closed; table/cursor overlap is checked.
- 20182 actual freestanding32-bit native calls cover every mode byte, pointer
  aliasing and unsigned arithmetic extremes. Invalid signed division is excluded.
- 192 cases execute nine original setup/call/delay/status-mask instructions
  from `func_1515BAE0`, starting at `1515BB68` (ROM `189018`), connected to both
  bodies. Pointer fields are object `0x1C`/`0x18`, index `0x10`, mode `0x12` in
  the JAL delay slot; the returned word is masked to u8. Earlier context and
  return scaffolding are seeded/synthetic, not a complete caller qualification.
- Five compiler profiles preserve bounded public behavior. Six compiled
  negatives detect missing tick scaling, inclusive upper comparison, wrong
  reflection, wrong mode priority, cached velocity and wrong lower-stop flag.
- Copied owners retain89 symbols, all88 neighbors' bytes/relative relocations,
  the relocation-owned624-byte pool and the same two existing warnings. Raw
  target bytes/four relocations agree with standalone C. Actual guarded padding
  and linking emit all98 retail words. Alternate global addresses exercise
  HI16 carry; stale expected words and stale relocation metadata fail closed.
- Production source, complete linked slot and historical guard prefix are checked.

Ten pre-install tests pass in24.806 seconds, no skips/errors/failures. Synthetic
table fixtures exercise all index bytes; this does not establish real asset
table bounds. These are bounded instruction/native checks, not complete caller,
hardware division, gameplay acceptance or host-port adoption.

## Production Audit

US ELF rebuild passes. Across all6059 linked slots, only `func_1514401C`
changes. Every address/extent and protected `.init`, `.init_data`, `.debugger`
and `.game_data` section remains unchanged. All720 Game-data owners /189088
bytes remain exact. The prior10866 guards are pinned unchanged;46 new checked
register-field guards total10912.

Matching: total3350/5465 exact (61.30%), Game2677/4792 (55.86%),
2115 different, zero address drift. Conversion stays total5465/6042 (90.45%),
Game4792/5321 (90.06%); the placeholder was already counted as C. README updates
only aggregate matching rows.

All142 expanded post-link regression tests pass in672.201 seconds with zero
skips, errors or failures, including all eleven new cursor-updater tests.
The original caller-fragment check was strengthened after pre-install testing
to compare full memory and ordered reads/writes, including the original delay
load and synthetic return read; it passes in this final suite. Final tool,
syntax and diff checks pass. Documentation:60 documents /3679 relative links /
zero broken links. Final post-regression linked audit again confirms that only
the target changed, with no address/extent/protected-data drift and all10866
historical guards unchanged. No sibling/frozen Release/save/runtime or push work.

## Resume

Next forward placeholder `func_151441A4`:86-word leaf,
VA `151441A4..151442FC`, ROM `171654..1717AC`. Original inspection shows four
halfword output pointers, incoming stack byte values through argument13,
an unsigned five-entry mode table at `jtbl_800A5648_game`, direct/zero/scaled
output paths and ordered stores that can alias. Recover all fourteen argument
positions, exact jump-table destinations and lazy stack-byte reads before
choosing the semantic ABI. This is static inspection, not a recovery or test.
The preserved data table's five destinations are `151441F4`, `1514420C`,
`151441D0`, `15144228`, `15144270` for modes0..4. They select all-zero,
three-zero/fourth-byte, four direct bytes, and two separate scaled-three/zero
blocks. Unsigned modes>=5 use the inline scaled-three/zero default at
`151442B8`. Keep the two duplicated scaled blocks until their retail read
schedules are understood. Entry unconditionally reads mode at SP0x37, scale
at SP0x33 and the first scaled byte at SP0x13; do not assume all unused case
inputs are lazy. Argument7 at SP0x1C is not read by this leaf, but occupies
an ABI slot. Stores followed by signed halfword rereads in zero modes must
retain pointer-alias behavior.

Original caller `func_1515BBF0` stages ten bytes from object0x20..0x29 into
SP0x10..0x34 and calls at `1515BC6C` (ROM `18911C`), with the last input store
in the delay slot. Its four outputs are caller-stack halfwords at offsets
0x70/0x6E/0x6C/0x6A. Inspect setup from `1515BC10` before connecting the
fragment; this turn only inspected assembly, not caller execution.
Sampler `func_151432BC` still needs two path-local exits/circle-byte scheduling;
oriented `func_15142600` still has27 private-layout differences. Both stay
uninstalled. No sibling/frozen Release/save/runtime or push work.

Ignored receipts: `conker/build/game-cursor-updater/` and
`conker/build/game-cursor-updater-test/`. The broader matching goal stays active.
