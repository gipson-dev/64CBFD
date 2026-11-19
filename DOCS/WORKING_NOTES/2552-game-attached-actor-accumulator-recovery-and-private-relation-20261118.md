# Attached-actor accumulator recovery and private relation - 2026-11-18

`func_150BA55C` has a complete tested **private C recovery**. It emits **229
words /916 bytes, frame280**, versus retail **229 words, frame264**. A complete
finite-value/private-state relation and a private source-derived fitting
experiment now pass. **The source remains uninstalled, with zero new matching
credit**. Actual padders, rebases, guards and production-image adoption remain open.

Production stays at [Note2551](2551-game-surface-impact-callback-guarded-byte-match-20261118.md):
**4,552 /5,514 (82.55%)** total, **3,879 /4,841 (80.13%)** Game, Init492/492,
Debugger181/181, zero drift and962 different. **135 more matches** reach85%.
These are the retained actual production measurements, verified against unchanged
ELF/source/CSV/progress inputs. No fresh production recount is claimed. The root
README remains byte-identical; detailed work stays in this note.

Starting consumer `f10a5b68641e6857d2fb79b2853327d3ac9d3629`, tools
`441556cda8265b625cf8f0c23222516548777bb2`. The committed1798-input manifest is
verified, with the new owner C/assembly added for **1800 frozen inputs**. Callback
table and dispatcher were already frozen. Immutable byte copies and predecessor
references are retained in `conker/build/game-next-150ba55c-private/`; no live
hardlinks. The preceding matching turn installed the291-word surface callback.

## Function, ABI and recovered semantics

Owner `conker/src/game/generated_E7970.c`, original `conker/asm/E7970.s`,
VA150BA55C..150BA8F0, ROM E7A0C..E7DA0. The corrected private declaration is
`void func_150BA55C(u8 *effect)`; the existing false zero-return placeholder
stays in production until adoption. The complete copied owner preserves all
**five neighboring functions and normalized pools** under the existing O2/g3
profile. There are39 raw/retail binding sites.

The aligned retail census finds no direct JAL and one literal pointer at
ROM22F0F0 /VA8008A630: **D_8008A4E8 index0x52**. The original45-word
`func_15149264` passes the effect pointer and ignores V0. Its entire production
body and the332-byte table prefix through this index are literal retail.
This is a scoped aligned-pointer/JAL census, not an exclusion of every possible
indirect address construction.

The recovery retains:

- Cached payload/source pointers at effect+0x28, the source's active word and
 identity-byte gate, lifetime=-1 on identity failure, and source+0x1D4 readiness
 gate. There is no invented null-source gate.
- One real-provider draw before the accumulator update; late rate/time loads,
 a stored/reloaded accumulator and the strict `1.0f < value` condition.
- Cached average source dimensions and heading before the transform provider;
 exposed origin/radius/unused-height outputs; and acceleration base/range loaded
 after that provider. Acceleration Y is initialized **once before the loop**.
- Two unsigned RNG remainders modulo127/31, signed16 yaw/pitch and radius read
 after both RNG calls, direction output, live source Y ratio, and origin offsets.
- Three ordered rotation draws, a separate spread draw before its constant
 reads, late retained-origin reads for velocity, two acceleration draws and the
 final size/speed draws followed by duration RNG.
- All13 submit arguments, late size/speed/damping constants and effect bytes,
 modulo41+60 lifetime, and the public accumulator reload/subtract/store/reload
 after submission. It does not replace the loop by a fixed count or add a cap.

Unknown object fields keep explicit offsets/widths. Typed point/payload shapes
and comments describe known behavior; no shared headers, compiler profile,
production source/assembly/guards, object, ELF, host source or Release artifact
changes. Selected unbound SHA:
`f15047c12d789d1d967f6ba5f8b6aff151880d272d3a25591d0039745951b43e`.

## Paired fresh qualification

Both final configurations pass **five tests**, with zero failures/errors/skips:
**77.325s primary /90.147s private sibling overlay**.
All **332 imported tool files per configuration** are fingerprinted. The overlay
has835 files:339 matching sibling copies,487 primary fallbacks, eight task
artifacts and one empty package bootstrap. The real sibling's HEAD/status and343
dependency hashes remain unchanged; conflicting pending work was not overwritten.

1. Complete before/after owner compilation, all229 source words/39 bindings,
 independent GNU original assembly and literal ROM binding, five neighbors/pools
 and the callback census.
2. **1584 guest cases per stream**,226 reachable words each, full public memory,
 all four submitted12-byte vectors, mutable retained origin/radius/height and
 output buffers, cached-versus-live source fields, signed-zero inputs, unsigned
 RNGs, all256 initial identity bytes and saved ABI. **80 bounded nontermination
 prefixes per stream** cover infinity and large unchanged float accumulators;
 they make no termination claim and add no runtime limit to C.
3. **192 cases per stream through all45 original dispatcher words**, with the
 actual0x52 callback, enabled/disabled update, signed16 timer wrap, conditional
 cleanup and release, and a freshly reloaded post-cleanup lifetime. A wrong
 callback-pointer control is effective. Cleanup/release remain opaque services.
4. **752 SDK32 native cases each at O0/O2/O3**, strict aliasing, no fast math and
 UBSan, compared with independent transcripts checked on retail MIPS. All11
 source controls are effective: identity/readiness, rate, both moduli, rotation,
 spread, persistent acceleration Y, duration, late bytes and decrement.
5. Complete **five-entry-path/two-loop-outcome finite/private relation**,
 **280 mapped frame/incoming bytes** and **16 explicitly untouched source-only
 bytes**, with complete snapshots at every provider/return. Saved registers,
 outgoing homes, scalar size cache and all retained buffers are accounted for.
 Five instruction controls and a source-only write control reject intended errors.

The initially ineffective native Y-reset control exposed a fixture gap: later
provider mutations overwrote Y before observation. Restricting that component's
mutation to submit makes its cross-iteration lifetime observable. Final paired
receipts include this correction and reject the bad reset. Earlier failed
receipts remain retained, not counted as passing evidence.

The instruction relation preserves arithmetic observation order but permits
commutative **finite-value** add/multiply operands. A strict operand-order
control fails at the source-dimension average: the two source loads feed the
opposite add operands. Raw FCSR flags, traps, NaN payload selection, fault
prefixes, asynchronous behavior, arbitrary public/private aliases and full deep
services/gameplay remain outside this proof. Providers may mutate all previously
exposed buffers and ordinary public memory; they cannot inspect unpassed locals
or implementation PCs. Concrete guest/native exceptional cases do not broaden
the all-input symbolic domain.

## Source-derived fit and remaining adoption

Twenty-one candidate compilations were measured across the original screen,
buffer/cursor forms, no-unroll/no-constant backend flags, arrays, local sample
scope, inline duration and explicit average. The eight final shape screens and
six profiles preserve all five neighbors/pools. No-unroll emits the same bytes;
no-constant emits218 words/frame256 and is rejected. Arrays and scoped samples
compile away. No guessed volatility or dummy locals were introduced.

The private `fit.py` experiment reproduces **all229 original unbound words and
all39 bindings**, retaining every source word with no insertion/omission. The
fit derives stack fields from the proved byte map; uses the two semantic FP-role
cycles20/22 and26/30 without changing saved-register homes; recovers the average
operand assignments; and retargets the cached S8 address from D_8009FE40 to the
rotation buffer. The original source HI/LO pair is carried to the real loop
load, and the source rotation address setup becomes its recovered saved-register
copy. Only the constant LUI moves from source word75 into the loop; this shifts57
source positions and branch displacements are recomputed from source edges.
The experiment stores source indices/fields and verifies against independently
assembled retail; it is **not yet a maintained/adopted normalizer**.

Continue the same function:

1. Freeze these eight newly committed tools as well as the1800 protected inputs.
 Promote the tested private derivation into a fail-closed normalizer, retaining
 the explicit finite/FP boundary and complete projection. Qualify relocation
 transport and every derived source word with effective corruption controls.
2. Run both actual owner padders, independent GNU rebases and actual guard
 controls. Reuse or connect the already-recovered39-word `func_150BA4C0` factory
 and its payload-copy contract as applicable; do not broaden its opaque services.
3. Run actual Make with an independent strict full-image prediction, with no
 blanket section/metadata exclusions. Only then install source/derived guards,
 audit all other functions/addresses/data, run installed checks and actual recount.
4. Update aggregate README counts only after those gates and commit tools first.

Native Graphify update exited1 with old IDs retained. The
scoped AST/target-edge refresh and post-hook ID retention are recorded separately;
there is no forced shrink or full-corpus extraction claim. The85% goal remains
active. Routine work uses zero Claude calls and no REA/WSL reconfiguration.
Frozen Release, host captures, real saves and sibling dirty work remain preserved.
No push or automatic pause.
