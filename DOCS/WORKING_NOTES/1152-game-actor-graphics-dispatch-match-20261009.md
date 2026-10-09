# Game Actor Graphics Dispatch Match

Date: 2026-10-09

## Result

Continue [Note 1151](1151-game-effect-allocation-core-match-20261009.md)
under the [focused workflow](../AGENT_WORKFLOW.md), one Codex writer and
zero Claude calls. Restore false-zero `func_15147C4C` in
[generated_174BF0.c](../../conker/src/game/generated_174BF0.c):
VA **0x15147C4C..0x15147D1C**, ROM **0x1750FC..0x1751CC**,
**52 words / 208 bytes / frame 0x38**, directly byte-exact from complete
semantic C with **zero target guards**. Preserve the original assembly,
compiler profile, manifests, layout and padder.

Start from clean parent **65542b01** and mounted tools **2807f51**. The
baseline is the exact Note 1151 ELF, SHA-256
`67d19ec4a6bc4d4aec25153efaf0fe09971064147defa5ee984c791e3f7d8404`.
The full-ELF audit permits only the target's 208-byte code slot and its
symbol-size field **12 -> 208** to change. All **6,058** function-slot
addresses/extents, every other body and every other ELF byte remain unchanged,
including the complete protected Game-data image. Conversion CSV bytes and
all **11,475 guards** are unchanged. New ELF SHA-256:
`7eb984ef2d80b7ffce34bc2eb3d93bddd5357e4fb14c55f732405803931afbf2`.

The placeholder already counted as C; no converted-function or converted-byte
credit. Fresh matching totals advance exactly one: **5,484 converted / 3,400
exact (62.00%)**, Game **4,811 / 2,727 (56.68%)**, Init 492 / 492 and
Debugger 181 / 181 exact. Zero address drift and **2,084 different**.
The trail constructor `func_151DA6F8` remains **144 words / 61 differences**;
the wider Game goal remains open. Root README receives aggregate rows only.

## Recovered Contract

Recover a pointer-returning three-argument O32 interface: graphics-command
address, actor address and **signed halfword index**. Local byte-pointer
declarations express address transport/field access, not original type names.
Inspect the existing graphics helper's complete declaration/body in
[game_16EE20.c](../../conker/src/game_16EE20.c); its index is likewise s16.

- Read actor+0x1E as u16. Only when bit **0x20** is set, read the full
  optional word at actor+0x28; otherwise forward zero without reading it.
- Call `func_151462C8` with all nine words: original commands, actor+0x34,
  0, 0, 0, sign-extended index, actor+0x54, **2**, optional word.
- Save its returned command address. Read actor+0x31 as an **unsigned byte
  after the call**, not before: the helper may change the live selector.
- For selectors **0x13..0xFF**, call `func_1516972C(actor)` and return the
  saved graphics result, ignoring any V0 residue from cleanup.
- For selector zero, return the graphics result without a callback-table read.
- For selectors **1..0x12**, read the live entry in **D_8008A2A4**, invoke
  it with actor, graphics result and sign-extended index, and return the
  **callback's result**, not the saved graphics result. Retail has no null
  check for this callback and no null-result early exit for the graphics helper.

The protected retail table has 19 entries: slot zero is null and all 18
dispatch slots are nonnull function addresses. The target itself has two
aligned Game-data pointer witnesses at **0x8008BB98 / 0x8008C454** and no
direct J26 references in the inspected retail assembly. These are static
identity/ABI routing evidence, not fresh execution of upstream dispatchers.

## Complete Source Fitting

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_actor_graphics_dispatch_candidates.py)
compiles six complete ordinary forms. The first semantic body is already
**52/0x38/0 differences** under existing IDO 5.3 O2g3. Nested-else is
also exact. Signed-selector and word-selector forms have three and two
differences respectively; word-index emits 53 words/frame0x48/35 differences.
Unsigned public index is an ordinary experiment, not an effective semantic
negative: both callee declarations narrow it back to s16.

Four profile results: O2g3 **52/0**, O2 **52/20**, O1g3 and O1 **57/55**,
all selected-profile frames 0x38. No isolated compiler diagnostics or pools.
Relocations are J26 calls at +0x60 / +0x7C and the callback table's HI/LO
pair at +0x98 / +0xA0. No scheduling guard, fixed return, truncated prefix,
fake padding or profile change is needed.

## Qualification

The [eight-test suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_actor_graphics_dispatch_match.py)
reuses the existing MIPS instruction oracle, native32 harness, compiler,
ELF/object/pool parsers and actual generated-slice padder. A local signed-byte
load adapter supports the complete signed-selector experiment; no shared
oracle or historical test is changed. Independent full helper arguments,
return choices and public-memory expectations supplement stream comparison.

- **5,002 guest cases / 10,004 executions**: all 256 selector bytes, signed
  halfword boundaries/high words, optional flag/word cases, zero/nonzero helper
  and callback returns, selector/table mutations and nine outgoing argument
  homes overwritten by the helper. All **52 retail words** execute; complete
  GP/FP, saved-register/stack, event and memory states agree at SP phases 0/8.
- **196 missing-public-byte pairs** qualify emitted fault prefixes. Minimal
  fixtures omit optional bytes when the flag is clear and all table bytes on
  zero/cleanup selectors. This proves emitted access order with bounded
  helper inputs, not portable C fault behavior or hardware traps.
- **12 complete compiled forms / eight samples each** include six effective
  semantic negatives: wrong optional flag, zero forwarded index, threshold
  18 instead of 19, discarded callback return, wrong graphics flag and stale
  pre-helper selector. Each stream first completes; fixture crashes cannot
  count as a negative. The unsigned-index experiment was rejected as a
  negative because independent call arguments remained correct.
- Preserve **10 owner neighbors**, all their instruction bytes, relative
  relocations and pools. The same **seven diagnostics** remain. Actual
  generated-slice padding emits all **208 bytes**, without `.space` or target
  guards. **Four independent GNU links / 240 cases** qualify HI/LO carry,
  independently moved table addresses and different J26 regions.
- **655,616 actual native32 C cases** cover all 65,536 signed-halfword bit
  patterns, all 256 selector bytes, optional/full-word values, live helper
  mutations, distinct callback return and **256-byte actor/canary comparisons**.
  Native pointers use valid bounded arrays. Graphics/cleanup/callback helpers
  are fixtures, not their actual implementations or gameplay acceptance.
- **1,344 cases / 2,688 executions** use all protected retail callback-table
  identities, zero/cleanup selectors, signed boundaries and both SP phases.
  Each nonnull table entry resolves to a function in the linked ELF. These
  execute the complete dispatcher with bounded callback hooks, **not** actual
  callback bodies or upstream dispatchers. Both incoming pointer witnesses
  and the whole protected data image remain exact.

Final pre-install **eight tests pass in 24.832s**. Final post-install
**eight tests pass in 27.622s**, no skips. Fresh **25 shared tooling tests
pass in 0.315s**, and both local tools checks pass. Preserve the existing
duplicate generated_12D630 recipe warning and seven owner diagnostics.
Do not present the earlier allocation-core/trail suites as fresh reruns:
their unchanged instruction/data/relocation evidence is retained by the
copied-owner and full-ELF audits. Historical baseline-sensitive suites are
not rewritten to accommodate this new checkpoint.

Twenty-three mounted/mirrored tool files parse and match exactly. Scoped
documentation validation checks **138 documents / 4,190 relative links /
zero broken** before the parent commit.

## Receipts And Banking

Ignored `conker/build/game-actor-graphics-dispatch-test/` receipts include
baseline.json, before.elf, before guards/progress, slot.json, guest.json,
faults.json, forms.json, owner.json, native.json, table.json, linked.json
and after.json. Separate complete-form screens live in
game-actor-graphics-dispatch/. Preserve the baseline; commit no private ROM,
ELF/object/native binary, temporary generated source, progress CSV or save.

Per "Keep commited", mounted tools
**7b8870292a591bd543b5152c112823e055d3f5a1** is committed first; parent
source/docs/gitlink pins that exact commit. Mirror only the two absent new
files, checking parse and exact bytes. Preserve older standalone HEAD ddbdd16,
independent owner-pool/effect-test fingerprints, existing untracked files and
history. No push, pause, reset or duplicate standalone commit.

Manual Graphify refresh refuses **16,951 nodes** over retained **38,739**,
preserving **19,398 nodes from 2,972 excluded files still on disk**. Do not
force overwrite or change dependencies/accounts. Parent post-commit rebuild
is checked separately. No OGL/Release, runtime/save/editor or bridge work.
Graph corpus repair and actual graphics/cleanup/callback/hardware/gameplay
remain open. One writer/zero Claude calls suffices because complete assembly,
compiler and independent tests settle this target's return/ABI decisions.

## Next Work

Recover false-zero **func_15147740**, VA **0x15147740..0x151478D0**,
ROM **0x174BF0..0x174D80**, **100 words / 400 bytes / frame0x20**, in this
same owner. Its full retail routine subtracts a live global from a signed
halfword timer, narrows/reloads it, validates two unsigned selectors and one
signed selector, invokes three callback tables, reloads actor fields after
calls and conditionally cleans up. Preserve its void/unspecified-V0 boundary;
do not invent a status return from helper residue. Alternatively continue
the trail constructor's **61 actual differences**. Keep the already exact
allocation core, wrapper and graphics dispatcher intact and the wider goal open.
