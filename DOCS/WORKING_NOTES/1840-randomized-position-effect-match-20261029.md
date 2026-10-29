# 1840: Randomized position effect match

Date: 2026-10-29. Target `func_151C56A4`, owner `generated_1F2730`.
VA `0x151C56A4..0x151C577C`, ROM `0x1F2B54..0x1F2C2C`: 216 bytes /54 words.

The zero-return placeholder becomes `void func_151C56A4(f32 *position, u8 kind,
s32 mode)`. It builds the existing six-byte `Header` and twelve-byte `Header2`:
header bytes 3/-1, unsigned first random modulo 3 plus 3 as a halfword, byte0;
three floats truncated to signed integer coordinates; a second random low bit
plus6; then `func_151602C0` with FF/E8/AB/FF/0/0/kind/mode. The factory result
is ignored. The first helper can mutate the source before coordinate reads;
the second helper runs after capture. Source uses existing types and precise
helper prototypes, with an explanatory comment. No arbitrary gameplay label.

All 54 words and all three R_MIPS_26 relocations emit directly from C using
the existing default O2/g3 profile. The original 80-byte frame saves RA at+52,
uses incoming homes +80/+84/+88 and an outgoing argument extent44. No guards,
insertions, omissions, frame adjustments, shared header edits or profile changes.
The complete guard CSV and conversion inventory CSV remain byte-identical.

Eight fresh qualification methods pass independently in each tools copy,
plus shared tools checks. Installed checks rerun two methods per copy; the six
other methods reuse only complete input/module/artifact identity.

- Guest: 7,840 cases /23,520 executions compare original, raw and padded C in
  literal registers, FP state, RAM, calls/events, access traces and HI/LO. All
  54 words execute. Cases include high-bit random values, modulo boundaries,
  unsigned kind, signed modes, signed zero/subnormals/fractional coordinates,
  signed-int boundaries and provider mutations before/after capture.
- Native32 O0/O2/O3 each pass 3,136 valid-conversion cases with UBSan and reject
  eight controls: signed remainder, wrong count/header/axis/selector/colour,
  missing draw and capture before the first helper. Nonfinite/out-of-range
  conversion uses a bounded guest sentinel model only; native undefined float
  conversions and actual hardware FCSR behavior are not claimed.
- 50 dispatched access prefixes agree in full literal state. Three independent
  layouts pass 144 rebase cases. Two original caller windows each pass48 cases:
  VA151C5358 /ROM1F2808 (4words, parent func_151C5280), and VA150288CC /
  ROM55D7C (6words, parent func_150265CC). The latter overwrites v0 with1;
  both ignore the effect result. Earlier parent gates are preconditions.
- Complete owner compilation/padding preserves seven neighbors and pools.
  Five actual Make commands reproduce the exact qualified object without C
  diagnostics. The inherited duplicate-recipe Make warning remains.
- Independent whole-image prediction equals production:156 changed bytes,
  155 target code plus one target extent, zero metadata rearrangements or
  exclusions. All 6,055 other linked bodies and all function addresses remain
  fixed. Protected Game data stays exact across189,088 bytes /720 owners.

Providers are bounded models. Their interfaces agree with the retained
`game_DAE50.c` random routine and `game_18D770.c` factory. This does not execute
the complete PRNG/factory/allocator or complete parent/gameplay paths. Header
padding byte5 is uninitialized as in retail: the known five bytes are checked;
literal guest state matches, but no portable native padding value is claimed.
The existing factory copies all six bytes; no zero initialization is invented.

Fresh actual adopted-ELF count: **3,917/5,506 (71.14%)**, Game **3,244/4,833
(67.12%)**, Init492/492 and Debugger181/181, zero drift. **213** more to4,130.
Tools commit first: `6baaf6164bc007361f387da8f719b5174f0ae6ea`. No push. Root README has aggregate changes only.

Scoped AST refresh retains or uniquely relocates all49,590 previous nodes,
preserves102,833 previous directed relationships, and retires the target's one
obsolete s32 return reference against recovered void source. Helper call edges
and original caller metadata are source/binding checked. Outside-scope manifest
rows and analytics remain historical; this is not a full-corpus extraction.

Artifacts: `conker/build/game-random-position-effect-match/`. Next screened
target `func_150B53D0` needs complete qualification. Parked private candidates remain
uncredited. Older tools mirror preserves1,958 inherited dirty paths plus three
new modules. No host-port, frozen Release, save/editor, private-input or memory
changes. Zero Claude calls. The 75% goal remains active.
