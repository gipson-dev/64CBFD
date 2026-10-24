# Actor Class Dispatch Direct C Match

Date: 2026-10-24. Consumer predecessor `487edcb3`; tools predecessor
`8e2e877c`. Qualification tools committed first as
`2266dcbc04ab352d86af461d492586d10c7933d3`. No push requested/performed.
Routine work, zero Claude calls; no provider/dependency or host changes.

## Recovered Routine

`func_15192800`, `conker/src/game/generated_1BFCB0.c`, replaces the
three-word zero-return placeholder with complete class dispatch C.
VA `0x15192800..0x151928B0`, ROM `0x1BFCB0..0x1BFD60`, exclusive ends:
176 bytes / 44 words / frame 48 / six bindings, no alignment tail.
Use the original address-based name, a local typed callback alias and
`void(void *actor, s32 unused)` to preserve the actual actor pointer ABI.

1. Store the full unused A1 word home. A NULL actor skips both helpers and
   all table reads. Otherwise pass the actor and a local signed-word output
   to `func_151928B0`; a false result skips the remaining work.
2. The unchanged selector accepts byte IDs zero through four as row zero,
   and 0x53 as row one. Other IDs fail without producing a usable row.
3. Read actor+0x184 only after selection succeeds. `func_1510F8CC` returns
   the low five bits. Class five selects column two in world 0x14, otherwise
   column one; class six selects column three; all other classes select one.
4. Read the selected row pointer from `D_8008F860`, then its callback.
   Call a non-NULL entry with the original actor pointer; ignore its result.
   No speculative row-range check or extra fallback is added.

The switch form emits all retail words directly at normal O2/g3. Both the
nested and early-exit switch screens match; if/conditional forms emit a
40-byte frame and 23 different words and are not selected. `void *` and
the canonical actor-pointer screen both preserve the exact raw body.
The generic pointer keeps the existing struct127 caller and u8 callbacks
compatible without a shared-header/type rewrite.

No guards, new profile, volatile barrier, inline assembly, inserted/omitted
words or assembly-body replacement. Word 28 at +0x70 is an unreachable
duplicate case-result assignment emitted by the original switch shape;
retain it in the full match. All other 43 executable words are visited.
Six bindings are JALs at +0x14/+0x24, world HI/LO at +0x4C/+0x50 and table
HI/LO at +0x78/+0x80. The complete historical guard CSV is byte-identical.

Raw payload SHA-256:
`5c714d20b045d9d6912d5fea3d4c3cccc7a34559889d2a62cfae459019f5f482`.
Resolved retail body SHA-256:
`26aab509ba1d3ca63036f11094fa1f7d7e61d953c267eeea4c81294a76fb9a4b`.

## Actual Caller And Helpers

An aligned full-ROM scan finds no literal target pointer and exactly one
JAL site, ROM `0x9F2B8`, in `func_15071DF4`. Execute its complete 11 words
at VA `0x15071DF4..0x15071E20`, ROM `0x9F2A4..0x9F2D0`, in 2,048 phases.
It passes `D_800D154C` (struct127 pointer) and `D_800D1580` (word), ignoring
the result. Add its local explicit void prototype in `game_981E0.c`.
All 328 owner functions/pools and the complete padded object remain fixed.
Native checks compile the actual existing C wrapper with the recovered C.

Execute all 26 original row-selector words, including its five-entry jump
table at `0x800A8160`, plus all three original mask-helper words. Native
checks compile the existing selector C and use the bounded low-five-bit
mask contract; the classifier's separate source stub remains uncredited.

Verify actual data at ROM `0x234320`: rows `D_8008F840` and `D_8008F850`.
Each has only column two non-NULL, pointing to `func_15192920` and
`func_151B1AB0`, respectively. Also test controlled populated and all-NULL
tables to distinguish columns one/three. Callback bodies remain bounded
providers, not a claim about their lower factory services or gameplay.

## Focused Qualification

Both tools copies pass eight fresh checks before and after installation:
no errors, failures, skips or reused checks. Pre-install primary/mirror:
95.067s / 151.549s; installed: 99.612s / 84.966s. Both shared project-tool
checks exit zero. Reuse existing source-span, MIPS/frame/fault/native32,
relocation, pool and ordinary padder helpers.

- 7,432 original/raw/padded/actual-Make guest phases cover all 256 actor
  ID bytes, all 32 classes with upper-word flags, worlds 19/20/21, three
  table layouts, two stack phases, NULL actors and callback mutation.
- Native32 O0/O2/O3 trap UBSan passes 147,456 direct and 147,456 actual-C-
  parent cases per optimization, plus direct NULL checks. Full struct127
  backing and ten effective defined wrong-C controls check selected row,
  class/world branches, callback identity, argument and ignored entries.
- Forty-three fired root-access prefixes compare complete original/C
  private states. Twenty-four extra guest phases cover row output overlapping
  the late actor-kind word and the full unused A1 home overlapping actor ID.
  These qualify instruction accesses, not portable C private/fault semantics.
- Nine independent GNU links compare original, qualified padded and actual
  Make objects at three entry/world/table placements, including HI/LO carry
  boundaries. Forty-eight rebased phases and three image corruptions pass.

An initial isolated padder probe omitted the owner's existing
`--rodata-symbol jtbl_800A8160_game` option. Reuse that actual Make mapping
for the unchanged selector's .rodata reference; no build-rule change or
verification relaxation. Rename the private `types.py` probe to avoid
shadowing Python's standard library in child processes, then rerun both
pre-install suites successfully. These were fixture issues, not C fixes.

## Production And Preservation

Advance the preceding checkpoint's four qualified overrides, then seal
15,978 baseline files. Add the two tools modules in both copies:
15,982 files / 34 focused inputs / all 1,454 linker objects. Verify native
and Linux-cache bytes using checked stdin/tar bridges, no DrvFS project reads.
Preserve all 1,618 prior mirror dirty statuses/hashes/HEAD; add only the two
owned modules, now 1,620 paths. Do not commit/reset that older mirror.

Actual Make uses the normal three-command target and five-command caller
recipes, O2/g3. Preserve the selector neighbor/pools, complete qualified
target object and byte-identical caller object. Isolated diagnostics are
empty; whole-owner diagnostics are unchanged. Inherited pointer/integer
and duplicate generated_12D630 recipe warnings remain; not warning-free.

Production Make exits zero in 2.280s and exactly reproduces the independent
complete image prediction: 133 changed bytes, 132 target code plus one
function-size metadata byte, 12 to 176. Zero exclusions or unrelated changes.
All other 6,054 bodies/all 6,055 addresses and protected Game data remain:
720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Audit all 15,982 live files around adoption with exactly four overrides:
target source, caller declaration source, target object and linked ELF.
The guard CSV and caller object stay byte-identical. Re-capture the actual
adopted native ELF and freshly recount those bytes through the checked bridge.
ELF SHA-256:
`693badff1224f03e5d012f81d6701439265561c94a0e98a76b56470d277ef9ae`.

| Section | Exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,780 / 5,505 (68.66%) | 0 | 1,725 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,107 / 4,832 (64.30%) | 0 | 1,725 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The 75% threshold remains 4,129 exact functions: 349 more needed. The live
ELF-pinned screen now has 1,596 placeholders, 120 semantic/other definitions
and nine parser-unlocated entries. `func_1510D8C0` already has a Gfx* body
and remains a separate matching case. Next real placeholder `func_151DD8C0`,
owner `generated_20A990`, has 43 body words plus one alignment word. Its
recorded-input private C screen emits the body length but still differs;
it is unqualified, uninstalled and uncredited. Keep the separate larger
`func_1509E730`, `func_1508CAD8` and `func_15169070` work unchanged.
README changes only its two aggregate rows; host Release, saves,
configuration and unrelated sibling work remain untouched.
