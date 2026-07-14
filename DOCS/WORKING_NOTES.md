# Working Notes

A running log of in-progress work. The point of this file is recovery: if an
editor, terminal, or assistant session crashes mid-task, the next session
(human or AI) can read this file and pick up where things left off without
re-deriving context from scratch.

This is a scratch/log document, not polished documentation. Entries are
allowed to be rough. Once a piece of work is finished and stable, its
findings belong in [ASSET_FORMATS.md](ASSET_FORMATS.md), [PROJECT.md](PROJECT.md),
or another permanent doc, and the entry here can be trimmed down to a one-line
summary or removed.

## How to use this file

1. Before starting a non-trivial task, add or update the **Current focus**
   section below with what you're about to do and why.
2. While working, jot down anything that would be expensive to re-discover:
   the file/function you were in, a command that reproduced a bug, a
   hypothesis you ruled out, a partially-written patch that isn't committed.
3. When you stop (task done, or interrupted), update the entry with the
   actual end state: what's done, what's half-done, what's next.
4. Start a new dated entry in the **Session log** for each distinct work
   session; keep the newest entry at the top.

## Current focus

**Status:** build works end-to-end (extract → compile → link → replace →
reassemble ROM). Ran a real matching pass on the 44 ECTS-ported functions
using both the linked ELF and a custom ground-truth-vs-compiled-bytes
comparison script (asm-differ's whole-binary `-m` mode is unreliable right
now - see gotcha below). 6 more now byte-match exactly (2 new real fixes, 4
were already matching but an earlier verification method gave false
negatives), and 6 more are confirmed logically complete (their only
remaining diff is a call to a still-unmatched function elsewhere - nothing
left to fix in those functions themselves). 32 genuinely still need work.
**Working on:** Function-matching passes on the remaining 32. Two real
fixes so far worth knowing about (see Session log): `func_15079A58` needed
`D_800D2110`'s declared type corrected from `s16[]` to `s16*` (ECTS agreed);
several others hit register-allocation quirks in IDO that resisted a few
rewrite attempts and were left as-is rather than sunk-cost-chased further.
**Files touched (infra fixes):**
- `conker/conker.us.yaml`: added `asm_nonmatching_label_macro: ""`,
  `asm_function_alt_macro: glabel`, and `generate_asm_macros_files: false`
  to `options:`; changed 26 standalone `rodata` subsegments to `bin` (see
  link-blocker writeup below); split one of those (`0x236430`) into three
  pieces (`data`/`bin`/`data`) since two legitimate data symbols lived right
  at its edges.
- `conker/include/macro.inc`: kept the project's original simple
  `glabel`/`dlabel`/`jlabel` macros (auto-regeneration is now disabled - see
  above), and added no-op `endlabel`/`enddlabel` macros since current
  splat's raw `.s` output now emits those unconditionally and the originals
  didn't have them.
- `conker/include/asm_processor_prelude.inc`: new file, extends
  `tools/asm-processor`'s bundled `prelude.inc` with `alabel`/`ehlabel`/
  `enddlabel` (all as trivial no-op-style macros matching the existing
  `glabel`/`dlabel`/`jlabel`/`endlabel` style already there). Used only by
  the GLOBAL_ASM-in-`.c`-files path; unrelated to `macro.inc` above, which
  is used by raw top-level `.s` files - the two don't need to match each
  other's style since different tools read them.
- `conker/Makefile`: point `--asm-prelude` at the new file instead of
  `$(ASM_PROCESSOR_DIR)/prelude.inc`.
- `tools/splat_ext/rzip.py`: accept/forward `**kwargs` in
  `N64SegRzip.__init__`.
- `conker/include/variables.h`: `D_800D2110` type fix (see above).
- A repo-wide re-checkout to fix CRLF corruption (see below - no source
  content changed, just line endings/symlinks).
**Files touched (ECTS port, see Session log for full results):** all 14
`conker/src/{game,debugger}_*.c` files that had ECTS-matched functions this
repo didn't, plus `conker/include/structs.h`, `conker/include/variables.h`,
and `conker/include/functions.h` to add the struct fields/globals/prototypes
those functions needed that hadn't been discovered here yet.
**Last known good state:** `make check`, `make extract`, `make -C conker
extract`, the full C compile, and the full link (`build/conker.us.elf` and
`build/conker.us.bin` both produced) all succeed from a totally clean
`rm -rf asm build assets && make extract`. `make -C conker replace
NON_MATCHING=1 && make` from repo root produces `build/conker.us.z64:
FAILED` (expected - ROM isn't byte-perfect yet, only ~20% of functions are
matched) rather than erroring out. `make -C conker progress NON_MATCHING=1`
produces real, `.map`-file-derived numbers - see [PROJECT.md](PROJECT.md)
for the current table (unchanged by this matching pass, since `progress.py`
counts by GLOBAL_ASM-pragma presence, not byte-exactness, and no pragmas
were added/removed here).
**Next step:** keep working the 32 remaining real diffs (list and diff
sizes in Session log below), smallest first. The verification scripts below
aren't committed (scratchpad only) - rewrite is quick if needed, see the
"Verification method" note in the Session log.
**Gotchas:**
- `conker/include/macro.inc` used to get silently regenerated by splat on
  every `make extract` with a newer `.ent`/`.aent`-based template
  incompatible with the project's original simple macros - this is now
  disabled (`generate_asm_macros_files: false` in `conker.us.yaml`), so the
  committed file is authoritative again. If you ever re-enable that option,
  expect this file to change out from under you.
- **asm-differ's whole-binary `-m`/`-o` modes are unreliable right now.**
  There's a pre-existing (not caused by this session - `init` was never
  touched) byte-level divergence starting at file offset 15835 in
  `build/conker.us.bin` versus the pristine `conker.us.bin`, inside the
  already-58%-matched `init` section. Since asm-differ's default mode reads
  the *whole rebuilt binary* at a function's mapped offset, anything
  downstream of that divergence point (which is effectively all of `game`
  and `debugger`) can show garbled/empty comparisons even for functions that
  are actually byte-perfect. Nobody could see this before this session since
  the ROM never linked successfully here before. Root-causing the
  init-section drift is a separate, larger task - not attempted here. In
  the meantime, verify functions by comparing the *linked* ELF's
  disassembly for a given function symbol (immune to this, since it reads
  bytes at the function's own address rather than walking sequentially from
  file start) against ground-truth bytes read directly from the pristine
  `conker.us.bin` at the function's VRAM-derived offset - see the
  `elf_words()`/`ground_truth_bytes()` pattern in the (uncommitted,
  scratchpad) verification scripts used this session.
- This workspace's git checkout had `core.symlinks=false` and CRLF line
  endings baked into the working tree for ~450 tracked files (pre-existing,
  not caused by this session - visible in `git status` from the very start
  of the conversation). Both are now fixed locally (`core.symlinks=true`,
  `core.autocrlf=input`, full re-checkout). If a fresh clone/devcontainer
  shows this again, see the fix steps below rather than re-deriving them.
- The pinned `tools/n64splat` submodule commit (`d6ae992`) is newer than
  whatever version `tools/splat_ext/rzip.py` was originally written against:
  it now passes a `bss_size` kwarg into segment constructors that the old
  signature didn't accept. Fixed by accepting `**kwargs`.
- Current `tools/n64splat` also defaults `asm_nonmatching_label_macro` to
  `"nonmatching"` and `asm_function_alt_macro` to `"alabel"` for all
  compilers (including IDO). The pinned `tools/asm-processor`'s
  `process_line()` hardcodes recognition of only the literal words
  `glabel`/`dlabel`/`jlabel`/`endlabel` when pre-computing section sizes (grep
  for `text_glabels` around asm_processor.py:612-616 to see exactly). Any
  other macro name in a generated `.s` file - `nonmatching`, `alabel` - gets
  silently miscounted as a real instruction, producing either `.text block
  without an initial glabel` or `incorrectly computed size for section
  .text`. Fixed by disabling the nonmatching-size annotation entirely
  (confirmed `tools/progress.py` doesn't read it) and by making splat emit
  `glabel` instead of `alabel` for alternate function entry points (adding a
  second `glabel` line for the same concept works fine and IS recognized).
  Also swapped `--asm-prelude` from the submodule's sparse `prelude.inc` to a
  new project-owned file so `alabel`/`ehlabel`/`enddlabel` are at least
  defined as assembly macros too, independent of the asm-processor
  size-counting fix. The `conker.eu.yaml`/`conker.debug.yaml`/
  `conker.ects.yaml` configs are much less developed (no `platform:`,
  different options) and weren't touched - revisit if those versions are
  ever built for real.

### Link-time blocker: RESOLVED (2026-07-14)

`make -C conker --jobs` compiled every `.c` file successfully but failed at
the final link (`build/conker.us.elf`) with **1153** `undefined reference to
'.L15xxxxxx'`-style errors, spread across 26 files under
`build/asm/data/*.rodata.s.o` (e.g. `249CC0.rodata.s.o`, `24B280.rodata.s.o`,
`game_161520.rodata.s.o`).

**Actual root cause** (the theory below at the time this was first written
turned out to be half right): these `.rodata` chunks are jump tables,
declared in `conker/conker.us.yaml` as **standalone** `[addr, rodata]`
subsegments (e.g. `- [0x249CC0, rodata]`), each containing an array of code
addresses (`.word` values) that other, often-distant functions jump through.
Splat's disassembler only auto-labels a jump-table *target* address
(emitting a real, linkable `jlabel`) when it can see, in the same analysis
pass, that the address is referenced by a jump table it recognizes as
belonging to that function's own context. Declared as bare `rodata`, these
tables get disassembled as generic data with symbolic `.L`-prefixed
references to their target addresses - and `.L`-prefixed symbols are a hard
GNU-as convention for compiler-local temporary labels that are **discarded
at assembly time and can never be made global**, no matter what `.global`
directives you add after the fact (confirmed by trying it - not worth
repeating). Some targets also turned out to sit in address gaps that no
declared function/segment covered at all (e.g. `.L15141CB4` referenced
4 instructions *past* the end of the function `splat` currently thought
owned that address range), so this wasn't purely a labeling problem - in a
few spots the function boundary itself was wrong.

Tried and abandoned: `symbol_addrs.us.txt` supports `type:jtbl_label` and
`segment:<name>` attributes specifically for this scenario, but they only
rename the *reference* side (turning `.L15141CB4` into a real name in the
referencing `.s` file) - they don't create a *definition* unless the target
address already falls within a segment that gets symbolically disassembled,
and don't fix cases where the target address isn't covered by any segment.

**Actual fix:** the jump-table *contents* don't need to be human-readable
disassembly at all - nobody is going to hand-match a jump table's raw
`.word` values as "C code." Changed all 26 standalone `rodata` subsegments
in `conker/conker.us.yaml` to `bin` (raw opaque byte blobs, linked in
directly via `ld -r -b binary`, no symbolic disassembly, no cross-file label
references, byte-identical to the source ROM by construction). This
eliminated all 1153 errors in one pass. It also had a good side effect: with
the standalone rodata segment gone, splat's own boundary detection correctly
re-drew the neighboring function's boundary to include the address that used
to be an out-of-range gap (`func_15141C0C` in `game_16EE20.c` now correctly
extends to the address that used to be `.L15141CB4`, no longer needing any
external reference at all).

One block (`0x236430`) turned out to contain two legitimate, by-name-referenced
data symbols (`D_80091A30`, `D_80091AB8`) right at its edges, not just
jump-table garbage - converting the whole block to `bin` removed their
definitions too, producing 2 new `undefined reference` errors (confirmed via
diffing against the pre-existing `symbol_addrs.us.txt` entries and computing
their byte offset within the block: `0x2364F0` and `0x236578`, both inside
`[0x236430, 0x2365B0)`). Fixed by splitting that one block into three:
`[0x236430, data]` (before), `[0x236510, bin]` (the actual problem region,
narrowed down from the original link-error offsets), `[0x236578, data]`
(after) - restoring symbolic disassembly (and therefore real `dlabel`
definitions) for the two legitimate data symbols while keeping the jump
table itself opaque.

**Result:** `make -C conker --jobs` now produces `build/conker.us.elf` and
`build/conker.us.bin` cleanly. `make -C conker replace NON_MATCHING=1 &&
make` (repo root) produces a real `build/conker.us.z64` - it says `FAILED`
against the sha1 check, which is expected and correct given only ~20% of
functions are matched (see [PROJECT.md](PROJECT.md)'s progress table,
freshly regenerated from this working build). `make -C conker progress
NON_MATCHING=1` works for the first time and produced the current numbers in
PROJECT.md.

If similar `undefined reference to '.L...'`-style link errors show up again
after matching more functions near a `rodata`/`bin` boundary, check whether
the newly-matched function's actual byte range still lines up with what the
neighboring `bin` block assumes - the `0x236430` situation above is the
pattern to look for (a `bin` block edge sitting right next to a real,
by-name symbol another file depends on).

### CRLF/symlink fix steps (for next time)

```sh
git config core.symlinks true
git config core.autocrlf input
# Force re-checkout of every tracked, non-submodule file so the working tree
# picks up clean LF content and real symlinks (plain `git checkout -- .` is a
# no-op here since git already considers CRLF-vs-LF "clean" once
# core.autocrlf is set - the file has to be removed first):
git ls-files -s | awk '$1 != "160000" {print $4}' > /tmp/tracked.txt
xargs -a /tmp/tracked.txt -d '\n' rm -f
git checkout -- .
```

## Session log

### 2026-07-14

- Added this file and [PC_PORT_ROADMAP.md](PC_PORT_ROADMAP.md), and linked
  both from [README.md](README.md).
- User asked to continue mapping the `game` section using `debug_proto/` and
  `ects_proto/` (untracked sibling checkouts of this same decomp targeting
  the debug and ects ROMs respectively) as reference. `debug_proto` and
  `ects_proto` are byte-identical to each other in `conker/src/` (0 files
  differ) but 277 of 82 tracked `game_*.c` files differ from this repo's
  `conker/src/` - some files ahead here, some ahead there. Main repo's
  overall matched-function count (1475/7261) is higher than the proto trees'
  (1429/7261 each), so the plan is to selectively pull over the functions
  *they* have matched that *this repo* doesn't, file by file - not a wholesale
  merge.
- Before any of that could start, the build was completely broken in this
  workspace: fixed the symlink/CRLF checkout corruption and two
  splat-version compatibility bugs (see Current focus above) needed just to
  get `make extract` / `make -C conker extract` working at all.
- With a working compile, ported all 56 candidate functions (46 `game`, 10
  `debugger`) from `ects_proto/conker/src/` into this repo's `conker/src/`,
  replacing their `#pragma GLOBAL_ASM(...)` stubs with the real matched C
  bodies. Mechanical extraction was via a small Python script (brace-counted
  function-body extraction + exact pragma-string replacement); it's in the
  scratchpad, not committed, but the approach is simple enough to redo:
  find `<rettype> <funcname>(` at column 0, then match braces from the
  following `{` to find the end.
  - **Extraction gotcha:** the first version of the script matched the
    *first* occurrence of `funcname(` in the source, which for a handful of
    functions was a forward declaration (`void func_X(void);`) rather than
    the real definition, and then grabbed the *next* unrelated `{` in the
    file as the "function body" - producing duplicate/corrupted functions in
    `debugger_256F80.c` and `debugger_257350.c` specifically. Fixed by
    checking that the character after the matched parameter list's closing
    `)` is `{` (skipping straight to `;`-terminated prototypes). Re-ran
    cleanly for `debugger_257350.c`; hand-fixed `debugger_256F80.c` (only one
    function affected there, `func_160018BC`) since it had already been
    manually patched for other errors by that point.
  - **Struct/header divergence:** ects_proto's struct definitions have
    diverged from main's (more fields discovered there, since more
    functions have been matched using them). Every ported function that hit
    a "field/type undefined" compile error needed the missing struct
    field(s), global variable(s), or function prototype ported over from
    ects_proto's `structs.h`/`variables.h`/`functions.h` too - in every case
    this was ects turning an existing anonymous `padN[size]` byte range into
    named sub-fields of the same total size (safe, no layout change), except
    for `struct210.unk3C` and `struct102`/`struct115`/`struct126`/`struct127`
    a few fields where ects had also *widened* a struct past main's
    previously-assumed size. Cross-checked each field name for existing
    live (non-comment, non-GLOBAL_ASM) usages elsewhere in `conker/src`
    before changing a type, to avoid silently breaking an already-working
    function; found none.
  - **One real pre-existing bug fixed along the way:** `game_1944C0.c`'s
    `func_1516972C`/`func_1516979C` (already matched, not part of this port)
    called `func_151696DC()` with zero arguments via an implicit
    (prototype-less) declaration - harmless while `func_151696DC` was still
    raw asm, but the real ECTS-matched definition takes one `void *arg0`.
    Fixed both call sites to pass `arg0`, matching ECTS.
  - **Verification:** wrote a second small script that compares each ported
    function's freshly-compiled instruction words (via
    `mips-linux-gnu-objdump`) against the ground-truth retail-US words still
    embedded as comments in the pre-port `asm/nonmatchings/.../func_*.s`
    stub files (these survive until the next `make extract`, so re-run the
    comparison *before* re-extracting if resuming this). Full
    `tools/asm-differ` wasn't usable since the link blocker means there's no
    linked ELF/map yet.
  - **Result: 12 of 56 ported functions byte-match `us` retail exactly,
    out of the box, with no annotation needed:**
    `game_161520.c` (`func_151348F0`, `func_15134CD4`, `func_15135658`,
    `func_15136A1C`), `game_169510.c` (`func_1513F6C0`), `game_16EE20.c`
    (`func_15142AC0`, `func_15142B04`, `func_15143044`, `func_15143E24`,
    `func_15143E64`, `func_15144A74`), `game_1944C0.c` (`func_15168E34`).
  - **The other 44 compile cleanly but do not yet byte-match `us`** (ECTS
    codegen differs from retail US, as expected) - each is marked with
    `// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet
    byte-verified for us` directly above the function so nobody mistakes
    them for confirmed matches. These are still a large head start over raw
    assembly (real variable names, control flow, and struct field usage) and
    are the natural next matching-pass targets once the link blocker is
    resolved and `asm-differ` is usable again.
- Resolved the link-time blocker (converted 26 standalone jump-table
  `rodata` segments to `bin`, split one that also held real data symbols -
  full root-cause writeup and fix are above in "Link-time blocker:
  RESOLVED"). The build now goes all the way through `make -C conker
  --jobs` → `make -C conker replace NON_MATCHING=1` → `make` (repo root),
  producing a real (correctly non-matching) `build/conker.us.z64` for the
  first time. Regenerated `DOCS/PROJECT.md`'s progress table from this
  working build via `make -C conker progress NON_MATCHING=1` - the new
  numbers (1553/7644 total, 20.32%) are lower than what was previously
  documented there (2003/8062, 24.84%), which is expected: this is the
  *first* `.map`-file-derived progress count this checkout has ever
  produced (nothing before this session ever linked successfully here), so
  the old table numbers weren't verified against a working build and
  shouldn't be trusted over this one. Also updated `DOCS/UPDATE_LOG.md`.
- Ran a real matching pass on the 44 ECTS-ported, not-yet-byte-verified
  functions from the earlier session entry. Discovered the earlier
  standalone-`.o` verification method gave false negatives for any function
  making an external call or referencing external data (unresolved
  relocations show as `jal 0`/`lui at,0x0` in an un-linked `.o`, which look
  like mismatches but aren't) - switched to reading the *linked* ELF's
  disassembly instead, keyed by function symbol name (immune to the
  init-section drift noted in the Gotchas above, since it doesn't walk the
  binary sequentially). Also added a classifier that decodes each differing
  instruction word and flags cases where literally the only differences are
  jump/call target addresses - those are functions that are already
  logically correct, just waiting on a callee elsewhere to also get matched
  (once that happens, these will self-resolve without any further edits).
  - **6 more functions confirmed byte-exact** (comments removed, no longer
    marked NON-MATCHING): `game_16EE20.c` (`func_15142A80`, `func_15142B44`,
    `func_15144B34`), `game_1944C0.c` (`func_15169668`), `game_981E0.c`
    (`func_15072DA0`), `game_A28B0.c` (`func_15079A58` - genuinely fixed
    this session, not a false-negative correction; see below).
  - **6 functions confirmed "logically complete"** - their only remaining
    diff is the jal target address of a callee that isn't matched yet; the
    comment on each now says exactly which callee is blocking it instead of
    the generic "not yet byte-verified" text: `game_161520.c`
    (`func_151352EC` blocked on `func_15169804`, `func_1513530C` blocked on
    `func_15169824`), `game_16EE20.c` (`func_15143794` blocked on
    `func_151423D8`, `func_15143834` blocked on `func_15143794` itself),
    `game_1944C0.c` (`func_15168A2C` blocked on `func_15168B10`,
    `func_15169040` blocked on `func_15169070`).
  - **One real bug found and fixed:** `func_15079A58` in `game_A28B0.c`
    writes through `D_800D2110[idx]`. Retail's disassembly loads
    `D_800D2110` itself as a 4-byte *value* before indexing into it (i.e. as
    a pointer), but it was declared `extern s16 D_800D2110[];` (a fixed
    array at that address) - changed to `extern s16 *D_800D2110;` (matching
    `ects_proto`'s own declaration, which had already made this exact
    correction) and combined two statements into one
    (`D_800D2110[...] = (a<<8)+b;` instead of computing an intermediate
    `tmp` first) to match retail's instruction scheduling. Now byte-exact.
    Worth checking whether `D_800D2110`'s other few call sites need the
    same treatment if they ever get matched.
  - **32 functions still have genuine, unresolved diffs** (not just
    downstream call targets), ranging from 3 to 662 differing words:
    `debugger_257350.c` (`func_16001B00` 3, `func_16001B34` 13,
    `func_16002D2C` 35, `func_160033A8` 154, `func_1600288C` 265,
    `func_16001BB4` 365, `func_16002DE4` 399), `debugger_256F80.c`
    (`func_16001830` 25, `func_16001700` 71, `func_160018BC` 75),
    `game_83300.c` (`func_15060BA4` 5, `func_1506196C` 12,
    `func_1505EEB0` 18), `game_A28B0.c` (`func_1507A3E8` 13 - byte-packing
    idiom, tried explicit-associativity parens, didn't help), `game_981E0.c`
    (`func_150721A4` 15), `game_1944C0.c` (`func_1516968C` 15,
    `func_151696DC` 21, `func_15169070` 110), `game_14FF90.c`
    (`func_15125628` 18), `game_16DC80.c` (`func_1514143C` 12),
    `game_DBA60.c` (`func_150AED9C` 12), `game_EF410.c` (`func_150C251C`
    12), `game_16EE20.c` (`func_15142A5C` 6 - tried 3 rewrites, all failed
    to reproduce retail's plain `blez` vs our `bgtz`/`blezl` forms; comment
    on the function documents what was tried), `game_77AD0.c`
    (`func_1504BA38` 12, `func_1504CA60` 10, `func_1504C8BC` 50,
    `func_1504ADD0` 57, `func_1504A620` 60, `func_1505210C` 81,
    `func_1504AF10` 118, `func_1504BE2C` 191, `func_1504B0FC` 661 - the
    591-instruction water-physics function, unsurprisingly the hardest).
    Several of the smaller ones (`func_15060BA4`, `func_15142A5C`) are pure
    IDO register-allocation quirks where the logic is already provably
    correct but a handful of temp-register choices differ - these can eat
    a lot of time for uncertain payoff; the bigger ones likely have genuine
    remaining logic gaps worth investigating first.
  - **Verification method** (not committed - recreate from this
    description if resuming): for a given `fname funcname` pair, run
    `mips-linux-gnu-objdump -d build/conker.us.elf`, find the function's
    disassembly by symbol name, and compare word-for-word against bytes
    read directly from the pristine `conker.us.bin` at offset
    `int(funcname.split("_")[1], 16) - <segment vram> + <segment rom start>`
    (`game`: vram `0x15000000`, rom `0x2D4B0`; `debugger`: vram
    `0x16000000`, rom `0x255880` - both from `conker.us.yaml`). Decode each
    differing word's top 6 bits to classify jump/call-class opcodes (2, 3)
    separately from real differences.
