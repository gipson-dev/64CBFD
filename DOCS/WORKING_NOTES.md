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

**Update (2026-07-14, second session):** all baseroms and generated
artifacts (`asm/`, `build/`, `assets/`, `conker/conker.us.bin`) vanished
from the workspace between sessions during a `rom backup/` reorganization.
**Resolved for all four versions**: hash-verified baseroms re-installed at
repo root (`baserom.us.z64` recovered by the user into `rom backup/`;
`baserom.ects.z64` found in `rom backup/initial ROMs/` - see Session log).
Generated artifacts need a fresh `make extract` before resuming matching
work. Details in the Session log.

**Status (first session):** build works end-to-end (extract → compile → link → replace →
reassemble ROM). Ran a real matching pass on the 44 ECTS-ported functions
using both the linked ELF and a custom ground-truth-vs-compiled-bytes
comparison script (asm-differ's whole-binary `-m` mode is unreliable right
now - see gotcha below). 6 more now byte-match exactly (2 new real fixes, 4
were already matching but an earlier verification method gave false
negatives), and 6 more are confirmed logically complete (their only
remaining diff is a call to a still-unmatched function elsewhere - nothing
left to fix in those functions themselves). 32 genuinely still need work.
**Working on:** Function-matching passes on the remaining **25** (was 32 -
third session resolved 7, see its Session log entry, which also has a
list of reusable IDO/cfe codegen idioms worth reading before attempting
any rewrite). Persistent non-matchers are documented with comments in
the source (`func_1514143C`, `func_1507A3E8`, `func_150721A4`,
`func_1504BA38`, `func_151696DC`, `func_1516968C` - the last three are
within 1-2 words, all pure register-allocation residue). Earlier finding
still relevant: `func_15079A58` needed `D_800D2110`'s declared type
corrected from `s16[]` to `s16*` (ECTS agreed).
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

### 2026-07-14 (third session - matching pass resumed, 6 more resolved)

- Re-established the verification tooling from the second-session notes
  (scripts in scratchpad again, not committed: `verify_funcs.py` compares
  linked-ELF disassembly per symbol vs pristine-bin ground truth;
  `dump_func.py` prints ours-vs-truth side by side). Fresh baseline exactly
  reproduced the previous session's numbers (32 real-diff functions).
- **5 more functions byte-exact:** `func_16001B00` (debugger_257350.c),
  `func_15060BA4`, `func_1506196C` (game_83300.c), `func_150AED9C`
  (game_DBA60.c), `func_15142A5C` (game_16EE20.c - previously resisted 3
  rewrites). **1 more logically complete:** `func_1504CA60` (game_77AD0.c),
  now blocked only on callees `func_150ADA20`/`func_15058EA4`.
  **26 real-diff functions remain.**
- **IDO/cfe idioms learned (apply these before brute-forcing rewrites):**
  1. In leaf functions, *named locals* get `v0`/`v1` (in order of first
     assignment); *expression temps* get `t6`,`t7`,... A local still live
     at `return` gets `v1` (v0 stays free for return staging). So: truth
     using `v0`/`v1` for a value = introduce a named local; truth using
     `t6+` = fold the local into the expression. (Fixed `func_16001B00`,
     `func_15142A5C`, `func_150AED9C`, `func_1506196C` this way.)
  2. `u8` field updates: write through the field (`s->f += x`) - IDO
     stores the raw sum (`sb`) and re-derives the masked value via `andi`
     for later comparisons. A `u8 temp` local masks first and reuses one
     register for both (wrong). (Fixed `func_15060BA4`.)
  3. `return x > 0;` compiles to the `slt` idiom; `if (x > 0) return 1;
     return 0;` compiles to the branchy `blez` form. Branch polarity picks
     which return block is placed last: put the return the branch *jumps
     to* in the tail position (`if (c) return A; return B;` puts B's block
     last).
  4. cfe evaluates a binary op's *right* operand first (seen on `*` and on
     the innermost `|` of a chain). If truth's first-allocated temp
     belongs to the source's left operand, swap the operands (watch addu
     operand order for `a[i+k]`-style addressing: `(a + i)[k]` vs
     `a[i + k]` flips it). (Fixed `func_1506196C`.)
  5. mips_to_c artifacts: `spXX` f32 locals that are only ever *assigned*
     are caller-save spill slots - delete them. `temp_fN` names are cfe CSE
     temps - inline the expression instead of declaring a local; a declared
     f32 local costs a stack slot (frame size) even when never spilled.
     (Fixed `func_1504CA60`'s 0x40-vs-0x30 frame this way.)
  6. IDO aggressively folds `base+const` pointer locals into direct field
     offsets: block-scope locals, `(u8*)`/`(s32)` casts, and struct-member
     views all fold back to `lw off(a0)`. Could NOT reproduce retail's
     materialized `addiu v0,a0,0x110` in `func_1514143C` - documented in a
     comment on the function; revisit with fresh ideas (maybe the real
     sub-struct type at 0x110 matters, or retail passed `&arg0->unk110`
     somewhere nearby so the address had other uses).
- `func_1507A3E8` (byte-packing) also left documented-non-matching: retail
  evaluates the four `|` terms strictly left-to-right with `or(A,B)`
  operand order and per-load `lui`/`lbu` pairs adjacent; every attempted
  form (term reorder, `|=` chain, volatile) moves one property and breaks
  another. Both functions' comments carry the full details.
- Verification-cycle recipe for this machine (WSL): recreate `/tmp/rv.sh`
  from the scratchpad each time (WSL /tmp does not survive distro
  auto-shutdown between invocations), then
  `bash /tmp/rv.sh [func names...]` = incremental `make -C conker -j
  NON_MATCHING=1` + verify. Full cycle ~60-90s through /mnt/c. The script
  now fails loudly on compile errors (an earlier version piped make through
  grep/tail, which silently swallowed a build failure and verified a stale
  ELF - three "identical results" from three different sources was the
  telltale).
- **The verification method is now committed tooling:** `make -C conker
  match-progress NON_MATCHING=1` (add `LIST=1` for per-function output)
  runs `tools/match_progress.py` over *every* C-converted function from
  `progress.csv` and classifies each as byte-exact / blocked-on-callees /
  still-differing. First whole-project numbers: 379/1553 byte-exact
  (24.40%) - init 201/232 (86.64%), game 167/1151 (14.51%), debugger
  11/170 (6.47%). Snapshot tables published in the root README,
  DOCS/README.md, and DOCS/PROJECT.md. The debugger section's low
  byte-exact rate despite 93% conversion is the most surprising number -
  those 159 differing functions were converted long ago and never
  byte-verified; worth a dedicated look (may share one systematic cause,
  e.g. a compile-flag or header difference).
- **Continuation (same session): 1 more byte-exact, 2 real type-level bugs
  fixed, several near-matches.**
  - `func_150C251C` (game_EF410.c) byte-exact - it is an exact twin of
    `func_150AED9C`; the same rewrite applied verbatim. **7 resolved
    total this session; 25 real-diff functions remain.**
  - Type fixes with cross-function payoff (both in previously-unmatched
    code only - verified zero collateral in matched functions by diffing
    whole-object disassembly before/after):
    `func_1516968C`'s arg2 is really `u8` (its prologue
    `sw a2/andi/move` now matches exactly) and `struct102.unkC` is really
    `u8` at 0xC (was s16; retail uses `lbu`) - together 15→2 diffs on that
    function; `D_800DD198` is really `void*[6]` (was `u8[]`; retail
    indexes it `i*4`) - a genuine logic bug in the ECTS port, and fixing
    it plus the u8 arg dropped `func_15169070` from 110→71 diffs and got
    `func_151696DC` to within 1 word.
  - Documented-non-matching (comments on the functions carry details):
    `func_150721A4` (cfe stages call-arg shift+mask through the arg regs
    with fixup moves; retail uses temps then masks straight into arg regs
    - every source form tried compiles byte-identically),
    `func_151696DC` and `func_1504BA38` (same class: IDO evicts a live
    value to a different register than retail chose),
    `func_1516968C` (only the two lbu operands of `==` are ordered
    a1-base-first in retail; cfe canonicalizes both source orders to
    a0-base-first).
  - New idiom observed (add to the list above): **when a call target's
    param is `u8`/`u16`, passing an unmasked expression lets the
    conversion generate the `andi` directly into the arg register;
    an explicit `& 0xFF` in the caller often compiles the same - but the
    *callee-side* `u8` parameter type is what produces the
    `sw aN/andi/move` prologue** (that prologue in ground truth = the
    parameter is narrow-typed, fix the signature before anything else).

### 2026-07-14 (second session - ROM inventory after `rom backup/` reshuffle)

- The workspace lost all root-level baseroms AND all generated artifacts
  (`asm/`, `build/`, `assets/`, `conker/conker.us.bin` etc.) since the
  previous session. `rom backup/` was reorganized with a new set of files
  (the old `[DC].rom` files and the EU `.n64` are gone; everything is now
  native big-endian `.z64` - verified magic `80 37 12 40` on all).
- **Full hash inventory of `rom backup/`** (PowerShell gotcha: `[...]` in
  the filenames is a wildcard to `Get-FileHash -Path`; must use
  `-LiteralPath` or the hashes come out silently wrong/stale):
  - `Conker's Bad Fur Day (Europe).z64` = `ee7bc665...` **= expected EU
    baserom** (already byteswapped, unlike last session's v64 copy).
    Re-installed as `baserom.eu.z64`, hash re-verified.
  - `Conkers Bad Fur Day [ntsc][debug][DC].z64` = `3b99222e...`
    **= expected debug baserom**. Re-installed as `baserom.debug.z64`,
    hash re-verified.
  - `Conker's Bad Fur Day (Uncensored).z64` = `4df27756...` - same US-based
    romhack analyzed last session, unchanged.
  - `Conker's Bad Fur Day [ects][DC].z64` (sha1 `598d9d9f...`, header CRC
    `A08D0F77`) and `Conkers Bad Fur Day [ECTS Demo][EC].z64` (sha1
    `2cc98818...`, header CRC `094D7111`): both genuine ECTS demo builds
    (internal name `CBFD ECTS`) but **two different dumps, neither matching
    `conker.ects.sha1` (`06597dc9...`)**. The old `[ects][DC].rom` that DID
    match is gone.
  - `Conkers Bad Fur Day [Debug][EC].z64`: garbage internal header
    (non-ASCII name/ID) - scrambled or bad dump, matches nothing, don't use.
  - `Conker's Bad Fur Day [Español].z64` (sha1 `52e4355f...`): Spanish
    translation hack, US-based (keeps retail header CRCs like the
    Uncensored hack does).
  - Plus `Uncensored Patches/` (.bps + .xdelta, ~2 MB each; the .bps footer
    says source crc32 `CE8CC172` → target crc32 `E1B9019B`, and the target
    crc32 matches the Uncensored .z64 here exactly - so the patch source,
    crc32 `CE8CC172`, is the missing retail US ROM) and the Bradygames
    strategy guide PDF.
- **Tried and failed: reconstructing retail US from the two hacks.**
  Idea: Uncensored = retail everywhere except assets06/assets16 (proven
  last session), so splice those two segments in from Español and check
  sha1. Result: no match. Diagnostics show why: Español vs Uncensored
  differ by 427 bytes outside the two segments (Spanish text elsewhere,
  fine), 2,020,358 bytes in assets16 - **exactly** the Uncensored-vs-retail
  count from last session, so Español's assets16 is almost certainly retail
  audio - but 396,111 bytes in assets06, ~10x the 39,919 the censorship
  accounts for: the translation rewrites the dialogue/subtitle data living
  in assets06, so retail assets06 is not recoverable from these two ROMs.
  (Side finding worth keeping: this independently confirms assets06 holds
  per-line text/metadata - it's the segment a subtitle translation has to
  rewrite.) The BPS patch can't recover it either - BPS stores only new
  bytes for changed regions, not the old ones.
- **`rom backup/initial ROMs/` resolved the remaining gaps.** The user
  pointed out this subfolder holding the *original* pre-reshuffle files:
  `Conker's Bad Fur Day [ects][DC].rom` (sha1 `06597dc9...` **= expected
  ECTS baserom**, installed as `baserom.ects.z64`), the debug `[DC].rom`
  (same hash as already installed), and the two source archives the
  loose ROMs came from - `Conker's Bad Fur Day (Aug 26, 2000
  prototype).zip` (contains the ects `[DC].rom` + an alternate
  `[ECTS Demo][EC].v64` dump in v64 order) and `(Oct 25, 2000
  prototype).zip` (debug `[DC].rom` + `[Debug][EC].v64`). This explains
  the odd `[EC]` files in the main folder: they're v64-order alternate
  dumps of the same two prototypes, and the loose
  `[Debug][EC].z64`'s garbage header is just a botched v64→z64
  conversion of one - ignore them; the `[DC]` dumps are canonical.
- **Build environment on this machine (was undocumented - expensive to
  re-derive):** builds run inside the local WSL2 distro **`PSBBN`**
  (Debian 13), operating directly on the repo via
  `/mnt/c/Users/grego/OneDrive/Desktop/.vscode/64CBFD`. Set up this
  session: python venv at **`~/conker-venv`** (inside WSL) holding both
  `requirements.txt` and `tools/n64splat/requirements.txt` deps (the
  splat submodule needs its own requirements file too - `intervaltree`
  etc. - or you get a bare `ModuleNotFoundError`), plus apt packages
  `binutils-mips-linux-gnu build-essential libglib2.0-0`. Invoke as:
  `PATH="$HOME/conker-venv/bin:$PATH" make ...` from the repo dir in WSL.
  The IDO 5.3 recomp binaries in `ido/` run fine from /mnt/c.
- **Checkout corruption regressed and was re-fixed.** `core.symlinks` was
  back to `false` and `core.autocrlf` to `true` (cause unknown - possibly
  OneDrive), which turned `tools/splat_ext/rareunzip.py` (a git symlink)
  into a 15-byte text file. That is what splat's opaque
  `could not load segment type 'rzip'` error actually means - the
  extension loader swallows the underlying ImportError
  (`segment.py:161`, bare `except Exception: return None`). Re-applied
  the documented fix (config + full re-checkout, WORKING_NOTES edits
  stashed/restored around it); all 3 repo symlinks are real again and
  line endings are LF. If `rzip` fails to load again, check this first.
- **Full build chain re-verified end-to-end** after extraction: `make -C
  conker -j` compiles and links `build/conker.us.elf` (its verify step
  says `build/conker.us.bin: FAILED`, which is the expected non-matching
  result at ~20% - use `NON_MATCHING=1` to skip), then `make -C conker
  replace NON_MATCHING=1` and root `make NON_MATCHING=1` produce
  `build/conker.us.z64`. Same state as last session's "last known good".
- **Net state:** all four versions are buildable again -
  `baserom.us.z64`, `baserom.eu.z64`, `baserom.debug.z64`,
  `baserom.ects.z64` at repo root, every one verified against its
  `conker.<ver>.sha1`. Everything generated must be re-extracted
  (`make extract` etc.) - see the first-session notes below for the
  splat/config fixes that are already committed and should make that
  clean. (Reminder from those notes: `conker.debug.yaml` /
  `conker.ects.yaml` still need the same config modernization us/eu got
  before *those* versions can extract.)

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
- Inspected two new ROMs dropped into `rom backup/`:
  - **`Conker's Bad Fur Day (Europe).n64` is the missing EU baserom.**
    Despite the `.n64` extension it's v64 (16-bit byte-swapped) order;
    byteswapped to big-endian z64 its SHA1 is
    `ee7bc6656fd1e1d9ffb3d19add759f28b88df710`, exactly matching the
    repo's expected root-level `conker.eu.sha1`. Installed the converted
    copy as `baserom.eu.z64` (repo root, untracked like the other
    baseroms); `make check VERSION=eu` passes. All four target versions
    (us / eu / debug / ects) now have hash-verified baseroms available
    locally (debug and ects match the two `[DC].rom` files already in
    `rom backup/`).
  - **EU extraction pipeline now works end to end:** `conker.eu.yaml` and
    `game.eu.rzip.yaml` were still in pre-modernization splat format
    (missing `platform`/`basename`, `sha1` nested under `options`) - the
    same class of splat-version fix already applied to the `us` configs.
    After fixing both, `make extract VERSION=eu` runs clean and the
    decompressed code image `conker/conker.eu.bin` **verifies OK** against
    `conker/conker.eu.sha1`. Note `conker.debug.yaml` / `conker.ects.yaml`
    at the repo root still have the old format and will need the identical
    two-line fix before extracting those versions. What EU enables: a
    third matched-code reference (alongside `debug_proto`/`ects_proto`)
    for cross-version function matching - `symbol_addrs.eu.txt`,
    `undefined_funcs.eu.txt` and the `src_eu` build path already exist in
    `conker/`, so the scaffolding was always intended for this.
  - **`Conker's Bad Fur Day (Uncensored).z64` is a US romhack, not a
    baserom** (SHA1 `4df27756ef604e82c6874aade21075b5bc8d405a`, matches no
    expected hash - don't use it as one). It is byte-identical to
    `baserom.us.z64` except for ~2.06 MB confined to exactly two asset
    segments: `assets06` (39,919 bytes differ, 7.4% of the segment) and
    `assets16` - the segment `conker.us.yaml` already annotates as
    "MP3s" - (2,020,358 bytes, 8.6%). Its header CRCs are unchanged from
    retail yet still boot-valid because the CIC checksum only covers ROM
    `0x1000`-`0x101000`, which the hack never touches.
    **What it's useful for:** it's a ready-made differential probe for the
    asset-format work - decompressing `assets06`/`assets16` from both ROMs
    and diffing file-by-file (via the `assets_offsets_table` at
    `0xAB1950`) pinpoints exactly which files are censored voice lines,
    confirming assets16 = dialogue audio bank and revealing what
    per-line metadata lives in assets06. Not usable for code work (no
    code differs).
- Pulled both (same session):
  - **EU disassembly extracted.** Modernized `conker/conker.eu.yaml` the
    same way `conker/conker.us.yaml` was (top-level `sha1`,
    `platform: n64`, `generate_asm_macros_files: false`,
    `asm_nonmatching_label_macro: ""`, `asm_function_alt_macro: glabel`;
    dropped the removed `find_file_boundaries`/`create_detected_syms`/
    `cpp_args`/`undefined_syms_path` options), **plus version-separated
    output paths** (`asm_path: asm_eu`, `asset_path: assets_eu`,
    `src_path: src_eu`) so extracting EU never clobbers the us `asm/` /
    `assets/` / `src/` trees in this same checkout - note the us and eu
    configs would otherwise write to the same default paths. Running
    `python3 ../tools/n64splat/split.py conker.eu.yaml` from `conker/`
    produced `conker/asm_eu/` with 651 `.s` files and 5,759 disassembled
    functions across init/game/debugger. `include/macro.inc` confirmed
    untouched. These dirs are generated artifacts (like `asm/`) - regen
    with the command above, don't commit.
  - **Censored-file list pinned down.** File-level diff of the two rzip
    containers (walking each segment's leading `(offset, type|length)`
    pair table per `tools/splat_ext/rzip.py`) shows the offset tables are
    byte-identical - the hack replaces files strictly in place. Changed:
    **15 of 50 files in `assets06`** (indices 1, 4, 6, 7, 8, 12, 14, 15,
    16, 22, 30, 33, 40, 47, 48) and **23 of 453 files in `assets16`**
    (indices 5, 19, 20, 27, 34, 35, 36, 47, 83, 119, 126, 143, 149, 150,
    175, 287, 289, 325, 341, 384, 387, 426, 439). The assets16 files
    begin with an `0xFFF3` MPEG audio frame sync in both ROMs - they are
    raw MPEG-2 Layer III (MP3) streams stored uncompressed, replaced
    wholesale with uncensored takes. The changed assets06 files keep
    identical headers and diverge later - so assets06 holds some
    per-line structured data (subtitle text? timing/metadata tables?)
    worth reversing next; the 15 changed ones are the natural samples to
    stare at since we know exactly which dialogue they belong to.
