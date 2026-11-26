# Random target callback match - 2026-11-26

`func_1518F1A0` replaces the zero-return placeholder in
`conker/src/game/generated_1BA1D0.c`. The linked **121 words / 484 bytes** and
all **20 binding positions** match retail with the original **32-byte frame**.
**107 words emit directly from semantic C; 14 checked guards** normalize a
closed group of RAM reads, equivalent field addresses and pure address work.
VA `0x1518F1A0..0x1518F384`, ROM `0x1BC650..0x1BC834`, no alignment tail,
insertion, omission, Makefile or compiler-profile change. All 60 raw/padded
neighbors and pools stay fixed; 58 original exported jump labels are retained.
The existing guard CSV is preserved byte-for-byte as the new manifest prefix.

Production recount: **4,699 / 5,528 (85.00%) total** and
**4,026 / 4,855 (82.92%) Game**. Init 492/492, Debugger 181/181,
zero address drift, 829 still different. **85% is reached; the active goal
is 90%, requiring 4,976 accepted matches, 277 more.** This change earns one
matching credit; conversion rows and all denominators stay fixed.

The recovered ABI is `s32 func_1518F1A0(u8 *record)`, matching the actual
generic byte-pointer callback table. The 320-byte record has an animation
rate at 0x24, float outputs at 0x2C/0x30, and a 48-byte target block at 0x110.
Local type/field names describe measured roles; original source names remain
unknown. Three signed16 clocks at 0x12C/0x12E/0x13C subtract live
`D_800BE9E4` with modulo 16 truncation. Explicit unsigned32 intermediates also
preserve the final animation-rate addition without C signed overflow.

An expired split clock is reset by an unsigned RNG draw modulo 6. Another draw's
low two bits select between `splitA..pivot` (nonzero) and `pivot..splitB`
(zero), followed by a float RNG sample. The other expired clocks reset by
unsigned draws modulo 17 and modulo 15, then refresh their float targets.
The three smoothing coefficients are the original fixed data at
`D_800A7B68`/`6C`/`70`, bits `3EB7CED9`, `3E3E76C9`, `3E6C8B44`.
The animation rate uses signed32-to-float conversion under the current rounding
mode and truncation back to signed32. Returning1 keeps the record alive.

There are no aligned direct JAL patterns in the ROM. The aligned pointer at
ROM 0x22E844 is actual Game-data `D_80089D60[9]`, VA 0x80089D84, established
by section ownership, the 44-word callback table and the retained data ASM.
Its bits happen to decode as a branch when treated as instructions; that
does not make this data an executable branch. The complete 195-word dispatcher
`func_1513CFE4`, VA 0x1513CFE4..0x1513D2F0, calls this second-table entry at
0x1513D090, resumes at 0x1513D098, consumes its status, and uses rate0x24 to
advance the animation cursor. The aligned-pattern census does not rule out
compressed, script-driven or derived references.

The first complete C body had the correct size/frame but19 differences.
Inlining float RNG calls in their expressions recovered the original FP operand
order, and a compound final addition recovered its integer operand order.
Ordinary declaration/scope/pointer-view/register-hint variants did not remove
the remaining14 words. The selected body has no invented padding objects,
dummy local, physical register assignment, changed FP operand or profile.

The 14 offsets are30,A4,A8,AC,B0,B4,B8,BC,C0,C4,C8,CC,D8,DC (hex).
Retail computes S0=record+0x110 at the branch-likely delay and join; raw C
loads splitValue there and computes that address later. The target read uses
S1+0x128 instead of S0+0x18. The firstTimer read is advanced over a disjoint
splitValue store, and its SH/LH use S1+0x12C instead of S0+0x1C.
The fields at 0x30(4),0x128(4),0x12C(2) are disjoint for every common valid
record base, and no observer call intervenes. All control/call words and
positions and every COP1 arithmetic/conversion/transfer word and relative
order remain identical. No FP commutative rewrite or new operation is used.
Three guarded raw relocation positions and their moved replacements are
explicitly checked. **Raw scalar-read/fault order differs; raw fault identity
is not claimed.** Normalized literal private/fault states are qualified.

Validation:

- Both complete production padders,60 neighboring functions, all pools and
  the actual three-command Make recipe agree. Four existing Warning712
  signatures at the two `func_1518E4A0(arg0)` and two `func_15190454(arg0)`
  calls remain, with zero new diagnostics or warning suppression.
- Guest: 1,096 cases per five streams; all 121 target instructions execute.
  Four literal streams have identical complete private memory, GPR/FPR,
  HI/LO, FP/FCSR, trace and144 access-fault prefixes. Raw completion state,
  register state and write order agree with retail. An independent full-body
  reference compares public memory, calls, ordered FP operations, FCSR and
  return. Cases include all rounding modes, existing flags, unsigned high-bit
  draws, timer/rate wrap, opaque provider mutations of live fields/globals,
  and aliases between record output fields and the global delta. Invalid
  guest conversions use a bounded software model, not hardware acceptance.
- Native: actual recovered byte-pointer C and typed 320-byte state in three
  units,4,096 cases at O0/O2/O3, strict aliasing/FP, UBSan traps and LTO type
  checks. Full arenas, canaries, globals, call sequence, return and MXCSR agree
  over all four rounding modes with finite signed32-conversion inputs. Opaque
  `noipa` providers preserve call boundaries and mutate live state. Eight
  deliberate semantic changes all finish with comparison exit42; no compiler
  error, signal or trap counts as detection. An initial control exposed that
  two high-bit RNG values have the same residues modulo 6 and7; adding draws
  6/17/15 made the modulo controls effective without changing production C.
- Complete original dispatcher195/frame32 is pinned to ASM/ROM/frozen ELF.
  The second callback table's176 bytes are likewise pinned.432 cases per
  original/raw/normalized stream include108 connected children each and158
  parent instructions, comparing an independent complete-parent reference.
  Inactive/absent callbacks, lifetime, both fade fields, animation wrapping,
  bounce/removal and late rate use are included. Zeroing the callback return
  and inverting its status consumer independently cause record release.
  Other nonzero callbacks, exit callbacks and unvisited parent paths are not
  newly qualified; complete parent execution on these bounded paths does not
  mean all 195 instructions or all possible paths were exercised.
- Both padders reject28 guarded-word and6 guarded-binding corruptions and
  expose214 unguarded-word and34 unguarded-binding changes. Twenty independent
  GNU links and100 guest rebases cross jump regions and signed-low carry
  seams. Both padders reject oversized bodies. Guards cannot hide changed
  preimages or bindings. RNG helpers remain opaque services; their retained
  ASM/ROM/ELF pins do not establish original RNG execution or helper credit.
- The independent frozen old-C plus original-ASM image prediction equals
  the complete private and production ELF: **448 changed bytes, zero
  exclusions**. All 189,088 protected data bytes across 720 owners stay fixed.
  ELF SHA256: `e22da1ad7bd44ee8e075b1bb6ddbf9701501f993ca6eb3d7e9680cf933473eda`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 113.164 s | 5 fresh / 0 reused |
| preinstall-sibling | 105.216 s | 5 fresh / 0 reused |
| installed-primary | 98.677 s | 5 fresh / 0 reused |
| installed-sibling | 104.709 s | 5 fresh / 0 reused |

All 20 packaged target tests are fresh with identical primary/isolated-sibling
source, task, import and data fingerprints. Shared tools-check passes. Prior
unchanged broad-suite receipts are reused explicitly, not called fresh.
The first isolated caller fixture resolved an older helper's ROM path inside
the tools overlay. A scoped consumer-root binding corrected that fixture;
both complete pre-install suites were rerun after the correction. The original
failed receipt remains private. No production-C or reference-semantic change.
Frozen inputs: 3995; copies: 2928. The separately
dirty real tools sibling remains intact. Tools commit:
`5a3249d0cdd658ec640930388900bc3185dc0345`. Baseline consumer:
`69f6c16afcf225d8b095367200c1cc8fbcb43be3`. Detailed receipts remain in
`conker/build/game-random-targets-1518f1a0-private`.

Zero Claude calls and no subagents for this routine. The historical generated
host target is still an empty stub and its active implementation is unqualified.
No host transfer/build/launch or Release change. Scoped Graphify extraction
audits all 61 owner definitions and preserves old IDs/qualification metadata
after observing actual hook termination; no full-corpus extraction claim.
No push, gameplay or hardware acceptance. README changes only its aggregate
rows/date. Continue to90% from the sealed checkpoint with a fresh small
unmatched Game function; protect all accepted work and frozen baselines.
