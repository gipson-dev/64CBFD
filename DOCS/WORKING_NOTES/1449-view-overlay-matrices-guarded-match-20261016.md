# View Overlay Matrices Guarded Match

Date: 2026-10-16. Consumer predecessor **4e0fef10**, tools predecessor
**e5a8f98**. The previous turn made semantic progress in Note 1448; this
checkpoint closes func_15019CC8's remaining instruction match. Keep the full
Game matching goal open after banking this function.

## Complete Target

```text
func_15019CC8  VA 0x15019CC8..0x15019E60  ROM 0x47178..0x47310
102 words / 408 bytes / frame 0x40
Raw C: 102 words, 37 differences. Guarded output: all 102 words byte-exact.
```

Retain the complete viewport/matrix/category/mode-5 protocol recovered in
[Note 1448](1448-view-overlay-matrices-semantic-restoration-20261016.md).
Full-word view addressing, unsigned wrapping, signed-16 helper arguments,
live base/page/category reads, the page-pointer label and final cursor are
unchanged. No shared header, caller interface or compiler-profile change.

Remove the separate narrowed local and cast at its two helper uses. Keep
the three equivalent unsigned scale trees distinct:

```c
(u32)view * 0x180
((u32)view * 3) << 7
(((u32)view << 2) - (u32)view) << 7
```

All are view*384 modulo 2^32. These matching-oriented spellings recover the
carrier lifetime; they are not proof of the original source spelling.
Each shift expression is enclosed before adding the live base/page offsets.
The emitted C now preserves S0, saves S0/RA at SP+0x20/+0x24, stores the
sign-extended helper view at SP+0x28, recomputes all three offsets, and emits
the complete original epilogue. The former four trailing padding words are
no longer needed; the actual function extent grows from 392 to 408 bytes.

## Compiler Evidence

Reuse the existing fingerprint-locked UOPT debugger setup with this owner's
normal **O2/g3** profile. The text-measurer helper's loop-unroll override is
explicitly excluded. The new adapter consumes the immutable Note 1448 owner
snapshot and its selected refinement, leaving current source/ELF/guards
unchanged. It can be rerun after installation without substituting current
source for the frozen diagnostic input.

```sh
python3 -m tools.experiments.game_view_overlay_uopt_trace --variant baseline --mode 5
python3 -m tools.experiments.game_view_overlay_uopt_trace --variant baseline --mode 6
python3 -m tools.experiments.game_view_overlay_uopt_trace --variant selected --mode 5
python3 -m tools.experiments.game_view_overlay_uopt_trace --variant selected --mode 6
python3 -m tools.experiments.game_view_overlay_address_candidates
```

Both sources mark the full-view parameter as virtual-register variable
**284|0**, expression 10, storage P, procedure 2719, offset 4. That frontend
marker alone does not imply physical register retention. Baseline mode5
shows three uncolored view ranges, colors **[-1, -1, -1]**. The selected
source has one view range with internal color **14**, and its independently
checked object actually uses S0. Internal color 14 is not MIPS GPR 14.

Baseline UOPT shares its view*384 expression across callbacks. The selected
source exposes distinct multiply, multiply/shift and shift/subtract/shift
trees, retaining the full view instead. Every diagnostic requires the fired
stream-buffer and suppressed-real-printer probes, successful owned child/driver
completion, and unchanged complete text/functions/bindings/pools versus a
normal compile. Compiler fingerprints are locked; no compiler or debugger is
installed or modified. Suppressed real-number output supplies no valid numeric
timings or cost measurements.

The old scale-mixed spelling in Note 1448 omitted the outer parentheses around
a shift. Its promising saved-register shape was not semantic evidence and it
was never installed. Ten corrected address-tree screens replace that result.
The selected direct-cast form has 102 words / frame 0x40 / 37 differences.
The 35-difference alternative would require an arithmetic rewrite; this
selection requires only temporary-role normalization.

## Derived Guards

Append **37 expected-word/binding guards** derived from the complete raw
object. Preserve all existing guard bytes as an exact mixed-line-ending prefix.

- Rename only defined/used scratch roles in the two projection blocks,
  category gate, final matrix command and page-table address chain.
- Coalesce the raw last projection's non-overlapping temporary lifetimes
  into retail's reused T8 role. This is not one global register permutation.
- Preserve every opcode, immediate, shift, branch, instruction position,
  call delay, frame/home access and all **24** binding positions/kinds/names.
  No scheduling move, arithmetic rewrite, insertion, omission or trampoline.

```text
Raw C SHA-256
82f129eefc33dbf4f8df37348dd0d0404992fe2b1a0c905b9f4a49568520007a
Guarded retail slot SHA-256
9fca17d91442d21fe0acf95915a4848ed0ef1b2ea2fe7f2ab03dbd8330cd72d3
```

An initial expected-binding table puts the setup JAL at 0x74. The object
gate rejects it; inspection confirms 0x70 and the table is corrected before
manifest generation or installation. This is a fixture error, not a compiler
or production defect.

## Qualification

The corrected **eight-test pre-install suite passes in 70.903s**:

- **3,584 three-way guest cases**, all 256 page encodings, full-word view
  boundaries, signed helper arguments, category gates, two stack phases and
  five fired effects. Visit all 102 instructions. Compare complete memory
  and public protocol for raw C, and complete modeled state for retail/guarded.
  Callback snapshots include the 512-byte command prefix.
- **158** fired memory-access fault prefixes across six paths. Raw C retains
  complete memory, access events and call order; normalized output retains
  complete retail state. This qualifies emitted guest order, not portable C
  faults, arbitrary aliases, hardware timing or gameplay.
- **1,536 native32 cases each** at O2/O0 with UBSan, the actual SDK body in
  separate units, a real 256-word table, complete command-buffer/table checks
  and eight compiled semantic controls with explicit rejection exits.
- Reject all **102** raw-word and **24** binding corruptions, unexpected pools
  and every field of all **37** appended guards. Check an unmodified positive
  manifest and exact prefix before field-only mutations. Verify only register
  fields differ in the raw-to-normalized instruction templates.
- Three independent original-assembly/padded-source links check all 102 words
  and 24 bindings, including HI16/LO16 carries and JAL rebases.
- **75** actual caller cases retain the fresh full 412-word frame driver,
  its three-word cut at 0x15018B98..0x15018BA4, full-word delay-slot view load
  and returned cursor publication. This is not the entire frame pipeline.
- Four owned normal-profile UOPT compiles qualify baseline/selected mode5/6
  diagnostics, integer view colors, procedure boundaries and full object
  identity. No numeric real diagnostics are used.

All **15** owner neighbors retain their raw bytes and bindings, and all four
old Warning 712 sites retain their statements/carets/functions with physical
source lines checked. The first test draft used stack-store index 26 instead
of 24, and compared linked addresses with unlinked templates. Correct both
assertions and rerun successfully; neither is a production failure.

## Complete Image

The frozen owner/link-script inputs reproduce the complete Note 1448 ELF.
Independently predict only the 408-byte target slot and 392 -> 408 symbol-size
change. The complete first prediction changes **318 ELF bytes**: 317 code
bytes plus one size byte. No serialization adjustment, reordered metadata or
excluded section is required.

```text
ELF    088cddcb3aaf1085034a492241d590ed1542344da71d608ec5a7c510937330a0
Owner  bc4ea6e920cb471bdc9d17f336deffa4d0a464ca66c50920379e2c2b329428e9
Guards e09a6696c524fad38b6c2cbefdb4c8249e012efdd59b6a14cc51ac5958939239
```

The normal shared-manifest rebuild exits 0. Its complete owner object equals
the qualified padded object, including every function and binding. All
3,257,636 ELF bytes equal the immutable first prediction, as do the installed
source and guard manifest. The shared-manifest change rebuilds other guarded
owners as normal; their linked bodies/data remain unchanged. Existing warnings,
including the duplicate generated_12D630 recipe, remain in normal-build.log;
this is not a warning-free build.

All **eleven final tests pass in 74.110s**, including the focused suite and
complete installed-image/input controls. Preserve all **104** other captured
inputs, every unrelated symbol's address/body/extent and protected **189,088
bytes / 720 owners**, with zero excluded sections. Controls reject changes to
all **107** live inputs and selected target/caller/data/metadata bytes. The
three-input successor accepts only the exact measured source/ELF/guards and
checks both fixture stages. Prior unchanged broad suites are reused, not
represented as fresh tests.

Fresh official matching numbers:

| Section | Converted | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,501 / 6,044 (91.02%) | 3,603 / 5,501 (65.50%) | 0 | 1,898 |
| Init | 492 / 539 (91.28%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,828 / 5,323 (90.70%) | 2,930 / 4,828 (60.69%) | 0 | 1,898 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

Conversion counts/bytes stay fixed: the semantic predecessor already counted
as C. Update only two aggregate README match rows; keep this narrative in the
working documentation and check off the completed instruction-match item.

Tools commit **52a9ed6** banks six focused files before the consumer pin.
Windows AST checks pass for all 12 files across both copies; all six new mirror
files are byte-identical. Eleven shared padder tests pass in each checkout
(0.050s consumer, 0.060s mirror), and make tools-check passes. Preserve older
mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **871** initial
dirty-file hashes and **877** final dirty paths, without committing/resetting it.

Zero Claude calls. No push, account/auth retry, host-port edit/build/launch
or frozen Release action.

## Resume Boundary

Next **func_15019F20**, VA 0x15019F20..0x1501A220, ROM 0x473D0..0x476D0,
frame **0x18**. Its original slot contains **191 body words plus one trailing
NOP**. Fresh assembly inspection identifies a timing/state updater rather
than a display-list provider: counter/divisor arithmetic, float scale updates
and a final func_150A019C call. The frame driver's direct call ignores its
return and passes no arguments; verify other callers before changing the
placeholder interface. It remains a 12-byte C stub, not part of this match.

Keep adjacent func_15094AB8, rectangle's 18-word fit and the wider Game/
additional-source queue open. No complete gameplay or host-port equivalence.
