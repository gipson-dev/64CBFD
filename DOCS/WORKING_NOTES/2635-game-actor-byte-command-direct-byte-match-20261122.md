# 2635 - Actor byte-command direct byte match

Date: 2026-11-22. The total 85% matching goal remains active.

`func_1506160C` in `conker/src/game_83300.c` replaces an empty void body
with its complete actor command/priority update. All **108 instructions emit
directly from C**, with **no frame, guards, inserted/omitted words or padding**.
The original symbol, five-argument interface and SDK actor structure are retained;
the four scalar parameters are recovered as `u8`.
Original: `conker/asm/nonmatchings/game_83300/func_1506160C.s`.
VA 1506160C..150617BC; ROM 8EABC..8EC6C; body/slot 432 bytes.

Production is **4,617 / 5,528 (83.52%) total**, **3,944 / 4,855 (81.24%) Game**,
with **zero address drift**, **911 different**, and **82 more matches** to 85%.
Init remains 492/492 and Debugger 181/181. Conversion rows are unchanged.
Only this function adds credit; the two repaired callers were already matched.

## Recovered behavior and layout

Commands below eight enforce priority against actor byte A. Commands 1, 2, 4,
5 and 6 update the original command bytes with distinct defaults; command 1
resets priority. A nonzero aggregate gate word mirrors actor byte 8 into 7.
High commands set/clear per-slot low flags, conditionally reset the selected
byte, and clear its high flag. Command 10 sets the high flag. Actor byte 2FD
or the selected global gate byte controls the final selected-byte write.

The real SDK `struct127` is 0x32C bytes; existing `pad2FC[1]` supplies byte
2FD, and `unkE.ub[1]` supplies byte F. `actor_commands.h` names the aligned
four-byte `ActorCommandGates` union with `word` and `bytes[4]` views for
`D_800DBFF4`; related byte-address aliases remain unchanged. Existing byte
consumers and the generated local target prototype use the corrected type.
The signed `value` local follows the command-to-slot register lifetime.
Keeping the low mask and using `mask << 4` as an expression avoids the
rejected extra frame/save introduced by assigning the shifted mask.

## Existing matched callers preserved

The unchanged packed caller `func_150721A4` now emits 19 raw words under the
byte prototype. Nine expected-word/relocation guards replace ten old rows;
two redundant copies are omitted instead of three. Its complete output stays
the original 17 words/frame 32. A symbolic interpreter proves all 2^32 packed
values, saved SP/RA and five outgoing arguments; a changed-shift control fails.
Both complete game_981E0 padded objects remain identical (328 functions).

`func_150771F0` uses a local `u8 command` for the existing ternary selection.
This restores 41 raw words/frame 32 without an extra byte mask. Three existing
guard preimages/expected relocations at 24/28/30 change; all nine replacement
words/relocations stay unchanged. Its complete game_A28B0 padded object stays
identical (211 functions). All other guard rows retain their exact bytes.
These are maintenance of existing matches, with no additional credit.

## Qualification evidence

- Fresh complete target-owner compilation with frozen old and proposed new
  headers preserves 88 raw neighboring functions, constant pools and diagnostics.
- Guest execution: 21,528 cases per raw/retail stream, all 256 command, priority,
  flag and guest-slot values, high-word narrowing and incoming o32 homes.
  107/108 instructions execute; duplicated comparison 95 remains unexecuted.
  Forty-six complete access-fault state pairs pass in five cases.
- Native SDK32 at O0/O2/O3: 3,864 cases each with strict aliasing, UBSan, full
  actor/gate canaries and ten effective source controls. High-command native
  slots are 0..3. Guest slots outside that domain, including slot 4 flag alias
  and MIPS masked shifts, are guest evidence only.
- Complete original/current 14-word forwarding caller: 4,096 cases per stream,
  frame 24, all byte arguments and correct five-argument ABI. Connected packed
  caller: 2,048 cases/layout. Complete selector caller: 2,560 cases/layout,
  all 41 words, all outer/selector bytes; alternate helper internals are
  contracted. Public memory/calls/saved ABI agree. Raw volatile-register/PC
  identity and selector fault-order identity are not claimed.
- Both padders match all three routines. Sixteen target and 24 caller GNU
  links pass across four HI16 carry boundaries. Eight malformed expected-word
  and relocation controls are rejected by both padders.
- Literal transitive includes identify 214 consumers among 698 active C
  owners; explicit Make prerequisites alone identify only 27. Private receipts
  cover 692 actual Make commands. After the selector-only repair, 167 exact
  prior owner receipts were reused and 47 owners rebuilt. All 214 receipts
  have frozen source/header/profile/tool/guard fingerprints and fresh structural
  audits in each tools configuration. Production forcibly rebuilt all 214
  owners before the ordinary ELF/progress build.
- Seven objects change discarded debug/extern metadata. Six independently
  rebuilt original-header baselines prove the unrelated declaration-size
  changes predate this proposal. Only the new gate extern size 0->4 belongs
  to this repair. Final linked absolute symbols remain unchanged; the existing
  linker discards `.mdebug`. Production checks retained sections, every named
  relocation and symbol record; only discarded physical debug paths may differ.
- The complete production ELF equals an independent prediction modifying
  only the 432 retail target bytes and target symbol size 24->432:
  **311 changed bytes, zero exclusions, no metadata permutations**.
  All 189,088 protected GameData bytes across 720 owners remain exact.
- Eight fresh focused checks pass in each tools configuration before and
  after adoption, plus shared `make tools-check`. The second configuration
  uses a disposable overlay; the real sibling's dirty state, HEAD and 353
  dependency hashes remain preserved. No push was performed.

Raw target SHA256:
`634bdc6aa824905d87a4429a8d66f26c5c5853fc63488d232d975412e505dbd6`.
Production ELF SHA256:
`5e93bd00f68063b2ac0ff0ca359f6097c1dd858c5e6f75a057a1234f8d8a9d56`.

Reusable command, from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_actor_byte_command_1506160c_match -v
```

Frozen private inputs and immutable qualified receipts are required by the
focused packet; the manifest fails closed on changed inputs. Fresh checks
are distinguished from reused recipe receipts. Task packet:
`conker/build/game-actor-byte-command-1506160c-private/`.

Codex owned implementation and validation. Claude calls attempted/completed:
0/0; local instruction, caller and compiler evidence resolved the ABI choices.
The host applicability check is read-only. No host/Release changes or gameplay/
hardware acceptance are claimed. After this checkpoint is committed and banked,
continue the next remaining Game routine using the newly frozen baseline.

Graph maintenance: the native update exited 1 with all
71,048 prior IDs retained. The subsequent serial scoped extraction
covers 19 C/Python files with no missing AST sources, producing
71,120 nodes / 169,840 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
The native scan triggered protection against replacing the larger existing
graph with a smaller corpus. The successful scoped merge supplies this update.
