# 1745 - Vertex texture-coordinate shift guarded C match

Verified: 2026-10-27. Target `func_15116058`, owner `generated_142560`.
VA `15116058..15116110`; retail ROM `143508..1435C0`.

## Result and semantic body

Replace the zero-return placeholder with the complete 46-word /184-byte
record updater. The frame remains zero; the existing O2/g3 profile is unchanged.
This is a guarded C match: the raw semantic body has 40 word differences;
40 relocation-aware expected-word guards close register lifetimes and one
independent two-word schedule. It is not a compiler-only match.

The recovered `TexcoordShiftRecord` exposes only the count at +0x16, buffer
pointers at +0x20/+0x24 and packed offset at +0x3C. Capture both signed 16-bit
offsets before writes. For each 16-byte vertex, copy the other buffer's signed
texture-coordinate halfwords at +8/+10 with the offsets added, truncating each
store to 16 bits. The source selector is logical-not of the complete buffer
byte; the destination uses the complete byte. Preserve the selector reload
between coordinates, pointer reloads after writes, and count reload after the
second store. The explicit empty-count gate keeps cursor initialization local
to the nonempty loop. Masking the low packed halfword recovers the 46-word form.

The record fields and comment describe these measured accesses. Shared
structures, SDK headers, other function bodies and compiler flags are unchanged.

## Interface and reference boundary

The emitted routine consumes one record pointer in A0. The full aligned retail
census finds no matching pointer literal, JAL word or J word. No caller path or
unidentified dynamically constructed call is credited by this work. The
reconstruction uses `void(TexcoordShiftRecord *)` for its record effects.
V0 incidentally retains the signed high offset; raw and normalized guest cases
check that machine-visible value separately. It is not promoted to a portable
C return-value contract without a caller declaration or return consumer.

Native32 asserts the actual 32-bit record layout, 16-byte SDK Vtx size and
texture-coordinate offset +8. Native indirect calls use the typed void API.
Arbitrary buffer bytes and record/global overlap are bounded guest-machine
cases, not claims that indexing a two-element C array outside 0/1 is portable.

## Derived guard closure

The raw body SHA is pinned before deriving any replacements. Opening renames
follow each packed-word, count and shifted-halfword definition through its last
use, including the separate temporary and final V0 lifetimes. The loop uses two
closed GPR cycles, expressed as source-register to retail-register mappings:

- `3 -> 8 -> 7 -> 3` for cursor, buffer selector and logical-not temporary.
- `10 -> 15 -> 12 -> 25 -> 14 -> 11 -> 24 -> 13 -> 10` for loop temporaries.

Record A0, high offset V0, low offset A1, index A2, address T1 and return RA
remain fixed. The remaining schedule swaps the independent cursor zero and
LO16 address add at words 10/11. Move the LO16 binding from byte +44 to +40;
the HI16 binding stays at +36. No opcode, arithmetic operation, memory access,
branch destination, immediate, frame or function length is changed. Expected
words and bindings fail closed before emitting each replacement. Preserve every
old guard-manifest byte and append exactly 40 target rows.

## Qualification

Both tools copies execute eight fresh canonical methods with zero errors,
failures or skips. Primary execution is 8.002s; the mirror's exact receipt is
retained in the ignored stage. Both `check_project_tools.py` checks pass.

- 356 guest cases cover empty and nonempty loops, signed halfword boundaries,
  wrapping stores, two stack phases and all 256 buffer bytes. Every original
  word is visited. Raw C agrees on memory and incidental V0; the normalized
  body agrees on complete private machine state.
- 48 alias cases cover nine layouts: equal/overlapping vertex buffers, a count
  overwritten by either coordinate store, packed offsets overwritten after
  capture, selector changes between coordinates, and pointer changes after
  a halfword store. Required live reads remain observable.
- Native32 O0/O2/O3 each pass 540 positive cases, including counts 0x7FFF,
  0x8000 and 0xFFFF, valid overlapping vertex arrays, typed indirect calls,
  trapping UBSan and eight effective functional negative controls.
- 76 access-fault prefixes fire. Empty input needs only the packed word and
  count mapped. Three large unsigned-count prefixes prove a first iteration;
  full large-count completion is exercised natively. Fault semantics are guest-only.
- Four actually compiled guest negatives reject cached selector, cached count,
  cached destination pointer and XOR source selection. The first negative suite
  failed because the cached-count mutant's extra iteration corrupted a pointer
  and reached unmapped memory. Its bounded witness now keeps that pointer valid
  and produces an ordinary wrong-memory result; candidate source is unchanged.
  The failed receipts remain in `failed-canonical-v1/`; the accepted suites are v2.
- All 46 raw-word corruptions, all 40 actual padder guard-row corruptions and a
  wrong binding are rejected. Six independent GNU links across three layouts
  preserve both HI16/LO16 bindings and signed-low carry, with 12 rebased guest cases.
- Seven whole-image corruptions and three wrong-input cases are rejected.

The copied complete owner preserves all 83 neighbors, its pools and ten
GLOBAL_ASM routines. The actual five-command Make recipe reproduces all 84
compact functions and the complete padded object. Each tools copy then runs two
fresh installed owner/image methods and reuses six semantic methods only after
module, frozen-input, raw/Make artifact and sealed-input fingerprints agree.
Unchanged broad neighbor suites are retained receipts, not freshly rerun tests.
No emulator, R4300 hardware, rendering or gameplay acceptance is claimed.

## Production, image and actual recount

Ordinary production Make passes, preserving the inherited duplicate
`generated_12D630` recipe warning. The entire ELF equals the independently
predicted predecessor with exactly 138 target code bytes and one target
symbol-size byte changed: 139 total, zero exclusions or serialization allowance.
All 6,056 function addresses and 6,055 other bodies remain fixed. Protected Game
data is exact across 720 owners /189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

All 107 focused inputs and 16,152 sealed Native/cache files are audited with
five declared source/guard/object/ELF/map adoption paths. The conversion CSV is
unchanged; the old guard prefix is unchanged and 40 rows are appended. Two
inherited receipt labels saying the guard manifest was unchanged were corrected
to this explicit prefix-and-append statement, with prior receipt hashes retained.

The actual captured, adopted Native ELF recount is 3,822/5,506 exact (69.42%):
Game 3,149/4,833 (65.16%), Init 492/492 and Debugger 181/181. Zero address drift;
1,684 C functions still differ. The 75% threshold remains 4,130 exact functions,
308 more. Remaining source-shape triage is 1,555 placeholders, 120 semantic/other
and nine unlocated entries; shape classification alone gives no matching credit.

## Checkpoint and reproducibility

Baseline consumer `6017864be30c3e367bdaf0cc0ce6da9e809b1957`; tools
`dab739dda5fa3c40fa69da2420611a54d4e5a0b1`. Tools are banked first in
`3d000d5fe836ae8fcf10706a8a408db021b9f46a`, then pinned by the consumer.
Preserve the older mirror's 1,700 inherited dirty paths plus this target's two
new files; do not reset it or duplicate its history. Nothing is pushed.

- Snapshot SHA: `3850f9037183934a33b3bea9b189db221ac883b430ff06ec8eea39a3d83c252e`.
- Raw body SHA: `4038e27a208a573949810c3baf0f1a75c3ae1513dc422a1d975853e1b06cef40`.
- Padded object SHA: `eff434ec09e76e78c959d31944e4aa3db6f0640eba9d50091ecb8017860ddb59`.
- Adopted ELF SHA: `53f02cac34ee5d56ed2f09b86f5e4b09ed5e0f9d9e098c1d453db5567dac10e1`.
- Reproduce: `python3 -m unittest tools.tests.test_game_vertex_texcoord_shift_match -v`
  from the prepared consumer/cache. Ignored evidence lives in
  `conker/build/game-vertex-texcoord-shift-match/`; every execution gets a fresh
  PID-specific directory. Rejected source/profile experiments remain uncredited.

Codex owns implementation and validation; routine Claude budget is zero calls.
Refresh changed-source Graphify with checked node/relationship retention and no
full-corpus extraction claim. The 75% goal stays active. Next screened placeholder
`func_1519E304` in `generated_1CA420` (46 words) requires its own full gates.
