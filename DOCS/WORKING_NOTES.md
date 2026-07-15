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

**Update (2026-07-15, ninth session continued):** fixed a real bug in
`tools/progress.py` (project-owned, not the n64splat submodule) that was
inflating every raw-function count in the "Functions" progress table.
Its map-file parser tried to skip jump-table-target local labels
(`.L15029BA0`-style) via `if new_function.startswith("L8")` - dead code,
it never matched anything (missing the leading `.`, and written for
unmodified real-address labels this project's remapped `0x10`/`0x15`/
`0x16xxxxxx` addressing never produces anyway). Fixed to
`.startswith(".L")` and regenerated: **`game` 6915→5313 total functions,
`init` 547→538, `debugger` unaffected (172/182, was already clean)** -
converted counts unchanged (1152/232/172), only the denominators got more
honest. This supersedes the manual grep-based correction from earlier the
same day (still useful as a spot-check method, no longer needed as a
workaround). Tables updated project-wide. Two `dlabel`-tagged artifacts
in `game` (data auto-named like functions) remain uncorrected - out of
scope for this fix (`.L`-prefix filtering doesn't touch them), tiny
residual (2 of several thousand), not worth a special-case hack.

**Update (2026-07-15, eighth session):** "knock out fast functions."
**Critical finding, read this before trusting any single-function
diff/word-count from `match_progress.py` or the `dump_func.py`-style
verification pattern:** both tools compute a function's retail ROM
address from `progress.csv`'s `offset` column - but that column is
regenerated from the **current build's `.map` file** every time `make
progress` runs, not from a fixed retail source. For any function whose
build address has drifted from what its own name implies (extremely
common in `game`, only 17% byte-exact, so most of it has some size
mismatch upstream), this silently fetches "truth" bytes from the *wrong*
ROM location and produces nonsense diffs - not a small-diff false
positive like the padding bug two sessions ago, but complete garbage
(confirmed on `func_150ADA20`: reported "truth" was unrelated code from
768 bytes away). The **aggregate percentages in the byte-matching
snapshot are still fine** (a real mismatch just shows as "diff" either
way), but do not trust an *individual* function's reported diff content
for anything in `game` without cross-checking against its `.s` file's own
address comments first (fixed at extraction time, never drifts) - see the
fixed `dump_func.py` in the Session log. Not fixed in `match_progress.py`
itself this session (would need every function's true retail address from
a source that doesn't reflect current build state - `symbol_addrs.us.txt`
for named symbols, or parsing the name for `func_XXXXXXXX` ones - deeper
fix, not attempted).

Net conversions this session: 2 very-high-value functions,
`func_150ADA20`/`func_150ADACC` (the game's PRNG - `func_150ADA20` alone
is called from 100+ sites across a dozen files) - plus a real bug fix
(its existing prototype declared `u8` return, silently truncating a
32-bit PRNG value at every call site for who knows how long). Both are
logically verified correct (algorithm matches retail instruction-by-
instruction) but not yet byte-exact - register allocation differs, same
class of remaining work as `func_1600160C` last session. Getting here
required adding real, reusable build-system capability: this file needs
native MIPS III 64-bit instructions (`dsll32`/`ld`/`sd`/...) that the
project's global `-mips2` target can't emit (falls back to
`__ll_lshift`/`__ull_rshift` software-emulation calls instead), so added
a per-file `-mips3` override plus `--no-warn-mismatch` on the linker (ISA
info in ELF `e_flags` alone, not a real 32-vs-64-bit ABI conflict despns
what the error text implies) - see Session log, both are reusable for any
other 64-bit function found later. Also tried and **reverted** converting
a whole raw `.s` file (`asm/50D80.s` → `c` type) to reach one trivial
function inside it - broke the link with the exact jump-table
`.L`-label issue already documented from the "Link-time blocker" fix
(different jlabel set, same root cause) - don't retry this without
first checking whether the target file's own `.L...` labels are
referenced from rodata elsewhere. `init`'s smallest remaining raw
functions are mostly genuine hand-written libultra SDK code (confirmed
via `/* Handwritten function */` markers and known real-SDK filenames
like `setsr`/`getsr`) - low yield there, redirect future "fast function"
hunts to `game`'s 4161-function backlog instead, specifically ones
already living in split `asm/nonmatchings/` files (no yaml-splitting
risk) - see Session log for the exact search method.

**Update (2026-07-15, seventh session):** converting raw-`GLOBAL_ASM`
debugger functions to C (user asked to work on functions still needing
conversion). Set up `mips_to_c` in this environment (pycparser version
mismatch - fixed with `pip install --break-system-packages pycparser==2.21`
- and `conker/tools/ctx.py` for the type-context file, both undocumented
before now). Converted 2 of debugger's 12 remaining raw functions
(`func_1600160C`, `func_16001678`); found one (`func_16003650`) is
genuinely hand-written CP0/TLB code with no C equivalent, permanently
skip it. **Unexpected big win:** converting those 2 functions fixed a
pre-existing symbol-address-placement bug affecting several `D_1600xxxx`
globals in `debugger/debugger.c`, which was silently blocking byte-matches
for *other, unrelated, already-converted* functions in the same file -
debugger's byte-exact rate jumped 8.82%→74.42% (15→128 of 172) from that
one fix, not from the 2 conversions themselves being byte-perfect (they
aren't, see Session log). 10 raw functions remain in debugger (1 of which,
`func_16003650`, will never convert); `init` has **306** real raw
functions remaining (315 minus 9 `jlabel` artifacts) and `game` has
**4161** (5764 minus 1603 `jlabel`/`dlabel` artifacts - filtered and
confirmed same session, see Session log and PROJECT.md's "Functions"
caveats for the reusable grep method). Tables updated in
PROJECT.md/README.md/DOCS/README.md. Full detail,
including two still-open blockers (`func_16001B34`'s float-argument gap
affects `func_16000F8C`/`func_1600078C`; register-allocation/operand-order
tuning needed on the 2 converted functions), in the Session log.

**Update (2026-07-15, sixth session):** picked up init-segment matching.
Found `conker/conker.ld` (gitignored, splat-generated) had been silently
clobbered by the EU extraction two sessions ago - it isn't
version-namespaced like `asm_path`/`asset_path`/`src_path` were, so
running `make extract VERSION=eu` after `us` overwrote the shared file
with `asm_eu/*.s.o` object paths, breaking the `us` link
(`cannot find build/asm_eu/header.s.o`). Fixed by re-running
`make -C conker extract VERSION=us` to regenerate it. **Bigger find:**
`tools/match_progress.py`'s classifier was over-strict about function
length, misclassifying 56 already-byte-exact functions project-wide as
"diff" just because retail's declared symbol length includes a few
trailing inter-function alignment nops. Fixed (see PROJECT.md's
"2026-07-15 correction" note) - init jumped 86.64%→96.12% with zero
source changes. Of init's remaining 9 non-exact: 4 are blocked on
not-yet-matched `game`-segment callees (self-resolving), 4 are NOT bugs
in those functions - a rodata float-constant-pool address drift
originating elsewhere (not root-caused this session, see Session log),
and 1 (`__n_vsVol`) is a real but narrow VR4300 multiply-hazard
nop-scheduling difference (not attempted - low payoff for one function).
Updated the progress tables in PROJECT.md/README.md/DOCS/README.md.
Full detail in the Session log below.

**Update (2026-07-14, fourth session):** found `baserom.debug.z64` and
`baserom.ects.z64` missing from the repo root again (only `us`/`eu` were
present; `us`/`eu` extraction artifacts were intact) alongside a set of
untracked zero-byte `conker/core.*` files - looks like an unclean
crash/restart wiped those two root baseroms without touching anything
else. `rom backup/` currently holds only 5 files (no `initial ROMs/`
subfolder, no ECTS Demo/Español/Uncensored-Patches items the second
session's inventory described - that inventory is stale, don't trust its
file list, only its hashes). Re-hashed `rom backup/Conkers Bad Fur Day
[ntsc][debug][DC].rom` and `rom backup/Conker's Bad Fur Day [ects][DC].rom`
against `conker.debug.sha1`/`conker.ects.sha1` (both matched exactly) and
copied them in as `baserom.debug.z64`/`baserom.ects.z64`. All four
baseroms are hash-verified at the repo root again. `debug`/`ects` are
still unextracted (`conker/conker.debug.bin`/`conker/conker.ects.bin`
don't exist) - expected, since `conker.debug.yaml`/`conker.ects.yaml`
still need the same splat-modernization fix `us`/`eu` already got (see
below) before `make extract VERSION=debug|ects` will work. The
zero-byte `core.*` files were left alone (not created this session,
cause unknown - possibly worth asking the user about if they recur).

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

### 2026-07-15 (ninth session, continued - USF sound rip found in rom backup/)

- User pointed at `rom backup/Conker's Bad Fur Day sound files/` - a
  community USF (Ultra64 Sound Format) rip: `NUS-NFUE-USA.usflib` (7.4 MB
  shared library, `NUS-NFUE-USA` = CBFD's real N64 cartridge product code)
  + 173 `.miniusf` pointer files, tagged `artist=Robin Beanland`,
  `usfby=Josh W. / hcs`, `copyright=Rare`. Confirmed genuine PSF-family
  files (`PSF!` magic = `"PSF"` + version byte `0x21`, the registered USF
  tag).
  - Filenames are `sparseNN[a-g].miniusf`, `NN` **hex**. Extracted 148
    unique base indices, exactly contiguous `0x01`-`0x94` with no gaps and
    no `0x00` - independently corroborates the `assets17/0003` "149
    entries" figure from the wiki (§6 in ASSET_FORMATS.md, added earlier
    this session) if index 0 is a silence/no-music slot. Folded into
    ASSET_FORMATS.md §6 as a cross-reference.
  - These are real playable audio (any PSF-family player, e.g. foobar2000
    + `in_usf`) - noted as a listening reference for identifying which
    sequence index plays where in-game, and flagged that
    `NUS-NFUE-USA.usflib` may embed the same sample/sequence memory image
    as `assets17`'s `0002`/`0003` sub-files - worth diffing against if
    anyone picks the container format work back up.
  - Not attempted: actually playing/diffing the USF data against the
    ROM's `assets17` content, or writing an extractor. This was a
    cross-reference/documentation pass only.

### 2026-07-15 (ninth session - reference sweep: N64ops03.txt, project wiki)

- User pointed at `rom backup/N64ops03.txt` (a generic 1998 MIPS/N64 opcode
  reference - opcode/COP0/COP1 encoding tables, ROM header layout) and the
  `64CBFD.wiki` submodule, asking for useful info. `N64ops03.txt` is
  low-novelty (project tooling already handles instruction decoding) but a
  handy human-readable cross-check for the ROM header layout.
- The wiki had real, mostly non-redundant content. Folded two pieces into
  [ASSET_FORMATS.md](ASSET_FORMATS.md) at the user's request:
  - **New §2a**: a reported compressed-code-loading mechanism (4096-byte
    on-demand chunks via a bad-virtual-address/TLB-miss trick, chunk table
    at ROM `0x42454` XOR-encrypted with key `0x8039CCCA`, based at
    `0x42450`) - distinct from the asset `rzip` containers in §2. Marked
    Tentative - sourced from the wiki's `Useful-Info` page (originally a
    Discord chat with `gamemasterplc`), not reproduced against this repo's
    own extraction. `0x42450` falls in the `init`/boot ROM range - worth
    checking against `conker.us.yaml`'s actual `init`/`init_data` split
    before trusting the exact offsets.
  - **§6 (`assets17`) extended**: confirmed `0x4231`/"B1" is the real
    `AL_BANK_VERSION` libaudio.h constant (corroborates, doesn't change,
    the header already decoded there); added that `assets17` sub-file
    `0003` uses a *different* magic (`"S1"` = `AL_SEQBANK_VERSION`) and
    format (a 149-entry offset+length table, likely `ALSeqFile` sequence
    data) - a separate container schema from the B1 sample bank, and
    `0002` (~21MB) is the raw sample bank with a known third-party
    extraction path (N64 Midi Tool → DLS → SF2). Also marked Tentative -
    same wiki source, unverified here, and the wiki's own file-index
    labeling for the B1 header is internally inconsistent (worth
    resolving before relying on it).
  - Updated §9's open-questions bullets to point at both additions.
  - Not folded in (lower confidence / already covered): `Patterns.md`'s
    IDO/cfe idiom list (already has a project-native equivalent building up
    in this file's own Session log entries).
- **Not addressed**: the wiki submodule has substantial uncommitted local
  changes (`git -C 64CBFD.wiki status` shows nearly every page modified,
  plus `Contributing.md`/`Home.md`/`Using-Ghidra.md` showing as deleted
  relative to its last commit) - flagged to the user, not investigated or
  touched further this session since it wasn't asked for.
- **Follow-up, same session: did the OS function name/address table diff.**
  Parsed `Useful-Info.md`'s 115-entry `0x8000xxxx`-addressed table and
  cross-referenced against `symbol_addrs.us.txt`. Address mapping: this
  project's `init` segment uses an artificial vram (`0x10001000`+, splat
  bookkeeping only) offset by exactly `-0x70000000` from the real N64
  address the wiki's table uses (confirmed via `__osSetSR`'s own `.s`
  file: real `0x80022a30` ↔ project `0x10022a30`) - subtract `0x70000000`
  from any wiki address to look it up here. Result: **101/115 already
  correctly named, zero mismatches** (good sign the existing naming is
  trustworthy), **8 unique addresses genuinely missing** (14 raw entries
  counting aliases - several wiki addresses list multiple real names for
  one address, e.g. libultra functions that are byte-identical at that
  specific address). Of those 8: three (`0x10024400`, `0x10026700`,
  `0x10026750`) were confirmed-covered still-raw `GLOBAL_ASM` functions
  using generic `func_XXXXXXXX` names - added real names to
  `symbol_addrs.us.txt` (`osPiGetDeviceType` for the first, aliases noted
  in `//` comments since splat's parser supports them; `__osSiRawReadIo`/
  `__osSpRawWriteIo` for the other two, real SDK behavior - SI and SP
  raw I/O share one implementation, not a coincidence). Re-ran
  `make extract VERSION=us` to apply the new names, then rebuilt - one
  stale cached `build/src/libultra/os/initialize.c.o` briefly showed
  `undefined reference to 'func_10026700'` even though no source
  referenced that name (a leftover object file from before the rename,
  not a real problem - `rm`ing it and rebuilding fixed it immediately).
  Confirmed no regressions and a small bonus: `init` byte-exact went
  223→224 and blocked-on-callees 4→3, both counts otherwise stable. The
  other 5 addresses (`osViModePalLan1`/`osViModeMpalLan1`/
  `osViModeNtscLan1`/`__osRcpImTable`/`__libm_qnan_f`, ROM range
  `~0x2be30`-`~0x2c920`) don't correspond to anything in the current
  `conker.us.yaml`/`symbol_addrs.us.txt` at all despite falling within the
  already-covered `init` code range - likely un-split data tables
  currently absorbed into a surrounding rodata/bin blob rather than a
  segment-boundary gap. Not added (would need understanding the current
  subsegment structure around them first, same caution as the earlier
  jump-table lesson this session) - left as a known lead.

### 2026-07-15 (eighth session - "knock out fast functions")

- **init's tiny candidates mostly aren't real conversion targets.**
  Checked the smallest remaining raw `init` functions
  (`__osSetSR`/`__osGetSR`/`func_10007DA0`/etc.) - `__osSetSR`/`__osGetSR`
  are explicitly tagged `/* Handwritten function */` in their `.s` files
  (raw `mtc0`/`mfc0` COP0 register moves, no C equivalent - same class as
  last session's `func_16003650`). `__osSetFpcCsr`/`__osSpSetStatus` etc.
  aren't tagged but match known real-SDK filenames
  (`asm/libultra/os/setsr.s` etc., configured `asm` type in
  `conker.us.yaml`, not `c`) - these correspond to files Nintendo/SGI
  actually shipped as hand-written `.s` in the real N64 SDK, a
  well-established fact in the wider decomp community. Didn't convert any
  of these - redirected effort to `game` instead, which is Rare's own
  compiled code and has a real 4161-function backlog.
- **Attempted and reverted: splitting a whole raw `.s` file to reach one
  trivial function inside it.** `asm/50D80.s` (segment `[0x50d80, asm]`
  in `conker.us.yaml`, no `name:`) contains `func_150238D0`, an empty
  function (`jr ra; nop`) - found via a regex sweep of the whole `asm/`
  tree for the literal 2-instruction empty-function pattern (7 hits
  total repo-wide, listed in `asm/142560.s`, `asm/18A8F0.s`,
  `asm/20AE20.s`, `asm/50D80.s`, `asm/6B320.s`, `asm/71820.s`,
  `asm/B3020.s` - none converted this session, see below for why). Since
  the containing file was never split at function granularity, reaching
  it meant changing `[0x50d80, asm]` → `[0x50d80, c, game_50D80]` and
  re-running `make extract VERSION=us` - splat auto-inlined the trivial
  function as real C directly (`void func_150238D0(void) {}`, no
  `GLOBAL_ASM` stub needed) and stubbed the other ~10 functions in the
  file normally. **Broke the link**: `undefined reference to
  '.L15029BA0'` / `.L150288E4_game_data` etc. from
  `build/asm/data/23B4E0.rodata.s.o` - this is the exact same
  `.L`-prefixed-jump-table-label problem as the first session's
  "Link-time blocker: RESOLVED" writeup (further up this file), just a
  *different* rodata block (`23B4E0`) referencing labels that used to
  live safely inside the monolithic `asm` block and lost their linkable
  identity once split. Reverted cleanly (yaml line back to `asm`, deleted
  the generated `src/game_50D80.c` and
  `asm/nonmatchings/game_50D80/`, re-ran `make extract VERSION=us`,
  confirmed clean rebuild). **Lesson for next time:** before converting
  any whole raw `.s` file to unlock a function inside it, grep the file
  for `jlabel` definitions first (`grep jlabel asm/<file>.s`) and check
  whether any rodata block elsewhere references them by name - if so,
  this will break the same way, and the real fix (converting that rodata
  block to `bin` type per the original writeup) has to happen in the same
  change.
- **Found the safe "fast function" territory: functions in already-`c`-
  type files.** Cross-referenced every raw (`language != c`) `glabel`
  function's name against `asm/nonmatchings/**/*.s` (a single `find`,
  not one call per row) to identify which raw functions live inside files
  that are *already* split at function granularity (no yaml/extraction
  risk, same safe workflow as last session's `debugger.c` work): **155 in
  init, 721 in game.** This is the list to work from for future
  low-risk conversions, sorted by size - smallest game ones start at 8
  words (`func_150A7770`, itself hand-written per its `.s` comment) and
  9 words (`func_150ADACC`, see below).
- **Converted `func_150ADA20` and `func_150ADACC` (`game_DAE50.c`) - the
  game's core PRNG.** `func_150ADA20()` is called from 100+ sites across
  a dozen `src/*.c` files (grep confirmed), always with zero arguments,
  so no call-site argument-count bug like earlier sessions' finds - but
  its *existing* prototype in `functions.h` was wrong regardless:
  `u8 func_150ADA20(void);` when the real return is a full 32-bit value
  (confirmed from the raw asm's `dsll32`/`dsra32` sign-extension
  sequence, and from callers like `% 25000U`/`% 0xFFFFU` that only make
  sense on an untruncated value) - fixed to `s32`. This bug has been
  silently truncating the PRNG's output to 0-255 at every one of those
  100+ call sites for an unknown number of past sessions.
  - `game_DAE50.c` already had detailed (commented-out, never enabled)
    draft analysis of both functions from an earlier session ("well this
    is a bastard" / "NON-MATCHING: hand-written function") - the bit-math
    reasoning was mostly right; used it as a base, worked out the exact
    op sequence directly from the raw `.s` instead of trusting the
    draft's own arithmetic (it had some confused shift-amount comments).
    Both are a straightforward 64-bit xorshift-style mix operating on the
    global 64-bit seed `D_800885B0`.
  - **Discovered mid-verification that this file needs `-mips3`, not the
    project's global `-mips2` (`MIPSBIT` in `conker/Makefile`).** First
    compile attempt produced 68 words instead of 18 for `func_150ADA20`
    - IDO was calling `__ll_lshift`/`__ull_rshift` (software 64-bit-shift
    emulation - these are literally two of the "trivial init functions"
    from two sessions ago) instead of emitting native
    `dsll32`/`dsrl`/`daddiu`/`ld`/`sd`, because MIPS II (the project-wide
    default) has no 64-bit integer instructions at all - the file's own
    top comment already said "// some mips3/64bit stuff going on here"
    from a prior session, unactioned until now. Fixed with a target-
    specific Makefile override (same established pattern already used
    for per-file `OPT_FLAGS`, just applied to `MIPSBIT` instead):
    `$(BUILD_DIR)/$(SRC_DIR)/game_DAE50.c.o: MIPSBIT := -mips3` (IDO
    warns `-mips3 should not be used for ucode 32-bit compiles` - harmless
    for us, we're not compiling RSP ucode). This alone fixed the
    instruction *selection* (dsll32 etc. now appear, matching truth's
    opcodes exactly) but broke the *link*: `mips-linux-gnu-ld: linking
    32-bit code with 64-bit code` / `failed to merge target specific
    data`. Root cause: `readelf -h` showed the object's `e_flags` ISA bit
    set to `mips3` (`0x20000001`) vs every other object's `mips2`
    (`0x10000001`) - both still `Class: ELF32` (not a real 32/64-bit ABI
    class conflict despite the error wording), just an ISA-level
    mismatch binutils refuses to link by default. Fixed by adding
    `--no-warn-mismatch` to the project's global `LDFLAGS` - confirmed
    this only relaxes the mismatch check, doesn't change any generated
    code. **Both the `MIPSBIT` override and `--no-warn-mismatch` are now
    permanent, reusable infrastructure** for any other function
    discovered later that needs real 64-bit ops.
  - **Verification tooling was giving false data for this function until
    fixed mid-session** - see "Current focus" above for the critical
    `progress.csv`-drift finding this surfaced. Rewrote `dump_func.py`
    (scratchpad) to resolve ground-truth address/length from the
    function's own `.s` file comments (fixed at extraction time) instead
    of `progress.csv`'s `offset` column, falling back to the old
    progress.csv method (now explicitly labeled untrusted in the output)
    only when no `.s` file can be found.
  - **Current state: both logically verified correct, not yet byte-
    exact.** After the `-mips3` fix, `func_150ADA20` is 19 words
    (truth 18) and `func_150ADACC` is 8 words (truth 6) - every
    *instruction type* matches truth exactly (same ops, same operands
    conceptually), remaining diffs are register-allocation/scheduling
    choices (e.g. ours loads the global via a separate `lui`+`addiu`+`ld`
    instead of retail's combined `lui`+`ld` with immediate offset). Tried
    one rewrite (reading the global directly 3x instead of caching in a
    local) - made `func_150ADA20` worse (20 words) - reverted. Same class
    of remaining work as `func_1600160C` two sessions ago; not resolved,
    flagged for a future targeted pass rather than guessed at further
    here. This does NOT block the 100+ callers from being useful/typed
    correctly - only the two functions' own byte-exactness is pending.
  - `func_1000EB00` (the `init`-section function blocked on
    `func_150ADA20` two sessions ago) is still `BLOCK`, not yet resolved
    - expected, since `match_progress.py`'s blocked-classification needs
    the *callee* to be byte-exact too, not just present as real C. Will
    self-resolve once `func_150ADA20` itself matches.
- Cleaned up `ctx.c`/`ctx.c.m2c` (mips_to_c cache artifacts) before
  finishing - not committed, regenerate on demand per last session's
  notes.

### 2026-07-15 (seventh session - raw-asm-to-C conversion pass, debugger)

- User asked to work on functions still needing conversion from raw
  assembly to C (as opposed to the previous session's *matching* pass on
  already-converted functions). Surveyed remaining raw counts via
  `progress.csv` (`language != "c"` rows) per section: **init 315,
  game 5764, debugger 12.** Game's raw count is inflated by data-label
  artifacts (`.L15032138_game_data` etc. - 1-2 "word" entries that are
  jump-table/data labels caught in the same CSV, not real functions);
  didn't filter these out this session, but don't trust the raw 5764
  figure as "functions to convert" without doing so first. Debugger's 12
  is small and bounded (all real functions, 27-420 words) - picked it as
  this session's target since finishing it is an achievable milestone.
- **Follow-up, same session: filtered the artifacts and got real counts.**
  Every `.s` file under `asm/` tags each label as `glabel` (real
  function), `jlabel` (internal jump-table target, not independently
  convertible), or `dlabel` (data). Cross-referenced every raw
  `progress.csv` row's name against `grep -rhoP '\bjlabel\s+\K\S+' asm/`
  and the `dlabel` equivalent (first attempt used a variable-length regex
  lookbehind - `grep: lookbehind assertion is not fixed length` - fixed by
  switching to `\K` instead of `(?<=...)`). **Real remaining raw function
  counts: game 4161 (not 5764 - 1601 `jlabel` + 2 `dlabel` artifacts,
  the `dlabel` ones being `D_150A9C40` and, confusingly,
  `func_150AA814` - a jump table stored as rodata that got a
  function-shaped auto-generated name), init 306 (not 315 - all 9
  artifacts are `jlabel`), debugger 10 (already accurate, no artifacts).**
  Tried to extend the same method to sanity-check the C-converted
  *numerator* too (e.g. is debugger's "172 converted" also inflated?) -
  this doesn't work: a function's `glabel` line disappears from `asm/`
  once it's actually converted (no more `.s` file backing it), so there's
  nothing left to grep against. Also tripped over a real gotcha here:
  naively excluding any `language: c` row whose name matched the `dlabel`
  set caught 140 of debugger's 172 as "artifacts" - but those are
  legitimate `extern` data-symbol declarations (`D_16003888` etc.), not
  function-conversion noise; `progress.csv` intentionally tracks data
  symbols alongside functions, so that exclusion was wrong, not a finding.
  Full writeup and the reusable grep pair are in
  [PROJECT.md](PROJECT.md)'s "Functions" caveats. **Net effect for
  planning:** the game section's true raw-function backlog (4161) is
  headroom for many future sessions - didn't start on it this session
  (stayed with debugger, see below) - and the corrected counts are
  what to plan against, not the raw `progress.csv` totals.
- **Set up `mips_to_c` (undocumented in this repo before now):**
  `tools/mips_to_c/m2c.py` failed with `ModuleNotFoundError:
  pycparser.plyparser` - the environment had `pycparser` 3.0 installed but
  `pyproject.toml` pins `^2.21`, and 3.0 removed the `plyparser` submodule.
  Fixed with `pip install --break-system-packages pycparser==2.21`. Also
  needed a type-context file: `conker/tools/ctx.py path/to/some.c`
  preprocesses that file (and its includes) into `conker/ctx.c`, which
  `m2c.py --context conker/ctx.c` reads for struct/global/function-signature
  info - generated one from `src/debugger/debugger.c` (pulls in
  `functions.h`/`variables.h` transitively). Deleted the generated
  `ctx.c` afterward (regenerate on demand, don't commit it - same
  category as `asm/`/`assets/`/`build/`).
- **`func_1600160C` (27 words) converted.** Raw asm proved it takes an
  `s32 arg0` (`andi $v0,$a0,...`), but its only call site
  (`src/debugger/debugger.c`, inside `func_160012B0`) was
  `func_1600160C()` - zero args, no prototype existed anywhere. This is
  the same class of bug as last session's `func_151696DC` call-site fix:
  the call happened to already compile correctly because `arg0` (the
  caller's own first param) was still sitting in `$a0` un-clobbered at
  that point, so the missing argument was silently free. Fixed the call
  site to `func_1600160C(arg0)` explicitly (verified this doesn't change
  `func_160012B0`'s own already-exact codegen) and added a real prototype
  to `functions.h`.
- **`func_16001678` (31 words) converted.** A framebuffer-region fill loop
  (writes the repeating word `0x10001` in 4-word bursts). No prior call
  sites reference it (dead code from the game's perspective, or
  called via a function pointer table not yet identified) so no call-site
  bug to fix here.
- **`func_16003650` (40 words) is genuinely not a C-conversion target.**
  Its `.s` file is headed `/* Handwritten function */` and contains raw
  `mtc0`/`tlbr`/`mfc0` (COP0/TLB) instructions reading all 32 TLB entries'
  EntryHi/EntryLo0/EntryLo1/PageMask into four output arrays - no C
  compiler emits these opcodes, so there's no source form that would
  "match" it by compiling. 32 other top-level (non-`nonmatchings`) `.s`
  files repo-wide share this `/* Handwritten function */` marker (grep for
  it in `asm/`) - same story for all of them. Left as `GLOBAL_ASM`
  permanently; doesn't count against real conversion progress once
  someone decides how to annotate "not applicable" functions (not
  attempted here - `progress.py`/`match_progress.py` don't currently
  special-case this).
- **Major incidental discovery: fixed a symbol-address-placement bug
  affecting the whole file.** Investigating why the two newly-converted
  functions weren't byte-exact, found `lui/lw` pairs loading
  `D_160038A8`/`D_16003888` from the wrong address - `nm
  build/conker.us.elf` showed both symbols linked ~16 bytes *before* the
  address their own `D_<hex>` name encodes (e.g. `D_16003888` resolved to
  `0x16003878`). No `symbol_addrs.us.txt` or `undefined_syms_auto.txt`
  entry existed for either - same unexplained-linker-placement class of
  bug as last session's init literal-pool drift, but for a raw data
  region instead of compiler-emitted float constants. **After converting
  the 2 functions (replacing their `GLOBAL_ASM` pragmas with real C),
  this resolved itself** - re-`nm`'d and both symbols now land exactly on
  their name-implied addresses. Re-ran match-progress and found this
  wasn't cosmetic: `func_16000424`, `func_16000058`, `func_16000000` (all
  pre-existing, already-converted functions using these same globals,
  previously showing as "diff") flipped to byte-exact with zero edits to
  them. **Debugger's byte-exact count jumped 15→128 of 172 (8.82%→74.42%)
  from this one side effect** - dwarfing the 2 functions actually
  converted. Root mechanism not identified (didn't dig into *why*
  replacing the `GLOBAL_ASM` stub fixed the neighboring data layout) -
  worth remembering as a technique: if a file has multiple
  address-drift-looking diffs across unrelated functions, try converting
  a neighboring still-raw function before hunting the "real" cause.
- **The 2 converted functions are themselves still not byte-exact** (18
  and 27 real diffs respectively, down from being entirely un-comparable
  as raw asm) - both are pure register-allocation/operand-order
  differences now, not logic bugs (every load address and control-flow
  edge matches; only instruction *scheduling* for a multiply-by-constant
  sub-expression differs). Tried three source rewrites for
  `func_1600160C`'s `(pos>>2) * (D_160038A8*2)` term chasing retail's
  exact `sra`-then-`sll`-then-`multu` order (plain inline expression,
  explicit named `stride` temp, swapped multiplicand order) - best result
  (16 remaining diffs, kept in source) still doesn't match; IDO's
  constant-multiply strength reduction seems to override source-level
  operand order here. Not resolved - next attempt should try forcing the
  doubling via `<<1` instead of `*2`, or splitting `pos` itself into a
  temp before the shift.
- **Not converted, left for later:** `func_16000F8C` and `func_1600078C`
  (both already had partial commented-out drafts from an earlier session,
  marked "lots to figure out"/"close but still some stuff") - both call
  `func_16001B34` in a way that needs a 5th `f64` argument, but
  `func_16001B34`'s current declared signature (in `debugger_257350.c`,
  itself already flagged `// NON-MATCHING: ported from ects_proto`) only
  takes 4 params. Fixing either properly means first extending
  `func_16001B34`'s signature and its callee `func_16001BB4`'s
  format-string handling to support float/double formatting - a separate,
  larger task, not attempted. `func_160006CC`, `func_160014F0`,
  `func_16000590`, `func_16001390`, `func_16001044`, `func_16000B14`
  (debugger.c) and `func_160021FC` (debugger_257350.c) were not started -
  `func_16001044` (155 words) is a 3-mode number formatter (hex/decimal/
  float) worth doing first among these since several already-converted
  functions call it with an still-unverified signature; its float mode
  also calls `func_16001B34`, same blocker as above.

### 2026-07-15 (sixth session - init-segment matching pass)

- **Toolchain note:** this environment has `mips-linux-gnu-objdump`/`-ld`
  etc. directly on `PATH` and IDO runs fine - none of the WSL/`PATH=...`
  workarounds from the second-session notes were needed here. Just
  `make -C conker <target>` from the repo directly.
- **`conker.ld` regression (root-caused and fixed):** `make -C conker
  match-progress` failed at the link step with `cannot find
  build/asm_eu/header.s.o`. `conker/conker.ld` is gitignored
  (`.gitignore: *.ld conker.ld`) and regenerated by splat on every
  `make extract` - but unlike `asm_path`/`asset_path`/`src_path` (which
  the EU-extraction session deliberately version-separated), the linker
  script's output path isn't parameterized by version at all, it's always
  written to the same `conker/conker.ld`. The EU extraction two sessions
  ago (`make extract VERSION=eu`) was the *last* extraction run in this
  checkout, so it left `conker.ld` full of `build/asm_eu/*.s.o` paths (651
  occurrences, confirmed by mtime: `conker.ld` regenerated 6s after
  `asm_eu/`). Fixed with `make -C conker extract VERSION=us`, which
  regenerates it correctly (1155 `build/asm/` refs, 0 `asm_eu`). Didn't
  touch `conker/asm` (already correctly extracted, untouched by the EU
  run) - only the linker script needed regenerating. **If EU/debug/ects
  extraction is ever run again, re-run `make extract VERSION=us`
  immediately after to restore `conker.ld` before doing any `us` work.**
  Worth fixing properly some day (e.g. version-suffix the ld script like
  the other paths, or just don't regenerate it for non-primary versions)
  but not attempted here.
- **`tools/match_progress.py` false-diff bug (root-caused and fixed):**
  built a small ours-vs-truth per-function disassembly dumper (uncommitted
  scratchpad, `dump_func.py` - same idea as the game-matching sessions'
  tool of the same name, rewritten from scratch since the old one wasn't
  saved) to inspect the init section's 28 "diff" functions one at a time.
  First function checked, `osCreateThread`, showed `ours=50 words,
  truth=52 words` - but every one of the 50 words it *does* have matched
  retail exactly, and the "extra" 2 truth words were both `0x00000000`.
  Sampled 10 more of the smallest-diff functions the same way: 9/10 showed
  the identical pattern (ours is a byte-exact *prefix* of truth, with only
  trailing all-zero words missing). Root cause: `progress.csv`'s declared
  function length is `next_symbol_addr - this_symbol_addr` from retail's
  address layout, which silently includes a handful of inter-function
  alignment nops that aren't really part of the preceding function's body
  - and `classify()` returned `"diff"` on ANY length mismatch before ever
  comparing content, so these always-correct functions could never be
  recognized. Fixed by trimming trailing all-zero `truth` words down to
  `len(ours)` before the length check, but only when `ours` is shorter (an
  `ours`-longer-than-`truth` case, or non-zero trailing words, still falls
  through to a real diff - confirmed both matter, see below). Re-ran
  project-wide: **total 379→435 exact (+56), init 201→223 (+22), game
  167→197 (+30), debugger 11→15 (+4) - zero source lines changed.**
  Progress tables updated in PROJECT.md/README.md/DOCS/README.md (dated
  2026-07-15).
- **Init's remaining 9 non-exact, fully characterized:**
  - **4 blocked, self-resolving:** `func_1000EB00`, `func_100125CC`,
    `func_1001263C`, `func_100127D0` - every diff word is a `jal` to a
    `game`-segment function that isn't byte-matched yet (`func_150ADA20`,
    `func_151F2CDC`, `func_151F2D6C`, `func_151F2BA8`, `func_151F2E4C`).
    Nothing to do here directly; they'll flip to exact as those `game`
    functions get matched.
  - **4 are an external rodata-pool address drift, not bugs in the
    functions themselves:** `func_10012D80`, `func_10012F94` (both in
    `src/libultra/audio/init_128D0.c`), `func_1001DAE4`
    (`src/libultra/audio/init_1D900.c`), `alCents2Ratio`
    (`src/libultra/audio/cents2ratio.c`). Every diff word is a
    `lui at,0x8003` + `lwc1 $fN,OFF(at)` pair loading a float/double
    literal from the compiler's per-file `.lit4`/`.lit8` pool - the
    disassembly is otherwise 100% identical to retail, but the loaded
    address is off by a constant delta *per source file*: -880 bytes for
    both `init_128D0.c` usages, -128 bytes for both the
    `init_1D900.c`/`cents2ratio.c` usages (confirmed by computing the real
    runtime addresses from each `lui`+offset pair - `0x8002C7C0` vs
    truth's `0x8002C450` for `func_10012D80`, etc.). Two different files
    showing two different, but *internally consistent per file*, deltas
    means each file's own literal pool is shifted by some fixed amount
    relative to retail - almost certainly one extra/missing/non-deduped
    literal earlier in *that file's own* pool (IDO pools `.lit4`/`.lit8`
    per translation unit, first-use order), not a shared/global table.
    **Not root-caused this session** - would need walking each file's own
    float/double literals in source order and diffing against retail's
    real pool contents at that file's base address in `init_data`
    (`conker.us.yaml`: `init_data` real vram `0x800290D0`, rom
    `0x290D0` - note this is a *different* address space than the `init`
    code segment's own splat-assigned vram `0x10001000`+, which is purely
    organizational and unrelated to the real runtime addresses embedded in
    instructions). Whoever picks this up next: don't try to "fix" these 4
    functions' own source, the bug is upstream of them.
  - **1 real narrow diff:** `__n_vsVol` (`src/init_1AAE0.c`) is short 4
    words - retail has extra `nop`s between an integer `multu`/`mflo`
    chain and the following `multu` (`t1 = (vs->tremelo * vs->velocity *
    vs->envGain) >> 6;`) that our compiled output doesn't emit. The build
    already passes `-Wab,-r4300_mul` (a VR4300 multiply-hazard workaround
    flag), so this is an assembler/compiler scheduling difference tied to
    the exact instruction sequence, not a logic bug - fixing it would mean
    finding a source form that reproduces retail's scheduling (e.g. an
    explicit intermediate temp forcing a spill/reload). Not attempted -
    one function, uncertain payoff.
- `dump_func.py` (scratchpad, not committed): given a function name, reads
  `progress.csv` for its section/vaddr/length, slices ground-truth bytes
  from `conker.us.bin` at the `SEGMENTS`-derived offset (same table as
  `match_progress.py`), and prints ours (from `build/conker.us.elf` via
  objdump) vs. truth (disassembled standalone via
  `objdump -D -b binary -m mips:4300 -EB`) side by side with a `<<`
  marker on mismatched words. Useful for any future single-function
  investigation - cheap to recreate from this description.

### 2026-07-15 (fifth session - Uncensored BPS/xdelta patches confirmed)

- User dropped `rom backup/Conker's Bad Fur Day (Uncensored).bps` and
  `.xdelta` (2,066,835 / 2,074,498 bytes) - the actual patch files the
  second session's inventory only saw inside a since-vanished
  `Uncensored Patches/` subfolder and reasoned about from the BPS footer
  alone. Parsed the BPS1 footer directly: source crc32 `CE8CC172`, target
  crc32 `E1B9019B`, patch crc32 `7187DF51`.
- **Confirmed empirically** (computed crc32 of files already in the repo):
  `baserom.us.z64` = `CE8CC172` (exact match to the patch's declared
  source - so today's root-level `baserom.us.z64` genuinely is the
  retail US ROM the second session went looking for) and `rom
  backup/Conker's Bad Fur Day (Uncensored).z64` = `E1B9019B` (exact match
  to the target). So `baserom.us.z64` + this patch = the Uncensored
  romhack, byte-for-byte.
- Since both endpoint ROMs are already present locally, the patch itself
  doesn't unlock new capability for the existing whole-file
  assets06/assets16 diff (already done, see the 2026-07-14 entry below) -
  but its BPS instruction stream (copy/insert ops with explicit offsets
  and lengths) would give exact byte-range boundaries for every changed
  region, finer-grained than the file-index-level diff already recorded.
- **Follow-up, same session: extracted the byte-range list.** Skipped
  parsing the BPS op stream (not needed) - did a direct full-ROM XOR diff
  of `baserom.us.z64` vs `rom backup/Conker's Bad Fur Day (Uncensored).z64`
  instead (both 67,108,864 bytes; `int.from_bytes` XOR + regex over the
  result, ~1.3s total, no numpy available in this env so this was the fast
  path), then mapped every differing byte range onto `assets06`/`assets16`
  file indices using the offset-table format from `tools/splat_ext/rzip.py`
  reimplemented standalone (section ROM bases `0x0117FE50`/`0x01330478`
  from `conker.us.yaml`). Totals matched the prior file-level finding
  exactly (39,919 / 2,020,358 bytes, 15 / 23 files - good cross-check that
  both the old and new methods agree). Full per-file byte-range table and
  the finding it enables (each `assets06` file's changes cluster in one
  sub-block well after a stable header, i.e. point directly at that file's
  container-table entry for the replaced dialogue line; `assets16` changes
  span nearly the whole file, confirming wholesale audio swaps not worth
  reversing further) are written up in
  [ASSET_FORMATS.md](ASSET_FORMATS.md) §4. Scratch pickles (`diff_ranges.pkl`,
  `offset_tables.pkl`, `per_file_ranges.pkl`) are in the scratchpad, not
  committed - cheap to regenerate from the description above if needed.
- **Follow-up, same session: walked the nested container to decode the
  dialogue-text schema.** Per the "first changed byte" pointers above,
  parsed each of the 15 `assets06` files' own §3-format container table,
  found the compressed entry 1 (decompresses to another §3-format
  container one level deeper - not yet documented before this), and
  checked its entries against the byte-range diffs. In 7/15 files the
  censored line falls exactly in that nested table's *last* entry (usually
  `flags=0x80`, the §3 terminator bit, but non-zero length) - decoding it
  as ASCII gives the literal subtitle text with `0x0A` line breaks, e.g.
  file 0033 entry 58 retail `"what the [censor-glyphs] !..."` vs
  Uncensored `"what the fuck !..."`. **Censorship mechanism confirmed:**
  retail substitutes a run of placeholder bytes from a ~9-value set
  (`0xA1-0xA6`, `0xB2-0xB5`) for the profane word, roughly matching its
  length but not a fixed per-letter cipher; `0xBD` is an unrelated
  formatting/pause glyph present identically in both versions (don't
  confuse it with the censor set). Full writeup with decoded examples in
  [ASSET_FORMATS.md](ASSET_FORMATS.md) §4 ("Dialogue text schema decoded")
  and the updated §9 open-questions bullet. Not done: the other 8/15
  files (censored line isn't the final nested entry - same container
  format, just need to identify which entry), and the exact
  placeholder-glyph selection rule.

### 2026-07-14 (fourth session - debug/ects baserom recovery)

- User asked to pull what's available for the `game` functions from `rom
  backup/`. Investigation found `us`/`eu` baseroms and their generated
  artifacts (`asm/`, `build/`, `conker/conker.us.bin`) all intact, but
  `baserom.debug.z64` and `baserom.ects.z64` missing from the repo root -
  a partial regression of the second session's "all four resolved" state.
  Untracked zero-byte `conker/core.*` files (9 of them) suggest an unclean
  process crash/restart is the likely cause, though this wasn't confirmed.
- `rom backup/` today has only 5 files (`Conker's Bad Fur Day
  (Europe).n64`, `... (Uncensored).z64`, `... [ects][DC].rom`, `Conkers
  Bad Fur Day [ntsc][debug][DC].rom`, `baserom.us.z64`) - no `initial
  ROMs/` subfolder or the other items the second session's inventory
  described. That inventory's file list is no longer accurate (folder's
  been reorganized again since); its recorded hashes are still good
  reference values, which is what mattered here.
- Re-verified `[ntsc][debug][DC].rom` sha1
  `3b99222ee76f6277a963142cd807b3df25d5174f` and `[ects][DC].rom` sha1
  `06597dc935651f8995bfacc30fde6e621d44c3e1` against
  `conker.debug.sha1`/`conker.ects.sha1` - both exact matches - and copied
  them in as `baserom.debug.z64`/`baserom.ects.z64`. All four baseroms
  (us/eu/debug/ects) are hash-verified at the repo root again.
  `us`/`eu` remain extracted and buildable (unaffected by this); `debug`
  and `ects` are still unextracted since their `.yaml` configs need the
  same splat modernization `us`/`eu` already received (see "Current
  focus" above and the first-session notes below) - not attempted this
  session, wasn't asked for.

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
