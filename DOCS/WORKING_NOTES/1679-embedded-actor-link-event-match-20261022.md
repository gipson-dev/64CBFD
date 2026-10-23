# Embedded Actor Link Event Guarded C Match

Date: 2026-10-22. Predecessor consumer `1a0e729e`, tools `41380d8`.
Qualification tools committed first as `0723f62`.

## Recovery And Interface

Recover `func_150F088C` in `conker/src/game/generated_11C2B0.c`:
VA `150F088C..150F0938`, ROM `11DD3C..11DDE8`, 43 words / 172 bytes,
frame 24 and one R_MIPS_26 binding at +0x44 to `func_1516972C`.
Keep the address-based name, add a purpose comment and retain original ASM.

Use `void (u8 *owner, u8 *eventBytes, u8 command)`, matching the actual
pointer-typed callback table and caller. The earlier isolated integer-address
screen was not the recovered interface. The typed pointer body emits the
same raw words, and needs no caller or shared-header edit. Reuse the owner's
existing `structs.h` include and typed release-helper declaration.

A private eight-byte link at owner +0x170 contains a pointer and identity
byte +0x174. Command zero is tested first: release the owner if event word
+0 matches the link pointer, or if the identity matches raw event byte +4.
This is an eight-byte release wire payload, not the paired event's identity
field. Command 0x2D uses the twelve-byte pair view: capture the current link,
prefer the first matching pointer, store the opposite pointer, then read
and store the corresponding late identity byte +9 or +8. Preserve opaque
bytes, short-circuiting and all other commands' ignored-argument behavior.

Keep these views private. Do not reinterpret the legacy global owner structs,
invent validation, merge this body with the neighboring indirect-link
`func_150F07E4`, or change the compiler profile.

## Guard Derivation

This is guarded semantic C, not a compiler-only match. A closed V1/A0 role
exchange within words 24 through 36 and commutative BNEL operands at words
26/34 derive exactly four changes. The symmetric word 26 stays identical.

| Offset | Expected raw C | Retail |
| --- | --- | --- |
| `060` | `8C430000` | `8C440000` |
| `064` | `8CA40000` | `8CA30000` |
| `088` | `546A0005` | `55440005` |
| `090` | `AC440000` | `AC430000` |

Only register fields change; opcodes, immediates, frame, calls, extent and
instruction count stay fixed. No inserted or omitted words. Verify the
complete raw hash and binding before normalization, and preserve the old
CSV prefix byte for byte.

Raw C text SHA-256:
`0406414cf853d75c4297b39aee759f40e3a18d190d31c3b32b099fe44c05a095`.
Qualified guard CSV SHA-256:
`3d9cc32d7a0b09feb9d5ef64850e01f87d22b65d4afe329d201b525158382292`.

## Registered Caller And Retained Helpers

Aligned retail scanning finds exactly one literal target pointer, ROM
`22EB14` / VA `8008A054`, and no direct JAL. It is slot 10 of the eighteen
entries at `D_8008A02C`, ROM `22EAEC`, in `22E730.rodata.s`.

The actual caller is the existing exact 55-word/frame-24 `func_151416E8`:
VA `151416E8..151417C4`, ROM `16EB98..16EC74`, selector byte owner +0x168.
It bypasses NULL callbacks, invokes the pointer/byte interface at `15141734`,
and reloads its command rather than consuming the callback's incidental V0.
Afterward, commands 0x22/0x24/0x25 compare event[0] with owner[0x168], then
release, store -1 or store 2 at owner +0x169. Qualify these post-callback paths
as well as the link-update paths. Compile its actual existing C body in the
native harness; no substitute caller is credited.

Naturally reachable caller coverage is 53 of 55 words. The branch/delay at
`15141790` / `15141794` remain unreachable under the earlier command gates;
retain them statically instead of forcing entry. Preserve the caller's
complete sixteen-function object, SHA-256
`b093947ef99b319c886aaa07ff3b194d3e9279fb6230f5d9be9e7cb3daa43602`.

Qualify all 56 original/current words of `func_1516972C`, `func_151696DC`
and `func_15169804`: signed cached scan count, owner-slot replacement with
owner +8 successor, owner type and optional type/default release dispatch.
Lower release and other callback slots remain bounded providers. Larger
broadcast dispatchers, complete heap behavior and gameplay remain unclaimed.

## Qualification

Both tools copies pass eight pre-install tests, then two fresh installed
checks, with zero failures/errors/skips. Explicitly reuse six unchanged
behavioral checks only under strict source, raw/padded object, guard, helper
and complete-image identity. Both shared tools checks pass.

- 5,420 guest phases cover every byte command, noncanonical incoming homes,
  full-word pointer patterns, ordering, first-match preference and ignored
  unmapped arguments. Another 240 phases cover guest-only overlapping data.
- 194,560 defined native32 cases per O0/O2/O3 build, trap UBSan and twelve
  effective wrong-C controls. Use fenced typed subobjects and real interior
  pointers; exercise post-callback matches without forging pointer bytes.
- 2,880 complete registered-caller phases cover all eighteen slots, NULL
  bypass, byte narrowing, release and post-callback identity updates.
- 120 original/current release-chain phases visit all 56 helper words,
  including negative signed-byte counts 128/255 and bounded release providers.
- Nine independent GNU links and 120 rebase phases preserve original/raw/
  padded C at alternate entries and helper addresses.
- 866 fired root fault prefixes compare guarded complete state, PC and delay
  identity. Visit 42 target words; duplicate packet-load word 33 is naturally
  unreachable and retained statically. Raw complete-GPR equality is unclaimed.
- Nine raw/binding corruptions and seven strict-image controls are rejected;
  the old zero-return stub fails effective semantic cases.

Native checks cover defined typed/disjoint 32-bit objects. Guest aliases,
invalid addresses, incoming-home overlap and access faults qualify emitted
N64 instruction behavior, not portable C fault semantics, native64 or host
runtime acceptance. Raw public memory/traces pass; only normalized output
claims literal complete-machine-state equality with retail.

The first run rejected an inherited five-command Make assumption before
running tests. Inspect this owner's actual three-command compile/pad/assemble
recipe, correct the harness expectation and rerun all eight tests in both
copies. Keep the failed precondition receipt separate; it earns no credit.

## Production And Preservation

Normal O2/g3 Make reproduces the separately qualified complete padded object
byte for byte. Preserve all 43 owner neighbors, raw/padded pools and extents.
Independent full linking and production Make agree on exactly 121 changed
bytes: 120 code bytes and one symbol-size byte, with zero exclusions. The
target size grows from 12 to 172 in its original slot; every address is fixed.

ELF SHA-256:
`789a57d1998bf2cdcdf0ad844612dde7c9654572091c151bc4d01794c24a4190`.
Padded owner object SHA-256:
`7542e3ef5a12a2fe371e0ce7d11cf75613591d7e3ca51585df4293a3576deebb`.

Preserve all other 6,054 function bodies and all 6,055 addresses. All 720
protected Game-data owners / 189,088 bytes stay exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Seal and recheck 15,886 files, all 1,454 linker objects and thirty focused
input pins. Advance the preceding checkpoint's six adopted inputs explicitly;
this checkpoint has four mutable manifest entries: source, object, CSV and ELF.
The linker script and progress CSV are promoted unchanged. Marking the guard
CSV old for bounded Make is justified by its intact prefix and four rows
owned solely by the rebuilt target, not by claiming the whole CSV unchanged.

Commit primary tools before the consumer. Preserve all 1,570 preexisting
dirty paths and the HEAD of the independent older tools mirror; add only
the two identical target tool files. No push or host-port edits.

## Handoff

Fresh standard matching against the adopted live ELF reports total
**3,749/5,505 (68.10%)**, Game **3,076/4,832 (63.66%)**, Init 492/492 and
Debugger 181/181 exact. Zero drift; 1,756 different. The 75% target remains
4,129 exact, requiring **380 more matches**. The refreshed queue has 1,625
placeholders, 122 semantic/other and nine unlocated definitions.

Next `func_1514D4B8` has a saved 43-word compiler-only emission screen, not
completed qualification or installation. Leave it uncredited until its
actual callers, signed node links, recursion, native cases and complete
production image pass. Retain the 862-word `func_1508CAD8` stub in the queue.
README changes only Total/Game aggregate matching rows. Post-commit graph
worker completion, fresh-output provenance and every-old-node retention
remain private audit receipts, with incremental/excluded-corpus caveats.
The wider goal remains active; host Release, saves and configuration stay frozen.
