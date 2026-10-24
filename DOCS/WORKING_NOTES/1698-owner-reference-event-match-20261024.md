# Actor Reference Event Match

Date: 2026-10-24. Consumer predecessor `ac92f815`; tools predecessor
`ce6299b2`. Qualification tools committed first as
`3f7fb091fe5eb393384c2a2530b029440cc4aaf3`. No push requested/performed.
Routine work, zero Claude calls; no provider or package changes.

## Recovered Routine

`func_150B5840`, `conker/src/game/generated_E2880.c`, replaces a three-word
zero-return placeholder with the complete actor reference event. VA
`0x150B5840..0x150B58EC`, ROM `0xE2CF0..0xE2D9C`, exclusive ends:
172 bytes / 43 body words, frame 24, one binding. Preserve the separate
zero alignment word through VA `0x150B58F0` / ROM `0xE2DA0`.

Recover `void(struct260 *owner, s32 pairAddress, u8 command)`, matching
the actual event-table callback declaration. A local `OwnerReference`
view at owner+0x28 has a signed reference word and tag byte at +0x2C.
Keep the original address-named symbol, canonical release-helper prototype
and explicit header-pointer conversion; no unrelated shared-header repair.

1. Command zero reads pair word zero and releases the owner when it matches
   the stored reference, or when the tag matches pair byte four. Preserve
   short-circuiting and the actual owner argument to the release service.
2. Command 0x2D captures the current reference before the first pair word.
   A first-word match stores pair word one, then reads pair byte nine and
   writes the tag. Otherwise a second-word match stores the captured first
   word, then reads byte eight and updates the tag. The first match wins.
3. Other byte commands do not dereference either input. Preserve byte
   truncation and the full incoming A2 word home before narrowing.

The reference store can alias a later tag source, so keep each tag load
after its word store. Do not pre-cache both tags or replace the sequence
with a simultaneous structure copy. Guest NULL-pointer tests qualify
instruction access boundaries, not portable C NULL arithmetic.

## Derived Branch Guard

Reuse the existing semantic link-event shape and its
`game_link_event_callback.checked_parts` raw-body validator. The new typed
interface emits the same 43-word raw body under normal O2/g3. Four source
order/comparison screens retain one commutative comparison difference;
reordering the two loads additionally regresses their literal order.

At +0x88, word 34, raw `0x548A0005` compares A0 with T2; retail
`0x55440005` compares T2 with A0. Both are the same BNE-likely condition
with displacement five and the same RA-load delay slot. Equality/inequality
is symmetric for every register value, including signed/high-bit patterns.

Validate the complete raw-body hash and sole JAL binding, then derive the
replacement by exchanging only RS/RT fields. Keep opcode, displacement,
delay slot, frame, saved-register lifetime, code extent and relocations
unchanged. Append exactly one expected-word guard with no relocation at
that offset. There are no inserted/omitted instructions or profile changes.
This is guarded semantic C, not compiler-only matching.

Retain the unreachable duplicate pair-word load at +0x84. All 42 executable
root words are visited; the duplicate is not counted as visited or excluded
from the 43-word match. The sole release JAL binding remains at +0x44.

Raw body SHA-256:
`4d9d64e0a3911e4a931a63b7ad418cb8f237dbe1f8e305038ec0586129dc49ec`.
Resolved retail body SHA-256:
`24402ea6c07f6dd74d3aa730803a6b1e6e4e879599bc642aa14dda7f2d040435`.
Complete 44-word retail slot SHA-256:
`8284e7efc015baf9e55ce0c693c637622ed0c5567345e2fa4c4a592190eb104a`.
Normalized raw payload and bindings equal the independently assembled
original, rather than only agreeing at the current resolved address.

## Caller And Helper Boundaries

An aligned full-ROM scan finds no direct JAL sites and one literal pointer
at ROM `0x22F424`, VA `0x8008A964`: slot 35 of `D_8008A8D8`, 74 entries.
Verify that live table word and the retained dispatcher against retail.
The existing callback type is `void (*)(struct260 *,s32,u8)`; do not reuse
the previous recovery's distinct descriptor-table ABI or field offsets.

The full 23-word `func_15149434` dispatcher is already byte-exact and
unchanged. Execute it in 6,144 phases over all 256 selector bytes, null/
present callbacks, command/match cases and optional index-zero callback.
Check its unsigned header-byte read, >=74 fallback to zero, byte-command
narrowing and complete entry-to-return contract. All 23 words are visited.
Controlled table entries exercise lookup/call behavior, not every actual
unrelated handler in the production table.

Compile the actual retained dispatcher C together with the new root and
actual `func_1516972C` release C for native tests. Exercise all 28 release
words in 288 connected guest phases, including bookkeeping mutation before
the late kind read, low/high kinds and callback/fallback routing.
Bookkeeping, destructor and fallback remain bounded providers; no claim
of complete engine, gameplay or hardware acceptance.

## Focused Qualification

Both tools copies pass eight fresh checks before and after installation,
zero errors/failures/skips and zero reused checks. Pre-install primary/mirror:
59.103s / 59.060s; installed: 61.739s / 61.123s. Both shared tool checks
exit zero. Reuse existing MIPS, frame/fault, native32, source-span,
relocation, object/pool and normal generated-padder helpers.

- 19,440 original/raw/fitted guest phases cover all byte commands with
  upper-word variants, first/second/neither matches, signed/high reference
  patterns, tag boundaries, release mutations, seven alias layouts and two
  stack phases. Raw C and guarded code preserve complete original private
  state/events as well as independently checked public semantics.
- Native32 O0/O2/O3 trap UBSan covers 1,572,864 selected cases per
  optimization, ten effective defined wrong-C controls and 131,072 actual
  C-parent cases. Use full allocated backing and numeric native-endian
  words with byte accesses. Guest big-endian aliases/private homes are
  checked separately, not mislabeled as portable native behavior.
- Twenty-eight fired root-access fault prefixes compare original/raw/
  fitted private states, return lifetime, PC and delay origin. Five
  unsupported commands ignore NULL inputs in the guest model. This does
  not establish portable C fault semantics or hardware behavior.
- Forty-five normalizer negatives reject every changed raw word, missing
  binding and shortened body. Two actual generated-padder corruptions
  reject a changed expected word and wrong relocation expectation. A
  separate prefix mutation also fails closed; preserve all previous rows.
- Nine GNU links compare independently assembled original, qualified padded
  and actual Make objects at three code/helper address pairs. Execute 126
  rebased phases; four strict-image corruptions are rejected.

The new cache runner initially retained the previous module glob and was
corrected before qualification. Scratch fixture generation also needed its
literal newline escapes corrected; native Python syntax checking preceded
the first full passing suite. No production semantics, warning settings or
immutable-input constraints were relaxed.

## Production And Preservation

Advance the prior sealed baseline only for its three qualified source/
object/ELF overrides. Seal 15,958 initial files, adding the two owned tools
files in both copies: 15,962 files / 30 focused inputs / all 1,454 linker
objects. Use checked native stdin/tar bridges and verified Linux cache,
without DrvFS project reads.

Actual shadow Make uses three normal commands with IDO O2/g3 and the
generated-slice padder. Its complete padded object equals qualification.
Preserve all five raw/padded neighbors and pools, plus the complete caller
and release-owner objects. Isolated compiler diagnostics are empty;
whole-owner diagnostics are unchanged. The inherited duplicate
generated_12D630 recipe warning remains; no warning-free build claim.

Production Make exits zero in 0.585s. Its `-o retail_word_patches.us.csv`
avoids unrelated recompilation after appending an owner-specific row;
the modified owner still compiles through the actual padder with that row.
Independent and production links agree on exactly 119 changed ELF bytes:
118 target-code bytes and one target symbol-size byte, 12 to 172.
No metadata exclusions or unrelated changes. Preserve all other 6,054
bodies, all 6,055 addresses and protected Game data: 720 owners /
189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Audit all 15,962 native entries before/after adoption with exactly four
overrides: target source, guard CSV, target object and ELF. Recapture the
actual live adopted ELF and independently recount that stream, not an
inferred +1. The CSV diff is exactly one inserted row and zero removals;
its previous bytes remain an identical prefix. Existing CRLF notice remains.

Installed ELF SHA-256:
`77441b8262708606f7245e167a9f09fb33a7fa8f3fc0f48e788e0799aa514556`.
Installed target object SHA-256:
`04a51cc6f0d8d157ae5a06604de26175c83d1cc688a3ffc3944a5e0e7ced9daa`.
Guard CSV SHA-256:
`6d19dfd5806dedfc839f6c7e33f8fb2d1123d826021b93505bd7a265e516f427`.
Previous guard-prefix SHA-256:
`3a5b68d16b833e8b1e1c054f492606354062658a3bfa01cd520b97f9f29a5d1c`.

Preserve all 1,608 pre-existing older-mirror dirty paths/statuses/hashes/HEAD;
add only the two owned tools files, leaving 1,610 dirty paths. Do not reset
or commit that independent mirror. Host Release, saves, configuration,
private inputs, providers and packages are untouched.

## Measured Progress And Resume

| Section | Byte-Exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,775 / 5,505 (68.57%) | 0 | 1,730 |
| Game | 3,102 / 4,832 (64.20%) | 0 | 1,730 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Remove only `func_150B5840` from the live-ELF-pinned queue. Remaining
source screens: 1,601 placeholders, 120 semantic/other and nine unlocated
entries. Next real placeholder is `func_1512C150`, `generated_157840.c`,
44 words. `func_1510D8C0` already has a `Gfx *` C definition missed by
the parser and stays a separate uncredited matching case. Keep the 92-word
`func_1509E730`, 862-word `func_1508CAD8` and unmatched 121-word
`func_15169070` dispatcher separate. Target 4,129 exact C functions:
354 more, goal incomplete.

Root README changes only its two aggregate matching rows. Retain normal
post-commit Graphify worker receipts and audit all eight changed C/Markdown
hashes/mtimes/memberships plus all 43,972 prior nodes. The retained-corpus
warning remains; do not claim full-corpus re-extraction or old-edge retention,
and do not forge a missing commit stamp.

Ignored evidence: `conker/build/game-owner-reference-event/qualified/`.
Tools: `tools/experiments/game_owner_reference_event.py` and
`tools/tests/test_game_owner_reference_event.py`.
