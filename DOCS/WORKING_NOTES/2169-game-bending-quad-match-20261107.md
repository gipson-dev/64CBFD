# Signed bending quad recovered and byte matched

Date: 2026-11-07. Continues [Note 2168](2168-game-oriented-quad-match-20261107.md)
from consumer `cf3b6d4fcfa71b931ca73acbeb3b9cc04cde3fd8` and tools
`f0603f975c508c00f1c1860cddb6dd6757e92501`. One qualified Game recovery
advances the active 80% total goal. Host code and frozen Release are untouched.

## Recovered source and interface

`Vtx *func_1513F114(u8 *actor, s16 view)` replaces the false s32 zero-return
placeholder and local prototype in `conker/src/game_169510.c`. Its complete
**231 words / 924 bytes** match retail under the existing O2/g3, MIPS2/O32
profile with **61 expected-word guards**, the original **144-byte frame**,
and unchanged RA/S0/F20-pair lifetimes. VA is 0x1513F114..0x1513F4B0;
ROM is 0x16C5C4..0x16C960. No shared header or compiler profile changes.

1. Query the view's vertex buffer through func_151D5D60, keep its initial
   pointer separately, and return null on failure. If fresh, copy the 64-byte
   actor template into both buffer halves, reloading the destination slot
   between copies.
2. Recover lower = -(height * scaleY), upper = height + lower, and the two
   view-direction coefficients. Form the signed displacement cross-product
   scaled by D_800BE9A8. Its sign controls the final angle sign; sqrtf uses
   the absolute magnitude and actor+0x4C scales the result.
3. Clamp against D_800A51BC/D_800A51C0 before applying the sign. Both retail
   constants are float 0x3FC90FDB. Preserve the captured forward coefficient
   across sinf/cosf and pass the same angle through F12 to both F0-returning
   helpers.
4. Emit the four rotated lower/upper corners through the live escaped cursor.
   Each coordinate truncates to s32 then stores its low halfword. Preserve
   texture/color fields, clear all flags, and return the captured first pointer.

Source comments name the bending operation and escaped fields without
asserting an unproved original actor type. A small scratch structure holds
savedForward/first/cursor at SP+0x84/+0x88/+0x8C. Fresh is +0x4B, angle +0x4C,
sine +0x74, upper +0x78, lower +0x7C, and incoming view +0x96. The selected
raw SHA-256 is `cbcae288e52212ca344c87cc3836bb44eabac70edfe61f5dcddc3cbadef1e72e`.

## Closed normalization and actual callers

The raw semantic C has 61 word differences. Guards normalize four copy-spill
words, a closed F14/F16/F18 role cycle, two multiply-operand commutations,
two independent lower/forward spills, and the upper-corner allocation schedule.
No branch, call, prologue, epilogue, frame size or saved-register lifetime is
changed. All 15 bindings remain identical, including the guarded LO16 word.

The **48-word upper-corner schedule** is generated from explicit operations,
not copied from retail. An ordered symbolic expression proof preserves the
five stores at +0x20/+0x22/+0x24/+0x26/+0x30, actor reads tagged by intervening
public-write epochs, live F6/F8 and pending T6, preserved registers, first and
cursor. Only add/multiply operand commutation is allowed; no reassociation.
The proof covers valid public actor/output RAM disjoint from compiler spills.
Deliberate private aliases are separate complete normalized-retail guest checks.

The complete aligned-ROM census finds no direct JAL and one entry pointer at
ROM 0x22E8E8: **slot 3 of the actual 39-entry renderer-table prefix**. The
following E7000000 graphics command is outside that table. Complete original
**295-word func_1513DB00** passes actor A0/signed view A1 at 0x1513DC24 and
consumes the returned V0 pointer at 0x1513DC30. **That renderer remains a
production stub**; its other services remain bounded in the caller oracle.

The original memcpy/backend routines compare across all 11/52 words and are
connected in selected guest cases. They execute 62 of 63 words: the backend's
fallback fresh-byte address is unreachable with this caller's real nonnull
fresh pointer. Existing exact cosf/sinf compare across all 88/104 words,
but their execution is bounded to typed F12/F0 providers here. Allocator and
trigonometric correctness are not new restorations or gameplay acceptance.

## Focused evidence and limits

Seven checks pass before and after installation in both tools configurations:

* **746 guest cases per body**, including a minimal null fixture, agree with
  an independent ordered model. All 231 target words execute. Complete machine
  state agrees for normalized and retail code. Cover signed views and upper
  bits, both sqrt paths and branch-likely annulment, positive/negative zero,
  adjacent clamp thresholds, widths/scales, exceptional casts, helper field
  mutations, live cursor/captured first, template/actor and private-stack aliases.
  Raw C agrees on **700 valid nonprivate cases**.
* **290 original renderer cases per body**, with **128 actual target calls
  per body**, qualify pointer/s16/pointer-return ABI and float helper clobbers
  against the independent leaf provider. All 295 renderer words compare;
  293 execute. Duplicate defaults 115/146 are skipped by checked branches.
* **1,068 fired access cuts**, including **162 delay cuts**, preserve full
  memory, registers, PC/delay context and access prefixes for normalized versus
  retail code. An effective raw private-prefix counterexample is retained:
  raw code is not claimed to have retail private/fault identity.
* Native32 O0/O2/O3 each pass **627 cases**, with SDK Vtx16/pointer32, typed
  callback slot 3, checked float argument bits, escaped scratch mutations,
  trapping UBSan, round-to-nearest and no FTZ/DAZ. Ten compiled semantic
  negatives reject with exit 1, including sign/abs/clamp/gain, cached copy
  destination, reloaded direction, lost cursor/flags and wrong return.
* Six effective symbolic negatives, all 231 raw-word corruptions, all 15
  binding corruptions and historical guard/pool/options corruptions reject.
  Two independent GNU links preserve five calls and five HI16/LO16 pairs,
  including signed-low carry. Nine whole-image corruptions reject.

Native fixtures use finite representable casts and valid disjoint objects.
Private homes, aliases and exceptional casts are guest evidence. The float
model canonicalizes NaNs and does not emulate FCSR, NaN payload propagation
or hardware exceptions. Commutation/guest agreement does not establish those
hardware properties or portable C behavior for arbitrary stack aliases.

One bounded packet-only Claude review was attempted and completed. Packet
SHA-256: `6c85f48da1bde953c8cff483a756ed08c1d219f2c8b07f49078abb87716c3968`.
Verified sign/clamp/ABI and live-read observations agree with independent tests.
Its suggested late fourth-offset local was compiled twice: both have 231
words but a wrong 152-byte frame and 99/98 differences, so both are rejected.
Its raw instruction-identity/FCSR claims are also rejected. The selected
source has 61 raw differences and the explicit float-model limits above.
An initially ineffective pointer-negative fixture was replaced by a real T6
clobber; the corrected check rejects. No source defect was inferred from it.

## Production and progress

Freeze **181 inputs** and qualify complete predecessor/recovered owner objects
and padding. All **58 raw/padded neighbors**, pools and register/options
metadata remain fixed. The 43 inherited owner warnings are paired with no
new warning. Actual Make performs one O2/g3 owner compile and matches the
predicted padded object and complete linked ELF byte for byte.

Exactly **764 ELF bytes change**: 687 in the target Game slot, 38 in .symtab
(including two target-size bytes, 12 to 924), and 39 in .strtab. Three explicit
GNU symbol/name encounter-order permutations account for all metadata bytes.
Every named definition is unchanged except target size. **Zero exclusions**;
all **6,052 addresses** and **189,088 protected Game-data bytes / 720 owners**
remain fixed. Guard history is preserved with 61 new rows; Makefile, shared
headers and conversion CSV remain unchanged. `make all` retains expected
checksum exit 2 and the inherited duplicate generated_12D630 recipe warning.
This is not a whole-ROM checksum match.

Both tools configurations pass fresh shared smoke checks. Three unchanged
shared regression receipts per copy are reused after exact fingerprints.
The sibling overlay and explicit read-only missing-helper fallback preserve
all 2,434 inherited dirty sibling paths.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,239 / 5,512 | 76.90% | 0 | 1273 |
| Game | 3,566 / 4,839 | 73.69% | 0 | 1273 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**171 more exact functions** remain to 4,410 / 80%. README gets aggregate
rows only; four concise index leads preserve their full history. Refresh
Graphify with scoped legacy-node retention, without claiming a full-corpus
extraction. Commit tools first, then consumer source/guards/docs/pin, and
verify a fresh terminal hook, clean task trees and stable production.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `85c87d6a7517a03de99e75e3ca4d66973af398e03c2ddc9947d4f69cc21a6402` |
| Production binary | `5c7b4e6d3a08a9901d7545a5813d8b826e72ea21a2b5a79eadae26b1d623ec3e` |
| Padded owner | `56d7a0872cf5ea6770456206c917cee8bf8233a1a7d229b055f6310c61b63936` |
| Guard manifest | `aee1f39799c5248b3f94790093179df1c51f8232e5453ad36af313644000f152` |

Ignored receipts: `conker/build/game-bending-quad-1513F114-match/` and adjacent
private source screens/review. The seven-check commands are
`python3 conker/build/game-bending-quad-1513F114-match/validate_animation.py mounted preinstall`
and the corresponding `sibling` / `installed` runs. Production uses actual
Make, literal full-image prediction, linked recount and post-commit audit.

Next: **func_1513FAB4**, a related **336-word / 152-byte-frame** oriented
quad routine, VA 0x1513FAB4..0x1513FFF4, ROM 0x16CF64..0x16D4A4. Graphify
shows wrappers func_1513FA2C/func_1513FA70. Audit their actual register/float
interfaces and the complete direction helper before choosing its C signature.
It remains a production stub and is uncredited pending full qualification.
