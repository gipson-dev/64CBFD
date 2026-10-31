# Cosine height delta restored directly from C

Date: 2026-10-31. Function `func_151162D4`, owner
`conker/src/game/generated_142560.c`, retail assembly `conker/asm/142560.s`.
VA `0x151162D4..0x151163C0`, ROM `0x143784..0x143870`.
All 59 words (236 bytes) emit directly from semantic C under the retail O2/g3
profile. There are no new guards, insertions, omissions or alignment words.
The frame is 40 bytes, RA is saved at SP+20, the previous signed height at
SP+30, speed at SP+32, amplitude at SP+36, and the record pointer in its
incoming argument home at SP+40.

## Recovered behavior and interface

`void func_151162D4(CosineHeightRecord *record)` takes one record. The private
record view names its signed height at +0x12, float offset at +0x18, packed
parameters at +0x3C, signed output delta at +0x5C, and unsigned phase at +0x7C.
It truncates the prior height-plus-offset to a signed halfword, snapshots the
signed low-halfword amplitude and unsigned high-halfword phase speed, then
calls `cosf` with the signed interpretation of the phase multiplied by
`0.0054931640625f` (word `0x3BB40000`). The cosine result times the cached
amplitude becomes the new offset. The phase advances with wrapping 32-bit
speed-times-ticks arithmetic. Finally, the integral change from the captured
old height is stored in the signed output halfword.

The snapshots are significant: the provider can alter the record or tick
global. The new height and phase are reloaded after the call; amplitude, speed
and prior integral height remain the original snapshots. The signed phase
conversion and intermediate halfword narrowing are explicitly retained.
Local declaration order, the typed record and the explicit low-halfword mask
recover the original register allocation without binary normalization.

`func_1511A738` is the original 34-word direct caller. Its call at
`0x1511A798` ignores the return and forwards the record and its +0x80/+0x84
fields to `func_1511A494`. The typed caller cast is word-neutral. The provided
retail input contains one aligned direct JAL at ROM `0x147C48` and one aligned
literal pointer at `0x22D8DC` / VA `0x80088E1C`, row 33 of the 12-byte callback
table starting at `0x80088C90`. The census is scoped to the provided input.

## Qualification evidence

- Raw C, original assembly, padded owner and actual-Make object agree across
  three GNU-linked address layouts, including HI/LO carry boundaries. There
  are three bindings: the cosine call and the tick global's HI/LO pair.
- Guest reference: 1,152 ordinary cases / 4,608 executions, all 59 root words
  visited, ten global/record alias cases, and 80 fault-prefix cuts. This
  routine has no memory operation in a branch delay slot; zero such cuts are
  reported. Literal register, FP, HI/LO, memory, call and access states agree.
- The complete original 34-word parent runs for 96 cases / 1,536 executions.
  Four poisoned return values demonstrate the ignored-return interface.
  Lookup/reset and follow-provider behavior remain bounded hooks.
- The original 88-word cosine slot, including its 85-word body and retained
  padding, is connected for 64 cases / 256 executions using original retail
  constants and an independent cosine reference. These cases visit 62 helper
  body words; complete helper-path coverage is not claimed.
- Native32 runs 262,145 finite cases each at O0, O2 and O3, with trapping
  UBSan and float-cast-overflow checks. All 65,536 amplitude and speed
  halfwords are exercised, with full record/canary and provider-argument
  checks. A directed narrowing/rounding boundary distinguishes a signed
  halfword prior height from a 32-bit temporary. All 15 compiled negative
  controls fail through semantic mismatch (exit 1).
- Both tools copies pass eight fresh canonical methods and shared tools
  checks. After production installation, two checks run freshly in each
  copy; six unchanged checks are reused only under complete input, module
  and artifact fingerprint equality.
- The complete owner retains all 83 raw/padded neighbors and normalized
  pools. The five actual Make commands reproduce the qualified object.
  Target/compiler/assembler diagnostics are empty. The dry Make plan retains
  two pre-existing duplicate-recipe warnings unrelated to this owner.
- Strict full-image prediction has zero exclusions: 173 changed bytes =
  172 target-code bytes + one symbol-extent byte, with no metadata reorder.
  All 6,055 other bodies and all function addresses remain fixed. All
  189,088 protected Game-data bytes and 720 owners remain exact. Progress
  CSV, the entire guard manifest and shared headers remain unchanged.

The model covers finite, defined float-to-s32 conversions and the guest's
low-halfword stores. It does not establish portable C alias/fault behavior,
complete hardware FCSR flags/traps, or gameplay acceptance.

## Banked state and continuation

Predecessor consumer `9834c97aafe697128aef91524ba49b2f3ec4b450`.
Tools committed first at `76e2b88b02b44b47ddbeb42753d0306efad4a43d`; the older dirty mirror is preserved without
committing it. Actual production ELF SHA-256:
`b8bdfa1266b65b7c09471ca5606a00d4461ecd29093e099ca39ec7ef6c6d5a8f`.

Actual recount: **3,980 / 5,506 (72.28%)**, Game **3,307 / 4,833 (68.43%)**,
Init 492/492, Debugger 181/181; zero drift, 1,526 different and **150** more
needed for 4,130/5,506 (75%). The goal remains active. Next private screen:
`func_150B5950`. Build evidence is under
`conker/build/game-cosine-height-delta-151162D4-match/`. Historical completed
builds are restorable from the sibling `64CBFD Build Archive`. No push.
