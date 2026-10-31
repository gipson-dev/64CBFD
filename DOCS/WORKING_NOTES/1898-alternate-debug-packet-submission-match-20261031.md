# 1898 - Alternate floating packet submission: guarded C match

Date: 2026-10-31. Function `func_151A0F28` in
`conker/src/game/generated_1CC440.c`. VA `0x151A0F28..0x151A1010`,
ROM `0x1CE3D8..0x1CE4C0`: 58 words / 232 bytes, no alignment words.
The semantic body emits 58 words under the existing O2/g3 profile. Ten
relocation-aware guards recover two closed schedules; 48 words are unchanged.
No insertions, omissions, assembly injection or shared-header changes.

## Recovered behavior and interface

`void func_151A0F28(f32 x, f32 y, f32 value, u8 variant, s32 flags)`
forwards three float representations, `163.0f`, and a fixed 28-argument packet
to `func_151A11CC`. The repeated global float `D_800A8D24` has retail bits
`0x4001374C`. Other packet fields are the original integer constants, narrowed
variant byte and signed flags word. The first two floats remain in f12/f14;
the third is passed through a2 and its o32 argument home. No float arithmetic
occurs. The higher-level purpose of these latent debug/effect parameters is
not proven: the actual retail callee is an empty six-word routine.

The helper retains its previously qualified full 28-argument fixed signature. Its first
four parameter homes still emit exactly `swc1 f12,0(sp)`, `swc1 f14,4(sp)`,
`sw a2,8(sp)`, `sw a3,12(sp)`, `jr ra`, `nop`. All six original words are
unchanged in the raw before/after owners, padded owner and actual Make output.
The preceding wrapper recovery established this floating interface; this
recovery uses the same compatible prototype without changing the helper source.

The 120-byte frame saves RA at SP+116. Incoming value, variant and flags homes
are SP+128, SP+132 and SP+136. The 28 outgoing slots occupy register arguments
and stack offsets+16..+108. No saved S-register or pointer lifetime is invented.

## Scheduling and reference boundaries

Guards at word indices1..6 move the independent global load ahead of RA and
argument-home stores and byte narrowing. Guards at indices48..51 move the
variant stack store after the three repeated float stores. The two sequences
retain the same instruction/binding multisets, operands and destinations.
Forty effective row-corruption controls check expected/replacement words and
relocation preimages/results. The complete raw payload and binding map are
also fingerprinted; 237 payload/scope controls reject changed inputs.

Normalized code preserves the original access prefixes and delay-slot store.
Raw C has the same complete final register/memory state and argument transcript
on mapped valid fixtures. An effective unmapped-global control demonstrates
that its fault order differs: this is recorded, not claimed equivalent to the
original. No portable C fault-order or FCSR claim is made.

The complete aligned-ROM census finds no JAL or literal function pointer to
this wrapper. Three JALs reach the helper at ROM `0x1CE3C0`, `0x1CE4A8`,
`0x1CE664`. Their existing machine interfaces and all other bodies are preserved.
This census does not establish unreachability or complete indirect-reference
coverage; no original wrapper caller execution is claimed.

## Fresh qualification

- Eight fresh methods and project tools checks pass independently in both tools
  copies. After production, two installed methods rerun per copy; six semantic
  methods are reused only through exact input/module/artifact fingerprints.
- Guest: 2,272 cases / 6,816 executions across three independent GNU layouts.
  All 58 root words are visited. Original/padded/actual-Make normalized images
  are byte-identical. Original, padded and raw C streams are executed; raw final
  state agrees while only the normalized stream claims original access order.
  All 28 arguments, all 256 variant bytes, wide variant inputs, flags, stack
  phases and float representations including signaling NaNs are checked.
- 62 fired original/normalized access-prefix pairs include two branch-delay
  cuts. An unmapped-global control proves the raw fault-order difference.
- 144 connected cases / 432 executions retain and visit all six original helper
  words. All 28 argument slots, original float homes, surrounding memory and
  saved-register restoration agree. The helper has no external effect.
- Native SDK32 O0/O2/O3: 720,896 positive cases per profile with trapping UBSan,
  all 65,536 tested variant input values, all 256 narrowed bytes, 11 float
  patterns, varied full-width flags and 12 effective source controls. Every
  selected/control source compiles. Signaling-NaN representation preservation
  is checked by the guest model, not claimed for the native C harness.

## Owner, production and banking

All 38 raw/padded owner neighbors and normalized pools are unchanged. Five
actual Make commands reproduce the qualified padded object. Selected, owner
and Make diagnostics are empty. The already qualified helper signature and its six-word body are unchanged.

The independent complete ELF prediction has zero exclusions and exactly 231
changed bytes: 182 root-code bytes, one root-extent byte and 48 metadata bytes. All
6,055 other linked bodies, every address and 189,088 protected Game bytes
across 720 owners remain unchanged. A closed four-symbol serialization moves `D_800A8D24` after `D_800A80A4`,
`func_150F6850` and `D_80096174` in the ELF symbol/string tables. The prediction
rebuilds the complete named rows and contiguous name block from their original
fields; names, addresses, bindings and sizes are preserved apart from the
selected root extent. The initial prediction failure and exact diagnosis are
retained. This is a measured metadata permutation, not a byte exclusion.
The inherited guard prefix is byte-identical;
only the ten reviewed target rows are appended. Conversion inventory unchanged.

Tools commit `7de173c672f2447b9fe37d02ff9a5eacf73724d3` precedes the consumer commit. Production ELF SHA-256:
`782de3882fb7da42092ce29e6ee3994d1e1b8958d15fe1930dbf72d75fecd8a9`.
Actual adopted-ELF recount: **3,975 / 5,506 (72.19%)**, Game
**3,302 / 4,833 (68.32%)**, Init 492/492 and Debugger 181/181. Zero drift;
1,531 C functions still differ. **155 more** are needed for 4,130 exact (75%).
Next screen: `func_151B5240`. This recovery contributes one match; the already exact
empty helper contributes no additional credit.

Artifacts and immutable inputs remain under ignored
`conker/build/game-effect-debug-packet-alt-151A0F28-match/`. The root README
changes only two aggregate rows. The scoped graph refresh retains prior nodes
and valid relationships, updates the recovered wrapper signature and retires the
obsolete placeholder return edge. No full-corpus extraction, global clustering,
hardware, gameplay acceptance or push is claimed.
