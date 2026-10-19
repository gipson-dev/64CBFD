# Balanced Target Assignment Semantic Recovery And Private Layout Boundary

Verified: 2026-10-19. Complete experimental **func_1508BF14** is recovered and
passes eight focused tests. **It is not installed or byte-exact.** Preserve
the production source, guards, Makefile, assembly, ROM, ELF and progress CSV.
VA1508BF14..1508C194, ROM B93C4..B9644, generated_B3020,160 words/640 bytes.
Consumer predecessor e418f7b; tools predecessor c939d75. Bank tools
**de2850c** before the consumer documentation/tools-pin commit. No push.

The selected no-unroll body emits160 words/frame224 with123 real differences;
retail uses frame176. Fitting the slot and agreeing on public results does
not establish the private layout. A frame-only edit corrupts the real caller's
saved return address. No new guards, production build or matching credit.

## Recovered Behavior

1. Capture the initial context's signed count/current index, flag, active,
   team, output, neighbor and distance table bases. Capture the current team
   once. There are no helper calls, including on empty/negative counts.
2. Clear exactly count signed-byte reuse cells for positive count, retaining
   the remainder loop and four-byte unrolled clear. Retail's first cell is
   SP+7C; its pass word is SP+A4. The intervening40-byte footprint is measured,
   not proof of an engine-wide maximum-count invariant.
3. Process flag2/3 receivers first, then every other flag class. Only receivers
   on the cached current team receive output. Flags and other table contents
   are read as execution reaches them; do not snapshot mutable table values.
4. Consider positive active candidates on a different team. Search their
   16-entry neighbor row for the receiver, stopping at -1. A matching distance
   of -1 is excluded too. Use the candidate's current reuse count as a MIPS
   low-five-bit shift count, with32-bit wrapping result and signed comparison.
5. Keep the first strict minimum below10,000,000. Increment the selected
   candidate's reuse byte, then store best cost followed by selected index at
   cached context+45C/+49C plus receiver*4. Return0.

The no-selection case is significant: retail still increments
`uses[-1]`, the byte at SP+7B, without initializing it. The experimental C
backs that access inside a41-byte array and initializes the extra cell to0;
`uses` points to the second byte. This makes the bounded native operation
defined instead of introducing an out-of-array read/write. That private value
does not enter candidate scoring for the qualified disjoint contexts. It is
**not retail private-byte identity**, and the initializer must not be treated
as an original source fact. Retail poison values are preserved in guest tests.

The unsigned32 shift and explicit low-five-bit mask avoid signed-left-shift UB.
They emit an extra ANDI. Any future normalization must prove the hardware
SLLV equivalence and its register lifetime, not simply replace words from ROM.

The other-source snapshot is a cross-check only: its scalar scratch object,
word/byte casts and clear stores are not a valid byte-exact C donor. The
experimental body keeps descriptive local names and the address-based export;
it does not invent original names or record types.

## Fresh Qualification

**Eight tests pass in24.064 seconds**, without skips:

- 94 fixtures/two stack phases give188 completed retail/raw pairs against an
  independently structured reference. Compare every public byte, ordered
  cost-before-target stores, no-helper behavior and zero result. The executed
  fixtures visit all160 retail words.
- Counts include INT_MIN,-1,0, all clear remainders,16,17,31,32,39,40. Counts
  above16 deliberately use inactive candidates and explicitly backed overlapping
  tables. This is not full behavior for arbitrary larger counts or a native
  out-of-range guarantee. Current indices are backed0..15.
- Native32 O0, O2 and O2+UBSan each pass all94 fixtures with empty sanitizer
  diagnostics. Ten effective behavioral negatives reject reversed pass order,
  last-tie selection, omitted reuse penalties, zero-active acceptance, teammate
  selection, unsigned scores, ignored row/distance sentinels, byte-truncated
  flags and shortened neighbor rows. Every negative compiles and exits25;
  none relies on a signal or compiler error.
- Four private poison values0/7F/A5/FF preserve the same public miss results.
  Retail increments its original SP+7B poison; the C increments its backed
  zero-initialized miss cell. The complete private memories intentionally differ.
- Two fired access-cut negatives establish actual private mismatches. Raw
  access0 saves RA at incomingSP-180 rather than retail incomingSP-132. After
  editing only frame immediates, access13 writes the cached flags pointer at
  incomingSP+36 rather than incomingSP-68. Both gates fire before the store.
- The aligned ROM scan finds the single JAL at ROM CB564/VA1509E0B4. Eighteen
  runs retain its actual JAL/NOP, branch/RA delay load and S0/SP/JR/NOP epilogue
  inside func_1509DFC4, with the72-byte caller frame as an explicit live-in.
  The frame-only control overwrites the caller RA home with context+15C and
  fails at that unowned jump. The full upstream switch is not executed.
- Three independently assembled/linked GNU maps include HI/LO carry
  boundaries and move code, global pointer and context backing. Thirty-three
  rebased retail/raw pairs agree with the independent public reference.
  Both raw global bindings are retained; no normalized byte identity is claimed.
- Both complete-owner profiles preserve72 neighbors and all pools. The real
  padder fits the primary640-byte candidate while preserving all73 addresses,
  every other padded instruction and all other extents/pools. The expanded
  seven-command Make recipe reproduces those same qualified objects and bytes
  in an ignored shadow build. Its normal object still supplies only the
  pre-existing func_150891E8 override; do not apply it to this target.
- All frozen production inputs remain byte-identical. Shared tools checks and
  syntax checks of the three new files in both tools checkouts pass. The older
  standalone mirror HEAD and all1,374 pre-existing dirty leaf hashes are preserved;
  only three absent task files are copied and verified there, without a commit.

An initial byte-flags negative survived because the fixtures changed all
receivers' pass together, preserving their relative order. Mixed258/259 and2
fixtures made the control effective. The failed initial receipt is not a pass.
No Claude call, REA setup, dependency change, host operation, hardware or full
gameplay acceptance was involved.

## Compiler Screens

The reproducible four-form/two-profile screen has empty diagnostics throughout:

| Form | Profile | Words | Frame | Word differences |
| --- | --- | ---: | ---: | ---: |
| Selected explicit unrolled clear | Primary no-unroll | 160 | 224 | 123 |
| Selected explicit unrolled clear | Normal | 198 | 232 | 180 |
| Indexed counter clear | Primary no-unroll | 148 | 224 | 139 |
| Indexed counter clear | Normal | 160 | 224 | 116 |
| Pointer/counter clear | Primary no-unroll | 148 | 224 | 142 |
| Pointer/counter clear | Normal | 159 | 224 | 133 |
| Named context/explicit clear | Primary no-unroll | 152 | 232 | 150 |
| Named context/explicit clear | Normal | 190 | 240 | 180 |

The two clear controls retain the selected declaration block, so their unused
temporary declarations are part of the measured screen, not recovered source
requirements. Earlier ignored declaration/array-size probes also failed the
private-frame gate. Do not choose a shape merely for a lower difference count.

Selected raw SHA256:

```text
c31e39062a3c82931d51d574c1106272083e651bfc04b8e796c6b31490009795
```

## Production And Resume

Fresh matching remains **Game3,008/4,832 (62.25%)** and
**total3,681/5,505 (66.87%)**,1,824 different/zero drift. Init492/492 and
Debugger181/181 remain exact; owner60/73 exact,13 nonmatches. Conversion
counts and root README are unchanged. The complete production ELF remains:

```text
f56b8cca096731899df5ddecd2fcd8060cf57f53ac03508ab093929f7e14ee4d
```

Continue the same function, not another broad batch:

1. Recover the source declaration/storage lifetimes and frame176 without
   padding locals, physical-register C bindings or frame-only patches.
2. Restore count S3, scratch S2, teams S4, cached team S5 and receiver T1;
   retain the actual saved-register and cached-pointer homes. Fit the clear
   loop and flag/neighbor register reuse before later scheduling.
3. Resolve the backed native miss cell versus retail's uninitialized SP+7B
   explicitly. Preserve retail poison/private prefixes in the final emitted
   routine; do not claim the initialized raw cell is original behavior.
4. Only after full private-state, caller, fault-prefix, relocation and actual
   padding qualification, install a byte-exact body and strictly predict the
   entire ELF. Preserve every neighbor, historical guard and protected Game
   data. Keep the broad Game goal active.

From64CBFD under WSL:

```sh
python3 -m unittest tools.tests.test_game_balanced_target_assignment_recovery -v
python3 -m tools.experiments.game_balanced_target_assignment_candidates --screens
python3 -m tools.experiments.game_balanced_target_assignment_candidates --screens --normal
python3 -m tools.match_progress conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
make tools-check
```

Ignored source screens, immutable inputs, raw objects, native vectors, real
padding/Make-shadow output and receipts live under
`conker/build/game-balanced-target-assignment/`. Keep the scratch-file recovery
closed: the user confirmed the previously overwritten `Desktop/.vscode/Conkers`
file was disposable. Do not investigate OneDrive recovery or repeat the broken
unquoted-path compiler invocation.
