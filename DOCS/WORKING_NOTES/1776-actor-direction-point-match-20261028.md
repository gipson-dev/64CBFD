# Actor direction point — direct C match

Verified 2026-10-28. Restore `func_15107A20` in
`conker/src/game/generated_133190.c`: VA 0x15107A20..0x15107AE0,
ROM 0x134ED0..0x134F90, 48 words / 192 bytes, frame 56 and saved S0.
All words emit directly under the existing O2/g3 profile. No guards are added.

## Recovered interface and behavior

`void func_15107A20(struct127 *actor, s16 yaw, s16 pitch, vertex *point, struct17 *originOut)`

Query the actor origin and radius through `func_1515C244`, then build a
radius-scaled direction through `func_15143794`. Multiply point.y by the
actor's late-read +0xF0 scale, add the three queried origin components, and
optionally copy the complete origin. Preserve the canonical 812-byte actor
and distinct 12-byte vertex/struct17 types. Shared headers are unchanged.
The otherwise unused second scale is still supplied to the origin provider.
The original fifth-argument home is read after the second helper.

The two J26 bindings remain at +40 (origin) and +60 (direction). Compiler
and original object body SHA-256 are both
`57821ffdd6ebe93f9decc67ea990a48d788c2ffd6b639d2d74174b5f6340b153`.

## Original callers and retained helpers

A complete ROM call census finds two direct sites and no pointer literals:

- `func_15107700`: site VA 0x151077D8 / ROM 0x134C88. Execute its
  121-word original extent across 128 cases. Verify the actor-availability
  gate, signed angles/lifetime, default lifetime 300, unaligned four-byte
  copy at every alignment, stack point/origin outputs, all 15 ray arguments,
  miss/factory failure/success, the 80-byte descriptor, actual fractional
  point interpolation, extension copy, and final return.
- `func_15107924`: site VA 0x151079A0 / ROM 0x134E50. Execute its
  63-word original extent across 48 cases. Verify inactive/stale actors,
  signed angles, NULL origin output, equal points, independent changes in
  each axis, change-byte stores, interpolation, and final return.

The current C parents remain zero-return placeholders and receive no credit.
Original-path execution reaches 119/121 and 62/63 words. The unreachable
ordinary duplicates at 0x15107744, 0x15107870 and 0x15107970 follow branches
whose corresponding delay-slot stores/loads already select the joined path.

Five retained helpers are checked against ROM and connected to instruction
execution: origin (41 words), direction (40), trig lookup (27), fractional
points (38), and memcpy (11). Together, 156/157 words execute; the origin
branch-likely delay word at 0x1515C258 is unreachable because the preceding
id < 0xBB test excludes id 0xFF. Retain it unchanged. Use the actual retained
65-float trig table and both fractional-point constants. Another 512 cases
exercise the real origin/direction/trig path, including signed radius and
height boundaries and actor-id cutoffs. Only ray and record-factory providers
are bounded in the caller chains. No full caller C or gameplay acceptance
is implied.

## Qualification and complete-image evidence

Both tools copies pass eight fresh canonical methods and shared tool checks.
Production runs two fresh installed methods per copy and reuses the other
six only after exact module, input and artifact fingerprint comparison.

- 3,108 guest cases cover signed halfword angles, optional output, late
  scale reads, provider changes to argument homes and 36 storage overlaps.
  All 48 target words execute; original and compiled states/traces agree.
- 696 fired access-prefix pairs preserve complete registers, memory, calls,
  PC and delay-slot context. A NULL optional output causes no output read/write.
- Native32 O0/O2/O3 each pass 76,800 cases and seven effective controls,
  with trapping UBSan, canonical types, the five-argument void function
  pointer, complete actor/point/origin fences, and late scale mutations.
- Three independent GNU layouts pass 72 guest cases using original,
  compiler and actual Make objects; both J26 relocations are preserved.
- Four actually compiled IDO mutations fail semantic expectations. Three
  raw body/binding controls and six complete-image corruptions are rejected.

The 37-function owner preserves all 36 neighbors, pools and eight GLOBAL_ASM
routines. Its existing `RETAIL_RODATA_SYMBOL=D_800A2420` setting is required
when applying the real padder, preserving the interpolation constants'
relocations. Actual Make executes five commands and reproduces the qualified
padded object exactly. The selected function has no compiler diagnostics.
The owner retains exactly two inherited Warning 712 diagnostics in
`func_1510764C` and `func_15107678`; only source line numbers shift.

The sealed production audit verifies 16,323 paths, with 330 focused frozen
inputs. An independent byte-level prediction matches the complete linked
ELF with zero exclusions: 143 code bytes plus one symbol-size byte change
(12 -> 192). All 6,056 function addresses, the other 6,055 bodies, and all
720 protected Game data owners / 189,088 bytes remain fixed. The inventory
CSV and complete existing guard manifest are unchanged.

Guest overlaps/fault probes qualify emitted instruction order, not portable
C alias or hardware exception semantics. Native providers are bounded;
IEEE model agreement is not hardware NaN payload/FCSR or gameplay proof.

## Bank and measured progress

Predecessor consumer: `1876db0fabb3b6b0106d4f723d950c48bdd40e4f`.
Tools committed first: `50e7703b103fd769d3cbccc77a57fe64399ead05`.
The older standalone tools mirror retains all 1,769 inherited dirty paths,
with only these three qualification modules added. No push is performed.

Adopted ELF SHA-256:
`a0fc94c6245861327c84b0ed12cdf8f4a7b1fad91a25045a838620ccf8a68ac5`.
Raw receipts live under `conker/build/game-actor-direction-point-match/`.

| Section | Byte-exact C | Different | Address drift |
| --- | ---: | ---: | ---: |
| Total | 3,854 / 5,506 (70.00%) | 1,652 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,181 / 4,833 (65.82%) | 1,652 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

These totals come from the adopted native ELF, not the isolated candidate.
The 75% threshold remains 4,130 exact C functions: 276 more are required.
Next inspect `func_151DC8BC` in `generated_209B50`; its queue position is
only a screen. `func_1514E920` stays parked and uncredited.
