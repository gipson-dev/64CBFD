# Record Payload Constructor Direct Match - 2026-10-14

## Result

Continue [Note1366](1366-codec-frame-dispatch-guarded-match-20261014.md)
from consumerfafb9e34/tools a337e52. Convert func_1513C350 at
VA0x1513C350 / ROM0x169800 from GLOBAL_ASM plus its commented draft to
complete semantic C. All103 words (412 bytes) emit directly under the
existing O2/g3 profile, frame0x38. No new guards, padding words, compiler
selection, shared header or public ABI change is required.

The routine selects category0x4A/0x1B from the descriptor flag, allocates a
record, copies its40-byte descriptor, initializes the view/attributes,
clears four resource slots, allocates optional resources with a live global
limit, and copies an optional three-word payload. Preserve the address-keyed
public name and struct210-return prototype; use descriptive locals/parameters.

The complete rebuilt ELF is byte-for-byte identical to the baseline because
the original assembly already supplied retail code. The only generated
progress change is this routine's assembly-to-C language field. The33 earlier
direct donor imports remain banked separately from this reconstructed draft.
The wider source-adoption and Game matching goal remains active.

## Steps

1. [x] Revalidate the clean consumer/tools baseline; pin nine source/image/profile/guard/header/assembly inputs.
2. [x] Read the complete retail routine, active shared prototype, callers, SDK structures and existing helper implementations/declarations.
3. [x] Screen field assignments, two structure-assignment forms and memcpy in the full owner; retain the directly matching structure assignment.
4. [x] Keep the existing public signature and function-local typed helper declarations; express32-bit table/pointer conversions explicitly.
5. [x] Preserve58 neighbors, sizes, relative relocations, normalized pools, all actual caller instructions and the same43 inherited warnings.
6. [x] Verify both actual padders without new target guards and four independent original/rebased comparisons.
7. [x] Pass4,320 MIPS cases, all103 reached words,208 actually fired root-memory prefixes and1,944 native32 cases per O2/O0 profile.
8. [x] Install only the qualified C body; verify the entire ELF, symbols, data, overflow, Makefile and guards remain byte-identical.
9. [x] Change only the selected progress language field; preserve immutable history through an exact whole-CSV hash gate.
10. [x] Pass12 target/capture tests19.764s and20 affected historical/control tests21.583s+5.177s, plus project tools checks.
11. [x] Sync only eight compatible task files to the older mirror; preserve499 unrelated dirty fingerprints and independent HEAD.
12. [x] Bank tools4e667db567cfd04e9f10ae3a5d69baa99a5389da before the consumer pin/source/docs, without push or host/Release work.
13. [x] Qualify func_1501B22C's61-word slot:59 code words plus two NOPs match with four guards. See [Note1368](1368-view-frustum-side-plane-guarded-match-20261014.md).
14. [ ] Continue actual failed-body/used-interface and pool-binding recovery, the unrecovered layer decoder/dependency and original Game matching.

## Source And Interface Evidence

The scalar draft matches99 of103 words; its first and third payload loads/
stores use t5/t7 instead of retail's assembler temporary. The semantic
structure assignment produces the complete retail six-word copy:

```c
if (payload) {
    *(struct167 *)record->unkA4 = *payload;
}
```

struct167 contains exactly three s32 words. The destination begins at0xA4;
the fourth word at0xB0 stays untouched. Both aggregate-address forms match
directly. memcpy emits100 words and a different call/epilogue; reject it.
The scalar-fields control retains the same bounded output/memory but differs
in raw words and final caller-scratch state. It is an allocation control,
not an effective functional negative.

Keep the existing shared11-argument struct210-return prototype in
conker/include/functions.h. The table remains its established32-bit word
interface; use explicit address/pointer casts without inventing a new shared
table layout. The three typed helper declarations follow the nearby
func_1513D2F0's function-local pattern. Their pointer returns agree with the
existing factory/resource implementations; cast resource pointers explicitly
into the record's32-bit storage. Byte parameters retain retail truncation.

The first naive insertion triggers late-declaration/implicit-return conflicts;
proper local declarations resolve them without changing other bodies.
Both before/after complete owners retain43 inherited warnings from the
existing caller/type family. The recovered constructor adds no warnings.
Do not describe the production build as warning-free; the known duplicate
generated_12D630 Makefile recipe warning also remains unchanged.

The primary full-owner padder still applies every existing neighbor guard.
The standalone extracted target uses no guard manifest because it has no
guards; supplying the whole owner's guard list correctly fails closed on
unapplied neighbor entries. No production guard is removed or disabled.
The separately assembled original agrees with both padded objects at retail
and rebased code/helper/global addresses, including HI/LO carry boundaries.

## Behavioral Qualification

All4,320 MIPS cases compare helper calls/payloads, return pointer, complete
public memory and architectural state against independent expected results.
The matrix crosses descriptor flags, default/explicit tables, zero/positive/
negative resource counts, signed loop limits, five payload layouts, factory
success/failure, helper mutations and two stack phases. Full-width arguments
and byte truncations exercise the complete11-argument o32 interface.

Helper updates change the descriptor before its copy and the loop limit
during setup/allocation. Resource/footer allocation hooks also return null
in selected modes. All103 code words are reached. All208 actually fired
root-memory prefixes agree on full state and actual PC/delay-slot identity.
Helpers are atomic bounded contracts, not arbitrary helper-fault qualification.

Native32 O2/O0 each pass1,944 cases, asserting SDK-compatible used-field
offsets/size and comparing full record/descriptor/payload bytes, callbacks,
live limit and returned pointer. The fwrapv profile models N64 non-trapping
signed arithmetic; native endianness is not guest-endian proof. Include
stddef.h for the harness's NULL definition, without changing production C.

Native cases use absent, disjoint or exact-self payloads and limits within
the four-element resource array. Partial aggregate overlap and a fifth
resource-slot write are guest-only emitted-access probes, not portable C
claims. Preserve retail's unchecked live limit and access sequence; add no
bounds repair or padding operation. No complete allocator/gameplay acceptance
is claimed by these component hooks.

Compiled category-mask, descriptor-copy-length and resource-clear-range
controls fail as intended. Raw image/source/progress/guard/profile/header/
assembly and frozen-input corruption controls remain effective.

## Closed Image And History

| Input | SHA-256 |
| --- | --- |
| Unchanged complete ELF | c9ff4e7ec28882546f87fb159a96b0c0e1c2b8fac6de4eb58725d91eef78a3bd |
| Baseline owner | 1dec97c1f46d7814f8f0f009232e323c5cb1fd6e1fa9e490042646156c87e0f8 |
| Final owner | 914f001c486928dec6b98dc840d66a3708d9e2c176f009fcc6eafdf5da268fb7 |
| Baseline progress | b7d6d464014d793ad67a1b6e39e5c4e51a29dfe87e1f5c3e8c109201d3cb2c02 |
| Final progress | 005fd7682d37802a2b7591cfb023648b6a083c8df6b957bdfedd737222cad68e |
| Unchanged Makefile | 838070597f76ea2f7182c158dfb6710946cfcabcb5435e994f93cdb99340e313 |
| Unchanged guards | 25d0c541e1bd0ea1d537439e8ba4234ad629ee9c5405025cc0408d99f28e5b9a |

Every serialized ELF byte, symbol address/extent/type, protected section and
overflow body is fixed. Protected data remains189,088 bytes across720 owners,
zero differences. All three pinned shared headers and original assembly also
remain unchanged. No expected-word substitution supplies this function.

The new inverse handles only the exact final progress CSV hash and path,
projecting it onto the pinned previous CSV. Unknown/corrupt inputs pass through
unchanged. After-progress capture cannot overwrite an existing fixture.
The affected earlier tests retain effective corruption controls; no baseline
is recaptured or excluded. The old113-test receipt in Note1366 is prior evidence,
not a new broad run. Fresh qualification comprises12 target/capture checks and
20 affected historical/control checks; unchanged behavior/neighbor receipts
are reused on the basis of the identical full image and58-neighbor proof.

Private inputs/receipts remain in
`conker/build/game-record-payload-constructor/`.
The fresh additional-source audit is
`conker/build/alternative-source-byte-audit-20261014/payload-constructor-after.json`.
It reports no remaining applicable raw linked donors; failed/commented/
used-interface/pool cases are not thereby completed.

```sh
python3 -m tools.experiments.game_record_payload_constructor_candidates
python3 -m unittest tools.tests.test_game_record_payload_constructor tools.tests.test_game_record_payload_constructor_candidates -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Progress And Boundaries

Fresh matching: Game2,873/4,831 (59.47%), total3,546/5,504 (64.43%),
different1,958, drift0. Conversion5,504/6,044 (91.07%),86.09% bytes;
Game4,831/5,323 (90.76%),85.46% bytes. Init492/492 C remains exact.
Legacy Debugger181/181 still includes140 data labels; executable-only
total3,406/5,364 (63.50%), Debugger41/41. Root README changes only four
aggregate rows. Structured CSV measurement skips the concatenated repeated
section headers instead of interpreting them as data.

All801 original archive files remain unchanged. Eight task mirror files
agree byte-for-byte, pass syntax checks and three standalone candidate tests
in0.002s. Mirror HEAD remains ddbdd16b53ce60b054fb6e11bf0649a41f48375a;
dirty count grows503 to507 because four task files are new. All499 unrelated
dirty fingerprints remain fixed. Preserve its independent history.

Tools4e667db banks first. No push, Claude call, host transfer/build or
frozen-Release operation occurs; preserve saves/configuration and unrelated
work. Full graph refresh refuses19,035 partial nodes in place of the40,814
curated graph, retaining19,398 nodes from2,972 excluded but still-present
files. Do not force it; await the incremental source commit worker separately.

Next func_1501B22C at VA0x1501B22C / ROM0x486DC remains a zero-return C stub
in conker/src/game_476D0.c. Its original draft is void with an indexed input;
the prior O2/g3 screen reports59 emitted/61 retail words and four differences.
That is unqualified survey evidence, not a complete-owner match or missing
padding diagnosis. Inspect actual slot/ABI/source scheduling next.

The layer decoder func_151F78B4 and its dependency func_151F63C4 remain
unrecovered. The99 individual compile failures,59 commented compile failures
and real symbol/pool/pseudo-operation cases remain explicit queues. Continue
actual reconstruction and original Game matching rather than crediting
survey discovery, empty donor queues or component hooks as goal completion.

## Post-Bank Verification

Consumere1f955a6 banks the source, tools pin and aggregate/detailed docs.
All16 post-bank target/capture/historical-control checks pass27.177s. The
incremental build reports ELF/progress up to date and retains the c9ff4e7e
complete image and005fd768 progress. The CSV is an ignored generated artifact,
not a tracked source file; do not force-add it. Main and active tools are clean
before this receipt commit; the independently dirty mirror stays preserved.

The source commit's incremental graph worker completes at40,826 nodes /
81,005 edges. It preserves the curated/excluded-file boundary and skips only
the oversized HTML visualization. No smaller forced refresh, push, host
transfer/build or frozen-Release operation is performed.
