# Matrix Reflection Direct Homes And Cache Removal

Date: 2026-10-13. Continue
[Note 1341](1341-game-matrix-reflection-economical-index-and-conditional-homes-20261013.md)
on `func_15034F30`: VA `0x15034F30..0x150356C8`, ROM `0x623E0..0x62B78`,
486 words / 1,944 bytes, original frame `0x190`.

## Scope And Baseline

Consumer baseline: `a636309c8d6d5ff4ce864023ef2b9c4394297e55`.
Tools baseline: `6bd22228863993d46e0ad1cdce6b3edeed24069e`.
Production remains the zero-return placeholder in
`conker/src/game/generated_61D10.c`. All candidate work is uninstalled.
No guard, compiler-profile, production source, linked image or progress edit.

New generator and qualification:

- `tools/experiments/game_matrix_reflection_dispatch_homes.py`
- `tools/tests/test_game_matrix_reflection_dispatch_homes.py`

The full Game matching goal remains active. This checkpoint earns no conversion
or matching credit and makes no host-port or gameplay acceptance claim.

## Missing Read And Real Dispatch

The economical cold329 source's access deficit is a missing **mode home**
read, not a missing output read. For mode0/count0/null actor, the fired oracle
records retail/cold/selected mode-home reads **3/2/3** and own access counts
**51/50/51**. The selected body restores that actual read.

Recover a volatile mode home with two opening snapshots after identity, the
shared mode0/mode1 primary route, and the later live mode read in the
far-in-range arm. Explicit primary/secondary/finish labels express the retail
dispatch. `firstMode` replaces the existing, same-size `matrixOffset` local;
there is no padding local, register binding or copied instruction body.

The selected `actor-gate-inputFixed` form emits:

| Measurement | Result |
| --- | --- |
| Complete body | 486 words |
| Frame | 400 bytes / `0x190` |
| Literal differences | 331 |
| Changes versus banked333 words | 289 |
| Compiler diagnostics / extra pools | Empty / 0 bytes |
| Production installation | No |

The score improves banked333 by two and the previous best332 by one, but this
is a substantial source/dispatch change, not two independent scheduling edits.
Thirty named complete forms produce eight extent/frame-valid literal arrays.
Equal331 scores do not imply identical instruction arrays.

Rejected forms remain visible and are not installed:

- Dispatch snapshots alone: 485 words / frame400 / 298 differences. Wrong extent.
- Input address recomputation alone: 487..490 words / frame408 (`0x198`). Wrong frame.
- Primary-only cursor output: 486/frame400/336; secondary-only: 485/frame400/468.
- Both cursor-output paths: 486/frame400/331. Tail carrier variants differ in
  emitted words despite sharing that score.

After normalization, recompute the real input matrix address from `input+i*64`
and use the existing byte offset for output conversion. Their existing loop
updates maintain the bounded input/output index relation. The tail reuses
`inputFixed` only after its representation-flag lifetime, restoring the earlier
input/output flag register roles without an incoming flag-home store.

## Owned Compiler Evidence

Fingerprint-locked CFE/UOPT/UGEN capture runs only on an owned compiler child.
The gate fires, the driver exits successfully, and normal/traced objects and
pools are identical. The recorded frame transitions are **88 -> 104 -> 400**.
Final physical layout: locals296 / saved88 / outgoing16.

Frontend definitions are M288/P76; optimizer definitions are M296/P76. Those
logical stream definitions are candidate-specific, not an original-frame
requirement. Compiler temporaries change while the physical400-byte frame stays
fixed. All four original matrix offsets remain `-268,-192,-128,-64`, corresponding
to SP+`0x84,0xD0,0x110,0x150`.

Both streams contain five direct `lod P+16` output-home reads and three direct
`lod P+8` mode reads. Neither contains `lda`/`rlda P+16` output-address work.
There is no `&output` expression or replacement indirect load in the selected C.
Raw words and byte offsets are retained in `direct-home-lowering.json`; no
undocumented stream flag-bit interpretation is needed.

Reflection's fp address cache is removed. The only optimized M-storage `rlda`
records are the two conversion-buffer `(-268, raw register20)` records. The
conversion cache still uses s4 rather than retail s5, so that role is unresolved.
The input bank is now s6, and words19..21 align the original input move,
`guMtxIdentF` call and direct SP+`0x150` argument. Input flag s7 and output flag
fp are also recovered.

The compiler strength-reduces the input cursor into s2: initialize from s6,
then advance by64. There is no shift-by6 instruction. Retail instead keeps a
saved shifted index across calls. The saved-role problem is **not finished**.

## Qualification And Remaining Differences

The inherited semantic, alias, native32, caller, full-owner/padder and rebase
contracts remain enabled. The full sampled guest domain covers 4,800 cases
with equal complete sampled RAM and helper packets. This does not establish
arbitrary inputs or actual SDK/provider execution.

Across192 fault domains, **10,196 common cuts actually fire**. All192 prior
full modeled agreements remain equal, with no loss and no new agreement.
Output-home read counts equal retail; absolute own-access-count distance from
retail never worsens relative to banked333. Hardware PC/BD/full FCSR/HI and
full-parent/gameplay execution are outside that evidence.

Opening cut1 still differs: the candidate first saves RA (`0xAFBF0064`), while
retail first saves s6 (`0xAFB60058`). Both stack phases retain this boundary.
For the fixed-input return witness, RAM/FPRs agree but GPR9/14 differ. Banked333
differs at GPR9/13: recovering13 while losing14 is not full-register improvement.
The original mixed-format alias still reaches the same bounded provider
rejection; its final result is not claimed.

Four controlled provider-action cases at phases0/8 prove the mode home remains
live after identity and a matrix helper. A compiled stale-mode negative has
opacity bytes retail/selected/bad **200/200/100**, an effective public mismatch.
These are guest-oracle provider actions, not observed SDK implementations.

## Restart And Test-Handoff Repair

The old test/update handles did not survive the restart. Process inventories
showed no surviving test/compiler/graph worker, so the suite was rerun rather
than assuming its old completion result.

The first fresh full run reports **24 tests / one failure / 102.045 seconds**.
An inherited home-control test compares the old407 diagnostic to the new331
candidate. It also pins the old indirect address/load words to `self.words`.
That is stale fixture identity, not a failed semantic or fault gate.

Only the new test subclass overrides that method. It separately asserts the
old407 diagnostic's shape, literal address/load words and distinction from the
new331 array. All21 older cold/home forms, the eight lower329 regressing domains,
the11/15-word array distinctions and the selected count-distance requirement
remain checked. The banked tests are unchanged; no assertions are monkeypatched.
Three fresh home/live-mode checks pass in **76.679 seconds** after this repair.
The final complete run passes **all24 checks in76.603 seconds**, including the
22 target checks and two protected text/data checks. Its full output is retained
locally in `conker/build/game-matrix-reflection-dispatch-homes-test/restarted-suite-fixed.log`.

The restarted REA server is connected, but its Windows Ghidra adapter rejects
this MIPS ELF target with `target_format_unsupported`. See
[the verified setup and host limitations](../REVERSE_ENGINEERING_SETUP.md).
No dependency install, unrelated configuration edit or target execution occurs.
Routine investigation uses zero additional Claude calls.

## Frozen Production And Banking

All seven target inputs and protected text inputs remain fixed. Root README
SHA256 stays `640d27f289d843d625eabd94f747b399fc31105726db2a78ab245962ac885e8c`.
The production ELF stays
`38ac5d5272b5800ff666bb1d284ccfa12409f3a25fa06b38068cd9d337973561`.
The unchanged banked counts are Game2,824/4,823, total3,497/5,496, different1,999,
drift0, converted5,496/6,044. There is no rebuild or aggregate credit change.

Both active and older tools copies pass ROM-free wrapper and Windows syntax
checks. Older HEAD remains `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`; all436
initial dirty-path fingerprints are preserved. Exactly two previously absent,
byte-identical files are added, with no mirror-history duplication or push.
Tools **af0ed5c607622da8157ce21d9cb04e0d821f1797** banks only the two new
generator/test files first. The consumer records that exact pin and these docs.

Direct Graphify update refuses a proposed18,736-node replacement for40,516
existing nodes. Preserve19,398 retained nodes from2,972 excluded-but-existing
files, the skill0.9.20/package0.9.26 warning and the zero-node devcontainer
warning. No forced shrink or install. Record the incremental hook separately.

Reproduction from the prepared consumer root under WSL:

```sh
python3 -m tools.experiments.game_matrix_reflection_dispatch_homes --filter actor-gate-inputFixed
python3 -m unittest tools.tests.test_game_matrix_reflection_dispatch_homes \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_05_production_and_protected_data_unchanged \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_06_effective_immutable_production_controls -v
make tools-check
```

## Next Work

Stay on this same function. Recover the original opening saved-store schedule
and the saved shifted-index lifetime rather than the strength-reduced input
cursor. Then finish the remaining331 words and all private/fault/linked-image
gates. Do not install or normalize the routine solely from sampled RAM agreement,
the correct extent/frame, recovered register roles or a lower aggregate score.
