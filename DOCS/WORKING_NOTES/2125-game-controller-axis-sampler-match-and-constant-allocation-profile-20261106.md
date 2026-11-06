# Controller-axis sampler match and constant-allocation profile

Date: 2026-11-06. Continue the 80% matching goal from consumer
`45058e1fc95c46a3aa06d787048ba245b609fad9` and mounted tools
`e4405212d70fbc95f854c5b58ae89d61e5316ff8`, following
[Note 2124](2124-game-asset-block-walker-match-and-startup-selector-abi-20261106.md).

## Installed reconstruction

`func_1503F9F0`, owner `generated_6CEA0`, now matches its complete **70-word**
slot: VA `0x1503F9F0..0x1503FB08`, ROM `0x6CEA0..0x6CFB8`, 280 bytes,
leaf with no frame, eight HI16/LO16 bindings. Its supported interface is
`void(s16 slot, s16 *x, s16 *y)`. Retail stores the original argument word
in the incoming SP+0 home, then sign-extends its low half for the slot.
The recovered input header is four bytes: unsigned button half, signed X
and signed Y bytes at offsets 2 and 3. Native SDK fixtures assert the size,
offset and 32-bit pointer ABI. No additional controller fields are inferred.

The signed halfword at `D_80084484` decrements with 16-bit wrap. The routine
loads `D_800BE728`, indexes its pointer table by signed slot times four, and
loads the selected controller pointer even on a countdown-blocked call.
That last load is in the original decision branch's delay slot. When the
decrement is nonzero, it writes the countdown and clears X followed by Y.

When the decrement becomes zero, it reads the signed X byte, resets the
countdown to five, and writes X unless it is within inclusive [-20,20],
which becomes zero. It reads Y only after the X output store and applies
the same dead zone. It then clears input X and Y in order, reloads each
output halfword, and clamps it to [-1,1], X followed by Y. Those fresh reads
and ordered stores are retained for aliases. The table lookup consumes the
slot before its signed local is reused for X. No null gate or extra bounds
check is added. The neighboring reset and unfinished renderer remain intact.

## Compiler fit and guarded normalization

The ordinary source initially emitted 69 words, with countdown-address CSE
keeping a separate address register live across the branch. The local,
already supported `-Wo,-no_const_in_reg` option recovers the original direct
LUI/LH and separate branch-local LUI/SH accesses, producing 70 words.
Initializing the pad pointer before the countdown and recovering the X
local's lifetime reduce 43 differences to **nine**. The override is scoped
to `generated_6CEA0.c.o` through CFLAGS; the asm-processor still receives
its supported O2/g3 flags. Both owner neighbors emit unchanged.

Semantic C emits **61 of 70 words directly**. Nine relocation-aware guards
implement only this closed recipe; the complete raw body and all eight
bindings must match their pinned fingerprints before any recipe is derived:

| Offsets | Normalization |
| --- | --- |
| 0x08, 0x0C, 0x10 | Rotate the independent A0 sign extension after the countdown LUI/LH pair; move both bindings with their instructions. |
| 0x50, 0x58 | Move the constant five from T3 to dead V1 for its sole countdown store. |
| 0x64, 0xC4 | Move the first constant -1 from T4 to T3 through its sole X-clamp use. |
| 0xB0, 0xF4 | Move the second constant -1 from T5 to T4 through its sole Y-clamp use. |

No instruction insertion, omission, frame, branch, immediate, algorithm or
memory-order change is used. The old guard CSV prefix is retained byte for
byte and exactly nine rows are appended. Compact data is fixed; the compact
GPR mask changes from `80004006` to `A3007F7E`, independently derived from
the complete emitted body. Its other 20 metadata bytes and all padded pools
are unchanged. Do not describe the whole compact metadata as unchanged.

One packet-only Claude advisory call used disabled built-in tools and an
empty strict MCP configuration. Its proposed comparison and compound-store
changes emitted 72 and 69 words and were rejected. The supported allocation
option was found and tested locally. A response-print encoding error did
not lose the saved response or cause a second call. Codex remained the only
writer. The first full test run had one fixture API error in the independent
GNU emitter; correcting its argument list yielded a fresh complete pass,
with no C or recipe change for the fixture fix.

## Qualification

All eight pre-install checks passed in the mounted configuration and the
sibling tools overlay, then all eight passed again after installation on
both actual helper configurations. New target modules are overlaid only in
the ignored build directory; sibling tracked edits and 2,428 untracked files
are preserved. Both tools smokes are fresh. Three unchanged shared suites
per copy are explicitly reused from Note 2124 after verifying the exact
helper and test-source hashes: match-progress, word-patch padding and PC16.
They are not described as fresh sampler regression runs.

- **5,567 cases per body**, original/raw/padded: full memory and access trace,
  signed selector and raw high bits, countdown wrap, all 256 values in each
  axis, all dead-zone boundaries, saved GPR/FPR/SP and 363 aliases involving
  outputs, input bytes, globals and incoming homes.
- **59 access-cut prefixes** agree in memory/trace for all three bodies;
  retail and padded complete machine states also agree. Raw private GPR/PC
  equality is not claimed across the deliberately normalized schedule.
- All **66 reachable words** execute. A conservative branch CFG independently
  proves the four unreachable words at 0x7C, 0xA0, 0xC8 and 0xF8. They remain
  in the literal 70-word body; this is not missing coverage hidden as success.
- **144 cases per body** connect the original six-word caller window in
  `func_1503FB40`, including its output-address setup and following global
  load that overwrites V0. The parent supplies slot zero in its preceding
  branch delay. Full parent execution is not claimed; its C remains unfinished.
  Independent aligned-ROM census finds only JAL at ROM 0x6D198, no tail jumps
  or literal function pointers.
- **27 independent GNU links** exercise all eight bindings over nine separate
  global layouts and HI/LO carry edges, with 36 semantic cases per body. The
  original assembly object is assembled independently of the patch recipe.
- **786,462 native32 SDK/UBSan calls**, at O0/O2/O3, cover all 65,536 countdown
  patterns, all 65,536 axis-byte pairs, direct calls and compatible callbacks,
  legal signed-slot backing and overlapping output halves. Ten incorrect
  variants return the checked rejection code with no fault or diagnostics.
- All 280 one-byte raw corruptions, eight binding corruptions, three guard
  prefix corruptions and five whole-image corruptions are rejected. The
  former zero-return stub and wrong default compiler profile fail closed.

These qualify the routine and bounded caller window, not host controller,
camera or gameplay acceptance. The separate host port and frozen Release
artifacts were not changed.

## Actual production and continuation

Actual Make compiled the changed source once with the scoped option, then
linked the production ELF and recounted it:

```sh
make -C conker -o retail_word_patches.us.csv -o Makefile -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

The old-dependency flags avoid rebuilding unaffected owners for a shared
guard file and Makefile whose only new guard set and CFLAGS override belong
to this sampler. The changed C source still forces its real compile. The
exact CSV prefix/rows, exact Make insertion, unchanged raw+padded neighbors
and full linked-image audit cover the result. Retain **both** `-o` flags for
subsequent scoped work until a deliberate broader rebuild; do not alter
unaffected object mtimes to hide their dependency age.

The full ELF equals the independently predicted **206-byte** change with
**zero exclusions** or metadata permutations. Only this function's slot and
symbol size (12 to 280 bytes) change. All **6,052 function addresses** stay
fixed, and all **189,088 protected data bytes in 720 owners** remain exact.
Conversion rows and progress.csv are unchanged. The unfinished wider image
retains the expected checksum failure; the existing duplicate generated_12D630
recipe warning is unchanged apart from line numbers.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,194 / 5,512 (76.09%) | 0 | 1,318 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,521 / 4,839 (72.76%) | 0 | 1,318 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**216 more** matches reach the current 4,410 threshold for 80%. Fingerprints:

- ELF: `f11b4a443d5ba5673a082006f1f5e7d98babc1569dfd05629c6893354a0b4058`.
- Owner: `78295381d7f34db9bf3fc5efe4ecd108c387adb793d488e2e936b3c0c9e80dcf`.
- Code binary: `3ff8e77cf24bd200621d57a6626eb03bf881c985867d2cc797276ed9919abc61`.
- Guard CSV: `7d469fee131d8adbc169fda991046c614fea90f2704bfcd612c41371e6efa1f0`.
- Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence lives under `conker/build/game-controller-axis-sampler-1503F9F0-match/`.
Graphify receives a scoped refresh with old-node retention accounting; this
does not claim a full-corpus extraction. Tools are committed before consumer.

Next: `func_150DB518` in `generated_108320`, another 70-word routine. Inspect
its five pointer gates, signed-half sixth argument, byte seventh argument,
eighth word, partially defined effect request, original factory contract,
return use, caller homes and pointer reloads before recovery. Keep handwritten
`func_150A76F0`, private inputs/saves, unrelated work and frozen host Release
separate. The full 80% goal remains active.
