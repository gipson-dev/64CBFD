# Game Effect-Record Constructor Match

Date: 2026-10-09

## Result

Continue [Note 1149](1149-game-table-driven-effect-constructor-restoration-20261009.md)
under the [focused workflow](../AGENT_WORKFLOW.md), one Codex writer and zero
Claude calls. Restore false-zero `func_15147DA0` in
[generated_175250.c](../../conker/src/game/generated_175250.c):
VA 0x15147DA0..0x15147EB8, ROM 0x175250..0x175368,
**70 words / 280 bytes / frame 0x40**, directly byte-exact from complete
semantic C with **zero target guards**. Correct only its local prototype in
[game_2062D0.c](../../conker/src/game_2062D0.c); every instruction in that
62-function owner remains unchanged. The caller `func_151DA6F8` remains
**144 words / frame 0xD0 / 61 actual differences**.

Start from clean parent e8118f25 and mounted tools 77001d3. The baseline ELF
is the exact Note 1149 artifact, SHA-256
`a0ed058388ea573771373ec23cb71ea656e2b4d5a889b96682a7921911f56093`.
The new full-ELF audit permits only the callee's 280-byte slot and its own
symbol-size field **12 -> 280** to change. All 6,058 slot addresses/extents,
every other function body and every other ELF byte remain unchanged, including
all protected data. Conversion CSV bytes and all **11,475 guards** are
unchanged. New ELF SHA-256:
`479ab6cadef42c95c2b96c3de72d6d33dd6a01d7b7159613cbb5c8fc320fc0be`.

The placeholder already counted as C: no converted-function or converted-byte
credit. Fresh matching totals advance exactly one: **5,484 converted / 3,398
exact (61.96%)**, Game **4,811 / 2,725 (56.64%)**; Init 492 / 492 and
Debugger 181 / 181 exact, zero address drift and **2,086 different**.
Root README changes only its two aggregate matching rows, with no function
narrative. The wider Game goal stays active.

## Recovered Contract

The complete mixed O32 interface has fifteen arguments: request pointer,
descriptor pointer, payload-byte count, six full-word low-byte output values,
two full-word fade values, render pointer, extra bytes, byte channel and
full-word context. In particular **active through fadeAlpha are incoming
32-bit words**, not byte parameters. Only channel is declared as an incoming
byte. Six output fields narrow at their byte stores; fade values are forwarded
as complete words to the allocation core. Other existing owner prototypes
are outside this scoped correction.

Write request+0x10 = 1 before calling `func_15147A80` with all eleven
arguments: request, payloadBytes+0x48, 0x14, 1, 0, 1, full fadeFlag,
full fadeAlpha, extraBytes, byte channel and full context. Recover the size
addition as unsigned 32-bit arithmetic, retaining retail wrap without C
signed-overflow UB. Target conversion back to the signed callee word preserves
the bit pattern; this is not a portable acceptance claim for invalid sizes.

A null allocation returns immediately without reading the descriptor, render
record or created payload pointer. On success capture `*(created+0x98)`,
copy all 32 live descriptor bytes, store the six low bytes at +0x20..+0x25,
then copy **eight live render words** to +0x28..+0x47 inline. Keep the captured
payload pointer across memcpy and preserve the original created pointer for
return, ignoring memcpy's destination return. Descriptor/render reads occur
after allocation; render reads occur after memcpy. There is no invented
zero-fill, extra tail or null guard for success-path inputs.

The eight-word render aggregate describes the actual 32-byte copied extent,
not original declaration names or gameplay meaning. Word alignment and the
prepared target implementations are explicit boundaries. Allocation remains
bounded in qualification: the separate 115-word `func_15147A80` is still
a false-zero placeholder, not restored by this wrapper.

## Complete Source Fitting

The [callee driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_effect_record_constructor_candidates.py)
screens nine complete ordinary forms and four compiler profiles. The selected
straightforward body matches all 70 retail words directly with the existing
IDO 5.3 `-O2 -g3` profile, no isolated diagnostics or pools. Profile results
are O2g3 **70/0 differences**, O2 **70/2**, O1g3 **82/79**, O1 **82/80**,
all frame0x40. Its only relocations are J26 at +0x5C to func_15147A80 and
+0x84 to memcpy. No compiler-profile, padder, assembly, layout or patch CSV
change is needed.

Before recovering the callee, the [caller fitting driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_trail_effect_constructor_matching.py)
screened **73 additional complete source forms**: descriptor-kind placement,
payload field permutations, meaningful control/render grouping, one-element
record arrays, copy-pointer lifetimes, register qualifiers and volatile
records. Ordinary field ordering reaches 59 differences; the combined early
kind/volatile-payload experiment reaches 57. Neither resolves render prefix
SP+0x64 versus retail SP+0x54. A volatile qualifier is not evidence of the
original declaration. **None is installed**; no artificial 16-byte render
tail, scalar filler, guard or retail-word replacement is added. The banked
constructor stays at 61 differences. Do not assign progress credit to an
uninstalled experimental stream or compare unspecified padding values.

## Qualification

The [nine-test suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_effect_record_constructor_match.py)
reuses existing instruction oracles, native32 harness, compiler/owner and
ELF/object/pool parsers and the actual generated-slice padder. Independent
packed-memory/call expectations provide semantic checks, not only pairwise
agreement between streams.

- **1,816 cases / 3,632 executions** compare complete selected/retail words,
  full high-bit arguments, all six low-byte outputs, allocation failure,
  live descriptor/render/payload-pointer mutations, helper clobbers and both
  SP phases. All 70 words execute; complete GP/FP, memory and event states
  agree, including saved-register lifetime and original-pointer return.
- **584 real missing-public-byte pairs** compare emitted fault prefixes.
  **12 safe aliases** cover descriptor=request, render=descriptor and exact
  render self-assignment. Lazy null cases omit all success-only input bytes.
  Do not claim portable invalid-C behavior, hardware traps or overlapping
  descriptor memcpy qualification.
- Fourteen complete compiled forms first execute to completion over twelve
  samples each. **Six effective negatives** alter state, allocation size,
  fade width, descriptor size or return pointer; the narrowed ordinary form
  is also semantically wrong for full fade words. Execution failure alone
  cannot qualify a negative.
- Preserve all **10 callee-owner neighbors** and **62 caller-owner functions**,
  pools and relative relocations. Diagnostics stay **0 / 6** respectively.
  Actual generated-slice padding emits 280 bytes without `.space`, with the
  exact two relocations. **Four independent GNU links / 128 cases** cover
  J26 regions and full behavior; retail-symbol owner output equals the
  isolated exact stream. There are no target HI/LO relocations to claim.
- **65,536 actual native32 C cases** vary full high words with all low16
  patterns, six byte outputs, fade/context transport, unsigned size wrap,
  live mutations, allocation failure, captured payload pointer and original
  return. Check **two 512-byte canary regions**. Helpers are bounded fixtures,
  not actual allocation-core or gameplay acceptance.
- **128 connected cases / 256 executions** run the unchanged banked
  144-word caller, selected/original 70-word callee and actual linked
  11-word memcpy. All **225 words** execute and full states agree. This does
  not make the caller retail-exact or qualify the allocation core/hardware.
- Source-byte-validated cached streams qualify all **73 caller forms** over
  **32 cases each / 2,336 executions**, comparing defined record fields,
  helper arguments and preserved return. These forms remain uninstalled;
  their private frames/unspecified padding, native and fault behavior are
  not claimed identical or fully qualified.

Final pre-install run: **nine tests pass in 34.610s**. Final post-install run:
**nine pass in 39.334s**, no skips. Fresh **25 shared padder/linker tests pass
in 0.302s**, and both mounted/older-standalone tool checks pass. Preserve the
duplicate generated_12D630 recipe warning and six existing caller-owner
diagnostics; the production build is not warning-free. Prior historical
whole-ELF tests are not blanket reruns against a changed baseline.

Nineteen mounted/mirrored tool files parse and match exactly. Scoped relative
link validation checks **136 documents / 4,169 links / zero broken** before
the parent commit.

## Receipts And Banking

Ignored `conker/build/game-effect-record-constructor-test/` receipts include
baseline.json, before.elf, before manifests/progress, slot.json, guest.json,
faults.json, forms.json, owner.json, linked.json, native.json, caller.json,
caller-fitting.json and after.json. Source/object screens stay in the separate
ignored constructor directories. For a fresh screen, run the caller fitting
driver before test09; that test validates exact generated source bytes before
using its complete cached streams. Preserve the captured baseline rather than
recapture the installed ELF as an old placeholder baseline. Commit no ROMs,
binaries, generated temporary sources, progress CSV or private state.

Per "Keep commited", mounted tools
**658b6154fa7cd9534cf093b6925c2dd10de02d4b** is committed first; parent
source/docs/gitlink then pin exactly that commit. Mirror only the three absent
new files and verify exact bytes. Preserve older standalone HEAD ddbdd16,
its independent owner-pool/effect-test fingerprints, unrelated untracked
paths and history. No push, pause, reset or duplicate standalone commit.

Manual Graphify refresh refuses 16,930 nodes over retained 38,719, keeping
19,398 nodes from 2,972 excluded files still on disk. Do not force overwrite
or change dependencies/accounts. No OGL/Release, runtime/save/editor or bridge
work. Graph repair and hardware/gameplay remain open.

## Next Work

Recover complete **func_15147A80**, VA 0x15147A80..0x15147C4C,
**115 words / 460 bytes**, in generated_174BF0.c, preserving this exact
wrapper and its full eleven-word allocation interface. Alternatively continue
the unchanged caller's 61 actual layout/register/scheduling differences from
its complete semantic body and the new fitting evidence, not removed zero
placeholders. Resolve the 32-byte prefix placement without inventing a tail;
keep complete upstream callers and hardware/gameplay as separate gates.
