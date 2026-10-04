# Init Callee Preserving Core Adapter Fitting

Date: 2026-10-04. Baseline: `44dadc33`.

## Result

Opt-in assembler symbol INIT_DECODE_CORE_PRESERVES_CALLEE=1 removes ten
duplicate adapter reloads after the compiled C core returns. Physical retail
frame stores and RA restoration remain. The adapter body falls 296 to 256
bytes, aligned text 304 to 256. Every linked shape saves 48 bytes, with
unchanged stack bounds. Packed O2 linked text is 4,640 / 656 over retail.

The original reload path remains the default. This is isolated fitting and
bounded context qualification, not production conversion or changed corpus.

## Ownership And Register Contract

The normal compiled core and its callees preserve S0-S7, GP and FP across
the call. The adapter itself does not modify those ten registers. Reloading
them from the retail frame is therefore redundant when this connected call
contract holds. The saved cells still must be written: physical frame contents
are part of the oracle, and six cells seed retail scratch-FPR history.

Only the ten LW instructions from offsets A48..A64, A78 and A7C are gated.
The saved RA is still restored because the adapter's JAL changes it. SP
adjustments, argument marshaling, state stores and FPR publication are
unchanged. State remains 116 bytes, physical frame A88 and extra area 98.
The macro is not appropriate for a nonstandard core that clobbers these
registers. This does not justify removing retail assembly's own restores.

## Active Boundary Gate

CalleePreservingFixture locates the unique direct adapter JAL to the compiled
core and captures its return PC at JAL + 8, before any adapter restoration.
It compares all ten callee registers with the adapter-entry snapshot for
every bounded context execution. Thus an outer handler's eventual register
restoration cannot hide a violated core-to-adapter contract.

The explicit gate checks all six adapters retain the ten stores and contain
none of their ten reloads. Its positive empty-stream cases execute the
compiled core. The final negative cases replace the verified core return
delay-slot NOP with an ORI that clobbers S0; all six executions must raise
the specific callee-register guard failure. No compiled source is altered
by this test-only instruction injection.

The first strengthened probe incorrectly searched for an S0 reload in the
top-level core. Its isolated test fails in 2.475s on frame/O2 because that
core never uses S0 and has no such reload. The probe is corrected to the
unique JR RA and verified NOP delay slot; the isolated strengthened gate
then passes in 4.935s. This is a probe correction, not a candidate failure.
The already-loaded whole suite used the earlier snapshot-tamper negative
gate; the separately fresh instruction-injection run qualifies the final
stronger gate. No claim is made that the whole suite loaded the later edit.

## Measurements And Verification

Fresh whole guest suite: 35 tests in 250.420s, 34 passes / one intentional
opt-in corpus skip. Both CU1 context sets, representative retail pages,
initializer poison, allocation order, root descent, repeats/overflow and
neighbor red-zone checks pass. Nested lookup still records 3,212 calls /
3,383 iterations on page 169. All observed descents equal static bounds:

| Shape / profile | Linked before / after | Static / observed descent |
| --- | ---: | ---: |
| Frame / O2 g3 | 5,824 / 5,776 | 3,272 / 3,272 |
| Frame / O1 | 6,336 / 6,288 | 3,208 / 3,208 |
| Aligned end / O2 g3 | 4,720 / 4,672 | 3,232 / 3,232 |
| Aligned end / O1 | 6,128 / 6,080 | 3,192 / 3,192 |
| Packed remaining / O2 g3 | 4,688 / 4,640 | 3,240 / 3,240 |
| Packed remaining / O1 | 6,128 / 6,080 | 3,200 / 3,200 |

Packed minimum SP remains 0x80031D68 and known-neighbor clearance 88 bytes;
this is not complete reservation/hardware proof. Sixteen supporting helper/
selection and omitted-option size tests pass in 1.966s. Combined with the
separately strengthened gate: 51 passing test executions / one corpus skip,
excluding the initial failing probe. Project tool and whitespace checks pass.

The adapter .text without the new symbol matches HEAD's assembly byte-for-byte
under ABI shadow plus core-owned state, verified with GNU objcopy and cmp.
Artifacts are in `conker/build/init-callee-preserving-adapter-20261004`.
The prior omitted-option size gate still reports Note 873's 4,688 linked O2.
No entire ELF/ROM match, production build or sibling-port test is claimed.

## Next

- [x] Remove duplicate reloads only behind an explicit assembler symbol.
- [x] Verify callee values at the core return boundary and activate a clobber guard.
- [x] Preserve saved frame cells and qualify six bounded shapes.
- [ ] Qualify the changed combination's full masked CU1-clear and CU1-set corpus.
- [ ] Continue fitting, entry ownership and hardware/context/complete-reservation gates.

The new corpus class is InitDecompressorCalleePreservingAdapterCorpusTests.
Notes 871/872's 1,014 paired pages do not qualify this changed core/adapter
combination. Production sources, defaults, progress CSV and README counts
are unchanged; unrelated dirty Game source/tests remain preserved and unstaged.
