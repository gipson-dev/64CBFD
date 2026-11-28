# Byte preset pointer selector direct byte match - 2026-11-28

`func_1519003C` in `conker/src/game/generated_1BA1D0.c` replaces its three-word
zero-return placeholder with **120 words / 480 bytes emitted directly from C**,
VA `0x1519003C..0x1519021C`, ROM `0x1BD4EC..0x1BD6CC`. There is no frame,
alignment tail or new word guard. The qualified interface is
`u8 *func_1519003C(u8 *record, s32 *count)`.

Actual production: **4,724 / 5,528 (85.46%) total**, **4,051 / 4,855 (83.44%)
Game**, Init 492/492, Debugger 181/181. Zero address drift; 804 still different.
Conversion rows and denominators are unchanged. **252 more matches** reach the
active 90% target of 4,976/5,528. This adds exactly one direct C match.
Previous consumer `956df5d3`; tools packet `e476d7b458dc1c118c7273f8f002c0a391af8bcc` was committed first.

## Recovered behavior and original callers

The switch reads the unsigned byte at record +4. Thirty recognized byte IDs
select one of nineteen mutable byte-preset arrays, `D_800A7AC8` through
`D_800A7B10`, at word-spaced addresses. A recognized case stores count 1 and
returns that exact array pointer. The other 226 IDs store count 0 and return
NULL. The first four record bytes are not read. Presets retain address-based
names because the evidence establishes their byte lookup role without a
broader gameplay interpretation. No shared-header change is required.

Both original direct JALs are pinned at ROM **0x529C0 / 0x55438**, VA
**0x15025510 / 0x15027F88**, in `func_1502460C` and `func_150265CC`.
Their complete original bodies are retained as evidence (2,032 / 3,451 words),
but only **61 original caller-window words** are qualified. All 61 execute in
**1,812 fixtures x four streams / 7,248 connected executions**. Both callers
consume the pointer and count; both pointer-to-NULL and count-to-zero controls
are effective at each site. Preset bytes are loaded unsigned, including 128
and 255. The second selector gate admits types 0x49/0x58, and the following
delta argument is truncated to signed 16 bits. Negative signed cache indices
are additional guest-only cases, outside the portable typed native scope.
The next ten-argument provider `func_1518F51C` is an **opaque boundary**;
neither that provider nor either complete parent is claimed qualified.

## Full owner, two tables and exact linking

The complete owner has **61 C definitions and no GLOBAL_ASM**. All sixty other
source bodies and raw/padded function payloads stay fixed. Both generic and
generated padders reproduce the frozen before object and the same selected
whole object. The generic route explicitly restores all **58 original exported
case aliases**, rather than ignoring their symbol-namespace difference.

The compiler emits two contiguous jump tables: **122 entries at
`jtbl_800A7DC0` and 23 entries at `jtbl_800A7FA8`**, a 0x1E8-byte stride.
All **145 R_MIPS_32 entries** have their original target-relative case ownership;
145 single-entry mutations reject. The compiler's 592-byte pool comprises
580 table bytes and twelve zero alignment bytes. That tail is not substituted
for original public data: the adjacent coefficient **`D_800A8004` stays intact**.

One target-specific Makefile assignment binds the existing generated padder to
`jtbl_800A7DC0`. The actual **three-command** Make recipe, O2/g3/mips2/o32 profile,
and guard history otherwise remain unchanged. Four pre-existing unrelated IDO
Warning 712 diagnostics and six existing duplicate-recipe warnings are
retained; the change introduces no compiler or assembly warning.

All **42 external code binding positions** (38 preset HI16/LO16 and four table
bindings) match. The original assembly also has **two internal PC16 bindings**;
actual GNU linking resolves them to the preserved original case alias.
**Sixteen actual GNU links** cover four independent code/table/global rebases,
including signed HI16/LO16 carry seams. All 120 code words and all 145 table
entries match at every rebase, with no word normalization.

## Execution and production acceptance

- SDK/native32: **2,048 cases each at O0/O2/O3**, all 256 selectors, two valid
  typed count-alias modes and four initial count patterns. All twelve record
  bytes, the output word, exact pointer identity and nineteen unchanged presets
  are checked. Separate translation units, strict aliasing, trapping UBSan and
  LTO type checks pass. Native aliased-count expectations use the native object
  representation. Six semantic controls fail with exit 42.
- Guest: **4,704 cases x four streams / 18,816 executions**, all **120 reachable
  words** executed, no unreachable words. Retail, raw C and both padded streams
  have identical complete normal states and literal fault-prefix states across
  **657 access-fault quadruples**. Five count-alias modes, three sparse pointer
  domains, both stack phases and 96 guest-only preset/table alias cases are
  included. Four semantic controls reject. No portable C fault-semantics claim
  is made.
- Independent frozen-before-C plus original-target-ASM prediction equals the
  private and actual production full ELF: **701 changed bytes, zero exclusions**.
  All named symbol definitions and section geometry are preserved except the
  declared target's size/body. Closed symbol/string serialization permutations
  are accounted explicitly, including a fixed three-record anchor cycle; no
  actual C image bytes supply the prediction. All **720 protected data owners /
  189,088 bytes**, other function bodies, addresses, guard history and conversion
  rows remain fixed. Nine strict-image controls reject, including both original
  JALs, target entry, last table entry, adjacent coefficient, neighbor, extent, named
  anchor value and ELF header.
- Five complete packaged tests pass in both closed tools roots before and after
  installation: **20 fresh checks**, equal reports and audited import/data
  closures. Shared `make tools-check` passes. The real dirty tools sibling is
  preserved; qualification uses an isolated twin with immutable dependencies.

ELF SHA256: `ea77aae524e21278d3b274c51cfa4de5055dd2ac80664a6848a983cd59c88b47`.
Mapped/aligned typed objects define the native C scope; guest-only aliases and
fault prefixes provide additional machine evidence. No new visible gameplay
acceptance is claimed.

README changes are its two aggregate rows only. Graph refresh uses scoped AST
extraction with old-ID and qualification retention, not full-corpus extraction.
Final graph/hook/immutable-bank receipts live in
`conker/build/game-preset-pointer-selector-1519003c-private/`. Host applicability
is assessed read-only: the N64 object table-anchor setting is specific to the
decomp build. There are no host edits, builds or launches; Release stays frozen.
N82 `func_1514EECC` remains parked. No push or subagent is used.

Next: continue ordinary unmatched Game matching from the sealed N91 bank.
