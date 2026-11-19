# Actor burst complete normal-execution relation and vector homes

Date: 2026-11-19. Continue `func_150BBB5C` from Note2562. The entire private
C recovery now passes the ordered normal-execution relation against
separately assembled retail across all16 initial masked-count pairs and80
symbolic paths. **This is not a byte match or an installation.** The body
is591 words versus587 retail words, still with an extra saved S4.

## Source changes established by instruction traces

The trail's first FP mismatch was resolved by two ordinary source changes:
place its Z update before the X-velocity update, and reverse the source
operands of its Y-coordinate addition. Together they recover the retail
sequence without another volatile view, extra arithmetic or a profile change.
Either change alone leaves an ordered FP difference.

The next mismatch was at the trail call: its18 argument words and vector
values agreed, but both raw vector addresses were20 bytes too high.
Moving the existing position/velocity array declarations after five existing
float scalar declarations recovers retail's exact incoming-SP-relative
addresses, **-400 for position and -412 for velocity**. No array was enlarged
and no padding variable was introduced. The frame remains624 bytes.

This closes the trail loop in the symbolic trace and exposes the final
burst's multiply operand order. Reversing that source multiply's operands
recovers the observed order while preserving its public read after the
random helper. A temporary-based alternative fails that ordering check.
Finally, ordering the three final descriptor velocity assignments X/Y/Z
recovers retail's horizontal multiply, negate, component multiplies and
additions. The other five assignment permutations fail the ordered trace.

The selected complete owner uses the existing O2/g3 profile. It has
**591 words / frame624 / 58 relocation sites**,569 unequal overlapping
words and four extra words. All eight owner neighbors and normalized pools
are unchanged. Raw SHA-256:
`ed52a6efaa49f8b77cd93ab52d9f49f605329dd5ac3b0cff60eef23a1c7e5773`.
Earlier589/590-word candidates remain preserved separately.

## Complete normal-execution relation and its contract

Only the first two random results' actual two-bit masks are specialized.
All16 mask pairs cover particle counts6..9 and trail counts10..13. Later
helper results remain arbitrary symbolic values. Each pair has five paths,
collectively visiting every591 raw and587 retail instruction position.

For every pair, the complete traces agree on:

- Ordered FP operations, operands and symbolic FCSR transitions.
- Helper order, all argument words and exact passed private addresses.
- The168-byte sprite, complete124-byte descriptors, and both trail vectors,
  retaining untouched symbolic bytes and permitted provider mutations.
- Public-read multisets within each quiet helper epoch.
- Restored stack, return address and saved integer/FP ABI state on return;
  the early rejection result is checked. Active results remain discarded
  as the real caller discards them.

The instruction decoder and transfer engine from Note2562 are reused
unchanged. Providers preserve the o32 saved ABI, but may arbitrarily clobber
caller registers/FCSR, change public memory, and mutate previously passed
private packet/vector ranges at later calls. Public memory and literals
are disjoint from the private frame; providers cannot inspect unpassed
locals, caller implementation code or its return PCs. Public reads are
ordinary, mapped and aligned within this normal-execution contract.

**Complete private-frame equality, arbitrary fault prefixes, interrupts,
portable undefined inputs and gameplay acceptance remain unproved.**
The full normal relation does not establish literal matching, a fitting
slot, physical coexistence with the following routine or safe adoption.

## Validation, rejected controls and remaining work

The focused suite checks the full-owner/80-path relation,274 direct guest
cases/all587 retail words and two early type-byte fault checks,384 native
SDK32 cases each at O0/O2/O3 with UBSan/strict aliasing and12 effective
semantic negatives, and3,072 cases through the original caller's relevant
dispatch paths with six caller controls. Thirteen effective full-relation
controls cover the newly recovered ordering/homes, wrong sound data and
the earlier sprite/descriptor constraints. Verifier limitations cannot
count as semantic rejections.

Native fixture remains2,827,780 bytes with SHA-256
`423cca435e1405de3fa1a4660e5c34507e75a9c702726394fbe1a72a2eb7e43e`.
Caller coverage remains42/252 caller positions and584/587 target positions;
the direct guest tests cover the remaining rejection. The alternate helper
is still an opaque ABI service. The oversized raw body extends16 bytes
past its slot, so the unused raw callback is omitted on the mutually
exclusive alternate path; no physical-overlay coexistence is claimed.

Descriptor arrays, register hints, unsigned count/index variants and
equivalent descriptor address spellings do not remove S4. A volatile
descriptor regresses the first-loop FP order. Integer address views add
another word; ordinary field/byte views leave the591-word object identical.
The constant-allocation profile rejected in Note2560 remains rejected.

All1,875 committed baseline inputs are frozen and verified. Production
source/object/ELF, original ASM, profiles, guard recipes, protected data,
progress and root README tables remain unchanged. The sibling tools HEAD,
dirty status and343 dependency hashes are preserved. Both final five-test suites pass with zero errors, failures or skips and341
imported tool hashes each. Runner times are416.411s primary and450.17s
sibling. The893-file overlay uses339 matching sibling files,549 primary
fallbacks, four task files and one bootstrap. `make tools-check` passes.

Paired receipts,
exact traces/terms and graph-retention evidence are under
`conker/build/game-next-150bbb5c-trail-private/`.

Total stays **4,558 / 5,514 (82.66%)**, Game **3,885 / 4,841 (80.25%)**,
zero drift; **129** more matches reach85%. No matching credit, production
Make/recount, host/Release/save change or gameplay acceptance is claimed.

Resume `tools/experiments/game_actor_burst_150bbb5c_full_manifest.json`.
Recover S4/address lifetime and the remaining physical/private layout
differences without weakening the complete normal relation. Then pass
both padders, strict independent whole-image prediction, actual Make,
installed tests and fresh recount before credit. Keep the85% goal active;
commit tools before the consumer, with no push or automatic pause.
