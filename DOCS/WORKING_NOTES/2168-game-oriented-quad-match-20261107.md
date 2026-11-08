# Oriented record quad recovered and directly byte matched

Date: 2026-11-07. Continues [Note 2167](2167-game-billboard-quad-match-20261107.md)
from consumer `265531b75c136cccee09a55c8897b299cfea1b8d` and tools
`ab3c1e9c1f4ffbc6d8d9ebdd6739b5de7e08739c`. One qualified Game recovery
advances the active 80% total goal. Host code and frozen Release are untouched.

## Recovered interface and complete semantic body

`Vtx *func_1513EE14(u8 *actor, s16 view)` replaces the false s32 zero-return
placeholder in `conker/src/game_169510.c`. All **192 words / 768 bytes**
emit directly from C under the existing O2/g3, MIPS2/O32 profile, with
**zero guards**, the original **216-byte frame**, saved RA/S0 lifetimes,
private homes, untouched alignment bytes and all eight literal call bindings.
VA is 0x1513EE14..0x1513F114; ROM is 0x16C2C4..0x16C5C4.

1. Query the view's 64-byte vertex buffer through func_151D5D60, capturing
   the original pointer separately. Return null on failure. If fresh, copy
   the actor's 64-byte template into both buffer halves, capturing the slot
   address but reloading its pointer for the second copy.
2. Build an orientation matrix with func_150A8050 from actor+0x40/+0x44/+0x48.
   Afterwards, load translation from +0x34/+0x38/+0x3C into its last row.
3. Read width/height from +0x2C/+0x30 after that helper returns. Build
   (+W,+H),(-W,+H),(-W,-H),(+W,-H) in a separate corner array.
4. Call func_150A7960 four times with z=0 and separate transformed-point
   outputs. **All four transformations finish before any vertex emission.**
5. Truncate each transformed component to s32 and store its low 16 bits.
   Clear all four flags, advance the live cursor exactly three times,
   and return the separately captured first pointer.

Unlike the related scaled callback in Note 2164, this routine uses a
separate source-corner array, does not scale the matrix rows, and emits
after completing all four calls. A single private scratch structure makes
the original field layout explicit: fresh at SP+0x3F, points +0x40, corners
+0x70, matrix +0x90, first +0xD0 and cursor +0xD4. Three alignment bytes at
+0x3C..+0x3E remain untouched. No filler instructions or frame guards are
used. S0 changes from actor to matrix after the final actor field reads.

Raw SHA-256: `63dd1815127cdc5ce2e6fe1070dd393e2a7aa698a07196e00a82e305bca6a327`.
The eight R_MIPS_26 bindings are at bytes 40 (backend), 96/120 (memcpy),
156 (orientation), and 304/352/396/440 (point transforms). Two independent
GNU links preserve all eight calls at retail and rebased addresses.

## Actual renderer and original helpers

The complete aligned-ROM census finds no direct JALs and one entry pointer:
ROM 0x22E938, **slot 23** of the actual 39-entry renderer table prefix.
Following graphics commands are not classified as function pointers.

The complete **295-word func_1513DB00** calls this selected callback with
actor A0 and signed 16-bit view A1 at 0x1513DC24. It tests and consumes the
returned V0 vertex pointer at 0x1513DC30 before later graphics work.
**That renderer remains a production stub.** Its original execution is
checked against a counterpart with the independent oriented-quad provider;
other renderer services remain bounded. No renderer restoration, full
rendering correctness or gameplay acceptance is inferred.

The complete original **11-word memcpy**, **40-word point transformer** and
**52-word buffer backend** are compared against ROM and the predecessor
production ELF, where all are already exact. Selected cases connect them
directly. All 103 helper words compare and 102 execute. The remaining
backend word supplies a fallback fresh-byte pointer; this caller always
passes its real nonzero byte address. Orientation and allocation remain
bounded providers; no trigonometric-helper or allocator restoration is claimed.

## Focused qualification

Seven checks pass before and after installation in both tools configurations:

* **355 guest cases per body** compare complete public RAM, helper calls and
  pointer return with an independent ordered model. All 192 target words
  execute and complete private machine state agrees. Cover null/reused/fresh
  buffers, signed views/upper bits, corner signs and negative zero, helper
  field changes, copied-slot mutations, live cursor and captured-return homes,
  exceptional casts, template/actor aliases and private-points output aliases.
  The explicit stack output is included in model observations. Null-buffer
  fixtures leave actor/output memory unmapped; all three gap bytes stay fixed.
* **290 original renderer cases per body**, with **128 actual leaf calls per body**,
  check table slot 23 and the pointer/s16/pointer-return interface against
  the independent provider. All 295 renderer words compare; 293 execute.
  Duplicate defaults 115/146 are skipped by both explicit preceding branches,
  whose opcodes/offsets are checked. Hidden-buffer cases cover words 24..34.
* **948 fired access cuts**, including **158 delay cuts**, compare full memory,
  GPR/FPR/HI/LO, PC, delay context and access prefixes. Cover saved RA/S0,
  S0's actor-to-matrix lifetime, escaped cursor/first, incoming view,
  private-point aliases and original-helper execution.
* SDK native32 O0/O2/O3 each pass **216 cases** with Vtx16, pointer32,
  typed services, checked relative scratch addresses, all four calls before
  output, live cursor redirects and captured return, with trapping UBSan.
  Ten compiled semantic negatives reject with exit 1: stub, missing flags,
  wrong query size, translation, corner sign, z input, coordinate axis,
  second-copy offset, cursor advances and return.
* All 192 raw-word corruptions, eight binding corruptions, historical-guard/
  pool/options corruptions and seven whole-image corruptions reject. Two
  independent GNU links preserve all eight literal calls without guards.

Native fixtures use valid disjoint objects and finite representable s32
casts, with round-to-nearest and no FTZ/DAZ. Private homes, aliases and
exceptional casts are separate guest evidence. The float model canonicalizes
NaNs and does not emulate FCSR, NaN payload propagation or hardware exception
behavior. Routine direct matching used zero Claude calls.

## Production, documentation and next target

Freeze 181 inputs, qualify both complete owner compilations and padding,
then run actual Make. All **58 raw and padded neighbors**, pools and
register/options metadata stay fixed. There are 43 paired inherited owner
warnings and no new warning. The one actual O2/g3 owner compilation matches
its predicted padded object and complete ELF byte for byte.

Exactly **537 bytes change**: 535 in this 768-byte Game slot plus two target
symbol-size bytes changing 12 to 768. There are **zero exclusions**, no
symbol/name swaps, and no other definition change. All **6,052 addresses**
and **189,088 protected Game bytes across 720 owners** remain fixed.
The shared headers, complete guard manifest, Makefile and conversion CSV
remain unchanged. `make all` retains expected checksum exit 2 and the
inherited duplicate generated_12D630 recipe warning; this is not a whole-ROM
checksum match.

Both tools copies pass fresh shared smoke checks. Three unchanged shared
regressions per copy are explicitly reused after exact fingerprints. The
new-module overlay and recorded read-only missing-helper fallback preserve
all 2,434 inherited dirty sibling paths.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,238 / 5,512 | 76.89% | 0 | 1274 |
| Game | 3,565 / 4,839 | 73.67% | 0 | 1274 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**172 more exact functions** remain to 4,410 / 80%. README gets aggregate
rows only. Four concise index leads retain their complete history. Refresh
Graphify with scoped, fail-closed legacy-node retention, without claiming a
fresh full-corpus extraction. Commit tools before consumer source/docs/pin,
then verify a fresh hook terminal, clean task trees and stable production.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `1d0e5e42b224b419fd3eea7dde7953a4e567c7d74aab77eb34646340e9200a15` |
| Production binary | `b41553e5cc1edcef9fdf2f88b03381ccb8aa9e2240029ee083aee5b7947d3973` |
| Padded owner | `72cbd99248434055f8775690d7c9175384ad707b91c1e2168419b40ba4aabb95` |
| Unchanged guard manifest | `17a99bdbcac743a6a0830994c31ffde2a4c2f5aee472086617feab423a238279` |

Ignored receipts: `conker/build/game-oriented-quad-1513EE14-match/`;
initial source/ABI/graph screen: adjacent private directory.

Next: **func_1513F114**, the related **231-word** routine with a **144-byte
frame**, VA 0x1513F114..0x1513F4B0, ROM 0x16C5C4..0x16C960. Its retained
body combines view-direction coefficients, actor geometry and a signed
square-root adjustment before emitting vertices. Inspect its full source,
caller ABI, floating-point branches and constants independently. It remains
a placeholder and receives no credit here. Continue the active 80% goal;
preserve private inputs, real saves, unrelated work and frozen host Release.
