# Shared Overlay Provider Guarded Match

Date: 2026-10-16. Consumer predecessor **7f6ca61c**, tools predecessor
**dc4765f**. Previous goal turn: **progress**, completing the per-view render
provider. Continue the full Game matching goal after this checkpoint.

## Recovered Routine

```text
func_150198FC  VA 0x150198FC..0x15019BB8  ROM 0x46DAC..0x47068
175 retail words / 700 bytes / frame 0x28
```

Replace the false zero-return C placeholder in game_45B80.c. Keep its stable
address-based name and add a semantic comment and Gfx * cursor interface:

- Perform the optional mode-1 pass before reading the live signed view maximum.
  For any nonzero maximum, including a negative value, publish maximum+1 with
  32-bit wrapping and emit its full-screen viewport. Zero uses the base view
  and leaves the current-view word untouched. Use unsigned scale arithmetic.
- Reset graphics state with the original six arguments, including view 255.
  Read the disabled byte after that callback, not at entry.
- When disabled and the signed capture byte is zero, emit SDK color-image and
  floating-point scissor commands, draw the backward-indexed framebuffer,
  restore graphics state, then explicitly set the capture byte to one.
  Callback writes to that byte must not replace the literal reset.
- For a nonzero signed capture byte below five, store its increment before
  calling the maintenance helper. Negative bytes participate; do not replace
  the comparison with an unsigned or 1..4-only test.
- Draw the current framebuffer after either disabled branch, using its live
  pointer after earlier callbacks. The enabled path resets the capture byte.
- Retain the view-zero rejection gate, live world argument, ordered UI chain,
  late disabled/requested flag reads, both mode-3 passes and final cursor return.

Capture/redraw is the working interpretation of the emitted color/scissor
commands and framebuffer-pointer protocol, not a new runtime visual result.

The alternate source at Another Source/CBFD-Recompiled/conker/conker/src/
game_45B80.c still uses GLOBAL_ASM for this routine. No donor C adoption or
host renderer repair is claimed. Add only owner-local declarations for the
signed counter and backward table label; shared headers and profiles stay fixed.

## Source Screens

Twenty-three complete-owner forms are reproducible through:

```sh
python3 -m tools.experiments.game_shared_overlay_pass --screens
python3 -m tools.experiments.game_shared_overlay_pass --types
python3 -m tools.experiments.game_shared_overlay_pass --structures
python3 -m tools.experiments.game_shared_overlay_pass --cursors
```

The selected semantic source emits **175 words / frame 0x28 / 79 raw
differences**. Signed viewport/count spelling, explicit/prefix/compound
increments, byte-array/struct/cast views and typed return spelling do not
improve it. Cached-phase variants have 176 words; unsigned-byte conditions
have 178, and an integer cursor has 86 differences. The outside-gate phase
form has 175/78 but is not an exact or qualified replacement. Do not mistake
equal length/frame or the smallest difference count for acceptance.

All **15 selected-owner neighbors** have unchanged raw bytes and relative
bindings, including the freshly restored per-view provider and the frame
driver whose integer argument cast is removed. Four existing Warning 712
sites retain their statements, caret columns and containing functions, with
physical source lines verified against a fresh predecessor compile.

## Derived Normalization

This is **not a direct C match or merely a global register permutation**.
Derive **79** expected-word/binding guards from the complete compiler object:

- Rename defined/used scratch roles within the viewport, color/scissor,
  counter and late-flag lifetimes. Preserve saved registers, frame and homes.
- Fold the counter's LUI/ADDIU/LB address sequence into LUI/LB. Rematerialize
  the high address in the increment arm and use the corresponding relocated
  low offset for its byte store, instead of preserving a scratch pointer.
  These three instruction-role rewrites are explicit in the normalizer.
- Reorder independent address/graphics preparation and the associated call
  positions through a complete 175-position placement map. Retarget branches
  using that map; transfer each moved call/data binding with its instruction.
- Exchange (-page)<<2 with -(page<<2) in unsigned 32-bit arithmetic. Verify
  all 256 page bytes and independent relocation carries.

No word insertion/omission, saved-register change, frame/home rewrite or
compiler-profile change. The raw object has **53** target bindings; the
normalized target has **55**, explicitly including the rematerialized counter
HI16/LO16 pair. A first provisional normalization misses two scratch uses;
the complete-word gate rejects it before installation. Preserve that ignored
failed receipt separately and use the qualified normalized-guards.csv.

```text
Raw target SHA-256
a8165e3f7012d81e4bf2d7b78648404f59a037a26ccdd510c6e801eaf49f846f
Guarded retail slot SHA-256
1c24e38cc9553d61c3cb85ab80eb111c8c4531348fafb9a45ae944591763eda4
```

## Focused Qualification

The corrected six-test pre-install suite passes in **45.886s**. The separate
real caller-cut test passes in **4.441s**:

- **3,240** retail/raw-C/guarded cases cover all 175 instructions, every one
  of the 256 counter/page/disabled encodings, signed count and dimension
  boundaries, f32 integer-rounding cases, two stack phases and ten fired
  mutation sites. Compare raw C's public protocol and complete retail/guarded
  modeled states. Hash the bounded 512-byte written prefix at each callback
  and compare all public memory at the end.
- **124** fired memory-access fault prefixes across six paths plus **32**
  repeated state transitions. These qualify emitted guest instruction order,
  not portable C faults or arbitrary hardware FCSR outcomes.
- Native32 separate units, O2/O0 with UBSan, **1,384 cases each**. Use one
  actual 256-word framebuffer array, with the retail label at its last
  element so every backward page index is in bounds. Check the complete
  cursor allocation, untouched table and callback prefix snapshots.
- Eight compiled controls fail observably: unsigned phase, reversed increment,
  positive-only viewport gate, wrong bounded table page, swapped scissor
  dimensions, cached flags, preserved callback phase and dropped final return.
  The table negative remains in bounds; no signal/UB/compile failure counts
  as an effective semantic rejection.
- Reject all **175** raw-word and **53** binding corruptions, an extra binding,
  unexpected pools, and every field of all 79 appended guard rows. The
  unmutated manifest is an explicit positive control with an exact byte prefix.
- Three independent original-assembly/padded-source links check all words,
  moved J26 bindings and both folded/rematerialized HI16/LO16 carry cases.
- **384** caller/provider cases use the freshly built, completely checked
  412-word C frame driver, its actual four-word call cut at 0x15018B68, and
  the real 175-word provider. Verify the post-return live count reload before
  global cursor publication. Stop at 0x15018B78; this does not qualify the
  remaining caller pipeline, unfinished providers or gameplay.

The first guard-field mutation test serialized the whole historical CSV,
changing mixed line endings before the intended field mutation. Preserve
the original prefix and verify an unchanged round trip. Reuse the already
qualified expected manifest for field-only byte mutations, after the
unmocked positive gate; do not reparse/rederive the unchanged object for
every field. Full installation checks still derive and validate it normally.
Confirm the exact owned processes/cwd, interrupt the obsolete tests at PIDs
1321189 and 1321729, drain both sessions to terminal, then rerun successfully.
The interruption ResourceWarning is not a production build failure.

These are bounded contracts, not completed graphics, hardware timing/FCSR
or gameplay acceptance. Unchanged broad neighbor suites are not fresh runs.

## First Whole-Image Prediction

Before installation, freeze the original owner object and link script and
reproduce the entire predecessor ELF. Independently predict only the target
slot and symbol-size change. The complete prediction changes **566 ELF
bytes**: **564** target-code bytes plus **two** size bytes (12 -> 700).
No metadata adjustment, reordering or section exclusion is required.

```text
ELF    5711ff13c02d9267df983aa9a23e7f47db4a6363c409dc8fde05ff1e002b4aa8
Owner  ef6b3c5ea8ebb03d5e6b9704e8cbc517b264773a9c97413e5a258c8e1e2d4556
Guards 0d03d88454cbbf2b26690ca5639320bae5672b16b2beb3381854e7d75a257577
```

The existing **2,226,298 guard bytes** are an exact prefix, including their
mixed line endings; append only 79 derived rows. Do not normalize history
or change Git configuration. The installed source and guards already equal
the first prediction. The normal shared-manifest rebuild exits 0; the entire
3,257,636-byte ELF equals that immutable first prediction. Existing warnings
and the duplicate generated_12D630 recipe warning remain in normal-build.log;
this is not a warning-free build.

All **ten final tests pass in 87.347s**, including the full installed-image
audit, all **106** live input controls, targeted code/caller/data/metadata
corruptions and the exact three-input successor with both fixture stages.
Preserve **103** other inputs, every unrelated function's body/address/extent
and protected **189,088 bytes / 720 owners**, with zero excluded sections.

## Verified Checkpoint

| Section | Converted | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,501 / 6,044 (91.02%) | 3,602 / 5,501 (65.48%) | 0 | 1,899 |
| Init | 492 / 539 (91.28%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,828 / 5,323 (90.70%) | 2,929 / 4,828 (60.67%) | 0 | 1,899 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

Conversion counts/bytes stay fixed because the old C stub already counted
as converted. Change only two aggregate README rows; check off the prior
provider item and retain the remaining queue explicitly.

Tools commit **d2251c7d36ddd7dbbed597c7535097148c8fbcc7** banks six focused
files before the consumer pin. Windows AST passes for all 12 files across
both copies; all six mirror copies are byte-identical. Eleven shared padder
tests pass in each checkout (0.055s consumer, 0.071s mirror), and make
tools-check passes. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **859** original dirty-file
hashes and **865** final dirty paths, without committing/resetting that
independent checkout. Prior unchanged broad suites are reused, not rerun.

## Resume Boundary

Next **func_15019CC8**, 102 words / 408 bytes / frame 0x40, ROM
0x47178..0x47310, still a 12-byte C stub. func_15019F20 (192 words), the
adjacent func_15094AB8, rectangle's 18-word fit and wider Game/additional-source
queue remain open. Do not describe the frame pipeline as complete.

Zero Claude calls. No push, account/auth retry, host-port edit/build/launch
or frozen Release action. Preserve the independently dirty older tools mirror.
