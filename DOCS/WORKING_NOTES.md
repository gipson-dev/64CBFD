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

**Update (2026-07-17, finish-what-is-possible init/libultra pass - +16 more
functions converted and one lingering libultra `GLOBAL_ASM` removed).** Added
C and wired `conker.us.yaml`/local `conker.ld` entries for `osRecvMesg`,
`osSendMesg`, `osJamMesg`, `osStartThread`, `osSetThreadPri`,
`osStopThread`, `osDestroyThread`, `osVirtualToPhysical`, `osPiRawReadIo`,
`osPiRawStartDma`, `osEPiRawStartDma`, `__osSpRawStartDma`,
`__osSiRawStartDma`, `bzero`, and `bcopy`; also replaced the
`osAiSetNextBuffer` `GLOBAL_ASM` body with C using the existing
`hdwrBugFlag` data label. Verified all new/touched objects compile and
`build/conker.us.elf` links with `NON_MATCHING=1`, then regenerated
progress. Total raw conversion is now `1631 / 6034 (27.03%)`, init is
`297 / 538 (55.20%)`, byte-weighted total raw conversion is `7.27%`, and
byte-weighted init raw conversion is `25.18%`. Current `match-progress`:
`914 / 1631 (56.04%)`, blocked `495`, differ `222`; init is
`77 / 297 (25.93%)`, blocked `159`, differ `61`; game is
`816 / 1153 (70.77%)`, blocked `323`, differ `14`; debugger remains
`21 / 181 (11.60%)`, blocked `13`, differ `147`. The exact-match drop is
expected for this pass because several newly converted init/libultra rows sit
early in the link and moved downstream addresses; the new C is raw-progress
source, not final size-matched source.

**Update (2026-07-16, bigger stock init/libultra pass - +9 more functions
converted).** Added C and wired `conker.us.yaml`/local `conker.ld` entries
for `lldiv`, `ldiv`, `_Litob`, `__osTimerServicesInit`,
`__osTimerInterrupt`, `__osSetTimerIntr`, `__osInsertTimer`, `osSetTimer`,
and `osGetTime`. The timer cluster uses the ROM's existing `D_8002BD70` /
`D_800429B0` / `D_800429B8` / `D_800429BC` / `D_800429C0` storage labels
rather than introducing new stock `__os*` data symbols. Verified all new
objects compile and `build/conker.us.elf` links with `NON_MATCHING=1`, then
regenerated progress. Total raw conversion is now
`1615 / 6034 (26.76%)`, init is `281 / 538 (52.23%)`, byte-weighted total
raw conversion is `7.14%`, and byte-weighted init raw conversion is
`23.16%`. Current `match-progress`: `1085 / 1615 (67.18%)`, blocked `324`,
differ `206`; init is `207 / 281 (73.67%)`, blocked `29`, differ `45`.
`init_5AB0` still needs a different treatment because it is one large
handwritten asm segment; tiny plain-memory candidates such as
`func_10007A24` and `func_10005BE0` are visible, but pulling them out
cleanly requires splitting that segment around the converted C.

**Update (2026-07-16, init raw conversion continuation - +12 more stock
libultra functions converted).** Added C and wired `conker.us.yaml`/local
`conker.ld` entries for `osPiGetStatus`, `osPiGetDeviceType`,
`__osSpGetStatus`, `__osSpSetStatus`, `__osSpSetPc`, `__osSpDeviceBusy`,
`__osSiDeviceBusy`, `__osSiRawReadIo`, `__osSpRawWriteIo`,
`osSpTaskYield`, `osSpTaskYielded`, and `__osDequeueThread`. Verified the
new objects compile and `build/conker.us.elf` links with `NON_MATCHING=1`.
Regenerated progress: total raw conversion is now `1602 / 6034 (26.55%)`,
init is `268 / 538 (49.81%)`, and byte-weighted init raw conversion is
`21.49%`. Current `match-progress`: `1085 / 1602 (67.73%)`, blocked `324`,
differ `193`; init is `207 / 268 (77.24%)`, blocked `29`, differ `32`.
Remaining tiny init asm rows are mostly CP0/cache/TLB/math instructions or
custom startup functions, so keep using stock libultra source where the C
is real and leave pure hardware instruction shims as raw asm.

**Update (2026-07-16, init raw conversion pass - +24 stock libultra/libc
functions converted).** Converted stock init-section helpers by adding C
sources and flipping their `conker.us.yaml`/`conker.ld` subsegments from
raw asm to C: `memcpy`, `strlen`, `strchr`, `__ull_rshift`, `__ull_rem`,
`__ull_div`, `__ll_lshift`, `__ll_rem`, `__ll_div`, `__ll_mul`,
`__ull_divremi`, `__ll_mod`, `__ll_rshift`,
`__osPiCreateAccessQueue`, `__osPiGetAccess`, `__osPiRelAccess`,
`osCreateMesgQueue`, `__osSiCreateAccessQueue`, `__osSiGetAccess`,
`__osSiRelAccess`, `osViSwapBuffer`, `osViGetCurrentFramebuffer`,
`osViGetNextFramebuffer`, and `osPiGetCmdQueue`. Verified the new objects
compile and `build/conker.us.elf` links with `NON_MATCHING=1`. Regenerated
progress: total raw conversion is now `1590 / 6034 (26.35%)`, init is
`256 / 538 (47.58%)`, and byte-weighted init raw conversion is `21.14%`.
Current `match-progress`: `1085 / 1590 (68.24%)`, blocked `323`, differ
`182`; init is `207 / 256 (80.86%)`, blocked `28`, differ `21`. The
byte-match dip is expected because this was a raw-conversion pass, not a
size-matching pass.

**Update (2026-07-16, debugger raw conversion finish - 10 debugger
functions converted; one hardware asm exception remains).** Converted the
remaining debugger raw queue to C except `func_16003650`:
`func_16000590`, `func_160006CC`, `func_1600078C`, `func_16000B14`,
`func_16000F8C`, `func_16001044`, `func_16001390`, `func_160014F0`,
`func_16001BB4`, and `func_160021FC`. Added `struct263`, split
`struct118`'s debugger fields, and declared the debugger globals needed by
the recovered C. Verified `build/src/debugger/debugger.c.o`,
`build/src/debugger_257350.c.o`, and `build/conker.us.elf` with
`NON_MATCHING=1`. Regenerated progress: total raw conversion is now
`1566 / 6034 (25.95%)`, debugger is `181 / 182 (99.45%)`, and
byte-weighted debugger raw conversion is `99.19%`. `func_16003650` remains
`GLOBAL_ASM` because it is a real CP0/TLB reader (`tlbr` plus CP0 register
moves), not safely representable as pure C with this compiler. Current
`match-progress`: `1106 / 1566 (70.63%)`, blocked `298`, differ `162`;
the debugger byte-match dip (`21 / 181`, 13 blocked, 147 differ) is expected
because these new C bodies are raw-progress placeholders, not size-matched
retail code yet.

**Update (2026-07-16, raw conversion pass - +6 game functions converted
from raw assembly to C).** Converted `func_15074A94`, `func_1514672C`,
`func_1513E13C`, `func_1513F6E8`, `func_1513FA2C`, and `func_1513FA70`
from `GLOBAL_ASM` to C, and split `struct210`'s `0x128` float out of
padding as `unk128` for `func_1513F6E8`. Verified `build/conker.us.elf`
links, then regenerated `progress.csv`: total raw conversion is now
`1556 / 6034 (25.79%)`, game is `1153 / 5314 (21.70%)`, byte-weighted
total is `6.61%`. `make -C conker match-progress NON_MATCHING=1` reports
`1234 / 1556 (79.31%)`, blocked `285`, differ `37`; the raw-conversion
win intentionally shifts game-section layout until these C bodies are
size-matched or padded back.

**Update (2026-07-16, nineteenth session - two more hand-written-asm
functions identified and made byte-exact; match_progress now anchors
named symbols; verified snapshot after progress.csv regen: 897/1552
(57.80%), game 525/1149, still-differ 41 -> 37. The denominator dropped
by 2 - the two conversions moved out of the C-converted count into asm,
same accounting as the session-18 PRNG pair; before the regen the same
build measured 899/1554 with both counted exact.)**
Continued the `game` still-differ queue ("continue with functions").
Results:

- **Tool fix (match_progress.py)**: implemented the eighth session's
  deferred "deeper fix" - for named (non-`func_XXXXXXXX`) symbols the
  retail VRAM anchor now comes from `symbol_addrs.<version>.txt` (new
  `--symbol-addrs` flag, auto-found next to progress.csv) instead of
  progress.csv's current-build offset. `guMtxCatL`/`guMtxXFML`
  immediately reclassified DIFF->BLOCK: both are already source-matched
  (stock libultra mtxcatl.c shape); their only diffs are jal targets to
  `guMtxL2F`/`guMtxXFMF`/`guMtxCatF`/`guMtxF2L2`, which sit +0x300 from
  retail in our build. The same alias resolution was added to
  `is_symbol_addr_drift` so lui/addiu references to named symbols
  classify as drift too.
- **func_15125628 (game_14FF90.c) byte-exact via hand-authored
  GLOBAL_ASM**: the 4-timer-byte decrementer is almost certainly
  hand-written asm in retail - every access is an assembler-macro
  expansion (self-base `lbu $v0, sym` loads, `lui $at` stores, two
  independent %hi per block). Proved by experiment that IDO only emits
  that shape when each of the 8 accesses references a distinct
  single-use symbol (8 distinct externs compile byte-identical
  structurally; any same-symbol pair CSEs into lui+addiu+0(rN)).
  Tried and ruled out: volatile casts (double-loads), literal-address
  casts (lui+ori CSE), offset spellings off the 3 neighboring scalars
  (multi-use symbols re-materialize into registers). Since no plausible
  C exists, wrote `asm/nonmatchings/game_14FF90/func_15125628.s` BY HAND
  from the retail bytes (26 words; no re-extraction dance needed - much
  cheaper than the session-18 pragma-then-extract route, and doesn't
  clobber undefined_funcs_auto.txt). Verified 0/26 at the name-implied
  address.
- **func_1505EEB0 (game_83300.c) byte-exact the same way** (17 words,
  0/17): same non-CSE signature (self-base `lw` of D_800CC2D0->
  interaction_state PLUS a separate lui/addiu of the same symbol), plus
  an unfilled jr-delay nop with the return move scheduled before it -
  IDO never does either. Tried first: pointer do-while (18 diffs),
  D_800CC2D0[i] indexing (no strength reduction - multu by 812),
  scalar-struct extern (still CSEs). Hand-authored .s, C kept in
  comments.
- Dead ends recorded in-source: func_1504BA38 (12 rename diffs - tried
  baiting retail's a1 with an unused 2nd parameter; K&R s8, ANSI s8,
  ANSI s32 all home a1 to the stack at entry); func_1507A3E8 (u8 locals
  fix load order but demote temps to named regs; innermost-pair swap
  leaves lui-pairing wrong); func_151696DC (2-diff scheduling coin-flip:
  both `i = 0` reorders regress to 11 diffs).
- Remaining game still-differ (14): the 2-diff pair
  func_1516968C/func_151696DC (cfe canonicalization / scheduler
  coin-flip), four documented-dead-end small ones, and the
  game_77AD0.c cluster (func_1504A620/ADD0/AF10/B0FC/BE2C/C8BC,
  func_1505210C, func_15169070) - the big ones are fresh territory for
  a future session. Watch for more hand-written-asm signatures there
  (self-base loads + lui-at stores + same-symbol double %hi = convert,
  don't chase).

**Update (2026-07-16, eighteenth session part 5 - func_16001044 done;
EVERY debugger overlay function is now byte-exact: 149/171 exact
(87.13%), zero function rows left in the diff queue; total 897/1554
(57.72%).)**
Worked `func_16001044` (the mode 0/1/2 number renderer in
`debugger/debugger.c`). Real idioms recovered and verified against
retail (kept in the commented draft): the divisor-table copy is a
**struct assignment** (IDO's `$at` 3-word block-copy loop - added a
`Table1044` typedef), the hex digit is a **u8 local** (`andi 0xff` after
every arithmetic step), the decimal loop uses separate `base`/`stop`
pointer locals plus `printed = 0` positioned after the negative check,
`exp` is s32 (`sra` not `srl`), and - the big one - **the f32
reinterpret must go through the local's address** (`*(s32 *) &f = arg2;`;
the old `*(f32 *) &arg2` took the parameter's address, forcing arg2
stack-homed for the whole function at a cost of ~30 diffs). Got from
151 real diffs to 151-words/~35-diffs - but 4 words SHORT (uopt hoists
one `&sp78` materialization to a callee-saved at entry where retail
rematerializes per site, the same value-copy micro-idioms as
func_16001BB4), and since this file's `D_1600xxxx` data is inline in
.text, wrong size is unacceptable. Converted to **GLOBAL_ASM** via the
same pragma-then-`make extract` dance as func_16001BB4 (remember: the
extraction clobbers `conker/undefined_funcs_auto.txt` again - re-append
`func_10026700`/`func_10026750`). Verified 0/155 word diffs at the
name-implied retail offset. Also tested and ruled out: compiling
`debugger.c` at plain `-O2` without `-g3` (much worse - `-g3` is
load-bearing for the existing matches).

Remaining debugger still-differ rows (22) are now ALL data content
(`D_16003xxx`/`D_16004xxx`). Progress tables in README.md /
DOCS/README.md / DOCS/PROJECT.md regenerated end-of-day.

**Update (2026-07-16, eighteenth session part 4 - THE DEBUGGER OVERLAY
DATA DISPLACEMENT IS HEALED: debugger 27 -> 147/172 byte-exact (85.47%),
total 776 -> 895/1555 (57.56%).)**
Closed out the size problem. The two remaining func_16001BB4 words are
uopt scheduling coin-flips, not structure - our build produces the SAME
double `beqz t9` branch pair and the same blocks; only the delay-fill
choices differ (retail likely-converts branch 1 with the duplicated
`addiu a3,s2,1`, and fills the loop-back `b` delay with an `lbu` preload
of the loop top; ours fills the `b` delay with the addiu instead - the
two choices interlock). Tried and ruled out at the source level:
shared vs per-instance _PAD i/c pairs, assignment-in-condition,
assignment-in-macro-argument, `(s32)` cast on the chunk expression,
goto vs while(1) vs `for (;; fmt = fmt_ptr + 1)` - all compile
byte-identical. Since the C is semantically verified and only 2 words
off, converted `func_16001BB4` to **GLOBAL_ASM** (C kept in comments
with a detailed note) so the function occupies its exact retail 402
words. Verified via raw linked-ELF bytes vs retail ROM:
**func_16001BB4 is 0/402 diffs**, and the whole debugger overlay's
remaining text diffs are just `func_16001044` (151/155, the next
target) and `func_1600288C` (21/294 - the exp stack-slot offset x~15
plus qr; note its slot layout shifted again after the 16001BB4 pragma
change, so re-tune AFTER other file edits settle, and beware:
`match_progress.py`'s per-function diff counts are wrong for these rows
(reported 226/363 where raw bytes show 21/0) - trust raw byte compares
at name-implied offsets).

Re-extraction gotchas hit on the way (WSL env): splat needed
`pip3 install --break-system-packages colorama intervaltree spimdisasm
tqdm n64img pygfxd crunch64 msgpack` (and re-pin `pycparser==2.21` for
mips_to_c afterwards - requirements.txt upgraded it to 3.0). Splat only
emits a nonmatchings `.s` for functions that are GLOBAL_ASM pragmas in
the current `.c` (so set the pragma FIRST, then `make -C conker extract
VERSION=us`). The extraction also regenerates
`conker/undefined_funcs_auto.txt` and DROPS symbols referenced only from
GLOBAL_ASM blocks inside `.c` files - the link then fails with
`undefined reference to func_XXXXXXXX`; fix by appending
`func_XXXXXXXX = 0xXXXXXXXX;` lines (name-implied addresses; this
session needed func_10026700/func_10026750).

Remaining debugger still-differ rows are now almost all **data**
(`D_16003xxx`/`D_16004xxx` content diffs - the file's rodata/data blobs
our compile emits vs retail's: string tables, the `_Litob` digit
strings D_16003CB8/CCC, the jump table D_1600487C region, float pool
D_16004950 etc.). That's the next debugger frontier after
func_16001044: make debugger_257350.c's emitted data byte-match.

**Update (2026-07-16, eighteenth session part 3 - the SDK source works:
func_16002DE4 byte-exact, func_1600288C and func_16001BB4 nearly so; the
debugger data displacement is down from -0x60 to -8.)**
Followed the Plauger identification to its source: **the N64 SDK's libultra
libc ships this exact code, and n64decomp/mk64 (`src/os/_Ldtob.c`,
`src/os/_Printf.c`) and n64decomp/sm64 (`lib/src/`) carry IDO-matched
copies.** Worked the three remaining size-wrong functions from those texts:

- `func_16002DE4` = `_Genld`: transcribed mk64's text with our field names
  (width=precision, len=part2_len, dest=buff, unkC=part1_len,
  unk18=num_mid_zeros, unk1C=part3_len, unk20=num_trailing_zeros,
  unk28=width, padWidth=num_leading_zeros, func_16001AD0=memcpy,
  D_16004878="0"). **369/369 words, zero real diffs** after one statement
  swap (retail assigns `arg2 = D_16004878;` before `arg3 = 1;`). Now
  classified BLOCK. Key shapes: in-place `p`/`xexp` mutation, compound
  `(px->width -= xexp) < 0` tests, `unk1C = arg3` embedded in the copy
  call, comma statements, `u8 point = '.'` local.
- `func_1600288C` = `_Ldtob`: **294/294 words, 26 remaining diffs, all
  stack-slot offsets** (qr at 92 vs 100, exp at 152 vs 142; frame and
  every other slot exact). Load-bearing finds: `err` is s32 (s16 adds a
  caller-side sll/sra retail lacks); retail's 0.0/1.0 come from **f32
  variables** (`fzero`/`one` - literals constant-fold to double pairs,
  but f32 locals constant-propagate to single materializations +
  cvt.d.s, exactly retail's `mtc1 zero,$f4; cvt.d.s` and
  `lui at,0x3f80` forms); a **`volatile f64 zero2 = zero;`** copy is
  what reproduces retail's memory-homed loop-backedge zero (a plain
  copy coalesces into callee-saved $f22 - volatile blocks the coalesce;
  possibly the original had something equivalent, or uopt's
  constant-spill strategy differs subtly); `lo` top-level + `qr`
  **block-scoped in the for** gives retail's `lw t2/move s1,t2`
  backedge (top-level qr kills the move); declaration order controls
  slot packing (moving `zero`/`fzero`/`one` declarations after `n2`
  fixed zero2 to 160 and the frame to 216).
- `func_16001BB4` = `_Printf`: rewritten with the SDK's **ATOI/_PROUT/
  _PAD macros** - the pad emissions each have a distinct i/c local pair
  (ten s32 locals), and the running total is **`st.pad2C`** (Plauger's
  `_Pft.size` struct field), which resolves the thirteenth session's
  "total in a stack slot 0xd4(sp)" mystery for free. Also found and
  fixed a REAL bug: retail's `func_160021FC` (_Putfld) reads the length
  modifier from **struct offset 0x34** (`lbu 0x34($s1)` x5), so
  `u8 length` was added to struct262 and `st.length` replaces the old
  `length_mod` local that never reached the callee (h/l/L modifiers were
  silently dropped). **400/402 words, ~6 real diff instructions**: two
  s32 dead pads (`pad1`, and `n` from an assignment-in-condition
  experiment) restore the frame to 224 and collapse ~90 offset diffs.
  Two single-word idioms remain: (1) retail computes the first chunk as
  `subu v0` + `move s1,v0` (uopt web-split across the callback; ours
  coalesces into s1 - assignment-in-condition did NOT reproduce it),
  and (2) retail's last-_PAD skip is the classic IDO
  **beqzl+beqz double branch on the same register** with
  `fmt = fmt_ptr + 1` in the likely delay and a `lbu` loop-top preload
  in the final `b 0x64` delay - goto-form and while(1)-form both compile
  identical without it. These 2 missing words shift everything after
  func_16001BB4 by **-8** (map confirms: func_160021FC at 0x160021F4
  etc.), which is now the ONLY remaining displacement - down from -0x60.

Verified snapshot: `776/1556` exact, `623` blocked, `157` still differ;
debugger `28/173` exact (func_16002DE4 joined), `7` blocked, `138` still
differ. `match_progress` currently over-reports func_1600288C (226) and
func_16001BB4 (363) because of the -8 shift interacting with its
counting; the `.o`-level diffs (26 and 14 including relocs) are the real
numbers. **Next session: close func_16001BB4's two words** (that heals
the whole overlay's data placement), then func_16001044 (151 diffs,
correct size), then 288C's qr/exp slots. The debug ROM may help on the
beqzl idiom (it contained func_16002D2C word-for-word).

**Update (2026-07-16, eighteenth session part 2 - THE DEBUGGER FORMATTER IS
PLAUGER'S STANDARD C LIBRARY; func_160033A8 code-exact via _Litob.)**
Continued the size-wrong five with `func_160033A8`. The decisive discovery:
**`debugger_257350.c`'s formatter engine is Rare's 64-bit adaptation of
P.J. Plauger's "The Standard C Library" printf implementation.** Found by
searching for the code shape (`table[uValue % radix]`) after the aligned
diff kept resisting register-allocation guesses. The mapping:
`func_16001BB4` = `_Printf`, `func_1600288C` = `_Ldtob`,
`func_16002DE4` = `_Genld` (its `(struct262 *, u8 code, u8 *p, s16 nsig,
s16 xexp)` signature is exactly `_Genld`'s), `func_160033A8` = `_Litob`,
`func_16002D2C` (matched session 11) = `_Dtest`, and `func_160021FC` is
likely `_Putfld`. **Work the remaining three from Plauger's published
source, not from decompiler output.**

Rewrote `func_160033A8` to `_Litob`'s exact shape and it now compiles
**byte-identical to retail (168/168 words, frame 0x90, zero real diffs at
the .o level)**; after a full build, `match_progress.py` reclassifies it
from `DIFF` (125 real diffs) to `BLOCK` - its only remaining mismatches
are `%lo(D_16003Cxx)` displacement, i.e. the known -0x60 data placement.
The load-bearing Plauger idioms (all verified against retail bytes):
- `table`/`radix` are **declaration initializers**; radix is the nested
  ternary `(c == 'o') ? 8 : (c != 'x' && c != 'X') ? 10 : 16` (the inner
  ternary's temp produces retail's `move t1,t0`; as an if/else statement
  uopt coalesces it away, and `radix = base;` via a second variable
  wrongly promotes radix to a callee-saved register).
- `uvalue` initializes **directly from `arg0->num.value`** and the sign
  test reads the struct again - there is NO `s64 value` local; retail's
  64/68(sp) pair is cfe's 64-bit staging temp, not a variable.
- The negate is `uvalue = -uvalue;` (retail negates the uvalue slots).
- **`buf[--pos] = table[...]`** - the pre-decrement's temp is what stops
  uopt from strength-reducing the indexing into a moving `out` pointer
  (the fifteenth session's `out` was a wrong turn; reverted).
- The loop is `while ((arg0->num.value > 0) && (pos > 0))` with
  **`lldiv_t qr` block-scoped inside the loop** and
  `lldiv(arg0->num.value, radix)` reading the struct directly.
- `arg0->len = 24 - pos;` then passing `arg0->len` to the copy (no
  `total` local - deleting it fixed the last +8 frame-size delta), and
  the final width fixup **reuses `pos`** (Plauger reuses `i`).

Verified snapshot after full rebuild: `775/1556` exact, **`622` blocked**,
**`159` still differ**; debugger is `27/173` exact, `6` blocked, `140`
still differ. Remaining real-diff debugger functions: `func_16001044`
(151, correct size since session 10), `func_1600288C` (263 = `_Ldtob`),
`func_16002DE4` (366 = `_Genld`), `func_16001BB4` (392 = `_Printf`).
Once those three are size-correct the -0x60 data displacement heals and
the ~130 blocked `D_16003xxx`/`D_16004xxx` rows plus the small blocked
functions should all flip to exact.

**Update (2026-07-16, eighteenth session - PRNG pair identified as
hand-written assembly; both now byte-exact via GLOBAL_ASM.)**
Closed out `func_150ADACC` (3 real diffs) and `func_150ADA20` (19 real
diffs): they are **hand-written assembly in the original game**, not
compiler output, so no C source shape can match them. Evidence, in
decreasing order of strength: retail `func_150ADA20` is strictly
source-order sequential where IDO -O2 provably reschedules (our build of
the equivalent C interleaves the shift pairs); its loads/stores are the
assembler's literal `ld a0, D_800885B0` / `sd a0, D_800885B0` macro
expansions (`lui a0; ld a0,(a0)` self-base and `lui at; sd`); it reuses
only a0/a1/a2 as scratch in a void-arg function; the `jr ra` delay slot
holds a useful `dsra32`; and `func_150ADACC`'s dead `li a0,0; jr ra`
ending is **unique in the entire ROM** (scanned - 1 hit). Tried and ruled
out on the way: s64 local (daddiu lands in t7, dead store eliminated),
ANSI and K&R u64 parameter (both home the a0/a1 pair via sw/sw/ld -
retail has no homing), `(s64)arg0 + 1` expression (t7 again). Reverted
both to `#pragma GLOBAL_ASM` (the extracted `.s` files were still intact)
with the verified-correct C kept as comments, same convention as
`func_16003650`. Restored the seventeenth session's `u32` prototype for
`func_150ADACC` in `functions.h` so caller `func_1501905C` stays matched.
Verified via ELF-at-symbol-address comparison: both functions byte-exact
at their name-implied retail offsets. New verified snapshot:
`775/1556` exact (denominator dropped by 2 - the pair moved out of the
C-converted count), `621` blocked, **`160` still differ**; `game` is
`525/1151` exact, `608` blocked, **`18` still differ**.

Environment notes for future sessions on the Windows host: builds run via
WSL distro `PSBBN` (`wsl.exe -e bash -lc`, strip UTF-16 NULs from output);
the correct ELF for `match_progress.py` is `conker/build/conker.us.elf`,
NOT the repo-root `build/conker.us.elf` (a data-only ROM-image ELF that
silently yields 0/1558). Also guarded `tools/match_progress.py`'s SIGPIPE
handler with `hasattr` - native Windows Python has no `signal.SIGPIPE`.

**Update (2026-07-16, seventeenth session - address-drift noise reduced;
seed setter/caller improved.)**
Continued matching "as many as possible" after the sixteenth-session helper
work. Improved `tools/match_progress.py` again:
- Classifies external literal/data address drift as blocked when a mismatched
  load/store or address-materializing `addiu`/`ori` has the same instruction
  shape and a matching recent `lui` base. This moves the known debugger
  `D_1600xxxx` low-half displacement functions (`func_16000000`,
  `func_16000058`, `func_16000424`) out of the real source-diff queue.
- Computes retail slice lengths from sorted symbol VRAMs (including asm rows)
  instead of trusting shifted current-layout `progress.csv` lengths. This
  fixed `func_15055D48`: the current map made it look 67 words long, but the
  next name-implied symbol (`func_15055E50`) proves the retail slice is 66
  words; the extra word was the next function's prologue after one alignment
  nop. It is now correctly `BLOCK`.
- Installed SIGPIPE default handling so `--list | head` no longer prints a
  Python `BrokenPipeError` traceback.

Source work: `func_1501905C`'s remaining real mismatch was a bad signature on
`func_150ADACC`. Retail passes the seed constant in `a0`, while the old
`s64` prototype forced a two-register call. Changed the declaration and
definition to `u32`, and rewrote the setter as:
`arg0 += 1; D_800885B0 = arg0;`. This moves `func_1501905C` to `BLOCK` and
improves `func_150ADACC` from `7` real diffs (old `s64`) / `4` real diffs
(`u32` one-expression form) to **`3` real diffs**. Remaining callee delta:
retail uses `daddiu a0,a0,1`, stores `a0`, then has a dead `li a0,0` before
`jr ra`; IDO's best C form found so far uses `addiu a0,a0,1`, stores `a0`,
and omits the dead assignment. Adding `arg0 = 0;` after the store was
optimized away.

Verified snapshot after these changes: `775/1558` exact, `621` blocked on
address drift, `162` still differ; `game` is `525/1153` exact, `608`
blocked, `20` still differ; `debugger` is `27/173` exact, `5` blocked,
`141` still differ.

**Update (2026-07-16, sixteenth session - progress target checked;
function-pointer drift classified; func_1516968C temp dead end.)**
Ran the requested `make -C conker progress NON_MATCHING=1`; it was already
up to date (`Nothing to be done for 'progress'`). Used the drift-aware
`match_progress.py` listing for the actual candidate selection.

Tooling fix: `func_15010680` and `func_150106B0` looked like one-real-diff
`game` functions, but each is only assigning a global function pointer to a
shifted callee (`func_150EA904` / `func_150EB430`). The only byte mismatch is
the `%lo` half of the loaded function address (for example current
`0x150EAC04` vs name-implied retail `0x150EA904`). Updated
`tools/match_progress.py` to recognize `lui`+`addiu`/`ori` address
materializations of `func_XXXXXXXX` symbols and classify those as blocked,
like `j`/`jal` target drift. Verified snapshot now reports
`775/1558` exact, `605` blocked, `178` still-differ; `game` is
`525/1153` exact, `601` blocked, `27` still-differ.

Source experiment tried and reverted: in `func_1516968C`, added a local
`u8 value = *arg1` to try forcing retail's `a1`-base load before
`arg0->unkC`. It worsened the function from `2` to `7` real diffs, so the
source is back at the prior best form. The existing comment remains accurate:
cfe canonicalizes the equality load order.

**Update (2026-07-16, fifteenth session - func_160033A8 pointer form
improved debugger progress.)**
Continued the debugger function work after re-reading this file. Kept the
fourteenth-session `match_progress.py` fix as the measurement baseline, then
worked `func_160033A8` in `conker/src/debugger_257350.c`.

Best measured source change: add a branch-local moving `out` pointer for the
temporary decimal/octal/hex buffer. The first emitted digit now assigns
`out = &buf[pos]` inside the nonzero/width branch (or the one-past end in
the zero-width branch), the loop decrements `out`, and the final copy passes
`out` to `func_16001AD0`. This keeps the better pointer live range and
improves the corrected progress snapshot from `774/1558` total /
`26/173` debugger to **`775/1558` total / `27/173` debugger**.
`func_160033A8` is still non-matching, but improved from `154` to **`130`
real diffs** (`171` words).

Dead end tried and reverted: hoisting `out = &buf[pos]` before the first
digit branch, then pre-decrementing it in the branch. That shrank the
function back to `159` words but lost the real win: progress returned to
`774/1558`, debugger `26/173`, and `func_160033A8` measured at `153` real
diffs. Keep the branch-local `out` form unless a future experiment beats the
`775/1558` snapshot.

**Update (2026-07-16, fourteenth session - match-progress made truly
drift-aware; func_16001BB4 experiments bounded.)**
Re-read this file and continued the debugger function work. The
`func_16001BB4` best source state from the thirteenth session is still the
best measured one: the real `&arg3` va_list fix plus explicit
`spacePad`/`zeroPad`/`flagChars`/`digitBase` locals. Re-tested several
source-shape ideas and reverted them because none beat **369 words / 359
real diffs**:
- Reordering the long-lived locals/initializers to try to give
  `digitBase` first claim on a saved register: no register or score change.
- Dropping the `spacePad` alias while keeping `zeroPad`/`flagChars` and
  `digitBase`: no score change, still hoisted `D_16003C70` into `s8`.
- `register s32 digitBase`: no effect.
- `volatile u8 length_mod`: forced stack-ish behavior in the length-modifier
  area but bloated the function to `373 words / 371 real diffs`.

Important tool fix: `tools/match_progress.py` did **not** actually do the
name-implied-VRAM comparison that earlier notes described. It used
`progress.csv`'s current shifted address, which made downstream debugger
functions look worse or better depending on upstream size drift (for
example `func_16002D2C` is truly exact, but was reported as 45 diffs; and
`func_1600288C` looked like only 2 diffs because it was just a length
mismatch at the wrong retail offset). Fixed the helper to use
`func_XXXXXXXX` names as the retail VRAM anchor when possible, and to count
length mismatch **in addition to** overlapping word diffs. New verified
snapshot from `make -C conker match-progress NON_MATCHING=1`:
`774/1558` total byte-exact, `603` blocked-on-callee, `181` still differ;
debugger is now `26/173` byte-exact. With corrected accounting,
`func_16002D2C` is no longer listed (exact), while the true nearby debugger
targets are `func_160033A8` (154 diffs), `func_1600288C` (267 diffs),
`func_16001BB4` (359 diffs), and `func_16002DE4` (364 diffs).

Checked the apparent tiny debugger candidates too: `func_16000000`,
`func_1600160C`, and `func_16001678` only differ in embedded `D_16003xxx`
addresses caused by the still-open data-placement displacement, not in
their source bodies. Do not spend source-matching time on them until the
data displacement is healed.

**Update (2026-07-16, thirteenth session - func_16001BB4 nudged to
369 words / 359 real diffs; pressure dead ends recorded.)**
Continued the twelfth-session `func_16001BB4` focus in
`conker/src/debugger_257350.c`. Kept the real `va_list` bug fix
(`func_160021FC(&st, &arg3, *scan, buf)`) and added explicit locals for
the long-lived padding/flag strings plus decimal base:
`spacePad = D_16003C70`, `zeroPad = D_16003C94`,
`flagChars = D_16004804`, `digitBase = 10`. This is behavior-neutral, but
it gives IDO a slightly more retail-like source shape around the flag scan,
digit parsing, and padding callbacks. Verified with
`make -C conker match-progress NON_MATCHING=1`: overall exact count stays
`445/1558`, debugger exact count stays `25/173`, and
`func_16001BB4` improves from the prior `369 words / 360 real diffs` to
**`369 words / 359 real diffs`**.

Dead ends tried and reverted:
- `volatile s32 total` forced stack traffic but bloated the function to
  `387 words / 382 real diffs`.
- Reusing `st.pad2C` as the accumulator looked tempting because retail's
  accumulator sits at `0xd4(sp)`, but IDO optimized it back into a register
  in the wrong allocation shape and also landed at `387 words / 382 real
  diffs`.
- Adding a `lengthChars = D_16004800` alias for the length-modifier
  `strchr` lost the one-diff improvement (`369 words / 360 real diffs`).

Current best next step: do **not** chase `total` directly with `volatile`
or `st.pad2C`. The remaining gap still looks like an original-source
register-pressure/allocation idiom, but the productive lever is likely the
expression/variable lifetime shape around the parse loops and padding
emission, not a forced accumulator spill.

**Update (2026-07-15, twelfth session - func_16001BB4's "impossible diff"
explained; a real va_list bug found and fixed; 367->369/402 words.)**
Picked up the session-eleven punch list's last untouched item,
`func_16001BB4` (the hand-rolled vsprintf engine, `debugger_257350.c`).
Naive `diff.py func_16001BB4` (and my own first pass reading it) produced
garbage: the "target" column's first instructions read *already-populated*
stack slots with no prologue in sight, which is impossible for a real
function entry. Root cause: **this specific function is short enough
(historically noted as -0x8C/-35 words) that our build's own
`debugger_257350.c` text section has drifted +0x300 (768 bytes) from
retail by the time it reaches `func_16001BB4`**, so the plain
name-based/map-based address that `diff.py` resolves for the *retail* side
is simply wrong by that amount - it was showing bytes ~192 instructions
into the function's real body, not its start. Confirmed and measured the
drift two independent ways: (1) `conker.us.yaml`'s uncompressed, fixed
`debugger` segment mapping (`start: 0x255880` = `vram 0x16000000`, exact -
no compression, no relocation table) gives retail's true file offset for
any `func_XXXXXXXX` name directly (`0x255880 + (vram - 0x16000000)`), and
reading that offset in `conker.us.bin` for `func_16001BB4` (`0x257434`)
lands on a legit `addiu sp,sp,-0xe0` prologue; (2) a `jal` inside the
region resolves to `0x160021FC`, matching `func_160021FC`'s *name* exactly
- confirming retail's real `func_16001BB4` is 402 words (0x648 bytes),
not the 367 our build had. **`diff.py`'s `--base-shift` flag fixes this
completely**: `--base-shift=-0x300 func_16001BB4` (plus an explicit end
address in the *current*-image address space, since `--base-shift` moves
only the base/retail side) gives a real, readable, aligned diff. This
`-0x300`/`vram-formula` trick is the same class of fact
`match_progress.py` already encodes (it reads ground truth from the
name-implied VRAM offset precisely to be drift-immune) - worth reusing
`--base-shift` explicitly next time any of the other still-short debugger
functions (or their downstream neighbors) look similarly nonsensical when
diffed directly.
- **Traced the aligned target assembly end-to-end** against the current
  C source: every block (the literal-text copy loop, the `%`-flags
  `strchr` loop, `*`-vs-digit-loop width/precision parsing x2, the
  length-modifier `strchr` + `ll`->`L` check, all 6 padding-emission
  do-while loops plus the 3 single-shot `unkC`/`len`/`unk1C` copies, and
  the final `flags&4` pad_total block + loop-back) matches our C
  structure block-for-block. One genuine bug found in that trace, not
  just a byte-matching nicety: **retail passes `&arg3` (the address of
  the local `s32 *arg3`, `addiu a1,sp,0xec`) to `func_160021FC`, not
  `arg3`'s value** - our call site was
  `func_160021FC(&st, arg3, *scan, buf)`. Since `func_160021FC` is a
  hand-rolled va_list walker (confirmed in an earlier session: it must
  consume the actual `%d`/`%s`/`%f` value argument, not just the
  `*`-width/precision case `func_16001BB4` already handles inline), it
  needs to advance the caller's va_list pointer *through* that address,
  which our old value-passing call could never let it do - a real
  functional bug for any multi-argument format string, independent of
  matching. **Fixed**: `func_160021FC(&st, &arg3, *scan, buf);`. Verified
  safe (taking `&arg3` forces the compiler to treat `arg3` as
  memory-resident/reloaded-after-calls, which is exactly the standard C
  semantics needed here since `func_160021FC` is opaque `GLOBAL_ASM`).
- **Measured effect via `tools/match_progress.py`** (confirmed this is
  the right tool for future sessions - it independently reimplements the
  same name-implied-VRAM-offset technique, no need to hand-roll it again):
  `func_16001BB4` went from 367 words/365 diffs to **369 words/360
  diffs** against retail's true 402-word length - real, verified
  progress, zero regressions (`445/1558` byte-exact overall, unchanged;
  the tool's drift-immunity means resizing a still-`diff` function can't
  regress an already-`exact` one).
- **Remaining ~33-word gap, characterized but not closed**: retail keeps
  `total` in a stack slot (`0xd4(sp)`, reloaded+stored around every
  `arg0()` callback invocation and every early return) for the *entire*
  function, where our version keeps it in a register (`s4`) throughout -
  worth ~9 words (2 per accumulate site x9 call sites: the literal copy
  plus the other 8 emission blocks) if reproduced. This is almost
  certainly a **register-pressure spill**, not a source-shape choice:
  retail simultaneously keeps `a3`=fmt, `s3`=dest, `s4`=callback,
  `s5`=`D_16003C94`, `s6`=`D_16004804`, `s7`=`D_16003C70`, `s8`=10 all
  live across the whole function (7 hoisted constants/params) plus
  `s0`-`s2` for loop temps - all 9 callee-saved slots claimed, leaving
  none for `total`. Our version doesn't hoist `D_16003C94`/`D_16003C70`
  nearly as aggressively (saw redundant `lui+addiu` re-materializations
  of `D_16003C94`'s address at at least 2 call sites where retail reuses
  a single hoisted register) - so counterintuitively, *fixing* that
  particular inefficiency would shrink us further from retail, not grow
  us; the two effects are presumably related (whatever source shape
  forces retail's compiler to hoist all 7 constants across the whole
  function is probably the same shape that would also evict `total` to
  memory). Same idiom-hunting problem class as the still-open
  `func_1600160C` multiply-scheduling and `func_16002D2C`
  unfolded-(s16) cases - not attempted further this session; next
  attempt should try increasing the *simultaneous* live range of the
  three global-pointer constants (e.g. referencing all three, or `st`'s
  fields, in a way that discourages per-use rematerialization) rather
  than touching `total` directly.

**Update (2026-07-15, eleventh session part 3 - THE BLOCKING IDIOM IS
CRACKED; func_16002D2C byte-exact; func_160033A8 structurally rebuilt.)**

- **The unfolded-(s16) idiom, solved**: retail's `li 2; sll 16; sra 16`
  pairs come from **`return (s16) (cond ? 2 : 1);`** - IDO 5.3's cfe
  lowers a cast-of-ternary by converting **each arm at its own definition
  site**, and uopt never constant-folds those conversions. Every
  plain-variable form (s16 local, s32 + cast, two returns, if/else arms)
  gets folded to `li v0,N`. Corollary discovered on the same function:
  reading `arg1[0]` directly everywhere (no `val` local) is also required
  - CSE supplies the single lhu in a2, while a named u16 local flips the
  a2/v1 register assignment or materializes a spurious `andi 0xFFFF`.
  With both, **func_16002D2C is byte-exact (46/46)**. Committed.
- **Ruled out compiler differences definitively**: IDO 7.1 (fetched
  decompals ido-static-recomp, user-approved) produces an in-place
  `sra a2/sll a2/sra a2` entry conversion that contradicts retail's
  three-register form - the file is IDO 5.3. `-cckr` produces `srl` for
  the u16 exponent shift where retail has `sra` - the file is ANSI mode.
  `-O1` bloats everything ~35%. So: **5.3, ANSI, -O2, as configured.**
- **New idiom catalogue from func_160033A8** (all verified against the
  retail listing, function now 159/170 words with a fully-matching entry
  and radix-selection region): `u8`-typed parameters produce the entry
  `andi 0xFF` + home-slot store (same convention as func_16002DE4's known
  signature); `pos -= 1` instead of `pos = 23` keeps the buffer index a
  register expression (a constant assignment folds the store into a fixed
  sp offset, retail computes base+index); the radix selection is
  `if (c=='o') radix = 8; else radix = (c!='x' && c!='X') ? 10 : 16;`
  (outer if/else + NEGATED inner ternary - arm order follows source
  order); `uvalue % radix` / `uvalue / radix` with **no (u32) casts**
  (s32 radix promotes to s64 with sign-extension: `sra a2,t1,31` before
  __ull_rem/__ull_div); the loop re-reads `arg0->num.value` into `value`
  each iteration (reuses value's stack slot as the lldiv argument).
  Remaining delta is pure register allocation (retail: &buf in s2, radix
  spilled to 0x70; ours: radix in s2, buf sp-folded) - an explicit bufp
  local didn't change it; parked with a detailed comment in the source.
- Fast iteration harness for single-function experiments (compiles one
  file with exact project flags, diffs one function against retail bytes
  positionally): `scratchpad/quicktest.sh` - recreate from the session
  transcript if needed; ~5s per experiment vs ~40s full make.

**Update (2026-07-15, eleventh session part 2 - the %-engine's blocking
idiom identified and characterized; func_16002D2C structure verified).**
Worked `debugger_257350.c`'s five size-wrong functions. Results:

- `func_16002D2C` (the IEEE-double exponent classifier): full structural
  rematch - the entire lower half (normal/zero/negative-exponent paths)
  is now instruction-exact, 41/46 words. The remaining 5-word deficit is
  ONE compiler idiom, precisely characterized and (so far) uncrackable:
  in the Inf/NaN branch retail emits an **unfolded (s16) conversion of a
  constant** (`li v1,2; sll v0,v1,16; sra t4,v0,16`) eagerly after each
  of the two `ret = 2` / `ret = 1` assignments, plus a dead `li v1,1`
  from beqzl delay-slot duplication. Our IDO 5.3 always either folds the
  conversion into `li v0,2` or elides it as a no-op. Tried and ruled out:
  plain s16 local, reusing `exp` (s16) or `val` (u16, lhu-tainted web),
  s32 + explicit `(s16)` cast, single-return phi (produces ONE merged
  conversion with bnezl tests - closest shape so far), two returns,
  if/else arms, `-O1` for the file (everything bloats ~35%, definitively
  wrong - the file IS -O2), `-cckr` (+1 word, wrong shape). The debug ROM
  (Oct 2000) contains this function **word-for-word identical** to retail
  US (found at ROM 0x1936FC by scanning for the 0x7FF0 mask), so the
  codegen is deterministic, not a build fluke. Whatever the source does,
  it defeats uopt's constant folding through the phi web - suspect an
  interaction with something else in the original translation unit.
- `func_1600288C` (the %f/%e/%g formatter, 296 insns): diverges at the
  prologue itself - retail uses frame 0xD8 saving s0-s5, ours 0xF8 saving
  s0-s6, i.e. our decompiled C keeps at least one more value live than
  the original. Deep restructure needed, not a local tweak. Parked.
- The other three (`func_16001BB4` -0x8C, `func_16002DE4` +0x78,
  `func_160033A8` -0x44) share the same s16-heavy engine style and likely
  the same idiom problem; not attempted this pass.
- Practical note for whoever resumes: rebuilding this file requires
  `rm build/src/debugger_257350.c.o` when experimenting with per-object
  Makefile flag overrides - make doesn't rebuild on flag changes.

**Update (2026-07-15, eleventh session - six debugger functions matched
byte-exact; debugger overlay code-drift eliminated through 0x16001BB4).**
Matched, all verified 0 real diffs at their name-implied retail bytes:

- `func_16001700` / `func_16001830` / `func_160018BC`
  (`debugger_256F80.c`): retail is compiled from **stock libultra
  controller source**, not the ects_proto decompiler shapes -
  `func_16001830` is `__osContGetReadData` (the by-value
  `__OSContReadFormat requestformat = *(__OSContReadFormat *)ptr;` struct
  copy through a stack temp is what generates the lwl/lwr pairs),
  `func_160018BC` is `__osPackReadData` (stack-resident template struct
  copied per controller with swl/swr; note its zero-fill covers all 16
  OSPifRam words including pifstatus, one more than stock libultra's
  ramarray-only loop - hence `ARRLEN(ramarray) + 1`), and `func_16001700`
  is a synchronous osContInit-style poll. Two hard-won idioms in 1700:
  the 0xFF fill loop only matches as an **indexed do-while reusing the
  busy-wait counter variable as the index** (`t = 0; do { ((u32 *)
  &__osContPifRam)[t] = CONT_CMD_NOP; t++; } while (t < ...)`) - a
  pointer-walk version CSEs `&__osContPifRam` into a1 across the loop,
  the pifstatus store, and the following call (2 insns shorter than
  retail, which rematerializes the address each time), and an indexed
  for-loop with a separate `i` gets unrolled 4x. Reusing `t` also puts
  retail's `move s0,zero` reset in the jal delay slot exactly.
- `func_16001678` (`debugger.c`): retail is **void** - the old
  `u32`-returning version cost exactly 4 extra insns (merged-exit `move
  v0`/`addiu v0`/second `jr` block) and was the sole source of the +0x10
  text drift that had shifted everything from `func_160016F4` to
  `func_16001B00`. Sole caller `func_16000B14` clobbers v0 immediately
  (verified in the asm), so the return value was fiction. Also `>> 1` on
  `D_160038A8` is arithmetic (s32), not the old `(u32)` cast's srl.
- `func_1600160C` (`debugger.c`): matches only as sequential
  compound-assignment statements accumulating into `pos` (`pos >>= 2;
  pos *= D_160038A8 << 1; pos += ...; pos += ...; pos += 0x10;` then
  `return D_8002AAE8[D_16003888] + pos;`). Three separate IDO behaviors
  had to be steered: parens do NOT stop reassociation of integer `+`
  (needed the named-variable accumulation to force `addu v1,v1,x`
  chains), `* 2` gets hoisted out of a multu into a post-mflo `sll` but
  **`<< 1` stays inline as the multu operand**, and reusing `pos` itself
  (rather than a fresh `off`/`stride` local) is what lands the retail
  register assignment.
- `func_16001B34` (`debugger_257350.c`): **it's a true varargs function**
  - `s32 func_16001B34(u8 *arg0, u8 *arg1, ...)` with
  `va_start(ap, arg1)` passed straight to `func_16001BB4`. This is the
  final word on the two-session 4-vs-5-argument saga: IDO's varargs
  codegen homes all four register args at entry (frame 0x20, args at
  0x20-0x2C, reloads a1/a2 from home slots for the call), which neither
  K&R definitions nor address-taken params reproduce (both were tried
  and produce the old 13-diff shape). The va_list == `&arg2` home slot,
  so callers passing the `%f` f64 need no prototype tricks at all -
  though `functions.h` still deliberately omits the prototype (now
  merely optional rather than load-bearing; could be added back as
  `(u8 *, u8 *, ...)` if wanted).
- `func_16001B00` (strlen): confirmed already byte-exact - the "3 diffs"
  in the previous session's list was stale.

**Current debugger overlay state**: zero code drift from 0x16000000
through `func_16001BB4`'s start; every function before it is either
byte-exact or (for `func_16001044`, 146 diffs, correct size) content-only.
Remaining -0x60 data-section displacement (rodata linked 0x60 low, so any
function referencing `D_16003xxx`+ shows a few phantom %lo diffs -
including the GLOBAL_ASM ones, which proves it's placement not code) is
fully accounted for by five size-wrong functions in `debugger_257350.c`:
`func_16001BB4` (-0x8C), `func_1600288C` (+0x8), `func_16002D2C` (-0x14),
`func_16002DE4` (+0x78), `func_160033A8` (-0x44). Match those five and the
whole overlay's data heals. Verification script recreated at
`diffcheck.py` (see 2026-07-15 method note; now drift-aware: compares
built words against retail bytes at the **name-implied** address).

**Update (2026-07-15, tenth session continued - func_16001B34 fixed,
func_16001044 safely re-converted).** Followed up on the tenth session's
"net wash" ending by tackling its top recommended next step: found and
fixed the actual root cause of `func_16001B34`'s 4-vs-5-argument gap.
**The fix was the opposite of what two sessions of notes assumed**:
`func_16001B34` itself does NOT need a 5th parameter - ground-truth bytes
read directly from its own name-implied address (`0x16001B34`, immune to
build drift) confirm retail's real implementation is exactly the
already-existing 4-parameter, 22-word, 32-byte-frame shape. The 5th
argument (the `f64` every caller passes via `sdc1` to the stack) relies
entirely on the standard MIPS O32 ABI shadow-space convention: it lands
at a fixed offset immediately after `arg3`'s spilled home slot "for
free," where `func_16001BB4`'s hand-rolled va_list walk (`&arg2` onward -
confirmed by that function explicitly advancing its `s32 *arg3`
parameter through memory as it parses each `%`-specifier) finds it
without `func_16001B34` needing to reference it at all. **The actual fix
was at the call site**: removed `func_16001B34`'s prototype from
`functions.h` entirely so the compiler doesn't reject a 5th argument
against a 4-param signature, relying on implicit per-call-site
declaration (same class of trick already used elsewhere in this
codebase). Re-enabled `func_16001044` with the corrected 5-argument
float-mode call - **reached retail's exact word count (155/155)** for
the first time, confirmed via `nm` that this introduces zero symbol
drift, and confirmed via the three independently-verifiable functions
(`func_16000424`/`func_16000058`/`func_16000000`, all 0 diffs) that nothing
regressed. `func_16000590` was also retried (now calling a working
`func_16001044`) but still falls 1 word short for an unrelated reason (a
loop-exit-condition codegen quirk, two different loop restructurings
both failed to close it) and demonstrably still cascades if left in
(confirmed by re-testing), so it stays reverted - only `func_16001044`
is now live. Net new state: **debugger 126/173 byte-exact** (up from
172 total functions to 173, `func_16001044` itself not yet byte-exact at
151/155 remaining diffs, but structurally safe and a real net conversion
gain with zero collateral damage - unlike the immediately-prior attempt
this same session, which had none). See Session log for full detail.

**Update (2026-07-15, tenth session - "continue function," net result: a
wash, but valuable lessons captured).** Resumed the debugger raw-asm-to-C
backlog from two sessions ago (`func_16000F8C`, `func_160006CC`,
`func_160014F0`, `func_16000590`, `func_16001390`, `func_16001044`,
`func_16000B14`, `func_160021FC`). Converted 5 of them
(`func_160014F0`, `func_16001044`, `func_16000590`, `func_16001390`,
`func_160006CC`) - all logically verified correct against the raw asm -
but **none reached retail's exact word count**, and since `debugger.c`'s
`D_1600xxxx` globals are embedded *inline in the .text segment* (not real
`.data`/`.rodata`, confirmed via `nm` showing type `T`), any function
short by even one word shifts every symbol after it, which broke several
already-matched functions' data-symbol addresses - the same drift
mechanism as two sessions ago, this time worse (debugger's byte-exact
count fell from 128/172 to 9-11/17x at the low point). **Reverted all 5
new conversions back to `GLOBAL_ASM`**, keeping the verified-correct C as
commented-out drafts directly above each pragma (matching this file's
existing convention for `func_1600078C`/`func_16000F8C`) - confirmed via
the two functions with independently-checkable ground truth
(`func_16000424`, `func_16000058`, back to 0 diffs) that this fully
restored the pre-session baseline (`make match-progress` confirms
exactly 128/172, 74.42%, matching before this session started).
**Net effect: zero new byte-exact conversions, but the session banked
real, reusable findings** - see Session log for the full blow-by-blow,
including a firm empirical rule (every converted function's word count
must match retail exactly or it cascades), a fix for `func_16001044`'s
biggest single contributor (a `memcpy()` call that should have been an
inline copy loop), and a discovered blind spot in the `dump_func.py`
verification tool (falls back to untrusted `progress.csv` addressing for
any function whose `.s` file no longer exists, i.e. anything converted
more than ~2 sessions ago - this produced a scary-looking but false
"34/34 words differ" reading for `func_160012B0` that had nothing to do
with this session's changes). Didn't reach `func_16000B14`/
`func_160021FC` (the two largest remaining) - next session should start
there, or finish `func_16001B34`'s missing 5th (`f64`) argument first
(it's what's blocking `func_16001044`'s float-mode path from reaching
exact word count, and by extension everything that calls it).

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

### 2026-07-15 (tenth session, continued - func_16001B34's real fix)

- Picked up the tenth session's #1 recommended next step immediately
  (same conversation, user pointed at the exact "Current focus" bullet).
- **Read the strings at `D_160047E8`/`D_160047F0`/`D_160047F4` directly
  from the pristine ROM** (same address-computation technique as
  `dump_func.py`) instead of continuing to guess at their role:
  `D_160047E8` = `"%s%s%f"` (an actual printf-style format string!),
  `D_160047F0` and `D_160047F4` both point to **empty strings** (`"\0"` at
  their exact address, not the `"hlL / +-#0"` table text that happens to
  sit a few bytes further along - that table is a shared internal
  constant used by `func_16001BB4`'s parser, unrelated to what these two
  pointers are passing). This immediately explained the calling
  convention: `func_16001044`'s float mode is effectively calling
  something like `sprintf(buf, "%s%s%f", "", "", value)` - two empty
  decoration strings around the float, not three independent format
  strings as guessed two sessions ago.
- **Confirmed `func_16001BB4` (`debugger_257350.c`, already marked
  NON-MATCHING/ported-from-ects, 367 words) is a genuine hand-rolled
  vsprintf-family implementation**, not just format-string-shaped code:
  it takes `s32 *arg3` as a value pointer and *explicitly advances it
  through memory* (`arg3 = (s32*)((u8*)va + 4)`) as each `%`-specifier is
  consumed - a real, manually-implemented va_list walk. This is the key
  fact that resolved the whole mystery.
- **First attempt (wrong): extended `func_16001B34` to a 5-parameter
  signature** (`u8*, u8*, s32, s32, f64`), matching the naive
  "just add the missing argument" instinct. Compiled fine, but checking
  its own ground truth (see below) proved this was structurally wrong.
- **Ground-truth check that overturned the assumption:** `func_16001B34`
  has no `.s` file (already C, ported from ects_proto, never
  `GLOBAL_ASM` in this repo) so `dump_func.py` can't verify it via the
  trusted path - worked around this by computing its ROM offset directly
  from its own **name-implied address** (`0x16001B34`, the same trick
  used for the RNG functions two sessions ago: `func_` names encode the
  real retail address, immune to any build-time drift regardless of
  whether a `.s` file still exists) and reading 22 words directly out of
  `conker.us.bin`. Result: retail's real implementation is a plain
  32-byte-frame, 4-parameter function - **no 5th-argument handling
  anywhere in it**. This directly contradicted the just-written 5-param
  version.
- **Reasoned out why from the MIPS O32 ABI itself:** a callee's incoming
  register arguments (`a0`-`a3`) get 16 bytes of "shadow space" reserved
  at a fixed offset in the caller's frame; a 5th+ argument sits
  immediately after that shadow space, at a **predictable, fixed offset
  relative to the callee's own stack pointer once its frame is
  allocated** - and critically, that offset turned out to be exactly 4
  bytes past `arg3`'s own spilled home slot. Since `func_16001BB4`'s
  va_list walk starts at `&arg2` and advances 4 bytes at a time,
  **the 5th argument (the double) lands exactly where the walk would
  find it without `func_16001B34` ever needing to name or reference it
  as a parameter.** Reverted the 5-param signature back to the
  confirmed-correct 4-param one.
- **The real fix: remove `func_16001B34`'s prototype from
  `functions.h` entirely.** With no prototype visible, each call site
  gets an implicit (K&R-style) declaration and the compiler doesn't
  reject a 5th argument - it just loads/stores whatever's provided per
  the standard calling convention, which places it at the correct ABI
  shadow-space-adjacent offset regardless. Verified this doesn't change
  `func_16001B34`'s own compiled bytes at all (word count still exactly
  22, matching the name-implied ground truth) - only affects how far
  *callers* are allowed to reach.
- **Re-enabled `func_16001044`'s draft** with the corrected float-mode
  call (`func_16001B34(buf, D_160047E8, D_160047F0, D_160047F4, (f64)
  f)`, 5 real arguments instead of the earlier session's 4-arg
  workaround that silently dropped the double). Result: **155/155 words
  - exact word count**, the first time this function has reached it.
  Confirmed via `nm` that `D_16003888`/`D_160038A8` (the drift canaries
  from two sessions of this saga) stayed at their correct addresses, and
  via the three functions with independently-checkable ground truth
  (`func_16000424`/`func_16000058`/`func_16000000`) that nothing
  regressed (all stayed at 0 diffs). `func_16001044` itself is NOT yet
  byte-exact content-wise (151/155 words still differ - register
  allocation/scheduling throughout, not a structural problem) but that's
  now a normal "needs a future matching pass" function rather than an
  active liability.
- **Tried re-enabling `func_16000590` too** (calls `func_16001044`,
  including its now-working float-mode path) - still 78/79 words, a
  *different*, unrelated 1-word gap (retail materializes its final loop's
  `i<16` exit condition into a register via a standalone `slti` before
  the branch; neither a plain `for` nor a `do-while` restructuring
  reproduced it). **Confirmed this single word DOES still cascade**
  (`func_16000424` etc. dropped back to real diffs with it enabled) -
  reverted it again, draft preserved as a comment noting the float-mode
  blocker is now resolved so only the loop-shape issue remains.
- **Final state, rebuilt and reconfirmed:** `func_16001044` live and
  word-count-safe; `func_160014F0`, `func_16000590`, `func_16001390`,
  `func_160006CC` still reverted (drafts preserved) for the reasons
  logged in the prior entry, now updated where they mentioned the
  `func_16001B34` gap as blocking (it no longer is - only their own
  independent loop-shape/codegen issues remain). `make match-progress`:
  debugger 126/173 (total functions 172→173 for `func_16001044`, exact
  count 128→126 since it's not yet byte-exact itself - a real, safe net
  gain, not a regression). Project total 547/1557.

### 2026-07-15 (tenth session - debugger conversions attempted and reverted)

- Resumed from the eighth session's deferred list. Set up `mips_to_c`
  again (`python3 tools/ctx.py .../debugger.c` - context regeneration is
  cheap, not committed, same as before).
- **`func_160014F0` (glyph blitter, 71 words)** - straightforward 8x8
  bitmap font blit using `D_16003CE0` (newly declared: 768-byte font
  table, 96 printable-ASCII glyphs × 8 bytes, size matches
  `match-progress`'s previously-unexplained `D_16003CE0 (debugger, 192
  words)` entry exactly) and the current color `D_1600388C`. Converted
  cleanly, logic verified correct, but landed at 70/71 words. Tried
  matching retail's apparent 4x-unrolled inner loop explicitly (writing
  the C with 4 statements per iteration instead of a plain 8-iteration
  loop) - **made it worse** (71 diffs instead of ~65) - reverted that
  specific attempt back to the plain loop. Ultimately reverted to
  `GLOBAL_ASM` entirely once the cascading-drift problem was understood
  (see below) - draft kept as a comment.
- **`func_16001044` (number formatter, 155 words) - the big one, and the
  main source of this session's problems.** Hex/decimal/float display
  routine called by many other functions. Fixed a real, independent bug
  while establishing its signature: `functions.h` had NO prior
  declaration for it, and its return value is never used at any call
  site, confirmed `void`.
  - Hex mode and decimal mode (with correct leading-zero suppression -
    always show the units digit, suppress leading zeros before the first
    nonzero digit) were straightforward once traced fully from the raw
    asm.
  - Float mode depends on `func_16001B34`, whose *current* 4-param
    signature (`u8*, s32, s32, s32`) is already known-incomplete (flagged
    two sessions ago) - it needs a 5th `f64` argument that the retail
    call site clearly passes (visible in the raw asm as an `sdc1` store
    to the outgoing stack argument area) but the existing implementation
    in `debugger_257350.c` doesn't accept. Wrote the call with the 4
    params it currently supports (dropping the double) - compiles, but
    is known-functionally-wrong for float display and was always going to
    be short some instructions.
  - **First compile came in at 139/155 words - a 16-word deficit, way
    more than the float-mode gap alone could explain.** Root cause:
    `memcpy(sp78, D_16003B50, sizeof(sp78))` compiled to an actual `jal
    memcpy` library call (5-ish setup words) instead of retail's inlined,
    unrolled 10-word struct copy (the exact 3-words-per-iteration pattern
    visible in the original raw `.s` - this project's `D_16003B50` is a
    10-entry table of descending powers of ten, `[0]`=1 (units) through
    `[9]`=1000000000, used for decimal digit extraction). **Fixed by
    replacing the `memcpy()` call with an explicit `for` loop** copying
    element-by-element - IDO inlined that as expected, closing the gap to
    152/155 (only 3 words short, all attributable to the func_16001B34
    gap). **Lesson: never reach for `memcpy()`/library calls for small
    fixed-size copies in this codebase - write the loop explicitly, IDO
    won't auto-recognize the copy pattern and will emit a real call
    instead of inlining.**
- **`func_16000590`/`func_160006CC` (2 more, both callers of
  `func_16001044`)** - converted following the same tracing process.
  `func_16000590` reads `arg0` at struct offset `0x12C` - beyond
  `struct118`'s currently-known size (`0x128`) - used a raw pointer cast
  instead of extending the struct (matches the "crazy struct offset"
  idiom from the project wiki's `Patterns.md`, reviewed a few sessions
  ago: don't touch a struct's shape for one field access when you're not
  sure of the full layout elsewhere). `func_160006CC` needed one
  non-obvious fix: it looked like `D_16003B48`'s initial load was pure
  dead code (immediately overwritten) so the first draft dropped it
  entirely - but retail still *performs* the dead load-and-store (visible
  as a real `lw`+`sw` pair in the raw asm), so dropping it cost 3 real
  words. Restored it as an explicit (unused-value) statement to match.
  Landed at 78/79 and 47/48 words respectively - both within 1 word,
  neither blocked by anything fundamental.
- **`func_16001390` (rectangle fill, 88 words, no existing callers)** -
  same unrolled-loop idiom problem as `func_160014F0`, landed at 82/88 (6
  short). Lower confidence throughout (parameter semantics inferred, not
  confirmed by any caller) and no caller to lose value by reverting -
  first one cut when the drift problem was diagnosed.
- **The cascading drift, diagnosed properly this time.** After all 5
  conversions, `make match-progress` showed debugger collapsed from
  128/172 to 9-11/17x, and previously-exact functions (`func_16000424`,
  `func_16000058`, `func_16000000`) were back to showing real diffs.
  Confirmed via `nm build/conker.us.elf` that `D_16003888`/`D_160038A8`
  (embedded inline in `.text`, not real data - see two sessions ago's
  writeup) had drifted again, same mechanism as before. This time
  **quantified it precisely**: summed each new function's word-count
  deficit (`func_16001044`: -16 initially, `func_160014F0`: -1,
  `func_16000590`: -1, `func_16001390`: -6, `func_160006CC`: -4) and
  confirmed the *measured* drift at any point matched the *sum of
  deficits of every not-yet-fixed function before that point in the
  file* - not approximately, exactly. This is a strong, generalizable
  diagnostic: if `D_16003888` (or any embedded-in-.text symbol) drifts by
  N words, sum your recent functions' `ours` vs. `truth` word counts from
  `dump_func.py` and it will account for all N.
  - Fixed `func_16001044`'s memcpy issue (closed 16→3), which shrank the
    total drift from -12 (after reverting `func_16001390`) down to -4.
    Fixed `func_160006CC`'s dead-code drop (closed -4→-1), shrinking
    further. At that point decided the remaining ~4-5 words (all tied to
    the `func_16001B34` gap, not independently fixable without that
    larger task) weren't worth continuing to chase live, and reverted
    `func_16001044` (and by extension `func_16000590`, which calls its
    float-mode path) and the two smaller stragglers
    (`func_160014F0`, `func_160006CC`) rather than ship a partial fix.
  - **Verification wrinkle discovered mid-diagnosis:** `dump_func.py`
    (the trusted-address tool from two sessions ago) only stays trusted
    for functions whose `asm/nonmatchings/.../<name>.s` file still
    exists. For functions converted long enough ago that the file's
    gone (e.g. `func_160012B0`, `func_16001338` - converted well before
    this whole multi-session arc), it silently falls back to the
    untrusted `progress.csv`-derived address and can report wildly wrong
    diff counts (`func_160012B0` showed "34/34 words differ" at one
    point despite being completely untouched this session - a pure
    measurement artifact from residual unrelated drift elsewhere in
    `game`/`init`, not a real problem). **When cross-checking a
    "regression," always check `dump_func.py`'s own `[address source:
    ...]` line - if it says "UNTRUSTED", that specific number is not
    reliable evidence of anything.** Confirmed the real restoration via
    the subset of functions that *do* still have accessible `.s` files
    (`func_16000424`/`func_16000058`/`func_16000000`, all back to 0
    diffs) plus the final `make match-progress` total matching the
    pre-session 128/172 exactly.
  - After reverting, confirmed clean: `D_16003888`/`D_160038A8` both
    back to their name-implied addresses, `make match-progress` reports
    debugger at exactly 128/172 (74.42%) and project total 549/1556
    (35.28%) - identical to the eighth/ninth session's ending numbers.
- **Net result: zero new byte-exact debugger functions, but the
  groundwork is banked for next time.** All 5 drafts remain as verified
  (logic-correct, word-count-close) comments directly above their
  `GLOBAL_ASM` pragmas - re-enabling any of them individually is a
  straightforward uncomment once its remaining word-count gap is closed.
  New global declarations added this session and kept (harmless whether
  the functions using them are C or asm): `D_16003CE0`, `D_16003B50`,
  `D_16003B30`, `D_160047A4`, `D_160047AC`, `D_16003B48`, `D_160037F0`,
  `D_160047E4`/`E8`/`F0`/`F4`, plus prototypes for all 5 functions and
  `func_16001B34` in `functions.h`.
- **Recommended next steps, in priority order:** (1) resolve
  `func_16001B34`'s missing 5th argument properly - this single fix
  would let `func_16001044` (and therefore `func_16000590`) reach exact
  word count, which is most of the remaining value here; (2) work out
  retail's exact unrolled-loop shape for the `func_160014F0`/
  `func_16001390` idiom (a manual 4x-unroll attempt made things worse
  this session, so the right shape isn't simply "unroll by 4" - may need
  `mips_to_c`'s own inlining/unrolling heuristics investigated, or trying
  different loop trip counts); (3) only then re-attempt
  `func_16000B14`/`func_160021FC` (the two largest, not started).

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
    sequence index plays where in-game.
- **Follow-up, same session: did the diff.** Decoded `.miniusf`'s
  "reserved" PSF section directly (not zlib-compressed despite the outer
  PSF wrapper - raw, tagged `SR64`, a flat list of `(u32 length, u32
  address, length bytes)` sparse RDRAM-write blocks; 326 blocks for
  `sparse01.miniusf`, consumed the entire reserved area with zero leftover
  bytes, confirming the parse). Extracted sequence-bank entry `[1]` from
  this repo's own `assets/rzip/assets17/0003.bin` (offset 1296, length
  30462, via its own `S1`-tagged offset table) and searched for it
  byte-for-byte in `sparse01.miniusf`'s blocks - **no match**, individually
  or concatenated, not even an 8-byte prefix. Same negative result testing
  the largest blocks (seven consecutive 4096-byte pages, clearly sample
  audio by entropy) against the raw sample bank `0002.bin`. **Conclusion:
  the USF rip holds post-processing runtime state** (decompressed
  samples/parsed sequence structures as the audio driver leaves them in
  RDRAM right before playback) **, not a copy of the ROM's
  compressed/encoded container** - different pipeline stages, won't
  byte-match by design. Updated ASSET_FORMATS.md to say so plainly so this
  specific approach isn't retried.
  - **Bonus, same investigation:** resolved the wiki's B1-header
    file-index inconsistency by just checking this repo's own extraction
    directly instead of trusting the wiki's contradictory text - confirmed
    `assets17/0000.bin` has the `B1` header (matching what
    ASSET_FORMATS.md's own §6 prose already said) and `0003.bin` has `S1`.
    Also glanced at `0004`/`0005`/`0006.bin` (144 / 17408 / 42000 bytes) -
    `0004` looks like a small table of 4-byte big-endian values, `0005` is
    mostly/all zero bytes, `0006` starts with small paired byte values
    (possibly a per-note/channel mapping) - none decoded further.

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

**Update (2026-07-16, nineteenth session - game-section candidate pass):**

- Worked the fresh game candidates from the handoff list.
  - `func_15125628`: added the missing linker symbol
    `D_800DBFF7 = 0x800DBFF7` to `conker/undefined_syms.us.txt` and changed
    the fourth cooldown decrement from `(&D_800DBFF6)[1]` to named
    `D_800DBFF7`. This is source-clearer and link-safe now. Focused raw-word
    compare reports `26 words, 16 diffs` (previous handoff target was
    `26 words, 20 diffs`). The remaining mismatch is still the IDO global
    byte load/store shape: retail uses `lbu v0,%lo(sym)(v0)` plus `sb
    ..., %lo(sym)(at)`, while current C keeps an address register and stores
    through offset zero. A volatile-cast test was worse (`34 words, 32
    diffs`) and was reverted.
  - `func_1505EEB0`: tried a retail-shaped rewrite that put the object
    pointer in `v1` and the index in `a2`, but IDO produced extra branch/store
    scheduling (`22 words, 22 diffs`). Restored the baseline source; focused
    compare is back to `18 words, 18 diffs`.
  - Stock `guMtxXFML` / `guMtxCatL`: the current source is the expected
    stock wrapper shape. Focused compare shows only callee-address drift
    (`guMtxXFML`: 2 `jal` diffs, `guMtxCatL`: 4 `jal` diffs), so no source
    rewrite was useful here.
  - `func_1504CA60`: focused compare still shows only two `jal` target diffs
    (`func_150ADA20`, `func_15058EA4`), so it remains logically complete and
    blocked on address drift.
- Verification:
  - `make build/src/game_83300.c.o build/src/game_14FF90.c.o
    build/conker.us.elf NON_MATCHING=1`
  - `make match-progress NON_MATCHING=1 LIST=1`
  - Overall byte-exact summary unchanged at `897 / 1554 (57.72%)`; game
    remains `525 / 1151 (45.61%)`, with 18 still-differ game rows.

**Continuation (2026-07-16, same session):**

- Continued smallest-first game candidates after the `D_800DBFF7` improvement.
  - `func_1504BA38`: re-tested two register-allocation nudges (`s8 *` table
    pointer form and split base+index pointer construction). The byte-pointer
    form got worse (`47 words, 28 diffs`) and the split pointer form was
    identical to baseline (`46 words, 12 diffs`). Restored the original source.
  - `func_1504C8BC`: tried a nested `if (temp != NULL) { ... } return 1;`
    shape to chase retail's entry `bnezl`/delay-slot load. It made the whole
    function worse (`76 words, 51 diffs`, baseline `50 diffs`), so restored
    the original structure.
  - `func_15125628`: explicit assignment (`x = x - 1`) generated the same
    `26 words, 16 diffs` as `x--`; kept the shorter post-decrement spelling.
  - `func_1507A3E8`: local byte temporaries loaded bytes in source order but
    worsened to `14 diffs` (baseline `13 diffs`), so restored the one-line
    expression.

**Continuation (2026-07-16, game_1944C0 small rows):**

- `func_1516968C`: tried guarded one-local and two-local byte-load rewrites to
  force retail's `*arg1` load before `arg0->unkC`. Both changed temp registers
  to `v0`/`v1` and worsened the focused compare to `4 diffs`; restored the
  original expression. Baseline remains `20 words, 3 focused diffs` here
  (two swapped `lbu`s plus the shifted `jal func_1516972C` target).
- `func_151696DC`: changed the loop from a per-iteration `slot` pointer local
  to an indexed `slots[i]` form. This keeps `arg0` in `a0` and the current slot
  in `a1`, matching retail's allocator choice. Focused compare improved from
  the noisy allocator mismatch to `20 words, 2 diffs`; the only remaining
  difference is the schedule order of `i = 0` and `slots = D_800DD198` around
  the count branch. Moving `i = 0` after `slots` or inside the branch worsened
  to `11 diffs`, so the 2-diff ordering is the keeper.

**Continuation (2026-07-16, game_77AD0 cluster pass):**

- `func_1504ADD0`: changed the local declaration layout to `s32 i;
  struct127 *obj; u8 sp48[6];`. The earlier `u8 i` form forced the loop
  counter through an `andi`; the first `s32 i` test removed that mask but left
  the stack temp at `sp+0x4c`. Moving `sp48` after the pointer gives the retail
  `sp+0x48` temp and keeps the clean signed loop counter. Linked
  `match-progress` now reports `73 words, 52 real diffs` (handoff target was
  57). Remaining shape is still a register-allocation swap (`i` in `s1`,
  object in `s0`; retail has `s0`/`s1`) plus the direct `D_800D154C` store and
  loop-bound register choice. Tried and rejected: explicit `limit = 0x19`
  (spilled the bound and moved temp to `sp+0x44`) and `register` locals
  (identical codegen).
- `func_1504AF10`: kept a signed field cast in the y-position store:
  `arg0->y_position + (s16) arg0->unk90`. Retail uses `lh` for `unk90`; the
  previous source treated the `u16` struct field as unsigned and emitted the
  large unsigned-to-float correction path. This drops the function from 118 to
  `123 words, 116 real diffs`. Reordering `sp28`/`idx` compiled identically and
  was reverted.
- `func_1504A620`: tried the tempting in-place-argument rewrite (normalizing
  `arg0` directly instead of a `mantissa` local) to chase retail's FPR layout.
  It worsened from 63 to 64 real diffs, so the original source is restored.
- `func_1505210C`: retail saves `arg1`/`-arg2` in callee-saved FPRs
  (`f22`/`f20`) across the trig calls. A small `arg1Copy` long-lived-local
  test made the function worse (`81 -> 82`), so it was reverted. Needs a deeper
  FPR-live-range rewrite rather than a simple alias.
- `func_15169070`: raw retail/current disassembly shows the C structure is
  close, but the saved-register frame is shifted (`arg2`/`arg3` in `s3`/`s4`
  current vs `s2`/`s3` retail, with `D_800DD190` address correspondingly
  shifted). No safe small source keeper found in this pass; still
  `124 words, 74 real diffs`.
- `func_1504BE2C` / `func_1504B0FC`: inspected as remaining cluster tail.
  Both are still broad allocator/control-flow problems (`191` and `664` real
  diffs respectively), not quick declaration/cast fixes.
- Verification snapshot:
  - Object rebuilds: `make build/src/game_77AD0.c.o
    build/src/game_1944C0.c.o NON_MATCHING=1`
  - Direct link used after the object build because `make build/conker.us.elf`
    tries to refresh a long libultra generated-object chain and timed out in
    this workspace: `mips-linux-gnu-ld -T build/conker.ld -Map
    build/conker.us.map -T undefined_syms.us.txt -T undefined_funcs.us.txt -T
    undefined_syms_auto.txt -T undefined_funcs_auto.txt --no-check-sections
    --no-warn-mismatch -o build/conker.us.elf`, followed by `objcopy`.
  - `make match-progress NON_MATCHING=1 LIST=1`: total `898 / 1552 (57.86%)`,
    init `223 / 232`, game `526 / 1149 (45.78%)`, debugger `149 / 171`;
    game still-differ rows are now 13.

**Continuation (2026-07-16, game_1944C0 / cluster cleanup):**

- `func_15169070`: added an intentional `u8 pad[16]` local to force IDO's
  stack frame to retail's `0x58` bytes. This aligns the homed argument offsets
  (`sp+0x58`, `sp+0x5c`, `sp+0x64`) and drops the function from 74 to
  `124 words, 67 real diffs`. A plain local array is enough; `volatile` is not
  needed. Tried explicit `arg2Copy`/`arg3Copy` locals to chase retail's
  `s2`/`s3` allocation, but that regressed the row back to 74 diffs, so only
  the padding keeper remains. Remaining mismatch is mostly saved-register
  assignment (`arg2`/`arg3` still in `s3`/`s4`, while retail uses `s2`/`s3`,
  and `D_800DD190` still lands in `s2` instead of retail `s4`).
- `func_1505210C`: tested `register` on the result locals (score unchanged)
  and on the long-lived incoming float values (`81 -> 82`, worse). Restored
  the baseline source; the retail `f20`/`f22` save shape needs a deeper
  rewrite than local aliasing.
- `func_1504AF10`: tested a signed local `yOffset` for `unk90`; worsened
  `116 -> 120`, so restored the direct `(s16) arg0->unk90` cast.
- Verification snapshot after this continuation:
  - `make build/src/game_77AD0.c.o build/src/game_1944C0.c.o NON_MATCHING=1`
  - direct `mips-linux-gnu-ld` plus `objcopy` as above
  - `make match-progress NON_MATCHING=1 LIST=1`: total unchanged at
    `898 / 1552 (57.86%)`; game remains `526 / 1149 (45.78%)` with 13
    still-differ rows. Cluster rows now: `func_1504ADD0` 52,
    `func_1504A620` 63, `func_15169070` 67, `func_1505210C` 81,
    `func_1504AF10` 116, `func_1504BE2C` 191, `func_1504B0FC` 664.

**Continuation (2026-07-16, ultralib reference added):**

- Added `decompals/ultralib` as the `tools/ultralib` submodule. This is a
  reference source tree for stock libultra/libgultra matching work (especially
  2.0L gu/math/audio/io source-shape checks), not part of the Conker game
  source build. Use it to compare rows like `guMtxXFML`, `guMtxCatL`,
  `guPerspective*`, `guRotate*`, and other libultra-derived functions before
  chasing custom C rewrites.
- Immediate comparison pass:
  - `guMtxXFML` / `guMtxCatL`: local `mtxcatl.c` matches the stock wrapper
    shape from ultralib (`guMtxL2F` -> float op -> fixed-point conversion).
    Keep the local `guMtxF2L2` call in `guMtxCatL`: retail really calls the
    second fixed-point conversion copy at `0x151EFD00`, while ultralib's
    stock source names the generic `guMtxF2L`.
  - `guPerspectiveF` / `guPerspective` and `guRotateF` / `guRotate`: ultralib
    gives the clean stock SDK source, but current `match-progress` classifies
    all six named gu rows as `BLOCK`, not `DIFF`:
    `guPerspectiveF`, `guPerspective`, `guRotateF`, `guRotate`,
    `guMtxXFML`, `guMtxCatL`. Treat these as source-complete for now; do not
    chase custom rewrites unless they reappear as real-diff rows after callee
    or layout drift changes.

**Continuation (2026-07-16, address/callee drift map):**

- Added `--explain-blocks` to `tools/match_progress.py`. With `--list`, blocked
  rows now print the address/callee pairs that explain their drift, e.g.
  `jal target current_symbol@current_vram -> retail_symbol@retail_vram`.
  This is diagnostic-only; the regular `make match-progress NON_MATCHING=1`
  summary is unchanged.
- Current blocked-row target drift is dominated by global layout skew:
  619 explained callee differences are `+0x2D0`, 161 are `+0x2C0`, then much
  smaller counts at `+0x2C4`, `+0x2CC`, and `+0x2B8`.
- The first game-section layout drift contributors, in retail order:
  - `func_1504A620`: `0 -> -0xC`
  - `func_1504ADD0`: `-0xC -> -0x8`
  - `func_1504AF10`: `-0x8 -> -0x10`
  - `func_1504B0FC`: `-0x10 -> +0x1F0` (adds `0x200`; largest local source)
  - `func_1504BE2C`: `+0x1F0 -> +0x2A8` (adds `0xB8`)
  - `func_1505210C`: `+0x2A8 -> +0x2B8`
  - `func_15055D48`: `+0x2B8 -> +0x2C0`
  - `func_150721A4`: `+0x2C0 -> +0x2CC`
  - `func_1507515C`: `+0x2CC -> +0x2D0`
  - `func_1514143C`: `+0x2D0 -> +0x2C8`
  - `func_15141928`: `+0x2C8 -> +0x2D0`
  - `func_15169070`: `+0x2D0 -> +0x2C4`
  - `func_15169850`: `+0x2C4 -> +0x2D0`
- Concrete gu examples from `--explain-blocks`:
  - `guPerspectiveF` is blocked by `guMtxIdentF@0x150A7E90 ->
    guMtxIdentF@0x150A7BC0` plus two external load/store immediate drifts.
  - `guRotateF` is blocked by `guNormalize@0x151F02C0 -> guNormalize@0x151EFFF0`,
    `guMtxIdentF@0x150A7E90 -> guMtxIdentF@0x150A7BC0`, and one external
    immediate drift.
  - `guMtxXFML` is blocked by `guMtxL2F@0x151F0188 -> guMtxL2F@0x151EFEB8`
    and `guMtxXFMF@0x151F0410 -> guMtxXFMF@0x151F0140`.
  - `guMtxCatL` is blocked by two `guMtxL2F` calls, `guMtxCatF@0x151F04B0 ->
    guMtxCatF@0x151F01E0`, and `guMtxF2L2@0x151EFFD0 ->
    guMtxF2L2@0x151EFD00`.
- Next best address-drift reducers are still the size-drifting real-diff rows,
  especially `func_1504B0FC` and `func_1504BE2C`. Fixing callers will not clear
  the 618 blocked rows while those callee/layout islands remain oversized.
- Verification:
  - `python -m py_compile tools/match_progress.py`
  - `make match-progress NON_MATCHING=1`: total `898 / 1552 (57.86%)`,
    blocked `618`, differ `36`; game `526 / 1149 (45.78%)`, blocked `610`,
    differ `13`.

**Continuation (2026-07-16, func_1504B0FC stack/call drift):**

- `func_1504B0FC`: fixed a real call-shape error at the `func_1510F820` site.
  Retail passes `arg0->pad188` in `a0`, `&arg0->unk18C` in `a1`, then the
  five output pointers; the ported C had an extra leading `var_f12` argument,
  which promoted to double and shifted the real arguments. Removing that
  argument changed the call setup to the retail register shape and reduced the
  frame from `0xA0` to `0x98`.
- Block-scoped the five temporary output floats used only by the
  `arg0->unk28 < 40.0f` branch. This moved their stack block down from
  `sp+0x74..0x84` to `sp+0x44..0x54` and moved downstream `func_1504BA38`
  from `0x1504BC28` to `0x1504BC1C`.
- Removed the dead `sp6C = var_f12` local/assignment. IDO was preserving a
  needless high stack slot; removing it drops the frame further from `0x98` to
  `0x90`. Retail is still `0x78`, so the remaining mismatch is still mostly
  stack/local lifetime and FPR register allocation, not a bad callee signature.
- Current layout after the pass: `func_1504B0FC` starts at `0x1504B0EC`;
  `func_1504BA38` now starts at `0x1504BC1C` (retail `0x1504BA38`, current
  delta `+0x1E4`, improved from `+0x1F0`). `func_1504BE2C` now starts at
  `0x1504C010`; `func_1504C078` at `0x1504C314`.
- Diff score: `func_1504B0FC` is now `591 words, 658 real diffs` (from 664).
  The global progress summary is unchanged because the function is still a
  real-diff row, but this pass reduced the local address drift by `0xC`.
- Verification:
  - `make build/src/game_77AD0.c.o NON_MATCHING=1`
  - direct link plus `objcopy`
  - `make match-progress NON_MATCHING=1`: total `898 / 1552 (57.86%)`,
    blocked `618`, differ `36`; game `526 / 1149 (45.78%)`, blocked `610`,
    differ `13`.
  - `git diff --check`

**Continuation (2026-07-16, big layout win from func_1504B0FC fallback):**

- `func_1504B0FC`: converted the current source-matching attempt to a
  relocatable `GLOBAL_ASM` fallback in
  `asm/nonmatchings/game_77AD0/func_1504B0FC.s`. The improved C body is kept
  under `#if 0` as the next rewrite baseline, but the build now uses retail
  instructions with internal branch labels and symbol-based external calls
  (`func_1510F820`, `func_1505210C`, `func_15052408`, `func_15059444`,
  `func_15060A30`, `func_1507CD64`) instead of baked absolute `jal` words.
- Size/layout result: `func_1504B0FC` now emits `0x93c` bytes, matching the
  retail size. The downstream layout jump collapsed by exactly `0x200`:
  `func_1504BA38` moved from `0x1504BC1C` to `0x1504BA28`, only `-0x10` from
  its retail address (`0x1504BA38`). Current key starts:
  `func_1504B0FC=0x1504B0EC`, `func_1504BA38=0x1504BA28`,
  `func_1504BE2C=0x1504BE1C`, `func_1504C078=0x1504C120`,
  `func_1505210C=0x150521B4`.
- Blocked-drift histogram after the fallback: 619 explained callee differences
  are now `+0xD0`, 161 are `+0xC0`, then `+0xC4` (39), `+0xCC` (10), and
  `+0xB8` (3). This replaces the old `+0x2D0`/`+0x2C0` dominant drift, so
  B0FC is no longer the global layout anchor. The next local size reducers are
  `func_1504BE2C` first, then later rows like `func_1505210C` and the smaller
  `15055D48`/`150721A4`/`1507515C` islands.
- Progress snapshot after rebuild/link: total `898 / 1551 (57.90%)`, blocked
  `618`, differ `35`; game `526 / 1148 (45.82%)`, blocked `610`, differ `12`.
  The blocked count is unchanged because those rows still have callee-address
  drift, but the dominant drift magnitude is now `0x200` smaller and the game
  real-diff queue dropped by one row (`func_1504B0FC` left C accounting).
- Verification:
  - `make build/src/game_77AD0.c.o NON_MATCHING=1`
  - direct `mips-linux-gnu-ld` plus `objcopy`
  - `make match-progress NON_MATCHING=1`
  - `match_progress.py --list --explain-blocks` spot checks on the gu rows and
    the post-B0FC cluster.

**Continuation (2026-07-16, func_1504BE2C layout island collapsed in C):**

- `func_1504BE2C`: removed the remaining major game-section size island without
  falling back to asm. Three source/type fixes did the work:
  - Added the missing `func_1507EB2C(f32)` prototype. Without it, K&R/default
    promotion made the call pass a double and emit an extra `cvt.d.s`; retail
    passes the float directly in `f12`.
  - Changed `struct127::pad54` from `u32` to `f32`, matching retail's
    `lwc1`/`swc1` half-speed update at offset `0x54`.
  - Removed the impossible extra unsigned-float correction after loading
    `arg0->unk31C->padA[1]`. IDO already emits the single unsigned-byte to
    float correction that retail has; the hand-written source was forcing a
    second guard.
  - Changed `struct126::unk14` from two bytes to a `u16` field. Retail stores
    the random offset with `sh` and copies it with `lhu` before writing
    `D_800CC2B2`; the signed divide still happens through `D_800CC2B2`.
- Size/layout result: `func_1504BE2C` shrank from `0x304` bytes to `0x248`
  bytes (retail is `0x24c`). Current key starts after link:
  `func_1504BE2C=0x1504BE1C`, `func_1504C078=0x1504C064`,
  `func_1505210C=0x150520F8`. The function is now only 4 bytes smaller than
  retail instead of `0xB8` larger, so the post-cluster drift is essentially
  gone.
- Global drift result: explained callee-address differences are now dominated
  by `+0x10` (620 occurrences), with much smaller counts at `+0x4` (39),
  `+0xC` (10), and `-0x4` (3). This replaces the previous `+0xD0` dominant
  drift after the B0FC fallback.
- Progress snapshot from direct `match_progress.py` after rebuild/link: total
  `985 / 1551 (63.51%)`, blocked `531`, differ `35`; game
  `613 / 1148 (53.40%)`, blocked `523`, differ `12`. That is +87 total
  byte-exact rows and +87 game byte-exact rows versus the B0FC snapshot; the
  still-differ queue is unchanged because BE2C still has 144 real instruction
  diffs, but it no longer blocks the large downstream callee island.
- Verification:
  - `make build/src/game_77AD0.c.o NON_MATCHING=1`
  - direct `mips-linux-gnu-ld` plus `objcopy`
  - direct `match_progress.py progress.csv build/conker.us.elf conker.us.bin`
  - `match_progress.py --list --explain-blocks` histogram. The
    `make match-progress NON_MATCHING=1` wrapper timed out in this workspace,
    but the direct summary/list command completed and uses the same rebuilt
    `progress.csv`, ELF, and BIN inputs.

**Continuation (2026-07-16, func_150721A4 asm fallback clears the last big
callee plateau):**

- `func_150721A4`: converted this 17-word wrapper to a small relocatable
  `GLOBAL_ASM` fallback in `asm/nonmatchings/game_981E0/func_150721A4.s`.
  The C body is preserved under `#if 0`. Existing notes already showed the
  source logic was right but IDO inserted three extra move/staging words:
  retail keeps `D_800D1580` in `v1`, computes `t6=v>>8` and `t7=v>>16`, then
  masks directly into `a1/a2/a3` before calling `func_1506160C`.
- Layout result: `func_150721A4` now emits the retail `0x44` bytes instead of
  the C build's `0x50`. Current key starts after link:
  `func_150721A4=0x150721A4`, `func_150721E8=0x150721E8`,
  `func_1507515C=0x1507515C`, `func_15075400=0x15075400`,
  `func_150ADA20=0x150ADA20`. This removes the `+0xC` transition that fed the
  previous `+0x10` callee plateau.
- Global drift result after refreshed progress CSVs: only 45 explained callee
  address differences remain (`40` at `-0xC`, `3` at `-0x4`, one each at
  `-0x10` and `-0x14`). The former dominant `+0x10` plateau is gone.
- Progress snapshot after object rebuild, direct link, and regenerated
  `progress.init.csv`/`progress.game.csv`/`progress.debugger.csv`: total
  `1466 / 1550 (94.58%)`, blocked `50`, differ `34`; game
  `1090 / 1147 (95.03%)`, blocked `46`, differ `11`. This is the large
  address-drift payoff from the small wrapper: compared with the BE2C snapshot,
  exact rows went `985 -> 1466` and game exact rows went `613 -> 1090`.
- Remaining game still-differ rows: `func_1516968C` (2),
  `func_151696DC` (2), `func_1504BA38` (12), `func_1507A3E8` (13),
  `func_1514143C` (14), `func_1504ADD0` (52), `func_1504A620` (63),
  `func_15169070` (67), `func_1505210C` (81), `func_1504AF10` (116),
  `func_1504BE2C` (144). `func_150721A4` left the diff queue.
