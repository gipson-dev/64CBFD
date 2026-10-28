# 1753 - Spawn-result query direct C match

Verified: 2026-10-27. Target `func_1507E114`, owner `game_A9D90`.
VA `1507E114..1507E1D0`; retail ROM `AB5C4..AB680`.

## Recovered routine and interface

Replace the zero-return placeholder with the complete 47-word /188-byte C
routine. Normal O2/g3 emits every word directly: frame 0x60, nine bindings,
zero guards and no compiler diagnostics. Preserve all 15 neighbors and pools,
including three GLOBAL_ASM routines, and all 16 compact functions. The actual
five-command asm-processor/IDO/postprocess/legacy-padder/assembler Make plan
reproduces the qualified object, retaining `jtbl_8009B884_game`.

The interface is `s32 func_1507E114(s32 *unusedSelection)`. The sole original
caller supplies the address of its saved selection word. Retail saves the full
pointer at incoming SP+0 but never reads through it. Preserve that unused
parameter and home rather than inventing an input/output role.

An unsigned byte `D_800D18A8` gates the query. Disabled returns zero without
reading the context. Full-word contexts 0x22 and 0x18 also return zero. Otherwise,
store the sign-extended `D_800BE3DF` byte to the context before loading the
unsigned `D_800BE3E0` selection byte, then call `func_15084D70` with eleven
physical arguments. Ignore its direct return and return the result output plus
one. The signed source byte and post-store selection read are observable.

The shared header currently declares `D_800BE9F4` as `u16 *` and
`D_800BE3DF` as `u8`. This routine uses explicit 32-bit pointer/word and
signed-byte conversions to express the measured accesses without changing the
shared declarations or violating effective types through an incompatible word
lvalue. Native32 checks qualify the existing compiler/ABI conversion behavior;
this is not a declaration repair or a portable 64-bit-pointer claim.

The helper's output widths are established from its original stores:

| Argument | Target frame location | Object |
| --- | --- | --- |
| 4 | +0x54 | three s16 position values |
| 5 | +0x48 | three f32 rotation values |
| 6 | +0x43 | first byte |
| 7 | +0x42 | second byte |
| 8 | +0x44 | word flags |
| 9 | +0x3C | signed word tag |
| 11 | +0x5C | word result |

Arguments 1/2/3 are zero, the selection byte and one; argument 10 is one.
Declare the result, position, rotation, flags, bytes and signed tag in this
order to recover their original lifetimes and addresses. The original helper
can leave the last result unwritten, so no default initializer is introduced.
Those paths preserve the prior guest stack word and wrapping instruction add;
native tests use helpers that write the result and avoid signed overflow.
One redundant context load at offset 44 is unreachable. All 47 literal words
are exact; all 46 reachable words are exercised.

## Caller and complete original-helper evidence

The aligned whole-ROM census finds one JAL at ROM 35118, VA 15007C68, inside
`func_15007B3C`; no target pointer or tail J is present. Fifty-four cases run
the authentic six-word window `15007C64..15007C7C`, checking the pointer
setup, saved-word delay store, untouched input canary and return store at
caller SP+0x2C. The containing parent's C placeholder remains uncredited.

Thirty-six cases connect the complete 424-word original `func_15084D70`,
with actual actor-state and spawn-table memory. These paths execute without
opaque subcalls, cover entry-link selection/fallback and signed tags, and
verify the resulting zero/one result flags. Nine link-zero cases leave the
result unwritten and return the seeded guest word plus one. Its production C
placeholder remains unchanged and uncredited. This selected-path execution
is not full helper, parent, RNG, spawn gameplay or hardware acceptance.

## Qualification

Both tools copies pass eight fresh canonical methods and shared project-tool
checks. Each copy then runs two fresh installed owner/image checks and reuses
six unchanged semantic checks only after exact module/input/artifact identity.

- 3,522 guest cases cover every gate byte and previous-context byte, unsigned
  selection boundaries, full-word context values, five layouts, output homes,
  provider mutations, unwritten results and guest wrapping addition. Compare
  complete private GPR/FPR/RAM/events, visits and ordered memory traces.
- Alias cases are linked with actual GNU symbol definitions in both original
  and compiled objects. They include overlapping context/source bytes, a
  context over the result home, a gate over the incoming pointer home and a
  selection byte changed by the context store. The first fixture incorrectly
  moved memory labels without relocating instructions; corrected fixtures
  use independent GNU links. An initial alias linker-script format omission
  is also retained in the failed receipts. Production C never changed.
- Native32 O0/O2/O3 with trapping UBSan pass 165,888 positive cases per profile
  and eight effective C controls. They cover valid typed outputs, null/valid
  unused input pointers, the legacy 32-bit context conversions and provider
  changes to globals. Indeterminate outputs, signed overflow and guest label/
  stack overlays remain outside the native contract.
- 110 fired access-prefix pairs preserve full private state, trace and PC/
  delay ownership. Sparse mappings prove disabled/blocked early returns
  suppress context, selection or helper reads as applicable. The input pointer
  is never dereferenced.
- Six dedicated GNU links over three layouts pass 18 rebase cases, including
  all nine bindings and signed-low carries. Alias links are additional.
  Three raw controls reject truncation, changed binding and changed dead word.
- A compiled result-initializer mutant fails the unwritten-home case: seed
  85 must return 86. Six whole-image corruption controls fail closed.

Routine Claude calls: zero.

## Production, progress and banking

The actual production build reproduces the independently predicted whole ELF:
140 changed code bytes plus one function-size byte, 141 total, zero exclusions.
The target extent changes 12->188; every other named definition is fixed.
All 6,056 function addresses, 6,055 other bodies, 720 protected Game owners and
189,088 protected bytes remain unchanged and exact. No metadata cycle is
introduced. Inventory CSV, guard CSV, shared headers and the caller/helper
objects remain byte-identical. The only build warning is the inherited
duplicate generated_12D630 recipe.

ELF SHA-256:
`ef65f9bccc08a981415cbf87a4f744c610fcb56e29622863df3d3044bb5aeef4`.
Unchanged Native CRLF guard CSV SHA-256:
`f867c3817abab6b6ef822343afa48a4b188e7067ce1d4c69a078b54a6f4b4c40`.
The Native/cache seal covers 16,192 inputs and 174 focused inputs. Recount the
captured adopted Native ELF against the unchanged C inventory:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,831 /5,506 (69.58%) | 1,675 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,158 /4,833 (65.34%) | 1,675 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only `func_1507E114` becomes exact. Converted totals remain fixed. Threshold
4,130 leaves 299 more matches to 75%. Remaining source screens contain 1,546
placeholders, 120 semantic/other definitions and nine unlocated entries.

Predecessor consumer `a0cfdab62dac9f937a621def4614cab481a1d86c` and tools
`48c9c089ae9380bddc235552a1ca59ec28a8a0ff`. Bank tools first at
`98c3fb3d0dd30b71a4b3748a5c20ffc1e3ea4dfc`, then source, consumer pin and
measured documentation. Preserve the old mirror's 1,716 inherited dirty paths
plus two new tools files without committing its independent history. No push.
The root README changes only its two aggregate matching rows.

Refresh ten changed C/Markdown/tool sources with Graphify. Retain every prior
node and still-valid relationship/context; the target keeps its s32 return
and gains its s32-pointer parameter and helper-call relationship. Preserve
outside-scope freshness and historical communities; no full-corpus extraction
or global clustering/centrality claim. Evidence, graph diagnostics and the
independent final audit remain in `conker/build/game-spawn-result-query-match/`.

Next inspect `func_150D2110` in `generated_FF5C0` using a fresh predecessor
and caller/ABI audit. Keep `func_1514E920` private and uncredited. The 75% goal
remains active.
