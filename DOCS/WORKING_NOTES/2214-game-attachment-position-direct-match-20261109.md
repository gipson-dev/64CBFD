# Attachment Position Direct Match - 2026-11-09

`func_150D88E0` replaces a false zero-return placeholder with the original
attachment-offset selection and matrix transform. All **80 words /320 bytes**
emit directly from C under existing **O2/g3**, with original **0x40 frame**
and no padding. **No guards, profile changes or binding rows** are required.

Production: Total **4,283 /5,513 (77.69%)**, Game **3,610 /4,840 (74.59%)**,
Init **492/492**, Debugger **181/181**, zero drift; **1,230** still different.
**128** more exact functions reach4,411/5,513 and80%. Conversion rows stay fixed.

## ABI and recovered body

Owner `conker/src/game/generated_105760.c`; original `conker/asm/105760.s`.
VA150D88E0..150D8A20; ROM105D90..105ED0. RA is saved at SP+0x24;
there are no saved S registers. Incoming homes are SP+0x40/+0x44/+0x48.

```c
s32 func_150D88E0(f32 *position, u8 *owner, u8 selector);
```

Select the joint and local x/z offsets using the low selector byte:

| Selector | Joint | X | Z |
| --- | --- | --- | --- |
| 3 | 18 | -7.0 | 30.0 |
| 4 | 21 | -4.0 | 35.0 |
| 5 | 15 | 5.0 | 20.0 |
| 6 | 24 | 5.0 | 31.0 |

Set y to positive zero. Read the matrix base from owner+0x1D4, select a
64-byte matrix record, and call handwritten `func_150A7960` with the matrix,
three float inputs and three output pointers. Its recovered seven-argument
prototype keeps the mixed o32 ABI: the first pointer occupies A0, so float
input bits travel in A1/A2/A3; output pointers use outgoing SP+0x10/+0x14/+0x18.
Reload the destination from its incoming home after the helper, then reload
and store local x/y/z in that order. Return1 independently of helper return.

The byte-index expression `(f32 *)(*(u8 **)(owner+0x1D4)+joint*64)` preserves
all80 original words. Natural float-pointer indexing also has80 words and
frame0x40 but nine register/scheduling differences; reversing the local
declaration groups gives27 differences. Both forms were rejected. Integer
address variants also match, but the selected byte view expresses the actual
record stride without a new shared layout or fabricated field names.

## Selector-domain boundary

Retail initializes joint/x/z only for selector bytes3..6. Other bytes fall
through and use pre-existing private stack values. The source deliberately
retains that uninitialized default path and comments on it. A default return
or zero initialization changes the original N64 behavior and is rejected by
effective compiled controls.

The caller does **not** prove selectors stay within3..6. The outer script
handler `func_15071DC8` forwards general argument D_800D1580 to dispatcher
`func_15141A7C`; its callback `func_150D8A34` merely narrows that context to u8.
No static asset-domain restriction was established or assumed.

The matching credit is for the fixed IDO N64 build's literal80-word body,
including every selector-byte path. Native C qualification is limited to
the defined3..6 domain. Seeded guest stack tests outside that domain do not
establish portable C behavior, valid matrix backing in all scripts, complete
script-dispatch acceptance, or host/gameplay parity. A future host port must
make its own explicit decision about invalid selectors.

## Qualification

- **118 frozen inputs** include the owner, caller/dispatcher sources and
  objects, original handwritten matrix helper, callback registration,
  compiler/headers, guards/layout, ROM and linker inputs. All320 raw bytes
  and the one R26 binding are pinned. Single-byte, binding-name, retail-slot
  and complete-image corruption controls reject.
- Both padders agree on all nine owner functions. All **eight raw/padded
  neighbors**, including the complete caller, literal pools and register
  mask union remain unchanged. The actual **three-command Make recipe**
  reproduces the qualified object with zero compiler diagnostics.
- Independent whole-ELF prediction permits only this320-byte body and its
  symbol extent12->320: **247 changed bytes, zero exclusions and no metadata
  reorder**. All **6,052 function addresses**, other bodies and **189,088
  protected data bytes across720 owners** remain fixed. Makefile, guards,
  headers, callback data and progress CSV remain unchanged.
- **1,248 guest cases per body** cover all256 selector bytes, high incoming
  words before narrowing, both stack phases, seeded default locals, arbitrary
  result bits, resource/height changes, output-home redirection and local
  mutations. Every one of the **80 body words executes**. Raw and retail
  full literal machine state, calls, snapshots and access order agree.
- **Six independent GNU links /30 rebased candidate cases**, **30 guest alias
  cases** and **117 fired fault-prefix pairs** compare registers,
  FPRs, HI/LO, memory, trace, dispatched word, PC and delay origin. Aliases
  include matrix data, owner height and overlapping private local words.
  These guest-only checks do not claim portable C private-stack/fault behavior.
- **1,036 complete caller cases per body** execute all54 caller instructions
  (55-word slot), zero/nonzero resource gates, all byte contexts plus high
  words, and later effects with live vector/owner reloads. Two real dispatcher
  windows each pass30 cases per body, including the clear-versus-sign-extended
  unused argument. Registration D_8008A0B4[8] atVA8008A0F4/ROM22EBB4 remains
  pointer150D8A34/count-1 in both linked images. Dispatcher windows are bounded
  connections, not a full script-engine execution claim.
- The actual handwritten **40-word matrix helper** is baseline byte-exact;
  all40 words execute across **1,024 connected cases per body**. Its model
  uses balanced single-precision sums with separate rounding, matching the
  original load/store order. Invalid-selector connections use bounded seeded
  stack inputs; finite RNE model agreement is not hardware FCSR/NaN/trap proof.
- Native32 **O0/O2/O3 each pass120 cases** restricted to3..6. They check
  the seven typed arguments, owner pointer offset0x1D4, all owner-prefix bytes,
  all512 matrix words, complete output and return, in-place output and both
  the real C matrix model and mutating provider. Trap UBSan stays enabled.
  Only GCC's expected maybe-uninitialized warning for the retained default
  path is suppressed in this native harness; no production flags change.
- All **17 compiled semantic controls** fail observably in IDO guest execution
  and every native profile. Three additional guest-only controls reject full
  word selector dispatch, an early default return and default initialization.
  Negative objects and any literal pools link independently; those pools are
  test fixtures, with no production code/data substitution.

Seven fresh target checks pass in both tools environments before and after
installation. Shared smoke checks are fresh in both; three unchanged shared
regressions per copy are explicitly reused by exact helper/test fingerprints.
Only this owner recompiles in production, with zero compiler diagnostics,
and actual ELF/recount agrees with prediction. The inherited whole-ROM
checksum mismatch still makes `make all` exit2; existing duplicate Make
recipe warnings remain.

Fresh target entrypoint: `python3 -m unittest
 tools.tests.test_game_attachment_position_150d88e0_match -v` under WSL.
The private replay drivers record each checkout/phase and every dependency
fingerprint; reused regressions are recorded separately from these fresh runs.
Routine review uses zero Claude calls; Codex owns implementation and validation.

Tools commit before consumer. Sibling tools retain2434 inherited dirty paths;
frozen host Release is untouched. Graphify uses a scoped AST refresh with
old-node retention evidence, not full-corpus extraction or semantic API work.

Receipts: conker/build/game-attachment-position-150D88E0-match/.
Next queue: `func_150EEE00`, subject to a fresh source/ABI/owner audit.
A private complete-owner screen emits80 words/frame0x60 with36 differences
using a recovered typed helper declaration. That helper remains a stub; its
ABI and all affected callers/neighbors need audit before installation.
No matching credit is assigned to this next candidate; the80% goal stays active.

Production ELF SHA-256: 45e5e2570fb7ae8103f5ee4924f57e888f6f1e5b705024687c088bc69c86b006.
Guard SHA-256: 6a6094f04735cb3127833e50b21f98c3374916605acd7aa79ccdebd80d22dfe7 (unchanged).
