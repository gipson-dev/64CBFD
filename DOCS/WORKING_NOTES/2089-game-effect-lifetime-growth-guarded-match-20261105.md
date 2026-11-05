# Game effect lifetime growth guarded match (2026-11-05)

## Outcome and acceptance boundary

`func_151A25E0` replaces a false zero-return placeholder with a complete void
effect callback. The natural C body has 67 words, no frame, and the original
two timestep relocations. A derived transformation of ten temporary GPR
lifetimes, one independent timer-load schedule and two commutative unsigned
multiply operands produces all 67 retail words with 23 checked guard rows.
It inserts or omits no instructions and changes no profile, frame, opcode,
arithmetic association, branch destination, offset or relocation identity.

Production equals the independently qualified image. The authoritative
recount is 4,160/5,512 total (75.47%) and 3,487/4,839 Game (72.06%), with
zero address drift. Private screens receive no matching credit.

## Retail behavior and ABI

| Item | Evidence |
| --- | --- |
| Function / owner | `func_151A25E0`, `generated_1CC440` |
| Source / original assembly | `conker/src/game/generated_1CC440.c`, `conker/asm/1CC440.s` |
| Virtual interval | `0x151A25E0..0x151A26EC` |
| ROM interval | `0x1CFA90..0x1CFB9C` |
| Body / frame | 268 bytes / zero |
| Global binding | signed integer timestep `D_800BE9E4` |
| HI16 / LO16 positions | +0x68 / +0xA0, unchanged |
| Callback registry | `D_8008C9C8[19]`, 22 entries |
| Sole aligned pointer literal | ROM `0x2314D4`, VA `0x8008CA14` |
| Direct JAL census | none |
| Caller windows | `func_15167E0C`: 17 words; `func_15168870`: 13 words |

The callback receives one writable, halfword-aligned effect pointer in A0
and returns void. It reads signed lifetime at +0x38 and fourteen signed
halfword parameters beginning at +0x50. Parameter6 is retained and unused.
All comparisons are strict, and later active stages override earlier output:

1. If parameter2 < lifetime, alpha at +0x3F becomes the low byte of
   parameter0 * (parameter1 - lifetime).
2. If parameter5 < lifetime, size fields +0x36 then +0x34 receive the low
   halfword of parameter3 * (parameter4 - lifetime).
3. If lifetime < parameter8, alpha becomes the low byte of parameter9 * lifetime.
4. If lifetime < parameter10, both size fields grow by parameter11 times the
   **live** integer timestep. The product and additions wrap at 32 bits before
   their halfword stores; an unsigned increment expresses this without signed
   overflow in the recovered C. Both old size values precede the output stores.
5. If lifetime < parameter12, the halfword at +0x32 receives parameter13 and
   parameter12 becomes -9999. This is the original sentinel, with no clamp:
   lifetimes below -9999 can satisfy the condition again on a later invocation.
6. The low byte of parameter7 * lifetime is stored at +0x42, +0x41 and +0x40.

The explicit lifetime refreshes after growth and the sentinel write retain
retail's reload lifetime. Earlier alpha and size writes can overlap the global
timestep through guest memory aliases, so preloading the timestep is incorrect.
An actual compiled early-load control has both an alias counterexample and an
unmapped-global fault when the original inactive growth path requires no load.

Both original caller windows read a signed method selector, skip -1 and NULL,
invoke the registry callback, restore their saved owner and reload the observed
halfword afterward. Every valid table slot is tested. These bounded windows do
not recover either complete large parent or qualify other provider gameplay.

## Source and normalization provenance

The recovery follows the complete retail routine, the existing neighboring
`func_151A1E34` lifetime ramps, the 22-entry registry and both real callers.
The owner lacks the shared variables header, so a local declaration of
`extern s32 D_800BE9E4` exposes the existing symbol with its established width;
no shared header or other owner is edited.

The first semantic body emitted 65 words because its cached lifetime omitted
two retail refreshes. Adding the explicit refreshes recovers all 67 words.
Signed/unsigned, captured-size, outer-scope, register and split-declaration
increment screens preserve the same remaining 23 differences; they do not
earn independent matching credit. The selected unsigned product and additions
also qualify extreme full-word timestep inputs without native signed overflow.

The normalizer fingerprints the complete natural body and both relocation
tuples, then derives each replacement from:

- ten scoped GPR definition/use lifetimes, preserving every non-register bit;
- operand exchange in MULTU at +0x7C and +0xF0, which preserves the entire
  unsigned 64-bit HI/LO product; and
- permutation `[45,46,47,48,49,44]` of natural instruction indices 44..49:
  move only `LH V1,+0x38(A0)` from +0xB0 to +0xC4 across MFLO, two ADDU and
  stores to +0x34 and +0x36. Those two halfwords cannot overlap +0x38 for any
  effect placement. No branch enters the interior of this straight-line block.

The complete 67-instruction permutation is bijective; the derived changed-word
set must equal exactly the 23 manifest rows. The original HI/LO bindings are
outside the moved block. Original/fitted private states are compared literally;
natural C register allocation and fault PCs are not equated with retail.

## Focused qualification

Commands from the consumer root under WSL PSBBN:

```sh
python3 -m tools.experiments.game_effect_lifetime_growth_candidates
python3 -m unittest tools.tests.test_game_effect_lifetime_growth_match -v
python3 -m unittest tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -v
make tools-check
```

The fresh pre-install eight-test suite passes in 53.765 seconds:

- 6,272 cases per original/natural/fitted body cover signed lifetime extremes,
  all 32 feasible gate masks, strict boundaries, override priority, six full-word
  timestep patterns, two ordinary halfword alignments, two private placements
  and both stack phases. All 67 retail words execute.
- 2,200 alias phases per body cover every halfword-aligned placement of the
  timestep in the 0x6C-byte record, plus the first outside boundary: 54 inside
  layouts and one boundary layout. Eighteen repeated updates check sentinel
  behavior across negative lifetimes around -9999.
- Native32 O0/O2/O3 each cover all 65,536 lifetime bit patterns through a direct
  call and the canonical typed callback, for 393,216 positive executions total.
  Typed halfword storage, complete byte comparisons and trap UBSan qualify the
  actual C; thirteen independently compiled semantic wrong-C controls fail.
  Guest aliases qualify the global/record overlap separately from native storage.
- 1,104 connected cases per body execute both original windows across all
  22 table slots plus signed -1, with NULL cases, halfword alignment, stack
  phase, saved-owner homes, expiration flag and late observed reloads. Other
  callbacks are explicit bounded providers, not transplanted source bodies.
- 644 fired root-memory fault prefixes preserve the complete original/fitted
  private state, memory, events, instruction visits and calls. An inactive growth
  path succeeds with the global timestep unmapped.
- Nine independent GNU links of original, natural and fitted objects cover
  separate function placements and both HI/LO low-half carry edges. Thirty-six
  rebased cases per body include live timestep aliases and literal word identity.
- Four actual IDO semantic controls and the early-step control have guest
  counterexamples. All 268 one-byte raw-body corruptions, three binding changes,
  three real padder preimage corruptions and three complete-ELF corruptions fail.
- The copied owner preserves all 38 neighbors and normalized pools. Both
  relocations, every address and all protected Game data are fixed. The strict
  full-image prediction changes only this target among 6,052 functions and
  accounts for 195 changed bytes, including its symbol size 12 -> 268.

Shared 19 regressions pass in 6.743 seconds and `make tools-check` passes.
Two fixture issues were corrected before the accepted run: the generic frame
gate interpreted the opening LH immediate as a frame adjustment, and the base
oracle lacked the callers' signed-byte load. A target-scoped frame check and
the already established signed-byte-capable oracle preserve those gates; no
shared helper, production profile or emitted word was changed to bypass them.

## Production closure and recount

`make -C conker -j4 build/conker.us.elf progress.csv` completes successfully.
The shared guard prerequisite triggers a full rebuild. The actual production
owner and ELF equal the independently compiled/padded/linked qualified
artifacts byte for byte. The installed eight-test suite passes in 53.502 seconds.

The old guard file survives as an exact byte prefix plus exactly 23 rows.
The frozen Makefile, conversion CSV and generated linker are unchanged. All
six existing GLOBAL_ASM pragmas and 38 neighboring functions are preserved.
The complete ELF prediction accounts for 195 changed bytes, including only
the target body and its symbol-size update from 12 to 268, with zero exclusions.

`make -C conker all` produces the code binary, then returns 2 at the existing
overall retail SHA check expected for this incomplete decompilation. The
duplicate `generated_12D630` recipe and existing SDK warnings are inherited;
the target owner has no fresh compile diagnostics.

Fresh production recount:

```sh
cd conker
python3 ../tools/match_progress.py progress.csv build/conker.us.elf conker.us.bin --version us --objdump mips-linux-gnu-objdump --list
```

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,160 / 5,512 | 75.47% | 0 | 1,352 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,487 / 4,839 | 72.06% | 0 | 1,352 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

The converted inventory remains 5,512/6,046. The current 80% threshold is
4,410 exact functions, requiring 250 more. README changes are aggregate rows
only; function detail stays in this note and concise index entries.

## Fingerprints and preserved scope

| Artifact | SHA-256 |
| --- | --- |
| Natural compact target | `dae35a0e353a29c2fb2970f4f190f710bad9716602819dd2d78fcd244e61f9a7` |
| Linked retail target | `a7058300b6c0b1e2c82ae3e626a25356e5b78ffa99e8969ca7e2218dcc7004f5` |
| Frozen predecessor ELF | `557cd1685bfb53e29ce35d423d84c2ad62820bd56c4506c99c64910d3d3024b5` |
| Qualified owner | `35040b8d23a7f48de8a770ef06e981efe6abe3bda2717f646b3a3911c93bcef7` |
| Qualified ELF | `4dfa62fd6f26d30aa472519a5bf2422e45faa0b9f1ac7cd88018ef2638ab0c96` |
| Production code binary | `4ce46897ec9e1db205f3bfc69e9b783ff62dc0d4ca2048ad4b50d24ec3e69a7a` |
| Production guard CSV, working bytes | `1c9ebf7263167c226127fa85fed6324db2e2eaababe0d966a5d999269eb1578c` |
| Protected Game data | `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670` |

Frozen source, owner, ELF, guard prefix, Makefile, progress CSV, linker and graph,
plus copied-owner artifacts and fresh JSON receipts, are retained under ignored
`conker/build/game-effect-lifetime-growth-151A25E0-match/`. The protected data
remains 189,088 bytes across 720 owners, with no differences.

The main baseline is `bd27728122eaef5040c17bd5d4baa9165b4f8a54`; mounted
tools baseline is `04191f14cfe10203fe1f723ddf9f724a502ea28b`. Both began clean.
The separate sibling `64CBFD Tools` checkout at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`
has six pre-existing tracked changes and 2,428 untracked files, all preserved.
Fresh target tests use the consumer's mounted tools only;
no second-checkout qualification or synchronization is claimed.

## Continuation and graph retention

The actual production rerank selects `func_15056A00` next, 66 words and
65 real differences. Keep the seven documented
boundary cases separate: `func_150A76F0`, `func_151F8870`, `func_150A613C`,
`func_150AE280`, `func_15115F68`, `func_151AE2BC` and `func_150A6760`.

The standard AST update refused a reduced 24,839-node extraction rather than
overwriting the frozen 58,632-node graph. Its existing corpus warning retains
31,816 nodes from 3,754 source files omitted by the scanner. No force, purge,
package upgrade or full-corpus re-extraction is claimed. Existing warnings
remain for skill/package versions 0.9.20/0.9.26 and zero-node `devcontainer.json`.

The explicit AST refresh of eight changed consumer paths yields 58,641 nodes,
112,401 links and 5,214 communities. It retains 58,629 old IDs verbatim;
three Update Log heading IDs relocate after the new entry is prepended.
Twelve IDs are added: nine from this note and those three relocated headings.
**Zero nodes outside the changed paths are removed.** The scoped refresh uses
no semantic LLM calls. HTML is skipped above the 5,000-node visualization limit.
The ignored `graph-retention.json` stores the old-node and hash evidence.

Qualified graph SHA-256:
`e9800547c240149ef46e72a0891de3b893391b8083b538e12bbb10701fef36f1`.
The unchanged production link map has SHA-256
`2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb`.
Tools are banked first as `337d228fbae2525e74f4b98a054aab00af4cf005`.
