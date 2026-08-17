# Plan to 100% — Byte-For-Byte US ROM

Working checklist for finishing the US build. Numbers below are the verified
snapshot from 2026-08-17 (commit `512fe07`). Regenerate all numbers before
planning a session; do not trust this file's counts after any landed batch.

## Goal and ground rules

- **Done** means `make -C conker replace NON_MATCHING=1 && make --jobs`
  produces `build/conker.us.z64: OK` (sha1 `4cbadd3c…`), with every linked
  function byte-exact or deliberately raw asm.
- The symbol-based matcher (`make -C conker match-progress NON_MATCHING=1`)
  is the authoritative per-function measurement. Whole-ROM diffs mislead
  once layout drifts.
- Never enlarge a retail span, never edit matcher rules to hide diffs, never
  use a shifted current-build address as ground truth
  (see `DOCS/CONTRIBUTING.md`, "Avoid false wins").
- Commit only tracked source/config/docs; worklists and build output stay
  untracked.

## Current state (2026-08-17)

| Section | Byte-exact | Blocked | Differ |
| --- | ---: | ---: | ---: |
| total | 2529 / 5978 (42.31%) | 1 | 3448 |
| init | 387 / 508 | 1 | 120 |
| game | 1969 / 5289 | 0 | 3320 |
| debugger | 173 / 181 | 0 | 8 |

Work inventory behind those 3,449 non-exact rows:

| Bucket | Count | Nature |
| --- | ---: | --- |
| Real C, small diffs | ~363 | compiled code differs by 1–20 words |
| `return 0;` stubs | 3,086 | placeholder writes wrong bytes into ROM |
| of which touch COP0 | 11 | cannot be C under IDO (see Phase 3) |

Stub sizes: 157 are ≤24 words, most are 25–150 words; 435 source files hold
them. Largest files: `generated_142560` (65), `generated_49D30` (51),
`generated_B3020` (47), `generated_20AE20` (45), `generated_1BA1D0` (40).

Raw-asm remainder outside the matcher: 60 functions (TLB/cache/CP0/startup),
already retail bytes, no ROM impact. Converting them is optional polish.

## Per-session runbook

1. **Environment** (macOS host): submodules initialized, `baserom.us.z64`
   symlinked/renamed from the ROM, image built once:
   `docker build --platform linux/amd64 . -t conker-amd64`.
   All commands run through `conker/q.sh <cmd>` or:
   `docker run --rm --platform linux/amd64 -v "$(pwd)":/conker -w /conker/conker conker-amd64 bash`.
2. **Regenerate worklists** (fast, always fresh):
   ```sh
   conker/q.sh "cd conker && make --jobs 8 NON_MATCHING=1 >/dev/null 2>&1 && \
     make match-progress NON_MATCHING=1 LIST=1 2>/dev/null | grep -E '^(DIFF|BLOCK)'" \
     > nonexact.txt
   # stubs.txt: functions whose source body is a bare `return 0;` placeholder
   # (classifier script in WORKING_NOTES 2026-08-17 entry; or rerun
   #  cluster_stubs.py after rebuilding stubs.txt)
   ```
3. **Loop** per function/file: inspect retail asm (`conker/asm/<slice>.s` or
   `fdiff.py`), edit C, then:
   ```sh
   conker/q.sh game/generated_XXXX.c -- func_YYYY [...]
   ```
   which rebuilds the object, relinks, and diffs against retail.
4. **Validate before committing** (required by CONTRIBUTING):
   ```sh
   conker/q.sh "cd conker && make --jobs 8 NON_MATCHING=1 2>&1 | tail -1 && \
     make progress NON_MATCHING=1 2>&1 | grep -E '^\|' && \
     make match-progress NON_MATCHING=1 2>&1 | grep -E '^\|'"
   git diff --check
   ```
   Exact count must rise by the expected number; no section may regress.
5. **Commit** style: short imperative subject (`7 more byte-exact game
   functions`), note the new total in the body.

## Phase 1 — real-code small diffs (~363 functions)

Smallest-diff-first order: `grep -E '^DIFF' nonexact.txt` sorted by the diff
count. Run `conker/tools/perm.py FUNC` first; it applies the known idiom
transforms automatically and `--apply` writes winners back
(`batch_perm.py N` sweeps everything with ≤N diffs). When the permuter
fails, work manually with `tools/fdiff.py` output plus these session-proven
moves (details and examples in `DOCS/WORKING_NOTES.md`, 2026-08-17 entry):

- Float sums: try both associativities and every load order; only one
  permutation usually matches (`func_15144A74` took a 144-variant matrix).
- Pointer arithmetic: reassociate constants (`p + 0x88 + i*0x34`), index
  through a cast record type instead of raw byte math.
- Branch operand order: plain `a == b` mirrors unpredictably; retail often
  wrote `(a - b) == 0` / `!= 0` — the subtraction fixes rs/rt.
- Calls: a callee that looks argument-less may still receive the just-loaded
  value; passing it reproduces `beql` + delay-slot moves.
- Comparison-heavy chains: each comparison needs its own idiom choice; fix
  them one at a time, relinking between edits.

Known-stuck patterns (parked, need research — see backlog): `jal` +
`or a0,v0,zero` delay move with global in `v0` (`func_1509D054`), dead
argument homing `sw a0, home(sp)` in a delay slot (`func_151ACB60`), pure
register-allocation swaps like `t7`↔`t8`/`v0`↔`v1` (`func_1519C910`,
`func_15087FC4`). Don't burn a session re-trying source shapes on these;
install the upstream decomp-permuter instead (Backlog T1).

Also here: `func_10012588` (init, the sole address-drift blocker — its call
resolves to the wrong linked target; heal by making the callee exact or
fixing its placement) and the two debugger stragglers' bigger brothers
(`func_16001390` at 2 diffs, `func_16000F8C` at 5).

## Phase 2 — stub decompilation (3,086 functions)

The bulk. Each stub currently writes `move v0,zero; jr ra; nop` into the
ROM image, so the ROM cannot match until every stub is either decompiled or
flipped (Phase 3).

Strategy, in order of value:

1. **File-batched, smallest stubs first.** Sort files by
   `(mean stub words, stub count)`. A 30-stub file usually shares struct
   accessors/state machines; recover the record types once (CONTRIBUTING,
   "Recover record types before forcing operand order") and the rest fall as
   families. One `q.sh` invocation checks a whole file's functions.
2. **First pass with mips_to_c**: `python3 tools/mips_to_c/m2c.py
   conker/asm/<slice>.s` (asm slices hold the retail instructions), then
   hand-normalize names/types. Expect ~80% semantic accuracy; byte-exactness
   still needs the Phase-1 idiom loop per function.
3. **Cross-reference ports** for SDK/duplicate bodies: check the project's
   already-exact primary copy first (`conker/src/libultra/...`), then
   local `banjo_decomp`/`dk64-main` checkouts if present, with the owning
   object's compiler profile (`-O1` for stock SDK, `-g` for audio —
   Makefile override list already encodes most of these; new splits must be
   recorded in `conker.us.yaml` with objects in retail order).
4. **Repeat-family sweep**: before decompiling a shape, grep the retail asm
   for identical instruction bodies at other addresses; solve the shape once
   and clone with constants adjusted (verify each member — offsets and
   signedness differ).

Throughput note: small accessors run ~10–30/session; 100+ word state
machines can take a session each. At roughly 10/session average this phase
is ~300 sessions — automate everything you can (Backlog T2, T3).

## Phase 3 — COP0 stragglers and the asm-flip decision (11 functions)

Cop0-touching non-exact functions:
`__osDisableInt, __osGetSR, __osProbeTLB, __osRestoreInt, __osSetCompare,
__osSetSR, osGetCount, osMapTLB, osMapTLBRdb, osSetIntMask, osUnmapTLB`.

IDO 5.3 `cc` silently drops `asm("...")` strings, and there is no CP0
intrinsic — these bodies cannot be produced from C (verified 2026-08-17).
The SDK shipped them as `LEAF()` assembly; ultralib
(`tools/ultralib/src/os/*.s`) holds reference sources.

Decision needed (maintainer call, blocking only for the final ROM sha1):
flip each back to raw asm by **deleting its `src/game/generated_<name>.c`**
file — `tools/patch_generated_slice_ld.py` then keeps the original
`build/asm/...s.o` in the link, restoring retail bytes at the cost of one
C-conversion row each (converted count drops by 11, ROM gains correctness).
Alternative if 6038/6038 conversion is a hard goal: leave them as the
documented permanent exceptions and accept a non-matching ROM — not
recommended given the stated goal. Whatever is chosen, record it in
`DOCS/PROJECT.md` and the progress tables.

## Phase 4 — endgame and final validation

Once match-progress shows 5978/5978 exact (or the agreed flipped roster):

1. **Empty the overflow sections.** Non-matching oversized functions execute
   out-of-line at `0x10F00000/0x15F00000/0x16F00000`; their trampolines and
   ROM placement break the image. Check the map:
   `grep -E 'overflow' conker/build/conker.us.map` — every overflow section
   must be size 0, and no `__retail_overflow_*` symbols may remain.
2. **Full pipeline, uncompressed first**: `make -C conker replace
   NON_MATCHING=1 && make --jobs`. A `FAILED` that survives 100% function
   exactness means section padding/placement or rzip output differs — diff
   `conker/build/conker.us.bin` against `conker/conker.us.bin` with
   `tools/first-diff.py`, and check `assets/game/code_padding.bin` usage and
   linker-script anchors (`retail_layout.us.txt` rows) around the first
   differing byte.
3. **Determinism check**: rebuild twice from clean (`make -C conker
   really-clean` path, re-extract) and confirm identical sha1 twice.
4. Final gate: `build/conker.us.z64: OK`. Update README/PROJECT tables,
   UPDATE_LOG milestone, and this file (mark phases done).

## Research backlog

- **T1 — upstream decomp-permuter.** Install
  `github.com/simonlindholm/decomp-permuter` (gitignored as optional tool;
  aliases in `.bash_aliases` already expect it under `tools/`). Import the
  stubborn Phase-1 functions and let it search line layout, `condition ^ 0`,
  temp insertion. Expected to unlock the parked register-allocation cases.
- **T2 — perm.py transform library.** Add: pointer reassociation (`p + c +
  i*k` permutations), record-typing rewrites, per-comparison idiom mixing,
  argument-passing variants for zero-arg calls, `u8/u16` parameter-width
  sweeps. Each transform should encode one *verified* recovery from
  WORKING_NOTES so `batch_perm.py` can sweep stubs after first-pass
  decompilation.
- **T3 — stub triage bot.** Extend `cluster_stubs.py` with fuzzy opcode
  windows (register-normalized, constant-masked) to surface families the
  exact-signature clustering missed (current: 2,980 clusters, largest 5).
  Feed matches to a mips_to_c + perm.py pipeline for unattended
  first-passes; human review stays mandatory before `--apply`.
- **T4 — unsolved codegen shapes.** jal-delay `or a0,v0,zero`, dead arg
  homing, and the `func_1519C910`-style allocation flips. Approach: find
  these patterns in *already exact* functions (none known for the first
  two), or bisect with the permuter once T1 lands.
- **T5 — remaining 60 raw asm conversions** (optional, after ROM OK):
  TLB/cache/CP0/startup per WORKING_NOTES; most have no C form, so this is
  documentation-only work.

## Appendix — measurement commands

```sh
# per-function truth
conker/q.sh game/<file>.c -- func_<addr> [func_<addr>...]
# full sweep + list
conker/q.sh "cd conker && make match-progress NON_MATCHING=1 LIST=1" | tail -n +7
# first ROM byte difference after replace
conker/q.sh "python3 tools/first-diff.py"   # uses diff_settings.py paths
```

History of technique: `DOCS/CONTRIBUTING.md` (curated) and
`DOCS/WORKING_NOTES.md` (session log, newest findings last).
