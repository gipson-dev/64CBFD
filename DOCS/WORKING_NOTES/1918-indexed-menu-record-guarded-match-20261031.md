# Indexed menu record replacement - guarded byte match

2026-10-31. `func_150B76BC`, owner `generated_E4070`, is recovered from its
zero-return placeholder. Its 236-byte slot at VA `0x150B76BC..0x150B77A8`
(ROM `0xE4B6C..0xE4C58`) matches all 59 retail words after three expected-word
guards. There are no inserted, omitted, alignment or control-flow words.

## Recovered behavior and ABI

The function is `void func_150B76BC(s32 x, s32 slot)`. It converts the full
signed x coordinate to float32, supplies y=170, and prepares the existing
60-byte `MenuRecordDescriptorE4070` with asset `D_800918E8`, width field 64,
height field 88, two 81 scale fields, mode 6 and the original byte parameters.
Forty descriptor bytes have defined stores; the remaining twenty retain their
existing stack contents. Those bytes are not claimed initialized by portable C.

The selected entry is `((void **)D_800D9898)[slot]`. Its previous pointer is
captured and released if nonzero, then the factory result replaces that entry,
including a null result. Destructor/factory mutations are observed in retail
order. The target itself leaves the menu state byte to its helpers/callers.
The forward declaration now states the correct two-argument void signature.

Both complete original callers execute: `func_150B765C` supplies `(60,1)` and
`func_150B768C` supplies `(230,2)`, then each sets state 3. Their JALs are at ROM
`0xE4B18` and `0xE4B48`; the aligned ROM census finds no literal function pointers.
The source retains the address-based name and labels uncertain descriptor fields
by their recovered offsets rather than inventing field meanings.

## Compiler shape and normalization

The existing owner Make profile is `-O2 -g3 -Wo,-loopunroll,0`, using
`game_active_record_lookup_match.compile_owner`. The raw semantic body already
matches the 96-byte frame, RA at SP+0x14, descriptor at SP+0x24, six relocations,
and the selected pointer's four spill/reload instructions at SP+0x20.

A named pointer local displaced that spill; repeated indexed accesses recovered
it naturally. No frame or stack-access normalization is used. The only remaining
differences are independent setup words 13..15: AT loads the 170.0f upper half,
T6 loads 1 and T7 loads 88. Guards apply the closed permutation `[15,13,14]`.
The destinations are distinct; no relocations, memory accesses, immediates,
branch destinations or following uses change. All original guard rows remain
an identical prefix. Six real padder controls reject stale words/bindings.

## Validation

- Guest execution compares original, raw C and normalized bodies across 768
  cases / 2,304 executions, visits all 59 words, and compares complete final
  machine state, calls, memory and traces. All 118 access-prefix cuts agree.
- Three independent symbol layouts exercise 96 rebases, including signed low
  halves; three descriptor/global stack aliases remain guest-only evidence.
- Both full 12-word callers run in 32 cases. The original 8-word factory wrapper
  and 26-word constructor run together in 96 cases; allocation and copying are
  explicit ABI hooks, without a hardware or full-gameplay claim.
- Native32 C runs 7,680 cases per `-O0`, `-O2`, `-O3` profile with UBSan. It covers
  all ten valid table slots, untouched neighbors, signed conversion boundaries,
  float32 rounding, optional destruction, null allocation and live helper effects.
  Thirteen wrong variants fail in both native and compiled guest checks.
- Eight fresh canonical tests pass independently in each tools copy, alongside
  both shared tools checks. After installation, two tests per copy run fresh;
  six unchanged semantic checks are reused only under exact input/module/artifact
  fingerprints. Fresh and reused evidence are recorded separately.
- All 20 owner neighbors and pools agree. Three actual Make commands reproduce
  the qualified padded object with zero inherited/new compiler diagnostics.
- Strict full-image prediction accounts for all 224 changed bytes: 185 target
  code bytes, one target extent byte and 38 metadata bytes. The metadata change
  is a closed adjacent symbol/string permutation of `func_15131AFC` and
  `D_8009E708`; all named definitions retain their values/types/extents.
  No regions are excluded. All 6,055 other bodies, all 6,056 addresses and
  protected Game data (189,088 bytes across 720 owners) remain fixed.

## Banking and continuation

Tools commit: `04fcaab1a8b25ead5bd4b67a01b2bb8612bfedcc`. The production ELF is
`333cd9a49306db1458dd2e90b7577b214503f2752d3144cb9f747075ecdbd0d4`.
Actual recount: **3,995/5,506 (72.56%)** total, **3,322/4,833 (68.74%)** Game;
Init 492/492 and Debugger 181/181 remain exact, with zero address drift.
**135** additional functions are required for 75% (4,130 total).

The detailed receipts are under ignored
`conker/build/game-menu-indexed-record-150B76BC-match/`. The root README changes
only its two aggregate status rows. Graph updates are scoped to the source,
three tools modules and seven documents, retaining old valid relationships;
they do not claim full-corpus extraction or global reclustering.

Next queued screen: `func_150C7C90`. Other private candidates remain uncredited.
No push or host-port/Release changes are included.
