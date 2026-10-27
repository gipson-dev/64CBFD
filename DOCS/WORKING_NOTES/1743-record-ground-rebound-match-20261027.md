# 1743 - Record ground rebound callback match

Verified 2026-10-27, following [Note 1742](1742-actor-transition-initializer-match-20261027.md).

## Result

Replaced the zero-return placeholder for `func_150BCFB8` in
`conker/src/game/generated_E8C10.c` with the registered rebound callback.
Its complete **184-byte / 46-word** body matches directly from semantic C at
VA `0x150BCFB8..0x150BD070`, ROM `0xEA468..0xEA520`.
There are **zero guards**, inserted words or omitted instructions. This is a
leaf with no frame; all three incoming register-argument homes and the fifth
argument's stack load match. The normal O2/g3 owner profile applies.

The actual adopted Native ELF recount is **3,820 / 5,506 exact (69.38%)**,
Game **3,147 / 4,833 (65.11%)**, Init 492/492 and Debugger 181/181. Address drift
is zero; 1,686 C functions differ. This restores an existing C inventory row;
converted counts/bytes and progress CSV bytes are unchanged. The 75% threshold
stays 4,130, requiring **310 more** exact functions. The wider goal remains open.

## Registration, ABI and behavior

The actual 15-entry registry `D_80089934` registers this routine at slot 2,
literal ROM `0x22E3FC`. No aligned direct JAL to the target exists.
The two retail indirect sites are `0x1513300C` in `func_15132DDC`
and `0x151339B0` in `func_15133894`. Both pass the record, three
position floats, a ground-height float and the normal-vector pointer. The
recovered interface is `s32(record *, f32, f32, f32, f32, f32 *)`.
The target uses the record and ground height; it preserves the unused incoming
float homes and never dereferences the unused normal pointer. It returns 1.

The local record prefix gives names to the measured offsets: extent 0x10,
damping 0x14, height 0x3C, velocity 0x44..0x4C, rotation velocity 0x50..0x58,
and flags 0x60. Shared headers and other functions are unchanged.

The common height calculation is extent times `D_8009FEF8` plus the
incoming ground height. The constant is binary32 `0x3F8CCCCD` (1.1f).
Multiplication and addition round separately; an effective wider-intermediate
native control distinguishes that sequence from a final-only float rounding.

- When vertical velocity is strictly greater than -2.0f, it clears the three
  velocity components and applies the original full-word flag mask
  `0xFFFFFF90`, retaining the rotation components.
- Otherwise it damps all six motion components and negates the vertical
  velocity before multiplying. The ordered comparison sends NaN vertical
  values down this branch. The damping field is not read on the settling path.

The complete original and retained 80-word `func_15133894` dispatcher are
connected in guest checks. All 80 instructions are visited across its gates,
attached-surface exclusions and dispatch paths. Checks preserve the copied
position across the pre-provider, reload method and attached-surface state
after the ground provider, pass all six callback arguments, and sign-extend
the callback return through its byte local. Other registry entries and the
two provider implementations are bounded contracts. The larger caller's
actual argument envelope is inspected separately; whole-caller gameplay and
provider semantics are not claimed or newly credited.

## Owner and strict image preservation

Raw isolated C, complete-owner C and independently assembled retail agree in
all 46 words and the HI16/LO16 pair for `D_8009FEF8`. All eight other
owner functions and normalized pools are fixed. The actual three-command
Make route reproduces all nine compact functions and the complete padded
object. Baseline, recovered owner and isolated diagnostics are empty.

The first body/extent-only full-image predictor correctly rejected 38 further
metadata bytes. The diagnosed change is a closed serialization reorder of
`func_151417C4` and `D_8009EF5C`: two 16-byte symbol rows exchange
positions, and their 14-byte and 11-byte names exchange order in one 25-byte
string-table window. Both named definitions retain their original value,
size, binding/type and section. The predictor pins the exact predecessor
rows, names, extents and offsets before reproducing this reorder. No code or
data is normalized away, and no image exclusions are used.

Both tools copies pass eight fresh canonical methods, zero errors/failures/
skips, in 12.047 and 11.986 seconds. Both shared tools checks pass. Per-copy
coverage includes:

- 4,212 guest root cases, all 46 instructions, all low flag bytes, signed zero,
  subnormals, ordered NaN/infinity model cases and five alias layouts.
- 388 complete original/retained dispatcher cases, including return-byte
  truncation and provider-visible snapshots/reloads.
- Native32 O0/O2/O3 with 8,280 direct/typed-indirect cases per profile, exact
  record layout assertions, trapping UBSan and 11 effective controls.
  Finite outputs are bit-exact; NaN outputs are checked by classification.
- 73 fired fault prefixes, sparse settling without damping/angular mappings,
  and effective compiled MIPS early-damping/unused-normal read controls.
- Six GNU links over three layouts and 144 rebased guest cases, including
  signed-low relocation carries. Three raw/binding negatives, nine strict
  image corruptions and three wrong-input controls also pass.

These are emitted-instruction and bounded binary32/ABI checks, not proof of
R4300 FCSR exception behavior, NaN payload portability or hardware gameplay.

The seal covers **16,142 Native inputs** and **85 focused frozen inputs**.
Actual production Make completes in **0.623 seconds** and reproduces the exact
independent prediction: **182 changed bytes = 143 code + 39 metadata**. The
metadata consists of the target size byte and the closed 38-byte symbol/string
reorder. All 6,056 addresses and 6,055 other bodies stay fixed. All named ELF
definitions are unchanged except the target extent. Protected Game data is
exact across 720 owners / 189,088 bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

After installation each copy passes two fresh owner/image methods; six
unchanged semantic methods are reused only under exact input, module and
prepared-artifact fingerprints. Four adopted outputs are source, owner object,
ELF and map. Guard/layout manifests and progress CSV remain fixed. The recount
reads the captured, actually adopted Native ELF rather than a projected gain.

| Artifact | SHA256 or commit |
| --- | --- |
| Tools commit | 9cdb3266bd81e8162e125699d24bafdae738b9ee |
| Adopted ELF | 69219af068e12484b842db07cfe9df8e9dbbe6fce15dea1ce808131bcb55c087 |
| Recovered owner source | 8efda682a86ca3915437aa684438413e4d214a471ff0ba09033361b6db01d540 |
| Padded target owner object | 6d8e6e50d6b34ab8576ca1335ecf9a6073cef9b5896a93fc3a02d1ae5c293081 |
| Raw selected C payload | ac4efd8d1086a313e862d5a099612735fe25cf83e1b500aca3eea80111d133ed |
| Input snapshot | 2dc81b9df292bddaee95f364acbf643da0fdad45810780642000a729d066cd84 |

Frozen raw compilation, the rejected first predictor, its symbol diagnosis and
fresh canonical/production receipts remain in
`conker/build/game-record-rebound-match/`. The semantic source candidate
did not change during the serialization audit. No compiler install or sibling
host/editor/Release change was needed. Routine Claude calls: 0.

## Next boundary

The next screened placeholder is `func_150FA468` / `generated_126F60`,
a 46-word window. It remains uncredited until the full source/ABI/caller,
owner/Make, guest/native, image, production, recount and documentation gates
pass. Root README gets aggregate rows only. Refresh the changed sources
structurally and validate retained type relationships from actual declarations;
preserve historical communities/centrality without a full-corpus claim.
