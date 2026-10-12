# Game Event Record Constructor Direct Match - 2026-10-12

## Scope And Change

Resume from consumer `55dc6bc7` / tools `d3426e6` and
[Note 1314](1314-game-mode-callback-dispatcher-direct-match-20261012.md).
Both active repositories were clean. Keep the full Game matching goal active,
with the retained text218/frame0x80/114/cut27 and matrix translator still open.

Target `func_15015104` in [game_40490.c](../../conker/src/game_40490.c:274):
VA0x15015104..0x150151D4, ROM0x425B4..0x42684, 52 words / 208 bytes,
frame0x58. The existing semantic body compiled to 50 words/frame0x50 with
37 real differences. Only these two lines change:

```c
flags = *(s32 *)(arg0 + 0x20);
data.unkC = (flags ? 1 : 0) | (flags ? 2 : 0);
```

Retain the raw flag word rather than first converting it to a boolean. The
two independent tests recover all52 instructions directly at unchanged O2/g3
MIPS2, including original incoming-home reloads and frame. No diagnostics,
pool, expected-word guard, shared header, compiler profile or Makefile change.
Volatile-view controls did not match and remain ignored, not installed.

## Contract

- Set original input byte+0x14 to1. Snapshot its pointer and low byte of the
  word at+0x1C before either helper call.
- Call func_1510F800(0), reload the incoming pointer and pass signed halfwords
  at+0/+4 to func_1510FD20. Its return becomes the packet's word+8.
- Reload the pointer again, read its raw word+0x20 once and form flag0 or3.
  Packet word+0x10 is zero; six padding bytes are not initialized by this body.
- Creator arguments are (0x12C,-1,-1,-1,0,0x2C,0x14,0xFF,0). On nonnull
  allocation, copy exactly20 bytes to result+0x28; always return1.
- Packet resides at frame SP+0x44, original input home at SP+0x58; preserve
  RA save/restore and all delay slots. The data registry references this handler
  in [2275E0.data.s](../../conker/asm/data/2275E0.data.s:354).

## Qualification

Seven pre-install tests pass in68.022 seconds and seven post-install tests
in17.114 seconds, no skips.

```sh
python3 -m tools.experiments.game_event_record_constructor_candidates
python3 -m unittest tools.tests.test_game_event_record_constructor_match -v
```

- 15,552 guest cases cover six flag words, six code words, six coordinate
  patterns, four projection IDs, two stack phases, three helper mutations and
  null/separate/input-alias allocations. Complete RAM/events/GPR/FPR/calls
  agree with retail. Independently check signed arguments and all20 seeded
  packet/copy bytes, including padding.
- Guest-only provider mutations redirect the incoming home after each helper;
  native providers mutate the original input in place. Opaque helpers clobber
  caller-saved registers; their actual implementations are not exercised.
- Missing state/code/coordinate/flag bytes fail closed. All240 own-routine
  access-cut pairs fire and agree, with terminal no-fault controls. Helper
  accesses and call observation are excluded. PC/EPC/FCSR/hardware parity
  and live gameplay are not claimed by this bounded instruction model.
- The old source still has equivalent packet/helper results in the tested
  incoming-home redirect case. Its frame and first-access partial SP differ.
  Correct the original negative-test assumption instead of claiming a public
  semantic failure that was not observed.
- Native32 O2/O0 passes24,576 cases each, 49,152 comparisons, with nine creator
  arguments, signed coordinates, state/fences and alias output. Independently
  validate14 defined packet bytes; check all20 copied bytes against the memcpy
  witness without fixing unspecified C padding. Three fresh compiled controls
  reject wrong code, missing flag bit and wrong return.
- Production-preprocessed owner retains all31 neighbor bodies and relative
  relocations, all normalized pools, and zero warnings. Before/after production
  legacy padding changes only the target body/size/relocation locations.
- The strict full-owner padder rejects the same preexisting func_15014094
  overflow before and after (0xB8 vs slot0xB0). This is not a new defect or a
  strict-owner pass. Both isolated target padders emit identical208-byte objects.
  Missing split assembly for already-matched neighbors is represented by
  independently sourced retail layout/ROM metadata, not copied target words.
- Independent assembly/link of the complete original and C at three code/
  callee layouts produces identical52-word bodies without source guards.

Fixture fixes were bounded: define NULL for the native harness, compare target
relocations at their new instruction locations, locate preserved neighbor
metadata and distinguish existing whole-owner overflow from target fitting.
No shared oracle, helper ABI or neighbor implementation is changed.

## Build And Image Audit

`make -C conker -j4 build/conker.us.elf progress.csv` succeeds; only the known
duplicate generated_12D630 recipe warning remains. The literal whole ELF equals
the saved before-image except105 changed bytes in the declared208-byte target
slot and one byte of its exact symbol-size field, 200->208. All other bytes,
code, addresses, metadata and sections stay fixed. The changed slot has37
changed words. All189,088 Game-data bytes /720 owners remain exact, SHA0bbc00e1.
Guard history, progress.csv, retail layout and Makefile remain byte-identical.

ELF SHA-256: `c58a81de35830dfc82b671074e142d560b8faca9a5e395bdd499b1643ee0e12c`.
Owner source SHA-256: `b8f927f450741296f1e5834f635d5aba27c47df613ce1284a5fc8fbfc5b809c3`.
Fresh matching: Game2,815/4,823 (58.37%), total3,488/5,496 (63.46%),
different2,008/drift0. Converted functions/bytes stay fixed; root README gets
only its two aggregate matching rows.

## Retained Fixture And Bank

After the independent image gate passes, archive the text fixture's previous
manifest and complete C3CA image in ignored `game-event-record-constructor-test/
text-fixture-before-event-record/`. Advance only the expected ELF hash and
generated before-image/manifest; the other eight protected inputs and snapshot
hashes are verified unchanged. No old receipt is deleted or relabeled.
The callback checkpoint's historical whole-image test07 remains frozen to its
own bank; this new target's full-image gate proves that dispatcher unchanged.

Fresh combined target/text regression passes all16 tests in84.143 seconds,
including immutable/corruption controls and retained text53-word/710-of-768
access-cut evidence. Six callback regressions01..06 pass in50.777 seconds;
their historical whole-image07 is not rewritten or presented as a current gate.
These are22 distinct current/regression tests, no skips.

Mounted tools `ec4865d3101a7eccef1e0a69a2025a0682b93e8d` is committed
first, then source, this note, five indexes, workflow, README aggregates and
consumer gitlink. Preserve older tools HEAD`ddbdd16b`
and its dirty work: synchronize only absent task files and the fingerprint-
checked shared ELF-hash fixture. No older commit/reset/stash/history duplication,
push, OGL/Release/ROM/save/config/editor change, or extra Claude call.
All102 unrelated saved task fingerprints stay identical; dirty380 becomes
dirty382 and task hashes103 become105. WSL consumer/mounted/older tools checks,
Windows py_compile and whitespace checks pass. All4,574 relative links across
eight checked documents resolve. Repeat final integrity controls after bank
and require a fresh terminal Graphify Rebuilt receipt with advanced log bytes/
UTC and zero workers; preserve the existing graph/version/scan-size warnings.

## Next

`func_1501AE94` in `game_476D0.c` is the next ordinary queue entry:
44 words/frame0, still a zero-return placeholder with37 differences. Retail
indexes0x180-byte records through D_800BE628 and tests float bounds at+0x2C/
+0x30 against2.0f/(float D_800BE620-2.0f), then+0x24/+0x28 against0.0f/
float D_800BE624. Recover ordered comparisons and NaN behavior from the
original branches, not a simplified conjunction. No source fit is yet accepted.
Keep text218/114/cut27, translator49/34 and handwritten non-C-ABI150A76F0
boundaries separate and open; the full Game goal is not complete or narrowed.
