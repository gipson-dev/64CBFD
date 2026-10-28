# Actor action dispatch direct C match

Verified: 2026-10-28. Status: adopted after qualification and the native ELF recount.

`func_150979CC` now resolves an actor, marks its lookup record active when its
signed index is below the live byte count, and dispatches the mode-dependent
action. It returns 0 for a missing actor and 999999 otherwise. Its complete
48-word / 192-byte retail slot, 24-byte frame and ten external bindings emit
directly from C using the existing O2/g3 profile. No guards, shared header,
compiler profile or helper implementation changes are needed.

## Source and ABI

The owner is `conker/src/game/generated_C4DC0.c`; the retail window is
VA 0x150979CC..0x15097A8C, ROM 0xC4E7C..0xC4F3C. Preserve the existing private
48-byte `SpawnLookupRecord` view with state byte at +2, already used by its
neighbor. The public actor pointer uses `struct127 *`; the callback returns
signed32 and takes a signed index and a pointer to its command/context words.

The lookup receives only the index. Its return must be checked before any
count, record table, mode or context access. Count and table pointer are read
after the lookup; the signed comparison deliberately has no added lower-bound
clamp. Mode is read after the state store, and context[1] is read only for mode
2. Mode 2 and nonzero context[1] call `func_15053430`; the other successful
paths call `func_15060F28(actor, 0)`. Helper results do not replace 999999.

The entry stores index/context into the incoming +0/+4 homes and saves RA at
frame +20. Guest tests preserve the late home reloads and state-byte aliases
with globals and context. Those emitted-code alias tests do not claim portable
C parameter mutation through invalid native pointers. Native negative-index
cases use a valid allocated prefix; wrapping addresses stay in the guest suite.

## Original caller and helper boundaries

The 15-entry `D_8008845C` descriptor table registers the target at slot 1,
ROM 0x22CF20 / VA 0x80088460. The original `func_150ADAF0` caller window is
35 words at VA 0x150AE108..0x150AE194 / ROM 0xDB5B8..0xDB644. Tag 2 selects
slot 1. The JALR delay slot clears only bits 12..15 with mask 0xFFFF0FFF,
retaining the upper command bits; A1 carries the original context pointer.
It reserves 16 outgoing argument bytes. Connected execution stops at
0x150AE188 after the target returns, before the final three words that use
outer-owned S7 to restore RA and release that outgoing home. Those three
literal tail words are checked statically; this does not execute the complete
handwritten interpreter or claim an ordinary isolated C ABI for its parent.

The retained original lookup `func_1505EEF4` is 55 words / 220 bytes, no frame,
at VA 0x1505EEF4..0x1505EFD0 / ROM 0x8C3A4..0x8C480. It scans all 25 inline
actor slots at 0x800CC2D0, stride 0x32C, testing the state word and ID byte at
+0x13F. It returns an actor pointer or NULL; A1 is its scratch value 25.
All 25 hit positions, not-found and high command bits are exercised.

The current decomp parent and lookup remain 12-byte zero-return placeholders;
the alternate action remains a 16-byte argument-home/zero-return placeholder,
and the default action remains a 16-byte two-home/return placeholder. Their
source and linked bytes stay fixed. Original retail caller/lookup execution
and bounded opaque action effects qualify this target; they add no helper C
credit or full interpreter, gameplay or hardware acceptance.

## Qualification and image preservation

Both primary and preserved standalone tools copies pass eight fresh canonical
methods with zero failures, errors or skips. Each installed copy then passes
two fresh owner/image methods and reuses six unchanged semantic results only
after exact input/module/artifact fingerprints agree.

- Guest: 1,104 cases, all 48 words visited, 13 state/mode/context/home/count/
  pointer alias layouts, signed index and mode/flag boundaries, lookup effects,
  private home probes and lazy unmapped exits.
- Native32: 262,144 positive cases per O0/O2/O3 profile with trapping UBSan,
  all 256 count bytes, all 65,536 signed16 index encodings on NULL lookup,
  non-NULL negative indices inside allocated storage, provider mutations,
  complete state arrays, affected padding and buffer fences. Thirteen source
  controls are effective; cached-mode alias rejection is checked separately
  in the guest suite, not counted as a native global-alias control.
- Connected caller: 636 cases using the original caller prefix and complete
  55-word lookup, all 25 hit slots/not-found, retained high command bits,
  callback return and outgoing home behavior.
- Access faults: 554 fired prefix pairs with complete private PC, delay and
  trace equality. NULL lookup needs no globals/context mapping; non-mode-2
  paths accept NULL context.
- Relocation/padder: three GNU layouts / 72 cases, ten HI16/LO16/J26 bindings,
  signed-low carries, three effective raw corruptions and identical actual
  padding. Three compiled IDO controls reject cached mode, an added lower
  bound and a wrong result by mapped values or action arguments.
- Actual three-command generated Make shadow and production build both emit
  the qualified owner; selected/before/after/Make diagnostics are empty.
  Preserve the inherited duplicate generated_12D630 Make recipe warning.
- Strict complete-image prediction changes exactly 145 bytes: 144 code bytes
  and one function-size byte (12 to 192). Zero exclusions or metadata reorder.
  All 6,056 function addresses, 6,055 other linked bodies, all named definitions,
  three compact/padded neighbors and owner pools stay fixed. All 720 protected
  Game data owners / 189,088 bytes remain exact. The map, inventory CSV and
  historical guard manifest remain byte-identical.

Freeze 16,267 source/tool/build inputs and 268 focused inputs, including the
original descriptor object; validate all 25 qualified artifact fingerprints.
The initial narrower caller run is archived under `canonical-initial-coverage`;
only the strengthened all-slot/high-command-bit rerun supplies final receipts.
Tools commit `8441b9870f80393ec258ca045503942ac10e423e` precedes the consumer
source/pin/documentation commit. Preserve the standalone mirror's 1,746
inherited dirty paths and add only the two qualification modules; do not commit
or reset that separate mirror. No push is requested or performed.

## Measured progress and next step

The actual adopted native ELF recount is 3,846 / 5,506 exact C functions
(69.85%); Game 3,173 / 4,833 (65.65%), Init 492 / 492 and Debugger 181 / 181.
There are 1,660 different C functions and zero address drift. The 75% goal stays
open: ceil(0.75 * 5,506) = 4,130, requiring 284 additional exact functions.
The remaining screen has 1,531 placeholders, 120 semantic/other and 9 unlocated
source shapes. Only this target is removed from the predecessor queue.

Next inspect `func_1509CBD4` in `generated_C9EC0`, a 48-word screen candidate;
its source/ABI/caller/whole-image qualification is still pending.
`func_1514E920` remains parked and uncredited. Keep detailed updates in the
working notes and status documents; the root README changes only its two
aggregate match rows.

## Reproduction artifacts

Private receipts live in `conker/build/game-actor-action-dispatch-match/`:
`preparation.json`, `sealed-production-proof.json`, both pre-install and
installed test receipts, `sealed-live-adoption-audit.json`,
`75-percent-queue.json`, `match-progress-v2.log` and the native final audit.
The graph refresh is scoped to these seven documents, the owner C file and
the two tools modules. Preserve all old nodes and valid directed contexts;
the target's existing signed32 return contexts remain valid. Outside-scope
freshness, communities and global analytics stay historical.

| Artifact | SHA-256 |
| --- | --- |
| Raw 48-word body | `d59793c9530abb3fe2575634521231b372007ae183ec461e791387ea50119f3a` |
| Retail linked 192 bytes | `13395829b02e7ad9b12775c632260155e2d700a14aabcead3fdf1885c617e949` |
| Qualified padded owner | `ad5628d90ee58fee1e342536e33e15c302eaad8ec34faf17b7d3a27b37a4fec1` |
| Adopted ELF | `94a8c7a621abb2f884dbd959f6bb6ec427539b9f3a164f7efcf16299e0b708c3` |
| Input snapshot | `af092558934cef4c29b4906b11d7bffad4b2e0baef142fd9860c5b5d7a100867` |
| Native guard manifest, unchanged | `1383ae8599001c8769a2557ce1e4d2791f5f3bb5fcf8b59e822cdbc12e618f85` |
