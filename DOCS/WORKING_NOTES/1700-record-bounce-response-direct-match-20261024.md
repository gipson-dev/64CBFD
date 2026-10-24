# Record Bounce Response Direct C Match

Date: 2026-10-24. Consumer predecessor `f3d362ed`; tools predecessor
`060e1103`. Qualification tools committed first as
`b844373aad221cd0c0c8afffe28cd7d8ed83b20f`. No push requested/performed.
Routine work, zero Claude calls; no dependency/provider/host changes.

## Recovered Routine

`func_15131B7C`, `conker/src/game/generated_15D730.c`, replaces a three-word
zero-return placeholder with the complete collision bounce response.
VA `0x15131B7C..0x15131C2C`, ROM `0x15F02C..0x15F0DC`, exclusive ends:
176 bytes / 44 words / frame zero / four bindings, no alignment tail.

Recover `s32(BounceRecord15D730 *,void *,f32 *,BounceResponse15D730 *)`.
Use local record and response views, retaining the original function name.
Record extent is +0x3C, position +0x40, velocity +0x58, vertical acceleration
+0x64 and motion flags +0x68. Response flags and signed selector are +0/+1;
the damping factor is +4. No shared-header changes. The neighboring original
update at VA `0x15130448..0x1513045C` adds +0x64 times timestep to vertical
velocity, establishing the acceleration field's name rather than guessing spin.

1. Set height to point Y plus extent times original `D_800A3848`, bits
   `0x3D75C290` (single-precision 0.06000000238).
2. Multiply X velocity by response damping, Y velocity by its negation and
   Z velocity by damping. Preserve each separate factor read: a preceding
   velocity store can affect a later factor under guest overlap.
3. If absolute resulting Y velocity is strictly below original `D_800A384C`,
   bits `0x3FFF9DB3` (1.997000098), clear XYZ velocity and vertical acceleration.
   Then clear response bit 0x1 and motion bits 0x6 with late byte/word reads.
4. Return exactly one on both paths. The surface argument is unused by the
   body, but its full incoming A1 word is stored in the original home slot.

The typed reconstruction emits all 44 words directly on the first compile
under normal IDO O2/g3; the flat byte-pointer screen has nine differences.
Retain the existing local `fabsf` intrinsic convention. No guards, barriers,
inline assembly, new pools or compiler-profile changes. All 44 words are
reachable and exercised. Constant HI/LO bindings are +0x4/+0x8 and +0x1C/+0x64.
Raw original/C payloads and bindings match before address resolution.

Raw payload SHA-256:
`ff79a72beafa40d94c90ee7fac65bb04abb23430f99663e182370c2dcbe1c1ae`.
Resolved retail body SHA-256:
`e1adeb742171d46200f4c823be8ceb15e514f780f3d7ea51d3a42bc27e686ee6`.

## Callback And Caller Boundaries

An aligned full-ROM scan finds no direct JAL site and exactly one pointer,
at ROM `0x22E334`: slot zero of `D_80089874`, VA `0x80089874`. This is not
the neighboring `D_80089878` byte-command callback family.

Execute all 78 words of original `func_151319C4`, frame 64, in 640 phases.
It checks response flag 1, the signed selector/-1 gate, a non-null table
entry and record height below surface height. The first position query can
return zero; otherwise a second bounded query adjusts a local point and
record +0x80. On success it builds a local three-float callback point, reloads
the signed selector and callback, passes record/surface/point/response and
narrows the callback's result to a byte.

Cover active/inactive, signed selector boundaries, null callbacks, height and
both provider-result gates, two stack phases and provider mutations. Verify
the actual retail slot-zero pointer; nonzero/negative selector table entries
are controlled fixtures, not a claim that arbitrary retail selectors are safe.
`func_1514672C` and `func_15046C80` remain bounded providers; no claim of
their full engine behavior. Parent C is still a placeholder and uncredited.

## Focused Qualification

Both primary and older-mirror tools copies pass eight fresh checks before
and after installation: no errors, failures, skips or reused checks.
Pre-install primary/mirror: 18.462s / 18.007s; installed: 19.609s / 18.828s.
Both shared project-tool checks exit zero. Reuse the established MIPS/FPU,
fault-prefix, native32, object/pool, relocation and ordinary padder helpers.

- 11,776 root phases cover strict threshold/equality boundaries, signed zero,
  denormals, positive/negative/zero damping, all response-flag bytes, eight
  guest alias layouts and both ordinary stack phases. Check an independent
  ordered public model plus complete original/C private state and return.
- Three additional nonfinite Y-velocity cases qualify ordered guest-model
  behavior only, not FCSR, hardware NaN payloads or complete gameplay.
- Native32 O0/O2/O3 trap UBSan runs 1,792 direct plus 1,792 typed-callback
  cases per optimization, ten effective wrong-C controls and full typed
  backing/offset assertions. Check all reserved bytes and unchanged inputs.
  Guest aliases are separate, not portable native typed-overlap claims.
- Eighty-eight fired root-access fault prefixes check literal private state
  and access boundaries. Three arbitrary unused surface words, including
  zero/high bits, establish no surface dereference in the emitted root.
  Do not claim portable C fault semantics or full native parent C.
- Nine independent GNU links compare assembled original, qualified padded
  and actual Make objects at three code/constant layouts, with HI/LO carries.
  Twenty-four rebased phases preserve all four bindings and public behavior.
- Eleven strict image corruptions reject header/tail/code and each of the
  four symbol/string records in the closed serialization prediction.

The private cache runner initially retained the previous tool glob; correct
it before qualification. The first relocation fixture used the emitter's
wrong argument shape; its corrected version then exposed default GNU text
alignment at non-16-byte entries. Use the existing explicit SUBALIGN(4)
linker-script pattern and rerun successfully. These were fixture failures;
no production semantics or image-preservation requirements were relaxed.

## Closed Image And Production

The complete independent and production ELFs agree on 159 changed bytes:
130 target code bytes and 29 metadata bytes, zero exclusions. Target extent
12 to 176 accounts for one byte. The other 28 are two closed adjacent
symbol/string exchanges: `D_800A3848` with `D_80095B48`, and `D_800A0BD0`
with `D_8009E810`. Validate both original record tails, string positions and
eleven-byte names before predicting their exchanges. Counter-compare every
named definition, including duplicates; only the target extent may differ.
No address, definition, section or unrelated symbol is discarded or masked.

Advance only the previous checkpoint's three authorized source/object/ELF
overrides. Seal 15,966 files, then add the two owned tools in both copies:
15,970 files / 29 focused inputs / all 1,454 linker objects. Verified Linux
cache and checked native stdin/tar bridges avoid DrvFS project reads.
Preserve all 1,612 old mirror dirty paths/statuses/hashes/HEAD; only the two
owned modules are added, now 1,614 paths. Do not commit/reset that mirror.

Actual shadow Make uses five normal commands, including GLOBAL_ASM pre/post
processing for the two retained assembly functions, ordinary generated
padding and GNU assembly. All 31 compact functions and complete padded
object agree with qualification. Preserve all 30 raw/padded neighbors and
pools. Isolated diagnostics are empty, whole-owner diagnostics unchanged.
Inherited duplicate generated_12D630 recipe warnings remain.

Production Make exits zero in 0.670s. Preserve all other 6,054 bodies, all
6,055 addresses and protected Game data: 720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The entire guard CSV remains unchanged, SHA-256
`6d19dfd5806dedfc839f6c7e33f8fb2d1123d826021b93505bd7a265e516f427`.

Audit all 15,970 native files around adoption with exactly three overrides:
source, target object and ELF. Re-capture the actual live adopted ELF and
freshly recount that stream, not an inferred +1.

Installed ELF SHA-256:
`89ed50475949eb6e7211cfdc8bfd15b72d56b7fb2f97bcd8e772101f9dbb074e`.
Installed target object SHA-256:
`b0fceadfeed31bf48d4593c78bb0867280a54b28a242b4c2577b97992fcedccf`.

Root README changes only Total/Game aggregate rows. Detailed recovery
updates stay in DOCS. Host Release, saves, configuration, private inputs,
providers and packages remain untouched.

## Measured Progress And Resume

| Section | Byte-Exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,777 / 5,505 (68.61%) | 0 | 1,728 |
| Game | 3,104 / 4,832 (64.24%) | 0 | 1,728 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Remove only `func_15131B7C` from the live-ELF-pinned queue. Remaining source
screens: 1,599 placeholders, 120 semantic/other and nine unlocated entries.
Next real placeholder is `func_151BA468`, `generated_1E73B0.c`, 44 words;
it is not qualified here. `func_1510D8C0` has a `Gfx *` definition missed
by the parser and stays a separate uncredited matching case. Keep the
92-word `func_1509E730`, 862-word `func_1508CAD8` and unmatched 121-word
`func_15169070` C separate. Target 4,129 exact C functions: 352 more needed.
Goal remains active and incomplete.
