# Cached vector basis directly matched

Date: 2026-11-06. Continues [Note 2142](2142-game-selected-point-effect-descriptor-direct-match-20261106.md)
from consumer `c55798da62c64174b2139a4b1fe61e38671325e4` and mounted tools
`c9c32307a083f28266e297f9c6eec1c74790541f`, toward the active 80% goal.

## Direct source and state contract

`func_1514F6E8` in `conker/src/game/generated_17CAF0.c` emits all
**72 words / 288 bytes directly from semantic C**, with **zero guards**.
VA `0x1514F6E8..0x1514F808`, ROM `0x17CB98..0x17CCB8`, frame `0x20`,
no alignment tail. The first complete draft matches. The O2/g3/MIPS2/O32
profile and four JAL bindings are unchanged. All 40 compact and padded
neighbors, allocatable pools and register metadata remain fixed. The raw
.options payload and every header field except its displaced file offset
remain fixed; discarded raw debug/section geometry is not claimed identical.
No shared header, compiler profile or guard CSV changes are required.

The interface is `s32 (void *input)`, compatible with the existing typed
void-pointer caller in func_15153CCC. A local CachedVectorBasis17CAF0 pointer
names the real 44-byte prefix; existing SDK struct17 supplies each 12-byte
vector. Native assertions check pointer width, size and offsets. Offsets below
are hexadecimal.

| Offset | Field |
| --- | --- |
| 00 | Cached flags byte |
| 01..03 | Reserved bytes, preserved |
| 04 | Direction vector |
| 10 | Tangent vector |
| 1C | Bitangent vector |
| 28 | Radius, preserved by this routine |

If flag mask 0x01 is clear, the direction is normalized in place through func_15145128.
A zero helper result returns0 immediately. Otherwise all three direction
components are multiplied by 1000.0f and mask 0x01 is set. If mask 0x02 is clear,
func_15146078 builds the two basis vectors; failure returns0 and success
sets mask 0x06. If mask 0x04 is still clear, the two basis vectors are normalized
in place, in order, with an immediate0 return for either failure; success
sets mask 0x04. A completed or fully cached state returns 1.

Higher flag bits remain intact.
The routine reloads the live flags after helper calls and preserves earlier
updates when a later helper fails. S0 and RA stay saved over the helper calls;
no artificial frame object or volatile access was introduced.

## Caller and provider qualification

A complete ROM census finds exactly three JALs and no literal function
pointers or tail entries:

| Parent | Call VA | ROM offset | Input register |
| --- | --- | --- | --- |
| func_1514FF44 | 1514FF94 | 17D444 | S6 |
| func_15153CCC | 15153D14 | 1811C4 | S7 |
| func_151D09A8 | 151D0CA8 | 1FE158 | S6 |

Each result gates subsequent random effect generation. The three original
call/branch windows receive 144 cases per body and stop before RNG execution.
Both success and failure destinations, including branch-likely delay behavior,
are checked. The complete parents are not claimed recovered by this change.

Eight methods pass before and after installation in both tools configurations:

- **4,864 guest cases per body** cover all256 flags, nonzero full-word helper
  results, all helper failure paths, live flag/vector/radius mutations and
  partial writes. Raw C, padded C and retail are identical. Every reachable
  root word is visited; words40 and63 are unreachable duplicate byte loads
  left by retail's branch-likely layout.
- **192 alias cases per body** check separate state and two incoming-home
  placements. **156 fired memory access cuts** compare complete literal state,
  fault PC and delay markers. With all flags cached, only the flags byte is
  required. Guest stack bytes/faults are not portable C claims.
- **480 connected cases per body** run the actual50-word normalizer,
  148-word basis builder and29-word cross product, individually and together.
  Zero, axis, signed and general finite vectors are checked against a staged
  float32 reference, including optional nested length/reciprocal outputs.
  The cross order is temporary×direction, then bitangent×direction. The
  basis builder ignores its nested normalization results. No arbitrary NaN,
  FCSR, hardware or additional provider C recovery is credited.
- **Six independent GNU links**, three layouts and144 cases per body check
  all four JAL bindings and standalone zero tails.
- SDK **native32 with UBSan at O0/O2/O3** runs3,072 cases per profile,
  9,216 positive executions. It checks typed helper calls, input ABI, state
  sizes/offsets, all initialized fields, helper observations and partial
  failures. All nine negative controls fire: wrong gate, ignored failure,
  scale, basis outputs, cache mask, missing second normalization, stale
  flags, wrong success result and the old stub.
- **288 raw-byte, four binding and six full-image corruptions** fail closed.
  The former stub's false0 result is independently rejected on a cached state.

The 109 frozen core/header snapshots remain checked. Both tools configurations
pass fresh smoke checks; three unchanged shared regressions are reused only
with exact helper/test fingerprints. The sibling's compiler, parser, guest
oracle, native command and metadata serializer come from the sibling. Its
missing game_player_status_accessor_match.py uses an explicitly fingerprinted
mounted allocatable-pool auditor read-only. New target modules use a disposable
overlay; the sibling's 2434 dirty status paths are unchanged. Claude calls: 0.

## Production result and resume point

Actual Make recompiles only generated_17CAF0.c once, with zero C diagnostics,
and equals the complete independent **197-byte ELF prediction**, with **zero
excluded ranges**. Only the target body and symbol size12 to288 change;
there are no symbol/string permutations. All 6,052 function addresses, other
bodies, Makefile, progress.csv and 189,088 protected Game bytes across 720
owners stay fixed. The inherited duplicate12D630 recipe warning and expected
unfinished-ROM checksum exit2 remain. No gameplay or hardware acceptance is
claimed.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,212 / 5,512 (76.42%) | 0 | 1,300 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,539 / 4,839 (73.13%) | 0 | 1,300 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**198 more** matches reach the current4,410 threshold for80%.

- ELF: `ce3fbf40414bdeaebc52658f1f2d421439c7f5e0a8cb33f98240953b42ee01a6`.
- Owner: `3dd97920916f6903d4cbd1afe318cf81a7f00b8052bbeb22e83c7baf42b68fd2`.
- Binary: `48c4cecee865e1f32b1e6b0c918294afb4cbdf1e51ee83f581d4418e3d170eb7`.
- Unchanged guard CSV: `9892912f5423eb5e518da147fb0bf7e358de56260cb3d59e6b2e6d1bcff0c4ab`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Reproduction: `python3 -m unittest tools.tests.test_game_cached_vector_basis_match -v`.
Actual Make uses `-o retail_word_patches.us.csv -o Makefile`, followed by
ELF/progress, the expected unfinished-image `all`, and
`match-progress NON_MATCHING=1`. Receipts are in
`conker/build/game-cached-vector-basis-1514F6E8-match/`.

Tools commit precedes source/docs/pin; root README receives aggregate rows only.
Graphify retains nodes outside changed paths and the legacy fail-closed corpus;
this scoped refresh is not a full extraction. Next is **func_1517D690** in
generated_1A89B0,72 words, still a zero-return placeholder. Inspect its retail
routine and callers before recovery. It remains uncredited. Preserve handwritten
func_150A6FA0/func_150A76F0, unrelated work, private inputs/saves and frozen
host Release. Keep the full80% matching goal active.
