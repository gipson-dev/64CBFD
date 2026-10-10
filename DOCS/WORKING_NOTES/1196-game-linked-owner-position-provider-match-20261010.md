# Game Linked Owner Position Provider Match

Date: 2026-10-10

## Baseline And Result

Continue after consumer 3ef4e3099b838ad3e0858296908209bcd1c77809 and tools
704e5f8d758d8cc3f4d4b9066f8f7324b6ce901d, both active checkouts clean.
[Note 1195](1195-game-owner-point-arc-byte-match-20261010.md) completed and
banked the adjacent arc match. The wider Game matching goal remains active.

func_151B3F28: VA0x151B3F28..0x151B3FDC, ROM0x1E13D8..0x1E148C,
45 words / 180 bytes, leaf with no frame allocation. Replace its false
zero-return placeholder in [generated_1E0560.c](../../conker/src/game/generated_1E0560.c)
with the complete linked-owner position provider. Every linked byte matches
retail. This is semantic C plus narrow guards, not a plain-C match.

Single Codex writer, zero Claude calls. Reuse the offline workflow, scoped
graph query, complete compiler bodies and existing compiler/parser/MIPS/native32/
padder/ELF/data helpers. No shared helper or compiler profile changes. No OGL,
Release, save or editor changes. Root README receives only aggregate rows.

## Recovered Contract

Three arguments: actor, output XYZ pointer, and unsigned byte enable mode.
Retail first saves the entire incoming A2 word at SP+8, then tests its low byte.
Do not allocate a frame or substitute a narrow store for the argument home.

Enabled mode dereferences actor+0x150 and tests the linked object's first word.
There is no null-link safety gate: an enabled null link faults. If the first
word is nonzero, reload the link and compare actor+0x154's epoch with the
linked object's byte+0x3B. Failure leaves XYZ untouched, sets actor+0x10 bits
0xC and returns0. Success copies linked XYZ+0x14/+0x18/+0x1C, clears flag0x4
after all stores and returns1. Reload the link after each preceding output
store; output may replace that pointer or overlap source coordinates/flags.

Disabled mode does not read the link. Store output X=0, load D_800AA3AC,
store Z=0, then store the captured Y value. Clear flag0x8 and return1.
The constant's protected retail bits are 0x453B8000. Reading it before the
Z store matters when output overlaps the constant.

Actual registration is D_8008FAF0[0] at0x8008FAF0, ROM0x2345B0. The complete
original 81-word func_151B3184 invokes it for actor+0x14 with mode1 and
actor+0x20 with mode0. A failing provider still permits the second call and
causes the eventual removal callback. Registration and dispatcher stay unchanged.

## Compiler And Matching Recipe

[Candidate driver](../../tools/experiments/game_owner_link_position_candidates.py):
the selected complete O2/g3 body emits 44 words, frame 0, no pools, no diagnostics
and 16 raw differences. Five discriminating full source forms measure:

| Form | Words | Raw Differences |
| --- | ---: | ---: |
| Selected byte mode, captured constant, shared return | 44 | 16 |
| Word mode with explicit byte cast | 42 | 44 |
| Volatile byte mode | 44 | 19 |
| Early failure return | 44 | 21 |
| Constant read after Z store | 44 | 15 |

The late-constant form has fewer differences but violates the global/output
alias contract. It is not the selected source.

The recipe accepts only the complete expected 44-word instruction shape, with
relocation immediate fields handled separately. It never reads retail words to
construct output. Move the failure flag store ahead of its branch and copy the
existing shared return move into that branch's delay slot. Branch to the return
after the shared move. Adjust the two branches crossing the additional slot.
Rename only the disabled-path zero and captured-Y FP roles to retail f0/f10.

Append 44 manifest guards: nine changed words, 35 unchanged dependencies and
one inserted return-move copy. No omissions, frame changes or relocation-spec
substitutions. HI16/LO16 follow their original instructions through the added
slot. All four independent links reproduce all 45 original words, including
address sets crossing signed-low relocation boundaries.

## Fresh Qualification

[Focused suite](../../tools/tests/test_game_owner_link_position_match.py):
all nine tests pass before installation in 5.930s and after in 6.334s.

- 3,456 guest matrix cases / 10,368 executions compare complete original,
  raw C and normalized bodies: mode narrowing, flags, active/empty/stale epoch,
  12 raw float patterns and both stack phases. Entire memory, ordered reads/
  writes, return, full-word argument home and saved GP/FP/SP agree.
- 44 reachable retail words covered. Offset0x6C is an unreachable repeated
  flag load, retained by the full 45-word byte match, not claimed executed.
- 18 alias/control cases include output replacing the link, overlapping
  coordinates/flags and overwriting the constant. Cached-link and late-global
  controls demonstrably produce different memory.
- 14 paired fault prefixes retain ordered accesses and prior writes. Enabled
  null-link faults; disabled null-link succeeds without dereference. These
  qualify emitted guest order, not portable C fault semantics or hardware traps.
- Native32 executes 73,728 independent expected-result/flag/bit-pattern cases
  plus three aliases using the complete selected C. NaN, infinity, signed zero,
  output sentinels, link replacement and sequential coordinate overlap qualify.
- Twelve independent links across four entry/global address sets; 36 guest
  rebase cases. Full original 81-word dispatcher qualifies 24 connected cases,
  both endpoint calls and success/failure removal behavior.
- Copied actual owner preserves 16 neighbors, pools, relative relocations and
  every other padded byte, with zero diagnostics. Actual padder emits 180 bytes.
- Every individually stale raw word is rejected by the actual padder at its
  own offset; a relocation-spec negative is rejected separately.

Initial connected-fixture run lacked signed LB support; reuse the existing
ActorOracle implementation. Avoid importing a TestCase directly into this test
module so unittest does not accidentally rerun its unrelated suite. Both are
fixture corrections, not production changes or weakened gates.

Fresh build/progress and make tools-check pass. Existing duplicate generated_12D630
recipe and unrelated legacy compiler warnings persist; do not call the entire
build warning-free. The target's isolated and copied-owner compiles are clean.
Do not rerun settled broad suites: shared helpers/profiles are unchanged, and
the fresh copied-owner plus entire-ELF audit proves every other linked body
unchanged. Earlier arc receipts remain prior evidence, not fresh tests.

## Installation And Bank

The entire rebuilt ELF equals the baseline after replacing only the target
180-byte slot and symbol size. Decoded metadata agrees; symbol/string table
ordering is normalized for the physical byte comparison. Conversion CSV is
byte-identical. All prior guard bytes are retained as a prefix.

Protected data: 189,088 bytes / 720 owners, zero differences. SHA-256 remains
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
The registered provider and fallback constant are unchanged.

Fresh matcher: Game 2,746/4,816 (57.02%), total 3,419/5,489 (62.29%),
Init 492/492 and Debugger 181/181 exact. Zero drift / 2,070 different. One new
Game byte match; converted counts/bytes unchanged because the prior stub was C.

Tools 5a2c6f8fca1f43ebbf9c9861f1e36bbe7d6a805d banks the two authored files
first; parent source/guards/docs/pin follow. Only those absent new files are
mirrored to the older checkout. Its HEAD stays ddbdd16b53ce60b054fb6e11bf0649a41f48375a,
both pre-existing tracked dirty hashes stay identical, and 146 entries become 148.
No conflicting overwrite, reset, older-checkout commit or push.

Fresh graphify update . exits 1 rather than shrinking 39,166 nodes to 17,385;
preserves 19,398 nodes from 2,972 still-existing out-of-corpus files. Retain its
version/zero-node warnings; no force, purge or install. Await the detached
parent post-commit hook before reporting a clean, fully banked checkpoint.

Scoped documentation audit: 18 documents / 4,002 relative links, zero broken.
Twenty affected tooling files parse in both checkouts and have exact older
mirrors; two are newly authored for this match.

Post-install SHA-256:

- Source: 3db149df8d8ec9259bbad474443f218389fe9c77cd124c4b553c6e155443f6e7
- ELF: 372c1a3cb1d9bd30ade378f5ef1ae61ee55cf6d561514b7d0bfab2c950ea80d5
- Guards: fce7f717ad39f26abf14faea1222ff69004ed6e94c24b7f69438463aee5a4ce6
- Progress: 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24

Ignored measurements/receipts: conker/build/game-owner-link-position/ and
conker/build/game-owner-link-position-test/.

## Resume

- [x] Recover the complete byte-mode provider, pointer reloads and fallback access order.
- [x] Qualify raw/native/guest/aliases/faults/dispatch/rebases/owner/stale guards.
- [x] Install all 45 matching words and prove only the target slot/symbol size changed.
- [x] Measure fresh totals; bank tools before parent source/guards/docs/pin.
- [ ] Next: func_151B3FDC, VA0x151B3FDC..0x151B42A4,
  ROM0x1E148C..0x1E1754, 178 words / 712 bytes, frame 0x118.
  Registration D_8008FAF8[2] at0x8008FB00 is verified. Recover the complete
  adjacent callback from its assembly, respecting saved GP/FP homes and
  endpoint accesses; start with isolated complete-body compilation and no installation.
- [ ] Keep real trig/hardware/FCSR/live rendering/gameplay acceptance separate.
