# Three-row table payload constructor directly matched

Date: 2026-11-06. Continues [Note 2133](2133-game-owner-vector-payload-direct-match-and-caller-abi-20261106.md)
from consumer `b576b24c107d2899830da876324234721a5e797f` and tools
`0d9a9b782f9ba3e80a8ffe5ec6354ac561b66b74` toward the active 80% goal.

## Recovered source and ABI

`func_151623F4` in `conker/src/game_18D770.c` emits all **71 words / 284 bytes
directly from C**, with **zero guards** and no compiler profile change. VA
`0x151623F4..0x15162510`, ROM `0x18F8A4..0x18F9C0`; no alignment tail.
The original frame is `0x50`: RA+0x1C, result spill+0x24, Header+0x28,
32-byte payload+0x30, saved incoming words+0x50 onward. Declaring payload,
header, then result recovers the exact local homes and scheduling on the
first source screen. The old unspecified zero-return stub occupied 12 bytes.

The pointer-returning interface has eight arguments: actor pointer, selector
byte, flags byte, header ID byte, signed kind byte, signed lifetime halfword,
priority byte and full-word user data. Selector 0..2 is accepted; every other
byte returns zero before table reads or helper calls. A null actor is allowed
and is passed through, with no invented owner gate.

The payload copies two complete three-word rows from D_800A670C and
D_800A6730, initializes phase to floating zero and loads rate from
D_800A6754. The neighboring original callback func_15162510 reads the first
three floats as base, the next three as sine amplitude, then phase/rate;
that consumer supports the descriptive local field names. Its large FCSR
conversion body is not converted by this change. Table globals keep their
existing declarations; struct assignment preserves the six raw word copies,
including arbitrary float encodings, without arithmetic or conversion.

The Header contains ID, kind, lifetime and flags. The helper receives
`(&header, actor, 32, priority, userData)`. Failure returns zero. Success
copies the complete captured 32-byte payload to record+0x18 and returns the
preserved record pointer. Tables may change inside the helper; the captured
payload must remain unchanged. The header's padding byte has guest-only
literal value proof, not a portable C value promise.

The root forward declaration and definition agree. game_36680 now has the
same proper local prototype and explicit actor-address casts at both C call
sites. All **77 + 82 = 159 raw and padded neighboring bodies**, allocatable
pools, bindings and metadata remain fixed. The complete padded caller object
is byte-identical. Its compact object has declaration/debug differences,
which the production padder removes; no section is silently excluded.
Root warnings remain 42 and caller warnings 6, with complete normalized
diagnostic sets unchanged. Shared headers, original ASM, guards and Make
rules are untouched. All **144 frozen inputs** are audited.

Eight bindings are checked: three HI16/LO16 table pairs at offsets20/40,
50/5C,9C/AC, plus calls atE0/FC to func_1516037C and Init memcpy.

## Qualification and limits

Eight focused checks pass both before and after installation in each actual
tools configuration. The sibling uses only an ignored five-module overlay;
its real shared helpers and exact fingerprints are recorded, preserving its
six tracked edits and 2,428 untracked files. Both tools smokes are fresh;
three unchanged shared suites per copy are explicitly reused by exact source
fingerprints from Note 2124. Zero Claude calls are needed.

- **14,592 guest cases per body** cover every selector byte and byte argument
  axis, signed lifetime boundaries, arbitrary raw table words, invalid early
  returns, null actor, both allocation outcomes, mutable tables and incoming
  homes, both stack phases, and all 71 words. RAM, registers, FPRs, events,
  access traces, call arguments, snapshots and copied payloads agree literally.
- **576 table/stack alias cases per body** and **82 fired access-cut prefixes**
  compare full instruction states. Aliases are guest instruction tests. An
  initial test moved the table memory without relocating the test instructions;
  explicit independent HI/LO rebinding fixed that fixture. Production C did
  not change, and the full canonical suites were rerun.
- **256 connected cases per body** execute all **32 record-helper words and
  11 memcpy words**, with current linked helper slots verified against retail.
  The allocator remains an explicit opaque boundary. Actual request
  `(53,userData,56,1,priority,1)`, six-byte header copy, actor pointer store,
  failure return and final 32-byte copy are independently checked. This does
  not qualify the whole allocator, callback or engine.
- **128 complete-caller cases per body** execute both original 19-word
  wrappers, func_150098F8 and func_1500A55C, including their full prologues,
  eight arguments, real call delay stores and epilogues. Both submit
  `(actor,1,22,0,-1,300,255,1)`; all 38 parent words are visited.
- **Six independent GNU links**, three layouts and **96 cases per body**
  cover all eight bindings, signed-low16 carry boundaries, rebase-sensitive
  addresses and both calls; standalone zero alignment bytes are checked.
- SDK **native32 O0/O2/O3 with UBSan** executes **262,144 cases per profile**,
  **786,432 positive executions / 8,650,752 calls including ten controls**.
  Every selector byte, all byte input axes, both allocation outcomes, null
  actor, raw float words, table mutations, complete payload, defined header
  fields, actor identity, return pointer and canaries are checked. All ten
  controls are rejected by checked state/result differences (mask1023);
  sanitizer traps cannot satisfy a control. Only header padding values stay
  outside the portable native contract.
- All **284 raw byte corruptions**, **eight binding corruptions**, five
  whole-image corruptions and the old three-word stub are rejected.

## Actual production

```sh
make -C conker -o retail_word_patches.us.csv -o Makefile --output-sync=target -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

The two edited sources compile exactly once each under the unchanged
O2/g3/MIPS2/O32 profile. The actual ELF equals the literal **217-byte
prediction**, with **zero exclusions or metadata permutations**: only the
constructor body and symbol size12 to284 change. All **6,052 addresses**,
conversion rows, progress.csv, guard bytes and **189,088 protected data bytes
in 720 owners** stay fixed. Both complete source diagnostics remain unchanged,
48 warnings total. The duplicate generated_12D630 recipe warning and expected
unfinished full-image checksum failure remain; no warning-free build is claimed.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,203 / 5,512 (76.25%) | 0 | 1,309 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,530 / 4,839 (72.95%) | 0 | 1,309 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**207 more** matches reach the current 4,410 threshold for 80%.

- ELF: `5b3e85e83f8b69982c48b619a9ffe9981d5ac55109ab0f85b9e92df58a43f851`.
- Owner: `523b7dd957e1640999427cd306f5b68e83fcf453301c9dbb3301dbb2fbfbfcc4`.
- Code binary: `739af6250ba25338762040eb9036330d2f0d5913aada17dc8d3803c03f7d488a`.
- Guard CSV: `ad8c4e24d535e3ccc7aa3d4c3ae7db4972c569bbf690238f68c65757438993c6`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence: `conker/build/game-selector-table-payload-151623F4-match/`.
Scoped Graphify refresh retains old nodes outside changed paths; no full
corpus extraction is claimed. Tools are committed before the consumer pin,
two source files and documents. Root README changes aggregate rows only.

Next static target: **func_151897A4**, generated_1B5CC0, 71 words/frame0x68,
VA151897A4..151898C0, ROM1B6C54..1B6D70. Original code preserves the descriptor's
byte+0x8A across a counted series of func_151137D4 calls, advancing a display
cursor, 64-byte records and a fixed-point field. Inspect descriptor widths,
saved-register roles, live reloads and all callers before conversion. It is
uninstalled and uncredited. Preserve unrelated work, private inputs/saves,
handwritten func_150A76F0 and frozen host Release. The 80% goal stays active.
