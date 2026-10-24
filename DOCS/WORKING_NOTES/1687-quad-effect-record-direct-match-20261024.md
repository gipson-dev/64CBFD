# Animated Quad Record Direct C Match

Date: 2026-10-24. Consumer predecessor `097beeb9`; tools predecessor
`19a576c1`. Qualification tools committed first as
`c31f6b242987627e99ac33e5dd98b30deed92c13`. No push requested/performed.

## Recovered Routine

`func_15171CA0`, owner `conker/src/game/generated_19F150.c`:

- VA `0x15171CA0..0x15171D4C`, ROM `0x19F150..0x19F1FC`.
- All 43 words directly from C, frame 32, one allocator binding, no guards,
  profile changes or shared-header edits. Symbol size advances 12 to 172 bytes.
- Raw C SHA-256:
  `18166ee5cc5a55c2a59f5e19d295b5b3093f9043ea6d12428d7b8b6a7d549d97`.
- Retail/resolved SHA-256:
  `e9f73f215b5d0002fde49fdc162ef94cbd2cf859a159eeb6082c6da25f8e995d`.

Recover a pointer-returning eight-argument interface:
`s16 lifetime, u16 color, u8 imageIndex, s32 flags, s32 frameStep,
s32 alternate, u8 slot, s32 context`. Call the existing typed allocator
`func_15167A68(alternate == 0 ? 0xF : 0x43, context, 0x60, 1, slot, 1)`.
Keep its actual byte-valued fifth/sixth arguments. Return NULL immediately
on failure; otherwise initialize only the recovered metadata and four flags.

The local `QuadEffect19F150` uses four real SDK `Vtx` objects at +0x10.
Their flag halfwords are +0x16/+0x26/+0x36/+0x46. Caller geometry writes
confirm this vertex layout; do not replace it with an invented packed type.
The updater establishes signed lifetime at +0x50, animation accumulator at
+0x52 and signed step at +0x54. Renderer bit extraction establishes packed
color at +0x56; +0x58 selects image metadata and +0x59 contains flags.
The header and trailing six bytes remain opaque and preserved.

A zero-first ternary retains the original branch polarity and fallthrough
constants. Early NULL return retains all 43 words. Keep the flags assignment
before the four vertex clears in C: IDO schedules the final byte store after
those clears, preserving retail's captured input. No instruction patches
are needed to force that order.

## Original Callers And Allocator

Aligned target JALs occur only at ROM `0x19F240` / VA `0x15171D90` in
`func_15171D4C`, and ROM `0x19F3F8` / VA `0x15171F48` in
`func_15171F04`. No aligned literal function pointers are present.
Execute the authentic 24-word and 21-word argument/setup windows, including
the target and its following success/failure branch boundaries, over 112
phases in their real 48-byte frames. Confirm signed halfword, unsigned
halfword/byte and four stack arguments. The floating homes are preserved as
raw words. Both parents remain C placeholders; full geometry is not claimed.

The current 28-word `func_15167A68`, frame 40, is byte-exact against retail.
Execute every word in 112 connected-helper phases. Its lower
`func_10003C6C` allocation and `func_15168A4C` registration providers
remain explicitly bounded. Also compile the actual installed allocator C
body in native32 fixtures; confirm its context byte and selector stores.
No claim is made for the complete heap/list pipeline.

## Focused Qualification

Both tools copies pass six fresh checks before and after installation,
zero errors/failures/skips and no reused checks. Pre-install primary/mirror:
2.887s / 2.852s; installed: 3.898s / 4.038s. Both shared tools checks exit zero.

- 336 ordinary guest phases cover width boundaries, full-word mode selection,
  allocation failure, hostile caller-saved clobbers, live incoming-home
  mutations, two stack phases and returned-record/home overlap. Compare
  complete literal registers, RAM, events, calls and saved-RA lifetime.
- All 43 root words and all 28 connected allocator words are visited.
  The independent reference preserves the first-halfword capture before
  frame clearing, later home reloads and flags capture before vertex clears.
- Native32 O0/O2/O3 with trap UBSan: 7,168 selected calls per optimization,
  every image/slot byte, full-word boundaries, NULL/non-NULL results,
  all record bytes and surrounding fences. Fourteen defined wrong-C
  controls fail effectively. Native storage remains disjoint and typed.
- Nine independent GNU links compare original, padded and actual Make
  objects. 288 cases exercise independent entry/helper rebases, returned
  guest record/home aliases and both stack phases.
- All 444 root-access fault prefixes fire with equal state, PC and delay
  origin. Nine image corruption/truncation controls are rejected. Guest
  private-home overlap and fault schedules are not portable C claims.
- The caller fixture's failure boundary and outgoing-home setup were corrected
  before the final fresh suites. No provider install or production helper
  change bypassed a failure.

## Production And Preservation

The isolated body, complete owner and independently assembled original have
identical payloads and the same single binding. Six raw/padded neighbors and
all owner pools are unchanged. The actual three-command Make recipe, normal
O2/g3, emits the qualified object byte-for-byte. Compiler diagnostics are
empty; inherited duplicate-recipe warnings remain unchanged.
Production Make exits zero in 0.547s.

Independent and production full links reproduce the exact body/size-only
prediction: 126 changed ELF bytes, 125 code bytes plus one size byte, zero
exclusions. All other 6,054 function bodies and all 6,055 addresses are fixed.
The complete guard manifest is unchanged. Protected Game data remains exact:
720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Result ELF SHA-256:
`fb1c38c6c9f3125f6f410be7df90b459dac9ea3cf0af4d0179b631745e3c6198`.
Target object SHA-256:
`9c0a40e09e8368356406f78dec1cf3eb6509f8b5e5c5f301c60b2554d6a6ad60`.

Seal 15,918 files, 27 focused inputs and all 1,454 linker objects.
Verify fresh native capture and Linux cache bytes, stream over native stdin
and checked tar without DrvFS project reads, and audit every file before and
after live adoption. Only target source/object/ELF change. Preserve all
1,586 pre-existing older-mirror dirty paths/statuses/hashes and its HEAD,
adding only two task files. Host Release, saves/configuration are untouched.

## Live Recount And Handoff

The actual adopted Windows ELF equals the independent and production images.
Fresh standard matcher exits zero in 1.365s:

| Section | Exact C functions | Address drift | Still different |
| --- | --- | --- | --- |
| Total | 3,759 / 5,505 (68.28%) | 0 | 1,746 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,086 / 4,832 (63.87%) | 0 | 1,746 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Converted-C denominator unchanged. The active 75% goal requires 4,129 exact
functions, 370 more. Remove only `func_15171CA0` from the ELF-pinned queue:
1,615 placeholders, 122 semantic/other definitions and nine parser-unlocated
entries remain. Next `func_1510D8C0` already has a `Gfx *` semantic body;
the private source-shape parser misses that return spelling. Triage it before
the next placeholder `func_1518C850`; neither is newly credited.
Keep the 862-word `func_1508CAD8` owner stub separately queued.

Bank the nine scoped consumer paths; root README changes only its Total/Game
aggregate rows. Use the normal Graphify commit hook and audit all 43,864 old
nodes for retention or unique relocation, plus all eight changed C/Markdown
hashes, mtimes and memberships. Do not forge a missing commit stamp or claim
excluded-old retention as a full corpus re-extraction.
