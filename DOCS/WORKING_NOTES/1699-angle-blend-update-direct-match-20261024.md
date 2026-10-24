# Actor Angle Blend Direct C Match

Date: 2026-10-24. Consumer predecessor `f53d6605`; tools predecessor
`3f7fb091`. Qualification tools committed first as
`060e1103d14909db42c6e5dffa6bf17b36cc1d36`. No push requested/performed.
Routine work, zero Claude calls; no provider, dependency or host changes.

## Recovered Routine

`func_1512C150`, `conker/src/game/generated_157840.c`, replaces a three-word
zero-return placeholder with the complete actor angle blend update.
VA `0x1512C150..0x1512C200`, ROM `0x159600..0x1596B0`, exclusive ends:
176 bytes / 44 words / frame 24 / five bindings. There is no alignment tail.

Recover `void(struct108 *actor)` using the existing structure and fields:
flags +0x240, target angle +0x37C, current angle +0x384 and blend factor
+0x5CC. Retain the address-named entry and canonical angle-helper symbol.
No broad structure/header repair, new helper or new floating-point pool.

1. Add original `D_800A3694`, bits `0x3BC49BA6` (single-precision 0.006),
   to the blend factor, then clamp values greater than one to exactly one.
   This is an upper-only clamp; preserve negative and ordered-NaN behavior.
2. On exact factor equality with one, assign original `D_800A3698`, bits
   `0x4479C000` (999), to the current angle and clear only flags bit 0x2.
3. Otherwise call `func_15048A70(current,target)`, multiply its delta by the
   late-reloaded blend factor and add it to the late-reloaded current angle.
   Preserve separate single-precision rounding and the actual float ABI.

Putting the completion assignment before the flag clear recovers the exact
retail schedule under ordinary IDO O2/g3. The first draft had 21 differences;
the final clean body has none. No word guards, inline assembly, volatile
barriers, special compiler profile, inserted instructions or assembly replacement.

Preserve the literal unreachable duplicate words at +0x44 and +0x78.
All 42 reachable root words are exercised; both duplicates remain included
in the complete 44-word match, not excluded or claimed as visited.

Bindings remain step HI/LO at +0x10/+0x14, sentinel HI/LO at +0x1C/+0x60
and helper JAL at +0x80. Independently assembled original and raw C payloads
and bindings are identical before resolving addresses.

Raw payload SHA-256:
`45802c6cfb72bd08e36109489194d51877d6c25c29e93b4133f36af97b5f63b7`.
Resolved retail body SHA-256:
`e5cf6761014c9f9998563a3ca70ed25527a2e0b2075a96fcf5f1d78bf61d19d5`.

## Caller And Helper Boundaries

An aligned full-ROM scan finds exactly three direct JAL sites, at ROM
`0x1504FC`, `0x156FD8` and `0x1595E8`, and no literal function pointer.
The first two set A0 from S0 in the delay slot; the third already has the
actor in A0. Their immediate continuations use no return value. Only call
windows are audited for the first two large routines, not complete execution.

Execute the complete original 58-word `func_1512C068` in 96 phases. Its
heading selects +2/-2; kinds 0x40/0x80 skip distance preparation. Otherwise
it computes planar distance, writes +0x370 and, below 42, resets the blend,
sets the initial target-offset angle, calls `func_15123A54`, then ORs bit
0x2 into the late flags value. It always invokes the recovered root.
Exercise distances 0/41/42/43, heading/kind gates and orientation-provider
mutations. Visit 57 words; its duplicate MTC1 at +0x38 is unreachable.
The orientation service remains a bounded provider. The caller's C body
is still a placeholder and receives no restoration or matching credit.

The unchanged 24-word `func_15048A70` is already byte-exact. It returns
target-current after a single angle fold when current-target is >180 or
<=-180. Do not replace this with repeated modulo wrapping. Execute 405
connected phases over boundary and multi-turn angles; visit 23 words,
preserving its unreachable duplicate MTC1 at +0x30. Compile its actual C
body with the root in native tests, rather than substituting the guest hook.

## Focused Qualification

Both primary and older-mirror tools copies pass eight fresh checks before
and after installation: no errors, failures, skips or reused checks.
Pre-install primary/mirror: 13.302s / 13.095s; installed: 14.004s / 14.195s.
Both shared project-tool checks exit zero. Reuse existing MIPS/FPU,
fault-prefix, native32, relocation, parser, pool and generated-padder helpers.

- 4,464 guest root phases cover float32 clamp/equality boundaries, signed
  zero, denormals, angle-fold thresholds, flags, helper mutation, four
  big-endian alias layouts, two stack phases and private owner-home redirection.
  Independently check public semantics plus complete original/C private state.
- Three additional nonfinite-factor cases cover ordered guest-model behavior,
  not FCSR exception modes, hardware NaN payload guarantees or gameplay.
- Native32 O0/O2/O3 trap UBSan runs 2,184 direct and 2,184 typed-wrapper
  cases per optimization, with ten effective wrong-C controls. Use full
  `struct108` storage, compile-time field-offset assertions and unchanged-byte
  checks. Do not claim native private-home aliases or complete native parent C.
- Forty-two fired root-access fault prefixes compare literal original/C
  private states and access boundaries. These are emitted-instruction checks,
  not portable C fault semantics.
- Nine independent GNU links compare original, qualified padded and actual
  Make objects at three address layouts, including HI/LO carry boundaries.
  Eighteen rebased phases preserve all five bindings and helper arguments.
- Seven image corruptions fail closed, including header/tail/code and both
  symbol/string records involved in the exact serialization prediction.

The initial caller test incorrectly assumed the one inspected site was the
only direct caller. Full-ROM evidence identified two more; correct the
inventory to three and audit their actual argument/continuation words before
qualification. No production semantics or preservation gate was relaxed.

## Closed Image Accounting

The independent link changes exactly 163 bytes: 148 target-code bytes and
fifteen metadata bytes. One metadata byte changes target extent 12 to 176.
The other fourteen belong to a closed two-name symbol/string serialization
exchange between `D_800A3698` and `D_8009ED98`, triggered by the first C
reference to the completion constant.

Validate both predecessor records, adjacent symbol/string positions and
eleven-byte NUL-terminated names. Predict the exchange of the record tails
and strings while retaining each serialized st_name position. Compare a
Counter of every named definition, including duplicates: only the target
extent may change. Neither constant's value, address or section changes.
The final full ELF equals this byte-for-byte prediction with zero exclusions;
do not ignore whole symbol/string sections or silently mask the exchange.

## Production And Preservation

Advance exactly the previous checkpoint's four approved source/guard/object/
ELF overrides, then seal 15,962 files. Add only the two target tools modules
in both local copies: 15,966 files / 28 focused inputs / all 1,454 linker
objects. Use verified Linux cache and checked native stdin/tar bridges;
no DrvFS project reads. Preserve all 1,610 old mirror dirty paths, statuses,
hashes and HEAD; only the two owned new modules are added, now 1,612 paths.
Do not reset or commit that independent mirror.

Actual shadow Make uses the normal three-command IDO O2/g3 generated-slice
recipe. Complete compact/padded owner outputs match qualification; preserve
all 14 raw/padded neighbors and pools. Isolated diagnostics are empty and
whole-owner diagnostics unchanged. Inherited duplicate generated_12D630
recipe warnings remain, not a warning-free build claim.

Production Make exits zero in 0.587s and reproduces the strict independent
image. Preserve all other 6,054 bodies, all 6,055 addresses and protected
Game data: 720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The entire guard CSV remains unchanged, SHA-256
`6d19dfd5806dedfc839f6c7e33f8fb2d1123d826021b93505bd7a265e516f427`.

Audit all 15,966 native entries around adoption with exactly three overrides:
target source, target object and linked ELF. Re-capture the actual adopted
ELF and freshly recount that stream, not an inferred +1.

Installed ELF SHA-256:
`26c6992d9fb1e6f8f3c7b729db1af9e5e0934c245d0a8cdd84f9fe9334dc1343`.
Installed target object SHA-256:
`6933db56f5c3e12714111cebb2c5d8b7aebdbf3e3a7197c2a97a17536149a6c1`.

Root README changes only its Total/Game aggregate matching rows. Detailed
progress belongs here and in DOCS indexes. Host Release, saves, configuration,
private inputs, provider settings and packages remain untouched.

## Measured Progress And Resume

| Section | Byte-Exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,776 / 5,505 (68.59%) | 0 | 1,729 |
| Game | 3,103 / 4,832 (64.22%) | 0 | 1,729 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Remove only `func_1512C150` from the live-ELF-pinned queue. Remaining source
screens: 1,600 placeholders, 120 semantic/other and nine unlocated entries.
Next real placeholder is `func_15131B7C`, `generated_15D730.c`, 44 words.
It is not qualified by this checkpoint. `func_1510D8C0` already has a
`Gfx *` definition missed by the parser and remains a separate uncredited
matching case. Keep `func_1509E730` (92 words), `func_1508CAD8` (862 words)
and unmatched `func_15169070` C (121 words) separate. Target 4,129 exact C
functions: 353 more needed; goal remains incomplete.
