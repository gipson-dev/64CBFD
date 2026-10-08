# Game Attachment Progress Copy Direct Match

Date: 2026-10-08

## Scope And Baseline

Continue Game matching from commit `ca08b828` and
[Note 1109](1109-game-attachment-progress-direct-match-20261007.md).
Recover `func_150331B8`, VA `150331B8..1503327C`, ROM `60668..6072C`.
Retail is **49 words / 196 bytes / frame `0x30`**, not the 50-word estimate
in the prior conversation handoff. The old three-word zero-return C placeholder
was padded to 49 words, with **46 instruction differences**. It was already
counted as converted, not semantically recovered or exact.

The [production owner](../../conker/src/game/generated_5D2C0.c) now contains
the complete setup/progress copier and clamp. All **49 words emit directly
as retail** under existing `-O2 -g3` / MIPS2. No guards, instruction insertion
or omission, padding promotion, profile/Makefile changes or shared types.
Reuse the setup declaration recovered in Note 1109.

## Recovered Contract

Cache actor source `+0x2D0` before reading node attachment `+0x48`. The actor
read is required even when absent attachment returns zero; actor `+0x2E4` and
source data are lazy behind that attachment gate. For a nonnull attachment,
read the complete actor word `+0x2E4`, mask its low byte, and skip setup only
when that byte is `0xFF`. Otherwise call
`func_1503F5B8(attachment, 0, index, 1.0f, 0.0f, 1)`.
Float one is in A3, float zero at `sp+0x10`, integer one at `sp+0x14`.

Keep the cached source across setup, even when actor `+0x2D0` changes.
Changes to that source's float remain visible. Its retail spill is `sp+0x2C`;
declaring source before attachment reproduces it directly. Reversed declaration
order emits the same 49 words but differs at the two `sp+0x28` spill accesses.

Reload the incoming node home after setup (also on the no-setup source gate).
Null cached source skips copy/clamp, not earlier setup. Otherwise read source
float `+8`, reload node attachment, and store current float `+8`.
**Reload attachment again after this store**: output may overlap node `+0x48`
and replace the pointer. Read end `+0x18` before current `+8`; when
`end <= current`, store single-precision `end - 1.0f`. Every successful path
returns zero. Do not add node/actor/post-setup null gates or an early source gate.
Required reads/stores and preceding partial effects are original behavior.

## Compiler Evidence

The [candidate driver](../../tools/experiments/game_attachment_copy_candidates.py)
and [ten tests](../../tools/tests/test_game_attachment_copy_match.py) retain
**11 distinct source/profile combinations / 396 ordinary executions**.
All eight register/comparison/signed-index forms are raw exact at `-O2 -g3`.
All-control homes/faults/read-order/private equivalence is not claimed.

| Profile | Meaningful Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| `-O2 -g3` | 49 | `0x30` | 0 |
| `-O2` | 48 | `0x30` | 43 |
| `-O1 -g3` | 53 | `0x30` | 51 |
| `-O1` | 53 | `0x30` | 51 |

## Qualification

All **ten pre-install tests pass in 45.008 seconds**, zero skips/errors/failures.
The added fifth negative and prior progress-owner recheck pass as two tests in
5.899 seconds before installation.

- **60,000 guest cases plus eight lazy coverage cases**: eight index words,
  25 current/end float patterns, six setup mutation modes, two SP phases.
  Independent contract checks returns, ABI, public read/write order, memory
  and node home. Full C/retail GP/FP files and events agree; saved SP/GP/RA/FP
  preserved. Only unvisited word is unreachable branch-likely duplicate 11.
- **97 aliases**, source/destination equality, source at node pointer field,
  destination overlapping node `+0x48`, pointer and incoming-home replacement.
  Explicit copy-induced replacement proves the new attachment is clamped.
  Arbitrary private-stack aliases are not established.
- Two lazy gates and **13 required read/store faults**, actor source before
  absent return, node/index/source/destination/end, replacement pointers and
  post-setup nulls. Exact fault, ordered preceding public trace and partial
  effects agree. Source null skips copy, not setup.
- **75,000 native32 cases plus one lazy case**, complete actual C, valid aligned
  objects, five public callback modes and three source forms (separate,
  destination alias, null). Compare return, calls, six ABI words and all bytes
  of six objects. Signed zero, adjacent thresholds, extremes, infinity, quiet
  NaNs and subnormal values included. Native invalid pointers/private homes
  and FCSR exception/trap state are not qualified.
- Five compiled effective negatives: reread actor source, strict clamp, omit
  minus one, unmasked setup index, cache destination. Each changes calls or
  public memory; a fault is not accepted as successful negative evidence.
- Copied owner: **40 functions / 39 unchanged neighbors**, zero warnings,
  isolated target equal, neighbor bytes/relocations and pools intact.
  Prior progress-owner isolation now retains the existing setup declaration
  because both recovered functions use that prototype.
- Real padder: **196-byte meaningful body and slot**, no padding. Sole symbolic
  `R_MIPS_26` at `+0x5C`, complete links under independent entry/callee rebases.

Setup uses a bounded validating callback, not the connected full callee or
hardware/PC-port acceptance. Both models execute the complete original body.
The first alias fixture overwrote its own node pointer during initialization;
correcting that mapped-pointer fixture required no production change.

All **52 installed copy/progress/lookup/key-fit/resolver regression tests pass
in 452.150 seconds**, zero skips/errors/failures. Both actual-wrapper connection
suites and prior alias/home/native/owner/padder gates remain green.
`make tools-check`, Python syntax, driver CLI help and whitespace checks pass.
Documentation checks **92 documents / 4,052 relative links / zero broken links**.
This remains scoped guest/native/tool qualification, not full setup/FCSR/hardware
or PC-port acceptance.

## Linked Audit And Progress

US ELF and CSV rebuilt through normal rules. Compare to Note 1109's ignored
`game-attachment-progress-test/after.json`. Only target changes across
**6,058 symbols / 6,042 slots**. All **6,057 other symbol bodies**, slot addresses
and extents, sixteen overflows, protected Init/Debugger/Game-data sections,
**720 exact data owners / 189,088 bytes**, **11,063 guards**, and conversion CSV
hash remain unchanged. Only pre-existing duplicate `generated_12D630` warning.

Exact **3,367/5,467 total (61.59%)**, **2,694/4,794 Game (56.20%)**,
**2,100 different**, zero drift. Init 492/492 and Debugger 181/181 remain exact.
Conversions/byte percentages unchanged: this replaces an already-counted C
placeholder. Root README changes snapshot date and two aggregate rows only.
New authoritative ignored checkpoint:
`conker/build/game-attachment-copy-test/after.json`, with `audit.py` / `audit.json`.

```sh
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_attachment_copy_match tools.tests.test_game_attachment_progress_match tools.tests.test_game_matrix_parent_lookup_match tools.tests.test_game_matrix_pair_resolver_key_fit tools.tests.test_game_matrix_pair_resolver_recovery -v
make tools-check
```

## Next Work

Continue Game matching, not complete. Next local unrecovered body is node
action dispatcher `func_15031A50`; inspect callbacks, required reads and slot.
Its retail slot is 113 words / 452 bytes / frame `0x28`, with jump tables at
`80096F40` and `80096F7C`. Preserve existing Game-data table owners while
recovering byte selector `node+1`, guarded actor `+0x31C` state update,
actor `+0x9C` flag mutations and callback routes. V0 is not uniformly cleared:
default/flag paths retain the selector, call paths retain callback results.
Do not silently turn this body into a zero-return dispatcher.
Resolver `func_15031070` remains C84/frame `0x20`/40 differences, missing the
meaningful V0-to-A1 key move. Wrapper key/primary-read, basis private layout,
translator and sampler boundaries remain open. No sibling, frozen Release,
real-save, runtime/hardware or push action.
