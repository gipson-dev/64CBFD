# Owner timeout transition - direct C match

Verified 2026-10-28. Restore func_1519E754 in generated_1CA420:
VA 0x1519E754..0x1519E818, ROM 0x1CBC04..0x1CBCC8, 49 words / 196 bytes.
Normal O2/g3 emits every retail instruction directly, with frame 0x28,
five relocations and no new guards. The first complete semantic candidate
matches in isolation and in its full owner; no compiler-profile change.

## Recovered behavior and interface

The interface is void func_1519E754(u8 *record). The 12-byte
OwnerTimeoutPayload1CA420 at record +0x28 contains an owner pointer,
identity byte at +0x2C and signed elapsed timer at +0x30. Its padding is
explicit; shared headers and existing payload types remain unchanged.

Read the owner's first word and mark retirement when it is zero. Always
compare the saved identity with owner +0x3B, including that zero-word route.
An identity mismatch also retires the record. Invalid links skip the clock,
elapsed timer and owner-state reads.

For a valid link, add D_800BE9E4 to the elapsed timer with 32-bit unsigned
wrap, then interpret the result as signed. State 0x7C at owner +0x84 keeps
the record alive regardless of the elapsed value. Other states retire it;
only a signed elapsed value greater than 200 also calls func_1519E3BC with
owner, duration 300, record group byte +0xC and context byte +1.

After any helper call, use the saved retirement byte. Retiring clears
D_800E0920, sets the signed lifetime at record +0xE to -1 and sets bit 0
of flags at +0xD. Preserve other flag bits, including helper mutations.
The clock declaration is added locally to this owner only.

| Retail property | Qualified result |
| --- | --- |
| Frame / preserved registers | 40 bytes; S0 and RA |
| Saved retirement byte | Frame SP +0x23, across the helper |
| Clock bindings | HI16 / LO16 at function +0x20 / +0x54 |
| Helper call | R_MIPS_26 at +0x84 to func_1519E3BC |
| Global clear bindings | HI16 / LO16 at +0x94 / +0x98 to D_800E0920 |
| Owner preservation | All 22 neighboring functions, bindings and pools |
| Guard manifest | Entire file unchanged |

## Original dispatcher and effect helper

The aligned ROM census finds no direct J/JAL to the target and exactly one
pointer literal: slot 9 of D_8008A4E8, VA 0x8008A50C / ROM 0x22EFCC.
The original 45-word func_15149264 dispatches that one-pointer callback and
ignores its result. Its timer, disabled-selector, destructor and release
routes are exercised in 288 cases, visiting all 45 words. The 98-entry update
table, 10-entry exit table and current dispatcher remain literally retail.

The already restored func_1519E3BC is a 42-word helper. Fifty connected
original-instruction cases visit all 42 words and verify reset, presets 3/4
and controller factory arguments, including group/context bytes and changes
across the helper. Its complete current production body stays byte-exact.
Reset, preset-builder, factory, destructor and release services are bounded
providers in this qualification; this does not claim full-game acceptance.

## Focused qualification and production

Both tools copies pass eight fresh canonical methods and shared tools checks.
After production, each passes two fresh installed methods. Six semantic
methods are reused only with exact module, input and artifact fingerprints.

- 1,016 guest cases visit all 49 words. Cover signed/wrapped timer boundaries,
  all flag/group/context bytes, four owner/record alias layouts and helper
  mutations. Deliberate saved-byte overwrites remain guest-only evidence.
- 440 fired access-prefix pairs compare complete state, trace, PC and delay
  slots. Invalid-owner cases still require the identity read and skip later
  clock/timer/state fields.
- Native32 O0/O2/O3 each pass 524,288 cases, including all 65,536 lifetime
  encodings, timer overflow boundaries and all byte encodings. Verify the
  typed layout, one-pointer void ABI, whole-record/owner fences and trapping
  UBSan. Twelve semantic mutations fail in native runs and twelve separately
  compiled IDO mutations fail in guest runs.
- Six GNU layouts run 96 cases, including HI16/LO16 carry and three global /
  record alias layouts. Three raw-body/binding corruptions and six whole-image
  corruptions are rejected. Raw C, actual Make and original objects link to
  identical instructions in every tested layout.
- The actual three-command Make recipe reproduces the qualified owner and
  padded object. Selected and owner compiler diagnostics are empty. Make
  retains its known unrelated duplicate generated_12D630 recipe warning.

The immutable qualification seal covers 16,379 paths and 376 focused inputs.
Independent image prediction permits precisely 144 changed bytes: 143 code
bytes and one symbol-size byte (12 -> 196), with zero exclusions. All 6,056
function addresses, 6,055 other bodies and 720 protected Game owners /
189,088 bytes remain fixed. Shared declarations, caller/helper source,
Makefile, layout, conversion CSV and complete guard manifest stay unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Raw compiler / original relocatable body | b4c2dc25b7aa7166c5b5c8c65eca4d9d46a7d39f228b3e316086355add54a788 |
| Linked retail slot | 495b7c7d68d2644029335f491970507d22ef9f5ae7ff96c5802aa93b22d6ced0 |
| Adopted owner object | 8e4e086312c7763f74ff7e8d3eb8c3c46538743502e46346c1e2b1eb039bdcc6 |
| Adopted ELF | 92e68c907aba901c0e2b87dc83601de8ff7ef7cbb25d4ffc9135d39d01403ab4 |

## Bank and measured progress

Predecessor consumer: 02c315c51103bac49351f56ec7242718a7fdb184.
Tools committed first: 990ff03ae1275ed2e3d509e1fb68112ec5e51aca.
Preserve 1,790 inherited dirty paths in the older tools mirror and add only
three qualification modules there. No push. Routine Claude calls: zero.
Graph work is a scoped AST refresh with old-node and valid-relationship
retention, not full-corpus extraction or global reclustering. The former s32
placeholder return context must be retired against the recovered void ABI.
Raw receipts: conker/build/game-owner-timeout-transition-match/.

| Section | Byte-exact C | Different | Address drift |
| --- | ---: | ---: | ---: |
| Total | 3,861 / 5,506 (70.12%) | 1,645 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,188 / 4,833 (65.96%) | 1,645 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

269 more exact C functions are needed to reach 4,130 / 75%.
Next inspect func_1500A6D8; the queue is a screen, not qualification.
func_1514E920 remains parked and uncredited.
