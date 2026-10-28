# 1749 - RGB rectangle fill direct C match

Verified: 2026-10-27. Target `func_15110544`, owner `generated_13D350`.
VA `15110544..15110600`; retail ROM `13D9F4..13DAB0`.

## Result and recovered behavior

Replace the zero-return placeholder with the complete 47-word /188-byte routine.
Every word emits directly from the normal O2/g3 C profile: frame 0x20, two
R_MIPS_26 call bindings, zero new guards. All 33 owner neighbors and literal
pools remain fixed; all 34 compact functions match the actual Make output.

The recovered interface is `Gfx *(Gfx *, s32 left, s32 top, s32 right,
s32 bottom, u8 red, u8 green, u8 blue)`. The O32 incoming coordinate words
remain full-width signed values. On the big-endian guest, colors come from
incoming SP+23, +27 and +31, ignoring the high three bytes of each argument
word. Preserve the incoming coordinate homes and the color reads after the
first helper returns. The last coordinate is forwarded as the fifth argument
in the second call's delay slot.

Use SDK graphics macros to emit pipe sync, fill-cycle other mode, the selected
RGBA16 color image, a repeated RGBA5551 fill color, and a clipped rectangle.
Other-mode words remain EF302C0F/00000004: fill cycle, bilinear filter,
filtered conversion, primitive depth source and the retail legacy blend-mask
nibble 0xF. That unsupported legacy nibble remains explicit rather than being
silently dropped. Alpha is one. Cast the packed color to u32 before shifting
it left 16; this keeps native C defined without changing any retail word.

`func_1501A680` appends the selected framebuffer's RGBA16 color-image command
and returns the next cursor. `func_1501A6CC` clips left to at least 2 and top
to at least 0, caps right at width-2 and bottom at height, then appends the
fill rectangle. Preserve each helper's returned cursor, including the final
return. Their existing 19- and 38-word linked bodies are already byte-exact.
No shared declarations, helpers, build flags or guard rows change here.

## Actual callers and graphics integration

An aligned whole-ROM census finds six JAL references and no direct pointer
literal or tail J. Call sites are ROM 127004, 13D47C, 13D698, 13D908, 13DB38
and 13F168 (VA 150F9B54, 1510FFCC, 151101E8, 15110458, 15110688 and 15111CB8).
The original envelopes pass four coordinate words and three color words;
colors are either zero, byte table loads or the constants 22/28/27. Several
coordinates come from truncated record floats; that wider conversion behavior
is not newly qualified by this integer routine.

Run the complete original 42-word `func_15110600` category caller with the
recovered target and both original/existing helper bodies. All 42 caller
words and every word of both helpers are visited across 96 cases. Check the
five actual commands and returned cursor for active categories 27/30/49,
child-state gates, both framebuffers, three dimensions and two stack phases.
The other five callers receive static interface review; no complete parent
or gameplay acceptance is claimed for them.

## Fresh qualification and explicit reuse

Both canonical tools copies pass eight fresh target methods plus their shared
tools checks. Each installed copy then runs owner/image checks fresh and reuses
the other six semantic receipts only after full module/input/artifact identity.

- 9,232 guest cases cover all three byte channels, high-word noise, signed
  coordinate boundaries, two stack phases, output/incoming-home overlap and
  four effectful provider modes. All 47 target words are visited. Compare full
  private machine state and memory/access traces between original and rebuilt.
- Native32 O0/O2/O3 with trapping UBSan pass 3,840 positive cases per profile
  and seven effective bounded C controls. Typed eight-argument calls, all red
  bytes, varied green/blue, cursor redirects, final return and unchanged output
  canaries are checked. Native helpers remain explicit bounded contracts.
- 800 real-helper cases verify signed clipping boundaries, both framebuffers,
  actual command encoding and cursor advancement. 114 fired guest fault-prefix
  pairs check instruction/PC/delay-slot and complete state agreement. These
  fault checks describe emitted guest instructions, not portable C faults.
- Six independent GNU links over three layouts, including a different JAL
  region, preserve both call bindings and pass 12 effectful guest cases.
  Three raw-word/binding controls, seven full-image corruptions and three
  wrong-input controls fail closed.
- An actual compiled early-color-capture mutant is rejected by post-helper
  incoming-home mutation. An ordinary temporary was initially optimized back
  to the original late-load shape, so that ineffective witness was replaced
  with a volatile early capture. Production C and its artifacts did not change.

The first harness attempt lacked the prepared evidence fingerprint. Early
Make assertions assumed a three-command owner; this owner uses the existing
five-command asm-processor/IDO/postprocess/padder/assembler recipe. Corrected
receipts retain the failures and use that actual recipe. Neither issue was a
production function defect. Routine Claude budget/calls: zero.

## Build, strict image and actual recount

Normal production Make passes, with only the inherited duplicate 12D630 recipe
warning. The independent complete-ELF prediction allows exactly 139 changed
code bytes and one symbol-size byte, 140 total, with zero exclusions. All
6,056 function addresses and the other 6,055 bodies remain fixed. Protected
Game data remains exact: 720 owners /189,088 bytes, zero differences.

The Native/cache audit verifies 16,172 sealed inputs and 133 focused inputs,
with only the qualified source, owner object, ELF and map overrides. C inventory
and the complete guard CSV are unchanged. Native guard CSV SHA-256:
`bc18bdc4633b2387568bc04ee6f816ede14290f391446f745a97b44027eecc59`.
ELF SHA-256:
`a9cb525e36f47e0e5cccd406f0082c1cefba460988ecc97cebac39d2ba776f8c`.

Recount the captured adopted Native ELF, not a private candidate:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,827 /5,506 (69.51%) | 1,679 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,154 /4,833 (65.26%) | 1,679 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

The sole newly exact entry is `func_15110544`. Conversion totals stay fixed.
The 75% threshold is 4,130, requiring 303 more exact matches. Remaining source
screens: 1,550 placeholders, 120 semantic/other definitions and nine unlocated
entries. These shapes are not matching qualification.

## Banking and resume

Predecessor consumer `f0d05191112f882123c256e5002f38f588723202`, tools
`f77d4b4af6358f81480ecf638ddc53490bed53ad`. Bank qualified tools first at
`5a5f2e5dccbd48131f5b06a8a5866e55d6621b99`, then source, consumer pin and
measured docs. Preserve the old tools mirror's 1,708 inherited dirty paths
plus the two new qualification files; do not commit its independent history.
No push. Root README receives only its two aggregate rows.

Graphify refresh is scoped to the ten changed code/document/tool files, with
source-aware node and relationship retention checked before adoption. Preserve
historical communities and outside-manifest rows; no full-corpus extraction,
global clustering or centrality claim. Final graph receipts and the independent
final audit live in the ignored stage below.

Evidence: `conker/build/game-rgb-fill-rectangle-match/`, especially
`preparation.json`, canonical/installed receipts, `sealed-production-proof.json`,
`sealed-live-adoption-audit.json`, `75-percent-queue.json` and `FINAL_AUDIT.json`.
Next inspect `func_15147040` in `generated_173D40` (47 words), beginning with
graph/source/retail/caller review and a new frozen predecessor. Keep
`func_1514E920` parked as private/uncredited. The 75% goal remains active.
