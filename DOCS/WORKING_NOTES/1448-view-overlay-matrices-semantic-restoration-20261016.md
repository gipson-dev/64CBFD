# View Overlay Matrices Semantic Restoration

Date: 2026-10-16. Consumer predecessor **ca914feeb**, tools predecessor
**d2251c7**. The preceding checkpoint completed func_150198FC. Continue the
wider Game matching goal after this checkpoint; this restoration is **not
byte-exact** and does not increase the matching totals.

## Recovered Routine

```text
func_15019CC8  VA 0x15019CC8..0x15019E60  ROM 0x47178..0x47310
102 retail words / 408 bytes / frame 0x40
98 emitted C words / 392 bytes / frame 0x40 / 94 slot-word differences
```

Replace the false 12-byte zero-return C placeholder in game_45B80.c. Retain
the stable address-based name and add the semantic comment, Gfx * cursor
parameter and full-word view parameter. The caller's obsolete integer cursor
cast is removed without changing its machine code.

- Emit the SDK viewport using the full 32-bit view, a 0x180-byte view stride,
  the live page byte's 16-byte stride and offset 0x40. Unsigned arithmetic
  preserves the guest's 32-bit wrapping for high and negative view encodings.
- Narrow the view only for the signed-16-bit helper arguments. Call the
  six-argument graphics reset with four zero arguments after the view.
- Emit MODELVIEW/LOAD/NOPUSH with D_80089470, then PROJECTION/LOAD/NOPUSH
  with the live base/page address and offset 0x100. DA380007 is not PUSH.
- Read the live full category word after setup. Exactly 0x1D enables the
  mode-6 category pass; matching only the low halfword would be incorrect.
- Append both mode-5 passes with view zero and final arguments zero then one.
  Emit the live projection matrix again, then PROJECTION/MUL/NOPUSH using
  the page-pointer table and the full view's 64-byte stride. Return the cursor.

The legacy D_800DC2A0 pointer declaration labels the table itself. Address
that label before indexing, not its pointee; the source comment records this
distinction. Native qualification binds it to a real 256-word array, with
all page indices and the wrong-page control remaining in bounds. Shared
headers and compiler profiles are unchanged.

The alternate source at Another Source/CBFD-Recompiled/conker/conker/src/
game_45B80.c still uses GLOBAL_ASM here. No donor C or host renderer change
is claimed. These command meanings are a static interpretation, not fresh
visual/gameplay acceptance.

## Matching Still Open

All **49** complete-owner source/profile screens have receipts in the ignored
conker/build/game-view-overlay-pass directory. Reproduce the groups through:

```sh
python3 -m tools.experiments.game_view_overlay_pass --screens
python3 -m tools.experiments.game_view_overlay_pass --lifetimes
python3 -m tools.experiments.game_view_overlay_pass --cursors
python3 -m tools.experiments.game_view_overlay_pass --profiles
python3 -m tools.experiments.game_view_overlay_pass --integers
python3 -m tools.experiments.game_view_overlay_pass --carriers
python3 -m tools.experiments.game_view_overlay_pass --expressions
python3 -m tools.experiments.game_view_overlay_pass --pointers
```

Screens cover register hints, signed/unsigned products, int versus SDK long,
narrowed-local lifetimes, mutable parameter carriers, integer/split cursors,
equivalent scale expressions and typed pointer bases. Lengths are 97, 98,
99, 101, 103, 138 or 141 words; none recovers the full retail shape. The first
integer-return screen has a mismatched local prototype; correct the screen's
prototype derivation and rerun all five pointer/return screens successfully.
That diagnostic is not a production failure.

The selected ordinary semantic source emits **98 words / frame 0x40**.
Retail retains the full view in S0, saves S0/RA at SP+0x20/+0x24 and the
narrowed view word at SP+0x28, and recomputes the three 0x180-byte offsets.
The candidate instead uses the incoming argument home at SP+0x44, caches the
scaled offset, saves RA at SP+0x1C and does not use S0. Frame-size agreement
does not establish saved-register lifetime or stack-layout agreement.

Use the existing normal O2/g3 profile and padder. Add **zero word guards**,
instruction insertions or source assembly. The four zero padding words after
the emitted return preserve the retail slot boundary; they do not close the
instruction difference. The linked symbol extent is 392, not 408 bytes.

```text
Raw C SHA-256
ae42e63a7e607f8266c98ac290d964a0a6902e33200ca5f485cd21d1b97a2146
Unguarded 408-byte slot SHA-256
814f9f2177f63bf9efe050a8a16d8fc3e96d5d1e73a15380e533e12ad62d0b56
```

## Qualification

The six pre-install tests pass in **39.683s**. All **nine final tests pass in
86.850s**, including the installed-image and successor controls:

- **3,584** retail/raw-C guest cases, all 256 page encodings, full-word view
  boundaries, signed helper arguments, category gates and two stack phases.
  Visit all 102 retail and 98 emitted instructions. Five effect sites fire,
  including a guest-only page change between the last two matrix commands.
  Compare public memory, ordered calls, cursor returns and 512-byte callback
  prefix hashes. The shared engine checks saved registers, stack and RA.
- **1,536 native32 cases each** at O2 and O0 with UBSan, separate translation
  units and the actual SDK macro body. Check the complete cursor allocation,
  table and callback snapshots. Eight compiled semantic controls reject with
  explicit exits 21/22/23/25, not signals, UB or compilation failure.
- Reject all **98** raw-word corruptions, all **24** binding corruptions,
  an extra binding and unexpected pools. Three independent source links
  verify all 98 words and 24 bindings across HI16/LO16 carries and JAL rebases.
  These are source relocation checks, not original/source byte identity.
- **75** caller/provider cases use the freshly checked full 412-word frame
  driver and its real three-word cut at 0x15018B98..0x15018BA4. Exercise the
  full-word view load in the call delay slot and the returned cursor store.
  This is not the previous provider's four-word cut or the full frame pipeline.
- Preserve all **15** owner neighbors' raw bytes and bindings. Four old
  Warning 712 sites retain their statements, caret columns and containing
  functions, with actual physical source lines checked against the predecessor.

Public semantic and ABI checks do not establish identical private stack state,
register scheduling, emitted access-fault prefixes, arbitrary alias behavior,
hardware timing or gameplay. Those instruction-level differences remain open.
Prior unchanged broad neighbor suites are reused, not represented as fresh runs.

## Complete Installed Image

Before installation, freeze the old owner object and linker script, reproduce
the complete predecessor ELF and independently predict only this slot and its
symbol-size change. The first whole-image prediction changes **324 bytes**:
322 target-code bytes plus two size bytes for 12 -> 392. No metadata adjustment,
serialization change, reordering or excluded section is needed.

```text
ELF    132fce9cd5b0394cc37ad6909381a5ddf06f95407054387f8270a1060c77b131
Owner  fb6e0f93f93502e9fdcfdaf5e441a6e9492d684cf93ef7e51c66b8ccdc123c11
Guards 0d03d88454cbbf2b26690ca5639320bae5672b16b2beb3381854e7d75a257577
```

The final normal build exits 0 and all 3,257,636 ELF bytes equal that first
prediction. The installed source also equals its first prediction. Preserve
the complete guard CSV byte-for-byte, all **105** other captured inputs and
protected **189,088 bytes / 720 owners**, with zero excluded sections. Controls
reject alterations to all **107** captured live inputs and selected target,
caller, data and symbol/metadata bytes. The two-input successor fixture accepts
only the exact measured source/ELF pair; both fixture stages are tested.

Existing pointer/integer and duplicate generated_12D630 recipe warnings remain
in normal-build-final.log. This is not a warning-free build.

## Checkpoint And Resume

Fresh official matching numbers are **unchanged**:

| Section | Converted | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,501 / 6,044 (91.02%) | 3,602 / 5,501 (65.48%) | 0 | 1,899 |
| Init | 492 / 539 (91.28%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,828 / 5,323 (90.70%) | 2,929 / 4,828 (60.67%) | 0 | 1,899 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

Conversion counts/bytes are also unchanged because the old C stub already
counted as converted. Root README aggregate rows remain correct and untouched;
keep the function narrative here and in concise working indexes.

Tools commit **e5a8f98** banks the six focused files before the consumer pin.
Windows AST checks pass for all 12 files across both copies; the six new mirror
files are byte-identical. Eleven shared padder tests pass in each checkout
(0.069s consumer, 0.049s mirror), and make tools-check passes. Preserve older
mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **865** original
dirty-file hashes and **871** final dirty paths. Do not commit or reset it.

Next: the source restoration is complete, but **func_15019CC8's instruction
match remains open**. A bounded UOPT lifetime/CSE investigation should explain
the lost S0 carrier and cached index before any normalization is considered;
do not repeat the same 49 spelling screens or call four trailing NOPs a match.
func_15019F20 remains a 192-word C stub. The adjacent func_15094AB8, rectangle's
18-word fit and wider Game/additional-source queue remain open.

Zero Claude calls. No push, host-port edit/build/launch or frozen Release action.
