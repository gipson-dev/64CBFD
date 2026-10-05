# Game Actor Update Dispatcher And Carried Slot ABI

Follow-up: [Note 1007](1007-game-actor-update-pass-semantic-recovery-and-captured-order-20261005.md)
now recovers the caller semantically and connects this actual dispatcher.
The caller-placeholder preservation statements below describe this historical
checkpoint; the dispatcher itself remains direct and byte-exact.

Date: 2026-10-05. Starting HEAD: `316a3287`, the actor display-list scan in
[Note 1005](1005-game-actor-display-list-scan-match-and-live-callback-state-20261005.md).

## Recovery

`func_1502BD84` in `conker/src/game/generated_58F80.c` replaces its false
zero-return placeholder with the original per-actor update dispatcher:

```c
void func_1502BD84(ActorUpdate58F80 *actor, s32 slot);
```

All **88 words / 352 bytes**, ROM **0x59234**, address
**0x1502BD84..0x1502BEE4**, and the **0x20-byte frame** emit directly from
default IDO 5.3 O2/g3. There are **no new guards or compiler-profile overrides**.
Complete slot SHA-256:
`0ce9ed73235a6dfd192422f224efe6d78bcb0b07a8cd2eb9bccb942370a9d9b6`.

The scoped actor view covers active +0, id +4, state +5, signal +0xA4,
flags +0xF8, event bytes +0x134/+0x135, prepare +0x1C9, work +0x1D4,
status +0x1FC and optional word +0x260, retaining stride 0x32C.

## Ordered Behavior

1. Read state, then clear work even on an early exit. State 5 invokes
   `func_1502DF38(slot, 1)` before the ordinary id-255/state-3 exclusions.
2. State 2 takes the dedicated `func_1502C608(slot)` path and exits.
3. Other admitted actors optionally invoke `func_1502FBE8(actor)`, then
   `func_1502E4C4(slot)`, `func_1502DF38(slot, 0)` and `func_1503A08C(actor)`.
4. Reread work after those calls. Zero stores status 2; any nonzero word
   invokes `func_150345E4(slot)` and `func_1503A830(actor)` in that order.
5. Read `D_800C666F[slot * 16]`; a nonzero byte invokes `func_1503DF48(slot)`.
6. Reread activity after the callback. Active actors invoke
   `func_1502EEF4(slot)` and `func_1502F264(slot)`, then optional signal,
   flags-bit-14 and event-byte callbacks. Each later field is read after
   preceding calls. Do not recheck the initial id/state gates or activity
   between these later callbacks.

The original input slot home is retained at entry SP+4. Slot validation,
null fallbacks and new gameplay rules are not introduced.

## ABI Discovery And Matching

The first unadopted candidate treated `func_1502EEF4` as a zero-argument
callback because the call site has no adjacent argument move. That candidate
emitted **87 words / frame 0x20 / 42 differences**. A shifted-bit control
reached 88 words with 27 differences, without recovering the missing contract.

Review of the actual callee proves it consumes `$a0`: at **0x1502EEFC** it
copies a0 to s2, then computes `D_800CC2D0 + slot * 0x32C`. The original
caller loads a0 from its slot home before testing activity, carrying that
value into the call with a nop delay slot. Adding the missing **slot argument**
to semantic C resolves all scheduling/register differences directly.

This was also a test-boundary correction: the exploratory fixture originally
ignored that argument and could not detect its absence. The final fixture
records/validates it. An explicit omitted-slot negative control demonstrates
the wrong argument after a clobbering metadata callback. The actual callee
prefix provides an independent ABI witness; no faulty exploratory source
or zero-argument contract was adopted in production.

The driver `tools/experiments/game_actor_update_dispatch_candidates.py`
contains **26 reproducible forms**, including explicitly named negative controls.

| Candidate | Body Words | Frame | Different Words |
| --- | ---: | ---: | ---: |
| Existing placeholder | 3 | 0 | 83 |
| Wrong omitted-slot control | 87 | 0x20 | 42 |
| Correct baseline | 88 | 0x20 | 0 |
| Byte-state local | 88 | 0x20 | 4 |
| Word-state / alternate index / structured table forms | 88 | 0x20 | 0 |
| Shifted flag control with corrected slot call | 89 | 0x20 | 23 |
| Wrong work-one comparison | 89 | 0x20 | 54 |

The production definition equals the selected baseline. Existing downstream
placeholder bodies and the caller placeholder remain unchanged; old-style
declarations preserve their current definition shapes while supplied call
arguments are verified against the recovered contracts.

## Qualification

`tools/tests/test_game_actor_update_dispatch_match.py` passes **9 tests in
7.781 seconds, no skips** against the final rebuilt ELF:

- **5194 full dispatcher cases**, each comparing retail, direct C and the
  equivalent nonmatching shifted-flag control. The independent 5184-case
  gate/work matrix covers signal alternatives, id/state/prepare/activity,
  flags, optional work, metadata and signed work words. Additional cases
  exercise live callback mutations and slot-home phases/indices.
- **49152 native C cases** cover every state byte and callback ordering,
  plus two native mutation cases. Actor size/field offsets, slot arguments,
  event bytes, status stores and table fences are checked with 32-bit pointers.
- **48 actual `func_1502EEF4` prefixes** compare retail and recovered callers
  through the first 21 callee words. They verify the carried slot, computed
  actor pointer and nested stack frame, stopping before its actor loop.
- Missing-slot and wrong-work negative controls produce observable argument,
  callback or status differences. The missing-slot control sees `0xA5000004`
  instead of slot zero after the mock callback clobbers volatile registers.
- All **87 reachable dispatcher words** execute. One retained duplicate
  prepare-byte load at **0x1502BDEC** is skipped by the branch/delay-slot paths.
  It is included in the byte-exact 88-word slot.
- Selected C agrees with retail through ordered memory accesses, callback
  arguments, work/status writes and saved-register lifetime. The shifted
  control is compared at the external-memory/call boundary; its different
  private stack reload schedule is not claimed byte-exact.
- Original caller `func_1502BEE4` retains its full **176-word** placeholder
  slot/hash. The original ASM calls the dispatcher twice, but the current C
  caller is not restored or qualified as a connected full actor pipeline.

Most update callbacks remain opaque fixtures. Actual-prefix qualification
stops before the downstream loop; it is not full-callee, animation, gameplay,
hardware rendering or PC runtime acceptance. Negative slot tests are bounded
guest-instruction checks with mapped metadata, not supported native gameplay.

## Measured Progress

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3302 / 5463 (60.44%) | 0 | 2161 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2629 / 4790 (54.89%) | 0 | 2161 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The owner rebuild succeeds. A pre-edit address/length/SHA-256 snapshot of all
**6060 slots** confirms that only `func_1502BD84` changes relative to the
banked scan checkpoint. No added/deleted slots; the previous scan stays exact.
Full Init code **164048 bytes**, Init data/rodata **17376 bytes**, Debugger
**19800 bytes**, Game data **189088 bytes / 720 owners** remain retail-exact.
Conversion totals and **47 retained Init ASM functions** remain unchanged.

The **10606-row** patch table is unchanged, has no duplicate keys and retains
SHA-256 `22f784b5c5dc38114c6d2ed9da81fb74ea9ac3eb5c97c4a3be57d129d1fa4099`.
`make tools-check` passes. README changes are aggregate counts only.

The complete actor/viewport/SDK/resource/matching/tool regression passes
**311 tests in 257.161 seconds, no skips**, against the final rebuilt ELF.
`git diff --check` and all **2923 relative links** in the touched status,
roadmap, README and working-note documents pass. Existing unrelated recipe
warnings remain; the isolated direct candidate emits no diagnostics.

## Reproduction And Next

Run from the `64CBFD` root in PowerShell:

```powershell
wsl python3 -m tools.experiments.game_actor_update_dispatch_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_actor_update_dispatch_match -q -f
wsl make tools-check
git diff --check
```

For the combined regression prepend `tools.tests.test_game_actor_update_dispatch_match`
to [Note 1005's combined actor/viewport/resource/tool modules](1005-game-actor-display-list-scan-match-and-live-callback-state-20261005.md).
No sibling source, build, save or frozen Release change is made.

Next bounded target: **`func_1502BEE4`**, **176-word slot / frame 0x88**,
ROM **0x59394**, the caller in the same owner. Recover its full table traversal,
per-actor update ordering, local status storage and callback contracts before
claiming a connected actor-update pipeline. Audit callees that consume carried
argument registers even when no adjacent move appears at a call site.
