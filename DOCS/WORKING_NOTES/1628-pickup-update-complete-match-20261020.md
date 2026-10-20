# Pickup Update Complete Match

Date: 2026-10-20. Consumer predecessor: `7ac0d759`.
Tools predecessor: `9c3c005`; checkpoint **b66644c** is committed first.
This completes [Note 1627](1627-pickup-update-private-homes-and-selector-cursor-20261019.md).
The user expanded the active objective to **75% total byte-exact C matching**.
The previous and current turns make progress; the wider goal is not complete.

## Installed Result

Complete typed `void func_1508DC24(void)` replaces the 12-byte zero-return
placeholder in [generated_B3020.c](../../conker/src/game/generated_B3020.c).
All **681 words / 2,724 bytes / frame 280** are now byte-exact:
VA **1508DC24..1508E6C8**, ROM **BB0D4..BBB78**.

The original function name and purpose comment are preserved. The body handles
player item states, attached-effect pruning and pickup respawns, with recovered
signed counts/modes/selectors, word-width states, original reloads, ownership
updates and coordinate-helper calls. All 17 private homes and the cached-base
versus live-cursor distinction from the preceding note remain intact.

**This is a guarded reconstruction, not a compiler-only match.** Both existing
compiler profiles still emit the same raw **680 words / 636 counted
differences / 73 bindings**. No compiler flags or Makefile are changed.

## Checked C Origins

[The layout recipe](../../tools/experiments/game_pickup_state_update_layout.py)
maps the complete semantic C object to the original instruction/register
schedule. Its normalizer reads no ROM, assembly or diagnostic file.

- Retain **667 unique C origins**, coalesce 13 redundant origins and reuse
  existing origins 14 additional times: 680 - 13 + 14 = 681 output words.
- Derive 32 positions, including ordinary/likely branch forms, equivalent
  equality operand orders, direct symbolic memory accesses and the independent
  null-object path. These are not 32 extra instructions.
- Recover five lifetime-scoped role intervals and **406 typed operand fields**.
  Branch destinations follow source origins, with six explicit control-flow
  exceptions, all fingerprinted and tested.
- Preload the existing effect-kind constants, reuse real effect cursors and
  increments in their original branch-delay positions, and retain the original
  signed selector addition/store behavior.
- Coalesce redundant argument copies, literal/address materializations and
  private counter reloads at their original common blocks. Five copies of an
  existing zero word occupy mandatory executable branch delays, not tail padding.
- Recover **77 output bindings** from the 73 raw entries. The selector and
  tick bases split into their original direct references; the actor base is
  hoisted and its 0x31C offsets retained. Exact code and binding maps match an
  independently GNU-assembled original object.

The recipe pins the raw code, raw bindings, origin/role/branch description,
normalized code and output bindings. All 680 raw-word and linked-field
mutations, 73 binding mutations, 406 operand-field changes and six branch
exception changes are rejected.

## Guard And Production Gates

[The integration helper](../../tools/experiments/game_pickup_state_update_integration.py)
appends **680 expected-word rows**, including **181 identity checks**.
One real effect-kind preload (`addiu fp,zero,0x22`) is inserted after raw
offset **B4**, at output word 46. The entire previous manifest prefix is
preserved byte-for-byte; there are no omitted CSV rows.

Both full raw owner profiles preserve all **72 other bodies and pools**.
The actual seven-command expanded Make shadow uses the same four existing
normal-profile overlays; this target needs no extra overlay. Actual padding
keeps all 73 owner addresses and changes only the target extent, **12 to
2,724 bytes**. Omitting the required existing route-search overlay is an
effective wrong-profile control.

The first independent full link caught two closed GNU symbol-order groups:

| Previous Order | Required Order |
| --- | --- |
| D_8009DA90, D_8009D1E0, D_800A6060 | D_8009D1E0, D_800A6060, D_8009DA90 |
| D_800AB494, D_800886F4 | D_800886F4, D_800AB494 |

Prediction explicitly preserves each symbol's attributes/value/section and
rewrites only those named slots/string entries, in addition to target code
and target symbol size. No ELF section or metadata range is excluded.
The actual production build exactly reproduces that complete image:

- **2,205 changed bytes**: **2,167 target-code bytes**, **38 metadata bytes**.
- The metadata consists of two target-size bytes and 36 bytes in those exact
  symbol/name permutations. Header, neighbor, target, size and each named
  metadata-slot/string mutation are rejected by the wrong-image tests.
- Every **6,056 other function body**, all **6,057 function addresses** and
  all **189,088 protected Game-data bytes / 720 owners** remain fixed.
- The ROM, original assembly, Makefile and progress CSV are byte-identical.
  This replaces already-counted C; it does not create a conversion row.

The actual build exits zero in **330.783s**. Existing broad-build warnings
remain visible in its saved log; the focused owner compiles without diagnostics.

## Qualification

**27 pre-install tests pass in each copy**, zero skips/errors/failures.
Primary **140.949s**; standalone mirror **112.284s**.
**27 installed tests also pass in each copy**, zero skips/errors/failures:
primary **76.920s**, standalone mirror **54.918s**.

- All 234 corpus cases, both profiles and both stack phases pass:
  **936 candidate fixture/profile/phases**, all **681 retail words visited**.
  Ordered public reads/writes, canonical calls and full public state agree.
- **468 complete final modeled states** now match literally, including GPRs,
  FPRs, condition, lo, complete private/public RAM, access/call/visit histories.
  This closes the preceding note's 0/468 literal final GPR result.
- **818 fired own-access cuts** compare the same complete modeled state before
  attempted reads/writes: first and last access per PC across six fixtures
  in two stack phases. Constructor, provider and call-argument bookkeeping
  cannot satisfy these gates. The old raw layout is an effective GPR negative
  even when its final memory agrees.
- Three independently GNU-linked original code/data rebase plans exercise
  signed LO16 carries and the 0x31C actor addends. **36 rebased phases** pass.
  The raw C and original are linked independently, not by a relocation helper
  that discards LO16 addends.
- Retain 34 fired home aliases/34 effective old-home controls, two live
  selector-cursor aliases/two intermediate controls, eight real original
  coordinate-helper phases/four old-home controls and the extra-read negative.
- Retain 234 native32 fixtures at O0/O2/O3 with trap UBSan, six compiled
  semantic negatives and the actual installed-predecessor stub negative.
- All four task files agree between tools copies; eight Python copies parse.
  Both project-tools checks pass. Historical seven-input fixtures are frozen
  explicitly after a strict live installed audit; historical pins are not
  rewritten to accept the new source.

Hardware FCSR/MMU behavior, unrestricted connected providers/local capacity,
complete gameplay and host-port acceptance are not claimed. The host Release
checkpoint, real saves/configuration and sibling source are untouched.
Unchanged neighbor-suite receipts are reused through whole-image preservation,
not represented as fresh broad runtime tests.

## Counts And 75% Target

Fresh actual matcher: **Game 3,020/4,832 (62.50%)**,
**overall 3,693/5,505 (67.08%)**, **1,812 different / zero drift**.
Init remains 492/492 exact; Debugger remains 181/181 exact.
Owner is **72/73 exact**, leaving `func_1508CAD8` (862 words).

The target is the README's existing function-matching metric, not converted
bytes or percentage of all assembly routines. At denominator 5,505, 75%
requires **ceil(0.75 * 5,505) = 4,129 exact functions**, hence **436 additional
matches** after this checkpoint. Recalculate if the conversion denominator
changes. Root README gets only refreshed aggregate rows/date.

A fresh ignored `75-percent-queue.json` is pinned to the actual installed ELF.
It classifies the 1,812 nonexact entries as 1,677 simple zero-return placeholders,
126 semantic/other definitions and nine not located by the bounded source
lookup. Those source-shape counts and instruction traits are a triage screen,
not ABI, semantic or installation qualification.

The smallest 32-word entry, `func_150A76F0`, is explicitly handwritten and
returns through v0 with inputs in non-o32 registers. Do not invent ordinary C
or normalization from its length alone. The first unflagged small candidate,
`func_1519BE1C` (39 words, generated_1C2C60), has been read in full: it
copies three incoming velocity words, updates vertical velocity and integrates
position using acceleration and timestep. Audit its callers, float ordering
and alias behavior before conversion. The other 39-word candidates and the
remaining 862-word owner routine stay queued, not declared complete.

## Preservation And Receipts

All **1,466 pre-existing mirror dirty paths/statuses/hashes** and HEAD
`ddbdd16b` are preserved. Only the four absent task files are added;
final dirty paths **1,470**. No mirror commit/reset/stash/clean, push,
dependency/compiler update or advisory writer.

```text
Raw C code:   aa2d148b4b51b725d32722cd832571aad2822a9bc68f16a97116b93a3a411f82
Raw bindings: 69b8067c4b8d498971e8f9aaef8d3522e8bb230c5b88fc14698b9c56af09b978
Recipe:       b0d2527c2fe5bf8a2d80673dc0199495a2e2129173c1929cba85a2f5826ab0fc
Normalized:   5e52891e4fa104702217ed8bad51fe03490d6e4e9a3e36733887e6fdc9d1e6c2
New bindings: 56b606886944ff98d418f3fbe06c0c8b45a37623301296b76232b63fa5efda60
Installed C:  6d27ddeec0aa1d0ccb55d601a7ed08aa96a591a076c2a3adccd7818b60b7f7b5
Guards:       7ca8a25f8ea41d9e2e4a795281619c21048f5c24b252d48a9367eb5cd5e36e76
Linked ELF:   7854836fbb41afc2d971461115bf67053eeb41f9d190434c10e7cb668ca49ecd
```

Ignored receipts live under
`conker/build/game-pickup-state-update/lifetimes/layout/`:
primary/mirror pre-install and installed logs/JSON, original/rebased objects,
fault-cut/native/home-alias receipts; `integration/` holds full owner/Make/
padding/first-link/build/audit/matcher receipts, mirror preservation, queue,
and graph before/after evidence. Graph closeout is recorded after the consumer
commit. No claim of achieving the 75% goal.
