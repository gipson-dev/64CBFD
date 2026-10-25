# Preset Payload Dispatch Direct C Match

Date: 2026-10-25

`func_1518F51C` now replaces its zero-return placeholder with complete semantic
C. All **45 words / 180 bytes**, frame **56**, two call bindings and the table
HI/LO pair emit directly from C, **without guards or an alignment tail**.
Only this function receives new matching credit.

## Source And ABI

Owner `generated_1BA1D0`, source `conker/src/game/generated_1BA1D0.c`, original
assembly `conker/asm/1BA1D0.s`. VA `0x1518F51C..0x1518F5D0`, VROM
`0x1BC9CC..0x1BCA80`. Bindings: classifier `func_1518FDC4` at +40,
`D_8008D630` HI/LO at +72/+88, factory `func_1518F5D0` at +156.

The ten arguments are object pointer, unsigned variant byte, signed halfword
mode, three signed bytes, unsigned value byte, signed word extraBytes,
unsigned channel byte, and signed word context. Reject a null object or zero
classifier result. Otherwise select one of nineteen preset pointers, add the
late variant times the **80-byte** preset stride, and forward the arguments to
the factory. Preserve the original argument-home reloads and full pointer return.

An unwritten local word above the classifier's output byte keeps that byte at
SP+`0x33`, rather than the initial screen's SP+`0x37`. The frame and complete
instruction stream then match. No inline assembly, physical-register binding,
profile change or instruction normalization is needed.

The downstream `func_151D2F00` signature confirms scalar extraBytes/context.
The factory adds `0x60` to extraBytes, the next constructor adds `0x30`, and
`func_15167A68` passes that byte count to the allocator. The smaller caller
requests twelve extra bytes, then copies twelve bytes to result+`0x90`.
Earlier private pointer interpretations of those two inputs are rejected.

The retained factory's return declaration becomes `void *`/NULL, while its
three-word stub remains identical. Its parameters and the classifier retain
their existing non-prototype declarations: defined formals add argument-home
stores to these unresolved stubs under g3, changing 12 bytes to 28/24.
Typed function-pointer casts instead emit 49 words with 41 differences and
indirect calls; that experiment is also rejected. The recovered wrapper's
default-promoted calls are qualified against the actual byte/word ABI.
Neither provider body is restored or credited by this interface correction.
No shared header changes.

The aligned complete prepared-ROM scan finds one JAL to each provider, both
inside this wrapper, and no aligned provider literals. Source search finds
only their two existing definitions. Arbitrary computed calls are not excluded.

## Original Classifier And Callers

The classifier's complete **158-word** retail image is independently assembled
and locked. Both real jump tables are loaded from the frozen original data.
All 256 object-type bytes and unsigned variant boundaries are exercised.
Supported types select presets 0..18; acceptance requires variant zero.
Supported-type rejection still writes the private output byte. The production
C classifier remains a zero-return placeholder and gets no recovery credit.

Five aligned wrapper calls occur across four original callers:

- `func_1502460C`, 2,032 words, call VA `15025564` / VROM `52A14`.
- `func_150265CC`, 3,451 words, call VA `15027FE8` / VROM `55498`.
- `func_1509D180`, 384 words, call VA `1509D4AC` / VROM `CA95C`.
- `func_15194FF4`, 123 words, calls VA `15195160`/`151951C8`, VROM `1C2610`/`1C2678`.

All four complete original images are independently assembled and locked to
retail. Sixty phases execute the final four setup instructions, actual JAL and
delay slot, recovered wrapper/actual classifier, and return boundary, stopping
before the caller continuation at call+8. All ten incoming and factory ABI slots
are observed. These bounded windows do not qualify full caller entry/return,
restore their C bodies, or establish full factory/heap/gameplay behavior.

## Focused Qualification

Both tools copies pass **six fresh checks**, zero failures/errors/skips/reuses:
primary **19.492 seconds**, older mirror **12.831 seconds**. Shared project-tool
checks pass in 0.500/0.305 seconds.

- **4,270 guest phases** cover type/variant axes, signed-width edges, opaque
  result gates, null/high-word factory returns, helper changes to late argument
  homes and table entries, and both stack phases. All **45 root words** and
  **158 actual classifier words** execute. Original/selected complete modeled
  GPR/FPR/HI/LO/RAM/event/call states agree.
- Native32 O0/O2/O3 each pass **97,280 cases**, including null object, rejected
  classifier, allocation success and allocation failure. Actual SDK types,
  signed byte/halfword edges, full extraBytes/context words and all nineteen
  preset rows are checked. Six effective stride/width/return/gate negatives
  exit 23. Trap UBSan is enabled. Native harnesses alone use `-mstackrealign`.
- Opaque Native fixtures allocate valid extended preset arrays for variant
  stress; this is not a claim that the real classifier accepts nonzero variants.
  Deliberate guest home overwrites are not portable Native C alias guarantees.
- **Nine independent GNU links / eighteen rebased phases** cover all four
  bindings and HI/LO carries. **132 fired target-access fault prefixes** agree
  in complete modeled state, dispatched word, PC and branch-delay context.
- All 45 raw-word corruptions, four binding corruptions, five strict-image
  mutations and six frozen-input controls reject. Guest instruction-order
  evidence is separate from hardware, MMU, FCSR or portable fault semantics.

All **60 raw and padded neighbors** and pools remain fixed, including both
unresolved provider stubs and the previous initializer recovery. The existing
ordinary three-command O2/g3 Make recipe reproduces the qualified owner.
Four inherited Warning 712 diagnostics and the duplicate generated_12D630
recipe warning remain unchanged; this is not a warning-free build.

## Exact Image And Production

The first body/size-only prediction rejects fourteen additional bytes. The
independent link exchanges adjacent `D_8009E6DC` and `D_800991CC` symbol/string
records. The bounded existing serializer checks their exact values, sections,
bindings and order; a named-definition multiset verifies preservation.
The complete prediction changes **150 bytes**: **135 code**, one target-size
byte, and fourteen bytes in that closed swap. **No metadata is excluded**.

Tools commit `8ad2cea49aaa283e232f3f3ddf5aa975da370405` precedes the consumer
pin/source/docs. Actual production Make exits zero and reproduces the entire
independent image. All **6,055 function addresses** and the other **6,054 bodies**
remain fixed. All **720 protected Game-data owners / 189,088 bytes** stay exact,
SHA-256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Each copy passes two fresh installed owner/image checks. Four unchanged
semantic checks are explicitly reused only after complete input/module and
qualified-artifact identities agree; those four are not fresh tests. Native
adoption verifies all **16,066 sealed files** before/after copying. Exactly the
target owner source, owner object and linked ELF differ from the sealed baseline.
The guard CSV and all other inputs remain byte-identical.

The recount streams the actual adopted Native ELF to the verified cache.
Total **3,801 / 5,505 (69.05%)**; Game **3,128 / 4,832 (64.74%)**;
Init **492 / 492**; Debugger **181 / 181**. Zero address drift, **1,704** still
different. The 75% threshold remains 4,129, **328 more matches**.
Only this wrapper leaves the prior queue. The factory remains explicitly
classified as an unresolved pointer/NULL placeholder. Adopted ELF SHA-256:
`5ef98eaf08feb4a0553161a5fcde17ad5f05cca08055c99c92e50d73d73a83e3`.

## Corrections And Handoff

The first generated runner has a quoting error and stops before cache writes
or compilation. The next attempt identifies the closed serialization swap.
The first semantic run identifies missing signed-byte-load support in the
reused low-word oracle; a local LB implementation fixes the fixture. The next
coverage accumulator omits null-path visits, despite the cases executing.
Its correction retains the all-45-word requirement and adds allocation-failure
and high-word-return cases. Final complete suites above are rerun fresh in both
copies. Failed producer logs/receipts remain separate from accepted results.
These fixes do not change the recovered C body.

Baseline consumer `a6a0261b34f4a3d718cab00afb1cf293694c1eee`, tools
`6a4959782f8e077d9124bc3c603791a312bd0194`. The older standalone tools mirror's
1,660 prior dirty paths, contents/statuses and HEAD remain preserved, plus two
owned modules; no mirror commit/reset/stash. Receipts live in ignored
`conker/build/game-preset-payload-dispatch-match/`.

Next ordinary placeholder: `func_151D3D50`, owner `generated_200930`, 45-word
retail slot, uncredited until its own full qualification/adoption. Keep existing
C `func_15014094` and parser-missed `Gfx *func_1510D8C0` separate.

Refresh exactly the eight changed C/Markdown files through the supported
Graphify incremental merge API, retaining historical outside-scope nodes/rows
without a full-corpus freshness claim. Audit every prior node or unique
relocation and current file fingerprint before adoption. Index new tools
separately. Skip the automatic hook only for this owned refresh.
Claude calls zero; no host/editor/Release, dependency or global configuration
changes. Nothing is pushed. The wider 75% goal remains active.
