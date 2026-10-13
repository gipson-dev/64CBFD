# Game Actor Callback Dispatch Direct Match And Frame Provenance - 2026-10-12

## Scope And Result

Resume the full Game matching goal from consumer `1e4cd63a` / tools `e5c3868`
and [Note 1321](1321-game-actor-callback-dispatch-semantic-recovery-and-frame-boundary-20261012.md).
Keep the same target until its remaining eight frame words are resolved.
The consumer was clean; tools had only the interrupted, untracked frame probe.
Preserve the independent older tools checkout and frozen host Release.

[func_150345E4](../../conker/src/game/generated_61490.c) now emits **all81 words
directly from semantic C**, original frame0x20, no guards, padding or profile
change. VA0x150345E4..0x15034728 / ROM0x61A94..0x61BD8,324 bytes.
Remove the named type/actor locals; use the indexed actor table expression and
signed32 switch selector. This retains all73 formerly exact words and fixes
exactly the eight frame/home instructions listed in Note1321.

No caller, helper declarations, shared headers, Makefile, layout, guard or
conversion-row changes. The already-qualified void(s32) caller stays fixed.
The repeated source expression is deliberate: restoring a named actor local
reintroduces the measured frame reservation. This is source-level fitting,
not a physical-register binding or compiler modification.

## Read-Only Compiler Evidence

Use the prepared compiler and existing GDB on a newly owned compiler driver.
No install, rebuild, account/model change or second advisory. The previous
target-specific advisory budget is exhausted; its switch-scratch explanation
was unproven and does not establish an unavoidable compiler defect.

New [frame trace](../../tools/experiments/game_actor_callback_frame_trace.py)
locks cc/cfe/uopt/ugen hashes, follows owned child execs, copies the actual CFE
and UOPT input files before their consumers run, and decodes them using the
existing descriptor-aware wire parser. Observe simulated memory read-only;
require completed driver/consumers and identical normal/traced object functions,
relocations, text and pools. Hashes remain:

| Compiler | SHA256 |
| --- | --- |
| cc | ca4b4385eb89c5098b665ffe256f59aa1bfd73ccd8f104fcb3eee0314dcd236a |
| cfe | f6122d3fafc6d9140013068cc762f8048b1bd349e94e8d0839d5bdef26842db9 |
| uopt | 23c108b975e88034af4ccbd89bd054a1ff3ee4ea9de28f25d91d75a7800f527d |
| ugen | fa9d94d28fc012ccaf231861a807387278f566ae70fd951c6c41443c135ea23d |

The interrupted f_spill_to_temp/f_temp_offset/f_free_temp probes never fired;
their zero-event route is rejected, not evidence of absent allocation. Add a
fired frame watch after f_readuinstr begins; no simulated-memory writes.
The prepared generated C's host-little-endian MEM_U32 and byte-address XOR3
define the observer's memory interpretation.

| Measurement | Previous Semantic Body | Direct Match |
| --- | ---: | ---: |
| CFE M definition | 12 | 4 |
| CFE anonymous switch VREG home | -12 | -4 |
| UOPT M definition | 16 | 8 |
| UOPT actor call-save home | -16 | -8 |
| UGEN saved reservation | 8 | 8 |
| UGEN local reservation | 16 | 8 |
| UGEN outgoing reservation | 16 | 16 |
| UGEN temporary increment | 0 | 0 |
| Final frame | 40 | 32 |

Observed frame writes:0->8->24->40 versus0->8->24->32. The order of local and
outgoing reservations differs; summands are identified from the compiler source
and captured M definitions, not inferred from frame-write order alone. Temporary
lists are empty at observed writes; no claim about every unobserved compiler path.
Two diagnostic labels originally swapped local/outgoing globals; the new body
made that test expectation fail. Correct the observer labels to local10019BA0 /
outgoing10019D4C; focused trace tests then pass. No compiler or production fix
was inferred from that fixture error.

Four unchanged-profile source screens: selected81/frame0x28/8 differences;
signed-byte switch81/0x28/12; inline-address switch81/0x20/0;
inline-address plus named type81/0x28/12. Only the complete direct body is accepted.
Ignoring the named type is not enough; captured upstream storage explains why.

## Qualification

```sh
python3 -m tools.experiments.game_actor_callback_frame_trace --screens
python3 -m unittest tools.tests.test_game_actor_callback_dispatch_match -v
make -C conker -j4 build/conker.us.elf progress.csv
```

New [match tests](../../tools/tests/test_game_actor_callback_dispatch_match.py)
reuse the existing target/native/pool/padder helpers without changing shared
oracle semantics. Historical Note1321 image tests retain their original snapshot;
the new suite owns an independent current baseline and whole-image gate.

All seven function tests pass before installation. The combined nine-test run
takes97.157 seconds with the one diagnostic-label expectation failure described
above. Both corrected trace tests pass in3.977 seconds. **All nine installed
tests pass in91.763 seconds**, no skips.

- 65,536 guest cases across all256 type bytes, full-word index extremes, mutable
  providers, ordered gates and two stack phases; add24 incoming-index/actor-home
  mutation cases and36 non-seven flag cases. All81 words execute.
- Compare literal complete RAM, private addresses, events, GPR/FPR state and
  visits between retail and candidate. No eight-byte affine normalization.
  The independent reference also checks public storage, helper arguments and
  incoming-home contents. Guest frame overwrites remain guest-only evidence.
- All130 own-access fault pairs fire across two stack phases; literal completed
  RAM/events/register prefixes match. The old0x28-frame control fails literal
  RAM/events as expected. Null-buffer minimal backing passes. Provider accesses
  remain excluded; no hardware PC/FCSR/full-gameplay claim.
- Native32 O2/O0 each passes32,768 cases with complete26-actor backing and ordered
  helper traces. Cached type, mutually-exclusive state dispatch, nonzero flag and
  disable-recheck negatives each fail observably. Helpers remain opaque providers.
- All nine target-owner neighbors and38 caller-owner functions/relative
  relocations/pools stay fixed. Full GLOBAL_ASM processing and both full-owner
  padders agree. Three independent code/data links match all81 original words,
  including HI/LO carry-sensitive addresses; no frame guards.
- Trace controls reject absent frame gates, incomplete child exit and corrupted
  optimizer input. Complete normal/traced objects and pools stay identical.

## Linked Audit And Banking

The build succeeds with the existing duplicate generated_12D630 recipe warning;
no new target diagnostic and no ROM build/replacement. The literal whole-image
gate allows only **eight target bytes**, the low byte of each Note1321 frame word.
Every other ELF byte is unchanged, including all symbol sizes and the caller.
Guards/progress.csv/layout/Makefile remain byte-identical; guard rows stay14,641.
All189,088 Game-data bytes /720 owners remain exact, SHA0bbc00e1.

| Artifact | SHA256 |
| --- | --- |
| Source | e14931f134e733634b3a8fd3b45a82719210058558e83d625a9a717bcff6c3d8 |
| ELF | 1bb360141434d070e78d90085197c2fbdb914986026f9a718a0ccb23e330b024 |
| Caller | d15e8947326b0be2765599152782bb2227102c640630a034774d76bf543c9699 |
| Guards | 8bd422a0acd766c6dbd4e3cbaedf01c22e43cee418079facdf566eca08151cc4 |

Fresh matching: Game2,821/4,823 (58.49%), total3,494/5,496 (63.57%), drift0,
different2,002; +1 matching, converted functions/bytes unchanged. Root README
changes aggregate rows only. Check off the old frame task without closing Game.

After the independent eight-byte image proof, archive the prior text manifest/ELF
under this target's ignored test folder and advance only the text ELF fingerprint.
All eight other protected inputs stay fixed; fresh text integrity/corruption
tests05/06 pass in1.466 seconds. Reuse broader unchanged Note1321/1320 receipts
explicitly, not as freshly rerun suites. A mistyped test06 selector is corrected;
it is not a production defect or a passing test.

Bank mounted tools `80e6fed` first, then the consumer's source/docs/exact gitlink.
Consumer/mounted/older tools checks, both Windows syntax checks and whitespace
checks pass. Older HEADddbdd16b and116 unrelated saved hashes stay fixed; copy
only two absent task files and the verified shared text pin. Dirty394->396 /
fingerprints117->119, no older commit/reset/stash. Keep the active checkouts clean;
verify relative links, post-bank integrity and fresh terminal Graphify Rebuilt with
zero workers. Preserve existing graph version/scan/HTML-limit warnings.
No push, host/Release/save/config/editor change or additional Claude call.

## Next

The eight-word func_150345E4 task is finished. Continue the full Game goal with
func_150341BC in the same owner: VA0x150341BC..0x15034340, ROM0x6166C..0x617F0,
97 words/frame0, currently94 linked word differences behind its zero-return
placeholder. Focused graph and complete original inspected; its direct original
caller is func_15033FE0. Recover the output cursor/slot ABI, attached-record/type
gates, signed scaled halfword commands, byte1D1 command and live global selected
actor lookups before any installation. No new candidate or qualification yet.
Keep text218/114/cut27, translator49/34 and wider Game/runtime gates open.
