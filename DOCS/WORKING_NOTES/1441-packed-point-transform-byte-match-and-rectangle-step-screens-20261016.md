# Packed Point Transform Byte Match And Rectangle Step Screens

Date: 2026-10-16. Consumer predecessor **c2032e34**, tools predecessor
**e3dca0d**. Previous goal turn: **progress**, establishing actual UOPT
temporary blockers. The wider Game matching goal stays active.

## Rectangle Follow-Through

`game_packet_rectangle_step_lifetime.py` measures **12** complete-owner
sources against the installed 18-word rectangle baseline: the predecessor,
six signed/unsigned S/T halfword forms, three used original-T role splits
and two explicit SDK-equivalent staged-corner forms. All compile without
diagnostics; none improves the fit. Revalidate physical objects, bindings,
linked words, frame and frozen inputs, not just stored scores.

Unsigned S alone keeps 346 words / frame 0x88 but has **19 differences**,
adding earlier masking and shortening the literal prefix. Unsigned T/both
add a word. Signed forms change length/frame. Splitting the original T role
keeps 346 words but grows the frame to 0x90. Staging lower corners after the
first command-word store uses actual scalar roles, not padding, but emits
348/350 words with 303/304 differences. Install none of these.

**func_15095D34 remains 346 words / frame 0x88 / 18 differences**, literal
148/91-word spans. Keep its twelve flip-block scratch/schedule words and six
macro-home accesses open. The new single-function recovery below does not
erase that task or count the rectangle as matched.

## Recovered Transform

Advance another unfinished Game routine in the same owner,
`conker/src/game/generated_C1D70.c`:

```text
func_150948C0  VA 0x150948C0..0x1509499C  ROM 0xC1D70..0xC1E4C
55 words / 220 bytes / frame 0x90
```

Replace its false zero-return placeholder with a void signed-coordinate
transform. A packed source supplies the slot range at byte 1 and a pointer
to 16-byte coordinate rows at byte 4. Its provider fills a private 16-pointer
table. Visit all sixteen slots, transform each non-null row's first three
**signed halfwords** through `func_150A7960` using the current global matrix
pointer, and write a 12-byte float output row. Leave unpopulated outputs
untouched. Keep the original two incoming arguments and seven-argument
matrix-call ABI.

The adjacent additional-source draft is only a semantic lead: its incomplete
incoming signature and incorrect 32-bit coordinate accesses are not imported.
Retail loads, offsets, stride, frame, call sites and stores are authoritative.
Name the minimal source view `PackedPointSource948C0`, and add the recovered
behavior comment beside the function.

The first complete-owner draft has 56 words because the explicit cursor
keeps an extra array-base expression across the provider call. Recover
indexed traversal and the original displacement-first output address to get
the original 55 words and frame. The only remaining raw differences are:

```text
+0x30  move s0,zero          -> addiu s2,s2,%lo(D_800D2C20)
+0x34  addiu s2,s2,%lo(...) -> move s0,zero
```

These independent, non-trapping ALU instructions initialize separate
registers before either is consumed. Two expected-word/relocation guards
normalize that closed schedule. Preserve the raw low-half immediate as zero
and guard its actual `R_MIPS_LO16` binding; the first qualification correctly
rejects a mistakenly linked immediate in the relocatable expected word.
No other instructions, profile, insertion, omission or guard history change.

Raw C target SHA-256:
`ec77730c11f7586e3749fbbace26b2fa2d575272ac174ee1c09a2fa1ae968d10`.
The linked, guarded slot is exactly all 55 retail words, SHA-256:
`052c22bf6fbe9f23e5d4c3ffd9b9d1e5a2bc6192f556a42fa6845216127da0ad`.

## Explicit Provider Boundary

**func_1509499C is not restored or newly matched.** Its guarded/unrolled
slot-builder drafts do not reproduce retail's 71 words; they stay in the
experiment only. Preserve its existing production stub byte-for-byte and
do not claim the installed pair or a working gameplay pipeline. The caller
uses its existing return declaration and ignores the return value.

Qualification connects the wrapper to the **real 71-word retail provider**
and **real 40-word matrix routine**. This proves the recovered caller's
contract; it is not a claim that those original bytes replace the current
provider stub in the installed ELF. Eighteen neighboring function bodies
and relative bindings, including the provider and rectangle, remain fixed.

## Qualification And Image Scope

Seven pre-install tests pass in **50.291s**. They include **2,048** range /
stack-phase / alias fixtures, each executing original, raw-C and normalized
wrapper bodies with the real retail helpers. Compare complete modeled
GPR/FPR/memory/call/access state across all three bodies and independently
check public outputs. Cover all **256** range bytes, phases 0/8, disjoint
output and output aliases with point data or source storage.
These alias receipts apply to compiled flat-guest execution, not portable C
strict-aliasing guarantees; native cases use valid disjoint storage.

Separate native 32-bit O2/O0 units with UBSan pass **2,560 cases each**;
four effective controls reject wrong loop count, unsigned coordinates,
output stride and coordinate selection through observable mismatches.
The native slot provider is a contract fixture, not restored production C.
Retain the existing limits on hardware FCSR/fault/async/gameplay claims.

Freeze the complete first ELF prediction before installation. The initial
slot/extent-only prediction correctly rejects an additional **40-byte**
metadata reorder. Account explicitly for the adjacent `func_151AF388` /
`D_80089974` symbol entries and their string records, preserving all values,
sizes, attributes and ownership. No new symbols, metadata exclusions or
unexplained bytes are accepted.

The final first prediction changes **208 ELF bytes**: 167 code bytes, one
function-size byte (12 -> 220), and 40 explicitly serialized symbol/string
bytes. All 97 other tracked inputs remain fixed; preserve prior guards as
an exact byte prefix before appending the two new rows.

Strict after fingerprints:

```text
ELF    fee3933f88d705e9f424ef7ffce1d914f806bdb78a260e86cafb770bb1629796
Owner  57ff978c80acf2972ac16c211abf7aefc38047b947b7aeb8d67d20e92149b71b
Guards 795d726ce98edecbc1b2666efec10628dfe4d0cf1621499f737ce76f3eef2aec
```

The shared CSV dependency triggers a broad normal guest-object rebuild.
Pre-existing duplicate `generated_12D630` recipe and pointer/varargs/long-
double warnings in unrelated slices are not new target diagnostics and are
not silently repaired. No host-port or frozen Release build is authorized.

## Verified Checkpoint

The normal guest build finishes with exit 0. All **ten final tests pass in
103.223s**: seven semantic/source/prelink tests plus three installed-image
tests. The entire 3,257,636-byte installed ELF equals the first prediction,
with precisely the 208 changes described above. Protected **189,088 bytes /
720 owners** are exact, all 18 neighbors and 97 other inputs remain fixed,
and the prior guard CSV is an exact byte prefix. The exact-successor adapter
recognizes only the three fingerprints above and verifies their saved
predecessors; unknown live inputs are not normalized.

Fresh official measurements:

| Section | Converted | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,501 / 6,044 (91.02%) | 3,596 / 5,501 (65.37%) | 0 | 1,905 |
| Init | 492 / 539 (91.28%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,828 / 5,323 (90.70%) | 2,923 / 4,828 (60.54%) | 0 | 1,905 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

Only the exact counts increase by one; the replaced placeholder already
counted as converted C. Root README edits are restricted to the two affected
aggregate match rows. Detailed updates stay in this note and the five
working-document indexes.

Tools commit **6909297872940316dd97c8453ca3aaadf6dd0fc7** banks the five
experiment/checkpoint/test files before the consumer pin. Windows AST parsing
passes for all ten files across both tools copies; the five mirrored files
are byte-identical. All eleven shared padder tests pass in each copy
(0.050s consumer, 0.047s old mirror), and `make tools-check` passes. Preserve
the old mirror's HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **828**
initial dirty-file hashes and **833** final dirty paths. Do not commit or
reset that independent mirror.

## Resume Boundary

Continue both open jobs after this checkpoint: the rectangle's 18-word fit
and the original 71-word slot provider. Keep all broader Game, additional-
source, caller and inherited-stack queues open. No push, Claude/auth retry,
or host-port/frozen Release edit or launch occurs.
