# Game Owner Point Arc Byte Match

Date: 2026-10-10

## Baseline And Result

Continue after consumer 45dca444570a39b3d8287b90814b5863ab0f32c8 and tools
c5260a6cd0c3041fcf21f9711a4dfd276e00a001, both active checkouts clean.
The preceding goal turn made progress by certifying the branch-copy slot fold
in [Note 1194](1194-game-owner-point-arc-certified-branch-fold-20261010.md).

func_151B3CF0: VA 0x151B3CF0..0x151B3F28, ROM 0x1E11A0..0x1E13D8,
142 words / 568 bytes, frame 0x88. The false zero-return placeholder in
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c) is replaced by
the complete semantic owner ten-point arc routine with its one-argument ABI.
All 568 linked bytes now match retail, with no address drift.

Raw IDO output remains 144 words / 138 differences / frame136. The linked
142-word match uses certified register/scheduling guards, not a plain-C match.
No profile changes, frame patches or inserted words. Converted counts stay
unchanged because this function was already represented by a C placeholder.

Single Codex writer, zero Claude calls. Reuse the offline workflow, scoped graph
query, complete compiler bodies and existing parsers/MIPS/native32/padder/audit
helpers. No OGL, Release, save or editor changes. Function narratives stay out
of the root README; only its measured aggregate rows and date are updated.

## Recovered Behavior

The complete source is unchanged from Note 1194's qualified six-read body:
snapshot both XYZ endpoints once; form delta, midpoint and relative endpoints;
reject near-zero horizontal displacement without output stores; normalize the
horizontal direction; compute projected/vertical span, angle and half-radius;
then write ten XYZ positions at actor+0x48 with a 0x18-byte stride.
Return 1 on both paths. Point velocities, metadata and flags remain unchanged.

Load bias and angle step after the angle helper, retain that step across all
twenty sin/cos calls, and advance angle once per point including the final one.
The original saved-register homes, nine vector homes, SP+0x80 delta-Y store/load,
entire final private memory and six input reads remain intact.

## Closed Matching Recipe

[Matching driver](../../tools/experiments/game_owner_points_arc_matching.py)
starts only from the complete raw compiler output. Four closed windows each
retain every source instruction once after the already certified two-copy fold:
opening address/input schedule, vector workspace/projection, radius/counter
setup, and the final loop. Explicit expected FP fields recover endpoint,
normalization, projection, radius, angle and temporary roles. A closed S1/S2
counter/cursor swap restores retail allocation and the original angle update
in the branch delay slot. The restore tail and original frame are not patched.

Generation does not read retail words to construct output. Retail is an
independent comparison input. The driver carries relocations with moved source
instructions and reports raw versus normalized relocation offsets separately.
All four independently linked symbol sets reproduce the original words.

Full-function symbolic qualification covers X-active, Z-only-active and early
return paths. The two active paths each retain 21 ordered helper calls and
30 ordered public stores; early return has neither. Complete byte memory,
read/write multisets, branch decisions, saved GP/FP state and return agree;
all 142 words are reached. The expression model permits add/multiply operand
commutation, specifically the three midpoint additions and radius/cos multiply.
It is not a raw-C NaN-payload, FCSR/trap or access-order proof. Exact linked
retail bytes and bounded numeric qualification are separate, stronger gates
for the installed machine routine and modeled helper contract respectively.

The production manifest appends 144 expected-word/relocation rows: 104 changed
words, two certified omissions and 38 no-op guards. Four rows transfer relocation
records. Every raw word is guarded, including unchanged proof dependencies.
No history rows are replaced. Both symbolic and actual padder gates reject
effective live-value/counter/angle errors; every individual stale word is rejected
at its own offset by the actual padder.

## Fresh Qualification And Installation

[Focused suite](../../tools/tests/test_game_owner_points_arc_match.py):
all twelve tests pass before installation in 25.814s and again after the fresh
linked build in 34.324s, zero skips. Reuse Note 1194's 35 source forms and 48
retained suites explicitly: source/profile/helper/parser/oracle fingerprints are
unchanged, and the selected source is asserted identical. Do not call them fresh.

- Guest: 2,560 cases / 7,680 executions, all flag bytes, five geometries and
  two stack phases; every original142/raw144/matched142 word reached. Complete
  actor/canaries, saved registers, final private memory/writes and six reads agree.
- Boundaries/helper mutations: 48 cases / 144 executions; signed zero, threshold,
  tiny/NaN/infinity, snapshot and retained-step cases; seven compiled semantic
  negatives remain effective.
- Actual raw native32 C: 512 finite cases against original guest, with bitwise
  helper arguments/order and complete actor/canary agreement.
- Actual original 81-word registered update: 18 cases / 36 executions; original
  one-argument callback at 0x8008FAFC and return ABI.
- Four independent symbol sets / twelve actual links: 40 cases / 120 executions;
  all nine relocation uses, complete private memory and six reads retained.
  Every 568-byte matched body equals independently linked original assembly.
- Actual copied owner: 16 neighbors, pools, all other padded bytes, addresses and
  relative relocations unchanged. Isolated/owner match equal; next function remains
  exactly 568 bytes away. Raw unguarded padder still rejects two-word overflow.
- Six endpoint missing-byte faults in both phases: 12 cases / 24 executions.
  Retain six earlier public fault-prefix tests and two unused-byte cases.
- Retain independent ten/seven-read and wrong-private-home controls. Add all
  144 stale-word negatives and five effective Z/half/FP/counter/angle negatives.
- Fresh make -C conker -j4 build/conker.us.elf progress.csv succeeds. The shared
  manifest dependency rebuilds other objects too; duplicate generated_12D630
  recipe and unrelated pointer/type warnings remain. Target compilation has
  zero diagnostics; do not describe the full build as warning-free.
- Whole-ELF audit proves only this 568-byte target slot and its symbol size change.
  Decode/compare symbol and string tables before comparing all remaining ELF
  bytes. All other function bodies, addresses, extents and section bytes agree.
- All 189,088 protected bytes / 720 owners remain exact, SHA-256
  0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
  Registration and every prior guard row/prefix byte remain unchanged.
  Conversion progress.csv is byte-identical to baseline.

The first stale-word fixture used objcopy --update-section, which removed text
relocations and could fail before the intended changed word. Replace it with
structured ELF text-offset mutation that leaves all relocation records intact;
assert the exact mutated offset in each stale-word failure. This is a fixture
correction, not permission to weaken relocation guards.

Actual sinf/cosf still have zero-return placeholders; the full 80-word angle
helper is exact. Their linked bodies are audited unchanged. Bounded helper
responses and native32 comparisons are not real trig, hardware/FCSR or live
rendering/gameplay acceptance. Recover real trig as separate work.

## Banked State

Fresh matcher: total3,418/5,489 (62.27%), Game2,745/4,816 (57.00%), Init492/492
and Debugger181/181 exact. Zero drift / 2,071 different: one new Game match.
Converted counts/bytes remain unchanged. Fresh make tools-check passes.

Tools 704e5f8d758d8cc3f4d4b9066f8f7324b6ce901d commits the two authored files
before parent source/guards/docs/pin. Mirror only those absent files to the older
checkout: HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a, all 144 prior dirty
entries and both tracked dirty hashes retained; two additions yield 146.
No conflicting overwrite, reset, older commit, push or duplicate history.

Fresh graphify update . exits 1, refusing 39,156-to-17,375 node shrink; preserves
19,398 nodes from 2,972 out-of-corpus files. Keep version/zero-node warnings;
no force/purge/install. Await the detached parent hook before a clean-bank report.
Scoped documentation audit: 17 documents / 3,992 relative links, zero broken.
Eighteen affected tooling files parse in both checkouts and have exact older
mirrors; two are newly authored this turn. Related arc matching/installation
roadmap tasks are checked off; trig/live tasks remain open.

Post-install SHA-256:

- Source: 32c76e5d38ce06228f0044ac95bc52fa4dd847cebf5e71399c1a7ddc8f75171a
- ELF: 8c9b447267d0254e88b4db07aebc97080c5790b0d0a6c7e766609855a80f9be7
- Guards: c5c7d6d501b8feb9135604788ca06e1124bec1df53345f7b1bd4fa3b6c789135
- Progress: 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24

Ignored receipts: conker/build/game-owner-points-arc-matching/ and
conker/build/game-owner-points-arc-match-test/.

## Resume

- [x] Recover all FP/GPR roles, counter/cursor schedule and branch-delay angle update.
- [x] Reproduce and install all 142 retail words from complete semantic C plus guards.
- [x] Qualify raw/native/guest/dispatch/rebase/owner/fault/data/guard-history gates.
- [x] Rebuild and audit the entire ELF; measure the single new byte-exact match.
- [x] Bank tools first and parent source/guards/docs/pin second; preserve older work.
- [ ] Next: func_151B3F28, VA0x151B3F28..0x151B3FDC, ROM0x1E13D8..0x1E148C,
  45 words / 180 bytes, currently a false zero-return C placeholder in this owner.
  Recover its attached-object position provider and three-argument/u8 ABI:
  pointer/active-word/epoch validation, repeated pointer reloads before XYZ stores,
  success flag-0x4 clear, failure flag-0xC set/return0, and disabled fallback
  (0, D_800AA3AC, 0) with flag-0x8 clear/return1. Preserve pointer/output aliases
  and the original argument home; inspect the actual caller registration first.
- [ ] Recover actual trig separately before full arc rendering/gameplay acceptance.

The wider Game matching goal remains active; this function's match is complete.
