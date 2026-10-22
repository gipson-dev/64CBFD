# Category-Gated Framebuffer Fill Direct C Match

Date: 2026-10-22

## Result

Recover `func_15110600` in `conker/src/game/generated_13D350.c` from its
zero-return placeholder. All **42 words / 168 bytes, frame 40 and eleven
relocations** emit directly from C under the normal O2/g3 profile.
No guards, inserted instructions, dummy locals or profile changes.

VA 15110600..151106A8 / ROM 13DAB0..13DB58, ends exclusive. Preserve
`conker/asm/13D350.s`. Keep the address-based name, descriptive commands
parameter and purpose comment. Recover the Gfx pointer return and three
unused float parameters from the caller interface. The old body was 12 bytes
in its 168-byte slot; converted-C totals do not change.

Raw unlinked body SHA-256:
`c26471a6edb347254ad0bb557190e5bc06c39bf466499bd95c416ec2d607024b`.
Pin all eleven bindings: five global HI16/LO16 pairs and the helper JAL.

## Recovered Contract

Read the complete D_800BE9F0 category word once. Fill for 0x1B and 0x1E.
For 0x31 only, load D_800DBFF0, then its child pointer at +0x3D4, then the
unsigned child byte at +0x78; require exactly 3. Other categories must not
read that pointer chain. Rejected paths return the incoming commands pointer
without reading the dimensions or RGB bytes.

For an accepted path, call func_15110544 with this exact packet:

| Argument | Value |
| --- | --- |
| 0 | Incoming Gfx pointer |
| 1 | 2 |
| 2 | 0 |
| 3 | D_800BE620 minus 2, wrapping as a full word |
| 4 | Complete D_800BE624 word |
| 5 / 6 / 7 | Unsigned D_800DBEA8 bytes 0 / 1 / 2 |

The dimensions are the existing framebuffer width/height, confirmed by
init_39C0 and the graphics routines. These are full-frame bounds, not a
top-strip height. Spell the subtraction through u32 to avoid signed overflow
while retaining the exact ADDIU. Do not narrow categories or dimensions,
widen the child-byte load, sign-extend colors, swap channels or discard the
helper return, including NULL.

The current local helper definition remains its old s32-returning placeholder.
Keep the explicit Gfx-pointer cast at this word-return ABI boundary rather than
inventing an incompatible prototype or changing its unfinished body.
No shared header or caller-source changes.

Retail stores all three incoming float argument words to entry-SP +4/+8/+12,
even when no fill occurs. Preserve those complete homes, the 40-byte frame
and saved RA. Integer-parameter screens emit the same words, but identical
code does not supersede the actual caller's float-word transfer evidence.

## Caller And Helper Bounds

The aligned retail scan finds no direct JAL and one literal pointer at
ROM 22DCA4 / VA 800891E4: slot 3 of D_800891D8. This is static evidence,
not proof against dynamically constructed references.

Execute the actual 17-word caller window 15110244..15110288, stopping before
the mapped boundary word at 15110288. It stages the existing stack packet,
loads the table selection, transfers F12/F14/F18 through MFC1 to A1/A2/A3,
calls through T9, then copies the returned cursor to A0. Twenty-four phases
cover category/child gates, two SP phases, effectful helper behavior and NULL.
Initial FPRs, V0 and the already-established commands pointer are explicit
window-entry preconditions; earlier parent setup is not executed.

The full 267-word parent func_1510FEA0 remains a 12-byte production stub.
Do not claim a restored full caller or graphics workflow.

Separately execute the complete original 47-word func_15110544 together with
the current, independently byte-checked 19-word func_1501A680 and 38-word
func_1501A6CC providers. Across 72 phases, verify both framebuffer pages,
three dimension pairs, gates and the exact five-command payload: pipe sync,
render-mode setup, color image, duplicated RGBA5551 fill color and rectangle.
The active result is commands +40 bytes. The C fill-helper stub is not restored
or credited; command-byte evidence is not RDP/hardware or gameplay acceptance.

## Qualification

Tools, identical in both local copies:
`experiments/game_category_frame_fill.py` and
`tests/test_game_category_frame_fill.py`.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 6.381s | 8 tests, 6.389s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 1.806s | 2 tests, 1.798s | 0 / 0 / 0 |

Explicitly reuse the other six pre-install checks per copy only under strict
source, raw/padded object, helper/input and complete-image identity. They are
not fresh installed executions. Shared tools checks pass in both copies
(0.166/0.109s). Routine Codex qualification uses zero Claude calls.

- 4,288 guest phases visit all 42 words, cover all category/state bytes plus
  high-word category and dimension boundaries, and check full fences,
  unchanged unused homes and literal modeled private state. Opaque helpers
  change globals and clobber caller-saved registers/argument homes.
- Native32 O0/O2/O3 each pass 8,192 selected-body cases with trap UBSan.
  Seven effective defined wrong-C controls cover category/state gates, child
  width, color sign/order, width subtraction and discarded return. Use the
  established generic-view alias flag and aligned freestanding entry.
- Six independent GNU links cover three entry/global/helper rebases and
  48 phases, including signed-low relocation boundaries. Check 396 fired
  root-data fault prefixes and five strict whole-image corruption controls.
- Pin 30 historical inputs, both retained GLOBAL_ASM inputs and the old padded
  object. Preserve all 33 raw/padded owner neighbors and pools. Independent
  GNU assembly agrees in words/bindings; actual Make's five productive owner
  commands agree with the qualified raw and padded objects.
- Unbacked inactive context, dimensions and colors are genuinely unread.
  Raw unusual float words are guest ABI transport cases, not native arithmetic
  or FCSR/NaN acceptance. No portable C fault/MMU claim.

Harness bring-up corrected binding container types, base-oracle namespace
initialization and accidental display-list/stack overlap. Keep the disjointness
assertion and initialize task-specific anchors after the base constructor.
The complete emitted C body did not change during those fixture corrections.
A bounded per-process Linux PATH avoids Windows executable-lookup stalls;
no persistent environment or dependency change is made.

## Production

Commit tools first: `81b701f3deb885d31c83fc79e04bdaa3b3741b96`. No push.
Preserve all 1,548 prior older-mirror dirty paths, statuses, hashes and HEAD;
add only two task files, leaving 1,550 dirty paths. Do not reset or commit it.

Seal 15,842 files, including all 1,454 linker objects. Normal Make in the
verified Linux copy completes in 0.542s. The existing duplicate
generated_12D630 recipe warning remains; no new target compiler diagnostics.
This is not a warning-free or clean-from-scratch build.

Every static input and non-target object remains byte-identical. Revalidate
live bytes before and after adopting only the owner object, ELF, linker script
and progress CSV; linker-script and conversion-CSV bytes remain unchanged.
Live adoption audit: 47.766s.

The independent full-ELF prediction is reproduced with zero exclusions:
**136 changed bytes =135 code bytes +1 target-size metadata byte**.
No symbol reordering or other metadata adjustment is needed. Preserve all
other 6,054 bodies, all 6,055 addresses and all 720 protected Game-data owners /
189,088 bytes. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
ELF SHA-256:
`7b60d04532880d1f7196594913fc1545714644388bc727b8b4775fa9c18b7b60`.
Padded owner SHA-256:
`9215ca9c8a8b08e8c2ff6be7ecc2db7955e5083f776e29cff16204864ac62bf9`.

## Handoff

The standard matcher against the actual live ELF completes in 33.300s:
total **3,736/5,505 (67.87%)**, Game **3,063/4,832 (63.39%)**,
Init 492/492 and Debugger 181/181 exact. Zero address drift; 1,769 different.
The 75% threshold remains 4,129 exact, requiring **393 more matches**.
Queue shapes: 1,638 placeholders, 122 semantic/other and nine unlocated.
Next func_1514A4EC is screened only, unmodified and uncredited.
Keep func_1508CAD8's 862-word stub queued.

Root README changes only its two aggregate rows. Detailed progress stays
here and in concise indexes. Post-commit graph-worker and every-old-node
retention audits remain private receipts; retain the excluded-corpus/large-HTML
caveats without claiming full re-extraction or a fresh corpus-membership count.
Frozen host Release remains untouched.
