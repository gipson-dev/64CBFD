# Text-buffer fade guarded match and compiler lifetime recovery

Date: 2026-11-06. Continue the 80% goal from consumer
`af352ae25dda412dca21b43c8f1504d0fdb5fc05` and mounted tools
`05f9b8333a87893ab4fc262eb1829093d71778ba`.
This completes the unresolved target in
[Note 2117](2117-game-text-buffer-fade-semantic-recovery-and-private-home-boundary-20261106.md).

## Result and source contract

`func_150D01A0`, owner `generated_FC5F0`, is now matched across its complete
69-word / 276-byte slot: VA0x150D01A0..0x150D02B4,
ROM0xFD650..0xFD764, frame0x30, S0/RA homes0x18/0x1C,
incoming owner home0x30 and second descriptor-pointer home0x20.
The raw semantic C has six scheduling differences; six expected-word guards
produce all original words. There are no frame/size guards or inserted words.

The callback retains its original `s32(u8 *)` type and returns1. Active mask1
resets the signed payload countdown to8. Positive counts produce byte
opacity `count * 31`, inverse255-opacity, and decrement by the live tick word
modulo256. Nonpositive counts use opacity0/inverse255. The inverse pass draws
the live indexed buffer, and the opacity pass draws index XOR1. Both use
color206/196/97 and text coordinates146/190, mode129. Unsigned subtraction
before byte truncation avoids signed-overflow assumptions for extreme ticks.
The source uses the existing descriptor type and descriptive first/second
pointer names. The indexed formal-address expression preserves the observed
owner-home reloads; it is a compiler fit, not proof of original spelling.

## Measured compiler cause and six-word schedule

Qualified CFE/UOPT/UGEN captures use only newly owned compiler children,
normal O2/g3, exact cc/cfe/uopt/ugen fingerprints, actual intermediate paths,
fired probes, completed producer/consumer/driver exits and unchanged complete
emitted text/bindings/pools. Reproduce the final capture with:

```sh
python3 -m tools.experiments.game_text_buffer_fade_frontend_trace
```

The prior `if (opacity != 0)` promotes the byte to a signed-word predicate.
UOPT retains byte opacity in S0 but adds a separate J-typed M-16 temporary,
creating the unwanted SP+0x20 spill. A scalar `if (opacity)` removes that
promoted lifetime. Separate pass pointers move the second descriptor to
M-16; explicit else defaults restore the positive-count exit branch and its
byte-store delay slot. Assigning inverse before opacity restores the two
opening independent constant moves. The final optimized M-16 records are
only an A-typed pointer store/reload; there is no J-typed opacity spill.

The final captures contain577 CFE and582 optimized records. CFE SHA-256
`0fad404162d13b0358dbdd2921ddbbd9a1280d96c2514cd77e17e088c57e0293`;
UOPT SHA-256
`7d5fb2fac3eb2d2444308127d91e9aa68065928ecb874a0cc4629061b1e43223`.
The prior indexed/direct control captures and the focused source screens
remain in the ignored target directory. No additional Claude call was made;
Note2117's one bounded advisory and its rejected hypotheses remain historical.

Only offsets0xB4..0xC8 differ in raw output. Their six-word multisets are equal:

| Raw order | Retail order |
| --- | --- |
| Owner-home LW | A0=206 |
| Descriptor ADDIU | Owner-home LW |
| Descriptor SW at SP+0x20 | A1=196 |
| A0=206 | A2=97 |
| A1=196 | Descriptor ADDIU |
| A2=97 | Descriptor SW at SP+0x20 |

The branch at0xB0, pointer use/definition chain, call at0xCC, argument mask,
all six relocation bindings and every other word already match. The guard
restores retail's delay-slot constant and its conditional owner reload.
Raw access order and raw fault-prefix equality are not claimed. The previous
raw opacity-spill witness now preserves tick7 even before normalization.

## Fresh qualification and production proof

Run from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_text_buffer_fade_match -v
```

Eight focused match checks and three historical recovery-boundary checks pass
in the mounted tools and against an ignored overlay using the dirty sibling's
actual complete-owner compiler, parser, guest oracle and native32 command
builder. Mounted fallbacks supply newer dependencies absent from the older
sibling; exact helper paths/hashes are recorded. The sibling is not edited.
Both checkouts also pass tools smoke, match-progress, pad-word-guard and
PC16 regression checks. Older unchanged recovery semantic/native receipts
are reused explicitly; they are not presented as new full-suite runs.

- 4,600 cases per guest body compare retail, raw C and normalized output
  with an independent external-state/call-order reference. All69 retail
  words execute; ABI registers and return1 are checked. Normalized full RAM,
  registers, events and access traces agree literally.
- 156 guest stack/tick aliases per normalized body,48 fired access-fault
  prefixes, and an incoming owner-home redirect verify live first-pass
  reloading and the second descriptor's capture before its color provider.
  Guest private-home probes are separate from portable native-C claims.
- The complete35-word original parent runs168 cases per body. It covers31
  parent words in normal success/skip paths, preserves record lifetime and
  clears active mask1. An effective zero-return callback control executes the
  four-word expiry path and writes lifetime-1, proving return1 matters.
- The original22-word color helper runs1,024 cases per body with every word
  covered. Independently predicted color bytes, text calls and countdown
  state agree. The large text renderer remains opaque; full renderer,
  hardware and gameplay acceptance are not claimed.
- Nine independent GNU links at three addresses test all six bindings,
  HI/LO carry boundaries and111 sampled cases per normalized body.
- SDK native32 layout and compatible callback-pointer tests execute61,440
  positive cases across O0/O2/O3 with UBSan. Seven effective controls reject
  unsigned counts, missing reset, added ticks, multiplier32, added inverse,
  same-buffer second pass and return0. Native indices are limited to0/1.
- 276 raw-byte corruptions, six binding corruptions, six actual padder
  expected-word controls and five whole-image corruptions fail closed.

The initial renamed-buffer negative control was an unchanged-source no-op;
it is corrected and every negative body is now required to differ from the
selected source. The first standalone owner reproduction omitted Make's
existing `D_800A0860` rodata binding. Reproducing that binding restores the
complete owner byte-for-byte. Neither fixture issue is a production defect.

There are96 frozen inputs. All24 compact and padded neighbors, allocated
pools and the existing rodata owner are preserved. The strict whole-ELF
prediction changes206 bytes: the target slot and its12-to276-byte symbol
extent only. It has zero exclusions and zero metadata permutations. All6,052
function addresses stay fixed. All189,088 protected bytes /720 owners agree.
The guard CSV retains its entire predecessor byte sequence and appends only
the six checked schedule rows.

Actual Make's object and ELF equal the independent prediction. The conversion
CSV is unchanged; a fresh linked recount provides the new matching total.
The existing full-ROM checksum mismatch still returns2 under `make all`;
this function match does not make the unfinished full ROM exact. Existing
duplicate-recipe and unrelated compiler diagnostics remain outside this
target's warning-free owner compile.

Production ELF SHA-256
`de38b29e6cea1979d9e246ba6ee4336c72693e9172b1f0cff0cb607c5f20df5e`;
guard CSV SHA-256
`f95322a63ee1e477fdde683de56f67da25c3ee5c097dfb94141fc94fa013a5e4`.
Receipts and full logs are in
`conker/build/game-text-buffer-fade-150D01A0-match/`.

## Progress and next action

Production is **4,187/5,512 (75.96%)**, Game **3,514/4,839 (72.62%)**,
Init492/492 and Debugger181/181, zero drift. **223 more** at the current
inventory are needed for the4,410-function80% threshold. README changes are
limited to aggregate rows; the detailed narrative stays here.

The historical69-word/34-difference private body remains reproducible against
its immutable predecessor snapshot, including its failing SP+0x20 witness.
Only this qualified successor receives matching credit. Preserve that
distinction and the eight earlier project boundaries.

Next resume the private `func_1514A594` dual-point motion screen in
`conker/build/game-dual-point-motion-1514A594-match/`. Its minimal source
retains frame0x18 but emits72 words into a67-word slot; it remains uninstalled
and uncredited. Inspect the five excess operations, complete-owner diagnostic
provenance and the original float access order before another focused form.
Do not pad or guard away that overflow. The80% goal remains active.

Graphify receives a scoped refresh with old-node retention, not a claim of
fresh full-corpus extraction. Unrelated sibling edits, private inputs, real
saves and the frozen host-port Release remain preserved. No push or host
runtime acceptance is added.
