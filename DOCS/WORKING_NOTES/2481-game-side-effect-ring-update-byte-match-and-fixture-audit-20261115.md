# 2481 - Side-effect ring update matched and fixture boundaries corrected

`func_1519F4F0` replaces its zero-return placeholder with the complete semantic
ring updater. Both padding paths emit all **192 retail words / 768 bytes**,
with the retail **0x78 frame**, **18 checked guards**, no inserted words and no
omissions. Raw C has 192 words and a 0x80 frame; the private-frame mapping and
ordinary-field scheduling adjustment are explicitly proved below.

Fresh production recount: total **4,511 / 5,514 (81.81%)**, Game
**3,838 / 4,841 (79.28%)**, Init **492/492**, Debugger **181/181**,
zero address drift, **1,003** still different. Exactly one new C match is
credited. At this denominator the 85% threshold is 4,687: **176 more** are
required. The wider goal remains active.

## Callback, records and behavior

Owner `generated_1CC440`, source `conker/src/game/generated_1CC440.c`, VA
`0x1519F4F0..0x1519F7F0`, code-image offsets `0x1CC9A0..0x1CCCA0`.
Baseline consumer `74d9ee54f39ee2b9233c4eedcc10d728dfef8292`, tools
`8159f5ebfeba1577c6ed180c98b373a0e74fd0e0`.

Recover `s32 func_1519F4F0(SideEffect1519F4F0 *effect)`. This is slot **5**
in `D_8008A200`, dispatched indirectly by the complete original
`func_15147740`. The table's 60 bytes match both the retail code image and the
current ELF. There are no direct JAL sites for this callback in the scanned
2,467,288-byte code image; this is not a complete asset-ROM/computed-call census.

The 0xA0-byte effect has unsigned capacity at +0x25, signed count/head/tail
bytes at +0x2C/+0x2D/+0x2E, three published coordinates at +0x54, the full
floor-query result at +0x60, captured entry base at +0x94 and payload at +0x98.
The payload is the 80-byte constructor record recovered in
[Note 2480](2480-game-side-effect-constructor-pointer-abi-and-byte-match-20261115.md).

| Entry offset | Recovered member |
| --- | --- |
| 0x00 / 0x04 / 0x08 | X / Z / height floats |
| 0x0C | Phase float |
| 0x10 / 0x12 / 0x14 | Signed alpha / delay / light halfwords |
| 0x16 / 0x1A | Retained halfwords |
| 0x18 | Signed lifetime halfword |
| 0x1C / 0x20 | X / Z velocity floats |

The stride is **0x24**. Capture both object pointers before the initial gate.
If count is below two and payload kind bit zero is set, return zero. Otherwise
walk backward from tail, wrapping negative cursors to capacity minus one.
Update lifetime, delay or alpha, phase and coordinates. Lifetime expiration
sets a flag; it does not skip the subsequent movement and query side effects.

Capture `D_800A8CF0` once when entering a nonempty traversal. Keep live tick
and time-scale reads at their retail points; query callbacks may change them.
Build `(x, height + 30, z)`, reject coordinates outside the cached bound,
otherwise query `func_15045800(position, 0, height - 30, result)`. Only a hit
copies result height into the entry. A miss or negative alpha also expires it.
Advance the live signed head toward an expired cursor, decrementing the live
count and wrapping at capacity; clear that head entry's alpha. Preserve every
reload around callbacks and byte/halfword truncation. Unsigned 32-bit arithmetic
keeps the retail low-word products/subtractions without C signed-overflow UB.

After traversal, accumulate payload +0x46 by signed payload +0x48 times the
live tick. The constructor's existing `zero46` member name is retained. Publish
head X/height/Z when count is positive, otherwise three positive zeroes, then
return one. Do not add new empty/null gates or early exits.

The query result is **36 bytes**, not a single output float: height, nine
vertex halfwords, retained halfword, metadata, flags/state, retained halfword
and value. The actual callee's definition establishes this complete extent.
Native size/offset assertions and complete byte snapshots cover it.

## Checked instruction equivalence

Selected O2/g3 C raw SHA-256:
`c4a7291bc1c3c2e49926dd3068f30e67d63877f9a0d67ea2507846e00018b34e`.
All nine bindings are pinned. Source/layout alternatives are retained privately;
none is installed or credited. No profile, inline assembly, shared header or
artificial C frame padding is introduced.

The 18 guards comprise two push/pop adjustments, six vector-home/address
adjustments, six internal F20/F22 role changes and four words of one independent
load permutation. The raw 0x80 frame and retail 0x78 frame both pass the vector
at exactly **incoming SP -0x20..-0x15**. Every exposed position byte is initialized;
no unknown stack bytes are created, removed or copied by normalization.

Twelve matching ABI save/reload pairs remain inside each complete private
frame, disjoint from the callback home area and the vector. The two single FP
values dominate every body use; entry/exit double-register saves remain in
their original ABI lanes. The control graph has **21 branch sites** and the
same targets in both streams. Local equivalence therefore composes through
all loop traversals, preserving provider arguments and ordered FP/FCSR effects.

The only ordinary access commute moves entry X's load past Z's MUL/ADD/store.
Their common base has disjoint offsets 0 and 4; F8 is unused by those three
instructions and neither modifies the base. No call or interior branch enters
the block. Arithmetic order stays fixed, including exceptional operands.

This is normal execution equivalence for valid aligned ordinary memory and
normal o32 providers. Public objects do not alias the callee's private stack.
Providers observe arguments/public memory/FCSR, not unpassed private homes,
internal saved registers or implementation PCs. Volatile/MMIO, concurrent
observers and **raw fault scratch identity are outside the claim**. Guarded
instructions restore retail's actual access/fault order; that emitted order is
checked separately. No instruction/data/metadata exclusion is used.

All 192 words emit. Exactly **187 are reachable**, and all execute in the
corpus. Preserved duplicate/unreachable offsets are 0x68, 0xFC, 0x1AC, 0x1E0
and 0x2B0. Two padders and two independent symbol rebases agree with retail;
201 changed-word/binding controls reject corrupted inputs.

## Fresh behavioral checks and corrected fixtures

- **4,085 cases per retail/raw/guarded stream** cover capacities 1/2/5/10 and
  signed-boundary 127/128 cases, wrapping counters, extreme ticks, expiration,
  delay/alpha, bound rejection, query miss/hit, live global/pointer mutations,
  machine aliases and modeled NaN/Inf operand rules. Both independent memory
  results and ordered FP operands agree.
- **283 native32 cases per six O0/O2/O3 strict/no-strict-aliasing profiles**,
  UBSan traps, actual typed objects and endian-normalized complete 160-byte
  effect, 80-byte payload and every 36-byte entry snapshot. Four semantic
  source controls at three optimizations fail. Native scope excludes the
  guest-only overlapping-storage and exceptional-operand stress cases.
- **432 complete original dispatcher cases per stream**, verified slot 5,
  result-dependent retirement and saved ABI state. The void dispatcher's
  scratch return is uncredited. **96 cases per stream** execute the original
  32-word height-query wrapper across all three valid routes; provider argument
  widths, threshold bits, result extent and fallback route are checked.
- **378 fired emitted memory cuts** compare retail with the exact guarded
  stream, including complete machine/private state. Opaque providers' internal
  accesses are not instrumented. Raw scheduling fault identity is not claimed.
- Primary preinstall/installed suites, both affected suites in an ignored
  sibling overlay, shared tools checks, actual Make, independent GNU ELF link,
  production/full-image audit and fresh recount pass.

An initial private fixture put payload at 0x40000, the emulator's stack base,
so its public filter hid payload bytes. The expanded alias corpus exposed a
saved-register overwrite in retail as well. Reject that initial fixture for
credit. The ring payload is now 0x60000 and alternate storage 0x70000, with
explicit disjoint-window assertions. The previous constructor fixture's output
also moved from 0x40000 to **0x80000**, making its allocation/payload public
to the filter. Its complete corrected suite passes in both tools copies before
adoption; the section-level production audit preserves its body and bindings.
No previous constructor body or guard changes, and no additional credit.

A separate native runner bug reused the baseline source-path variable in its
control loop. The next optimization therefore compiled the intentionally wrong
counter source. Its observed executable text exactly matches the reproduced
counter mutant (SHA-256
`2b8359bc6ebb90b2772afe5564fc82efd3fb1ffe3cff38641794e750aeba4c3d`).
The corrected `control_path` keeps baseline and mutant inputs distinct. The
passing six-profile result above uses the corrected runner. Original artifacts,
diagnostics and reproduction remain in `native-issue-before-fixture/`.

Behavioral reports now measure the live source installation state and compare
four production fingerprints before/after execution, replacing fixed private
status fields. Fresh guest reruns in both tools copies cover this reporting
change; the mathematical, native and caller inputs remain unchanged.

## Production checkpoint and next target

The **877-input** baseline changes only source, guards, owner object and ELF.
Only one of **698 objects** changes. All **38 owner neighbors**, **6,050 other
linked functions**, addresses, conversion rows, guard history and **189,088
protected data bytes** stay fixed. The complete ELF delta is **560 bytes**,
zero exclusions and no metadata permutations. ELF SHA-256:
`29d206f55163699565107bebaf610b9c9a383ddef1ca7292fd6370400e6fcd60`.

Primary tools commit **`50727d614d7925e8692e99834713557ff80b6666`** precedes the consumer pin. Eight task files
are tested through an ignored overlay; sibling HEAD
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, status fingerprint and all **2,434
dirty paths** remain unchanged. The 8-file scoped AST refresh retains all
**62,283 prior IDs**; it is not full-corpus extraction. No Claude calls or push.
The host folder still contains only `.codex` and `recomp_scene`; no host build
applies, and Release/saves/private inputs remain untouched.

Receipts are in `conker/build/game-side-effect-update-1519f4f0-private/`.
Reproduce the target suite with
`python3 -m unittest tools.tests.test_game_side_effect_update_1519f4f0_match -v`
under the prepared PSBBN environment. Preserve historical frozen and
qualified-private receipts. Five DOCS indexes get one concise entry; the main
README changes aggregate rows only.

Next: **`func_1519F7F0`**, the **415-word** remaining callback in this owner,
VA `0x1519F7F0..0x1519FE6C`, offsets `0x1CCCA0..0x1CD31C`, frame **0x118**.
It is slot 5 of the second callback table `D_8008A23C` (entry `8008A250`).
Read its complete body and actual interface before recovering it. No private
candidate for it exists; freeze the new committed baseline before edits.
