# Parity descriptor constructor restored directly from C

Date: 2026-10-31. Target `func_151A90C0`, owner
`conker/src/game/generated_1D4E00.c`, assembly `conker/asm/1D4E00.s`.
VA `0x151A90C0..0x151A91AC`, ROM `0x1D6570..0x1D665C`.
All 59 words (236 bytes) emit directly from semantic C under O2/g3. There
are no guards, insertions, omissions or alignment words. The frame is 88
bytes, RA is saved at SP+28, the one-byte tag buffer starts at SP+40, and
the 40-byte request starts at SP+48. The full selector is preserved in its
incoming SP+92 home. A float parity value and a one-byte array recover the
retail floating comparisons, lifetime and stack layout without padding edits.

## Recovered request and interface

`void func_151A90C0(u8 *owner, s32 selector)` builds a request using the low
parity bit and, after successful allocation, copies the selector's low byte
to the returned object's +0x80 field. Allocation failure makes no copy.

| Request offset | Field | Initialization |
| --- | --- | --- |
| 0x00 | kind byte | 2 |
| 0x04 | owner pointer | input owner |
| 0x08 | primary float | odd: D_800A8F58; even: D_800A8F5C |
| 0x0C | secondary float | odd: D_800A8F60; even: D_800A8F64 |
| 0x10..0x20 | five floats | positive zero |
| 0x24 | enabled byte | 1 |
| 0x25 | signed mode byte | -1 |
| 0x26 | flags byte | 0 |

Bytes 1..3 and 0x27 are padding, not initialized fields. Native tests do not
assign them fixed values. Guest tests preserve the exact seeded padding;
the original allocator entry copies all 40 bytes verbatim. No blanket zero
initialization is added.

The allocator call supplies the request pointer, -1, 1, 255, and a fifth
zero word on the outgoing stack. `func_151A8B20`'s return type is corrected
to `u8 *`; its unfinished null-return body remains unchanged in machine
code. Its parameters stay unspecified until that body is recovered: adding
a full five-parameter definition introduced debug argument-home stores and
was rejected by the neighbor gate. The observed call contract is checked
independently. The callback table and local dispatcher pointer now use the
observed void return interface; the dispatcher's code remains unchanged.

## Caller and qualification

- `func_151A9060` is the original 24-word dispatcher. It sets mask
  0x04 in owner byte +0x16, bounds the signed selector at +0x18 to 0..7, calls a
  non-null entry of D_8008F984, and returns 1. Entries 0..5 point to this
  target; the other two callbacks remain bounded in the tests. The provided
  retail input contains no aligned direct JAL to the target and six literal
  pointers at ROM 0x234444..0x234458. For 384 cases / 6,144 executions, all
  dispatcher words execute, including invalid-index and null-entry controls.
  Four return-poison values prove the callback result is ignored.
- Raw C, original assembly, padded owner and actual-Make object agree under
  three GNU-linked layouts, including HI/LO carry boundaries. All ten
  bindings agree: four float-global pairs and two calls.
- Guest tests run 720 ordinary cases / 2,880 executions, 16 alias cases and
  105 interrupted-access prefixes, including 13 branch-delay cuts. All 59
  target words are visited. Complete GPR/FPR, HI/LO, memory, call argument,
  40-byte payload and access states agree across the four images.
- The original 11-word Init memcpy is connected for 256 cases / 1,024
  executions, including successful allocation and return-pointer aliases.
  All its words execute. The allocator's first ten original instructions
  are separately connected for 32 cases / 128 executions; the original
  memcpy copies the full 40-byte packet into its real private buffer.
  The stop is before the allocator's remaining code, which stays bounded.
- Native32 runs 262,144 cases each at O0, O2 and O3 with trapping UBSan.
  It covers all 65,536 low-selector values with varied high bits, both parity
  choices, allocation success/failure, provider mutations, nonfinite float
  bit patterns, all 36 initialized request bytes, exact argument logs,
  complete owner/output state and canaries. All 15 compiled negative controls
  fail with semantic mismatch (exit 1), not a compiler failure or trap.
- Both tools copies pass eight fresh canonical methods and shared checks.
  After installation, two methods run freshly per copy; six unchanged
  semantic checks are reused only under full input/module/artifact identity.
- All 22 raw/padded neighbors and normalized pools are preserved, including
  the allocator stub and the typed callback dispatcher. Three actual Make
  commands reproduce the qualified object. Executed compiler/assembler
  diagnostics are empty; the dry plan retains two unrelated pre-existing
  duplicate-recipe warnings.
- Strict whole-image prediction has zero exclusions: 311 changed bytes =
  179 target-code bytes + one symbol-extent byte + 131 metadata bytes. The
  metadata changes are five closed named permutations, including exact
  string blocks, at symbol offsets 0x2B1BB4, 0x2B2404, 0x2B7374, 0x2BA0D4
  and 0x2CCC04. Every named definition retains its value, extent, type and
  section except the target's recovered size. All 6,055 other bodies and
  all addresses remain fixed; all 189,088 Game-data bytes and 720 owners
  remain exact. Guard CSV, progress inventory and shared headers are unchanged.

These tests establish the recovered constructor and the stated provider
contracts. They do not establish portable C padding/alias/fault behavior,
hardware FCSR flags/traps, the full unfinished allocator, or gameplay acceptance.

## Banked state

Predecessor consumer `edc4ea45d789efbdc30ee52a718f3df03894a31f`.
Tools committed first at `6291e0bf94dac8dbf451dcfab8b91af15fe8a878`; the older tools mirror's existing work is
preserved without committing that checkout. Actual production ELF SHA-256:
`f5716f71650d84b8c842d382765bbd484a9a1ff0317b33e5d5c8860d8f3dbacb`.

Actual recount: **3,982 / 5,506 (72.32%)**, Game **3,309 / 4,833 (68.47%)**,
Init 492/492, Debugger 181/181; zero drift, 1,524 different, and **148** more
needed for 4,130/5,506. The 75% goal remains active. Next private screen:
`func_151AE2BC`. Evidence: `conker/build/game-parity-descriptor-create-151A90C0-match/`.
Historical completed builds are restorable from sibling `64CBFD Build Archive`.
No push.
