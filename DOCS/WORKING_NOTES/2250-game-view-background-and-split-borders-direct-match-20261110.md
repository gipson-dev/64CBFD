# Selected-view background and split-screen borders matched directly

Date: 2026-11-10. `func_151103C8` replaces its zero-return placeholder with
the complete graphics callback: **95 words / 380 bytes**, original **0x28
frame**, **zero guards**. All words emit directly from semantic C using the
existing SDK graphics macros and O2/g3 owner profile.

Fresh production-ELF recount: **4,319 / 5,513 (78.34%)** total; Game
**3,646 / 4,840 (75.33%)**; Init **492/492**, Debugger **181/181**.
Zero address drift; **1,194** different. **92 more** accepted matches reach
4,411/5,513 and the active 80% goal. Conversion CSV and converted-byte counts
remain fixed. The root README receives aggregate row changes only.

Baseline consumer `1610a363d49a447ba66d6bb6276c8fb693c268fc`, tools
`07f41c42e2e6b526d233bc339d6b93c73c1eb9af`, from
[Note 2249](2249-game-angular-spring-update-byte-match-20261110.md).
Bank the eight proof files first in tools commit `0d055a93c5fffffc92062d5b87586c77b0ba8ab5`. Local commits only.

## Complete behavior and interface

Owner `conker/src/game/generated_13D350.c`; complete original remains in
`conker/asm/13D350.s`. Retail VA **0x151103C8..0x15110544**, ROM
**0x13D878..0x13D9F4**. The old 12-byte stub differed in 94 retail-slot words.

The source exports a display-list cursor callback:

```c
Gfx *func_151103C8(Gfx *commands, f32 unusedX, f32 unusedY, f32 unusedZ);
```

The original dispatch at **0x1511027C** selects slot 0 of **D_800891D8**,
passes the cursor in A0 and float bits from F12/F14/F18 through A1/A2/A3,
then copies returned V0 into A0. It also supplies four stack words which this
routine does not read. Preserve those words and the three unused incoming
float homes. The original total formal-parameter count is unproven; this
semantic interface does not infer it from untouched extra caller arguments.

The callback fills the selected view through `func_15110544`, using unsigned
RGB bytes at D_800DBEA8. Rectangle inputs are truncated view left/top/bottom
and the truncated rounded float expression `right - 1.0f`. It returns that
helper's cursor unless live split mode D_80082FA0 is nonzero and live selected
view D_80082FA4 is zero.

On the split path, append pipe sync, restore full-frame scissor through
`func_1501A490(commands, 0xFF, 0, 0, 0, 0)`, set fill color **0x00010001**,
and submit a horizontal divider from `(0, (height >> 1)-6)` to
`(width, (height >> 1)+6)`. Re-read split mode after that helper; when it is
not one, submit a vertical divider from `((width >> 1)-1, 0)` to
`((width >> 1)+1, height)`. Propagate every returned cursor.

All global gates and dimensions retain retail load timing. Effectful helper
models change mode/index after the initial fill, dimensions after scissor,
and mode/dimensions after the horizontal divider. Independent return arenas
ensure no caller cursor is silently reused. These model boundaries do not
claim that the real graphics helpers have those mutations.

Signed dimensions use the prepared SDK32 arithmetic-right-shift semantics,
including negative odd values. Replacing that shift with logical shift is an
effective negative control. Native tests use the qualified two's-complement
ABI; sparse full-word indices and physical aliases are guest-only evidence.

The existing local `Record13D350` gains typed top/bottom/left/right fields at
**0x24/0x28/0x2C/0x30**. Its stride remains **0x180**, and the existing matrix
remains at **0xBC**. Native static assertions check all offsets and sizes.
This matches the independently recovered view layout in `game_476D0.c`.
No shared header changes or new shared layout assumptions are introduced.

The scissor helper retains its actual `s32` cursor-return ABI and signed16
view argument; the local call explicitly converts its result back to Gfx*.
The fill helper's three color parameters are unsigned bytes. Existing helper
definitions and all neighboring instructions remain unchanged.

## Direct compiler recovery and exact image

The first complete source emitted the correct 95 words/frame0x28 with 16
register-allocation differences. A bounded eight-form pointer screen found
two direct matches. Select the explicit SDK32 byte-address calculation:

```c
(Record13D350 *)((u32)D_800BE628 + (u32)D_80082FA4 * 0x180)
```

Unsigned address arithmetic preserves retail wrapping multiplication/addition
and recovers the opening register roles without hints or binary guards.
Native proof uses valid indices into its four allocated records; arbitrary
guest address wrapping does not imply portable out-of-bounds C behavior.

Raw target SHA256:
`6408ce807109ec1d9943d8fb3ecf3938ddd6efbbabfa758d0215bbc090897ef9`.
All **24 relocation bindings** remain explicit. No inserted/omitted words,
new guards, opaque target assembly, profile edits or data-pool change.

Freeze **2,258 input fingerprints** with retained mutable pre-adoption inputs.
Five actual Make commands include asm-processor preprocessing/postprocessing,
IDO compilation, generated padding and assembly. Independent whole-owner
compilation agrees. All **33 other functions**, including the two remaining
GLOBAL_ASM routines, retain code and bindings; pools and zero diagnostics
remain fixed. The owner FP register mask gains one bit;
independent and actual-Make masks agree. No unexplained linked section changes.

The strict whole-ELF prediction accounts for exactly **309 changed bytes**:
target body and symbol extent **12 -> 380** only. No metadata permutations;
**zero exclusions**. All **6,050 function addresses** stay fixed. All
**189,088 protected bytes / 720 data owners** remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Makefile, profiles, shared headers, layout, guard history and conversion CSV
remain byte-for-byte unchanged.

## Fresh qualification and limits

- **474 guest cases / 948 executions**, all 95 words visited, exact complete
  registers/memory/access traces, helper mutation/cursor paths, signed
  dimension extremes, all meaningful gates and unused float homes.
- **28 invalid-conversion prefixes** stop before an unqualified TRUNC result.
  Retail converts left, top, bottom, then right-minus-one; preserve that
  emitted order. Prefix equality does not prove FCSR, traps or an invalid
  portable C cast. Native tests consume only defined finite conversion cases.
- **434 native SDK32 cases** at `-O0`, `-O2`, `-O3`, each matching **1,993,432
  public/call bytes**, with strict aliasing and UBSan. Real SDK Gfx macros,
  typed 0x180-byte records and separately returned cursor offsets are used.
- **15 effective compiled controls**, each with a normally completed witness
  and zero earlier execution errors. The private division-form diagnostic was
  not counted; the qualified logical-shift control distinguishes the negative
  dimension behavior using supported emitted instructions.
- Both padders, **119 word/binding corruption checks**, **16 GNU linker
  comparisons** across four independent low-half symbol sets, **64 rebased
  executions**, and **154 literal instruction-access-cut pairs**.
- **216 real callback pairs** cover the complete 17-word dispatch window,
  authentic MFC1 argument transfers, untouched extra stack arguments and
  returned cursor publication. The larger parent remains a placeholder.
- **72 pairs** execute the actual fill, scissor, color-image and rectangle
  helper bodies: all **228 provider words** are checked against current ELF,
  **160 provider words** are visited. An independent complete packet model
  checks every resulting command and cursor. Scissor coverage is the actual
  view-0xFF full-frame path; its other paths are not newly claimed.
- Eight complete-image corruption probes and closed live-input, data, guard
  and address audits complete the focused suite.

Eight fresh pre-install methods pass in each tools environment. After source
installation, two methods run fresh and six semantic checks are reused only
with exact tool/dependency fingerprints. Shared tool smoke is fresh; three
prior unchanged helper regressions per environment are explicitly reused.
The sibling tools checkout's **2,434 existing dirty paths** are preserved.
Its target wrappers run from a private overlay with recorded read-only
fallbacks; actual Make uses the mounted CLI. This is not a clean-clone claim.

Production Make agrees with independent ELF/binary prediction and fresh
progress succeeds. Existing whole-ROM checksum exit2 and duplicate
generated_12D630 warnings remain expected. ELF SHA256:
`ef51ce6aa449da99e521462e0a00b37ac2a39c2ebf67ef2a53fa5c3fafd2f3bd`. Binary SHA256:
`f632af06ec4dabf81c5ccfec9f3546f63a9543d9517707ebb543a0e764432e4c`.

Codex is the sole writer; zero Claude calls. No push, installation, account
change, host-port edit, save mutation or Release build. Invalid conversion
results, full rendering-parent behavior, FCSR, hardware and gameplay remain
outside this proof.

## Graph and continuation

Scoped Graphify refresh retains or relocates all 59711 old
nodes, producing 59711 nodes / 113097 links.
Definitions outside the declared scope remain fixed apart from community
metadata. All 32 C function positions and both retained assembly references
are checked. Historical excluded nodes are retained; this is not full-corpus
re-extraction. Post-commit receipts separately check heading moves and actual
graph-worker completion.

```sh
python3 -m unittest tools.tests.test_game_view_split_borders_151103c8_match -v
make -C conker match-progress NON_MATCHING=1
```

Reproduction requires the prepared PSBBN consumer and retained mutable
baseline under `conker/build/game-next-151103C8-match/frozen/`. No private
ROM/ELF binary is committed.

Next: **`func_151B4CD0`**, 95 retail words/frame
0x58, in `conker/src/game/generated_1E2180.c`. Its 12-byte
stub differs at 94 retail-slot words. It is unchanged
and uncredited. Inspect the complete original and actual caller/helper ABI
before reconstruction. Keep the 80% goal active.
