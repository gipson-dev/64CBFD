# Owner Pair Event Direct C Match

Date: 2026-10-24. Consumer predecessor `7006747e`; tools predecessor
`5a4c1944`. Qualification tools committed first as
`ce6299b2ed14afd4478693efb9b735c4aa162790`. No push requested/performed.
Routine work, zero Claude calls; no provider or package changes.

## Recovered Routine

`func_1518C850`, `conker/src/game/generated_1B8F40.c`, replaces a three-word
zero-return placeholder with the complete owner paired-reference event.
VA `0x1518C850..0x1518C8F4`, ROM `0x1B9D00..0x1B9DA4`, exclusive ends:
164 bytes / 41 body words, frame 24, one binding. Preserve the separate
three zero alignment words through VA `0x1518C900` / ROM `0x1B9DB0`.
All body words emit directly from normal IDO O2/g3 C, with no guards.

Recover `void(void *owner, s32 pairAddress, u8 command)`, matching the
actual descriptor callback type. Keep the original address-named symbol;
locals identify the owner, paired word address, byte command and captured
first reference. The owner stores a reference word at +0x24 and a tag byte
at +0x28. This is observed reference/tag behavior, not a guessed actor name.

1. For command 0x2D, capture pair word zero. If it matches the owner's
   reference, replace that reference with pair word one, then read byte nine
   and write the owner's tag. Otherwise, if pair word one matches the current
   reference, store the captured first reference, then read byte eight and
   update the tag. The first match wins when both words match.
2. For command zero, separately capture pair word zero. Release the owner
   when it matches the reference, or when the owner's tag matches pair byte
   four. The tag comparison is short-circuited after a word match.
3. Other byte commands do not dereference owner or pair. Preserve byte
   truncation and the full incoming A2 word home before narrowing.

Word stores precede tag reads. Overlap can change the later byte source,
so do not capture both tag bytes early or reverse the store sequence.
The original release call receives the owner, never the pair address.

## Direct Compiler Fit

Initial semantic forms emit 40 words or retain six register differences.
Explicitly capture `first` in each of the two separate command scopes.
That recovers the retail V0 lifetime without binding physical registers,
adding volatile barriers, changing the profile or installing patch rows.
A shared outer capture instead regresses to 40 words. Additional typed
field-pointer views emit 42/43 words and remain discarded private screens.

Retain the unreachable duplicate pair-word load at +0x44 as emitted by
the compiler. All 40 executable root words are visited; the duplicate is
not counted as visited or excluded from the 41-word matching extent.
The sole binding is the release JAL at +0x8C.

Raw body SHA-256:
`5add0cf25c2711fd608d1e8be3349da1909aa4905551d7444b5d0857b3e71e73`.
Resolved retail body SHA-256:
`24ddfd61d45af9da5eea8f928c43df3e5e5b946e555f129b2d26a54e62f389ff`.
Complete 44-word retail slot SHA-256:
`05c54df8c579dacede92550c6f41ea1db672a2f4862fe47174d5dd20e760ba41`.
Independently assembled original and isolated/whole-owner C have identical
raw payloads and symbolic bindings before resolution.

## Caller And Helper Boundaries

An aligned full-ROM scan finds no direct JAL sites and exactly one literal
function pointer at ROM `0x2305D0`, VA `0x8008BB10`. This is offset +0x1C
of descriptor type 31 in `D_8008B4A8`, stride 52. Verify the live descriptor
word against retail and the existing `struct115` callback declaration
`void (*)(void *,s32,u8)` without incompatible function-pointer casts.

Execute the complete 124-word original `func_15169070` dispatcher from entry
to return in 180 phases: empty/clamped ranges, empty and multi-node lists,
null/present callbacks, both rows, commands 0/15/16/45/255 and reference
match cases. Observe 123 parent words. The generic notification can mutate
the live successor after capture; traversal still uses the saved successor
from `D_800DD198`. Clamp and generic notification remain bounded providers.

Do not replace the retail parent with the current linked C version: that
version is 121 words, differs from the original and remains unmatched.
Its source/object are preserved unchanged, and it receives no matching
credit. Executing the original parent does not qualify the current C
parent or the full generic notification implementation.

The retained `func_1516972C` release helper is already byte-exact and
unchanged. Exercise all 28 words in 288 connected phases, including a
bookkeeping mutation before the late owner-kind read, kind below two,
callback present/absent and fallback routing. Compile its actual C body
natively with the root. Bookkeeping, destructor and fallback remain
bounded providers, not newly recovered implementations.

## Focused Qualification

Both tools copies pass eight fresh checks before and after installation,
zero errors/failures/skips and zero reused checks. Primary/mirror pre-install:
34.592s / 33.978s; installed: 35.593s / 35.185s. Both shared tool checks
exit zero. Reuse existing MIPS, frame/fault, source-span, native32,
relocation, object/pool and ordinary generated-padder helpers.

- 19,440 guest root phases cover all low byte commands with upper-word
  variants, signed/high reference patterns, first/second/neither matches,
  tag boundaries, release mutations, seven owner/pair/home alias layouts
  and both stack phases. Compare complete original state/events as well
  as independent public reference semantics. Private stack aliases remain
  guest tests, not portable native-C claims.
- Native32 O0/O2/O3 with trap UBSan covers 1,572,864 selected cases per
  optimization and ten effective defined wrong-C controls. Use complete
  allocated backing for owner/pair aliases, numeric native-endian words
  and byte accesses, rather than undersized declared objects or a fixed
  byte-array word-punning fixture. Native expected byte order is native;
  guest big-endian alias order is checked separately.
- Another 131,072 native descriptor-interface cases per optimization use
  the actual `struct115` type and callback assignment, with no incompatible
  function-pointer cast. The actual release C runs through bounded lower
  providers. No full native-parent acceptance is claimed.
- Twenty-eight fired root-access fault prefixes preserve complete private
  guest state, saved registers, return lifetime, PC and delay origin. Five
  unsupported commands also ignore NULL owner/pair pointers. Do not claim
  portable C fault semantics or hardware parity from the guest model.
- Nine GNU links compare independently assembled original, qualified padded
  and actual Make objects at three code/helper address pairs. Execute 126
  rebased phases with aliases and both stack phases. Four strict-image
  corruptions reject header, trailing, code or retail-body changes.

The initial caller fixture incorrectly used the current C parent's 121-word
extent for the original. Inspect the original JR/delay tail and correct it
to 124 words. A wrong-owner negative also needed an explicit valid void
pointer conversion; retain -Werror rather than suppressing its diagnostic.
Discarded source-screen syntax and CRLF extraction mistakes were corrected
before fresh qualification; no production behavior or input seal was relaxed.

## Production And Preservation

Advance the previous sealed baseline only for its three qualified source/
object/ELF overrides. Seal 15,954 initial files, adding the two owned tools
files in both copies: 15,958 files / 28 focused inputs / all 1,454 linker
objects. Use checked native stdin/tar bridges and the verified Linux cache,
without DrvFS project reads.

Actual shadow Make uses three normal commands with IDO O2/g3 and the
generated-slice padder; its complete padded object equals qualification.
Preserve all eight raw/padded neighbors and pools, including the existing
factory and other unmatched bodies. Isolated compiler diagnostics are empty;
whole-owner diagnostics are unchanged. The inherited duplicate
generated_12D630 recipe warning remains; no warning-free build claim.

Production Make exits zero in 0.570s. Its `-o retail_word_patches.us.csv`
marks the audited unchanged CSV as old, avoiding unrelated rebuilds; it
does not skip the modified owner or change any guard bytes. Independent
and production links agree exactly: 114 changed ELF bytes, 113 target-code
bytes and one target symbol-size byte, 12 to 164. No metadata exclusions
or unrelated changes. Preserve all other 6,054 bodies, all 6,055 addresses
and protected Game data: 720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Audit all 15,958 native entries before/after adoption with exactly three
overrides: target source, target object and ELF. Recapture the actual live
adopted ELF and independently recount that stream, not an inferred +1.

Installed ELF SHA-256:
`8baf4f6801f09a46a08e6118722cda721b13e0d16a66ffb1d1b0bbda9fcf48d9`.
Installed target object SHA-256:
`282f1b79f43f9ea673a2e095fe0254bd1bf42bd63ae8128b5db2da8485a33e8b`.
Unchanged guard CSV SHA-256:
`3a5b68d16b833e8b1e1c054f492606354062658a3bfa01cd520b97f9f29a5d1c`.

Preserve all 1,606 pre-existing older-mirror dirty paths/statuses/hashes/HEAD;
add only the two owned tools files, leaving 1,608 dirty paths. Do not reset
or commit that independent mirror. Host Release, saves, configuration,
private inputs, providers and packages are untouched.

## Measured Progress And Resume

| Section | Byte-Exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,774 / 5,505 (68.56%) | 0 | 1,731 |
| Game | 3,101 / 4,832 (64.18%) | 0 | 1,731 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Remove only `func_1518C850` from the live-ELF-pinned queue. Remaining source
screens: 1,602 placeholders, 120 semantic/other and nine unlocated entries.
Next real placeholder is `func_150B5840`, `generated_E2880.c`, 44 words.
`func_1510D8C0` already has a `Gfx *` C body missed by the parser and stays
a separate uncredited matching case. Keep the 92-word `func_1509E730`,
862-word `func_1508CAD8` and current 121-word dispatcher separate.
Target 4,129 exact C functions: 355 more, goal incomplete.

Root README changes only its two aggregate matching rows. Retain the normal
post-commit Graphify worker receipts and audit all eight changed C/Markdown
hashes/mtimes/memberships plus all 43,962 prior nodes. The retained-corpus
warning remains; do not claim full-corpus re-extraction or old-edge retention,
and do not forge a missing commit stamp. No gameplay/hardware acceptance
is inferred from this recovery.

Ignored evidence: `conker/build/game-owner-pair-event/qualified/`.
Tools: `tools/experiments/game_owner_pair_event.py` and
`tools/tests/test_game_owner_pair_event.py`.
