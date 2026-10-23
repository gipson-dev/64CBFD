# Payload Owner Link Event Guarded C Match

Date: 2026-10-23. Predecessor consumer `b4addef2`, tools `24b7f918`.
Qualification tools committed first as `b792eeb`.

## Recovery And Interface

Recover `func_15193234` in `conker/src/game/generated_1BFDD0.c`:
VA `15193234..151932E0`, ROM `1C06E4..1C0790`, 43 words / 172 bytes,
frame 24 and one R_MIPS_26 release binding at +0x94. Keep the address-based
name, add a purpose comment and retain original `conker/asm/1BFDD0.s`.

Use `void (struct260 *owner, s32 eventAddress, u8 command)`, matching the
actual callback-table declaration and complete current caller. Convert the
word-sized event address into a private packet view inside the callback.
The earlier pointer/pointer compiler screen had the same emitted words,
but was not the recovered typed table interface.

The owner's payload at +0x28 contains a pointer, identity byte +0x2C and
three opaque bytes. Test command 0x2D first: capture the current link once,
prefer the first matching packet pointer, store the opposite pointer, then
read and store its late identity byte +9 or +8. Command zero releases the
owner if packet word +0 matches its link, or if raw packet byte +4 matches
the link identity. That command-specific byte is not the retarget packet's
identity at +8/+9. Ignore other commands without dereferencing their payload.
Preserve short-circuiting, full incoming command homes and opaque storage.

Keep both wire views private. Add the existing `structs.h` types and a local
release declaration to this owner only; do not change shared headers,
global actor structures, existing caller code or compiler profiles.

## Four-Word Allocation Fit

This is guarded semantic C, not a compiler-only match. Derive one closed
V1/A0 exchange across words 10 through 24, commuting the two equality tests
at words 12/20. The symmetric word 12 stays identical. Only four words change:

| Offset | Expected raw C | Retail |
| --- | --- | --- |
| `028` | `8C430000` | `8C440000` |
| `02C` | `8CA40000` | `8CA30000` |
| `050` | `54790013` | `57240013` |
| `058` | `AC440000` | `AC430000` |

Opcodes, immediates, branch targets, frame, saved-register lifetime, call
binding and extent stay fixed. No inserted or omitted words. Verify the
complete raw hash and relocation before normalization; preserve the whole
old guard-manifest prefix byte for byte. Retain the naturally unreachable
duplicate load at `15193280` (word 19 / +0x4C); all other 42 target words
are naturally visited without forcing entry.

Raw C text SHA-256:
`00311607be3f803315d4dc1683cd884d1fe3dd2dd4cfc6aa0c38c74e301e89d2`.
Qualified guard CSV SHA-256:
`514908c88bb9f7608478de0e044172a7d12a6dc7d198b3372a6c954ae5748282`.

## Registered Caller And Release Chain

Aligned ROM scanning finds exactly one literal pointer and no direct JAL:
VA `8008A918` / ROM `22F3D8`, slot 16 of the 74-entry table
`D_8008A8D8`, VA `8008A8D8` / ROM `22F398`, in `22EF80.rodata.s`.
Verify all table words against both original ROM and current ELF.

The actual caller is the existing exact 23-word/frame-24 `func_15149434`,
VA `15149434..15149490`, ROM `1768E4..176940`, in
`conker/src/game/done/game_1765E0.c`. Its selector is an unsigned byte at
owner +0x13. Original LBU and current `struct260` confirm this; an earlier
private handoff incorrectly called it signed. Values 74..255 fall back to
slot zero. Keep the original redundant BLTZ instruction, the branch-likely
NULL bypass, byte-command narrowing and actual indirect call at `15149478`.

Qualify all 23 original/current caller words across 20,480 phases, every
selector byte, eight command patterns and five link relations. Compile its
actual existing C body in the native harness, not a substitute dispatcher.
Other non-NULL callbacks remain bounded providers. Preserve the caller's
entire twelve-function object, SHA-256
`e25e23423217e12289d36ef8ddd82eb68ba757c7b708340995f7a7d8a987aabf`.

Also qualify all 56 retained original/current words of `func_1516972C`,
`func_151696DC` and `func_15169804`: signed cached scan count, owner-slot
replacement by owner +8, type gating and optional type/default release.
All helper words are visited across 120 phases, including count bytes
128/255. Lower release/type providers, full heap and broadcast dispatchers
remain outside this acceptance claim.

## Qualification

Both tools copies pass eight fresh pre-install tests, then two fresh
installed checks, with zero errors/failures/skips. Explicitly reuse six
unchanged behavioral checks after installation only under strict source,
raw/padded object, guard, caller/helper and complete-image identity. Both
shared tools checks pass. Reuse existing parsers, IDO compiler, MIPS oracles,
GNU linker, padder and native32 compiler without dependency or oracle changes.

- 5,420 target guest phases and 240 guest aliases cover all byte commands,
  noncanonical incoming homes, full pointer words, first-match order, late
  byte reads, short-circuiting and ignored unmapped payloads.
- 2,631,680 native32 cases per O0/O2/O3 build cover direct target calls and
  the actual dispatcher over every selector byte and command. Trap UBSan
  and twelve effective wrong-C controls pass. Allocate an extended owner
  in fresh GNU/Linux brk storage with no declared short header object;
  use a disjoint typed packet, real pointers, explicit opaque bytes and
  byte fences. Preserve the existing `struct260` definition unchanged.
- Nine independent GNU links and 120 rebase phases preserve original/raw/
  padded C at alternate entries and release addresses.
- 866 fired root-access prefixes compare normalized complete state, memory,
  attempted access and branch-delay PC. Raw C public results and traces
  pass, but raw complete-GPR equality is not claimed.
- Nine raw/binding corruptions and seven strict-image controls are rejected.
  The old zero-return placeholder fails effective semantic cases.

Native evidence is bounded to GNU/Linux 32-bit allocated owner storage and
disjoint typed packets. Guest aliases, private homes and invalid-address
prefixes qualify emitted N64 behavior, not portable C fault semantics,
native64 or gameplay/hardware acceptance. Only guarded output claims literal
complete-machine-state equality with retail.

## Production And Preservation

Normal O2/g3 and the actual three-command compile/pad/assemble recipe
reproduce the qualified complete owner object byte for byte. Preserve all
five neighboring functions, pools and extents. Independent linking and
production Make agree on exactly 119 changed ELF bytes: 118 target-code
bytes and one symbol-size byte, with zero exclusions. Every address is fixed.

ELF SHA-256:
`af40284c5c7c36eb5e4a7edea75fd7680a88275767f0da332e8bc9534260cc57`.
Padded owner object SHA-256:
`dba1daa56e29f2a9c18cfa468a32b9eb68c22e9583fcb9e32fcbbafca15a7dc7`.

Preserve all other 6,054 bodies, all 6,055 function addresses and all 720
protected Game-data owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Seal and recheck 15,894 files, all 1,454 linker objects and 29 focused input
pins. Advance the preceding checkpoint's three adopted entries explicitly;
this checkpoint has four mutable entries: source, object, guard CSV and ELF.
Promote the linker script and progress CSV unchanged. Marking the guard CSV
old for bounded Make is justified by its intact prefix and four new rows
scoped solely to the rebuilt target, not whole-file identity.

Stage private receipt imports, validate the complete manifest before copying,
and replace imported files atomically. Preserve all 1,574 preexisting dirty
paths and the HEAD of the older independent tools mirror, adding only the
two identical target tool files. Commit primary tools before the consumer.
No push, dependency installation or host-port changes.

## Handoff

Fresh standard matching against the adopted live ELF reports total
**3,751/5,505 (68.14%)**, Game **3,078/4,832 (63.70%)**, Init 492/492 and
Debugger 181/181 exact. Zero drift; 1,754 different. The 75% target stays
4,129 exact, requiring **378 more matches**. The refreshed queue has 1,623
placeholders, 122 semantic/other definitions and nine unlocated entries.

Next `func_1519E570` in `generated_1CA420.c` is queued only, 43 words / 41
placeholder differences. Establish its full interface and semantics before
qualification, installation or credit. Retain the 862-word `func_1508CAD8`
stub in the queue. README changes only Total/Game aggregate matching rows.
Post-commit Graphify completion, fresh-output provenance and every-old-node
retention remain private audited receipts; no clean full-corpus extraction
is claimed. The wider goal stays active. Host Release, saves and configuration
remain frozen and untouched.
